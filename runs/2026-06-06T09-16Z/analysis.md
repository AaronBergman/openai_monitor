# Run Analysis: 2026-06-06T09-16Z

**Fetch time:** 2026-06-06T09:16:16Z  
**Total URLs in sitemap:** 1331  
**Added:** 11 | **Updated:** 837 | **Removed:** 28  
**Anomalies:** 0 | **Fetch failures:** 0  
**Baseline run:** 2026-06-03T09-15Z (3 days ago)

---

## Anomalies

None detected. All `<lastmod>` timestamps are plausible, chronologically consistent, and pre-date the fetch time.

---

## Executive Summary

This run captures **three days of changes** (June 3–6, 2026). The site saw a meaningful cluster of new policy and research content on June 3–4, a new dedicated GPT-Rosalind product page, 28 URL removals (including the entire `/deployco/` subdomain), a new `Merchant Feed Terms of Service`, and a sitewide navigation update that touched the template of ~837 pages.

---

## 1. Major Removals (28 URLs)

### Deployment Company subdomain wiped from sitemap
Three `/deployco/` URLs were removed, along with `/business/the-openai-deployment-company/`:
- `https://openai.com/deployco/`
- `https://openai.com/deployco/privacy-policy/`
- `https://openai.com/deployco/terms-of-use/`
- `https://openai.com/business/the-openai-deployment-company/`

**Significance:** OpenAI previously had a separate "Deployment Company" entity with its own subdomain and legal terms. Removal from the sitemap suggests this entity has been dissolved, absorbed, or rebranded. The content is no longer publicly indexed.

### Infrastructure/product pages removed
- `/reserved-capacity/` — dedicated reserved-capacity offering page gone (likely merged into enterprise sales flow)
- `/agent-platform/` — agent platform landing page removed
- `/chatgpt/download/` — ChatGPT download page removed (download links now elsewhere)
- `/advertisers/` — advertiser-facing page removed

### Section/hub pages removed
- `/science/` — OpenAI Science hub page
- `/foundation/` — Foundation page (the OpenAI Foundation now has its own site at `openaifoundation.org`, reflected in updated sitewide nav)
- `/safety/evaluations-hub/` — Safety evaluations hub page
- `/contributions/` — Contributions listing page
- `/newsroom/security/` and `/newsroom/global-affairs/` — These newsroom paths have been superseded by `/news/security/` and `/news/global-affairs/` (URL migration already tracked in prior runs)
- `/solutions/healthcare/` — Old healthcare solutions page (replaced by `/solutions/industries/healthcare/`)
- `/business/guides-and-resources/` — Old guides hub (replaced by `/business/learn/`)
- `/academy/top-10-use-cases-codex-for-work/` — Removed academy page

### Stale/superseded terms removed
- `/policies/plugin-terms/` — Plugin terms (plugins deprecated long ago)
- `/policies/sora-usage-policies/` — Sora usage policy (replaced by general usage policies)
- `/policies/creating-sora-videos-in-line-with-our-policies/` — Sora content policy removed
- `/policies/business-terms/` — Old business terms (superseded by May 2025 terms)
- `/policies/row-privacy-policy/` — Old rest-of-world privacy policy removed
- `/policies/services-privacy-policy/` — Old services privacy policy removed
- `/chatgpt/search-product-discovery/` — Old search product discovery page
- `/form/custom-models/` — Custom models form removed

---

## 2. New Pages (11 URLs)

### GPT-Rosalind product landing page
**URL:** `https://openai.com/gpt-rosalind/`  
**lastmod:** 2026-06-04  

OpenAI now has a dedicated product page for GPT-Rosalind, its purpose-built life sciences AI model. The page positions it as a model for biological reasoning—covering molecules, proteins, genes, pathways, disease biology. It highlights a partnership with Amgen, benchmarks on Genebench (+53.7% performance per token), Medchem Bench (+18%), Labworkbench (+19.6%), and LifeSci Bench (+4.4%). The page also promotes integration with Codex for automating repeatable scientific workflows.

A **Rosalind Biodefense** program is featured: trusted developers and public-health teams can apply to access GPT-Rosalind for biodefense (early detection, preparedness, diagnostics, response, countermeasures).

### Biodefense in the Intelligence Age
**URL:** `https://openai.com/index/biodefense-in-the-intelligence-age/`  
**lastmod:** 2026-06-04  

A Global Affairs post (June 4) outlining OpenAI's "action plan for AI-powered biological resilience." References the April 2026 introduction of GPT-Rosalind and the May 2026 Rosalind Biodefense announcement. Links to a full PDF plan. Argues that the same capabilities that help scientists understand disease can have biosecurity implications, and that responsible defenders should be equipped with advanced capabilities alongside governance safeguards.

### A Blueprint for Democratic Governance of Frontier AI
**URL:** `https://openai.com/index/frontier-safety-blueprint/`  
**lastmod:** 2026-06-03  

A Global Affairs post (June 3) releasing a blueprint for how the U.S. can build a durable federal framework for governing frontier AI. Three-part strategy: (1) build a national framework leveraging emerging state-law consensus (California SB 53, New York RAISE Act, Illinois SB 315); (2) strengthen CAISI as the primary federal institution for frontier AI safety; (3) a broader resilience plan for national security. References a White House executive order "Promoting Advanced Artificial Intelligence Innovation and Security" signed June 2026.

### OpenAI Public Policy Agenda
**URL:** `https://openai.com/index/public-policy-agenda/`  
**lastmod:** 2026-06-03  

A structured Global Affairs post (June 3) outlining OpenAI's full policy agenda across: Mission and principles, Policy priorities, Safety, Youth safety, AI resilience, AI infrastructure and energy.

### ChatGPT Memory "Dreaming"
**URL:** `https://openai.com/index/chatgpt-memory-dreaming/`  
**lastmod:** 2026-06-04  

A Research/Product post (June 4) on improving memory synthesis in ChatGPT—optimizing for freshness, continuity, and relevance. Describes a new "dreaming" approach to memory consolidation. Tagged as Research, Product, and Release.

### Introducing New Capabilities to GPT-Rosalind
**URL:** `https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/`  
**lastmod:** 2026-06-04  

Companion post to the GPT-Rosalind product page, describing new evals and capabilities.

### Products — Release Notes hub
**URL:** `https://openai.com/products/release-notes/`  
**lastmod:** 2026-06-05  

A new centralized release notes page under the Products section. Previously release notes were under `/chatgpt/` or other paths.

### Business Pricing
**URL:** `https://openai.com/business/pricing/`  
**lastmod:** 2026-06-05  

A new dedicated pricing page for business/enterprise plans under `/business/`. Shows Codex-based plans with usage pricing.

### Merchant Feed Terms of Service
**URL:** `https://openai.com/policies/merchant-feed-terms-of-service/`  
**lastmod:** 2026-06-03  

New legal terms governing merchant product content ("Merchant Feed") submitted to OpenAI. References a feed specification at `developers.openai.com/commerce/specs/feed`. This is the formal legal basis for merchants to share product catalog data with OpenAI for use in its products (ChatGPT shopping). Published June 3, 2026.

### Endava: Redesigning Software Delivery Around AI Agents
**URL:** `https://openai.com/index/endava-frontiers/`  
**lastmod:** 2026-06-04  

A case study (June 4) about Endava's use of ChatGPT + Codex to accelerate software delivery and reshape enterprise workflows.

### Wasmer: Building a Node.js Runtime for the Edge with Codex
**URL:** `https://openai.com/index/wasmer/`  
**lastmod:** 2026-06-03  

A Codex case study (June 3) about how Wasmer used Codex to build a Node.js runtime for the edge.

---

## 3. Significant Updates

### Site-wide navigation template update (837 pages)
The dominant change across all 837 "updated" pages is a **template-level navigation revision**. The prior navigation lacked explicit "Deployment Safety" and "Apps SDK" product links; the new template adds them. Summary of navigation changes observed across pages:

**Added to nav:**
- "Deployment Safety" → `https://deploymentsafety.openai.com/` (external)
- "Apps SDK" → `https://developers.openai.com/apps-sdk` (external)
- "Release Notes" → `/products/release-notes/`

**Removed from nav:**
- "Research Residency" link removed

**Changed:**
- "Foundation" now links to `https://openaifoundation.org` (separate site, previously had an internal page at `/foundation/`)
- "ChatGPT for Education" link added to Business section
- "ChatGPT Enterprise" link added

The volume of updated pages (837) is consistent with a sitewide template rebuild. The actual page content (body) is largely unchanged for most pages — the diff noise comes from header/footer/navigation changes.

### Notable specific content updates within the wave:
- **`/business/customer-stories/`** — Added new entries: Wasmer (Jun 3), Endava (Jun 4)
- **`/index/virgin-atlantic/`** — Added "Endava" related cross-content block (Jun 6 lastmod; same-day sitewide refresh)
- **`/about/`** — Updated June 3

---

## 4. Thematic Interpretation

### Policy week (June 3–4)
OpenAI published four related policy/governance documents in two days: a public policy agenda, a frontier AI governance blueprint referencing new state and federal legislation, a biodefense action plan, and the GPT-Rosalind biodefense program launch. This cluster coincides with the White House executive order on AI referenced in the blueprint — suggesting coordinated policy/publication timing.

### Rosalind expansion
GPT-Rosalind now has a product landing page (added to sitemap today) and the Rosalind Biodefense program is formally launched. This represents OpenAI's formal entry into the life sciences vertical as a named product offering, distinct from its general API.

### Commerce/merchant integration
The new Merchant Feed ToS signals that OpenAI's shopping capabilities in ChatGPT are maturing into a formal merchant program with legal infrastructure (feed specs, terms, commerce policies).

### Structural cleanup
The removal of the `deployco` subdomain, old plugin terms, Sora-specific policies, and redundant `/newsroom/` paths suggests a routine cleanup: retiring entities that no longer exist, consolidating overlapping sections, and pruning stale content from the public index.
