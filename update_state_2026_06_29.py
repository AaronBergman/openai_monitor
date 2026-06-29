#!/usr/bin/env python3
"""Update state/known_urls.json for the 2026-06-29T09-15Z run."""
import json
from pathlib import Path

RUN_ID = "2026-06-29T09-15Z"
REPO_ROOT = Path("/home/user/openai_monitor")

diff_path = REPO_ROOT / f"runs/{RUN_ID}/diff.json"
state_path = REPO_ROOT / "state/known_urls.json"

diff = json.loads(diff_path.read_text())
known = json.loads(state_path.read_text()) if state_path.exists() else {}

# Merge all current URLs (build from the fresh sub-sitemaps)
import xml.etree.ElementTree as ET
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

current = {}
sub_latest = REPO_ROOT / "sitemaps/openai.com/sub/latest"
for xml_file in sub_latest.glob("*.xml"):
    try:
        root = ET.fromstring(xml_file.read_text())
        for url in root.findall("sm:url", NS):
            loc = url.find("sm:loc", NS)
            lastmod = url.find("sm:lastmod", NS)
            if loc is not None:
                current[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
    except Exception as e:
        print(f"Warning: {xml_file}: {e}")

# Update last_seen for all current URLs
for url, lastmod in current.items():
    if url not in known:
        # New URL
        known[url] = {
            "first_seen": RUN_ID,
            "last_seen": RUN_ID,
            "current_lastmod": lastmod,
            "lastmod_history": [{"run_id": RUN_ID, "lastmod": lastmod}] if lastmod else []
        }
    else:
        entry = known[url]
        entry["last_seen"] = RUN_ID
        # Track lastmod changes
        if lastmod != entry.get("current_lastmod"):
            history = entry.get("lastmod_history", [])
            history.append({"run_id": RUN_ID, "lastmod": lastmod})
            entry["lastmod_history"] = history
            entry["current_lastmod"] = lastmod

# DON'T update last_seen for removed URLs (they just don't appear in current)

state_path.write_text(json.dumps(known, indent=2, sort_keys=True))
print(f"Updated state/known_urls.json: {len(known)} URLs tracked")
