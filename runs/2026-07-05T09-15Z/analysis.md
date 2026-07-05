# Run 2026-07-05T09-15Z — Analysis

**Fetch time:** 2026-07-05T09:16:55Z
**Baseline:** 2026-07-04T09-15Z (2026-07-04T09:16:02Z)
**Sub-sitemaps recursed:** 34/34, all HTTP 200
**Total URL universe:** 1386 (unchanged for the fifth consecutive run)

## Anomalies

None. Specifically checked and clear:
- No `<lastmod>` later than fetch time (latest observed lastmod was 2026-07-05T09:09:26Z, ~7 minutes before fetch).
- No `<lastmod>` moved backwards relative to its prior recorded value for any of the 8 updated URLs — all 8 new lastmods are strictly later than the previous snapshot's.
- No URLs added or removed, so no backdating, reappearance, or migration-between-sub-sitemaps checks apply this run. (Section-membership was also explicitly re-checked across all 1386 common URLs — zero URLs changed sub-sitemap.)

## Significant updates

None. All 8 lastmod bumps below turned out to be pure CMS republish/timestamp events with **zero** byte-level content change in the converted markdown.

## Routine updates (8 of 8, all byte-identical content)

| URL | Old lastmod | New lastmod |
|---|---|---|
| `/business/solutions/data/` | 2026-07-01T08:12:07Z | 2026-07-04T11:47:53Z |
| `/business/solutions/design/` | 2026-06-26T12:18:30Z | 2026-07-04T11:46:42Z |
| `/business/solutions/engineering/` | 2026-06-26T21:24:39Z | 2026-07-04T11:47:15Z |
| `/business/solutions/finance/` | 2026-06-26T12:18:27Z | 2026-07-04T11:48:21Z |
| `/business/solutions/marketing/` | 2026-06-29T05:15:29Z | 2026-07-04T11:48:41Z |
| `/index/core-dump-epidemiology-data-infrastructure-bug/` | 2026-07-04T04:10:44Z | 2026-07-05T09:09:26Z |
| `/index/mapping-ai-jobs-transition-eu/` | 2026-07-04T06:22:39Z | 2026-07-05T04:25:10Z |
| `/solutions/` | 2026-07-04T08:30:24Z | 2026-07-05T03:55:29Z |

For each, the freshly fetched markdown was diffed byte-for-byte (`diff -u`) against the prior git-committed snapshot; every diff returned empty. The four `/business/solutions/*` pages all got timestamp bumps clustered within a 2-minute window on 2026-07-04 (11:46–11:48Z), consistent with a single CMS template deploy touching that whole solutions-vertical group without changing any of their visible content. The other three (the core-dump postmortem, the EU jobs-transition report, and the top-level `/solutions/` page) each ticked forward again — these three have now shown fresh timestamps with no content change on multiple consecutive runs, suggesting they're on some kind of periodic re-render/cache-bust cycle (e.g., recirculation widget re-evaluation) rather than genuine edits.

## New pages

None.

## Removals

None.

## Fetch failures

None. All 8 updated-URL fetches via `tools/html_to_md.py` succeeded (sizes 8.6KB–29KB, no Cloudflare challenge markers).
