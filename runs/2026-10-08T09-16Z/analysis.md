# Run 2026-10-08T09-16Z Analysis

**Fetch time:** 2026-10-08T09:17:25Z (sitemap + 792 pages, 0 fetch failures)
**Baseline:** 2026-09-28T09-17Z — NOTE: a **10-day gap** (no runs for Sep 29 – Oct 7), so this diff aggregates ~10 days of change, including DevDay 2026 (keynote Sep 29).
**Stats:** 2021 URLs | 37 added | 755 updated | 1 removed | 7 anomalies | 42 sub-sitemaps

## Anomalies
- **reappeared_url** `/business/plugins/alpaca/` — last seen 2026-09-24T09-16Z, absent from the baseline, back now (page content is the plugin listing again).
- **reappeared_url** `/policies/row-privacy-policy/` — last seen 2026-05-27T09-17Z (also dropped from the sitemap in the 2026-09-22 run per git history; returns now). It is now served as "Privacy policy".
- **sub_sitemap_migration** (5, per `sub_sitemaps` recorded in state): `/index/managing-ai-investments-in-agentic-era/`, `/index/codex-maxxing-long-running-work/`, `/index/the-five-ai-value-models-driving-business-reinvention/` (ai-adoption → learn-guides); `/index/builders-guide-to-gpt-5-6/` (applied-ai → learn-guides); `/business/plugins/box/` (plugins-legal/operations → plugins-productivity). A new `learn-guides` bucket appears to be absorbing business-guide articles. (Caveat: state only began recording sub-sitemap membership recently, so earlier moves may be undetected.)
- No future-dated or backwards `<lastmod>` values; no backdated new URLs.

## Significant updates
- **Site-wide nav/footer refresh (~752 pages):** footer product list swaps "GPT-5.4" → "GPT-6.1 Sol" (and GPT-6 label → "GPT-6 Astra"), adds "Dots" (chatgpt.com/features/dots) and an "OpenAI Status" link; "Codex" link now points to chatgpt.com/codex/ instead of /codex/. Also continued "Plugins" footer link rollout (188 pages).
- **Homepage-style recirculation cards** (~130 pages) rotated: Sep 22 GPT-6 Sol/Luna and prompt-caching cards replaced by Oct 6–7 posts (GPT-6 for everyone, teens, Atlassian, Radisson, Albertsons).
- **`/policies/privacy-policy/`**: "Updated" date moved May 18 → **September 10, 2026** (lastmod Sep 30); intro no longer says "ChatGPT **and Sora**" (Sora dropped from the sentence); data-collection bullets reworded.
- **`/index/learning-to-reason-with-llms/`** (o1 post): now carries a banner stating it "introduced OpenAI o1", that o1-preview/o1-mini are retired from the API and o1 is deprecated, pointing to current models. Likely the same legacy-post banner treatment for `/index/thinking-with-images/` and `/index/introducing-o3-and-o4-mini/` (large diffs).
- **`/business/pricing/`**: adds a "Dots" feature row (Business Premium and Enterprise), drops a "Canvas" row.
- **`/products/release-notes/`**: new Oct 5, 2026 entry — self-serve HIPAA compliance support / BAA acceptance for API organizations.
- `/index/codex-for-every-role-tool-workflow/`: partner logo grid rework (many image lines removed).

## Routine updates
~740 further URLs: lastmod bump with only the nav/footer and card-rotation changes above; 2 with zero rendered diff.

## New pages (37)
Models/product: `/index/gpt-6-for-everyone/` (GPT-6 + "Intelligent UI" rolled out to all ChatGPT users, 1.2B weekly), `/index/introducing-gpt-6-1-sol/` (upgrade nearly matching Astra at ~1/5 the price; cached input $0.10/M), `/index/practical-guide-building-gpt-6/`, `/index/introducing-dots/` (24/7 agents with own cloud computer, 4,000+ app plugins, Slack/Teams), `/index/devday-2026-recap/` (20+ announcements), `/devday/2026/`, `/index/new-chatgpt-ads-format-and-measurement/` (new visual ad format), `/index/teens-learn-and-plan/`, `/business/marketplace/` (spend OpenAI commitment on partner products), `/codex-originals/` + `/form/codex-originals/`.
Safety/policy: `/index/disrupting-a-coordinated-model-distillation-campaign/` (adversarial distillation to extract protected reasoning, earliest activity first week of July), `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/eu-text-provenance/` (opt-in API text watermarking for select models), `/index/sharing-ai-progress-in-mathematics/`, `/policies/sign-in-with-chatgpt-terms/`, `/form/sign-in-with-chatgpt-interest/`, `/form/private-intelligence-interest/`, `/form/computer-use-research-collaboration/`.
Customer/partner: Atlassian, Radisson, Albertsons, Chatham Financial, Jump Trading, Basis (tax workbook, GPT-6 Astra), The Den, Ironclad, Lenfest Institute, small-business push, Australia commitments, MegazoneCloud, plugins Sandstone/Spacefast/Alpaca, `/business/learn/board-guide-cybersecurity-ai/`, essay `/index/the-eternal-complement/` (first in a "next economy" series on an independent-voices platform).

## Removals
- `/form/ultrafast/` — "Stay updated on Ultrafast mode" waitlist (GPT-5.6 Sol on Cerebras, up to 750 tok/s). Last snapshot in git history.
