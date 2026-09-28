# Run 2026-09-28T09-17Z — analysis

Fetch time: 2026-09-28T09:17:32Z
Baseline: 2026-09-27T09-16Z
Sub-sitemaps fetched: 42 (union: 1,985 URLs, unchanged from baseline)

## Anomalies

None. Specifically checked and ruled out:

- **Future-dated `<lastmod>`**: none of the 1,985 current URLs have a `<lastmod>` later than this run's fetch time (2026-09-28T09:17:32Z).
- **Backwards-moving `<lastmod>`**: all 35 updated URLs moved forward in time relative to their prior recorded value; none regressed.
- **Backdated new URLs**: N/A — zero URLs added this run.
- **Disappeared/reappeared URLs**: N/A — zero URLs removed this run.
- **Sub-sitemap migration**: zero URLs changed which sub-sitemap(s) they belong to.

## Updates

0 added, **35 updated** (lastmod bump only), 0 removed.

All 35 URLs with a changed `<lastmod>` were fetched fresh via `tools/html_to_md.py` and diffed against the markdown captured from the prior commit.

**28 of the 35 produced a zero-line diff** — no substantive content change, only a server-side `<lastmod>` timestamp refresh (CMS re-save / cache touch):

- /business-data/
- /business/
- /business/solutions/data/
- /business/solutions/design/
- /chatgpt-work/
- /codex/
- /hugging-face-incident-and-misalignment/
- /index/a-scorecard-for-the-ai-age/
- /index/advancing-the-price-performance-frontier-with-gpt-5-6/
- /index/astra-for-law/
- /index/better-prompt-caching-for-gpt-6/
- /index/builders-guide-to-gpt-5-6/
- /index/building-standards-next-phase-ai/
- /index/chatgpt-for-academic-researchers/
- /index/chatgpt-for-your-most-ambitious-work/
- /index/gpt-5-6-frontier-intelligence-efficiency/
- /index/gpt-5-6/
- /index/grab-openai-ai-skills-southeast-asia/
- /index/introducing-chatgpt-small-business-program/
- /index/introducing-gpt-5-3-codex/
- /index/introducing-gpt-6-sol-and-luna/
- /index/model-misalignment-reporting-framework/
- /index/navier-stokes-solution/
- /index/priorities-principles-third-party-assessments/
- /index/two-years-of-openai-academy/
- /index/v7/
- /products/release-notes/

**7 had a non-trivial diff**, all cosmetic/navigational rather than substantive edits to the article itself:

1. **Site-wide nav change — "Plugins" link added to footer.** Four otherwise-unrelated pages (`/index/devday-2026/`, `/index/managing-ai-investments-in-agentic-era/`, `/research/`, `/science/`) each gained one new footer nav item: `[Plugins](/business/plugins/)`. The `/business/plugins/` page itself already existed (unchanged `lastmod`), so this isn't a new page — it's OpenAI rolling a nav-bar link to their existing Business Plugins directory out across more of the site. Likely a phased frontend deploy (other pages will probably pick up the same link in coming days).
2. **`/research/` — card title copy edit.** A release card's title changed from "A new generation of intelligence" to "**GPT‑6 Astra:** A new generation of intelligence" (linking to `/index/gpt-6-astra/`). Minor clarity edit, no other change.
3. **`/index/codex-flexible-pricing-for-teams/`, `/index/codex-for-almost-everything/`, `/index/previewing-gpt-5-6-sol/`** — their "latest posts" recirculation carousels rotated to surface newer articles (e.g. swapping in "ChatGPT Ads expands to Southeast Asia and Taiwan", "Better prompt caching for GPT-6", "Introducing GPT-6 Sol and Luna" in place of older cards like "Reimagining advertising with AI", "How to connect AI usage to business value", "Now everyone can put data to work"). This is an automated "recent posts" widget, not an edit to the article's own content — the swapped-in articles were already known/indexed, not new pages.

None of the 7 represent a change to the substantive claims or body content of the article/page itself.

## New pages

None.

## Removals

None.
