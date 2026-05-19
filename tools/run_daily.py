#!/usr/bin/env python3
"""Daily monitoring run script for openai.com sitemap changes."""

import os
import sys
import json
import subprocess
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import httpx
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "httpx", "--quiet"], check=True)
    import httpx

REPO_ROOT = Path(__file__).parent.parent
TOOLS_DIR = REPO_ROOT / "tools"

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

def fetch_xml(url: str, client: httpx.Client, retries: int = 3) -> str | None:
    """Fetch XML from URL with retries."""
    for attempt in range(retries):
        try:
            r = client.get(url, timeout=30)
            r.raise_for_status()
            return r.text
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
                return None

def parse_sitemap_index(xml_text: str) -> list[str]:
    """Parse sitemap index and return list of sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    locs = []
    for sitemap in root.findall(f"{{{NS}}}sitemap"):
        loc = sitemap.find(f"{{{NS}}}loc")
        if loc is not None:
            locs.append(loc.text.strip())
    return locs

def parse_url_set(xml_text: str) -> dict[str, str | None]:
    """Parse url set and return dict of url -> lastmod."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url_el in root.findall(f"{{{NS}}}url"):
        loc = url_el.find(f"{{{NS}}}loc")
        lastmod = url_el.find(f"{{{NS}}}lastmod")
        if loc is not None:
            urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
    return urls

def url_to_filename(sub_url: str) -> str:
    """Convert sub-sitemap URL to filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> _openai.com_sitemap.xml_page.xml
    path = sub_url.replace("https://", "").replace("http://", "")
    path = path.rstrip("/")
    path = path.replace("/", "_")
    if not path.endswith(".xml"):
        path += ".xml"
    return path

def load_baseline() -> dict[str, str | None]:
    """Load all baseline URLs from sub/latest/ files."""
    baseline = {}
    sub_latest = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / "latest"
    if not sub_latest.exists():
        return baseline
    for f in sub_latest.glob("*.xml"):
        try:
            text = f.read_text()
            urls = parse_url_set(text)
            baseline.update(urls)
        except Exception as e:
            print(f"  WARN: could not parse {f}: {e}", file=sys.stderr)
    return baseline

def get_url_path(url: str) -> str:
    """Get the repo path for a URL using url_path.py."""
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "url_path.py"), url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()

def fetch_page(url: str, md_path: Path) -> tuple[str, bool, str]:
    """Fetch a page and convert to markdown. Returns (url, success, error)."""
    md_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "html_to_md.py"), "--url", url, "--output", str(md_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    if result.returncode != 0:
        return url, False, result.stderr.strip() or result.stdout.strip()
    # Sanity check
    try:
        content = md_path.read_text()
        if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
            return url, False, f"Blocked/too-short ({len(content)} chars)"
    except Exception as e:
        return url, False, str(e)
    return url, True, ""

def main():
    run_id = os.environ.get("RUN_ID") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ")
    fetch_time = datetime.now(timezone.utc).isoformat()

    print(f"=== OpenAI Monitor Run: {run_id} ===")
    print(f"Fetch time: {fetch_time}")

    # Paths
    sitemap_dir = REPO_ROOT / "sitemaps" / "openai.com"
    sub_dated = sitemap_dir / "sub" / run_id
    sub_latest = sitemap_dir / "sub" / "latest"
    pages_dir = REPO_ROOT / "pages" / "openai.com"
    run_dir = REPO_ROOT / "runs" / run_id
    state_file = REPO_ROOT / "state" / "known_urls.json"

    sub_dated.mkdir(parents=True, exist_ok=True)
    sub_latest.mkdir(parents=True, exist_ok=True)
    run_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)

    # STEP 1: Load baseline
    print("\n[1] Loading baseline...")
    baseline = load_baseline()
    print(f"  Baseline: {len(baseline)} URLs")

    # Find prior run_id from latest.xml
    prior_run_id = None
    for f in sorted((REPO_ROOT / "sitemaps" / "openai.com").glob("2*.xml"), reverse=True):
        if f.name != "latest.xml" and f.stem != run_id:
            prior_run_id = f.stem
            break
    print(f"  Prior run: {prior_run_id}")

    # STEP 2: Fetch sitemaps
    print("\n[2] Fetching sitemaps...")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; OpenAI-Monitor/1.0)"}

    with httpx.Client(headers=headers, follow_redirects=True) as client:
        # Fetch index
        index_url = "https://openai.com/sitemap.xml"
        index_xml = fetch_xml(index_url, client)
        if not index_xml:
            print("FATAL: Could not fetch sitemap index", file=sys.stderr)
            sys.exit(1)

        # Save index
        index_path_dated = sitemap_dir / f"{run_id}.xml"
        index_path_latest = sitemap_dir / "latest.xml"
        index_path_dated.write_text(index_xml)
        index_path_latest.write_text(index_xml)
        print(f"  Saved index ({len(index_xml)} bytes)")

        # Parse sub-sitemap URLs
        sub_urls = parse_sitemap_index(index_xml)
        print(f"  Found {len(sub_urls)} sub-sitemaps")

        # Check for new/removed sub-sitemaps
        baseline_sub_files = {f.name for f in sub_latest.glob("*.xml")}
        current_sub_files = {url_to_filename(u) for u in sub_urls}
        new_subs = current_sub_files - baseline_sub_files
        removed_subs = baseline_sub_files - current_sub_files
        if new_subs:
            print(f"  NEW sub-sitemaps: {new_subs}")
        if removed_subs:
            print(f"  REMOVED sub-sitemaps: {removed_subs}")

        # Fetch all sub-sitemaps
        current_urls: dict[str, str | None] = {}
        sub_xml_map: dict[str, str] = {}

        def fetch_sub(sub_url):
            xml = fetch_xml(sub_url, client)
            return sub_url, xml

        with ThreadPoolExecutor(max_workers=10) as pool:
            futures = {pool.submit(fetch_sub, u): u for u in sub_urls}
            for fut in as_completed(futures):
                sub_url, xml = fut.result()
                fname = url_to_filename(sub_url)
                if xml:
                    (sub_dated / fname).write_text(xml)
                    (sub_latest / fname).write_text(xml)
                    urls = parse_url_set(xml)
                    current_urls.update(urls)
                    sub_xml_map[sub_url] = xml
                else:
                    print(f"  WARN: failed to fetch {sub_url}", file=sys.stderr)

        print(f"  Total current URLs: {len(current_urls)}")

    # STEP 3: Diff
    print("\n[3] Computing diff...")
    added = {u: v for u, v in current_urls.items() if u not in baseline}
    removed = {u: baseline[u] for u in baseline if u not in current_urls}
    updated = {
        u: {"old": baseline[u], "new": current_urls[u]}
        for u in current_urls
        if u in baseline and current_urls[u] != baseline[u]
    }
    print(f"  Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")

    # STEP 4: Anomaly detection
    print("\n[4] Anomaly detection...")
    anomalies = []
    fetch_dt = datetime.fromisoformat(fetch_time)

    for url, lastmod in current_urls.items():
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
            if lm_dt.tzinfo is None:
                lm_dt = lm_dt.replace(tzinfo=timezone.utc)
            # Future lastmod
            if lm_dt > fetch_dt:
                anomalies.append({
                    "kind": "future_lastmod",
                    "url": url,
                    "details": f"lastmod {lastmod} is after fetch time {fetch_time}"
                })
        except Exception:
            pass

    # Backwards lastmod
    for url, info in updated.items():
        old, new = info["old"], info["new"]
        if old and new:
            try:
                old_dt = datetime.fromisoformat(old.replace("Z", "+00:00"))
                new_dt = datetime.fromisoformat(new.replace("Z", "+00:00"))
                if old_dt.tzinfo is None:
                    old_dt = old_dt.replace(tzinfo=timezone.utc)
                if new_dt.tzinfo is None:
                    new_dt = new_dt.replace(tzinfo=timezone.utc)
                if new_dt < old_dt:
                    anomalies.append({
                        "kind": "backwards_lastmod",
                        "url": url,
                        "details": f"lastmod moved backwards: {old} -> {new}"
                    })
            except Exception:
                pass

    # Load known_urls for reappeared/backdated checks
    known_urls = {}
    if state_file.exists():
        try:
            known_urls = json.loads(state_file.read_text())
        except Exception:
            pass

    for url in added:
        lastmod = current_urls[url]
        if url in known_urls:
            anomalies.append({
                "kind": "reappeared",
                "url": url,
                "details": f"URL reappeared; first_seen={known_urls[url].get('first_seen')}"
            })
        elif lastmod:
            try:
                lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
                first_seen_dt = datetime.strptime(run_id, "%Y-%m-%dT%H-%MZ").replace(tzinfo=timezone.utc)
                if lm_dt.tzinfo is None:
                    lm_dt = lm_dt.replace(tzinfo=timezone.utc)
                diff_days = (first_seen_dt - lm_dt).days
                if diff_days > 7:
                    anomalies.append({
                        "kind": "backdated_new_url",
                        "url": url,
                        "details": f"New URL with lastmod {lastmod} predates first_seen by {diff_days} days"
                    })
            except Exception:
                pass

    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies:
        print(f"    [{a['kind']}] {a['url']}: {a['details']}")

    # STEP 5: Fetch changed/new pages
    print(f"\n[5] Fetching {len(added) + len(updated)} pages...")
    to_fetch = list(added.keys()) + list(updated.keys())

    # Capture prior markdown for updated pages
    prior_md: dict[str, str] = {}
    for url in updated:
        path = get_url_path(url)
        if path:
            full_path = REPO_ROOT / path
            try:
                result = subprocess.run(
                    ["git", "show", f"HEAD:{path}"],
                    capture_output=True, text=True, cwd=REPO_ROOT
                )
                if result.returncode == 0:
                    prior_md[url] = result.stdout
            except Exception:
                pass

    fetch_failures = []
    fetch_successes = []

    def do_fetch(url):
        path = get_url_path(url)
        if not path:
            return url, False, "Could not compute path"
        md_path = REPO_ROOT / path
        return fetch_page(url, md_path)

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(do_fetch, u): u for u in to_fetch}
        done = 0
        for fut in as_completed(futures):
            url, success, error = fut.result()
            done += 1
            if success:
                fetch_successes.append(url)
                if done % 10 == 0:
                    print(f"  ... {done}/{len(to_fetch)} done")
            else:
                fetch_failures.append({"url": url, "error": error})
                print(f"  FAIL: {url}: {error}")

    print(f"  Fetched: {len(fetch_successes)} ok, {len(fetch_failures)} failed")

    # STEP 6: Analyze changes
    print("\n[6] Analyzing changes...")

    def diff_markdown(url: str) -> str:
        """Get a simple text diff summary for an updated page."""
        old = prior_md.get(url, "")
        path = get_url_path(url)
        if not path:
            return "(path unknown)"
        new_path = REPO_ROOT / path
        try:
            new = new_path.read_text()
        except Exception:
            return "(could not read new file)"

        old_lines = set(old.splitlines())
        new_lines = set(new.splitlines())

        added_lines = [l for l in new.splitlines() if l and l not in old_lines and len(l) > 20][:5]
        removed_lines = [l for l in old.splitlines() if l and l not in new_lines and len(l) > 20][:5]

        parts = []
        if added_lines:
            parts.append("Added content: " + " | ".join(added_lines[:3]))
        if removed_lines:
            parts.append("Removed content: " + " | ".join(removed_lines[:3]))

        if not parts:
            # Check if only lastmod changed
            old_len = len(old)
            new_len = len(new)
            if abs(old_len - new_len) < 50:
                return f"Minor change (content length: {old_len} -> {new_len} chars)"
            return f"Content changed (length: {old_len} -> {new_len} chars)"

        return "; ".join(parts)

    # Get page summaries for new pages
    def get_page_summary(url: str) -> str:
        path = get_url_path(url)
        if not path:
            return "(unavailable)"
        full = REPO_ROOT / path
        try:
            text = full.read_text()
            # Take first 500 non-empty chars
            lines = [l.strip() for l in text.splitlines() if l.strip() and not l.startswith("#")]
            summary = " ".join(lines)[:500]
            return summary
        except Exception:
            return "(could not read)"

    # Categorize updates
    significant_updates = []
    routine_updates = []

    for url in sorted(updated.keys()):
        diff = diff_markdown(url)
        if "Minor change" in diff or ("length" in diff and abs(
            int(re.search(r'(\d+) ->', diff).group(1)) - int(re.search(r'-> (\d+)', diff).group(1))
        ) < 200 if re.search(r'(\d+) -> (\d+)', diff) else False):
            routine_updates.append((url, diff))
        else:
            significant_updates.append((url, diff))

    # STEP 7: Write analysis
    print("\n[7] Writing analysis...")

    analysis_lines = [
        f"# Analysis: {run_id}",
        "",
        f"**Fetch time:** {fetch_time}",
        f"**Baseline:** {prior_run_id}",
        f"**Total URLs:** {len(current_urls)}",
        f"**Added:** {len(added)} | **Updated:** {len(updated)} | **Removed:** {len(removed)} | **Anomalies:** {len(anomalies)}",
        "",
    ]

    if anomalies:
        analysis_lines += ["## Anomalies (Highest Signal)", ""]
        for a in anomalies:
            analysis_lines.append(f"- **[{a['kind']}]** `{a['url']}`")
            analysis_lines.append(f"  - {a['details']}")
        analysis_lines.append("")

    if significant_updates:
        analysis_lines += ["## Significant Updates", ""]
        for url, diff in significant_updates[:30]:
            path = get_url_path(url)
            analysis_lines.append(f"- **{url}**")
            analysis_lines.append(f"  - Change: {diff}")
            if url in updated:
                analysis_lines.append(f"  - lastmod: {updated[url]['old']} → {updated[url]['new']}")
        analysis_lines.append("")

    if routine_updates:
        analysis_lines += [f"## Routine Updates ({len(routine_updates)} pages)", ""]
        for url, diff in routine_updates[:20]:
            analysis_lines.append(f"- `{url}` ({diff})")
        if len(routine_updates) > 20:
            analysis_lines.append(f"- ... and {len(routine_updates)-20} more")
        analysis_lines.append("")

    if added:
        analysis_lines += ["## New Pages", ""]
        for url in sorted(added.keys()):
            summary = get_page_summary(url)
            path = get_url_path(url)
            analysis_lines.append(f"### {url}")
            analysis_lines.append(f"- **lastmod:** {added[url]}")
            analysis_lines.append(f"- **Path:** `{path}`")
            analysis_lines.append(f"- **Summary:** {summary[:300]}")
            analysis_lines.append("")

    if removed:
        analysis_lines += ["## Removed Pages", ""]
        for url in sorted(removed.keys()):
            analysis_lines.append(f"- `{url}` (lastmod was: {removed[url]})")
        analysis_lines.append("")

    if fetch_failures:
        analysis_lines += [f"## Fetch Failures ({len(fetch_failures)})", ""]
        for ff in fetch_failures:
            analysis_lines.append(f"- `{ff['url']}`: {ff['error']}")
        analysis_lines.append("")

    (run_dir / "analysis.md").write_text("\n".join(analysis_lines))
    print(f"  Written: runs/{run_id}/analysis.md")

    # STEP 8: Update README
    print("\n[8] Updating README...")

    readme_path = REPO_ROOT / "README.md"
    old_readme = readme_path.read_text() if readme_path.exists() else ""

    # Build new section
    tl_dr_parts = []
    if added:
        tl_dr_parts.append(f"{len(added)} new URL{'s' if len(added)>1 else ''}")
    if updated:
        tl_dr_parts.append(f"{len(updated)} updated page{'s' if len(updated)>1 else ''}")
    if removed:
        tl_dr_parts.append(f"{len(removed)} removed URL{'s' if len(removed)>1 else ''}")
    if not tl_dr_parts:
        tl_dr_parts.append("no changes detected")

    # Summary text
    notable_new = []
    for url in sorted(added.keys()):
        notable_new.append(f"  - [{url}]({url}) — lastmod {added[url]}")

    notable_updated = []
    for url, diff in significant_updates[:10]:
        notable_updated.append(f"  - [{url}]({url}): {diff[:120]}")

    new_section = f"""## {run_id}

**TL;DR:** {", ".join(tl_dr_parts)} across {len(current_urls):,} total tracked URLs."""

    if anomalies:
        new_section += f"\n\n**⚠️ Anomalies ({len(anomalies)}):**\n"
        for a in anomalies:
            new_section += f"- [{a['kind']}] `{a['url']}`: {a['details']}\n"

    if added:
        new_section += f"\n\n**New pages ({len(added)}):**\n"
        for url in sorted(added.keys())[:10]:
            path = get_url_path(url)
            rel_path = f"../{path}" if path else url
            new_section += f"- [{url}]({url}) ([snapshot]({rel_path}))\n"
        if len(added) > 10:
            new_section += f"- ... and {len(added)-10} more\n"

    if notable_updated:
        new_section += f"\n\n**Notable updates ({len(significant_updates)}):**\n"
        for line in notable_updated:
            new_section += f"{line}\n"
        if len(significant_updates) > 10:
            new_section += f"- ... and {len(significant_updates)-10} more\n"

    if removed:
        new_section += f"\n\n**Removed ({len(removed)}):**\n"
        for url in sorted(removed.keys()):
            new_section += f"- `{url}`\n"

    new_section += f"""
---
*Stats: {len(current_urls):,} total URLs | {len(added)} added | {len(updated)} updated | {len(removed)} removed | {len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps | {len(fetch_failures)} fetch failures*

"""

    # Prepend to README
    if "## " in old_readme:
        # Find first ## heading
        idx = old_readme.find("\n## ")
        if idx >= 0:
            header = old_readme[:idx+1]
            rest = old_readme[idx+1:]
            new_readme = header + new_section + rest
        else:
            new_readme = new_section + old_readme
    else:
        new_readme = (
            "# OpenAI.com Sitemap Monitor\n\n"
            "Daily tracking of changes to OpenAI's public website. Newest entries first.\n\n"
            + new_section + old_readme
        )

    readme_path.write_text(new_readme)
    print("  Written: README.md")

    # STEP 9: Update state/known_urls.json
    print("\n[9] Updating state...")

    for url, lastmod in current_urls.items():
        if url not in known_urls:
            known_urls[url] = {
                "first_seen": run_id,
                "last_seen": run_id,
                "current_lastmod": lastmod,
                "lastmod_history": [{"run_id": run_id, "lastmod": lastmod}] if lastmod else []
            }
        else:
            known_urls[url]["last_seen"] = run_id
            old_lm = known_urls[url].get("current_lastmod")
            if lastmod != old_lm:
                known_urls[url]["current_lastmod"] = lastmod
                known_urls[url].setdefault("lastmod_history", []).append({
                    "run_id": run_id, "lastmod": lastmod
                })

    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(known_urls, indent=2, sort_keys=True))
    print(f"  Updated state/known_urls.json ({len(known_urls)} URLs)")

    # STEP 10: Write diff.json
    print("\n[10] Writing diff.json...")
    diff_data = {
        "run_id": run_id,
        "fetch_time": fetch_time,
        "baseline": prior_run_id,
        "added": sorted(added.keys()),
        "removed": sorted(removed.keys()),
        "updated": [
            {"url": u, "old_lastmod": info["old"], "new_lastmod": info["new"]}
            for u, info in sorted(updated.items())
        ],
        "anomalies": anomalies,
        "fetch_failures": fetch_failures
    }
    (run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2))
    print(f"  Written: runs/{run_id}/diff.json")

    # Summary
    print(f"\n=== Run Complete ===")
    print(f"Run ID: {run_id}")
    print(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}")
    print(f"Anomalies: {len(anomalies)}, Fetch failures: {len(fetch_failures)}")

    return run_id, len(added), len(updated), len(removed), len(anomalies)

if __name__ == "__main__":
    main()
