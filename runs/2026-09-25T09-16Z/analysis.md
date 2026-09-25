# Analysis — run 2026-09-25T09-16Z

Fetch window: 2026-09-25T09:16–09:21Z. Baseline: 2026-09-24T09-16Z (1 day prior — no gap).
Sitemap index: 42 sub-sitemaps, 1,984 URLs total (down from 2,007 in the baseline).

## Anomalies

1. **Sub-sitemap migration.** `business/plugins/firecrawl/` moved from
   `sitemap.xml/plugins-engineering-it/` to `sitemap.xml/plugins-productivity/`,
   with its `<lastmod>` bumped in the same run. Simple recategorization, not a content
   concern by itself — but it landed alongside a much bigger change to the same
   section (see below).

2. **High-churn plugin delisting.** All 23 URLs removed from the sitemap today are
   `/business/plugins/<slug>/` pages. Cross-referencing `state/known_urls.json`:
   21 of the 23 were **first_seen just six days ago**, in the 2026-09-19T09-15Z run,
   and are now gone entirely — confirmed via direct fetch (`floot`, `make`,
   `whisper-transcribe-ai` all return HTTP 404). One (`alpaca`) had been listed
   since 2026-07-10. This reads as a batch of third-party plugin listings approved
   on 2026-09-19 that got pulled six days later — either a moderation reversal or a
   review-gate that let them through prematurely. Worth watching for a similar
   pattern next time a plugin batch appears.

No future-dated `<lastmod>` values and no backwards-moving `<lastmod>` values were
found in this run.

## Significant updates (real content changes, verified by markdown diff)

Of 435 URLs with a changed `<lastmod>`, only **143** had any actual rendered-content
difference; the other **292** were byte-identical to the prior snapshot (pure
`<lastmod>` bump with no visible change — most likely a cache/CDN regeneration sweep
across the plugin directory; not reported individually below).

### The ChatGPT plugin/apps directory got a template overhaul, tied to "ChatGPT Work"

Roughly 120 of the 143 real changes are near-identical, small diffs applied uniformly
across `/business/plugins/<slug>/` pages:

- "Add plugin" button copy changed to **"Install plugin"**.
- The "Common use cases" section was renamed **"What else can you do?"**, its prose
  descriptions were trimmed, and its example-prompt links now read **"Try in ChatGPT
  Work"** and point at `chatgpt.com/?surface=work&q=...` instead of a bare
  `chatgpt.com/?q=...` link.
- Headings were personalized per plugin, e.g. "Add plugins in a few clicks" → "Add
  the ZoomInfo plugin in a few clicks", and "Find a plugin" → "Find the ZoomInfo
  plugin".
- A new "Plugins" breadcrumb/nav link (`/business/plugins/`) was added to the page
  footer nav on nearly every touched page.
- Some plugin icon image assets were swapped for new file IDs (e.g.
  `codex-security`, `mailchimp`, `figma`, `airtable`, `klaviyo`, `semrush`).

This directly parallels a `products/release-notes/` entry dated 2026-09-23 ("Live now
supports plugins on web, iOS, and Android... Voice is also available in Work on web
and mobile") — i.e., the plugin surface is being wired into the new **ChatGPT Work**
product, and the marketing copy across the whole plugin directory was updated to
match on 2026-09-25.

The **"Data" plugin's URL changed** from `/business/plugins/data-analytics/` to
`/business/plugins/data/` — old links across `business/solutions/marketing/`,
`finance/`, `operations/`, and `sales/` were updated to match, and those four
solutions pages also gained newly-rendered plugin-icon images that weren't rendering
in the prior snapshot.

### DevDay 2026 keynote announced

`/live/` (saved: [pages/openai.com/live/index.md](../../pages/openai.com/live/index.md))
now leads with:

> Join us for the OpenAI DevDay 2026 keynote — Livestream will begin on Tuesday,
> September 29 at 10 AM PDT.

This is a forward-looking, time-sensitive announcement — DevDay 2026 is four days out
from this run. The page also dropped several old 2025 replay links in favor of a
"Load more" control.

### `/products/release-notes/` — two new entries, two rolled off

New (Sep 23, 2026): "Use plugins in Voice and get work done by speaking" and
"ChatGPT for iOS updates: redesigned home, iPad split view, and nested
repositories." Two older entries (ChatGPT for Word; connect multiple accounts to
plugins) scrolled out of the visible window.

### `/research/index/publication/` went from empty to populated

Previously rendered **"No results found."** — the entire publication-listing page
was empty in the prior snapshot (and the 2026-09-23 run's README flagged this same
page rendering "No results found" as a suspected one-off scrape glitch). It has now
stayed empty across at least two snapshots (2026-09-24, 2026-09-23) before today, so
this was not a transient scrape artifact — it now lists 9 publications spanning
2026-07-28 to 2026-09-23 (MentalHealthBench, the Navier–Stokes solution, GPT-6 Astra
system card, the Hugging Face incident writeup, etc.). Reads as a real front-end bug
on OpenAI's listing page that was broken for at least ~2 days and got fixed today.

### Customer-story carousel rotation

`business/customer-stories/` and `business/why-openai/startups/` swapped in new
featured stories — Harvey, Ringg, invideo, Parallel, Higgsfield AI, and a retitled V7
story ("How V7 gives AI agents institutional memory" → "V7 cuts costs 78% while
boosting accuracy with GPT‑5.6 Luna") — and dropped Fyxer, Legora, Playco, Replit,
and an ATV Big Air Tour story. Routine content-marketing rotation.

### News listing pages

`news/applied-ai/`, `news/ai-adoption/`, and `news/company-announcements/` surfaced
previously-published `index/` articles into their carousels (antimicrobial-molecule
research, quantum-computing experiments, AI-native workflow report) and added
"GPT-6" / "Plugins" nav links. These underlying articles were already in the sitemap
from prior runs — only the listing/carousel placement is new today.

## Routine updates

The remaining ~15 real-content diffs are minor nav/breadcrumb additions (new
"Plugins" links added to `about/`, `academy/workspace-agents/`, `index/*` pages) or
single-line copy fixes, not independently notable.

## New pages

None — 0 URLs added to the sitemap this run.

## Removals

23 pages removed, all `/business/plugins/<slug>/` — see Anomaly #2 above for the
full list and churn analysis. Prior snapshots remain in git history
(`git log -- pages/openai.com/business/plugins/<slug>/index.md`).

## Fetch failures

None. All 42 sub-sitemaps and all 435 updated pages fetched successfully on the
first or second attempt.
