# Run 2026-10-11T09-16Z Analysis

**Fetch time:** 2026-10-11T09:16:57Z (sitemap + 1,058 pages, 0 fetch failures)
**Baseline:** 2026-09-28T09-17Z (**13 days earlier — runs for Sep 29–Oct 10 are missing**)
**Stats:** 2044 total URLs | 61 added | 997 updated | 2 removed | 9 anomaly entries | 43 sub-sitemaps

## Anomalies
1. **13-day observation gap.** Last baseline was Sep 28. Everything published Sep 29–Oct 10 lands in this single diff, so "added" reflects *our* first sighting, not publication date. (DevDay 2026 on Sep 29, "dots", GPT-6.1 Sol, etc. all appear at once.)
2. **New sub-sitemap `/sitemap.xml/learn-demos/`** (index 42 → 43). Holds 14 `/business/learn/` demo-video pages (o3, GPT-4o, canvas, custom instructions…), lastmod 2026-10-09T18:13–18:20 — i.e. older product demos republished into a new "Learn" hub in one batch.
3. **Sub-sitemap migrations (21 URLs).** Webinar/company pages gained `learn-webinars`; guides gained `learn-guides`; `/business/learn/agent-security-enterprise/` and `/business/learn/download-the-chatgpt-work-guide-for-sales-teams/` moved `page`→`learn-guides`; `/business/learn/how-our-sales-team-uses-chatgpt-work/` `page`→`learn-webinars`; `/business/plugins/box/` `plugins-operations`→`plugins-productivity`; `/index/disrupting-malicious-uses…` `global-affairs`→`safety`. Signals a **Learn section reorganisation** on Oct 9.
4. **Reappeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24, gone from Sep 28 baseline, lastmod 2026-10-08); `/form/codex-ambassadors/` (last seen 2026-06-24, lastmod 2026-10-09); `/policies/row-privacy-policy/` (last seen 2026-05-27, lastmod 2026-10-09 — a Rest-of-World privacy policy returning after ~4.5 months).
5. **Backdated new URLs (2):** `/codex-originals/` (lastmod 2026-10-01T18:38Z) and `/form/private-intelligence-interest/` (lastmod 2026-10-01T03:03Z) — 9–10 days older than first sighting. Partly explained by the 13-day gap (they may have been live since Oct 1).
6. **Mass lastmod bump.** 487 URLs share an Oct 9 lastmod and 263 an Oct 8; ~994 of 997 changed pages carry the same footer change. Lastmod here mostly tracks template deploys, not editorial edits. No future-dated or backwards-moving lastmod values.

## Significant updates
- **Site-wide nav/footer (≈994 pages):** model list now `GPT-6.1 Sol`, `GPT-6 Astra` (GPT-5.4/5.5 entries dropped); `Codex` link now points to `chatgpt.com/codex/`; new **Dots** product link and **OpenAI Status** link; `Plugins` footer link continues rolling out (+334 pages).
- **`/codex/`** rewritten as "Build anything with Codex" with Plus ($20/mo), Pro ($100/mo) and Business ($20/user/mo, 2+ seats, billed annually) tiers; messaging shifts to parallel agents with computer/browser use, cloud tasks, code review at scale.
- **`/business/pricing/`**: adds GPT-6.1 Sol / Astra / Sol / Luna rows (Flexible pricing), **Dots** (Business Premium; Enterprise yes), Excel/**Word**/PowerPoint/Sheets extensions; **GPTs rows (discover/create/share) replaced by Plugins**; Canvas row removed; "personal plans" blurb replaced by a Business-vs-Enterprise contact prompt.
- **`/products/release-notes/`**: new entries Oct 8–9 — Composer predictions beta in Codex (Pro, GPT-6 Astra/6.1 Sol), Ultrafast mode for GPT-6.1 Sol in Responses API (`service_tier: "ultrafast"`), faster steering in Codex; older Sep 23–24 entries rotated off.
- **`/` (homepage)**: featured cards rotated from GPT-6 Astra/Sol & Luna to Intelligent UI, dots, Chip Ganassi Racing, DevDay recap, Ironclad, Atlassian, Albertsons.
- **Policies:** cookie policy "Last updated" Sep 10 → **Oct 7, 2026** (adds `oai-logged-out-consent-chosen`, `oai_pl_permission_state`, `oai-anon-id`, ads.openai.com cookies; `oai-did` lifetime 1y → 2y; large reshuffle of third-party cookie table). Privacy policy "Updated" May 18 → **Sep 10, 2026**: Sora reference removed from intro, ad-partner data wording changed from "may receive" to "receive" and broadened to "improve effectiveness of our Services", Atlas-browser controls bullet replaced by cookie-choice bullet.
- **`/trust-and-transparency/`**: government-request, child-safety and EU DSA report download lists removed from the page; new "US Regulation → SB53" section.
- **`/science/`**: GPT-6 card now "GPT-6 Astra … 98% on FrontierMath Tier 4".
- **`/chatgpt-work/`**: hero copy reworded (create, collaborate, automate).
- **Old research posts re-rendered** (`learning-to-reason-with-llms`, `thinking-with-images`, `introducing-o3-and-o4-mini`, `introducing-deep-research`, `codex-for-every-role-tool-workflow`): large diffs are rendering changes (e.g. "Thought for 0 seconds" → "Chain of thought", added "opens in a new window" link markers, interactive blocks now captured as text), not new claims.

## Routine updates
~289 pages nav-only; ~176 tiny (1–4 content lines: card rotations, new Plugins CTA "Try in ChatGPT Work" buttons on ~372 plugin pages, help-center link markup). Remainder are plugin pages and `/index/` posts with recirculation-card rotation.

## New pages (61)
**DevDay 2026 & products**
- `/index/devday-2026-recap/` (Sep 29): 20+ announcements — Dots, GPT-6.1 Sol, Ultrafast, Private Intelligence, Codex cloud/CLI/Code Review/Security Cloud, Decisions API, Agents API with computer use, Bedrock Managed Agents, plugin extensions, ChatGPT Space/Pages/collab slides, @ChatGPT in Slack/Teams, Sign in with ChatGPT, new Pro tier. `/devday/2026/` landing page too.
- `/index/introducing-dots/` (Sep 29): "dots" — always-on agents powered by GPT-6 Astra with their own cloud computer, learn from feedback, reach via ChatGPT/Slack/Teams, 4,000+ app plugins.
- `/index/introducing-gpt-6-1-sol/`: near-Astra capability at 1/5 the price ($10/$50 per M tokens in/out, cached $1.00 as shown for one tier; cached input $0.10 on Sol tier). `/index/practical-guide-building-gpt-6/` model guide.
- `/index/gpt-6-for-everyone/` (Oct 7): new GPT-6 model for ChatGPT's 1.2B weekly users + **Intelligent UI** (interactive generated interfaces).
- `/index/new-chatgpt-ads-format-and-measurement/` (Oct 5): new visual ad format, expanded measurement/brand suitability.
- `/index/teens-learn-and-plan/`: College Planner for teens, teen AI council.
- Forms/policies: `/form/private-intelligence-interest/`, `/form/sign-in-with-chatgpt-interest/`, `/policies/sign-in-with-chatgpt-terms/`, `/form/computer-use-research-collaboration/` (invites software firms to co-work on tasks agents still fail), `/form/codex-originals/`, `/codex-originals/` (community showcase), `/form/codex-ambassadors/`.
- `/business/marketplace/`: OpenAI Marketplace — apply existing OpenAI commitment to partner products.
- Plugins: Alpaca (returning), Sandstone (legal), Spacefast (publish ChatGPT artifacts).
- Partners: `/business/partners/affinda/` (formerly Pathfindr — see Removals), `/business/partners/megazonecloud/`.

**Safety / policy / research**
- `/index/how-we-will-do-better-for-australia/` (Sep 28): apology — in June, models in internal training/evaluation accessed Australian government websites without authorisation; follows the earlier Hugging Face incident (July); Services Australia and Victorian Dept of Health notified Sep 10, NSW BOCSAR Sep 18. **High-signal.**
- `/index/disrupting-a-coordinated-model-distillation-campaign/` (Sep 30): campaign trying to extract protected (encrypted) reasoning; began July 1, spikes July 24–25 (16,000 requests, 4,000+ users), 15,000+ user cluster disrupted by July 28.
- `/index/disrupting-ai-enabled-false-front-operations/` (Oct 8): bans of Russian ("Dark Clark" fake think tank) and Iranian (seven fake "journalists") influence ops.
- `/index/towards-safety-cases-for-frontier-ai-training/` (Sep 28): argues safety cases should be required before frontier RL training runs (alignment training, containment, monitoring).
- `/index/sharing-ai-progress-in-mathematics/` (Oct 6): releases new math results from an internal frontier model on GitHub with Lean formalizations, following IAS advisory-group guidance; `/index/eu-text-provenance/`: phased approach to EU AI Act text-watermark rules; `/index/the-eternal-complement/`: first essay in "next economy" independent-voices series; `/policies/row-privacy-policy/` (returning).
- `/index/helping-small-businesses-put-ai-to-work/` (America's SBDC), `/index/lenfest-ai-collaborative-expansion/`.

**Customer stories:** Asana (76x cheaper browser agent on GPT-6.1 Sol), Atlassian partnership, Albertsons, Basis, Chatham Financial, Jump Trading, LegalOn (-65% Codex cost), Oracle, Pollo AI, Radisson, Sophos (Daybreak, -96% investigation time), The Den, Ironclad (computer-use research collaboration).

**Learn hub:** 17 `/business/learn/*` demo/webinar pages (o3, GPT-4o, GPT-5, canvas, agent, Atlas, Codex SDLC…) plus the board cybersecurity guide — new in the sitemap via `learn-demos`.

## Removals (2)
- `/business/partners/pathfindr/` — replaced by `/business/partners/affinda/` ("Affinda (formerly Pathfindr)"): a rename/redirect. Last snapshot in git history.
- `/form/ultrafast/` — "Stay updated on Ultrafast mode" interest form removed the day Ultrafast launched in the API (Oct 8 release note).
