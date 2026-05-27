#!/usr/bin/env python3
"""
Daily monitoring script for openai.com sitemap.
Run from the repo root.
"""
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

# ── Config ─────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent
RUN_ID = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%MZ")
FETCH_TIME = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

MAX_PAGE_WORKERS = 8

# ── Paths ───────────────────────────────────────────────────────────────────
SITEMAPS_DIR = REPO_ROOT / "sitemaps" / "openai.com"
SUB_LATEST = SITEMAPS_DIR / "sub" / "latest"
SUB_RUN = SITEMAPS_DIR / "sub" / RUN_ID
RUNS_DIR = REPO_ROOT / "runs" / RUN_ID
STATE_FILE = REPO_ROOT / "state" / "known_urls.json"
README = REPO_ROOT / "README.md"


def ensure_dirs():
    for d in [SITEMAPS_DIR, SUB_LATEST, SUB_RUN, RUNS_DIR, REPO_ROOT / "state"]:
        d.mkdir(parents=True, exist_ok=True)


# ── Sitemap fetching (plain httpx is fine for XML) ──────────────────────────
def fetch_xml(url: str, retries: int = 4) -> str:
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


def sanitize_name(url: str) -> str:
    """Produce a safe filename from a sub-sitemap URL."""
    parts = urlsplit(url)
    # e.g. https://openai.com/sitemap.xml/page/ -> sitemap.xml_page
    path = parts.path.strip("/").replace("/", "_")
    return path + ".xml"


def parse_sitemap_index(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    locs = []
    for el in root.findall("sm:sitemap/sm:loc", NS):
        if el.text:
            locs.append(el.text.strip())
    return locs


def parse_url_set(xml_text: str) -> dict[str, str | None]:
    """Return {url: lastmod_or_None}."""
    root = ET.fromstring(xml_text)
    result = {}
    for url_el in root.findall("sm:url", NS):
        loc_el = url_el.find("sm:loc", NS)
        lastmod_el = url_el.find("sm:lastmod", NS)
        if loc_el is not None and loc_el.text:
            loc = loc_el.text.strip()
            lastmod = lastmod_el.text.strip() if lastmod_el is not None and lastmod_el.text else None
            result[loc] = lastmod
    return result


# ── Step 1: Read baseline ───────────────────────────────────────────────────
def load_baseline() -> dict[str, str | None]:
    """Return {url: lastmod} from latest sub-sitemaps."""
    baseline: dict[str, str | None] = {}
    for f in SUB_LATEST.glob("*.xml"):
        try:
            text = f.read_text(encoding="utf-8")
            baseline.update(parse_url_set(text))
        except Exception as e:
            print(f"  Warning: could not parse {f.name}: {e}")
    print(f"Baseline: {len(baseline)} URLs from {len(list(SUB_LATEST.glob('*.xml')))} sub-sitemaps")
    return baseline


# ── Step 2: Fetch + snapshot ────────────────────────────────────────────────
def fetch_and_snapshot() -> tuple[str, list[str], dict[str, dict[str, str | None]]]:
    """
    Returns (index_xml, [sub_sitemap_urls], {sub_name: {url: lastmod}}).
    """
    print(f"Fetching sitemap index: {SITEMAP_INDEX_URL}")
    index_xml = fetch_xml(SITEMAP_INDEX_URL)

    # Save index
    (SITEMAPS_DIR / f"{RUN_ID}.xml").write_text(index_xml, encoding="utf-8")
    (SITEMAPS_DIR / "latest.xml").write_text(index_xml, encoding="utf-8")

    sub_urls = parse_sitemap_index(index_xml)
    print(f"Found {len(sub_urls)} sub-sitemaps")

    sub_data: dict[str, dict[str, str | None]] = {}

    for sub_url in sub_urls:
        name = sanitize_name(sub_url)
        try:
            xml_text = fetch_xml(sub_url)
        except Exception as e:
            print(f"  ERROR fetching {sub_url}: {e}")
            continue

        (SUB_RUN / name).write_text(xml_text, encoding="utf-8")
        (SUB_LATEST / name).write_text(xml_text, encoding="utf-8")

        urls = parse_url_set(xml_text)
        sub_data[name] = urls
        print(f"  {name}: {len(urls)} URLs")

    return index_xml, sub_urls, sub_data


def build_current_map(sub_data: dict[str, dict[str, str | None]]) -> dict[str, str | None]:
    current: dict[str, str | None] = {}
    for urls in sub_data.values():
        current.update(urls)
    return current


# ── Step 3: Diff ─────────────────────────────────────────────────────────────
def compute_diff(baseline: dict[str, str | None], current: dict[str, str | None]):
    added = [u for u in current if u not in baseline]
    removed = [u for u in baseline if u not in current]
    updated = [
        {"url": u, "old_lastmod": baseline[u], "new_lastmod": current[u]}
        for u in current
        if u in baseline and current[u] != baseline[u]
    ]
    return added, removed, updated


# ── Step 4: Anomaly detection ─────────────────────────────────────────────────
def detect_anomalies(added, removed, updated, current, baseline, fetch_time_str, known_urls):
    anomalies = []
    fetch_dt = datetime.fromisoformat(fetch_time_str.replace("Z", "+00:00"))

    for u in current:
        lastmod = current[u]
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
        except Exception:
            continue

        # lastmod in the future
        if lm_dt > fetch_dt:
            anomalies.append({
                "kind": "future_lastmod",
                "url": u,
                "details": f"lastmod {lastmod} is after fetch time {fetch_time_str}"
            })

        # lastmod moved backwards
        if u in baseline and baseline[u]:
            try:
                old_dt = datetime.fromisoformat(baseline[u].replace("Z", "+00:00"))
                if lm_dt < old_dt:
                    anomalies.append({
                        "kind": "lastmod_regression",
                        "url": u,
                        "details": f"lastmod moved backwards: {baseline[u]} -> {lastmod}"
                    })
            except Exception:
                pass

    # New URL with backdated lastmod
    for u in added:
        lastmod = current[u]
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
            first_seen_dt = datetime.fromisoformat(
                RUN_ID.replace("T", "T").replace("-", ":").replace("Z", "+00:00")
            )
        except Exception:
            continue
        # if lastmod is more than 7 days before run_id, flag as potentially backdated
        delta = (first_seen_dt - lm_dt).total_seconds()
        if delta > 7 * 86400:
            anomalies.append({
                "kind": "backdated_new_url",
                "url": u,
                "details": f"New URL with lastmod {lastmod} predates first_seen by {delta/86400:.1f} days"
            })

    # URL disappeared and reappeared
    for u in added:
        if u in known_urls and known_urls[u].get("last_seen") and known_urls[u]["last_seen"] != known_urls[u].get("first_seen", ""):
            prev_seen = known_urls[u].get("last_seen", "")
            if prev_seen < RUN_ID:
                anomalies.append({
                    "kind": "reappeared_url",
                    "url": u,
                    "details": f"URL previously seen (last_seen={prev_seen}), then gone, now back"
                })

    return anomalies


# ── Step 5: Fetch + convert pages ─────────────────────────────────────────────
def url_to_repo_path(url: str) -> Path:
    result = subprocess.run(
        [sys.executable, "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return REPO_ROOT / result.stdout.strip()


def fetch_page(url: str, out_path: Path) -> tuple[bool, str]:
    """Returns (success, error_msg)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            [sys.executable, "tools/html_to_md.py", "--url", url, "--output", str(out_path)],
            capture_output=True, text=True, cwd=REPO_ROOT, timeout=60
        )
        if result.returncode != 0:
            return False, result.stderr[:500]

        if out_path.exists():
            content = out_path.read_text(encoding="utf-8")
            if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                return False, f"Blocked or too short: {len(content)} chars"
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "Timeout after 60s"
    except Exception as e:
        return False, str(e)


def get_prior_markdown(md_path: Path) -> str | None:
    """Get the prior markdown from git for diffing."""
    rel = md_path.relative_to(REPO_ROOT)
    result = subprocess.run(
        ["git", "show", f"HEAD:{rel}"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode == 0:
        return result.stdout
    return None


def summarize_markdown_diff(prior: str | None, current_path: Path) -> str:
    """Produce a concise English description of what changed."""
    if prior is None:
        return "[New page - no prior version]"
    if not current_path.exists():
        return "[Fetch failed]"
    current = current_path.read_text(encoding="utf-8")

    prior_lines = set(prior.splitlines())
    current_lines = set(current.splitlines())
    added_lines = [l for l in current_lines - prior_lines if l.strip()]
    removed_lines = [l for l in prior_lines - current_lines if l.strip()]

    # Remove lines with just whitespace/numbers
    added_lines = [l for l in added_lines if len(l.strip()) > 5][:15]
    removed_lines = [l for l in removed_lines if len(l.strip()) > 5][:15]

    parts = []
    if added_lines:
        parts.append("Added content:\n" + "\n".join(f"  + {l[:120]}" for l in added_lines[:8]))
    if removed_lines:
        parts.append("Removed content:\n" + "\n".join(f"  - {l[:120]}" for l in removed_lines[:8]))

    if not parts:
        # Check length change
        prior_len = len(prior)
        current_len = len(current)
        if abs(prior_len - current_len) < 100:
            return "Minor changes only (whitespace or trivial reordering)"
        return f"Content changed: {prior_len} chars -> {current_len} chars"

    return "\n".join(parts)


def process_pages(added: list, updated: list, fetch_failures: list) -> dict:
    """Fetch pages for added and updated URLs. Returns {url: {'prior': str|None, 'diff_summary': str}}."""
    urls_to_fetch = list(set(added + [u["url"] for u in updated]))
    print(f"\nFetching {len(urls_to_fetch)} pages (added={len(added)}, updated={len(updated)})...")

    prior_content: dict[str, str | None] = {}
    for url in [u["url"] for u in updated]:
        md_path = url_to_repo_path(url)
        prior_content[url] = get_prior_markdown(md_path)

    results = {}
    # Process in batches
    batch_size = MAX_PAGE_WORKERS
    for i in range(0, len(urls_to_fetch), batch_size):
        batch = urls_to_fetch[i:i+batch_size]
        for url in batch:
            md_path = url_to_repo_path(url)
            print(f"  Fetching: {url}")
            success, err = fetch_page(url, md_path)
            if not success:
                print(f"    FAILED: {err}")
                fetch_failures.append({"url": url, "error": err})
                results[url] = {"prior": prior_content.get(url), "diff_summary": f"[Fetch failed: {err}]"}
            else:
                diff = summarize_markdown_diff(prior_content.get(url), md_path)
                results[url] = {"prior": prior_content.get(url), "diff_summary": diff}
                print(f"    OK")

    return results


# ── Step 7: Write analysis ─────────────────────────────────────────────────────
def write_analysis(added, removed, updated, anomalies, fetch_failures, page_results, current):
    lines = [
        f"# Run Analysis: {RUN_ID}",
        f"",
        f"**Fetch time:** {FETCH_TIME}",
        f"**Total URLs in sitemap:** {len(current)}",
        f"**Added:** {len(added)} | **Updated:** {len(updated)} | **Removed:** {len(removed)}",
        f"**Anomalies:** {len(anomalies)} | **Fetch failures:** {len(fetch_failures)}",
        f"",
    ]

    if anomalies:
        lines += ["## Anomalies (Highest Signal)", ""]
        for a in anomalies:
            lines.append(f"- **{a['kind']}** — `{a['url']}`")
            lines.append(f"  {a['details']}")
        lines.append("")

    if updated:
        lines += ["## Significant Updates", ""]
        for u in updated:
            url = u["url"]
            lines.append(f"### {url}")
            lines.append(f"- lastmod: `{u['old_lastmod']}` → `{u['new_lastmod']}`")
            if url in page_results:
                lines.append(f"- Diff summary:")
                lines.append(f"  ```")
                lines.append(f"  {page_results[url]['diff_summary'][:500]}")
                lines.append(f"  ```")
            lines.append("")

    if added:
        lines += ["## New Pages", ""]
        for url in added:
            lines.append(f"### {url}")
            lastmod = current.get(url, "unknown")
            lines.append(f"- lastmod: `{lastmod}`")
            if url in page_results:
                lines.append(f"- Summary: {page_results[url]['diff_summary'][:300]}")
            lines.append("")

    if removed:
        lines += ["## Removed Pages", ""]
        for url in removed:
            lines.append(f"- `{url}` (last in git history)")
        lines.append("")

    if fetch_failures:
        lines += ["## Fetch Failures (needs follow-up)", ""]
        for f in fetch_failures:
            lines.append(f"- `{f['url']}`: {f['error']}")
        lines.append("")

    analysis_path = RUNS_DIR / "analysis.md"
    analysis_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Analysis written to {analysis_path}")
    return analysis_path


# ── Step 8: Update README ──────────────────────────────────────────────────────
def update_readme(added, removed, updated, anomalies, fetch_failures, page_results, current):
    existing = README.read_text(encoding="utf-8") if README.exists() else ""

    # Build new section
    tl_dr_parts = []
    if added:
        tl_dr_parts.append(f"{len(added)} new pages added")
    if updated:
        tl_dr_parts.append(f"{len(updated)} pages updated")
    if removed:
        tl_dr_parts.append(f"{len(removed)} pages removed")
    if anomalies:
        tl_dr_parts.append(f"{len(anomalies)} anomalies detected")
    tl_dr = ", ".join(tl_dr_parts) if tl_dr_parts else "No significant changes detected"

    lines = [
        f"## {RUN_ID}",
        f"",
        f"**TL;DR:** {tl_dr}. Sitemap now contains {len(current)} total URLs across all sub-sitemaps.",
        f"",
    ]

    if anomalies:
        lines.append("### ⚠️ Anomalies")
        for a in anomalies:
            lines.append(f"- **{a['kind']}**: `{a['url']}` — {a['details']}")
        lines.append("")

    if added:
        lines.append("### New Pages")
        for url in added[:20]:  # cap at 20 for readability
            md_path = url_to_repo_path(url)
            rel = md_path.relative_to(REPO_ROOT)
            lastmod = current.get(url, "")
            diff = page_results.get(url, {}).get("diff_summary", "")
            brief = diff.split("\n")[0][:100] if diff else ""
            lines.append(f"- [`{url}`]({rel}) — lastmod `{lastmod}` {brief}")
        if len(added) > 20:
            lines.append(f"- _(and {len(added) - 20} more)_")
        lines.append("")

    if updated:
        lines.append("### Updated Pages")
        for u in updated[:20]:
            url = u["url"]
            md_path = url_to_repo_path(url)
            rel = md_path.relative_to(REPO_ROOT)
            diff = page_results.get(url, {}).get("diff_summary", "")
            brief = diff.split("\n")[0][:100] if diff else ""
            lines.append(f"- [`{url}`]({rel}) — `{u['old_lastmod']}` → `{u['new_lastmod']}` {brief}")
        if len(updated) > 20:
            lines.append(f"- _(and {len(updated) - 20} more)_")
        lines.append("")

    if removed:
        lines.append("### Removed Pages")
        for url in removed[:20]:
            lines.append(f"- `{url}`")
        if len(removed) > 20:
            lines.append(f"- _(and {len(removed) - 20} more)_")
        lines.append("")

    if fetch_failures:
        lines.append("### Fetch Failures")
        for f in fetch_failures[:10]:
            lines.append(f"- `{f['url']}`: {f['error'][:80]}")
        lines.append("")

    lines += [
        f"**Stats:** {len(current)} total URLs | +{len(added)} added | "
        f"~{len(updated)} updated | -{len(removed)} removed | "
        f"{len(anomalies)} anomalies | {len(fetch_failures)} fetch failures",
        "",
        "---",
        "",
    ]

    new_section = "\n".join(lines)

    # Prepend new section after the first heading (# OpenAI Sitemap Monitor)
    if existing.startswith("#"):
        first_newline = existing.find("\n")
        header = existing[:first_newline + 1]
        rest = existing[first_newline + 1:]
        new_content = header + "\n" + new_section + rest
    else:
        new_content = new_section + existing

    README.write_text(new_content, encoding="utf-8")
    print(f"README updated")


# ── Step 9: Update state ───────────────────────────────────────────────────────
def update_state(current, baseline, added, removed, updated):
    known = {}
    if STATE_FILE.exists():
        known = json.loads(STATE_FILE.read_text(encoding="utf-8"))

    today = RUN_ID

    # All current URLs - update last_seen
    for url, lastmod in current.items():
        if url not in known:
            known[url] = {
                "first_seen": today,
                "last_seen": today,
                "current_lastmod": lastmod,
                "lastmod_history": [{"lastmod": lastmod, "run_id": today}]
            }
        else:
            known[url]["last_seen"] = today
            old_lastmod = known[url].get("current_lastmod")
            if lastmod != old_lastmod:
                known[url]["current_lastmod"] = lastmod
                history = known[url].get("lastmod_history", [])
                history.append({"old": old_lastmod, "new": lastmod, "run_id": today})
                known[url]["lastmod_history"] = history

    STATE_FILE.write_text(json.dumps(known, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"State updated: {len(known)} URLs")


# ── Step 10: Write diff.json ───────────────────────────────────────────────────
def write_diff_json(added, removed, updated, anomalies, fetch_failures, baseline_run_id):
    diff = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": baseline_run_id,
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures,
    }
    diff_path = RUNS_DIR / "diff.json"
    diff_path.write_text(json.dumps(diff, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Diff written to {diff_path}")


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print(f"=== OpenAI Sitemap Monitor Run: {RUN_ID} ===")
    print(f"Fetch time: {FETCH_TIME}")

    ensure_dirs()

    # Step 1: Baseline
    print("\n--- Step 1: Loading baseline ---")
    baseline = load_baseline()

    # Determine baseline run_id from git log
    result = subprocess.run(
        ["git", "log", "--oneline", "-1", "--", "sitemaps/openai.com/latest.xml"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    baseline_run_id = result.stdout.strip().split()[1] if result.stdout.strip() else None

    # Step 2: Fetch + snapshot
    print("\n--- Step 2: Fetching sitemaps ---")
    try:
        index_xml, sub_urls, sub_data = fetch_and_snapshot()
    except Exception as e:
        error_msg = f"CRITICAL: Could not fetch sitemap index: {e}"
        print(error_msg)
        analysis = f"# Run Analysis: {RUN_ID}\n\n**CRITICAL FAILURE:** {error_msg}\n"
        (RUNS_DIR / "analysis.md").write_text(analysis)
        # Prepend to README
        existing = README.read_text(encoding="utf-8") if README.exists() else ""
        README.write_text(f"## {RUN_ID} — FAILED\n\nCritical error: {error_msg}\n\n---\n\n" + existing)
        return 1

    current = build_current_map(sub_data)
    print(f"\nCurrent sitemap: {len(current)} total URLs")

    # Step 3: Diff
    print("\n--- Step 3: Computing diff ---")
    added, removed, updated = compute_diff(baseline, current)
    print(f"Added: {len(added)} | Updated: {len(updated)} | Removed: {len(removed)}")

    # Step 4: Anomaly detection
    print("\n--- Step 4: Anomaly detection ---")
    known_urls = {}
    if STATE_FILE.exists():
        known_urls = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    anomalies = detect_anomalies(added, removed, updated, current, baseline, FETCH_TIME, known_urls)
    print(f"Anomalies: {len(anomalies)}")
    for a in anomalies[:5]:
        print(f"  {a['kind']}: {a['url']}")

    # Step 5: Fetch + convert pages
    print("\n--- Step 5: Fetching changed/new pages ---")
    fetch_failures = []
    page_results = process_pages(added, updated, fetch_failures)

    # Step 7: Analysis
    print("\n--- Step 7: Writing analysis ---")
    write_analysis(added, removed, updated, anomalies, fetch_failures, page_results, current)

    # Step 8: Update README
    print("\n--- Step 8: Updating README ---")
    update_readme(added, removed, updated, anomalies, fetch_failures, page_results, current)

    # Step 9: Update state
    print("\n--- Step 9: Updating state ---")
    update_state(current, baseline, added, removed, updated)

    # Step 10: Write diff.json
    print("\n--- Step 10: Writing diff.json ---")
    write_diff_json(added, removed, updated, anomalies, fetch_failures, baseline_run_id)

    print(f"\n=== Run {RUN_ID} complete ===")
    print(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}, Anomalies: {len(anomalies)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
