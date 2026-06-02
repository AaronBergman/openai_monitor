#!/usr/bin/env python3
"""
Daily monitoring run script for openai.com sitemap changes.
Run ID: passed as env var or computed at start.
"""

import os, sys, json, subprocess, shutil, re, difflib
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

try:
    import httpx
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "httpx", "--quiet"])
    import httpx

RUN_ID = os.environ.get("RUN_ID", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ"))
REPO_ROOT = Path(__file__).parent
FETCH_TIME = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

print(f"=== Run ID: {RUN_ID} ===")
print(f"Fetch time: {FETCH_TIME}")

# ---------- helpers ----------

def fetch_xml(url: str) -> str:
    """Fetch XML with plain httpx (fine for sitemaps)."""
    resp = httpx.get(url, timeout=30, follow_redirects=True,
                     headers={"User-Agent": "Mozilla/5.0 SitemapMonitor/1.0"})
    resp.raise_for_status()
    return resp.text

def url_to_path(url: str) -> str:
    """Shell out to tools/url_path.py for canonical path."""
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "url_path.py"), url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()

def fetch_page(url: str, out_path: Path) -> bool:
    """Fetch page via html_to_md.py. Returns True on success."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "html_to_md.py"),
         "--url", url, "--output", str(out_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    if result.returncode != 0:
        return False
    if out_path.exists():
        content = out_path.read_text(errors="replace")
        if len(content) < 100 or "Enable JavaScript" in content:
            return False
    else:
        return False
    return True

def sanitize_name(url: str) -> str:
    """Convert sub-sitemap URL to a filesystem-safe name."""
    # e.g. https://openai.com/sitemap.xml/api/ -> _openai.com_sitemap.xml_api.xml
    url = url.rstrip("/")
    path_part = url.replace("https://", "").replace("http://", "")
    path_part = path_part.replace("/", "_")
    if not path_part.endswith(".xml"):
        path_part += ".xml"
    return path_part

def parse_sitemap_urls(xml_text: str) -> dict:
    """Parse flat sitemap; return {url: lastmod_or_None}."""
    urls = {}
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return urls
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for url_el in root.findall(".//sm:url", ns):
        loc = url_el.findtext("sm:loc", namespaces=ns)
        lastmod = url_el.findtext("sm:lastmod", namespaces=ns)
        if loc:
            urls[loc.strip()] = (lastmod or "").strip()
    return urls

def parse_sitemap_index(xml_text: str) -> list:
    """Parse sitemap index; return list of sub-sitemap URLs."""
    locs = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return locs
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for sitemap_el in root.findall(".//sm:sitemap", ns):
        loc = sitemap_el.findtext("sm:loc", namespaces=ns)
        if loc:
            locs.append(loc.strip())
    return locs

# ---------- STEP 1: BASELINE ----------

print("\n--- Step 1: Loading baseline ---")

def load_baseline() -> dict:
    """Load baseline URLs from latest sub-sitemaps."""
    baseline = {}
    sub_latest = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / "latest"
    if not sub_latest.exists():
        return baseline
    for xml_file in sub_latest.glob("*.xml"):
        try:
            text = xml_file.read_text()
            urls = parse_sitemap_urls(text)
            baseline.update(urls)
        except Exception as e:
            print(f"  Warning: could not parse {xml_file}: {e}")
    print(f"  Baseline: {len(baseline)} URLs from {len(list(sub_latest.glob('*.xml')))} sub-sitemaps")
    return baseline

baseline_urls = load_baseline()

# ---------- STEP 2: FETCH + SNAPSHOT ----------

print("\n--- Step 2: Fetching sitemaps ---")

INDEX_URL = "https://openai.com/sitemap.xml"

try:
    index_xml = fetch_xml(INDEX_URL)
    print(f"  Fetched index: {len(index_xml)} bytes")
except Exception as e:
    print(f"  FATAL: Could not fetch sitemap index: {e}")
    sys.exit(1)

# Save root index
sitemap_dir = REPO_ROOT / "sitemaps" / "openai.com"
sitemap_dir.mkdir(parents=True, exist_ok=True)
(sitemap_dir / f"{RUN_ID}.xml").write_text(index_xml)
(sitemap_dir / "latest.xml").write_text(index_xml)
print(f"  Saved root index to sitemaps/openai.com/{RUN_ID}.xml")

# Parse sub-sitemap URLs
sub_sitemap_urls = parse_sitemap_index(index_xml)
print(f"  Found {len(sub_sitemap_urls)} sub-sitemaps")

# Create sub dirs
sub_run_dir = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / RUN_ID
sub_latest_dir = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / "latest"
sub_run_dir.mkdir(parents=True, exist_ok=True)
sub_latest_dir.mkdir(parents=True, exist_ok=True)

# Fetch all sub-sitemaps
current_urls = {}  # url -> lastmod
sub_sitemap_data = {}  # name -> xml_text
fetch_failures_sitemaps = []

for sub_url in sub_sitemap_urls:
    name = sanitize_name(sub_url)
    try:
        xml_text = fetch_xml(sub_url)
        urls = parse_sitemap_urls(xml_text)
        current_urls.update(urls)
        sub_sitemap_data[name] = xml_text
        # Save
        (sub_run_dir / name).write_text(xml_text)
        (sub_latest_dir / name).write_text(xml_text)
        print(f"  [{name[:50]}]: {len(urls)} URLs")
    except Exception as e:
        print(f"  ERROR fetching {sub_url}: {e}")
        fetch_failures_sitemaps.append({"url": sub_url, "error": str(e)})

print(f"\n  Total current URLs: {len(current_urls)}")

# ---------- STEP 3: DIFF ----------

print("\n--- Step 3: Computing diff ---")

added_urls = [u for u in current_urls if u not in baseline_urls]
removed_urls = [u for u in baseline_urls if u not in current_urls]
updated_urls = [
    {"url": u, "old_lastmod": baseline_urls[u], "new_lastmod": current_urls[u]}
    for u in current_urls
    if u in baseline_urls and current_urls[u] != baseline_urls[u]
]

print(f"  Added:   {len(added_urls)}")
print(f"  Removed: {len(removed_urls)}")
print(f"  Updated: {len(updated_urls)}")

# ---------- STEP 4: ANOMALY DETECTION ----------

print("\n--- Step 4: Anomaly detection ---")

anomalies = []
fetch_time_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

# Load known_urls.json for extra context
known_urls_path = REPO_ROOT / "state" / "known_urls.json"
try:
    known_urls = json.loads(known_urls_path.read_text())
except:
    known_urls = {}

for url in current_urls:
    lm = current_urls[url]
    if not lm:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm + "T00:00:00+00:00" if len(lm) == 10 else lm.replace("Z", "+00:00"))
    except:
        continue

    # Future lastmod
    if lm_dt > fetch_time_dt:
        anomalies.append({"kind": "future_lastmod", "url": url,
                          "details": f"lastmod {lm} is after fetch time {FETCH_TIME}"})

    # Lastmod moved backwards
    if url in baseline_urls and baseline_urls[url] and lm:
        try:
            old_dt = datetime.fromisoformat(baseline_urls[url] + "T00:00:00+00:00" if len(baseline_urls[url]) == 10
                                            else baseline_urls[url].replace("Z", "+00:00"))
            if lm_dt < old_dt:
                anomalies.append({"kind": "lastmod_backwards", "url": url,
                                  "details": f"lastmod moved from {baseline_urls[url]} to {lm}"})
        except:
            pass

# New URL whose lastmod predates first_seen by more than a few days
for url in added_urls:
    lm = current_urls.get(url, "")
    if not lm:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm + "T00:00:00+00:00" if len(lm) == 10 else lm.replace("Z", "+00:00"))
        first_seen_dt = datetime.fromisoformat(RUN_ID[:10] + "T00:00:00+00:00")
        days_diff = (first_seen_dt - lm_dt).days
        if days_diff > 7:
            anomalies.append({"kind": "backdated_new_url", "url": url,
                              "details": f"new URL with lastmod {lm} predates first_seen by {days_diff} days"})
    except:
        pass

# Disappeared and reappeared
for url in added_urls:
    if url in known_urls and known_urls[url].get("last_seen"):
        last_seen = known_urls[url]["last_seen"]
        if last_seen < RUN_ID[:10]:
            # Check if there was a gap
            anomalies.append({"kind": "reappeared_url", "url": url,
                              "details": f"URL last seen {last_seen}, now reappearing in {RUN_ID}"})

print(f"  Anomalies found: {len(anomalies)}")
for a in anomalies[:5]:
    print(f"    [{a['kind']}] {a['url'][:70]}")

# ---------- STEP 5: FETCH + CONVERT CHANGED PAGES ----------

print("\n--- Step 5: Fetching changed/new pages ---")

pages_to_fetch = []
for url in added_urls:
    rel_path = url_to_path(url)
    if rel_path:
        pages_to_fetch.append((url, REPO_ROOT / rel_path, "added"))

for item in updated_urls:
    url = item["url"]
    rel_path = url_to_path(url)
    if rel_path:
        pages_to_fetch.append((url, REPO_ROOT / rel_path, "updated"))

print(f"  Pages to fetch: {len(pages_to_fetch)}")

fetch_failures_pages = []
page_prev_content = {}  # url -> prior markdown text

# Capture prior content for updated pages
for url, md_path, kind in pages_to_fetch:
    if kind == "updated" and md_path.exists():
        page_prev_content[url] = md_path.read_text(errors="replace")

# Fetch in batches of 10 with subprocess concurrency
import concurrent.futures

def fetch_one(args):
    url, md_path, kind = args
    try:
        ok = fetch_page(url, md_path)
        return (url, md_path, kind, ok, None)
    except Exception as e:
        return (url, md_path, kind, False, str(e))

fetch_results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_one, args): args for args in pages_to_fetch}
    done_count = 0
    for future in concurrent.futures.as_completed(futures):
        url, md_path, kind, ok, err = future.result()
        fetch_results.append((url, md_path, kind, ok, err))
        done_count += 1
        if done_count % 20 == 0 or done_count == len(pages_to_fetch):
            print(f"  Progress: {done_count}/{len(pages_to_fetch)}")
        if not ok:
            fetch_failures_pages.append({
                "url": url,
                "error": err or "content too short or blocked"
            })
            # Restore prior content if we overwrote
            if url in page_prev_content and md_path.exists():
                md_path.write_text(page_prev_content[url])

successful_fetches = [(url, md_path, kind) for url, md_path, kind, ok, err in fetch_results if ok]
print(f"  Successful: {len(successful_fetches)}, Failures: {len(fetch_failures_pages)}")

# ---------- STEP 6: ANALYZE CHANGES ----------

print("\n--- Step 6: Analyzing changes ---")

page_analyses = []  # list of dicts with url, kind, summary

def brief_diff(old_text: str, new_text: str) -> str:
    """Return a brief description of what changed between two markdown texts."""
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()

    # Count line changes
    added_lines = []
    removed_lines = []
    for line in difflib.unified_diff(old_lines, new_lines, lineterm=""):
        if line.startswith("+") and not line.startswith("+++"):
            added_lines.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed_lines.append(line[1:].strip())

    # Filter trivial whitespace/empty changes
    added_lines = [l for l in added_lines if l]
    removed_lines = [l for l in removed_lines if l]

    if not added_lines and not removed_lines:
        return "No substantive changes detected (whitespace/formatting only)"

    summary_parts = []
    if removed_lines:
        sample = "; ".join(removed_lines[:3])
        summary_parts.append(f"Removed: {sample[:200]}")
    if added_lines:
        sample = "; ".join(added_lines[:3])
        summary_parts.append(f"Added: {sample[:200]}")

    return " | ".join(summary_parts) + f" ({len(added_lines)} lines added, {len(removed_lines)} removed)"

for url, md_path, kind in successful_fetches:
    analysis = {"url": url, "kind": kind, "path": str(md_path.relative_to(REPO_ROOT))}

    if kind == "updated" and url in page_prev_content:
        new_content = md_path.read_text(errors="replace") if md_path.exists() else ""
        diff_summary = brief_diff(page_prev_content[url], new_content)
        analysis["diff_summary"] = diff_summary
    elif kind == "added":
        content = md_path.read_text(errors="replace") if md_path.exists() else ""
        # Extract title/first heading
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        title = next((l.lstrip("#").strip() for l in lines if l.startswith("#")), "")
        # Brief content summary (first 300 chars of non-heading content)
        body_lines = [l for l in lines if not l.startswith("#")]
        body_preview = " ".join(body_lines)[:300]
        analysis["title"] = title
        analysis["preview"] = body_preview

    page_analyses.append(analysis)

# ---------- STEP 7: WRITE analysis.md ----------

print("\n--- Step 7: Writing analysis ---")

run_dir = REPO_ROOT / "runs" / RUN_ID
run_dir.mkdir(parents=True, exist_ok=True)

analysis_lines = [
    f"# Analysis: {RUN_ID}",
    f"",
    f"**Fetch time (UTC):** {FETCH_TIME}",
    f"**Total current URLs:** {len(current_urls)}",
    f"**Baseline URLs:** {len(baseline_urls)}",
    f"",
    f"## Summary",
    f"",
    f"| Category | Count |",
    f"|----------|-------|",
    f"| Added    | {len(added_urls)} |",
    f"| Removed  | {len(removed_urls)} |",
    f"| Updated  | {len(updated_urls)} |",
    f"| Anomalies| {len(anomalies)} |",
    f"| Fetch failures (pages) | {len(fetch_failures_pages)} |",
    f"",
]

if anomalies:
    analysis_lines += ["## Anomalies (High Signal)", ""]
    for a in anomalies:
        analysis_lines.append(f"- **{a['kind']}**: `{a['url']}`")
        analysis_lines.append(f"  - {a['details']}")
    analysis_lines.append("")
else:
    analysis_lines += ["## Anomalies", "", "None detected.", ""]

# New pages
added_analyses = [p for p in page_analyses if p["kind"] == "added"]
if added_urls:
    analysis_lines += [f"## New Pages ({len(added_urls)} total)", ""]
    for url in added_urls:
        a = next((p for p in added_analyses if p["url"] == url), None)
        analysis_lines.append(f"### `{url}`")
        if a:
            if a.get("title"):
                analysis_lines.append(f"**Title:** {a['title']}")
            if a.get("preview"):
                analysis_lines.append(f"**Preview:** {a['preview'][:300]}")
        else:
            analysis_lines.append("*(fetch failed or not attempted)*")
        analysis_lines.append("")

# Updated pages
updated_analyses = [p for p in page_analyses if p["kind"] == "updated"]
# Sort by significance (ones with actual diff summaries first)
significant_updates = [p for p in updated_analyses if p.get("diff_summary") and
                       "No substantive" not in p.get("diff_summary", "")]
routine_updates = [p for p in updated_analyses if not p.get("diff_summary") or
                   "No substantive" in p.get("diff_summary", "")]

if significant_updates:
    analysis_lines += [f"## Significant Updates ({len(significant_updates)})", ""]
    for p in significant_updates[:30]:
        analysis_lines.append(f"### `{p['url']}`")
        analysis_lines.append(f"- {p['diff_summary']}")
        analysis_lines.append("")

# Routine updates (just list)
if routine_updates:
    analysis_lines += [f"## Routine Updates ({len(routine_updates)} pages — lastmod changed, content unchanged or not fetched)", ""]
    for p in routine_updates[:50]:
        analysis_lines.append(f"- `{p['url']}`")
    if len(routine_updates) > 50:
        analysis_lines.append(f"- ... and {len(routine_updates) - 50} more")
    analysis_lines.append("")

# Also list updated URLs that weren't fetched (only lastmod changed, no page fetch attempted)
unfetched_updated = [item for item in updated_urls
                     if not any(p["url"] == item["url"] for p in updated_analyses)]
if unfetched_updated:
    analysis_lines += [f"## Updated URLs (lastmod changed, content not re-fetched as per limit): {len(unfetched_updated)}", ""]
    # Group by pattern
    for item in unfetched_updated[:30]:
        analysis_lines.append(f"- `{item['url']}` ({item['old_lastmod']} → {item['new_lastmod']})")
    if len(unfetched_updated) > 30:
        analysis_lines.append(f"- ... and {len(unfetched_updated)-30} more")
    analysis_lines.append("")

# Removed pages
if removed_urls:
    analysis_lines += [f"## Removed Pages ({len(removed_urls)})", ""]
    for url in removed_urls:
        analysis_lines.append(f"- `{url}`")
    analysis_lines.append("")

# Fetch failures
if fetch_failures_pages:
    analysis_lines += [f"## Fetch Failures — Needs Follow-up ({len(fetch_failures_pages)})", ""]
    for f in fetch_failures_pages[:20]:
        analysis_lines.append(f"- `{f['url']}`: {f.get('error','unknown')}")
    analysis_lines.append("")

(run_dir / "analysis.md").write_text("\n".join(analysis_lines))
print(f"  Written runs/{RUN_ID}/analysis.md")

# ---------- STEP 8: UPDATE README.md ----------

print("\n--- Step 8: Updating README.md ---")

readme_path = REPO_ROOT / "README.md"
existing_readme = readme_path.read_text() if readme_path.exists() else ""

# Build new section
def make_tldr():
    parts = []
    if added_urls:
        parts.append(f"{len(added_urls)} new page{'s' if len(added_urls)!=1 else ''}")
    if removed_urls:
        parts.append(f"{len(removed_urls)} removal{'s' if len(removed_urls)!=1 else ''}")
    if updated_urls:
        parts.append(f"{len(updated_urls)} lastmod update{'s' if len(updated_urls)!=1 else ''}")
    if anomalies:
        parts.append(f"{len(anomalies)} anomal{'ies' if len(anomalies)!=1 else 'y'}")
    if not parts:
        return "No changes detected — sitemap identical to prior baseline."
    return f"Detected {', '.join(parts)} vs the prior run."

tldr = make_tldr()

# Summarize significant new/updated pages for README
readme_new_section = [
    f"## {RUN_ID[:10]} — Run {RUN_ID}",
    "",
    f"**TL;DR:** {tldr}",
    f"Stats: {len(current_urls)} total URLs, +{len(added_urls)} added, ~{len(updated_urls)} updated lastmod, -{len(removed_urls)} removed, {len(anomalies)} anomalies, {len(sub_sitemap_urls)} sub-sitemaps.",
    "",
]

if anomalies:
    readme_new_section += ["### ⚠ Anomalies", ""]
    for a in anomalies[:10]:
        readme_new_section.append(f"- **{a['kind']}** — `{a['url'][:80]}`: {a['details']}")
    readme_new_section.append("")

if added_urls:
    readme_new_section += [f"### New Pages ({len(added_urls)})", ""]
    for url in added_urls[:20]:
        a = next((p for p in added_analyses if p["url"] == url), None)
        rel_path = url_to_path(url)
        link = f"[`{url.replace('https://openai.com','')}`]({rel_path})" if rel_path else f"`{url}`"
        if a and a.get("title"):
            readme_new_section.append(f"- {link} — {a['title'][:100]}")
        else:
            readme_new_section.append(f"- {link}")
    if len(added_urls) > 20:
        readme_new_section.append(f"- ... and {len(added_urls)-20} more (see [analysis](runs/{RUN_ID}/analysis.md))")
    readme_new_section.append("")

if significant_updates:
    readme_new_section += [f"### Notable Updates ({len(significant_updates)})", ""]
    for p in significant_updates[:10]:
        url = p["url"]
        rel_path = url_to_path(url)
        link = f"[`{url.replace('https://openai.com','')}`]({rel_path})" if rel_path else f"`{url}`"
        diff_summary = p.get("diff_summary","")[:200]
        readme_new_section.append(f"- {link}: {diff_summary}")
    if len(significant_updates) > 10:
        readme_new_section.append(f"- ... and {len(significant_updates)-10} more significant updates")
    readme_new_section.append("")

if updated_urls and not significant_updates:
    readme_new_section += [f"### Updated (lastmod changed, {len(updated_urls)} pages)", ""]
    # Just note the count and refer to analysis
    readme_new_section.append(f"All {len(updated_urls)} updated pages had lastmod changes but no detected content differences. See [analysis](runs/{RUN_ID}/analysis.md) for full list.")
    readme_new_section.append("")

if removed_urls:
    readme_new_section += [f"### Removed ({len(removed_urls)})", ""]
    for url in removed_urls[:10]:
        readme_new_section.append(f"- `{url}`")
    readme_new_section.append("")

if fetch_failures_pages:
    readme_new_section += [f"### Fetch Failures ({len(fetch_failures_pages)} pages)", ""]
    readme_new_section.append(f"Cloudflare blocked {len(fetch_failures_pages)} page fetch(es); prior snapshots preserved. See [analysis](runs/{RUN_ID}/analysis.md).")
    readme_new_section.append("")

readme_new_section.append("---")
readme_new_section.append("")

new_section_text = "\n".join(readme_new_section)

# Prepend to existing README, after main title if present
if existing_readme.startswith("# "):
    # Find end of title line
    first_newline = existing_readme.find("\n")
    title_part = existing_readme[:first_newline+1]
    rest = existing_readme[first_newline+1:].lstrip("\n")
    new_readme = title_part + "\n" + new_section_text + "\n" + rest
else:
    new_readme = new_section_text + "\n" + existing_readme

readme_path.write_text(new_readme)
print(f"  Updated README.md")

# ---------- STEP 9: UPDATE state/known_urls.json ----------

print("\n--- Step 9: Updating state/known_urls.json ---")

today = RUN_ID[:10]

for url, lastmod in current_urls.items():
    if url not in known_urls:
        known_urls[url] = {
            "first_seen": RUN_ID,
            "last_seen": today,
            "current_lastmod": lastmod,
            "lastmod_history": [{"run": RUN_ID, "lastmod": lastmod}] if lastmod else []
        }
    else:
        entry = known_urls[url]
        entry["last_seen"] = today
        if lastmod and lastmod != entry.get("current_lastmod"):
            history = entry.get("lastmod_history", [])
            history.append({"run": RUN_ID, "lastmod": lastmod})
            entry["lastmod_history"] = history
            entry["current_lastmod"] = lastmod

# Don't remove entries for removed URLs; just don't update last_seen

known_urls_path.parent.mkdir(parents=True, exist_ok=True)
known_urls_path.write_text(json.dumps(known_urls, indent=2, sort_keys=True))
print(f"  Updated state/known_urls.json: {len(known_urls)} entries")

# ---------- STEP 10: WRITE diff.json ----------

print("\n--- Step 10: Writing diff.json ---")

# Determine prior run baseline
prior_run_ids = sorted([
    d.name for d in (REPO_ROOT / "runs").iterdir()
    if d.is_dir() and d.name != RUN_ID
])
prior_run_id = prior_run_ids[-1] if prior_run_ids else None

diff_data = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME,
    "baseline": prior_run_id,
    "added": added_urls,
    "removed": removed_urls,
    "updated": updated_urls,
    "anomalies": anomalies,
    "fetch_failures": fetch_failures_pages + fetch_failures_sitemaps
}

(run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2))
print(f"  Written runs/{RUN_ID}/diff.json")

print(f"\n=== Run {RUN_ID} complete ===")
print(f"  Added: {len(added_urls)}, Updated: {len(updated_urls)}, Removed: {len(removed_urls)}, Anomalies: {len(anomalies)}")
print(f"  Fetch failures (pages): {len(fetch_failures_pages)}")
