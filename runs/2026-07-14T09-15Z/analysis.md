# openai.com sitemap monitoring — run 2026-07-14T09-15Z

- Fetch time (UTC, observed by this run): 2026-07-14T09:17:08Z
- Baseline run: 2026-07-13T09-16Z
- Sub-sitemaps: 34 (unchanged count)
- Total URLs this run: 1449 (baseline: 1412)
- Added: 39 | Removed: 2 | Updated (lastmod changed): 61 | Fetch failures: 0
- Anomalies: 0

## Anomalies

None detected this run:
- No `<lastmod>` later than the observed fetch time.
- No `<lastmod>` moved backwards vs the prior snapshot.
- No newly-added URL whose `<lastmod>` predates today by more than a few days (all 39 added URLs carry `<lastmod>` from 2026-07-13T20:41Z–2026-07-14T09:16Z, i.e. same-day).
- No URL reappeared after previously disappearing (checked all 39 added URLs against `state/known_urls.json`; none were previously known).
- No URL migrated between sub-sitemaps (all common URLs stayed in `sitemap.xml_page.xml` or their prior sitemap).

## Significant updates (real content changes)

Of the 61 URLs with a changed `<lastmod>`, only a minority carry an actual textual/content change — most are pure "cache revalidation" (lastmod bumped, body byte-identical apart from shared nav/footer, see "Routine updates" below). The substantive ones:

### 1. `/business/partners/` — rebuilt into the hub for a much larger OpenAI Partner Network
This page grew from a small "Become a partner / Log in" widget with ~14 partner logos into a full marketing hub: a "Find a partner" locator link, client testimonials (T-Mobile/Accenture, Agilent/BCG, Paychex/Bain, eBay/Artium, Cengage/Eliza, ACHP/Snorkel, VanEck/Altimetrik), quotes from partner-firm executives, an "Impact at a glance" stats block (80% reduction in Target's Service Center Assistant handling time, 16% increase in booking value for Norwegian Cruise Line, 23% improved conversion for Docplanner), and a much longer roster of logos. This lines up directly with the 37 new partner detail pages added this run (see below) — together they read as a single coordinated launch of an expanded/relaunched OpenAI Partner Network. A pre-existing article, `/index/introducing-openai-partner-network/`, is now linked from the page as the announcement post (that URL's own lastmod did not change this run, so it was published earlier and isn't new to this snapshot).

### 2. Codex-for-work → "ChatGPT Work" rebrand, and docs migrating off openai.com
A cluster of Academy pages (`/academy/codex-for-work/`, `/academy/getting-started/`, `/academy/how-finance-teams-use-codex/`, `/academy/working-with-codex/`, `/academy/what-is-codex/`, `/academy/codex-how-to-start/`, `/academy/codex-settings/`, `/academy/codex-plugins-and-skills/`, `/academy/codex-automations/`, `/academy/how-to-use-chatgpt-work-for-everyday-tasks/`, and the codex-for-work sub-pages) were edited to replace "Codex" / "Codex for work" branding with "ChatGPT Work" throughout. Concretely:
- `/academy/codex-for-work/`'s H1 changed from "Codex for work" to "ChatGPT Work".
- `/academy/how-finance-teams-use-codex/` now reads: _"This webinar was recorded when these workflows lived in the former Codex app. You can now follow along using ChatGPT Work at chatgpt.com or in the ChatGPT desktop app."_ — confirming the standalone Codex desktop app has been folded into the ChatGPT app as a "Work" mode.
- `/academy/getting-started/` was rewritten to explain "Chat" vs. "Work" as two modes inside ChatGPT ("Use **Chat** when you want a quick answer... Use **Work** when you want ChatGPT to complete a larger task...").
- Several of these pages now point their "Learn more" / "Explore" links off openai.com entirely, to a new external docs domain, **learn.chatgpt.com** (e.g. `/docs/get-started-with-work`, `/docs/quickstart`, `/docs/automations`, `/docs/skills-and-plugins`, `/docs/reference/settings`) — i.e. product documentation for this feature is moving off the marketing site.
- Consistent with this, the sitemap shows `/form/codex-app/` (the "Sign up for the Codex app" Linux waitlist) **removed** this run while `/form/chatgpt-app/` (a "ChatGPT app on Linux" waitlist) was **added** — the Codex app waitlist form was replaced by a ChatGPT app waitlist form.

### 3. `/index/introducing-parental-controls/` — new safety notification + Study Mode toggle
The page's changelog was extended with an update dated **July 13, 2026**: OpenAI is expanding parent safety notifications to cover additional situations where a teen may need urgent adult support, including alerting parents when a linked teen's account is banned for violent activity (explicitly scoped to exclude fictional writing, gaming, news/political discussion, general anger, or abstract questions). The update also says parents with linked teen accounts can now turn on Study Mode directly from Parental Controls (on by default for new teen chats when enabled there).

### 4. `/solutions/` — life-sciences link retargeted, new Education vertical, apps→plugins rename
- The "Life sciences" card now links to `/gpt-rosalind/` instead of `/solutions/industries/life-sciences/`. The old URL was **removed** from the sitemap this run (see Removals) — its content is superseded by the already-existing `/gpt-rosalind/` page (present in the repo since bootstrap), i.e. a consolidation/rename rather than new content.
- A new "Education" card was added, linking to `/business/solutions/education/` (already in the sitemap, unchanged lastmod — an existing page just newly surfaced from `/solutions/`).
- The apps-explore link was retargeted from `/business/apps/` to `/business/plugins/`.
- Also picked up the site-wide "Introducing ChatGPT Work" promo banner and the GPT-5.6/footer-nav changes described below.

### 5. `/build-week/` — livestream links populated as event dates approach
Each day's livestream entry went from plain text ("July 13 at 10 a.m. PDT") to a live hyperlink (X broadcast, Discord, or OpenAI Academy webinar page). One schedule time changed: **July 20** moved from **5 p.m. PDT to 11 a.m. PDT**. A submission note was also added: Devpost hackathon entries can now additionally be submitted via a "Devpost Hackathons Codex plugin."

### 6. Site-wide footer/nav refresh (touches ~30 of the 61 "updated" pages)
A large share of this run's "updated" pages (e.g. most `/policies/*`, `/index/introducing-the-adoption-news-channel/`, `/index/gartner-2026-agentic-coding-leader/`, `/index/codex-maxxing-long-running-work/`, `/news/ai-adoption/`, several Academy articles) show **no body-text change** — only the shared footer "Latest Advancements" list changed from GPT-5.5/GPT-5.4/GPT-5.3 Instant to **GPT-5.6**/GPT-5.5/GPT-5.4 (GPT-5.3 Instant dropped off), and the Business footer column gained "Customer Stories" and "Partner Network" links. This is a template-level nav update, not an edit to the article itself, and is the main reason the "updated" count (61) is much larger than the number of pages with real content changes (~6).

### 7. `/index/gpt-5-6/` — cosmetic link fix only
The only change is that an existing mention of "the multi-agent beta in the Responses API" gained a hyperlink to `https://developers.openai.com/api/docs/guides/responses-multi-agent`. No textual content changed.

### 8. `/business/` header variant continues to spread
`/business/learn/` and `/business/partners/` now render the distinct "Why OpenAI / Products / Solutions / Resources / Customers / Pricing" business-specific header (with "Try OpenAI / Contact sales" CTAs) instead of the generic site header (Research/Products/Business/Developers/Company). This is the same redesign variant flagged as a rare anomaly in the 2026-07-13 run; it appears to be a progressive rollout rather than an A/B test, since it's now present on more pages and the diff shows a clean one-way transition.

## Routine updates (lastmod bumped, no substantive change)

34 of the 61 "updated" URLs are **byte-for-byte identical in body content** apart from the shared nav/footer changes described in item 6 above, or apart from a client-side "table of contents" widget rendering fully vs. showing "Loading…" (an artifact of when-in-render the HTML was captured, not an editorial change) — for example `/policies/communications-privacy-policy/`, `/policies/civil-user-data-requests/`, `/index/the-five-ai-value-models-driving-business-reinvention/`, `/academy/*` course pages with 20–28 line diffs. These are consistent with the "cache revalidation" pattern flagged in prior runs (see 2026-07-13T09-16Z analysis).

## New pages (39 added)

**37 new OpenAI Partner Network detail pages** under `/business/partners/<slug>/`, all first-seen with same-day `<lastmod>` timestamps (mostly 2026-07-13T20:41–20:42Z, three at 2026-07-14T09:02–09:13Z): Accenture, Accenture Federal Services, AI Works, Algorithmic Intelligence, Altimetrik, Artefact, Artium, Bain & Company, Boston Consulting Group, Capco, Capgemini, CGI, Cognizant, Deepsense, Dentsu Japan, Eliza Solutions Corp, Endava, Ernst & Young, Fellow Intelligence, Fractal, HCLTech, Infosys, KPMG, McKinsey & Company, ML6, NTT DATA, Pathfindr, PwC, Recursive, Reply, SB OAI Japan GK, SIA, Slalom, Statworx, Thinking Machines Data Science, Tribe AI, Unit8. Each is a short profile page (logo, one-paragraph description of the partnership, "Countries served," "Industry," and in several cases a "Partner Summit 2026 Award" category, e.g. McKinsey's "Enterprise Reinvention Leadership Award"). Together with `/business/partners/locator/` (also new — the "Find a partner" tool) this is a large-scale build-out of OpenAI's systems-integrator/consulting partner ecosystem, coordinated with the `/business/partners/` hub rewrite described above.

- `/form/chatgpt-app/` — new "ChatGPT app on Linux" waitlist form, replacing the removed `/form/codex-app/` (see Significant updates #2).

## Removals (2)

- `/form/codex-app/` ("Sign up for the Codex app" Linux waitlist) — superseded by `/form/chatgpt-app/`, consistent with the Codex-app-into-ChatGPT-Work rebrand this run.
- `/solutions/industries/life-sciences/` — consolidated into the pre-existing `/gpt-rosalind/` page, which `/solutions/` now links to instead. Not a content loss: the last snapshot remains in git history (`git log -- pages/openai.com/solutions/industries/life-sciences/index.md`), and the successor page (`/gpt-rosalind/`) has been tracked in this repo since bootstrap.

## Fetch failures

None. All 100 fetches (39 added + 61 updated) via `tools/html_to_md.py` succeeded — no Cloudflare challenge pages, no undersized responses.

## Stats

- Total URLs in current snapshot: 1449
- Sub-sitemaps: 34
- Added: 39
- Removed: 2
- Updated (lastmod changed): 61
- Updated with real content change: 8 (partners hub, ~13 Codex→ChatGPT-Work rebrand pages, parental controls, solutions, build-week, gpt-5-6 link fix, plus the business-header rollout noted on 2 of those pages)
- Updated as pure nav/footer/TOC-render noise: ~34 (cache revalidation / shared-template bump, no editorial change)
- Anomalies: 0
- Fetch failures: 0
