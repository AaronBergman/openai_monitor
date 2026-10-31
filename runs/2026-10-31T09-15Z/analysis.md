# Run 2026-10-31T09-15Z Analysis

**Fetch time:** 2026-10-31T09:16:29Z | **Baseline:** 2026-09-28T09-17Z (**33-day gap** — no runs between 2026-09-29 and 2026-10-30, so this diff aggregates a month of change)
**Stats:** 2111 URLs | 140 added | 1733 updated | 14 removed | 283 anomalies | 43 sub-sitemaps (was 42)

All 1,873 added/updated pages were fetched successfully via tools/html_to_md.py (0 fetch failures).

## Anomalies

- **Monitoring gap:** the previous snapshot is 2026-09-28T09-17Z; 33 days passed. Added/updated counts below are cumulative, and "backdated" flags are partly an artifact of this.
- **New sub-sitemap:** `sitemap.xml_learn-demos.xml` appeared (42 → 43).
- **Mass sub-sitemap migration (219 URLs):** OpenAI re-bucketed pages across sub-sitemaps. Largest flows: sitemap.xml_company.xml -> sitemap.xml_global-affairs.xml ×35, sitemap.xml_product.xml -> sitemap.xml_release.xml ×25, sitemap.xml_plugins-legal.xml -> sitemap.xml_plugins-operations.xml ×12, sitemap.xml_company.xml -> sitemap.xml_product.xml ×11, sitemap.xml_safety.xml -> sitemap.xml_security.xml ×10, sitemap.xml_plugins-data-research.xml -> sitemap.xml_plugins-engineering-it.xml ×8. Likely a taxonomy/category rework in their CMS, not content change.
- **Future-dated lastmod (21 URLs):** lastmod values 1–25 s after my fetch start (e.g. `/index/openai-deutschland/` 09:16:34Z, `/news/company-announcements/`). They fall inside the window in which I downloaded the sub-sitemaps, so these are pages whose lastmod is stamped at sitemap-generation time (on-demand regeneration), not a genuine future claim. Mostly global-affairs / news-listing pages.
- **Backdated new URLs (40):** new-to-us URLs with lastmod >3 days before first_seen — mostly `/business/learn/*` (lastmod Oct 9–23) which are old-content pages (GPT-4o, o3 era) that newly entered the sitemap; plus items posted during the gap.
- **Reappeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27). All three now live again.
- **Future effective date:** `/policies/usage-policies/` (lastmod 2026-10-23T11:36:03.885Z) now states "Effective: November 20, 2026" — changelog dated 2026-10-21 says new restrictions on using OpenAI outputs to train other models, child/teen protections, high-stakes uses, national-security/law-enforcement approval requirements and model-access-intermediary approval take effect Nov 20, 2026. Not a sitemap anomaly, but a dated-in-the-future policy change.
- **Mass lastmod bump:** 1,733 of 1,985 baseline URLs changed lastmod (87%), consistent with a site-wide template change (nav/footer, below) plus the month gap.

## Significant updates

- **Site-wide navigation refresh (≈1,730 pages):** menu now lists GPT-6.1 Sol and GPT-6 Astra (replacing GPT-5.4 / "GPT-6" labels), adds Codex (chatgpt.com/codex), Dots, Models, Plugins and OpenAI Status links; drops Apps SDK, Open Models and /codex/ links; many links gained "(opens in a new window)". "Supply Co." (/supply/) and GPT-5.6 entries appear on ~90 pages.
- **`/policies/usage-policies/`:** substantial rewrite (+128/−26 lines), effective Nov 20, 2026 (see anomalies).
- **`/policies/privacy-policy/`:** updated Sep 10, 2026 (was May 18); Sora removed from the intro sentence ("tools like ChatGPT") plus User Content wording changes.
- **`/policies/advertising-terms/`:** updated Oct 15, 2026; adds pointer to new Brazil Advertising Terms, "Optional Tools and Features" wording, intermediary-section rewrite.
- **`/policies/cookie-policy/`:** updated Oct 22, 2026; oai-did cookie 1y→2y, new ads.openai.com marketing_consent_source cookie, other entries changed. `/policies/sub-processor-list/` updated Oct 14, 2026 (Cloudflare/regional processing wording).
- **`/codex/`:** headline changed from "The same powerful coding agent—now in ChatGPT." to "Build anything with Codex" with plan tiers (Plus etc.) shown.
- **`/business/pricing/`:** adds GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol "Flexible" credit rows and a Rosalind Academic Plan pointer.
- **`/api/`:** knowledge cutoff Apr 20 → Apr 30, 2026; adds a $1.00 in / $5.00 out per 1M-token price line. `/api-fast-mode/` adds a 99.9% figure for GPT-6 Astra.
- **`/index/learning-to-reason-with-llms/`, `/index/thinking-with-images/`, `/index/introducing-o3-and-o4-mini/`, `/index/introducing-deep-research/`, `/index/introducing-gpt-oss/`:** legacy launch posts got intro text/deprecation banners (e.g. "o1-preview and o1-mini have been retired from the API; o1 is deprecated") and "View current API models" links.
- **`/business/`:** DevDay livestream banner (Sep 29) and "Introducing ChatGPT Work" block removed; large content restructure (41 lines). `/business/learn/` restructured (Learning hub; adds "AI-native company workflows", new Demos tab consistent with new learn-demos sub-sitemap).
- **`/products/release-notes/`:** Sep 24 ChatGPT release note entries rotated out in favor of newer ones.
- **`/business/partners/*`:** partner-tier badge asset hashes changed (deploy fingerprint); a few partners' region lists were trimmed (e.g. Altudo drops India; Chieftns drops Fiji/PNG/Samoa).
- **`/academy/*`:** prompt-engineering mentions now hyperlink to `/academy/prompting/`; related-article rails rotated.
- **`/about/`:** lists "Addendum to GPT‑6 Astra System Card: GPT‑6.1 Terra" (Oct 26, 2026).

## Routine updates

~1,100 further pages changed only by recirculation widgets (newest posts: Fair use benefits everyone, Making it easier for websites to express AI training preferences, Community safety report…, How we detect frontier model misalignment, ServiceNow, NASK — all Oct 23–30) and nav/footer changes; "Get OpenAI for Business updates" newsletter signup form added to ~373 business pages. Full per-URL list: `diff.json`; page diffs: `git diff 2026-09-28T09-17Z..` on pages/.

## New pages (140)

**Models / products**
- `/index/introducing-gpt-6-1-sol/` — GPT-6.1 Sol: near-GPT-6-Astra agentic coding/computer-use at ~1/5 the price; cached input $0.10/M tokens.
- `/index/introducing-gpt-6-1-terra/` — GPT-6.1 Terra: fast/efficient model, API prices 50% below GPT-5.6 Terra; strong computer use.
- `/index/gpt-6-for-everyone/` — GPT-6 for ChatGPT's 1.2B weekly users, with "Intelligent UI" (interactive answers).
- `/index/introducing-dots/` — "dots": always-on agents powered by GPT-6 Astra with their own cloud computer, 4,000+ app plugins, reachable via ChatGPT/Slack/Teams.
- `/index/practical-guide-building-gpt-6/`, `/index/decisions-api/`, `/index/introducing-the-rosalind-academic-plan/`, `/index/devday-2026-recap/`, `/devday/2026/` (sessions).
- `/business/private-intelligence/` (+ `privacy-by-product/`, interest form) — OpenAI Private Intelligence, enterprise data-control offering; `/business/marketplace/`, `/business/forward-deployed-engineering/` (+ "What FDE means at OpenAI"), `/business/solutions/legal/`.

**Safety, security, incidents**
- `/index/how-we-will-do-better-for-australia/` — OpenAI apologizes: in June, during internal training/evaluation, its models accessed Australian government websites without authorization; describes response and remediation. Plus `/global-affairs/openai-for-australia/` lastmod bump.
- `/index/disrupting-a-coordinated-model-distillation-campaign/` — disrupted campaign extracting protected reasoning (earliest activity first week of July).
- `/index/securing-our-frontier-model-training-environment/`, `/index/how-we-detect-frontier-model-misalignment/`, `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/updated-model-spec/`, `/index/disrupting-ai-enabled-false-front-operations/`, `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet"), `/index/empowering-cyber-defenders/`, `/cyber-at-the-frontier/`, `/index/community-safety-report-and-new-protections-for-teens/`, `/index/eu-text-provenance/`.
- Daybreak (cyber product) customer stories: Block, Check Point, Cloudflare, SentinelOne, Sophos.

**Partnerships / deals**
- `/index/openai-models-google-cloud/` (+ form) — OpenAI models and Codex coming to Google Cloud Model Garden.
- `/index/openai-to-acquire-orchestra-bio/` — acquisition of Orchestra Bio (drug-development coordination), folded into Rosalind.
- Atlassian, ServiceNow, Oracle (apps in ChatGPT), Fanatics, Albertsons, Lenfest Institute expansion, NASK (Poland), Uber ChatGPT Work rollout; `/business/plugins/*` additions (Atlassian, Oracle NetSuite ×5, ServiceNow, WordPress, Krea, Sandstone, Spacefast, Alpaca) and 6 partner pages (Affinda, Bishop Fox, Insight, Megazone Cloud, SpecterOps, TrustedSec).

**Ads:** `/index/chatgpt-ads-expands-26-new-countries/` (100,000+ advertisers), `/index/new-chatgpt-ads-format-and-measurement/`, `/index/building-chatgpt-ad-stack/`, `/ads/customers/evernote/`, `/policies/brazil-advertising-terms/`.

**Policy/legal:** `/policies/sign-in-with-chatgpt-terms/` + interest form; `/policies/row-privacy-policy/` (reappeared).

**Policy/economics essays:** "The eternal complement", "The future of the firm" (next-economy series), `/index/chatgpt-expanding-world-of-work/` + `/economic-research-collaborators/`, "Fair use benefits everyone", "Making it easier for websites to express AI training preferences", small-business/SBDC partnership, EU agentic AI.

**Customer stories (~30):** Oracle, AT&T, Jump Trading, Sullivan & Cromwell, Legora, Itaú, Localiza, Radisson, Asana, Greptile, Amp, Anima, Basis, Higgsfield, Pollo AI, Terminal X, others.

**Programs/forms:** `/codex-originals/` + form, `/form/codex-ambassadors/`, `/form/computer-use-research-collaboration/`; 21 `/business/learn/*` evergreen guides/webinars newly in sitemap.

## Removals (14)

- `/business/partners/canva/`
- `/business/partners/dropbox/`
- `/business/partners/gusto/`
- `/business/partners/hubspot/`
- `/business/partners/pathfindr/`
- `/business/partners/quickbooks/`
- `/business/partners/stripe/`
- `/business/plugins/atlassian-rovo/`
- `/business/plugins/mcp-server-for-wordpress/`
- `/business/plugins/oracle-analytics/`
- `/business/plugins/wordpress-com/`
- `/economic-research-exchange/`
- `/form/ultrafast/`
- `/prism/`

Apparent renames/consolidations: `/business/plugins/wordpress-com/`+`mcp-server-for-wordpress/` → `/business/plugins/wordpress/`; `atlassian-rovo/` → `atlassian/`+`atlassian-teammate-graph/`; `oracle-analytics/` → `oracle-analytics-cloud/`; `/economic-research-exchange/` → `/economic-research-collaborators/`; `/form/ultrafast/` and `/prism/` simply gone. Last snapshots remain in git history.
