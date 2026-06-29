#!/usr/bin/env python3
"""Daily OpenAI sitemap monitor run for 2026-06-29T09-15Z"""

import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import httpx

RUN_ID = "2026-06-29T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REPO_ROOT = Path("/home/user/openai_monitor")
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def fetch_xml(url: str) -> str:
    r = httpx.get(url, timeout=30, follow_redirects=True)
    r.raise_for_status()
    return r.text

def parse_sitemap_index(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    locs = []
    for sitemap in root.findall("sm:sitemap", NS):
        loc = sitemap.find("sm:loc", NS)
        if loc is not None:
            locs.append(loc.text.strip())
    return locs

def parse_urlset(xml_text: str) -> dict[str, str | None]:
    """Returns {url: lastmod_or_None}"""
    root = ET.fromstring(xml_text)
    urls = {}
    for url in root.findall("sm:url", NS):
        loc = url.find("sm:loc", NS)
        lastmod = url.find("sm:lastmod", NS)
        if loc is not None:
            urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
    return urls

def sanitize_name(loc_url: str) -> str:
    """Convert sub-sitemap URL to filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> sitemap.xml_page.xml
    path = loc_url.replace("https://openai.com/", "").rstrip("/")
    return path.replace("/", "_") + ".xml"

def url_to_path(url: str) -> Path:
    result = subprocess.run(
        ["python", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return REPO_ROOT / result.stdout.strip()

def fetch_page(url: str, out_path: Path) -> bool:
    """Returns True on success."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["python", "tools/html_to_md.py", "--url", url, "--output", str(out_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    if result.returncode != 0:
        return False
    if out_path.exists():
        content = out_path.read_text()
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            return False
        return True
    return False

def read_baseline_urls() -> dict[str, str | None]:
    """Read all URLs from sub/latest/ sitemaps."""
    baseline = {}
    sub_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    for xml_file in sub_latest.glob("*.xml"):
        try:
            urls = parse_urlset(xml_file.read_text())
            baseline.update(urls)
        except Exception as e:
            print(f"Warning: could not parse {xml_file}: {e}")
    return baseline

def main():
    print(f"=== Run {RUN_ID} ===")
    print(f"Fetch time: {FETCH_TIME}")

    # 1. BASELINE
    print("\n[1] Reading baseline...")
    baseline = read_baseline_urls()
    print(f"  Baseline URLs: {len(baseline)}")

    # 2. FETCH + SNAPSHOT
    print("\n[2] Fetching fresh sitemap index...")
    root_xml = fetch_xml("https://openai.com/sitemap.xml")

    # Save root index
    root_dir = REPO_ROOT / "sitemaps/openai.com"
    (root_dir / f"{RUN_ID}.xml").write_text(root_xml)
    (root_dir / "latest.xml").write_text(root_xml)
    print(f"  Saved root index")

    sub_locs = parse_sitemap_index(root_xml)
    print(f"  Found {len(sub_locs)} sub-sitemaps")

    # Fetch all sub-sitemaps
    current = {}  # url -> lastmod
    sub_dated = REPO_ROOT / f"sitemaps/openai.com/sub/{RUN_ID}"
    sub_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    sub_dated.mkdir(parents=True, exist_ok=True)
    sub_latest.mkdir(parents=True, exist_ok=True)

    sub_xmls = {}  # filename -> xml_text
    for loc in sub_locs:
        name = sanitize_name(loc)
        try:
            xml_text = fetch_xml(loc)
            sub_xmls[name] = xml_text
            urls = parse_urlset(xml_text)
            current.update(urls)
            (sub_dated / name).write_text(xml_text)
            (sub_latest / name).write_text(xml_text)
        except Exception as e:
            print(f"  ERROR fetching {loc}: {e}")

    print(f"  Current URLs: {len(current)}")

    # 3. DIFF
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

    print(f"  Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")

    # 4. ANOMALY DETECTION
    print("\n[4] Detecting anomalies...")
    anomalies = []
    fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

    # Load known_urls.json for anomaly checks
    known_path = REPO_ROOT / "state/known_urls.json"
    known_urls = {}
    if known_path.exists():
        known_urls = json.loads(known_path.read_text())

    for url, lastmod in current.items():
        if lastmod:
            try:
                lm_dt = datetime.fromisoformat(lastmod + "+00:00" if len(lastmod) == 10 else lastmod.replace("Z", "+00:00"))
                # Future lastmod
                if lm_dt > fetch_dt:
                    anomalies.append({"kind": "future_lastmod", "url": url,
                                      "details": f"lastmod {lastmod} is after fetch time {FETCH_TIME}"})
                # Backward lastmod
                prior_lm = baseline.get(url)
                if prior_lm and prior_lm > lastmod:
                    anomalies.append({"kind": "backward_lastmod", "url": url,
                                      "details": f"lastmod moved backward: {prior_lm} -> {lastmod}"})
            except Exception:
                pass

    # Disappeared and reappeared
    for url in added:
        if url in known_urls and known_urls[url].get("last_seen"):
            last_seen = known_urls[url]["last_seen"]
            if last_seen != RUN_ID:  # was gone for at least one run
                fs = known_urls[url].get("first_seen", "unknown")
                anomalies.append({"kind": "reappeared", "url": url,
                                  "details": f"URL disappeared and reappeared. first_seen={fs}, was last_seen={last_seen}"})

    # Backdated new URL
    for url in added:
        lm = current.get(url)
        if lm and url not in known_urls:
            try:
                lm_dt = datetime.fromisoformat(lm + "+00:00" if len(lm) == 10 else lm.replace("Z", "+00:00"))
                run_dt = datetime.fromisoformat("2026-06-29T09:15:00+00:00")
                days_old = (run_dt - lm_dt).days
                if days_old > 7:
                    anomalies.append({"kind": "backdated_new_url", "url": url,
                                      "details": f"New URL has lastmod {lm} which is {days_old} days before first_seen"})
            except Exception:
                pass

    print(f"  Anomalies: {len(anomalies)}")

    # 5. FETCH + CONVERT changed and new pages
    print("\n[5] Fetching page content...")
    fetch_failures = []
    pages_fetched = []

    urls_to_fetch = added + [u["url"] for u in updated]
    print(f"  URLs to fetch: {len(urls_to_fetch)}")

    # Capture prior content for updated pages before overwriting
    prior_content = {}
    for item in updated:
        url = item["url"]
        md_path = url_to_path(url)
        if md_path.exists():
            prior_content[url] = md_path.read_text()

    # Fetch in batches of 10
    import concurrent.futures
    def fetch_one(url):
        md_path = url_to_path(url)
        try:
            success = fetch_page(url, md_path)
            if success:
                return ("ok", url, md_path)
            else:
                return ("fail", url, md_path)
        except Exception as e:
            return ("error", url, str(e))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch_one, url): url for url in urls_to_fetch}
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            status, url, info = future.result()
            if status == "ok":
                pages_fetched.append(url)
                if (i+1) % 10 == 0:
                    print(f"  Progress: {i+1}/{len(urls_to_fetch)}")
            else:
                fetch_failures.append({"url": url, "error": str(info)})
                print(f"  FAIL: {url}")

    print(f"  Fetched OK: {len(pages_fetched)}, Failed: {len(fetch_failures)}")

    # 6. ANALYZE
    print("\n[6] Analyzing changes...")
    analysis_lines = []

    # --- Anomalies ---
    analysis_lines.append(f"# Run Analysis: {RUN_ID}")
    analysis_lines.append(f"\nFetch time: {FETCH_TIME}")
    analysis_lines.append(f"Total URLs in current sitemap: {len(current)}")
    analysis_lines.append(f"Baseline URLs: {len(baseline)}")
    analysis_lines.append(f"\n---\n")
    analysis_lines.append("## Anomalies\n")
    if anomalies:
        for a in anomalies:
            analysis_lines.append(f"- **{a['kind']}** `{a['url']}`\n  {a['details']}")
    else:
        analysis_lines.append("No anomalies detected.")

    # --- New Pages ---
    analysis_lines.append("\n## New Pages\n")
    if added:
        for url in added:
            md_path = url_to_path(url)
            rel = md_path.relative_to(REPO_ROOT)
            lm = current.get(url, "unknown")
            summary = ""
            if md_path.exists():
                content = md_path.read_text()
                # Extract first meaningful lines
                lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
                summary = " ".join(lines[:3])[:300]
            analysis_lines.append(f"### [{url}]({url})")
            analysis_lines.append(f"- lastmod: `{lm}`")
            analysis_lines.append(f"- file: `{rel}`")
            if summary:
                analysis_lines.append(f"- preview: {summary}")
            analysis_lines.append("")
    else:
        analysis_lines.append("No new pages.")

    # --- Updated Pages ---
    analysis_lines.append("## Updated Pages\n")
    if updated:
        for item in updated:
            url = item["url"]
            md_path = url_to_path(url)
            rel = md_path.relative_to(REPO_ROOT)
            analysis_lines.append(f"### [{url}]({url})")
            analysis_lines.append(f"- lastmod: `{item['old_lastmod']}` → `{item['new_lastmod']}`")
            # Diff summary
            if url in prior_content and md_path.exists():
                new_content = md_path.read_text()
                old_lines = set(prior_content[url].splitlines())
                new_lines = set(new_content.splitlines())
                added_lines = [l for l in new_content.splitlines() if l not in old_lines and l.strip()][:5]
                removed_lines = [l for l in prior_content[url].splitlines() if l not in new_lines and l.strip()][:5]
                if added_lines:
                    analysis_lines.append(f"- Added content: {' | '.join(added_lines[:3])[:200]}")
                if removed_lines:
                    analysis_lines.append(f"- Removed content: {' | '.join(removed_lines[:3])[:200]}")
            analysis_lines.append("")
    else:
        analysis_lines.append("No updated pages.")

    # --- Removed Pages ---
    analysis_lines.append("## Removed Pages\n")
    if removed:
        for url in removed:
            analysis_lines.append(f"- `{url}`")
    else:
        analysis_lines.append("No removed pages.")

    # --- Fetch Failures ---
    analysis_lines.append("\n## Fetch Failures\n")
    if fetch_failures:
        for ff in fetch_failures:
            analysis_lines.append(f"- `{ff['url']}`: {ff['error']}")
    else:
        analysis_lines.append("No fetch failures.")

    # Write analysis
    run_dir = REPO_ROOT / f"runs/{RUN_ID}"
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "analysis.md").write_text("\n".join(analysis_lines))
    print(f"  Wrote {run_dir}/analysis.md")

    # 7. Write diff.json
    diff = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": "2026-06-27T09-15Z",
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures
    }
    (run_dir / "diff.json").write_text(json.dumps(diff, indent=2))
    print(f"  Wrote diff.json")

    # Return results for README update and state update
    return diff, current, baseline, prior_content

if __name__ == "__main__":
    result = main()
    print("\nDone. Results ready for README and state update.")
