# Run 2026-10-26T09-17Z

**Fetch time:** 2026-10-26T09:17:48Z (sitemap index + 43 sub-sitemaps; 1,820 pages fetched, 0 failures)
**Baseline:** 2026-09-28T09-17Z — **28 days earlier; 27 daily runs were missed.** All changes below are cumulative over the gap.

Totals: 2,093 URLs (was 1,985) · 114 added · 6 removed · 1,706 `<lastmod>` updates · 7 anomalies · 43 sub-sitemaps (was 42).

## Anomalies

1. **Coverage gap.** No snapshots for 2026-09-29 → 2026-10-25. Things announced inside the gap (e.g. dots on Sep 29, the DevDay 2026 recap, GPT-6 for everyone on Oct 7) appear here only as "added", and any page created and deleted within the gap is invisible.
2. **Reappeared URLs (3):**
   - `/business/plugins/alpaca/` — last seen 2026-09-24, dropped in the Sep 25 purge of 23 URLs, back with lastmod 2026-10-25T21:46Z (now in plugins-finance).
   - `/form/codex-ambassadors/` — last seen 2026-06-24, back with lastmod 2026-10-26T09:04Z (17 min before fetch). Pairs with new `/form/codex-originals/` (lastmod 09:02Z) and `/codex-originals/` (Oct 24): a Codex community/creator program appears to be launching.
   - `/policies/row-privacy-policy/` — last seen 2026-05-27, back with lastmod 2026-10-24.
3. **Missing `<lastmod>` on a new URL:** `/index/introducing-gpt-6-1-sol/` (the GPT-6.1 Sol launch post) has no lastmod in the release sub-sitemap — the only non-merch URL like this. Page fetched fine.
4. **Sub-sitemap migrations: 220 URLs** changed sub-sitemap. Largest flows: company→global-affairs 35, product→release 25, plugins-legal→plugins-operations 12, company→product 11, safety→security 10, plugins-data-research→plugins-engineering-it 8, plugins-hr→plugins-operations 7, product→research 7. Looks like a re-tagging of article categories (and of the plugin categories) rather than content changes.
5. **New sub-sitemap `learn-demos`** (14 URLs, all new `/business/learn/*` demo pages such as "Delegate work to ChatGPT agent").
6. No future-dated lastmods (latest: `/index/scaling-storage-one-billion-users-part-two/` at 09:17:31Z, 17 s before fetch — just published) and no backwards-moving lastmods. No new URL's lastmod predates the baseline fetch, so nothing is "backdated" relative to our observations.

## Significant updates

All 1,706 updated pages changed rendered content, but almost entirely through **site-wide template changes**, not edits:
- **Nav/footer overhaul on ~1,703 pages:** adds "GPT-6.1 Sol" and "GPT-6 Astra" model links, "Dots" (chatgpt.com/features/dots), "Plugins" (developers.openai.com/plugins), "Models" and "OpenAI Status" links; drops "GPT-5.4", "Open Models", "Apps SDK"; Codex link now points to chatgpt.com/codex/; many help-center links gain "(opens in a new window)".
- **"Get OpenAI for Business updates" email signup block** added to ~378 business pages.
- **Recirculation widgets** rotated: new cards (NASK partnership, frontier-training security, Patch the Planet, Uber, storage part II, cyber defenders) replace GPT-6 Sol/Luna and prompt-caching cards.
- Largest real-content diffs (by line count) are mostly layout re-renders of old posts (`learning-to-reason-with-llms`, `thinking-with-images`, `genebench-pro/case-studies`); not analyzed individually.

## New pages (114) — highlights

Models / products
- `/index/introducing-gpt-6-1-sol/` — GPT-6.1 Sol: near-GPT-6-Astra intelligence on agentic coding/computer use/professional work at one-fifth Astra's price; $10 in / $50 out per M tokens, cached input discounted heavily.
- `/index/gpt-6-for-everyone/` (Oct 7) — new GPT-6 model for ChatGPT's 1.2 B weekly users plus "Intelligent UI" (answers as interactive generated interfaces).
- `/index/introducing-dots/` (Sep 29) — "dots": always-on agents powered by GPT-6 Astra with their own cloud computer, 4,000+ app connections via plugins, reachable via ChatGPT/Slack/Teams; Microsoft Agent 365 tie-in.
- `/index/devday-2026-recap/`, `/devday/2026/` — DevDay recap: "20+ announcements" on agents, Codex, models.
- `/index/decisions-api/` — Decisions API for fast, cheap, focused decisions; pairs with GPT-Live voice.
- `/index/practical-guide-building-gpt-6/` — model guide for the GPT-6 family.
- `/index/introducing-the-rosalind-academic-plan/`, `/index/openai-to-acquire-orchestra-bio/` — life-sciences push (sponsored GPT-Rosalind access for labs; acquisition of Orchestra Bio, a drug-development coordination platform).

Ads
- `/index/chatgpt-ads-expands-26-new-countries/` (Oct 21) — ads now in 89 countries, 100,000+ advertisers in ~8 months; Free and Go plans only.
- `/index/new-chatgpt-ads-format-and-measurement/`, `/index/building-chatgpt-ad-stack/` — visual ad format, measurement, and an engineering write-up of the ad stack; plus `/policies/brazil-advertising-terms/`.

Safety / security / policy
- `/index/securing-our-frontier-model-training-environment/` (Oct 23) — hardened containment for training environments after red-teaming agents found sandbox escapes, novel internet paths and cross-task communication; references the July "Hugging Face incident"; training resumed with stronger defenses.
- `/index/towards-safety-cases-for-frontier-ai-training/` — argues safety cases should be required before continuing frontier RL runs.
- `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet"), `/index/empowering-cyber-defenders/` (democratic governance part II, "Cybersecurity 2.0 blueprint"), `/cyber-at-the-frontier/`, `/index/disrupting-a-coordinated-model-distillation-campaign/` (campaign since early July extracting protected reasoning), `/index/eu-text-provenance/` (text watermarking for EU rules), `/index/openai-nask-ai-safety-security-partnership/` (Poland's NASK), `/index/broad-access-through-consistent-standards/`.

Partnerships / customers
- `/index/openai-models-google-cloud/` — OpenAI models and Codex coming to Google Cloud Model Garden (+ `/form/openai-on-google-cloud/`).
- `/index/atlassian-partnership/` + 3 Atlassian plugin pages (replacing `atlassian-rovo`); Oracle NetSuite plugins (4); `/index/uber-chatgpt-work-rollout/` (30,000+ employees); ~25 customer/startup stories (Albertsons, Itaú, Radisson, Jump Trading, Sophos, SentinelOne, Anima…); 6 new partner pages (Bishop Fox, SpecterOps, TrustedSec — security firms; Affinda, Insight, Megazone).
- `/business/forward-deployed-engineering/`, `/index/forward-deployed-engineering-means/`, `/business/marketplace/`, `/business/solutions/legal/`, `/business/contact-sales-retail/`; 18 `/business/learn/*` demos/webinars.
- Other: `/index/sharing-ai-progress-in-mathematics/` (with $5 M to a Simons Foundation initiative), `/form/private-intelligence-interest/`, `/form/sign-in-with-chatgpt-interest/`, `/policies/sign-in-with-chatgpt-terms/`.

Full URL list: `diff.json`.

## Removals (6)
`/business/partners/pathfindr/`, `/business/plugins/atlassian-rovo/` (superseded by `/business/plugins/atlassian/`), `/business/plugins/mcp-server-for-wordpress/` and `/business/plugins/wordpress-com/` (superseded by new `/business/plugins/wordpress/`), `/form/ultrafast/`, `/prism/`. Last markdown stays in `pages/` and in git history.

## Fetch failures
None.
