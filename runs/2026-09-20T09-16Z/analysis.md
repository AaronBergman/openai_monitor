# Run 2026-09-20T09-16Z — analysis

**Fetch window:** 2026-09-20T09:18:40Z – 2026-09-20T09:18:49Z UTC (sitemap fetch); page fetches immediately following.
**Baseline:** 2026-09-19T09-15Z (consecutive day, no gap).

## Summary

Quiet day. Sitemap union is unchanged in size: **1,974 total URLs across 42 sub-sitemaps**, identical to yesterday. 0 URLs added, 0 removed, 0 sub-sitemap sections added/removed, 0 section migrations. 95 URLs had a `<lastmod>` bump; of those, only **10** carried a visible content diff after fetching and converting — the other 85 were re-deploys/cache-busts with byte-identical markdown (typically a changed CDN asset-signature query string with no visible text/structure change, or a timestamp-only touch).

## Anomalies

**None.** No future-dated `<lastmod>` values, no backwards-moving `<lastmod>` values, no backdated new URLs (0 new URLs today), no reappeared URLs, no section migrations.

## Significant updates (real content diff)

All 10 pages with a real diff are continuations of the plugin-directory template refresh that began on 2026-09-19 (documented in yesterday's README entry) — this looks like the rollout finishing propagation to a handful of pages that missed the first wave, rather than a new initiative:

- **9 plugin pages** picked up the same template changes yesterday's 224-plugin refresh applied elsewhere: [Cloudinary](../../pages/openai.com/business/plugins/cloudinary/index.md), [Conductor](../../pages/openai.com/business/plugins/conductor/index.md), [Coupler.io](../../pages/openai.com/business/plugins/coupler-io/index.md), [Coveo](../../pages/openai.com/business/plugins/coveo/index.md), [Datadog Experiments](../../pages/openai.com/business/plugins/datadog-experiments/index.md), [dbt](../../pages/openai.com/business/plugins/dbt/index.md), [Deepnote](../../pages/openai.com/business/plugins/deepnote/index.md), [Egnyte](../../pages/openai.com/business/plugins/egnyte/index.md), [Fireflies](../../pages/openai.com/business/plugins/fireflies/index.md).
  - "Add plugin" CTA → "Install plugin"
  - "## Common use cases" heading → "## What else can you do?"
  - Try-it links gained `surface=work` query parameter and button text changed from generic "(opens in a new window)" to "Try in ChatGPT Work(opens in a new window)"
  - Each use-case's one-sentence description paragraph (that used to sit above the screenshot) was removed, leaving just the screenshot + example-prompt image caption + try-it link
  - Datadog Experiments and Deepnote additionally had their top hero image strip collapse from 3 example-prompt thumbnails down to 1
- **[Cognition/Devin testing with Astra](../../pages/openai.com/index/cognition-devin-testing-with-astra/index.md)** — routine "recent posts" carousel refresh only: dropped the "Helping older adults use AI in everyday life" card, added the new "Introducing the Australian Youth Safety Blueprint" card (published 2026-09-18, already covered in yesterday's run). Not a change to the article's own content.

## Routine updates (lastmod bump, no visible diff)

85 URLs — mostly further plugin pages (~65 of them, spanning many categories: box, canva, circleback, clickhouse, clickup, clio, close, coda, codex-security, coingecko, coinmarketcap, company-knowledge, context7, coursera-learning, courtlistener, creative-claw, daloopa, datadog, datasite, deepjudge, demandbase, descript, digitalocean, documents, docusign, dropbox, dropbox-dash, easyreply, elevenlabs, elicit, exa, explain-video-generator, factset, fal, fathom, fieldy, figma, financial-datasets, firebase, firecrawl, floot, foreflight-mobile, forms-ai, g2, gamma, gitbook, honeybook, hubspot, mercury, paypal, quickbooks, shopify, slack, stripe, wix), plus the plugins directory landing page itself, `business/model/`, `business/contact-sales-legal/`, `chatgpt-work/`, several `index/*` article/case-study pages (an-alien-mind, apple-is-getting-this-wrong, astra-for-law, cooley-gopublic, the 9 disrupting-malicious-uses-of-ai-* pages, gpt-6-astra and gpt-6-astra-next-generation-work, helping-older-adults-use-ai-in-everyday-life, how-to-connect-ai-usage-to-business-value, navier-stokes-solution, put-data-to-work, reimagining-advertising-with-ai, scaling-storage-one-billion-users-part-one), `products/release-notes/`, and one form page (`form/sponsored-agents-hubspot/`).

Given none of these produced a visible markdown diff, this reads as background CDN/asset-signature churn (image URLs in these templates embed expiring signed query params) rather than editorial activity.

## New pages

None. 0 URLs added to the sitemap today.

## Removed pages

None. 0 URLs removed from the sitemap today.

## Fetch failures

None. All 95 page fetches via `tools/html_to_md.py` succeeded with no Cloudflare-challenge blocks.

---
_Stats: 1974 total URLs | 0 added | 95 updated (10 with visible content diff) | 0 removed | 0 anomalies | 42 sub-sitemaps_
