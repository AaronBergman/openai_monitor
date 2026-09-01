# Analysis — Run 2026-09-01T09-16Z

**Fetch time:** 2026-09-01T09:17:44Z UTC
**Baseline:** 2026-08-31T09-15Z (consecutive day)
**Totals:** 1625 URLs across 36 sub-sitemaps (0 removed, 3 added) | 214 URLs with a changed `<lastmod>` | 0 anomalies | 0 fetch failures

This is the largest single-day `<lastmod>` batch since the 2026-08-28 run (963 updated). Of the 214 touched pages, 70 are byte-for-byte identical to their prior snapshot (pure metadata/cache-bust touches), 127 changed only in the "Keep reading" / related-articles widget (which pages get surfaced changes daily as new posts publish, without altering the page's own content), and 17 had a substantive, human-legible change. All 217 changed-or-new page fetches (214 updated + 3 added) succeeded on the first attempt via `tools/html_to_md.py`.

## Anomalies

None detected:
- No `<lastmod>` later than fetch time (future-dated).
- No `<lastmod>` moved backwards vs. the prior snapshot.
- No new URL whose `<lastmod>` predates its first_seen by more than a few days (all 3 new URLs carry an Aug 31–Sep 1, 2026 `<lastmod>`, consistent with same-day publication).
- No URL reappeared after having previously disappeared (checked all 3 added URLs against `state/known_urls.json`; none were previously known).
- No sub-sitemap section migrations (every URL common to both snapshots kept the same section).

The unusually large update count (214, vs. 25/51/63 on the three preceding days) is not itself flagged as a timestamp anomaly — none of the touched pages show a `<lastmod>` inconsistent with observed reality, they were simply bumped in bulk, spanning content published from just this week back to roughly January 2026 (see "Routine" section below).

## Substantive updates (17 pages)

1. **[`/policies/ad-policies/`](../../pages/openai.com/policies/ad-policies/index.md)** — Legal-services advertising restriction relaxed. Previously: "Ads for legal advice, representation, or legal services... are not permitted." Now: permitted in the US only when the advertiser is licensed to practice law in that jurisdiction; explicitly still prohibited outside the US. Two policy-section headers renamed ("Ad placement policy" → "Ad placement policies", "Ad content policy" → "Ad content policies"). Changelog bumped to "v1.5 (Aug 2026): Updated to reflect that legal services are permitted in the US." Updated-date bumped from Aug 10 to Aug 31, 2026.

2. **[`/collective-cyberdefense/`](../../pages/openai.com/collective-cyberdefense/index.md)** — Signatory roster changed: **added Cohesity and HPE**, **removed BCG** (net 155 → 156 companies). The page was also restructured: the flat signatory list gained an A–Z jump index and the page picked up a new "First day signatories" footer heading (likely a template change alongside the roster update, not just new logos).

3. **[`/index/bringing-chatgpt-for-teachers-to-more-us-school-districts/`](../../pages/openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts/index.md)** — State count in signed "General Offers" dropped from **16 states to 15**: **New York was removed** from the list (Illinois, Iowa, Maine, Massachusetts, Missouri, Nebraska, New Hampshire, New Jersey, Ohio, Rhode Island, Tennessee, Texas, Vermont, Virginia, Washington remain; California is covered separately). No accompanying explanation on the page for why New York dropped off — worth watching for a follow-up post.

4. **[`/index/introducing-new-capabilities-to-gpt-rosalind/`](../../pages/openai.com/index/introducing-new-capabilities-to-gpt-rosalind/index.md)** — All internal links to `/gpt-rosalind/` repointed to `/rosalind/`, catching this page up to the Rosalind rebrand first reported on 2026-08-29.

5. **[`/business/frontier/`](../../pages/openai.com/business/frontier/index.md)** — Compliance language softened from "is built on the same trusted security and compliance foundation... **that meets** leading standards" to "**is aligned with** leading standards" (SOC 2 Type II, ISO/IEC 27001/27017/27018/27701, CSA STAR) — a subtle legal hedge on certification claims.

6. **[`/business/why-openai/small-business/`](../../pages/openai.com/business/why-openai/small-business/index.md)** — Webinar schedule refreshed: several past sessions converted from "Register here" to "Watch the recording"/"Watch on-demand"; the "Launch Smarter on Shopify with ChatGPT and Codex" session was rescheduled from Aug 19 to **Sep 2, 2026**.

7. **[`/business/solutions/cybersecurity/`](../../pages/openai.com/business/solutions/cybersecurity/index.md)** — New banner added promoting a livestream on **September 3, 2026 at 1pm PT** on "how frontier AI is reshaping cyber defense," linking to `/business/learn/intelligence-at-work-cyber/`.

8. **[`/index/partnering-with-codeai/`](../../pages/openai.com/index/partnering-with-codeai/index.md)** — The "Hour of AI" link was cleaned from a long UTM-tracking-parameter URL to a bare `https://code.org/hour-of-ai` link.

9. **[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)** — Rolling changelog window advanced. New entries surfaced (older ones — Codex MCP server deprecation, plugin discovery, time-aware answers, faster long conversations, all dated Aug 21–24 — rolled off the visible window, though they remain live at their own URLs):
   - **Mutual TLS (mTLS) and X.509 workload identity federation** for the OpenAI API — now GA (Aug 29).
   - **Connect multiple Google accounts** (Gmail/Calendar/Contacts) to ChatGPT (Aug 28).
   - **Import and sync plugin marketplaces from GitHub** for Business workspace admins (Aug 28).
   - **More controls in temporary chat** — optional personalization via memory/instructions/plugins (Aug 27).
   - **Centralized identity management in Admin Console** for Enterprise/Edu — SCIM, groups, roles (Aug 27).

10. **[`/signals/`](../../pages/openai.com/signals/index.md)** and **[`/signals/research/`](../../pages/openai.com/signals/research/index.md)** — New research report listed: *"Training novices to think, or giving them LLMs? Evidence from an RCT"* (Aug 2026), examining how ChatGPT access and causal-reasoning training affect performance on a real business problem. The older *"State of enterprise AI 2025"* report (Dec 2025) was dropped from the `/signals/research/` listing (report itself presumably still hosted, just delisted).

11. **[`/index/our-approach-to-advertising-and-expanding-access/`](../../pages/openai.com/index/our-approach-to-advertising-and-expanding-access/index.md)** — Two straight-quote-to-curly-quote typography fixes, plus its related-articles widget refreshed (routine, bundled with the substantive quote fix).

12–13. **[`/solutions/blueprints/mcpkit/`](../../pages/openai.com/solutions/blueprints/mcpkit/index.md)** and **[`/solutions/blueprints/knowledge-retrieval/`](../../pages/openai.com/solutions/blueprints/knowledge-retrieval/index.md)** — These two legacy pages finally picked up the "Why OpenAI / Solutions / Resources / Customers / Pricing" global nav that has been sitewide since 2026-07-25 (previously flagged as a live A/B test in the 2026-07-28 run; here it reads as simple template catch-up on stale pages, not a new test flip). Minor content-card and icon changes accompanied the nav sync.

14. **[`/index/reasoning-models-chain-of-thought-controllability/`](../../pages/openai.com/index/reasoning-models-chain-of-thought-controllability/index.md)** and **[`/index/how-we-monitor-internal-coding-agents-misalignment/`](../../pages/openai.com/index/how-we-monitor-internal-coding-agents-misalignment/index.md)** — Both gained an "Alignment" tag link (`/news/?tags=alignment`) in their topic-tag footer — a taxonomy/tagging cleanup, not a content change.

15. **[`/index/introducing-intelligence-age/`](../../pages/openai.com/index/introducing-intelligence-age/index.md)** — Lost its "Keep reading" widget entirely (previously surfaced a self-referential link to `/index/introducing-ai-futures/`); the widget section was removed from this page rather than just refreshed.

## Routine, low-signal updates (197 pages)

- **127 pages** changed only in the "Keep reading" / related-articles widget at the bottom of the page — new/removed card references to recently published posts (chiefly surfacing the three new posts and other late-August posts), with zero change to the page's own body content.
- **70 pages** are byte-for-byte identical to their prior snapshot — pure `<lastmod>` bumps with no visible change at all. Unlike recent days' clustering in a handful of `/business/` or `/index/` collections, this batch spans an unusually wide and old range of content — some pages (e.g. `/solutions/blueprints/mcpkit/`, `/index/work-with-codex-from-anywhere/`) got `<lastmod>` jumps of 80–150 days, consistent with a broad CMS reindex/republish sweep rather than editorial activity. Full per-URL list in [`diff.json`](diff.json).

## New pages (3)

- **[A milestone in expanding access to AI](../../pages/openai.com/index/expanding-access-to-ai-with-chatgpt-ads/index.md)** (Product, Aug 31) — ChatGPT Ads has reached **$1 billion in annualized revenue run rate** in under 200 days since launch, with tens of thousands of advertisers. Self-service Ads Manager access is expanding today to India, Europe, the Middle East, and North Africa (ads previously available in 40+ countries via managed sales/partners). Notes CPC/outcome-based bidding now dominant, 50+ technology/measurement partners, and cites an advertiser 3x ROAS example. Frames advertising as one pillar of a "diversified business model" alongside subscriptions, enterprise, and API revenue, supporting the free ad-tier for 1B+ weekly active users.

- **[Polimill builds Japan's next-generation public AI infrastructure](../../pages/openai.com/index/polimill/index.md)** (customer story, Aug 31) — Polimill's QommonsAI (built on OpenAI's API and Codex) is used by roughly 1,050 Japanese municipalities and 550,000 public employees for tasks like assembly response, public services, social welfare, and legal search. Codex cut development time 3–5x. Fits the ongoing pattern of public-sector/government AI-adoption customer stories.

- **[OpenAI supports California's bill to advance youth AI safety](../../pages/openai.com/index/supporting-california-bill-advance-ai-youth-safety/index.md)** (Company, Aug 31) — OpenAI publicly backs California SB 1119 (age verification, independent audits, parental controls, crisis-resource connections, ad-targeting limits for minors) and published a letter urging Governor Newsom to sign it. Explicitly ties this to the existing "ChatGPT for Teens" product and prior teen-safety commitments (parental controls, age prediction, Teen Safety Blueprint, Model Spec teen protections). Continues a steady cadence of teen-safety policy posts throughout August.

## Removals

None this run.
