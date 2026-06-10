#!/usr/bin/env python3
"""
Daily monitoring script - 2026-06-10T09-15Z run.
Fetches sitemaps, diffs, fetches changed pages, updates state.
"""
import concurrent.futures
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import httpx

RUN_ID = "2026-06-10T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REPO_ROOT = Path("/home/user/openai_monitor")
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
MAX_PAGE_WORKERS = 8
# For large update batches, cap how many we fetch
MAX_UPDATED_FETCHES = 200

print(f"=== Run ID: {RUN_ID} ===")
print(f"=== Fetch time: {FETCH_TIME} ===")

# ─── Helpers ─────────────────────────────────────────────────────────────────

def fetch_xml(url, retries=4):
    delay = 2
    for attempt in range(retries + 1):
        try:
            r = httpx.get(url, timeout=30, follow_redirects=True,
                          headers={"User-Agent": "Mozilla/5.0 openai-sitemap-monitor/1.0"})
            r.raise_for_status()
            return r.text
        except Exception as e:
            if attempt == retries:
                raise
            print(f"  Retry {attempt+1}/{retries} for {url}: {e}")
            time.sleep(delay)
            delay *= 2

def sanitize_filename(url):
    parsed = urlparse(url)
    path = parsed.path.lstrip("/").replace("/", "_").rstrip("_")
    return f"{path}.xml"

def parse_sub_sitemap(text_or_path):
    if isinstance(text_or_path, str) and not text_or_path.strip().startswith("<"):
        tree = ET.parse(text_or_path)
        root = tree.getroot()
    else:
        content = text_or_path if isinstance(text_or_path, str) else text_or_path.read_text()
        root = ET.fromstring(content)
    result = {}
    for url_el in root.findall(f"{NS}url"):
        loc = url_el.findtext(f"{NS}loc", "").strip()
        lastmod = url_el.findtext(f"{NS}lastmod", "").strip()
        if loc:
            result[loc] = lastmod
    return result

def url_to_path(url):
    result = subprocess.run(
        ["python3", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()

def fetch_page(url):
    rel_path = url_to_path(url)
    if not rel_path:
        return url, None, "no_path"
    output_path = REPO_ROOT / rel_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            ["python3", "tools/html_to_md.py", "--url", url, "--output", str(output_path)],
            capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
        )
        if output_path.exists():
            content = output_path.read_text(encoding="utf-8")
            if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                return url, rel_path, f"blocked ({len(content)} chars)"
            return url, rel_path, None  # success
        return url, rel_path, f"no output file (rc={result.returncode})"
    except subprocess.TimeoutExpired:
        return url, rel_path, "timeout"
    except Exception as e:
        return url, rel_path, str(e)

# ─── STEP 1: Load baseline ───────────────────────────────────────────────────

print(f"\nStep 1: Loading baseline...")
baseline_urls = {}
sub_latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
baseline_files = sorted(sub_latest_dir.glob("*.xml"))
for f in baseline_files:
    try:
        baseline_urls.update(parse_sub_sitemap(f.read_text(encoding="utf-8")))
    except Exception as e:
        print(f"  WARNING: {f.name}: {e}")
print(f"  Baseline: {len(baseline_urls)} URLs from {len(baseline_files)} sub-sitemaps")

# Load known_urls for anomaly detection
known_urls_path = REPO_ROOT / "state/known_urls.json"
known_urls = {}
if known_urls_path.exists():
    known_urls = json.loads(known_urls_path.read_text(encoding="utf-8"))
print(f"  Known URLs in state: {len(known_urls)}")

# ─── STEP 2: Fetch & Snapshot sitemaps ───────────────────────────────────────

print(f"\nStep 2: Fetching sitemaps...")
sitemaps_dir = REPO_ROOT / "sitemaps/openai.com"
sub_run_dir = REPO_ROOT / f"sitemaps/openai.com/sub/{RUN_ID}"
sitemaps_dir.mkdir(parents=True, exist_ok=True)
sub_run_dir.mkdir(parents=True, exist_ok=True)
sub_latest_dir.mkdir(parents=True, exist_ok=True)

root_xml = fetch_xml("https://openai.com/sitemap.xml")
(sitemaps_dir / f"{RUN_ID}.xml").write_text(root_xml, encoding="utf-8")
(sitemaps_dir / "latest.xml").write_text(root_xml, encoding="utf-8")
print(f"  Saved root sitemap index")

root_tree = ET.fromstring(root_xml)
sub_sitemap_urls = [
    sm.findtext(f"{NS}loc", "").strip()
    for sm in root_tree.findall(f"{NS}sitemap")
    if sm.findtext(f"{NS}loc", "").strip()
]
print(f"  Found {len(sub_sitemap_urls)} sub-sitemaps")

current_urls = {}
for sub_url in sub_sitemap_urls:
    try:
        xml_content = fetch_xml(sub_url)
        fname = sanitize_filename(sub_url)
        (sub_run_dir / fname).write_text(xml_content, encoding="utf-8")
        (sub_latest_dir / fname).write_text(xml_content, encoding="utf-8")
        entries = parse_sub_sitemap(xml_content)
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
for url in sorted(baseline_set & current_set):
    old_lm = baseline_urls[url]
    new_lm = current_urls[url]
    if old_lm != new_lm:
        updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

print(f"  Added: {len(added)}")
print(f"  Removed: {len(removed)}")
print(f"  Updated: {len(updated)}")

# ─── STEP 4: Anomaly Detection ───────────────────────────────────────────────

print(f"\nStep 4: Anomaly detection...")
anomalies = []
fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except:
        return None

for url, lm in current_urls.items():
    dt = parse_dt(lm)
    if dt and dt > fetch_dt:
        anomalies.append({"kind": "future_lastmod", "url": url,
                           "details": f"lastmod {lm} is after fetch time {FETCH_TIME}"})

for entry in updated:
    old_dt = parse_dt(entry["old_lastmod"])
    new_dt = parse_dt(entry["new_lastmod"])
    if old_dt and new_dt and new_dt < old_dt:
        anomalies.append({"kind": "backwards_lastmod", "url": entry["url"],
                           "details": f"lastmod moved backwards: {entry['old_lastmod']} → {entry['new_lastmod']}"})

for url in added:
    lm = current_urls[url]
    lm_dt = parse_dt(lm)
    if lm_dt:
        run_dt = datetime.fromisoformat(RUN_ID[:10] + "T00:00:00+00:00")
        diff_days = (run_dt - lm_dt).days
        if diff_days > 7:
            anomalies.append({"kind": "backdated_new_url", "url": url,
                               "details": f"new URL has lastmod {lm} which predates first_seen {RUN_ID[:10]} by {diff_days} days"})

for url in added:
    if url in known_urls and known_urls[url].get("last_seen", "") < RUN_ID[:10]:
        prev_last = known_urls[url].get("last_seen", "unknown")
        anomalies.append({"kind": "reappeared_url", "url": url,
                           "details": f"URL previously seen (last_seen: {prev_last}) and reappeared"})

print(f"  Anomalies: {len(anomalies)}")

# ─── STEP 5: Fetch changed/new pages ─────────────────────────────────────────

print(f"\nStep 5: Fetching changed/new pages...")

# Capture prior content for updated pages before overwriting
prior_content = {}
for entry in updated:
    url = entry["url"]
    rel = url_to_path(url)
    if rel:
        full_path = REPO_ROOT / rel
        if full_path.exists():
            prior_content[url] = full_path.read_text(encoding="utf-8")

# Decide which pages to fetch:
# - All added pages (always)
# - Updated pages up to cap
urls_to_fetch_added = list(added)
urls_to_fetch_updated = [e["url"] for e in updated]

# If very large batch, note we're sampling
if len(urls_to_fetch_updated) > MAX_UPDATED_FETCHES:
    print(f"  NOTE: {len(urls_to_fetch_updated)} updated URLs, capping at {MAX_UPDATED_FETCHES}")
    urls_to_fetch_updated = urls_to_fetch_updated[:MAX_UPDATED_FETCHES]

all_urls_to_fetch = list(set(urls_to_fetch_added + urls_to_fetch_updated))
print(f"  Total pages to fetch: {len(all_urls_to_fetch)} (added={len(urls_to_fetch_added)}, updated sample={len(urls_to_fetch_updated)})")

fetch_failures = []
fetch_results = {}  # {url: rel_path}

def fetch_with_progress(url):
    return fetch_page(url)

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_PAGE_WORKERS) as executor:
    futures = {executor.submit(fetch_page, url): url for url in all_urls_to_fetch}
    completed = 0
    for future in concurrent.futures.as_completed(futures):
        url, rel_path, error = future.result()
        completed += 1
        if completed % 10 == 0 or completed == len(all_urls_to_fetch):
            print(f"  Progress: {completed}/{len(all_urls_to_fetch)} pages")
        if error:
            fetch_failures.append({"url": url, "error": error})
            if "blocked" not in error:
                print(f"  FAIL: {url}: {error}")
        else:
            fetch_results[url] = rel_path

print(f"  Fetched OK: {len(fetch_results)}, Failures: {len(fetch_failures)}")

# ─── STEP 6: Compute page diffs ──────────────────────────────────────────────

print(f"\nStep 6: Computing page diffs...")

def summarize_diff(old, new):
    if not old:
        return "[new page - no prior version]"
    old_lines = set(old.splitlines())
    new_lines = set(new.splitlines())
    added_lines = sorted([l for l in new_lines - old_lines if l.strip() and len(l.strip()) > 5])
    removed_lines = sorted([l for l in old_lines - new_lines if l.strip() and len(l.strip()) > 5])
    parts = []
    if added_lines:
        parts.append("Added: " + " | ".join(l[:80] for l in added_lines[:5]))
        if len(added_lines) > 5:
            parts[-1] += f" (+{len(added_lines)-5} more lines)"
    if removed_lines:
        parts.append("Removed: " + " | ".join(l[:80] for l in removed_lines[:5]))
        if len(removed_lines) > 5:
            parts[-1] += f" (+{len(removed_lines)-5} more lines)"
    if not parts:
        diff_len = len(new) - len(old)
        return f"Minor changes (content {'grew' if diff_len > 0 else 'shrank'} by {abs(diff_len)} chars)"
    return " | ".join(parts)

page_diffs = {}  # {url: diff_summary}
actual_changes = 0
for url in urls_to_fetch_updated:
    if url not in fetch_results:
        continue
    rel_path = fetch_results[url]
    full_path = REPO_ROOT / rel_path
    if not full_path.exists():
        continue
    new_content = full_path.read_text(encoding="utf-8")
    old_content = prior_content.get(url, "")
    if old_content and old_content != new_content:
        page_diffs[url] = summarize_diff(old_content, new_content)
        actual_changes += 1
    elif not old_content:
        page_diffs[url] = "[no prior version on disk]"

new_page_summaries = {}
for url in urls_to_fetch_added:
    if url not in fetch_results:
        continue
    rel_path = fetch_results[url]
    full_path = REPO_ROOT / rel_path
    if full_path.exists():
        content = full_path.read_text(encoding="utf-8")
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#") and not l.startswith("!")]
        summary = " ".join(lines[:5])[:400] if lines else "(no content)"
        new_page_summaries[url] = summary

print(f"  Updated pages with actual content changes: {actual_changes}/{len(urls_to_fetch_updated)} fetched")

# ─── Save run outputs ─────────────────────────────────────────────────────────

run_dir = REPO_ROOT / f"runs/{RUN_ID}"
run_dir.mkdir(parents=True, exist_ok=True)

# Write diff.json
diff_data = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME,
    "baseline": "2026-06-09T09-15Z",
    "added": added,
    "removed": removed,
    "updated": updated,
    "anomalies": anomalies,
    "fetch_failures": fetch_failures,
}
(run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nDiff.json written")

# Write analysis.md (basic structured version; will be enriched by Claude)
analysis_lines = [
    f"# Analysis: {RUN_ID}",
    f"",
    f"**Fetch time:** {FETCH_TIME}  ",
    f"**Total current URLs:** {len(current_urls)}  ",
    f"**Baseline URLs:** {len(baseline_urls)}  ",
    f"**Added:** {len(added)}  ",
    f"**Removed:** {len(removed)}  ",
    f"**Updated (sitemap lastmod):** {len(updated)}  ",
    f"**Pages with actual content changes:** {actual_changes}  ",
    f"**Anomalies:** {len(anomalies)}  ",
    f"**Fetch failures:** {len(fetch_failures)}  ",
    f"",
]

if anomalies:
    analysis_lines += ["## Anomalies", ""]
    for a in anomalies:
        analysis_lines.append(f"- **{a['kind']}** — `{a['url']}`  ")
        analysis_lines.append(f"  {a['details']}")
        analysis_lines.append(f"")
else:
    analysis_lines += ["## Anomalies", "", "None detected.", ""]

if added:
    analysis_lines += [f"## New Pages ({len(added)})", ""]
    for url in added:
        lm = current_urls.get(url, "")
        analysis_lines.append(f"### {url}")
        analysis_lines.append(f"- lastmod: `{lm}`")
        if url in new_page_summaries:
            analysis_lines.append(f"- Content preview: {new_page_summaries[url][:300]}")
        analysis_lines.append(f"")
else:
    analysis_lines += ["## New Pages", "", "None.", ""]

if updated:
    analysis_lines += [f"## Updated Pages ({len(updated)} total, {len(page_diffs)} with content changes)", ""]
    for entry in updated:
        url = entry["url"]
        analysis_lines.append(f"### {url}")
        analysis_lines.append(f"- lastmod: `{entry['old_lastmod']}` → `{entry['new_lastmod']}`")
        if url in page_diffs:
            analysis_lines.append(f"- Changes: {page_diffs[url][:400]}")
        analysis_lines.append(f"")
else:
    analysis_lines += ["## Updated Pages", "", "None.", ""]

if removed:
    analysis_lines += [f"## Removed Pages ({len(removed)})", ""]
    for url in removed:
        analysis_lines.append(f"- `{url}` (lastmod was `{baseline_urls.get(url, 'unknown')}`)")
    analysis_lines.append(f"")
else:
    analysis_lines += ["## Removed Pages", "", "None.", ""]

if fetch_failures:
    analysis_lines += [f"## Fetch Failures ({len(fetch_failures)})", ""]
    for ff in fetch_failures:
        analysis_lines.append(f"- `{ff['url']}`: {ff['error'][:200]}")
    analysis_lines.append(f"")

(run_dir / "analysis.md").write_text("\n".join(analysis_lines), encoding="utf-8")
print(f"Analysis.md written (basic)")

# ─── STEP 9: Update state/known_urls.json ────────────────────────────────────

print(f"\nStep 9: Updating state/known_urls.json...")
for url in current_urls:
    lm = current_urls[url]
    if url not in known_urls:
        known_urls[url] = {
            "first_seen": RUN_ID,
            "last_seen": RUN_ID,
            "current_lastmod": lm,
            "lastmod_history": [{"run_id": RUN_ID, "lastmod": lm}] if lm else [],
        }
    else:
        entry = known_urls[url]
        entry["last_seen"] = RUN_ID
        if lm and lm != entry.get("current_lastmod", ""):
            entry.setdefault("lastmod_history", []).append({"run_id": RUN_ID, "lastmod": lm})
            entry["current_lastmod"] = lm

known_urls_path.write_text(json.dumps(known_urls, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
print(f"  Updated {len(known_urls)} URL entries")

# ─── Summary ─────────────────────────────────────────────────────────────────

print(f"\n=== Pipeline complete ===")
print(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}, Anomalies: {len(anomalies)}")
print(f"Actual content changes: {actual_changes}")
print(f"Fetch failures: {len(fetch_failures)}")

# Save summary for Claude to use in README
summary = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME,
    "total_urls": len(current_urls),
    "baseline_urls": len(baseline_urls),
    "added": len(added),
    "removed": len(removed),
    "updated_sitemap": len(updated),
    "updated_actual": actual_changes,
    "anomalies": len(anomalies),
    "fetch_failures": len(fetch_failures),
    "added_urls": added,
    "removed_urls": removed,
    "updated_with_changes": list(page_diffs.keys())[:50],
    "new_page_summaries": new_page_summaries,
    "page_diffs_sample": {k: v for k, v in list(page_diffs.items())[:30]},
}
(run_dir / "pipeline_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Pipeline summary saved to runs/{RUN_ID}/pipeline_summary.json")
