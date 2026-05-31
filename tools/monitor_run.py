#!/usr/bin/env python3
"""
Full monitoring run script for OpenAI sitemap tracking.
Usage: python tools/monitor_run.py <run_id>
"""

import os
import sys
import json
import re
import subprocess
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import concurrent.futures

try:
    import httpx
except ImportError:
    httpx = None

REPO_ROOT = Path(__file__).parent.parent
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"


def get_run_id():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ")


def fetch_xml(url: str) -> str:
    """Fetch XML with plain httpx (sitemaps don't need curl-cffi)."""
    import httpx as hx
    resp = hx.get(url, timeout=30, follow_redirects=True,
                  headers={"User-Agent": "Mozilla/5.0 OpenAI-Sitemap-Monitor/1.0"})
    resp.raise_for_status()
    return resp.text


def parse_sitemap_index(xml_text: str) -> list[str]:
    """Return list of sub-sitemap URLs from a sitemap index."""
    root = ET.fromstring(xml_text)
    urls = []
    for sitemap in root.findall(f"{{{SITEMAP_NS}}}sitemap"):
        loc = sitemap.findtext(f"{{{SITEMAP_NS}}}loc")
        if loc:
            urls.append(loc.strip())
    return urls


def parse_urlset(xml_text: str) -> dict[str, str | None]:
    """Return {url: lastmod_or_None} from a urlset sitemap."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return {}
    result = {}
    for url_el in root.findall(f"{{{SITEMAP_NS}}}url"):
        loc = url_el.findtext(f"{{{SITEMAP_NS}}}loc")
        lastmod = url_el.findtext(f"{{{SITEMAP_NS}}}lastmod")
        if loc:
            result[loc.strip()] = lastmod.strip() if lastmod else None
    return result


def sanitize_filename(url: str) -> str:
    """Convert sub-sitemap URL to a safe filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> _openai.com_sitemap.xml_page.xml
    parsed = urlparse(url)
    path = parsed.netloc + parsed.path
    path = path.rstrip("/")
    safe = re.sub(r"[^\w.\-]", "_", path)
    if not safe.endswith(".xml"):
        safe += ".xml"
    return safe


def load_baseline(run_id: str) -> dict[str, str | None]:
    """Load all URLs from the most recent prior run's sub-sitemaps as the baseline.

    We use the dated subdirectory (not sub/latest/) because sub/latest/ is
    overwritten during the current run's fetch step. We find the most recent
    dated directory that is not the current run_id.
    """
    sub_base = REPO_ROOT / "sitemaps" / "openai.com" / "sub"
    baseline = {}
    if not sub_base.exists():
        return baseline

    # Find the most recent prior dated directory
    dated_dirs = sorted(
        [d for d in sub_base.iterdir() if d.is_dir() and d.name != "latest" and d.name < run_id],
        reverse=True
    )
    if not dated_dirs:
        print("  No prior dated sub-sitemap directory found; baseline is empty.")
        return baseline

    prior_dir = dated_dirs[0]
    print(f"  Loading baseline from: {prior_dir.name}")

    for f in prior_dir.glob("*.xml"):
        try:
            text = f.read_text(encoding="utf-8")
            urls = parse_urlset(text)
            for url, lastmod in urls.items():
                if url not in baseline:
                    baseline[url] = lastmod
        except Exception as e:
            print(f"  Warning: could not parse {f.name}: {e}")

    return baseline


def url_to_md_path(url: str) -> Path:
    """Convert a URL to its markdown path in the repo."""
    result = subprocess.run(
        ["python3", str(REPO_ROOT / "tools" / "url_path.py"), url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    rel = result.stdout.strip()
    if not rel:
        # Fallback
        parsed = urlparse(url)
        path = parsed.path
        if path.endswith("/"):
            rel = f"pages/openai.com{path}index.md"
        elif "." not in path.split("/")[-1]:
            rel = f"pages/openai.com{path}.md"
        else:
            rel = f"pages/openai.com{path}"
    return REPO_ROOT / rel


def fetch_page(url: str, out_path: Path) -> tuple[bool, str]:
    """Fetch a page via html_to_md.py. Returns (success, error_msg)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["python3", str(REPO_ROOT / "tools" / "html_to_md.py"),
         "--url", url, "--output", str(out_path)],
        capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
    )
    if result.returncode != 0:
        return False, result.stderr.strip() or result.stdout.strip()
    if not out_path.exists():
        return False, "Output file not created"
    content = out_path.read_text(encoding="utf-8", errors="replace")
    if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
        return False, f"Blocked (content={len(content)} chars)"
    return True, ""


def get_prior_md(path: Path) -> str | None:
    """Get the prior version of a file from git."""
    rel = path.relative_to(REPO_ROOT)
    result = subprocess.run(
        ["git", "show", f"HEAD:{rel}"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode == 0:
        return result.stdout
    return None


def diff_markdown(old: str, new: str) -> list[str]:
    """Return meaningful diff lines (additions/deletions, ignoring whitespace noise)."""
    old_lines = set(l.strip() for l in old.splitlines() if l.strip())
    new_lines = set(l.strip() for l in new.splitlines() if l.strip())
    added = [l for l in new_lines - old_lines if len(l) > 20]
    removed = [l for l in old_lines - new_lines if len(l) > 20]
    return added[:30], removed[:30]


def summarize_md(md_path: Path) -> str:
    """Get a short summary of a markdown file."""
    if not md_path.exists():
        return "(file not found)"
    text = md_path.read_text(encoding="utf-8", errors="replace")
    # Find first substantial paragraph
    lines = [l.strip() for l in text.splitlines() if l.strip() and not l.startswith("#")]
    lines = [l for l in lines if len(l) > 40]
    return " ".join(lines[:3])[:400] if lines else text[:400]


def detect_anomalies(
    baseline: dict[str, str | None],
    current: dict[str, str | None],
    fetch_time: datetime,
    known_state: dict
) -> list[dict]:
    """Detect anomalies in the sitemap data."""
    anomalies = []
    fetch_ts = fetch_time.isoformat()

    for url, lastmod in current.items():
        if lastmod is None:
            continue

        try:
            lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
        except ValueError:
            continue

        # Future lastmod
        if lm_dt > fetch_time:
            anomalies.append({
                "kind": "future_lastmod",
                "url": url,
                "details": f"lastmod={lastmod} is later than fetch time {fetch_ts}"
            })

        # Backward lastmod
        if url in baseline and baseline[url] and lastmod:
            old_lm = baseline[url]
            if old_lm and lastmod < old_lm:
                anomalies.append({
                    "kind": "backward_lastmod",
                    "url": url,
                    "details": f"lastmod moved backward: {old_lm} -> {lastmod}"
                })

        # Backdated new URL
        if url not in baseline and url in known_state:
            state_entry = known_state[url]
            first_seen_id = state_entry.get("first_seen", "")
            if first_seen_id:
                try:
                    first_seen_dt = datetime.strptime(first_seen_id, "%Y-%m-%dT%H-%MZ").replace(tzinfo=timezone.utc)
                    days_diff = (first_seen_dt - lm_dt).days
                    if days_diff > 7:
                        anomalies.append({
                            "kind": "backdated_url",
                            "url": url,
                            "details": f"New URL but lastmod={lastmod} predates first_seen={first_seen_id} by {days_diff} days"
                        })
                except ValueError:
                    pass

        # Disappeared and reappeared: only flag if the URL was absent from the
        # immediately-prior dated baseline (not just any prior run). We check
        # known_state.last_seen vs the prior run_id to avoid false positives.
        if url not in baseline and url in known_state:
            st = known_state[url]
            last_seen = st.get("last_seen", "")
            # Only flag as reappeared if last_seen matches the immediately prior run
            # (i.e., URL was present last run but vanished from that run's baseline)
            # Since we now use the dated baseline, url not in baseline means it was
            # genuinely absent from the prior run's sitemap snapshot.
            if last_seen and last_seen < run_id:
                anomalies.append({
                    "kind": "reappeared_url",
                    "url": url,
                    "details": f"URL absent from prior run ({last_seen} baseline) but present now — possible brief removal or sitemap gap"
                })

    return anomalies


def main():
    run_id = get_run_id()
    fetch_time = datetime.now(timezone.utc)
    print(f"\n=== OpenAI Sitemap Monitor Run: {run_id} ===")
    print(f"Fetch time: {fetch_time.isoformat()}")

    # --- STEP 1: BASELINE ---
    print("\n[1] Loading baseline...")
    baseline = load_baseline(run_id)
    print(f"  Baseline URLs: {len(baseline)}")

    # Load known_urls state
    state_path = REPO_ROOT / "state" / "known_urls.json"
    if state_path.exists():
        with open(state_path) as f:
            known_state = json.load(f)
    else:
        known_state = {}
    print(f"  Known state URLs: {len(known_state)}")

    # --- STEP 2: FETCH + SNAPSHOT ---
    print("\n[2] Fetching sitemap index...")
    try:
        index_xml = fetch_xml(SITEMAP_INDEX_URL)
    except Exception as e:
        print(f"  FATAL: Could not fetch sitemap index: {e}")
        # Write failure record
        run_dir = REPO_ROOT / "runs" / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        (run_dir / "analysis.md").write_text(
            f"# Run {run_id}\n\n**FATAL ERROR**: Could not fetch sitemap index.\n\nError: {e}\n"
        )
        return 1

    # Save root index
    root_sitemap_dir = REPO_ROOT / "sitemaps" / "openai.com"
    root_sitemap_dir.mkdir(parents=True, exist_ok=True)
    (root_sitemap_dir / f"{run_id}.xml").write_text(index_xml, encoding="utf-8")
    (root_sitemap_dir / "latest.xml").write_text(index_xml, encoding="utf-8")
    print(f"  Saved root index ({len(index_xml)} chars)")

    # Parse sub-sitemap URLs
    sub_urls = parse_sitemap_index(index_xml)
    print(f"  Found {len(sub_urls)} sub-sitemaps")

    # Fetch all sub-sitemaps
    sub_dir_dated = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / run_id
    sub_dir_latest = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / "latest"
    sub_dir_dated.mkdir(parents=True, exist_ok=True)
    sub_dir_latest.mkdir(parents=True, exist_ok=True)

    # Clear old "latest" files that match our naming convention to avoid stale data
    # (We'll overwrite/add as we go)

    current_urls: dict[str, str | None] = {}  # url -> lastmod
    url_to_subsitemap: dict[str, str] = {}    # url -> sub-sitemap name

    def fetch_sub(sub_url):
        try:
            xml_text = fetch_xml(sub_url)
            return sub_url, xml_text, None
        except Exception as e:
            return sub_url, None, str(e)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        futures = {ex.submit(fetch_sub, u): u for u in sub_urls}
        for future in concurrent.futures.as_completed(futures):
            sub_url, xml_text, err = future.result()
            fname = sanitize_filename(sub_url)
            if err:
                print(f"  WARNING: Failed to fetch {sub_url}: {err}")
                continue
            # Save
            (sub_dir_dated / fname).write_text(xml_text, encoding="utf-8")
            (sub_dir_latest / fname).write_text(xml_text, encoding="utf-8")
            # Parse
            urls = parse_urlset(xml_text)
            sub_name = sub_url.rstrip("/").split("/")[-1]
            for url, lastmod in urls.items():
                current_urls[url] = lastmod
                url_to_subsitemap[url] = sub_name

    print(f"  Total current URLs: {len(current_urls)}")

    # --- STEP 3: DIFF ---
    print("\n[3] Computing diff...")
    baseline_set = set(baseline.keys())
    current_set = set(current_urls.keys())

    added_urls = sorted(current_set - baseline_set)
    removed_urls = sorted(baseline_set - current_set)
    updated_urls = []

    for url in current_set & baseline_set:
        old_lm = baseline[url]
        new_lm = current_urls[url]
        if old_lm != new_lm:
            updated_urls.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

    print(f"  Added: {len(added_urls)}, Removed: {len(removed_urls)}, Updated: {len(updated_urls)}")

    # --- STEP 4: ANOMALY DETECTION ---
    print("\n[4] Detecting anomalies...")
    anomalies = detect_anomalies(baseline, current_urls, fetch_time, known_state)
    print(f"  Anomalies: {len(anomalies)}")
    for a in anomalies:
        print(f"    [{a['kind']}] {a['url'][:80]}")

    # --- STEP 5: FETCH + CONVERT changed/new pages ---
    print("\n[5] Fetching page content for new/updated URLs...")
    pages_to_fetch = [(u, "added") for u in added_urls] + \
                     [(e["url"], "updated") for e in updated_urls]

    # Capture prior markdown for updated pages before overwriting
    prior_mds: dict[str, str | None] = {}
    for url, reason in pages_to_fetch:
        if reason == "updated":
            md_path = url_to_md_path(url)
            prior_mds[url] = get_prior_md(md_path)

    fetch_failures = []
    fetch_results: dict[str, bool] = {}

    def do_fetch(args):
        url, reason = args
        md_path = url_to_md_path(url)
        # If updated and we have prior, save it temporarily
        try:
            ok, err = fetch_page(url, md_path)
            return url, ok, err
        except Exception as e:
            return url, False, str(e)

    # Modest parallelism for Cloudflare
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(do_fetch, args): args for args in pages_to_fetch}
        done = 0
        for future in concurrent.futures.as_completed(futures):
            url, ok, err = future.result()
            fetch_results[url] = ok
            done += 1
            if not ok:
                fetch_failures.append({"url": url, "error": err})
                print(f"  [{done}/{len(pages_to_fetch)}] FAIL {url[:70]}: {err[:60]}")
            else:
                print(f"  [{done}/{len(pages_to_fetch)}] OK   {url[:70]}")

    print(f"  Fetch successes: {sum(1 for v in fetch_results.values() if v)}/{len(fetch_results)}")
    print(f"  Fetch failures: {len(fetch_failures)}")

    # --- STEP 6: ANALYZE ---
    print("\n[6] Analyzing changes...")

    analysis_sections = {
        "anomalies": [],
        "updated": [],
        "new": [],
        "removed": [],
        "failures": [],
    }

    # Analyze updated pages
    for entry in updated_urls:
        url = entry["url"]
        if not fetch_results.get(url, False):
            continue
        md_path = url_to_md_path(url)
        prior = prior_mds.get(url)
        if prior:
            new_text = md_path.read_text(encoding="utf-8", errors="replace") if md_path.exists() else ""
            added_lines, removed_lines = diff_markdown(prior, new_text)
            analysis_sections["updated"].append({
                "url": url,
                "old_lastmod": entry["old_lastmod"],
                "new_lastmod": entry["new_lastmod"],
                "added_lines": added_lines[:10],
                "removed_lines": removed_lines[:10],
            })
        else:
            analysis_sections["updated"].append({
                "url": url,
                "old_lastmod": entry["old_lastmod"],
                "new_lastmod": entry["new_lastmod"],
                "added_lines": [],
                "removed_lines": [],
            })

    # Analyze new pages
    for url in added_urls:
        md_path = url_to_md_path(url)
        summary = summarize_md(md_path) if fetch_results.get(url) else "(fetch failed)"
        analysis_sections["new"].append({
            "url": url,
            "lastmod": current_urls.get(url),
            "summary": summary,
            "subsitemap": url_to_subsitemap.get(url, "unknown"),
        })

    # Record removals
    for url in removed_urls:
        analysis_sections["removed"].append({
            "url": url,
            "last_lastmod": baseline.get(url),
        })

    # Record anomalies
    analysis_sections["anomalies"] = anomalies

    # Record failures
    analysis_sections["failures"] = fetch_failures

    # --- STEP 7: WRITE analysis.md ---
    print("\n[7] Writing analysis.md...")
    run_dir = REPO_ROOT / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    analysis_md_parts = [f"# Analysis: {run_id}\n"]
    analysis_md_parts.append(f"**Fetch time:** {fetch_time.isoformat()}\n")
    analysis_md_parts.append(f"**Stats:** {len(current_urls)} total URLs | "
                              f"{len(added_urls)} added | {len(updated_urls)} updated | "
                              f"{len(removed_urls)} removed | {len(anomalies)} anomalies | "
                              f"{len(fetch_failures)} fetch failures\n")

    # Anomalies section
    analysis_md_parts.append("\n## Anomalies\n")
    if anomalies:
        for a in anomalies:
            analysis_md_parts.append(f"- **{a['kind']}**: {a['url']}\n  {a['details']}\n")
    else:
        analysis_md_parts.append("None detected.\n")

    # Notable Updates
    analysis_md_parts.append("\n## Updated Pages (with content changes)\n")
    notable_updates = [e for e in analysis_sections["updated"] if e["added_lines"] or e["removed_lines"]]
    routine_updates = [e for e in analysis_sections["updated"] if not e["added_lines"] and not e["removed_lines"]]

    if notable_updates:
        for e in notable_updates[:30]:
            analysis_md_parts.append(f"### {e['url']}\n")
            analysis_md_parts.append(f"- lastmod: `{e['old_lastmod']}` → `{e['new_lastmod']}`\n")
            if e["added_lines"]:
                analysis_md_parts.append("- **Added content:**\n")
                for l in e["added_lines"][:5]:
                    analysis_md_parts.append(f"  - {l[:150]}\n")
            if e["removed_lines"]:
                analysis_md_parts.append("- **Removed content:**\n")
                for l in e["removed_lines"][:5]:
                    analysis_md_parts.append(f"  - {l[:150]}\n")
    else:
        analysis_md_parts.append("No substantive content differences detected in updated pages.\n")

    if routine_updates:
        analysis_md_parts.append(f"\n**Routine lastmod-only updates (no text diff available):** {len(routine_updates)} pages\n")

    # New Pages
    analysis_md_parts.append("\n## New Pages\n")
    if analysis_sections["new"]:
        for n in analysis_sections["new"]:
            rel_path = url_to_md_path(n["url"]).relative_to(REPO_ROOT)
            analysis_md_parts.append(f"### {n['url']}\n")
            analysis_md_parts.append(f"- Sub-sitemap: `{n['subsitemap']}`\n")
            analysis_md_parts.append(f"- lastmod: `{n['lastmod']}`\n")
            analysis_md_parts.append(f"- Path: `{rel_path}`\n")
            analysis_md_parts.append(f"- Summary: {n['summary'][:300]}\n")
    else:
        analysis_md_parts.append("No new pages.\n")

    # Removals
    analysis_md_parts.append("\n## Removed Pages\n")
    if analysis_sections["removed"]:
        for r in analysis_sections["removed"]:
            analysis_md_parts.append(f"- `{r['url']}` (last lastmod: {r['last_lastmod']})\n")
    else:
        analysis_md_parts.append("No pages removed.\n")

    # Fetch failures
    if fetch_failures:
        analysis_md_parts.append("\n## Fetch Failures (needs follow-up)\n")
        for f in fetch_failures:
            analysis_md_parts.append(f"- `{f['url']}`: {f['error']}\n")

    analysis_text = "".join(analysis_md_parts)
    (run_dir / "analysis.md").write_text(analysis_text, encoding="utf-8")
    print("  Wrote analysis.md")

    # --- STEP 8: UPDATE README.md ---
    print("\n[8] Updating README.md...")
    readme_path = REPO_ROOT / "README.md"
    old_readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

    # Build the new section
    new_section_parts = [f"\n## {run_id}\n\n"]

    # TL;DR
    tldr_parts = []
    if added_urls:
        tldr_parts.append(f"{len(added_urls)} new URL{'s' if len(added_urls)!=1 else ''} added")
    if updated_urls:
        tldr_parts.append(f"{len(updated_urls)} page{'s' if len(updated_urls)!=1 else ''} updated")
    if removed_urls:
        tldr_parts.append(f"{len(removed_urls)} URL{'s' if len(removed_urls)!=1 else ''} removed")
    if not tldr_parts:
        tldr_parts.append("no structural changes")

    new_section_parts.append(f"**TL;DR:** This run found {', '.join(tldr_parts)} in OpenAI's public sitemap. ")

    if anomalies:
        new_section_parts.append(f"**{len(anomalies)} anomaly/anomalies detected — see below.**\n\n")
    else:
        new_section_parts.append("No anomalies detected.\n\n")

    # Anomalies
    if anomalies:
        new_section_parts.append("### ⚠ Anomalies\n\n")
        for a in anomalies:
            new_section_parts.append(f"- **{a['kind']}** — {a['url']}: {a['details']}\n")
        new_section_parts.append("\n")

    # New pages
    if analysis_sections["new"]:
        new_section_parts.append("### New Pages\n\n")
        for n in analysis_sections["new"]:
            md_path = url_to_md_path(n["url"])
            try:
                rel = md_path.relative_to(REPO_ROOT)
            except ValueError:
                rel = md_path
            new_section_parts.append(f"- **[{n['url']}]({n['url']})** (`{n['subsitemap']}`)")
            if n["summary"] and n["summary"] != "(fetch failed)":
                snippet = n["summary"][:200]
                new_section_parts.append(f": {snippet}")
            elif n["summary"] == "(fetch failed)":
                new_section_parts.append(" *(fetch failed)*")
            new_section_parts.append("\n")
        new_section_parts.append("\n")

    # Notable updates (with content diffs)
    if notable_updates:
        new_section_parts.append("### Notable Updates\n\n")
        for e in notable_updates[:15]:
            new_section_parts.append(f"- **{e['url']}**: lastmod `{e['old_lastmod']}` → `{e['new_lastmod']}`")
            if e["added_lines"]:
                snippet = e["added_lines"][0][:150]
                new_section_parts.append(f"\n  - Added: _{snippet}_")
            if e["removed_lines"]:
                snippet = e["removed_lines"][0][:150]
                new_section_parts.append(f"\n  - Removed: _{snippet}_")
            new_section_parts.append("\n")
        new_section_parts.append("\n")

    # Removals
    if removed_urls:
        new_section_parts.append("### Removed Pages\n\n")
        for url in removed_urls:
            new_section_parts.append(f"- {url}\n")
        new_section_parts.append("\n")

    # Failures
    if fetch_failures:
        new_section_parts.append(f"### Fetch Failures\n\n")
        for f in fetch_failures[:10]:
            new_section_parts.append(f"- `{f['url']}`: {f['error'][:100]}\n")
        new_section_parts.append("\n")

    # Stats footer
    new_section_parts.append(
        f"**Stats:** {len(current_urls)} total URLs | "
        f"{len(added_urls)} added | {len(updated_urls)} updated | "
        f"{len(removed_urls)} removed | {len(anomalies)} anomalies | "
        f"{len(sub_urls)} sub-sitemaps\n\n"
    )
    new_section_parts.append("---\n")

    new_section = "".join(new_section_parts)

    # Prepend to README (after any top-level header)
    if old_readme.startswith("# "):
        # Find end of first section header line
        first_newline = old_readme.index("\n") + 1
        # Find first "## " section or insert after intro
        match = re.search(r"\n## ", old_readme)
        if match:
            insert_pos = match.start() + 1  # just before "## "
            new_readme = old_readme[:insert_pos] + new_section + old_readme[insert_pos:]
        else:
            new_readme = old_readme + new_section
    else:
        new_readme = new_section + old_readme

    readme_path.write_text(new_readme, encoding="utf-8")
    print("  Updated README.md")

    # --- STEP 9: UPDATE state/known_urls.json ---
    print("\n[9] Updating state/known_urls.json...")

    for url in current_urls:
        lastmod = current_urls[url]
        if url not in known_state:
            known_state[url] = {
                "current_lastmod": lastmod,
                "first_seen": run_id,
                "last_seen": run_id,
                "lastmod_history": [{"lastmod": lastmod, "run_id": run_id}] if lastmod else [],
            }
        else:
            entry = known_state[url]
            old_lm = entry.get("current_lastmod")
            entry["last_seen"] = run_id
            if lastmod != old_lm:
                entry["current_lastmod"] = lastmod
                hist = entry.get("lastmod_history", [])
                hist.append({"old": old_lm, "new": lastmod, "run_id": run_id})
                entry["lastmod_history"] = hist

    # Write state
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(known_state, f, indent=2)
    print(f"  State updated: {len(known_state)} URLs")

    # --- STEP 10: WRITE diff.json ---
    print("\n[10] Writing diff.json...")

    # Find previous run_id from baseline
    prev_runs = sorted([d.name for d in (REPO_ROOT / "runs").iterdir() if d.is_dir()])
    prev_run = None
    for r in reversed(prev_runs):
        if r < run_id:
            prev_run = r
            break

    diff_data = {
        "run_id": run_id,
        "fetch_time": fetch_time.isoformat(),
        "baseline": prev_run,
        "added": added_urls,
        "removed": removed_urls,
        "updated": updated_urls,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures,
    }

    with open(run_dir / "diff.json", "w") as f:
        json.dump(diff_data, f, indent=2)
    print("  Wrote diff.json")

    print(f"\n=== Run {run_id} complete ===")
    print(f"  Added: {len(added_urls)}, Updated: {len(updated_urls)}, Removed: {len(removed_urls)}")
    print(f"  Anomalies: {len(anomalies)}, Fetch failures: {len(fetch_failures)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
