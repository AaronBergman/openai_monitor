#!/usr/bin/env python3
"""Canonical URL -> repo path mapping for openai_monitor.

Both the bootstrap and the daily routine MUST use this function so that the
same URL always maps to the same file on disk.

Mapping rules:
    https://openai.com/                         -> pages/openai.com/index.md
    https://openai.com/foo                      -> pages/openai.com/foo.md
    https://openai.com/foo/                     -> pages/openai.com/foo/index.md
    https://openai.com/foo/bar/                 -> pages/openai.com/foo/bar/index.md
    https://openai.com/foo/bar?x=1#frag         -> pages/openai.com/foo/bar.md
                                                   (query/fragment stripped)

Coexistence: `pages/openai.com/foo.md` (a file) and `pages/openai.com/foo/`
(a directory) can coexist on every modern filesystem and in git.

Usage as CLI:
    python tools/url_path.py https://openai.com/academy/codex/
    -> pages/openai.com/academy/codex/index.md
"""
import re
import sys
from urllib.parse import urlsplit


PAGES_ROOT = "pages"


def url_to_repo_path(url: str) -> str:
    parts = urlsplit(url)
    host = parts.netloc.lower()
    path = parts.path or "/"

    trailing_slash = path.endswith("/")
    segments = [s for s in path.split("/") if s]

    if not segments:
        return f"{PAGES_ROOT}/{host}/index.md"

    safe = [re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("._") or "_" for s in segments]

    if trailing_slash:
        return f"{PAGES_ROOT}/{host}/" + "/".join(safe) + "/index.md"
    return f"{PAGES_ROOT}/{host}/" + "/".join(safe) + ".md"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: url_path.py <url>", file=sys.stderr)
        return 2
    print(url_to_repo_path(sys.argv[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
