#!/usr/bin/env python3
"""Full monitoring pipeline for openai.com sitemap."""

import os
import sys
import json
import glob
import shutil
import subprocess
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import httpx

RUN_ID = "2026-06-08T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REPO_ROOT = Path("/home/user/openai_monitor")
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

print(f"=== Run ID: {RUN_ID} ===")
print(f"=== Fetch time: {FETCH_TIME} ===")


# ─── STEP 1: Read baseline ───────────────────────────────────────────────────

def parse_sub_sitemap(path):
    """Parse a sub-sitemap XML file and return dict of {url: lastmod}."""
    result = {}
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        for url_el in root.findall(f"{NS}url"):
            loc = url_el.findtext(f"{NS}loc", "").strip()
            lastmod = url_el.findtext(f"{NS}lastmod", "").strip()
            if loc:
                result[loc] = lastmod
    except Exception as e:
        print(f"  WARNING: Failed to parse {path}: {e}")
    return result

baseline_urls = {}  # {url: lastmod}
latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
# Use the most recent naming convention: sitemap.xml_*.xml (32 files)
baseline_files = sorted(latest_dir.glob("sitemap.xml_*.xml"))
print(f"\nStep 1: Loading baseline from {len(baseline_files)} sub-sitemaps...")
for f in baseline_files:
    entries = parse_sub_sitemap(f)
    baseline_urls.update(entries)
print(f"  Baseline: {len(baseline_urls)} URLs")


# ─── STEP 2: Fetch & Snapshot ────────────────────────────────────────────────

print(f"\nStep 2: Fetching sitemaps...")

def fetch_xml(url, retries=3):
    for attempt in range(retries):
        try:
            r = httpx.get(url, timeout=30, follow_redirects=True,
                          headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()
            return r.text
        except Exception as e:
            if attempt == retries - 1:
                raise
            import time; time.sleep(2 ** attempt)

# Fetch root sitemap index
root_xml = fetch_xml("https://openai.com/sitemap.xml")
run_sitemaps_dir = REPO_ROOT / f"sitemaps/openai.com"
run_sitemaps_dir.mkdir(parents=True, exist_ok=True)
(run_sitemaps_dir / f"{RUN_ID}.xml").write_text(root_xml)
(run_sitemaps_dir / "latest.xml").write_text(root_xml)
print(f"  Saved root sitemap index")

# Parse sub-sitemap URLs from root
root_tree = ET.fromstring(root_xml)
sub_sitemap_urls = []
for sm in root_tree.findall(f"{NS}sitemap"):
    loc = sm.findtext(f"{NS}loc", "").strip()
    if loc:
        sub_sitemap_urls.append(loc)
print(f"  Found {len(sub_sitemap_urls)} sub-sitemaps")

# Fetch each sub-sitemap
sub_run_dir = REPO_ROOT / f"sitemaps/openai.com/sub/{RUN_ID}"
sub_run_dir.mkdir(parents=True, exist_ok=True)
sub_latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
sub_latest_dir.mkdir(parents=True, exist_ok=True)

def sanitize_filename(url):
    """Convert URL to safe filename using the 'sitemap.xml_<section>' convention."""
    # Extract just the path part after the last /sitemap.xml/
    # e.g. https://openai.com/sitemap.xml/api/ -> sitemap.xml_api.xml
    parsed = urlparse(url)
    path = parsed.path  # e.g. /sitemap.xml/api/
    # Remove leading slash
    path = path.lstrip("/")
    # Replace slashes with underscores
    path = path.replace("/", "_").rstrip("_")
    return f"{path}.xml"

current_sub_sitemaps = {}  # {filename: xml_content}
current_urls = {}  # {url: lastmod}

for sub_url in sub_sitemap_urls:
    try:
        xml_content = fetch_xml(sub_url)
        fname = sanitize_filename(sub_url)
        current_sub_sitemaps[fname] = (sub_url, xml_content)
        # Save to run-specific dir
        (sub_run_dir / fname).write_text(xml_content)
        # Overwrite latest
        (sub_latest_dir / fname).write_text(xml_content)
        # Parse URLs
        entries = {}
        tree = ET.fromstring(xml_content)
        for url_el in tree.findall(f"{NS}url"):
            loc = url_el.findtext(f"{NS}loc", "").strip()
            lastmod = url_el.findtext(f"{NS}lastmod", "").strip()
            if loc:
                entries[loc] = lastmod
        current_urls.update(entries)
        print(f"  {fname}: {len(entries)} URLs")
    except Exception as e:
        print(f"  ERROR fetching {sub_url}: {e}")

print(f"  Total current URLs: {len(current_urls)}")


# ─── STEP 3: Diff ────────────────────────────────────────────────────────────

print(f"\nStep 3: Computing diff...")

baseline_set = set(baseline_urls.keys())
current_set = set(current_urls.keys())

added = sorted(current_set - baseline_set)
removed = sorted(baseline_set - current_set)
updated = []
for url in baseline_set & current_set:
    old_lm = baseline_urls[url]
    new_lm = current_urls[url]
    if old_lm != new_lm:
        updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})
updated.sort(key=lambda x: x["url"])

print(f"  Added: {len(added)}")
print(f"  Removed: {len(removed)}")
print(f"  Updated: {len(updated)}")


# ─── STEP 4: Anomaly Detection ───────────────────────────────────────────────

print(f"\nStep 4: Anomaly detection...")

anomalies = []
fetch_dt = datetime.now(timezone.utc)

def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except:
        return None

# Load known_urls for history
known_urls_path = REPO_ROOT / "state/known_urls.json"
known_urls = {}
if known_urls_path.exists():
    known_urls = json.loads(known_urls_path.read_text())

# Check for future lastmod
for url, lm in current_urls.items():
    dt = parse_dt(lm)
    if dt and dt > fetch_dt:
        anomalies.append({
            "kind": "future_lastmod",
            "url": url,
            "details": f"lastmod {lm} is in the future (fetch time: {FETCH_TIME})"
        })

# Check for backwards lastmod (lastmod decreased)
for entry in updated:
    old_dt = parse_dt(entry["old_lastmod"])
    new_dt = parse_dt(entry["new_lastmod"])
    if old_dt and new_dt and new_dt < old_dt:
        anomalies.append({
            "kind": "backwards_lastmod",
            "url": entry["url"],
            "details": f"lastmod moved backwards from {entry['old_lastmod']} to {entry['new_lastmod']}"
        })

# Check for backdated new URLs
for url in added:
    lm = current_urls[url]
    lm_dt = parse_dt(lm)
    if lm_dt:
        # first_seen is run_id format, compare date portion
        first_seen_str = RUN_ID[:10]  # YYYY-MM-DD
        first_seen_dt = datetime.fromisoformat(first_seen_str).replace(tzinfo=timezone.utc)
        diff_days = (first_seen_dt - lm_dt.replace(tzinfo=timezone.utc)).days
        if diff_days > 7:
            anomalies.append({
                "kind": "backdated_new_url",
                "url": url,
                "details": f"new URL has lastmod {lm} which predates first_seen {RUN_ID[:10]} by {diff_days} days"
            })

# Check for reappeared URLs
for url in added:
    if url in known_urls and known_urls[url].get("last_seen", "") < RUN_ID:
        prev_last = known_urls[url].get("last_seen", "unknown")
        anomalies.append({
            "kind": "reappeared_url",
            "url": url,
            "details": f"URL was previously seen (last_seen: {prev_last}) and has reappeared"
        })

print(f"  Anomalies: {len(anomalies)}")
for a in anomalies[:5]:
    print(f"    {a['kind']}: {a['url']}")


# ─── STEP 5: Fetch changed/new pages ─────────────────────────────────────────

print(f"\nStep 5: Fetching changed/new pages...")

def url_to_path(url):
    """Convert URL to repo path using tools/url_path.py"""
    result = subprocess.run(
        ["python3", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()

def fetch_page(url, output_path):
    """Fetch page using html_to_md.py"""
    result = subprocess.run(
        ["python3", "tools/html_to_md.py", "--url", url, "--output", str(output_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    return result.returncode, result.stdout, result.stderr

pages_to_fetch = [(url, "added") for url in added] + [(entry["url"], "updated") for entry in updated]
print(f"  Total pages to fetch: {len(pages_to_fetch)}")

# For updated pages, capture prior content first
prior_content = {}
for entry in updated:
    url = entry["url"]
    rel_path = url_to_path(url)
    if rel_path:
        full_path = REPO_ROOT / rel_path
        if full_path.exists():
            prior_content[url] = full_path.read_text()

fetch_failures = []
fetched_pages = []
page_diffs = {}  # {url: (old_content, new_content)}

# Batch fetches with limited parallelism (use subprocess for each, up to 8 at a time)
import concurrent.futures

def fetch_one(args):
    url, kind = args
    rel_path = url_to_path(url)
    if not rel_path:
        return url, kind, None, "no_path", ""

    output_path = REPO_ROOT / rel_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # For updated pages, save prior content
    old_content = prior_content.get(url, "")

    returncode, stdout, stderr = fetch_page(url, output_path)

    # Sanity check
    if output_path.exists():
        content = output_path.read_text()
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            return url, kind, rel_path, "blocked", f"Content too short or blocked ({len(content)} chars)"
        return url, kind, rel_path, "ok", old_content
    else:
        return url, kind, rel_path, "error", stderr[:200]

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(fetch_one, args): args for args in pages_to_fetch}
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        url, kind, rel_path, status, extra = future.result()
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(pages_to_fetch)} pages fetched...")

        if status == "ok":
            fetched_pages.append((url, kind, rel_path))
            if kind == "updated" and extra:  # extra is old_content
                new_content = (REPO_ROOT / rel_path).read_text() if rel_path else ""
                if extra != new_content:
                    page_diffs[url] = (extra, new_content)
        elif status in ("blocked", "error", "no_path"):
            fetch_failures.append({"url": url, "error": f"{status}: {extra}"})
            print(f"  FAIL [{status}]: {url}")

print(f"  Fetched: {len(fetched_pages)}, Failures: {len(fetch_failures)}")


# ─── STEP 6: Analyze ─────────────────────────────────────────────────────────

print(f"\nStep 6: Analyzing changes...")

def summarize_diff(old, new):
    """Simple line-based diff summary."""
    old_lines = set(old.splitlines())
    new_lines = set(new.splitlines())
    added_lines = [l for l in new_lines - old_lines if l.strip()]
    removed_lines = [l for l in old_lines - new_lines if l.strip()]

    summary_parts = []
    if added_lines:
        # Show up to 5 added lines
        snippet = "; ".join(added_lines[:5])
        if len(added_lines) > 5:
            snippet += f" ... (+{len(added_lines)-5} more)"
        summary_parts.append(f"Added content: {snippet[:300]}")
    if removed_lines:
        snippet = "; ".join(removed_lines[:5])
        if len(removed_lines) > 5:
            snippet += f" ... (+{len(removed_lines)-5} more)"
        summary_parts.append(f"Removed content: {snippet[:300]}")

    return " | ".join(summary_parts) if summary_parts else "Minor whitespace or formatting changes"

# Build analysis for new pages
new_page_summaries = {}
for url, kind, rel_path in fetched_pages:
    if kind == "added" and rel_path:
        full_path = REPO_ROOT / rel_path
        if full_path.exists():
            content = full_path.read_text()
            # Extract first meaningful lines as summary
            lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
            summary = " ".join(lines[:3])[:300] if lines else "(no content extracted)"
            new_page_summaries[url] = summary

# Build update summaries
update_summaries = {}
for url, (old, new) in page_diffs.items():
    update_summaries[url] = summarize_diff(old, new)


# ─── STEP 7: Write runs/<run_id>/analysis.md ─────────────────────────────────

print(f"\nStep 7: Writing analysis...")

run_dir = REPO_ROOT / f"runs/{RUN_ID}"
run_dir.mkdir(parents=True, exist_ok=True)

analysis_lines = [
    f"# Analysis: {RUN_ID}",
    f"",
    f"**Fetch time:** {FETCH_TIME}  ",
    f"**Total current URLs:** {len(current_urls)}  ",
    f"**Baseline URLs:** {len(baseline_urls)}  ",
    f"**Added:** {len(added)}  ",
    f"**Removed:** {len(removed)}  ",
    f"**Updated:** {len(updated)}  ",
    f"**Anomalies:** {len(anomalies)}  ",
    f"**Fetch failures:** {len(fetch_failures)}  ",
    f"",
]

# Anomalies section
if anomalies:
    analysis_lines += [f"## Anomalies", f""]
    for a in anomalies:
        analysis_lines.append(f"- **{a['kind']}** — `{a['url']}`  ")
        analysis_lines.append(f"  {a['details']}")
        analysis_lines.append(f"")
else:
    analysis_lines += [f"## Anomalies", f"", f"None detected.", f""]

# Updated pages
if updated:
    analysis_lines += [f"## Updated Pages ({len(updated)})", f""]
    for entry in updated:
        url = entry["url"]
        rel = url_to_path(url)
        analysis_lines.append(f"### {url}")
        analysis_lines.append(f"- lastmod: `{entry['old_lastmod']}` → `{entry['new_lastmod']}`")
        if url in update_summaries:
            analysis_lines.append(f"- Changes: {update_summaries[url]}")
        elif url in fetch_failures or url not in {f['url'] for f in fetch_failures}:
            analysis_lines.append(f"- Page diff: (fetch attempted)")
        analysis_lines.append(f"")
else:
    analysis_lines += [f"## Updated Pages", f"", f"None.", f""]

# New pages
if added:
    analysis_lines += [f"## New Pages ({len(added)})", f""]
    for url in added:
        analysis_lines.append(f"### {url}")
        lm = current_urls.get(url, "")
        if lm:
            analysis_lines.append(f"- lastmod: `{lm}`")
        if url in new_page_summaries:
            analysis_lines.append(f"- Summary: {new_page_summaries[url]}")
        analysis_lines.append(f"")
else:
    analysis_lines += [f"## New Pages", f"", f"None.", f""]

# Removed pages
if removed:
    analysis_lines += [f"## Removed Pages ({len(removed)})", f""]
    for url in removed:
        analysis_lines.append(f"- `{url}` (lastmod was `{baseline_urls.get(url, 'unknown')}`)")
    analysis_lines.append(f"")
else:
    analysis_lines += [f"## Removed Pages", f"", f"None.", f""]

# Fetch failures
if fetch_failures:
    analysis_lines += [f"## Fetch Failures ({len(fetch_failures)})", f""]
    for ff in fetch_failures:
        analysis_lines.append(f"- `{ff['url']}`: {ff['error'][:200]}")
    analysis_lines.append(f"")

(run_dir / "analysis.md").write_text("\n".join(analysis_lines))
print(f"  Written: runs/{RUN_ID}/analysis.md")


# ─── STEP 8: Update README.md ─────────────────────────────────────────────────

print(f"\nStep 8: Updating README.md...")

readme_path = REPO_ROOT / "README.md"
existing_readme = readme_path.read_text() if readme_path.exists() else ""

# Determine if there's notable content
has_anomalies = len(anomalies) > 0
has_additions = len(added) > 0
has_removals = len(removed) > 0
has_updates = len(updated) > 0

# Build the new section
section_lines = [
    f"## {RUN_ID[:10]} — Run {RUN_ID}",
    f"",
]

# TL;DR
if not has_additions and not has_removals and not has_anomalies and not has_updates:
    tldr = f"Routine daily check on {RUN_ID[:10]}: no changes detected. OpenAI's public sitemap remains stable with {len(current_urls)} indexed URLs across {len(sub_sitemap_urls)} sub-sitemaps."
elif has_additions or has_removals or has_updates:
    parts = []
    if has_additions:
        parts.append(f"{len(added)} new page{'s' if len(added) != 1 else ''} added")
    if has_removals:
        parts.append(f"{len(removed)} page{'s' if len(removed) != 1 else ''} removed")
    if has_updates:
        parts.append(f"{len(updated)} page{'s' if len(updated) != 1 else ''} updated")
    changes_str = ", ".join(parts)
    tldr = f"Daily check on {RUN_ID[:10]}: {changes_str} in OpenAI's public sitemap (total: {len(current_urls)} URLs)."
else:
    tldr = f"Daily check on {RUN_ID[:10]}: sitemap activity detected."

section_lines += [f"**TL;DR:** {tldr}", f""]

# Anomalies
if anomalies:
    section_lines += [f"### ⚠️ Anomalies", f""]
    for a in anomalies:
        section_lines.append(f"- **{a['kind']}**: `{a['url'][:80]}` — {a['details'][:150]}")
    section_lines.append(f"")

# Notable additions
if added:
    section_lines += [f"### New Pages ({len(added)})", f""]
    for url in added[:20]:  # cap at 20
        path = url_to_path(url)
        lm = current_urls.get(url, "")
        lm_str = f" (lastmod: {lm})" if lm else ""
        if path and (REPO_ROOT / path).exists():
            section_lines.append(f"- [{url}]({path}){lm_str}")
        else:
            section_lines.append(f"- `{url}`{lm_str}")
    if len(added) > 20:
        section_lines.append(f"- ...and {len(added)-20} more (see [analysis](runs/{RUN_ID}/analysis.md))")
    section_lines.append(f"")

# Notable updates
if updated:
    section_lines += [f"### Updated Pages ({len(updated)})", f""]
    for entry in updated[:20]:
        url = entry["url"]
        path = url_to_path(url)
        change_note = update_summaries.get(url, "lastmod updated")
        if path and (REPO_ROOT / path).exists():
            section_lines.append(f"- [{url}]({path}): {change_note[:120]}")
        else:
            section_lines.append(f"- `{url}`: {change_note[:120]}")
    if len(updated) > 20:
        section_lines.append(f"- ...and {len(updated)-20} more (see [analysis](runs/{RUN_ID}/analysis.md))")
    section_lines.append(f"")

# Removals
if removed:
    section_lines += [f"### Removed Pages ({len(removed)})", f""]
    for url in removed[:20]:
        section_lines.append(f"- `{url}` (last seen: {baseline_urls.get(url, 'unknown')})")
    if len(removed) > 20:
        section_lines.append(f"- ...and {len(removed)-20} more")
    section_lines.append(f"")

# Stats footer
section_lines += [
    f"---",
    f"*Stats: {len(current_urls)} total URLs | +{len(added)} added | ~{len(updated)} updated | -{len(removed)} removed | {len(anomalies)} anomalies | {len(sub_sitemap_urls)} sub-sitemaps*",
    f"",
    f"",
]

new_section = "\n".join(section_lines)

# Prepend to README
# Find the right insertion point - after any top-level header and intro
if "## 2026-" in existing_readme or "## 2025-" in existing_readme:
    # Find the first run section and insert before it
    import re
    match = re.search(r'^## \d{4}-\d{2}-\d{2}', existing_readme, re.MULTILINE)
    if match:
        insert_pos = match.start()
        new_readme = existing_readme[:insert_pos] + new_section + existing_readme[insert_pos:]
    else:
        new_readme = existing_readme + "\n" + new_section
else:
    new_readme = existing_readme + "\n" + new_section

readme_path.write_text(new_readme)
print(f"  Updated README.md")


# ─── STEP 9: Update state/known_urls.json ────────────────────────────────────

print(f"\nStep 9: Updating state/known_urls.json...")

# Update entries
for url in current_urls:
    lm = current_urls[url]
    if url not in known_urls:
        known_urls[url] = {
            "first_seen": RUN_ID,
            "last_seen": RUN_ID,
            "current_lastmod": lm,
            "lastmod_history": [{"run_id": RUN_ID, "lastmod": lm}] if lm else []
        }
    else:
        entry = known_urls[url]
        entry["last_seen"] = RUN_ID
        if lm and lm != entry.get("current_lastmod", ""):
            entry.setdefault("lastmod_history", []).append({"run_id": RUN_ID, "lastmod": lm})
            entry["current_lastmod"] = lm

# Note removed URLs (don't delete them, just stop updating last_seen)

known_urls_path.write_text(json.dumps(known_urls, indent=2, sort_keys=True))
print(f"  Updated {len(known_urls)} URL entries")


# ─── STEP 10: Write diff.json ─────────────────────────────────────────────────

print(f"\nStep 10: Writing diff.json...")

diff_data = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME,
    "baseline": "2026-06-07T09-15Z",
    "added": added,
    "removed": removed,
    "updated": updated,
    "anomalies": anomalies,
    "fetch_failures": fetch_failures
}

(run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2))
print(f"  Written: runs/{RUN_ID}/diff.json")

print(f"\n=== Pipeline complete ===")
print(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}, Anomalies: {len(anomalies)}")
