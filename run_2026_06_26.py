#!/usr/bin/env python3
"""
OpenAI Sitemap Monitor - Run for 2026-06-26
run_id = 2026-06-26T09-15Z
"""
import os, sys, json, subprocess, shutil, re
from pathlib import Path
from datetime import datetime, timezone
from xml.etree import ElementTree as ET
from urllib.parse import urlparse

import httpx

RUN_ID = "2026-06-26T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
ROOT_DIR = Path("/home/user/openai_monitor")
PAGES_DIR = ROOT_DIR / "pages/openai.com"
SITEMAPS_DIR = ROOT_DIR / "sitemaps/openai.com"
SUB_LATEST_DIR = SITEMAPS_DIR / "sub/latest"
SUB_DATED_DIR = SITEMAPS_DIR / "sub" / RUN_ID
RUNS_DIR = ROOT_DIR / "runs" / RUN_ID
STATE_FILE = ROOT_DIR / "state/known_urls.json"

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"


def log(msg):
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}Z] {msg}", flush=True)


def get_repo_path(url):
    """Call tools/url_path.py to get the repo path for a URL."""
    result = subprocess.run(
        [sys.executable, str(ROOT_DIR / "tools/url_path.py"), url],
        capture_output=True, text=True
    )
    return result.stdout.strip()


def sanitize_sub_name(url):
    """Convert sub-sitemap URL to a filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> sitemap.xml_page.xml
    path = urlparse(url).path  # /sitemap.xml/page/
    # strip leading slash, replace / with _
    clean = path.strip("/").replace("/", "_")
    return clean + ".xml"


def fetch_sitemap(url):
    """Fetch a sitemap XML. Returns text or raises."""
    resp = httpx.get(url, timeout=30, follow_redirects=True)
    resp.raise_for_status()
    return resp.text


def parse_sitemap_index(xml_text):
    """Parse a sitemap index and return list of sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    urls = []
    for sitemap in root.findall(f"{{{NS}}}sitemap"):
        loc = sitemap.findtext(f"{{{NS}}}loc")
        if loc:
            urls.append(loc.strip())
    return urls


def parse_sub_sitemap(xml_text):
    """Parse a sub-sitemap and return dict of {url: lastmod or None}."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url_el in root.findall(f"{{{NS}}}url"):
        loc = url_el.findtext(f"{{{NS}}}loc")
        lastmod = url_el.findtext(f"{{{NS}}}lastmod")
        if loc:
            urls[loc.strip()] = (lastmod or "").strip()
    return urls


def load_baseline():
    """Load all sub-sitemap URLs from sitemaps/openai.com/sub/latest/"""
    baseline = {}
    for f in SUB_LATEST_DIR.glob("*.xml"):
        try:
            xml_text = f.read_text(encoding="utf-8")
            urls = parse_sub_sitemap(xml_text)
            for url, lastmod in urls.items():
                baseline[url] = lastmod
        except Exception as e:
            log(f"Warning: could not parse baseline {f}: {e}")
    return baseline


def main():
    log(f"=== Run {RUN_ID} starting ===")
    log(f"Fetch time: {FETCH_TIME}")

    # Create run dirs
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    SUB_DATED_DIR.mkdir(parents=True, exist_ok=True)
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    # ===== STEP 1: Load baseline =====
    log("Step 1: Loading baseline...")
    baseline = load_baseline()
    log(f"  Baseline: {len(baseline)} URLs")

    # Also note what sub-sitemaps existed
    baseline_sub_sitemaps = set(f.name for f in SUB_LATEST_DIR.glob("*.xml"))

    # ===== STEP 2: Fetch new sitemaps =====
    log("Step 2: Fetching sitemap index...")
    try:
        index_xml = fetch_sitemap(SITEMAP_INDEX_URL)
    except Exception as e:
        log(f"FATAL: Could not fetch sitemap index: {e}")
        # Write failure analysis
        analysis = f"# Run {RUN_ID} - FAILURE\n\nCould not fetch sitemap index: {e}\n"
        (RUNS_DIR / "analysis.md").write_text(analysis)
        return 1

    # Save root index
    index_path = SITEMAPS_DIR / f"{RUN_ID}.xml"
    index_path.write_text(index_xml, encoding="utf-8")
    (SITEMAPS_DIR / "latest.xml").write_text(index_xml, encoding="utf-8")
    log(f"  Saved root index to {index_path}")

    # Parse sub-sitemap URLs
    sub_urls = parse_sitemap_index(index_xml)
    log(f"  Found {len(sub_urls)} sub-sitemaps")

    # Fetch each sub-sitemap
    current = {}  # url -> lastmod
    sub_sitemap_map = {}  # url -> sub-sitemap name (for anomaly detection)
    fetch_failures = []

    for sub_url in sub_urls:
        fname = sanitize_sub_name(sub_url)
        try:
            xml_text = fetch_sitemap(sub_url)
            urls = parse_sub_sitemap(xml_text)
            # Save dated + latest copies
            (SUB_DATED_DIR / fname).write_text(xml_text, encoding="utf-8")
            (SUB_LATEST_DIR / fname).write_text(xml_text, encoding="utf-8")
            for url, lastmod in urls.items():
                current[url] = lastmod
                sub_sitemap_map[url] = fname
            log(f"  {fname}: {len(urls)} URLs")
        except Exception as e:
            log(f"  WARN: Failed to fetch {sub_url}: {e}")
            fetch_failures.append({"url": sub_url, "error": str(e)})

    log(f"  Total current URLs: {len(current)}")

    # ===== STEP 3: Diff =====
    log("Step 3: Computing diff...")
    added = [url for url in current if url not in baseline]
    removed = [url for url in baseline if url not in current]
    updated = [
        {"url": url, "old_lastmod": baseline[url], "new_lastmod": current[url]}
        for url in current
        if url in baseline and current[url] != baseline[url] and current[url]
    ]

    log(f"  Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")

    # ===== STEP 4: Anomaly detection =====
    log("Step 4: Detecting anomalies...")
    anomalies = []
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}

    fetch_dt = datetime.fromisoformat(FETCH_TIME.rstrip("Z")).replace(tzinfo=timezone.utc)

    for url, lastmod in current.items():
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod).replace(tzinfo=timezone.utc)
        except ValueError:
            continue

        # Future lastmod
        if lm_dt > fetch_dt:
            anomalies.append({
                "kind": "future_lastmod",
                "url": url,
                "details": f"lastmod {lastmod} is after fetch time {FETCH_TIME}"
            })

        # Backwards lastmod
        if url in baseline and baseline[url]:
            try:
                old_dt = datetime.fromisoformat(baseline[url]).replace(tzinfo=timezone.utc)
                if lm_dt < old_dt:
                    anomalies.append({
                        "kind": "backwards_lastmod",
                        "url": url,
                        "details": f"lastmod moved from {baseline[url]} back to {lastmod}"
                    })
            except ValueError:
                pass

    # New URL with backdated lastmod
    for url in added:
        lastmod = current[url]
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod).replace(tzinfo=timezone.utc)
            # first_seen is now, so if lastmod is >7 days before now, it's suspicious
            age_days = (fetch_dt - lm_dt).days
            if age_days > 7:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"New URL but lastmod is {age_days} days old ({lastmod})"
                })
        except ValueError:
            pass

    # Disappeared and reappeared
    for url in added:
        if url in state and state[url].get("last_seen"):
            last_seen = state[url]["last_seen"]
            if last_seen < "2026-06-24":  # Was absent last run
                anomalies.append({
                    "kind": "reappeared_url",
                    "url": url,
                    "details": f"URL reappeared (last seen: {last_seen})"
                })

    # Sub-sitemap migration: check if a URL moved sub-sitemaps
    # Load old sub-sitemap mapping from prior run
    old_sub_map = {}
    for f in SUB_LATEST_DIR.glob("*.xml"):
        if f.name in [sanitize_sub_name(u) for u in sub_urls]:
            # This is current, skip - we need the old state
            pass
    # Check state for sub-sitemap info
    for url in updated:
        url_str = url["url"]
        old_sub = state.get(url_str, {}).get("sub_sitemap", "")
        new_sub = sub_sitemap_map.get(url_str, "")
        if old_sub and new_sub and old_sub != new_sub:
            anomalies.append({
                "kind": "sub_sitemap_migration",
                "url": url_str,
                "details": f"Moved from {old_sub} to {new_sub}"
            })

    log(f"  Anomalies: {len(anomalies)}")

    # ===== STEP 5: Fetch and convert changed/new pages =====
    log("Step 5: Fetching changed/new pages...")
    pages_to_fetch = added + [u["url"] for u in updated]
    log(f"  Pages to fetch: {len(pages_to_fetch)}")

    page_fetch_failures = []
    page_diffs = {}  # url -> (old_content, new_content)

    import concurrent.futures

    def fetch_page(url):
        md_path = get_repo_path(url)
        if not md_path:
            return url, None, "no path"
        full_path = ROOT_DIR / md_path

        # Capture prior content for updated pages
        prior_content = None
        if full_path.exists():
            prior_content = full_path.read_text(encoding="utf-8", errors="replace")

        # Fetch page
        full_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = full_path.with_suffix(".tmp.md")
        try:
            result = subprocess.run(
                [sys.executable, str(ROOT_DIR / "tools/html_to_md.py"),
                 "--url", url, "--output", str(tmp_path)],
                capture_output=True, text=True, timeout=60
            )
            if tmp_path.exists():
                content = tmp_path.read_text(encoding="utf-8", errors="replace")
                if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                    tmp_path.unlink(missing_ok=True)
                    return url, prior_content, f"fetch blocked (content: {content[:80]})"
                # Success - overwrite
                shutil.move(str(tmp_path), str(full_path))
                return url, prior_content, None
            else:
                return url, prior_content, f"no output file; stderr: {result.stderr[:200]}"
        except subprocess.TimeoutExpired:
            tmp_path.unlink(missing_ok=True)
            return url, prior_content, "timeout"
        except Exception as e:
            tmp_path.unlink(missing_ok=True)
            return url, prior_content, str(e)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(fetch_page, url): url for url in pages_to_fetch}
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            url = futures[fut]
            try:
                url, prior, err = fut.result()
                done += 1
                if err:
                    page_fetch_failures.append({"url": url, "error": err})
                    log(f"  [{done}/{len(pages_to_fetch)}] FAIL {url}: {err[:60]}")
                else:
                    if prior is not None:
                        # Updated page - store diff info
                        md_path = get_repo_path(url)
                        full_path = ROOT_DIR / md_path
                        if full_path.exists():
                            new_content = full_path.read_text(encoding="utf-8", errors="replace")
                            page_diffs[url] = (prior, new_content)
                    log(f"  [{done}/{len(pages_to_fetch)}] OK {url}")
            except Exception as e:
                done += 1
                log(f"  [{done}/{len(pages_to_fetch)}] ERROR {url}: {e}")
                page_fetch_failures.append({"url": url, "error": str(e)})

    all_fetch_failures = fetch_failures + page_fetch_failures

    # ===== STEP 6: Analyze =====
    log("Step 6: Writing analysis...")

    def text_diff_summary(old, new, max_lines=30):
        """Simple line-based diff summary."""
        import difflib
        old_lines = old.splitlines()
        new_lines = new.splitlines()
        diff = list(difflib.unified_diff(old_lines, new_lines, lineterm="", n=2))
        if not diff:
            return "No substantive changes detected."
        # Count adds/removes
        adds = [l for l in diff if l.startswith("+") and not l.startswith("+++")]
        removes = [l for l in diff if l.startswith("-") and not l.startswith("---")]
        summary = f"+{len(adds)} lines, -{len(removes)} lines\n"
        # Show first max_lines of diff
        summary += "\n".join(diff[:max_lines])
        if len(diff) > max_lines:
            summary += f"\n... ({len(diff) - max_lines} more lines)"
        return summary

    analysis_lines = [
        f"# Run {RUN_ID} Analysis",
        f"\nFetch time: {FETCH_TIME}",
        f"Baseline: 2026-06-24T09-15Z ({len(baseline)} URLs)",
        f"Current: {len(current)} URLs",
        f"\n## Summary",
        f"- Added: {len(added)}",
        f"- Removed: {len(removed)}",
        f"- Updated: {len(updated)}",
        f"- Anomalies: {len(anomalies)}",
        f"- Page fetch failures: {len(page_fetch_failures)}",
    ]

    if anomalies:
        analysis_lines += ["\n## Anomalies (Highest Signal)"]
        for a in anomalies:
            analysis_lines.append(f"\n### {a['kind']} — {a['url']}")
            analysis_lines.append(a['details'])

    if updated:
        analysis_lines += ["\n## Updated Pages"]
        for u in updated:
            url = u["url"]
            analysis_lines.append(f"\n### {url}")
            analysis_lines.append(f"lastmod: {u['old_lastmod']} → {u['new_lastmod']}")
            if url in page_diffs:
                old_c, new_c = page_diffs[url]
                analysis_lines.append("\n**Diff:**")
                analysis_lines.append("```diff")
                analysis_lines.append(text_diff_summary(old_c, new_c))
                analysis_lines.append("```")
            else:
                analysis_lines.append("(Page diff not available - fetch may have failed)")

    if added:
        analysis_lines += ["\n## New Pages"]
        for url in added:
            md_path = get_repo_path(url)
            full_path = ROOT_DIR / md_path if md_path else None
            analysis_lines.append(f"\n### {url}")
            analysis_lines.append(f"lastmod: {current.get(url, 'N/A')}")
            if full_path and full_path.exists():
                content = full_path.read_text(encoding="utf-8", errors="replace")
                # First 300 chars as preview
                preview = content[:400].replace("\n", " ").strip()
                analysis_lines.append(f"Preview: {preview}")

    if removed:
        analysis_lines += ["\n## Removed Pages"]
        for url in removed:
            analysis_lines.append(f"- {url}")

    if all_fetch_failures:
        analysis_lines += ["\n## Fetch Failures (Needs Follow-up)"]
        for f in all_fetch_failures:
            analysis_lines.append(f"- **{f['url']}**: {f['error']}")

    analysis_text = "\n".join(analysis_lines)
    (RUNS_DIR / "analysis.md").write_text(analysis_text, encoding="utf-8")
    log(f"  Written {RUNS_DIR / 'analysis.md'}")

    # ===== STEP 7: Update README.md =====
    log("Step 7: Updating README.md...")

    readme_path = ROOT_DIR / "README.md"
    existing_readme = readme_path.read_text(encoding="utf-8")

    # Build new section
    new_section_lines = [
        f"## {RUN_ID[:10]} — Monitoring Run",
        f"",
        f"**Fetch time:** {FETCH_TIME}  ",
        f"**Baseline:** 2026-06-24T09-15Z  ",
        f"**Stats:** {len(current)} total URLs | +{len(added)} added | ~{len(updated)} updated | -{len(removed)} removed | {len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps",
        f"",
    ]

    # TL;DR
    if len(added) == 0 and len(removed) == 0 and len(updated) == 0 and len(anomalies) == 0:
        tldr = "No changes detected in this run. The OpenAI sitemap remains identical to the prior snapshot from 2026-06-24."
    else:
        parts = []
        if added:
            parts.append(f"{len(added)} new URL(s)")
        if removed:
            parts.append(f"{len(removed)} removal(s)")
        if updated:
            parts.append(f"{len(updated)} update(s)")
        if anomalies:
            parts.append(f"{len(anomalies)} anomaly(ies)")
        tldr = f"This run detected {', '.join(parts)} compared to the last snapshot from 2026-06-24."

    new_section_lines += [
        f"**TL;DR:** {tldr}",
        f"",
    ]

    if anomalies:
        new_section_lines += ["### Anomalies"]
        for a in anomalies:
            new_section_lines.append(f"- **{a['kind']}**: `{a['url']}` — {a['details']}")
        new_section_lines.append("")

    if added:
        new_section_lines += ["### New Pages"]
        for url in added[:20]:  # Cap at 20 for readability
            md_path = get_repo_path(url)
            lastmod = current.get(url, "")
            full_path = ROOT_DIR / md_path if md_path else None
            preview = ""
            if full_path and full_path.exists():
                content = full_path.read_text(encoding="utf-8", errors="replace")
                # Get first meaningful line
                for line in content.splitlines():
                    line = line.strip()
                    if line and not line.startswith("#") and len(line) > 20:
                        preview = f" — {line[:120]}"
                        break
            new_section_lines.append(f"- [`{url}`]({md_path}){preview}")
        if len(added) > 20:
            new_section_lines.append(f"- _(and {len(added)-20} more)_")
        new_section_lines.append("")

    if updated:
        new_section_lines += ["### Updated Pages"]
        for u in updated[:20]:
            url = u["url"]
            md_path = get_repo_path(url)
            change_desc = f"lastmod {u['old_lastmod']} → {u['new_lastmod']}"
            if url in page_diffs:
                old_c, new_c = page_diffs[url]
                adds_count = sum(1 for l in new_c.splitlines() if l not in old_c.splitlines())
                change_desc += f" (content changed)"
            new_section_lines.append(f"- [`{url}`]({md_path}): {change_desc}")
        if len(updated) > 20:
            new_section_lines.append(f"- _(and {len(updated)-20} more)_")
        new_section_lines.append("")

    if removed:
        new_section_lines += ["### Removed Pages"]
        for url in removed[:20]:
            new_section_lines.append(f"- `{url}`")
        if len(removed) > 20:
            new_section_lines.append(f"- _(and {len(removed)-20} more)_")
        new_section_lines.append("")

    new_section_lines += [
        f"Full analysis: [runs/{RUN_ID}/analysis.md](runs/{RUN_ID}/analysis.md)",
        f"",
        "---",
        "",
    ]

    new_section = "\n".join(new_section_lines)

    # Prepend to existing README (after the first H1 heading)
    # Find the first run section marker to insert before it
    lines = existing_readme.splitlines(keepends=True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("## 20") or line.startswith("## Run"):
            insert_at = i
            break

    if insert_at > 0:
        new_readme = "".join(lines[:insert_at]) + new_section + "".join(lines[insert_at:])
    else:
        # No existing run sections, append at end
        new_readme = existing_readme.rstrip() + "\n\n" + new_section

    readme_path.write_text(new_readme, encoding="utf-8")
    log("  README.md updated")

    # ===== STEP 8: Update state/known_urls.json =====
    log("Step 8: Updating state/known_urls.json...")

    today = RUN_ID[:10]
    for url in current:
        if url not in state:
            state[url] = {
                "first_seen": RUN_ID,
                "last_seen": today,
                "current_lastmod": current[url],
                "lastmod_history": [current[url]] if current[url] else [],
                "sub_sitemap": sub_sitemap_map.get(url, "")
            }
        else:
            state[url]["last_seen"] = today
            old_lm = state[url].get("current_lastmod", "")
            if current[url] and current[url] != old_lm:
                history = state[url].get("lastmod_history", [])
                history.append(current[url])
                state[url]["lastmod_history"] = history
                state[url]["current_lastmod"] = current[url]
            state[url]["sub_sitemap"] = sub_sitemap_map.get(url, "")

    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    log(f"  Updated state: {len(state)} URLs")

    # ===== STEP 9: Write diff.json =====
    log("Step 9: Writing diff.json...")
    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": "2026-06-24T09-15Z",
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": all_fetch_failures
    }
    (RUNS_DIR / "diff.json").write_text(json.dumps(diff_data, indent=2), encoding="utf-8")
    log("  Written diff.json")

    log(f"\n=== Run {RUN_ID} complete ===")
    log(f"Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}, Anomalies: {len(anomalies)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
