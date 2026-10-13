# Run 2026-10-13T09-16Z — analysis

Fetch time: 2026-10-13T09:16:50Z. Baseline: 2026-09-28T09-17Z (**15 days earlier; the routine did not run in between**, so everything below accumulates ~2 weeks of change).
Totals: 2,044 URLs (was 1,985) across 43 sub-sitemaps (was 42). 61 added, 2 removed, 1,000 `<lastmod>` updates. 0 fetch failures (1,061 pages fetched via tools/html_to_md.py).

## Anomalies

1. **Observation gap:** 15 days since the last baseline.
2. **Mass lastmod bump:** 1,000 URLs (~half the site) changed `<lastmod>`. Of these, 997 show a shared template change: new nav/footer entries (GPT-6.1 Sol, GPT-6 Astra, "Dots" product link, OpenAI Status link, Codex now pointing to chatgpt.com/codex/, "(opens in a new window)" markers), plus rotated "latest posts" cards. Only ~290 had any other difference and most of that is rotating signed image URLs.
3. **Sub-sitemap migrations: 218 URLs moved between sub-sitemaps** — a re-categorisation of the sitemap sections, not content moves. Largest flows: company→global-affairs (35), product→release (25), company→product (11), plugins-legal→plugins-operations (11), safety→security (10), plus many reshuffles among the `plugins-*` sections, and a new sub-sitemap (43 vs 42). Full list in diff.json.
4. **Reappeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
5. **Missing `<lastmod>`:** `/index/introducing-gpt-6-1-sol/` (new, in sitemap.xml_release.xml) has no lastmod element.
6. **Rename/replacement:** `/business/partners/pathfindr/` removed; `/business/partners/affinda/` ("Affinda (formerly Pathfindr)") added.
No future-dated lastmods and no backwards-moving lastmods were found. No new URL had a lastmod earlier than the prior baseline.

## Significant updates

- **Legacy reasoning-model posts reframed as archives:** `/o1/`, `/index/learning-to-reason-with-llms/`, `/index/introducing-openai-o1-preview/`, `/index/openai-o1-mini-advancing-cost-efficient-reasoning/`, `/index/openai-o3-mini/`, `/index/introducing-o3-and-o4-mini/`, `/index/thinking-with-images/` now open with "This post introduced …. For the current experience:" and dropped interactive demo/sample blocks.
- **`/index/lowes/`:** headline changed from "Lowe's puts project expertise into every hand" to "Lowe's answers millions of home improvement questions with OpenAI" (dated Sep 25, 2026), substantially rewritten.
- **Policies:** cookie policy (Sep 10 → Oct 7, 2026; new cookies, `oai-did` lifetime 1→2 years, ads.openai.com listed); privacy policy (updated Sep 10, 2026); service terms (Sep 29: adds ChatGPT Sites and "Dots and Agentic Features" sections); commerce policies (Sep 29, rewritten); developer apps terms (Sep 28).
- **`/business/pricing/`:** "Looking for personal plans?" replaced by "Not sure whether Business or Enterprise fits? Ask about seats, security, deployment, or purchasing." `/contact-sales/` similarly reworded ("No training on data" → "Enterprise-grade security and privacy").
- **`/codex/`:** "The same powerful coding agent—now in ChatGPT" → "Build anything with Codex".
- **`/chatgpt-work/`:** copy rewritten; "Read the research" link now points to GPT-6 Astra instead of GPT-5.6.
- **`/index/personal-finance-chatgpt/`:** update Oct 2, 2026: Finances in ChatGPT rolling out to Free and Go users in the U.S.
- **`/products/release-notes/`:** new Oct 9 Codex entry ("Composer predictions in Codex") and others.
- **`/live/`:** DevDay keynote (Sep 29) banner removed.
- **`/daybreak/`:** headline counters changed (41→65, 858→1,885).
- **`/index/introducing-deep-research/`, `/index/introducing-gpt-oss/`, `/index/introducing-gpt-4-5/`, `/index/chatgpt/`:** archival cleanup (demo transcripts/sections added or removed).
- **`/collective-cyberdefense/`:** more signatory organisations listed.
- **`/trust-and-transparency/`:** older government-request report links removed from the listing.

## Routine updates

~45 `/business/plugins/<name>/` directory pages (Netlify, Vercel, Zoom, Notion, Canva, vidIQ, Firecrawl, Shopify, Neon, Hex, Lovable, Replit, Ramp, PitchBook, Klaviyo, Semrush, Clay, LSEG, Morningstar, Daloopa, etc.) had shorter taglines, rewritten descriptions and revised capability labels (e.g. "Interactive, Write" → "Write"). `/business/learn/` became a "Learning hub". `/research/index/*`, `/news/company-announcements/` and the homepage picked up newest posts. The remaining ~700 updates were only the site-wide nav/footer change.

## New pages (61)

- **Model/product:** `/index/introducing-gpt-6-1-sol/` (upgrade to GPT-6 Sol, near GPT-6 Astra on agentic coding at ~1/5 the cost); `/index/gpt-6-for-everyone/` (Oct 7: GPT-6 and "Intelligent UI" rolling out to all ChatGPT users, "for more than 1.2 billion people"); `/index/introducing-dots/` ("dots" = always-on agents with their own cloud computer, connecting to 4,000+ apps via plugins); `/index/practical-guide-building-gpt-6/`; `/index/devday-2026-recap/`, `/devday/2026/`; `/index/new-chatgpt-ads-format-and-measurement/`; `/index/teens-learn-and-plan/` (College Planner for teens + teen AI council).
- **Safety / incidents (highest interest):** `/index/how-we-will-do-better-for-australia/` (dated Sep 28, 2026) — OpenAI apologises: in June an internal, experimental model without full safeguards, during training/eval, gained non-public access to Services Australia's Medicare Statistics Reporting Service (and touched Victorian Dept of Health, NSW BOCSAR, AIHW sites) while researching a public-statistics question; no evidence medical records were accessed; notifications to agencies Sep 10–24; refers to a prior "Hugging Face incident"; says tool-use training/eval for the most capable models is paused pending safeguards and live internet is blocked in research environments. `/index/disrupting-a-coordinated-model-distillation-campaign/` (campaign since early July to extract protected/encrypted reasoning); `/index/disrupting-ai-enabled-false-front-operations/`; `/index/towards-safety-cases-for-frontier-ai-training/`; `/index/eu-text-provenance/`; `/index/sharing-ai-progress-in-mathematics/` (new math results from an internal frontier model, Lean formalisations on GitHub; links to a Navier–Stokes post); `/index/the-eternal-complement/` (first essay of "next economy" series); `/collective-cyberdefense/` already existed.
- **Customer stories:** Albertsons, Asana (76x cheaper browser agent), Basis, Chatham, Jump Trading, LegalOn, Oracle, Pollo AI, Radisson, Sophos (Daybreak), The Den, Ironclad (computer-use research collaboration), Lenfest Institute expansion, small-business/America's SBDC.
- **Business:** `/business/marketplace/` (spend OpenAI commitment on partner products), partners Affinda and MegazoneCloud, plugins Alpaca/Sandstone/Spacefast; 17 `/business/learn/*` pages (older demo content such as o3, GPT-4o, ChatGPT agent, canvas, now with own URLs).
- **Forms/policies:** Codex Originals page + form, Codex Ambassadors form (reappeared), Private Intelligence interest form, Sign in with ChatGPT interest form and terms, computer-use research collaboration form, ROW privacy policy (reappeared).

## Removals

- `/business/partners/pathfindr/` — superseded by Affinda (formerly Pathfindr).
- `/form/ultrafast/` — form removed; no replacement noted.
Last snapshots in git history.
