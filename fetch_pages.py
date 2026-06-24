#!/usr/bin/env python3
"""Fetch pages from the diff.json and update analysis."""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path("/home/user/openai_monitor")
RUN_ID = "2026-06-24T09-15Z"
MAX_WORKERS = 8

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
CA_BUNDLE = "/root/.ccr/ca-bundle.crt"


def url_to_repo_path(url: str) -> str:
    from urllib.parse import urlsplit
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


def git_show_file(path: str) -> str | None:
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


def diff_md(old: str, new: str) -> list[str]:
    import difflib
    return list(difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile="old", tofile="new", n=2,
    ))


def summarize_diff(diff_lines: list[str]) -> str:
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


def fetch_page(url: str, out_path: Path, env: dict) -> tuple[bool, str]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            [sys.executable, "tools/html_to_md.py", "--url", url, "--output", str(out_path)],
            capture_output=True, text=True, timeout=60, cwd=REPO, env=env
        )
        if result.returncode != 0:
            return False, (result.stderr or result.stdout).strip()[:200]
        if out_path.exists():
            content = out_path.read_text(encoding="utf-8", errors="replace")
            if len(content) < 100 or "Enable JavaScript and cookies to continue" in content:
                return False, f"Blocked or empty ({len(content)} chars)"
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)[:100]


def main():
    diff_path = REPO / f"runs/{RUN_ID}/diff.json"
    diff_data = json.loads(diff_path.read_text(encoding="utf-8"))

    added = diff_data["added"]
    updated = diff_data["updated"]

    pages_to_fetch = [(u, "added") for u in added] + [(u["url"], "updated") for u in updated]
    print(f"Pages to fetch: {len(pages_to_fetch)} ({len(added)} added, {len(updated)} updated)")

    # Capture prior markdown for updated pages
    prior_md = {}
    for url, kind in pages_to_fetch:
        if kind == "updated":
            rel = url_to_repo_path(url)
            old = git_show_file(rel)
            if old:
                prior_md[url] = old

    # Build env with SSL cert
    env = os.environ.copy()
    env["SSL_CERT_FILE"] = CA_BUNDLE
    env["REQUESTS_CA_BUNDLE"] = CA_BUNDLE

    fetch_failures = []
    fetch_results = {}

    def do_fetch(args):
        url, kind = args
        rel = url_to_repo_path(url)
        out_path = REPO / rel
        ok, err = fetch_page(url, out_path, env)
        return url, kind, rel, ok, err

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(do_fetch, item): item for item in pages_to_fetch}
        for i, future in enumerate(as_completed(futures)):
            url, kind, rel, ok, err = future.result()
            if ok:
                fetch_results[url] = (kind, rel)
                print(f"  [{i+1}/{len(pages_to_fetch)}] OK   {url[:75]}")
            else:
                fetch_failures.append({"url": url, "error": err})
                print(f"  [{i+1}/{len(pages_to_fetch)}] FAIL {url[:60]}: {err[:40]}")

    print(f"\nFetched: {len(fetch_results)} OK, {len(fetch_failures)} failed")

    # Analyze results
    analysis_items = []

    for url, (kind, rel) in fetch_results.items():
        out_path = REPO / rel
        new_content = out_path.read_text(encoding="utf-8", errors="replace") if out_path.exists() else ""

        if kind == "added":
            lines = [l.strip() for l in new_content.splitlines() if l.strip() and not l.startswith("#")]
            snippet = " ".join(lines[:5])[:300]
            # Find lastmod from diff
            lm = next((u for u in diff_data["updated"] if u.get("url") == url), {})
            analysis_items.append({
                "kind": "added", "url": url, "rel_path": rel,
                "lastmod": next((u["new_lastmod"] for u in diff_data["updated"] if u["url"] == url), None),
                "snippet": snippet,
            })
        else:  # updated
            old_content = prior_md.get(url, "")
            diff = diff_md(old_content, new_content)
            summary = summarize_diff(diff)
            entry = next((u for u in diff_data["updated"] if u["url"] == url), {})
            analysis_items.append({
                "kind": "updated", "url": url, "rel_path": rel,
                "old_lastmod": entry.get("old_lastmod"),
                "new_lastmod": entry.get("new_lastmod"),
                "diff_summary": summary,
                "diff_lines": len(diff),
            })

    # Re-read current added lastmods from sitemap data
    import xml.etree.ElementTree as ET
    current = {}
    sub_latest = REPO / "sitemaps/openai.com/sub/latest"
    for fname in os.listdir(sub_latest):
        if fname.endswith(".xml"):
            try:
                tree = ET.parse(sub_latest / fname)
                root = tree.getroot()
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                for ue in root.findall("sm:url", ns):
                    loc = ue.find("sm:loc", ns)
                    lm = ue.find("sm:lastmod", ns)
                    if loc is not None:
                        current[loc.text.strip()] = lm.text.strip() if lm is not None else None
            except Exception:
                pass

    for item in analysis_items:
        if item["kind"] == "added" and not item.get("lastmod"):
            item["lastmod"] = current.get(item["url"])

    # Write updated analysis.md
    run_dir = REPO / f"runs/{RUN_ID}"

    analysis_lines = [
        f"# Run {RUN_ID} Analysis\n\n",
        f"**Fetch time:** {diff_data['fetch_time']}  \n",
        f"**Baseline:** {diff_data['baseline']}  \n",
        f"**Stats:** {len(current)} total URLs | {len(added)} added | {len(updated)} updated | "
        f"{len(diff_data.get('removed', []))} removed | {len(diff_data.get('anomalies', []))} anomalies\n\n",
    ]

    # Anomalies
    anomalies = diff_data.get("anomalies", [])
    if anomalies:
        analysis_lines.append("## Anomalies\n\n")
        for a in anomalies:
            analysis_lines.append(f"- **{a['kind']}**: `{a['url']}`  \n  {a['details']}\n")
        analysis_lines.append("\n")

    # New pages
    new_items = [i for i in analysis_items if i["kind"] == "added"]
    if new_items:
        analysis_lines.append("## New Pages\n\n")
        for item in sorted(new_items, key=lambda x: x["url"]):
            analysis_lines.append(f"### {item['url']}\n")
            analysis_lines.append(f"- lastmod: `{item.get('lastmod')}`\n")
            if item.get("snippet"):
                analysis_lines.append(f"- Summary: {item['snippet'][:300]}\n")
            analysis_lines.append(f"- File: `{item['rel_path']}`\n\n")

    # Updated pages (key ones)
    upd_items = [i for i in analysis_items if i["kind"] == "updated"]
    if upd_items:
        analysis_lines.append("## Updated Pages\n\n")
        # Sort by number of diff lines (most changed first)
        upd_sorted = sorted(upd_items, key=lambda x: x.get("diff_lines", 0), reverse=True)
        for item in upd_sorted[:50]:
            analysis_lines.append(f"### {item['url']}\n")
            analysis_lines.append(f"- lastmod: `{item['old_lastmod']}` → `{item['new_lastmod']}`\n")
            analysis_lines.append(f"- Diff: {item['diff_summary']}\n")
            analysis_lines.append(f"- Diff lines: {item['diff_lines']}\n")
            analysis_lines.append(f"- File: `{item['rel_path']}`\n\n")
        if len(upd_sorted) > 50:
            analysis_lines.append(f"... and {len(upd_sorted)-50} more updates (smaller changes)\n\n")

    # Removed
    removed = diff_data.get("removed", [])
    if removed:
        analysis_lines.append("## Removed Pages\n\n")
        for url in removed:
            analysis_lines.append(f"- `{url}`\n")
        analysis_lines.append("\n")

    # Fetch failures
    all_failures = list(fetch_failures)
    if diff_data.get("fetch_failures"):
        all_failures = list(fetch_failures)  # use fresh only

    if all_failures:
        analysis_lines.append("## Fetch Failures (needs follow-up)\n\n")
        for f in all_failures[:20]:
            analysis_lines.append(f"- `{f['url']}`: {f['error']}\n")
        if len(all_failures) > 20:
            analysis_lines.append(f"- ... and {len(all_failures)-20} more\n")
        analysis_lines.append("\n")

    (run_dir / "analysis.md").write_text("".join(analysis_lines), encoding="utf-8")
    print(f"Written: runs/{RUN_ID}/analysis.md")

    # Update diff.json with new fetch failures
    diff_data["fetch_failures"] = fetch_failures
    (run_dir / "diff.json").write_text(json.dumps(diff_data, indent=2), encoding="utf-8")

    return analysis_items, fetch_failures, new_items, upd_items, removed


if __name__ == "__main__":
    result = main()
    print("\nDone!")
