#!/usr/bin/env python3
"""Daily monitoring run for openai.com sitemap changes."""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

import httpx

# ── Constants ──────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent
RUN_ID = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ")
FETCH_TIME = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Output dirs
SITEMAPS_DIR = REPO_ROOT / "sitemaps" / "openai.com"
SUB_LATEST_DIR = SITEMAPS_DIR / "sub" / "latest"
SUB_DATED_DIR = SITEMAPS_DIR / "sub" / RUN_ID
PAGES_DIR = REPO_ROOT / "pages" / "openai.com"
RUNS_DIR = REPO_ROOT / "runs" / RUN_ID
STATE_FILE = REPO_ROOT / "state" / "known_urls.json"

MAX_PAGE_WORKERS = 8

print(f"=== Run ID: {RUN_ID} ===")
print(f"Fetch time: {FETCH_TIME}")


# ── Helpers ────────────────────────────────────────────────────────────────────

def url_to_repo_path(url: str) -> str:
    """Canonical URL -> repo path via the shared module."""
    result = subprocess.run(
        ["python", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()


def sanitize_sub_name(loc: str) -> str:
    """Convert sub-sitemap URL to a safe filename."""
    parts = urlsplit(loc)
    path = parts.path.rstrip("/")
    name = path.replace("/", "_").lstrip("_") or "root"
    return name + ".xml"


def fetch_xml(url: str, retries: int = 3) -> bytes:
    """Fetch XML with retries."""
    for attempt in range(retries):
        try:
            resp = httpx.get(url, timeout=30, follow_redirects=True)
            resp.raise_for_status()
            return resp.content
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise
    raise RuntimeError(f"Failed to fetch {url}")


def parse_sitemap_index(content: bytes) -> list[str]:
    """Parse sitemap index and return list of sub-sitemap URLs."""
    root = ET.fromstring(content)
    locs = []
    for sitemap in root.findall("sm:sitemap", NS):
        loc = sitemap.findtext("sm:loc", namespaces=NS)
        if loc:
            locs.append(loc.strip())
    return locs


def parse_url_sitemap(content: bytes) -> dict[str, str | None]:
    """Parse a URL sitemap and return {url: lastmod}."""
    root = ET.fromstring(content)
    urls = {}
    for url_el in root.findall("sm:url", NS):
        loc = url_el.findtext("sm:loc", namespaces=NS)
        lastmod = url_el.findtext("sm:lastmod", namespaces=NS)
        if loc:
            urls[loc.strip()] = lastmod.strip() if lastmod else None
    return urls


def read_baseline() -> dict[str, str | None]:
    """Read all sub/latest/ sitemaps and return union of {url: lastmod}."""
    baseline = {}
    for xml_file in SUB_LATEST_DIR.glob("*.xml"):
        try:
            content = xml_file.read_bytes()
            urls = parse_url_sitemap(content)
            baseline.update(urls)
        except Exception as e:
            print(f"  Warning: could not parse {xml_file}: {e}")
    print(f"Baseline: {len(baseline)} URLs from {len(list(SUB_LATEST_DIR.glob('*.xml')))} sub-sitemaps")
    return baseline


def fetch_page_to_md(url: str, md_path: Path) -> tuple[bool, str]:
    """Fetch a page and convert to markdown. Returns (success, error_msg)."""
    md_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            ["python", "tools/html_to_md.py", "--url", url, "--output", str(md_path)],
            capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
        )
        if result.returncode != 0:
            return False, result.stderr.strip() or result.stdout.strip()
        # Sanity check
        if md_path.exists():
            content = md_path.read_text(encoding="utf-8", errors="replace")
            if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                return False, "Cloudflare challenge page or empty response"
            return True, ""
        return False, "Output file not created"
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)


def get_prior_md_content(md_path_str: str) -> str | None:
    """Get prior git HEAD content of a file."""
    result = subprocess.run(
        ["git", "show", f"HEAD:{md_path_str}"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode == 0:
        return result.stdout
    return None


def diff_markdown(old: str, new: str) -> str:
    """Compute a simple diff summary between old and new markdown."""
    old_lines = set(old.strip().splitlines())
    new_lines = set(new.strip().splitlines())
    added = [l for l in new_lines - old_lines if l.strip()]
    removed = [l for l in old_lines - new_lines if l.strip()]
    summary_parts = []
    if removed:
        sample = removed[:3]
        summary_parts.append(f"Removed lines (sample): {sample}")
    if added:
        sample = added[:3]
        summary_parts.append(f"Added lines (sample): {sample}")
    if not summary_parts:
        return "No substantive text changes (whitespace/ordering only)"
    return "; ".join(summary_parts)


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2))


# ── Main Run ───────────────────────────────────────────────────────────────────

def main():
    # ── Step 1: Read baseline ──
    print("\n[1/10] Reading baseline...")
    baseline = read_baseline()

    # ── Step 2: Fetch + snapshot current sitemaps ──
    print("\n[2/10] Fetching current sitemaps...")

    # Fetch index
    print(f"  Fetching index: {SITEMAP_INDEX_URL}")
    index_content = fetch_xml(SITEMAP_INDEX_URL)
    sub_urls = parse_sitemap_index(index_content)
    print(f"  Found {len(sub_urls)} sub-sitemaps")

    # Save index
    dated_index_path = SITEMAPS_DIR / f"{RUN_ID}.xml"
    dated_index_path.write_bytes(index_content)
    (SITEMAPS_DIR / "latest.xml").write_bytes(index_content)
    print(f"  Saved index to {dated_index_path}")

    # Fetch sub-sitemaps
    SUB_DATED_DIR.mkdir(parents=True, exist_ok=True)
    current_urls: dict[str, str | None] = {}
    sub_url_to_file: dict[str, str] = {}

    for sub_url in sub_urls:
        safe_name = sanitize_sub_name(sub_url)
        try:
            content = fetch_xml(sub_url)
            urls = parse_url_sitemap(content)
            current_urls.update(urls)
            # Save dated
            dated_path = SUB_DATED_DIR / safe_name
            dated_path.write_bytes(content)
            # Save latest
            (SUB_LATEST_DIR / safe_name).write_bytes(content)
            sub_url_to_file[sub_url] = safe_name
            print(f"  {safe_name}: {len(urls)} URLs")
        except Exception as e:
            print(f"  ERROR fetching {sub_url}: {e}")

    print(f"  Total current URLs: {len(current_urls)}")

    # ── Step 3: Diff ──
    print("\n[3/10] Diffing...")
    baseline_set = set(baseline.keys())
    current_set = set(current_urls.keys())

    added_urls = sorted(current_set - baseline_set)
    removed_urls = sorted(baseline_set - current_set)
    updated_urls = []
    for url in current_set & baseline_set:
        old_lm = baseline.get(url)
        new_lm = current_urls.get(url)
        if old_lm != new_lm:
            updated_urls.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

    print(f"  Added:   {len(added_urls)}")
    print(f"  Removed: {len(removed_urls)}")
    print(f"  Updated: {len(updated_urls)}")

    # ── Step 4: Anomaly detection ──
    print("\n[4/10] Anomaly detection...")
    state = load_state()
    anomalies = []
    fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

    # Check future lastmod
    for url, lastmod in current_urls.items():
        if lastmod:
            try:
                lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
                if lm_dt.tzinfo is None:
                    lm_dt = lm_dt.replace(tzinfo=timezone.utc)
                if lm_dt > fetch_dt:
                    anomalies.append({
                        "kind": "future_lastmod",
                        "url": url,
                        "details": f"lastmod={lastmod} is after fetch time {FETCH_TIME}"
                    })
            except ValueError:
                pass

    # Check lastmod moved backwards
    for item in updated_urls:
        old_lm = item["old_lastmod"]
        new_lm = item["new_lastmod"]
        if old_lm and new_lm:
            try:
                old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
                new_dt = datetime.fromisoformat(new_lm.replace("Z", "+00:00"))
                if old_dt.tzinfo is None:
                    old_dt = old_dt.replace(tzinfo=timezone.utc)
                if new_dt.tzinfo is None:
                    new_dt = new_dt.replace(tzinfo=timezone.utc)
                if new_dt < old_dt:
                    anomalies.append({
                        "kind": "lastmod_moved_backwards",
                        "url": item["url"],
                        "details": f"old={old_lm} → new={new_lm}"
                    })
            except ValueError:
                pass

    # Check new URLs with backdated lastmod
    for url in added_urls:
        lastmod = current_urls.get(url)
        first_seen_str = RUN_ID  # They're new now
        if lastmod:
            try:
                lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
                if lm_dt.tzinfo is None:
                    lm_dt = lm_dt.replace(tzinfo=timezone.utc)
                # If lastmod is more than 30 days before now
                age_days = (fetch_dt - lm_dt).days
                if age_days > 30:
                    anomalies.append({
                        "kind": "new_url_backdated_lastmod",
                        "url": url,
                        "details": f"New URL but lastmod={lastmod} is {age_days} days old"
                    })
            except ValueError:
                pass

    # Check reappeared URLs
    for url in added_urls:
        if url in state and state[url].get("last_seen"):
            # URL was previously known, disappeared, now back
            prior_last_seen = state[url].get("last_seen", "")
            if prior_last_seen and prior_last_seen < (datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ")):
                anomalies.append({
                    "kind": "url_reappeared",
                    "url": url,
                    "details": f"URL was previously seen (last_seen={prior_last_seen}), disappeared, now back"
                })

    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies:
        print(f"    [{a['kind']}] {a['url'][:80]}")

    # ── Step 5: Fetch + convert changed pages ──
    print("\n[5/10] Fetching changed/new pages...")
    urls_to_fetch = added_urls + [item["url"] for item in updated_urls]
    print(f"  Pages to fetch: {len(urls_to_fetch)}")

    fetch_failures = []
    page_diffs = {}  # url -> diff summary for updated pages
    prior_contents = {}  # url -> prior md content

    # Capture prior content for updated pages
    for item in updated_urls:
        url = item["url"]
        md_path_str = url_to_repo_path(url)
        prior = get_prior_md_content(md_path_str)
        if prior:
            prior_contents[url] = prior

    # Fetch pages in batches
    import concurrent.futures

    def fetch_one(url: str) -> tuple[str, bool, str]:
        md_path_str = url_to_repo_path(url)
        if not md_path_str:
            return url, False, "Could not compute path"
        md_path = REPO_ROOT / md_path_str
        success, error = fetch_page_to_md(url, md_path)
        return url, success, error

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_PAGE_WORKERS) as executor:
        futures = {executor.submit(fetch_one, url): url for url in urls_to_fetch}
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            url, success, error = future.result()
            if success:
                short_url = url[len("https://openai.com"):][:60]
                print(f"  [{i}/{len(urls_to_fetch)}] OK: {short_url}")
            else:
                print(f"  [{i}/{len(urls_to_fetch)}] FAIL: {url[:60]}: {error}")
                fetch_failures.append({"url": url, "error": error})

    # ── Step 6: Analyze diffs for updated pages ──
    print("\n[6/10] Analyzing page diffs...")
    for item in updated_urls:
        url = item["url"]
        md_path_str = url_to_repo_path(url)
        if not md_path_str:
            continue
        md_path = REPO_ROOT / md_path_str
        if url in prior_contents and md_path.exists():
            new_content = md_path.read_text(encoding="utf-8", errors="replace")
            diff_summary = diff_markdown(prior_contents[url], new_content)
            page_diffs[url] = diff_summary

    # ── Step 7: Write analysis ──
    print("\n[7/10] Writing analysis...")
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    analysis_lines = [
        f"# Analysis: {RUN_ID}",
        f"",
        f"**Fetch time:** {FETCH_TIME}  ",
        f"**Total URLs in current sitemap:** {len(current_urls)}  ",
        f"**Baseline URLs:** {len(baseline)}  ",
        f"",
        f"## Summary",
        f"",
        f"- Added: {len(added_urls)}",
        f"- Removed: {len(removed_urls)}",
        f"- Updated: {len(updated_urls)}",
        f"- Anomalies: {len(anomalies)}",
        f"- Fetch failures: {len(fetch_failures)}",
        f"",
    ]

    if anomalies:
        analysis_lines += [
            "## Anomalies (High Signal)",
            "",
        ]
        for a in anomalies:
            analysis_lines.append(f"### [{a['kind']}]")
            analysis_lines.append(f"- URL: {a['url']}")
            analysis_lines.append(f"- Details: {a['details']}")
            analysis_lines.append("")

    if updated_urls:
        analysis_lines += [
            "## Updated Pages",
            "",
        ]
        for item in updated_urls:
            url = item["url"]
            analysis_lines.append(f"### {url}")
            analysis_lines.append(f"- lastmod: `{item['old_lastmod']}` → `{item['new_lastmod']}`")
            if url in page_diffs:
                analysis_lines.append(f"- Content diff: {page_diffs[url]}")
            analysis_lines.append("")

    if added_urls:
        analysis_lines += [
            "## New Pages",
            "",
        ]
        for url in added_urls:
            lastmod = current_urls.get(url)
            md_path_str = url_to_repo_path(url)
            md_path = REPO_ROOT / md_path_str if md_path_str else None
            # Get a brief summary from the markdown
            summary = ""
            if md_path and md_path.exists():
                content = md_path.read_text(encoding="utf-8", errors="replace")
                # Take first 300 chars as summary
                lines = [l.strip() for l in content.splitlines() if l.strip()]
                summary = " ".join(lines[:5])[:300]
            analysis_lines.append(f"### {url}")
            analysis_lines.append(f"- lastmod: {lastmod}")
            analysis_lines.append(f"- path: {md_path_str}")
            if summary:
                analysis_lines.append(f"- Summary: {summary[:200]}")
            analysis_lines.append("")

    if removed_urls:
        analysis_lines += [
            "## Removed Pages",
            "",
        ]
        for url in removed_urls:
            analysis_lines.append(f"- {url}")
        analysis_lines.append("")

    if fetch_failures:
        analysis_lines += [
            "## Fetch Failures (needs follow-up)",
            "",
        ]
        for ff in fetch_failures:
            analysis_lines.append(f"- {ff['url']}: {ff['error']}")
        analysis_lines.append("")

    analysis_text = "\n".join(analysis_lines)
    (RUNS_DIR / "analysis.md").write_text(analysis_text)
    print(f"  Written: {RUNS_DIR / 'analysis.md'}")

    # ── Step 8: Update README ──
    print("\n[8/10] Updating README...")
    readme_path = REPO_ROOT / "README.md"
    existing_readme = readme_path.read_text() if readme_path.exists() else ""

    # Build new section
    def fmt_url_link(url: str, md_path_str: str) -> str:
        """Format as markdown link."""
        label = url.replace("https://openai.com", "")
        return f"[{label}]({md_path_str})"

    new_section_lines = [
        f"## {RUN_ID}",
        f"",
        f"**TL;DR:** Today's run (fetched {FETCH_TIME}) found {len(added_urls)} new URLs, "
        f"{len(updated_urls)} updated, and {len(removed_urls)} removed out of {len(current_urls)} total "
        f"across {len(sub_urls)} sub-sitemaps. "
        + (f"**{len(anomalies)} anomalies detected — see below.**" if anomalies else "No anomalies detected."),
        f"",
    ]

    if anomalies:
        new_section_lines += ["### Anomalies", ""]
        for a in anomalies:
            new_section_lines.append(f"- **[{a['kind']}]** `{a['url']}` — {a['details']}")
        new_section_lines.append("")

    if added_urls:
        new_section_lines += [f"### New Pages ({len(added_urls)})", ""]
        for url in added_urls[:30]:  # cap at 30 for readability
            md_path_str = url_to_repo_path(url)
            lastmod = current_urls.get(url, "")
            md_path = REPO_ROOT / md_path_str if md_path_str else None
            # Get first heading from md
            summary = ""
            if md_path and md_path.exists():
                content = md_path.read_text(encoding="utf-8", errors="replace")
                for line in content.splitlines():
                    line = line.strip()
                    if line.startswith("#"):
                        summary = line.lstrip("#").strip()
                        break
                if not summary:
                    lines = [l.strip() for l in content.splitlines() if l.strip()]
                    summary = lines[0][:100] if lines else ""
            entry = f"- [{url.replace('https://openai.com','')}]({md_path_str})"
            if summary:
                entry += f" — {summary[:100]}"
            if lastmod:
                entry += f" (lastmod: {lastmod})"
            new_section_lines.append(entry)
        if len(added_urls) > 30:
            new_section_lines.append(f"- _...and {len(added_urls)-30} more_")
        new_section_lines.append("")

    if updated_urls:
        new_section_lines += [f"### Updated Pages ({len(updated_urls)})", ""]
        for item in updated_urls[:20]:
            url = item["url"]
            md_path_str = url_to_repo_path(url)
            diff = page_diffs.get(url, "")
            entry = f"- [{url.replace('https://openai.com','')}]({md_path_str}) — lastmod `{item['old_lastmod']}` → `{item['new_lastmod']}`"
            if diff and diff != "No substantive text changes (whitespace/ordering only)":
                entry += f"; {diff[:120]}"
            new_section_lines.append(entry)
        if len(updated_urls) > 20:
            new_section_lines.append(f"- _...and {len(updated_urls)-20} more_")
        new_section_lines.append("")

    if removed_urls:
        new_section_lines += [f"### Removed Pages ({len(removed_urls)})", ""]
        for url in removed_urls[:20]:
            new_section_lines.append(f"- `{url}`")
        if len(removed_urls) > 20:
            new_section_lines.append(f"- _...and {len(removed_urls)-20} more_")
        new_section_lines.append("")

    if fetch_failures:
        new_section_lines += [f"### Fetch Failures ({len(fetch_failures)})", ""]
        for ff in fetch_failures[:10]:
            new_section_lines.append(f"- `{ff['url']}`: {ff['error']}")
        new_section_lines.append("")

    new_section_lines += [
        f"**Stats:** {len(current_urls)} total URLs | "
        f"{len(added_urls)} added | {len(updated_urls)} updated | "
        f"{len(removed_urls)} removed | {len(anomalies)} anomalies | "
        f"{len(sub_urls)} sub-sitemaps",
        "",
        "---",
        "",
    ]

    new_section = "\n".join(new_section_lines)

    # Prepend to README (after the first line/header if there is one)
    if existing_readme.startswith("# "):
        # Find end of first header section
        lines = existing_readme.split("\n")
        insert_at = 0
        for i, line in enumerate(lines):
            if i > 0 and line.startswith("## "):
                insert_at = i
                break
            elif i > 3:  # After a few lines, just insert
                insert_at = i
                break
        if insert_at == 0:
            insert_at = len(lines)
        new_readme = "\n".join(lines[:insert_at]) + "\n\n" + new_section + "\n".join(lines[insert_at:])
    else:
        new_readme = new_section + existing_readme

    readme_path.write_text(new_readme)
    print(f"  README.md updated")

    # ── Step 9: Update state/known_urls.json ──
    print("\n[9/10] Updating state...")
    for url in current_urls:
        lastmod = current_urls[url]
        if url not in state:
            state[url] = {
                "first_seen": RUN_ID,
                "last_seen": RUN_ID,
                "current_lastmod": lastmod,
                "lastmod_history": [{"run_id": RUN_ID, "lastmod": lastmod}] if lastmod else []
            }
        else:
            state[url]["last_seen"] = RUN_ID
            old_lm = state[url].get("current_lastmod")
            if old_lm != lastmod:
                state[url]["current_lastmod"] = lastmod
                if "lastmod_history" not in state[url]:
                    state[url]["lastmod_history"] = []
                state[url]["lastmod_history"].append({"run_id": RUN_ID, "lastmod": lastmod})
    save_state(state)
    print(f"  State: {len(state)} URLs")

    # ── Step 10: Write diff.json ──
    print("\n[10/10] Writing diff.json...")
    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": None,  # Will be filled from latest run
        "added": added_urls,
        "removed": removed_urls,
        "updated": updated_urls,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures,
    }

    # Find prior run_id from sitemaps directory
    prior_runs = sorted([
        f.stem for f in SITEMAPS_DIR.glob("*.xml")
        if f.stem != "latest" and f.stem != RUN_ID
    ])
    if prior_runs:
        diff_data["baseline"] = prior_runs[-1]

    (RUNS_DIR / "diff.json").write_text(json.dumps(diff_data, indent=2))
    print(f"  Written: {RUNS_DIR / 'diff.json'}")

    print(f"\n=== Run complete: {RUN_ID} ===")
    print(f"Added: {len(added_urls)}, Updated: {len(updated_urls)}, Removed: {len(removed_urls)}, Anomalies: {len(anomalies)}")
    return diff_data


if __name__ == "__main__":
    TZ = "UTC"
    os.environ["TZ"] = TZ
    main()
