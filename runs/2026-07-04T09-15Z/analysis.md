# Run 2026-07-04T09-15Z — Analysis

**Fetch time (UTC):** 2026-07-04T09:16:02Z – 2026-07-04T09:22Z (sitemap index + 34 sub-sitemaps + 9 page fetches)
**Baseline:** 2026-07-03T09-16Z (prior run, commit e4c0359)

## Summary

Very quiet day. Sitemap index still lists exactly 34 sub-sitemaps (no section added/removed/renamed). Union across all sub-sitemaps: **1,386 URLs**, unchanged from baseline — **0 added, 0 removed**. **9 URLs** had a `<lastmod>` bump. No section migrations (no URL moved between sub-sitemaps).

## Anomalies

**None.** Checked all categories:
- No `<lastmod>` later than fetch time (2026-07-04T09:16Z) — the latest claimed lastmod among updates was 2026-07-04T08:30:24.381Z (`/solutions/`), safely in the past.
- No `<lastmod>` moved backwards vs. prior snapshot for any of the 9 updated URLs (all history entries in `state/known_urls.json` increase monotonically).
- No new URLs (added = 0), so no backdating check applicable.
- No disappeared/reappeared URLs.
- No cross-sitemap migrations.

## Updated pages (9)

Fetched and diffed all 9 against the prior committed markdown. Result: **8 of 9 had zero content diff** — the lastmod bump reflects a CMS republish/rebuild with no visible change to the rendered page. Only one page had a real (minor) diff.

| URL | Old lastmod | New lastmod | Content diff? |
|---|---|---|---|
| `/business/` | 2026-07-03T09:12:14Z | 2026-07-03T21:49:42Z | None (byte-identical) |
| `/solutions/` | 2026-06-25T16:40:48Z | 2026-07-04T08:30:24Z | None (byte-identical) |
| `/index/core-dump-epidemiology-data-infrastructure-bug/` | 2026-07-03T02:39:36Z | 2026-07-04T04:10:44Z | None (byte-identical) |
| `/index/genebench-pro/case-studies/` | 2026-07-02T22:57:25Z | 2026-07-03T20:54:23Z | None (byte-identical) |
| `/index/introducing-genebench-pro/` | 2026-07-03T08:47:32Z | 2026-07-03T20:54:36Z | None (byte-identical) |
| `/index/mapping-ai-jobs-transition-eu/` | 2026-06-29T10:24:03Z | 2026-07-04T06:22:39Z | None (byte-identical) |
| `/index/samsung-electronics-chatgpt-codex-deployment/` | 2026-07-01T04:14:31Z | 2026-07-03T19:32:12Z | None (byte-identical) |
| `/policies/professional-services-security-measures/` | 2026-07-01T18:51:37Z | 2026-07-03T09:50:37Z | None (byte-identical) |
| `/index/prc-linked-influence-operations-ai-debates/` | 2026-06-23T14:00:52Z | 2026-07-03T16:51:54Z | **Yes** (see below) |

### `/index/prc-linked-influence-operations-ai-debates/` — the one real diff

The "related Global Affairs articles" carousel at the bottom of the page refreshed to point at newer posts (e.g. now surfaces "Mapping Europe's AI Workforce Opportunity", Jun 29, and "How ChatGPT adoption has expanded", Jun 30, in place of older entries). The page's global footer also gained two links — "Customer Stories" and "Partner Network" — that are already present on other recently-fetched pages (`/business/`, the core-dump post, the Samsung post). This page just hadn't been re-rendered against the current site template since before those footer links were added; it isn't a new site-wide change today, just this one page catching up.

No headline, body copy, or claims changed on this page.

## New pages

None.

## Removals

None.

## Note on the 8 no-diff lastmod bumps

Across the OpenAI Next.js/Contentful stack, a `<lastmod>` bump with zero rendered-markdown diff typically means a CMS-side republish, cache invalidation, or a build touching page metadata/build IDs that don't surface in the visible HTML we convert to markdown (e.g. structured data, image CDN query params identical, or A/B experiment bucket assignment). Not treated as an anomaly since it's consistent with prior days' patterns (see e.g. runs from late June with 0-anomaly, high-lastmod-churn days).

## Fetch failures

None. All 34 sub-sitemaps and all 9 page fetches succeeded on the first attempt (via `tools/html_to_md.py`, `chrome110` impersonation).
