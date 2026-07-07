# Run 2026-07-07T09-16Z — Analysis

Fetch time (UTC): 2026-07-07T09:18:38Z
Baseline: 2026-07-06T09-15Z
Sub-sitemaps: 34/34 fetched successfully
Total URLs in current snapshot: 1386 (unchanged from baseline)

## Anomalies

None detected this run.

- No `<lastmod>` later than fetch time (latest claimed lastmod was 2026-07-07T08:19:18Z, ~1h19m before fetch).
- No `<lastmod>` moved backwards vs. the prior snapshot.
- No added URLs, so no backdating check applicable.
- No URLs disappeared/reappeared vs. `state/known_urls.json`.
- No genuine sub-sitemap migrations (0 URLs changed which sub-sitemap they belong to).

## Significant updates

**1. Continued rollout of "Customer Stories" / "Partner Network" footer nav links, plus a new "Table of Contents" widget on older article pages.**

Yesterday's run (2026-07-06) first spotted two new footer nav links — "Customer Stories" (`/business/customer-stories/`) and "Partner Network" (`/business/partners/`) — appearing on 3 pages that still used an older page template. Today the same rollout hit 68 more pages, mostly older `/global-affairs/`, `/index/`, `/news/`, and `/policies/` articles (2019–2025 vintage posts and legacy policy pages). Both linked pages already existed in our tracking (first seen 2026-05-07 and 2026-06-17 respectively) — this is a template/navigation sync catching up stragglers, not new content.

A subset of ~13 of these pages (e.g. `openai-for-australia`, `openais-economic-blueprint`, `japan-economic-blueprint`, `musenet`, `us-caisi-uk-aisi-ai-update`, `how-your-data-is-used-to-improve-model-performance`) also picked up a new **"Table of Contents"** sidebar widget for the first time. Because of how OpenAI's page renders this addition, our markdown extraction shows the article's title/date/category block appearing twice in a row — this is a rendering artifact from the underlying page structure, not duplicated content on the live site.

A handful of pages that still carried the *very old* pre-redesign header (`Why OpenAI / Solutions / Resources / Customers / Pricing` nav, "Try OpenAI / Contact sales" CTA) — `openai-lp`, `enterprise-privacy`, `business/why-openai/startups`, `global-affairs/disrupting-malicious-uses-of-ai` — were fully migrated today to the current site template (`Research / Business / Developers / Company / Foundation` nav, "Log in / Try ChatGPT" CTA, restructured footer with a new "Developers" column). This nav taxonomy itself is not new — it has been live on most of the site since at least late June — today's change is just these specific legacy pages finally catching up.

**2. `/api/pricing/` was rebuilt into a dedicated, API-only pricing page.**

Previously `/api/pricing/` rendered essentially the same combined ChatGPT+API pricing content as `/business/pricing/` (plan tiers, ChatGPT Business/Enterprise cards, a shared FAQ). As of this run it is a standalone page: a per-model token-pricing table, an interactive pricing calculator (model selector, image-resolution toggle, live price computation), and an API-specific FAQ ("Which model should I use?", "How is pricing calculated for images?", "Can I set spending limits?", etc.). `/business/pricing/` itself was also touched (lastmod bump) but its content is byte-identical to yesterday — it continues to serve the combined ChatGPT-oriented pricing experience. This reads as OpenAI splitting API and ChatGPT pricing into two distinct destinations.

**3. Minor genuine text change:** the core-dump epidemiology postmortem (`/index/core-dump-epidemiology-data-infrastructure-bug/`) added a byline — "*By Nathan Bronson, Member of Technical Staff*" — its only change today.

## Routine updates

The remaining touched pages beyond the two items above show only:
- **Related-articles carousel rotation** (most `/global-affairs/` and `/index/` archive pages) — the "recirculation" widget at the bottom of old posts now surfaces newer articles (e.g. "How ChatGPT adoption has expanded", "Mapping Europe's AI Workforce Opportunity", "Helping build shared standards for advanced AI"). No change to the article body itself.
- **Category listing refresh** on the seven `/news/*` index pages (`/news/`, `/news/company-announcements/`, `/news/engineering/`, `/news/global-affairs/`, `/news/product-releases/`, `/news/safety-alignment/`, `/news/security/`) — these pages simply list the most recent posts in each category, so they update whenever new posts publish; expected behavior, not a template or policy change.
- **`brand/`** — lastmod bump only, page content unchanged aside from the nav/footer template sync described above.
- 6 pages had a pure lastmod bump with **zero** detectable content change: `business/pricing/`, `form/vc-partnerships-application/`, `index/diagnose-rare-childhood-diseases/`, `index/how-agents-are-transforming-work/`, `index/mapping-ai-jobs-transition-eu/`, `solutions/`.

## New pages

None. 0 added.

## Removals

None. 0 removed.

## Fetch failures

None. All 34 sub-sitemaps and all 76 updated pages fetched cleanly (no Cloudflare challenge-page content, no undersized responses).

## Stats

- Total URLs: 1386
- Added: 0
- Updated: 76
- Removed: 0
- Anomalies: 0
- Sub-sitemaps: 34/34
