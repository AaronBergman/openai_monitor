# Run 2026-08-18T09-16Z — analysis

Fetch time (observed, UTC): 2026-08-18T09:17:07Z
Baseline: 2026-08-17T09-20Z
Sub-sitemaps recursed: 35 (1,585 URLs in current union; 1,584 in baseline)

## Anomalies

**No timestamp anomalies.** Checked all 85 updated + 3 added URLs: zero `<lastmod>` values later than fetch time, zero backwards `<lastmod>` moves vs. the prior snapshot, zero backdated new URLs (lastmod predating first_seen by more than a few days), zero disappeared-then-reappeared URLs.

**Large sub-sitemap recategorization (125 URLs moved between sub-sitemaps).** This is the standout event of the run. OpenAI restructured which sub-sitemap category many existing URLs belong to — same URL, same content, different `/sitemap.xml/<section>/` bucket. Net category-size deltas:

| sub-sitemap | before | after | delta |
|---|---:|---:|---:|
| `company` | 235 | 176 | -59 |
| `product` | 147 | 124 | -23 |
| `api` | 15 | 6 | -9 |
| `safety` | 103 | 96 | -7 |
| `brand-stories-sora` | 3 | 1 | -2 |
| `page` | 482 | 480 | -2 |
| `conclusion` | 21 | 17 | -4 |
| `engineering` | 20 | 18 | -2 |
| `release` | 35 | 65 | +30 |
| `global-affairs` | 100 | 131 | +31 |
| `security` | 24 | 45 | +21 |
| `research` | 35 | 41 | +6 |
| `learn-openai-on-openai` | 1 | 7 | +6 |
| `webinar` | 2 | 7 | +5 |
| `global-affairs-news-listed` | 0 | 4 | +4 (new bucket) |
| `sora` | 0 | 3 | +3 (new bucket) |
| `chatgpt` | 2 | 3 | +1 |
| `startup` | 8 | 9 | +1 |
| `publication` | 132 | 133 | +1 |

Pattern: URLs are migrating out of the catch-all `company` and `product` buckets into more specific taxonomies — `release`, `global-affairs`, `security`, `research`. Two brand-new buckets appeared (`global-affairs-news-listed`, `sora`), likely split out of `global-affairs`/`brand-stories-sora`. This reads as a backend taxonomy/tagging cleanup rather than anything suspicious — no URLs were added or removed by this migration, and no content changed as a result (see below). Full list of all 125 moves is in this run's `diff.json` under `anomalies`.

## Significant updates (content actually changed)

Sampled unified diffs (git-tracked prior markdown vs. freshly fetched markdown) for all 85 updated URLs. 48 had a real textual diff; 37 had a `<lastmod>` bump with byte-identical rendered content (routine backend re-save, not a content change — 5 of those 37 coincide with a sub-sitemap migration, the other 32 don't correlate with anything observed).

- **[Trust & Transparency hub](../../pages/openai.com/trust-and-transparency/index.md)** — Added a new **Brazil Election Compliance Plan** disclosure/download (in connection with TSE Ordinance No. 463/2026 and TSE Resolution No. 23,610/2019), ahead of Brazilian elections. Also updated the model list (added GPT‑5.6, dropped GPT‑5.3 Instant) and added "Customer Stories", "Partner Network", and "Supply Co." to site nav.
- **[Daybreak (cybersecurity)](../../pages/openai.com/daybreak/index.md)** — Added a new UK AI Security Institute benchmark chart ("The Last Ones") showing GPT‑5.6-Sol reaching the highest completion levels on a cyber network-takeover task among tested frontier models. Added a card linking to the new "The Defender's Window" essay (see below); dropped an older card for "Scaling Trusted Access for Cyber with GPT‑5.5."
- **[API landing page](../../pages/openai.com/api/index.md)** — Primary CTA changed from "Try ChatGPT" → "Start building" (now deep-links to platform.openai.com). Copy updated from "GPT‑5" to "GPT‑5 series." Swapped a "Front-end coding examples" callout for a new "Model best practices" callout linking to the new [Builder's guide to GPT‑5.6](../../pages/openai.com/index/builders-guide-to-gpt-5-6/index.md).
- **[Release notes](../../pages/openai.com/products/release-notes/index.md)** — New Aug 14, 2026 entry: **"ChatGPT app experience updates"** (GA) — interactive quizzes for studying, project-memory management, and easier switching between typing/dictation/desktop workflows.
- **[OpenAI Academy: Finance](../../pages/openai.com/academy/finance/index.md)** and **[Marketing](../../pages/openai.com/academy/marketing/index.md)** — Headlines retitled ("ChatGPT for finance teams" → "Learn ChatGPT workflows for finance teams", similarly for marketing), added cross-links to the matching `/business/solutions/` page.
- **Site-wide header/nav redesign continuing to roll out.** A subset of fetched pages (e.g. `business/plugins/sales/`, `business/learn/how-our-sales-team-uses-chatgpt-work/`) still show the *old* nav (Research/Products/Business/Developers/Company/Foundation, "Log in"/"Try ChatGPT") flipping to the *new* nav (Why OpenAI/Products/Solutions/Resources/Customers/Pricing, "Try OpenAI"/"Contact sales") — consistent with the new nav already seen on other pages in prior runs. This is a template rollout in progress, not new content.
- **[Codex landing page](../../pages/openai.com/codex/index.md)** and **[Small-business program announcement](../../pages/openai.com/index/introducing-chatgpt-small-business-program/index.md)** — Both had a "this post is outdated, see current page" redirect banner removed. Housekeeping.
- **Customer-story template refresh** (`index/ai-clinical-copilot-penda-health`, `index/accelerating-life-sciences-research-with-retro-biosciences`, `index/blue-j`, plus similar smaller moves on `index/circles`, `index/ringcentral`, `index/virgin-atlantic/chatgpt-work`, `index/zapier`, `index/safetykit`) — Page-header block (date/category tag/title/dek/share) moved to the top of the page above the table of contents (previously it rendered after the ToC — a template/layout change, no wording changes to the underlying article body). The Blue J story additionally gained new stat callouts ("2.7 hours saved per user weekly", "1/700 fewer than 1 in 700 answers disputed") and a pulled quote.
- **[business/solutions/operations/](../../pages/openai.com/business/solutions/operations/index.md)** — Largest single diff of the run: full page-body rewrite (headline, CTA copy, feature blurbs, workflow example prompt) — reads as a straightforward copy refresh for the operations-team solutions page, not a product change.

## Routine updates

The remaining ~35 updated pages (customer partner logos under `business/partners/*`, plugin pages under `business/plugins/*`, several `index/*` announcement pages) had only whitespace/entity normalization (e.g. `–` → `—`) or no detectable content diff at all despite a `<lastmod>` bump — treated as routine.

## New pages

- **[New policy ideas for the Intelligence Age](../../pages/openai.com/index/new-policy-ideas-for-the-intelligence-age/index.md)** (Global Affairs, claimed 2026-08-17) — OpenAI is awarding grants to 14 independent organizations to promote economic opportunity and societal resilience as AI advances, following through on the "Industrial Policy for the Intelligence Age" commitment from April 2026.
- **[OpenAI joins PORTS-Pike project](../../pages/openai.com/index/openai-joins-ports-pike-project/index.md)** (Global Affairs / Company, claimed 2026-08-17) — OpenAI, with SB Energy, NVIDIA, and the U.S. Department of Energy, is building an ~8 GW data center campus in Pike County, Ohio. Expected 35,000 construction jobs through 2032 and 2,500 permanent operating jobs; $40M community grant fund (on top of SB Energy's existing $40M); $84M in Codex credits for ~844,000 eligible Ohio college students in 2026–2027.
- **[The Defender's Window](../../pages/openai.com/index/the-defenders-window/index.md)** (Security, claimed 2026-08-17) — Essay by Greg Brockman on the current cybersecurity moment, what OpenAI is doing to defend itself, and what defenders should do now. Fits with this run's Daybreak-page benchmark update and the broader recent cyber-safety push (Daybreak, "Putting frontier cyber models in more trusted hands").

## Removals

- `https://openai.com/api/pricing/` (first seen 2026-05-07, last seen 2026-08-17) — removed from the sitemap.
- `https://openai.com/business/chatgpt-pricing/` (first seen 2026-05-07, last seen 2026-08-17) — removed from the sitemap.

Both are pricing pages; last known-good snapshots remain in git history (`git log -- pages/openai.com/api/pricing/index.md`, `git log -- pages/openai.com/business/chatgpt-pricing/index.md`). No replacement URL was added in this run's diff, so it's not a clean redirect/rename — worth a follow-up check next run to see if pricing content resurfaces elsewhere.

## Fetch failures

None. All 3 new + 85 updated pages (88 total) fetched and converted successfully.
