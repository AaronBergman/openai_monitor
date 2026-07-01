# Run Analysis: 2026-07-01T09-15Z

**Fetch time:** 2026-07-01T09:16:32Z
**Baseline:** 2026-06-29T09-15Z
**Total current URLs:** 1386
**Baseline URLs:** 1381

---

## ANOMALIES

**None detected.** No future-dated lastmod, no backwards-moving lastmod, no disappear/reappear, no genuine sub-sitemap migrations.

### Methodology correction: prior "sub-sitemap migration" anomalies were a tooling artifact

While computing this run's diff, a URL (`/index/introducing-gpt-5-2-codex/`) appeared to have moved between sub-sitemaps compared to the naive baseline comparison. Investigating further revealed the true cause: **OpenAI's sitemap deliberately cross-lists many URLs in multiple sub-sitemaps at once** (e.g., a single announcement can appear in both `sitemap.xml_product.xml` and `sitemap.xml_release.xml` simultaneously — confirmed directly in the freshly-fetched raw XML: 31 URLs currently overlap between `product` and `release` alone, 15 between `company` and `product`, 4 between `company` and `release`; 206 URLs total belong to more than one sub-sitemap right now, versus 205 in the prior baseline).

The diffing approach used in earlier runs recorded only a single sub-sitemap per URL in a plain dict, so when a multi-listed URL was enumerated in a different file order between two snapshots, the last-seen sub-sitemap name would silently overwrite the others — creating the *appearance* of a URL migrating from one category to another when nothing had actually changed. This is the most likely explanation for the large "migration" anomaly counts reported in previous runs (114 on 2026-06-27, 5 flagged similarly on 2026-06-26/others). Those were very likely measurement artifacts, not real OpenAI-side taxonomy changes.

This run's diff logic was rewritten to track the **full set** of sub-sitemaps each URL belongs to and only flags a migration when that set actually changes between snapshots. Under the corrected logic, **today's genuine migration count is 0.** Past README entries describing "sitemap taxonomy reorganizations" are left as-is per the log's append-only policy, but should be read with this caveat: the underlying pages almost certainly never moved; the appearance of movement was very likely a false signal from the old diffing method, now fixed.

---

## SIGNIFICANT NEW PAGES (5)

### 1. Core dump epidemiology: fixing an 18-year-old bug (Engineering)
**URL:** https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug/
**Lastmod:** 2026-07-01T08:16:04Z (claimed) — published same day as this run, unusually fresh
**Sub-sitemap:** engineering

A detailed postmortem about diagnosing a run of mysterious crashes in Rockset (OpenAI's internal search/data-infrastructure system, acquired 2024), used to power ChatGPT's connectors and conversation search. Engineers initially debugged individual core dumps one at a time ("doctor" approach) and got stuck; the breakthrough came from switching to a population-level ("epidemiologist") approach — having ChatGPT write a pipeline to bulk-analyze a year's worth of core dumps — which revealed the crashes were actually **two unrelated bugs**: (1) silent hardware corruption on a single bad Azure host, and (2) an 18-year-old race condition in the open-source library GNU libunwind. Notable as a rare deep engineering-culture post showing internal AI-assisted debugging workflow.

### 2. Introducing GeneBench-Pro (Research)
**URL:** https://openai.com/index/introducing-genebench-pro/
**Lastmod:** 2026-07-01T09:16:07Z (claimed)
**Sub-sitemap:** research

A new, harder benchmark for computational biology — 129 questions across 10 domains (statistical genetics, population genetics, regulatory omics, functional genomics, clinical variant interpretation, pharmacogenomics, cancer genomics, etc.). Extends the earlier "GeneBench" to test "research taste": judgment calls like choosing an analysis path, revising assumptions under ambiguous/messy real-world data, and knowing when a result is decision-ready, rather than just running a fixed workflow. Companion case-studies page (below) published same day.

### 3. GeneBench-Pro case studies (Research)
**URL:** https://openai.com/index/genebench-pro/case-studies/
**Lastmod:** 2026-07-01T09:16:08Z (claimed)
**Sub-sitemap:** page (generic page type, not "research" — worth noting as a minor taxonomy quirk, not flagged as an anomaly since it's a first-seen URL, not a migration)

Walks through 10 representative GeneBench-Pro benchmark problems in detail; companion deep-dive to the announcement above.

### 4. How ChatGPT adoption has expanded (Global Affairs / OpenAI Signals)
**URL:** https://openai.com/index/how-chatgpt-adoption-has-expanded/
**Lastmod:** 2026-06-30T16:01:46Z (claimed)
**Sub-sitemap:** global-affairs

New OpenAI Signals usage-data report. Key claims: six months after signup, users send 50% more messages/day and have tried 2x as many distinct capabilities as when they joined (measured via a 53-category message classifier on a 0.1% user sample, accounts created 2025-10-15 through 2026-05-01). Adoption has grown fastest, in relative terms, in Africa and Asia, and in lower-Human-Development-Index countries — attributed partly to free/Go tier pricing. Framed as evidence of ChatGPT's usage "deepening" and globalizing.

### 5. Mapping Europe's AI Workforce Opportunity (Global Affairs / Economic Research)
**URL:** https://openai.com/index/mapping-ai-jobs-transition-eu/
**Lastmod:** 2026-06-29T10:24:03Z (claimed)
**Sub-sitemap:** global-affairs

Extends OpenAI's US "AI Jobs Transition Framework" (April 2026) to the EU labor market, using the EU's ESCO occupation taxonomy and Eurostat data. Splits EU employment into four buckets: ~12% in occupations that may grow with AI, ~14% at higher near-term automation potential, ~27% likely to reorganize, ~47% with less immediate change. Notes the EU has a smaller share of high-automation-potential employment than the US. Country-level: Luxembourg/Sweden/Netherlands skew toward "may grow," while Germany/Greece/Italy skew toward "higher automation potential." Positions OpenAI as advocating policy preparation (monitoring systems, national readiness plans) rather than making employment forecasts.

---

## NOTABLE UPDATES

### Health Privacy Notice — substantive rewrite (policy)
**URL:** https://openai.com/policies/health-privacy-policy/
**Lastmod:** 2026-06-26T09:01:53Z → 2026-06-29T21:00:42Z
**Header change:** "Published: January 7, 2026" → "Updated: June 29, 2026"

This is a real, substantive rewrite, not a routine touch. The single "Health" feature is renamed/split into two distinct offerings: **"ChatGPT Health"** and **"Connect Health"** (collectively "Health Features"), and the notice's scope, memory-handling rules, and third-party-account-linking language were all expanded and rewritten accordingly (e.g., a new "Linked Accounts" control replaces the old "Apps" control section; memory rules are now split by product; Health Features are described as "only available to certain users at this time"). This directly correlates with previously-seen new pages like `/index/introducing-chatgpt-health/` and `/index/openai-for-healthcare/` — this is the legal/privacy scaffolding catching up to that product launch.

### Moderna customer story — quote removed, footer nav expanded
**URL:** https://openai.com/index/moderna/
A direct pull-quote from Moderna's CIO Brad Miller ("90% of companies want to do GenAI, but only 10% of them are successful...") was removed from the body copy. Cause unknown (attribution dispute, exec departure, or just editorial trim) — flagged for awareness, not urgency. Separately, the page footer nav gained two new links present site-wide: "Customer Stories" and "Partner Network" under the Business section.

### Routine "Keep reading" recirculation refreshes (noise, not substantive)
The following pages showed lastmod bumps and diff lines, but on inspection the only change was which article thumbnails appear in the "Keep reading" widget at the bottom of the page (reflecting the day's new publications) — no body content changed:
`chatgpt-enterprise-spend-controls`, `helping-build-shared-standards-for-advanced-ai`, `lseg`, `omio`, `samsung-electronics-chatgpt-codex-deployment`, `signals/`, `academy/codex-automations/`.

### Pure CMS-touch, zero content diff (lastmod bumped, byte-for-byte identical markdown)
9 Codex Academy pages (`codex-for-work/how-business-operations-teams-use-codex`, `codex-for-work/how-data-science-teams-use-codex`, `codex-for-work/how-sales-teams-use-codex`, `codex-how-to-start`, `codex-plugins-and-skills`, `codex-settings`, `how-finance-teams-use-codex`, `how-to-use-codex-for-everyday-work`, `what-is-codex`, `working-with-codex`) all got a uniform lastmod bump to ~2026-07-01T07:48Z with no content change — consistent with a batch CMS republish/cache-bust rather than an edit.

Other lastmod-only bumps with no content diff: `business/`, `business-data/`, `business/solutions/data/`, `business/chatgpt-pricing/`, `business/pricing/`, `api/pricing/`, `codex/`, `products/release-notes/`, `signals/research/`, six `form/*` pages (100-chats-book-request, chatgpt-pro-community, life-sciences-access, openai-campus-leaders-interest-form, rosalind-biodefense-program, trademark-counterfeit-disputes, openai-campus-network-student-club-interest-form), `policies/professional-services-security-measures/`, `policies/uk-online-safety-act/`, and several `/index/*` article pages (gpt-5-immunology-mystery, hp-frontier-partnership, how-agents-are-transforming-work, openai-broadcom-jalapeno-inference-chip, previewing-gpt-5-6-sol). Likely infrastructure-level cache/CDN timestamp refresh rather than edits.

---

## REMOVALS

None this run.

---

## FETCH FAILURES

None. All 34 sub-sitemaps and all 47 changed/new page fetches succeeded on the first attempt.
