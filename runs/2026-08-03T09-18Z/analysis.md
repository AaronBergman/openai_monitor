# Run 2026-08-03T09-18Z — Analysis

**Fetch time:** 2026-08-03T09:24:14Z
**Baseline:** 2026-08-02T09-16Z (consecutive day)
**Sitemap totals:** 1547 URLs across 35 sub-sitemaps (unchanged from baseline: +0 / -0)
**Updated (lastmod changed):** 71
**Anomalies:** 0

## Methodology note (correction made mid-run)

The first pass at diffing sub-sitemap membership flagged 123 URLs as having "migrated"
from one sub-sitemap section to another (e.g. `gpt-5-6` moving from `product` to
`release`). On investigation this was a **tooling artifact, not a real site change**:
215 URLs in this sitemap are legitimately cross-listed in more than one sub-sitemap
simultaneously (e.g. `/index/gpt-5-6/` appears in *both* `sitemap.xml/product/` and
`sitemap.xml/release/` in both today's and yesterday's snapshots). The first-pass script
kept only a single sub-sitemap name per URL (last-one-wins), and the iteration order
differed between how the baseline was parsed (alphabetical glob) and how the fresh fetch
was parsed (root-index order) — producing 123 phantom "migrations" that were really just
order-of-processing noise. Rebuilding the comparison with full multi-membership sets
(url → *set* of sub-sitemaps) per snapshot shows **zero actual sub-sitemap membership
changes** between 2026-08-02 and 2026-08-03. Recorded here so this class of false
positive is easier to recognize in future runs.

## Anomalies

None. No future-dated or backward-moving `<lastmod>` values among the 71 updated URLs.
No added/removed URLs this run, so no reappearance or backdating checks apply. No real
sub-sitemap migrations (see correction above).

## Significant updates

- **[Ten advances in mathematics and theoretical computer science](../../pages/openai.com/index/ten-advances-in-mathematics/index.md)**
  (`/index/ten-advances-in-mathematics/`, published 2026-08-01) — OpenAI softened a claim
  in the lead paragraph two days after publication. Was: *"...ten results to problems
  that have been open and have seen no progress on the main result for at least a
  decade, and in most cases much longer."* Now: *"...ten results, each of which resolves
  or makes substantial progress on a long-standing open problem."* The original wording
  implied all ten problems were fully closed with zero progress in ≥10 years; the revised
  wording explicitly allows for partial progress rather than full resolution — a
  meaningfully weaker claim. Reads as a post-publication correction, plausibly prompted
  by outside scrutiny of the original framing (this is a domain — AI-assisted claims
  about solving open math problems — that has drawn public fact-checking before).

## Routine updates (no real content change)

- **55 `/business/partners/*` pages** (Accenture, Bain, BCG, KPMG, McKinsey, PwC, and
  the rest of the consulting-partner roster) had their partner-tier badge image URL's
  cache-busting query parameter change (`?dpl=...` hash) with **no other diff** —
  consistent with a platform redeploy, not an edit.
- **4 partner pages** (`altimetrik/`, `blend360/`, `ml6/`, `zs/`) additionally rendered a
  different top-nav/header variant on this fetch — "Why OpenAI / Products / Solutions /
  Resources / Customers / Pricing" with a "Try OpenAI / Contact sales" CTA, versus the
  standard "Research / Products / Business / Developers / Company" with "Try
  ChatGPT / Log in" seen on the other 56 partner pages fetched in the same run. This same
  phenomenon (a subset of partner pages returning a different nav variant between
  fetches) was already observed and logged as likely server-side A/B testing in the
  2026-08-01 run — not treated as a new finding, just a recurring artifact of how these
  pages are served. Not counted as a content anomaly.
- **[`index/ntt-data/`](../../pages/openai.com/index/ntt-data/index.md)** — only the
  "Keep reading" related-articles sidebar rotated to surface newer posts (Ten advances in
  mathematics, Advancing responsible AI across Europe, Building abundant intelligence);
  the case-study article itself is unchanged.
- **11 pages** had their `<lastmod>` bumped with **zero detectable markdown-content
  difference** (likely metadata-only republish / CMS "touch", not visible in rendered
  text): `api-reserved-tier/`, `api-scale-tier/`,
  `index/advancing-the-price-performance-frontier-with-gpt-5-6/`, `index/avatarin/`,
  `index/how-news-organizations-are-using-ai/`, `index/introducing-gpt-live/`,
  `index/unive/`, `policies/ad-tools-subprocessors/`, `policies/ad-tools-terms/`,
  `research/verify/`, `student-collective/`.

## New pages

None. 0 URLs added to the sitemap this run.

## Removals

None. 0 URLs removed from the sitemap this run.

## Fetch failures

None. All 71 updated-page fetches succeeded via `tools/html_to_md.py` (curl-cffi, Chrome
impersonation); no Cloudflare challenge pages encountered.
