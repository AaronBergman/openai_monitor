# Run 2026-07-28T09-16Z — Analysis

**Fetch time (this run):** 2026-07-28T09:17:08Z (root index + all 34 sub-sitemaps fetched sequentially/in parallel starting 09:16Z)
**Baseline:** 2026-07-27T09-17Z (consecutive day — no gap)
**Sub-sitemaps:** 34 (unchanged count vs. baseline)
**Totals:** 1,485 URLs current vs. 1,484 baseline → **+1 added, 0 removed, 142 updated (lastmod bump)**, of which **41 had a detectable content diff** and 101 were byte-identical republishes.

---

## Anomalies

**1. Nav A/B-test flip-flop on `/business/plugins/*` catalog pages (soft anomaly, not a timestamp issue)**

Six `/business/plugins/` pages picked up a fresh `<lastmod>` today; five of them (`netlify`, `salesforce`, `spaceship`, `creative-production`, `hubspot`) changed **only** their top navigation/header markup — no body content changed at all. Critically, the change ran in **both directions in the same run**:

- `netlify`, `salesforce`, `spaceship`, `creative-production`: reverted from the newer "Why OpenAI / Products / Solutions / Resources / Customers / Pricing" nav (which our snapshot picked up on 2026-07-25, see that run's analysis) **back** to the older "Research / Products / Business / Developers / Company" nav + "Log in / Try ChatGPT" CTA.
- `hubspot`: flipped the **opposite** way — old nav → new nav.

Since these are near-simultaneous fetches (all within our ~09:17Z run) of structurally identical plugin-listing page templates, and the "same" nav variant that rolled out sitewide on 2026-07-25 is now inconsistent even within a single crawl, this reads as **live server-side A/B-testing or feature-flag randomization** on the nav component rather than a directional redesign rollout or a genuine "backwards" content restoration. Flagging because it means any single snapshot of these templated pages can show either nav variant depending on which bucket the request lands in — worth remembering when reading past/future nav-related notes in this log.

No genuine timestamp anomalies this run: zero future-dated lastmods, zero backwards lastmod moves, zero reappeared (previously-removed) URLs, zero cross-section migrations, and the one new URL's lastmod (`2026-07-28T09:09:10Z`) is essentially simultaneous with its first appearance in our snapshot — not backdated.

---

## Notable additions

- **`/index/how-ai-is-expanding-what-people-do-at-work/`** (lastmod `2026-07-28T09:09:10Z`, dated "July 27, 2026" on-page, filed under Company) — first entry in a new **"Work at the Frontier"** research series from OpenAI Economic Research. Analyzes 800,000+ US ChatGPT messages and finds that **43.5% of occupation-specific AI use** falls outside the user's own occupation ("task crossover") — e.g. 77% of customer-experience workers' occupation-specific AI use is for tasks belonging to other roles, 75% for designers, 69% for HR. Marketing and engineering tasks are shown to "travel" the farthest across occupations. Links out to a full PDF report. Fits with OpenAI's ongoing economic-impact publishing (AI Jobs Transition Framework, "How ChatGPT adoption has expanded") and is already being cross-linked from `/signals/research/`, `/news/company-announcements/`, and the homepage feed.

---

## Notable updates

- **`/business/plugins/adobe-photoshop/`** — genuine content rewrite, not just nav noise. The plugin listing rebranded from **"Adobe Photoshop"** (narrow: background removal, color/lighting edits, "continue in Photoshop for full creative control") to **"Adobe"** (broad: photos, videos, PDFs, social assets, Creative Cloud asset search, "data-driven documents from the conversation"). Example prompts changed from Photoshop-specific ("@Adobe Photoshop remove background...") to multi-tool ("@Adobe retouch this set of photos... then resize for YouTube Shorts and Instagram Reels", "...create a flyer... convert into a polished PDF"). Reads as Adobe's ChatGPT integration graduating from a single-app connector to a suite-wide one.
- **`/form/enterprise-trusted-access-for-cyber/`** — new required question added to the Trusted Access for Cyber (TAC) intake form: whether the applicant wants access to "OpenAI cyber models through AWS" if their TAC application is approved, and consent to share contact/approval info with AWS for that purpose. First sign we've seen of an AWS distribution channel for OpenAI's defensive-cybersecurity model access program.
- **Homepage (`/`)** — routine carousel/feed reorder: "Daybreak: Tools for securing every organization" moved down and had its date corrected (was showing "Jul 23, 2026 · 8 min read" in the older snapshot, now shows its real date "Jun 22, 2026" further down the feed as the Health-in-ChatGPT and OpenAI Presence stories moved up); no new stories in the top slots that weren't already known.
- **`/news/company-announcements/`** and **`/index/introducing-b2b-signals/`** and **`/index/how-chatgpt-adoption-has-expanded/`** — rolling "related stories" widgets refreshed to surface the newest posts (today's new task-crossover report, the Effingham County data-center piece, "How news organizations are using AI") and drop older ones (June items on the Ona acquisition, Oracle partnership, confidential S-1 filing, "Built to benefit everyone," and the Economic Research Exchange rolled off the visible list — **all still live pages**, just no longer linked from these particular listing modules; confirmed present in today's sitemap).
- **`/signals/research/`** — added a link to today's new task-crossover report; also quietly removed a duplicate entry for "How people are using ChatGPT" that had been listed twice (as a PDF and as a blog post) — now listed once.
- Recurring footer/nav widget refresh continues to reach stragglers: several pages (`/policies/health-privacy-policy/`, `/policies/coordinated-vulnerability-disclosure-policy/`, `/academy/sales/`, `/business/new-in-chatgpt-for-work-march-updates-2025/`) had their "latest releases" quick-link list bump **GPT‑5.6** into the list (already known to us since 2026-07-10, not new) while **GPT‑5.3 Instant** rolled off the bottom — this is a rolling "last N releases" widget, not new news.

---

## Routine updates (no detectable content change)

101 of the 142 lastmod-bumped URLs are byte-identical to yesterday's snapshot after whitespace normalization — a pure backend touch/republish with zero visible change. These are concentrated in the `/business/plugins/*` integrations catalog (bigger clusters: apps-data 15, apps-go-to-market 14, apps-project-management 9, apps-developer-tools 9, apps-collaboration 8) plus a handful of `page` and `company` section pages, almost all re-touched in a tight 2026-07-28 02:59–03:03 UTC window — reads as a scheduled CDN/cache resync sweep rather than editorial activity.

The remaining diffed-but-minor pages (`/business/learn/` dropped date-stamps on two carousel cards; `/academy/codex-for-work/how-sales-teams-use-codex/` added a cover-image thumbnail to an existing webinar link; `/index/the-five-ai-value-models-driving-business-reinvention/` added a bare "Share" line) are cosmetic markup churn with no substantive meaning.

---

## Removals

None this run — 0 URLs dropped out of the sitemap union.

---

## Method notes

- All 34 sub-sitemaps fetched successfully (plain fetch, no Cloudflare issue on XML endpoints).
- All 143 target pages (1 added + 142 updated) fetched successfully via `tools/html_to_md.py`'s underlying `fetch_html`/`html_to_md` functions (imported directly rather than shelled out per-URL, to keep 8-way thread-pool concurrency within the polite ≤10-worker guideline) — zero blocked/failed fetches this run.
- Prior markdown for all 142 updated URLs was captured via `git show HEAD:<path>` before overwriting, then diffed line-by-line (whitespace-trimmed) against the freshly fetched version to separate real content changes (41) from pure republish noise (101).
