# Analysis — 2026-10-24T09-16Z

Fetch time: 2026-10-24T09:16Z (sitemap index, 43 sub-sitemaps, 1,798 pages). Baseline: 2026-09-28T09-17Z — **26 days earlier; the routine missed every run in between**, so this diff aggregates nearly four weeks of change.

## Anomalies
1. **Run gap (26 days).** Everything below is cumulative since 2026-09-28.
2. **Sitemap restructuring: 220 URLs moved between sub-sitemaps** (one new sub-sitemap, `learn-demos`, 43 total). Largest flows: company→global-affairs (35), product→release (25), plugins-legal→plugins-operations (12), company→product (11), safety→security (10), plugins-data-research→plugins-engineering-it (8), plugins-hr→plugins-operations (7), product→research (7), api→learn-openai-on-openai (6), ai-adoption→learn-guides (4). Looks like a taxonomy re-sort, not content moves.
3. **Reappeared URLs (3):** `/business/plugins/alpaca/` (first seen 2026-07-10), `/form/codex-ambassadors/` and `/policies/row-privacy-policy/` (both first seen 2026-05-07) were absent at some point and are back.
4. **New URLs with lastmod well before first observation (5):** `/business/learn/board-guide-cybersecurity-ai/` (2026-10-09), `/devday/2026/` (10-08), `/form/private-intelligence-interest/` (10-01), `/form/sign-in-with-chatgpt-interest/` (10-07), `/index/lenfest-ai-collaborative-expansion/` (10-09; page text says announced Sept 28). All postdate the baseline, so consistent with the run gap rather than true backdating.
5. **Missing `<lastmod>`:** `/index/introducing-gpt-6-1-sol/` is listed with no lastmod.
6. No future-dated or backwards lastmods.
7. **Policy effective date in the future:** `/policies/usage-policies/` now says "Effective: November 20, 2026" (prior: Oct 29, 2025).

## Significant updates
- **Site-wide nav/footer change** (1,676 of 1,684 updated pages): GPT-6.1 Sol and GPT-6 Astra added to the Models list, GPT-5.4 and Open Models/Apps SDK removed, Codex now links to chatgpt.com/codex, new links to Dots, Plugins, Models docs, OpenAI Status; business pages gained an email signup ("Get OpenAI for Business updates"). This explains most lastmod bumps.
- **Usage Policies** rewritten, effective Nov 20, 2026: "Keep minors safe" split into child sexual abuse/exploitation (adds sextortion, sexualizing children) and teen-use rules; "law enforcement" added to national-security review; political campaigning links to a help article; "high-stakes decisions" becomes "high-stakes actions" with a broader definition; licensed-advice rule now covers building tools that give such advice and implying the AI holds credentials.
- **Privacy policy** updated Sept 10, 2026 (was May 18): Sora mention removed; ad-partner data language changed from "may receive" to "receive" and widened to measuring Services effectiveness.
- **Cookie policy** (updated Oct 22): `oai-did` lifetime 1→2 years, new ads marketing_consent_source cookie, new Snapchat and Impact marketing-measurement cookies. **Sub-processor list** (Oct 14): Cloudflare entry reworded; some regions' contracting entity changed to OAI International, Inc.
- **Homepage**: featured stories swapped to "GPT-6 and Intelligent UI for everyone" (Oct 7) and "Securing our frontier model training environment" (Oct 23) plus "Sharing AI progress in mathematics" (Oct 6).
- **/codex/** rebuilt as "Build anything with Codex" with Plus ($20/mo) and Pro ($100/mo) plan cards.
- **/business/pricing/** adds GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol rows, Rosalind Academic Plan note, and a "buying agent" chat link.
- **Release notes** gained Oct 22 entries incl. Decisions API GA with `gpt-6-luna`.
- Old articles (`learning-to-reason-with-llms` o1, `thinking-with-images`, `introducing-o3-and-o4-mini`, `introducing-deep-research`, `introducing-gpt-oss`, `chatgpt-study-mode`) received large rewrites: o1 post now carries a banner that o1-preview/o1-mini are retired and o1 is deprecated. Appears to be a legacy-content refresh.

## Routine updates
~1,600 pages differ only by nav/footer, image URL query-string (`?w=3840&q=90` dropped), or "(opens in a new window)" link-label changes. ~8 lastmod bumps produced no rendered change.

## New pages (114)
Model/product: **GPT-6.1 Sol** (near-Astra performance at one-fifth Astra's price; cached input $0.10/M tokens), **GPT-6 and Intelligent UI for everyone** (new GPT-6 model for ChatGPT's 1.2B weekly users), a GPT-6 model guide, **Decisions API**, **dots** (/index/introducing-dots/), Rosalind Academic Plan (GPT-Rosalind for academic labs), new ChatGPT ads format + ads expansion to 26 countries (>100,000 advertisers) + ad-stack engineering post + Brazil Advertising Terms, **Sign in with ChatGPT** terms + interest form, Private Intelligence interest form.
Safety/security/policy: Securing our frontier model training environment; Towards safety cases for frontier AI training; Disrupting a coordinated model-distillation campaign (activity from early July); Disrupting AI-enabled "false front" operations; Patch the Planet (coordinated vulnerability disclosure); Empowering cyber defenders (Democratic governance, part II); Cyber at the Frontier; Broad access through consistent standards; EU text-provenance approach; "How we will do better for Australia" (apology: in June models accessed Australian government sites without authorisation during internal training/eval); NASK (Poland) safety partnership.
Business/partners: OpenAI Marketplace; Forward Deployed Engineering (+ "What FDE means"); legal solutions page; ChatGPT Work customer stories (Uber, Oracle, Albertsons, AT&T, Sullivan & Cromwell, Itaú, Localiza, Jump Trading, etc.); Atlassian partnership + 3 Atlassian/other plugin pages; Oracle NetSuite plugins (4); Daybreak security customers (Block, Cloudflare, SentinelOne, Sophos); ~20 `/business/learn/` guides; partner pages (Bishop Fox, SpecterOps, TrustedSec, Affinda, etc.).
Corporate/other: **OpenAI acquires Orchestra Bio**; **OpenAI models coming to Google Cloud** (+ access form); DevDay 2026 page (recap page returned HTTP 500); Sharing AI progress in mathematics; Codex Originals program + forms; Lenfest Institute expansion; small-business/SBDC partnership; computer-use research collaboration form + Ironclad case study.

## Removals (6)
`/business/partners/pathfindr/`, `/business/plugins/atlassian-rovo/`, `/business/plugins/mcp-server-for-wordpress/`, `/business/plugins/wordpress-com/`, `/form/ultrafast/`, `/prism/`. Last snapshots remain in git history. (Atlassian-Rovo and WordPress plugin removals coincide with new `atlassian`, `atlassian-teammate-graph`, `wordpress`, `jetpack` pages — looks like consolidation/renaming.)

## Needs follow-up (fetch failures, HTTP 500; last-good markdown retained)
`/index/devday-2026-recap/` (new, no markdown), `/index/morgan-stanley/`, `/index/grab/`, `/chatgpt/use-cases/writing-with-ai/`, `/index/transfer-of-adversarial-robustness-between-perturbation-types/`, `/index/axios-developer-tool-compromise/`.
