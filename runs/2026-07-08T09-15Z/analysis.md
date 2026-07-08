# Run 2026-07-08T09-15Z — Analysis

**Fetch time:** 2026-07-08T09:16:23Z
**Baseline:** 2026-07-07T09-16Z
**Sub-sitemaps:** 34 (unchanged)
**Totals:** 1387 URLs (was 1386) | +1 added | 85 updated | 0 removed

## Anomalies

### 1. Pre-existing duplicate sitemap entry with conflicting `<lastmod>` (not new today, but flagged for the record)

`https://openai.com/enterprise-privacy/` appears **twice** inside the `page` sub-sitemap
(`sitemap.xml/page/`), with two different `<lastmod>` values on the two entries:

- `2026-07-06T21:19:27.711Z`
- `2025-01-31T01:52:00.485Z` (the page's original 2025 lastmod)

Checked back through the last four days of saved snapshots (2026-07-05 through today) — the
duplicate pair is present, unchanged, in every one of them. It isn't something that changed today;
it just hadn't been surfaced before because most tooling (including this run's first-pass parser)
silently keeps whichever occurrence it reads last, which can flip which lastmod "wins" depending on
parse order. This run's diff now takes the **max** (freshest-claimed) lastmod when a URL has
conflicting entries, so it doesn't register as a false "update" and known_urls.json continues
tracking `2026-07-06T21:19:27.711Z` as it has been. Flagging this here because it's a genuine
inconsistency in OpenAI's own sitemap generation — two contradictory claims about when the same
page was last modified — even though it's evidently a long-standing artifact rather than something
that happened today.

No future-dated `<lastmod>` values, no backwards-moving lastmod vs. yesterday, no
disappeared/reappeared URLs, and no sub-sitemap migrations were found this run.

## Significant updates

### Business-section top navigation redesign, mid-rollout (67 pages)

The biggest substantive change this run: 67 of the 79 individual `/business/apps/<vendor>/`
integration pages (e.g. `adobe-acrobat`, `figma`, `github`, `stripe`, `linear`, `hubspot`...) plus
`/business/learn/gartner-2026-agentic-coding-leader/` were rebuilt with a new top-level site
navigation and a reorganized footer:

- **Top nav, old:** `Research / Products / Business / Developers / Company / Foundation`, with
  `Log in` / `Try ChatGPT` as the primary calls to action.
- **Top nav, new:** `Why OpenAI / Products / Solutions / Resources / Customers / Pricing`, with
  `Try OpenAI` / `Contact sales` as the primary calls to action — a distinctly more
  enterprise/sales-oriented framing, dropping the consumer-facing "Log in / Try ChatGPT" pairing
  entirely on these pages.
- **Footer reorganization:** a new standalone "Developers" column appeared (Apps SDK, Open Models,
  Docs, Resources, Developer Forum — pulled out of what used to be folded into "API Platform" and
  "Business"); "Foundation" and "Research Residency" links were dropped from the footer; "Deployment
  Safety" was added under Safety; "News" moved from the catch-all "More" column into "Company"; and
  the "Business" footer column gained "Customer Stories" and "Partner Network" links (continuing a
  rollout first spotted two days ago).

**This redesign has not reached everywhere yet.** The `/business/apps/` hub page itself,
`/business/`, `/business/pricing/`, `/business/chatgpt-pricing/`, and 11 of the 79 app pages
(`atlassian-rovo`, `fireflies`, `gmail`, `google-calendar`, `microsoft-outlook-calendar`,
`microsoft-outlook-email`, `microsoft-teams`, `notion`, `slack`, `zoom`) all had their `<lastmod>`
bumped today but their rendered markdown came back **byte-identical** to yesterday — they're still
running the old nav/footer. A newly published page (`australian-payments-plus`, see below) also
still shows the old nav. This reads as an in-progress, partial rollout of a business-focused IA
overhaul, currently concentrated on individual app-integration pages, not yet on hub/pricing pages
or brand-new content.

### Small genuine content additions (not template noise)

- **`/security-and-privacy/`** — added a row of compliance badge images (SOC 2, ISO 27001, ISO
  27701, ISO 42001, STAR Level One Self-Assessment) just above the "Security at every step" section.
- **`/live/`** — added a "Get notified when we go live" email signup form (first name, last name,
  work email) to the livestream replay page.
- **`/index/mufg/`** — the customer-story byline date moved from "May 28, 2026" to "July 7, 2026"
  (page republished/re-dated); hero image removed from the top of the page; related-articles
  carousel rotated; footer nav gained the Customer Stories/Partner Network links.

### Rendering-order artifacts (not real content changes)

`/index/gdpval/` and `/index/sparse-transformer/` both show large diffs that are purely a
reordering of the same hero block (title, date, publication tag, hero image, "Share" button) to
appear *before* the table-of-contents list instead of after it — no text content was added or
removed. `/index/musenet/` shows "Loading…" placeholders swapped for resolved audio-sample labels
("MuseNet audio sample 1", etc.) — a client-hydration timing artifact of the static HTML fetch, not
a real edit. This matches the same "Table of Contents" template-migration pattern called out in the
2026-07-07 run, now touching a couple more `/index/` pages.

## Routine updates (18 pages)

- **Footer-only** (Customer Stories + Partner Network links added, nothing else changed):
  `/index/openai-for-healthcare/`, `/index/introducing-gpt-5-5/`, `/policies/oct-2024-row-terms/`,
  `/signals/b2b/`, `/signals/data/`, `/signals/data-download/`.
- **Related-articles carousel rotation only** (footer already had the new links from a prior run, or
  bundled with the footer change above): `/index/openai-for-healthcare/`, `/index/introducing-gpt-5-5/`.
- **Lastmod bump, zero detectable content change:** `/business/`, `/business/apps/`,
  `/business/chatgpt-pricing/`, `/business/pricing/`, `/index/mapping-ai-jobs-transition-eu/`,
  `/index/previewing-gpt-5-6-sol/`, `/signals/research/`, `/signals/research/2026q1-update/`, and
  the 11 `/business/apps/*` pages listed above that didn't get the nav redesign.

## New pages (1)

**[`/index/australian-payments-plus/`](../../pages/openai.com/index/australian-payments-plus/index.md)**
— new customer story: Australian Payments Plus (AP+), Australia's national payments infrastructure
operator, using ChatGPT Enterprise and Codex. Headline stats: 2+ hours saved weekly for 77% of
surveyed employees, 80% reporting improved creativity/work quality, working simulations built with
Codex in 1 day (down from days/weeks), and complex payments-reconciliation investigations cut from
4 hours to 30 minutes. Fits the same finance/enterprise customer-story cadence as `MUFG` (published
recently) — OpenAI continuing to build out its financial-services case-study library. Still uses the
old top nav, confirming the nav redesign hasn't reached newly published pages yet.

## Removals

None this run.
