# Run 2026-08-23T09-16Z — Analysis

**Fetch time:** 2026-08-23T09:17:36Z UTC
**Baseline:** 2026-08-22T09-17Z (consecutive day)
**Sub-sitemaps recursed:** 36 (unchanged set of sections; confirmed no new/removed sub-sitemap files)
**Total unique URLs (union across all sub-sitemaps):** 1,606

## Anomalies

None found.

Checks performed:
- **Future-dated `<lastmod>`:** none. All 35 updated `<lastmod>` values are earlier than the 2026-08-23T09:17:36Z fetch time.
- **Backwards-moving `<lastmod>`:** none. Every updated URL's new `<lastmod>` is later than its prior value, both vs. yesterday's snapshot and vs. full history in `state/known_urls.json`.
- **Backdated new URLs:** N/A — zero URLs added this run.
- **Disappeared-then-reappeared URLs:** N/A — zero URLs removed this run.
- **Sub-sitemap migrations:** A first pass flagged 128 apparent "migrations" (e.g., `company`→`global-affairs`, `product`→`release`). Investigation showed this was a false positive in the diff tooling: many OpenAI URLs are legitimately listed in **more than one** sub-sitemap simultaneously (e.g. `/index/introducing-chatgpt-agent/` appears in both `sitemap.xml_product.xml` and `sitemap.xml_release.xml`, in both yesterday's and today's snapshots). A dict-based "last file wins" mapping made stable multi-membership look like churn. Recomputing with full section-*set* comparison per URL (old set vs. new set) confirms **zero real section-set changes** this run. Noting this here in case future runs need the same care.

## Notable updates

None. All 35 lastmod-touched pages were diffed markdown-for-markdown against yesterday's committed snapshot.

- **33 of 35** pages: zero rendered-text difference — pure lastmod/metadata touch (deploy re-render, cache-bust, or backend timestamp bump with no visible content change).
- **2 of 35** pages: only their bottom-of-page "related articles" carousel rotated to surface newer posts — not an edit to the article's own text:
  - [`/index/expanding-daybreak-as-the-cyber-defense-window-narrows/`](../../pages/openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/index.md) — related-card carousel shifted forward by one slot: dropped "Responding to the next frontier of critical cyber capabilities" (Aug 7), added "Offering Zero Data Retention for frontier models" (Aug 19) and "Introducing ChatGPT for Teens" (Aug 18) alongside the existing "The Defender's Window" (Aug 17) card.
  - [`/index/model-ml/`](../../pages/openai.com/index/model-ml/index.md) — one related-story card swapped: "Gradient Labs gives every bank customer an AI account manager" (Apr 1) replaced by "Replit expands access to software creation with GPT-5.6 Luna" (Aug 19).

## Routine updates

The remaining 33 updated URLs (partner pages, news category indexes, pricing, interview guide, release-notes, student-collective, etc.) showed no diff at all between yesterday's and today's markdown snapshots. Full list in `diff.json`.

## New pages

None. 0 URLs added.

## Removals

None. 0 URLs removed.

## Fetch failures

None. All 35 updated-URL fetches via `tools/html_to_md.py` succeeded (no Cloudflare challenge pages, no sub-100-char outputs).

## Stats

- Total URLs: 1,606
- Added: 0
- Updated: 35
- Removed: 0
- Anomalies: 0
- Sub-sitemaps: 36
