# Run 2026-08-02T09-16Z — Analysis

Fetch window: ~2026-08-02T09:16Z–09:22Z UTC.
Baseline: 2026-08-01T09-16Z (prior run).

## Summary

Quiet day. 1 genuinely new page, 73 lastmod-only sitemap entries touched, 0 removals, 0 sub-sitemap migrations, 0 timestamp anomalies. The bulk of the "updated" count is noise from two distinct non-editorial causes explained below, not fresh writing.

## Anomalies

None detected this run:
- No `<lastmod>` later than fetch time.
- No `<lastmod>` moving backwards vs. the prior snapshot.
- The 1 new URL's `<lastmod>` (2026-08-02T06:42:50.078Z) is same-day, not backdated.
- No URL disappeared-and-reappeared.
- No URL moved from one sub-sitemap section to another.

## Notable additions

- **[How OpenAI's Finance team uses AI](../../pages/openai.com/business/solutions/finance/workflows/index.md)** (`/business/solutions/finance/workflows/`) — a new Business/Solutions marketing page showcasing 16 real internal finance workflows (planning, forecasting, monthly close, treasury, investor relations) built by OpenAI's own Finance team with ChatGPT Work and Codex. Each workflow links out to a LinkedIn post from the finance professional who built it. Promotes a "finance webinar" (hosted on a separate `webinar.openai.com` subdomain, not covered by this sitemap) and fits the ongoing "ChatGPT Work" enterprise-productivity push seen in recent runs.

## Notable updates (substantive content change)

- **Homepage (`/`)** — swapped a featured story tile: added a link to the new *"Ten advances in mathematics and theoretical computer science"* publication (published Aug 1), removed the tile for *"How we monitor internal coding agents for misalignment"* (a March safety post). Routine homepage rotation, not a content rewrite.
- **[Ten advances in mathematics and theoretical computer science](../../pages/openai.com/index/ten-advances-in-mathematics/index.md)** — trivial copyedit: two list items ("Connes's rigidity conjecture", "Ehrhart's volume conjecture") gained a missing trailing period. No substantive change.

## Routine / non-substantive updates (69 URLs — lastmod bumped, no visible content change)

Two distinct mechanical causes were identified, verified by diffing rendered markdown and by diffing raw sitemap `<url>` blocks:

1. **Site-wide partner-directory redeploy (62 pages).** Every page under `/business/partners/*` (Accenture, Bain, BCG, Cognizant, Deloitte-adjacent consultancies, McKinsey, PwC, etc. — the full partner roster) got its `<lastmod>` bumped between 2026-08-01T19:46Z and 19:48Z. Diffing rendered markdown shows the *only* change is the Contentful deployment-ID query string on the "Elite Partner" badge image (`?dpl=dpl_2nDw...` → `?dpl=dpl_4ZpC...`), i.e. an asset cache-buster from a platform redeploy — no textual or structural change to any partner page.
2. **Silent CMS touches (7 pages: `api-fast-mode`, `api-reserved-tier`, `api-scale-tier`, `introducing-gpt-live`, `unive`, `ad-tools-subprocessors`, `ad-tools-terms`, `verify`, `student-collective`).** `<lastmod>` moved forward with **zero** detectable difference in rendered markdown and zero change to `<xhtml:link>` hreflang alternates. These read as CMS "touch" republishes (e.g. an editor opening and re-saving without changes) rather than content edits.
3. **Localization expansion (2 pages).** `/index/avatarin/` gained 12 new `hreflang` alternate-language links (ca-ES, es-ES, fa-IR, fil-PH, gu-IN, hy-AM, kk-Cyrl, mr-IN, my-MM, pa-IN, ta-IN, ur-IN) — the page is now localized into a dozen more languages. `/index/advancing-responsible-ai-across-europe/` gained one new alternate, `my-MM` (Burmese). English content unchanged in both cases. This also explains the unusually large raw XML diff on `sitemap.xml_page.xml` (~3,100 lines): adding hreflang blocks shifts the alphabetical ordering of surrounding `<xhtml:link>` entries throughout the file, producing a big line-diff for what is actually a small, targeted change.

Full list of the 69 non-substantive URLs is in `runs/2026-08-02T09-16Z/diff.json` under `updated`.

## Removals

None.

## Fetch failures

None — all 15 fetched pages (14 updated + 1 new) returned usable markdown on the first attempt.

## Sub-sitemap coverage

All 35 sub-sitemap sections fetched successfully (34 category sections + `page`, the largest catch-all). No sections added or removed vs. the prior run.
