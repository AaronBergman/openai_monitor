#!/usr/bin/env python3
"""Daily monitoring routine for OpenAI sitemap changes."""
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

# ─── Config ───────────────────────────────────────────────────────────────────
RUN_ID = "2026-06-24T09-15Z"
FETCH_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SITEMAP_INDEX = "https://openai.com/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
REPO = Path("/home/user/openai_monitor")
MAX_PAGE_WORKERS = 10

# ─── Helpers ──────────────────────────────────────────────────────────────────

def url_to_repo_path(url: str) -> str:
    parts = urlsplit(url)
    host = parts.netloc.lower()
    path = parts.path or "/"
    trailing_slash = path.endswith("/")
    segments = [s for s in path.split("/") if s]
    if not segments:
        return f"pages/{host}/index.md"
    safe = [re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("._") or "_" for s in segments]
    if trailing_slash:
        return f"pages/{host}/" + "/".join(safe) + "/index.md"
    return f"pages/{host}/" + "/".join(safe) + ".md"


def sanitize_sub_name(url: str) -> str:
    """Turn a sub-sitemap URL into a safe filename."""
    path = urlsplit(url).path.rstrip("/")
    # e.g. /sitemap.xml/page -> sitemap.xml_page.xml
    parts = [p for p in path.split("/") if p]
    return "_".join(parts) + ".xml"


def fetch_xml(url: str) -> str:
    import httpx
    r = httpx.get(url, timeout=30, follow_redirects=True)
    r.raise_for_status()
    return r.text


def parse_sitemap_index(xml_text: str):
    """Return list of sub-sitemap URLs from a sitemap index."""
    root = ET.fromstring(xml_text)
    locs = []
    for sm in root.findall("sm:sitemap", NS):
        loc = sm.find("sm:loc", NS)
        if loc is not None:
            locs.append(loc.text.strip())
    return locs


def parse_url_set(xml_text: str) -> dict:
    """Return {url: lastmod_or_None} from a urlset sitemap."""
    root = ET.fromstring(xml_text)
    urls = {}
    for url_elem in root.findall("sm:url", NS):
        loc = url_elem.find("sm:loc", NS)
        lastmod = url_elem.find("sm:lastmod", NS)
        if loc is not None:
            urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
    return urls


def load_baseline():
    """Load all URLs from sitemaps/openai.com/sub/latest/."""
    sub_latest = REPO / "sitemaps/openai.com/sub/latest"
    baseline = {}
    for fname in sorted(os.listdir(sub_latest)):
        if not fname.endswith(".xml"):
            continue
        fpath = sub_latest / fname
        try:
            tree = ET.parse(fpath)
            root = tree.getroot()
            for url_elem in root.findall("sm:url", NS):
                loc = url_elem.find("sm:loc", NS)
                lastmod = url_elem.find("sm:lastmod", NS)
                if loc is not None:
                    baseline[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
        except Exception as e:
            print(f"  [WARN] Error parsing baseline {fname}: {e}", file=sys.stderr)
    return baseline


def fetch_page_md(url: str, out_path: Path) -> tuple[bool, str]:
    """Fetch a page and write markdown. Returns (success, error_msg)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            [sys.executable, "tools/html_to_md.py", "--url", url, "--output", str(out_path)],
            capture_output=True, text=True, timeout=60, cwd=REPO
        )
        if result.returncode != 0:
            return False, result.stderr.strip() or "non-zero exit"
        # Sanity check
        if out_path.exists():
            content = out_path.read_text(encoding="utf-8", errors="replace")
            if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                return False, f"Blocked or empty: {len(content)} chars"
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)


def git_show_file(path: str) -> str | None:
    """Get the git HEAD version of a file."""
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{path}"],
            capture_output=True, text=True, timeout=10, cwd=REPO
        )
        if result.returncode == 0:
            return result.stdout
        return None
    except Exception:
        return None


def diff_md(old: str, new: str, context: int = 3) -> list[str]:
    """Produce a unified diff between old and new text."""
    import difflib
    return list(difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile="old",
        tofile="new",
        n=context,
    ))


def summarize_diff(diff_lines: list[str]) -> str:
    """Very brief summary of what changed in a diff."""
    added = [l[1:].strip() for l in diff_lines if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:].strip() for l in diff_lines if l.startswith("-") and not l.startswith("---")]
    added = [l for l in added if l]
    removed = [l for l in removed if l]
    parts = []
    if added:
        parts.append(f"+{len(added)} lines (e.g. {added[0][:80]!r})")
    if removed:
        parts.append(f"-{len(removed)} lines (e.g. {removed[0][:80]!r})")
    return "; ".join(parts) if parts else "(no textual diff)"


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print(f"=== OpenAI Monitor Run: {RUN_ID} ===")
    print(f"Fetch time: {FETCH_TIME}")

    # ── 1. Load baseline ──────────────────────────────────────────────────────
    print("\n[1] Loading baseline...")
    baseline = load_baseline()
    print(f"    Baseline: {len(baseline)} URLs")

    # ── 2. Fetch current sitemaps ─────────────────────────────────────────────
    print("\n[2] Fetching current sitemaps...")

    root_xml = fetch_xml(SITEMAP_INDEX)
    sub_urls = parse_sitemap_index(root_xml)
    print(f"    Found {len(sub_urls)} sub-sitemaps")

    # Save root index
    run_sitemap_dir = REPO / f"sitemaps/openai.com/sub/{RUN_ID}"
    run_sitemap_dir.mkdir(parents=True, exist_ok=True)
    (REPO / f"sitemaps/openai.com/{RUN_ID}.xml").write_text(root_xml, encoding="utf-8")
    (REPO / "sitemaps/openai.com/latest.xml").write_text(root_xml, encoding="utf-8")

    # Fetch sub-sitemaps
    current = {}  # url -> lastmod
    sub_xmls = {}  # sanitized_name -> xml_text

    for sub_url in sub_urls:
        try:
            xml_text = fetch_xml(sub_url)
            urls = parse_url_set(xml_text)
            current.update(urls)
            sname = sanitize_sub_name(sub_url)
            sub_xmls[sname] = xml_text
            print(f"    {sname}: {len(urls)} URLs")
        except Exception as e:
            print(f"    [WARN] Failed to fetch {sub_url}: {e}", file=sys.stderr)

    # Save sub-sitemaps
    sub_latest = REPO / "sitemaps/openai.com/sub/latest"
    sub_latest.mkdir(parents=True, exist_ok=True)
    for sname, xml_text in sub_xmls.items():
        (run_sitemap_dir / sname).write_text(xml_text, encoding="utf-8")
        (sub_latest / sname).write_text(xml_text, encoding="utf-8")

    print(f"    Total current URLs: {len(current)}")

    # ── 3. Diff ───────────────────────────────────────────────────────────────
    print("\n[3] Computing diff...")
    baseline_set = set(baseline.keys())
    current_set = set(current.keys())

    added = sorted(current_set - baseline_set)
    removed = sorted(baseline_set - current_set)
    updated = []
    for url in sorted(baseline_set & current_set):
        old_lm = baseline[url]
        new_lm = current[url]
        if old_lm != new_lm:
            updated.append({"url": url, "old_lastmod": old_lm, "new_lastmod": new_lm})

    print(f"    Added: {len(added)}, Removed: {len(removed)}, Updated: {len(updated)}")

    # ── 4. Anomaly detection ──────────────────────────────────────────────────
    print("\n[4] Detecting anomalies...")
    anomalies = []
    fetch_dt = datetime.fromisoformat(FETCH_TIME.replace("Z", "+00:00"))

    # Future lastmod
    for url, lm in current.items():
        if lm:
            try:
                lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
                if lm_dt > fetch_dt:
                    anomalies.append({
                        "kind": "future_lastmod",
                        "url": url,
                        "details": f"lastmod {lm} is after fetch time {FETCH_TIME}"
                    })
            except ValueError:
                pass

    # Backwards lastmod (updated but new lastmod is earlier)
    for item in updated:
        old_lm = item["old_lastmod"]
        new_lm = item["new_lastmod"]
        if old_lm and new_lm:
            try:
                old_dt = datetime.fromisoformat(old_lm.replace("Z", "+00:00"))
                new_dt = datetime.fromisoformat(new_lm.replace("Z", "+00:00"))
                if new_dt < old_dt:
                    anomalies.append({
                        "kind": "backwards_lastmod",
                        "url": item["url"],
                        "details": f"lastmod moved backwards: {old_lm} -> {new_lm}"
                    })
            except ValueError:
                pass

    # Load state for first_seen checks
    state_file = REPO / "state/known_urls.json"
    if state_file.exists():
        known_state = json.loads(state_file.read_text(encoding="utf-8"))
    else:
        known_state = {}

    # New URL with old lastmod (backdating)
    for url in added:
        lm = current[url]
        if lm:
            try:
                lm_dt = datetime.fromisoformat(lm.replace("Z", "+00:00"))
                # first_seen is now (this run), so backdated if lastmod is more than 7 days old
                age_days = (fetch_dt - lm_dt).days
                if age_days > 7:
                    anomalies.append({
                        "kind": "backdated_new_url",
                        "url": url,
                        "details": f"New URL with lastmod {lm} ({age_days} days old)"
                    })
            except ValueError:
                pass

    # Reappeared URLs
    for url in added:
        if url in known_state and known_state[url].get("last_seen"):
            last_seen = known_state[url]["last_seen"]
            anomalies.append({
                "kind": "reappeared_url",
                "url": url,
                "details": f"URL disappeared and reappeared; last_seen was {last_seen}"
            })

    print(f"    Anomalies detected: {len(anomalies)}")
    for a in anomalies[:10]:
        print(f"      [{a['kind']}] {a['url'][:80]}")

    # ── 5. Fetch pages ────────────────────────────────────────────────────────
    pages_to_fetch = []
    for url in added:
        pages_to_fetch.append(("added", url))
    for item in updated:
        pages_to_fetch.append(("updated", item["url"]))

    print(f"\n[5] Fetching {len(pages_to_fetch)} pages...")

    # Capture prior markdown for updated pages before fetching new
    prior_md = {}
    for kind, url in pages_to_fetch:
        if kind == "updated":
            rel_path = url_to_repo_path(url)
            old_content = git_show_file(rel_path)
            if old_content:
                prior_md[url] = old_content

    fetch_failures = []
    fetch_results = {}

    def fetch_one(kind_url):
        kind, url = kind_url
        rel_path = url_to_repo_path(url)
        out_path = REPO / rel_path
        success, err = fetch_page_md(url, out_path)
        return kind, url, rel_path, success, err

    with ThreadPoolExecutor(max_workers=MAX_PAGE_WORKERS) as executor:
        futures = {executor.submit(fetch_one, item): item for item in pages_to_fetch}
        for i, future in enumerate(as_completed(futures)):
            kind, url, rel_path, success, err = future.result()
            if success:
                fetch_results[url] = rel_path
                print(f"    [{i+1}/{len(pages_to_fetch)}] OK  {url[:70]}")
            else:
                fetch_failures.append({"url": url, "error": err})
                print(f"    [{i+1}/{len(pages_to_fetch)}] FAIL {url[:70]}: {err}")

    print(f"    Fetched OK: {len(fetch_results)}, Failed: {len(fetch_failures)}")

    # ── 6. Analyze ────────────────────────────────────────────────────────────
    print("\n[6] Analyzing changes...")
    analysis_items = []

    # Analyze updated pages
    for item in updated:
        url = item["url"]
        if url not in fetch_results:
            continue
        rel_path = fetch_results[url]
        new_content = (REPO / rel_path).read_text(encoding="utf-8", errors="replace") if (REPO / rel_path).exists() else ""
        old_content = prior_md.get(url, "")
        diff = diff_md(old_content, new_content)
        summary = summarize_diff(diff)
        analysis_items.append({
            "kind": "updated",
            "url": url,
            "rel_path": rel_path,
            "old_lastmod": item["old_lastmod"],
            "new_lastmod": item["new_lastmod"],
            "diff_summary": summary,
            "diff_lines": len(diff),
        })

    # Analyze new pages
    for url in added:
        if url not in fetch_results:
            continue
        rel_path = fetch_results[url]
        content = (REPO / rel_path).read_text(encoding="utf-8", errors="replace") if (REPO / rel_path).exists() else ""
        # Extract first meaningful lines for summary
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
        snippet = " ".join(lines[:5])[:300]
        analysis_items.append({
            "kind": "added",
            "url": url,
            "rel_path": rel_path,
            "lastmod": current[url],
            "snippet": snippet,
        })

    # ── 7. Write analysis.md ──────────────────────────────────────────────────
    print("\n[7] Writing analysis.md...")
    run_dir = REPO / f"runs/{RUN_ID}"
    run_dir.mkdir(parents=True, exist_ok=True)

    analysis_lines = [f"# Run {RUN_ID} Analysis\n",
                      f"**Fetch time:** {FETCH_TIME}  \n",
                      f"**Baseline:** prior run (latest.xml / sub/latest/)  \n",
                      f"**Stats:** {len(current)} total URLs | {len(added)} added | {len(updated)} updated | {len(removed)} removed | {len(anomalies)} anomalies\n\n"]

    # Anomalies
    if anomalies:
        analysis_lines.append("## Anomalies\n\n")
        for a in anomalies:
            analysis_lines.append(f"- **{a['kind']}**: `{a['url']}`  \n  {a['details']}\n")
        analysis_lines.append("\n")

    # Updated pages
    updated_items = [i for i in analysis_items if i["kind"] == "updated"]
    if updated_items:
        analysis_lines.append("## Updated Pages\n\n")
        for item in sorted(updated_items, key=lambda x: x["url"]):
            analysis_lines.append(f"### {item['url']}\n")
            analysis_lines.append(f"- lastmod: `{item['old_lastmod']}` → `{item['new_lastmod']}`\n")
            analysis_lines.append(f"- Diff: {item['diff_summary']}\n")
            analysis_lines.append(f"- File: `{item['rel_path']}`\n\n")

    # Added pages
    added_items = [i for i in analysis_items if i["kind"] == "added"]
    if added_items:
        analysis_lines.append("## New Pages\n\n")
        for item in sorted(added_items, key=lambda x: x["url"]):
            analysis_lines.append(f"### {item['url']}\n")
            analysis_lines.append(f"- lastmod: `{item['lastmod']}`\n")
            if item.get("snippet"):
                analysis_lines.append(f"- Summary: {item['snippet'][:200]}\n")
            analysis_lines.append(f"- File: `{item['rel_path']}`\n\n")

    # Removed pages
    if removed:
        analysis_lines.append("## Removed Pages\n\n")
        for url in removed[:50]:
            analysis_lines.append(f"- `{url}`\n")
        if len(removed) > 50:
            analysis_lines.append(f"- ... and {len(removed)-50} more\n")
        analysis_lines.append("\n")

    # Fetch failures
    if fetch_failures:
        analysis_lines.append("## Fetch Failures (needs follow-up)\n\n")
        for f in fetch_failures:
            analysis_lines.append(f"- `{f['url']}`: {f['error']}\n")
        analysis_lines.append("\n")

    (run_dir / "analysis.md").write_text("".join(analysis_lines), encoding="utf-8")
    print(f"    Written: runs/{RUN_ID}/analysis.md")

    # ── 8. Update README.md ───────────────────────────────────────────────────
    print("\n[8] Updating README.md...")
    readme_path = REPO / "README.md"
    existing_readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

    # Build new section
    readme_section = [f"## {RUN_ID}\n\n"]
    readme_section.append(f"**{FETCH_TIME}** — {len(added)} new pages, {len(updated)} updated, {len(removed)} removed, {len(anomalies)} anomalies across {len(current)} total URLs ({len(sub_urls)} sub-sitemaps).\n\n")

    # TL;DR paragraph
    if not added and not updated and not removed and not anomalies:
        readme_section.append("No changes detected. Routine health check — all URLs match the prior baseline.\n\n")
    else:
        summary_parts = []
        if added:
            summary_parts.append(f"{len(added)} new URL(s) appeared")
        if updated:
            summary_parts.append(f"{len(updated)} existing URL(s) had their `<lastmod>` timestamp updated")
        if removed:
            summary_parts.append(f"{len(removed)} URL(s) were removed from the sitemap")
        if anomalies:
            kinds = list(set(a["kind"] for a in anomalies))
            summary_parts.append(f"{len(anomalies)} anomaly(-ies) detected ({', '.join(kinds)})")
        readme_section.append("**TL;DR:** " + "; ".join(summary_parts) + ".\n\n")

    # Anomalies
    if anomalies:
        readme_section.append("### ⚠️ Anomalies\n\n")
        for a in anomalies[:20]:
            readme_section.append(f"- **{a['kind']}**: [`{a['url'].split('openai.com')[-1]}`]({a['url']}) — {a['details']}\n")
        if len(anomalies) > 20:
            readme_section.append(f"- ... and {len(anomalies)-20} more anomalies (see `runs/{RUN_ID}/analysis.md`)\n")
        readme_section.append("\n")

    # Notable additions
    if added_items:
        readme_section.append("### New Pages\n\n")
        for item in sorted(added_items, key=lambda x: x["url"])[:20]:
            slug = item["url"].replace("https://openai.com", "")
            rel_md = item["rel_path"]
            snippet = item.get("snippet", "")[:120]
            readme_section.append(f"- **[{slug}]({item['url']})** ([md]({rel_md})) — {snippet}\n")
        if len(added_items) > 20:
            readme_section.append(f"- ... and {len(added_items)-20} more new pages\n")
        readme_section.append("\n")

    # Notable updates
    if updated_items:
        readme_section.append("### Updated Pages\n\n")
        for item in sorted(updated_items, key=lambda x: x["url"])[:20]:
            slug = item["url"].replace("https://openai.com", "")
            readme_section.append(f"- **[{slug}]({item['url']})** — {item['diff_summary']}\n")
        if len(updated_items) > 20:
            readme_section.append(f"- ... and {len(updated_items)-20} more updates\n")
        readme_section.append("\n")

    # Removals
    if removed:
        readme_section.append("### Removed Pages\n\n")
        for url in removed[:15]:
            slug = url.replace("https://openai.com", "")
            readme_section.append(f"- `{slug}`\n")
        if len(removed) > 15:
            readme_section.append(f"- ... and {len(removed)-15} more removals\n")
        readme_section.append("\n")

    # Stats footer
    readme_section.append(f"_Stats: {len(current)} total URLs | {len(added)} added | {len(updated)} updated | {len(removed)} removed | {len(anomalies)} anomalies | {len(sub_urls)} sub-sitemaps_\n\n")
    readme_section.append("---\n\n")

    # Prepend to existing README
    new_section = "".join(readme_section)
    # Find where to insert (after the first H1 line, or at top)
    h1_match = re.search(r"^# .+\n", existing_readme, re.MULTILINE)
    if h1_match:
        insert_pos = h1_match.end()
        new_readme = existing_readme[:insert_pos] + "\n" + new_section + existing_readme[insert_pos:]
    else:
        new_readme = new_section + existing_readme

    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"    README.md updated")

    # ── 9. Update state/known_urls.json ───────────────────────────────────────
    print("\n[9] Updating known_urls.json...")
    today = RUN_ID[:10]

    # Update existing entries
    for url in current:
        lm = current[url]
        if url in known_state:
            entry = known_state[url]
            entry["last_seen"] = today
            # Track lastmod history
            if lm and (not entry.get("lastmod_history") or entry["lastmod_history"][-1] != lm):
                entry.setdefault("lastmod_history", [])
                entry["lastmod_history"].append(lm)
            entry["current_lastmod"] = lm
        else:
            # New URL
            known_state[url] = {
                "first_seen": today,
                "last_seen": today,
                "current_lastmod": lm,
                "lastmod_history": [lm] if lm else [],
            }

    # URLs no longer present: we do NOT remove them from state (they stay with last_seen)

    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(known_state, indent=2, sort_keys=True), encoding="utf-8")
    print(f"    state/known_urls.json updated: {len(known_state)} entries")

    # ── 10. Write diff.json ───────────────────────────────────────────────────
    print("\n[10] Writing diff.json...")
    diff_data = {
        "run_id": RUN_ID,
        "fetch_time": FETCH_TIME,
        "baseline": "prior (latest.xml / sub/latest/)",
        "added": added,
        "removed": removed,
        "updated": [{"url": u["url"], "old_lastmod": u["old_lastmod"], "new_lastmod": u["new_lastmod"]} for u in updated],
        "anomalies": anomalies,
        "fetch_failures": fetch_failures,
    }
    (run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2), encoding="utf-8")
    print(f"    Written: runs/{RUN_ID}/diff.json")

    print(f"\n=== Done. {len(added)} added, {len(updated)} updated, {len(removed)} removed, {len(anomalies)} anomalies ===")
    return {
        "added": len(added),
        "updated": len(updated),
        "removed": len(removed),
        "anomalies": len(anomalies),
        "fetch_failures": len(fetch_failures),
        "anomaly_details": anomalies,
        "total": len(current),
    }


if __name__ == "__main__":
    main()
