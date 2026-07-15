# Analysis — Run 2026-07-15T09-16Z

**Fetch time (this run):** 2026-07-15T09:17:58Z (sitemaps); page fetches completed by ~09:21Z
**Baseline:** 2026-07-14T09-15Z
**Sub-sitemaps:** 34/34 fetched successfully, no errors
**Totals:** 1443 URLs (was 1449) | +2 added | 170 updated (122 with a real markdown diff, 48 lastmod-only) | -8 removed | 0 anomalies | 0 fetch failures (1 transient network error on `index/uber-enables-outstanding-experiences/`, succeeded on retry)

## Anomalies

None detected by automated checks: no future-dated `<lastmod>`, no backwards-moving `<lastmod>` vs the last known value, no new URL backdated relative to its first_seen, no URL reappearance, no sub-sitemap migrations.

One soft observation, not a true anomaly: two items that "disappeared" from visible homepage/index carousels (the "Core dump epidemiology" engineering post from `/news/`, and "Boston Children's uses AI to unlock new diagnoses" from `/business/customer-stories/`) are **not** URL removals — both pages are still live and unchanged in the sitemap (`index/core-dump-epidemiology-data-infrastructure-bug/` lastmod 2026-07-06, `index/boston-childrens-hospital/` lastmod 2026-07-09). They simply fell off the first page of a paginated/curated feed as newer stories were promoted above them.

## Significant updates

### OpenAI Partner Network gets tier badges (completes yesterday's launch)
Yesterday's run (2026-07-14) reported 37 new `/business/partners/<slug>/` profile pages going live. Today, 36 of those pages gained a **partner tier badge** image (`/images/partner-tier-badges/OAI_PartnerNetwork_<Tier>.svg`):

- **Elite Partner** (7): Accenture, Accenture Federal Services, Bain & Company, Boston Consulting Group, Capgemini, KPMG, McKinsey & Company
- **Advanced Partner** (29): all the rest — AI Works, Algorithmic Intelligence, Altimetrik, Artefact, Artium, Capco, CGI, Cognizant, Deepsense, Dentsu Japan, Eliza, Endava, Ernst & Young, Fellow Intelligence, Fractal, HCLTech, Infosys, ML6, NTT DATA, Pathfindr, PwC, Recursive, Reply, SB OAI Japan GK, SIA, Slalom, Statworx, Thinking Machines Data Science, Tribe AI, Unit8

This looks like a formal two-tier certification program layered onto the partner directory the day after its launch.

### Partner rename: "Eliza Solutions Corp" → "Eliza"
`/business/partners/eliza-solutions-corp/` was removed and replaced by `/business/partners/eliza/` — same firm (AI-native services firm building production systems on OpenAI), same logo asset, now displaying the "Advanced Partner" badge. The `/business/partners/` directory page's link text and logo alt-text were updated to match ("Eliza Solutions Corp" → "Eliza"). Treated as a rename, not a genuine removal+addition.

### New guide: "How to manage AI investments in the agentic era"
New page `/index/managing-ai-investments-in-agentic-era/`, published July 14, 2026, filed under AI Adoption. Five practical steps for enterprise leaders: (1) sharpen visibility into usage/spend via updated Admin Console analytics, (2) evaluate model efficiency by outcome ROI rather than token price, (3) govern advanced agentic workflows before they scale (citing `ChatGPT Work`, Deployment Engineers, Zero Data Retention), (4) fund workflows that can compound, (5) match capacity to proven demand. Cites GPT‑5.6 gains: 54% fewer output tokens and 57% less time per task on the Artificial Analysis Coding Agent Index vs. its predecessor, and a 97% token-price drop from GPT‑4 to GPT‑5.4. Immediately cross-promoted on `/business/learn/` and featured atop `/news/` and `/news/ai-adoption/`.

### Academy's Codex how-to section consolidated (7 pages removed)
Seven granular Codex how-to pages were pulled from the Academy: `academy/codex-automations/`, `academy/codex-how-to-start/`, `academy/codex-plugins-and-skills/`, `academy/codex-settings/`, `academy/prompting/`, `academy/what-is-codex/`, `academy/working-with-codex/`. None of these slugs have a direct replacement; the content is superseded by the existing `academy/codex/` overview and the role-specific `academy/codex-for-work/how-<team>-teams-use-codex/` pages, which were themselves updated today (see below). Reads as a simplification of the Codex learning section from many narrow docs to fewer, broader ones — continuing the "docs moving toward `learn.chatgpt.com`" pattern flagged in the 2026-07-14 entry.

### "Codex" → "ChatGPT Work" rebrand continues in Academy
Building on yesterday's ~13-page rebrand, four more Academy pages swapped "Codex"/"ChatGPT Codex" language for "ChatGPT Work" today, with publish dates bumped from May 15, 2026 to July 14, 2026:
- `academy/` — the "Codex for work" category card is now labeled "ChatGPT Work"
- `academy/codex-for-work/how-data-science-teams-use-codex/` — "Top ChatGPT Codex use cases..." → "Top ChatGPT Work use cases...", "Download ChatGPT Codex" → "Download ChatGPT Work"
- `academy/codex-for-work/how-business-operations-teams-use-codex/` — same pattern
- `academy/codex-for-work/how-sales-teams-use-codex/` — same pattern, plus body rewrites ("Codex helps pull that context together..." → "ChatGPT Work helps pull that context together...", "Already have Codex installed?" → "Already have ChatGPT Work installed?")

### Business-site nav A/B test spreads to guide/report pages and solutions pages
The "Why OpenAI / Products / Solutions / Resources / Customers / Pricing" nav + "Introducing ChatGPT Work" promo banner (first spotted 2026-07-11, converging by 2026-07-14) is now live on:
- `/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/` (+ its `/index/` mirror)
- `/business/guides-and-resources/chatgpt-usage-and-adoption-patterns-at-work/`
- `/business/guides-and-resources/chatgpt-business-smb-guide/`
- `/business/guides-and-resources/staying-ahead-in-the-age-of-ai/`
- `/business/guides-and-resources/how-enterprises-are-scaling-ai/`
- `/business/customer-stories/`
- `/solutions/industries/retail/`, `/solutions/use-case/coding/`, `/solutions/use-case/research/` (banner only, no nav diff captured — likely already on the new nav)

On the solutions pages, the "Explore app integrations" link target also changed from `/business/apps/` to `/business/plugins/`.

### Two guide pages lost interactive "Try this prompt" widgets
Beyond the nav refresh, `chatgpt-business-smb-guide` and `chatgpt-usage-and-adoption-patterns-at-work` also lost content that the other guide pages kept: every inline "[Prompt] Try this ->chatgpt.com/?prompt=..." CTA button was stripped (about 10 on the SMB guide alone), and the usage-and-adoption report additionally lost several stat/ranking call-out boxes — "AI use is becoming habitual", "Usage correlates with education", the ranked "Top tasks for ChatGPT technical/go-to-market users" lists by department, and "Top 3 tools used within ChatGPT by job category" by role. The surrounding headings and prose stayed; only the interactive widgets and stat boxes vanished. This reads as a genuine content simplification tied to the redesign rather than a fetch artifact, since it recurred identically across two independent pages and the un-touched guide pages (staying-ahead, how-enterprises-are-scaling) show no such loss.

### Financial services Academy page drops its "Pre-built GPTs" section
`academy/financial-services/` had its entire "Pre-built GPTs" section removed — the intro paragraph and a 3-row table linking to three custom GPTs (KYC / AML Risk Screener GPT, Policy Interpreter GPT, Investment Research Assistant GPT). The "Pre-built GPTs" nav entry was also dropped from the page's table of contents.

### A number quietly disappeared from the GPT‑5.6 safety writeup
On `/index/gpt-5-6/`, the safety-testing paragraph changed from:
> "...approximately **700,000 A100e GPU hours** of black-box automated red teaming."
to:
> "...approximately **NVIDIA A100 Tensor Core GPU-equivalent hours** of black-box automated red teaming."

The specific figure (700,000) was removed and replaced with a vaguer unit description that no longer states a quantity. Everything else in the sentence is unchanged. Flagged here because it's a quiet edit to a quantitative safety claim on a model-launch page — worth watching for a follow-up correction or clarification.

### Codex adoption statistic revised on "How agents are transforming work"
`/index/how-agents-are-transforming-work/` changed:
> "Nearly a quarter of all Codex requests are for tasks that would take a person more than one hour to complete"
to:
> "In May 2026, more than 70% of users asked Codex to complete a task that would take a person more than one hour to complete"

Note the metric itself changed shape (share of *requests* → share of *users*, ~25% → 70%+), not just the number — these aren't directly comparable stats, so this reads as a replacement/correction rather than simple growth.

### Sora branding continues folding into ChatGPT
`/solutions/use-case/content-creation/` changed "Transform a storyboard or mood board into expressive, cinematic sequences before production starts with **Sora 2**" to "...with **ChatGPT**". Separately, `/stories/` dropped its "Sora" category-filter tab (now just All / ChatGPT / API) and its header CTA flipped back from "Try now / Contact sales" to "Log in / Try ChatGPT" — the opposite direction from the nav test spreading elsewhere, suggesting `/stories/` sits on a different template/experiment track.

### business/customer-stories and business/learn carousels refreshed
`/business/customer-stories/` added a new "How Deutsche Telekom is rewiring telecommunications with AI" (Jul 10, 2026) card (page itself unchanged, just newly promoted) and dropped "Boston Children's uses AI to unlock new diagnoses" off the visible list (pagination, see Anomalies note). `/business/learn/` added three new Guides cards, all pointing at pages covered above: "How to manage AI investments in the agentic era," "How agents are transforming work" ("a new Economic Research paper measuring Codex's economic potential at the frontier"), and "AI value models driving business reinvention."

## Routine updates (site-wide template refresh)

The large majority of the 170 lastmod-bumped pages carried only a mechanical footer/template refresh, with no unique body content change:
- The "Latest Advancements" footer list swapped `GPT-5.3 Instant` for `GPT-5.6` (now reads GPT-5.6 / GPT-5.5 / GPT-5.4) — sitewide.
- The Business footer column gained two new links: "Customer Stories" and "Partner Network" — sitewide.
- Many pages briefly show a duplicated/relabeled table-of-contents block ("Table of contents" label appearing/disappearing) — a client-side hydration timing artifact consistent with prior runs' notes, not a content edit.
- A "GPT 5-6 > Card" promotional tile was added to several "related content" carousels (`chatgpt-for-your-most-ambitious-work`, `codex-flexible-pricing-for-teams`, `codex-for-almost-everything`, `codex-for-every-role-tool-workflow`, `gpt-5-6-preferred-model-microsoft-365-copilot`, `introducing-gpt-live`, `introducing-the-codex-app`, `news/product-releases/`) — same GPT-5.6 promotion, not unique news.
- Many partner/card link labels gained a " | OpenAI" or " | OpenAI Academy" suffix in their link text (SEO/title-tag formatting) — cosmetic.
- 48 of the 170 updated URLs had a bumped `<lastmod>` but byte-identical markdown — pure rebuild noise.
- 7 pages (`index/digital-green/`, `index/harvey/`, `index/rakuten-2024/`, `index/upwork/`, `index/whoop/`, `stories/api/`, `stories/sora/`) had only the footer/TOC noise described above with no other change.
- `index/gpt-5-1-for-developers/` (a Nov 2025 page) only had its "related articles" carousel refreshed to current July 2026 stories — no body text change.

## New pages

- **[`/business/partners/eliza/`](../../pages/openai.com/business/partners/eliza/index.md)** — see rename note above.
- **[`/index/managing-ai-investments-in-agentic-era/`](../../pages/openai.com/index/managing-ai-investments-in-agentic-era/index.md)** — see new guide note above.

## Removals

- `academy/codex-automations/`, `academy/codex-how-to-start/`, `academy/codex-plugins-and-skills/`, `academy/codex-settings/`, `academy/prompting/`, `academy/what-is-codex/`, `academy/working-with-codex/` — consolidated, see Academy section above. Last snapshots remain in git history.
- `business/partners/eliza-solutions-corp/` — renamed to `business/partners/eliza/`, see above.

## Fetch failures

- `index/uber-enables-outstanding-experiences/` — transient `CurlError: Recv failure: Connection reset by peer` on first attempt; succeeded immediately on retry with no other changes needed. Not recorded as an unresolved failure.
