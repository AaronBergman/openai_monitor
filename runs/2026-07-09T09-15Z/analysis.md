# Analysis — Run 2026-07-09T09-15Z

**Fetch time:** 2026-07-09T09:16:52Z
**Baseline:** 2026-07-08T09-15Z
**Total URLs:** 1391 (baseline 1387)
**Added:** 5 | **Updated:** 138 (69 with visible content change) | **Removed:** 1 | **Migrated:** 4 | **Anomalies:** 0 | **Fetch failures:** 0

## Anomalies

None found this run:
- No `<lastmod>` later than fetch time (2026-07-09T09:16:52Z).
- No `<lastmod>` moved backwards vs the prior snapshot.
- No new URL whose `<lastmod>` predates its first_seen by more than a few days (all 5 added pages have lastmods from 2026-07-08/09, matching first_seen today).
- No URL disappeared-and-reappeared (the 5 added URLs are all genuinely new; the 1 removed URL — `/form/openai-for-science/` — has no history of prior removal).
- 4 URLs migrated sub-sitemaps: `sitemap.xml_global-affairs.xml` → `sitemap.xml_global-affairs-news-listed.xml` (see below) — a routine recategorization, not a red flag.

## Big story of the day: GPT-Live

OpenAI shipped **GPT-Live**, a new full-duplex voice model family now powering ChatGPT Voice:
- **[Introducing GPT-Live](../../pages/openai.com/index/introducing-gpt-live/index.md)** — the announcement post. GPT-Live-1 and GPT-Live-1 mini use a full-duplex architecture (listens and speaks simultaneously, can say "mhmm"/"yeah" while listening, doesn't rely on silence-based turn-taking). For deeper work (search, reasoning, agentic tasks) it delegates to a frontier text model (GPT-5.5 at launch) while keeping the conversation flowing. Evaluated against Advanced Voice Mode on GPQA, BrowseComp, and an internal telecom-support benchmark, with reported gains on all three. Rolling out today to ChatGPT on iOS/Android/web globally: GPT-Live-1 becomes default for Go/Plus/Pro, GPT-Live-1 mini for Free. API access "coming soon" — see the signup form below. New safety work specific to voice (audio-native evals, self-harm/psychosis/emotional-reliance testing, in-conversation safeguards, teen protections). No video/screen-share support yet.
- **[Sign-up form for GPT-Live-1 in the API](../../pages/openai.com/form/gpt-live-1-in-the-api/index.md)** — developers/enterprises can register interest ahead of API availability.
- The **homepage** (`pages/openai.com/index.md`) picked up a new hero takeover banner promoting GPT-Live.
- A GPT-Live system card was also published (externally, at `deploymentsafety.openai.com/gpt-live` — outside this repo's crawl scope, linked from the announcement).

## Other new pages

- **[Our approach to government and national security partnerships](../../pages/openai.com/index/government-national-security-partnerships/index.md)** — OpenAI published its "National Security Principles" (PDF linked, hosted at cdn.openai.com), developed with outside national-security expert David Kris. States support for democratic-society use of AI in cyber/biodefense, discloses existing "Trusted Access for Cyber" partnerships (Australia, Canada, Japan, South Korea, France, Germany, Poland, Netherlands, EU's ENISA) under the "Daybreak" program, reiterates contractual restrictions on its Dept. of War agreement (no mass domestic surveillance, no autonomous weapons direction, no high-stakes automated decisions), and calls for legislative safeguards on high-risk military AI use.
- **[Helping K–12 educators build practical AI skills](../../pages/openai.com/index/k-12-educators-practical-skills/index.md)** — OpenAI Academy + Walton Family Foundation "AI Skills Jam for K-12 Educators," 1,600+ teachers/administrators across US cities (Jonesboro GA, Fairfax VA, Orlando FL, Chicago IL, more) starting this week. Cites Walton/Gallup research claiming teachers save ~5.9 hrs/week using AI weekly.
- **[Separating signal from noise in coding evaluations](../../pages/openai.com/index/separating-signal-from-noise-coding-evaluations/index.md)** — OpenAI research publication auditing SWE-Bench Pro, a widely-used coding benchmark, and estimating **~30% of its tasks are broken**. Methodology includes human-supervised agent review and a human annotation campaign. Notable as public benchmark-quality criticism of a third-party eval suite.

## Notable updates (real content changes)

**[Release notes](../../pages/openai.com/products/release-notes/index.md)** — several new entries dated Jul 6, 2026: GPT-Realtime-2.1 and GPT-Realtime-2.1 mini (updated realtime reasoning models for voice apps, better alphanumeric recognition/noise handling/interruption behavior); GPT-5.5 Instant Mini now the ChatGPT rate-limit fallback (replacing GPT-5.3 Instant Mini); ChatGPT for PowerPoint reaches GA for Business workspaces (free through Aug 6, 2026, then flexible/token-based pricing); Workspace Agent runs move to token-based credit pricing for Business/Enterprise/Edu; ChatGPT for iOS gets Codex task management, diff controls, and attachment previews.

**[Business customer stories](../../pages/openai.com/business/customer-stories/index.md)** — two new case-study cards surfaced: "Australian Payments Plus moves faster with ChatGPT and Codex" and "MUFG aims to become AI-native with OpenAI" (both dated Jul 7, 2026 — the underlying pages were already known from prior runs, this is their first appearance in the customer-stories index listing).

**Business-section nav in flux.** Four `/business/apps/<vendor>/` integration pages flipped their top navigation today, in *both* directions — not a clean rollout:
- `hubspot` and `ramp` **gained** the business-specific nav ("Why OpenAI / Products / Solutions / Resources / Customers / Pricing" + "Try OpenAI / Contact sales" buttons), matching the ~60 other app pages that already had it.
- `fireflies` and `lseg` **lost** it, reverting to the older global site nav ("Research / Products / Business / Developers / Company / Foundation" + "Log in / Try ChatGPT").

No other content changed on these 4 pages. This looks like an unfinished/unstable template rollout (or A/B test) rather than a one-directional migration — worth watching for whether it settles.

Other `/business/*` and `/solutions/use-case/*` pages (`put-ai-to-work-for-marketing-teams`, `solutions/data`, `solutions/design`, `solutions/engineering`, `solutions/finance`, `solutions/sales`, `use-case/data-analysis`, `use-case/agents`, `use-case/research`, `use-case/content-creation`, `use-case/coding`, `industries/retail`) also picked up this same business-specific nav for the first time — consistent with the redesign-in-progress theme flagged in yesterday's run continuing to spread outward from `/business/apps/*` into the broader Solutions section.

## Sub-sitemap migration

4 URLs moved from `sitemap.xml/global-affairs/` to `sitemap.xml/global-affairs-news-listed/` (no content or lastmod change observed, purely a taxonomy/listing change on OpenAI's CMS):
- `/global-affairs/new-economic-analysis/`
- `/index/equipping-workers-with-insights-about-compensation/`
- `/index/how-countries-can-end-the-capability-overhang/`
- `/index/understanding-ai-and-learning-outcomes/`

## Routine updates (footer nav + carousel churn only)

**Sitewide footer addition:** dozens of pages across `/index/*` (mostly the legacy 2016–2018 research archive: Whisper, Jukebox, DALL-E 2, Dota 2/OpenAI Five, Gym, Roboschool, Triton, consistency models, etc.), `/research/index/*`, and a handful of others gained two new footer links under "Business" — **Customer Stories** and **Partner Network** — continuing the rollout first spotted several days ago. No other change on these pages.

**Related-articles carousel rotation only** (no other change): `/index/mapping-ai-jobs-transition-eu/`, `/index/gdpval/`, `/index/openai-for-healthcare/`, `/index/previewing-gpt-5-6-sol/`, `/index/cisco/`, `/index/boston-childrens-hospital/`, `/index/notion/`, `/news/company-announcements/`, `/news/research/`, `/research/index/`, `/research/index/publication/`, `/research/index/release/`, `/research/index/conclusion/`, `/research/index/milestone/` — all reflect the day's new posts (GPT-Live, national security principles, K-12 educators, coding evals) rotating into "keep reading" widgets. `gdpval`, `openai-for-healthcare`, and `previewing-gpt-5-6-sol` also show a "Table of contents" label appearing/disappearing — a known rendering-order artifact, not real content change.

**Pure timestamp touch, zero content change (69 pages):** the remaining ~55 `/business/apps/*` integration pages (Adobe Acrobat/Express/Photoshop, Agentforce, Aha, Airtable, Alpaca, Amplitude, Asana, Atlassian Rovo, Azure Boards, Basecamp, Biorender, Box, Canva, Clay, ClickUp, Cloudinary, Conductor, Coupler.io, Coveo, Daloopa, Dropbox, Egnyte, Figma, GitHub, GitLab Issues, Gmail, Google Calendar, Google Drive, Gusto, Help Scout, Hex, HighLevel, Hugging Face, Intercom, Jam, Klaviyo, Linear, Lovable, Mailchimp, Outlook Calendar/Email, SharePoint, Teams, Monday.com, Morningstar, Netlify, Notion, Pitchbook, Replit, Semrush, Slack, Spaceship, Stripe, Teamwork, Vercel, Zoho CRM/Desk, Zoom), plus `/business/learn/gartner-2026-agentic-coding-leader/`, got a fresh `<lastmod>` with byte-identical content — consistent with a scheduled CMS republish/cache-bust rather than genuine edits.

## Removal

**`/form/openai-for-science/`** — signup form ("Get involved with OpenAI for Science") removed from the sitemap. First seen 2026-05-07, last seen 2026-07-08. The associated `/science/` initiative content isn't otherwise in the sitemap; only this contact/signup form disappeared. Prior snapshot preserved in git history.

## Fetch failures

None. All 5 new pages and all 138 updated pages fetched cleanly (no Cloudflare challenge pages, no truncated output).
