# Run 2026-09-27T09-16Z — analysis

Fetch time: 2026-09-27T09:16:59Z
Baseline: 2026-09-26T09-15Z
Sub-sitemaps fetched: 42 (union: 1,985 URLs, unchanged from baseline)

## Anomalies

None. Specifically checked and ruled out:

- **Future-dated `<lastmod>`**: none of the 1,985 current URLs have a `<lastmod>` later than this run's fetch time (2026-09-27T09:16:59Z).
- **Backwards-moving `<lastmod>`**: all 21 updated URLs moved forward in time relative to their prior recorded value; none regressed.
- **Backdated new URLs**: N/A — zero URLs added this run.
- **Disappeared/reappeared URLs**: N/A — zero URLs removed this run.
- **Sub-sitemap migration (false positive, ruled out)**: an initial pass flagged 4 URLs (`global-affairs/new-economic-analysis`, `index/equipping-workers-with-insights-about-compensation`, `index/how-countries-can-end-the-capability-overhang`, `index/understanding-ai-and-learning-outcomes`) as having moved from `sitemap.xml_global-affairs.xml` to `sitemap.xml_global-affairs-news-listed.xml`. On verification this was an artifact of the detection script's iteration order — these URLs are, and were in the prior snapshot too, legitimately listed in **both** sub-sitemaps simultaneously (387 URLs in the current snapshot are cross-listed in more than one sub-sitemap; this is a pre-existing, unchanged pattern, not a migration). No content or categorization actually changed.

## Updates

0 added, **21 updated** (lastmod bump only), 0 removed.

All 21 URLs with a changed `<lastmod>` were fetched fresh via `tools/html_to_md.py` and diffed byte-for-byte against the markdown captured from the prior commit. **All 21 produced a zero-line diff** — no substantive content change was detected in any of them, only a server-side `<lastmod>` timestamp refresh (likely a CMS re-save, cache/CDN touch, or minor non-visible metadata update). Per the task's diff hygiene, none of these are reported as "notable updates" in the README since there is nothing to describe.

Updated URLs (all content-identical to prior snapshot):

- /business/learn/how-our-data-analytics-team-uses-chatgpt-work/
- /business/learn/how-our-marketing-team-uses-chatgpt-work/
- /hugging-face-incident-and-misalignment/
- /index/accelerating-antibiotic-discovery/
- /index/astra-for-law/
- /index/australian-youth-safety-blueprint/
- /index/cooley-gopublic/
- /index/expanding-openai-academy-with-new-learning-paths/
- /index/grab-openai-ai-skills-southeast-asia/
- /index/hex-gpt-6-astra/
- /index/higgsfield-from-prompt-to-production-with-astra/
- /index/introducing-gpt-6-sol-and-luna/
- /index/openai-extends-cyber-access-to-ukraine-for-civilian-defense/
- /index/parallel-cuts-time-and-cost-with-astra/
- /index/reimagining-advertising-with-ai/
- /index/research-acceleration-view-inside-openai/
- /index/scaling-storage-one-billion-users-part-one/
- /index/two-years-of-openai-academy/
- /index/v7/
- /live/
- /products/release-notes/

## New pages

None.

## Removals

None.

## Fetch failures

None — all 21 fetches via `tools/html_to_md.py` succeeded (Chrome-impersonated curl-cffi, no Cloudflare challenge pages received).
