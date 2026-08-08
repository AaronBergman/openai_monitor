#!/usr/bin/env python3
"""
Main monitoring script for openai_monitor.
Run from the repo root. Pass run_id as the first argument.
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from curl_cffi import requests as cffi_requests

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent))
from url_path import url_to_repo_path

REPO_ROOT = Path(__file__).parent.parent
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sanitize_filename(url: str) -> str:
    path = urlsplit(url).path.strip("/")
    return re.sub(r"[^A-Za-z0-9._-]", "_", path) + ".xml"


def fetch_xml(url: str, client=None) -> str:
    ca_bundle = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE") or True
    r = cffi_requests.get(url, impersonate="chrome110", timeout=30, allow_redirects=True, verify=ca_bundle)
    r.raise_for_status()
    return r.text


def parse_sitemap_index(xml_text: str) -> list[str]:
    """Parse a sitemap-index and return sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    urls = []
    for sitemap in root.findall(f"{{{NS}}}sitemap"):
        loc = sitemap.findtext(f"{{{NS}}}loc")
        if loc:
            urls.append(loc.strip())
    return urls


def parse_urlset(xml_text: str) -> dict[str, str | None]:
    """Parse a urlset sitemap and return {url: lastmod_or_None}."""
    root = ET.fromstring(xml_text)
    result = {}
    for url_el in root.findall(f"{{{NS}}}url"):
        loc = url_el.findtext(f"{{{NS}}}loc")
        lastmod = url_el.findtext(f"{{{NS}}}lastmod")
        if loc:
            result[loc.strip()] = lastmod.strip() if lastmod else None
    return result


def load_baseline() -> dict[str, str | None]:
    """Load baseline URL set from sub/latest/ directory."""
    latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    baseline = {}
    if latest_dir.exists():
        for f in latest_dir.glob("*.xml"):
            try:
                xml_text = f.read_text(encoding="utf-8")
                urls = parse_urlset(xml_text)
                baseline.update(urls)
            except Exception as e:
                print(f"Warning: could not parse baseline {f.name}: {e}")
    return baseline


def load_known_urls() -> dict:
    path = REPO_ROOT / "state/known_urls.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def main():
    if len(sys.argv) < 2:
        print("Usage: run_monitor.py <run_id>")
        sys.exit(1)

    run_id = sys.argv[1]
    fetch_time = now_utc()
    print(f"Run ID: {run_id}, Fetch time: {fetch_time}")

    # --- STEP 1: Load baseline ---
    print("Loading baseline...")
    baseline = load_baseline()
    print(f"  Baseline URLs: {len(baseline)}")
    known_urls = load_known_urls()

    # Find prior run_id for diff.json
    runs_dir = REPO_ROOT / "runs"
    prior_runs = sorted(runs_dir.iterdir()) if runs_dir.exists() else []
    prior_run_id = prior_runs[-1].name if prior_runs else None

    # --- STEP 2: Fetch + snapshot ---
    print("Fetching sitemap index...")
    root_xml = fetch_xml("https://openai.com/sitemap.xml")

    # Save root index
    sitemap_dir = REPO_ROOT / "sitemaps/openai.com"
    sitemap_dir.mkdir(parents=True, exist_ok=True)
    (sitemap_dir / f"{run_id}.xml").write_text(root_xml, encoding="utf-8")
    (sitemap_dir / "latest.xml").write_text(root_xml, encoding="utf-8")
    print("  Root sitemap saved.")

    sub_urls = parse_sitemap_index(root_xml)
    print(f"  Found {len(sub_urls)} sub-sitemaps")

    # Save sub-sitemaps
    sub_run_dir = REPO_ROOT / f"sitemaps/openai.com/sub/{run_id}"
    sub_latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    sub_run_dir.mkdir(parents=True, exist_ok=True)
    sub_latest_dir.mkdir(parents=True, exist_ok=True)

    current_all = {}  # url -> lastmod
    url_to_subsitemap = {}  # for tracking sub-sitemap membership

    def fetch_sub(sub_url):
        fname = sanitize_filename(sub_url)
        xml_text = fetch_xml(sub_url)
        return sub_url, fname, xml_text

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_sub, u): u for u in sub_urls}
        for future in as_completed(futures):
            sub_url, fname, xml_text = future.result()
            (sub_run_dir / fname).write_text(xml_text, encoding="utf-8")
            (sub_latest_dir / fname).write_text(xml_text, encoding="utf-8")
            urls_in_sub = parse_urlset(xml_text)
            for u, lm in urls_in_sub.items():
                current_all[u] = lm
                url_to_subsitemap[u] = sub_url
            print(f"  Sub-sitemap {fname}: {len(urls_in_sub)} URLs")

    print(f"Total current URLs: {len(current_all)}")

    # --- STEP 3: Diff ---
    baseline_set = set(baseline.keys())
    current_set = set(current_all.keys())

    added = sorted(current_set - baseline_set)
    removed = sorted(baseline_set - current_set)
    updated = []
    for url in current_set & baseline_set:
        old_lm = baseline[url]
        new_lm = current_all[url]
        if old_lm != new_lm:
            updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})
    updated.sort(key=lambda x: x["url"])

    print(f"Diff: +{len(added)} added, {len(updated)} updated, -{len(removed)} removed")

    # --- STEP 4: Anomaly detection ---
    anomalies = []
    fetch_dt = datetime.fromisoformat(fetch_time.replace("Z", "+00:00"))

    # Check for future lastmod
    for url, lm in current_all.items():
        if lm:
            try:
                lm_dt = datetime.fromisoformat(lm + ("T00:00:00+00:00" if len(lm) == 10 else "+00:00") if "+" not in lm and "Z" not in lm else lm.replace("Z", "+00:00"))
                if lm_dt > fetch_dt:
                    anomalies.append({
                        "kind": "future_lastmod",
                        "url": url,
                        "details": f"lastmod {lm} is after fetch time {fetch_time}"
                    })
            except Exception:
                pass

    # Check for backwards lastmod
    for entry in updated:
        old_lm, new_lm = entry["old_lastmod"], entry["new_lastmod"]
        if old_lm and new_lm:
            try:
                def parse_lm(s):
                    s = s.replace("Z", "+00:00")
                    if len(s.split("T")[0]) == 10 and "T" not in s:
                        s = s + "T00:00:00+00:00"
                    return datetime.fromisoformat(s)
                if parse_lm(new_lm) < parse_lm(old_lm):
                    anomalies.append({
                        "kind": "backwards_lastmod",
                        "url": entry["url"],
                        "details": f"lastmod moved backwards from {old_lm} to {new_lm}"
                    })
            except Exception:
                pass

    # Check for new URLs with old lastmod (backdated)
    for url in added:
        lm = current_all.get(url)
        if lm:
            try:
                lm_date = lm[:10]
                run_date = run_id[:10]
                lm_dt_simple = datetime.strptime(lm_date, "%Y-%m-%d")
                run_dt_simple = datetime.strptime(run_date, "%Y-%m-%d")
                delta = (run_dt_simple - lm_dt_simple).days
                if delta > 7:
                    anomalies.append({
                        "kind": "backdated_new_url",
                        "url": url,
                        "details": f"New URL has lastmod {lm} which is {delta} days before first_seen {run_id}"
                    })
            except Exception:
                pass

    # Check for reappeared URLs
    for url in added:
        if url in known_urls and known_urls[url].get("last_seen") and known_urls[url]["last_seen"] < run_id:
            anomalies.append({
                "kind": "reappeared_url",
                "url": url,
                "details": f"URL was previously seen (last_seen: {known_urls[url].get('last_seen')}, first_seen: {known_urls[url].get('first_seen')}), disappeared, and reappeared"
            })

    print(f"Anomalies detected: {len(anomalies)}")

    # Print anomaly summary
    for a in anomalies[:20]:
        print(f"  ANOMALY [{a['kind']}]: {a['url'][:80]} - {a['details'][:100]}")

    # --- STEP 5: Fetch + convert changed/new pages ---
    pages_to_fetch = added + [e["url"] for e in updated]
    print(f"\nFetching {len(pages_to_fetch)} pages (added + updated)...")

    fetch_failures = []
    page_diffs = {}  # url -> {"old": str, "new": str}

    def fetch_page(url):
        md_path = REPO_ROOT / url_to_repo_path(url)
        md_path.parent.mkdir(parents=True, exist_ok=True)

        # Capture prior for diff if updating
        prior_content = None
        if url not in added and md_path.exists():
            prior_content = md_path.read_text(encoding="utf-8")

        tmp_path = f"/tmp/monitor_page_{abs(hash(url))}.md"
        ret = os.system(f'python {REPO_ROOT}/tools/html_to_md.py --url "{url}" --output "{tmp_path}" 2>/dev/null')

        if ret != 0 or not os.path.exists(tmp_path):
            return url, None, prior_content, "html_to_md.py returned non-zero exit code"

        new_content = open(tmp_path, encoding="utf-8").read()
        if len(new_content) < 100 or "Enable JavaScript and cookies to continue" in new_content:
            return url, None, prior_content, f"Fetch blocked (content length={len(new_content)})"

        # Write page
        md_path.write_text(new_content, encoding="utf-8")
        return url, new_content, prior_content, None

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_page, u): u for u in pages_to_fetch}
        for i, future in enumerate(as_completed(futures)):
            url, new_content, prior_content, err = future.result()
            if err:
                fetch_failures.append({"url": url, "error": err})
                print(f"  FAIL [{i+1}/{len(pages_to_fetch)}] {url[:60]}: {err}")
            else:
                print(f"  OK   [{i+1}/{len(pages_to_fetch)}] {url[:70]}")
                if prior_content and new_content:
                    page_diffs[url] = {"old": prior_content, "new": new_content}

    print(f"Fetch complete: {len(pages_to_fetch) - len(fetch_failures)} succeeded, {len(fetch_failures)} failed")

    # --- STEP 7: Write analysis ---
    run_dir = REPO_ROOT / f"runs/{run_id}"
    run_dir.mkdir(parents=True, exist_ok=True)

    analysis_lines = [
        f"# Run {run_id} Analysis",
        f"",
        f"**Fetch time:** {fetch_time}  ",
        f"**Baseline:** {prior_run_id}  ",
        f"**Total current URLs:** {len(current_all)}  ",
        f"**Added:** {len(added)}  **Updated:** {len(updated)}  **Removed:** {len(removed)}  ",
        f"**Anomalies:** {len(anomalies)}  **Fetch failures:** {len(fetch_failures)}",
        f"",
    ]

    if anomalies:
        analysis_lines += ["## Anomalies (Highest Signal)", ""]
        for a in anomalies:
            analysis_lines.append(f"- **{a['kind']}**: `{a['url']}`")
            analysis_lines.append(f"  - {a['details']}")
        analysis_lines.append("")

    if fetch_failures:
        analysis_lines += ["## Fetch Failures (Needs Follow-up)", ""]
        for f_fail in fetch_failures:
            analysis_lines.append(f"- `{f_fail['url']}`: {f_fail['error']}")
        analysis_lines.append("")

    if updated:
        analysis_lines += ["## Updated Pages", ""]
        for entry in updated:
            url = entry["url"]
            analysis_lines.append(f"### {url}")
            analysis_lines.append(f"- lastmod: `{entry['old_lastmod']}` → `{entry['new_lastmod']}`")
            if url in page_diffs:
                old_md = page_diffs[url]["old"]
                new_md = page_diffs[url]["new"]
                old_len = len(old_md)
                new_len = len(new_md)
                analysis_lines.append(f"- Content length: {old_len} → {new_len} chars (delta: {new_len - old_len:+d})")
                # Simple line diff summary
                old_lines = set(old_md.splitlines())
                new_lines = set(new_md.splitlines())
                added_lines = [l for l in new_lines - old_lines if l.strip()][:5]
                removed_lines = [l for l in old_lines - new_lines if l.strip()][:5]
                if added_lines:
                    analysis_lines.append(f"- Sample new content lines:")
                    for l in added_lines:
                        analysis_lines.append(f"  + {l[:120]}")
                if removed_lines:
                    analysis_lines.append(f"- Sample removed content lines:")
                    for l in removed_lines:
                        analysis_lines.append(f"  - {l[:120]}")
            analysis_lines.append("")

    if added:
        analysis_lines += ["## New Pages", ""]
        for url in sorted(added):
            md_path = REPO_ROOT / url_to_repo_path(url)
            lm = current_all.get(url, "unknown")
            sub = url_to_subsitemap.get(url, "unknown")
            # Extract title from markdown if available
            title = ""
            if md_path.exists():
                content = md_path.read_text(encoding="utf-8")
                for line in content.splitlines():
                    line = line.strip()
                    if line.startswith("# "):
                        title = line[2:]
                        break
            analysis_lines.append(f"- `{url}`")
            if title:
                analysis_lines.append(f"  - Title: **{title}**")
            analysis_lines.append(f"  - lastmod: {lm}")
            analysis_lines.append(f"  - Sub-sitemap: {sub}")
        analysis_lines.append("")

    if removed:
        analysis_lines += ["## Removed URLs", ""]
        for url in removed:
            analysis_lines.append(f"- `{url}`")
            md_path = REPO_ROOT / url_to_repo_path(url)
            if md_path.exists():
                analysis_lines.append(f"  - Last snapshot at: `{url_to_repo_path(url)}`")
        analysis_lines.append("")

    analysis_text = "\n".join(analysis_lines)
    (run_dir / "analysis.md").write_text(analysis_text, encoding="utf-8")
    print(f"\nAnalysis written to runs/{run_id}/analysis.md")

    # --- STEP 8: Update README.md ---
    readme_path = REPO_ROOT / "README.md"
    existing_readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

    # Build new section
    readme_section_lines = [
        f"## {run_id}",
        f"",
        f"**Fetch time:** {fetch_time} UTC | **Baseline:** {prior_run_id}",
        f"",
    ]

    # TL;DR paragraph
    tldr_parts = []
    if added:
        tldr_parts.append(f"{len(added)} new URL(s) added")
    if updated:
        tldr_parts.append(f"{len(updated)} page(s) updated")
    if removed:
        tldr_parts.append(f"{len(removed)} URL(s) removed")
    if anomalies:
        tldr_parts.append(f"{len(anomalies)} anomaly/anomalies detected")
    if not tldr_parts:
        tldr_parts.append("no changes detected")
    readme_section_lines.append(f"**TL;DR:** This run found " + ", ".join(tldr_parts) + f" across OpenAI's public sitemap ({len(current_all)} total URLs across {len(sub_urls)} sub-sitemaps).")
    readme_section_lines.append("")

    if anomalies:
        readme_section_lines.append("### Anomalies")
        readme_section_lines.append("")
        for a in anomalies[:10]:
            readme_section_lines.append(f"- **{a['kind']}**: `{a['url'][:100]}`")
            readme_section_lines.append(f"  - {a['details']}")
        readme_section_lines.append("")

    if added:
        readme_section_lines.append("### New Pages")
        readme_section_lines.append("")
        for url in sorted(added)[:30]:
            md_path_rel = url_to_repo_path(url)
            md_path_abs = REPO_ROOT / md_path_rel
            title = ""
            if md_path_abs.exists():
                for line in md_path_abs.read_text(encoding="utf-8").splitlines():
                    if line.strip().startswith("# "):
                        title = line.strip()[2:]
                        break
            lm = current_all.get(url, "")
            entry = f"- [{url}]({md_path_rel})"
            if title:
                entry += f" — **{title[:80]}**"
            if lm:
                entry += f" (lastmod: {lm})"
            readme_section_lines.append(entry)
        if len(added) > 30:
            readme_section_lines.append(f"- ... and {len(added)-30} more (see runs/{run_id}/analysis.md)")
        readme_section_lines.append("")

    if updated:
        readme_section_lines.append("### Updated Pages")
        readme_section_lines.append("")
        for entry in updated[:20]:
            url = entry["url"]
            md_path_rel = url_to_repo_path(url)
            change_note = ""
            if url in page_diffs:
                old_len = len(page_diffs[url]["old"])
                new_len = len(page_diffs[url]["new"])
                change_note = f" (content: {old_len}→{new_len} chars)"
            readme_section_lines.append(f"- [{url}]({md_path_rel}) — lastmod `{entry['old_lastmod']}` → `{entry['new_lastmod']}`{change_note}")
        if len(updated) > 20:
            readme_section_lines.append(f"- ... and {len(updated)-20} more (see runs/{run_id}/analysis.md)")
        readme_section_lines.append("")

    if removed:
        readme_section_lines.append("### Removed URLs")
        readme_section_lines.append("")
        for url in removed[:20]:
            readme_section_lines.append(f"- `{url}`")
        if len(removed) > 20:
            readme_section_lines.append(f"- ... and {len(removed)-20} more")
        readme_section_lines.append("")

    if fetch_failures:
        readme_section_lines.append("### Fetch Failures")
        readme_section_lines.append("")
        for ff in fetch_failures[:10]:
            readme_section_lines.append(f"- `{ff['url']}`: {ff['error']}")
        readme_section_lines.append("")

    readme_section_lines.append(f"**Stats:** {len(current_all)} total URLs | +{len(added)} added | {len(updated)} updated | -{len(removed)} removed | {len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps")
    readme_section_lines.append("")
    readme_section_lines.append("---")
    readme_section_lines.append("")

    new_readme_section = "\n".join(readme_section_lines)

    # Find insertion point: after the first line (title), before the first ## section
    lines = existing_readme.splitlines()
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("## "):
            insert_at = i
            break
        if i > 5:  # If no ## found in first 5 lines, insert after title block
            insert_at = i
            break

    if insert_at == 0 and not any(l.startswith("## ") for l in lines):
        new_readme = existing_readme + "\n" + new_readme_section
    else:
        before = "\n".join(lines[:insert_at])
        after = "\n".join(lines[insert_at:])
        new_readme = before + "\n\n" + new_readme_section + after

    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"README.md updated.")

    # --- STEP 9: Update state/known_urls.json ---
    for url in current_all:
        if url not in known_urls:
            known_urls[url] = {
                "first_seen": run_id,
                "last_seen": run_id,
                "current_lastmod": current_all[url],
                "lastmod_history": [{"run_id": run_id, "lastmod": current_all[url]}]
            }
        else:
            known_urls[url]["last_seen"] = run_id
            if current_all[url] != known_urls[url].get("current_lastmod"):
                known_urls[url].setdefault("lastmod_history", []).append({
                    "run_id": run_id,
                    "lastmod": current_all[url]
                })
                known_urls[url]["current_lastmod"] = current_all[url]

    state_path = REPO_ROOT / "state/known_urls.json"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(known_urls, indent=2, sort_keys=True), encoding="utf-8")
    print(f"state/known_urls.json updated ({len(known_urls)} URLs)")

    # --- STEP 10: Write diff.json ---
    diff_data = {
        "run_id": run_id,
        "fetch_time": fetch_time,
        "baseline": prior_run_id,
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures
    }
    (run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2), encoding="utf-8")
    print(f"runs/{run_id}/diff.json written.")

    print(f"\nRun complete: +{len(added)} added, {len(updated)} updated, -{len(removed)} removed, {len(anomalies)} anomalies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
