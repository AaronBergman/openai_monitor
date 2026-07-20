# Run 2026-07-20T09-16Z — Analysis

**Fetch time:** 2026-07-20T09:18:53Z (sitemap index + all 34 sub-sitemaps)
**Baseline:** 2026-07-19T09-17Z (consecutive day)
**Total URLs:** 1459 (unchanged)

## Anomalies

None detected.

- No `<lastmod>` later than fetch time.
- No `<lastmod>` moved backwards vs. the prior snapshot for any URL (checked all 8 updated URLs against `state/known_urls.json` lastmod_history).
- No URL disappeared and reappeared.
- No URL migrated between sub-sitemaps.
- All 8 updated URLs' new `<lastmod>` values are within the last ~30 hours and consistent with their multi-day history of near-daily bumps (release-notes, gpt-5-6, cars24, public-policy, etc. have all bumped on nearly every run since first_seen) — nothing backdated.

## Significant updates

None. Of the 8 pages whose `<lastmod>` changed, 7 are byte-identical to yesterday's saved markdown. The 8th (`/research/`) has exactly one line of difference, and it's cosmetic:

- **[`/research/`](../../pages/openai.com/research/index.md)** — the hero image's `alt` text and CDN URL changed:
  - old: `![[2.0] Research > Hero > Media Item](https://downloads.ctfassets.net/kftzwdyauwt9/.../Research_Hero.png?...)`
  - new: `![Illustration representing OpenAI research overview](https://cdn.openai.com/ctf-cdn/research/research-hero-2400.webp?...)`
  This looks like an asset-pipeline migration (Contentful CDN → OpenAI's own `cdn.openai.com/ctf-cdn/` mirror) plus an alt-text cleanup (the old alt text was a raw CMS field-path placeholder, `[2.0] Research > Hero > Media Item`, now replaced with real descriptive alt text). No change to page copy, structure, or claims.

## Routine updates

7 pages had their sitemap `<lastmod>` bumped with zero content change (fully byte-identical to the 2026-07-19 snapshot):

- `/devday/terms-and-conditions/`
- `/index/why-teens-deserve-access-safe-ai/`
- `/products/release-notes/`
- `/index/gpt-5-6/`
- `/index/cars24/`
- `/index/unlocking-self-improvement-gpt-red/`
- `/company/public-policy/`

All 7 of these have bumped their `<lastmod>` on nearly every run for the past several days per `state/known_urls.json` — consistent with a backend process that re-touches timestamps on a recurring set of pages (index/story pages, release notes, policy hub) without necessarily editing content each time.

## New pages

None this run. 0 URLs added, 0 removed.

## Removals

None this run.

## Fetch failures

None. All 8 updated pages fetched cleanly via `tools/html_to_md.py` (curl-cffi, Chrome impersonation) — no Cloudflare challenge pages encountered, all outputs well above the 100-char sanity threshold.
