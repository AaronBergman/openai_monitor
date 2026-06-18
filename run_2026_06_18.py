#!/usr/bin/env python3
"""
Monitoring run for 2026-06-18
"""

import os
import json
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
import subprocess
import shutil
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
RUN_ID = "2026-06-18T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REPO_ROOT = Path("/home/user/openai_monitor")
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Directories
SITEMAPS_DIR = REPO_ROOT / "sitemaps" / "openai.com"
SUB_LATEST_DIR = SITEMAPS_DIR / "sub" / "latest"
SUB_RUN_DIR = SITEMAPS_DIR / "sub" / RUN_ID
PAGES_DIR = REPO_ROOT / "pages" / "openai.com"
RUNS_DIR = REPO_ROOT / "runs" / RUN_ID
STATE_FILE = REPO_ROOT / "state" / "known_urls.json"

def ensure_dirs():
    SUB_RUN_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

def fetch_xml(url):
    """Fetch XML using standard urllib (sitemaps don't need curl-cffi)."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; SitemapMonitor/1.0)"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")

def parse_sitemap_index(xml_text):
    """Parse sitemap index, return list of sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    urls = []
    for sitemap in root.findall("sm:sitemap", NS):
        loc = sitemap.findtext("sm:loc", namespaces=NS)
        if loc:
            urls.append(loc.strip())
    return urls

def parse_sub_sitemap(xml_text):
    """Parse sub-sitemap, return dict of {url: lastmod}."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url_el in root.findall("sm:url", NS):
        loc = url_el.findtext("sm:loc", namespaces=NS)
        lastmod = url_el.findtext("sm:lastmod", namespaces=NS)
        if loc:
            urls[loc.strip()] = (lastmod.strip() if lastmod else None)
    return urls

def sanitize_name(url):
    """Convert sub-sitemap URL to filename."""
    # e.g. https://openai.com/sitemap.xml/api/ -> sitemap.xml_api.xml
    path = url.replace("https://openai.com/", "").rstrip("/")
    path = path.replace("/", "_")
    if not path.endswith(".xml"):
        path += ".xml"
    return path

def get_url_path(url):
    """Get local path for a page URL using tools/url_path.py."""
    result = subprocess.run(
        ["python3", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()

def fetch_page(url, output_path):
    """Fetch page and convert to markdown using html_to_md.py."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["python3", "tools/html_to_md.py", "--url", url, "--output", str(output_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    return result.returncode == 0

def load_baseline():
    """Load baseline from sub/latest/*.xml and latest.xml."""
    baseline = {}
    latest_dir = SITEMAPS_DIR / "sub" / "latest"
    if latest_dir.exists():
        for f in latest_dir.glob("*.xml"):
            try:
                text = f.read_text(encoding="utf-8")
                urls = parse_sub_sitemap(text)
                baseline.update(urls)
            except Exception as e:
                print(f"  Warning: could not parse {f}: {e}")
    return baseline

def load_known_urls():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}

def save_known_urls(data):
    STATE_FILE.write_text(json.dumps(data, indent=2, sort_keys=True))

def main():
    print(f"=== OpenAI Sitemap Monitor Run: {RUN_ID} ===")
    print(f"Fetch time: {FETCH_TIME}")
    ensure_dirs()

    # --- STEP 1: BASELINE ---
    print("\n[1] Loading baseline...")
    baseline = load_baseline()
    print(f"  Baseline: {len(baseline)} URLs")

    # --- STEP 2: FETCH + SNAPSHOT ---
    print("\n[2] Fetching sitemap index...")
    index_xml = fetch_xml(SITEMAP_INDEX_URL)

    # Save root index
    run_index_path = SITEMAPS_DIR / f"{RUN_ID}.xml"
    run_index_path.write_text(index_xml)
    (SITEMAPS_DIR / "latest.xml").write_text(index_xml)

    sub_sitemap_urls = parse_sitemap_index(index_xml)
    print(f"  Found {len(sub_sitemap_urls)} sub-sitemaps")

    # Fetch all sub-sitemaps
    print("  Fetching sub-sitemaps...")
    current = {}  # {url: lastmod}
    url_to_subsitemap = {}  # {url: sub-sitemap-name}
    fetch_failures = []

    for sub_url in sub_sitemap_urls:
        try:
            xml_text = fetch_xml(sub_url)
            name = sanitize_name(sub_url)

            # Save to run dir
            (SUB_RUN_DIR / name).write_text(xml_text)
            # Overwrite latest
            (SUB_LATEST_DIR / name).write_text(xml_text)

            urls = parse_sub_sitemap(xml_text)
            for u, lm in urls.items():
                current[u] = lm
                url_to_subsitemap[u] = name
            print(f"    {name}: {len(urls)} URLs")
        except Exception as e:
            print(f"    ERROR fetching {sub_url}: {e}")
            fetch_failures.append({"url": sub_url, "error": str(e)})

    print(f"  Total current URLs: {len(current)}")

    # --- STEP 3: DIFF ---
    print("\n[3] Computing diff...")
    baseline_set = set(baseline.keys())
    current_set = set(current.keys())

    added = sorted(current_set - baseline_set)
    removed = sorted(baseline_set - current_set)
    updated = []
    for url in current_set & baseline_set:
        old_lm = baseline.get(url)
        new_lm = current.get(url)
        if old_lm != new_lm:
            updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})
    updated.sort(key=lambda x: x["url"])

    print(f"  Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}")

    # --- STEP 4: ANOMALY DETECTION ---
    print("\n[4] Checking for anomalies...")
    anomalies = []
    known_urls = load_known_urls()

    for url, lm in current.items():
        if not lm:
            continue
        try:
            lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
            fetch_dt = datetime.now(timezone.utc)

            # Future lastmod
            if lm_dt > fetch_dt:
                anomalies.append({
                    "kind": "future_lastmod",
                    "url": url,
                    "details": f"lastmod {lm} is in the future (fetch time {FETCH_TIME})"
                })

            # Backwards lastmod
            if url in baseline and baseline[url]:
                old_lm = baseline[url]
                try:
                    old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
                    if lm_dt < old_dt:
                        anomalies.append({
                            "kind": "backwards_lastmod",
                            "url": url,
                            "details": f"lastmod moved backwards: {old_lm} -> {lm}"
                        })
                except:
                    pass
        except:
            pass

    # New URLs with backdated lastmod
    for url in added:
        lm = current.get(url)
        if not lm:
            continue
        try:
            lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
            run_dt = datetime.fromisoformat(RUN_ID.replace("T", " ").replace("-", ":").rsplit(":", 1)[0] + ":00+00:00")
            # If lastmod is more than 7 days before first_seen
            delta = (run_dt - lm_dt).days
            if delta > 7:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"New URL with lastmod {lm} predates first_seen by {delta} days"
                })
        except:
            pass

    # Check for URLs that disappeared and reappeared
    for url in added:
        if url in known_urls:
            ls = known_urls[url].get("last_seen", "")
            if ls and ls < "2026-06-17":
                anomalies.append({
                    "kind": "reappeared_url",
                    "url": url,
                    "details": f"URL previously seen (last_seen: {ls}), now reappeared"
                })

    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies[:5]:
        print(f"    {a['kind']}: {a['url'][:80]}")

    # --- STEP 5: FETCH + CONVERT CHANGED/NEW PAGES ---
    print("\n[5] Fetching changed/new pages...")
    urls_to_fetch = list(added) + [u["url"] for u in updated]
    print(f"  Pages to fetch: {len(urls_to_fetch)}")

    page_fetch_failures = []
    prev_contents = {}

    # Capture prior content for updated pages before overwriting
    for item in updated:
        url = item["url"]
        rel_path = get_url_path(url)
        if rel_path:
            full_path = REPO_ROOT / rel_path
            if full_path.exists():
                try:
                    result = subprocess.run(
                        ["git", "show", f"HEAD:{rel_path}"],
                        capture_output=True, text=True, cwd=REPO_ROOT
                    )
                    if result.returncode == 0:
                        prev_contents[url] = result.stdout
                except:
                    pass

    def fetch_one(url):
        rel_path = get_url_path(url)
        if not rel_path:
            return url, False, "could not determine path"
        full_path = REPO_ROOT / rel_path
        try:
            ok = fetch_page(url, full_path)
            if ok:
                content = full_path.read_text(encoding="utf-8", errors="replace")
                if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                    return url, False, "blocked by Cloudflare (content too short or challenge page)"
            return url, ok, None
        except subprocess.TimeoutExpired:
            return url, False, "timeout"
        except Exception as e:
            return url, False, str(e)

    fetch_results = {}
    MAX_WORKERS = 8

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(fetch_one, url): url for url in urls_to_fetch}
        done = 0
        for future in as_completed(futures):
            url, ok, err = future.result()
            fetch_results[url] = (ok, err)
            done += 1
            if done % 10 == 0:
                print(f"    {done}/{len(urls_to_fetch)} fetched...")
            if not ok:
                page_fetch_failures.append({"url": url, "error": err or "unknown"})

    success_count = sum(1 for ok, _ in fetch_results.values() if ok)
    print(f"  Fetched successfully: {success_count}/{len(urls_to_fetch)}")
    print(f"  Fetch failures: {len(page_fetch_failures)}")

    # --- STEP 6: ANALYZE CHANGES ---
    print("\n[6] Analyzing changes...")

    analyses = {}

    # Analyze updated pages
    for item in updated:
        url = item["url"]
        ok, err = fetch_results.get(url, (False, "not fetched"))
        if not ok:
            continue

        rel_path = get_url_path(url)
        if not rel_path:
            continue
        full_path = REPO_ROOT / rel_path

        if url in prev_contents and full_path.exists():
            prev = prev_contents[url]
            curr = full_path.read_text(encoding="utf-8", errors="replace")
            if prev != curr:
                # Simple diff analysis
                prev_lines = set(prev.splitlines())
                curr_lines = set(curr.splitlines())
                added_lines = [l for l in curr_lines - prev_lines if l.strip()]
                removed_lines = [l for l in prev_lines - curr_lines if l.strip()]
                analyses[url] = {
                    "added_lines": len(added_lines),
                    "removed_lines": len(removed_lines),
                    "sample_added": added_lines[:3],
                    "sample_removed": removed_lines[:3]
                }

    # Analyze new pages
    new_page_summaries = {}
    for url in added:
        ok, err = fetch_results.get(url, (False, "not fetched"))
        if not ok:
            continue
        rel_path = get_url_path(url)
        if not rel_path:
            continue
        full_path = REPO_ROOT / rel_path
        if full_path.exists():
            content = full_path.read_text(encoding="utf-8", errors="replace")
            # Extract first 500 chars as summary
            lines = [l.strip() for l in content.splitlines() if l.strip()]
            new_page_summaries[url] = "\n".join(lines[:10])

    # --- STEP 7: WRITE ANALYSIS ---
    print("\n[7] Writing analysis...")

    analysis_lines = [
        f"# Run Analysis: {RUN_ID}",
        f"",
        f"**Fetch time:** {FETCH_TIME}",
        f"**Baseline:** 2026-06-17T09-15Z",
        f"**Total current URLs:** {len(current)}",
        f"",
    ]

    # Anomalies first
    analysis_lines += [
        "## Anomalies",
        "",
    ]
    if anomalies:
        for a in anomalies:
            analysis_lines.append(f"### {a['kind']}: {a['url'][:80]}")
            analysis_lines.append(f"  - {a['details']}")
            analysis_lines.append("")
    else:
        analysis_lines.append("No anomalies detected.")
        analysis_lines.append("")

    # Significant updates
    analysis_lines += [
        "## Updated Pages",
        f"",
        f"Total: {len(updated)} URLs with changed lastmod.",
        "",
    ]

    significant_updates = [(url, info) for url, info in analyses.items()
                           if info['added_lines'] + info['removed_lines'] > 5]

    if significant_updates:
        analysis_lines.append("### Significant Changes:")
        for url, info in significant_updates[:20]:
            analysis_lines.append(f"- **{url}**")
            analysis_lines.append(f"  - +{info['added_lines']} lines, -{info['removed_lines']} lines")
            if info['sample_added']:
                analysis_lines.append(f"  - Added: `{info['sample_added'][0][:80]}`")
            if info['sample_removed']:
                analysis_lines.append(f"  - Removed: `{info['sample_removed'][0][:80]}`")
        analysis_lines.append("")

    # Group updated by sub-sitemap
    subsitemap_counts = {}
    for item in updated:
        sm = url_to_subsitemap.get(item["url"], "unknown")
        subsitemap_counts[sm] = subsitemap_counts.get(sm, 0) + 1

    if subsitemap_counts:
        analysis_lines.append("### Updates by section:")
        for sm, count in sorted(subsitemap_counts.items(), key=lambda x: -x[1]):
            section = sm.replace("sitemap.xml_", "").replace(".xml", "")
            analysis_lines.append(f"  - `{section}`: {count}")
        analysis_lines.append("")

    # New pages
    analysis_lines += [
        "## New Pages",
        "",
        f"Total: {len(added)} new URLs.",
        "",
    ]
    for url in added:
        rel_path = get_url_path(url) or "unknown"
        lm = current.get(url, "unknown")
        analysis_lines.append(f"### {url}")
        analysis_lines.append(f"- **Path:** `{rel_path}`")
        analysis_lines.append(f"- **lastmod:** {lm}")
        if url in new_page_summaries:
            preview = new_page_summaries[url][:300]
            analysis_lines.append(f"- **Preview:**")
            analysis_lines.append(f"  ```")
            analysis_lines.append(f"  {preview}")
            analysis_lines.append(f"  ```")
        analysis_lines.append("")

    # Removals
    analysis_lines += [
        "## Removed Pages",
        "",
        f"Total: {len(removed)} URLs removed from sitemap.",
        "",
    ]
    for url in removed:
        analysis_lines.append(f"- {url}")
    analysis_lines.append("")

    # Fetch failures
    all_failures = fetch_failures + page_fetch_failures
    if all_failures:
        analysis_lines += [
            "## Fetch Failures (Needs Follow-up)",
            "",
        ]
        for f in all_failures:
            analysis_lines.append(f"- **{f['url']}**: {f['error']}")
        analysis_lines.append("")

    (RUNS_DIR / "analysis.md").write_text("\n".join(analysis_lines))

    # --- STEP 8: UPDATE README ---
    print("\n[8] Updating README...")

    readme_path = REPO_ROOT / "README.md"
    existing_readme = readme_path.read_text(encoding="utf-8")

    # Build new section
    section_lines = [
        f"## {RUN_ID}",
        f"",
    ]

    # TL;DR paragraph
    notable_items = []
    if added:
        notable_items.append(f"{len(added)} new page(s) added")
    if removed:
        notable_items.append(f"{len(removed)} page(s) removed")
    if anomalies:
        notable_items.append(f"{len(anomalies)} anomaly/anomalies detected")
    if significant_updates:
        notable_items.append(f"{len(significant_updates)} pages with substantial content changes")

    if notable_items:
        tldr = f"This run found {', '.join(notable_items)}. "
    else:
        tldr = "Routine monitoring run with no significant structural changes. "

    tldr += f"Total {len(updated)} URLs showed lastmod changes, suggesting routine content updates across OpenAI's site."

    section_lines.append(f"**TL;DR:** {tldr}")
    section_lines.append("")

    # Anomalies
    if anomalies:
        section_lines.append("### ⚠️ Anomalies")
        section_lines.append("")
        for a in anomalies:
            section_lines.append(f"- **{a['kind']}** — `{a['url'][:70]}`")
            section_lines.append(f"  - {a['details']}")
        section_lines.append("")

    # New pages
    if added:
        section_lines.append("### New Pages")
        section_lines.append("")
        for url in added:
            rel_path = get_url_path(url) or ""
            lm = current.get(url, "")
            section_name = url.replace("https://openai.com/", "").rstrip("/")
            ok, err = fetch_results.get(url, (False, "not fetched"))
            if ok and rel_path:
                section_lines.append(f"- **[{section_name}]({rel_path})** (lastmod: {lm})")
            else:
                section_lines.append(f"- **{section_name}** (lastmod: {lm}; fetch: {'ok' if ok else 'failed'})")
            if url in new_page_summaries:
                first_lines = [l for l in new_page_summaries[url].splitlines() if l][:3]
                if first_lines:
                    section_lines.append(f"  - Preview: {first_lines[0][:120]}")
        section_lines.append("")

    # Notable updates
    if significant_updates:
        section_lines.append("### Notable Updates")
        section_lines.append("")
        for url, info in significant_updates[:10]:
            section_name = url.replace("https://openai.com/", "").rstrip("/")
            rel_path = get_url_path(url) or ""
            if rel_path:
                section_lines.append(f"- **[{section_name}]({rel_path})**: +{info['added_lines']} / -{info['removed_lines']} content lines")
            else:
                section_lines.append(f"- **{section_name}**: +{info['added_lines']} / -{info['removed_lines']} content lines")
        section_lines.append("")
    elif updated:
        section_lines.append("### Updates")
        section_lines.append("")
        section_lines.append(f"No substantial content changes detected in the {len(updated)} updated URLs (lastmod timestamps changed but content diff was minimal).")
        section_lines.append("")
        # Show section breakdown
        if subsitemap_counts:
            section_lines.append("Updates by section:")
            for sm, count in sorted(subsitemap_counts.items(), key=lambda x: -x[1])[:10]:
                sec = sm.replace("sitemap.xml_", "").replace(".xml", "")
                section_lines.append(f"  - `{sec}`: {count} URLs")
        section_lines.append("")

    # Removals
    if removed:
        section_lines.append("### Removed Pages")
        section_lines.append("")
        for url in removed[:20]:
            section_lines.append(f"- {url}")
        section_lines.append("")

    # Stats footer
    section_lines.append(f"**Stats:** {len(current)} total URLs | +{len(added)} added | ~{len(updated)} updated | -{len(removed)} removed | {len(anomalies)} anomalies | {len(sub_sitemap_urls)} sub-sitemaps")
    section_lines.append("")
    section_lines.append("---")
    section_lines.append("")

    new_section = "\n".join(section_lines)

    # Find insertion point (after first line / title)
    lines = existing_readme.splitlines(keepends=True)
    insert_after = 0
    for i, line in enumerate(lines):
        if line.startswith("## ") and i > 0:
            insert_after = i
            break

    if insert_after > 0:
        new_readme = "".join(lines[:insert_after]) + new_section + "".join(lines[insert_after:])
    else:
        new_readme = new_section + existing_readme

    readme_path.write_text(new_readme)

    # --- STEP 9: UPDATE STATE ---
    print("\n[9] Updating state/known_urls.json...")

    known_urls = load_known_urls()

    for url in current:
        lm = current[url]
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
            old_lm = entry.get("current_lastmod")
            if old_lm != lm:
                entry["current_lastmod"] = lm
                history = entry.get("lastmod_history", [])
                history.append({"run_id": RUN_ID, "lastmod": lm})
                entry["lastmod_history"] = history

    save_known_urls(known_urls)

    # --- STEP 10: WRITE DIFF.JSON ---
    print("\n[10] Writing diff.json...")

    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": "2026-06-17T09-15Z",
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": all_failures
    }

    (RUNS_DIR / "diff.json").write_text(json.dumps(diff_data, indent=2))

    print("\n=== Run complete ===")
    print(f"  Added: {len(added)}")
    print(f"  Updated: {len(updated)}")
    print(f"  Removed: {len(removed)}")
    print(f"  Anomalies: {len(anomalies)}")
    print(f"  Fetch failures: {len(all_failures)}")

    return {
        "added": added,
        "updated": updated,
        "removed": removed,
        "anomalies": anomalies,
        "fetch_failures": all_failures,
        "current_count": len(current),
    }

if __name__ == "__main__":
    import sys
    os.environ["TZ"] = "UTC"
    result = main()
