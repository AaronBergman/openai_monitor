# Run 2026-10-18T09-16Z — analysis

Fetch time: 2026-10-18T09:16:28Z (sitemap) + 1,236 pages fetched via `tools/html_to_md.py` (0 failures). Baseline: 2026-09-28T09-17Z — **a 20-day gap** (no runs 09-29 → 10-17), so everything below is cumulative over three weeks.

Totals: 2,063 URLs (was 1,985) across 43 sub-sitemaps (was 42). 82 added, 4 removed, 1,154 `<lastmod>` changes.

## Anomalies
1. **Observation gap**: 20 days unobserved. "Added" URLs carry `<lastmod>` values of Oct 1–17; first_seen is 2026-10-18 for all.
2. **New sub-sitemap `/sitemap.xml/learn-demos/`** (43rd). Holds 14 new `/business/learn/*` how-to demos (o3 workflows, strategic planning, GPT‑5 for work, market research, ChatGPT agent, canvas, image generation, Google Drive connector, Projects, GPT‑4o writing, vision & voice, IDE shipping, canvas prototyping, custom instructions), all stamped 2026-10-09 — evidently a batch migration/import of older tutorials into the new "Learn" hub (several reference GPT‑4o/o3, i.e. old content).
3. **220 sub-sitemap migrations** — a wholesale re-categorisation. Largest flows: company→global-affairs (35), product→release (25), plugins-legal→plugins-operations (12), company→product (11), safety→security (10), plugins-data-research→plugins-engineering-it (8), plugins-hr→plugins-operations (7), product→research (7), api→learn-openai-on-openai (6). Also `/news/` engineering→security, and several `api`/`ai-adoption` index posts moved to `learn-guides`, `startup`, `product`, `chatgpt`. Full list in diff.json.
4. **Missing `<lastmod>`**: `/index/introducing-gpt-6-1-sol/` (new) has no `<lastmod>` at all — the only such URL. It is already linked from the site-wide nav and the pricing page.
5. **Backdated new URLs (lastmod 11–17 days before first_seen; likely just the observation gap)**: `/form/sign-in-with-chatgpt-interest/` (10-07), `/policies/sign-in-with-chatgpt-terms/` (10-06), `/codex-originals/` (10-01), `/form/private-intelligence-interest/` (10-01).
6. **Reappeared URLs** (previously seen, absent from baseline): `/form/codex-ambassadors/` (first seen 2026-05-07), `/policies/row-privacy-policy/` (2026-05-07), `/business/plugins/alpaca/` (2026-07-10).
7. No future-dated or backwards-moving `<lastmod>`.

## Significant updates
- **Site-wide nav/footer change (1,151 pages)**: model menu now lists **GPT‑6.1 Sol** and **GPT‑6 Astra** (GPT‑5.4 dropped); header "Codex" link now points to chatgpt.com/codex; new **Dots** (chatgpt.com/features/dots) and **OpenAI Status** links. "Plugins" link reached ~458 more pages. 215 business pages gained an "OpenAI for Business updates" email-signup block.
- **`/codex/`** relaunched: "The same powerful coding agent—now in ChatGPT" → "Build anything with Codex", with plan cards (Plus $20/mo, Pro from $100/mo…) "Codex is included in your ChatGPT plan".
- **`/business/pricing/`**: GPT‑6.1 Sol / GPT‑6 Astra / GPT‑6 Sol rows added; Rosalind Academic Plan pointer; "personal plans" CTA replaced by "Chat with buying agent".
- **`/policies/cookie-policy/`** (Sep 10 → Oct 7): new cookies (`oai-logged-out-consent-chosen`, `oai_pl_permission_state`), `oai-did` lifetime 1y → 2y, new ads.openai.com cookies (`oai-did`, `oai-anon-id`, `marketing_consent_source`); Auth0 platform cookies removed.
- **`/policies/privacy-policy/`** (May 18 → Sep 10): Sora dropped from intro; wording on receiving data from advertisers changed from "may receive" to "receive" for measuring ad effectiveness.
- **`/policies/advertising-terms/`** (Aug 25 → Oct 15): Brazil customers now governed by new Brazil Advertising Terms; intermediary/reseller sections restructured (new "Advertiser Vetting" clause); "Optional Tools and Features" wording.
- **`/policies/sub-processor-list/`** (Jul 9 → Oct 14): Cloudflare entry expanded with region lists / data-residency wording.
- **`/trust-and-transparency/`**: transparency figures updated to Jan–Jun 2026 (e.g. one count 224→620); older per-period report links reorganised.
- **`/products/release-notes/`**: Oct 15–16 API entries: prompt-to-voice + nine GPT‑Live voices (German, French, Hindi, Japanese, Korean); native "Decisions" integration in GPT‑Live.
- **Homepage `/`**: hero cards changed from GPT‑6 Astra/Sol & Luna to "GPT‑6 and Intelligent UI for everyone" (Oct 7), "Sharing AI progress in mathematics" (Oct 6), "Introducing Dots" (Sep 29).
- **Legacy launch posts** (`learning-to-reason-with-llms`, `thinking-with-images`, `introducing-o3-and-o4-mini`, `introducing-deep-research`, `introducing-gpt-oss`, `chatgpt-study-mode`, `introducing-gpt-4-5`): rewritten/re-rendered with "This post introduced…" retirement banners (e.g. o1‑preview/o1‑mini retired from API; o1 deprecated) and "(opens in a new window)" link annotations. Content-hygiene pass on historical posts.
- **`/index/introducing-openai-frontier/`**: three customer case-study blocks (incl. State Farm quote) and some related-post cards removed.
- Many `/business/plugins/*` pages (netlify, mercury, firecrawl, vercel, notion…): tagline/permission text edits ("Interactive, Write" → "Read, Write"), new deep-link install URLs (`chatgpt.com/plugins/plugin_…`), new file IDs.

## Routine updates
~730 pages changed beyond the shared nav (mostly carousel rotation, link annotations, image asset IDs); the rest are nav-only. Every one of the 1,154 updated pages differed from its prior snapshot, owing to the nav change.

## New pages (82)
- **Models/product**: `/index/introducing-gpt-6-1-sol/`, `/index/gpt-6-for-everyone/` (new GPT‑6 model for 1.2B+ users, Intelligent UI), `/index/introducing-dots/`, `/index/devday-2026-recap/`, `/devday/2026/`, `/index/new-chatgpt-ads-format-and-measurement/`, `/index/teens-learn-and-plan/` (College Planner for teens), `/index/introducing-the-rosalind-academic-plan/` (GPT‑Rosalind for academic labs), `/business/marketplace/`.
- **Policy**: `/policies/brazil-advertising-terms/`, `/policies/row-privacy-policy/`, `/policies/sign-in-with-chatgpt-terms/` (+ interest form).
- **Safety/global**: `/index/disrupting-ai-enabled-false-front-operations/`, `/index/how-we-will-do-better-for-australia/`, `/index/the-eus-next-chapter-in-ai-is-agentic/`, `/index/helping-small-businesses-put-ai-to-work/`, `/index/the-eternal-complement/`.
- **Customer stories (~20)**: Sullivan & Cromwell, Itaú, Grupo Boticário, Localiza, Benefit Street Partners, Block, SentinelOne, Sophos ("Daybreak" security product), Asana, Oracle, LegalOn, Radisson, Chatham, The Den, Jump Trading, Basis, Albertsons, Atlassian partnership, Lenfest.
- **Forms/community**: Codex Ambassadors, Codex Originals (+ page), computer-use research collaboration, Private Intelligence interest.
- **Partners**: Affinda (renamed from Pathfindr), MegazoneCloud, SpecterOps, TrustedSec, Bishop Fox (security consultancies tied to "GPT Cyber Models").
- **Plugins**: Jetpack, WordPress.com (`/business/plugins/wordpress/`), Spacefast, Sandstone, Alpaca (returned).
- **Learn**: 14 demos (above), GPT‑Live‑1 webinar, board guide to cybersecurity & AI.

## Removals (4)
- `/business/partners/pathfindr/` — renamed; replaced by `/business/partners/affinda/` ("Affinda (formerly Pathfindr)").
- `/business/plugins/wordpress-com/` and `/business/plugins/mcp-server-for-wordpress/` — superseded by `/business/plugins/wordpress/` and `/business/plugins/jetpack/`.
- `/form/ultrafast/` — form retired.
Last snapshots remain in git history.
