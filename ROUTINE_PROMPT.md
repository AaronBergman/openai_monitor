Your goal is to monitor the openai.com sitemap daily, detect every change, analyze the meaning, and accumulate the findings in this repo so a smart layperson can read README.md and understand what's been happening on OpenAI's public website.

SITEMAP INDEX: https://openai.com/sitemap.xml
This is a sitemap-INDEX (not a flat sitemap). It points to ~34 sub-sitemaps under https://openai.com/sitemap.xml/<section>/. You MUST recurse into every sub-sitemap and aggregate all the <url><loc> entries.

CLOUDFLARE NOTE: openai.com is fronted by Cloudflare with TLS-fingerprint bot detection. Plain `httpx`, `requests`, or `curl` from Python will receive HTTP 403 with body "Enable JavaScript and cookies to continue" on PAGE URLs (sitemap XML is unaffected). The repo's `tools/html_to_md.py` uses `curl-cffi` with `impersonate='chrome'` to bypass this. Do NOT roll your own fetch with httpx/requests for openai.com page content; it will silently produce 9KB of useless challenge-page HTML and break diffs. Always go through `tools/html_to_md.py --url <URL> --output <md_path>`. robots.txt explicitly allows scraping (`User-agent: * / Allow: /`).

REPO LAYOUT
- README.md                                     → public-facing accumulating changelog, newest-first
- sitemaps/openai.com/<run_id>.xml              → dated root sitemap-index snapshots
- sitemaps/openai.com/latest.xml                → most recent index (overwritten each run)
- sitemaps/openai.com/sub/<run_id>/*.xml        → dated sub-sitemap snapshots
- sitemaps/openai.com/sub/latest/*.xml          → most recent sub-sitemaps (overwritten each run)
- pages/openai.com/<path>.md                    → CURRENT markdown of each page (overwritten each run; git is the archive)
- runs/<run_id>/analysis.md                     → long-form analysis written this run
- runs/<run_id>/diff.json                       → machine-readable diff vs prior baseline
- state/known_urls.json                         → cumulative URL state: first_seen, last_seen, lastmod_history
- tools/html_to_md.py                           → THE conversion script (curl-cffi); always call this, never roll your own fetch or conversion
- tools/url_path.py                             → THE URL→repo-path mapping; always import or shell out to this
- tools/requirements.txt                        → pip dependencies (curl-cffi, html2text)

<run_id> = UTC time of run start, formatted YYYY-MM-DDTHH-MMZ.

PATH MAPPING — use tools/url_path.py, do not reinvent. Quick reference:
  https://openai.com/                       -> pages/openai.com/index.md
  https://openai.com/foo                    -> pages/openai.com/foo.md
  https://openai.com/foo/                   -> pages/openai.com/foo/index.md
  https://openai.com/academy/codex/         -> pages/openai.com/academy/codex/index.md
(Most openai.com URLs use trailing slashes, so most files will be index.md.)

TOOL INVOCATION
  pip install -r tools/requirements.txt --quiet              # once, at run start
  python tools/url_path.py <URL>                             # prints the repo path
  python tools/html_to_md.py --url <URL> --output <md_path>  # fetches via curl-cffi + converts in one shot
  python tools/html_to_md.py <html_in> <md_out>              # convert an already-saved HTML file

EACH RUN, IN ORDER

0. SETUP. From the repo root:
   - Set TZ=UTC for consistency.
   - `pip install -r tools/requirements.txt --quiet` (curl-cffi, html2text).
   - Compute run_id = UTC time of run start, formatted YYYY-MM-DDTHH-MMZ.

1. BASELINE. Read sitemaps/openai.com/latest.xml AND every file under sitemaps/openai.com/sub/latest/. The union of <url><loc> across all sub-sitemaps is your baseline URL set, with each URL's <lastmod>. Do NOT assume the prior run was exactly 24h ago; the routine may have missed days.

2. FETCH + SNAPSHOT.
   - Pull https://openai.com/sitemap.xml. Parse the <sitemap><loc> entries.
   - Recursively pull every sub-sitemap.
   - Save the root index to sitemaps/openai.com/<run_id>.xml AND overwrite latest.xml.
   - Save every sub-sitemap to sitemaps/openai.com/sub/<run_id>/<sanitized-name>.xml AND overwrite the matching file under sitemaps/openai.com/sub/latest/.
   - Record exact UTC fetch time.
   - The sitemap XML is reachable with plain httpx; you do not need curl-cffi for the sitemap step (only for page HTML).

3. DIFF current sitemap union vs baseline:
   - Added:   URLs in current but not baseline.
   - Removed: URLs in baseline but not current.
   - Updated: URLs in both whose <lastmod> changed.

4. ANOMALY DETECTION. Surface prominently:
   - <lastmod> later than fetch time (claimed future modification).
   - <lastmod> moved BACKWARDS vs prior snapshot (page now claims an earlier modification date than it did before — suspicious; possible republish or restoration).
   - New URL whose <lastmod> predates its first_seen by more than a few days (backdated, or page existed elsewhere first).
   - URL that disappeared and reappeared (consult state/known_urls.json).
   - URL that moved from one sub-sitemap to another (e.g., from /sitemap.xml/api/ to /sitemap.xml/page/) — note the migration.
   - Any other inconsistency between observation timestamps (yours) and claimed timestamps (theirs).

5. FETCH + CONVERT changed and new pages. For each Added or Updated URL:
   - Use tools/url_path.py to compute the destination markdown path.
   - Before overwriting an Updated page, capture the prior markdown for diffing in step 6 (e.g., `git show HEAD:<path> > /tmp/prev.md`).
   - Run `python tools/html_to_md.py --url <URL> --output <md_path>` — this is the ONLY supported fetch path. It uses curl-cffi with Chrome impersonation to get past Cloudflare.
   - Sanity check: if the resulting markdown is < 100 chars or contains "Enable JavaScript and cookies to continue", the fetch was blocked. Record this as a fetch failure and DO NOT overwrite the existing markdown (preserves the last-good snapshot).
   - If fetch fails, record clearly in runs/<run_id>/analysis.md with a "needs follow-up" note. Do not silently skip.

6. ANALYZE.
   - Updated pages: diff the captured prior markdown vs the freshly written markdown. Describe in plain language what substantively changed. Ignore noise (whitespace, trivial reordering).
   - New pages: summarize purpose, audience, key claims; contextualize against other recent additions ("appears related to X added on date Y", "fits with the recent push on Z").
   - Removed pages: note removal; the last snapshot lives in git history (`git log -- pages/openai.com/<path>.md`).

7. WRITE runs/<run_id>/analysis.md with structured findings, in this order: anomalies (highest signal), significant updates, routine updates, new pages, removals.

8. UPDATE README.md by PREPENDING a new dated section above the most recent existing run section:
   - One-paragraph TL;DR for a smart layperson.
   - Anomalies, called out clearly (never bury these).
   - Notable additions with plain-language summaries + relative links to the saved .md.
   - Notable updates with the specific substantive change.
   - Removals.
   - Stats footer: total URLs, # added, # updated, # removed, # anomalies, # sub-sitemaps.
   PRESERVE all prior README content. README is a permanent accumulating log.

9. UPDATE state/known_urls.json: bump last_seen for every URL still present, set first_seen for new URLs, append to lastmod_history when <lastmod> changes, set current_lastmod.

10. WRITE runs/<run_id>/diff.json with the structured diff:
    {
      "run_id": "...",
      "fetch_time": "...Z",
      "baseline": "<prior run_id or null>",
      "added":    ["url", ...],
      "removed":  ["url", ...],
      "updated":  [{"url": "...", "old_lastmod": "...", "new_lastmod": "..."}, ...],
      "anomalies": [{"kind": "...", "url": "...", "details": "..."}, ...],
      "fetch_failures": [{"url": "...", "error": "..."}, ...]
    }

11. COMMIT AND PUSH everything in one commit:
    <run_id>: N added, M updated, K removed, A anomalies

TIMESTAMP DISCIPLINE — never conflate these three:
- <lastmod>     = what OpenAI CLAIMS about a page.
- fetch time    = UTC time YOU actually retrieved the sitemap or page.
- first_seen    = earliest run_id when a URL appeared in any snapshot in this repo.
When describing what you did, cite observation timestamps. When describing what OpenAI asserts, cite <lastmod>. Anomalies live in the gap between these.

ROBUSTNESS
- If a hard error blocks the run (sitemap totally unfetchable, etc.), still commit a runs/<run_id>/analysis.md recording the failure and prepend a one-line README entry. The log stays continuous.
- Be idempotent: a duplicate run with the same run_id should not corrupt prior data — overwrite, don't duplicate.
- Bootstrap is already done. The first time you run, sitemaps/openai.com/latest.xml + sitemaps/openai.com/sub/latest/ already exist and pages/openai.com/ is already populated. Treat it as any other day: diff your fresh fetch against latest, expect very few changes.
- Be polite to Cloudflare: keep page-fetch parallelism modest (≤10 workers). The sitemap XML is fine at higher concurrency.
