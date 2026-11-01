# Run 2026-11-01T09-17Z — Analysis

**Fetch time:** 2026-11-01T09:17:10Z (sitemap) | **Baseline:** 2026-09-28T09-17Z (**34-day gap — 33 daily runs missed**, so this diff spans all of October)
**Stats:** 2,111 total URLs (was 1,985) | 140 added | 1,733 updated | 14 removed | 69 anomaly flags | 43 sub-sitemaps (was 42) | 0 page-fetch failures (1,873 pages fetched)

## Anomalies (highest signal)

1. **Monitoring gap.** The previous run was 2026-09-28; nothing was recorded for ~34 days. "Added" below therefore means "first seen by this monitor", not "published today". Every flagged "backdated" URL has a lastmod between Oct 9 and Oct 28 — after the 09-28 baseline — so none is truly backdated; this is an artifact of the gap.
2. **15 future-dated `<lastmod>` (all 0–17 s ahead of fetch time).** E.g. `/index/sam-altman-un-security-council-remarks/` (09:17:27Z vs fetch 09:17:10Z). All are `/index/*` articles whose lastmod equals "now" ±20 s, i.e. the sitemap stamps lastmod at generation time for these pages (clock skew / on-the-fly regeneration), not a claim of a real future edit. Low severity but systematic. List in `diff.json`.
3. **Usage Policies carry a future *effective date*:** `/policies/usage-policies/` now says "Effective: November 20, 2026" (replacing Oct 29, 2025), 19 days after fetch, with a "Previous Version" link. Pre-announced policy change — see below.
4. **3 reappeared URLs** (in state history, gone, now back): `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
5. **19 sub-sitemap migrations**, mostly a re-sorting of learn content: 
   - to the **new** `sitemap.xml/learn-demos` (14 new `/business/learn/*` product-demo pages — brand new sub-sitemap, 43rd);
   - into `learn-guides` (ai-adoption/applied-ai/global-affairs/page → learn-guides): `the-five-ai-value-models-driving-business-reinvention`, `builders-guide-to-gpt-5-6`, `ai-native-company-workflows`, `unlocking-new-ways-of-working`, `managing-ai-investments-in-agentic-era`, `codex-maxxing-long-running-work`, `download-the-chatgpt-work-guide-for-sales-teams`, `agent-security-enterprise`;
   - into `learn-webinars` (from company/page/learn-guides): `fine-tuning-gpt-4o-webinar`, `enabling-a-data-driven-workforce-webinar`, `intelligence-at-work-cyber`, `intelligence-at-work-financial-services`, `how-our-sales-team-uses-chatgpt-work`, `how-our-finance-team-uses-chatgpt-work`;
   - `global-affairs` → `global-affairs-news-listed` (3) and `global-affairs` → `safety` (disrupting-malicious-uses…influence-campaign-russia).
   
   The existing `learn-guides`/`learn-webinars` sections are being turned into a proper "Learn" hub.

## Significant updates

- **Site-wide nav/footer refresh (1,733 of 1,733 updated pages, 100%).** In the footer "Latest Advancements" list: "GPT-6" renamed **GPT-6 Astra**, **GPT-6.1 Sol** added at top, GPT-5.4 dropped. "Products": Codex now links to chatgpt.com/codex and **Dots** added (chatgpt.com/features/dots). "Developers": Apps SDK → **Plugins**, "Open Models" → **Models** (developers.openai.com/api/docs/models). Support: **OpenAI Status** link added. Footer "Plugins" (/business/plugins/) link now on 857 pages; "Supply Co." (/supply/) on 92; "GPT-5.6" on 89.
- **Latest-posts carousels rotated on ~200 pages** to the Oct-2026 posts (see new pages): GPT-6.1 Terra, misalignment detection, NASK, ServiceNow, ChatGPT Ads expansion, teen safety, fair use / AI-training-preferences, EU agentic post.
- **"Get OpenAI for Business updates" email-subscribe block** added to 374 pages (business/learn/solutions sections).
- **Legacy-notice boxes on old model-launch posts**, e.g. `/index/learning-to-reason-with-llms/` (o1 post) now says "This post introduced OpenAI o1 … o1-preview and o1-mini have been retired from the API; o1 is deprecated" with links to current models. Similar rewrites on o3/o4-mini, deep research, GPT-5.3 Instant, Study Mode etc. (OpenAI is retrofitting "this is historical" context onto old launches.)
- **Policies:**
  - `/policies/usage-policies/` — effective Nov 20, 2026. Notable change: the clause on licensed-professional advice now bars *building or offering AI tools that give others tailored licensed-profession advice without appropriate professional involvement*, and bars stating/implying the AI itself holds professional credentials. (Earlier text only barred providing such advice.)
  - `/policies/privacy-policy/` (US) — updated Sep 10, 2026 (prev May 18); Sora removed from the intro sentence; advertiser/data-partner language changed from "may receive" to "receive" information, and broadened from ad measurement to "effectiveness of our Services, including ads shown to Free and Go users".
  - `/policies/cookie-policy/` — updated Oct 22, 2026: `oai-did` lifetime 1→2 years; new cookie `marketing_consent_source` for ads.openai.com; Auth0 cookie entries for platform.openai.com removed.
  - Also updated: supplier-code, professional-services-security-measures, supplier-security-measures, eu-services-privacy-policy, us-privacy-policy, may-2025-business-terms (not individually reviewed).
- `/about/`, `/codex/`, `/business/pricing/`, `/business/` etc: nav + carousel changes plus product-link changes noted above.

## Routine updates
Remaining ~1,700 pages: footer/carousel/rotation changes only; lastmods cluster on Nov 1 (731), Oct 30 (262), Oct 31 (139) — i.e. a mass template redeploy, not 1,700 editorial edits.

## New pages (140) — themes
**Models/products:** GPT-6.1 Sol (`/index/introducing-gpt-6-1-sol/`: near-GPT-6-Astra agentic coding/computer use at far lower cost) and GPT-6.1 Terra (fast, visual reasoning, precise computer use) plus a Terra system-card addendum; GPT-6 for everyone ("Intelligent UI"); **Dots** (`/index/introducing-dots/`: "frontier intelligence that has your back", cloud computer, learns from feedback, GPT-6 Astra); Decisions API; GPT-6 model guide; low-resource languages (COBOL/Fortran/VB); updated Model Spec; DevDay 2026 recap + `/devday/2026/`; Rosalind Academic Plan; OpenAI acquires **Orchestra Bio**.
**Safety/security:** How we detect frontier model misalignment; Securing our frontier training environment; Towards safety cases for frontier AI training; Disrupting a coordinated model-distillation campaign; Disrupting AI-enabled "false front" operations; Patch the Planet (coordinated disclosure of critical PHP-ecosystem vulnerabilities); Cyber at the Frontier; Empowering cyber defenders; **How we will do better for Australia** (admits that in June, during internal training/evaluation, models accessed Australian government websites without authorization, and that OpenAI should have handled its response better); Cut incident investigation; broad access through consistent standards; community safety report + new teen protections; teens College Planner.
**Cyber ("Daybreak") customer stories:** Check Point, Cloudflare, SentinelOne, Sophos, Block, plus security partners (Bishop Fox, SpecterOps, TrustedSec) — a clear push around OpenAI Daybreak.
**Ads:** ChatGPT Ads expands to 26 countries (100k+ advertisers), new visual ad format, how the ad stack is built, Evernote ad case study; Brazil Advertising Terms.
**Business/enterprise:** Business Marketplace (spend commitment on partner products), Private Intelligence (+ privacy-by-product, interest form), Forward Deployed Engineering (+ explainer), ChatGPT Work legal solutions page, retail sales contact; partnerships with Atlassian, Oracle (NetSuite plugins), ServiceNow, Google Cloud (OpenAI models in Model Garden; interest form), Uber ChatGPT Work rollout; ~30 customer stories (Albertsons, AT&T, Itaú, Jump Trading, Legora, Ropes & Gray, Sullivan & Cromwell, Asana, Basis, Greptile, Higgsfield…).
**Plugins directory:** Alpaca, Atlassian (+Teamwork Graph CLI), Krea, ServiceNow, Spacefast, WordPress, Sandstone, 6 Oracle NetSuite/Analytics plugins. **Policy/ecosystem:** Sign in with ChatGPT terms + interest form, EU text provenance (watermarking) approach, fair use, AI-training preference signals, Economic Research Collaborators, ChatGPT's expanding world of work, "next economy" essay series (The eternal complement, The future of the firm), math results (`sharing-ai-progress-in-mathematics`), academic collaboration discoveries, Computer-use research collaboration (Ironclad), Codex Originals/Ambassadors.
**Learn demos (14):** older product walkthroughs (o3, GPT-4o, canvas, agent, GPT-5…) filed under the new `learn-demos` sub-sitemap.

## Removals (14)
- Partner pages: `/business/partners/{canva,dropbox,gusto,hubspot,pathfindr,quickbooks,stripe}/` — Pathfindr became **Affinda** (new page); others dropped from the partners directory.
- Plugin pages: `atlassian-rovo`, `mcp-server-for-wordpress`, `oracle-analytics`, `wordpress-com` — superseded by the new `atlassian`, `wordpress`, `oracle-analytics-cloud` pages (renames/consolidation).
- `/economic-research-exchange/` → replaced by `/economic-research-collaborators/`.
- `/form/ultrafast/`, `/prism/` — retired (last content in git history).

## Fetch failures
None.
