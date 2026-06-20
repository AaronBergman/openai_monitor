#!/usr/bin/env python3
"""
OpenAI Sitemap Monitor - Daily Run Script
Run ID: 2026-06-20T09-15Z
"""

import os
import json
import subprocess
import sys
import time
import difflib
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen, Request
from urllib.error import URLError

REPO_ROOT = Path("/home/user/openai_monitor")
RUN_ID = "2026-06-20T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def log(msg):
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {msg}", flush=True)

def fetch_xml(url, retries=3):
    """Fetch XML content with retries."""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SitemapMonitor/1.0)",
        "Accept": "application/xml,text/xml,*/*"
    }
    for attempt in range(retries):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise e

def parse_sitemap_index(xml_text):
    """Parse sitemap index to get sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    sitemaps = []
    for sitemap in root.findall("sm:sitemap", NS):
        loc = sitemap.findtext("sm:loc", namespaces=NS)
        lastmod = sitemap.findtext("sm:lastmod", namespaces=NS)
        if loc:
            sitemaps.append({"loc": loc, "lastmod": lastmod})
    return sitemaps

def parse_url_set(xml_text):
    """Parse a sub-sitemap to get URL entries."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url in root.findall("sm:url", NS):
        loc = url.findtext("sm:loc", namespaces=NS)
        lastmod = url.findtext("sm:lastmod", namespaces=NS)
        if loc:
            urls[loc] = lastmod  # may be None
    return urls

def sanitize_sub_sitemap_name(url):
    """Convert sub-sitemap URL to a filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> sitemap.xml_page.xml
    path = url.replace("https://openai.com/", "").rstrip("/").replace("/", "_")
    return path + ".xml"

def read_baseline():
    """Read all baseline URLs from sub/latest/ sitemaps."""
    baseline = {}  # url -> lastmod
    sub_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    if not sub_latest.exists():
        log("WARNING: No sub/latest/ found, starting fresh")
        return baseline
    for f in sub_latest.glob("*.xml"):
        try:
            content = f.read_text(encoding="utf-8")
            urls = parse_url_set(content)
            baseline.update(urls)
        except Exception as e:
            log(f"WARNING: Could not parse {f}: {e}")
    log(f"Baseline loaded: {len(baseline)} URLs from sub/latest/")
    return baseline

def get_url_path(url):
    """Call tools/url_path.py to get repo path."""
    result = subprocess.run(
        ["python", str(REPO_ROOT / "tools/url_path.py"), url],
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    return result.stdout.strip()

def fetch_page_to_md(url, output_path):
    """Fetch a page via html_to_md.py and return success/failure."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["python", str(REPO_ROOT / "tools/html_to_md.py"),
         "--url", url, "--output", str(output_path)],
        capture_output=True, text=True, cwd=str(REPO_ROOT),
        timeout=60
    )
    if result.returncode != 0:
        return False, f"Return code {result.returncode}: {result.stderr[:200]}"

    # Sanity check
    if output_path.exists():
        content = output_path.read_text(encoding="utf-8", errors="ignore")
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            return False, f"Blocked/empty response ({len(content)} chars)"
        return True, None
    return False, "Output file not created"

def get_prev_md(rel_path):
    """Get previous version of a markdown file from git."""
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{rel_path}"],
            capture_output=True, text=True, cwd=str(REPO_ROOT)
        )
        if result.returncode == 0:
            return result.stdout
    except Exception:
        pass
    return None

def diff_markdown(old_text, new_text):
    """Produce a unified diff summary."""
    if not old_text:
        return "[No previous version]"
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()
    diff = list(difflib.unified_diff(old_lines, new_lines, lineterm="", n=2))
    if not diff:
        return "[No substantive change detected]"
    return "\n".join(diff[:100])  # cap at 100 lines

def read_known_urls():
    """Read state/known_urls.json."""
    state_file = REPO_ROOT / "state/known_urls.json"
    if state_file.exists():
        return json.loads(state_file.read_text(encoding="utf-8"))
    return {}

def save_known_urls(data):
    state_file = REPO_ROOT / "state/known_urls.json"
    state_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def main():
    log(f"=== OpenAI Monitor Run: {RUN_ID} ===")
    log(f"Fetch time: {FETCH_TIME}")

    # Create run directory
    run_dir = REPO_ROOT / f"runs/{RUN_ID}"
    run_dir.mkdir(parents=True, exist_ok=True)

    # ── STEP 1: BASELINE ──
    log("Step 1: Reading baseline...")
    baseline = read_baseline()
    known_urls = read_known_urls()

    # ── STEP 2: FETCH + SNAPSHOT ──
    log("Step 2: Fetching sitemap index...")
    try:
        index_xml = fetch_xml(SITEMAP_INDEX_URL)
    except Exception as e:
        error_msg = f"FATAL: Could not fetch sitemap index: {e}"
        log(error_msg)
        analysis_path = run_dir / "analysis.md"
        analysis_path.write_text(f"# Run {RUN_ID}\n\n## FATAL ERROR\n\n{error_msg}\n\nFetch time: {FETCH_TIME}\n")
        # Update README with failure
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        new_entry = f"## {RUN_ID}\n\n**FATAL ERROR**: Could not fetch sitemap index. {e}\n\n---\n\n"
        (REPO_ROOT / "README.md").write_text(new_entry + readme, encoding="utf-8")
        return 1

    # Save index
    sitemap_dir = REPO_ROOT / "sitemaps/openai.com"
    sitemap_dir.mkdir(parents=True, exist_ok=True)
    (sitemap_dir / f"{RUN_ID}.xml").write_text(index_xml, encoding="utf-8")
    (sitemap_dir / "latest.xml").write_text(index_xml, encoding="utf-8")
    log("Saved root sitemap index")

    sub_sitemaps_meta = parse_sitemap_index(index_xml)
    log(f"Found {len(sub_sitemaps_meta)} sub-sitemaps")

    # Fetch sub-sitemaps (parallel, higher concurrency OK for XML)
    sub_dated_dir = REPO_ROOT / f"sitemaps/openai.com/sub/{RUN_ID}"
    sub_latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    sub_dated_dir.mkdir(parents=True, exist_ok=True)
    sub_latest_dir.mkdir(parents=True, exist_ok=True)

    current_urls = {}  # url -> lastmod
    url_to_subsitemap = {}  # url -> sub-sitemap name (for migration detection)
    fetch_errors = []

    def fetch_sub(meta):
        url = meta["loc"]
        name = sanitize_sub_sitemap_name(url)
        try:
            xml_text = fetch_xml(url)
            urls = parse_url_set(xml_text)
            return name, url, xml_text, urls, None
        except Exception as e:
            return name, url, None, {}, str(e)

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(fetch_sub, meta): meta for meta in sub_sitemaps_meta}
        for future in as_completed(futures):
            name, sub_url, xml_text, urls, error = future.result()
            if error:
                log(f"  ERROR fetching {sub_url}: {error}")
                fetch_errors.append({"url": sub_url, "error": error})
                continue

            (sub_dated_dir / name).write_text(xml_text, encoding="utf-8")
            (sub_latest_dir / name).write_text(xml_text, encoding="utf-8")

            for u, lm in urls.items():
                current_urls[u] = lm
                url_to_subsitemap[u] = name
            log(f"  Fetched {name}: {len(urls)} URLs")

    log(f"Total current URLs: {len(current_urls)}")

    # ── STEP 3: DIFF ──
    log("Step 3: Computing diff...")
    baseline_set = set(baseline.keys())
    current_set = set(current_urls.keys())

    added_urls = sorted(current_set - baseline_set)
    removed_urls = sorted(baseline_set - current_set)
    updated_urls = []
    for url in sorted(current_set & baseline_set):
        old_lm = baseline[url]
        new_lm = current_urls[url]
        if old_lm != new_lm:
            updated_urls.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

    log(f"Added: {len(added_urls)}, Removed: {len(removed_urls)}, Updated: {len(updated_urls)}")

    # ── STEP 4: ANOMALY DETECTION ──
    log("Step 4: Detecting anomalies...")
    anomalies = []
    fetch_time_dt = datetime.now(timezone.utc)

    # Check for future lastmod
    for url, lm in current_urls.items():
        if not lm:
            continue
        try:
            lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
            if lm_dt > fetch_time_dt:
                anomalies.append({
                    "kind": "future_lastmod",
                    "url": url,
                    "details": f"lastmod {lm} is after fetch time {FETCH_TIME}"
                })
        except ValueError:
            pass

    # Check lastmod moved backwards
    for item in updated_urls:
        url = item["url"]
        old_lm = item["old_lastmod"]
        new_lm = item["new_lastmod"]
        if old_lm and new_lm:
            try:
                old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
                new_dt = datetime.fromisoformat(new_lm.replace("Z", "+00:00"))
                if new_dt < old_dt:
                    anomalies.append({
                        "kind": "lastmod_moved_backwards",
                        "url": url,
                        "details": f"lastmod changed from {old_lm} to {new_lm} (went backwards)"
                    })
            except ValueError:
                pass

    # Check backdated new URLs
    for url in added_urls:
        lm = current_urls.get(url)
        if not lm:
            continue
        try:
            lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
            first_seen_dt = datetime.fromisoformat(RUN_ID.replace("T", "T").replace("-", ":").rsplit(":", 1)[0] + ":00+00:00") if False else fetch_time_dt
            delta_days = (first_seen_dt - lm_dt).days
            if delta_days > 7:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"New URL but lastmod={lm} predates first_seen by ~{delta_days} days"
                })
        except ValueError:
            pass

    # Check disappeared and reappeared URLs
    for url in added_urls:
        if url in known_urls and known_urls[url].get("last_seen"):
            last = known_urls[url]["last_seen"]
            if last != RUN_ID:
                anomalies.append({
                    "kind": "reappeared",
                    "url": url,
                    "details": f"URL was absent, last seen in run {last}, now reappeared"
                })

    log(f"Anomalies found: {len(anomalies)}")
    for a in anomalies:
        log(f"  [{a['kind']}] {a['url']}")

    # ── STEP 5: FETCH + CONVERT CHANGED PAGES ──
    log("Step 5: Fetching changed/new pages...")
    pages_to_fetch = []
    for url in added_urls:
        rel_path = get_url_path(url)
        if rel_path:
            pages_to_fetch.append(("added", url, rel_path))
    for item in updated_urls:
        rel_path = get_url_path(item["url"])
        if rel_path:
            pages_to_fetch.append(("updated", item["url"], rel_path))

    log(f"Pages to fetch: {len(pages_to_fetch)}")

    page_results = {}  # url -> {status, prev_md, new_md, diff, error}
    fetch_failures = list(fetch_errors)

    def process_page(kind, url, rel_path):
        abs_path = REPO_ROOT / rel_path
        prev_md = None
        if kind == "updated":
            prev_md = get_prev_md(rel_path)

        success, error = fetch_page_to_md(url, abs_path)
        if not success:
            return url, {"kind": kind, "rel_path": rel_path, "status": "failed", "error": error}

        new_md = abs_path.read_text(encoding="utf-8", errors="ignore") if abs_path.exists() else ""
        diff = diff_markdown(prev_md, new_md) if kind == "updated" else None
        return url, {"kind": kind, "rel_path": rel_path, "status": "ok",
                     "prev_md": prev_md, "new_md": new_md, "diff": diff}

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_page, kind, url, rel): (kind, url, rel)
                   for kind, url, rel in pages_to_fetch}
        done = 0
        for future in as_completed(futures):
            url, result = future.result()
            page_results[url] = result
            done += 1
            status = result["status"]
            if status == "failed":
                fetch_failures.append({"url": url, "error": result.get("error", "unknown")})
                log(f"  [{done}/{len(pages_to_fetch)}] FAILED {url}: {result.get('error')}")
            else:
                log(f"  [{done}/{len(pages_to_fetch)}] OK {url}")

    # ── STEP 6: ANALYZE ──
    log("Step 6: Analyzing changes...")

    def summarize_url(url):
        """Extract a short human label from URL."""
        path = url.replace("https://openai.com/", "").rstrip("/")
        return path if path else "(homepage)"

    # Build analysis text
    analysis_lines = [
        f"# Analysis: {RUN_ID}",
        f"",
        f"**Fetch time**: {FETCH_TIME}",
        f"**Baseline**: sub/latest/ (most recent prior run)",
        f"**Total current URLs**: {len(current_urls)}",
        f"**Added**: {len(added_urls)} | **Updated**: {len(updated_urls)} | **Removed**: {len(removed_urls)}",
        f"**Anomalies**: {len(anomalies)}",
        f"",
    ]

    if anomalies:
        analysis_lines += ["## Anomalies (Highest Signal)", ""]
        for a in anomalies:
            analysis_lines.append(f"- **[{a['kind']}]** `{a['url']}`")
            analysis_lines.append(f"  - {a['details']}")
        analysis_lines.append("")

    if fetch_failures:
        analysis_lines += ["## Fetch Failures", ""]
        for ff in fetch_failures:
            analysis_lines.append(f"- `{ff['url']}`: {ff.get('error', 'unknown')}")
        analysis_lines.append("")

    # Updated pages
    significant_updates = []
    routine_updates = []
    for item in updated_urls:
        url = item["url"]
        result = page_results.get(url, {})
        diff_text = result.get("diff", "")
        if diff_text and len(diff_text) > 50 and "[No substantive change]" not in diff_text:
            significant_updates.append((url, item, result))
        else:
            routine_updates.append((url, item, result))

    if significant_updates:
        analysis_lines += ["## Significant Updates", ""]
        for url, item, result in significant_updates:
            label = summarize_url(url)
            analysis_lines.append(f"### {label}")
            analysis_lines.append(f"- URL: {url}")
            analysis_lines.append(f"- lastmod: `{item['old_lastmod']}` → `{item['new_lastmod']}`")
            diff_text = result.get("diff", "")
            if diff_text:
                analysis_lines.append(f"- Diff (first 50 lines):")
                analysis_lines.append("```diff")
                analysis_lines.extend(diff_text.splitlines()[:50])
                analysis_lines.append("```")
            analysis_lines.append("")

    if routine_updates:
        analysis_lines += ["## Routine Updates", ""]
        for url, item, result in routine_updates:
            label = summarize_url(url)
            analysis_lines.append(f"- `{label}`: `{item['old_lastmod']}` → `{item['new_lastmod']}`")
        analysis_lines.append("")

    if added_urls:
        analysis_lines += ["## New Pages", ""]
        for url in added_urls:
            label = summarize_url(url)
            result = page_results.get(url, {})
            lm = current_urls.get(url)
            rel_path = result.get("rel_path", "")
            new_md = result.get("new_md", "")
            # Brief summary from first 200 chars of markdown
            summary = new_md[:300].replace("\n", " ").strip() if new_md else "[fetch failed]"
            analysis_lines.append(f"### {label}")
            analysis_lines.append(f"- URL: {url}")
            analysis_lines.append(f"- lastmod: {lm}")
            if rel_path:
                analysis_lines.append(f"- File: [{rel_path}]({rel_path})")
            analysis_lines.append(f"- Preview: {summary[:200]}...")
            analysis_lines.append("")

    if removed_urls:
        analysis_lines += ["## Removed Pages", ""]
        for url in removed_urls:
            label = summarize_url(url)
            analysis_lines.append(f"- `{label}`: {url}")
            analysis_lines.append(f"  - Last git record: `git log -- pages/openai.com/{label}.md` (or index.md)")
        analysis_lines.append("")

    analysis_text = "\n".join(analysis_lines)
    (run_dir / "analysis.md").write_text(analysis_text, encoding="utf-8")
    log("Written analysis.md")

    # ── STEP 7 ── (README update done in step 8 below)
    # ── STEP 8: UPDATE README ──
    log("Step 8: Updating README...")

    # Build README section
    tldr_parts = []
    if added_urls:
        tldr_parts.append(f"{len(added_urls)} new URL(s)")
    if updated_urls:
        tldr_parts.append(f"{len(updated_urls)} updated URL(s)")
    if removed_urls:
        tldr_parts.append(f"{len(removed_urls)} removed URL(s)")
    if anomalies:
        tldr_parts.append(f"{len(anomalies)} anomaly/anomalies")
    if not tldr_parts:
        tldr_parts.append("no changes detected")

    tldr = f"This run detected: {', '.join(tldr_parts)}."

    readme_section = [
        f"## {RUN_ID}",
        f"",
        f"**TL;DR**: {tldr}",
        f"",
    ]

    if anomalies:
        readme_section.append("### Anomalies")
        readme_section.append("")
        for a in anomalies:
            readme_section.append(f"- **[{a['kind']}]** `{a['url']}`: {a['details']}")
        readme_section.append("")

    if added_urls:
        readme_section.append("### New Pages")
        readme_section.append("")
        for url in added_urls[:20]:  # cap display
            label = summarize_url(url)
            rel_path = page_results.get(url, {}).get("rel_path", "")
            new_md = page_results.get(url, {}).get("new_md", "")
            # Get first meaningful line from markdown
            preview = ""
            for line in new_md.splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    preview = line[:120]
                    break
            if rel_path:
                readme_section.append(f"- [{label}]({rel_path}) — {preview}")
            else:
                readme_section.append(f"- `{label}` — {preview}")
        if len(added_urls) > 20:
            readme_section.append(f"- *(and {len(added_urls) - 20} more — see [analysis](runs/{RUN_ID}/analysis.md))*")
        readme_section.append("")

    if significant_updates:
        readme_section.append("### Notable Updates")
        readme_section.append("")
        for url, item, result in significant_updates[:10]:
            label = summarize_url(url)
            rel_path = result.get("rel_path", "")
            if rel_path:
                readme_section.append(f"- [{label}]({rel_path}): lastmod `{item['old_lastmod']}` → `{item['new_lastmod']}`")
            else:
                readme_section.append(f"- `{label}`: lastmod `{item['old_lastmod']}` → `{item['new_lastmod']}`")
        readme_section.append("")

    if removed_urls:
        readme_section.append("### Removed Pages")
        readme_section.append("")
        for url in removed_urls[:20]:
            label = summarize_url(url)
            readme_section.append(f"- `{label}`: {url}")
        readme_section.append("")

    readme_section += [
        f"### Stats",
        f"",
        f"- Total URLs: {len(current_urls)}",
        f"- Added: {len(added_urls)} | Updated: {len(updated_urls)} | Removed: {len(removed_urls)}",
        f"- Anomalies: {len(anomalies)} | Fetch failures: {len(fetch_failures)}",
        f"- Sub-sitemaps: {len(sub_sitemaps_meta)}",
        f"",
        f"See full analysis: [runs/{RUN_ID}/analysis.md](runs/{RUN_ID}/analysis.md)",
        f"",
        f"---",
        f"",
    ]

    readme_new_section = "\n".join(readme_section)

    readme_path = REPO_ROOT / "README.md"
    existing_readme = readme_path.read_text(encoding="utf-8")
    readme_path.write_text(readme_new_section + existing_readme, encoding="utf-8")
    log("Updated README.md")

    # ── STEP 9: UPDATE state/known_urls.json ──
    log("Step 9: Updating state/known_urls.json...")
    today = RUN_ID

    for url, lm in current_urls.items():
        if url not in known_urls:
            known_urls[url] = {
                "first_seen": today,
                "last_seen": today,
                "current_lastmod": lm,
                "lastmod_history": [{"run": today, "lastmod": lm}] if lm else []
            }
        else:
            entry = known_urls[url]
            entry["last_seen"] = today
            old_lm = entry.get("current_lastmod")
            if lm != old_lm:
                entry["current_lastmod"] = lm
                if "lastmod_history" not in entry:
                    entry["lastmod_history"] = []
                entry["lastmod_history"].append({"run": today, "lastmod": lm})

    save_known_urls(known_urls)
    log(f"State saved: {len(known_urls)} known URLs")

    # ── STEP 10: WRITE diff.json ──
    log("Step 10: Writing diff.json...")
    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": "sub/latest/",
        "added": added_urls,
        "removed": removed_urls,
        "updated": updated_urls,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures
    }
    (run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2, ensure_ascii=False), encoding="utf-8")
    log("Written diff.json")

    log("=== Run complete ===")
    log(f"Summary: {len(added_urls)} added, {len(updated_urls)} updated, {len(removed_urls)} removed, {len(anomalies)} anomalies")

    return {
        "added": len(added_urls),
        "updated": len(updated_urls),
        "removed": len(removed_urls),
        "anomalies": len(anomalies),
        "fetch_failures": len(fetch_failures),
        "total_urls": len(current_urls),
        "anomaly_list": anomalies,
        "added_sample": added_urls[:10],
        "removed_sample": removed_urls[:10],
    }

if __name__ == "__main__":
    result = main()
    print(json.dumps(result, indent=2))
