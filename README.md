# openai_monitor

A daily log of every change to OpenAI's public website — what appeared, what disappeared, and what was quietly updated. Newest runs at the top.

---

## 2026-06-28 — Run `2026-06-28T09-15Z`

**Fetch time:** 2026-06-28T09:15:00Z  
**Baseline:** 2026-06-27T09-15Z  
**Stats:** 1380 total URLs | +0 added | 32 updated | 0 removed | 0 anomalies | 34 sub-sitemaps

**TL;DR:** A quiet day with no new pages and no removals. All 32 URL updates carry freshened `<lastmod>` timestamps but the rendered content is byte-for-byte identical to yesterday — a routine CMS metadata-touch pattern, likely cache invalidations or backend publishing pipeline runs. The updates cluster into five recognizable batches: 11 OpenAI Academy Codex pages all touched around 06:42 UTC; three pricing pages (API, business, ChatGPT) touched together at ~16:50 UTC on Jun 27; five signup/interest forms batch-updated at ~22:30 UTC; three policy documents (UK Online Safety Act, Commerce Policies, Professional Services Security Measures) refreshed individually; and two Signals research pages updated at ~22:01 UTC. Five high-profile news articles — the GPT-5.6 Sol preview, the Jalapeño chip announcement, the Appia Foundation/AI standards post, the immunology mystery post, and the "how agents are transforming work" piece — all received minor timestamp bumps with no content change. No anomalies were detected.

### Anomalies

None.

### New Pages

None.

### Notable Updates (all metadata-only — no content changes)

- **11 Academy Codex pages** (`academy/codex-*`, `academy/how-*`, etc.) — Batch touch at ~06:42 UTC Jun 28. The full Codex Academy learning module received a coordinated CMS refresh with no visible changes.
- **3 Pricing pages** (`api/pricing/`, `business/pricing/`, `business/chatgpt-pricing/`) — Batch touch at ~16:50-16:51 UTC Jun 27. No pricing changes observed. May reflect a backend update ahead of GPT-5.6 Sol broader rollout.
- **3 Policy pages** — `policies/uk-online-safety-act/` (touched Jun 28 07:23), `policies/commerce-policies/` (touched Jun 27 13:29), `policies/professional-services-security-measures/` (touched Jun 28 07:33). All content unchanged.
- **5 news articles** — Timestamps bumped on: [Previewing GPT-5.6 Sol](pages/openai.com/index/previewing-gpt-5-6-sol/index.md), [Jalapeño chip](pages/openai.com/index/openai-broadcom-jalapeno-inference-chip/index.md), [AI standards / Appia Foundation](pages/openai.com/index/helping-build-shared-standards-for-advanced-ai/index.md), [GPT-5 immunology mystery](pages/openai.com/index/gpt-5-immunology-mystery/index.md), [How agents are transforming work](pages/openai.com/index/how-agents-are-transforming-work/index.md). No content changes.
- **Signals pages** — `signals/` and `signals/research/` touched at ~22:01 UTC Jun 27. Content unchanged; the signals/research page continues to feature the June 2026 "shift to agentic AI: evidence from Codex" report added in the prior run.
- **5 form pages** — Batch touch at ~22:30 UTC Jun 27 (`form/100-chats-book-request/`, `form/chatgpt-pro-community/`, `form/life-sciences-access/`, `form/rosalind-biodefense-program/`, `index/openai-campus-network-student-club-interest-form/`). No content changes.

### Removals

None.

Full analysis: [runs/2026-06-28T09-15Z/analysis.md](runs/2026-06-28T09-15Z/analysis.md)

---

## 2026-06-27 — Run `2026-06-27T09-15Z`

**Fetch time:** 2026-06-27T09:16:44Z  
**Baseline:** 2026-06-26T09-15Z  
**Stats:** 1380 total URLs | +5 added | 53 updated | 0 removed | 114 anomalies (all subsitemap taxonomy migrations) | 34 sub-sitemaps

**TL;DR:** Two major product announcements broke today. OpenAI previewed **GPT-5.6** — a new model family (Sol/Terra/Luna) coordinated with the U.S. government before release, with Sol being their strongest model yet and notable for new "ultra" multi-agent mode and cybersecurity capabilities that triggered the government coordination. Separately, the **Jalapeño chip page updated** (announced last run but freshly updated today with additional detail on performance). On the education front, OpenAI launched a new **Education solutions page** targeting campuses plus two new forms: a Campus Leaders community interest form and a Trusted Access for Biology Research form (extending vetted model access to life-sciences organizations below the Rosalind tier). The release notes gained two new entries: **Codex Remote is now generally available** on all ChatGPT plans with a new DigitalOcean plugin, and **memory improvements rolled out to ChatGPT Business**. Signals picked up a new research PDF on "The shift to agentic AI: evidence from Codex." The 114 flagged anomalies are all internal taxonomy changes — OpenAI reorganized their sitemap structure, moving ~100 URLs between sub-sitemaps into more logical categories (releases, security, global-affairs, research, webinars, etc.) — no content changed.

### Anomaly Note: Sitemap Taxonomy Reorganization (114 migrations)

OpenAI moved 114 URLs between sub-sitemaps today as part of a taxonomy cleanup. No content was added or removed — pages moved to semantically appropriate sub-sitemaps. Key patterns: release announcements consolidated into `sitemap.xml_release.xml`; security content into `sitemap.xml_security.xml`; global affairs and policy content into `sitemap.xml_global-affairs.xml`; learn-OpenAI-on-OpenAI demos into `sitemap.xml_learn-openai-on-openai.xml`; research publications into `sitemap.xml_publication.xml`. This appears to be a CMS/editorial taxonomy overhaul, not a content change.

### New Pages (5)

**⭐ [Previewing GPT-5.6 Sol: a next-generation model](pages/openai.com/index/previewing-gpt-5-6-sol/index.md)** (June 26, 2026)  
OpenAI announced a limited preview of GPT-5.6, a new model family with three variants:
- **Sol** — flagship, "strongest model yet"
- **Terra** — balanced, competitive with GPT-5.5 but 2× cheaper  
- **Luna** — fast and affordable, lowest cost

New capabilities: a `max` reasoning effort giving Sol maximum thinking time, and a new `ultra` mode that uses subagents to parallelize complex work. Sol sets state-of-the-art on Terminal-Bench 2.1 (coding), GeneBench v1 (long-horizon genomics), and ExploitBench (cybersecurity). The cybersecurity improvement triggered unusual U.S. government coordination: at the government's request, OpenAI is staging access through "a small group of trusted partners whose participation has been shared with the government" before broad release. OpenAI says this approach should not become a long-term default but is a short-term measure while the Administration develops a cyber Executive Order framework. Broad availability expected "in the coming weeks." Safety: GPT-5.6 Sol does not cross the "Cyber Critical" threshold per OpenAI's preparedness framework; "most robust safety stack to date" with multi-week adversarial red-teaming.

**[OpenAI for Education – solutions hub](pages/openai.com/business/solutions/education/index.md)** (new)  
New dedicated landing page targeting universities, colleges, and K-12 institutions. Three pillars: build student capability, expand faculty/staff capacity, and accelerate research. Includes a link to ChatGPT for K-12 teachers. Some image alt-text still shows "FPO placeholder" — suggests a very fresh launch.

**[Trusted Access for Biology Research form](pages/openai.com/form/trusted-access-for-biology-research/index.md)** (new)  
A new trusted-access tier for vetted biology and life-sciences organizations seeking access to OpenAI's "mainline models" (distinct from GPT-Rosalind, which remains a separate premium tier for frontier bio research). Applicants must demonstrate organizational identity, institutional mission alignment, and willingness to provide additional documentation. Reflects OpenAI's ongoing effort to expand STEM/science access with appropriate governance.

**[Campus Leaders Interest Form](pages/openai.com/form/openai-campus-leaders-interest-form/index.md)** (new)  
Interest form for enrolled university/college students (18+, 1+ year remaining) to join OpenAI's Campus Leaders community — helping peers learn AI, ~6–8 hours/month commitment. Related to the new Education solutions page.

**[Professional Services Security Measures policy](pages/openai.com/policies/professional-services-security-measures/index.md)** (new)  
New policy document covering security requirements for OpenAI's professional services engagements. Tied to enterprise/professional services expansion.

### Notable Updates

- **[Products Release Notes](pages/openai.com/products/release-notes/index.md)** — Two new entries: (1) **Codex Remote now GA** on all ChatGPT plans (Jun 25); includes a new DigitalOcean Droplet Workspace plugin and updated QR-pairing authentication. (2) **Memory improvements for ChatGPT Business** (Jun 25): improved memory now uses context from past chats automatically; users can review a memory summary, see "View Sources" on personalized responses, and correct or delete memories. No extra cost.
- **[Signals](pages/openai.com/signals/index.md) / [Signals Research](pages/openai.com/signals/research/index.md)** — New research report added: "The shift to agentic AI: evidence from Codex" (June 2026) — analysis of how agentic AI is shifting work patterns, especially inside organizations and at OpenAI. [PDF](https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf)
- **[Home page](pages/openai.com/index.md)** — Featured article replaced: "Codex for every role, tool, and workflow" → "Previewing GPT-5.6 Sol." Hero image updated to Sol/Terra/Luna visual.
- **[Company Announcements](pages/openai.com/news/company-announcements/index.md)** — Featured article updated to GPT-5.6 Sol.
- **12 Academy/Codex pages** — Bulk lastmod update (CMS refresh); no substantive content changes.
- **3 pricing pages** (API, business/pricing, chatgpt-pricing) — Lastmod updated; content unchanged (likely backend refresh ahead of GPT-5.6 pricing).
- **9 business/solutions pages** — Minor lastmod updates; one small capitalization fix on engineering page ("codex" → "Codex").

Full analysis: [runs/2026-06-27T09-15Z/analysis.md](runs/2026-06-27T09-15Z/analysis.md)

---

## 2026-06-26 — Run `2026-06-26T09-15Z`

**Fetch time:** 2026-06-26T09:17:38Z  
**Baseline:** 2026-06-24T09-15Z  
**Stats:** 1375 total URLs | +12 added | 82 updated | -3 removed | 0 anomalies | 34 sub-sitemaps

**TL;DR:** Two major posts dropped: OpenAI published an economic research piece showing Codex has entirely displaced ChatGPT as the primary AI tool inside OpenAI itself (99.8% of employee output tokens now go through Codex, including Legal and Recruiting), and announced a custom LLM inference chip co-developed with Broadcom code-named "Jalapeño." The business site got a structural overhaul — six new department-specific solution pages (finance, sales, marketing, design, data, engineering) and three new audience landing pages (enterprises, small business, startups) — with the old standalone `/startups/` page retired. The Codex ambassador form was quietly removed, and the trademark dispute form was renamed to explicitly scope it to trademark *counterfeiting*. 82 pages got lastmod bumps (continued post-Daybreak refresh), no anomalies.

### New Pages (12)

**⭐ [How agents are transforming work](pages/openai.com/index/how-agents-are-transforming-work/index.md)** (June 25, 2026)  
OpenAI's Economic Research paper measuring Codex's impact at the frontier. Key stats: by May 2026, Codex accounts for 99.8% of weekly output tokens generated within OpenAI. Every department — including Legal, Finance, and Recruiting — now uses Codex as its *primary* AI tool (not ChatGPT). Non-developer user adoption grew 137× for individuals and 189× for organizations since August 2025. Tasks are growing in horizon: 70% of sampled users made at least one Codex request estimated to represent >1 hour of human work. The paper frames this as evidence that "agentic AI changes the unit of knowledge work from single interactions to delegated, long-horizon tasks."

**⭐ [OpenAI and Broadcom unveil LLM-optimized inference chip ("Jalapeño")](pages/openai.com/index/openai-broadcom-jalapeno-inference-chip/index.md)** (June 24, 2026)  
OpenAI and Broadcom announced a custom inference chip designed as "the best inference platform for LLMs," with a nine-month tape-out timeline that was itself accelerated by OpenAI models. The post describes this as the first generation of a multi-generation platform, framed around making advanced AI more broadly available. This is OpenAI's first disclosed custom silicon effort, competing with Google's TPUs and Amazon's Trainium.

**Business site restructure — Solutions by department (6 new pages):**  
New depth-of-funnel pages targeting buyers by business function, each with role-specific messaging and case studies:
- [Finance](pages/openai.com/business/solutions/finance/index.md) — "Frontier AI for your finance team's most ambitious work"
- [Sales](pages/openai.com/business/solutions/sales/index.md)
- [Marketing](pages/openai.com/business/solutions/marketing/index.md)
- [Design](pages/openai.com/business/solutions/design/index.md)
- [Data](pages/openai.com/business/solutions/data/index.md)
- [Engineering](pages/openai.com/business/solutions/engineering/index.md)

**Business site restructure — Audience landing pages (3 new pages, 1 removed):**  
New segmented landing pages replacing the old generic `/startups/`:
- [For Enterprises](pages/openai.com/business/why-openai/enterprises/index.md)
- [For Small Business](pages/openai.com/business/why-openai/small-business/index.md)
- [For Startups](pages/openai.com/business/why-openai/startups/index.md) — replaces the removed `/startups/`

**[Trademark & Counterfeit Disputes form](pages/openai.com/form/trademark-counterfeit-disputes/index.md)**  
Replacement for the old `/form/trademark-disputes/` form. The new name specifically scopes it to trademark *counterfeiting*, suggesting the form was narrowed or restructured.

### Removed Pages (3)

- **`/form/codex-ambassadors/`** — Codex ambassador program form quietly removed. No replacement page announced.
- **`/startups/`** — Replaced by `/business/why-openai/startups/` as part of the business site restructure.
- **`/form/trademark-disputes/`** — Replaced by `/form/trademark-counterfeit-disputes/` (renamed with narrower scope).

### Notable Updates

- **[Daybreak hub](pages/openai.com/daybreak/index.md)** — Updated again (second consecutive day); Cyber tier table and partner section further refreshed.
- **[Daybreak partner network](pages/openai.com/daybreak/partners/index.md)** — Updated; additional partner details added.
- **[Release notes](pages/openai.com/products/release-notes/index.md)** — Updated June 26; new entries for recent product releases.
- **[Supplier security measures policy](pages/openai.com/policies/supplier-security-measures/index.md)** — First update since April 6, 2026; policy document revised.
- **[Commerce policies](pages/openai.com/policies/commerce-policies/index.md)** — Updated June 25; terms or prohibited-use language revised.
- 62 additional pages with lastmod bumps (ongoing CMS refresh, mostly customer stories and product pages).

Full analysis: [runs/2026-06-26T09-15Z/analysis.md](runs/2026-06-26T09-15Z/analysis.md)

---
## 2026-06-24 — Run `2026-06-24T09-15Z`

**TL;DR:** OpenAI launched the full **Daybreak** cybersecurity platform today — a major expansion of its AI-for-defense initiative. Five new pages launched (a Codex Security plugin setup guide, a 20+ company partner directory, a contact-cyber-sales page, and two major blog posts), the old "request a vulnerability scan" page was retired and replaced by a structured enterprise funnel, and the homepage was updated to feature the Daybreak announcement. Alongside Daybreak, OpenAI published a GPT-5 immunology success story, a Codex whitepaper on long-running agentic work, a new Omio customer story, and an AI governance post announcing the Appia Foundation (a Linux Foundation-hosted body for shared AI safety standards). The API pricing page gained a processing-mode selector UI (Standard / Batch / Data residency), and 131 URLs total had their `<lastmod>` updated reflecting June 22–24 content refreshes. No anomalies detected.

### New Pages (9)

**⭐ [Daybreak: Tools for securing every organization in the world](pages/openai.com/index/daybreak-securing-the-world/index.md)** (June 22, 2026)  
The anchor announcement for the full Daybreak launch. OpenAI is expanding its AI-powered cybersecurity initiative with Codex Security (AI vulnerability scanning + patch generation), the full release of GPT-5.5-Cyber (three tiers: default, Trusted Access for Cyber, and a restricted red-team mode), and a "Patch the Planet" initiative to auto-discover and patch vulnerabilities in major open-source projects (FreeBSD, Linux kernel, browsers). The stated goal: move past vulnerability *discovery* and into machine-speed end-to-end *patch automation*, with 20+ security company partners integrating these capabilities.

**⭐ [Patch the Planet](pages/openai.com/index/patch-the-planet/index.md)** (June 22, 2026)  
Dedicated post for the Daybreak open-source initiative. Describes a full pipeline — AI finds the bug, validates it, generates a patch, coordinates disclosure, and helps land the fix with the upstream maintainer. Early work covers OS-level vulnerabilities in FreeBSD and the Linux kernel, network infrastructure, and major browsers. Open-source maintainers are invited to participate.

**[Daybreak platform hub](pages/openai.com/daybreak/index.md)** (updated, first seen earlier)  
The `/daybreak/` hub page was significantly expanded with a GPT-5.5-Cyber tier comparison table, Codex Security plugin CTAs, a "Trusted by leading security organizations" section, and a grid of partner logos. Access tiers: GPT-5.5 (default, available now), GPT-5.5 with Trusted Access for Cyber (enterprise), GPT-5.5-Cyber (controlled preview for red-teamers/pentesters).

**[Codex Security plugin setup guide](pages/openai.com/daybreak/codex-security-plugin/index.md)** (new, June 24)  
Step-by-step guide to installing and running the @CodexSecurity plugin inside Codex (OpenAI's agentic coding tool) or via the Codex CLI. Self-serve vulnerability scanning, routing to the appropriate GPT-5.5-Cyber tier based on use case.

**[Daybreak Cyber Partner Program](pages/openai.com/daybreak/partners/index.md)** (new, June 24)  
Lists 20+ named security partners — including Akamai, Cato Networks, Check Point, CrowdStrike, Fortinet, Palo Alto Networks, Rapid7, and SentinelOne — integrating Daybreak/GPT-5.5 capabilities into their products. Includes quotes from CxOs at each partner and a "Become a partner" signup form.

**[Contact Cyber sales](pages/openai.com/daybreak/contact-cyber-sales/index.md)** (new, June 24)  
Enterprise sales contact page for Daybreak. Replaces the retired `/daybreak/request-a-vulnerability-scan/` page (see Removals).

**[How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery](pages/openai.com/index/gpt-5-immunology-mystery/index.md)** (June 23, 2026)  
Applied AI story: immunologist Dr. Unutmaz used GPT-5 Pro to surface literature connections that solved a years-old puzzle about immune cells involved in fighting cancer and infections. OpenAI's case for GPT-5 augmenting human expertise in specialized biomedical research.

**[Codex-maxxing for long-running work](pages/openai.com/index/codex-maxxing-long-running-work/index.md)** (June 22, 2026)  
A whitepaper (by Jason Liu) on using Codex as a persistent workspace for complex multi-session AI projects — breaking goals into verifiable steps, maintaining context across workstreams, and knowing when to delegate vs. apply human judgment. Links to a full PDF on the OpenAI CDN.

**[Helping build shared standards for advanced AI](pages/openai.com/index/helping-build-shared-standards-for-advanced-ai/index.md)** (June 23, 2026)  
OpenAI announces it helped found the **Appia Foundation** (hosted by the Linux Foundation), which will develop open, modular AI safety specifications enabling cross-jurisdiction third-party evaluations. Connects to the Preparedness Framework, Frontier Governance Framework, and OpenAI's existing standards work (ISO/IEC SC42, NIST AISIC, Frontier Model Forum, CoSAI, C2PA, IETF, FIDO Alliance).

**[Omio customer story](pages/openai.com/index/omio/index.md)** (June 23, 2026)  
Travel platform Omio using OpenAI for AI-powered trip planning and conversational booking. Mid-market enterprise story accompanying the major product launch cadence.

### Removed Pages (1)

**`/daybreak/request-a-vulnerability-scan/`** — Retired and replaced by the new `codex-security-plugin` (self-serve) and `contact-cyber-sales` (enterprise) pages. Signals a shift from one-off scan requests to a structured product-and-sales funnel.

### Notable Updates

**[API Pricing](pages/openai.com/api/pricing/index.md)** (lastmod Jun 11 → Jun 24)  
Added a new "Choose your processing mode" selector (Standard / Batch -50% / Data residency +10%). Prices for GPT-5, GPT-5.4, and GPT-5.4 mini are unchanged. Formatting of the price table was compacted.

**[Business Pricing](pages/openai.com/business/pricing/index.md)** (lastmod Jun 18 → Jun 24)  
Section header changed from "ChatGPT & Codex" to "Business" — minor branding alignment.

**[Homepage](pages/openai.com/index.md)** (lastmod Jun 18 → Jun 22)  
Daybreak announcement now featured in the main news carousel.

**~128 listing/news/customer-story pages** — Cascading `<lastmod>` bumps as the 9 new pages inserted themselves into site carousels and feeds. No substantive body content changes in spot-checked examples.

### Fetch Failures (1)

`/index/waymark/` — Transient TLS error during the batch fetch. Prior snapshot preserved in git. Will retry next run.

---

_Stats: 1,366 total URLs | +9 added | 131 lastmod-updated | 1 removed | 0 anomalies | 0 anomaly type | 34 sub-sitemaps_

_Full analysis: [runs/2026-06-24T09-15Z/analysis.md](runs/2026-06-24T09-15Z/analysis.md)_

---


## 2026-06-22 — Run `2026-06-22T09-15Z`

**TL;DR:** The standout addition is a major enterprise deployment announcement: **Samsung Electronics** is rolling out ChatGPT Enterprise and Codex to all employees in Korea and all Device eXperience (DX) division employees worldwide — one of OpenAI's largest enterprise deployments ever, with Codex weekly active users in Korea up ~800% since February 2026. Beyond that, 123 URLs had their `<lastmod>` timestamps refreshed, but the vast majority reflect CMS-level touch-ups (sidebar/related-articles rotation) rather than body content changes. Pages from the past week worth noting include GPT-5.5-Cyber for critical infrastructure defenders, LifeSciBench (a new expert-written life-science AI benchmark), GPT-Rosalind capability updates, and new ChatGPT Enterprise spend controls. One benign anomaly: the Release Notes page reports a `<lastmod>` fractionally in the future — its CMS sets timestamps at serve time.

### Anomalies

**`openai.com/products/release-notes/` — CMS-dynamic `<lastmod>`:** The timestamp `2026-06-22T09:17:11.130Z` is milliseconds *after* our 09:17:11Z fetch time. OpenAI's CMS appears to write the current server time into `<lastmod>` at sitemap-serve time for this page. No actual content change. This is a known CMS anti-pattern; worth watching to see if it recurs on future runs.

### New Pages (1)

**[Samsung Electronics brings ChatGPT and Codex to employees](pages/openai.com/index/samsung-electronics-chatgpt-codex-deployment/index.md)** ⭐ (published June 21, 2026) — Company  
Samsung Electronics is deploying ChatGPT Enterprise and Codex to all employees in Korea and all Device eXperience (DX) division employees globally — one of OpenAI's largest enterprise launches. Key stats: 5M+ people use Codex weekly; Codex weekly active users in Korea grew ~800% since February 1, 2026. Use cases span software development, marketing, manufacturing, and other non-technical functions. The deployment also expands an existing Samsung–OpenAI relationship that previously focused on AI infrastructure (Samsung supplying advanced memory chips). The same announcement notes ChatGPT Edu reaching Seoul National University's 47,000 members and integrations with KakaoTalk, LG Electronics, LG Uplus, and other Korean enterprises.

### Notable Updates

**~53 pages (bulk CMS republish, ~04:56–04:59 UTC):** A large batch of customer stories and brand pages received simultaneous timestamp bumps. Diffs confirm these are sidebar/related-articles rotations — the Samsung Electronics article was inserted into page carousels, displacing older articles. No body text changed.

**[GPT-5.5 and GPT-5.5-Cyber for Cybersecurity Defenders](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md)** — Published May 7, 2026; lastmod bumped from Jun 14 → Jun 22. Details the limited preview rollout of GPT-5.5-Cyber to defenders responsible for critical infrastructure, alongside Trusted Access for Cyber (TAC) safeguards. Diff: whitespace only.

**[Introducing New Capabilities to GPT-Rosalind](pages/openai.com/index/introducing-new-capabilities-to-gpt-rosalind/index.md)** — Published June 3, 2026; lastmod bumped Jun 18 → Jun 22. Enhancements to OpenAI's life-sciences model: stronger reasoning in medicinal chemistry, genomics, quantitative biology, and real-world lab workflow integration. Sidebar-only diff.

**[Introducing LifeSciBench](pages/openai.com/index/introducing-life-sci-bench/index.md)** — Published June 17, 2026; lastmod bumped Jun 18 → Jun 22. A new benchmark for evaluating AI on realistic life science research tasks — 750 expert-authored tasks, 173 scientist contributors, 19,020 rubric criteria across 7 workflow categories. Sidebar-only diff.

**[ChatGPT Enterprise Spend Controls & Usage Analytics](pages/openai.com/index/chatgpt-enterprise-spend-controls/index.md)** — Published June 18, 2026; lastmod bumped Jun 19 → Jun 22. New Global Admin Console tracks ChatGPT + Codex credit usage together by user, product, and model. Admins set workspace/group/individual limits; employees can request overrides. Sidebar-only diff.

**[Deployment Simulation](pages/openai.com/index/deployment-simulation/index.md)** — Published June 16, 2026; lastmod bumped Jun 19 → Jun 22. Safety research: predicts model behavior before release by replaying real prior conversations. Sidebar-only diff.

**[Training to Cycle Across Antarctica with ChatGPT](pages/openai.com/index/cycling-across-antarctica/index.md)** — Human interest story about James Benson-King preparing to be the first to cycle solo and unsupported to the South Pole (planned November). Sidebar-only diff.

**[Policies / Commerce Policies](pages/openai.com/policies/commerce-policies/index.md)** — lastmod bumped Jun 21. No content diff detected.

**[OpenAI Partner Network](pages/openai.com/business/partners/index.md)** + **[Introducing the OpenAI Partner Network](pages/openai.com/index/introducing-openai-partner-network/index.md)** — lastmod bumped Jun 20. Partner network launched Jun 14; these pages received a minor sidebar refresh. No content change.

**[Startups page](pages/openai.com/startups/index.md)** — lastmod bumped Jun 20. No content diff detected.

### Removals
None.

---

*Stats: 1,358 total URLs | +1 added | 123 lastmod-updated | 0 removed | 1 anomaly (dynamic CMS timestamp) | 0 fetch failures | 34 sub-sitemaps*

*Full analysis: [runs/2026-06-22T09-15Z/analysis.md](runs/2026-06-22T09-15Z/analysis.md)*

---

## 2026-06-19 — Run `2026-06-19T09-15Z`

**TL;DR:** OpenAI made a coordinated health AI push today: three new pages announced **GPT-5.5 Instant**'s improved health capabilities for ChatGPT's 230M+ weekly health users, a peer-reviewed NEJM AI study using an OpenAI reasoning model to surface 18 diagnoses from 376 previously unsolved rare pediatric disease cases, and new enterprise spend controls for ChatGPT/Codex credit management. The model versioning page for GPT-5.5 Instant incidentally reveals a fuller model lineage: 5.3 Instant (March 2026) → 5.5 Instant (May 2026), plus 5.4 Thinking and 5.5 Thinking variants. A large batch of ~80 customer story pages received simultaneous CMS re-publishes with no content changes, plus ~10 Codex Academy pages similarly refreshed. No anomalies, no removals.

### Anomalies
None.

### New Pages (3)

**[Improving health intelligence in ChatGPT](pages/openai.com/index/improving-health-intelligence-in-chatgpt/index.md)** ⭐ (published June 18, 2026) — Product  
OpenAI announces that GPT-5.5 Instant (released May 2026) delivers frontier-class health intelligence to all free ChatGPT users. Over 230 million people use ChatGPT for health and wellness questions weekly; this model now performs comparably to frontier Thinking models on HealthBench and HealthBench Professional — a substantial step forward from GPT-5.3 Instant (March 2026). The model was shaped by a global physician network that defines ideal health response behavior. Improvements include better recognition of urgent care situations, more relevant contextual questioning, and clearer communication of uncertainty. The page also confirms the existence of GPT-5.4 Thinking and GPT-5.5 Thinking as separate API-accessible variants, providing a more complete picture of the model family.

**[Using AI to help physicians diagnose rare genetic diseases affecting children](pages/openai.com/index/diagnose-rare-childhood-diseases/index.md)** ⭐ (published June 18, 2026) — Applied AI  
Documents a study published in NEJM AI (New England Journal of Medicine's AI journal) in which researchers used an OpenAI reasoning model to reanalyze 376 previously unsolved pediatric rare genetic disease cases. The model surfaced diagnostic leads for **18 cases** — diseases that had resisted prior analysis. The study is peer-reviewed and links to the abstract at ai.nejm.org. OpenAI categorizes this as "Applied AI," underscoring its push to demonstrate real-world clinical impact alongside consumer health improvements.

**[New usage analytics and updated spend controls for enterprises](pages/openai.com/index/chatgpt-enterprise-spend-controls/index.md)** (published June 18, 2026) — Product  
Enterprise admins now get a unified Global Admin Console that tracks ChatGPT and Codex credit consumption together, with breakdowns by user, product, and model. A new Cost API makes this data accessible to customer systems. Admins can set workspace defaults, group-level limits, and individual overrides; employees see their own usage versus budget and can request additional credits with context. Quote from Zipline co-founder confirms this was specifically requested by enterprise customers as Codex adoption spread beyond engineering into broader teams. This rounds out the "usage analytics" and "spend controls" features that first appeared as bullet points on the ChatGPT Business pricing page in yesterday's run.

### Notable Updates

**Homepage (`openai.com/`)** — Featured content updated: "Improving health intelligence in ChatGPT" (Jun 18) replaces "ChatGPT Images 2.0" in the hero/spotlight slot.

**[GPT-5.1 page](pages/openai.com/index/gpt-5-1/index.md)** — Gained a table of contents (sections: "GPT-5.1 Instant", "GPT-5.1 Thinking", "Making ChatGPT uniquely yours", "What's next") indicating a structural expansion; also rotated featured articles to include today's spend controls and health intelligence pages.

**[Business Partners page](pages/openai.com/business/partners/index.md)** — New partner logos added: HCLTech, Altimetrik, Accenture Federal Services, and Artefact. Footer link renamed from "Introducing Frontier Alliances" → "Introducing the OpenAI Partner Network," reflecting the rebrand/re-launch announced last week.

**[Public Policy Agenda](pages/openai.com/index/public-policy-agenda/index.md)** — Got a detailed table of contents making 5 named policy areas prominent: Frontier model safety/security/accountability, Youth safety, Education and AI literacy, Workforce and economic transition, and Deepfakes and content provenance.

**[EU Code of Practice](pages/openai.com/global-affairs/eu-code-of-practice/index.md)** — Related articles updated to reflect recent EU-focused content (supporting EU trustworthy AI ecosystem, PRC-linked influence operations).

**~80 customer story / brand story pages** — Simultaneous lastmod refresh around 2026-06-19T04:47Z. No content changes detected in spot-checked pages; CMS batch republish.

**~10 Codex Academy pages** — Simultaneous lastmod refresh around 2026-06-19T00:39Z. No content changes detected; likely a template or metadata update.

### Removals
None.

---

*Stats: 1,357 total URLs | +3 added | 132 lastmod-updated | 0 removed | 0 anomalies | 0 fetch failures | 34 sub-sitemaps*

*Full analysis: [runs/2026-06-19T09-15Z/analysis.md](runs/2026-06-19T09-15Z/analysis.md)*

---

## 2026-06-17 — Run `2026-06-17T09-15Z`

**TL;DR:** OpenAI formally launched the **OpenAI Partner Network** today — its most significant B2B ecosystem move yet — pairing a $150 million investment with a tiered program that currently counts ~26 founding partners (Accenture, AWS, BCG, Bain, McKinsey, PwC, Snowflake, Databricks, Capgemini, and more). The goal is to train 300,000 certified AI consultants by end of 2026. Separately, OpenAI published safety research on **Deployment Simulation**, a method for replaying real user conversations against candidate models before release to surface safety blind spots. A site-wide sitemap rebuild touched 349 URLs with fresh timestamps — all today's date, no substantive content changes detected. Zero true anomalies, zero removals.

### Anomalies
None. (The pipeline initially flagged 115 "future_lastmod" entries, but these are false positives: OpenAI's CMS stores full ISO 8601 timestamps in `<lastmod>`, and a date-only string comparison against today's date treats any same-day timestamp as "future." All 349 refreshed entries are from today, consistent with a CMS rebuild triggered by the Partner Network publication.)

### New Pages (4)

**[OpenAI Partner Network](pages/openai.com/business/partners/index.md)** ⭐ — *openai.com/business/partners/*
OpenAI's new hub for its partner ecosystem. ~26 founding organizations listed across four categories: management consulting (Accenture, Bain, BCG, McKinsey, PwC, EY), global systems integrators (Capgemini, CGI, Cognizant, Infosys, NTT DATA, Globant), cloud/data platforms (AWS, Databricks, Snowflake), and specialized AI firms (Dentsu, Endava, Fractal, ML6, Unit8, Deepsense, Slalom, others). Program structure: **three tiers** (Select → Advanced → Elite), **specializations** in Codex, cybersecurity, and agents, and a **Forward Deployed Experts** pilot that embeds qualified partner practitioners alongside OpenAI's own Forward Deployed Engineering teams. Login portal: partners.openai.com.

**[Introducing the OpenAI Partner Network](pages/openai.com/index/introducing-openai-partner-network/index.md)** ⭐ — *published June 14, 2026*
Official announcement post. Key quote: *"The limiting factor for seeing value from AI in the enterprise is no longer model capabilities. Instead, it's how organizations repeatably identify the right use cases, redesign workflows, integrate with existing systems, and drive adoption and change management at scale."* OpenAI is investing **$150 million** in this ecosystem and aims for **300,000 certified consultants** by end of 2026. Includes endorsement quotes from Accenture (Dr. Lan Guan), Bain (Chuck Whitten), BCG (Sylvain Duranton), McKinsey (Ben Ellencweig), PwC (Tyson Cornell), and Eliza (Stephen Garden). Customer success cases: Agilent+BCG, eBay+Artium, Paychex+Bain, T-Mobile+Accenture.

**[OpenAI Partner Network Interest Form](pages/openai.com/form/partner-network-interest/index.md)** — *openai.com/form/partner-network-interest/*
Application form for organizations wanting to join the Partner Network. Solicits company name, contact info, and capabilities. Targets companies with "strong customer relationships, proven AI implementation experience, and a clear commitment to building with OpenAI."

**[Predicting model behavior before release by simulating deployment](pages/openai.com/index/deployment-simulation/index.md)** ⭐ — *published June 16, 2026*
Safety research paper: **Deployment Simulation** is a method for assessing how a new model will behave once deployed by replaying prior user conversations (in a privacy-preserving manner) against the candidate model. Applied to multiple GPT-5 series Thinking deployments; helped surface novel misalignment before release, reduce "evaluation awareness" (models gaming evals), and extend safety coverage to agentic tool-use scenarios. OpenAI says it has "already used insights from Deployment Simulation during model development to identify blind spots in traditional evaluations." Full paper: cdn.openai.com/pdf/predicting-llm-safety-before-release-by-simulating-deployment.pdf

---

### Updated Pages
349 URLs received updated `<lastmod>` timestamps, all dated 2026-06-17. This is consistent with a CMS-wide rebuild triggered by the Partner Network publication. No substantive content changes detected in spot-checked pages. Categories affected: customer stories, product pages, Academy/Codex content, global affairs, policy pages.

### Removals
None.

---

*Stats: 1,353 total URLs | +4 added | 349 lastmod-refreshed | 0 removed | 0 true anomalies | 0 fetch failures | 34 sub-sitemaps*

*Full analysis: [runs/2026-06-17T09-15Z/analysis.md](runs/2026-06-17T09-15Z/analysis.md)*

---
## 2026-06-18T09-15Z

**TL;DR:** OpenAI published a new life science AI benchmark called **LifeSciBench** today — 750 expert-written research tasks across 7 biology domains created by 173 PhD scientists, designed to test whether AI can handle real wet-lab research workflows rather than trivia-style questions. The Business/Enterprise pricing pages were updated to explicitly call out "Usage analytics, budgeting, and spend controls" as a plan feature (previously the Business tier was described only as a "collaborative workspace"). 132 total URLs updated, mostly reflecting the new LifeSciBench content propagating through site-wide "recently published" sidebars. No anomalies.

### New Pages

**[Introducing LifeSciBench](pages/openai.com/index/introducing-life-sci-bench/index.md)** ⭐ (published June 17–18, 2026) — Research  
OpenAI's new benchmark for evaluating AI on life science research tasks. Key facts:
- **750 expert-authored tasks** across 7 research workflows (evidence handling, analysis, design & optimization, scientific reasoning, validation & operations, translation, scientific communication) and 7 biological domains
- **173 PhD-level contributors** from biotech/pharma; each task went through ≥2 rounds of expert review (≥90% reviewer agreement required)
- **1,062 attached artifacts** — figures, PDFs, sequence files, structure files, chemical files; 53% of tasks require interpreting at least one artifact
- **79% of tasks require multi-step reasoning** (average 4 steps)
- A [preprint PDF is available](https://cdn.openai.com/pdf/b4299379-0a97-4ffa-8b9b-c3fbb299caa9/lifescibench_preprint.pdf)
- Contextualizes against: OpenAI's existing biosecurity/life-science push (Rosalind 5.5 released earlier this month, "Accelerating Biological Research in the Wet Lab" post)

### Notable Updates

**[ChatGPT Business Pricing](pages/openai.com/business/chatgpt-pricing/index.md)** and **[Business Pricing](pages/openai.com/business/pricing/index.md)** (updated June 18, 2026)  
Both pages now list **"Usage analytics, budgeting, and spend controls"** as a key Business plan feature. The prior wording described the Business tier as "A secure, collaborative workspace for startups and growing businesses" — this new bullet is the first explicit mention of spend controls as a selling point, suggesting it's either a newly rolled out capability or newly prominent in their pitch to corporate buyers.

**[Building ChatGPT Atlas](pages/openai.com/index/building-chatgpt-atlas/index.md)** (updated June 18, 2026)  
This engineering deep-dive on the ChatGPT desktop renderer added a table of contents / in-page navigation section, making it easier to jump to specific sections like "Rendering: Getting pixels across the process boundary" and "Input events: Cracking and forwarding."

**Site-wide "Latest Content" rotation (86 `page` + 11 `openai-academy` + others)**  
The large wave of 132 updates is mostly sidebar churn: OpenAI's content templates include a "recently published" widget, and publishing LifeSciBench today triggered a repropagation across the site. The LifeSciBench thumbnail (asset ID `1iV0eZRf28MZRvIxYY`) now appears as the featured image on dozens of customer story and research pages, replacing the prior Rosalind 5.5 and Academy thumbnails.

**Stats:** 1354 total URLs | +1 added | ~132 updated | -0 removed | 0 anomalies | 34 sub-sitemaps

---
## 2026-06-13 — Run `2026-06-13T09-15Z`

**TL;DR:** OpenAI launched a comprehensive advertising platform today, upgrading the narrow "Conversion Tools" product into a full "Ad Tools" suite that now includes **audience targeting** (upload your customer list, OpenAI builds custom audiences) and **AI Creative Tools** (use OpenAI's models to generate and optimize ad creatives). Three new policy pages published June 12–13; two older Conversion pages removed and superseded. Separately, OpenAI Academy got a major refresh — new "Applying AI at Work" courses announced, completion certificates added, and all Academy pages updated. Codex gained **Windows support** today (previously macOS-only). The homepage removed its "Learn about ChatGPT Business" hero link and promoted "Stories" instead. 170 total sitemap updates, mostly nav/template refreshes across the site. Zero anomalies.

### Anomalies
None detected.

### New Pages (4)

**[OpenAI Ad Tools Terms](pages/openai.com/policies/ad-tools-terms/index.md)** ⭐ (published June 12, 2026) — Policy  
Establishes the legal framework for OpenAI's expanded advertising platform. Three tools covered: **(1) Conversion Tools** — unchanged from prior Conversion Terms, now incorporated by reference. **(2) Audience Data tools** — advertisers can upload first-party customer data so OpenAI builds custom audiences for ad targeting; strict rules: no data brokers, no third-party data enrichment, no inferring sensitive info about people, expressly prohibiting re-identification of OpenAI users. **(3) AI Creative Tools** — advertisers use OpenAI's AI to generate, modify, optimize, localize, and translate ads from their own brand materials; advertiser is fully responsible for verifying all factual claims in AI-generated creatives, including pricing, endorsements, and qualifications. This is a significant expansion: OpenAI now has the contractual framework for audience-targeted advertising (akin to Facebook Custom Audiences) and AI-generated ad creative (a new product category).

**[OpenAI Ad Tools Data Processing Addendum](pages/openai.com/policies/ad-tools-dpa/index.md)** ⭐ (effective June 12, 2026) — Policy  
The GDPR-compliant companion to the Ad Tools Terms. Establishes that OpenAI and advertisers are **independent data controllers** for most ad processing — not joint controllers and not processor/controller — with a narrow carve-out for "Restricted Processing" where OpenAI acts as data processor under the advertiser's instructions. Replaces the old Conversion DPA (effective May 14, 2026).

**[OpenAI Ad Tools Sub-Processor List](pages/openai.com/policies/ad-tools-subprocessors/index.md)** (updated June 12, 2026) — Policy  
Lists entities processing personal data for Ad Tools. Includes Cloudflare (CDN) and Microsoft (cloud infrastructure). Replaces the old Conversion Sub-Processor List.

**[New OpenAI Academy courses for the next era of work](pages/openai.com/index/academy-courses-applying-ai-at-work/index.md)** (June 12, 2026) — AI Adoption  
Product announcement for a refreshed Academy curriculum. Structured courses from AI fundamentals to repeatable workflows, completion certificates, organization-level enrollment for enterprises.

---

### Notable Updates

**[Codex](pages/openai.com/codex/index.md) — Now Available on Windows** (updated June 12, 2026)  
The Codex product page now reads "Available on macOS and Windows" with a new Microsoft Store installer link. Previously macOS-only.

**[OpenAI Academy](pages/openai.com/academy/index.md) — Major Refresh** (updated June 12, 2026)  
All eight Academy category pages updated simultaneously alongside the new course announcement. The Academy homepage now highlights "completion certificates" as a key feature. The "Codex for Everyday Work" article got new content about giving Codex rich workplace context (calendars, emails, docs, spreadsheets) rather than blank prompts.

**[Homepage](pages/openai.com/index.md)** (updated June 12, 2026) — "Learn about ChatGPT Business" hero link removed; "Stories" link added in its place.

**[Business Customer Stories](pages/openai.com/business/customer-stories/index.md)** (updated June 12, 2026) — **Preply** added ("How Preply combines AI and human tutors to personalize learning" — language learning platform with 95% weekly-active ChatGPT usage among employees). BBVA also newly featured.

**Bulk nav/template updates (~128 pages)** — The "Stories" link was added to hero sections across the site, and some footer links updated (e.g., `chatgpt.com/business/business-plan` → `/business/`). Template-wide propagation accompanying the Academy relaunch.

---

### Removals (2)

Superseded by new Ad Tools equivalents:

- `https://openai.com/policies/conversion-dpa/` → replaced by `/policies/ad-tools-dpa/`
- `https://openai.com/policies/conversion-subprocessors/` → replaced by `/policies/ad-tools-subprocessors/`

---

*Stats: 1,349 total URLs | +4 added | 170 updated | 2 removed | 0 anomalies | 0 fetch failures | 34 sub-sitemaps*

*Full analysis: [runs/2026-06-13T09-15Z/analysis.md](runs/2026-06-13T09-15Z/analysis.md)*

---
## 2026-06-12 — Run `2026-06-12T09-15Z`

**TL;DR:** OpenAI announced the **acquisition of Ona**, a cloud-execution and orchestration company, in what is the biggest news on OpenAI's site today. Ona's technology lets Codex agents run continuously inside a customer's own cloud environment even after the user's laptop is closed — addressing a key enterprise requirement for long-running agentic work. Codex now claims 5 million weekly users, up 400% from earlier this year. A new brand story for Preply (language learning) also launched. The 273 other `<lastmod>` changes across the sitemap appear to be a CMS rebuild artifact with no observable content changes. Zero anomalies, zero removals.

### Anomalies
None detected.

### New Pages (2)

**[OpenAI to acquire Ona](pages/openai.com/index/openai-to-acquire-ona/index.md)** ⭐ (Jun 11, 2026) — Company Announcement  
OpenAI is acquiring **Ona** (ona.com), a company that has given 2 million developers secure, reproducible cloud development environments. The deal is framed as giving Codex a "persistent place to work" — agents will be able to continue executing inside a customer's own cloud infrastructure beyond any single session, with the organization retaining control over where code runs, what it can access, how credentials are scoped, and how activity is logged. Ona's customer-controlled execution model is described as complementary to OpenAI's model intelligence and orchestration. The acquisition is subject to regulatory approval; until closing the companies remain independent. After closing, Ona's team joins OpenAI's Codex team. Quoted: Johannes Landgraf (Ona CEO): *"Agents need more than intelligence; they need a trusted workspace."* Thibault Sottiaux (OpenAI Core Products Lead): *"Enterprises want powerful agents that can do real work while meeting the security and control requirements of their environments."* This follows the Dell Codex partnership (May 18), the Oracle cloud commitment (Jun 10), and the confidential S-1 filing (Jun 8) — a clear pattern of enterprise-infrastructure moves ahead of IPO.

**[How Preply combines AI and human tutors to personalize learning](pages/openai.com/index/preply/index.md)** (Jun 12, 2026) — Brand Story  
New customer case study for **Preply**, a global language learning platform. Key reported metrics: 95% ChatGPT weekly active usage among Preply employees; 70%+ of tutors actively use the AI-powered Lesson Insights feature. Preply uses ChatGPT, the API, and Codex. Industry: Technology/Education. The article focuses on AI-generated lesson summaries that provide personalized feedback to language learners and their tutors.

---

### Notable Updates

**`/index/built-to-benefit-everyone-our-plan/`** — "Keep reading" section rotated: Ona acquisition is now the lead featured story, displacing the S-1 filing. Standard news ticker update.

**`/business/customer-stories/`** — Grid refreshed: **BBVA** banking story ("BBVA puts AI at the core of banking with OpenAI") added to featured cards; **Warp** story rotated off the grid (page still exists in sitemap).

**Pricing pages** (`/business/pricing/`, `/business/chatgpt-pricing/`, `/api/pricing/`) — `<lastmod>` timestamps updated; no content changes detected.

---

### Removals
None.

---

*Stats: 1,347 total URLs | +2 added | 273 sitemap-updated | 0 removed | 0 anomalies | 0 fetch failures | 34 sub-sitemaps*

*Full analysis: [runs/2026-06-12T09-15Z/analysis.md](runs/2026-06-12T09-15Z/analysis.md)*

---

## 2026-06-11 — Run `2026-06-11T09-16Z`

**TL;DR:** OpenAI launched a new "Applied AI" content section today — a distinct editorial category for real-world AI application stories, complete with its own sitemap sub-section (the 34th, up from 33). The inaugural article showcases a computational astrophysicist using Codex to generate and test mathematical algorithms for black hole simulations that are 1000× faster than current methods. Alongside that, a ChatGPT user story features a man training to become the first person to cycle Antarctica solo. On the policy front: OpenAI announced formal support for the EU's Code of Practice on AI-generated content transparency (part of EU AI Act implementation), published a threat report on PRC-linked influence operations targeting US AI debates, and announced an Oracle Cloud partnership allowing OCI customers to pay for OpenAI models with their existing Oracle credits. No pages removed; 0 anomalies.

### Anomalies
None detected.

### Structural Change: New "Applied AI" Sub-Sitemap

A new sub-sitemap (`sitemap.xml/applied-ai/`) appeared in the sitemap index today, bringing the total from 33 to 34. The corresponding news section page at `/news/applied-ai/` joins the existing news categories (Company, Research, Product, Safety, Engineering, Security, Global Affairs, AI Adoption). Currently the Applied AI section contains one article—the astrophysicist/Codex piece—suggesting this is a newly launched content vertical.

### New Pages (7)

**[How an astrophysicist uses Codex to help simulate black holes](pages/openai.com/index/using-codex-to-simulate-black-holes/index.md)** (Jun 11, 2026) — Applied AI (new category)  
The inaugural "Applied AI" article. Astrophysicist Chi-kwan "CK" Chan (University of Arizona / Event Horizon Telescope) uses Codex to derive and test new numerical algorithms for simulating black hole plasma. Standard algorithms must track every microscopic spiral of charged particles, making even supercomputers impractical. Codex generates candidate mathematical transformations in minutes vs. ~10 days by hand—though many fail and Chan tests each one rigorously. Quote: *"We don't accept an idea because it came from Einstein, from a bright student, or from an AI model. We accept it only after repeated testing."* If successful, the algorithms could unlock simulations of trillions of particles that are currently impossible.

**[Creating new simulations of black holes with Codex](pages/openai.com/index/creating-new-simulations-black-holes/index.md)** (Jun 11, 2026)  
Visual/photo essay companion to the above ("Project Owl" storytelling format, photos from Kitt Peak National Observatory). Adds context: Codex can speed up calculations "by a factor of 1000," Chan and his team are currently gathering data, and their goal is to release the first *moving image* of a black hole in 2027. Quote: *"It would take me ten days to come up with ten new approximations. With Codex, this can be done in minutes."*

**[Training to cycle across Antarctica with ChatGPT](pages/openai.com/index/cycling-across-antarctica/index.md)** (Jun 11, 2026)  
James Benson-King plans to attempt (November 2026) the first solo, unsupported cycle from the edge of Antarctica to the South Pole—up to 60 days. No standard training plan exists. He used ChatGPT to build a unified training system covering endurance, strength, cold-weather skills, and technical cycling simultaneously. Quote: *"Within just over a year, I feel competent enough to tackle Antarctica... I think I've managed to turn around in one year what potentially would have taken me two, three years."*

**[Supporting Europe's work in ensuring a trustworthy AI ecosystem](pages/openai.com/index/supporting-eu-trustworthy-ai-ecosystem/index.md)** (Jun 11, 2026) — Global Affairs  
OpenAI formally endorses the European Commission's Code of Practice on Transparency of AI-Generated Content (implementing the EU AI Act). Details the multi-layered approach: C2PA metadata on DALL·E 3 images (since 2024), SynthID watermarks on all ChatGPT/Codex/API-generated images, and a public verification tool at [openai.com/verify](/research/verify/). Acknowledges that metadata can be stripped and that provenance is "a nascent field" requiring continued ecosystem cooperation.

**[PRC-linked influence operations are targeting AI debates in the US](pages/openai.com/index/prc-linked-influence-operations-ai-debates/index.md)** (Jun 10, 2026) — Global Affairs  
OpenAI threat report: two clusters of ChatGPT accounts likely originating from China were identified and banned for using the model in covert influence operations targeting US AI/tech policy debates. **"Data Center Bandwagon"**: generated content claiming AI data center buildouts raised electricity prices for families. **"Tech and Tariffs"**: generated anti-tariff content (with instructions to exclude Xi Jinping from outputs), connected to accounts spreading false claims that ChatGPT user data was compromised. OpenAI found no evidence either campaign broke out beyond its own activity. Full PDF report linked. The report emphasizes these campaigns were testing narratives against "AI infrastructure — a foundation of US technological leadership."

**[Access OpenAI models and Codex through your Oracle cloud commitment](pages/openai.com/index/openai-on-oracle-cloud/index.md)** (Jun 10, 2026) — Partnerships / API Platform / Codex  
Oracle Cloud Infrastructure customers will be able to apply existing Oracle Universal Credits toward OpenAI frontier models and Codex. Availability "in the coming weeks." Framed as reducing procurement friction for enterprises already committed to Oracle. Contact your Oracle sales rep for details.

**[Applied AI news section](pages/openai.com/news/applied-ai/index.md)** — New section landing page  
The new `/news/applied-ai/` section page, added to the news category navigation. Currently lists one article (the black holes/Codex piece).

---

### Notable Updates

**Homepage** — Featured stories updated: Antarctica cycling and black holes/Codex stories now prominently featured. Chip Ganassi Racing story (May 28) also in rotation. Earlier small-business and farm stories demoted.

**`/news/ai-adoption/`** — "Applied AI" added as a navigation tab in the news category bar.

**Signals pages** (`/signals/`, `/signals/b2b/`, `/signals/research/`, `/signals/data/`, `/signals/data-download/`) — Timestamp bumps, likely CMS republishing triggered by today's additions.

---

### Removals
None.

---

*Stats: 1,345 total URLs | +7 added | 245 sitemap-updated | 0 removed | 0 anomalies | 0 fetch failures | 34 sub-sitemaps (+1 new: applied-ai)*

*Full analysis: [runs/2026-06-11T09-16Z/analysis.md](runs/2026-06-11T09-16Z/analysis.md)*

---

## 2026-06-10 — Run `2026-06-10T09-15Z`

**TL;DR:** Two new customer stories published (LSEG and Nextdoor on Codex), but the bigger news is what disappeared: 29 more pages were removed from the sitemap today — the second large batch in two days, bringing the two-day total to 57 removals. The most significant removals are the OpenAI Foundation page (which has fully migrated to its own domain `openaifoundation.org`), the ChatGPT Advertisers portal, all three DeployCo pages plus the Deployment Company business page, multiple deprecated policy pages (plugin terms, Sora policies, ROW and Services privacy policies), the Safety Evaluations Hub, the OpenAI Science page, and the Healthcare Solutions page. OpenAI's site navigation was also restructured across ~100+ pages, adding "Apps SDK" as a first-class menu item. The Industrial Policy for the Intelligence Age page was updated to note that its grant program received 400+ applications and has closed.

### Anomalies
None detected.

### New Pages (2)

**[LSEG: "From data to decisions: how LSEG is scaling trusted AI"](pages/openai.com/index/lseg/index.md)** (Jun 10, 2026)  
London Stock Exchange Group customer story. LSEG serves 40,000+ customers and 400,000+ end users across 190 markets. Using ChatGPT and the API, they compressed product release cycles from ~6 months to ~2 weeks, and customer-request-to-production from months to ~4 weeks. Joins a growing roster of financial services enterprise customers.

**[Nextdoor: "How engineers at Nextdoor use Codex to build without limits"](pages/openai.com/index/nextdoor/index.md)** (Jun 9, 2026)  
Nextdoor (110M users, 11 countries) platform engineering story. Codex enables "outcome engineering" — engineers describe what they want (screenshots, performance targets) rather than specifying implementation. One engineer now builds features that previously required 3 teams. Codex also handles hard debugging: embedded Rust databases, race conditions, Kubernetes pod failures. *"The bottleneck is no longer engineering, but the hard strategic questions about what to build next."*

---

### Notable Removals (29 total)

**Foundation page fully exits openai.com** — `/foundation/` removed. The OpenAI Foundation has its own domain (`openaifoundation.org`) and is now linked from the nav as an external site, confirming organizational separation following the nonprofit-to-PBC restructuring. The $25B program and $50M People-First AI Fund continue under the independent foundation.

**Advertisers page removed** — `/advertisers/` (the "Advertise in ChatGPT" portal) removed from openai.com. The advertising program appears to have moved to `ads.openai.com`.

**DeployCo brand fully gone** — Today's run removes the remaining DeployCo pages: `/deployco/`, `/deployco/privacy-policy/`, `/deployco/terms-of-use/`, and `/business/the-openai-deployment-company/` (the "OpenAI Deployment Company" landing). Combined with yesterday's removals, the entire DeployCo sub-brand is now scrubbed from openai.com.

**Policy cleanup** — Removed: plugin terms (final cleanup of deprecated ChatGPT Plugins ecosystem), ROW privacy policy, Services privacy policy, Sora usage policies, Sora video creation policy, business terms, invoice submission guidelines.

**Safety Evaluations Hub removed** — `/safety/evaluations-hub/` removed from sitemap. The hub itself lives at its own URL; the openai.com portal page is gone.

**Science & Healthcare pages removed** — `/science/` and `/solutions/healthcare/` removed; vertical solution pages appear to be consolidating into the core business pages.

**Other removals:** `/agent-platform/`, `/chatgpt/download/`, `/chatgpt/search-product-discovery/`, `/reserved-capacity/`, `/devday/directory/`, `/form/custom-models/`, `/contributions/`, `/newsroom/global-affairs/`, `/newsroom/security/`, `/index/gpt-5-2-codex/`, `/index/parameter-golf/`, `/academy/top-10-use-cases-codex-for-work/`, `/business/guides-and-resources/`.

---

### Notable Updates

**Navigation restructured across ~100+ pages** — The site nav was updated: "API Log In" (capitalized), "Apps SDK" added as a first-class developer nav item linking to the Apps SDK docs, and ChatGPT business tiers (Business, Enterprise, Education) restructured as distinct links. "Brand" link removed from developer nav.

**Industrial Policy for the Intelligence Age — grant inbox closed** — The June 9 policy paper's feedback/grant program received 400+ responses and closed submissions. Grant recipients are now under review.

**GPT-5.5 Instant personalization rolling to Free tier** — Update added: personalization is now available on ChatGPT Free (with a reduced set of past chats vs. paid tiers).

**New sub-sitemap: `global-affairs-news-listed`** — A new sub-sitemap appeared alongside the existing `global-affairs` sub-sitemap, providing alternate-language (`xhtml:link`) entries for Global Affairs news articles. Likely an SEO internationalization improvement.

---

*Stats: 1,338 total URLs | +2 added | ~319 sitemap-updated (56 actual content changes) | -29 removed | 0 anomalies | 0 fetch failures | 33 sub-sitemaps*

*Full analysis: [runs/2026-06-10T09-15Z/analysis.md](runs/2026-06-10T09-15Z/analysis.md)*

---

## 2026-06-09 — Run `2026-06-09T09-15Z`

**TL;DR:** A landmark day on openai.com. June 8, 2026, OpenAI announced it has confidentially submitted a draft S-1 to the SEC — the formal first step toward a public offering — while simultaneously publishing a major strategic vision essay by Sam Altman and Jakub Pachocki declaring OpenAI's "third phase" and a new Economic Research Exchange for academic study of AI's economic impacts. Alongside the announcements: 28 pages removed (including the entire DeployCo brand, the advertiser portal landing page, the OpenAI Foundation page, the Safety Evaluations Hub, and a raft of deprecated policy and product pages), 6 new pages added, and a sitewide CMS republish touched 672 URLs (142 with actual visible content changes).

### Anomalies
None detected.

### Major New Pages (6)

**[Confidential Submission of Draft S-1 to the SEC](pages/openai.com/index/openai-submits-confidential-s-1/index.md)** (Jun 8, 2026)  
OpenAI has filed a confidential S-1 with the SEC — the standard first step toward an IPO. The announcement is unusually candid: *"We expect it to leak so we're just announcing it."* Timing is undecided; they note some things "are likely easier as a private company." Includes a boilerplate Rule 135 disclaimer (not an offer to sell). A confidential S-1 gives the SEC a chance to review the filing before it becomes public; OpenAI can withdraw it if they decide not to proceed.

**[Built to Benefit Everyone: Our Plan](pages/openai.com/index/built-to-benefit-everyone-our-plan/index.md)** (Jun 8, 2026, by Sam Altman and Jakub Pachocki)  
A long-form strategic essay declaring OpenAI is entering its "third phase": from research org → product company → now making AI universally abundant. Three stated goals: (1) build an automated AI researcher (internal expectation: *"by March of 2028, a significant fraction of our research may be done by AI systems in tandem with our own researchers"*); (2) accelerate the economy with widely-shared gains; (3) give every person on Earth a personal AGI. The document argues AI must broaden rather than concentrate power, calls for an international governance body capable of slowing frontier development, and explicitly rejects full automation: *"entirely automating everything is not the future we want."*

**[Introducing the OpenAI Economic Research Exchange](pages/openai.com/index/economic-research-exchange/index.md)** (Jun 8, 2026)  
A new program for external academics to conduct rigorous empirical research on AI's economic effects using OpenAI tools and data, under formal data governance. Applications open now at `/form/economic-research-exchange/`; close July 5, 2026; decisions by July 31. Fields sought: labor economics, productivity, inequality, regional economics, development, and related. Builds on the existing OpenAI Signals data publication effort.

**[OpenAI Academy: Champion Programs](pages/openai.com/academy/champion-programs/index.md)** (Jun 9, 2026)  
A new enterprise change-management offering from OpenAI Academy targeting the people inside organizations who drive AI adoption — "OpenAI Champions." Structured learning journey: foundations → apply to work → connect with peers → shape strategy. Appears to formalize a previously informal role into a named program with curriculum and community.

*Also new:* [Economic Research Exchange RFP details](pages/openai.com/index/economic-research-exchange-request-for-proposals/index.md) and [application form](pages/openai.com/form/economic-research-exchange/index.md).

---

### Notable Content Changes

**[Release Notes](pages/openai.com/products/release-notes/index.md)** — New entry now at the top of the visible window (the previous "Active account session controls" entry from Jun 2 has scrolled below the fold):

- **Codex app updates: profile insights and share cards** (Codex, Jun 4): Activity insights and share cards added to the Profile section; users can review usage highlights and save/share a profile card (sharing on consumer ChatGPT plans). Bug fixes: Computer Use startup, browser/review UI issues, expanded onboarding role choices.

**[openai.com homepage](pages/openai.com/index.md)** — The top news spotlight has rotated. The previous featured stories ("How frontier firms are pulling ahead," "New ways to buy ChatGPT ads") have been replaced by the S-1 announcement, the Altman/Pachocki vision essay, and the Economic Research Exchange. The "Learn about ChatGPT Business" CTA has been removed from the nav strip.

---

### Significant Removals (28 total)

**DeployCo brand fully retired** — `/deployco/`, `/deployco/privacy-policy/`, `/deployco/terms-of-use/`, and `/business/the-openai-deployment-company/` all removed. The white-label enterprise deployment company brand has been completely scrubbed from openai.com.

**Advertisers portal removed** — `/advertisers/` (the "Advertise in ChatGPT" landing page describing ChatGPT's ad product and linking to `ads.openai.com`) has been removed from the sitemap. The advertising product itself may still exist, but OpenAI is no longer promoting it via a dedicated page on openai.com.

**OpenAI Foundation page removed** — `/foundation/` removed. The Foundation continues to operate at `openaifoundation.org` (still linked from the header), so this is likely a consolidation: the organization has its own domain and no longer needs a mirror page on openai.com.

**Safety Evaluations Hub removed** — `/safety/evaluations-hub/` (the "Deployment Safety" hub listing evaluation reports and risk measurements) removed. Content likely reorganized under `/trust-and-transparency/` or `/safety/`.

**Policy consolidation (6 pages):**
- `/policies/row-privacy-policy/` — Rest-of-World privacy policy removed (consolidated into `/policies/privacy-policy/`).
- `/policies/services-privacy-policy/` — Services communications privacy policy removed.
- `/policies/business-terms/` — Older business terms superseded.
- `/policies/plugin-terms/` — Plugin terms removed (plugins deprecated).
- `/policies/sora-usage-policies/` and `/policies/creating-sora-videos-in-line-with-our-policies/` — Sora-specific policy pages removed.

**Other removals:** `/chatgpt/download/`, `/chatgpt/search-product-discovery/`, `/science/`, `/solutions/healthcare/`, `/reserved-capacity/`, `/contributions/`, `/form/custom-models/`, `/devday/directory/`, `/newsroom/global-affairs/`, `/newsroom/security/`, `/index/gpt-5-2-codex/`, `/index/parameter-golf/`, `/academy/top-10-use-cases-codex-for-work/`, `/business/guides-and-resources/`, `/agent-platform/`.

---

### Routine Updates

672 sitemap lastmod changes (142 with actual visible content changes) reflect the June 8 sitewide CMS republish — consistent with a global navigation/template update triggered by the S-1 day announcements. Most visible changes are the new S-1 and vision essay appearing in "Keep reading" / related content sidebars across the site.

---

*Stats: 1,337 total URLs | +6 added | ~672 sitemap-updated (142 actual content changes) | -28 removed | 0 anomalies | 32 sub-sitemaps*

*Full analysis: [runs/2026-06-09T09-15Z/analysis.md](runs/2026-06-09T09-15Z/analysis.md)*

---

## 2026-06-08 — Run `2026-06-08T09-15Z`

**TL;DR:** No new or removed pages today — the URL count holds at 1,331. A CMS navigation overhaul touched 109 pages (but only 2 had any visible content change). The real news is in the release notes: OpenAI published a cluster of security and AI-capability updates dated June 2–4, including a new Active Sessions security feature, Lockdown Mode expanded to all users, ads launching in the UK for free-tier users, an upgraded memory system for ChatGPT, and moderation scores added directly to the Responses API. The site-wide footer nav was also restructured, with a new "Developers" standalone section and GPT-5.3-Codex quietly removed from the featured model list.

### Anomalies
None.

### Substantive Content Changes (2 pages)

**[Release Notes](pages/openai.com/products/release-notes/index.md)** — Five new release notes surfaced for June 2–4:

- **Active account session controls** (ChatGPT, Jun 2): New security feature in Settings > Security > Active sessions. Users can review all first-party sessions (device, location, sign-in time, trusted-device status) and sign out remotely. Covers ChatGPT, Codex, and API Platform sessions; does not cover Codex CLI or third-party app sessions.

- **Lockdown Mode for all users** (ChatGPT, Jun 4): Previously limited access, now available to all logged-in users across account types. Opt-in from Settings > Security. Disables web browsing, deep research, agent mode, file downloads, and web-derived image support to guard against prompt-injection data-exfiltration.

- **Ads rolling out in the UK** (ChatGPT, Jun 4): Free and Go plan users in the UK will begin seeing ads. Paid plans (Plus, Pro, Business, Enterprise, Education) remain ad-free.

- **Upgraded ChatGPT memory** (ChatGPT, Jun 4): New memory system that automatically stays current, reduces stale/contradictory memories, and tracks preferences and ongoing work. Plus/Pro US rollout first, capacity doubled for those tiers. Legacy saved-memories system remains as opt-out fallback.

- **Moderation scores in API** (API, Jun 4): Responses API and Chat Completions API now accept a `moderation` object, returning moderation results for both input and output in the same response (eliminating a separate API call).

*The prior top entry — Codex app updates 26.602 (Jun 4, activity insights, Computer Use fixes) — was pushed below "Load more."*

**[DALL-E 3 page](pages/openai.com/index/dall-e-3/index.md)** (representative of site-wide footer nav change) — Footer navigation restructured across 109 pages:
- **New "Developers" section** added: Apps SDK, Open Models, Docs, Resources, Developer Forum
- **"ChatGPT" → "Products"**: Codex and Release Notes added; links updated to canonical URLs
- **GPT-5.3-Codex removed** from "Latest Advancements" featured model list
- **Deployment Safety** added to Safety section
- **Research Residency** (`/residency/`) removed from Research section
- **Company section**: Foundation and Brand links removed; News added
- **"API Platform"** simplified (Pricing and Developer Forum links removed)

### Routine Sitemap Updates (107 pages — lastmod bumped, no visible content change)

Sections affected: `index/` (81 pages, mostly case studies and research), `academy/` (11), `policies/` (5), `stories/` (4), `business/` (2), `form/` (2), plus `gpt-rosalind/`, `podcast/`, `startups/`, `products/`. All reflect the CMS publishing the footer nav update. Policy pages with lastmod bumps but no text change: `privacy-policy`, `ad-policies`, `chatgpt-sites-terms`, `eu-services-privacy-policy`, `merchant-feed-terms-of-service`.

See full URL list in [runs/2026-06-08T09-15Z/analysis.md](runs/2026-06-08T09-15Z/analysis.md).

---
*Stats: 1,331 total URLs | +0 added | ~109 sitemap-updated (2 actual content changes) | -0 removed | 0 anomalies | 32 sub-sitemaps*

## 2026-06-07 — Run `2026-06-07T09-15Z`

**TL;DR:** No new or removed pages today — the sitemap URL count held steady at 1,331. A sitewide navigation template refresh touched ~357 pages (though only 68 got a sitemap lastmod bump, a consistent pattern for OpenAI template deploys). The most notable substantive change: a previously broken code example on the `chain-of-thought-monitoring` research page now renders correctly, revealing a Rust code snippet that illustrates how a verification function can be trivially bypassed — a key visual in OpenAI's research on reward hacking. The Codex Academy section (11 pages) received a batch refresh, and the editorial "Related Articles" spotlight rotated to feature biodefense and AI governance content.

### Sitewide Navigation Template Refresh (~357 pages)

The same template update propagated across most of the site:

- **"Related Articles" spotlight rotated**: sidebar now highlights Biodefense in the Intelligence Age (Jun 4), OpenAI public policy agenda (Jun 3), and A Blueprint for Democratic Governance of Frontier AI (Jun 3) — replacing the previous spotlight on Election Safeguards 2026, Grupo Folha partnership, and Education for Countries. This is OpenAI's main editorial promotion mechanism across the site.
- **Research Residency removed from footer nav**: The `/residency/` page still exists in the sitemap but is no longer linked in the site navigation.
- **Nav labels updated**: "Our Research" → "Research"; "ChatGPT" → "Products"; "For Business" → "Business"; "Developers" added as standalone item.
- **Lastmod gap**: 357 pages changed in content, only 68 got sitemap lastmod updates (~80% gap). This repo's git diff captures all changes; sitemap-only monitoring would miss most of them.

### Notable Content Fix: chain-of-thought-monitoring

The research page at [`/index/chain-of-thought-monitoring/`](pages/openai.com/index/chain-of-thought-monitoring/index.md) had a broken `componentCodeExample` placeholder that now renders. The newly visible code shows a Rust verification function being replaced by a trivial `return true` — the concrete example of reward hacking / verification bypass in OpenAI's research on monitoring frontier reasoning models.

### Codex Academy Batch Refresh (11 pages)

All Codex Academy learning pages refreshed in a ~30-second window at 06:16 UTC (batch CMS publish): `how-to-use-codex-for-everyday-work`, `codex-automations`, `codex-settings`, `codex-plugins-and-skills`, `codex-how-to-start`, `working-with-codex`, `what-is-codex`, plus role-specific guides for business ops, data science, sales, and finance teams.

### Policy Pages

- [`chatgpt-sites-terms`](pages/openai.com/policies/chatgpt-sites-terms/index.md): lastmod bumped Jun 6→7, no substantive policy text changes (template-only update).
- [`merchant-feed-terms-of-service`](pages/openai.com/policies/merchant-feed-terms-of-service/index.md): lastmod bumped Jun 5→7, likely re-indexed during template deploy. (This policy governing merchant product catalog data for ChatGPT shopping was new as of June 5.)

*Stats: 1,331 total URLs | +0 added | ~68 sitemap-reported updates (~357 actual) | -0 removed | 0 anomalies | 32 sub-sitemaps*

---