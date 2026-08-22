# Run 2026-08-22T09-17Z — Analysis

**Fetch time (ours):** 2026-08-22T09:17:16Z UTC
**Baseline:** 2026-08-21T09-16Z (consecutive day)
**Sub-sitemaps:** 36 (unchanged count from prior run)
**Totals:** 1,606 current URLs (1,604 baseline) | +2 added | 60 lastmod-updated | 0 removed

All 62 added/updated pages fetched successfully via `tools/html_to_md.py` (curl-cffi + Chrome impersonation). No fetch failures this run.

## Anomalies

None found.

- No `<lastmod>` later than fetch time (2026-08-22T09:17:16Z).
- No `<lastmod>` moved backwards vs. `state/known_urls.json` history for any URL.
- Both new URLs (`business/partners/quantium/`, `business/partners/tcs/`) have `<lastmod>` values same-day as their `first_seen` (2026-08-22T08:57:16Z and 2026-08-22T08:14:23Z respectively) — not backdated.
- No disappeared-then-reappeared URLs (0 removed this run).
- 4 URLs moved sub-sitemap category from `global-affairs` → `global-affairs-news-listed` (see below) — this is a **recurring, not new**, migration: `state/known_urls.json` shows these same 4 URLs (all present since bootstrap) have flip-flopped between these two category sitemaps across multiple prior runs (first flagged 2026-08-19, recurring here). Treated as a routine/unstable backend categorization quirk, not a content anomaly.

## Significant updates

### GPT-5.6 Sol price cut (promotional, ≥20% for 3 months)

- **[`/index/gpt-5-6/`](../../pages/openai.com/index/gpt-5-6/index.md)** — new changelog line: *"Update on August 21, 2026: OpenAI dropped the API and credit pricing of GPT‑5.6 Sol by over 20% for the next 3 months."*
- **[`/api/`](../../pages/openai.com/api/index.md)** — the pricing table for the featured model dropped from **$5.00 input / $30.00 output** per 1M tokens to **$4.00 input / $20.00 output** (a 20%/33% cut respectively), with new footnotes: *"Pricing above reflects standard processing rates for context lengths under 270K"* and *"GPT‑5.6 Sol's promotional pricing is available at least through November 21, 2026"* (three months from the Aug 21 announcement, consistent with the gpt-5-6 changelog note).
- Same page's top CTA flipped back from "Try ChatGPT" to **"Start building"** — this is at least the third flip of this specific A/B test observed in the last week (flagged 2026-08-18, 2026-08-20, now 2026-08-22).

### Two new Partner Network members: Quantium (Select) and TCS (Elite)

- **[`/business/partners/quantium/`](../../pages/openai.com/business/partners/quantium/index.md)** (new page) — Quantium, an Australian AI/data-analytics company (~1,200 people, 13 locations, founded 2002), joins as a **Select Partner**. Serves Australia, New Zealand, UK, US, India, South Africa.
- **[`/business/partners/tcs/`](../../pages/openai.com/business/partners/tcs/index.md)** (new page) — Tata Consultancy Services joins as an **Elite Partner**, tied to a Tata Group–OpenAI "foundational partnership" press release (global scope). This is the highest partner tier.
- **[`/business/partners/`](../../pages/openai.com/business/partners/index.md)** — partner directory grid updated to list both new logos (Quantium, TCS) in the relevant sections.

### Codex/ChatGPT product changelog — two new entries

- **[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)** picked up two new dated entries:
  - **Aug 20, 2026 (GA)** — "Codex and ChatGPT updates: Apple Messages, Sites, sharing, and pinned threads": new Apple Messages plugin (macOS desktop app, read/search Messages, prepare/send with approval gating), Site co-editing for workspace members, editable Site URLs (old address redirects), shareable read-only Codex thread snapshots (with secret redaction, but "review before sharing" caveat), and unified pinned-thread state across desktop and iOS.
  - **Aug 19, 2026 (Beta)** — "GitLab support in Codex cloud": connect a GitLab project, create environments, trigger tasks via `@codex` from issues/MRs, request one-off or automatic MR reviews. Requires GitLab 19.0+ for self-managed/dedicated instances.
  - Two older entries (Aug 13: Google Drive in Library, Chat model defaults) scrolled off the bottom of this rolling changelog page — not a site removal, just this page's own display window; both remain in git history.

### Interview guide: new AI-tool-use policy disclosure

- **[`/interview-guide/`](../../pages/openai.com/interview-guide/index.md)** — added a new "Our work in practice" intro section, and a new explicit candidate-facing disclosure: *"We want to understand how you think... Expectations for AI and other tools vary by interview: some formats intentionally allow them, while others are designed to assess your independent problem-solving without AI tools... If you're unsure, please ask your recruiter before the interview."* This is a new, substantive addition to OpenAI's own hiring process transparency, not a cosmetic edit. Nav also updated GPT-5.5→GPT-5.6 model list entry (removing GPT-5.3 Instant) and footer picked up Customer Stories/Partner Network/Supply Co. links (continuing nav-template propagation already noted in prior runs).

### Student Collective: newsletter launch replaces old CTA

- **[`/student-collective/`](../../pages/openai.com/student-collective/index.md)** — the "Explore ChatGPT for college students" section was replaced with a "Join our newsletter" call-to-action, linking to a new Substack (`openaistudentcollective.substack.com`) for OpenAI's Student Collective / Campus Leads program. A minor but real new distribution channel for this program.

## Routine, low-signal updates

Verified by diffing every changed page's markdown against yesterday's snapshot (via `git show HEAD:<path>`):

- **44 of 60 lastmod-updated URLs had zero rendered-text difference** — pure metadata/server re-render touch, no visible change.
- **7 partner-badge pages** (`endava`, `kpmg`, `mckinsey-and-company`, `ml6`, `ntt-data`, `pathfindr`, `pwc`) — only a Vercel deploy-ID (`dpl_...`) query-string changed on the partner-tier badge SVG URL; zero visible change. Same pattern flagged repeatedly in prior runs.
- **"Keep reading" carousel rotation** (`index/asana/`, `index/building-an-ai-native-finance-function/`, `index/putting-frontier-cyber-models-in-more-trusted-hands/`, and the `/news/*` category index pages) — bottom-of-page related-article cards rotated to surface yesterday's new posts (Introducing AI Futures, Offering Zero Data Retention, Stampli, ChatGPT Ads Europe, Partnering with CodeAI) in place of older cards. Expected daily churn, not an edit to the hosting page.
- `business/pricing/`, `business/learn/`, `codex/`, `business/plugins/creative-production/`, `business/plugins/databricks/`, `solutions/industries/financial-services/`, `signals/enterprise-data/`, `policies/ad-tools-dpa/`, and the remaining `index/*` URLs in the updated list were checked and found to have **no substantive text difference** — lastmod-only bumps from a sitewide re-render, consistent with the pattern seen on prior quiet days.

## New pages

1. **[Quantium — OpenAI Partner](../../pages/openai.com/business/partners/quantium/index.md)** (Select Partner) — see Significant updates above.
2. **[Tata Consultancy Services (TCS) — OpenAI Partner](../../pages/openai.com/business/partners/tcs/index.md)** (Elite Partner) — see Significant updates above.

## Removals

None this run.

## Section migrations

- 4 URLs (`index/equipping-workers-with-insights-about-compensation/`, `index/how-countries-can-end-the-capability-overhang/`, `global-affairs/new-economic-analysis/`, `index/understanding-ai-and-learning-outcomes/`) moved from the `global-affairs` sub-sitemap to `global-affairs-news-listed` — recurring flip-flop, not new (see Anomalies).

## Fetch failures

None. All 62 added/updated pages fetched cleanly (no Cloudflare-challenge content, all well above the 100-char sanity threshold).
