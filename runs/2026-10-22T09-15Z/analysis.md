# Run 2026-10-22T09-15Z Analysis

**Fetch time:** 2026-10-22T09:16Z (sitemap) / pages through ~09:20Z  
**Baseline:** 2026-09-28T09-17Z — **24-day gap** (no runs 09-29 → 10-21), so this run's diff covers almost a month of change.  
**Stats:** 2081 total URLs | 101 added | 1664 updated | 5 removed | 43 anomalies listed (10 substantive + 33 fetch-window timestamp artifacts) | fetch failures: 0

## Anomalies

1. **Usage Policies carry a future effective date.** `/policies/usage-policies/` now says "Effective: November 20, 2026" (previously October 29, 2025) and the changelog lists an entry dated 2026-10-21: "clarify restrictions on using OpenAI models and outputs to train other models", plus new language on tailored licensed-professional advice and on national-security/law-enforcement use requiring OpenAI review. The policy was published ~4 weeks ahead of when it takes effect. (Not a sitemap anomaly; a content observation.) Likely linked to the new post about a coordinated model-distillation campaign (below).
2. **33 `lastmod_within_fetch_window` entries.** 33-ish pages (GPT‑5/5.3/5.4/5.5/5.6, GPT‑4/4.5, o3/o4‑mini, DALL·E 3, 4o image gen, gpt‑oss‑safeguard, etc.) have `<lastmod>` values 0–45 s after my run-start clock (09:16:29). Interpretation: these were regenerated/republished by OpenAI's CMS *while* the sitemap was being served — consistent with a site-wide template rebuild in progress (see nav change below). Strictly "later than fetch start", but not a real future claim.
3. **7 backdated new URLs** (lastmod 12–21 days before first_seen, expected given the 24-day gap in my observations, so mostly benign): `/business/learn/board-guide-cybersecurity-ai/` (10‑09), `/codex-originals/` (10‑01), `/devday/2026/` (10‑08), `/form/private-intelligence-interest/` (10‑01), `/form/sign-in-with-chatgpt-interest/` (10‑07), `/index/basis-tax-workbook-with-astra/` (10‑09), `/index/lenfest-ai-collaborative-expansion/` (10‑09).
4. **3 reappeared URLs:** `/business/plugins/alpaca/` (last seen 2026‑09‑24, gone, back), `/form/codex-ambassadors/` (last seen 2026‑06‑24), `/policies/row-privacy-policy/` (last seen 2026‑05‑27).
5. No backwards `<lastmod>` moves detected. No sub-sitemap migrations were checked beyond what the script reports (none flagged).

## Significant updates

- **Site-wide navigation/footer refresh (1,664 of 1,664 updated pages).** Every updated page changed in the shared header/footer: footer now links GPT‑6.1 Sol, GPT‑6 Astra, Dots (chatgpt.com/features/dots), Codex (now chatgpt.com/codex/ instead of /codex/), Plugins (developers.openai.com/plugins), Models, and OpenAI Status; removed Open Models, Apps SDK, and older model links (GPT‑5.4 etc.). Header menu also gained spacing/markup changes. This explains why essentially the whole sitemap's lastmod advanced. A handful of pages were identical apart from this (e.g. old model posts, ~1,600 pages).
- **Usage Policies** (`/policies/usage-policies/`): see anomaly 1.
- **Privacy / ads policies:** `/policies/privacy-policy/` "Last updated" Sep 10 → Oct 7, 2026 and reworded advertiser-data language ("We receive information from advertisers and other data partners…"). Another policy moved Jul 9 → Oct 14, 2026. `/policies/supplier-code/` got a substantive rewrite (anti-corruption incl. facilitating payments, new sanctions/export-controls clause, risk-based management-system requirement, grievance language removed from bullet list).
- Other policy pages (cookie, professional-services/supplier security measures, EU services privacy, May‑2025 business terms, advertising terms) show large line counts mostly from the nav change and reformatting.
- `/business/learn/` index and `/business/pricing/`, `/business/customer-stories/`, `/solutions/industries/{financial-services,retail}/`, `/codex/`, `/products/release-notes/` changed in content as well as nav (new learn items, customer stories).

## New pages (101)

**Models / products**
- `/index/introducing-gpt-6-1-sol/` — GPT‑6.1 Sol: near GPT‑6 Astra capability on agentic coding/computer use at ~1/5 Astra's price; cached input $0.10/M tokens.
- `/index/gpt-6-for-everyone/` — GPT‑6 model for all ChatGPT users (1.2B weekly) with "Intelligent UI" (interactive answers).
- `/index/practical-guide-building-gpt-6/` — model guide for the GPT‑6 family.
- `/index/introducing-dots/` — "dots": persistent agents on GPT‑6 Astra with own cloud computer, connected to 4,000+ apps via plugins, reachable via ChatGPT/Slack/Teams. Footer link also added.
- `/index/devday-2026-recap/`, `/devday/2026/` — DevDay 2026 (20+ announcements) recap and sessions page.
- `/index/chatgpt-ads-expands-26-new-countries/`, `/index/new-chatgpt-ads-format-and-measurement/`, `/index/building-chatgpt-ad-stack/` — ChatGPT ads expansion (100k+ advertisers), new formats/measurement and a technical write-up; `/policies/brazil-advertising-terms/` added.
- `/policies/sign-in-with-chatgpt-terms/`, `/form/sign-in-with-chatgpt-interest/` — Sign in with ChatGPT program; `/form/private-intelligence-interest/` — "Private Intelligence" interest list.
- `/business/marketplace/` — OpenAI Marketplace: spend existing OpenAI commitment on partner products. Plus plugin pages (Alpaca, Atlassian, Atlassian Teamwork Graph CLI, Jetpack, Sandstone, Spacefast, WordPress.com) and partner pages (Affinda, Bishop Fox, Insight, MegazoneCloud, SpecterOps, TrustedSec).
- `/codex-originals/`, `/form/codex-originals/`, `/form/codex-ambassadors/` — Codex community programs.

**Partnerships / corporate**
- `/index/openai-models-google-cloud/`, `/form/openai-on-google-cloud/` — OpenAI frontier models and Codex coming to Google Cloud Model Garden.
- `/index/atlassian-partnership/` — Atlassian expansion (ties to new Atlassian plugin pages).
- `/index/openai-to-acquire-orchestra-bio/` — acquisition of Orchestra Bio (biopharma program coordination) folded into Rosalind life-sciences effort; `/index/introducing-the-rosalind-academic-plan/`, `/index/scaling-ai-research-for-complex-biological-data/`.
- `/index/lenfest-ai-collaborative-expansion/`, `/index/how-we-will-do-better-for-australia/`, `/index/the-eus-next-chapter-in-ai-is-agentic/`, `/index/eu-text-provenance/`, `/index/broad-access-through-consistent-standards/`, `/index/empowering-cyber-defenders/` (Democratic governance of frontier AI, part II), `/index/towards-safety-cases-for-frontier-ai-training/`.

**Security**
- `/index/disrupting-a-coordinated-model-distillation-campaign/` — OpenAI disrupted a campaign (earliest activity first week of July) extracting protected reasoning from its models; related to the Usage Policies change.
- `/index/disrupting-ai-enabled-false-front-operations/` — threat report on influence ops.
- `/index/coordinated-disclosure-of-critical-vulnerabilities/` — "Patch the Planet": critical PHP vulnerabilities found by Calif using GPT‑5.6 Sol; PHP checker released as a Codex skill.
- Customer security stories: Cloudflare, Sophos, SentinelOne, Block.

**Customer stories (~35):** Albertsons, AT&T legal, Amp, Asana (76x model-cost cut with GPT‑6.1 Sol), Basis, Benefit Street Partners, Chatham, Grupo Boticário, Higgsfield, Itaú, Jump Trading, LegalOn, Localiza, Oracle, Pollo AI, Radisson, Stack Overflow, Sullivan & Cromwell, Ted Taylor restaurant, Terminal X, The Den, Third Moment Research, Ironclad, plus `/business/solutions/legal/` and `/business/contact-sales-retail/`.

**Learning/other:** 19 `/business/learn/*` resource pages (backfill of older guides plus `gpt-live-1-webinar`, `board-guide-cybersecurity-ai`), `/index/teaching-students-to-think-and-learn-through-questions/`, `/index/teens-learn-and-plan/`, `/index/helping-small-businesses-put-ai-to-work/`, `/index/sharing-ai-progress-in-mathematics/`, `/index/low-resource-programming-languages/`, `/index/the-eternal-complement/`, `/form/computer-use-research-collaboration/`.

## Removals (5)
- `/business/partners/pathfindr/` — renamed: `/business/partners/affinda/` ("Affinda (formerly Pathfindr)") is new.
- `/business/plugins/atlassian-rovo/` — superseded by `/business/plugins/atlassian/` and `atlassian-teammate-graph`.
- `/business/plugins/wordpress-com/` and `/business/plugins/mcp-server-for-wordpress/` — superseded by `/business/plugins/wordpress/` (WordPress.com) and `/business/plugins/jetpack/`.
- `/form/ultrafast/` — form removed.
Last snapshots in git history.

## Fetch failures
None (1,765/1,765 pages fetched OK).

## Method notes
Baseline gap of 24 days means "added" includes pages published at any point 09‑29 → 10‑22; first_seen for all is 2026-10-22T09-15Z, not their true publication date. Page-level `known_urls.json` history entries use the {new, old, run_id} format.
