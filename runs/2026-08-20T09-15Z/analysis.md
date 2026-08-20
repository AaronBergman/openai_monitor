# Analysis — Run 2026-08-20T09-15Z

**Baseline:** 2026-08-19T09-16Z (consecutive day)
**Fetch time (root sitemap index + all 35 sub-sitemaps):** 2026-08-20T09:18:05Z UTC
**Sub-sitemaps fetched:** 35/35, no errors.
**Total URLs in union:** 1,601 (was 1,592)
**Page fetches attempted:** 156 (9 added + 147 updated). **Failures: 0** (9 needed a one-time `mkdir -p` for new directories, then succeeded).

## 1. Anomalies

None detected.

- No `<lastmod>` values later than fetch time.
- No `<lastmod>` values that moved backwards vs. the prior snapshot.
- All 9 newly-added URLs have `<lastmod>` within 1 day of first_seen (no backdating).
- No URL that disappeared in a prior run and reappeared today.
- No URL moved between sub-sitemap categories.

## 2. Significant updates (real content changes, ranked by importance)

### Ad Tools Data Processing Addendum rewritten — UK data transfers now handled separately from EEA/Swiss
**[`/policies/ad-tools-dpa/`](../../pages/openai.com/policies/ad-tools-dpa/index.md)** — effective date bumped from **June 12, 2026 → August 19, 2026**. This is a substantive legal restructuring, not a copyedit: previously all non-adequate-jurisdiction transfers relied on one set of EU Standard Contractual Clauses (SCCs) plus a "UK Addendum" bolted on for UK data. The new version splits responsibility by entity: **OpenAI Ireland Limited** now Processes EEA/Swiss Data directly, while **OpenAI OpCo, LLC** Processes UK Data under a dedicated **"UK SCCs"** framework (the EU SCCs as amended by the UK's International Data Transfer Addendum), with its own signature/effective-date mechanics, its own Annex I/Annex III appendix, and the UK Information Commissioner's Office named as the specific supervisory authority. Precedence order was also rewritten to add a new defined term "Advertising Terms" alongside the existing "Ad Tools Terms." Net effect: clearer, jurisdiction-specific compliance plumbing for OpenAI's advertising data-processing terms — likely a response to evolving post-Brexit UK transfer-mechanism requirements rather than a change in what data OpenAI collects or how.

### `/api/` landing page steers visitors toward ChatGPT instead of direct platform signup
**[`/api/`](../../pages/openai.com/api/index.md)** — the primary header/nav call-to-action changed from **"Start building"** (linking to `platform.openai.com` signup) to **"Try ChatGPT"** (linking to `chatgpt.com`) in both the top nav and mobile menu. Further down, a "Learn more" link near the agent-platform section switched from the internal `/agent-platform/` page to the external `developers.openai.com/api/docs/guides/agents` docs. This is a real, if small, positioning shift on OpenAI's flagship developer-facing page — the first click a new API visitor is nudged toward is now ChatGPT rather than platform sign-up.

### New Codex-focused ChatGPT for iOS release
**[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)** — new entry dated **Aug 18, 2026**: "ChatGPT for iOS updates: Codex Remote, MCP forms, and task reliability." Adds a setting to open ChatGPT directly into **Codex Remote** on launch, support for **standard MCP forms** and editable Messages approvals, voice support from existing task composers, and a string of reliability fixes (diff-review stability, task-list freezes, host-pairing). An older Aug 13 entry ("Updated model picker for Enterprise and Edu") rolled off the visible list as the page's rolling window advanced — it remains in git history.

### "Data Analytics" plugin quietly renamed to "Data" across Business solution pages
**[`/business/solutions/finance/`](../../pages/openai.com/business/solutions/finance/index.md)**, **[`/business/solutions/marketing/`](../../pages/openai.com/business/solutions/marketing/index.md)**, and **[`/business/solutions/operations/`](../../pages/openai.com/business/solutions/operations/index.md)** all changed references from "OpenAI's Data Analytics plugin" (and "Data Analytics and Product Design plugins") to simply "OpenAI's Data plugin" ("Data and Product Design plugins"). A small, consistent rebrand of a ChatGPT Work plugin name across at least three solution pages in one day — worth watching for a matching change on the plugin's own listing page in a future run.

### Business Operations webinar promo removed (event has passed)
**[`/business/solutions/operations/`](../../pages/openai.com/business/solutions/operations/index.md)** — the "Join us August 18, 2026 at 9:30 AM PT" webinar registration banner was removed now that the date has passed. Routine housekeeping, not a policy change.

## 3. Routine, low-signal updates (dominant pattern this run — 137 of 147 updated pages)

Four sitewide/template patterns account for the overwhelming majority of today's updates, none representing real content changes to the hosting pages:

1. **"Keep reading" / related-articles carousel refresh (~50 pages).** Bottom-of-page card carousels rotated in yesterday's and today's new posts (Offering Zero Data Retention, Replit, ChatGPT Ads Europe, ChatGPT for Teens, Pacing Model Development, Partnering with CodeAI) in place of older cards (Dali Rajic CRO announcement, Testing ads in ChatGPT, Daybreak on AWS, Model ML, etc.). Expected daily churn from the recommendation algorithm, not an edit to the page's own content.
2. **Global nav/footer refresh (~15 pages, continuing from 2026-08-19).** Nav's "Latest Advancements" link updated from GPT-5.5/5.4/5.3-era entries to include **GPT-5.6**; footer gained **Customer Stories**, **Partner Network**, and **Supply Co.** links. This is the same sitewide template change flagged yesterday, still propagating to pages whose cache hadn't re-rendered yet (e.g. `/policies/data-processing-addendum/`, `/business/learn/gartner-2026-agentic-coding-leader/`, several `/form/*` pages).
3. **Non-breaking-space / non-breaking-hyphen / word-joiner cleanup (~25 `/form/*` pages, 7 explicitly, 25 nbsp-only).** A batch of intake/legal-request forms (Rosalind biodefense, Trusted Access for Cyber/Biology, Codex Labs, Showcase Submission, Copyright Disputes, etc.) had invisible Unicode characters (U+00A0 non-breaking space, U+2011 non-breaking hyphen, U+2060 word joiner) normalized to plain ASCII equivalents around "(opens in a new window)" links and hyphenated terms like "GPT-Rosalind." Zero visible/textual change — pure encoding cleanup, likely a CMS re-save pass.
4. **Deploy-ID cache-buster churn (58 pages).** Only the `dpl_...` query-string on partner-badge SVGs or similar assets changed — a deployment artifact with zero visible change.

Legal/policy documents checked for substantive text beyond the DPA above: `/policies/data-processing-addendum/` — nav/footer noise only, no textual change.

## 4. New pages (9)

- **[Offering Zero Data Retention for frontier models](../../pages/openai.com/index/offering-zero-data-retention-for-frontier-models/index.md)** (Company/Safety, Aug 19) — the most substantive new page. Previews **Private Safety Processing**: a system that lets OpenAI's automated safety monitoring look for risk *patterns across multiple related interactions* — something today's per-interaction ZDR-compatible systems can't do — while keeping customer content encrypted with customer-controlled keys and inaccessible to OpenAI personnel except a narrow "alert category/severity" signal. Framed as preserving Zero Data Retention commitments as frontier-model deployments get longer and more agentic. Currently testing with early customers (Glean, Databricks, Abridge, Microsoft quoted); broader rollout plus a technical white paper promised for September 2026. Cross-linked into nearly every other recent post's "keep reading" carousel today, explaining much of the routine churn in §3.
- **[Replit expands access to software creation with GPT‑5.6 Luna](../../pages/openai.com/index/replit/index.md)** (Startup/customer story) — Replit is launching "Free Mode," letting anyone build software without worrying about token costs, powered by the **GPT-5.6 Luna** model variant.
- **7 new OpenAI Supply Co. merch pages** under `/supply/product/`: [`26-openai-1-64-car`](../../pages/openai.com/supply/product/26-openai-1-64-car/index.md) ('26 OpenAI 1:64 diecast car), [`air-freshener`](../../pages/openai.com/supply/product/air-freshener/index.md), [`bumper-sticker-pack`](../../pages/openai.com/supply/product/bumper-sticker-pack/index.md), [`decal-hoodie`](../../pages/openai.com/supply/product/decal-hoodie/index.md), [`pit-crew-shirt`](../../pages/openai.com/supply/product/pit-crew-shirt/index.md), [`r-d-co-race-pin-pack`](../../pages/openai.com/supply/product/r-d-co-race-pin-pack/index.md), and [`trackside-hat`](../../pages/openai.com/supply/product/trackside-hat/index.md). All seven share a **motorsport / pit-crew theme** — diecast racecar, trackside hat, pit-crew shirt, race pins — a themed merch drop rather than one-off items, and continues the "Supply Co." storefront that first appeared in nav/footer links on 2026-08-18/19.

## 5. Removals

None this run (0 URLs removed from the sitemap).

## 6. Fetch failures

None persisted. 9 of the 156 targeted fetches initially failed with `FileNotFoundError` because their parent directories (`pages/openai.com/supply/product/*`, `pages/openai.com/index/replit/`, `pages/openai.com/index/offering-zero-data-retention-for-frontier-models/`) did not yet exist — all were brand-new pages. Directories were created and all 9 re-fetched successfully; final failure count is 0.
