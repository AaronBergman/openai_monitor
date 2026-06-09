#!/usr/bin/env python3
"""
Daily monitoring run for openai.com sitemap changes.
Run ID: 2026-06-09T09-15Z
"""

import os
import sys
import json
import re
import subprocess
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

import httpx

RUN_ID = "2026-06-09T09-15Z"
REPO_ROOT = Path("/home/user/openai_monitor")
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Paths
SITEMAPS_DIR = REPO_ROOT / "sitemaps/openai.com"
SUB_LATEST_DIR = SITEMAPS_DIR / "sub/latest"
SUB_RUN_DIR = SITEMAPS_DIR / "sub" / RUN_ID
PAGES_DIR = REPO_ROOT / "pages"
RUNS_DIR = REPO_ROOT / "runs" / RUN_ID
STATE_FILE = REPO_ROOT / "state/known_urls.json"

# Create directories
RUNS_DIR.mkdir(parents=True, exist_ok=True)
SUB_RUN_DIR.mkdir(parents=True, exist_ok=True)


def log(msg):
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {msg}", flush=True)


def sanitize_sitemap_name(url: str) -> str:
    """Convert a sub-sitemap URL to a safe filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> _openai.com_sitemap.xml_page.xml
    parsed = urlparse(url)
    path = parsed.netloc + parsed.path
    # Remove trailing slash, replace special chars
    path = path.rstrip("/")
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", path)
    return f"_{safe}.xml"


def fetch_xml(url: str) -> str:
    """Fetch XML using plain httpx (sitemap XML is not blocked)."""
    r = httpx.get(url, timeout=30, follow_redirects=True)
    r.raise_for_status()
    return r.text


def parse_sitemap_index(xml_text: str) -> list[str]:
    """Parse a sitemap index and return list of sub-sitemap URLs."""
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_text)
    locs = []
    for sitemap in root.findall("sm:sitemap", ns):
        loc = sitemap.find("sm:loc", ns)
        if loc is not None and loc.text:
            locs.append(loc.text.strip())
    return locs


def parse_url_set(xml_text: str) -> dict[str, str]:
    """Parse a urlset sitemap, return {url: lastmod} dict."""
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        log(f"  XML parse error: {e}")
        return {}
    urls = {}
    for url_el in root.findall("sm:url", ns):
        loc = url_el.find("sm:loc", ns)
        lastmod = url_el.find("sm:lastmod", ns)
        if loc is not None and loc.text:
            urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None and lastmod.text else ""
    return urls


def load_baseline() -> dict[str, str]:
    """Load baseline URL set from sub/latest/*.xml files."""
    baseline = {}
    for f in SUB_LATEST_DIR.glob("*.xml"):
        try:
            xml_text = f.read_text(encoding="utf-8")
            urls = parse_url_set(xml_text)
            baseline.update(urls)
        except Exception as e:
            log(f"  Warning: could not load baseline {f.name}: {e}")
    return baseline


def url_to_repo_path(url: str) -> str:
    """Shell out to tools/url_path.py for canonical path."""
    result = subprocess.run(
        [sys.executable, "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()


def fetch_page_to_md(url: str, output_path: Path) -> tuple[bool, str]:
    """Fetch page via html_to_md.py, return (success, error_msg)."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, "tools/html_to_md.py", "--url", url, "--output", str(output_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    if result.returncode != 0:
        return False, result.stderr.strip() or result.stdout.strip()
    # Sanity check
    if output_path.exists():
        content = output_path.read_text(encoding="utf-8", errors="replace")
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            return False, f"Blocked/empty content: {len(content)} chars"
    return True, ""


# ============================================================
# STEP 1: Load baseline
# ============================================================
log("Loading baseline from sub/latest/...")
baseline = load_baseline()
log(f"  Baseline: {len(baseline)} URLs")

# ============================================================
# STEP 2: Fetch + snapshot current sitemap
# ============================================================
log("Fetching sitemap index...")
index_xml = fetch_xml(SITEMAP_INDEX_URL)
ACTUAL_FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Save index
index_run_path = SITEMAPS_DIR / f"{RUN_ID}.xml"
index_run_path.write_text(index_xml, encoding="utf-8")
latest_index_path = SITEMAPS_DIR / "latest.xml"
latest_index_path.write_text(index_xml, encoding="utf-8")
log(f"  Saved index -> {index_run_path.name}")

sub_sitemap_urls = parse_sitemap_index(index_xml)
log(f"  Found {len(sub_sitemap_urls)} sub-sitemaps")

# Fetch all sub-sitemaps
current = {}  # url -> lastmod
url_to_subsitemap = {}  # url -> sub-sitemap name
fetch_errors = []

for sub_url in sub_sitemap_urls:
    sname = sanitize_sitemap_name(sub_url)
    log(f"  Fetching {sub_url}...")
    try:
        sub_xml = fetch_xml(sub_url)
        # Save to run dir and overwrite latest
        (SUB_RUN_DIR / sname).write_text(sub_xml, encoding="utf-8")
        (SUB_LATEST_DIR / sname).write_text(sub_xml, encoding="utf-8")
        urls_in_sub = parse_url_set(sub_xml)
        log(f"    -> {len(urls_in_sub)} URLs")
        for u, lm in urls_in_sub.items():
            current[u] = lm
            url_to_subsitemap[u] = sname
    except Exception as e:
        log(f"    ERROR: {e}")
        fetch_errors.append({"url": sub_url, "error": str(e)})

log(f"  Total current URLs: {len(current)}")

# ============================================================
# STEP 3: Diff
# ============================================================
log("Computing diff...")
baseline_set = set(baseline.keys())
current_set = set(current.keys())

added = sorted(current_set - baseline_set)
removed = sorted(baseline_set - current_set)
updated = []
for url in current_set & baseline_set:
    if current[url] != baseline[url]:
        updated.append({"url": url, "old_lastmod": baseline[url], "new_lastmod": current[url]})
updated.sort(key=lambda x: x["url"])

log(f"  Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")

# ============================================================
# STEP 4: Anomaly detection
# ============================================================
log("Detecting anomalies...")
anomalies = []

fetch_dt = datetime.fromisoformat(ACTUAL_FETCH_TIME.replace("Z", "+00:00"))

# Load known_urls for history
known_urls = json.loads(STATE_FILE.read_text(encoding="utf-8"))

for url, lm in current.items():
    if not lm:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
    except ValueError:
        continue

    # Future lastmod
    if lm_dt > fetch_dt:
        anomalies.append({
            "kind": "future_lastmod",
            "url": url,
            "details": f"lastmod {lm} is after fetch time {ACTUAL_FETCH_TIME}"
        })

# Backwards lastmod (lastmod moved backward vs baseline)
for item in updated:
    url = item["url"]
    old_lm = item["old_lastmod"]
    new_lm = item["new_lastmod"]
    if old_lm and new_lm:
        try:
            old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
            new_dt = datetime.fromisoformat(new_lm.replace("Z", "+00:00"))
            if new_dt < old_dt:
                anomalies.append({
                    "kind": "backwards_lastmod",
                    "url": url,
                    "details": f"lastmod moved backwards: {old_lm} -> {new_lm}"
                })
        except ValueError:
            pass

# New URL with backdated lastmod
for url in added:
    lm = current.get(url, "")
    if not lm:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
        # If lastmod is more than 7 days before today
        days_before = (fetch_dt - lm_dt).days
        if days_before > 7:
            anomalies.append({
                "kind": "backdated_new_url",
                "url": url,
                "details": f"New URL with lastmod {lm} ({days_before} days before first_seen)"
            })
    except ValueError:
        pass

# URLs that disappeared and reappeared
for url in added:
    if url in known_urls and known_urls[url].get("last_seen") and known_urls[url]["last_seen"] < RUN_ID:
        prev_first_seen = known_urls[url].get("first_seen", "")
        if prev_first_seen:
            anomalies.append({
                "kind": "reappeared_url",
                "url": url,
                "details": f"URL previously seen (first_seen={prev_first_seen}), then disappeared, now reappeared"
            })

log(f"  Anomalies found: {len(anomalies)}")

# ============================================================
# STEP 5: Fetch changed and new pages
# ============================================================
log("Fetching changed and new pages...")

pages_to_fetch = []
for url in added:
    pages_to_fetch.append(("added", url))
for item in updated:
    pages_to_fetch.append(("updated", item["url"]))

log(f"  Pages to fetch: {len(pages_to_fetch)}")

page_fetch_failures = []
page_diffs = []  # list of {url, old_path, new_path, diff_summary}

# For updated pages, save previous content first
prev_contents = {}
for kind, url in pages_to_fetch:
    if kind == "updated":
        repo_path = url_to_repo_path(url)
        full_path = REPO_ROOT / repo_path
        if full_path.exists():
            try:
                result = subprocess.run(
                    ["git", "show", f"HEAD:{repo_path}"],
                    capture_output=True, text=True, cwd=REPO_ROOT
                )
                if result.returncode == 0:
                    prev_contents[url] = result.stdout
            except Exception:
                pass

# Fetch with modest parallelism using subprocess
import concurrent.futures

def fetch_one(args):
    kind, url = args
    repo_path = url_to_repo_path(url)
    if not repo_path:
        return (kind, url, False, "Could not compute repo path", None)
    full_path = REPO_ROOT / repo_path
    success, err = fetch_page_to_md(url, full_path)
    return (kind, url, success, err, repo_path)

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = list(executor.map(fetch_one, pages_to_fetch))

for (kind, url, success, err, repo_path) in futures:
    if not success:
        log(f"  FETCH FAIL [{kind}] {url}: {err}")
        page_fetch_failures.append({"url": url, "error": err})
    else:
        log(f"  OK [{kind}] {url} -> {repo_path}")

log(f"  Fetch failures: {len(page_fetch_failures)}")

# ============================================================
# STEP 6: Analyze diffs for updated pages
# ============================================================
log("Analyzing diffs...")

def summarize_diff(url, prev_text, new_text) -> str:
    """Produce a brief diff summary."""
    prev_lines = set(prev_text.splitlines())
    new_lines = set(new_text.splitlines())
    added_lines = [l for l in new_text.splitlines() if l not in prev_lines and l.strip()]
    removed_lines = [l for l in prev_text.splitlines() if l not in new_lines and l.strip()]
    summary = []
    if added_lines:
        summary.append(f"  Added lines (~{len(added_lines)}): " + " | ".join(added_lines[:3]))
    if removed_lines:
        summary.append(f"  Removed lines (~{len(removed_lines)}): " + " | ".join(removed_lines[:3]))
    return "\n".join(summary) if summary else "  (no visible text change)"

content_changes = []  # list of (url, old_preview, new_preview)
for kind, url in pages_to_fetch:
    if kind == "updated" and url in prev_contents:
        repo_path = url_to_repo_path(url)
        full_path = REPO_ROOT / repo_path
        if full_path.exists():
            new_text = full_path.read_text(encoding="utf-8", errors="replace")
            old_text = prev_contents[url]
            if old_text.strip() != new_text.strip():
                content_changes.append((url, old_text, new_text))

log(f"  Pages with actual content changes: {len(content_changes)}")

# ============================================================
# STEP 7: Write analysis.md
# ============================================================
log("Writing analysis.md...")

analysis_lines = [
    f"# Analysis: {RUN_ID}",
    "",
    f"**Fetch time:** {ACTUAL_FETCH_TIME}  ",
    f"**Total current URLs:** {len(current)}  ",
    f"**Baseline URLs:** {len(baseline)}  ",
    f"**Added:** {len(added)}  ",
    f"**Removed:** {len(removed)}  ",
    f"**Updated (sitemap lastmod):** {len(updated)}  ",
    f"**Pages with actual visible content changes:** {len(content_changes)}  ",
    f"**Anomalies:** {len(anomalies)}  ",
    f"**Fetch failures:** {len(page_fetch_failures)}  ",
    "",
    "---",
    "",
    "## Anomalies",
    "",
]

if anomalies:
    for a in anomalies:
        analysis_lines += [
            f"### {a['kind'].replace('_', ' ').title()}",
            f"**URL:** {a['url']}  ",
            f"**Details:** {a['details']}",
            "",
        ]
else:
    analysis_lines += ["None detected.", ""]

analysis_lines += ["---", "", "## Significant Updates", ""]

# Write content changes
if content_changes:
    for url, old_text, new_text in content_changes[:20]:
        repo_path = url_to_repo_path(url)
        analysis_lines += [
            f"### {url}",
            f"**Page:** [{repo_path}](../../{repo_path})  ",
        ]
        # Find updated item info
        for item in updated:
            if item["url"] == url:
                analysis_lines.append(f"**lastmod:** `{item['old_lastmod']}` → `{item['new_lastmod']}`  ")
                break
        # Show diff preview
        old_lines = old_text.splitlines()
        new_lines = new_text.splitlines()
        old_set = set(old_lines)
        new_set = set(new_lines)
        added_content = [l for l in new_lines if l not in old_set and l.strip() and not l.strip().startswith('#') and len(l.strip()) > 20]
        removed_content = [l for l in old_lines if l not in new_set and l.strip() and not l.strip().startswith('#') and len(l.strip()) > 20]
        if added_content:
            analysis_lines.append("\n**New content (sample):**")
            for l in added_content[:5]:
                analysis_lines.append(f"> {l.strip()[:200]}")
        if removed_content:
            analysis_lines.append("\n**Removed content (sample):**")
            for l in removed_content[:5]:
                analysis_lines.append(f"> ~~{l.strip()[:200]}~~")
        analysis_lines.append("")
else:
    analysis_lines.append("No pages with actual content changes (sitemap lastmod updates only).")
    analysis_lines.append("")

analysis_lines += ["---", "", "## All Updated URLs (lastmod changed)", ""]
for item in updated[:50]:
    analysis_lines.append(f"- `{item['url']}` — `{item['old_lastmod']}` → `{item['new_lastmod']}`")
if len(updated) > 50:
    analysis_lines.append(f"- *(... and {len(updated)-50} more)*")
analysis_lines.append("")

analysis_lines += ["---", "", "## New Pages", ""]
if added:
    for url in added[:30]:
        repo_path = url_to_repo_path(url)
        lm = current.get(url, "")
        analysis_lines.append(f"- [{url}]({url}) — lastmod: `{lm}`  ")
        analysis_lines.append(f"  Saved: `{repo_path}`")
    if len(added) > 30:
        analysis_lines.append(f"- *(... and {len(added)-30} more)*")
else:
    analysis_lines.append("None.")
analysis_lines.append("")

analysis_lines += ["---", "", "## Removed Pages", ""]
if removed:
    for url in removed[:30]:
        analysis_lines.append(f"- {url}")
    if len(removed) > 30:
        analysis_lines.append(f"- *(... and {len(removed)-30} more)*")
else:
    analysis_lines.append("None.")
analysis_lines.append("")

analysis_lines += ["---", "", "## Fetch Failures", ""]
if page_fetch_failures:
    for f in page_fetch_failures:
        analysis_lines.append(f"- `{f['url']}`: {f['error']}")
else:
    analysis_lines.append("None.")
analysis_lines.append("")

(RUNS_DIR / "analysis.md").write_text("\n".join(analysis_lines), encoding="utf-8")
log("  analysis.md written")

# ============================================================
# STEP 8: Update README.md
# ============================================================
log("Updating README.md...")

readme_path = REPO_ROOT / "README.md"
old_readme = readme_path.read_text(encoding="utf-8")

# Build the new section
readme_section_lines = [
    f"## Run: {RUN_ID}",
    "",
    f"**Fetch time:** {ACTUAL_FETCH_TIME} | **Total URLs:** {len(current)} | **Added:** {len(added)} | **Updated:** {len(updated)} | **Removed:** {len(removed)} | **Anomalies:** {len(anomalies)} | **Sub-sitemaps:** {len(sub_sitemap_urls)}",
    "",
]

# TL;DR paragraph
if len(added) == 0 and len(removed) == 0 and len(content_changes) == 0:
    readme_section_lines.append(
        f"**TL;DR:** Quiet day on OpenAI's public website. The sitemap reports {len(updated)} URL lastmod "
        f"timestamps changed, but no pages showed new visible content when fetched. No URLs were added or removed."
    )
elif len(added) > 0 or len(content_changes) > 0:
    added_desc = f"{len(added)} new URL(s) appeared" if added else ""
    updated_desc = f"{len(content_changes)} page(s) with visible content changes" if content_changes else ""
    parts = [p for p in [added_desc, updated_desc] if p]
    readme_section_lines.append(
        f"**TL;DR:** Today's scan found {', '.join(parts)} on openai.com. "
        f"The sitemap logged {len(updated)} timestamp changes across existing pages."
    )
else:
    readme_section_lines.append(
        f"**TL;DR:** Minor site changes today — {len(removed)} URL(s) removed, "
        f"{len(updated)} lastmod updates with {len(content_changes)} showing visible content changes."
    )
readme_section_lines.append("")

# Anomalies
if anomalies:
    readme_section_lines += ["### ⚠️ Anomalies", ""]
    for a in anomalies:
        readme_section_lines.append(f"- **{a['kind'].replace('_', ' ').upper()}** — `{a['url']}`: {a['details']}")
    readme_section_lines.append("")

# Notable content changes
if content_changes:
    readme_section_lines += ["### Notable Updates", ""]
    for url, old_text, new_text in content_changes[:10]:
        repo_path = url_to_repo_path(url)
        # Find lastmod change
        lm_change = ""
        for item in updated:
            if item["url"] == url:
                lm_change = f" (lastmod: {item['old_lastmod'][:10]} → {item['new_lastmod'][:10]})"
                break
        old_set = set(old_text.splitlines())
        new_set = set(new_text.splitlines())
        added_content = [l for l in new_text.splitlines() if l not in old_set and l.strip() and len(l.strip()) > 20]
        readme_section_lines.append(f"- **[{url}]({url})**{lm_change}")
        if added_content:
            for l in added_content[:2]:
                readme_section_lines.append(f"  > {l.strip()[:180]}")
    readme_section_lines.append("")

# New pages
if added:
    readme_section_lines += ["### New Pages", ""]
    for url in added[:15]:
        repo_path = url_to_repo_path(url)
        lm = current.get(url, "")
        readme_section_lines.append(f"- [{url}]({url}) (lastmod: {lm[:10] if lm else 'n/a'})")
    if len(added) > 15:
        readme_section_lines.append(f"- *... and {len(added)-15} more — see [runs/{RUN_ID}/analysis.md](runs/{RUN_ID}/analysis.md)*")
    readme_section_lines.append("")

# Removed pages
if removed:
    readme_section_lines += ["### Removed Pages", ""]
    for url in removed[:10]:
        readme_section_lines.append(f"- ~~{url}~~")
    if len(removed) > 10:
        readme_section_lines.append(f"- *... and {len(removed)-10} more*")
    readme_section_lines.append("")

readme_section_lines += [
    f"*Full analysis: [runs/{RUN_ID}/analysis.md](runs/{RUN_ID}/analysis.md)*",
    "",
    "---",
    "",
]

new_section = "\n".join(readme_section_lines)

# Find the insertion point: after the first "---" separator following the header
# We want to prepend AFTER the README header/intro, before the first run section
# Find the first "## Run:" to insert before it
first_run_pos = old_readme.find("\n## Run:")
if first_run_pos == -1:
    # No existing run sections, append after header
    new_readme = old_readme.rstrip() + "\n\n" + new_section
else:
    new_readme = old_readme[:first_run_pos + 1] + new_section + old_readme[first_run_pos + 1:]

readme_path.write_text(new_readme, encoding="utf-8")
log("  README.md updated")

# ============================================================
# STEP 9: Update state/known_urls.json
# ============================================================
log("Updating state/known_urls.json...")

for url in current:
    if url not in known_urls:
        known_urls[url] = {
            "first_seen": RUN_ID,
            "last_seen": RUN_ID,
            "current_lastmod": current[url],
            "lastmod_history": [{"run_id": RUN_ID, "lastmod": current[url]}] if current[url] else []
        }
    else:
        known_urls[url]["last_seen"] = RUN_ID
        old_lm = known_urls[url].get("current_lastmod", "")
        if current[url] != old_lm:
            known_urls[url]["current_lastmod"] = current[url]
            known_urls[url].setdefault("lastmod_history", []).append({
                "run_id": RUN_ID,
                "lastmod": current[url]
            })

STATE_FILE.write_text(json.dumps(known_urls, indent=2, ensure_ascii=False), encoding="utf-8")
log(f"  State updated: {len(known_urls)} URLs total")

# ============================================================
# STEP 10: Write diff.json
# ============================================================
log("Writing diff.json...")

diff_data = {
    "run_id": RUN_ID,
    "fetch_time": ACTUAL_FETCH_TIME,
    "baseline": "2026-06-08T09-15Z",
    "added": added,
    "removed": removed,
    "updated": updated,
    "anomalies": anomalies,
    "fetch_failures": page_fetch_failures
}
(RUNS_DIR / "diff.json").write_text(json.dumps(diff_data, indent=2, ensure_ascii=False), encoding="utf-8")
log("  diff.json written")

# ============================================================
# Summary
# ============================================================
log("")
log("=" * 60)
log(f"RUN COMPLETE: {RUN_ID}")
log(f"  Fetch time: {ACTUAL_FETCH_TIME}")
log(f"  URLs: {len(current)} current, {len(baseline)} baseline")
log(f"  Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")
log(f"  Content changes: {len(content_changes)}")
log(f"  Anomalies: {len(anomalies)}")
log(f"  Fetch failures: {len(page_fetch_failures)}")
log("=" * 60)
