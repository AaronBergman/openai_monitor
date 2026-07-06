# Run 2026-07-06T09-15Z — Analysis

Fetch time (UTC): 2026-07-06T09:16:18Z
Baseline: 2026-07-05T09-15Z
Sub-sitemaps: 34/34 fetched successfully
Total URLs in current snapshot: 1386 (unchanged from baseline)

## Anomalies

None detected this run.

- No `<lastmod>` later than fetch time.
- No `<lastmod>` moved backwards vs. the prior snapshot.
- No added URLs, so no backdating check applicable.
- No URLs disappeared/reappeared vs. `state/known_urls.json`.
- No URLs migrated between sub-sitemaps.

## Significant updates

None. All six `<lastmod>` bumps this run correspond to trivial or non-substantive changes (see below) rather than new claims, policy changes, or meaningful content edits.

## Routine updates (6 URLs touched, 0 added, 0 removed)

1. **https://openai.com/policies/kr-privacy-policy/** (lastmod 2026-06-17 → 2026-07-06T02:24Z)
   Page content diff shows only the addition of two site-wide nav links ("Customer Stories", "Partner Network" under Business) — part of the global site header, not a change to the Korean privacy policy text itself.

2. **https://openai.com/form/economic-research-exchange/** (lastmod 2026-06-15 → 2026-07-06T08:25Z)
   Same global nav addition ("Customer Stories", "Partner Network") as above. No change to the form page's own content.

3. **https://openai.com/index/deployment-simulation/** (lastmod 2026-06-25 → 2026-07-06T01:55Z)
   The "related articles" widget at the bottom of the page changed: it now surfaces "Introducing GeneBench-Pro" (Jun 30, 2026) instead of "Dreaming: Better memory for a more helpful ChatGPT" (Jun 4, 2026). Both articles already existed in the sitemap prior to this run (in `publication` and `release` sub-sitemaps respectively) — this is a related-content recommendation shuffle, not a new publication.

4. **https://openai.com/index/mapping-ai-jobs-transition-eu/** (lastmod 2026-07-05 → 2026-07-06T08:12Z)
   No detectable content diff. lastmod touched with no visible markdown change (likely a metadata-only re-save, e.g. internal CMS field or unrendered A/B test bucket).

5. **https://openai.com/solutions/** (lastmod 2026-07-05 → 2026-07-06T08:20Z)
   No detectable content diff.

6. **https://openai.com/policies/usage-policies/** (lastmod 2026-06-24 → 2026-07-06T08:27Z)
   No detectable content diff.

## New pages

None — 0 added URLs this run.

## Removals

None — 0 removed URLs this run.

## Fetch failures

None — all 6 changed pages fetched cleanly via `tools/html_to_md.py` (curl-cffi/Chrome impersonation), no Cloudflare challenge pages encountered.
