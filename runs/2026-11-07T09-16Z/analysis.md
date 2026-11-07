# Run 2026-11-07T09-16Z Analysis

**Fetch time:** 2026-11-07T09:16:35Z (sitemap + 1,904 pages, 0 fetch failures)
**Baseline:** 2026-09-28T09-17Z — a **40-day gap**: no snapshots exist for 2026-09-29 → 2026-11-06, so this run's diff aggregates ~6 weeks of change.
**Stats:** 2,141 total URLs | 172 added | 1,732 updated | 16 removed | 40 anomalies | 43 sub-sitemaps

## Anomalies
- **Monitoring gap:** 40 days since last snapshot. "Added" pages may have first appeared any time in that window; first_seen is recorded as this run, so it is an upper bound.
- **New sub-sitemap `/sitemap.xml/learn-demos/`** (42 → 43). It holds ~17 `/business/learn/*` pages (webinars/demos such as "Delegate work to ChatGPT agent", "GPT-5: our best model for work", GPT-4o/o3-era tutorials). Their lastmods are recent, but many titles are old products → looks like a back-catalogue being re-published into a new section.
- **30 backdated new URLs** (lastmod 8–29 days before first observation). Largest: `/business/learn/board-guide-cybersecurity-ai/` (29 d), `/business/partners/{bishop-fox,specterops,trustedsec}/` (22 d), `/form/computer-use-research-collaboration/` (18 d). Most are explained by the monitoring gap rather than true backdating.
- **3 reappeared URLs:** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
- **Missing `<lastmod>`:** `/index/advancing-independent-research-ai-alignment/` (had 2026-09-25T19:18:24Z, now none); new URLs with no lastmod: `/index/introducing-gpt-6-1-sol/`, `/index/introducing-gpt-6-1-terra/`, `/ads/customers/{evernote,flipsnack,vistaprint}/`. (The ~18 `/supply/product/*` merch pages have always lacked lastmod; not counted.)
- No future-dated lastmods, no backwards-moving lastmods.

## Significant updates
- **Site-wide navigation/footer redesign (~1,729 of 1,732 updated pages).** Same diff on nearly every page: header/footer model list changes from GPT-5.4 / GPT-6 to **GPT-6.1 Sol + GPT-6 Astra**; removed "Open Models", "Codex (/codex/)" and "Apps SDK" links; added "Plugins", "Models", "OpenAI Status", "Dots" (chatgpt.com/features/dots) and Codex (now chatgpt.com/codex/) links. Most `<lastmod>` bumps are this template push (lastmod peaks: 11-05 433 pages, 11-01 229, 11-07 224). Business pages also gained a "Get OpenAI for Business updates" email-subscribe block, and help-center links now say "(opens in a new window)".
- "Latest posts" widgets on many pages rotated to surface new articles (e.g. "Australian universities are creating AI-native graduates", Nov 5).
- Only ~3 updated pages lack the nav change; no other substantive per-page edits were individually reviewed because the template diff dominates (largest diffs: codex-for-every-role-tool-workflow, thinking-with-images, advertising-terms are nav + rewrapping).

## New pages (172) — themes
- **Model launches:** GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Cyber, GPT-6 and Intelligent UI for everyone, model guide for the GPT-6 family, Images 2.6, Decisions API, "dots", DevDay 2026 recap (`/devday/2026/`, `/index/devday-2026-recap/` — "20+ major announcements", 1.2B weekly users), updated Model Spec.
- **Cybersecurity push:** cyber-at-the-frontier, /cybersecurity/, Daybreak customer stories (Check Point, Sophos, Cisco, Cloudflare, SentinelOne, Block), Daybreak Red on AWS GovCloud, bigger bug bounties, Patch the Planet coordinated disclosure, Grid Protectors Program, security sprint, Hacktron partnership, partners (Bishop Fox, SpecterOps, TrustedSec).
- **Acquisitions/people:** acquisition of Pierre Computer Company (Codex tooling), Orchestra Bio (drug development, with GPT-Rosalind); Dan Driscoll (Senior Counselor, national security modernization); Jill Hazelbaker (Chief Corporate Affairs Officer).
- **Partnerships:** OpenAI models on Google Cloud, Atlassian, ServiceNow, Oracle (apps in ChatGPT), Poland's NASK, Lenfest Institute.
- **Ads:** ChatGPT Ads expands to 26 countries (100k+ advertisers), new ads format/measurement, how the ad stack was built, Brazil ad terms, /ads/customers/*.
- **Enterprise customer stories** (~40): AT&T, Uber, Albertsons, Itaú, Franklin Templeton, Jump Trading, law firms (Sullivan & Cromwell, Ropes & Gray, Legora), etc.
- **Plugins:** ~16 new `/business/plugins/*` (Atlassian, Oracle NetSuite family, ServiceNow, WordPress, Krea, Litera…); /business/marketplace/, /business/private-intelligence/, /business/forward-deployed-engineering/.
- **Safety/engineering/research:** misalignment detection, safety cases for frontier training, securing training environment, model-distillation campaign disruption, "false front" operations, Scaling Git, storage for 1B users part II, wet-lab agent benchmark, math progress.
- **Policy:** EU text provenance, fair use, teens safety report, Australia commitments, EU agentic AI; policies: sign-in-with-ChatGPT terms, marketplace customer program terms, row-privacy-policy.
- Other: /codex-originals/, /compute-campus/, /economic-research-collaborators/, forms (Codex ambassadors, OpenAI on Google Cloud, Sign in with ChatGPT interest).

## Removals (16)
Partner pages canva, dropbox, gusto, hubspot, pathfindr, quickbooks, stripe (`/business/partners/*`); plugin pages atlassian-rovo, litera-lito, mcp-server-for-wordpress, oracle-analytics, wordpress-com (apparently renamed: atlassian, litera, wordpress, oracle-analytics-cloud added); `/daybreak/partners-new/`, `/economic-research-exchange/` (apparently renamed → `/economic-research-collaborators/`), `/form/ultrafast/`, `/prism/`. Last snapshots remain in git history.
