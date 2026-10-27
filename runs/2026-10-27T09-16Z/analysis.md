# Run 2026-10-27T09-16Z

**Fetch time:** 2026-10-27T09:17:07Z (sitemap) + 1,827 pages fetched via curl-cffi, 0 failures.
**Baseline:** 2026-09-28T09-17Z — a **29-day gap** (no runs for Sep 29 – Oct 26), so this diff covers a full month.
Totals: 2,100 URLs (was 1,985) | 122 added | 1,705 updated | 7 removed | 43 sub-sitemaps (was 42; `learn-webinars` is new).

## Anomalies

1. **Six `<lastmod>` values later than our fetch time** (by 1–3 seconds): `/api/`, `/index/evaluating-chain-of-thought-monitorability/`, `/index/model-ml/`, `/index/mufg/`, `/index/oscar/`, `/signals/data/` all claim lastmod `2026-10-27T09:17:08–10Z` against our fetch at 09:17:07Z. They look like timestamps generated at request time (page regenerated on demand), not real edits.
2. **Usage Policies carry a future effective date.** `/policies/usage-policies/` now reads "Effective: November 20, 2026" (previously Oct 29, 2025) with a "Previous Version" link. See Significant updates.
3. **Three URLs disappeared and reappeared:** `/business/plugins/alpaca/` (last seen 2026-09-24; dropped in the Sep 25 purge, back now), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27, lastmod still 2026-03-06 → page came back with an old lastmod value, then content differs from stored copy).
4. **22 sub-sitemap membership changes**, mostly from a new `sitemap.xml/learn-webinars/` sub-sitemap that absorbed/duplicated `/business/learn/*` and webinar URLs (several moved out of `page` into `learn-webinars`/`learn-guides`; e.g. `/business/learn/how-our-sales-team-uses-chatgpt-work/` page→learn-webinars; `/business/learn/agent-security-enterprise/` page→learn-guides). `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` moved global-affairs→safety. Full list in diff.json.
5. **Observation gap:** the 29-day gap means "first_seen" for the 122 new URLs is only an upper bound; their lastmods (Oct 1 – Oct 27) show when they really appeared. 11 new URLs have lastmods before Oct 20 (e.g. `/devday/2026/` 2026-10-08, `/form/private-intelligence-interest/` 2026-10-01) — consistent with having been published during the gap, not backdating.
6. No backwards-moving lastmods.

## Significant updates

- **Site-wide navigation overhaul (all 1,705 updated pages).** Every refetched page differs in the global nav/footer: model list now leads with **GPT-6.1 Sol** and **GPT-6 Astra** (GPT-5.4 and "GPT-6" entries dropped); new links for **Dots** (chatgpt.com/features/dots), **Plugins** (developers.openai.com/plugins), **Models** and **OpenAI Status**; "Open Models" and "Apps SDK" links removed; Codex now points to chatgpt.com/codex; external links now labelled "(opens in a new window)". 378 pages gained a "Get OpenAI for Business updates" email-subscribe block. Since every URL's markdown changed, `<lastmod>` bump on all of them is real but mostly template-driven: ~875 pages have non-boilerplate diffs, most of which are rotating "latest posts" carousels.
- **Usage Policies rewritten (effective Nov 20, 2026).** Professional-advice rule narrowed to "building or offering AI tools that provide others with tailored advice … without licensed involvement", and may not imply the AI itself holds professional credentials; "national security … purposes" extended to "national security, law enforcement, or intelligence purposes"; the minors section was restructured ("Keep young people safe", with a dedicated child sexual abuse & exploitation item replacing granular bullets such as dieting/body-shaming/dangerous challenges for minors).
- **Privacy Policy updated Sep 10, 2026** (was May 18): Sora removed from the intro sentence; Memory wording ("Saved Memories"→"Memories"); advertiser/data-partner language strengthened ("We receive" rather than "may receive", purposes broadened to improving Services incl. ads for Free and Go users); export/delete bullets reshuffled.
- **Advertising Terms updated Oct 15, 2026** (was Aug 25): Brazil advertisers are governed by new **Brazil Advertising Terms** (`/policies/brazil-advertising-terms/`, new); the Ad Reseller Program Guide was removed and reseller/intermediary sections restructured (2.1 Authority, 2.2 Advertiser Vetting); "Optional Tools and Features" renamed.
- **Sub-processor list updated Oct 14, 2026** (was Jul 9): Cloudflare now lists regional processing for `us.api.openai.com`/`eu.api.openai.com` (Belgium, Denmark, Malaysia, New Zealand, Singapore etc.); Intercom and Confluent rows removed, Fivetran re-scoped.
- **`/codex/` relaunch:** title "Codex" → "Build anything with Codex"; new "Get started" pricing block (Plus $20/mo, Pro $100/mo, Codex included in ChatGPT plan).
- **`/business/pricing/`:** adds GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol, GPT-6 Luna as "Flexible" features, adds **Dots** (Business Premium/Enterprise), removes **Canvas** row; Rosalind Academic Plan callout.
- **Homepage `/`:** hero card changed from GPT-6 Astra to **Introducing GPT-6.1 Terra** (Oct 26); recent-posts carousel now includes GPT-6 and Intelligent UI for everyone, Securing our frontier model training environment.
- **Release notes (`/products/release-notes/`):** Oct 23 entries — workspace analytics (Usage/Insights) in Admin Console for Enterprise/Edu, 7-day grace period for personal-workspace migration; External access controls entry marked GA (was Preview).
- **Legacy-post retirement banners:** six o1/o3-era posts (`learning-to-reason-with-llms`, `introducing-o3-and-o4-mini`, `thinking-with-images`, o1 system card etc.) gained "This post introduced OpenAI o1…" banners stating o1-preview/o1-mini are retired, pointing to current API models.
- **`/form/codex-ambassadors/`** turned from an interest form into a **Codex Ambassador application** (requires work samples and a ~30s intro video).

## Routine updates

~830 other URLs changed only by nav/footer, plugin-page carousels (`/business/plugins/*`), webinar/customer-story widgets, and the pervasive "(opens in a new window)" label tweak. No per-page review warranted.

## New pages (122)

**Models / products**
- `/index/introducing-gpt-6-1-sol/` — GPT-6.1 Sol upgrade: near GPT-6 Astra on agentic coding/computer use at ~1/5 the price; cached input $0.10/M tokens. (Not in sitemap with lastmod yet — no `<lastmod>` on this and Terra.)
- `/index/introducing-gpt-6-1-terra/` — fast, cheap model with visual reasoning and computer use; API prices 50% below GPT-5.6 Terra.
- `/index/gpt-6-for-everyone/` — GPT-6 and "Intelligent UI" (visual/interactive responses) for all users.
- `/index/introducing-dots/` — "dots": persistent always-on agents on GPT-6 Astra with their own cloud computer, reachable via ChatGPT/Slack/Teams, ~4,000 plugin-connected apps.
- `/index/decisions-api/`, `/index/devday-2026-recap/` (20+ announcements), `/devday/2026/`.
- `/index/building-chatgpt-ad-stack/`, `/index/new-chatgpt-ads-format-and-measurement/`, `/index/chatgpt-ads-expands-26-new-countries/` (100,000+ advertisers), `/policies/brazil-advertising-terms/`.

**Security / safety / policy**
- `/index/disrupting-a-coordinated-model-distillation-campaign/` — OpenAI disrupted a campaign (earliest activity July) extracting protected reasoning, including by copying encrypted reasoning between conversations.
- `/index/securing-our-frontier-model-training-environment/`, `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet"), `/cyber-at-the-frontier/`, `/index/empowering-cyber-defenders/`, `/index/disrupting-ai-enabled-false-front-operations/`, `/index/openai-nask-ai-safety-security-partnership/`, `/index/eu-text-provenance/` (textGrain text watermarking for the EU AI Act), `/index/broad-access-through-consistent-standards/`.
- `/policies/sign-in-with-chatgpt-terms/` plus `/form/sign-in-with-chatgpt-interest/` — a new "Sign in with ChatGPT" program.

**Partnerships / deals**
- `/index/openai-models-google-cloud/` + `/form/openai-on-google-cloud/` — OpenAI frontier models and Codex coming to Google Cloud model garden / Marketplace.
- `/index/atlassian-partnership/` + 5 Atlassian/Oracle/WordPress plugin pages (Oracle NetSuite x5, Atlassian x2, WordPress, Alpaca, Sandstone, Spacefast).
- `/index/openai-to-acquire-orchestra-bio/` — acquisition of Orchestra Bio, folded into Rosalind (life sciences); `/index/introducing-the-rosalind-academic-plan/`.
- `/business/marketplace/` — OpenAI Marketplace: draw down OpenAI commitments on partner products.
- `/business/forward-deployed-engineering/` + `/index/forward-deployed-engineering-means/`; `/business/solutions/legal/`; security partner pages (Bishop Fox, SpecterOps, TrustedSec), plus Affinda, Insight, Megazone.

**Customer stories** (~40): Uber, Albertsons, Itaú, Sullivan & Cromwell, Block, Cloudflare, SentinelOne, Sophos, Jump Trading, Radisson, Oracle, Fanatics, Greptile, CodeRabbit, Higgsfield, etc.

**Other:** `/codex-originals/` + form, `/business/learn/*` (≈20 older guides/webinars newly indexed), `/index/teens-learn-and-plan/`, `/index/low-resource-programming-languages/`, `/index/sharing-ai-progress-in-mathematics/`, `/index/scaling-storage-one-billion-users-part-two/`, `/index/stack-overflow-chatgpt-plugin/`, `/index/the-eternal-complement/`.

## Removals (7)

`/prism/` (last lastmod 2026-09-15; Prism product page), `/form/ultrafast/` (Ultrafast mode signup — note new `/index/openai-cut-incident-investigation/` is an Ultrafast case story, suggesting Ultrafast shipped/became a product), `/business/partners/pathfindr/`, and plugin pages `/business/plugins/{atlassian-rovo,mcp-server-for-wordpress,oracle-analytics,wordpress-com}/` — replaced by `atlassian`, `wordpress`, `oracle-analytics-cloud` pages (renames). Last snapshots in git history.
