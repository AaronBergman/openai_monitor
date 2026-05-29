#!/usr/bin/env python3
"""OpenAI sitemap monitor - single run script."""

import os
import sys
import json
import subprocess
import re
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

import httpx

REPO = Path("/home/user/openai_monitor")
RUN_ID = "2026-05-29T09-16Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

print(f"Run ID: {RUN_ID}")
print(f"Fetch time: {FETCH_TIME}")

# ── helpers ──────────────────────────────────────────────────────────────────

def url_to_path(url: str) -> str:
    result = subprocess.run(
        ["python3", "tools/url_path.py", url],
        capture_output=True, text=True, cwd=REPO
    )
    return result.stdout.strip()

def fetch_xml(url: str) -> bytes:
    resp = httpx.get(url, timeout=30, follow_redirects=True,
                     headers={"User-Agent": "Mozilla/5.0 (compatible; sitemap-monitor/1.0)"})
    resp.raise_for_status()
    return resp.content

def parse_sitemap_index(xml_bytes: bytes) -> list[str]:
    """Return list of sub-sitemap URLs from a sitemap index."""
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = []
    for sitemap in root.findall("sm:sitemap", ns):
        loc = sitemap.find("sm:loc", ns)
        if loc is not None and loc.text:
            locs.append(loc.text.strip())
    return locs

def parse_urlset(xml_bytes: bytes) -> dict[str, str | None]:
    """Return {url: lastmod_or_None} from a urlset sitemap."""
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {}
    for url_el in root.findall("sm:url", ns):
        loc = url_el.find("sm:loc", ns)
        lastmod = url_el.find("sm:lastmod", ns)
        if loc is not None and loc.text:
            urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None and lastmod.text else None
    return urls

def sanitize_filename(url: str) -> str:
    """Turn a sub-sitemap URL into a safe filename."""
    # e.g. https://openai.com/sitemap.xml/page/ -> _openai.com_sitemap.xml_page.xml
    name = url.replace("https://", "").replace("http://", "")
    name = re.sub(r"[^a-zA-Z0-9._-]", "_", name)
    name = name.rstrip("_")
    if not name.endswith(".xml"):
        name += ".xml"
    return name

# ── STEP 1: read baseline ─────────────────────────────────────────────────────

print("\n=== STEP 1: Reading baseline ===")

baseline_urls: dict[str, str | None] = {}

latest_index = REPO / "sitemaps/openai.com/latest.xml"
sub_latest = REPO / "sitemaps/openai.com/sub/latest"

if latest_index.exists():
    try:
        index_bytes = latest_index.read_bytes()
        sub_urls_in_index = parse_sitemap_index(index_bytes)
        print(f"  Baseline index has {len(sub_urls_in_index)} sub-sitemaps")
    except Exception as e:
        print(f"  Warning: could not parse baseline index: {e}")
        sub_urls_in_index = []

if sub_latest.exists():
    for f in sub_latest.glob("*.xml"):
        try:
            urls = parse_urlset(f.read_bytes())
            baseline_urls.update(urls)
        except Exception as e:
            print(f"  Warning: could not parse {f.name}: {e}")

print(f"  Baseline total URLs: {len(baseline_urls)}")

# ── STEP 2: fetch + snapshot ─────────────────────────────────────────────────

print("\n=== STEP 2: Fetching sitemaps ===")

SITEMAP_INDEX_URL = "https://openai.com/sitemap.xml"

try:
    index_bytes = fetch_xml(SITEMAP_INDEX_URL)
    print(f"  Fetched root index ({len(index_bytes)} bytes)")
except Exception as e:
    print(f"  FATAL: could not fetch root sitemap: {e}")
    sys.exit(1)

# Save root index
dated_dir = REPO / "sitemaps/openai.com"
(dated_dir / f"{RUN_ID}.xml").write_bytes(index_bytes)
(dated_dir / "latest.xml").write_bytes(index_bytes)
print(f"  Saved root index")

sub_sitemap_urls = parse_sitemap_index(index_bytes)
print(f"  Found {len(sub_sitemap_urls)} sub-sitemaps")

# Fetch each sub-sitemap
sub_dated_dir = REPO / f"sitemaps/openai.com/sub/{RUN_ID}"
sub_latest_dir = REPO / "sitemaps/openai.com/sub/latest"
sub_dated_dir.mkdir(parents=True, exist_ok=True)
sub_latest_dir.mkdir(parents=True, exist_ok=True)

current_urls: dict[str, str | None] = {}
url_to_subsitemap: dict[str, str] = {}  # url -> sub-sitemap name

for sub_url in sub_sitemap_urls:
    fname = sanitize_filename(sub_url)
    try:
        sub_bytes = fetch_xml(sub_url)
        (sub_dated_dir / fname).write_bytes(sub_bytes)
        (sub_latest_dir / fname).write_bytes(sub_bytes)
        urls = parse_urlset(sub_bytes)
        for u in urls:
            url_to_subsitemap[u] = fname
        current_urls.update(urls)
        print(f"  {fname}: {len(urls)} URLs")
    except Exception as e:
        print(f"  Warning: failed to fetch {sub_url}: {e}")

print(f"  Total current URLs: {len(current_urls)}")

# ── STEP 3: diff ─────────────────────────────────────────────────────────────

print("\n=== STEP 3: Computing diff ===")

baseline_set = set(baseline_urls.keys())
current_set = set(current_urls.keys())

added_urls = sorted(current_set - baseline_set)
removed_urls = sorted(baseline_set - current_set)
updated_urls = []
for url in current_set & baseline_set:
    old_lm = baseline_urls[url]
    new_lm = current_urls[url]
    if old_lm != new_lm:
        updated_urls.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})
updated_urls.sort(key=lambda x: x["url"])

print(f"  Added: {len(added_urls)}")
print(f"  Removed: {len(removed_urls)}")
print(f"  Updated: {len(updated_urls)}")

# ── STEP 4: anomaly detection ─────────────────────────────────────────────────

print("\n=== STEP 4: Anomaly detection ===")

anomalies = []

fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

# Load state for historical context
state_file = REPO / "state/known_urls.json"
state: dict = {}
if state_file.exists():
    state = json.loads(state_file.read_text())

for url, lm in current_urls.items():
    if lm is None:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
    except ValueError:
        continue

    # Future lastmod
    if lm_dt > fetch_dt:
        anomalies.append({
            "kind": "future_lastmod",
            "url": url,
            "details": f"lastmod={lm} is after fetch_time={FETCH_TIME}"
        })

    # Backwards lastmod
    if url in state and "current_lastmod" in state[url]:
        old_lm = state[url]["current_lastmod"]
        if old_lm and old_lm != lm:
            try:
                old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
                if lm_dt < old_dt:
                    anomalies.append({
                        "kind": "backwards_lastmod",
                        "url": url,
                        "details": f"lastmod moved backward: {old_lm} -> {lm}"
                    })
            except ValueError:
                pass

# New URLs with backdated lastmod
for url in added_urls:
    lm = current_urls[url]
    if lm is None:
        continue
    try:
        lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
        # first_seen is RUN_ID date
        run_dt = datetime.fromisoformat("2026-05-29T09:16:00+00:00")
        delta = (run_dt - lm_dt).days
        if delta > 7:
            anomalies.append({
                "kind": "backdated_new_url",
                "url": url,
                "details": f"New URL with lastmod={lm} predates first_seen by {delta} days"
            })
    except ValueError:
        pass

# Reappeared URLs (was removed before)
for url in added_urls:
    if url in state:
        prev = state[url]
        if prev.get("last_seen") and prev["last_seen"] < "2026-05-28":
            anomalies.append({
                "kind": "reappeared_url",
                "url": url,
                "details": f"URL last seen {prev['last_seen']}, now reappeared"
            })

print(f"  Anomalies: {len(anomalies)}")
for a in anomalies[:10]:
    print(f"    {a['kind']}: {a['url']}")

# ── STEP 5: fetch + convert changed/new pages ─────────────────────────────────

print("\n=== STEP 5: Fetching page content ===")

pages_to_fetch = []
pages_to_fetch.extend([("added", u) for u in added_urls])
pages_to_fetch.extend([("updated", u["url"]) for u in updated_urls])

fetch_failures = []
prev_contents: dict[str, str] = {}  # url -> prior markdown text

for kind, url in pages_to_fetch:
    md_path_rel = url_to_path(url)
    if not md_path_rel:
        print(f"  Skip (no path): {url}")
        continue
    md_path = REPO / md_path_rel

    # Capture prior content for updated pages
    if kind == "updated" and md_path.exists():
        prev_contents[url] = md_path.read_text(encoding="utf-8", errors="replace")

    md_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        result = subprocess.run(
            ["python3", "tools/html_to_md.py", "--url", url, "--output", str(md_path)],
            capture_output=True, text=True, cwd=REPO, timeout=60
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr[:300])

        # Sanity check
        if md_path.exists():
            content = md_path.read_text(encoding="utf-8", errors="replace")
            if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                raise RuntimeError(f"Fetch blocked (content={len(content)} chars)")
            print(f"  OK [{kind}] {url} -> {md_path_rel} ({len(content)} chars)")
        else:
            raise RuntimeError("Output file not created")

    except Exception as e:
        err_str = str(e)
        print(f"  FAIL [{kind}] {url}: {err_str[:100]}")
        fetch_failures.append({"url": url, "error": err_str[:200]})
        # Don't overwrite existing if update failed
        if kind == "updated" and url in prev_contents:
            if md_path.exists():
                md_path.write_text(prev_contents[url])

print(f"  Fetch failures: {len(fetch_failures)}")

# ── STEP 6: analyze ──────────────────────────────────────────────────────────

print("\n=== STEP 6: Analyzing ===")

# Build analysis data
analysis_sections = {}

# Updated pages - compute diffs
analysis_sections["updated"] = []
for item in updated_urls:
    url = item["url"]
    md_path_rel = url_to_path(url)
    md_path = REPO / md_path_rel if md_path_rel else None

    failed = any(f["url"] == url for f in fetch_failures)
    if failed:
        analysis_sections["updated"].append({
            "url": url,
            "old_lastmod": item["old_lastmod"],
            "new_lastmod": item["new_lastmod"],
            "diff_summary": "FETCH FAILED - could not retrieve updated content"
        })
        continue

    current_text = ""
    if md_path and md_path.exists():
        current_text = md_path.read_text(encoding="utf-8", errors="replace")

    prior_text = prev_contents.get(url, "")

    # Simple diff: count changed lines
    prior_lines = set(prior_text.splitlines())
    current_lines = set(current_text.splitlines())
    added_lines = current_lines - prior_lines
    removed_lines = prior_lines - current_lines

    # Get meaningful content changes (skip blank lines)
    meaningful_added = [l for l in added_lines if l.strip() and len(l.strip()) > 10]
    meaningful_removed = [l for l in removed_lines if l.strip() and len(l.strip()) > 10]

    diff_summary = f"+{len(meaningful_added)} lines, -{len(meaningful_removed)} lines"
    if meaningful_added[:3]:
        diff_summary += f"\n  Sample additions: {'; '.join(meaningful_added[:3])[:200]}"
    if meaningful_removed[:3]:
        diff_summary += f"\n  Sample removals: {'; '.join(meaningful_removed[:3])[:200]}"

    analysis_sections["updated"].append({
        "url": url,
        "old_lastmod": item["old_lastmod"],
        "new_lastmod": item["new_lastmod"],
        "diff_summary": diff_summary
    })

# New pages - summarize
analysis_sections["added"] = []
for url in added_urls:
    md_path_rel = url_to_path(url)
    md_path = REPO / md_path_rel if md_path_rel else None

    failed = any(f["url"] == url for f in fetch_failures)
    summary = ""
    if not failed and md_path and md_path.exists():
        content = md_path.read_text(encoding="utf-8", errors="replace")
        # Extract first meaningful paragraph
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
        summary = " ".join(lines[:3])[:300] if lines else "(empty)"
    elif failed:
        summary = "FETCH FAILED"

    analysis_sections["added"].append({
        "url": url,
        "lastmod": current_urls[url],
        "path": md_path_rel or "unknown",
        "summary": summary
    })

analysis_sections["removed"] = removed_urls
analysis_sections["anomalies"] = anomalies
analysis_sections["fetch_failures"] = fetch_failures

# ── STEP 7: write analysis.md ────────────────────────────────────────────────

print("\n=== STEP 7: Writing analysis.md ===")

run_dir = REPO / f"runs/{RUN_ID}"
run_dir.mkdir(parents=True, exist_ok=True)

analysis_lines = [
    f"# Run Analysis: {RUN_ID}",
    f"",
    f"**Fetch time:** {FETCH_TIME}",
    f"**Run ID:** {RUN_ID}",
    f"",
    f"## Summary",
    f"",
    f"- Total current URLs: {len(current_urls)}",
    f"- Added: {len(added_urls)}",
    f"- Removed: {len(removed_urls)}",
    f"- Updated: {len(updated_urls)}",
    f"- Anomalies: {len(anomalies)}",
    f"- Fetch failures: {len(fetch_failures)}",
    f"- Sub-sitemaps: {len(sub_sitemap_urls)}",
    f"",
]

# Anomalies first
if anomalies:
    analysis_lines += ["## Anomalies (Highest Signal)", ""]
    for a in anomalies:
        analysis_lines += [
            f"### {a['kind']}: {a['url']}",
            f"{a['details']}",
            ""
        ]
else:
    analysis_lines += ["## Anomalies", "", "None detected.", ""]

# Significant updates
if analysis_sections["updated"]:
    analysis_lines += ["## Updated Pages", ""]
    for item in analysis_sections["updated"]:
        analysis_lines += [
            f"### {item['url']}",
            f"- lastmod: {item['old_lastmod']} → {item['new_lastmod']}",
            f"- {item['diff_summary']}",
            ""
        ]
else:
    analysis_lines += ["## Updated Pages", "", "None.", ""]

# New pages
if analysis_sections["added"]:
    analysis_lines += ["## New Pages", ""]
    for item in analysis_sections["added"]:
        analysis_lines += [
            f"### {item['url']}",
            f"- lastmod: {item['lastmod']}",
            f"- path: {item['path']}",
            f"- {item['summary'][:300]}",
            ""
        ]
else:
    analysis_lines += ["## New Pages", "", "None.", ""]

# Removals
if removed_urls:
    analysis_lines += ["## Removed Pages", ""]
    for url in removed_urls:
        analysis_lines += [f"- {url}"]
    analysis_lines += [""]
else:
    analysis_lines += ["## Removed Pages", "", "None.", ""]

# Fetch failures
if fetch_failures:
    analysis_lines += ["## Fetch Failures (needs follow-up)", ""]
    for f in fetch_failures:
        analysis_lines += [f"- **{f['url']}**: {f['error'][:200]}"]
    analysis_lines += [""]

(run_dir / "analysis.md").write_text("\n".join(analysis_lines))
print(f"  Written: runs/{RUN_ID}/analysis.md")

# ── STEP 8: update README.md ─────────────────────────────────────────────────

print("\n=== STEP 8: Updating README.md ===")

readme_path = REPO / "README.md"
existing_readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Build TL;DR
num_new = len(added_urls)
num_upd = len(updated_urls)
num_rem = len(removed_urls)
num_anom = len(anomalies)

if num_new == 0 and num_upd == 0 and num_rem == 0:
    tldr = (f"Routine monitoring run on {RUN_ID[:10]} found no changes to OpenAI's public sitemap. "
            f"The site currently lists {len(current_urls)} URLs across {len(sub_sitemap_urls)} sub-sitemaps.")
else:
    parts = []
    if num_new: parts.append(f"{num_new} new page{'s' if num_new != 1 else ''}")
    if num_upd: parts.append(f"{num_upd} updated page{'s' if num_upd != 1 else ''}")
    if num_rem: parts.append(f"{num_rem} removed page{'s' if num_rem != 1 else ''}")
    tldr = (f"On {RUN_ID[:10]}, OpenAI's public website showed {', '.join(parts)}. "
            f"The site currently lists {len(current_urls)} URLs across {len(sub_sitemap_urls)} sub-sitemaps.")

new_section_lines = [
    f"## {RUN_ID[:10]} — {RUN_ID}",
    f"",
    f"**TL;DR:** {tldr}",
    f"",
]

if anomalies:
    new_section_lines += ["### ⚠ Anomalies", ""]
    for a in anomalies:
        new_section_lines += [f"- **{a['kind']}** `{a['url']}`: {a['details'][:200]}"]
    new_section_lines += [""]

if added_urls:
    new_section_lines += ["### New Pages", ""]
    for item in analysis_sections["added"][:20]:
        url = item["url"]
        path = item["path"]
        lm = item["lastmod"] or "unknown"
        s = item["summary"][:150].replace("\n", " ") if item["summary"] else ""
        new_section_lines += [f"- [`{url}`]({path}) (lastmod: {lm}) — {s}"]
    if len(added_urls) > 20:
        new_section_lines += [f"- *...and {len(added_urls)-20} more*"]
    new_section_lines += [""]

if updated_urls:
    new_section_lines += ["### Updated Pages", ""]
    for item in analysis_sections["updated"][:20]:
        url = item["url"]
        path = url_to_path(url) or ""
        ds = item["diff_summary"].split("\n")[0]
        new_section_lines += [f"- [`{url}`]({path}) `{item['old_lastmod']}` → `{item['new_lastmod']}` — {ds}"]
    if len(updated_urls) > 20:
        new_section_lines += [f"- *...and {len(updated_urls)-20} more*"]
    new_section_lines += [""]

if removed_urls:
    new_section_lines += ["### Removed Pages", ""]
    for url in removed_urls[:20]:
        new_section_lines += [f"- `{url}`"]
    if len(removed_urls) > 20:
        new_section_lines += [f"- *...and {len(removed_urls)-20} more*"]
    new_section_lines += [""]

if fetch_failures:
    new_section_lines += ["### Fetch Failures", ""]
    for f in fetch_failures[:10]:
        new_section_lines += [f"- `{f['url']}`: {f['error'][:100]}"]
    new_section_lines += [""]

new_section_lines += [
    f"**Stats:** {len(current_urls)} total URLs | +{num_new} added | ~{num_upd} updated | -{num_rem} removed | {num_anom} anomalies | {len(sub_sitemap_urls)} sub-sitemaps",
    f"",
    "---",
    "",
]

new_section = "\n".join(new_section_lines)

# Find insertion point - after the first heading
lines = existing_readme.splitlines(keepends=True)
# Find first "## " section (or end of header block)
insert_pos = 0
found_first_section = False
for i, line in enumerate(lines):
    if line.startswith("## ") and i > 0:
        insert_pos = i
        found_first_section = True
        break

if found_first_section:
    new_readme = "".join(lines[:insert_pos]) + new_section + "".join(lines[insert_pos:])
else:
    new_readme = existing_readme + "\n" + new_section

readme_path.write_text(new_readme)
print(f"  README.md updated")

# ── STEP 9: update state/known_urls.json ─────────────────────────────────────

print("\n=== STEP 9: Updating state ===")

for url, lm in current_urls.items():
    if url not in state:
        state[url] = {
            "first_seen": RUN_ID,
            "last_seen": RUN_ID,
            "current_lastmod": lm,
            "lastmod_history": [{"run_id": RUN_ID, "lastmod": lm}] if lm else []
        }
    else:
        state[url]["last_seen"] = RUN_ID
        old_lm = state[url].get("current_lastmod")
        if old_lm != lm:
            state[url]["current_lastmod"] = lm
            if "lastmod_history" not in state[url]:
                state[url]["lastmod_history"] = []
            state[url]["lastmod_history"].append({"run_id": RUN_ID, "lastmod": lm})

# Mark removed URLs (don't delete, just don't update last_seen)
state_file.write_text(json.dumps(state, indent=2, sort_keys=True))
print(f"  state/known_urls.json updated ({len(state)} entries)")

# ── STEP 10: write diff.json ──────────────────────────────────────────────────

print("\n=== STEP 10: Writing diff.json ===")

# Determine baseline run_id from latest.xml filename history
prior_files = sorted(dated_dir.glob("*.xml"))
prior_files = [f for f in prior_files if f.name != "latest.xml" and f.name != f"{RUN_ID}.xml"]
baseline_run_id = prior_files[-1].stem if prior_files else None

diff_data = {
    "run_id": RUN_ID,
    "fetch_time": FETCH_TIME,
    "baseline": baseline_run_id,
    "added": added_urls,
    "removed": removed_urls,
    "updated": updated_urls,
    "anomalies": anomalies,
    "fetch_failures": fetch_failures
}

(run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2))
print(f"  Written: runs/{RUN_ID}/diff.json")

print(f"\n=== ALL STEPS COMPLETE ===")
print(f"Added: {num_new}, Updated: {num_upd}, Removed: {num_rem}, Anomalies: {num_anom}")
