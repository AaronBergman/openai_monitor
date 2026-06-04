# Analysis — 2026-06-04T09-15Z

**Fetch time:** 2026-06-04T09:22Z (approx)
**Baseline:** 2026-06-03T09-15Z
**Total current URLs:** 1327

## Summary
- Added: 7 URLs
- Updated: 200 URLs (sitemap lastmod changed)
- Removed: 0 URLs
- Anomalies: 0
- Fetch failures: 0

---

## Anomalies

None detected. All `<lastmod>` timestamps are plausible and none moved backwards.

---

## New Pages (7 Added)

### 1. GPT-Rosalind Product Page (MAJOR)
**URL:** `https://openai.com/gpt-rosalind/`
**Path:** `pages/openai.com/gpt-rosalind/index.md`
**lastmod:** 2026-06-04

OpenAI officially published a product landing page for **GPT-Rosalind**, described as "AI for life sciences research." The page positions it as "a purpose-built model for life sciences research, designed to reason across biology, scientific evidence, data, and tools." Key capabilities: biological reasoning (molecules, proteins, genes, pathways), integration with scientific tools and datasets, and evidence evaluation across papers. Benchmark improvements claimed: 53.7% increase per token on Genebench, 18.0% on Medchem Bench, 19.6% on Labworkbench. CTAs: "Contact sales" and "Request access." Complemented by:

- **`/form/rosalind-biodefense-program/`** — Application form for the Rosalind Biodefense Program (already in baseline from prior runs)
- **`/index/strengthening-societal-resilience-with-rosalind-biodefense/`** — Already in baseline; covers the biodefense launch (see below)

### 2. Rosalind Biodefense — New Capabilities Announcement
**URL:** `https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/`
**Path:** `pages/openai.com/index/introducing-new-capabilities-to-gpt-rosalind/index.md`
**lastmod:** 2026-06-04

New article announcing expanded capabilities for GPT-Rosalind. Accompanies the launch of the Rosalind Biodefense Program (announced May 29) and the dedicated product page.

### 3. A Blueprint for Democratic Governance of Frontier AI
**URL:** `https://openai.com/index/frontier-safety-blueprint/`
**Path:** `pages/openai.com/index/frontier-safety-blueprint/index.md`
**lastmod:** 2026-06-04 (published June 3)

OpenAI published a detailed blueprint for how the U.S. can build "a durable federal framework for governing increasingly capable AI systems." Three-part strategy: (1) build a national framework leveraging emerging state frontier safety laws (California SB 53, New York RAISE Act, Illinois SB 315); (2) strengthen CAISI as the primary federal AI safety institution; (3) mobilize a broader resilience plan. Released alongside a White House executive order on *Promoting Advanced Artificial Intelligence Innovation and Security*. Links to the full PDF on the OpenAI CDN.

### 4. OpenAI Public Policy Agenda
**URL:** `https://openai.com/index/public-policy-agenda/`
**Path:** `pages/openai.com/index/public-policy-agenda/index.md`
**lastmod:** 2026-06-04 (published June 3)

Comprehensive document outlining OpenAI's five policy principles (Democratization, Empowerment, Universal Prosperity, Resilience, Adaptability) and specific policy priorities: safety, youth safety, AI resilience, AI infrastructure/energy. This appears to be the first time OpenAI has published such a formal public policy agenda document on its main website.

### 5. Merchant Feed Terms of Service (MAJOR)
**URL:** `https://openai.com/policies/merchant-feed-terms-of-service/`
**Path:** `pages/openai.com/policies/merchant-feed-terms-of-service/index.md`
**lastmod:** 2026-06-04 (published June 3)

New legal document governing how merchants can submit product data (feeds) to OpenAI for use in its products. Key provisions:
- Merchants submit product content ("Merchant Content") via feeds per specs at `developers.openai.com/commerce/specs/feed`
- OpenAI gets a worldwide royalty-free license to reproduce, distribute, modify, and display the merchant content to surface/recommend products to users
- "OpenAI may use Merchant's name, brand, logos, and trademarks in connection with OpenAI's authorized use of Merchant Content"
- Merchant must comply with OpenAI's "Prohibited Products Policies" at `/policies/commerce-policies/`

**Significance:** This document signals OpenAI is building out a structured e-commerce/shopping capability in ChatGPT and the API — merchants can now formally feed their product catalogs to OpenAI for AI-powered product recommendations in ChatGPT conversations.

### 6. Endava Frontiers Customer Story
**URL:** `https://openai.com/index/endava-frontiers/`
**Path:** `pages/openai.com/index/endava-frontiers/index.md`
**lastmod:** 2026-06-04 (published June 4)

New customer story: "How Endava is redesigning software delivery around AI agents." Endava (global IT services company) is using ChatGPT + Codex for enterprise software delivery workflows. Covers rollout, results, and lessons.

### 7. Wasmer Customer Story
**URL:** `https://openai.com/index/wasmer/`
**Path:** `pages/openai.com/index/wasmer/index.md`
**lastmod:** 2026-06-03

New customer story about Wasmer (WebAssembly runtime company) using Codex to build a Node.js runtime for the edge. Added to the Customer Stories index page with the Wasmer story replacing the older Sea/David Chen story.

---

## Significant Updates (Selected from 200 Total)

### Codex Academy — Major Content Refresh (10+ pages, June 4)
All core Codex Academy educational pages received content updates today:
- `/academy/what-is-codex/` — Primary intro page updated
- `/academy/codex-how-to-start/` — Getting started guide
- `/academy/working-with-codex/` — Working guide
- `/academy/codex-automations/` — Automations module
- `/academy/codex-settings/` — Settings guide
- `/academy/codex-plugins-and-skills/` — Plugins and skills
- `/academy/how-finance-teams-use-codex/` — Finance use cases
- `/academy/codex-for-work/how-sales-teams-use-codex/` — Sales use cases
- `/academy/codex-for-work/how-data-science-teams-use-codex/` — Data science use cases
- `/academy/codex-for-work/how-business-operations-teams-use-codex/` — Business ops use cases
- `/academy/how-to-use-codex-for-everyday-work/` — Everyday work guide (new in this run, with today's date)

The `what-is-codex/` page diff shows a card reordering (sales teams and data science teams cards swapped positions). These Academy pages are being expanded alongside the "Codex for Knowledge Work" push.

### Codex for Knowledge Work Report (June 2)
**URL:** `https://openai.com/index/codex-for-knowledge-work/`
New post: "Codex is becoming a productivity tool for everyone" with key stats:
- **5 million weekly active users** (up 6x since desktop app launch in February)
- Knowledge workers now ~20% of users, growing 3x faster than developer users
- Primary knowledge worker tasks: reports, spreadsheets, presentations, contracts
- Links to new report: *The Next Era of Knowledge Work* (PDF on CDN)

### Codex for Every Role Tool Workflow (June 4)
**URL:** `https://openai.com/index/codex-for-every-role-tool-workflow/`
Framework article positioning Codex as a tool for all business roles, not just engineers.

### Stargate Michigan Data Center Groundbreaking (June 1)
**URL:** `https://openai.com/index/stargate-michigan-data-center/`
**Path:** `pages/openai.com/index/stargate-michigan-data-center/index.md`
OpenAI announced groundbreaking on "The Barn," a 1GW data center campus in Saline, Michigan, partnering with Oracle, Related Digital, and Walbridge. Key commitments: no cost to local ratepayers, union construction (2,500+ jobs), $10M investment in Saline Recreation Center, $1B projected tax revenue. Also: $45M in Codex credits for 400,000+ Michigan college/trade students during 2026-2027.

### OpenAI Frontier Models and Codex on AWS (June 1)
**URL:** `https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/`
OpenAI frontier models and Codex are now generally available on AWS via Amazon Bedrock. Enterprise path for AWS customers to use OpenAI through existing security/compliance workflows.

### OpenAI Frontier Governance Framework (May 28)
**URL:** `https://openai.com/index/openai-frontier-governance-framework/`
Publication of a framework explaining how OpenAI's safety/security practices align with emerging legal requirements (California Transparency in Frontier AI Act, EU AI Act Code of Practice for GPAI). Covers risk assessment across cyber offense, CBRN risks, harmful manipulation, and loss of control.

### Intelligence at Work Livestream Page (June 4)
**URL:** `https://openai.com/business/intelligence-at-work/`
Post-event page for a recent OpenAI enterprise livestream with CRO Denise Dresser, featuring a contact form for businesses interested in enterprise AI deployment.

### Stories Section Update (June 4)
All `/stories/` pages updated: the customer stories section now leads with the Chip Ganassi Racing story (May 28) and includes Wasmer, Endava, and other new stories. The stories section is organized by product: All / ChatGPT / API / Sora.

### Customer Stories Index (June 4)
**URL:** `https://openai.com/business/customer-stories/`
The stories index was updated: Wasmer's story (Jun 3, 2026) was added and the older "Sea's View on the Future of Agentic Software Development with Codex" story was removed from the highlighted section.

### Advancing Youth Safety (June 2)
**URL:** `https://openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership/`
OpenAI calls for global action on youth AI safety through a dedicated AI Safety Institute. Published ahead of/during the G7 Summit. Argues that protecting young people from AI risks is "a shared responsibility" and should not fall primarily on parents/families.

### AI Policy and Political Advocacy (June 1)
**URL:** `https://openai.com/index/our-views-on-ai-policy-and-political-advocacy/`
OpenAI clarifies its political stance: has not donated to super PACs, no employee-funded PAC, no donations to candidates. Addresses questions about "Leading the Future (LTF)" — clarifies that Greg Brockman's involvement is personal, not on behalf of OpenAI. "No outside political group speaks for OpenAI."

### Major Policy Updates (June 3)
- **`/policies/service-terms/`** — Updated (June 3, 2026) — Service terms received another update
- **`/policies/eu-services-privacy-policy/`** — Updated June 2, 2026 — EU-specific privacy policy (replaces the `row-privacy-policy` split; the old `services-privacy-policy` also appears to have been superseded but was already removed in a prior run)
- **`/policies/privacy-policy/`** — Updated (US users)
- **`/policies/sub-processor-list/`** — Updated

### Trustworthy Third-Party Evaluations (May 29)
**URL:** `https://openai.com/index/trustworthy-third-party-evaluations-foundations/`
Technical blog post on methodology for independent evaluations of frontier AI models. Discusses how modern models require "harness"-aware evaluation design (the surrounding setup matters, not just the model), and introduces a framework for evaluating capability claims vs safety mitigation claims.

### Election Safeguards 2026 (May 27)
**URL:** `https://openai.com/index/election-safeguards-2026/`
OpenAI's 2026 election year commitments: surfacing reliable voting information (partnering with AP for live vote counts in US and Brazil, Democracy Works for voter registration), supporting cyber defenders, increasing AI transparency, combating misuse. Building on 2024 work.

---

## Routine Updates

Large batch (~127 June 3 updates) consisting primarily of customer stories, policy pages, and publication pages receiving lastmod timestamp refreshes. These appear to be part of a site-wide content management refresh that touched many pages simultaneously. Most pages in this batch did not have significant content changes beyond lastmod.

---

## Removals

No URLs were removed from the sitemap between the June 3 and June 4 runs.

---

## Notable Context

This run captured the aftermath of a highly active period (roughly May 29 – June 4) in which OpenAI published:

1. **GPT-Rosalind** and the Rosalind Biodefense Program (life sciences AI + government biodefense)
2. **Frontier Safety Blueprint** (US federal AI governance proposal, timed with a White House executive order)
3. **Frontier Governance Framework** (internal compliance document for CA/EU regulations)
4. **Public Policy Agenda** (OpenAI's first formal public policy position document)
5. **Merchant Feed Terms** (formal e-commerce infrastructure for ChatGPT shopping)
6. **OpenAI on AWS** (GA distribution via Amazon Bedrock)
7. **Stargate Michigan** data center groundbreaking (1GW, union jobs, student Codex credits)
8. **Codex for Knowledge Work** report (5M weekly users, 20% non-developer)
9. Election safeguards and youth safety global leadership statements
10. Intelligence at Work livestream (enterprise go-to-market event)

The week's activity suggests several parallel strategic thrusts: federal policy engagement, life sciences/biodefense expansion, enterprise Codex adoption for non-developers, and e-commerce capability building.
