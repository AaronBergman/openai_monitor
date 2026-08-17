# Run 2026-08-17T09-20Z — analysis

- Fetch time (sitemap index + sub-sitemaps): ~2026-08-17T09:20–09:21Z
- Fetch time (33 changed pages): ~2026-08-17T09:21–09:23Z
- Baseline: 2026-08-16T09-15Z (prior run)
- Sub-sitemaps: 35 (unchanged count)
- Total unique URLs: 1,584 (unchanged count)
- Added: 0 · Removed: 0 · Updated (lastmod changed): 33 · Anomalies: 0

## Anomalies

None this run.

- No `<lastmod>` timestamps later than fetch time.
- No `<lastmod>` moved backwards vs. the prior snapshot.
- No new URLs (none added this run, so no backdating check applicable).
- No URL disappeared/reappeared (none removed this run).
- **False-positive check, not an anomaly:** an earlier pass of the diff script flagged 4 URLs (`global-affairs/new-economic-analysis/`, `index/equipping-workers-with-insights-about-compensation/`, `index/how-countries-can-end-the-capability-overhang/`, `index/understanding-ai-and-learning-outcomes/`) as having "migrated" from `sitemap.xml_global-affairs.xml` to `sitemap.xml_global-affairs-news-listed.xml`. On verification via `git diff` against the previous snapshot, both sub-sitemap files are byte-identical to yesterday's — these 4 URLs have always been listed in *both* sub-sitemaps simultaneously (duplicate cross-listing, a pre-existing structural quirk, not new today). The apparent "migration" was an artifact of the diffing script only keeping one sub-sitemap key per URL in a dict, keyed by iteration order. No actual sitemap-membership change occurred. Noted here for transparency; not included in README as a real event.

## Significant updates (content actually changed)

1. **[`business/plugins/sales/`](../../pages/openai.com/business/plugins/sales/index.md)** — nav-template flip: switched from the older business-specific nav ("Why OpenAI / Products / Solutions / Resources / Customers / Pricing", "Try OpenAI" + "Contact sales") to the current sitewide nav ("Research / Products / Business / Developers / Company / Foundation", "Log in" + "Try ChatGPT(opens in a new window)"). Same unresolved, first-flagged-2026-08-08 flip-flop bug tracked across many prior runs. No other content change.
2. **[`business/solutions/cybersecurity/`](../../pages/openai.com/business/solutions/cybersecurity/index.md)** — nav-template flip in the *opposite* direction: sitewide nav → old business-specific nav. Same bug, same run, flipping both ways simultaneously on different pages — consistent with flaky template caching / an unresolved A-B condition rather than a deliberate rollout. No other content change.
3. **[`index/improving-gpt-5-6-sol-in-chatgpt/`](../../pages/openai.com/index/improving-gpt-5-6-sol-in-chatgpt/index.md)** — routine "related articles" widget rotation: added a card linking to `index/previewing-ultrafast/` (published 2026-08-13, already known), dropped the card linking to `index/premium-seats-chatgpt-business/`. No body-text change.

## Routine updates (lastmod bump, no visible content change)

- **8 `/business/partners/*` pages** (`accenture`, `accenture-federal-services`, `capgemini`, `cognizant`, `ernst-and-young`, `ibm`, `kpmg`, `pwc`) — the partner-tier badge SVG's cache-busting `?dpl=` query parameter changed (`dpl_5xfYDbfSF5CJypESTKB8K4dtnxRu` → `dpl_8juo9XDHg5MmkQkGaWYYuUPqDCAz`) on all 8 simultaneously — a platform-wide deploy/asset-hash bump, not a content edit.
- **22 other pages** picked up a fresh `<lastmod>` with byte-identical markdown to the prior snapshot: `api-reserved-tier`, `business/partners/` (index), 11 `business/plugins/*` entries (`bigquery`, `databricks`, `figma`, `investment-banking`, `notion`, `product-design`, `public-equity-investing`, `replit`, `salesforce`, `snowflake`, `vercel`), `index/builders-guide-to-gpt-5-6`, `index/dali-rajic-chief-revenue-officer`, `index/how-enterprises-put-ai-to-work`, `index/previewing-ultrafast`, `index/third-party-cyber-evaluations-involving-openai-models`, `index/zapier`, `products/release-notes`, `signals/enterprise-data`, `solutions/industries/government`.

## New pages

None.

## Removals

None.

## Fetch failures

None. All 33 updated-page fetches succeeded on the first attempt (no Cloudflare-challenge markdown, all responses well above the 100-char sanity floor).
