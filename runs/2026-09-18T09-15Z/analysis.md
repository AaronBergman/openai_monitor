# openai.com sitemap monitor — analysis for run 2026-09-18T09-15Z

Fetch time (this run): 2026-09-18T09:15Z–09:25Z (UTC). Baseline: prior run `2026-09-17T09-15Z`.

Sitemap index: **40 sub-sitemaps (up from 39)** — a new section, `learn-webinars`, appeared. Total unique URLs across all sections: **1,748** (up from 1,733).

Diff stats: **16 added, 308 lastmod-updated (174 with a visible content diff after filtering out pure CDN-deploy-hash noise, 12 deploy-hash-only, 122 lastmod-only/no visible change), 1 removed, 2 anomalies (1 new sub-sitemap section + 1 section migration), 0 timestamp anomalies, 0 fetch failures** (324/324 added+updated page fetches succeeded via curl-cffi Chrome impersonation).

The day's story is a single coherent launch: **Astra for Law**, a new legal-industry product built on GPT‑6 Astra, along with a matching plugin-directory redesign and a new business-content push (ChatGPT Work guides for finance and marketing teams).

## Anomalies

No future-dated or backwards-moving `<lastmod>` values were found anywhere in the 1,748-URL set. No new URL's `<lastmod>` predates its first-seen date by more than a few days, and none of the 16 new URLs previously existed in `state/known_urls.json` (i.e., none are reappearances).

### New sub-sitemap section: `learn-webinars`

The sitemap index gained a 40th sub-sitemap, `https://openai.com/sitemap.xml/learn-webinars/`. It currently holds exactly one URL: `/business/learn/how-our-marketing-team-uses-chatgpt-work/`, a gated webinar registration page. This looks like a newly-introduced content type (distinct from the existing `learn-guides` and `webinar` sections) rather than a migration of existing content.

### 1 section migration: `box` plugin

`https://openai.com/business/plugins/box/` moved from `plugins-productivity` to `plugins-operations` (it remains cross-listed under `plugins-legal`, as it was yesterday). Minor reshuffle within the plugin taxonomy, likely incidental to the broader plugin-directory work described below.

## Significant updates

### New: "Astra for Law" — OpenAI's first named legal-industry product

Four new pages together announce a dedicated legal vertical built on GPT‑6 Astra:

- **[/index/astra-for-law/](../../pages/openai.com/index/astra-for-law/index.md)** — the announcement. Astra for Law combines GPT‑6 Astra with a legal search index (U.S. case law, statutes, regulations, court rules, and administrative decisions across 230M+ URLs, including Free Law Project/CourtListener's case-law collection covering 99.9%+ of published U.S. precedential case law) plus firm-specific privacy/governance controls. API customers **Harvey** and **Legora** are named as early builders on the platform. The page also references "26 new ecosystem plugins" connecting ChatGPT to legal-specialist tools like Relativity and Clio.
- **[/solutions/industries/law/](../../pages/openai.com/solutions/industries/law/index.md)** — a new industry solutions page. Notes Astra for Law is "initially available to selected law firms through Trusted Access in ChatGPT and Codex," and highlights zero-data-retention for API usage and "eyes-off" human review as legal-specific trust controls.
- **[/business/contact-sales-legal/](../../pages/openai.com/business/contact-sales-legal/index.md)** — a new dedicated sales-contact form for the legal vertical.
- **[/index/cooley-gopublic/](../../pages/openai.com/index/cooley-gopublic/index.md)** — a customer case study: international law firm Cooley (180 deals, $51.5B+ deal volume in 2025, a leading US issuer-side IPO practice) built "GO Public," a proprietary AI product on ChatGPT Work to synthesize IPO-related legal work.

### New: 8 legal-plugin integration pages, `plugins-legal` section grows from 10 to 20

New plugin pages added today: **Clio, DeepJudge, Harvey, iManage Work, Legora, NetDocuments, Relativity, and Thomson Reuters HighQ**. Combined with yesterday's initial 10 and today's `box` migration, the `plugins-legal` sub-sitemap now lists 20 URLs total. Several of the new plugins are cross-listed in a second category too (e.g. Clio/DeepJudge/iManage/Legora/Relativity/Thomson-Reuters-HighQ also appear under `plugins-productivity`; Harvey and NetDocuments also appear under `plugins-operations`), confirming plugins can belong to more than one directory category simultaneously.

### Plugin-directory template redesign (110 pages)

110 of the 308 lastmod-updated pages are existing `/business/plugins/*` pages that received the same template change, not distinct content edits:
1. Example-prompt cards gained a small provider icon.
2. The "open in ChatGPT" links for example prompts now prefix the plugin name with `@` (e.g. `?q=Airtable+...` → `?q=%40Airtable+...`), matching ChatGPT's @-mention plugin-invocation syntax.
3. A new **"Add plugins in a few clicks"** section was added, linking to a setup guide.
4. A new **"Explore related plugins"** carousel was added.
5. On many pages, a matching **"Find a plugin / Install and connect / Put it to work"** three-step onboarding walkthrough (with screenshots) was appended near the bottom of the page.

This reads as a directory-wide UX refresh timed to accompany the legal-plugin expansion, rather than content specific to any single plugin.

### New: ChatGPT Work content push for finance and marketing teams

Four new gated pages (all form-walled, so page bodies are mostly registration forms with no visible article text):
- `/business/learn/download-the-chatgpt-work-guide-for-finance-teams/` and `/business/learn/download-the-chatgpt-work-guide-for-marketing-teams/` — downloadable guides.
- `/business/learn/how-our-finance-team-uses-chatgpt-work/` and `/business/learn/how-our-marketing-team-uses-chatgpt-work/` — internal case-study webinars (the latter is the sole member of the new `learn-webinars` section).

### Sitewide navigation change: "GPT-6" added to the global "Latest Advancements" menu

Across many `/index/*` article pages, the persistent "Latest Advancements" sidebar/footer navigation block changed from listing `GPT-5.6 / GPT-5.5 / GPT-5.4` to leading with `GPT-6 / GPT-5.6 / GPT-5.5 / GPT-5.4`, linking to `/index/gpt-6-astra/`. Notably, GPT-6 Astra itself was first published on 2026-09-04 (two weeks ago) — this navigation update appears to have been held back until today, coinciding with the Astra for Law launch that showcases it.

## Routine updates

The remaining ~64 non-plugin pages with a visible diff are almost entirely the site's standard "recent posts" carousel refreshing to surface stories already reported in the prior two runs — **"Our framework for reporting model misalignment,"** **"Helping older adults use AI in everyday life,"** and **"How workers are unlocking new ways of working"** (all first seen 2026-09-17) — displacing older cards. No new information in these; they're noted here only because they triggered lastmod bumps.

Two small genuine copy edits were also found:
- `/index/estimating-worst-case-frontier-risks-of-open-weight-llms/`: heading corrected from "Author" to "Authors" (typo fix).
- `/index/advancing-youth-safety-in-emea/`: a partner-logo strip and a pull-quote (Natascha Gerlach, CIPL) were reordered lower on the page — cosmetic layout change, no wording changed.

12 pages showed a diff that was **purely a CDN deploy-hash change** in an image `src` query string (`?dpl=dpl_XXXX`) with no other difference — these are redeploy artifacts, not content changes, and are excluded from the "real diff" counts above.

## New pages (full list, 16)

| URL | lastmod | Section(s) |
|---|---|---|
| `/business/contact-sales-legal/` | 2026-09-18T08:54:46Z | page |
| `/business/learn/download-the-chatgpt-work-guide-for-finance-teams/` | 2026-09-17T22:27:30Z | learn-guides |
| `/business/learn/download-the-chatgpt-work-guide-for-marketing-teams/` | 2026-09-17T22:20:34Z | learn-guides |
| `/business/learn/how-our-finance-team-uses-chatgpt-work/` | 2026-09-17T22:29:06Z | learn-guides |
| `/business/learn/how-our-marketing-team-uses-chatgpt-work/` | 2026-09-17T22:24:21Z | learn-webinars (new section) |
| `/business/plugins/clio/` | 2026-09-17T21:58:43Z | plugins-legal, plugins-productivity |
| `/business/plugins/deepjudge/` | 2026-09-17T22:02:18Z | plugins-legal, plugins-productivity |
| `/business/plugins/harvey/` | 2026-09-17T21:57:52Z | plugins-legal, plugins-operations |
| `/business/plugins/imanage-work/` | 2026-09-17T21:57:05Z | plugins-legal, plugins-productivity |
| `/business/plugins/legora/` | 2026-09-17T21:57:00Z | plugins-legal, plugins-productivity |
| `/business/plugins/netdocuments/` | 2026-09-17T21:57:04Z | plugins-legal, plugins-operations |
| `/business/plugins/relativity/` | 2026-09-17T22:14:01Z | plugins-legal, plugins-productivity |
| `/business/plugins/thomson-reuters-highq/` | 2026-09-17T22:01:54Z | plugins-legal, plugins-productivity |
| `/index/astra-for-law/` | 2026-09-18T08:40:29Z | company |
| `/index/cooley-gopublic/` | 2026-09-17T23:05:50Z | page |
| `/solutions/industries/law/` | 2026-09-18T04:58:38Z | page |

## Removals

`https://openai.com/academy/custom-gpts/` was removed from the sitemap and independently confirmed to now return HTTP 404 on the live site (verified with a direct curl-cffi fetch) — a genuine page removal, not just a sitemap-listing change. It had been tracked since first_seen `2026-05-07`. The last-known content remains in git history (`git log -- pages/openai.com/academy/custom-gpts/index.md`).

## Fetch failures

None. All 324 added/updated page fetches succeeded (324/324).
