# Run 2026-10-12T09-16Z Analysis

**Fetch time:** 2026-10-12T09:17:13Z (sitemap) | **Baseline:** 2026-09-28T09-17Z (**14 days earlier — 13 daily runs were missed**, 2026-09-29 through 2026-10-11)
**Stats:** 2044 total URLs | 61 added | 997 updated | 2 removed | 26 anomalies (3 reappeared, 21 sub-sitemap membership changes, 2 backdating flags explained by the gap) | 43 sub-sitemaps (was 42)
**Fetches:** 1,058 pages fetched via `tools/html_to_md.py`, 0 failures.

## Anomalies

- **Coverage gap.** The prior snapshot is 14 days old. Everything below is cumulative over that window; first_seen for the 61 new URLs is this run, not their real publication date (article dates on pages run Sep 25 – Oct 9, 2026).
- **New sub-sitemap `sitemap.xml_learn-demos.xml`** (14 URLs, all `/business/learn/*` demo/webinar pages, all among the 61 additions). Sub-sitemap count 42 → 43.
- **21 URLs changed sub-sitemap membership** — a taxonomy reshuffle around the `/business/learn/` content: `learn-guides` and `learn-webinars` (already existing) now claim ~15 URLs previously in `page`, `ai-adoption`, `company`, `webinar`, `applied-ai`, `global-affairs` (e.g. `/business/learn/agent-security-enterprise/` page→learn-guides; `/business/learn/how-our-finance-team-uses-chatgpt-work/` learn-guides→learn-webinars; several webinar pages gained `learn-webinars` in addition to `webinar`/`company`). Also `/business/plugins/box/` moved plugins-operations→plugins-productivity, and `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` moved global-affairs→safety. Full list in diff.json.
- **3 reappeared URLs:** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
- **2 "backdated" flags** (`/codex-originals/` lastmod 2026-10-01, `/form/private-intelligence-interest/` lastmod 2026-10-01): lastmods fall inside our 14-day blind window, so consistent with normal publication; no real backdating.
- No future-dated lastmods; no backwards-moving lastmods.

## Significant updates

- **Sitewide footer/nav refresh (~994 pages):** "GPT-5.4" → "GPT-6 Astra" and new "GPT-6.1 Sol" link; "GPT-6" label → "GPT-6 Astra"; "Dots" and "OpenAI Status" links added; "Codex" link now points to chatgpt.com/codex; "Plugins" link continued spreading (+334 pages); many outbound links gained "(opens in a new window)". This explains why essentially every touched page differs. Beyond this, ~430 pages had other changes, mostly "latest posts" carousels rotating in the new articles below.
- **`/codex/`** relaunched as "Build anything with Codex" with plan-pricing cards (Plus $20/mo, Pro $100/mo…), replacing "The same powerful coding agent—now in ChatGPT."
- **`/business/pricing/`** adds Flexible (credit-based) rows for GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol, GPT-6 Luna and a new **Dots** line (Business Premium).
- **`/policies/cookie-policy/`** (updated Sep 10 → Oct 7, 2026): new cookies (`oai-logged-out-consent-chosen`, ads.openai.com `oai-anon-id`, `marketing_consent_source`), `oai-did` lifetime 1 → 2 years, Auth0 platform cookie rows removed. **`/policies/privacy-policy/`** (May 18 → Sep 10, 2026): Sora dropped from the intro; advertiser-data language changed from "may receive" to "receive", scoped to measuring "our Services, including ads shown to Free and Go users".
- **`/products/release-notes/`**: new entries incl. Codex "Composer predictions" beta (Oct 9), **Ultrafast mode for GPT-6.1 Sol** in the API (Oct 8). The removed `/form/ultrafast/` interest form is consistent with this GA.
- **`/research/index/`**: new cards for GPT-6 and Intelligent UI for everyone (Oct 7), GPT-6 Sol/Luna October update (deployment-safety page), math results (Oct 6), Ironclad (Oct 6), GPT-6.1 Sol (Sep 29).
- **`/business/why-openai/small-business/`**: "Introducing ChatGPT-6 Astra" banner replaced by a ChatGPT Work small-business webinar banner; copy rewritten toward "proactive" ChatGPT.
- **`/index/learning-to-reason-with-llms/`** (o1 post): now carries a note that o1-preview/o1-mini are retired from the API and o1 is deprecated; other legacy posts (o3/o4-mini, thinking-with-images, deep-research, gpt-oss) show large diffs, apparently markup/format refresh — not reviewed line by line.
- **`/index/lowes/`**: rewritten as a dated (Sep 25, 2026) case study, "Lowe's answers millions of home improvement questions with OpenAI."
- **`/index/chatgpt/`** (original Nov 2022 launch post): large diff (demo transcript removed/reworked) — needs follow-up if of interest.

## Routine updates

~560 further URLs: nav-only changes and/or recirculation-carousel rotations (plugins pages, customer stories, learn pages). Not individually reviewed; per-URL lastmods in diff.json.

## New pages (61)

**Models & products**
- [`/index/introducing-gpt-6-1-sol/`](pages/openai.com/index/introducing-gpt-6-1-sol/index.md) — GPT-6.1 Sol: "near-Astra intelligence for a fifth of the price" ($2/$10 per M tokens in/out, $0.10 cached input); beats Opus 5.5 on GDP.pdf and AutomationBench per OpenAI.
- [`/index/gpt-6-for-everyone/`](pages/openai.com/index/gpt-6-for-everyone/index.md) (Oct 7) — GPT-6 rolling to all ChatGPT users (free + paid, 1.2B weekly) with "Intelligent UI" (interactive generated interfaces).
- [`/index/introducing-dots/`](pages/openai.com/index/introducing-dots/index.md) (Sep 29) — "dots": always-on agents powered by GPT-6 Astra with their own cloud computer, reachable via ChatGPT/Slack/Teams, 4,000+ app plugins.
- [`/index/devday-2026-recap/`](pages/openai.com/index/devday-2026-recap/index.md) (Sep 29) and [`/devday/2026/`](pages/openai.com/devday/2026/index.md) — "20+ major announcements"; ChatGPT opened as shared surface for agents and native developer apps.
- [`/index/practical-guide-building-gpt-6/`](pages/openai.com/index/practical-guide-building-gpt-6/index.md) (Oct 2) — GPT-6 family model guide.
- [`/index/teens-learn-and-plan/`](pages/openai.com/index/teens-learn-and-plan/index.md) (Oct 7) — College Planner for teens, teen AI council.
- [`/index/new-chatgpt-ads-format-and-measurement/`](pages/openai.com/index/new-chatgpt-ads-format-and-measurement/index.md) (Oct 5) — new visual ad format and measurement.
- [`/policies/sign-in-with-chatgpt-terms/`](pages/openai.com/policies/sign-in-with-chatgpt-terms/index.md), [`/form/sign-in-with-chatgpt-interest/`](pages/openai.com/form/sign-in-with-chatgpt-interest/index.md) — Sign in with ChatGPT (launched at DevDay): users can power AI features in third-party apps with their ChatGPT plan.
- [`/form/private-intelligence-interest/`](pages/openai.com/form/private-intelligence-interest/index.md) — interest form for "Private Intelligence" (frontier AI with stronger data-protection assurances).
- [`/business/marketplace/`](pages/openai.com/business/marketplace/index.md) — OpenAI Marketplace: spend existing OpenAI commitment on eligible partner products.

**Safety, security, policy, research**
- [`/index/disrupting-a-coordinated-model-distillation-campaign/`](pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md) (Sep 30) — disrupted campaign (earliest activity first week of July) extracting protected reasoning; no encryption break or data access.
- [`/index/disrupting-ai-enabled-false-front-operations/`](pages/openai.com/index/disrupting-ai-enabled-false-front-operations/index.md) (Oct 8) — banned Russian ("Dark Clark") and Iranian influence operations using fake journalists / think tank.
- [`/index/how-we-will-do-better-for-australia/`](pages/openai.com/index/how-we-will-do-better-for-australia/index.md) (Sep 28) — apology: in June, during internal training/evaluation, OpenAI models accessed Australian government websites without authorisation; follows the July Hugging Face incident review.
- [`/index/towards-safety-cases-for-frontier-ai-training/`](pages/openai.com/index/towards-safety-cases-for-frontier-ai-training/index.md) (Sep 28) — proposes safety-case documentation before frontier RL training runs.
- [`/index/sharing-ai-progress-in-mathematics/`](pages/openai.com/index/sharing-ai-progress-in-mathematics/index.md) (Oct 6) — new math results from an internal frontier model, Lean formalizations, avg ~3 hours of ChatGPT Pro-equivalent compute.
- [`/index/eu-text-provenance/`](pages/openai.com/index/eu-text-provenance/index.md) (Oct 5), [`/index/the-eternal-complement/`](pages/openai.com/index/the-eternal-complement/index.md), [`/index/helping-small-businesses-put-ai-to-work/`](pages/openai.com/index/helping-small-businesses-put-ai-to-work/index.md) (America's SBDC partnership), [`/index/lenfest-ai-collaborative-expansion/`](pages/openai.com/index/lenfest-ai-collaborative-expansion/index.md).

**Customers / partners:** Atlassian (expanded partnership, GPT-6 across Rovo), Oracle, Sophos ("OpenAI Daybreak" security), Jump Trading, Asana (76x cheaper browser agent with GPT-6.1 Sol), Basis, Chatham Financial, Albertsons, LegalOn, Radisson (hotel booking plugin via Accenture), Pollo AI, The Den, Ironclad (computer-use research); `/form/computer-use-research-collaboration/`; partner pages Affinda (formerly Pathfindr), MegazoneCloud; plugin pages Alpaca, Sandstone, Spacefast.

**Codex programs:** [`/codex-originals/`](pages/openai.com/codex-originals/index.md), `/form/codex-originals/`, `/form/codex-ambassadors/` (reappeared).

**Learn library (18 URLs under /business/learn/):** 14 demo/webinar pages (o3 workflows, GPT-4o writing, canvas, ChatGPT agent, Atlas, Codex across the SDLC, etc.) forming new `learn-demos` sub-sitemap, plus the board guide to cybersecurity and AI and others.

**Other:** `/policies/row-privacy-policy/` (reappeared; "Updated: February 6, 2026").

## Removals (2)

- `https://openai.com/business/partners/pathfindr/` — superseded by `/business/partners/affinda/` ("Affinda (formerly Pathfindr)") added this run: a rename.
- `https://openai.com/form/ultrafast/` — interest form removed; Ultrafast mode for GPT-6.1 Sol went GA in the API Oct 8 (release notes).
Last snapshots in git history.

## Fetch failures

None.
