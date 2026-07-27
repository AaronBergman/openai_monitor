# Analysis — Run 2026-07-27T09-17Z

**Fetch time:** 2026-07-27T09:19:10Z
**Baseline:** 2026-07-26T09-15Z (consecutive day)
**Sitemap index:** unchanged — same 34 sub-sitemap `<loc>` entries as baseline.
**Total URLs:** 1484 (unchanged from yesterday)

## Anomalies

None. Specifically checked and clear:

- No future-dated `<lastmod>` (all 20 updated lastmods are ≤ fetch time 2026-07-27T09:19:10Z).
- No backwards-moving `<lastmod>` vs the prior snapshot.
- No new URLs (0 added), so no backdated-new-URL check applies.
- No removed URLs (0 removed), so no disappeared/reappeared check applies.
- No URL moved between sub-sitemap sections. **Verified with full per-URL set-comparison across all 34 sub-sitemaps** (every section a URL appears in, not just one) — an initial pass using a simpler "last file wins" URL→section mapping falsely flagged 4 URLs (`/global-affairs/new-economic-analysis/`, `/index/equipping-workers-with-insights-about-compensation/`, `/index/how-countries-can-end-the-capability-overhang/`, `/index/understanding-ai-and-learning-outcomes/`) as migrating from `global-affairs` to `global-affairs-news-listed`. Re-checked with full set comparison: these 4 URLs are listed in **both** `sitemap.xml_global-affairs.xml` and `sitemap.xml_global-affairs-news-listed.xml` in both yesterday's and today's snapshots — no change in section membership, just cross-listing (consistent with the "248 URLs legitimately appear in more than one sub-sitemap" note from the 2026-07-25 run). False positive, not a real migration.

## Significant updates

None. See "Routine updates" below — every `<lastmod>`-bumped page today is byte-identical to yesterday's markdown snapshot.

## Routine updates

20 URLs had their `<lastmod>` bumped (spanning the `api`, `business`, `chatgpt`/index, `product`, and `page` sections). All 20 were fetched via `tools/html_to_md.py` and diffed against the markdown captured immediately before overwrite; **all 20 are byte-identical** to yesterday's content:

| URL | old lastmod | new lastmod |
|---|---|---|
| `/api-reserved-tier/` | 2026-07-26T06:23:12.159Z | 2026-07-27T09:02:16.824Z |
| `/api-scale-tier/` | 2026-07-26T09:08:33.653Z | 2026-07-27T08:58:28.296Z |
| `/business/openai-presence/` | 2026-07-25T08:49:26.941Z | 2026-07-27T07:20:08.891Z |
| `/index/advancing-the-next-era-of-national-science/` | 2026-07-25T00:44:37.408Z | 2026-07-26T15:27:27.224Z |
| `/index/australian-payments-plus/` | 2026-07-25T06:55:27.471Z | 2026-07-27T06:43:50.772Z |
| `/index/building-openai-with-openai/` | 2026-07-26T08:33:16.701Z | 2026-07-27T09:09:56.601Z |
| `/index/codex-collaborator-creative-team/` | 2026-07-26T08:33:11.425Z | 2026-07-27T09:09:50.051Z |
| `/index/deutsche-telekom/` | 2026-07-25T06:52:59.137Z | 2026-07-27T05:28:45.020Z |
| `/index/health-in-chatgpt/` | 2026-07-26T08:43:14.333Z | 2026-07-27T08:21:22.599Z |
| `/index/introducing-chatgpt-health/` | 2026-07-25T07:00:27.412Z | 2026-07-26T20:18:03.017Z |
| `/index/introducing-openai-presence/` | 2026-07-25T08:49:35.011Z | 2026-07-27T07:20:12.326Z |
| `/index/openai-contract-data-agent/` | 2026-07-26T08:33:21.365Z | 2026-07-27T09:10:05.059Z |
| `/index/openai-gtm-assistant/` | 2026-07-26T08:33:20.882Z | 2026-07-27T09:10:05.417Z |
| `/index/openai-inbound-sales-assistant/` | 2026-07-26T08:33:20.501Z | 2026-07-27T09:10:01.324Z |
| `/index/openai-research-assistant/` | 2026-07-26T08:33:20.452Z | 2026-07-27T09:10:01.213Z |
| `/index/openai-scholars/` | 2026-07-24T18:51:28.355Z | 2026-07-26T15:58:29.709Z |
| `/index/openai-support-model/` | 2026-07-26T08:33:20.754Z | 2026-07-27T09:10:03.428Z |
| `/products/release-notes/` | 2026-07-26T09:00:41.569Z | 2026-07-27T08:30:01.329Z |
| `/signals/` | 2026-07-26T05:44:33.224Z | 2026-07-27T08:46:25.454Z |
| `/signals/research/` | 2026-07-26T05:44:50.178Z | 2026-07-27T08:46:28.590Z |

This is largely the same recurring set of pages seen touched (with zero visible change) on prior runs — in particular the six "OpenAI on OpenAI" internal-agent case studies (`openai-contract-data-agent`, `openai-gtm-assistant`, `openai-inbound-sales-assistant`, `openai-research-assistant`, `openai-support-model`) plus `building-openai-with-openai` and `codex-collaborator-creative-team`, which again cluster tightly in time (09:09:50–09:10:05 UTC today, vs. 08:33:1x UTC yesterday) — consistent with a recurring templated re-render/republish sweep over this same page cluster, still producing no detectable content drift. Two companion-page pairs also share near-identical timestamps: `business/openai-presence` + `index/introducing-openai-presence` (07:20:08 / 07:20:12) and `signals` + `signals/research` (08:46:25 / 08:46:28) — each pair reads as one edit event touching both a hub page and its paired detail page.

## New pages

None — 0 added URLs.

## Removals

None — 0 removed URLs.

## Fetch failures

None — all 20 fetches via `tools/html_to_md.py` succeeded (sizes 8.5KB–18.7KB, no Cloudflare challenge-page markers).

## Method note

Following the 2026-07-26 run's method, section-membership stability was verified using full set-comparison per URL across all 34 sub-sitemaps (every section a URL is listed under, not just a single "last file wins" mapping) — see Anomalies above for a false-positive migration this caught and corrected before it made it into this report.
