# Analysis: 2026-05-31T09-17Z

**Fetch time:** 2026-05-31T09:19:53 UTC  
**Baseline:** 2026-05-29T09-16Z  
**Stats:** 1311 total URLs | 5 added | 271 updated | 24 removed | 0 anomalies | 0 fetch failures

---

## Anomalies

None detected. (An earlier draft flagged 13 "reappeared_url" anomalies, but these were artifacts of a baseline-loading bug that picked up stale files from an older naming convention. Corrected baseline is 2026-05-29T09-16Z; against it, no anomalies are present.)

---

## New Pages (5)

### https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/
- **Sub-sitemap:** `publication`
- **lastmod:** 2026-05-29T08:03:31.979Z
- **Summary:** OpenAI's blog post announcing "Rosalind Biodefense" — a trusted-access program for deploying advanced AI in defensive biology. The post describes GPT-Rosalind, a model variant with elevated capabilities for biodefense use cases, subject to vetting. OpenAI frames this as extending its layered-safety strategy into life sciences, with access gated through a formal application process for "researchers, public health teams, and mission-driven organizations." This is a significant disclosure: it names a model variant not previously listed on the public site.

### https://openai.com/form/rosalind-biodefense-program/
- **Sub-sitemap:** `page`
- **lastmod:** 2026-05-29T13:13:43.990Z
- **Summary:** Application form for the Rosalind Biodefense Program. Offers free GPT-Rosalind API access for high-impact defensive applications in life sciences: non-pharmaceutical interventions, epidemiological modeling, biosurveillance, preparedness, MCM development. Directly paired with the blog post above.

### https://openai.com/index/boston-childrens-hospital/
- **Sub-sitemap:** `brand-stories-api`
- **lastmod:** 2026-05-30T19:40:25.635Z
- **Summary:** Customer case study. Boston Children's Hospital (~1M outpatient visits/year) uses AI for supply chain, billing, and operations automation. Built an enterprise AI layer after early fragmented deployments. Healthcare vertical customer story — adds to the growing list of healthcare AI deployments.

### https://openai.com/index/braintrust/
- **Sub-sitemap:** `brand-stories-api`
- **lastmod:** 2026-05-30T18:04:56.781Z
- **Summary:** Customer case study. Braintrust (an AI evaluation platform) uses Codex with GPT-5.5 to turn customer feature requests into preview branches in minutes. Key quote: "Codex unlocked our ability to try out customer feature requests in real time." Developer-tools vertical Codex case study.

### https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- **Sub-sitemap:** `safety`
- **lastmod:** 2026-05-31T05:21:06.127Z
- **Summary:** Technical/policy paper on best practices for independent AI evaluations. Covers harness design for agentic/multi-step systems, validity checks, and how different types of capability claims require different harness choices. Part of OpenAI's transparency push around frontier model evaluation methodology.

---

## Updated Pages (271 with changed lastmod)

The vast majority of the 271 lastmod changes reflect **sidebar/related-content refreshes** across the site: pages displaying "Related stories" widgets updated because featured items changed from (MUFG, Frontier Governance Framework) to (Boston Children's Hospital, Rosalind Biodefense). This is routine CMS propagation, not substantive edits to those pages.

Pages with verified substantive content changes:

- **https://openai.com/research/index/** — Research index now leads with "Strengthening societal resilience with Rosalind Biodefense," replacing "Introducing ChatGPT Images 2.0."
- **https://openai.com/news/research/** — News/research feed similarly updated to feature Rosalind Biodefense content.
- Individual brand-story pages (virgin-atlantic, bny, choco, databricks, endava, etc.) — "Related stories" sidebar refreshed to Boston Children's Hospital.

---

## Removed Pages (24)

URLs present in the 2026-05-29 sitemap but absent from the 2026-05-31 sitemap. Pages may still be accessible directly; removal means OpenAI is de-indexing them from public crawl.

### High-Signal Removals

**openai.com/advertisers/**
ChatGPT advertising product page (first seen 2026-05-07). Marketed ChatGPT as an ad channel with the pitch: "Reach people as they explore options, compare choices, and make decisions in ChatGPT." Removal from sitemap is notable — may signal a change in strategy or a redesign of how the ad product is marketed.

**openai.com/deployco/** + /deployco/privacy-policy/ + /deployco/terms-of-use/**
"DeployCo" was a sub-brand that appeared on 2026-05-20 (just 11 days ago) and is already de-listed. Having its own privacy policy and terms-of-use suggests it had a distinct legal identity. Very short lifespan; likely renamed, merged, or scrapped. The main page referenced the "OpenAI Deployment Company" concept.

**openai.com/business/the-openai-deployment-company/**
Removed alongside DeployCo. Marketing page for the "OpenAI Deployment Company" concept.

**openai.com/agent-platform/**
Developer-facing page for OpenAI's agent platform (first seen 2026-05-07). Included links to agent platform documentation and the Agents SDK. Removal suggests a restructuring of the developer portal or product renaming.

**openai.com/foundation/**
OpenAI Foundation landing page. A simple intro linking to openaifoundation.org. Removing it from openai.com's sitemap suggests the Foundation's web presence is fully migrating to its own domain.

**openai.com/policies/business-terms/**
The "current" business terms page de-listed. Historical versions (nov-2023, aug-2023, may-2025) remain in the sitemap. The page content was "Effective: January 1, 2026" — possibly now redirected or consolidated under the may-2025 archive URL.

**openai.com/policies/sora-usage-policies/** + /policies/creating-sora-videos-in-line-with-our-policies/**
Both Sora-specific policy pages removed — likely consolidated into general usage policies.

**openai.com/safety/evaluations-hub/**
The Safety Evaluations Hub was actually served from deploymentsafety.openai.com with its own branding ("Deployment Safety Hub"). Its openai.com sitemap entry being removed is consistent with that migration being complete.

**openai.com/science/**
The /science/ section page removed. Content may be merging into /research/ or another section.

**openai.com/solutions/healthcare/**
Healthcare vertical solutions page removed.

### Other Removals
- `openai.com/business/guides-and-resources/` — Business guides section index
- `openai.com/chatgpt/download/` — ChatGPT download page
- `openai.com/chatgpt/search-product-discovery/` — ChatGPT search product discovery
- `openai.com/contributions/` — Contributions page
- `openai.com/devday/directory/` — DevDay directory
- `openai.com/form/custom-models/` — Custom models application form
- `openai.com/index/gpt-5-2-codex/` — GPT-5.2-Codex blog post (may be superseded)
- `openai.com/index/parameter-golf/` — Research blog post removed
- `openai.com/newsroom/global-affairs/` — Global Affairs newsroom section index
- `openai.com/newsroom/security/` — Security newsroom section index
- `openai.com/reserved-capacity/` — Reserved capacity product page

---

## Interpretation

Three themes dominate this run:

1. **Rosalind Biodefense launch**: OpenAI publicly announced a biology-specific trusted-access program and named "GPT-Rosalind" as a model variant for the first time on the public site. The announcement propagated through 271 pages (sidebar updates). The companion application form went live simultaneously.

2. **DeployCo experiment ended**: A brand/product that debuted just 11 days ago (2026-05-20) has already been pulled from the sitemap. Worth monitoring for a relaunch under a different name.

3. **Broad sitemap housekeeping**: 24 pages de-listed including advertisers, agent-platform, foundation, science, healthcare solutions, reserved capacity, Sora policies, and DeployCo. This looks like a deliberate cleanup — pages being consolidated, redirected, or phased out.
