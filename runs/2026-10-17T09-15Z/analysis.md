# Run 2026-10-17T09-15Z — analysis

**Fetch time:** 2026-10-17T09:16:58Z | **Baseline:** 2026-09-28T09-17Z (**19 days earlier — the routine missed 2026-09-29 .. 2026-10-16**, so this diff spans nearly three weeks)
**Stats:** 2063 URLs | 82 added | 1153 updated | 4 removed | 25 anomalies | 43 sub-sitemaps (was 42), 0 fetch failures

## Anomalies

### Reappeared URLs (3)
- `/business/plugins/alpaca/` — last_seen 2026-09-24T09-16Z
- `/form/codex-ambassadors/` — last_seen 2026-06-24
- `/policies/row-privacy-policy/` — last_seen 2026-05-27T09-17Z

### Sub-sitemap changes (22)
Two **new sub-sitemaps** appeared: `learn-guides` and `learn-webinars` (43 total, was 42). Those two account for all 22 membership changes: existing `/business/learn/*`, `/business/*-webinar/` and a few `/index/*` guide pages were additionally (or instead) listed there. Pages moved *out of* `page` into them: `/business/learn/intelligence-at-work-cyber/`, `…-financial-services/`, `how-our-sales-team-uses-chatgpt-work/`, `download-the-chatgpt-work-guide-for-sales-teams/`, `agent-security-enterprise/`; `how-our-finance-team-uses-chatgpt-work/` moved `learn-guides` -> `learn-webinars`. Others are cross-listed (kept old membership, gained new). Separately `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` swapped `global-affairs` -> `safety`.

### Suppressed false positives
The automated backdated-new-URL check flagged 36 additions; all have lastmod 2026-10-01..10-16, i.e. after the 2026-09-28 baseline, so they are ordinary new pages discovered late because of the 19-day gap. Not anomalous. No future-dated or backwards lastmods.

## Significant updates
**Site-wide chrome change touched ~all 1,153 updated pages** (this is why nearly every page's lastmod moved):
- Nav "Latest" model list: GPT-5.4 and GPT-6 entries replaced by **GPT-6.1 Sol** and **GPT-6 Astra**.
- "Codex" link now points to `https://chatgpt.com/codex/` instead of `/codex/`; new **Dots** link (`chatgpt.com/features/dots`) and **OpenAI Status** link in footer/nav.
- "Plugins" nav link (`/business/plugins/`) now on ~459 more pages.
- Recirculation cards: "Introducing GPT-6 Sol and Luna" and "Better prompt caching for GPT-6" (Sep 22) replaced by "Introducing the Rosalind Academic Plan" (Oct 15) on ~130 pages each.
- 216 business pages gained a "Get OpenAI for Business updates" email-signup block.
- Help-center links now carry "(opens in a new window)" label (164 pages).
Median per-page diff was 26 changed lines, nearly all of it this chrome; per-page article edits were not itemised individually.

## New pages (82)
**Models / products:** `/index/introducing-gpt-6-1-sol/` — GPT-6.1 Sol, near-Astra intelligence at one-fifth the price, cached input $0.10/M tokens (note: **no `<lastmod>` in sitemap**). `/index/introducing-dots/` — "dots": GPT-6 Astra agents with their own cloud computer, working 24/7, connecting to 4,000+ apps via plugins, reachable from ChatGPT/Slack/Teams/voice. `/index/gpt-6-for-everyone/` — new GPT-6 model for ChatGPT's 1.2B weekly users with "Intelligent UI" (interactive generated interfaces). `/index/practical-guide-building-gpt-6/` model guide. `/index/new-chatgpt-ads-format-and-measurement/` (ads). `/index/introducing-the-rosalind-academic-plan/` sponsored GPT-Rosalind access for academic labs.
**DevDay 2026:** `/devday/2026/`, `/index/devday-2026-recap/` (20+ announcements; agents with ongoing responsibilities, ChatGPT opened as a shared surface for humans and agents), forms `/form/sign-in-with-chatgpt-interest/`, `/policies/sign-in-with-chatgpt-terms/` (Sign in with ChatGPT), `/form/computer-use-research-collaboration/`, `/form/private-intelligence-interest/`, `/codex-originals/`, `/form/codex-originals/`, `/form/codex-ambassadors/`.
**Safety / policy:** `/index/disrupting-a-coordinated-model-distillation-campaign/` (adversarial distillation of protected reasoning, earliest activity first week of July), `/index/disrupting-ai-enabled-false-front-operations/`, `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/eu-text-provenance/`, `/index/the-eus-next-chapter-in-ai-is-agentic/`, `/index/how-we-will-do-better-for-australia/`, `/policies/brazil-advertising-terms/`, `/policies/row-privacy-policy/`.
**Customer stories (~25):** Albertsons, Atlassian partnership, Asana (76x model-cost cut), Basis, Benefit Street Partners, Block, Chatham, Grupo Boticário, Higgsfield, Itaú, Jump Trading, LegalOn, Localiza, Oracle, Pollo AI, Radisson (ChatGPT hotel discovery), SentinelOne, Sophos (OpenAI "Daybreak"), Stack Overflow, Sullivan & Cromwell, The Den, Third Moment Research, Amp, Ironclad, Lenfest.
**Business:** `/business/marketplace/` (spend OpenAI commitment on partner products), partner pages (Affinda, Bishop Fox, MegazoneCloud, SpecterOps, TrustedSec), plugin pages (Alpaca, Jetpack, Sandstone, Spacefast, WordPress.com), 18 `/business/learn/*` guides/webinars (the new learn sub-sitemaps' content, e.g. GPT-Live-1 webinar).
**Other:** `/index/sharing-ai-progress-in-mathematics/`, `/index/teens-learn-and-plan/`, `/index/teaching-students-to-think-and-learn-through-questions/`, `/index/the-eternal-complement/`, `/index/helping-small-businesses-put-ai-to-work/`.
Full list in diff.json.

## Removals (4)
- `/business/partners/pathfindr/` -> renamed: replaced by `/business/partners/affinda/` ("Affinda (formerly Pathfindr)").
- `/business/plugins/mcp-server-for-wordpress/` and `/business/plugins/wordpress-com/` -> consolidated into new `/business/plugins/wordpress/` (WordPress.com) .
- `/form/ultrafast/` — gone, no obvious successor.
Last snapshots in git history.
