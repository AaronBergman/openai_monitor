#!/usr/bin/env python3
"""Canonical HTML -> Markdown converter for openai_monitor.

This is THE conversion logic. Both the bootstrap and every daily routine run
must use this exact script so bootstrap markdown and daily markdown are
byte-comparable. Conversion drift would manifest as fake "changes" in diffs.

openai.com is fronted by Cloudflare with TLS-fingerprint bot detection that
rejects plain Python clients (httpx, requests). We use curl-cffi with
`impersonate='chrome'` to send a real Chrome TLS handshake. The sitemap XML
is reachable without this, but page HTML is not.

Usage:
    python tools/html_to_md.py < input.html > output.md
    python tools/html_to_md.py input.html output.md
    python tools/html_to_md.py --url https://openai.com/foo/ --output out.md
    python tools/html_to_md.py --url https://openai.com/foo/      # writes md to stdout

Dependencies: curl-cffi, html2text.
Install: pip install -r tools/requirements.txt
"""
import argparse
import sys

import html2text


def html_to_md(html: str) -> str:
    h = html2text.HTML2Text()
    h.body_width = 0          # do not hard-wrap; line wrapping creates noisy diffs
    h.ignore_images = False
    h.ignore_links = False
    h.ignore_emphasis = False
    h.protect_links = True
    h.unicode_snob = True
    h.single_line_break = False
    return h.handle(html)


def fetch_html(url: str, timeout: float = 30.0) -> str:
    """Fetch a URL with Cloudflare-bypassing TLS impersonation."""
    import os
    from curl_cffi import requests
    ca_bundle = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE") or True
    # Use chrome110 fingerprint — compatible with proxy TLS re-termination
    r = requests.get(url, impersonate="chrome110", timeout=timeout, allow_redirects=True,
                     verify=ca_bundle)
    r.raise_for_status()
    return r.text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", nargs="?", help="Input HTML file (default: stdin)")
    ap.add_argument("output", nargs="?", help="Output markdown file (default: stdout)")
    ap.add_argument("--url", help="Fetch this URL (with curl-cffi Chrome impersonation) and convert it")
    ap.add_argument("--output", dest="output_flag", help="Output markdown file (alternative to positional)")
    args = ap.parse_args()

    if args.url:
        html = fetch_html(args.url)
    elif args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    md = html_to_md(html)

    out_path = args.output_flag or args.output
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        sys.stdout.write(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
