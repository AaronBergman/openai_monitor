# Run 2026-10-19T09-16Z Analysis

**Fetch time:** 2026-10-19T09:17:17Z (sitemaps); pages fetched immediately after via `tools/html_to_md.py` (0 failures)
**Baseline:** 2026-09-28T09-17Z — **a 21-day gap** (no runs between Sep 29 and Oct 18), so this run bundles three weeks of change.
**Stats:** 2063 URLs (was 1985) | 82 added | 1301 updated | 4 removed | 63 anomalies | 43 sub-sitemaps (was 42)

## Anomalies

1. **8 `future_lastmod`** — `chatham-financial`, `openai-support-model`, `hugging-face-incident-and-the-road-ahead`, `how-people-are-using-chatgpt`, `buy-it-in-chatgpt`, `accelerating-biological-research-in-the-wet-lab`, `hierarchical-text-conditional-image-generation-with-clip-latents`, `chatgpt-agent-system-card` (all `/index/`). Their `<lastmod>` is 0.3–3.7 seconds *after* my fetch time (2026-10-19T09:17:17Z), e.g. `…09:17:21.040Z`. That pattern (timestamps trailing the observation by seconds, 536 URLs stamped Oct 19) means lastmod is being stamped at sitemap-generation/render time, not at an edit. Low severity, but it confirms `<lastmod>` on a large share of URLs is not a reliable edit date today.
2. **Mass lastmod bump:** 1,301 of 1,985 baseline URLs changed lastmod; 536 of them today (Oct 19), 162 on Oct 8, 146 on Oct 15, 129 on Oct 9, 108 on Oct 14, 87 on Oct 17. Every one also had a real rendered difference — but nearly all from a **site-wide nav/footer rewrite** (below), not page-specific edits.
3. **3 `reappeared_url`:** `/business/plugins/alpaca/` (last seen 2026-09-24, back with lastmod Oct 8), `/form/codex-ambassadors/` (absent since June 24, back, lastmod Oct 16), `/policies/row-privacy-policy/` (absent since May 27, back, lastmod Oct 9).
4. **33 `backdated_new_url`** (new URL, lastmod >3 days before first_seen). 18 are `/business/learn/*` pages dated Oct 9 that are legacy content (GPT‑4o, o3, "ChatGPT agent", custom instructions…) — pages that clearly existed earlier in some form and were folded into the new Learning hub; the rest are Oct 1–9 posts we couldn't have seen during the gap. Mostly an artefact of the 21-day gap; the 18 `/business/learn/` ones are genuinely "old content, new URL".
5. **19 `sub_sitemap_migration`:** a new sub-sitemap `sitemap.xml_learn-webinars.xml` appeared and `sitemap.xml_learn-guides.xml` absorbed many pages. Moves: 6 `/business/learn/*` + 3 company webinar pages (`page`/`company`/`learn-guides` → `learn-webinars`); 7 `/index/*` pieces (`ai-adoption`/`applied-ai` → `learn-guides`, e.g. `builders-guide-to-gpt-5-6`, `managing-ai-investments-in-agentic-era`, `codex-maxxing-long-running-work`); 4 `global-affairs` → `global-affairs-news-listed`; and `disrupting-malicious-uses-of-ai-influence-campaign-russia` `global-affairs` → `safety`. Consistent with the Learning hub reorganisation.

## Significant updates

- **Site-wide nav/footer rewrite (1,298 pages).** Footer product list: `GPT-5.4` removed; `GPT-6 Astra` and **`GPT-6.1 Sol`** added; `Codex` now points to `chatgpt.com/codex/` instead of `/codex/`; new **Dots** link (chatgpt.com/features/dots) and **OpenAI Status** link; 594 pages added a **Plugins** link. "Latest posts" carousels rotated everywhere (Sol/Luna launch → Rosalind Academic Plan, Stack Overflow plugin, Atlassian, etc.).
- **`/codex/`** rebuilt as a plan-pricing landing page: "Build anything with Codex" — Plus ($20/mo), Pro ($100) tiers, "Codex is included in your ChatGPT plan" (was "The same powerful coding agent—now in ChatGPT").
- **`/business/pricing/`**: new rows for GPT‑6.1 Sol, GPT‑6 Astra/Sol/Luna ("Flexible" pricing for Business and Enterprise) and Dots (Business Premium).
- **Policies:** `/policies/supplier-code/` — Supplier Code of Conduct fully rewritten (previous version dated Oct 10, 2023; now "Updated Oct 15, 2026", new section structure). `/policies/privacy-policy/` (Sep 10, 2026 update: Sora reference dropped from intro; ad-data-partner language changed from "may receive" to "receive"). `/policies/cookie-policy/` (Oct 7, 2026: `oai-did` lifetime 1→2 years, new ads.openai.com cookies, Auth0 platform cookies removed). `/policies/advertising-terms/` (Oct 15: Brazil carve-out, intermediary terms restructured).
- **`/trust-and-transparency/`**: H1 2026 transparency numbers published — government content requests 224 → **620**, non-content requests 75 → 146 and 10 → 28 in sibling categories (per-period figures; see page); older 2023 report links dropped.
- **`/products/release-notes/`**: new Oct 15–16 API entries — prompt-to-voice custom voices (free to create) with nine new GPT‑Live voices (German, French, Hindi, Japanese, Korean) and native Decisions integration in GPT‑Live.
- **`/webmcp-challenge/`**: flipped from "10 days to explore WebMCP"/prize details to a winners showcase.
- **`/solutions/industries/financial-services/`**: replaced with "Frontier intelligence. Built for financial services" (GPT‑6 Astra, institution-data focus).
- **`/index/lowes/`**: rewritten as a case study with metrics ("answers millions of home improvement questions"; 300K associates).
- **`/research/index/`**: gained Oct 6–7 entries (GPT‑6 for everyone, October 2026 safety update, math results, Ironclad).
- **`/business/learn/`**: relaunched as a "Learning hub" (Guides / OpenAI on OpenAI / Webinars / Demos) with an email-signup block (216 pages carry a new "Get OpenAI for Business updates" form).
- **Plugin pages** (~90): refreshed install links (`chatgpt.com/plugins/…?install&prompt=…`), e.g. Netlify's tagline and capability tags changed ("Interactive, Write" → "Read, Write").
- Large re-diffs on old articles (`introducing-deep-research`, `introducing-o3-and-o4-mini`, `thinking-with-images`, `chatgpt-study-mode`, `genebench-pro/case-studies`) are extraction/layout churn (page sizes within ±3%), not substantive rewrites.

## Routine updates
Remaining ~1,000 updates are only nav/footer/carousel changes (see above) plus "(opens in a new window)" accessibility suffixes on external links.

## New pages (82)
- **Models/products:** [`/index/introducing-gpt-6-1-sol/`](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md) (no `<lastmod>` at all; available to Plus/Pro/Business/Enterprise/Edu in ChatGPT Work and Codex, API `gpt-6.1-sol`, $2/M input, $10/M output — confirmed by page text); `gpt-6-for-everyone` (GPT‑6 rolling out globally to all plans with "Intelligent UI"); `introducing-dots` (always-on agents with their own cloud computer, 4,000+ app connections, Microsoft Agent 365); `practical-guide-building-gpt-6`; `devday-2026-recap` (20+ announcements, 1.2B weekly users); `new-chatgpt-ads-format-and-measurement` (visual ads); `introducing-the-rosalind-academic-plan`; `teens-learn-and-plan` (College Planner for teens, teen AI council).
- **Safety/policy:** `disrupting-a-coordinated-model-distillation-campaign` (core cluster attributed to people associated with Moonshot AI/Kimi; attempts to extract protected reasoning); `disrupting-ai-enabled-false-front-operations` (Russia "Dark Clark", Iran "Bogus Bylines", others); `towards-safety-cases-for-frontier-ai-training`; `eu-text-provenance`; `the-eus-next-chapter-in-ai-is-agentic`; `how-we-will-do-better-for-australia`; `helping-small-businesses-put-ai-to-work` (America's SBDC); `sharing-ai-progress-in-mathematics` (results from an internal frontier model, Lean formalizations, $5M to a Simons Foundation initiative); `the-eternal-complement` (essay); `advancing-computer-use-with-ironclad`.
- **Customer stories (~25):** Asana, Albertsons, Atlassian, Block/Sophos/SentinelOne (OpenAI "Daybreak" security), Oracle, Jump Trading, Chatham, Itaú, Localiza, Grupo Boticário, Radisson, Sullivan & Cromwell, Amp, Higgsfield, Pollo AI, Third Moment Research, LegalOn, Basis, Benefit Street Partners, The Den, Stack Overflow, Lenfest.
- **Business:** `/business/marketplace/` (spend existing OpenAI commitment on partner products), partners Affinda (formerly Pathfindr), Bishop Fox, MegazoneCloud, SpecterOps, TrustedSec; plugins Alpaca, Jetpack, Sandstone, Spacefast, WordPress; 18 legacy `/business/learn/*` guides/videos; GPT‑Live‑1 webinar.
- **Programs/forms:** `/codex-originals/` + form, `/form/codex-ambassadors/`, `/form/computer-use-research-collaboration/`, `/form/private-intelligence-interest/`, `/form/sign-in-with-chatgpt-interest/`, `/policies/sign-in-with-chatgpt-terms/`, `/policies/brazil-advertising-terms/`, `/devday/2026/`.

## Removals (4)
- `/business/partners/pathfindr/` → replaced by `/business/partners/affinda/` (company renamed).
- `/business/plugins/wordpress-com/` → replaced by `/business/plugins/wordpress/`.
- `/business/plugins/mcp-server-for-wordpress/` — gone; WordPress presence now via `wordpress` and `jetpack`.
- `/form/ultrafast/` — form removed (Amp's story mentions "Ultrafast").
Last snapshots are in git history.

## Fetch failures
None (1,383 pages fetched, 0 blocked).
