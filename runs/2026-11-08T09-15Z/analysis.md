# Run 2026-11-08T09-15Z — analysis

Fetch time: 2026-11-08T09:16:18Z. Baseline: 2026-09-28T09-17Z — **41 days earlier** (the routine did not run Sep 29 – Nov 7), so this run folds six weeks of change into one diff. 2,141 URLs now vs 1,985 (172 added, 16 removed, 1,732 `<lastmod>` changes), 43 sub-sitemaps (was 42). All 1,904 added/updated pages fetched OK (0 failures); 1,735 produced different markdown, 169 are new files.

## Anomalies
1. **Mass sub-sitemap reshuffle (220 URLs migrated).** Largest flows: company→global-affairs (35), product→release (25), company→product (11), plugins-legal→plugins-operations (11), safety→security (10), plugins-data-research→plugins-engineering-it (8). Also a new sub-sitemap `learn-demos` (14 new URLs). Suggests OpenAI re-categorised content-type taxonomy, e.g. security posts moved out of safety and into a dedicated security bucket, plugin category re-bucketing.
2. **Gap-driven bulk `<lastmod>` bump.** 1,227 of the 1,732 updated URLs now carry a November 2026 lastmod (503 October). Nearly all of the site re-stamped because the global header/footer changed (see below) — so lastmod ≠ editorial change. Only ~637 pages have any diff beyond nav/footer/recirculation cards.
3. **Reappeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (previously absent from sitemap since ~2026-06-24), `/policies/row-privacy-policy/` (absent since 2026-05-27).
4. **New URLs with no `<lastmod>` (5):** `/ads/customers/{evernote,flipsnack,vistaprint}/`, `/index/introducing-gpt-6-1-sol/`, `/index/introducing-gpt-6-1-terra/`.
5. **Page-internal dates older than first_seen:** several new articles carry publish dates inside the gap (e.g. Introducing dots Sep 29, DevDay 2026 Recap Sep 29, distillation-campaign post Sep 30, Orchestra Bio acquisition Oct 20, Google Cloud Oct 21, Model Spec update Oct 29). Explained by the missed runs; they first appeared in the sitemap only in this snapshot's window or were re-stamped. No future-dated or backwards `<lastmod>` values.
6. **Forward-dated policy:** `/policies/usage-policies/` now says "Effective: November 20, 2026" (previous version Oct 29, 2025) — a future-effective policy rewrite published ahead of time.

## Significant updates
- **Global nav/footer change on all 1,732 pages:** GPT-5.4 link replaced by GPT-6.1 Sol and GPT-6 Astra; Codex link now points to chatgpt.com/codex; new links to Plugins, Models, OpenAI Status and Dots (chatgpt.com/features/dots); Open Models and Apps SDK links dropped.
- **Usage Policies** rewritten (effective Nov 20, 2026): e.g. now prohibits building/offering AI tools that give licensed-profession advice without a licensed professional and bars stating/implying the AI holds professional credentials.
- **Privacy policy** updated Sep 10, 2026 (Sora dropped from the intro; ad-partner data language changed from "may receive" to "receive" and widened to improving Services). **Cookie policy** updated Oct 22, 2026 (`oai-did` lifetime 1→2 years; new ads.openai.com `marketing_consent_source` cookie; Auth0 cookie rows removed).
- **Trust & transparency report** now shows Jan–Jun 2026 figures: 620 (was 224), 146 (was 75), 28 (was 10) in the three headline counts — large increases.
- **Business pricing:** Rosalind Academic Plan link; a tier now described as "More usage" (was "5x more usage"); notice that **from December ChatGPT and Codex share one plan usage limit**.
- **/codex/** relaunched as "Build anything with Codex" with Plus ($20/mo) and Pro ($100/mo) plan tiers.
- **/daybreak/** reframed from "$1 billion in Daybreak credits for defenders" to a broader cybersecurity-program page (agentic defense loop: inventory, discover, validate, assign, remediate, prove; Codex Security, GPT Cyber models, Patch the Planet).
- **/business/** homepage promo changed from DevDay livestream/ChatGPT Work to "Cyber at the Frontier" keynote (Nov 12, 10 AM PST), Private Intelligence, GPT-6.1 Terra.
- **Release notes** now lead with Nov 5 GPT-6-Cyber for authorized vulnerability research.
- Plugin pages (≈100) picked up template changes (30–45 diff lines each).

## New pages (172) — themes
- **Models:** GPT-6.1 Sol ("near-Astra intelligence for a fifth of the price", cached input $0.10/M), GPT-6.1 Terra (fast visual reasoning/computer use), GPT-6 Cyber (Nov 5), Images 2.6, Decisions API, a GPT-6 model guide, "GPT-6 and Intelligent UI for everyone", Introducing dots.
- **Cyber push:** `/cyber-at-the-frontier/`, `/cybersecurity/`, Patch the Planet coordinated disclosure, Hacktron partnership, bigger bug bounties, security sprint, securing frontier training environment, Grid Protectors Program, Daybreak Red on AWS GovCloud, partner/customer stories (Cisco, Cloudflare, Sophos, SentinelOne, Check Point, Block), new security partners (Bishop Fox, SpecterOps, TrustedSec).
- **Enterprise/commercial:** OpenAI Marketplace (spend OpenAI commitment on partner products) + Marketplace terms; Private Intelligence (+ interest form, privacy-by-product); forward-deployed engineering; `/business/solutions/legal/`; ≈25 customer stories; partnerships with Atlassian, ServiceNow, Oracle (apps in ChatGPT), and **OpenAI models on Google Cloud** (+ access form).
- **Ads:** ChatGPT Ads expands to 26 countries (100k+ advertisers), new ad format/measurement, how the ad stack was built, Brazil ad terms, 3 ads customer stories.
- **Corporate:** acquisitions of Orchestra Bio (drug development) and Pierre Computer Company (Codex tooling); Jill Hazelbaker named Chief Corporate Affairs Officer; Dan Driscoll Senior Counselor for National Security Modernization; NASK (Poland) safety partnership; compute campus page; Australia commitments; EU text-provenance and EU agentic posts.
- **Safety/policy/research:** updated Model Spec, model-distillation campaign disruption, false-front influence-operation disruption, misalignment detection, safety cases for frontier training, community safety report & teen protections, math progress, wet-lab agent benchmark, thousands-of-agents biology work, Rosalind academic plan.
- **Learning:** 14 `learn-demos`; `/business/learn/*` pages (older ChatGPT how-tos relocated/re-created).
- **Other:** Codex Originals/Ambassadors forms, Sign in with ChatGPT terms + interest form, computer-use research collaboration form, DevDay 2026 page and recap, Economic Research Collaborators.

## Removals (16)
Mostly renames/restructures: `/business/partners/{canva,dropbox,gusto,hubspot,pathfindr,quickbooks,stripe}/` (Pathfindr → `/business/partners/affinda/`); plugin slugs `atlassian-rovo`→`atlassian`, `litera-lito`→`litera`, `oracle-analytics`→`oracle-analytics-cloud`, `wordpress-com`→`wordpress`, `mcp-server-for-wordpress`; `/daybreak/partners-new/`; `/economic-research-exchange/` → `/economic-research-collaborators/`; `/form/ultrafast/`; `/prism/` (LaTeX workspace). Last snapshots in git history.
