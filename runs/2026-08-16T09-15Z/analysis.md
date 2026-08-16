# Run 2026-08-16T09-15Z — Analysis

**Fetch time:** 2026-08-16T09:16:09Z UTC
**Baseline:** 2026-08-15T09-16Z (consecutive day)
**Sitemap-index locations:** 35 sub-sitemaps, all fetched successfully.
**Totals:** 1,584 URLs (unchanged) | 0 added | 38 updated (`<lastmod>` changed) | 0 removed | 0 sub-sitemap migrations | 0 timestamp anomalies

A quiet day by volume — the smallest lastmod-change count in recent runs (38, vs 128 on 2026-08-15 and 343 on 2026-08-14) — but one of the 38 changes is the most editorially significant single-line edit seen in this log: OpenAI's `/about/` page swapped its "Our plan for AGI" link to point at a different, newer essay.

## Anomalies

None of the defined timestamp-based checks triggered:
- No `<lastmod>` later than fetch time (latest observed lastmod today: `api-reserved-tier/` at 2026-08-16T09:00:05.901Z, ~16 minutes before fetch).
- No `<lastmod>` moved backwards vs the prior snapshot — all 38 changed URLs moved forward.
- No new URLs (0 added), so no backdating check applies.
- No removed-then-reappeared URLs (0 added, 0 removed).
- No URL moved between sub-sitemaps (0 migrations) — note: an initial pass of this run's tooling *appeared* to show 19 "migrations," but that was a false positive from this run's own file-naming choice (sanitizing `sitemap.xml/sora/` to `sora.xml` instead of the repo's established `sitemap.xml_sora.xml` convention used by prior runs' scripts). Corrected before comparing; the true migration count is 0. This is the same class of methodology bug flagged and corrected on 2026-08-13/2026-08-14 — worth hard-coding the exact `sanitize_name()` logic from `run_monitoring.py` into `tools/` so future runs don't re-trip it.

**Editorial finding (not a timestamp anomaly, but the highest-signal item today):** the `/about/` page's flagship "Our plan for AGI" link was retargeted from `/index/planning-for-agi-and-beyond/` to `/index/built-to-benefit-everyone-our-plan/`. Both target pages already existed in the sitemap before today (first_seen 2026-05-07 and 2026-06-09 respectively) — this is a link change on the About page, not a new-content event. See Notable updates below.

## Notable updates

- **[`/about/`](../../pages/openai.com/about/index.md)** — the "Our plan for AGI" link beneath the mission statement now points to [`/index/built-to-benefit-everyone-our-plan/`](../../pages/openai.com/index/built-to-benefit-everyone-our-plan/index.md) ("Built to benefit everyone: our plan," by Sam Altman and Jakub Pachocki, dated June 8, 2026) instead of the older [`/index/planning-for-agi-and-beyond/`](../../pages/openai.com/index/planning-for-agi-and-beyond/index.md). The new target essay lays out three "current main goals" (build an automated AI researcher, accelerate the economy, give everyone a personal AGI) and frames OpenAI as entering a "third phase" focused on making advanced AI abundant and affordable rather than purely on frontier capability. This is the company's front door swapping its canonical mission-statement link to a ~2-month-newer essay — worth flagging even though neither underlying page is new today, since it changes what a first-time visitor to openai.com/about is pointed toward.
- **Partner directory refresh (7 pages, same underlying pattern):** [`/business/partners/`](../../pages/openai.com/business/partners/index.md) and six partner detail pages — [`accenture`](../../pages/openai.com/business/partners/accenture/index.md), [`capgemini`](../../pages/openai.com/business/partners/capgemini/index.md), [`ernst-and-young`](../../pages/openai.com/business/partners/ernst-and-young/index.md), [`ibm`](../../pages/openai.com/business/partners/ibm/index.md), [`kpmg`](../../pages/openai.com/business/partners/kpmg/index.md), [`pwc`](../../pages/openai.com/business/partners/pwc/index.md) — all bumped `<lastmod>` by roughly 24h with byte-identical markdown. Server-side re-render, no visible content change.
- **Continuing pattern — nav-template flip-flop:** [`business/partners/cognizant/`](../../pages/openai.com/business/partners/cognizant/index.md) flipped from the old-style nav (Research/Products/Business/Developers/Company) to the new-style nav (Why OpenAI/Products/Solutions/Resources/Customers/Pricing, "Try OpenAI"/"Contact sales" CTAs) between the 2026-08-15 snapshot and today's fetch. This is the same unstable condition first flagged 2026-08-08 and still ongoing; cognizant itself has now flipped direction across multiple recent runs. Given the instability, this reads less like a rollout in progress and more like two nav templates being served inconsistently (A/B test or cache/edge inconsistency) rather than a one-way migration.
- The remaining 29 of 38 changed URLs (`api-reserved-tier`, 10 `business/plugins/*` pages, `business/solutions/finance/workflows`, `form/ultrafast`, 7 `index/*` posts including `sora`, `products/release-notes`, and the `signals/*` cluster) all show `<lastmod>` bumps with byte-identical markdown vs. the prior snapshot — routine re-renders, no substantive change.

## Routine, low-signal updates

Of the 38 lastmod-updated URLs, 36 changed only their `<lastmod>` timestamp with no markdown diff. Only 2 had an actual content diff: `/about/` (the AGI-plan link swap, above) and `/business/partners/cognizant/` (the nav-template flip, above).

## New pages

None. 0 URLs added to the sitemap today.

## Removals

None. 0 URLs removed from the sitemap today.

## Fetch failures

None. All 38 updated pages fetched cleanly via `tools/html_to_md.py` (curl-cffi, Chrome impersonation); no Cloudflare challenge pages, no undersized output.
