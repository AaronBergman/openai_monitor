#!/usr/bin/env python3
"""
OpenAI sitemap monitoring script.
Run ID: determined at runtime
"""

import json
import os
import sys
import subprocess
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx
import tempfile
import shutil

RUN_ID = "2026-06-13T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REPO_ROOT = Path("/home/user/openai_monitor")
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def fetch_xml(url: str) -> str:
    """Fetch XML from URL using httpx (no Cloudflare bypass needed for sitemaps)."""
    r = httpx.get(url, timeout=30, follow_redirects=True,
                  headers={"User-Agent": "Mozilla/5.0 (compatible; openai-monitor/1.0)"})
    r.raise_for_status()
    return r.text

def sanitize_name(url: str) -> str:
    """Turn a sub-sitemap URL into a safe filename."""
    # e.g. https://openai.com/sitemap.xml/chatgpt/ -> sitemap.xml_chatgpt.xml
    path = url.replace("https://openai.com/", "").strip("/")
    return path.replace("/", "_") + ".xml"

def parse_urls_from_xml(xml_text: str) -> dict:
    """Parse <url> entries from a sitemap XML, return {loc: lastmod or None}."""
    urls = {}
    try:
        root = ET.fromstring(xml_text)
        for url_elem in root.findall("sm:url", NS):
            loc = url_elem.findtext("sm:loc", namespaces=NS)
            lastmod = url_elem.findtext("sm:lastmod", namespaces=NS)
            if loc:
                urls[loc] = lastmod
    except ET.ParseError:
        pass
    return urls

def parse_subsitemap_locs(xml_text: str) -> list:
    """Parse <sitemap><loc> entries from a sitemap index."""
    locs = []
    try:
        root = ET.fromstring(xml_text)
        for sitemap_elem in root.findall("sm:sitemap", NS):
            loc = sitemap_elem.findtext("sm:loc", namespaces=NS)
            if loc:
                locs.append(loc)
    except ET.ParseError:
        pass
    return locs

def load_baseline() -> dict:
    """Load baseline URLs from sub/latest/ directory."""
    baseline = {}
    sub_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    for xml_file in sub_latest.glob("*.xml"):
        try:
            content = xml_file.read_text()
            urls = parse_urls_from_xml(content)
            baseline.update(urls)
        except Exception as e:
            print(f"  Warning: failed to read {xml_file}: {e}")
    print(f"  Baseline: {len(baseline)} URLs from sub/latest/")
    return baseline

def url_to_path(url: str) -> Path:
    """Use tools/url_path.py to convert URL to repo path."""
    result = subprocess.run(
        ["python3", str(REPO_ROOT / "tools/url_path.py"), url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    rel_path = result.stdout.strip()
    if not rel_path:
        # Fallback
        from urllib.parse import urlparse
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        if not path:
            rel_path = f"pages/{parsed.netloc}/index.md"
        elif path.endswith("/"):
            rel_path = f"pages/{parsed.netloc}/{path}index.md"
        else:
            rel_path = f"pages/{parsed.netloc}/{path}.md"
    return REPO_ROOT / rel_path

def fetch_page(url: str, out_path: Path) -> tuple:
    """Fetch a page using html_to_md.py. Returns (success, content_or_error)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = out_path.with_suffix(".tmp.md")

    result = subprocess.run(
        ["python3", str(REPO_ROOT / "tools/html_to_md.py"),
         "--url", url, "--output", str(tmp_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )

    if tmp_path.exists():
        content = tmp_path.read_text()
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            tmp_path.unlink(missing_ok=True)
            return False, f"Fetch blocked (content too short or challenge page: {len(content)} chars)"
        # Move to final path
        shutil.move(str(tmp_path), str(out_path))
        return True, content
    else:
        return False, f"Script error: {result.stderr[:200]}"

def main():
    print(f"\n{'='*60}")
    print(f"OpenAI Sitemap Monitor - Run {RUN_ID}")
    print(f"Fetch time: {FETCH_TIME}")
    print(f"{'='*60}\n")

    # --- STEP 1: Load baseline ---
    print("STEP 1: Loading baseline...")
    baseline = load_baseline()

    # Also load prior known_urls state
    known_urls_path = REPO_ROOT / "state/known_urls.json"
    if known_urls_path.exists():
        with open(known_urls_path) as f:
            known_urls = json.load(f)
    else:
        known_urls = {}
    print(f"  Known URLs in state: {len(known_urls)}")

    # --- STEP 2: Fetch + Snapshot ---
    print("\nSTEP 2: Fetching sitemap index...")
    index_xml = fetch_xml(SITEMAP_INDEX_URL)

    # Save root index
    run_sitemap_dir = REPO_ROOT / f"sitemaps/openai.com"
    run_sitemap_dir.mkdir(parents=True, exist_ok=True)
    (run_sitemap_dir / f"{RUN_ID}.xml").write_text(index_xml)
    (run_sitemap_dir / "latest.xml").write_text(index_xml)
    print(f"  Saved root index")

    # Parse sub-sitemap locs
    sub_locs = parse_subsitemap_locs(index_xml)
    print(f"  Found {len(sub_locs)} sub-sitemaps")

    # Fetch all sub-sitemaps
    sub_dir_run = REPO_ROOT / f"sitemaps/openai.com/sub/{RUN_ID}"
    sub_dir_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    sub_dir_run.mkdir(parents=True, exist_ok=True)
    sub_dir_latest.mkdir(parents=True, exist_ok=True)

    current_urls = {}  # url -> lastmod
    url_to_subsitemap = {}  # url -> subsitemap name (for migration detection)

    print("  Fetching sub-sitemaps...")
    for loc in sub_locs:
        name = sanitize_name(loc)
        try:
            xml_text = fetch_xml(loc)
            (sub_dir_run / name).write_text(xml_text)
            (sub_dir_latest / name).write_text(xml_text)
            urls = parse_urls_from_xml(xml_text)
            for url, lastmod in urls.items():
                current_urls[url] = lastmod
                url_to_subsitemap[url] = name
            print(f"    {name}: {len(urls)} URLs")
        except Exception as e:
            print(f"    ERROR fetching {loc}: {e}")

    print(f"\n  Total current URLs: {len(current_urls)}")

    # --- STEP 3: Diff ---
    print("\nSTEP 3: Computing diff...")
    baseline_set = set(baseline.keys())
    current_set = set(current_urls.keys())

    added = sorted(current_set - baseline_set)
    removed = sorted(baseline_set - current_set)
    updated = []
    for url in baseline_set & current_set:
        old_lm = baseline.get(url)
        new_lm = current_urls.get(url)
        if old_lm != new_lm:
            updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})
    updated.sort(key=lambda x: x["url"])

    print(f"  Added:   {len(added)}")
    print(f"  Removed: {len(removed)}")
    print(f"  Updated: {len(updated)}")

    # --- STEP 4: Anomaly detection ---
    print("\nSTEP 4: Detecting anomalies...")
    anomalies = []
    fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

    def parse_dt(s):
        if not s:
            return None
        try:
            return datetime.fromisoformat(s.replace("Z", "+00:00"))
        except:
            return None

    # Future lastmod
    for url, lastmod in current_urls.items():
        dt = parse_dt(lastmod)
        if dt and dt > fetch_dt:
            anomalies.append({
                "kind": "future_lastmod",
                "url": url,
                "details": f"lastmod {lastmod} is after fetch time {FETCH_TIME}"
            })

    # Lastmod moved backwards
    for item in updated:
        old_dt = parse_dt(item["old_lastmod"])
        new_dt = parse_dt(item["new_lastmod"])
        if old_dt and new_dt and new_dt < old_dt:
            anomalies.append({
                "kind": "lastmod_backwards",
                "url": item["url"],
                "details": f"lastmod went from {item['old_lastmod']} back to {item['new_lastmod']}"
            })

    # New URLs with old lastmod
    for url in added:
        lastmod = current_urls.get(url)
        dt = parse_dt(lastmod)
        # first_seen is today, if lastmod is > 7 days old, flag it
        if dt:
            age_days = (fetch_dt - dt).days
            if age_days > 7:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"New URL with lastmod {lastmod} ({age_days} days old)"
                })

    # URL disappeared and reappeared
    for url in added:
        known = known_urls.get(url, {})
        last_seen = known.get("last_seen")
        if last_seen and last_seen < "2026-06-12":  # Was absent for at least a day
            anomalies.append({
                "kind": "reappeared",
                "url": url,
                "details": f"URL reappeared (last_seen was {last_seen})"
            })

    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies:
        print(f"    [{a['kind']}] {a['url']}: {a['details']}")

    # --- STEP 5: Fetch + Convert changed/new pages ---
    print(f"\nSTEP 5: Fetching {len(added)} new + {len(updated)} updated pages...")

    fetch_failures = []
    urls_to_fetch = []

    # Build list: (url, is_new)
    for url in added:
        urls_to_fetch.append((url, True))
    for item in updated:
        urls_to_fetch.append((item["url"], False))

    print(f"  Total pages to fetch: {len(urls_to_fetch)}")

    # Capture prior content for updated pages
    prior_content = {}
    for url, is_new in urls_to_fetch:
        if not is_new:
            out_path = url_to_path(url)
            rel = out_path.relative_to(REPO_ROOT)
            result = subprocess.run(
                ["git", "show", f"HEAD:{rel}"],
                capture_output=True, text=True, cwd=REPO_ROOT
            )
            if result.returncode == 0:
                prior_content[url] = result.stdout

    # Fetch pages with limited concurrency
    new_content = {}

    def fetch_one(args):
        url, is_new = args
        out_path = url_to_path(url)
        try:
            success, result = fetch_page(url, out_path)
            return url, is_new, success, result, out_path
        except Exception as e:
            return url, is_new, False, str(e), out_path

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch_one, args): args for args in urls_to_fetch}
        done_count = 0
        for future in as_completed(futures):
            url, is_new, success, result, out_path = future.result()
            done_count += 1
            if success:
                new_content[url] = result
                label = "NEW" if is_new else "UPD"
                if done_count % 20 == 0 or done_count <= 5:
                    print(f"  [{done_count}/{len(urls_to_fetch)}] {label} OK: {url[:80]}")
            else:
                fetch_failures.append({"url": url, "error": result})
                print(f"  FAIL: {url}: {result[:100]}")

    print(f"\n  Fetched: {len(new_content)} OK, {len(fetch_failures)} failed")

    # --- STEP 6: Analyze changes ---
    print("\nSTEP 6: Analyzing changes...")

    def diff_markdown(old: str, new: str) -> str:
        """Produce a short description of what changed between two markdown texts."""
        if not old:
            return "New page (no prior content)"
        old_lines = set(old.splitlines())
        new_lines = set(new.splitlines())
        added_lines = [l for l in new_lines - old_lines if l.strip()]
        removed_lines = [l for l in old_lines - new_lines if l.strip()]

        changes = []
        if added_lines:
            sample = added_lines[:3]
            changes.append(f"Added lines: {'; '.join(sample[:2])}" + (f" (+ {len(added_lines)-2} more)" if len(added_lines) > 2 else ""))
        if removed_lines:
            sample = removed_lines[:3]
            changes.append(f"Removed lines: {'; '.join(sample[:2])}" + (f" (+ {len(removed_lines)-2} more)" if len(removed_lines) > 2 else ""))

        if not changes:
            return "Minor/whitespace changes only"
        return " | ".join(changes)

    page_analyses = {}
    for url, content in new_content.items():
        is_new = url in added
        if is_new:
            # Summarize new page
            lines = [l.strip() for l in content.splitlines() if l.strip()]
            summary = " ".join(lines[:10])[:500]
            page_analyses[url] = {"type": "new", "summary": summary}
        else:
            # Diff against prior
            prior = prior_content.get(url, "")
            diff_desc = diff_markdown(prior, content)
            page_analyses[url] = {"type": "updated", "diff": diff_desc}

    # --- STEP 7: Write analysis.md ---
    print("\nSTEP 7: Writing analysis...")

    run_dir = REPO_ROOT / f"runs/{RUN_ID}"
    run_dir.mkdir(parents=True, exist_ok=True)

    analysis_lines = [
        f"# Run Analysis: {RUN_ID}",
        f"",
        f"**Fetch time:** {FETCH_TIME}",
        f"**Total current URLs:** {len(current_urls)}",
        f"**Added:** {len(added)} | **Updated:** {len(updated)} | **Removed:** {len(removed)}",
        f"**Anomalies:** {len(anomalies)} | **Fetch failures:** {len(fetch_failures)}",
        f"",
    ]

    if anomalies:
        analysis_lines += [
            "## Anomalies (High Signal)",
            "",
        ]
        for a in anomalies:
            analysis_lines.append(f"- **[{a['kind']}]** `{a['url']}`")
            analysis_lines.append(f"  - {a['details']}")
        analysis_lines.append("")

    if fetch_failures:
        analysis_lines += ["## Fetch Failures (Needs Follow-Up)", ""]
        for f in fetch_failures:
            analysis_lines.append(f"- `{f['url']}`: {f['error']}")
        analysis_lines.append("")

    if added:
        analysis_lines += ["## New Pages", ""]
        for url in sorted(added):
            analysis = page_analyses.get(url, {})
            out_path = url_to_path(url)
            rel = out_path.relative_to(REPO_ROOT)
            lastmod = current_urls.get(url, "unknown")
            analysis_lines.append(f"### {url}")
            analysis_lines.append(f"- **lastmod:** {lastmod}")
            analysis_lines.append(f"- **file:** `{rel}`")
            if analysis.get("summary"):
                analysis_lines.append(f"- **summary:** {analysis['summary'][:300]}")
            analysis_lines.append("")

    if updated:
        analysis_lines += [f"## Updated Pages ({len(updated)} total)", ""]
        # Group into significant and routine
        sig_updated = []
        routine_updated = []
        for item in updated:
            analysis = page_analyses.get(item["url"], {})
            diff = analysis.get("diff", "")
            if diff and "Minor/whitespace" not in diff and diff != "New page (no prior content)":
                sig_updated.append(item)
            else:
                routine_updated.append(item)

        if sig_updated:
            analysis_lines.append(f"### Significant Updates ({len(sig_updated)})")
            analysis_lines.append("")
            for item in sig_updated[:50]:  # Cap at 50 for readability
                url = item["url"]
                analysis = page_analyses.get(url, {})
                diff = analysis.get("diff", "")
                analysis_lines.append(f"- `{url}`")
                analysis_lines.append(f"  - lastmod: {item['old_lastmod']} → {item['new_lastmod']}")
                if diff:
                    analysis_lines.append(f"  - changes: {diff[:200]}")
            analysis_lines.append("")

        if routine_updated:
            analysis_lines.append(f"### Routine/Whitespace Updates ({len(routine_updated)})")
            analysis_lines.append("")
            for item in routine_updated[:20]:
                analysis_lines.append(f"- `{item['url']}`: {item['old_lastmod']} → {item['new_lastmod']}")
            if len(routine_updated) > 20:
                analysis_lines.append(f"- ... and {len(routine_updated)-20} more")
            analysis_lines.append("")

    if removed:
        analysis_lines += ["## Removed Pages", ""]
        for url in sorted(removed):
            analysis_lines.append(f"- `{url}`")
        analysis_lines.append("")

    (run_dir / "analysis.md").write_text("\n".join(analysis_lines))
    print(f"  Written: runs/{RUN_ID}/analysis.md")

    # --- STEP 8: Update README.md ---
    print("\nSTEP 8: Updating README.md...")

    readme_path = REPO_ROOT / "README.md"
    existing_readme = readme_path.read_text()

    # Build new section
    new_section_lines = [
        f"## {RUN_ID}",
        f"",
    ]

    # TL;DR
    tldr_parts = []
    if added:
        tldr_parts.append(f"{len(added)} new page{'s' if len(added)!=1 else ''}")
    if updated:
        tldr_parts.append(f"{len(updated)} updated page{'s' if len(updated)!=1 else ''}")
    if removed:
        tldr_parts.append(f"{len(removed)} removed page{'s' if len(removed)!=1 else ''}")
    if anomalies:
        tldr_parts.append(f"{len(anomalies)} anomal{'ies' if len(anomalies)!=1 else 'y'}")

    tldr = f"Routine daily scan of openai.com ({FETCH_TIME}). "
    if tldr_parts:
        tldr += "This run found: " + ", ".join(tldr_parts) + "."
    else:
        tldr += "No changes detected."

    if added:
        new_url_names = [u.replace("https://openai.com/", "/") for u in added[:3]]
        tldr += f" Notable new pages: {', '.join(new_url_names)}"
        if len(added) > 3:
            tldr += f" and {len(added)-3} more"
        tldr += "."

    new_section_lines.append(tldr)
    new_section_lines.append("")

    # Anomalies
    if anomalies:
        new_section_lines.append("### ⚠ Anomalies")
        new_section_lines.append("")
        for a in anomalies:
            new_section_lines.append(f"- **{a['kind']}**: `{a['url']}` — {a['details']}")
        new_section_lines.append("")

    # New pages
    if added:
        new_section_lines.append(f"### New Pages ({len(added)})")
        new_section_lines.append("")
        for url in sorted(added):
            out_path = url_to_path(url)
            rel = out_path.relative_to(REPO_ROOT)
            lastmod = current_urls.get(url, "unknown")
            analysis = page_analyses.get(url, {})
            summary = analysis.get("summary", "")[:200]
            new_section_lines.append(f"- [`{url.replace('https://openai.com', '')}`]({rel}) (lastmod: {lastmod})")
            if summary:
                new_section_lines.append(f"  > {summary}")
        new_section_lines.append("")

    # Updated pages
    if updated:
        sig_count = sum(1 for item in updated
                       if page_analyses.get(item["url"], {}).get("diff", "")
                       and "Minor/whitespace" not in page_analyses.get(item["url"], {}).get("diff", ""))

        new_section_lines.append(f"### Updated Pages ({len(updated)} total, {sig_count} significant)")
        new_section_lines.append("")

        shown = 0
        for item in updated:
            url = item["url"]
            analysis = page_analyses.get(url, {})
            diff = analysis.get("diff", "")
            if diff and "Minor/whitespace" not in diff and diff != "New page (no prior content)":
                out_path = url_to_path(url)
                rel = out_path.relative_to(REPO_ROOT)
                new_section_lines.append(f"- [`{url.replace('https://openai.com', '')}`]({rel})")
                new_section_lines.append(f"  - lastmod: {item['old_lastmod']} → {item['new_lastmod']}")
                new_section_lines.append(f"  - {diff[:250]}")
                shown += 1
                if shown >= 20:
                    remaining = sig_count - shown
                    if remaining > 0:
                        new_section_lines.append(f"- *(+{remaining} more significant updates — see [analysis]({run_dir.relative_to(REPO_ROOT)}/analysis.md))*")
                    break

        new_section_lines.append("")

    # Removed pages
    if removed:
        new_section_lines.append(f"### Removed Pages ({len(removed)})")
        new_section_lines.append("")
        for url in sorted(removed):
            new_section_lines.append(f"- `{url}`")
        new_section_lines.append("")

    if fetch_failures:
        new_section_lines.append(f"### Fetch Failures ({len(fetch_failures)})")
        new_section_lines.append("")
        for ff in fetch_failures[:5]:
            new_section_lines.append(f"- `{ff['url']}`: {ff['error'][:100]}")
        if len(fetch_failures) > 5:
            new_section_lines.append(f"- *(+{len(fetch_failures)-5} more)*")
        new_section_lines.append("")

    # Stats footer
    new_section_lines.append(f"*Stats: {len(current_urls)} total URLs | {len(added)} added | {len(updated)} updated | {len(removed)} removed | {len(anomalies)} anomalies | {len(sub_locs)} sub-sitemaps*")
    new_section_lines.append("")
    new_section_lines.append("---")
    new_section_lines.append("")

    new_section = "\n".join(new_section_lines)

    # Prepend to README - find the first ## date section
    # The README may start with a top-level header
    insert_marker = "## 2"  # All run sections start with ## 20YY-...
    if insert_marker in existing_readme:
        idx = existing_readme.index(insert_marker)
        new_readme = existing_readme[:idx] + new_section + existing_readme[idx:]
    else:
        # Append after first line
        lines = existing_readme.split("\n", 2)
        new_readme = lines[0] + "\n\n" + new_section + ("\n".join(lines[1:]) if len(lines) > 1 else "")

    readme_path.write_text(new_readme)
    print(f"  README.md updated")

    # --- STEP 9: Update state/known_urls.json ---
    print("\nSTEP 9: Updating state/known_urls.json...")

    for url in current_set:
        lastmod = current_urls[url]
        if url not in known_urls:
            known_urls[url] = {
                "first_seen": RUN_ID,
                "last_seen": RUN_ID,
                "current_lastmod": lastmod,
                "lastmod_history": [{"run_id": RUN_ID, "lastmod": lastmod}] if lastmod else []
            }
        else:
            known_urls[url]["last_seen"] = RUN_ID
            old_lm = known_urls[url].get("current_lastmod")
            if old_lm != lastmod:
                known_urls[url]["current_lastmod"] = lastmod
                hist = known_urls[url].get("lastmod_history", [])
                hist.append({"run_id": RUN_ID, "lastmod": lastmod})
                known_urls[url]["lastmod_history"] = hist

    # URLs no longer present - don't update last_seen (it stays at last run they appeared)

    with open(known_urls_path, "w") as f:
        json.dump(known_urls, f, indent=2, sort_keys=True)
    print(f"  Updated state/known_urls.json ({len(known_urls)} URLs)")

    # --- STEP 10: Write diff.json ---
    print("\nSTEP 10: Writing diff.json...")

    # Determine baseline run_id
    baseline_run_id = None
    latest_xml_path = REPO_ROOT / "sitemaps/openai.com/latest.xml"
    # Look at prior runs list
    prior_runs = sorted([d.name for d in (REPO_ROOT / "runs").iterdir() if d.is_dir()])
    if prior_runs:
        prior_runs_filtered = [r for r in prior_runs if r < RUN_ID]
        baseline_run_id = prior_runs_filtered[-1] if prior_runs_filtered else None

    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": baseline_run_id,
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures
    }

    with open(run_dir / "diff.json", "w") as f:
        json.dump(diff_data, f, indent=2)
    print(f"  Written: runs/{RUN_ID}/diff.json")

    print(f"\n{'='*60}")
    print(f"Run complete!")
    print(f"  Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}")
    print(f"  Anomalies: {len(anomalies)}, Failures: {len(fetch_failures)}")
    print(f"{'='*60}\n")

    return {
        "added": len(added),
        "updated": len(updated),
        "removed": len(removed),
        "anomalies": len(anomalies),
        "fetch_failures": len(fetch_failures),
        "added_urls": added,
        "anomaly_list": anomalies,
        "failure_list": fetch_failures,
    }

if __name__ == "__main__":
    result = main()
    # Return summary for notification decision
    print(json.dumps(result))
