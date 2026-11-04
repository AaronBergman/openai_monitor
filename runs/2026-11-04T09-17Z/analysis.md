# Run 2026-11-04T09-17Z Analysis

**Fetch time:** 2026-11-04T09:17:15Z (sitemap); pages fetched immediately after
**Baseline:** 2026-09-28T09-17Z — a **37-day gap**: the routine did not run (or commit) between Sep 29 and Nov 3, so this diff bundles ~5 weeks of change.
**Stats:** 2123 URLs | 152 added | 1734 updated | 14 removed | 112 raw anomaly flags (see below) | 43 sub-sitemaps | 0 fetch failures

Pipeline note: this run used a fresh scratch script (not the stale `run_daily.py`), writing fetches to a temp file first so blocked fetches never overwrite last-good markdown. `pip` and `python` pointed at different interpreters in this environment; deps were installed with `python -m pip`.

## Anomalies

1. **Unexplained 37-day gap in monitoring** (Sep 28 → Nov 4). Everything below is cumulative over that period; first_seen for all 152 "new" URLs is therefore recorded as this run, not the true publication date.
2. **future_lastmod ×52** — sitemap `<lastmod>` values later than our fetch start (09:17:15Z) by up to ~23 s (latest `2026-11-04T09:17:38.425Z`). Pattern is consistent with pages being regenerated/served live while the sitemap was being generated (lastmod ≈ "now"), not a true claim of future edits. Low signal but logged. Examples: `/index/cisco-cyber/`, `/index/forward-deployed-engineering-means/`, `/index/openai-on-oracle-cloud/`.
3. **backdated_new_url ×38** — new URLs whose lastmod is >3 days before our fetch. Largely an artifact of the 37-day gap (lastmods Oct 9–31 all fall inside the gap), so NOT evidence of backdating. Notable: `/devday/2026/` (lastmod 2026-10-31, page claims "this year we introduced…" — DevDay was Sep 29, so a post-event recap page was stood up a month later), `/business/learn/*` evergreen guides lastmod Oct 21–25 (likely a batch migration of library content into the sitemap).
4. **reappeared_url ×3** — `/business/plugins/alpaca/` (last_seen 2026-09-24), `/form/codex-ambassadors/` (last_seen 2026-06-24), `/policies/row-privacy-policy/` (last_seen 2026-05-27). Each vanished for weeks/months, then returned.
5. **sub_sitemap_migration ×19** — a reorganisation of the sitemap sections: ~11 URLs moved into `learn-guides` / `learn-webinars` (from `page`, `ai-adoption`, `applied-ai`, `company`, `global-affairs`), and ~6 from `global-affairs` into `global-affairs-news-listed`; plus `disrupting-malicious-uses-of-ai-influence-campaign-russia` moved `global-affairs` → `safety`. See diff.json.
6. **Future-dated policy**: `/policies/usage-policies/` now reads "Effective: November 20, 2026" (16 days after fetch) with a link to the previous Oct 29, 2025 version — i.e. new Usage Policies were published in advance of taking effect.

## Significant updates

- **Usage Policies rewritten (effective Nov 20, 2026).** Among changes: the "tailored advice requiring a license" clause now bans *building or offering AI tools that provide others* such advice without licensed-professional involvement, and bans stating/implying the AI itself holds professional credentials.
- **Privacy policy** (updated Sep 10, 2026, was May 18): Sora removed from the intro ("tools like ChatGPT"); advertiser/data-partner data language hardened from "may receive" to "receive", with use for ads to Free and Go users spelled out.
- **Cookie policy** (Oct 22, 2026, was Sep 10): `oai-did` retention 1→2 years, new `marketing_consent_source` cookie on ads.openai.com, help.openai.com added, several openai.com consent cookies and Auth0 platform cookies dropped from the table.
- **Sub-processor list** (Oct 14, 2026, was Jul 9): Cloudflare entry expanded with US/EU regional-processing notes (us.api / eu.api endpoints) and a long per-country region list.
- **Trust & transparency**: H1-2026 government-request stats added (e.g. 620 vs 224 prior-period figure; other counts 146, 28 replacing 75, 10), older 2023 reports dropped from the list.
- **Homepage**: lead cards switched from GPT-6 Astra / GPT-6 Sol & Luna to "Introducing GPT-6.1 Terra" (Oct 26, 2026).
- **/codex/** rebuilt as "Build anything with Codex" with Plus/Pro pricing tiers; **/business/pricing/** nav now lists GPT-6.1 Sol / GPT-6 Astra, adds Dots and a newsletter signup, drops GPT-5.4 and Apps SDK.
- **Archive banners on legacy model posts**: 7 pages (o1, o1-preview, o1-mini, o3-mini, o3/o4-mini, thinking-with-images, /o1/) gained "This post introduced…" notes saying the models are retired/deprecated, with links to current models — OpenAI is annotating old launch posts as historical.
- **/index/introducing-dots/** has an Nov 3, 2026 update: dots now also draw on GPT-6.1 Terra.
- **/products/release-notes/**: Oct 30, 2026 entry — GPT-6 Rosalind Research (life-sciences model) in Work, Codex and API for approved Business/Enterprise orgs.

## Routine updates

1734 URLs changed lastmod; none had zero rendered diff (fresh-fetch markdown differs from the stored copy, mostly from link-annotation churn such as "(opens in a new window)" suffixes, plus recirculation widgets). ~330 `/business/plugins/*` and ~70 `/business/partners/*` pages changed (template/nav updates and catalog edits). Not individually reviewed beyond sampling; diffs live in git (`git diff HEAD -- pages/`).

## New pages (152)

**Models & products:** `/index/introducing-gpt-6-1-sol/` (near-Astra agentic coding at ~1/5 price; cached input $0.10/M), `/index/introducing-gpt-6-1-terra/` (fast model, 50% cheaper than GPT-5.6 Terra, strong computer use), `/index/gpt-6-for-everyone/` (GPT-6 for all ChatGPT users with "Intelligent UI"; >1.2B weekly users claimed), `/index/practical-guide-building-gpt-6/`, `/index/decisions-api/` (GA; built on GPT-6 Luna), `/index/devday-2026-recap/`, `/devday/2026/`, `/index/updated-model-spec/` (Model Spec reorganised around five values), `/index/introducing-the-rosalind-academic-plan/`.
**Corporate / people:** Jill Hazelbaker as Chief Corporate Affairs Officer (ex-Uber), Dan Driscoll as Senior Counselor for National Security Modernization, `/index/openai-to-acquire-orchestra-bio/` (acquisition tied to Rosalind life-sciences).
**Partnerships:** OpenAI models on Google Cloud Model Garden (`/index/openai-models-google-cloud/`, `/form/openai-on-google-cloud/`), Oracle apps in ChatGPT, ServiceNow & Atlassian expansions, Poland's NASK safety partnership, `/business/marketplace/` (spend OpenAI commitment on partner products).
**Security/safety cluster:** `/index/disrupting-a-coordinated-model-distillation-campaign/` (campaign extracting "protected reasoning", earliest activity first week of July), `/index/disrupting-ai-enabled-false-front-operations/`, `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet"), `/index/securing-our-frontier-model-training-environment/`, `/index/rewarding-defenders-with-bigger-bug-bounties/`, `/index/grid-protectors-program/`, `/index/how-we-detect-frontier-model-misalignment/`, `/index/towards-safety-cases-for-frontier-ai-training/`, Daybreak customer stories (Check Point, Cisco, Cloudflare, Sophos, SentinelOne), `/cyber-at-the-frontier/`.
**Ads:** `/index/building-chatgpt-ad-stack/`, `/index/chatgpt-ads-expands-26-new-countries/` (100k+ advertisers), `/index/new-chatgpt-ads-format-and-measurement/`, Brazil advertising terms, Evernote ads story.
**Enterprise:** `/business/private-intelligence/` + interest form, `/business/forward-deployed-engineering/` + `/index/forward-deployed-engineering-means/`, `/business/solutions/legal/` with legal customer stories (Sullivan & Cromwell, Ropes & Gray, Legora, AT&T), ~20 customer stories, ~21 `/business/learn/*` webinar/guide pages, 15 new plugin pages (Oracle NetSuite family, Atlassian, ServiceNow, WordPress, Krea, Spacefast…), 6 new partner pages (Affinda, Bishop Fox, SpecterOps, TrustedSec, MegazoneCloud, Insight).
**Other:** Codex Originals / Ambassadors, `/index/introducing-dots/` already existed (updated), Sign in with ChatGPT terms + interest form, `/policies/row-privacy-policy/`, `/index/eu-text-provenance/`, `/index/fair-use-benefits-everyone/`, teen-safety posts, `/index/scaling-git-at-openai/`, `/index/scaling-storage-one-billion-users-part-two/`.

## Removals (14)

Last snapshots are in git history. Several look like renames/consolidations rather than deletions:
- `/business/partners/pathfindr/` → `/business/partners/affinda/` ("Affinda (formerly Pathfindr)").
- `/business/plugins/oracle-analytics/` → `/business/plugins/oracle-analytics-cloud/`; `/business/plugins/atlassian-rovo/` → `/business/plugins/atlassian/`; `/business/plugins/wordpress-com/` → `/business/plugins/wordpress/`.
- `/form/ultrafast/` → `/index/openai-cut-incident-investigation/` (Ultrafast story).
- `/economic-research-exchange/` → `/economic-research-collaborators/`.
- Genuine drops (no obvious successor): partner pages for Canva, Dropbox, Gusto, HubSpot, QuickBooks, Stripe; plugin `/business/plugins/mcp-server-for-wordpress/`; `/prism/`.

## Fetch failures

None.
