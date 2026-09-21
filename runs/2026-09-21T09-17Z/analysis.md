# Run 2026-09-21T09-17Z — analysis

**Fetch window:** 2026-09-21T09:17:39Z – 2026-09-21T09:18:43Z UTC (sitemap fetch); page fetches immediately following.
**Baseline:** 2026-09-20T09-16Z (consecutive day, no gap).

## Summary

Quiet day. Sitemap union is unchanged in size: **1,974 total URLs across 42 sub-sitemaps**, identical to yesterday. 0 URLs added, 0 removed. 38 URLs had a `<lastmod>` bump; of those, only **4** carried any visible markdown diff after fetching and converting, and all 4 turn out to be routine "recent posts" carousel refreshes or a CDN asset-signature change — no page's own editorial content changed.

## Anomalies

None, after verification. No future-dated `<lastmod>` values, no backwards-moving `<lastmod>` values, no backdated new URLs (0 new URLs today), no reappeared URLs.

A naive single-sub-sitemap-per-URL diff initially flagged 4 URLs (`understanding-ai-and-learning-outcomes`, `global-affairs/new-economic-analysis`, `how-countries-can-end-the-capability-overhang`, `equipping-workers-with-insights-about-compensation`) as having "moved" from `sitemap.xml_global-affairs` to `sitemap.xml_global-affairs-news-listed`. Re-checked against the full multi-listing-aware section data: all 4 were **already present in both sections in yesterday's baseline** and are still present in both today — the earlier flag was a false positive from only keeping the last-seen section per URL, not a real change. (368 of today's 1,974 URLs are legitimately cross-listed in 2+ sub-sitemaps, e.g. `https://openai.com/news/` appears in 8 sections; any anomaly detection here must diff full section *sets* per URL, not a single value, to avoid this false-positive class going forward.)

## Significant updates (real content diff)

None. The 4 URLs with a visible markdown diff are all cosmetic/carousel-only:

- **[ChatGPT for Excel](../../pages/openai.com/index/chatgpt-for-excel/index.md)** — "recent posts" carousel swapped 3 cards (out with Bringing ChatGPT for Teachers to more districts / Learning never stops / GPT‑5.6 in Kiro, in with Reimagining advertising with AI / How to connect AI usage to business value / Now everyone can put data to work); a customer testimonial quote (Hg's Amr Ellabban) moved further down the page; and the global nav's "Latest Advancements" dropdown now includes a **GPT-6** entry linking to `/index/gpt-6-astra/` that wasn't rendered in this page's cached nav before. The nav addition is a sitewide change, not specific to this page — worth watching whether it's now permanent nav furniture.
- **[1Password](../../pages/openai.com/index/1password/index.md)** — carousel swapped one card (out with "Helping older adults use AI in everyday life", in with "Introducing the Australian Youth Safety Blueprint," published 2026-09-18, already covered previously).
- **[Gilbert + Tobin](../../pages/openai.com/index/gilbert-tobin/index.md)** — carousel swapped 3 cards (older-adults-AI, Reimagining advertising with AI, How to connect AI usage to business value → out; Australian Youth Safety Blueprint, Cooley GO Public, Astra for Law → in). Article content itself unchanged.
- **[SDG Group partner profile](../../pages/openai.com/business/partners/sdg-group/index.md)** — only the "Advanced Partner" badge SVG's CDN deploy-hash query parameter changed (`dpl_DytABQsw...` → `dpl_ACiXehaLG...`); visually identical asset.

## Routine updates (lastmod bump, no visible diff)

34 URLs bumped `<lastmod>` with zero markdown diff: 7 more `business/partners/*` profile pages (gusto, hubspot, quantiphi, quickbooks, stripe, contact-sales-financial-services), `business/solutions/finance/workflows/`, `form/openai-for-government/`, `products/release-notes/`, and ~24 `index/*` article pages including the full "disrupting malicious uses of AI" report series (9 pages), astra-for-law, chatgpt-for-teens, cooley-gopublic, detecting-wildfires-early, gpt-6-astra and gpt-6-astra-next-generation-work, growing-atv-big-air-tour, helping-older-adults-use-ai-in-everyday-life, how-to-connect-ai-usage-to-business-value, reimagining-advertising-with-ai, scaling-storage-one-billion-users-part-one, two-blind-brothers, unlocking-new-ways-of-working. This reads as background CDN/asset-signature churn and/or server-side re-render touching `lastmod` without any visible text/structure change.

## New pages

None. 0 URLs added to the sitemap today.

## Removed pages

None. 0 URLs removed from the sitemap today.

## Fetch failures

None. All 38 page fetches via `tools/html_to_md.py` succeeded with no Cloudflare-challenge blocks.

---
_Stats: 1974 total URLs | 0 added | 38 updated (4 with visible content diff, 0 substantive) | 0 removed | 0 anomalies | 42 sub-sitemaps_
