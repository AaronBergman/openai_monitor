#!/usr/bin/env python3
"""
Full monitoring run for openai.com sitemap changes.
"""
import os, sys, json, re, subprocess, shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

RUN_ID = "2026-05-21T09-15Z"
REPO_ROOT = Path(__file__).parent.parent
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

def fetch_xml(url):
    """Fetch XML from a URL using curl with a browser User-Agent."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-A",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
             "--max-time", "30", url],
            capture_output=True, text=True
        )
        if result.returncode != 0 or not result.stdout.strip():
            print(f"  ERROR fetching {url}: curl failed (rc={result.returncode})")
            return None
        if "Enable JavaScript" in result.stdout:
            print(f"  ERROR fetching {url}: Cloudflare challenge")
            return None
        return result.stdout
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

def parse_sitemap_index(xml_text):
    """Parse sitemap index, return list of sub-sitemap URLs."""
    root = ET.fromstring(xml_text)
    locs = []
    for sitemap in root.findall(f"{{{NS}}}sitemap"):
        loc = sitemap.findtext(f"{{{NS}}}loc")
        if loc:
            locs.append(loc.strip())
    return locs

def parse_sub_sitemap(xml_text):
    """Parse sub-sitemap, return dict of {url: lastmod or None}."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url_elem in root.findall(f"{{{NS}}}url"):
        loc = url_elem.findtext(f"{{{NS}}}loc")
        lastmod = url_elem.findtext(f"{{{NS}}}lastmod")
        if loc:
            urls[loc.strip()] = (lastmod or "").strip()
    return urls

def sanitize_name(url):
    """Convert sub-sitemap URL to filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "_")
    host = parsed.netloc.replace(".", "_")
    return f"_{host}_{path}.xml"

def url_to_path(url):
    """Use tools/url_path.py to get repo-relative path."""
    result = subprocess.run(
        ["python", str(REPO_ROOT / "tools" / "url_path.py"), url],
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    if result.returncode == 0:
        return result.stdout.strip()
    return None

def fetch_page_to_md(url, md_path):
    """Fetch a page and convert to markdown."""
    result = subprocess.run(
        ["python", str(REPO_ROOT / "tools" / "html_to_md.py"), "--url", url, "--output", str(md_path)],
        capture_output=True, text=True, cwd=str(REPO_ROOT), timeout=120
    )
    return result.returncode == 0

def get_file_from_git(git_path):
    """Get file content from git HEAD."""
    result = subprocess.run(
        ["git", "show", f"HEAD:{git_path}"],
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    if result.returncode == 0:
        return result.stdout
    return None

def md_is_valid(path):
    """Check if markdown file looks valid (not a Cloudflare challenge page)."""
    if not path.exists():
        return False
    content = path.read_text(encoding="utf-8", errors="replace")
    if len(content) < 100:
        return False
    if "Enable JavaScript and cookies to continue" in content:
        return False
    return True

def diff_text(old, new):
    """Return a simple line-diff summary."""
    old_lines = set(old.splitlines()) if old else set()
    new_lines = set(new.splitlines()) if new else set()
    added = [l for l in new_lines - old_lines if l.strip()]
    removed = [l for l in old_lines - new_lines if l.strip()]
    return added[:20], removed[:20]

def main():
    print(f"=== OpenAI Monitor Run: {RUN_ID} ===")
    print(f"Fetch time: {FETCH_TIME}")

    # ── 1. BASELINE ──────────────────────────────────────────────────────────
    print("\n[1] Loading baseline...")
    baseline_urls = {}  # {url: lastmod}

    latest_sub_dir = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / "latest"
    for xml_file in sorted(latest_sub_dir.glob("*.xml")):
        content = xml_file.read_text(encoding="utf-8")
        try:
            urls = parse_sub_sitemap(content)
            baseline_urls.update(urls)
        except Exception as e:
            print(f"  Warning: could not parse {xml_file.name}: {e}")

    print(f"  Baseline: {len(baseline_urls)} URLs")

    # ── 2. FETCH + SNAPSHOT ───────────────────────────────────────────────────
    print("\n[2] Fetching fresh sitemaps...")
    root_xml = fetch_xml("https://openai.com/sitemap.xml")
    if not root_xml:
        print("  FATAL: Could not fetch root sitemap. Aborting.")
        # Write failure analysis
        run_dir = REPO_ROOT / "runs" / RUN_ID
        run_dir.mkdir(parents=True, exist_ok=True)
        (run_dir / "analysis.md").write_text(
            f"# Run {RUN_ID}\n\nFATAL: Root sitemap unreachable at {FETCH_TIME}.\n"
        )
        return

    # Save root index
    sitemap_dir = REPO_ROOT / "sitemaps" / "openai.com"
    sitemap_dir.mkdir(parents=True, exist_ok=True)
    (sitemap_dir / f"{RUN_ID}.xml").write_text(root_xml)
    (sitemap_dir / "latest.xml").write_text(root_xml)

    sub_urls = parse_sitemap_index(root_xml)
    print(f"  Found {len(sub_urls)} sub-sitemaps")

    # Fetch sub-sitemaps
    run_sub_dir = REPO_ROOT / "sitemaps" / "openai.com" / "sub" / RUN_ID
    run_sub_dir.mkdir(parents=True, exist_ok=True)
    latest_sub_dir.mkdir(parents=True, exist_ok=True)

    current_urls = {}  # {url: lastmod}
    url_to_sitemap = {}  # {url: sub-sitemap name}

    for sub_url in sub_urls:
        name = sanitize_name(sub_url)
        print(f"  Fetching: {sub_url}")
        sub_xml = fetch_xml(sub_url)
        if not sub_xml:
            print(f"    WARNING: Could not fetch {sub_url}")
            continue
        (run_sub_dir / name).write_text(sub_xml)
        (latest_sub_dir / name).write_text(sub_xml)
        try:
            urls = parse_sub_sitemap(sub_xml)
            for u in urls:
                url_to_sitemap[u] = name
            current_urls.update(urls)
        except Exception as e:
            print(f"    Warning: parse error on {name}: {e}")

    print(f"  Current: {len(current_urls)} URLs across {len(sub_urls)} sub-sitemaps")

    # ── 3. DIFF ───────────────────────────────────────────────────────────────
    print("\n[3] Diffing...")
    baseline_set = set(baseline_urls.keys())
    current_set = set(current_urls.keys())

    added = sorted(current_set - baseline_set)
    removed = sorted(baseline_set - current_set)
    updated = []
    for url in sorted(current_set & baseline_set):
        old_lm = baseline_urls[url]
        new_lm = current_urls[url]
        if old_lm != new_lm:
            updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

    print(f"  Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}")

    # ── 4. ANOMALY DETECTION ──────────────────────────────────────────────────
    print("\n[4] Checking anomalies...")
    anomalies = []

    fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

    # Load known_urls for history
    known_urls_path = REPO_ROOT / "state" / "known_urls.json"
    try:
        known_urls = json.loads(known_urls_path.read_text())
    except Exception:
        known_urls = {}

    for url, lastmod in current_urls.items():
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
        except Exception:
            continue
        # Future lastmod
        if lm_dt > fetch_dt:
            anomalies.append({
                "kind": "future_lastmod",
                "url": url,
                "details": f"lastmod {lastmod} is after fetch time {FETCH_TIME}"
            })
        # Backwards lastmod
        if url in known_urls:
            hist = known_urls[url].get("lastmod_history", [])
            if hist:
                prev_lm = hist[-1]
                try:
                    prev_dt = datetime.fromisoformat(prev_lm.replace("Z", "+00:00"))
                    if lm_dt < prev_dt:
                        anomalies.append({
                            "kind": "backwards_lastmod",
                            "url": url,
                            "details": f"lastmod moved backwards from {prev_lm} to {lastmod}"
                        })
                except Exception:
                    pass

    # New URLs with old lastmod (backdated)
    for url in added:
        lastmod = current_urls[url]
        if not lastmod:
            continue
        try:
            lm_dt = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
            first_seen_str = RUN_ID.replace("T", "T").replace("-", ":", 2).replace("Z", "+00:00")
            # Simple: just check if lastmod is >7 days before today
            today = datetime.now(timezone.utc)
            if (today - lm_dt).days > 7:
                anomalies.append({
                    "kind": "backdated_new_url",
                    "url": url,
                    "details": f"New URL has lastmod {lastmod}, which is {(today - lm_dt).days} days ago"
                })
        except Exception:
            pass

    # Disappeared and reappeared
    for url in added:
        if url in known_urls and known_urls[url].get("last_seen"):
            prev_last = known_urls[url]["last_seen"]
            if prev_last != RUN_ID:
                anomalies.append({
                    "kind": "reappeared_url",
                    "url": url,
                    "details": f"URL previously seen in {known_urls[url]['first_seen']}, disappeared, reappeared now"
                })

    print(f"  Anomalies: {len(anomalies)}")

    # ── 5. FETCH + CONVERT CHANGED/NEW PAGES ─────────────────────────────────
    print("\n[5] Fetching changed/new pages...")
    fetch_failures = []
    page_diffs = {}  # {url: (old_md, new_md)}

    pages_to_fetch = list(added) + [u["url"] for u in updated]
    # Limit to avoid hammering; prioritize
    print(f"  Pages to fetch: {len(pages_to_fetch)}")

    # For updated pages, capture old content first
    for item in updated:
        url = item["url"]
        rel_path = url_to_path(url)
        if rel_path:
            old_content = get_file_from_git(rel_path)
            if old_content:
                page_diffs[url] = {"old": old_content}

    # Fetch pages (modest parallelism via subprocess, sequential for safety)
    import concurrent.futures

    def fetch_one(url):
        rel_path = url_to_path(url)
        if not rel_path:
            return url, False, "Could not compute path"
        md_path = REPO_ROOT / rel_path
        md_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            ok = fetch_page_to_md(url, md_path)
            if not ok or not md_is_valid(md_path):
                return url, False, "Fetch failed or invalid content"
            content = md_path.read_text(encoding="utf-8", errors="replace")
            return url, True, content
        except Exception as e:
            return url, False, str(e)

    # Batch in groups of 10
    batch_size = 10
    results = []
    for i in range(0, len(pages_to_fetch), batch_size):
        batch = pages_to_fetch[i:i+batch_size]
        print(f"  Fetching batch {i//batch_size + 1}: {len(batch)} pages...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
            futs = {ex.submit(fetch_one, url): url for url in batch}
            for fut in concurrent.futures.as_completed(futs):
                url, ok, content = fut.result()
                results.append((url, ok, content))
                if not ok:
                    print(f"    FAIL: {url}: {content}")
                    fetch_failures.append({"url": url, "error": content})
                else:
                    print(f"    OK:   {url}")
                    if url in page_diffs:
                        page_diffs[url]["new"] = content

    # For added pages, just store new content
    for url, ok, content in results:
        if ok and url in added:
            rel_path = url_to_path(url)
            if rel_path:
                md_path = REPO_ROOT / rel_path
                if md_path.exists():
                    page_diffs[url] = {"new": content}

    # ── 6. ANALYZE ────────────────────────────────────────────────────────────
    print("\n[6] Analyzing changes...")

    analysis_sections = []

    # Anomalies
    if anomalies:
        lines = ["## Anomalies\n"]
        for a in anomalies:
            lines.append(f"- **{a['kind']}**: `{a['url']}`  \n  {a['details']}")
        analysis_sections.append("\n".join(lines))

    # Significant updates
    update_notes = []
    for item in updated:
        url = item["url"]
        old_lm = item["old_lastmod"]
        new_lm = item["new_lastmod"]
        note = f"- `{url}`\n  - lastmod: `{old_lm}` → `{new_lm}`"
        if url in page_diffs and "old" in page_diffs[url] and "new" in page_diffs[url]:
            added_lines, removed_lines = diff_text(page_diffs[url]["old"], page_diffs[url]["new"])
            if added_lines or removed_lines:
                note += f"\n  - Content changed: +{len(added_lines)} lines, -{len(removed_lines)} lines"
                if added_lines[:3]:
                    note += f"\n  - Sample added: {added_lines[0][:120]!r}"
        update_notes.append(note)

    if update_notes:
        analysis_sections.append("## Updated Pages\n\n" + "\n\n".join(update_notes))

    # New pages
    new_notes = []
    for url in added:
        lm = current_urls[url]
        note = f"- `{url}` (lastmod: `{lm}`)"
        if url in page_diffs and "new" in page_diffs[url]:
            content = page_diffs[url]["new"]
            # First 300 chars of content as summary
            preview = content[:300].replace("\n", " ").strip()
            note += f"\n  - Preview: {preview!r}"
        new_notes.append(note)

    if new_notes:
        analysis_sections.append("## New Pages\n\n" + "\n".join(new_notes))

    # Removals
    if removed:
        removal_notes = [f"- `{url}` (was lastmod: `{baseline_urls[url]}`)" for url in removed]
        analysis_sections.append("## Removed Pages\n\n" + "\n".join(removal_notes))

    # Fetch failures
    if fetch_failures:
        fail_notes = [f"- `{f['url']}`: {f['error']}" for f in fetch_failures]
        analysis_sections.append("## Fetch Failures\n\n" + "\n".join(fail_notes))

    # ── 7. WRITE ANALYSIS ─────────────────────────────────────────────────────
    print("\n[7] Writing analysis...")
    run_dir = REPO_ROOT / "runs" / RUN_ID
    run_dir.mkdir(parents=True, exist_ok=True)

    analysis_md = f"""# Run {RUN_ID}

**Fetch time:** {FETCH_TIME}
**Baseline:** prior run (sitemaps/openai.com/sub/latest/)
**Total URLs (current):** {len(current_urls)}
**Sub-sitemaps:** {len(sub_urls)}

## Summary
- Added: {len(added)}
- Updated: {len(updated)}
- Removed: {len(removed)}
- Anomalies: {len(anomalies)}
- Fetch failures: {len(fetch_failures)}

{chr(10).join(analysis_sections)}
"""
    (run_dir / "analysis.md").write_text(analysis_md)

    # ── 8. UPDATE README ──────────────────────────────────────────────────────
    print("\n[8] Updating README...")
    readme_path = REPO_ROOT / "README.md"
    existing_readme = readme_path.read_text(encoding="utf-8")

    # Build new section
    tl_dr = f"OpenAI sitemap monitoring run on {RUN_ID[:10]}: {len(added)} new URL(s), {len(updated)} updated, {len(removed)} removed."
    if anomalies:
        tl_dr += f" **{len(anomalies)} anomaly(ies) detected** (see below)."

    readme_new_section = f"""## {RUN_ID[:10]} — Monitoring Run

**TL;DR:** {tl_dr}

"""
    if anomalies:
        readme_new_section += "### Anomalies\n"
        for a in anomalies[:10]:
            readme_new_section += f"- **{a['kind']}**: `{a['url']}` — {a['details']}\n"
        readme_new_section += "\n"

    if added:
        readme_new_section += f"### New Pages ({len(added)})\n"
        for url in added[:20]:
            rel_path = url_to_path(url)
            lm = current_urls[url]
            if rel_path and (REPO_ROOT / rel_path).exists():
                readme_new_section += f"- [`{url}`]({rel_path}) (lastmod: {lm})\n"
            else:
                readme_new_section += f"- `{url}` (lastmod: {lm})\n"
        if len(added) > 20:
            readme_new_section += f"- ... and {len(added) - 20} more\n"
        readme_new_section += "\n"

    if updated:
        readme_new_section += f"### Updated Pages ({len(updated)})\n"
        for item in updated[:20]:
            readme_new_section += f"- `{item['url']}`: lastmod `{item['old_lastmod']}` → `{item['new_lastmod']}`\n"
        if len(updated) > 20:
            readme_new_section += f"- ... and {len(updated) - 20} more\n"
        readme_new_section += "\n"

    if removed:
        readme_new_section += f"### Removed Pages ({len(removed)})\n"
        for url in removed[:10]:
            readme_new_section += f"- `{url}`\n"
        if len(removed) > 10:
            readme_new_section += f"- ... and {len(removed) - 10} more\n"
        readme_new_section += "\n"

    readme_new_section += f"**Stats:** {len(current_urls)} total URLs | +{len(added)} added | ~{len(updated)} updated | -{len(removed)} removed | {len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps\n\n---\n\n"

    # Prepend to existing README (after first heading if present)
    lines = existing_readme.split("\n")
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_pos = i + 1
            # Skip blank lines after heading
            while insert_pos < len(lines) and not lines[insert_pos].strip():
                insert_pos += 1
            break

    new_readme = "\n".join(lines[:insert_pos]) + "\n\n" + readme_new_section + "\n".join(lines[insert_pos:])
    readme_path.write_text(new_readme)

    # ── 9. UPDATE STATE ───────────────────────────────────────────────────────
    print("\n[9] Updating state/known_urls.json...")
    for url in current_urls:
        lm = current_urls[url]
        if url not in known_urls:
            known_urls[url] = {
                "first_seen": RUN_ID,
                "last_seen": RUN_ID,
                "current_lastmod": lm,
                "lastmod_history": [lm] if lm else []
            }
        else:
            known_urls[url]["last_seen"] = RUN_ID
            old_lm = known_urls[url].get("current_lastmod", "")
            if lm and lm != old_lm:
                hist = known_urls[url].get("lastmod_history", [])
                if not hist or hist[-1] != lm:
                    hist.append(lm)
                known_urls[url]["lastmod_history"] = hist
                known_urls[url]["current_lastmod"] = lm

    known_urls_path.write_text(json.dumps(known_urls, indent=2, sort_keys=True))

    # ── 10. WRITE DIFF.JSON ───────────────────────────────────────────────────
    print("\n[10] Writing diff.json...")
    # Find prior run_id
    runs_dir = REPO_ROOT / "runs"
    prior_runs = sorted([d.name for d in runs_dir.iterdir() if d.is_dir() and d.name != RUN_ID])
    prior_run_id = prior_runs[-1] if prior_runs else None

    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": prior_run_id,
        "added": added,
        "removed": removed,
        "updated": updated,
        "anomalies": anomalies,
        "fetch_failures": fetch_failures
    }
    (run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2))

    print("\n=== Run complete ===")
    print(f"  Added: {len(added)}, Updated: {len(updated)}, Removed: {len(removed)}")
    print(f"  Anomalies: {len(anomalies)}, Failures: {len(fetch_failures)}")

    return diff_data

if __name__ == "__main__":
    os.chdir(REPO_ROOT)
    main()
