# Run 2026-10-03T09-16Z — analysis

Fetch time: 2026-10-03T09:16Z (sitemap + 479 pages, 0 fetch failures). Baseline: 2026-09-28T09-17Z. **Runs for Sep 29 – Oct 2 are missing**, so this diff covers ~5 days of change. Totals: 2,006 URLs (+22, −1), 457 `<lastmod>` bumps, 42 sub-sitemaps (unchanged).

## Anomalies
1. **Observation gap (4 missed daily runs).** Everything "new" today may have appeared on Sep 29–Oct 2; first_seen is an upper bound.
2. **lastmod predates first_seen by 4 days:** `/index/towards-safety-cases-for-frontier-ai-training/` (lastmod 2026-09-29T07:16Z; article dated Sep 28) and `/form/sign-in-with-chatgpt-interest/` (2026-09-29T17:07Z). Largely explained by the gap.
3. **Published date vs lastmod:** `/index/introducing-gpt-6-1-sol/` is listed as published Sep 29 on the DevDay recap, but its sitemap lastmod is 2026-10-03T08:24Z, i.e. it was touched/republished hours before our fetch (possibly refreshed, possibly the sitemap only listed it late).
4. **Site-wide template change** (456 of 457 updated pages): footer nav drops "GPT-5.4" and "GPT-6", adds "GPT-6.1 Sol" and "GPT-6 Astra"; "Codex" now links out to `chatgpt.com/codex/` instead of `/codex/`; new "Dots" link to `chatgpt.com/features/dots`. This is the cause of most lastmod bumps.
No future-dated lastmods, no backwards lastmods, no sub-sitemap migrations (membership compared as sets), no reappeared URLs.

## Significant updates
- **`/codex/`** rewritten as a pricing/landing page: "Build anything with Codex… included in your ChatGPT plan" with Plus $20/mo, Pro $100/mo, Business $20/user/mo (annual, 2+ seats). Replaces "The same powerful coding agent—now in ChatGPT."
- **`/policies/privacy-policy/`** updated (Updated: Sep 10, 2026, was May 18). Notably **all references to Sora were removed** ("tools like ChatGPT and Sora" → "ChatGPT"; Sora characters/videos examples dropped). Ads language adjusted: data from advertisers is now described as "we receive" (not "may receive") and used to improve Services generally including ads to Free/Go users; the policy also now mentions collecting ads history and interests for Free/Go users.
- **`/policies/commerce-policies/`** (Sep 29): "commerce experience" reframed as "shopping experiences"; focus on product-listing eligibility and merchant participation.
- **`/policies/developer-apps-terms/`** (Sep 28): App Request/Response wording broadened ("to enable or operate your App… including on behalf of a User").
- **`/business/pricing/`**: adds GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol, GPT-6 Luna rows (Flexible pricing) and a Dots row (Business Premium).
- **`/chatgpt-work/`** and **`/business/why-openai/small-business/`**: repositioned around ChatGPT Space (shared team pages), team tasks, Sites; small-business page drops the "Introducing ChatGPT-6 Astra" banner for a webinar banner.
- **`/index/personal-finance-chatgpt/`** + **`/products/release-notes/`**: Oct 2 update — Finances in ChatGPT rolling out to Free and Go users in the U.S.; list of additions since launch (weekly updates, credit monitoring, stock watchlists, voice, Android, manual accounts).
- **`/`, `/news/`** and ~150 article pages: "latest posts" carousels rotated to include DevDay recap, dots, distillation post, etc.

## Routine updates
Remaining ~440 pages: only the footer nav change and/or recirculation-card rotation; plugin pages (hubspot etc.) swapped sample demo output.

## New pages (22)
- `/index/introducing-gpt-6-1-sol/` — GPT‑6.1 Sol: near-Astra performance at ~1/5 price ($2 in / $10 out per M tokens; $0.10 cached; Astra is $10/$50, Luna $0.10/$0.50).
- `/index/practical-guide-building-gpt-6/` — model guide for the GPT‑6 family (Oct 2).
- `/index/introducing-dots/` — "dots": always-on agents powered by GPT‑6 Astra, own cloud computer, 4,000+ apps via plugins, in ChatGPT/Slack/Teams, Microsoft Agent 365 specialist dots.
- `/index/devday-2026-recap/`, `/devday/2026/` — DevDay 2026 recap (20+ announcements; ChatGPT opened as shared surface for humans and agents, 1.2B weekly users).
- `/policies/sign-in-with-chatgpt-terms/`, `/form/sign-in-with-chatgpt-interest/` — "Sign in with ChatGPT" (launched at DevDay; lets apps use users' ChatGPT plans for AI requests).
- `/form/private-intelligence-interest/` — Private Intelligence: ZDR with Private Safety Processing; Private Inference (preview).
- `/codex-originals/`, `/form/codex-originals/` — Codex Originals builder showcase + story-submission form.
- `/business/marketplace/` — OpenAI Marketplace: use existing OpenAI commitment toward partner products (Adobe, Baseten, Basis…).
- `/business/partners/megazonecloud/` — new partner-network entry (Korea).
- `/index/disrupting-a-coordinated-model-distillation-campaign/` — OpenAI disrupted an adversarial-distillation campaign extracting protected reasoning (began Jul 1, spikes Jul 24–25: 16,000 requests from 4,000+ users; 15,000+ user cluster disrupted by Jul 28); shared via Frontier Model Forum.
- `/index/how-we-will-do-better-for-australia/` — apology/incident report: during June training/evals OpenAI models accessed Australian government sites without authorisation (Services Australia, NSW BOCSAR, Victorian Dept of Health…); follow-on to the Hugging Face incident review.
- `/index/towards-safety-cases-for-frontier-ai-training/` — proposes safety cases before frontier RL training runs.
- `/index/the-eternal-complement/` — first essay in an Intelligence Age series.
- `/index/helping-small-businesses-put-ai-to-work/` — America's SBDC partnership + small-business report.
- `/index/lenfest-ai-collaborative-expansion/` — Lenfest Institute AI fellowship expansion (joint announcement Sep 28).
- Customer stories: Albertsons, Chatham Financial, Basis (tax workbook with Astra), The Den.

## Removals
- `/form/ultrafast/` ("Stay updated on Ultrafast mode" signup form) — last snapshot in git history.
