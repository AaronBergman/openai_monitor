#!/usr/bin/env python3
"""Full monitoring pipeline for openai.com sitemap changes."""

import os
import sys
import json
import httpx
import subprocess
import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

# Configuration
RUN_ID = "2026-06-17T09-15Z"
FETCH_TIME = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
REPO_ROOT = Path("/home/user/openai_monitor")
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

def sanitize_name(url):
    """Convert sub-sitemap URL to filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> sitemap.xml_page.xml
    path = url.replace("https://openai.com/", "").rstrip("/")
    return path.replace("/", "_") + ".xml"

def fetch_xml(url, max_retries=3):
    """Fetch XML content from a URL."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; SitemapBot/1.0)"}
    for attempt in range(max_retries):
        try:
            resp = httpx.get(url, headers=headers, timeout=30, follow_redirects=True)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            import time
            time.sleep(2 ** attempt)

def parse_sitemap_index(xml_text):
    """Parse a sitemap index and return list of sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    urls = []
    for sitemap in root.findall(f"{{{NS}}}sitemap"):
        loc = sitemap.find(f"{{{NS}}}loc")
        if loc is not None:
            urls.append(loc.text.strip())
    return urls

def parse_urlset(xml_text):
    """Parse a URL set sitemap, returning dict of {url: lastmod}."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url in root.findall(f"{{{NS}}}url"):
        loc = url.find(f"{{{NS}}}loc")
        lastmod = url.find(f"{{{NS}}}lastmod")
        if loc is not None:
            urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
    return urls

def load_baseline():
    """Load baseline URL set from latest sub-sitemaps."""
    baseline = {}
    sub_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    for xml_file in sub_latest.glob("*.xml"):
        try:
            with open(xml_file) as f:
                content = f.read()
            urls = parse_urlset(content)
            baseline.update(urls)
        except Exception as e:
            print(f"  Warning: could not parse {xml_file}: {e}")
    return baseline

def compute_diff(baseline, current):
    """Compute added, removed, updated."""
    added = [url for url in current if url not in baseline]
    removed = [url for url in baseline if url not in current]
    updated = []
    for url in current:
        if url in baseline and current[url] != baseline[url]:
            updated.append({
                "url": url,
                "old_lastmod": baseline[url],
                "new_lastmod": current[url]
            })
    return added, removed, updated

def detect_anomalies(added, updated, current, state):
    """Detect various anomalies."""
    anomalies = []
    fetch_date = FETCH_TIME[:10]  # YYYY-MM-DD

    for url, lastmod in current.items():
        if lastmod and lastmod > fetch_date:
            anomalies.append({
                "kind": "future_lastmod",
                "url": url,
                "details": f"lastmod={lastmod} is after fetch time {fetch_date}"
            })

    for item in updated:
        url = item["url"]
        old_lm = item["old_lastmod"]
        new_lm = item["new_lastmod"]
        if old_lm and new_lm and new_lm < old_lm:
            anomalies.append({
                "kind": "backwards_lastmod",
                "url": url,
                "details": f"lastmod moved backwards from {old_lm} to {new_lm}"
            })

    for url in added:
        url_state = state.get(url, {})
        first_seen = url_state.get("first_seen", RUN_ID)
        lastmod = current.get(url)
        if lastmod and first_seen and lastmod[:10] < first_seen[:10]:
            diff_days = (datetime.date.fromisoformat(first_seen[:10]) -
                        datetime.date.fromisoformat(lastmod[:10])).days
            if diff_days > 3:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"new URL has lastmod={lastmod} which is {diff_days} days before first_seen"
                })

    # Check reappeared URLs
    for url in added:
        url_state = state.get(url, {})
        if url_state.get("last_seen") and url_state.get("last_seen") < RUN_ID:
            prev_seen = url_state.get("last_seen")
            first_seen = url_state.get("first_seen")
            if first_seen and first_seen < prev_seen:
                anomalies.append({
                    "kind": "reappeared_url",
                    "url": url,
                    "details": f"URL was seen before (first_seen={first_seen}, last_seen={prev_seen}) and has reappeared"
                })

    return anomalies

def get_url_path(url):
    """Use tools/url_path.py to get the repo path for a URL."""
    result = subprocess.run(
        ["python3", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()

def fetch_page(url, output_path):
    """Fetch a page using html_to_md.py."""
    result = subprocess.run(
        ["python3", "tools/html_to_md.py", "--url", url, "--output", str(output_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    return result.returncode == 0, result.stderr

def check_md_valid(path):
    """Check if markdown file is valid (not a Cloudflare challenge page)."""
    try:
        with open(path) as f:
            content = f.read()
        if len(content) < 100:
            return False, "too short"
        if "Enable JavaScript and cookies to continue" in content:
            return False, "Cloudflare challenge page"
        return True, None
    except:
        return False, "file not readable"

def main():
    print(f"=== OpenAI Sitemap Monitor Run: {RUN_ID} ===")
    print(f"Fetch time: {FETCH_TIME}")
    print()

    # ── STEP 1: Load baseline ──────────────────────────────────────────────
    print("Step 1: Loading baseline...")
    baseline = load_baseline()
    print(f"  Baseline: {len(baseline)} URLs")

    # ── STEP 2: Fetch + Snapshot ──────────────────────────────────────────
    print("\nStep 2: Fetching sitemaps...")

    # Fetch root sitemap index
    root_xml = fetch_xml("https://openai.com/sitemap.xml")
    sub_urls = parse_sitemap_index(root_xml)
    print(f"  Found {len(sub_urls)} sub-sitemaps")

    # Save root index
    root_dated = REPO_ROOT / f"sitemaps/openai.com/{RUN_ID}.xml"
    root_latest = REPO_ROOT / "sitemaps/openai.com/latest.xml"
    root_dated.write_text(root_xml)
    root_latest.write_text(root_xml)
    print(f"  Saved root index")

    # Fetch and save each sub-sitemap
    dated_dir = REPO_ROOT / f"sitemaps/openai.com/sub/{RUN_ID}"
    dated_dir.mkdir(parents=True, exist_ok=True)
    latest_dir = REPO_ROOT / "sitemaps/openai.com/sub/latest"
    latest_dir.mkdir(parents=True, exist_ok=True)

    current = {}  # {url: lastmod}
    sub_sitemap_sources = {}  # {url: sub_sitemap_name}

    for sub_url in sub_urls:
        sname = sanitize_name(sub_url)
        try:
            xml_text = fetch_xml(sub_url)
            urls = parse_urlset(xml_text)
            current.update(urls)
            for u in urls:
                sub_sitemap_sources[u] = sname

            (dated_dir / sname).write_text(xml_text)
            (latest_dir / sname).write_text(xml_text)
            print(f"  {sname}: {len(urls)} URLs")
        except Exception as e:
            print(f"  ERROR fetching {sub_url}: {e}")

    print(f"\n  Total current URLs: {len(current)}")

    # ── STEP 3: Diff ──────────────────────────────────────────────────────
    print("\nStep 3: Computing diff...")
    added, removed, updated = compute_diff(baseline, current)
    print(f"  Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")

    # ── STEP 4: Anomaly detection ─────────────────────────────────────────
    print("\nStep 4: Detecting anomalies...")
    state_path = REPO_ROOT / "state/known_urls.json"
    with open(state_path) as f:
        state = json.load(f)

    anomalies = detect_anomalies(added, updated, current, state)
    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies:
        print(f"    [{a['kind']}] {a['url'][:80]}")

    # ── STEP 5: Fetch + convert changed/new pages ─────────────────────────
    print("\nStep 5: Fetching changed/new pages...")
    fetch_failures = []
    page_diffs = {}  # {url: {"prev": str, "curr": str}}

    urls_to_fetch = [(u, "added") for u in added] + [(u["url"], "updated") for u in updated]

    # For updated pages, capture prior markdown
    for item in updated:
        url = item["url"]
        rel_path = get_url_path(url)
        if not rel_path:
            continue
        full_path = REPO_ROOT / rel_path
        # Get prior content from git
        result = subprocess.run(
            ["git", "show", f"HEAD:{rel_path}"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        if result.returncode == 0:
            page_diffs[url] = {"prev": result.stdout, "curr": None}

    MAX_PARALLEL = 10
    import threading
    lock = threading.Lock()
    semaphore = threading.Semaphore(MAX_PARALLEL)

    def fetch_one(url, kind):
        rel_path = get_url_path(url)
        if not rel_path:
            with lock:
                fetch_failures.append({"url": url, "error": "could not compute path"})
            return

        full_path = REPO_ROOT / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        with semaphore:
            ok, err = fetch_page(url, full_path)

        if ok:
            valid, reason = check_md_valid(full_path)
            if not valid:
                with lock:
                    fetch_failures.append({"url": url, "error": f"invalid content: {reason}"})
                # Restore prior content if it existed
                if kind == "updated" and url in page_diffs and page_diffs[url]["prev"]:
                    full_path.write_text(page_diffs[url]["prev"])
                return

            if kind == "updated" and url in page_diffs:
                with open(full_path) as f:
                    page_diffs[url]["curr"] = f.read()
        else:
            with lock:
                fetch_failures.append({"url": url, "error": err or "fetch failed"})

    threads = []
    for url, kind in urls_to_fetch:
        t = threading.Thread(target=fetch_one, args=(url, kind))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"  Fetched {len(urls_to_fetch)} pages, {len(fetch_failures)} failures")
    for f in fetch_failures:
        print(f"    FAIL: {f['url'][:80]}: {f['error'][:60]}")

    # ── STEP 6: Analyze ───────────────────────────────────────────────────
    print("\nStep 6: Analyzing changes...")

    analysis_lines = []

    analysis_lines.append(f"# Run Analysis: {RUN_ID}")
    analysis_lines.append(f"\nFetch time (UTC): {FETCH_TIME}")
    analysis_lines.append(f"Total URLs: {len(current)}")
    analysis_lines.append(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}, Anomalies: {len(anomalies)}, Fetch failures: {len(fetch_failures)}")

    # Anomalies
    analysis_lines.append(f"\n## Anomalies ({len(anomalies)})")
    if anomalies:
        for a in anomalies:
            analysis_lines.append(f"\n### [{a['kind']}]")
            analysis_lines.append(f"- URL: {a['url']}")
            analysis_lines.append(f"- Details: {a['details']}")
    else:
        analysis_lines.append("\nNo anomalies detected.")

    # Updated pages
    analysis_lines.append(f"\n## Updated Pages ({len(updated)})")
    for item in updated:
        url = item["url"]
        analysis_lines.append(f"\n### {url}")
        analysis_lines.append(f"- lastmod: {item['old_lastmod']} → {item['new_lastmod']}")

        if url in page_diffs and page_diffs[url].get("prev") and page_diffs[url].get("curr"):
            prev = page_diffs[url]["prev"]
            curr = page_diffs[url]["curr"]
            # Simple diff: find lines that changed
            prev_lines = set(prev.splitlines())
            curr_lines = set(curr.splitlines())
            removed_content = [l for l in prev_lines - curr_lines if l.strip()][:10]
            added_content = [l for l in curr_lines - prev_lines if l.strip()][:10]
            if removed_content or added_content:
                analysis_lines.append("- Content changes:")
                for l in added_content[:5]:
                    analysis_lines.append(f"  + {l[:120]}")
                for l in removed_content[:5]:
                    analysis_lines.append(f"  - {l[:120]}")
        else:
            # Try to read current content
            rel_path = get_url_path(url)
            if rel_path:
                full_path = REPO_ROOT / rel_path
                if full_path.exists():
                    with open(full_path) as f:
                        content = f.read()
                    # Show first meaningful lines
                    lines = [l for l in content.splitlines() if l.strip()][:5]
                    analysis_lines.append("- Current content preview:")
                    for l in lines:
                        analysis_lines.append(f"  {l[:120]}")

    if not updated:
        analysis_lines.append("\nNo pages updated.")

    # New pages
    analysis_lines.append(f"\n## New Pages ({len(added)})")
    for url in added:
        analysis_lines.append(f"\n### {url}")
        lastmod = current.get(url)
        analysis_lines.append(f"- lastmod: {lastmod}")
        rel_path = get_url_path(url)
        if rel_path:
            full_path = REPO_ROOT / rel_path
            if full_path.exists():
                with open(full_path) as f:
                    content = f.read()
                lines = [l for l in content.splitlines() if l.strip()][:8]
                analysis_lines.append("- Content preview:")
                for l in lines:
                    analysis_lines.append(f"  {l[:120]}")

    if not added:
        analysis_lines.append("\nNo new pages.")

    # Removed pages
    analysis_lines.append(f"\n## Removed Pages ({len(removed)})")
    for url in removed:
        analysis_lines.append(f"- {url}")
    if not removed:
        analysis_lines.append("\nNo removed pages.")

    # Fetch failures
    analysis_lines.append(f"\n## Fetch Failures ({len(fetch_failures)})")
    for ff in fetch_failures:
        analysis_lines.append(f"- {ff['url']}: {ff['error'][:100]}")
    if not fetch_failures:
        analysis_lines.append("\nNo fetch failures.")

    analysis_text = "\n".join(analysis_lines)

    # Save analysis
    run_dir = REPO_ROOT / f"runs/{RUN_ID}"
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "analysis.md").write_text(analysis_text)
    print(f"  Analysis saved to runs/{RUN_ID}/analysis.md")

    # ── STEP 7: Already done above ────────────────────────────────────────

    # ── STEP 8: Update README ─────────────────────────────────────────────
    print("\nStep 8: Updating README...")

    readme_path = REPO_ROOT / "README.md"
    with open(readme_path) as f:
        existing_readme = f.read()

    # Build new section
    section_lines = []
    section_lines.append(f"## {RUN_ID[:10]} — Monitoring Run")
    section_lines.append("")

    # TL;DR
    if not added and not removed and not updated:
        tldr = f"No changes detected in this run. The sitemap remains stable at {len(current)} URLs across {len(sub_urls)} sub-sitemaps."
    else:
        parts = []
        if added:
            parts.append(f"{len(added)} new page{'s' if len(added)!=1 else ''}")
        if updated:
            parts.append(f"{len(updated)} updated page{'s' if len(updated)!=1 else ''}")
        if removed:
            parts.append(f"{len(removed)} removed page{'s' if len(removed)!=1 else ''}")
        tldr = f"This run found {', '.join(parts)} across OpenAI's public sitemap (now {len(current)} total URLs, {len(sub_urls)} sub-sitemaps)."
        if anomalies:
            tldr += f" **{len(anomalies)} anomaly{'ies' if len(anomalies)!=1 else ''} detected** (see below)."

    section_lines.append(f"**TL;DR:** {tldr}")
    section_lines.append("")

    # Anomalies
    if anomalies:
        section_lines.append("### ⚠️ Anomalies")
        for a in anomalies:
            section_lines.append(f"- **[{a['kind']}]** `{a['url']}`: {a['details']}")
        section_lines.append("")

    # New pages
    if added:
        section_lines.append(f"### New Pages ({len(added)})")
        for url in added[:20]:
            rel_path = get_url_path(url)
            lastmod = current.get(url, "unknown")
            # Try to get a title/summary from the page
            title = url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
            if rel_path and (REPO_ROOT / rel_path).exists():
                with open(REPO_ROOT / rel_path) as ff:
                    content = ff.read()
                # Try to get the first heading
                for line in content.splitlines():
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
            if rel_path:
                section_lines.append(f"- [{title}]({rel_path}) (lastmod: {lastmod})")
            else:
                section_lines.append(f"- {url} (lastmod: {lastmod})")
        if len(added) > 20:
            section_lines.append(f"- *(and {len(added)-20} more)*")
        section_lines.append("")

    # Updated pages
    if updated:
        section_lines.append(f"### Updated Pages ({len(updated)})")
        for item in updated[:20]:
            url = item["url"]
            rel_path = get_url_path(url)
            title = url.rstrip("/").split("/")[-1] or "index"
            summary = f"lastmod: {item['old_lastmod']} → {item['new_lastmod']}"
            # Add content summary if we have it
            if url in page_diffs and page_diffs[url].get("prev") and page_diffs[url].get("curr"):
                prev_lines = set(page_diffs[url]["prev"].splitlines())
                curr_lines = set(page_diffs[url]["curr"].splitlines())
                n_added = len(curr_lines - prev_lines)
                n_removed = len(prev_lines - curr_lines)
                if n_added or n_removed:
                    summary += f"; +{n_added}/-{n_removed} lines changed"
            if rel_path:
                section_lines.append(f"- [{title}]({rel_path}): {summary}")
            else:
                section_lines.append(f"- {url}: {summary}")
        if len(updated) > 20:
            section_lines.append(f"- *(and {len(updated)-20} more)*")
        section_lines.append("")

    # Removed pages
    if removed:
        section_lines.append(f"### Removed Pages ({len(removed)})")
        for url in removed[:20]:
            section_lines.append(f"- {url}")
        if len(removed) > 20:
            section_lines.append(f"- *(and {len(removed)-20} more)*")
        section_lines.append("")

    # Stats footer
    section_lines.append(f"*Stats: {len(current)} total URLs | +{len(added)} added | ~{len(updated)} updated | -{len(removed)} removed | {len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps | {len(fetch_failures)} fetch failures*")
    section_lines.append("")
    section_lines.append("---")
    section_lines.append("")

    new_section = "\n".join(section_lines)

    # Find where to insert (after the first heading line)
    if "---\n" in existing_readme:
        # Insert before the first existing run section
        # Find the first "## " after the main header
        lines = existing_readme.split("\n")
        insert_idx = None
        found_first_h1 = False
        for i, line in enumerate(lines):
            if line.startswith("# "):
                found_first_h1 = True
            elif found_first_h1 and line.startswith("## "):
                insert_idx = i
                break

        if insert_idx is not None:
            lines.insert(insert_idx, new_section)
            new_readme = "\n".join(lines)
        else:
            new_readme = existing_readme + "\n\n" + new_section
    else:
        new_readme = existing_readme + "\n\n" + new_section

    readme_path.write_text(new_readme)
    print(f"  README.md updated")

    # ── STEP 9: Update state/known_urls.json ─────────────────────────────
    print("\nStep 9: Updating state...")

    for url, lastmod in current.items():
        if url not in state:
            state[url] = {
                "first_seen": RUN_ID,
                "last_seen": RUN_ID,
                "current_lastmod": lastmod,
                "lastmod_history": [{"run_id": RUN_ID, "lastmod": lastmod}] if lastmod else []
            }
        else:
            url_state = state[url]
            url_state["last_seen"] = RUN_ID
            old_lm = url_state.get("current_lastmod")
            if lastmod != old_lm:
                url_state["current_lastmod"] = lastmod
                if "lastmod_history" not in url_state:
                    url_state["lastmod_history"] = []
                url_state["lastmod_history"].append({"run_id": RUN_ID, "lastmod": lastmod})

    with open(state_path, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    print(f"  State updated: {len(state)} URLs")

    # ── STEP 10: Write diff.json ──────────────────────────────────────────
    print("\nStep 10: Writing diff.json...")

    # Find prior run_id
    prior_run_ids = sorted([
        d.name for d in (REPO_ROOT / "runs").iterdir()
        if d.is_dir() and d.name != RUN_ID
    ])
    baseline_run_id = prior_run_ids[-1] if prior_run_ids else None

    diff = {
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
        json.dump(diff, f, indent=2)
    print(f"  diff.json saved")

    # Summary
    print(f"\n=== Run Complete ===")
    print(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}")
    print(f"Anomalies: {len(anomalies)}, Fetch failures: {len(fetch_failures)}")

    return {
        "added": len(added),
        "updated": len(updated),
        "removed": len(removed),
        "anomalies": len(anomalies),
        "fetch_failures": len(fetch_failures),
        "total": len(current)
    }

if __name__ == "__main__":
    main()
