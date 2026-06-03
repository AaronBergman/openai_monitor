#!/usr/bin/env python3
"""Full monitoring run for 2026-06-03T09-15Z."""

import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

import httpx

REPO = Path("/home/user/openai_monitor")
RUN_ID = "2026-06-03T09-15Z"
FETCH_TIME = datetime.now(timezone.utc)

SUB_LATEST = REPO / "sitemaps/openai.com/sub/latest"
SUB_SNAP = REPO / f"sitemaps/openai.com/sub/{RUN_ID}"
ROOT_LATEST = REPO / "sitemaps/openai.com/latest.xml"
ROOT_SNAP = REPO / f"sitemaps/openai.com/{RUN_ID}.xml"
PAGES_ROOT = REPO / "pages/openai.com"
STATE_FILE = REPO / "state/known_urls.json"
RUNS_DIR = REPO / f"runs/{RUN_ID}"

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

print(f"=== Run {RUN_ID} starting at {FETCH_TIME.isoformat()} ===")

# ── 0. Setup ──────────────────────────────────────────────────────────────────
SUB_SNAP.mkdir(parents=True, exist_ok=True)
RUNS_DIR.mkdir(parents=True, exist_ok=True)
PAGES_ROOT.mkdir(parents=True, exist_ok=True)


def sanitize_name(url: str) -> str:
    """Turn a sub-sitemap URL into a filename like openai.com_sitemap.xml_page.xml"""
    # Extract section from URL like https://openai.com/sitemap.xml/page/
    m = re.search(r'sitemap\.xml/([^/]+)/?$', url)
    if m:
        section = m.group(1)
        return f"openai.com_sitemap.xml_{section}.xml"
    # Fallback: strip scheme and sanitize
    clean = re.sub(r'https?://', '', url).rstrip('/')
    clean = re.sub(r'[^A-Za-z0-9._-]', '_', clean)
    return clean + ".xml"


def fetch_xml(url: str, timeout: float = 30.0) -> str:
    r = httpx.get(url, timeout=timeout, follow_redirects=True)
    r.raise_for_status()
    return r.text


def parse_urls_from_sitemap(xml_text: str) -> dict:
    """Returns {url: lastmod_or_None}"""
    result = {}
    try:
        root = ET.fromstring(xml_text)
        for url_el in root.findall(f"{{{NS}}}url"):
            loc = url_el.findtext(f"{{{NS}}}loc", "").strip()
            lastmod = url_el.findtext(f"{{{NS}}}lastmod", "").strip()
            if loc:
                result[loc] = lastmod or None
    except ET.ParseError as e:
        print(f"  [WARN] XML parse error: {e}")
    return result


def parse_sitemaps_from_index(xml_text: str) -> list:
    """Returns list of sub-sitemap URLs from sitemap index."""
    locs = []
    try:
        root = ET.fromstring(xml_text)
        for sm in root.findall(f"{{{NS}}}sitemap"):
            loc = sm.findtext(f"{{{NS}}}loc", "").strip()
            if loc:
                locs.append(loc)
    except ET.ParseError as e:
        print(f"  [WARN] XML parse error in index: {e}")
    return locs


# ── 1. Baseline ───────────────────────────────────────────────────────────────
print("\n[1] Loading baseline...")
baseline_urls: dict = {}  # {url: lastmod_or_None}

# Use only the canonical openai.com_sitemap.xml_*.xml files
canonical_pattern = re.compile(r'^openai\.com_sitemap\.xml_\w[\w.-]*\.xml$')
baseline_files = [f for f in SUB_LATEST.iterdir()
                  if canonical_pattern.match(f.name)]
print(f"  Found {len(baseline_files)} canonical baseline sub-sitemap files")

for bf in baseline_files:
    try:
        text = bf.read_text(encoding="utf-8")
        urls = parse_urls_from_sitemap(text)
        baseline_urls.update(urls)
    except Exception as e:
        print(f"  [WARN] Failed to read {bf.name}: {e}")

print(f"  Baseline: {len(baseline_urls)} URLs")

# ── 2. Fetch + Snapshot ───────────────────────────────────────────────────────
print("\n[2] Fetching sitemaps...")

# Fetch root index
print("  Fetching root sitemap index...")
try:
    root_xml = fetch_xml("https://openai.com/sitemap.xml")
except Exception as e:
    print(f"  [FATAL] Cannot fetch root sitemap: {e}")
    sys.exit(1)

ROOT_SNAP.write_text(root_xml, encoding="utf-8")
ROOT_LATEST.write_text(root_xml, encoding="utf-8")
print(f"  Saved root index to {ROOT_SNAP.name}")

sub_urls = parse_sitemaps_from_index(root_xml)
print(f"  Found {len(sub_urls)} sub-sitemaps")

# Fetch all sub-sitemaps
current_urls: dict = {}  # {url: lastmod_or_None}
sub_sitemap_sections: dict = {}  # {url: section_name}

def fetch_sub(sub_url):
    try:
        xml_text = fetch_xml(sub_url, timeout=30.0)
        urls = parse_urls_from_sitemap(xml_text)
        return sub_url, xml_text, urls, None
    except Exception as e:
        return sub_url, None, {}, str(e)

print(f"  Fetching {len(sub_urls)} sub-sitemaps concurrently...")
sub_results = {}
with ThreadPoolExecutor(max_workers=10) as ex:
    futures = {ex.submit(fetch_sub, u): u for u in sub_urls}
    for fut in as_completed(futures):
        sub_url, xml_text, urls, err = fut.result()
        if err:
            print(f"  [WARN] Failed to fetch {sub_url}: {err}")
        else:
            fname = sanitize_name(sub_url)
            snap_path = SUB_SNAP / fname
            latest_path = SUB_LATEST / fname
            snap_path.write_text(xml_text, encoding="utf-8")
            latest_path.write_text(xml_text, encoding="utf-8")
            sub_results[sub_url] = fname
            current_urls.update(urls)
            # Track which section each URL comes from
            for u in urls:
                sub_sitemap_sections[u] = fname

print(f"  Current total: {len(current_urls)} URLs across {len(sub_results)} sub-sitemaps")

FETCH_TIME = datetime.now(timezone.utc)

# ── 3. Diff ───────────────────────────────────────────────────────────────────
print("\n[3] Computing diff...")
baseline_set = set(baseline_urls.keys())
current_set = set(current_urls.keys())

added_urls = sorted(current_set - baseline_set)
removed_urls = sorted(baseline_set - current_set)
updated_entries = []
for url in sorted(current_set & baseline_set):
    old_lm = baseline_urls.get(url)
    new_lm = current_urls.get(url)
    if old_lm != new_lm:
        updated_entries.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

print(f"  Added: {len(added_urls)}")
print(f"  Removed: {len(removed_urls)}")
print(f"  Updated: {len(updated_entries)}")

# ── 4. Anomaly Detection ──────────────────────────────────────────────────────
print("\n[4] Detecting anomalies...")
anomalies = []

for url in current_set:
    lm = current_urls.get(url)
    if not lm:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
    except ValueError:
        continue

    # Future lastmod
    if lm_dt > FETCH_TIME:
        anomalies.append({
            "kind": "future_lastmod",
            "url": url,
            "details": f"lastmod {lm} is after fetch time {FETCH_TIME.isoformat()}"
        })

    # Backwards lastmod (lastmod went backward vs baseline)
    old_lm = baseline_urls.get(url)
    if old_lm:
        try:
            old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
            if lm_dt < old_dt:
                anomalies.append({
                    "kind": "backwards_lastmod",
                    "url": url,
                    "details": f"lastmod moved backward from {old_lm} to {lm}"
                })
        except ValueError:
            pass

# Load state for appeared/disappeared check
try:
    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
except Exception:
    state = {}

for url in added_urls:
    lm = current_urls.get(url)
    # Check backdating: if URL is "new" but lastmod is much older
    if lm:
        try:
            lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
            # first_seen would be today; if lastmod is > 7 days old, flag it
            age_days = (FETCH_TIME - lm_dt).days
            if age_days > 7:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"New URL with lastmod {lm} which is {age_days} days old"
                })
        except ValueError:
            pass

    # Check reappearance
    if url in state and state[url].get("last_seen"):
        prev_last_seen = state[url]["last_seen"]
        anomalies.append({
            "kind": "reappeared_url",
            "url": url,
            "details": f"URL disappeared then reappeared; last seen {prev_last_seen}"
        })

print(f"  Anomalies: {len(anomalies)}")
for a in anomalies:
    print(f"    [{a['kind']}] {a['url']}: {a['details']}")

# ── 5. Fetch + Convert Changed/New Pages ─────────────────────────────────────
print("\n[5] Fetching changed and new pages...")

def url_to_repo_path(url: str) -> str:
    parts = urlsplit(url)
    host = parts.netloc.lower()
    path = parts.path or "/"
    trailing_slash = path.endswith("/")
    segments = [s for s in path.split("/") if s]
    if not segments:
        return f"pages/{host}/index.md"
    safe = [re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("._") or "_" for s in segments]
    if trailing_slash:
        return f"pages/{host}/" + "/".join(safe) + "/index.md"
    return f"pages/{host}/" + "/".join(safe) + ".md"


pages_to_fetch = []
for url in added_urls:
    pages_to_fetch.append(("added", url))
for entry in updated_entries:
    pages_to_fetch.append(("updated", entry["url"]))

print(f"  {len(pages_to_fetch)} pages to fetch (added + updated)")

fetch_failures = []
content_changes = []  # (url, old_md_path_or_none, new_md)

def fetch_page(kind_url):
    kind, url = kind_url
    rel_path = url_to_repo_path(url)
    abs_path = REPO / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Capture prior markdown before overwriting
    prior_md = None
    if abs_path.exists():
        prior_md = abs_path.read_text(encoding="utf-8", errors="replace")

    # Fetch via html_to_md.py
    tmp_out = f"/tmp/page_{abs_path.stem}_{hash(url) & 0xFFFFFF}.md"
    result = subprocess.run(
        [sys.executable, str(REPO / "tools/html_to_md.py"), "--url", url, "--output", tmp_out],
        capture_output=True, text=True, timeout=60
    )

    if result.returncode != 0:
        return kind, url, rel_path, None, f"html_to_md failed: {result.stderr[:200]}"

    if not os.path.exists(tmp_out):
        return kind, url, rel_path, None, "Output file not created"

    new_md = open(tmp_out, encoding="utf-8", errors="replace").read()
    os.unlink(tmp_out)

    # Sanity check
    if len(new_md) < 100 or "Enable JavaScript and cookies to continue" in new_md:
        return kind, url, rel_path, None, f"Fetch blocked (len={len(new_md)})"

    abs_path.write_text(new_md, encoding="utf-8")
    return kind, url, rel_path, (prior_md, new_md), None


MAX_WORKERS = 8
processed = 0
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
    futures = {ex.submit(fetch_page, item): item for item in pages_to_fetch}
    for fut in as_completed(futures):
        processed += 1
        kind, url, rel_path, change_pair, err = fut.result()
        if processed % 50 == 0:
            print(f"  ... {processed}/{len(pages_to_fetch)} done")
        if err:
            fetch_failures.append({"url": url, "error": err})
        elif change_pair:
            prior_md, new_md = change_pair
            if prior_md != new_md:
                content_changes.append((kind, url, rel_path, prior_md, new_md))

print(f"  Fetch failures: {len(fetch_failures)}")
print(f"  Content changes: {len(content_changes)}")
for f in fetch_failures[:10]:
    print(f"    FAIL: {f['url']}: {f['error']}")

# ── 6. Analyze Content Changes ────────────────────────────────────────────────
print("\n[6] Analyzing changes...")

def summarize_diff(url, kind, prior_md, new_md):
    """Produce a brief summary of what changed."""
    if kind == "added" or prior_md is None:
        lines = new_md.splitlines()
        # Find title
        title = next((l.lstrip("# ").strip() for l in lines if l.startswith("#")), "")
        return f"NEW PAGE: {title or url}"

    prior_lines = set(prior_md.splitlines())
    new_lines = set(new_md.splitlines())
    added_lines = [l for l in new_md.splitlines() if l.strip() and l not in prior_lines]
    removed_lines = [l for l in prior_md.splitlines() if l.strip() and l not in new_lines]

    added_sample = " | ".join(added_lines[:3])[:200]
    removed_sample = " | ".join(removed_lines[:3])[:200]
    return f"+{len(added_lines)} lines / -{len(removed_lines)} lines. Added: {added_sample!r}. Removed: {removed_sample!r}"


change_summaries = []
for kind, url, rel_path, prior_md, new_md in content_changes:
    summary = summarize_diff(url, kind, prior_md, new_md)
    change_summaries.append((kind, url, rel_path, summary))

# ── 7. Write analysis.md ──────────────────────────────────────────────────────
print("\n[7] Writing analysis...")

analysis_lines = [
    f"# Analysis — {RUN_ID}",
    "",
    f"**Fetch time:** {FETCH_TIME.strftime('%Y-%m-%dT%H:%M:%SZ')}",
    f"**Baseline:** 2026-06-01T09-15Z",
    f"**Total current URLs:** {len(current_urls)}",
    "",
    "## Summary",
    f"- Added: {len(added_urls)} URLs",
    f"- Updated: {len(updated_entries)} URLs (sitemap lastmod changed)",
    f"- Removed: {len(removed_urls)} URLs",
    f"- Anomalies: {len(anomalies)}",
    f"- Content changes (actual markdown diff): {len(content_changes)}",
    f"- Fetch failures: {len(fetch_failures)}",
    "",
]

# Anomalies section
analysis_lines += ["## Anomalies", ""]
if anomalies:
    for a in anomalies:
        analysis_lines.append(f"- **[{a['kind']}]** `{a['url']}`")
        analysis_lines.append(f"  - {a['details']}")
        analysis_lines.append("")
else:
    analysis_lines += ["None detected.", ""]

# Content changes
analysis_lines += ["## Content Changes", ""]
if change_summaries:
    for kind, url, rel_path, summary in change_summaries:
        analysis_lines.append(f"### [{kind.upper()}] {url}")
        analysis_lines.append(f"**Path:** `{rel_path}`")
        analysis_lines.append("")
        analysis_lines.append(summary)
        analysis_lines.append("")
else:
    analysis_lines += ["No substantive content changes detected among fetched pages.", ""]

# New pages
analysis_lines += ["## New Pages", ""]
if added_urls:
    for url in added_urls:
        rel = url_to_repo_path(url)
        lm = current_urls.get(url, "")
        analysis_lines.append(f"- `{url}` (lastmod: {lm})")
        analysis_lines.append(f"  - Path: `{rel}`")
        analysis_lines.append("")
else:
    analysis_lines += ["None.", ""]

# Removed pages
analysis_lines += ["## Removed Pages", ""]
if removed_urls:
    for url in removed_urls:
        analysis_lines.append(f"- `{url}`")
    analysis_lines.append("")
else:
    analysis_lines += ["None.", ""]

# Fetch failures
analysis_lines += ["## Fetch Failures", ""]
if fetch_failures:
    for f in fetch_failures:
        analysis_lines.append(f"- `{f['url']}`: {f['error']}")
    analysis_lines.append("")
else:
    analysis_lines += ["None.", ""]

# Notable updated URLs (top 10 by most interesting)
analysis_lines += ["## Updated URLs (lastmod changed)", ""]
if updated_entries:
    analysis_lines.append(f"Total: {len(updated_entries)} URLs had lastmod changes.")
    analysis_lines.append("")
    analysis_lines.append("Sample (first 20):")
    for e in updated_entries[:20]:
        analysis_lines.append(f"- `{e['url']}`  {e['old_lastmod']} → {e['new_lastmod']}")
    analysis_lines.append("")
else:
    analysis_lines += ["None.", ""]

RUNS_DIR.joinpath("analysis.md").write_text("\n".join(analysis_lines), encoding="utf-8")
print(f"  Wrote {RUNS_DIR}/analysis.md")

# ── 8. Update README.md ───────────────────────────────────────────────────────
print("\n[8] Updating README.md...")

readme_path = REPO / "README.md"
existing_readme = readme_path.read_text(encoding="utf-8")

# Determine notable items for the README
notable_added = added_urls[:10]
notable_removed = removed_urls[:10]
# Pick content changes that are most interesting
notable_changes = change_summaries[:5]

fetch_time_str = FETCH_TIME.strftime('%Y-%m-%d %H:%M UTC')

new_section_lines = [
    f"## {RUN_ID}",
    f"*Fetched: {fetch_time_str} | Baseline: 2026-06-01T09-15Z*",
    "",
]

# TL;DR paragraph
if len(added_urls) == 0 and len(removed_urls) == 0 and len(updated_entries) == 0:
    tldr = "No changes detected vs the June 1 baseline."
elif len(added_urls) > 0 or len(removed_urls) > 0:
    parts = []
    if added_urls:
        parts.append(f"{len(added_urls)} new URL{'s' if len(added_urls)>1 else ''} added")
    if removed_urls:
        parts.append(f"{len(removed_urls)} URL{'s' if len(removed_urls)>1 else ''} removed")
    if updated_entries:
        parts.append(f"{len(updated_entries)} URL{'s' if len(updated_entries)>1 else ''} had lastmod updates")
    tldr = "Today's run detected " + ", ".join(parts) + "."
    if len(content_changes) > 0:
        tldr += f" {len(content_changes)} page{'s' if len(content_changes)>1 else ''} had substantive content changes."
else:
    tldr = f"{len(updated_entries)} URLs had sitemap lastmod timestamp updates"
    if len(content_changes) > 0:
        tldr += f"; {len(content_changes)} had actual content changes"
    tldr += "."

new_section_lines += [f"**TL;DR:** {tldr}", ""]

# Anomalies
if anomalies:
    new_section_lines += ["### Anomalies", ""]
    for a in anomalies:
        new_section_lines.append(f"- **{a['kind']}**: `{a['url']}` — {a['details']}")
    new_section_lines.append("")
else:
    new_section_lines += ["**Anomalies:** None.", ""]

# Notable additions
if notable_added:
    new_section_lines += ["### New Pages", ""]
    for url in notable_added:
        rel = url_to_repo_path(url)
        lm = current_urls.get(url, "")
        new_section_lines.append(f"- [{url}]({rel}) (lastmod: {lm})")
    if len(added_urls) > 10:
        new_section_lines.append(f"- *…and {len(added_urls)-10} more. See [analysis]({RUNS_DIR.relative_to(REPO)}/analysis.md).*")
    new_section_lines.append("")

# Notable content changes
if notable_changes:
    new_section_lines += ["### Content Changes", ""]
    for kind, url, rel_path, summary in notable_changes:
        new_section_lines.append(f"- **{url}** ([{rel_path}]({rel_path}))")
        new_section_lines.append(f"  - {summary[:300]}")
        new_section_lines.append("")

# Removals
if notable_removed:
    new_section_lines += ["### Removed Pages", ""]
    for url in notable_removed:
        new_section_lines.append(f"- `{url}`")
    if len(removed_urls) > 10:
        new_section_lines.append(f"- *…and {len(removed_urls)-10} more.*")
    new_section_lines.append("")

# Stats footer
new_section_lines += [
    f"*Stats: {len(current_urls)} total URLs | +{len(added_urls)} added | "
    f"~{len(updated_entries)} updated | -{len(removed_urls)} removed | "
    f"{len(anomalies)} anomalies | {len(sub_results)} sub-sitemaps*",
    "",
    "---",
    "",
]

new_section = "\n".join(new_section_lines)

# Prepend to README (insert after the main header)
if existing_readme.startswith("# "):
    # Find end of header lines
    lines = existing_readme.split("\n")
    insert_at = 1
    for i, l in enumerate(lines[1:], 1):
        if l.startswith("## ") or l.startswith("---"):
            insert_at = i
            break
        elif l.strip() == "":
            continue
        else:
            insert_at = i
            break

    # Actually just prepend after the first blank line after the H1
    header_end = existing_readme.find("\n\n")
    if header_end == -1:
        updated_readme = new_section + "\n" + existing_readme
    else:
        updated_readme = existing_readme[:header_end+2] + new_section + existing_readme[header_end+2:]
else:
    updated_readme = new_section + "\n" + existing_readme

readme_path.write_text(updated_readme, encoding="utf-8")
print("  Updated README.md")

# ── 9. Update state/known_urls.json ──────────────────────────────────────────
print("\n[9] Updating state...")

today = RUN_ID

for url in current_set:
    lm = current_urls.get(url)
    if url in state:
        state[url]["last_seen"] = today
        if lm and lm != state[url].get("current_lastmod"):
            state[url].setdefault("lastmod_history", [])
            old = state[url].get("current_lastmod")
            if old:
                state[url]["lastmod_history"].append({"run": today, "from": old, "to": lm})
            state[url]["current_lastmod"] = lm
    else:
        state[url] = {
            "first_seen": today,
            "last_seen": today,
            "current_lastmod": lm,
            "lastmod_history": []
        }

# Mark removed URLs (don't delete, just don't update last_seen)
# They'll be identifiable as last_seen < today

STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"  State: {len(state)} URLs total")

# ── 10. Write diff.json ───────────────────────────────────────────────────────
print("\n[10] Writing diff.json...")

diff = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME.strftime('%Y-%m-%dT%H:%M:%SZ'),
    "baseline": "2026-06-01T09-15Z",
    "added": added_urls,
    "removed": removed_urls,
    "updated": updated_entries,
    "anomalies": anomalies,
    "fetch_failures": fetch_failures,
}
RUNS_DIR.joinpath("diff.json").write_text(json.dumps(diff, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"  Wrote diff.json")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n=== DONE ===")
print(f"Added: {len(added_urls)}, Updated: {len(updated_entries)}, Removed: {len(removed_urls)}, "
      f"Anomalies: {len(anomalies)}, Failures: {len(fetch_failures)}, Content changes: {len(content_changes)}")
