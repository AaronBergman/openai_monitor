#!/usr/bin/env python3
"""
Daily monitoring run for openai.com sitemap changes.
Run ID: computed at start.
"""

import os
import sys
import json
import subprocess
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

os.environ["TZ"] = "UTC"

# ── Config ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent
RUN_ID = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ")
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"
PAGES_DIR = REPO_ROOT / "pages"
SITEMAPS_DIR = REPO_ROOT / "sitemaps" / "openai.com"
SUB_LATEST_DIR = SITEMAPS_DIR / "sub" / "latest"
STATE_FILE = REPO_ROOT / "state" / "known_urls.json"

FETCH_TIME = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
print(f"Run ID: {RUN_ID}")
print(f"Fetch time: {FETCH_TIME}")

# ── Helpers ───────────────────────────────────────────────────────────────────
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def fetch_xml(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SitemapBot/1.0)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")

def parse_sitemap_locs(xml_text: str) -> list[dict]:
    """Parse <url><loc> and <url><lastmod> from a sitemap."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"  XML parse error: {e}")
        return []
    urls = []
    for url_el in root.findall("sm:url", NS):
        loc = url_el.findtext("sm:loc", namespaces=NS) or ""
        lastmod = url_el.findtext("sm:lastmod", namespaces=NS) or ""
        if loc:
            urls.append({"url": loc.strip(), "lastmod": lastmod.strip()})
    return urls

def parse_sitemap_index_locs(xml_text: str) -> list[str]:
    """Parse <sitemap><loc> from a sitemap index."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    locs = []
    for sm in root.findall("sm:sitemap", NS):
        loc = sm.findtext("sm:loc", namespaces=NS) or ""
        if loc:
            locs.append(loc.strip())
    return locs

def url_to_path(url: str) -> Path:
    result = subprocess.run(
        ["python3", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return REPO_ROOT / result.stdout.strip()

def sanitize_name(url: str) -> str:
    """Convert a sub-sitemap URL to a safe filename."""
    name = url.replace("https://openai.com/sitemap.xml/", "sitemap.xml_")
    name = name.replace("https://openai.com/", "").replace("/", "_")
    name = name.replace("?", "_").replace("&", "_")
    if not name.endswith(".xml"):
        name += ".xml"
    return name

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Build baseline from latest sub-sitemaps
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 1: Building baseline ===")
baseline: dict[str, str] = {}  # url -> lastmod
for xml_file in SUB_LATEST_DIR.glob("*.xml"):
    content = xml_file.read_text(encoding="utf-8", errors="replace")
    for entry in parse_sitemap_locs(content):
        baseline[entry["url"]] = entry["lastmod"]
print(f"Baseline: {len(baseline)} URLs from {len(list(SUB_LATEST_DIR.glob('*.xml')))} sub-sitemaps")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: Fetch new sitemap index and all sub-sitemaps
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 2: Fetching sitemaps ===")

# Fetch index
print(f"Fetching index: {SITEMAP_INDEX_URL}")
index_xml = fetch_xml(SITEMAP_INDEX_URL)
sub_urls = parse_sitemap_index_locs(index_xml)
print(f"Found {len(sub_urls)} sub-sitemaps")

# Save index
run_index_path = SITEMAPS_DIR / f"{RUN_ID}.xml"
run_index_path.write_text(index_xml, encoding="utf-8")
(SITEMAPS_DIR / "latest.xml").write_text(index_xml, encoding="utf-8")

# Fetch sub-sitemaps
sub_run_dir = SITEMAPS_DIR / "sub" / RUN_ID
sub_run_dir.mkdir(parents=True, exist_ok=True)

current: dict[str, str] = {}  # url -> lastmod
sub_sitemap_map: dict[str, list[dict]] = {}  # sub_url -> entries

def fetch_sub(sub_url: str):
    try:
        xml_text = fetch_xml(sub_url)
        entries = parse_sitemap_locs(xml_text)
        return sub_url, xml_text, entries, None
    except Exception as e:
        return sub_url, None, [], str(e)

with ThreadPoolExecutor(max_workers=10) as ex:
    futures = {ex.submit(fetch_sub, u): u for u in sub_urls}
    for fut in as_completed(futures):
        sub_url, xml_text, entries, err = fut.result()
        safe_name = sanitize_name(sub_url)
        if err:
            print(f"  ERROR fetching {sub_url}: {err}")
            continue
        # Save to run-specific dir
        (sub_run_dir / safe_name).write_text(xml_text, encoding="utf-8")
        # Overwrite latest
        (SUB_LATEST_DIR / safe_name).write_text(xml_text, encoding="utf-8")
        for entry in entries:
            current[entry["url"]] = entry["lastmod"]
        sub_sitemap_map[sub_url] = entries

print(f"Current: {len(current)} URLs from {len(sub_urls)} sub-sitemaps")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: Diff
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 3: Computing diff ===")
baseline_set = set(baseline.keys())
current_set = set(current.keys())

added_urls = sorted(current_set - baseline_set)
removed_urls = sorted(baseline_set - current_set)
updated_entries = []
for url in current_set & baseline_set:
    if current[url] != baseline[url]:
        updated_entries.append({
            "url": url,
            "old_lastmod": baseline[url],
            "new_lastmod": current[url]
        })
updated_entries.sort(key=lambda x: x["url"])

print(f"Added: {len(added_urls)}, Removed: {len(removed_urls)}, Updated: {len(updated_entries)}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 4: Anomaly detection
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 4: Anomaly detection ===")
known_state = json.loads(STATE_FILE.read_text())

fetch_dt = datetime.now(timezone.utc)
anomalies = []

def parse_dt(s: str):
    if not s:
        return None
    try:
        s2 = s[:10]  # just date
        return datetime.strptime(s2, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except:
        return None

# Future lastmod
for url, lastmod in current.items():
    dt = parse_dt(lastmod)
    if dt and dt > fetch_dt:
        anomalies.append({"kind": "future_lastmod", "url": url, "details": f"lastmod={lastmod} is after fetch time {FETCH_TIME}"})

# Backwards lastmod (lastmod decreased)
for entry in updated_entries:
    old_dt = parse_dt(entry["old_lastmod"])
    new_dt = parse_dt(entry["new_lastmod"])
    if old_dt and new_dt and new_dt < old_dt:
        anomalies.append({"kind": "backwards_lastmod", "url": entry["url"],
                          "details": f"lastmod moved backwards: {entry['old_lastmod']} -> {entry['new_lastmod']}"})

# Backdated new URLs
for url in added_urls:
    lastmod = current[url]
    dt = parse_dt(lastmod)
    # first_seen will be today - if lastmod is > 30 days ago, that's suspicious backdating
    if dt:
        days_back = (fetch_dt - dt).days
        if days_back > 30:
            anomalies.append({"kind": "backdated_new_url", "url": url,
                               "details": f"New URL with lastmod {lastmod} ({days_back} days before first_seen)"})

# Reappeared URLs
for url in added_urls:
    if url in known_state and known_state[url].get("last_seen"):
        anomalies.append({"kind": "reappeared_url", "url": url,
                           "details": f"URL disappeared and reappeared; last seen {known_state[url].get('last_seen')}"})

print(f"Anomalies found: {len(anomalies)}")
for a in anomalies[:5]:
    print(f"  [{a['kind']}] {a['url'][:80]}")
if len(anomalies) > 5:
    print(f"  ... and {len(anomalies)-5} more")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 5: Fetch + convert changed and new pages
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 5: Fetching changed pages ===")

pages_to_fetch = []
for url in added_urls:
    pages_to_fetch.append(("added", url))
for entry in updated_entries:
    pages_to_fetch.append(("updated", entry["url"]))

print(f"Pages to fetch: {len(pages_to_fetch)}")

fetch_failures = []
page_diffs: dict[str, dict] = {}  # url -> {old_md, new_md}

def fetch_page(item):
    kind, url = item
    md_path = url_to_path(url)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    # Capture prior content for updated pages
    prior_content = None
    if kind == "updated" and md_path.exists():
        prior_content = md_path.read_text(encoding="utf-8", errors="replace")

    result = subprocess.run(
        ["python3", "tools/html_to_md.py", "--url", url, "--output", str(md_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )

    # Sanity check
    if md_path.exists():
        content = md_path.read_text(encoding="utf-8", errors="replace")
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            # Restore prior if available
            if prior_content:
                md_path.write_text(prior_content, encoding="utf-8")
            return url, None, kind, f"Blocked/empty response (len={len(content)})", prior_content
        return url, content, kind, None, prior_content
    else:
        return url, None, kind, "Output file not created", prior_content

with ThreadPoolExecutor(max_workers=8) as ex:
    futures = {ex.submit(fetch_page, item): item for item in pages_to_fetch}
    done = 0
    for fut in as_completed(futures):
        url, content, kind, err, prior = fut.result()
        done += 1
        if err:
            fetch_failures.append({"url": url, "error": err})
            if done % 10 == 0 or err:
                print(f"  [{done}/{len(pages_to_fetch)}] FAIL {url[:60]}: {err}")
        else:
            if kind == "updated" and prior:
                page_diffs[url] = {"old_md": prior, "new_md": content}
            if done % 20 == 0:
                print(f"  [{done}/{len(pages_to_fetch)}] OK ...")

print(f"Fetch complete. Failures: {len(fetch_failures)}, Updated with diffs: {len(page_diffs)}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 6: Analyze changes
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 6: Analysis ===")

def summarize_diff(old: str, new: str, max_chars: int = 500) -> str:
    old_lines = set(old.splitlines())
    new_lines = set(new.splitlines())
    added = [l for l in new.splitlines() if l.strip() and l not in old_lines]
    removed = [l for l in old.splitlines() if l.strip() and l not in new_lines]
    parts = []
    if added[:5]:
        parts.append("Added content: " + " | ".join(added[:5])[:200])
    if removed[:5]:
        parts.append("Removed content: " + " | ".join(removed[:5])[:200])
    if not parts:
        # Check length difference
        delta = len(new) - len(old)
        parts.append(f"Content changed (delta: {delta:+d} chars, likely minor updates)")
    return "; ".join(parts)[:max_chars]

def quick_summarize(md_content: str, url: str) -> str:
    lines = [l.strip() for l in md_content.splitlines() if l.strip()]
    # Try to get title + first meaningful paragraph
    title = ""
    body_lines = []
    for l in lines[:30]:
        if l.startswith("#") and not title:
            title = l.lstrip("#").strip()
        elif l and not l.startswith("#") and not l.startswith("!") and not l.startswith("["):
            body_lines.append(l)
        if len(body_lines) >= 3:
            break
    summary = ""
    if title:
        summary += f'"{title}" — '
    summary += " ".join(body_lines)[:300]
    return summary

# Build analysis strings
analysis_updated = []
for url, diff_data in list(page_diffs.items())[:50]:  # cap
    change_desc = summarize_diff(diff_data["old_md"], diff_data["new_md"])
    analysis_updated.append((url, change_desc))

analysis_added = []
for url in added_urls[:50]:
    md_path = url_to_path(url)
    if md_path.exists():
        content = md_path.read_text(encoding="utf-8", errors="replace")
        summary = quick_summarize(content, url)
    else:
        summary = "(fetch failed)"
    analysis_added.append((url, summary))

# ─────────────────────────────────────────────────────────────────────────────
# STEP 7: Write runs/<run_id>/analysis.md
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 7: Writing analysis ===")
run_dir = REPO_ROOT / "runs" / RUN_ID
run_dir.mkdir(parents=True, exist_ok=True)

with open(run_dir / "analysis.md", "w", encoding="utf-8") as f:
    f.write(f"# OpenAI Sitemap Analysis — {RUN_ID}\n\n")
    f.write(f"**Fetch time:** {FETCH_TIME}  \n")
    f.write(f"**Baseline URLs:** {len(baseline)}  \n")
    f.write(f"**Current URLs:** {len(current)}  \n")
    f.write(f"**Sub-sitemaps:** {len(sub_urls)}  \n\n")

    # Stats
    f.write(f"## Summary\n\n")
    f.write(f"- Added: {len(added_urls)}\n")
    f.write(f"- Removed: {len(removed_urls)}\n")
    f.write(f"- Updated (lastmod changed): {len(updated_entries)}\n")
    f.write(f"- Anomalies: {len(anomalies)}\n")
    f.write(f"- Fetch failures: {len(fetch_failures)}\n\n")

    # Anomalies
    if anomalies:
        f.write("## Anomalies\n\n")
        for a in anomalies:
            f.write(f"- **[{a['kind']}]** `{a['url']}`  \n")
            f.write(f"  {a['details']}\n\n")

    # Significant updates
    if analysis_updated:
        f.write("## Updated Pages\n\n")
        for url, desc in analysis_updated:
            f.write(f"- `{url}`  \n  {desc}\n\n")

    if len(updated_entries) > len(analysis_updated):
        f.write(f"_(+ {len(updated_entries) - len(analysis_updated)} more updated pages not detailed above)_\n\n")

    # New pages
    if analysis_added:
        f.write("## New Pages\n\n")
        for url, summary in analysis_added:
            f.write(f"- `{url}`  \n  {summary}\n\n")

    if len(added_urls) > len(analysis_added):
        f.write(f"_(+ {len(added_urls) - len(analysis_added)} more new pages)_\n\n")

    # Removed pages
    if removed_urls:
        f.write("## Removed Pages\n\n")
        for url in removed_urls:
            f.write(f"- `{url}`\n")
        f.write("\n")

    # Fetch failures
    if fetch_failures:
        f.write("## Fetch Failures (needs follow-up)\n\n")
        for ff in fetch_failures:
            f.write(f"- `{ff['url']}`  \n  Error: {ff['error']}\n\n")

print(f"Analysis written to {run_dir / 'analysis.md'}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 8: Update README.md
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 8: Updating README ===")
readme_path = REPO_ROOT / "README.md"
readme_old = readme_path.read_text(encoding="utf-8")

# Build the new section
tldr_parts = []
if added_urls:
    tldr_parts.append(f"{len(added_urls)} new URL{'s' if len(added_urls)!=1 else ''}")
if updated_entries:
    tldr_parts.append(f"{len(updated_entries)} updated")
if removed_urls:
    tldr_parts.append(f"{len(removed_urls)} removed")
if anomalies:
    tldr_parts.append(f"{len(anomalies)} anomal{'ies' if len(anomalies)!=1 else 'y'}")
if not tldr_parts:
    tldr_parts = ["no changes detected"]

tldr = ", ".join(tldr_parts)

new_section_lines = [
    f"## {RUN_ID}",
    "",
    f"**{tldr.capitalize()}.** ",
]

# Fill TL;DR with meaningful context
if added_urls or updated_entries or removed_urls:
    if added_urls:
        new_section_lines[-1] += f"OpenAI's sitemap gained {len(added_urls)} new page{'s' if len(added_urls)!=1 else ''}. "
    if updated_entries:
        new_section_lines[-1] += f"{len(updated_entries)} existing page{'s' if len(updated_entries)!=1 else ''} changed their `lastmod` timestamp. "
    if removed_urls:
        new_section_lines[-1] += f"{len(removed_urls)} page{'s' if len(removed_urls)!=1 else ''} disappeared from the sitemap. "
else:
    new_section_lines[-1] += "OpenAI's public sitemap had no changes since the last run."

new_section_lines.append("")

# Anomalies
if anomalies:
    new_section_lines.append("### Anomalies")
    new_section_lines.append("")
    for a in anomalies[:10]:
        new_section_lines.append(f"- **[{a['kind']}]** `{a['url']}`")
        new_section_lines.append(f"  {a['details']}")
    if len(anomalies) > 10:
        new_section_lines.append(f"- _(+{len(anomalies)-10} more — see runs/{RUN_ID}/analysis.md)_")
    new_section_lines.append("")

# Notable additions
if analysis_added:
    new_section_lines.append("### New Pages")
    new_section_lines.append("")
    for url, summary in analysis_added[:20]:
        md_path_rel = url_to_path(url).relative_to(REPO_ROOT)
        new_section_lines.append(f"- [{url}]({md_path_rel})")
        if summary and summary != "(fetch failed)":
            new_section_lines.append(f"  {summary[:200]}")
    if len(added_urls) > 20:
        new_section_lines.append(f"- _(+{len(added_urls)-20} more — see runs/{RUN_ID}/analysis.md)_")
    new_section_lines.append("")

# Notable updates
if analysis_updated:
    new_section_lines.append("### Updated Pages")
    new_section_lines.append("")
    for url, desc in analysis_updated[:20]:
        new_section_lines.append(f"- `{url}`")
        if desc:
            new_section_lines.append(f"  {desc[:200]}")
    if len(updated_entries) > 20:
        new_section_lines.append(f"- _(+{len(updated_entries)-20} more — see runs/{RUN_ID}/analysis.md)_")
    new_section_lines.append("")

# Removals
if removed_urls:
    new_section_lines.append("### Removed Pages")
    new_section_lines.append("")
    for url in removed_urls[:20]:
        new_section_lines.append(f"- `{url}`")
    if len(removed_urls) > 20:
        new_section_lines.append(f"- _(+{len(removed_urls)-20} more)_")
    new_section_lines.append("")

# Fetch failures note
if fetch_failures:
    new_section_lines.append(f"### Fetch Failures")
    new_section_lines.append(f"")
    new_section_lines.append(f"{len(fetch_failures)} pages could not be fetched — see runs/{RUN_ID}/analysis.md for details.")
    new_section_lines.append("")

# Stats footer
new_section_lines.append(
    f"**Stats:** {len(current)} total URLs | +{len(added_urls)} added | "
    f"~{len(updated_entries)} updated | -{len(removed_urls)} removed | "
    f"{len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps"
)
new_section_lines.append("")
new_section_lines.append("---")
new_section_lines.append("")

new_section = "\n".join(new_section_lines)

# Find insertion point - after the first heading (# OpenAI Sitemap Monitor) and its description
# Insert before the first ## heading
lines = readme_old.splitlines(keepends=True)
insert_idx = None
for i, line in enumerate(lines):
    if line.startswith("## ") and i > 0:
        insert_idx = i
        break

if insert_idx is not None:
    readme_new = "".join(lines[:insert_idx]) + new_section + "\n" + "".join(lines[insert_idx:])
else:
    readme_new = readme_old + "\n" + new_section

readme_path.write_text(readme_new, encoding="utf-8")
print("README updated")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 9: Update state/known_urls.json
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 9: Updating state ===")
today = RUN_ID[:10]

for url in current:
    lastmod = current[url]
    if url in known_state:
        entry = known_state[url]
        entry["last_seen"] = RUN_ID
        if lastmod and lastmod != entry.get("current_lastmod"):
            hist = entry.get("lastmod_history", [])
            hist.append({"run_id": RUN_ID, "lastmod": lastmod})
            entry["lastmod_history"] = hist
            entry["current_lastmod"] = lastmod
    else:
        known_state[url] = {
            "first_seen": RUN_ID,
            "last_seen": RUN_ID,
            "current_lastmod": lastmod,
            "lastmod_history": [{"run_id": RUN_ID, "lastmod": lastmod}] if lastmod else []
        }

STATE_FILE.write_text(json.dumps(known_state, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"State updated. Total known URLs: {len(known_state)}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 10: Write runs/<run_id>/diff.json
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== STEP 10: Writing diff.json ===")
# Find baseline run_id from latest.xml filename context
latest_runs = sorted(SITEMAPS_DIR.glob("*.xml"))
baseline_run = None
for p in reversed(latest_runs):
    if p.name != "latest.xml" and p.stem != RUN_ID:
        baseline_run = p.stem
        break

diff_data = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME,
    "baseline": baseline_run,
    "added": added_urls,
    "removed": removed_urls,
    "updated": updated_entries,
    "anomalies": anomalies,
    "fetch_failures": fetch_failures
}

with open(run_dir / "diff.json", "w", encoding="utf-8") as f:
    json.dump(diff_data, f, indent=2, ensure_ascii=False)
print(f"diff.json written")

# ─────────────────────────────────────────────────────────────────────────────
# Done - print summary for git commit message
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"RUN COMPLETE: {RUN_ID}")
print(f"  Added:    {len(added_urls)}")
print(f"  Updated:  {len(updated_entries)}")
print(f"  Removed:  {len(removed_urls)}")
print(f"  Anomalies:{len(anomalies)}")
print(f"  Failures: {len(fetch_failures)}")
print(f"{'='*60}")

# Save summary for shell to pick up
with open("/tmp/run_summary.json", "w") as f:
    json.dump({
        "run_id": RUN_ID,
        "added": len(added_urls),
        "updated": len(updated_entries),
        "removed": len(removed_urls),
        "anomalies": len(anomalies),
        "failures": len(fetch_failures)
    }, f)
