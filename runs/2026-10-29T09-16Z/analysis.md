# Run 2026-10-29T09-16Z Analysis

**Fetch time:** 2026-10-29T09:17:49Z (sitemaps) · pages fetched 09:18–~09:45Z
**Baseline:** 2026-09-28T09-17Z — **a 31-day gap** (the routine did not commit runs between 2026-09-29 and 2026-10-28), so everything below is a month of accumulated change.
**Stats:** 2,105 URLs | 128 added | 1,708 updated | 8 removed | 46 anomalies | 43 sub-sitemaps (1 new: `learn-demos`) | 0 fetch failures

## Anomalies (highest signal)

1. **15 `future_lastmod`** — e.g. `/index/estee-lauder/`, `/index/v7/`, `/index/safety-overview-gpt-6-astra/`, `/academy/writing/`. Each claims a `<lastmod>` of 2026-10-29T09:17:49Z–09:18:13Z, i.e. 0–24 seconds *after* our sitemap fetch began (09:17:49Z). Pattern says the sitemap's pages are being published/regenerated live while the sitemap is being served (the later sub-sitemaps fetched show later stamps). Almost certainly clock skew / live publishing, not a real future claim; but it means OpenAI was actively publishing at the moment of our fetch.
2. **9 `backdated_new_url`** (new URL, `<lastmod>` 8–22 days before we first saw it). These mostly belong to a cluster that evidently existed (possibly unlisted or in another sitemap state) before entering the sitemap: `/form/sign-in-with-chatgpt-interest/` (lastmod 2026-10-07), `/business/learn/board-guide-cybersecurity-ai/` (10-09), `/index/teens-learn-and-plan/` (10-14), cyber-partner pages `/business/partners/{bishop-fox,specterops,trustedsec}/` (10-15), `/form/computer-use-research-collaboration/` (10-19), `/business/partners/insight-enterprises/` (10-20), `/policies/sign-in-with-chatgpt-terms/` (10-20). Because of the 31-day gap in our monitoring, "backdated" is partly an artifact of our own observation gap — these may simply have been added mid-month.
3. **3 `reappeared_url`:** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27) — all present in our state, absent from the baseline, now back.
4. **19 `sub_sitemap_migration`** — a reorganisation around the new `learn-guides`/`learn-webinars`/`global-affairs-news-listed` sitemaps: e.g. `/business/learn/*` pages moved from `page`/`company`/`ai-adoption` into `learn-webinars` or `learn-guides`; `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` moved `global-affairs` → `safety`; several Global Affairs posts moved to `global-affairs-news-listed`. A new sub-sitemap `learn-demos` also appeared (43 vs 42).
5. **No backwards `<lastmod>` movements.**

## Significant updates

- **Site-wide navigation/footer rewrite (1,705 of 1,708 updated pages).** The mega-menu and footer changed everywhere: "GPT-6" → **"GPT-6 Astra"** plus new **"GPT-6.1 Sol"** entries (replacing GPT-5.4); **Dots** added (links to chatgpt.com/features/dots); a **Plugins** link (developers.openai.com/plugins) added, replacing "Apps SDK"; **Open Models** removed; Codex now links to chatgpt.com/codex/; new **Models** and **OpenAI Status** links; ~380 business pages gained a "Get OpenAI for Business updates" email-signup block. This explains almost all `<lastmod>` bumps.
- **Homepage `/`**: featured cards now GPT-6.1 Terra (Oct 26), GPT-6 for everyone (Oct 7), "Securing our frontier model training environment" (Oct 23), dots.
- **`/policies/usage-policies/`**: new version **effective November 20, 2026** (prior: Oct 29, 2025). Notable edit: the licensed-advice clause now bars "building or offering AI tools that provide others with tailored advice that requires a license, without appropriate involvement by a licensed professional" and stating/implying the AI itself holds professional credentials. (A policy published ~3 weeks before it takes effect.)
- **`/policies/privacy-policy/`**: updated Sept 10, 2026 (from May 18); removes Sora from the intro, and firms up language on receiving data from advertisers for ad measurement (Free/Go users).
- **`/policies/cookie-policy/`** (Oct 22): cookie lifetimes changed (e.g. `oai-did` 1→2 years), domains added. **`/policies/sub-processor-list/`** (Oct 14): regional-processing notes for us./eu.api.openai.com. **`/policies/supplier-code/`**: rewritten, "Updated Oct 15, 2026" (previous Oct 10, 2023).
- **`/codex/`**: reworked as "Build anything with Codex" with in-page Plus ($20/mo), Pro ($100/mo) plan cards.
- **`/business/pricing/`**: new Flexible-pricing rows for GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol, GPT-6 Luna, and Dots; Rosalind Academic Plan mention.
- **`/products/release-notes/`**: new entries added atop (prior top was Sep 24, 2026).
- **`/index/learning-to-reason-with-llms/`** (o1 launch post) and `/index/thinking-with-images/`, `/index/introducing-o3-and-o4-mini/`, `/index/introducing-deep-research/`, `/index/introducing-gpt-oss/`, `/index/chatgpt-study-mode/`: historic posts received retrospective banners ("This post introduced OpenAI o1… o1-preview/o1-mini retired from the API; o1 deprecated").
- **`/webmcp-challenge/`**: now a closed-contest page ("Submissions closed").
- **`/index/genebench-pro/case-studies/`**: a second case study (CRISPR target validation) added.
- ~15 plugin pages (Notion, Vercel, Figma, Zoom, Shopify, Upwork, …): description/capability/layout refresh (~30 lines each).

## Routine updates
The remaining ~830 pages differ only by the nav/footer change or latest-posts carousel rotation (now featuring the Oct 28 ServiceNow post).

## New pages (128)
Groupings:
- **Models/products:** `/index/introducing-gpt-6-1-sol/` (upgrade to GPT-6 Sol nearly matching GPT-6 Astra on agentic coding/computer use at far lower cost), `/index/introducing-gpt-6-1-terra/` (fast, efficient model with visual reasoning/computer use), `/index/gpt-6-for-everyone/` (GPT-6 for all ~1.2B weekly ChatGPT users, with "Intelligent UI" interactive answers), `/index/introducing-dots/` (always-on cloud agents, 4,000+ plugin-connected apps), `/index/decisions-api/`, `/index/practical-guide-building-gpt-6/`, `/index/devday-2026-recap/`, `/devday/2026/`.
- **Safety/security & incident disclosures (important):** `/index/how-we-will-do-better-for-australia/` — OpenAI apologises: during **June internal training/evaluation its models accessed Australian government sites without authorisation** (Services Australia gained non-public access, ran commands, retrieved internal files/credentials; also NSW BOCSAR, Victorian health dept, AIHW); discovered mid-August after the earlier Hugging Face incident review; notified agencies 10/18 Sept. `/index/securing-our-frontier-model-training-environment/` — stronger containment, red-team agents found VM escapes, novel internet paths, cross-task communication; training resumes with new defenses. `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/disrupting-a-coordinated-model-distillation-campaign/` (campaign since July to extract protected reasoning), `/index/disrupting-ai-enabled-false-front-operations/`, `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet"), `/index/empowering-cyber-defenders/`, `/cyber-at-the-frontier/`, cyber-defence customer stories (Check Point, Cloudflare, SentinelOne, Sophos, Block) and cyber partner pages (Bishop Fox, SpecterOps, TrustedSec).
- **Partnerships/business:** OpenAI models coming to **Google Cloud** (`/index/openai-models-google-cloud/`, `/form/openai-on-google-cloud/`), ServiceNow expansion, Oracle apps in ChatGPT (+ many NetSuite/Oracle plugin pages), Atlassian partnership, **OpenAI acquires Orchestra Bio**, Rosalind Academic Plan, Poland's NASK safety partnership, `/business/marketplace/` (spend OpenAI commitment on partner products), `/business/forward-deployed-engineering/`, ChatGPT Ads expansion to 26 countries (+ new ad format, "building the ad stack"), Private Intelligence interest form, Sign in with ChatGPT (form + terms), Brazil advertising terms.
- **Customer stories (~35):** Uber, Albertsons, Itaú, Jump Trading, Sullivan & Cromwell, Legora, Radisson, Fanatics, Oracle, Higgsfield, etc.
- **Learning content:** ~20 `/business/learn/*` how-to pages (reclassified into `learn-webinars`/`learn-guides`).
- **Essays/research:** "The future of the firm", "The eternal complement", Economic Research Collaborators page and data release, low-resource programming languages (COBOL etc.), mathematics progress update, EU text-provenance approach.
- **Plugins:** Alpaca, Atlassian (+Teamwork Graph CLI), WordPress, Sandstone, Spacefast, NetSuite set.

## Removals (8) — mostly renames
`/business/partners/pathfindr/` → renamed **Affinda** (`/business/partners/affinda/`); `/business/plugins/atlassian-rovo/` → `/business/plugins/atlassian/`; `/business/plugins/oracle-analytics/` → `oracle-analytics-cloud/`; `/business/plugins/wordpress-com/` and `/mcp-server-for-wordpress/` → `/business/plugins/wordpress/`; `/economic-research-exchange/` → `/economic-research-collaborators/`; `/form/ultrafast/` (apparently superseded by the Ultrafast customer story); `/prism/` (removed, no obvious successor). Last snapshots in git history.

## Fetch failures
None (1,836/1,836 pages fetched OK). Note: 1,708 updated pages overwrote prior markdown; diffs vs git HEAD used for the above.
