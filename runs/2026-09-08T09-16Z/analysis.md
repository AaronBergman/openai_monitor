# Analysis — Run 2026-09-08T09-16Z

**Baseline:** 2026-09-07T09-16Z (consecutive day)
**Fetch window:** 2026-09-08T09:17:04Z (sitemap index) – 09:18:20Z (last page) UTC
**Sub-sitemaps:** 37 (unchanged from baseline)
**Total URLs:** 1,633 (unchanged from baseline — 0 added, 0 removed)
**Updated (lastmod bump):** 108
**Fetch failures:** 0 (all 108 changed/new-page fetches succeeded on first attempt)

## Anomalies

**None**, after a methodology check.

The initial automated diff pass flagged 4 URLs as having "migrated" sub-sitemaps:
`/index/how-countries-can-end-the-capability-overhang/`, `/index/understanding-ai-and-learning-outcomes/`,
`/index/equipping-workers-with-insights-about-compensation/`, `/global-affairs/new-economic-analysis/` —
apparently moving from `sitemap.xml_global-affairs.xml` to `sitemap.xml_global-affairs-news-listed.xml`.

This is a **false positive** caused by dict-based tracking that only remembers the last sub-sitemap seen per
URL. A direct `grep` for the exact `<loc>` tag on both today's fetch and yesterday's committed snapshot shows
all 4 URLs have a genuine `<url><loc>` entry in **both** sub-sitemaps simultaneously, on both days. This is a
long-standing, stable duplicate cross-listing that has been independently rediscovered and debunked in this
repo's history at least half a dozen times (2026-07-09/10, 2026-07-27, 2026-08-17/19, 2026-09-04 entries).
It is not a real migration and is not counted as an anomaly here.

No future-dated `<lastmod>` values, no backwards-moving `<lastmod>` values, no backdated new URLs (there were
no new URLs today), and no reappeared URLs.

## Notable updates

### Real content changes (small number, mostly copy/CMS edits)

- **`/products/release-notes/`** — two entries newly visible in the rolling window: **"Zendesk and OneNote plugins in ChatGPT and Codex"** (Beta, dated Sep 3, 2026 — support-ticket triage and note-summarization plugins) and **"IPv6 support for api.openai.com"** (GA, dated Sep 1, 2026). Two older Sep 1 entries ("Healthcare plugins for ChatGPT and Codex", "ChatGPT for iOS updates") scrolled off the visible window as a result — they still exist in git history from the 2026-09-05 run. Worth flagging: the Zendesk/OneNote entry is dated Sep 3 but only appeared in our snapshot today (Sep 8), a 5-day gap between OpenAI's claimed publish date and our first observation — the page's `<lastmod>` did not bump between our Sep 5 and Sep 7 runs, so this looks like a backfilled/inserted historical entry rather than a same-day miss on our part.
- **`/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/`** — small factual addition to the body text: the "sovereignty" index used by the influence operation is now named explicitly ("a 'sovereignty' index _called the Burke Sovereignty Index_"). Related-content card swapped to surface yesterday's new Ukraine-journalism piece in place of an older "New policy ideas for the Intelligence Age" card.
- **`/index/openai-academy-for-news-organizations/`** and **`/index/learning-never-stops/`** — related-content carousels swapped in cards for yesterday's [Supporting independent journalism in Ukraine](../../pages/openai.com/index/supporting-independent-journalism-in-ukraine/index.md) post, replacing older cards ("OpenAI joins PORTS-Pike project", "Bringing ChatGPT for Teachers to more U.S. school districts"). No underlying article text changed.
- **`/index/supporting-independent-journalism-in-ukraine/`** — copyediting pass on yesterday's new press-release page: Oxford commas added throughout, byline formatting standardized (e.g., "Oksana Brovko, Chief Executive Officer of AIRPPU" → "—Oksana Brovko, Chief Executive Officer, AIRPPU"). No factual or substantive change.
- **`/index/an-alien-mind/`** — byline label changed from "Author:" to "By:". Cosmetic.
- **`/business/why-openai/startups/`** — customer-story carousel finally added the **Legora** and **Playco** GPT-6 Astra case studies (both published 2026-09-03) to the top of the list, pushing the Replit/Model ML/Warp/Parloa cards down. A 5-day lag between the case studies' publish date and this carousel picking them up — the same "CMS doesn't rebuild every page atomically" pattern noted repeatedly in past runs.
- **`/business/partners/ernst-and-young/`** and **`/business/partners/quantium/`** — partner-tier badge SVG got a new CDN deployment-hash query parameter; same badge image, no visual change. Routine, seen on prior days too.
- **`/signals/`** — the "ChatGPT and the price of work" report link in the Research section was replaced by a "Load more" pagination control (the report likely still exists, just moved behind a click). Minor UI/pagination change, not a content removal.

### Sitewide accessibility pass: image alt-text rewrite

**20 pages, 92 individual `<img>` tags** had their alt-text rewritten today, replacing internal CMS/CDN
naming conventions (e.g. `Signals Homepage > Layout > Hero > Card > ChatGPT and the price of work report > Media > Asset`,
or bare filenames like `1x1 staying ahead`, `chatpgt-agents-business-overview-card`) with genuine descriptive
alt text (e.g. `White dots sit at different heights on vertical dotted lines over a blue background`, `Pink,
purple, and orange shapes blend in an abstract gradient`). This reads as an accessibility/SEO remediation
pass, likely automated (the new alt text has an "AI-generated image description" style). Affected pages:
the `/academy/*` cluster (8 pages), `/signals/` and its subpages (`enterprise-data`, `data`, `data-download`,
`research`), `/api/`, `/business/`, `/business/learn/`, `/business/workspace-agents/`, `/education/`,
`/science/`, and `/solutions/use-case/content-creation/`. No visible text content changed on any of these
pages beyond the alt attributes and the nav-link addition described below.

### Sitewide nav: "GPT-6" added to the "Latest Advancements" sidebar list

**20 pages** had a single line added to their "Latest Advancements" research sidebar/footer nav block:
`* [GPT-6](/index/gpt-6-astra/)`, inserted above the existing `GPT-5.6` entry. This is a distinct nav
element from the main header/footer model link that already switched to GPT-6 back on 2026-09-04 — this
particular sidebar list (which enumerates model-launch history) simply hadn't been updated on these
specific pages until today, another instance of the CMS's page-by-page (not atomic) rebuild behavior.
Affected pages included `/index/gpt-5-cursor/`, `/index/gpt-5-amgen/`, `/index/gpt-5-first-look/`,
`/index/gpt-5-creative-writing/`, `/index/gpt-5-coding-design/`, `/index/gpt-5-medical-research/`,
`/index/o1-coding/`, `/science/`, `/index/my-dog-the-math-tutor/`, `/solutions/blueprints/mcpkit/`,
`/codex/`, `/solutions/blueprints/knowledge-retrieval/`, `/index/introducing-gpt-oss-safeguard/`,
`/solutions/industries/{healthcare,retail,government}/`, `/solutions/use-case/{agents,data-analysis,research,coding}/`,
`/build-week/`.

Many of the 33 pages with "non-trivial" diffs (see below) also picked up this same nav line as a side effect.

### Structural DOM reordering (rendering artifact, not a content change)

`/devday/` (255 diff lines) and `/business/solutions/finance/workflows/` (139 diff lines) both show their
entire footer navigation block relocated earlier in the document relative to a card/video gallery — the
gallery content itself is byte-identical, just appearing after the footer nav in this fetch instead of
before it. Combined with alt-text upgrades on the gallery images (generic filenames → descriptive text)
and the same GPT-6 nav-line addition. Reads as a template/lazy-load ordering change (client-rendered content
insertion point moved), not an edit to any visible text.

## Routine, low-signal updates

- **55 of 108** updated pages: `<lastmod>` touch only, byte-identical content — continues the pattern from
  prior runs (CMS re-save/cache-bust with no visible effect).
- **20 of 108**: nav-only — the single-line "GPT-6" addition to the "Latest Advancements" list, nothing else.
- The remaining **33** carry a mix of the alt-text rewrite, carousel/card rotation, and DOM reordering
  described above; only 6 of those 33 (release-notes, disrupting-malicious-uses, supporting-independent-journalism-in-ukraine,
  an-alien-mind, business/why-openai/startups, signals/) have any change a reader would actually notice on
  the rendered page.

## New pages

None. 0 URLs added to the sitemap today.

## Removals

None. 0 URLs removed from the sitemap today.
