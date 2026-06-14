## 2026-06-14 — Run `2026-06-14T09-17Z`

**TL;DR:** No new or removed URLs today. The 131 lastmod updates are almost entirely explained by a **sitewide navigation and template redesign** that rolled out June 13–14 across openai.com. The most meaningful signals: **Codex now appears in the global footer as a first-class product** alongside ChatGPT (a positioning upgrade, not just a feature mention); the **Research Residency program link was removed sitewide** (suggesting it's no longer active); a new **"Developers" section** was added to the footer navigation; and the Notion case study was quietly re-titled to center Codex rather than GPT-5. On the technical side, "Pro" tier pricing links switched from internal relative paths (`/chatgpt/pricing/`) to external absolute URLs (`chatgpt.com/pricing`), accelerating the structural separation between openai.com and chatgpt.com. No anomalies. Zero page additions or removals.

### Anomalies
None.

### Sitewide Navigation Redesign (131 lastmod updates)

OpenAI rolled out a sitewide footer overhaul across 131 pages in two waves (June 13 and June 14). Only 35 pages showed visible markdown content changes; the rest had invisible changes (CSS, JS bundles, CMS metadata).

**What changed in the footer navigation:**

- **"Our Research" → "Research"** (renamed)
- **"ChatGPT" → "Products"** (renamed and expanded — now explicitly lists Codex and Release Notes)
- **"For Business" → "Business"** (renamed)
- **New "Developers" section added** — Apps SDK, Open Models, Docs, Resources, Developer Forum
- **Safety section** now includes "Deployment Safety" as a distinct link (`deploymentsafety.openai.com`)
- **Removed:** "Research Residency" link, "API Pricing" link, "GPT-5.3-Codex" from Latest Advancements

**Article template:** Table of contents now renders at the top of blog/research posts rather than inline, causing a duplicate-TOC appearance in diffs. Layout-only change.

**"Pro" pricing link:** Changed from internal `/chatgpt/pricing/` to external `chatgpt.com/pricing` on all affected pages — another step in the architectural separation of ChatGPT from openai.com.

### Notable Individual Changes

**[Moderna brand story](pages/openai.com/index/moderna/index.md)** — A related-stories card changed title: "Notion's GPT-5 rebuild unlocks autonomous AI workflows" → **"What Codex unlocks for Notion"**. The Notion case study was retroactively re-framed around Codex rather than GPT-5, signaling how OpenAI wants Codex perceived as the enterprise narrative thread.

**[Cybersecurity in the Intelligence Age](pages/openai.com/index/cybersecurity-in-the-intelligence-age/index.md)** — Related articles rotated to show more recent pieces: "PRC-linked influence operations targeting AI debates" (Jun 10) and "Supporting Europe's trustworthy AI ecosystem" (Jun 11) replaced older articles.

**[Teen Safety, Freedom and Privacy](pages/openai.com/index/teen-safety-freedom-and-privacy/index.md)** — Related articles updated to include "Confidential submission of draft S-1 to the SEC" and Oracle partnership announcement.

**[Research / Publication index](pages/openai.com/research/index/publication/index.md)** — Minor: "GPT-5.4 Thinking System Card" and "Reasoning models struggle to control their chains of thought" swapped order.

### Strategic Interpretation

Codex's addition to the global product footer is the clearest signal this run. Together with last week's Astral acquisition (Python tooling) and the Ona acquisition (persistent cloud execution for agents, first seen Jun 12), OpenAI is assembling a distinct Codex product line with its own infrastructure layer — not just a ChatGPT feature. The Research Residency removal is the quietest but potentially most significant: the program was OpenAI's main pathway for training next-generation AI researchers; retiring it from public navigation suggests the company no longer needs it for talent acquisition at its current scale.

*Full analysis: [runs/2026-06-14T09-17Z/analysis.md](runs/2026-06-14T09-17Z/analysis.md) | Diff: [runs/2026-06-14T09-17Z/diff.json](runs/2026-06-14T09-17Z/diff.json)*

*Stats: 1,349 total URLs | 0 added | 131 updated | 0 removed | 0 anomalies | 34 sub-sitemaps*

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

# openai_monitor

## 2026-06-06T09-16Z — GPT-Rosalind Gets a Product Page, Policy Week Publishes AI Governance Blueprints, Deployment Company Subdomain Removed

**Fetch time:** 2026-06-06T09:16:16Z | **Baseline:** 2026-06-03T09-15Z (3 days)

**TL;DR:** A policy-intensive three-day window (June 3–6) produced a cluster of major publications: OpenAI's full public policy agenda, a blueprint for U.S. federal AI governance referencing new state laws (California SB 53, NY RAISE Act, Illinois SB 315) and a White House executive order, a biodefense action plan built around GPT-Rosalind, and a new GPT-Rosalind product landing page formalizing the company's life sciences vertical. On the infrastructure side, a new Merchant Feed Terms of Service appeared — legal plumbing for merchant product data in ChatGPT shopping. A sitewide navigation template update (touching ~837 pages) added "Deployment Safety" and "Apps SDK" links while removing "Research Residency." Notably, the entire `/deployco/` subdomain (OpenAI's "Deployment Company" entity) was removed from the sitemap alongside 27 other URLs representing retired pages, old policies, and defunct section hubs. No anomalies detected.

### Anomalies
None.

### Notable New Pages

- **[GPT-Rosalind product landing page](pages/openai.com/gpt-rosalind/index.md)** — OpenAI's life sciences AI model now has a dedicated product page. GPT-Rosalind is built for biological reasoning (molecules, proteins, genes, pathways, disease biology), with Codex integration for repeatable scientific workflows, and benchmarks: +53.7% on Genebench, +18% Medchem Bench, +19.6% Labworkbench. Features enterprise access and a **Rosalind Biodefense** program for public-health teams. Partners quoted: Amgen.

- **[Biodefense in the Intelligence Age](pages/openai.com/index/biodefense-in-the-intelligence-age/index.md)** (Jun 4) — An "action plan for AI-powered biological resilience." Argues that the same capabilities enabling biological science advances have biosecurity implications, and that responsible defenders should be equipped with advanced AI alongside governance safeguards. Links to a full PDF plan.

- **[A Blueprint for Democratic Governance of Frontier AI](pages/openai.com/index/frontier-safety-blueprint/index.md)** (Jun 3) — OpenAI's proposal for a durable U.S. federal framework for frontier AI governance. Three-part strategy: leverage state-law consensus (CA SB 53, NY RAISE Act, IL SB 315); strengthen CAISI as the primary federal AI safety institution; broader national resilience plan. References a White House executive order on AI signed June 2026.

- **[OpenAI Public Policy Agenda](pages/openai.com/index/public-policy-agenda/index.md)** (Jun 3) — Comprehensive structured document covering OpenAI's full policy stance: mission and principles, policy priorities, safety, youth safety, AI resilience, and AI infrastructure/energy.

- **[ChatGPT Memory "Dreaming"](pages/openai.com/index/chatgpt-memory-dreaming/index.md)** (Jun 4) — Research/Product post on a "dreaming" mechanism for improving ChatGPT memory synthesis, optimizing for freshness, continuity, and relevance.

- **[Merchant Feed Terms of Service](pages/openai.com/policies/merchant-feed-terms-of-service/index.md)** (Jun 3) — New legal terms governing merchant product catalog data shared with OpenAI for use in its products (ChatGPT shopping). References a feed spec at `developers.openai.com/commerce/specs/feed`.

- **[Products: Release Notes hub](pages/openai.com/products/release-notes/index.md)** — New centralized release notes page at `/products/release-notes/`, now linked from sitewide navigation.

- **[Business Pricing](pages/openai.com/business/pricing/index.md)** — Dedicated pricing page for business/enterprise plans, showing Codex-based usage pricing.

- **[Endava: Redesigning Software Delivery Around AI Agents](pages/openai.com/index/endava-frontiers/index.md)** (Jun 4) — Case study on Endava using ChatGPT + Codex to accelerate delivery and reshape enterprise workflows.

- **[Wasmer: Node.js Runtime for the Edge with Codex](pages/openai.com/index/wasmer/index.md)** (Jun 3) — Wasmer used Codex to build a Node.js runtime for the edge.

- **[New Capabilities for GPT-Rosalind](pages/openai.com/index/introducing-new-capabilities-to-gpt-rosalind/index.md)** — Companion post detailing new evals and capabilities for the life sciences model.

### Notable Updates

- **Sitewide navigation template refresh (~837 pages):** Template-level update across most pages. Added to nav: "Deployment Safety" (→ `deploymentsafety.openai.com`), "Apps SDK" (→ `developers.openai.com/apps-sdk`), "Release Notes" (→ `/products/release-notes/`). Removed: "Research Residency." "Foundation" now links to `openaifoundation.org`. Most page body content is unchanged; the diff reflects header/footer/nav template.
- **[Customer Stories](pages/openai.com/business/customer-stories/index.md)** — Added new entries: Wasmer (Jun 3) and Endava (Jun 4).

### Removed Pages (28 total)

**Deployment Company wound down:** The entire `/deployco/` subdomain and its associated business page were removed: `/deployco/`, `/deployco/privacy-policy/`, `/deployco/terms-of-use/`, `/business/the-openai-deployment-company/`.

**Retired product/infrastructure pages:** `/reserved-capacity/`, `/agent-platform/`, `/chatgpt/download/`, `/advertisers/`

**Retired section hubs:** `/science/`, `/foundation/` (Foundation now at `openaifoundation.org`), `/safety/evaluations-hub/`, `/contributions/`

**Stale redirects retired:** `/newsroom/security/`, `/newsroom/global-affairs/` (already migrated to `/news/security/` and `/news/global-affairs/`)

**Superseded policies removed:** `/policies/plugin-terms/`, `/policies/sora-usage-policies/`, `/policies/creating-sora-videos-in-line-with-our-policies/`, `/policies/business-terms/`, `/policies/row-privacy-policy/`, `/policies/services-privacy-policy/`

**Other:** `/solutions/healthcare/` (→ `/solutions/industries/healthcare/`), `/business/guides-and-resources/` (→ `/business/learn/`), `/chatgpt/search-product-discovery/`, `/form/custom-models/`, `/academy/top-10-use-cases-codex-for-work/`

**Stats:** 1331 total URLs | +11 added | ~837 updated | -28 removed | 0 anomalies | 32 sub-sitemaps

---

## 2026-06-03T09-15Z — Codex Goes Mass-Market, Stargate Michigan Breaks Ground, Service Terms Updated for On-Prem Deployments

**Fetch time:** 2026-06-03T09:22:47Z | **Baseline:** 2026-06-01T09-15Z

**TL;DR:** A major content day centered on Codex expanding beyond developers and OpenAI's infrastructure ambitions. Nine new pages appeared — two Codex announcements (5M+ weekly users, new plugins and website-creation for non-technical roles), an AWS partnership going GA, a Michigan data center groundbreaking (1GW "The Barn"), a Travelers Insurance customer story, a G7 youth safety piece, and a political-transparency statement addressing Greg Brockman's personal ties to Leading the Future. Two new legal documents also appeared: terms for the new ChatGPT Sites feature, and an EU-specific privacy policy. On the legal/compliance side, the Service Terms were updated for the first time since January to add a new "Licensed Materials" section governing on-premises software deployments — a notable signal about enterprise self-hosted offerings. The Sub-processor list also got its first update since February, adding Cloudflare as a web host for ChatGPT Sites and expanding moderation operations to the US. The June 2 "Intelligence at Work" livestream with Sam Altman and Denise Dresser has wrapped.

**Anomalies:** None.

### Notable New Pages

- **[Codex for every role, tool, and workflow](pages/openai.com/index/codex-for-every-role-tool-workflow/index.md)** — Product announcement: Codex now has 5M+ weekly users (6x since February), with non-developers growing 3x faster than developers. Introduces 6 new role-specific plugins (for analysts, marketers, finance, legal), in-place annotations, and a preview of **ChatGPT Sites** — an embedded web-app builder that lets you share interactive sites via URL.

- **[Codex is becoming a productivity tool for everyone](pages/openai.com/index/codex-for-knowledge-work/index.md)** — Accompanying report "The Next Era of Knowledge Work." Non-developers are ~20% of Codex users. Top tasks: reports, spreadsheets, presentations, data analysis. Fastest growing: data analysis and research. Users increasingly run multiple Codex tasks in parallel.

- **[Stargate Michigan data center](pages/openai.com/index/stargate-michigan-data-center/index.md)** — Groundbreaking for "The Barn," a **1GW data center campus** in Saline, Michigan alongside Oracle, Related Digital, Walbridge, and Governor Whitmer. Community commitments: no cost pass-through to ratepayers; closed-loop cooling; **2,500+ union construction jobs** + 450 permanent; **$10M** to Saline Recreation Center; **$1B projected tax revenue** over the lease term.

- **[OpenAI frontier models and Codex now available on AWS](pages/openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/index.md)** — General availability for enterprise customers. OpenAI capabilities run within existing AWS security, compliance, procurement, and governance workflows, including GovCloud regions.

- **[Travelers deploys AI-powered claims countrywide](pages/openai.com/index/travelers/index.md)** — Insurance customer story. Travelers built a fully autonomous voice assistant using **OpenAI Realtime API** that handles auto property damage claim filings end-to-end. **85–90% of customers complete claims through AI.** Rolled out from 8 states to nationwide in 2 months.

- **[Advancing youth safety and opportunity through global leadership](pages/openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership/index.md)** — Policy piece timed to the G7 Leaders' Summit in Évian, France. OpenAI calls for an **international youth AI safety institute** with a sustained mandate, drawing on examples like Estonia's national ChatGPT school rollout.

- **[Our views on AI policy and political advocacy](pages/openai.com/index/our-views-on-ai-policy-and-political-advocacy/index.md)** — Transparency statement: OpenAI has made no super PAC donations and has no employee PAC. Clarifies that Greg Brockman's personal support for Leading the Future (LTF) is "in a personal capacity, not on behalf of the company" and that "OpenAI does not direct the activities of LTF."

- **[ChatGPT Sites Terms](pages/openai.com/policies/chatgpt-sites-terms/index.md)** — New legal terms for the Sites feature. You retain content ownership; you grant OpenAI a royalty-free worldwide license to host it; you're responsible for end-user compliance.

- **[EU Services Privacy Policy](pages/openai.com/policies/eu-services-privacy-policy/index.md)** — EU/EEA/UK/Switzerland-specific privacy policy. Notes ads for "Free and Go" users in the EU.

### Key Legal/Compliance Changes

- **[Service Terms updated June 2](pages/openai.com/policies/service-terms/index.md)** — First update since January 9. New **Section 10 "Licensed Materials"** covers customers downloading/installing OpenAI software onto their own infrastructure. Limited, non-exclusive, non-sublicensable license; terminates at end of term. This is the first formal on-premises deployment language in OpenAI's standard service terms — significant for enterprise deals requiring data locality.

- **[Sub-processor list updated June 2](pages/openai.com/policies/sub-processor-list/index.md)** — First update since February 11. Cloudflare now listed as a **Web Hosting** processor for ChatGPT Sites pages (with classifier runs on hosted content). Content moderation scope expanded to include United States (previously Canada + Philippines only). Subscriber notification form migrated to HubSpot.

### Other Updates

- **Homepage / News listings:** Featured hero content rotated from GPT-5.5 to "Codex for every role." Research listing reordered GPT-5.5 Instant entries (same editorial rotation pattern as June 1).
- **Intelligence at Work page:** Switched from pre-event ("register to watch live June 2") to post-event ("Thanks for watching"). The Sam Altman / Denise Dresser enterprise livestream occurred June 2 as scheduled.
- **Customer stories:** Travelers added to the featured listing; AutoScout24 rotated out.
- **~25 customer story pages:** Bulk Contentful CDN image-hash rotation (no substantive content change).

*Stats: 1320 total URLs | +9 added | ~296 updated | -0 removed | 0 anomalies | 32 sub-sitemaps*

---
## 2026-06-01T09-15Z — GPT-5.5 Entry Reordered on Research Pages; Mass CMS Timestamp Refresh

**Fetch time:** 2026-06-01T09:17:27Z | **Baseline:** 2026-05-31T09-17Z

**TL;DR:** A quiet day for substantive content. The sitemap shows 245 URLs with updated `lastmod` timestamps, but inspecting the actual page snapshots reveals only **two pages with real content changes** — both research listing pages where OpenAI reordered the Apr 23 GPT-5.5 entries, placing "Introducing GPT-5.5" (Product) above "GPT-5.5 System Card" (Safety). The remaining 243 timestamp bumps are a routine CMS sweep with no visible changes to the underlying HTML. No pages added or removed. No anomalies.

### Actual Content Change

- **[Research news listing](pages/openai.com/news/research/index.md)** and **[Research hub](pages/openai.com/research/index/index.md)**: The ordering of two same-date (Apr 23, 2026) GPT-5.5 entries was swapped. "Introducing GPT-5.5" (tagged as Product) now appears before "GPT-5.5 System Card" (tagged as Safety). This is an editorial choice — leading with the product announcement rather than the safety documentation when listing the GPT-5.5 launch items.

### Routine CMS Timestamp Refresh (no content change)

245 URLs had their `lastmod` field bumped in the sitemap. Notable pages in this group with no actual content change include:
- `https://openai.com/codex/` (bumped to 2026-06-01T09:06Z)
- `https://openai.com/about/` (bumped to 2026-06-01T01:14Z)
- `https://openai.com/index/gpt-5-first-look/`, `/gpt-5-amgen/`, `/gpt-5-cursor/`, `/gpt-5-coding-design/`
- `https://openai.com/form/rosalind-biodefense-program/` (bumped to 2026-06-01T09:17Z, close to fetch time)
- `https://openai.com/form/stargate-infrastructure/`, `/form/codex-enterprise-promo/`
- `https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/`
- `https://openai.com/safety/`, `https://openai.com/trust-and-transparency/`

This mass-timestamp pattern is consistent with prior runs (May 31: 271 updated; May 29: 855 updated) and reflects OpenAI's CMS regenerating records without meaningful content edits.

---
*Stats: 1311 total URLs | 0 added | 245 updated (2 with actual content change) | 0 removed | 0 anomalies | 32 sub-sitemaps*



## 2026-05-31T09-17Z — Rosalind Biodefense Launches, DeployCo De-listed, 24 Pages Removed

**TL;DR:** OpenAI publicly launched "Rosalind Biodefense" — a vetted-access program granting free API access to a named model variant called GPT-Rosalind for defensive biology research. This is the first time a "Rosalind" model variant has appeared on OpenAI's public website. Five new pages were added (the blog post, an application form, two customer case studies for Boston Children's Hospital and Braintrust, and a technical paper on third-party evaluations). More notably, 24 pages were quietly removed from the sitemap, including the ChatGPT advertisers page, all three "DeployCo" sub-brand pages (which debuted just 11 days ago and are already gone), the OpenAI agent-platform developer page, the Foundation landing page, two Sora policy pages, the current business-terms URL, and the healthcare solutions page. The 271 "updated" URLs are a routine CMS ripple from new content being featured in sidebars across the site. No anomalies.

### New Pages

- [**Strengthening societal resilience with Rosalind Biodefense**](pages/openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/index.md) (`/index/strengthening-societal-resilience-with-rosalind-biodefense/`, lastmod: 2026-05-29) — Blog post announcing "Rosalind Biodefense," a trusted-access program deploying a named model variant (GPT-Rosalind) for defensive biology use cases — biosurveillance, epidemiological modeling, preparedness, non-pharmaceutical interventions, and MCM development. Access is gated through a formal vetting process. First appearance of a "Rosalind" model name on the public site.

- [**Rosalind Biodefense Program application form**](pages/openai.com/form/rosalind-biodefense-program/index.md) (`/form/rosalind-biodefense-program/`, lastmod: 2026-05-29) — The companion application form for the program above. Offers free GPT-Rosalind API access to vetted researchers, public health teams, and mission-driven organizations.

- [**Boston Children's Hospital uses AI to unlock new diagnoses**](pages/openai.com/index/boston-childrens-hospital/index.md) (`/index/boston-childrens-hospital/`, lastmod: 2026-05-30) — Customer case study. One of the world's largest pediatric hospitals (~1M outpatient visits/year) deployed an enterprise AI layer for supply chain, billing, and operations. Healthcare vertical story.

- [**How Braintrust turns customer requests into code with Codex**](pages/openai.com/index/braintrust/index.md) (`/index/braintrust/`, lastmod: 2026-05-30) — Case study. Braintrust (AI evaluation platform) uses Codex + GPT-5.5 to convert customer feature requests into preview branches in minutes. Emphasizes speed enabling "autonomous problem-solving."

- [**A shared playbook for trustworthy third party evaluations**](pages/openai.com/index/trustworthy-third-party-evaluations-foundations/index.md) (`/index/trustworthy-third-party-evaluations-foundations/`, lastmod: 2026-05-31) — Technical paper on harness design for independent AI evaluations, particularly for multi-step agentic systems. Part of OpenAI's push for credible external evaluation methodology.

### Notable Updates

- **https://openai.com/research/index/** and **https://openai.com/news/research/**: Research/news indexes now lead with "Rosalind Biodefense," replacing "ChatGPT Images 2.0." Routine editorial rotation.
- **271 total updated pages**: Virtually all are sidebar/related-content refreshes — Boston Children's Hospital and Rosalind Biodefense now appear in "Related stories" widgets across the site, bumping the CMS lastmod for each page they appear on.

### Removed Pages (24)

- **`openai.com/advertisers/`** — ChatGPT advertising product page. Marketed ChatGPT as an ad channel ("Reach people as they explore options, compare choices, and make decisions in ChatGPT"). Notable removal; may signal a strategy shift on the ads product.
- **`openai.com/deployco/`** + `/deployco/privacy-policy/` + `/deployco/terms-of-use/` — "DeployCo" sub-brand debuted 2026-05-20 (11 days ago) and is already de-listed. Had its own privacy policy and ToU suggesting a distinct legal identity. Very short lifespan; likely renamed or scrapped.
- **`openai.com/business/the-openai-deployment-company/`** — Paired with DeployCo; marketing page for the "OpenAI Deployment Company" concept.
- **`openai.com/agent-platform/`** — Developer-facing agent platform page. Likely part of a developer portal restructuring.
- **`openai.com/foundation/`** — OpenAI Foundation landing page; Foundation content migrating to its own domain (openaifoundation.org).
- **`openai.com/policies/business-terms/`** — The "current" business terms URL de-listed; historical versions (nov-2023, aug-2023, may-2025) remain. The page had "Effective: January 1, 2026."
- **`openai.com/policies/sora-usage-policies/`** + `/policies/creating-sora-videos-in-line-with-our-policies/`** — Both Sora-specific policy pages removed; likely merged into general usage policies.
- **`openai.com/safety/evaluations-hub/`** — Was actually served from deploymentsafety.openai.com; removal from openai.com sitemap confirms migration to that subdomain.
- **`openai.com/science/`** — Science section de-listed; likely merged into /research/.
- **`openai.com/solutions/healthcare/`** — Healthcare vertical solutions page removed.
- Other: `chatgpt/download/`, `chatgpt/search-product-discovery/`, `contributions/`, `devday/directory/`, `form/custom-models/`, `newsroom/global-affairs/`, `newsroom/security/`, `reserved-capacity/`, `index/gpt-5-2-codex/`, `index/parameter-golf/`, `business/guides-and-resources/`

**Stats:** 1311 total URLs | 5 added | 271 updated (CMS propagation) | 24 removed | 0 anomalies | 32 sub-sitemaps

---
## 2026-05-29 — Frontier Governance Framework, MUFG/Endava/CGR Customer Stories, Policy Cleanup

**Fetch time:** 2026-05-29T09:17Z UTC | **Baseline:** 2026-05-28T09-17Z

**TL;DR:** The big story today is OpenAI publishing its [Frontier Governance Framework](pages/openai.com/index/openai-frontier-governance-framework/index.md) — a formal document mapping their AI safety practices onto California's Transparency in Frontier AI Act and the EU AI Act's Code of Practice, making this OpenAI's first compliance-oriented safety document. Three new customer stories also appeared: Japanese banking giant MUFG deploying ChatGPT Enterprise to 35,000 employees, UK tech services firm Endava scaling engineering with Codex, and motorsport team Chip Ganassi Racing (now featured on the homepage). Four legacy policy pages were quietly retired (plugin terms, two regional privacy policy variants, and an old Codex Academy article). The 855 "updated" sitemap entries are a CMS timestamp sweep — content diffs show minimal actual changes. Three "Deployco" pages remain in the sitemap but return HTTP 404 for the second consecutive day.

### Notable: Deployco pages — sitemap present, HTTP 404

`/deployco/`, `/deployco/privacy-policy/`, and `/deployco/terms-of-use/` are listed in the sitemap with today's lastmod (2026-05-29) but return 404 when fetched. "Deployco" is not yet an announced product. This could indicate an unreleased product, a recently removed service, or a CMS artifact. Monitor closely.

### New Pages

- [**OpenAI's Frontier Governance Framework**](pages/openai.com/index/openai-frontier-governance-framework/index.md) (`/index/openai-frontier-governance-framework/`, lastmod: 2026-05-28) — Published May 28. A formal governance doc explaining how OpenAI's safety practices map to: (1) California's Transparency in Frontier AI Act and (2) the EU AI Act's Code of Practice for GPAI. Covers risk assessment for cyber offense, CBRN, harmful manipulation, and loss of control; also covers model reporting, incident response, and external expert input. Linked as a PDF. This is OpenAI's first document explicitly designed to satisfy legal/regulatory compliance obligations rather than explain internal philosophy.

- [**MUFG × OpenAI**](pages/openai.com/index/mufg/index.md) (`/index/mufg/`, lastmod: 2026-05-28) — Mitsubishi UFJ Financial Group deploys ChatGPT Enterprise to ~35,000 employees at Mitsubishi UFJ Bank. Focus: AI-native transformation, employee enablement, new retail banking customer experiences. MUFG is one of the world's largest banks (Asia-Pacific).

- [**Chip Ganassi Racing × OpenAI**](pages/openai.com/index/chip-ganassi-racing/index.md) (`/index/chip-ganassi-racing/`, lastmod: 2026-05-28) — In-depth feature on the partnership with the IndyCar/IMSA team. Originated from a chance meeting at a Women in Motorsports event. AI is used to analyze sensor data, race telemetry, and pit crew performance. The homepage now features this story prominently.

- [**Endava × OpenAI**](pages/openai.com/index/endava/index.md) (`/index/endava/`, lastmod: 2026-05-28) — UK tech services company Endava uses Codex to scale senior engineering expertise across its delivery lifecycle; claims weeks of work compressed into days. Part of the ongoing Codex enterprise customer story push.

### Removed Pages

- `https://openai.com/academy/top-10-use-cases-codex-for-work/` — Academy article; likely replaced by newer Codex content.
- `https://openai.com/policies/plugin-terms/` — ChatGPT plugin terms; expected cleanup as plugins were deprecated.
- `https://openai.com/policies/row-privacy-policy/` — Rest-of-World privacy policy variant; consolidated into main privacy policy.
- `https://openai.com/policies/services-privacy-policy/` — Services-specific privacy policy; also consolidated.

### Homepage Update

The [homepage](pages/openai.com/index.md) now features a Chip Ganassi Racing × OpenAI takeover/feature section (lastmod bumped from May 20 to May 28).

**Stats:** 1330 total URLs | +4 added | ~855 updated (mostly CMS timestamp sweep) | -4 removed | 0 anomalies | 32 sub-sitemaps

---
## 2026-05-28 — Privacy Policy Consolidation, "Intelligence at Work" Livestream, Safety Page Expands Election Commitments

**Fetch time:** 2026-05-28T09:17Z UTC | **Baseline:** 2026-05-27T09-17Z

**TL;DR:** Today's headline changes are a quiet privacy policy consolidation (two legacy region-specific policies retired, all traffic redirected to the unified US Privacy Policy), the announcement of an "Intelligence at Work" livestream on June 2 featuring Sam Altman, and the Safety page gaining three new public commitments about AI content governance. The 805 "updated" sitemap entries are a mass CMS sweep reflecting the day's new content in carousel sidebars site-wide — no substantive edits to those pages. Two flagged anomalies are CMS timing artifacts (lastmod is within 6 seconds of fetch; not meaningful). The OpenAI Deployment Company (`deployco/`) remains in the sitemap for a ninth consecutive day but still returns HTTP errors.

### Anomalies (CMS Timing Artifacts — Not Meaningful)
Two URLs showed `future_lastmod` by 6–11 seconds: `introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/` and `gpt-4o-system-card/`. The gap is less than the time it takes to load a sitemap. This is the CMS recording lastmod at the instant the sitemap is generated, slightly after our fetch time was recorded. No editorial significance.

### New Pages

- [**Intelligence at Work livestream**](pages/openai.com/business/intelligence-at-work/index.md) (`/business/intelligence-at-work/`) — Landing page for an enterprise-focused live event on **June 2 at 11:30am ET**. Denise Dresser (CRO) and product leadership will demo new capabilities coming to the OpenAI platform, discuss enterprise AI strategy, and take questions. Sam Altman is listed as a special guest. First business-focused live event announced on the site since the Codex launch webinars.

- [**Building self-improving tax agents with Codex**](pages/openai.com/index/building-self-improving-tax-agents-with-codex/index.md) (`/index/building-self-improving-tax-agents-with-codex/`) — Engineering post by OpenAI forward-deployed engineers and Thrive Holdings staff. Documents how Tax AI for Crete's 30+ accounting firm network was built using a Codex self-improvement loop: production failures are automatically converted into evals, which Codex then uses to improve itself autonomously. The post frames this as a repeatable pattern for production agentic systems and includes a how-to guide.

- [**Election safeguards 2026**](pages/openai.com/index/election-safeguards-2026/index.md) (`/index/election-safeguards-2026/`) — Global Affairs post (dated May 27) describing OpenAI's election-integrity measures ahead of global 2026 elections: helping voters access authoritative information, supporting cyber defenders, and increasing AI transparency. Part of a recurring pattern of pre-election policy disclosure; prior versions exist for 2024.

- [**How to use Codex for everyday work**](pages/openai.com/academy/how-to-use-codex-for-everyday-work/index.md) (`/academy/how-to-use-codex-for-everyday-work/`) — New Academy page (replaces the removed `top-10-use-cases-codex-for-work` page, same concept refreshed) with 10 Codex use cases for non-technical roles: daily work briefs, weekly summaries, slide decks, research-to-decision memos, file cleanup, spreadsheet consolidation, book-of-business prioritization, and month-end financial review. Targeted at business users, not developers.

- [**Warp customer story**](pages/openai.com/index/warp/index.md) (`/index/warp/`) — Developer tool company Warp uses GPT-5.5 to orchestrate agents across local, cloud, and open-source development workflows. Key metric: 30% fewer tokens per task versus prior models. Highlights agentic orchestration via "Oz," their internal system, and the integration of Codex into open source development at scale.

### Substantive Content Changes

- [**Safety page**](pages/openai.com/safety/index.md) — Three new bullet points added to OpenAI's public safety commitments: *"Improving transparency in AI content,"* *"Rigorously evaluating content to avoid reinforcing biases or stereotypes,"* and *"Partnering with governments to combat disinformation globally."* The last bullet is new and directly relevant to the election safeguards post published the same day.

- [**Privacy policy**](pages/openai.com/policies/privacy-policy/index.md) — Substantive change is only URL normalization (all `help.openai.com/en/articles/...` links replaced with `help.openai.com/articles/...` — removing the `/en/` segment). No policy language changed. The lastmod jumped from Feb 25 to May 28, which is misleading; this appears to be a publishing infrastructure change, not a policy revision.

- [**Consumer privacy page**](pages/openai.com/consumer-privacy/index.md) — The link labeled "Privacy policy" was updated to point to `/policies/privacy-policy/` instead of the now-removed `/policies/row-privacy-policy/`. This is the redirect confirming the consolidation described below.

### Removed Pages (Policy Consolidation + Plugin Cleanup)

- `https://openai.com/policies/row-privacy-policy/` — The "Rest of World" (non-EU/UK/Switzerland) privacy policy was a separate page. Removing it and updating the `consumer-privacy` page to point to the unified `/policies/privacy-policy/` indicates the ROW-specific variant has been merged into the main policy. The last snapshot is in git history.

- `https://openai.com/policies/services-privacy-policy/` — A second legacy variant removed in the same cleanup. Last snapshot in git.

- `https://openai.com/academy/top-10-use-cases-codex-for-work/` — Replaced by the newly-added `how-to-use-codex-for-everyday-work` Academy page (same concept, refreshed content and URL). A clean swap, not a content removal.

- `https://openai.com/policies/plugin-terms/` — ChatGPT plugins were deprecated in 2024; removing the terms page is a long-overdue cleanup. Last snapshot in git.

### Routine Updates (CMS Carousel Refreshes — 801 pages)

All 801 remaining "updated" pages show identical patterns: "Keep Reading" sidebars swapped to surface today's new content (Warp story, Cisco + Codex, building tax agents with Codex). No editorial changes to the pages themselves. The mass lastmod update is the CMS recording the current timestamp when regenerating sidebars.

### Continuing Issue: OpenAI Deployment Company (Day 9)

`https://openai.com/deployco/` (first seen May 20), `deployco/privacy-policy/`, and `deployco/terms-of-use/` (first seen May 22) remain in the sitemap with fresh timestamps but all three return HTTP errors when fetched. Nine consecutive days in the sitemap. The timestamps continue to be refreshed daily, suggesting active publishing work behind the scenes.

**Stats:** 1326 total URLs | +5 added | ~805 updated (801 CMS sweeps + 4 substantive) | -4 removed | 2 anomalies (CMS artifacts) | 3 fetch failures (deployco/)

---


## 2026-05-27 — ChatGPT Ads Expand Into Financial Services, Healthcare & Legal

**Fetch time:** 2026-05-27T09:17:36Z UTC | **Baseline:** 2026-05-26T09-16Z

**TL;DR:** The headline change today is a **significant expansion of OpenAI's ChatGPT advertising policy**: financial services, healthcare & medicine, and legal services advertisers can now be manually approved to run ads in ChatGPT — categories that were previously explicitly listed as prohibited. This is a notable move that opens ChatGPT's ad business to regulated professional verticals. Beyond that, a large CMS sweep (206 URLs, two waves: May 26 overnight + May 27 morning) refreshed "Keep Reading" / related-content sidebars across research pages, customer stories, and product pages to surface newer articles (Gartner MQ recognition, Virgin Atlantic/Codex story, Grupo Folha/UOL partnership). No new pages were added. The DeployCo sitemap anomaly continues for an 8th day.

### Substantive Content Changes

- [**Ad Policies**](pages/openai.com/policies/ad-policies/index.md) — **Policy expanded.** The ad content policy now states: *"We may approve ads from approved advertisers within the financial services, healthcare & medicine, and legal services categories. These categories are being rolled out gradually with approvals being reviewed manually on a case-by-case basis."* Previously, these three verticals were explicitly listed as disallowed at launch. This is a selective carve-out (manual approval only), suggesting OpenAI is quietly scaling ChatGPT's ad program into regulated industries. The page's "Updated" date changed from May 22 to May 26. (lastmod `2026-05-01` → `2026-05-27T09:15Z`)

### Routine Updates (CMS/Carousel Refreshes — No Core Content Changes)

**May 27 wave (~157 pages):** A broad CMS deploy updated "Keep Reading" sidebars to rotate in newer content. Removed from sidebars: Malta partnership (May 16), OpenAI Deployment Company launch (May 11), "Ramp code review with Codex" (May 20), "What Parameter Golf taught us" (May 12). Added to sidebars: Grupo Folha/UOL Brazil media partnership (May 25), Virgin Atlantic + Codex story (May 22), Gartner MQ Leader recognition (May 22), Dell Technologies + Codex partnership (May 18). Affects all news category index pages, research pages, customer story pages (Cisco, AdventHealth, BNY, Choco, Ramp, Healthify, Lifespan, Philips, Whoop, Oscar, Paradigm, Summer Health, Waymark, GenMab, Color Health, and ~140 more).

**May 26 wave (~49 pages):** Overnight batch — customer stories (BNY, Cisco, Uber), business pages. No content change, CMS metadata only.

### Continuing Anomaly: DeployCo Pages Not Live (Day 8)

`https://openai.com/deployco/` (lastmod `2026-05-27T08:02Z`) and `https://openai.com/deployco/privacy-policy/` remain in the sitemap with fresh timestamps but return HTTP errors when fetched — not yet live. Eight consecutive days in the sitemap. The freshly updated timestamps suggest active publishing activity behind the scenes.

### Removed Pages

The Plugin Terms policy (`https://openai.com/policies/plugin-terms/`) was already removed as of the May 26 run; it continues to appear as "removed" due to stale baseline files from May 23. Actual removal occurred between May 23 and May 26.

**Stats:** 1,324 total URLs | +0 added | ~206 lastmod-changed (1 with substantive content) | -1 removed | 0 anomalies | 2 fetch failures (both DeployCo) | 32 sub-sitemaps

---

## 2026-05-26 — Brazil Media Partnership Announced; Plugin Terms Removed; Priority API Pricing Expanded

**Fetch time:** 2026-05-26T09:18:05Z UTC | **Baseline:** 2026-05-25T09-15Z

**TL;DR:** The headline addition today is OpenAI's first media partnership in Brazil — a new page announcing a content deal with Grupo Folha (publisher of Folha de S.Paulo) and Grupo UOL, giving ChatGPT's 900M+ weekly users access to Brazilian journalism. Separately, the Plugin Terms policy page was quietly removed, consistent with the long-deprecation of the ChatGPT Plugins platform. The most substantive content change is to the [Priority Processing API page](pages/openai.com/api-priority-processing/index.md), which grew by ~4KB to add a comprehensive pricing table covering 15+ model tiers (GPT-5.5, GPT-5.4, GPT-5.2, GPT-5.1, GPT-5.1 Codex, GPT-5 Codex, GPT-4.1 series, o3, o4-mini) with input/output token costs, uptime SLAs (99.9%), and latency guarantees. The bulk of the 656 "updated" URLs are CMS timestamp refreshes with no visible content changes — 540 pages swept on May 22 and further batches of customer stories and Codex Academy content from May 24–26. The `deployco/privacy-policy/` fetch failure persists (day 7).

### New Pages

- [https://openai.com/index/grupo-folha-grupo-uol-partnership/](pages/openai.com/index/grupo-folha-grupo-uol-partnership/index.md) — **OpenAI, Grupo Folha, and Grupo UOL announce strategic content partnership** (published 2026-05-25). OpenAI's first Brazil media deal; Folha de S.Paulo and UOL journalism will appear as sourced summaries in ChatGPT. Brazil has >50M monthly ChatGPT users and ~140M messages/day.

### Substantive Content Changes

- [**api-priority-processing**](pages/openai.com/api-priority-processing/index.md) — Content grew +3,922 chars (6,402→10,324). A new detailed pricing table was added listing Priority Processing rates for 15+ model tiers: GPT-5.5 ($12.50/$75 per 1M tokens), GPT-5.4 mini ($1.50/$9), GPT-5.4 ($5/$30), GPT-5.2 ($3.50/$28), GPT-5.1 ($2.50/$20), GPT-5.1 Codex, GPT-5 Codex, GPT-4.1/mini/nano, GPT-4o, o3, o4-mini. Includes 99.9% uptime SLA and per-tier p50 latency SLA. Also adds a new "What are the rate limits?" FAQ section.
- [**agent-platform**](pages/openai.com/agent-platform/index.md) — Navigation sidebar restructured (+1,408 chars); SDKs/CLI and Voice Activity Detection links reorganized.
- [**homepage**](pages/openai.com/index.md) — Minor nav change: "Learn about ChatGPT Business" link removed from headline navigation area (−22 chars).

### Removed URLs

- `https://openai.com/policies/plugin-terms/` — Plugin Terms policy page removed. ChatGPT Plugins were deprecated in early 2024; this is final cleanup of the associated legal terms.

### Batch Timestamp Updates (No Content Changes)

656 URLs had lastmod bumps; nearly all are CMS/pipeline noise:

| Wave | Date | # Pages | Notes |
|---|---|---|---|
| Academy + site-wide CMS deploy | 2026-05-22 | ~540 | All academy courses, product pages, research pages — zero content delta |
| Legacy research + company pages | 2026-05-24 | ~67 | Old research publications, historical announcements |
| Customer stories + Codex Academy | 2026-05-25 | ~16 | BNY, Mercado Libre, Klarna, Rogo, etc. + Codex workflow guides |
| Customer stories (new batch) + misc | 2026-05-26 | ~24 | Balyasny, BBVA, Chime, Commonwealth Bank, Endex, Hebbia, JetBrains, etc. |

### Fetch Failures

- `https://openai.com/deployco/privacy-policy/` — Fetch failed (day 7 of sitemap presence without a live page)

**Stats:** 1,324 total URLs | +1 added | 656 lastmod-changed (2 with substantive content) | -1 removed | 0 anomalies | 32 sub-sitemaps

---
## 2026-05-25 — All Quiet: 158 Timestamp Bumps, No Content Changes; DeployCo Privacy Policy Still 404 (Day 6)

**TL;DR:** Today's run found no new pages and no removals — just 158 URLs whose `<lastmod>` timestamps changed, none of which reflected actual content edits. The changes cluster into four CMS/CDN deployment waves: a large batch of ~117 legacy research and publication pages all touched within a 2.5-minute window on the evening of May 24 UTC (classic backend deploy fingerprint), 22 customer story pages refreshed together this morning, 11 Codex Academy tutorial pages updated in the early hours, and 5 Signals product pages touched across the morning. Spot-checks on all four waves confirmed zero visible content change. The only genuine flag is the same as yesterday: `deployco/privacy-policy/` is still listed in the sitemap — now with a very fresh timestamp from just minutes before this run — but the page continues to return HTTP 404. That's six consecutive days in the sitemap without a live page.

### Anomalies

**ANOMALY — `deployco/privacy-policy/` returns 404 (day 6):** The URL `https://openai.com/deployco/privacy-policy/` appears in today's sitemap with lastmod `2026-05-25T09:10:04.929Z` — a timestamp only 6 minutes before this run's fetch. The page still returns HTTP 404. This is now the sixth consecutive day this URL has been in the sitemap without resolving to a live page. DeployCo is an OpenAI subsidiary involved in AI deployment services; the persistent sitemap presence with refreshing timestamps suggests an active publishing pipeline that has not yet made the page public. Needs continued monitoring.

### Batch Update Summary (All Timestamp-Only — No Content Changes Detected)

| Batch | Time cluster (UTC) | # Pages | Category |
|---|---|---|---|
| Research/publication CMS deploy | 2026-05-24T21:48–21:50 | 117 | Legacy research papers, announcements, old model posts |
| Customer stories | 2026-05-25T08:12–08:45 | 22 | Brand-stories and index/ customer case studies, + business/customer-stories/ |
| Academy / Codex tutorials | 2026-05-25T04:34–05:03 | 11 | Codex how-to and use-case guides |
| Signals product pages | 2026-05-25T05:57–09:04 | 5 | signals/, signals/b2b/, signals/data/, signals/research/, signals/data-download/ |
| Other | various | 3 | form/guaranteed-capacity/, index/the-next-phase-of-education-for-countries/, about/ |

The research batch is the most notable by size: ~117 pages all with new timestamps within 2.5 minutes of each other suggests a single CMS deployment pass. Sampled pages (GPT-4 Research, Sora, Hello GPT-4o) show zero content difference vs. prior snapshots.

### Fetch Failures

| URL | Status |
|-----|--------|
| https://openai.com/deployco/privacy-policy/ | HTTP 404 — in sitemap with lastmod 2026-05-25T09:10Z, page not found (day 6) |

**Stats:** 1,323 total URLs | +0 added | 158 lastmod-changed (all CMS/CDN deploys, 0 substantive content changes) | 0 removed | 1 anomaly | 1 fetch failure | 32 sub-sitemaps

---

## 2026-05-24 — Signals Data Download Expands; Codex Academy Share Buttons Removed; Sitemap Lists 404 DeployCo Privacy Policy (Day 5)

**TL;DR:** A quiet day with no new pages and no removals. The one genuinely new piece of content is on the **OpenAI Signals** data-download page, which added a download link for the **AI Jobs Transition Framework** dataset — an extension of the economic research initiative that previously only offered ChatGPT usage data. Thirteen Codex Academy pages had their "Share" button removed in a minor UI cleanup. The bulk of the 157 lastmod-bumped URLs are CMS metadata touches (126 with no rendered content change) and sitewide "related articles" widget rotations updating to surface newer posts like the Gartner/Codex leader announcement and the discrete-geometry conjecture result. One lingering anomaly: `deployco/privacy-policy/` remains in the sitemap with a fresh today's timestamp but returns HTTP 404 — now five days running.

### Anomalies

**ANOMALY — `deployco/privacy-policy/` still 404 (day 5 in sitemap):** The page `https://openai.com/deployco/privacy-policy/` was listed in today's sitemap with lastmod `2026-05-24T05:46:28.870Z` but returns HTTP 404. This is the fifth consecutive day this URL has appeared in the sitemap without a live page. The `deployco/terms-of-use/` page is no longer in the current sitemap (last seen 2026-05-23), but the privacy-policy remains. The sitemap is making a fresh claim (today's timestamp) about a page that doesn't exist. Prior content preserved in git history.

### Notable Content Update

**[Signals data download](pages/openai.com/signals/data-download/index.md)** — A new section "Report data and methodology" was appended, adding a download link for the [AI Jobs Transition Framework data](http://cdn.openai.com/signals/ai-job-transition-framework-data-download.zip). Previously the page only offered ChatGPT usage data (CSV files + data dictionary, citing an NBER working paper on "How People Use ChatGPT"). The AI Jobs Transition Framework is a separate OpenAI research initiative examining how AI affects employment transitions; making the underlying data publicly downloadable is a meaningful expansion of the Signals open-data commitment.

### Routine Updates

- **13 Codex Academy pages**: "Share" button removed from rendered output (UI cleanup). Affected pages: `codex-automations/`, all `codex-for-work/*` sub-pages, `codex-how-to-start/`, `codex-plugins-and-skills/`, `codex-settings/`, `how-finance-teams-use-codex/`, `top-10-use-cases-codex-for-work/`, `what-is-codex/`, `working-with-codex/`, plus the education article and model-spec post.
- **~17 customer story and research pages**: "Related articles" widgets rotated to surface newer content: "OpenAI named a Leader in enterprise coding agents by Gartner" (May 22), "How Virgin Atlantic ships faster with Codex" (May 22), "AdventHealth advances whole-person care with OpenAI" (May 21), "An OpenAI model has disproved a central conjecture in discrete geometry" (May 20).
- **126 pages**: Lastmod bumped, no visible content change (CMS metadata-only touches across research papers and customer stories, in two waves: ~06:34–06:36 UTC and ~07:29–07:31 UTC).
- **`research/index/` and `news/research/`**: "Introducing GPT-5.5" and "GPT-5.5 System Card" swapped display order — no content change, just listing reordering.

### Fetch Failures

| URL | Status |
|-----|--------|
| https://openai.com/deployco/privacy-policy/ | HTTP 404 — listed in sitemap with today's lastmod but page does not exist (day 5) |

**Stats:** 1,323 total URLs | +0 added | 157 lastmod-changed (1 substantive content addition, 13 UI changes, 143 CMS/widget touches) | 0 removed | 1 anomaly | 1 fetch failure | 32 sub-sitemaps

---

## 2026-05-23 — Gartner Names OpenAI a Leader in Enterprise AI Coding Agents; Virgin Atlantic Codex Story; Codex Security Features Added

**TL;DR:** The headline today is a Gartner analyst recognition: OpenAI published an announcement and a gated report download page declaring it has been named a **Leader in the Gartner® Magic Quadrant™ for Enterprise AI Coding Agents** (Gartner's evaluation was done in April 2026, report published May 20). The announcement claims Codex has **4 million weekly users** and enterprise customers including Cisco, Datadog, Dell, and NVIDIA; a limited-time promotion (through June 12) offers enterprise accounts 2 months of free Codex for new users. A **Virgin Atlantic customer story** went live detailing how the airline shipped its revamped mobile app with zero P1 defects, reduced legacy codebases by 78–80%, and cut 2-week refactors to 30 minutes — all using Codex. The **Daybreak page** received a real content addition: three new Codex Security feature descriptions (threat-model builder, vulnerability validation, automated detection). The **customer stories listing page** was refreshed with 5 new entries rotating off 4 older ones. On the anomaly front: **88% of all indexed URLs had their lastmod timestamps updated** overnight in a clear CMS-wide rebuild event with no real content change; and the two Deployco legal pages (Privacy Policy, Terms of Use) that appeared in the sitemap yesterday are still returning HTTP 404 — the mystery deepens.

### Anomalies

**ANOMALY — Mass CMS Timestamp Flood (88% of all URLs):** 1,169 of 1,323 URLs had lastmod updated between 2026-05-22T18:00Z and 2026-05-23T09:00Z. The largest wave (886 URLs) hit at 2026-05-22T18–19Z; a second wave (266 URLs) ran 2026-05-23T00–08Z. Spot-checked pages showed zero content change. This is consistent with a CMS rebuild or cache purge and does not represent 1,169 real edits. This pattern repeats from prior runs; flagging here for awareness.

**ANOMALY — Deployco Pages: HTTP 404 for Day 4 (sitemap ghost URLs):** `https://openai.com/deployco/privacy-policy/` and `https://openai.com/deployco/terms-of-use/` remain in the sitemap with updated timestamps (latest: 2026-05-23T08:57Z and 03:12Z respectively) but return HTTP 404 when fetched. This is the 4th consecutive day that at least one Deployco URL has been live in the sitemap but unreachable. No prior snapshot exists to preserve. Needs follow-up.

### New Pages (3 Added)

**[OpenAI named a Leader in enterprise coding agents by Gartner](pages/openai.com/index/gartner-2026-agentic-coding-leader/index.md)** *(AI Adoption, May 22, 2026)*

OpenAI was named a Leader in the **Gartner® Magic Quadrant™ for Enterprise AI Coding Agents** (Gartner evaluated in April 2026, published May 20). Key claims in the announcement: Codex has **4 million weekly users**; Cisco used Codex to build "the majority of its AI Defense security platform," cutting delivery time from several quarters to weeks. A temporary promo runs until June 12: enterprise accounts that contact sales can get 2 months of free Codex for new users. Denise Dresser (CRO) calls Codex "one of OpenAI's fastest-growing enterprise products." Gartner's citation: Magic Quadrant for Enterprise AI Coding Agents, Phillip Walsh et al., May 20, 2026.

**[Download the Gartner Magic Quadrant (gated form)](pages/openai.com/business/learn/gartner-2026-agentic-coding-leader/index.md)** *(Lead-gen, May 22, 2026)*

Paired landing page with a form (work email, name, company, size, existing customer) to download the full Gartner report. This is the gated companion to the public announcement above — a standard analyst-report lead-gen page.

**[How Virgin Atlantic ships faster with Codex](pages/openai.com/index/virgin-atlantic/index.md)** *(Customer Story, May 22, 2026)*

Virgin Atlantic deployed Codex to ship its revamped mobile app in time for the Christmas travel rush. Key metrics: **78–80% codebase size reduction** on legacy refactors; **~100% unit test coverage** on new app; **2-week refactors now take 30 minutes**; **zero P1 defects at launch**. Neil Letchford (VP Digital Engineering): "The ability to utilize Codex to improve the quality of the application before it got into the hands of our customers was a game-changer." The story also covers Codex unblocking data warehouse migrations and enabling analyst teams to build internal apps directly. Follows AdventHealth (May 21), Ramp (May 20), and Databricks (May 15) in a rapid cadence of enterprise Codex stories.

### Notable Content Updates

**[Daybreak](pages/openai.com/daybreak/index.md)** — Real content addition: three new Codex Security feature descriptions added to the page: "Find and fix vulnerabilities" (builds editable threat model from repo, focuses on realistic attack paths), "Burn down the backlog" (validates vulnerabilities in isolated environment to prioritize real issues over alert noise), "Automate detection and response" (AI-driven monitoring for high-risk vulnerabilities). Image asset also updated. This reinforces Codex Security as a distinct product capability within the Daybreak/security umbrella.

**[Customer Stories listing](pages/openai.com/business/customer-stories/index.md)** — Refreshed to show 5 new stories (Virgin Atlantic, AdventHealth, Ramp, Databricks, Simplex) while rotating 4 older ones off the listing (CyberAgent, Gradient Labs, STADLER, Wayfair). The rotated-off stories still exist individually in the sitemap; only the listing page changed. All 5 new featured stories are Codex-focused.

### Fetch Failures

| URL | Status |
|-----|--------|
| https://openai.com/deployco/privacy-policy/ | HTTP 404 — day 4 in sitemap, still unreachable |
| https://openai.com/deployco/terms-of-use/ | HTTP 404 — day 4 in sitemap, still unreachable |

**Stats:** 1,323 total URLs | +3 added | 1,169 lastmod-changed (mass CMS rebuild, ~0 real content changes on sampled pages; 2 real updates confirmed: `/daybreak/`, `/business/customer-stories/`) | 0 removed | 3 anomalies | 2 fetch failures | 32 sub-sitemaps

---

## 2026-05-22 — AdventHealth Case Study; Retail & Agents Pages Expanded; DeployCo Legal Pages Pre-Staged

**TL;DR:** Today's most substantive changes are on OpenAI's solutions pages: the **Retail industry page** grew by six new concrete AI use-case descriptions (shopping research, store teams, marketing creative, conversational shopping, supplier negotiations, store visits), and the **Agents use-case page** added four new enterprise workflow examples (lead qualification, IT requests, marketing content, product feedback). A new healthcare **customer story for AdventHealth** went live — a 9-state hospital system reporting 80% reduction in administrative task time using ChatGPT for Healthcare. The **Guaranteed Capacity sign-up form** was significantly redesigned, expanding from 3 endpoint regions to 10+ (US, EU, UK, Middle East, Japan, Korea, India, ANZ, ASEAN) and removing the TPM capacity estimate field. Most intriguingly, two new **DeployCo legal pages** (Privacy Policy + Terms of Use) appeared in the sitemap alongside the existing DeployCo landing page — all three return HTTP 404, now for the third consecutive day, suggesting an imminent launch of whatever "DeployCo" is. The Plugin Terms of Use was quietly removed from the sitemap. Of 131 lastmod-changed URLs, only 20 had true content differences; 110 were CMS timestamp-only touches.

### Anomalies

None. No future-dated lastmods, no backwards timestamp movements, no disappeared-then-reappeared URLs.

### Fetch Failures (Ongoing — DeployCo Mystery)

**`https://openai.com/deployco/`** (updated in sitemap, HTTP 404 — day 3)  
**`https://openai.com/deployco/privacy-policy/`** (new in sitemap, HTTP 404)  
**`https://openai.com/deployco/terms-of-use/`** (new in sitemap, HTTP 404)

DeployCo first appeared in the sitemap on May 20 and has returned 404 every day since. Today, legal pages for Privacy Policy and Terms of Use were added to the sitemap — also 404. The addition of legal pages strongly indicates this is a complete product entity (or newly-acquired company) being prepared for launch. The parent URL received a fresh lastmod timestamp today (`2026-05-22T00:07:03Z`), showing active CMS backend work. Assessment: launch appears imminent, likely within days.

### New Page: AdventHealth Case Study

**[AdventHealth advances whole-person care with OpenAI](pages/openai.com/index/adventhealth/index.md)** *(published May 21, 2026)*

AdventHealth is a hospital system across 9 states. They deployed ChatGPT for Healthcare to reduce administrative burden for physicians and operational staff. Key stats and claims:

- **80% reduction in time spent on administrative tasks** (headline figure)
- Main use case: utilization management — AI generates structured summaries of patient charts and drafts clinical rationales; the clinician makes the final call
- Framing: "We don't talk about AI as automation. We talk about time back."
- Success metric: messages per user per business day, tracked like any other KPI
- Rollout model: domain-based peer groups (finance with finance, HR with HR) rather than centralized training
- Quotes Rob Purinton, Chief AI Officer: "Adoption is not 'go use the product.' It's change leadership."
- Product used: ChatGPT Enterprise → ChatGPT for Healthcare

This is the third healthcare-focused case study in recent weeks, alongside broader enterprise vertical expansion. It fits with the pattern of OpenAI building out industry-specific ChatGPT variants.

### Notable Content Updates

**[Retail Industry Solutions](pages/openai.com/solutions/industries/retail/index.md)** — The retail page added six substantial new use-case sections (+3,355 chars). Topics: ChatGPT shopping research for consumers, AI companion tools for store associates, localized marketing creative generation, conversational product discovery, AI-assisted supplier negotiations, and converting store-visit field notes into action plans.

**[Agents Use Case](pages/openai.com/solutions/use-case/agents/index.md)** — Added four new concrete agent workflow examples (+2,039 chars): qualifying and routing leads (research → score → CRM update), reviewing IT requests (evaluate → compare approved systems → document in Slack), creating marketing content at scale (brief → multi-format drafts), and analyzing product feedback (aggregate → summarize → create tickets). All are multi-step, cross-tool workflows.

**[Guaranteed Capacity Form](pages/openai.com/form/guaranteed-capacity/index.md)** — Significant form redesign. Workload dropdown options renamed (e.g., "Codex BYOK" → "Codex", "Customer-facing product" → "API production environment"). Endpoint/region options expanded from 3 to 10+: now includes EU, UK, Middle East, Japan, Korea, India, ANZ, ASEAN alongside US and global. The "Estimated guaranteed capacity need" field (with TPM tiers up to 500M–1B) was removed entirely. This signals active enterprise sales expansion across Asia-Pacific and the Middle East.

**Keep Reading / Related Articles refreshed** — Multiple article pages (gpt-5-2-codex, databricks, nvidia, and others) had their "Keep reading" carousels updated to feature the new AdventHealth story and other recent posts. Ten OpenAI Academy Codex pages reordered their "How sales teams use Codex" link to the top of their related articles section. These are CMS-level content rotation changes with no body text changes.

### Removed

**`https://openai.com/policies/plugin-terms/`** — ChatGPT Plugins were deprecated in 2024; this is the Plugin Terms of Use document being removed from the sitemap. Final cleanup of plugin-era legal documents. Last snapshot preserved in git history.

**Stats:** 1,320 total URLs | +3 added | 131 lastmod-changed (20 true content changes, 110 CMS-only) | -1 removed | 0 anomalies | 3 fetch failures (all DeployCo) | 32 sub-sitemaps

---

## 2026-05-21 — AI Proves 80-Year-Old Math Conjecture; ChatGPT Pages Migrate to chatgpt.com

**TL;DR:** The headline today is a genuine AI research milestone: an internal OpenAI reasoning model autonomously **disproved the planar unit distance conjecture**, a famous open problem in combinatorial geometry that Paul Erdős posed in 1946. Fields medalist Tim Gowers calls it "a milestone in AI mathematics." Separately, the six main ChatGPT product pages on openai.com (enterprise, team, education, overview, pricing, desktop) were removed from the sitemap — continuing the migration of ChatGPT product content from openai.com to chatgpt.com. The 174 other "updated" URLs are a CMS artifact: ~100 had zero content change and the rest only rotated which articles appear in "Keep reading" carousels.

### Anomalies

None. No future-dated lastmods, no timestamps moving backwards, no reappeared URLs.

### Flagship New Page: AI Disproves Erdős Geometry Conjecture

**[An OpenAI model has disproved a central conjecture in discrete geometry](pages/openai.com/index/model-disproves-discrete-geometry-conjecture/index.md)** *(Research / Milestone, published May 20, 2026)*

For 80 years, mathematicians believed the "square grid" construction was essentially the best way to arrange n points in the plane to maximize the number of unit-distance pairs (pairs of points exactly distance 1 apart). An OpenAI general-purpose reasoning model — not a system trained specifically for math — disproved this conjecture by constructing configurations with polynomially more unit-distance pairs than any square-grid arrangement. The proof uses sophisticated tools from **algebraic number theory** (infinite class field towers, Golod–Shafarevich theory) that specialists had never connected to this geometric problem.

External verification: The proof was reviewed by leading mathematicians including Fields medalist Tim Gowers, Noga Alon (Princeton), and Arul Shankar (Princeton). Gowers says he would recommend it for the Annals of Mathematics "without any hesitation." The full proof, companion remarks, and an abridged model chain-of-thought are available as PDFs on OpenAI's CDN.

**Why this matters:** OpenAI frames this as the first time AI has autonomously resolved a prominent open problem at the center of an active mathematical subfield — not just verified a human proof, but discovered new mathematics. They position this as evidence that the same deep reasoning ability that works in mathematics can transfer to biology, physics, materials science, and medicine.

### New Brand Story: Ramp + Codex

**[How Ramp engineers accelerate code review with Codex](pages/openai.com/index/ramp/index.md)** *(Brand story, May 20, 2026)*

Ramp, an enterprise expense management company, describes using Codex with GPT-5.5 for code review and internal agentic tooling. Austin Ray (AI DevEx lead) says Codex is "industry gold standard" and reviews PRs in minutes with a "level of thoroughness that most human reviewers don't have time for." Follows similar case studies for Databricks, Dell, and Sea's David Chen.

### Structural Change: ChatGPT Pages Leaving openai.com

**7 URLs removed** from the sitemap, all in the `/chatgpt/` section:

| Removed from openai.com | Likely now at chatgpt.com |
|---|---|
| `/chatgpt/desktop/` | `chatgpt.com/download` |
| `/chatgpt/education/` | `chatgpt.com/business/education` |
| `/chatgpt/enterprise/` | `chatgpt.com/business/enterprise` |
| `/chatgpt/overview/` | `chatgpt.com/overview` |
| `/chatgpt/pricing/` | `chatgpt.com/pricing` |
| `/chatgpt/team/` | `chatgpt.com/business/business-plan` |
| `/chatgpt/use-cases/student-writing-guide/` | unclear |

This continues the brand separation first observed May 20: openai.com is becoming a research/API/company hub while chatgpt.com handles consumer and business product experiences. The footer of today's pages confirms this routing. Snapshots of all removed pages are preserved in this repo's git history.

### Notable Content Updates

- **`/solutions/use-case/content-creation/`**: Added a new content block about creating UI/UX mockups and concept visuals with ChatGPT. Substantive addition.
- **`/startups/`**: Added ~20 lines of how-to guidance for getting started on the OpenAI platform. Substantive addition.
- **`/deployco/`** (still unresolved): In the sitemap again (lastmod advanced to 2026-05-21T00:05Z), but the page is still returning invalid content when fetched. Monitoring continues.

### What the "174 Updates" Really Mean

The sitemap showed 174 lastmod changes, but inspection shows three distinct clusters with very different meanings:

1. **~100 pages at 02:13 UTC**: Zero content change. Likely a CMS deployment that touches all metadata. Do not interpret as editorial updates.
2. **~70 pages at 07:30–09:17 UTC**: Only the "Keep reading" article carousel changed (rotating in the geometry conjecture post and Ramp story). No article body content changed.
3. **Small set with real changes**: `/solutions/use-case/content-creation/`, `/startups/`, and a few minor typographic/asset fixes.

**Stats:** 1318 total URLs | +2 added | ~174 lastmod-changed (mostly CMS artifact) | -7 removed | 0 anomalies | 1 fetch failure (`/deployco/`) | 32 sub-sitemaps

---

Daily changelog of [openai.com](https://openai.com)'s public website,
maintained by a Claude Code routine. Each run diffs the current sitemap
against the prior one, fetches changed pages, and writes a plain-language
summary that a smart layperson can follow.

## 2026-05-20T09-16Z

**Fetch time:** 2026-05-20T09:16:48Z UTC | **Baseline:** 2026-05-18T09-15Z

**TL;DR:** A busy day across every dimension of OpenAI's public presence. The most structurally significant change is the **mass removal of 7 openai.com/chatgpt/* pages** from the sitemap — desktop, education, enterprise, overview, pricing, team, and the student writing guide — which are migrating to chatgpt.com (the enterprise button now points to `chatgpt.com/business/enterprise`). New product: **OpenAI Guaranteed Capacity**, a 1–3 year compute commitment program with volume discounts for enterprises — the announcement page, sign-up form, and companion Codex feedback form all went live simultaneously this morning. The research team published a **public image-provenance verification tool** at `research/verify/` that lets anyone check whether an image was generated by OpenAI tools using C2PA metadata or Google SynthID watermarks, part of a broader safety initiative detailed in a new "Advancing Content Provenance" blog post. International expansion continues: **OpenAI for Singapore** launched at the ATx Summit with an S$300M+ commitment, and **Singapore also joined the Education for Countries program** announced at the Education World Forum in London. A Dell Technologies partnership extends Codex into hybrid/on-premises enterprise environments. Both the ChatGPT pricing page and the API pricing page gained large FAQ sections answering common billing and feature questions. One mysterious URL — `/deployco/` — appeared in the sitemap but returned 404 when fetched; needs follow-up.

### Anomalies

None detected.

### Fetch Failures

- **`/deployco/`** — URL appeared in sitemap (lastmod: 2026-05-20T03:43:12Z, ~6 hours before the run) but returned HTTP 404 when fetched. The name hints at a new "Deployment Company" product page or similar. Possibly staged but not yet live. Will monitor in the next run.

### Major Structural Change: ChatGPT pages migrating to chatgpt.com

**7 URLs removed** from openai.com's sitemap, all in the `/chatgpt/` section:

| Removed Page | Last Seen | Content |
|---|---|---|
| `/chatgpt/desktop/` | 2026-04-09 | Desktop app marketing page |
| `/chatgpt/education/` | 2026-04-22 | ChatGPT for educators |
| `/chatgpt/enterprise/` | 2026-05-07 | Enterprise product page |
| `/chatgpt/overview/` | 2026-05-10 | ChatGPT overview hub |
| `/chatgpt/pricing/` | 2026-05-12 | ChatGPT plan pricing |
| `/chatgpt/team/` | 2026-05-12 | ChatGPT Team plan |
| `/chatgpt/use-cases/student-writing-guide/` | 2026-04-20 | Student writing guide |

This is not content deletion — these pages are moving to chatgpt.com. Confirmation: the business page updated its "Learn about ChatGPT Enterprise" link from `openai.com/chatgpt/enterprise/` to `https://chatgpt.com/business/enterprise`. Markdown snapshots of all removed pages are preserved in this repo's git history.

### New Pages (9 added)

- **[OpenAI Guaranteed Capacity](pages/openai.com/business/guaranteed-capacity/index.md)** *(lastmod: 2026-05-20T09:10Z; Business)* — New enterprise product: long-term compute commitments of 1–3 years with volume discounts, giving organizations certainty of access to OpenAI infrastructure for their highest-priority AI workflows and agents. A companion lead-capture form at `/form/guaranteed-capacity/` launched simultaneously. This signals OpenAI is now offering AWS/Azure-style capacity reservation deals.

- **[Advancing Content Provenance](pages/openai.com/index/advancing-content-provenance/index.md)** *(pub: May 19, 2026; Safety)* — OpenAI announces C2PA standard conformance for its image generation tools and integration of Google SynthID watermarking, enabling multi-layer provenance signals on all OpenAI-generated images. Introduces a public verification tool (see research/verify/ below) and outlines plans for broader content transparency. Accompanied by the new image-verification tool.

- **[Verify OpenAI-generated images](pages/openai.com/research/verify/index.md)** *(lastmod: 2026-05-20T08:45Z; Research preview)* — Public tool where anyone can upload an image to check whether it contains C2PA metadata or SynthID watermarks indicating it was generated by OpenAI tools (ChatGPT, API, or Codex). Currently a research preview. Directly tied to the content provenance safety initiative.

- **[OpenAI + Dell Codex Enterprise Partnership](pages/openai.com/index/dell-codex-enterprise-partnership/index.md)** *(pub: May 18, 2026; Company)* — OpenAI and Dell Technologies announce collaboration to deploy Codex in hybrid and on-premises enterprise environments. Codex (used by 4M+ developers/week) will connect with the Dell AI Data Platform and Dell AI Factory, bringing AI coding and automation to customers who need on-premises data governance.

- **[Introducing OpenAI for Singapore](pages/openai.com/index/introducing-openai-for-singapore/index.md)** *(pub: May 19, 2026; Global Affairs)* — Launched at the ATx Summit in Singapore, this S$300M+ partnership with the Ministry of Digital Development and Information covers: frontier AI deployment for Singapore's national AI strategy, AI talent development, and broad economic access to AI. Singapore positions itself as an "AI-powered economy."

- **[The Next Phase of OpenAI's Education for Countries](pages/openai.com/index/the-next-phase-of-education-for-countries/index.md)** *(pub: May 20, 2026; Global Affairs)* — Update from the Education World Forum in London. Singapore joins the Education for Countries program. Existing cohort: Estonia, Greece, Italy's CRUI, Slovakia, Trinidad & Tobago, Kazakhstan, UAE, and Jordan. Program focuses on large-scale, government-led AI-in-education research with a responsible-adoption mandate.

- **[/form/codex-project-showcase-and-feedback/](pages/openai.com/form/codex-project-showcase-and-feedback/index.md)** — New form for Codex users to submit projects for showcase and provide product feedback.

- **`/deployco/`** — In sitemap but returns 404. See Fetch Failures above.

### Notable Updates

- **[Homepage (/)](pages/openai.com/index.md)** — Featured article card swapped: "Introducing Advanced Account Security" (Apr 30) replaced by "Advancing content provenance" (May 19). Routine carousel rotation.

- **[Business page (/business/)](pages/openai.com/business/index.md)** — "Learn about ChatGPT Enterprise" button link changed from `openai.com/chatgpt/enterprise/` → `chatgpt.com/business/enterprise`. Reflects the chatgpt.com migration.

- **[ChatGPT Pricing (/business/chatgpt-pricing/)](pages/openai.com/business/chatgpt-pricing/index.md)** — Appended a new 8-question FAQ section. Key new facts: ChatGPT "Go" plan explicitly named; K–12 teachers in the U.S. get a free plan through June 2027; universities get ChatGPT Edu; nonprofits can get up to **75% discounts** on Business or Enterprise through "OpenAI for Nonprofits"; Business plans start at 2 users; credit card accepted for most plans, invoicing available for Enterprise.

- **[API Pricing (/api/pricing/)](pages/openai.com/api/pricing/index.md)** — Appended a large 7-question FAQ section. Key additions: model selection guidance (large vs. mini, reasoning vs. general); confirmation that Playground usage is billed the same as API; instructions for setting monthly spend limits; clarification that API is billed separately from ChatGPT subscriptions; image token pricing calculator revealed (detailed breakdown of tile calculations for `gpt-5`, `gpt-4.1`, etc.).

### Routine Updates (148 total lastmod changes)

- **72 /index/ blog posts** — Mix of CMS metadata sweep (41 on May 18, 27 on May 20). No substantive content changes detected.
- **25 /global-affairs/ pages** — 25 swept on May 18, 1 on May 20 (new Singapore article). Routine.
- **12 /academy/ Codex pages** — Minor updates to Codex Academy educational content (timestamps 2026-05-20).
- **12 /form/ pages** — CMS batch update (~09:07 UTC), no content changes.
- **6 /policies/ pages** — Routine policy maintenance.
- **Other sections** (brand, business-data, daybreak, news, podcast, signals, solutions, transparency-and-content-moderation): 1–2 pages each, routine.

**Stats:** 1,316 total URLs | +9 added | 148 updated (lastmod) | 7 removed | 0 anomalies | 1 fetch failure | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-20T09-16Z/diff.json](runs/2026-05-20T09-16Z/diff.json) | [runs/2026-05-20T09-16Z/analysis.md](runs/2026-05-20T09-16Z/analysis.md)*

---

## 2026-05-17T09-15Z

**Fetch time:** 2026-05-17T09:15:42Z UTC | **Baseline:** 2026-05-16T09-15Z

**TL;DR:** One new article today: Malta and OpenAI announced a "world's first" national partnership under the OpenAI for Countries program — every Maltese citizen can get free ChatGPT Plus for one year after completing a government-backed AI literacy course developed by the University of Malta. The initiative, called "AI for All," is managed by the Malta Digital Innovation Authority and launches in May 2026. George Osborne is identified as "Head of OpenAI for Countries," signaling this is a named, dedicated OpenAI program (already active in Estonia and Greece for education). Elsewhere, 33 URLs received lastmod updates, but content diffs show only one substantive change: the Astral acquisition article's "Keep reading" recommendation carousel rotated to show more recent articles (TanStack npm security post, Deployment Company launch, Campus Network interest form), and the global-affairs news hub now lists the Malta article. All other timestamp bumps — including a batch sweep of 16 teen-safety pages at ~05:35 UTC and a sweep of news hubs, policy pages, and the podcast page — show no visible content change. The `amex-chatgpt-business/` URL continues to appear as "removed" due to a legacy-file artifact in the repository; it has been absent from OpenAI's live sitemap since May 14. No anomalies.

### Anomalies

None detected.

### New Pages (1 added)

**[OpenAI and Malta partner to bring ChatGPT Plus to all citizens](pages/openai.com/index/malta-chatgpt-plus-partnership/index.md)** *(lastmod: 2026-05-16T10:31:32Z; Global Affairs)* — Malta and OpenAI announced what they call the world's first national partnership of this type: Maltese citizens who complete a free AI literacy course (developed by the University of Malta, covering what AI is, what it can't do, and how to use it responsibly at home and work) unlock one year of ChatGPT Plus at no cost to them. Distribution is managed by the Malta Digital Innovation Authority; the first phase launches in May 2026. The partnership is branded as part of **OpenAI for Countries** — a named program designed to take governments from early AI interest to strategic national adoption, with tailored priorities (education, workforce training, AI literacy) rather than a one-size-fits-all model. Malta's angle is civic AI literacy at population scale, with the University-designed course as the gating mechanism. The article explicitly positions this as a model for other countries: "Where Malta leads, I hope others will follow" (George Osborne, Head of OpenAI for Countries). Malta joins Estonia and Greece already cited as OpenAI for Countries partners.

### Notable Page Updates

- **[openai.com/index/openai-to-acquire-astral/](pages/openai.com/index/openai-to-acquire-astral/index.md)** — "Keep reading" recommendation carousel at the bottom of the page rotated. Previous recommendations (from May 6 and Apr 27 posts) replaced with: "Our response to the TanStack npm supply chain attack" (May 13), "OpenAI Campus Network: Student club interest form" (May 11), and "OpenAI launches the Deployment Company" (May 11). Article content unchanged.

- **[openai.com/news/global-affairs/](pages/openai.com/news/global-affairs/index.md)** — Malta article now appears in the hub listing. The older Cloudflare OpenAI Agent Cloud article (Apr 13) rotated off the featured section.

- **16 teen-safety and child-safety pages** received simultaneous lastmod bumps around 05:35 UTC with no visible content change — consistent with a CMS batch refresh of the teen-safety content cluster published in recent weeks.

- **Policy pages** (`/policies/conversion-dpa/`, `/policies/conversion-subprocessors/`, `/policies/conversion-terms/`, `/policies/kr-privacy-policy/`) and **`/podcast/`** received lastmod updates with no visible content change.

### Removed from Sitemap (1, artifact)

- **`https://openai.com/amex-chatgpt-business/`** — Recurring artifact: this URL has been absent from OpenAI's live sitemap since May 14. It keeps appearing in the baseline because legacy-named files from early runs remain in `sitemaps/openai.com/sub/latest/`. State records `last_seen = 2026-05-13T09-15Z`.

**Stats:** 1,314 total URLs | +1 added | 33 updated (lastmod) | 1 removed (artifact) | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-17T09-15Z/diff.json](runs/2026-05-17T09-15Z/diff.json) | [runs/2026-05-17T09-15Z/analysis.md](runs/2026-05-17T09-15Z/analysis.md)*

---

## 2026-05-18T09-15Z

**Fetch time:** 2026-05-18T09:16:52Z UTC | **Baseline:** 2026-05-17T09-15Z

**TL;DR:** No new pages or removals today. The 36 `<lastmod>` updates break into three clusters: (1) a **teen/child safety content sweep** — 15 safety-section pages had their sitemap timestamps refreshed again around 08:33 UTC (this is the third consecutive daily batch sweep of this cluster; content diffs show only the "Keep reading" recommendation carousels rotating, not new substantive text); (2) a **routine CMS refresh** of six news-hub landing pages and four product pages including `running-codex-safely`, `work-with-codex-from-anywhere`, and the GPT-5.5 article (the GPT-5.5 "Keep reading" box swapped out the "Testing ads in ChatGPT" link for "A new personal finance experience in ChatGPT," reflecting the May 15 launch); and (3) a **Conversion policy trio** (`conversion-terms`, `conversion-dpa`, `conversion-subprocessors`) quietly refreshed early this morning — the published date still reads May 14 and no text changed, so this looks like a backend CMS touch rather than a legal update. The `introducing-prism` page also got a lastmod bump (from May 5 → May 18) but no visible content change was detected. No anomalies.

### Anomalies

None detected.

### Notable Page Updates

- **Teen/child safety cluster (15 pages)** — For the third day running, the entire teen-safety content cluster received a simultaneous lastmod sweep (~08:33–34 UTC). Pages include `introducing-the-teen-safety-blueprint`, `updating-model-spec-with-teen-protections`, `teen-safety-policies-gpt-oss-safeguard`, `ai-literacy-resources-for-teens-and-parents`, `japan-teen-safety-blueprint`, and nine more. Content diffs show no substantive change; the `Keep reading` carousels rotated to surface more recent articles. This is likely an automated CMS republish triggered whenever the teen-safety content cluster is touched (possibly as OpenAI continues rolling out related work behind the scenes).

- **[/index/introducing-gpt-5-5/](pages/openai.com/index/introducing-gpt-5-5/index.md)** — The "Keep reading" section at the bottom of the GPT-5.5 release page was updated. The "Testing ads in ChatGPT" (May 7) recommendation was replaced with "A new personal finance experience in ChatGPT" (May 15). The main article content is unchanged. This is a routine carousel rotation.

- **[/index/introducing-prism/](pages/openai.com/index/introducing-prism/index.md)** — lastmod jumped from `2026-05-05` to `2026-05-18T08:05Z` — a 13-day gap, larger than other sweep items. No text differences detected in the rendered markdown. Could be a backend metadata or asset update. Prism is OpenAI's free AI-native scientific writing platform (a LaTeX workspace powered by GPT-5.2, built on the acquired Crixet platform).

- **[/form/enterprise-trusted-access-for-cyber/](pages/openai.com/form/enterprise-trusted-access-for-cyber/index.md)** — The "Trusted Access for Cyber" application form was refreshed (lastmod `2026-05-17T09:40Z`). This form lets vetted enterprise customers and cybersecurity practitioners apply for access to OpenAI's higher-risk dual-use cybersecurity capabilities — the pitch is that these tools are "powerful force multipliers for network defenders." Applicants must prove identity, professional use case, and OpenAI organization ID. This update follows the recent Axios and TanStack npm supply-chain security disclosures published on the same site.

- **[/form/codex-for-oss/](pages/openai.com/form/codex-for-oss/index.md)** — The open-source maintainer access form for Codex was also refreshed (lastmod `2026-05-17T09:39Z`). Selected maintainers get 6 months of ChatGPT Pro (includes Codex), conditional access to Codex Security, and API credits for coding/maintenance workflows.

- **Security posts** (`/index/axios-developer-tool-compromise/`, `/index/our-response-to-the-tanstack-npm-supply-chain-attack/`) — Both received lastmod bumps around 07:26 UTC with no visible content change. The Axios post advises macOS users to update apps before May 8 (already past); the TanStack post covers a North Korea-linked supply chain attack on the TanStack npm package.

- **Conversion policy trio** (`/policies/conversion-terms/`, `/policies/conversion-dpa/`, `/policies/conversion-subprocessors/`) — All three refreshed between 05:13–09:14 UTC. Published dates unchanged (May 14); no text differences detected. These govern how advertisers provide conversion data to OpenAI (part of OpenAI's advertising/measurement infrastructure launched with the Conversion Tools product).

**Stats:** 1,314 total URLs | +0 added | 36 updated (lastmod) | 0 removed | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-18T09-15Z/diff.json](runs/2026-05-18T09-15Z/diff.json) | [runs/2026-05-18T09-15Z/analysis.md](runs/2026-05-18T09-15Z/analysis.md)*

---

## 2026-05-16T09-15Z

**Fetch time:** 2026-05-16T09:17:04Z UTC | **Baseline:** 2026-05-15T09-15Z

**TL;DR:** Two headline launches today. First, OpenAI unveiled a **personal finance experience in ChatGPT** — Pro users in the U.S. can now connect their bank accounts and investment portfolios (via Plaid, 12,000+ institutions) and ask ChatGPT context-grounded questions about spending, goals, and tradeoffs. This is a major product step into personal financial services, directly competing with apps like Mint/Copilot/Monarch Money. Second, **Databricks published a case study** showing GPT-5.5 is now state-of-the-art on their OfficeQA Pro enterprise benchmark — 50% accuracy, 46% error reduction vs. GPT-5.4 — particularly for parsing scanned PDFs and legacy enterprise documents in long-running agent workflows. On the educational content side, OpenAI's Codex-for-work academy section kept expanding: three new role-specific guides appeared (for sales, data science, and business operations teams), and several existing Codex Academy pages were substantially expanded with cross-links and additional use cases. The stale `/amex-chatgpt-business/` URL (replaced by a `/business/`-hierarchy URL in the May 14 run) was finally cleaned from the sitemap. No anomalies.

### Anomalies

None detected.

### New Pages (5 added)

**[A new personal finance experience in ChatGPT](pages/openai.com/index/personal-finance-chatgpt/index.md)** *(lastmod: 2026-05-15T22:55:41Z)* — Announces a preview of a major new ChatGPT capability: Pro users in the U.S. can securely connect their financial accounts through Plaid (Intuit support coming), see a live dashboard of spending/portfolio/subscriptions, and ask ChatGPT questions grounded in their real financial data. The page touts ChatGPT's existing scale (200 million monthly users already asking money questions) and positions GPT-5.5's stronger reasoning as enabling more nuanced financial analysis. Supports saving "Financial memories" (e.g., ongoing savings goals) so context carries across conversations. OpenAI explicitly notes this is not a replacement for professional financial advice. Currently rolling out as a preview to Pro users before expanding to Plus and free tiers. Homepage carousel has been updated to feature this launch prominently.

**[Databricks brings GPT‑5.5 to enterprise agent workflows](pages/openai.com/index/databricks/index.md)** *(lastmod: 2026-05-16T00:28:31Z)* — Customer case study published May 15. Databricks integrated GPT-5.5 into their production agent harness after the model set a new state-of-the-art on OfficeQA Pro, their benchmark for complex enterprise document tasks (scanned PDFs, legacy files, long-context). Key metrics: **50% accuracy** on OfficeQA Pro (first model to cross that threshold) and **46% error reduction** vs. GPT-5.4. The gains are concentrated in parsing-heavy workflows where earlier models lost numerical precision on scanned digits. Databricks is now making GPT-5.5 available to their customer agent workflow builders.

**[How business operations teams use Codex](pages/openai.com/academy/codex-for-work/how-business-operations-teams-use-codex/index.md)** *(lastmod: 2026-05-16T07:17:13Z)* — Third entry in OpenAI Academy's role-specific Codex guides (the section was introduced May 14–15). Covers five use cases: off-track initiative briefs, strategic initiative health updates, leadership decision packets, board/company progress updates, and scenario/tradeoff models. Each use case shows how Codex aggregates scattered inputs (project trackers, KPI dashboards, meeting notes, Slack threads, spreadsheets) and produces the first working draft, with human judgment still owning the final recommendation.

**[How data science teams use Codex](pages/openai.com/academy/codex-for-work/how-data-science-teams-use-codex/index.md)** *(lastmod: 2026-05-16T07:17:12Z)* — Five use cases for data teams: KPI root-cause analysis, business impact readouts, analytics request agents, executive KPI reviews, and dashboard builder/monitor. Framing emphasizes that Codex handles the scaffolding (query structure, result formatting, presentation prep) while the data scientist owns analytical interpretation.

**[How sales teams use Codex](pages/openai.com/academy/codex-for-work/how-sales-teams-use-codex/index.md)** *(lastmod: 2026-05-16T07:17:06Z)* — Five use cases for sales: pipeline prioritization from underworked accounts, meeting prep and follow-up, forecast review and commit risk monitoring, strategic account plan refresh, and stalled deal diagnosis. Part of the same wave of role-specific Academy content; together these three guides represent OpenAI systematically building enablement material for the Codex-for-work non-developer audience introduced May 14.

### Notable Page Updates

- **[openai.com/](pages/openai.com/index.md)** (+68 chars) — Hero carousel rotated again: now leads with the personal finance feature ("A new personal finance experience in ChatGPT"). The previous featured story rolled off.

- **[openai.com/academy/codex-for-work/](pages/openai.com/academy/codex-for-work/index.md)** (+1,343 chars) — Hub page for the Codex-for-work section substantially expanded: now shows cards/previews for all three new role-specific guides (sales, data science, business operations) alongside the existing finance-teams guide.

- **[openai.com/academy/top-10-use-cases-codex-for-work/](pages/openai.com/academy/top-10-use-cases-codex-for-work/index.md)** (+3,479 chars) — The "Top 10 use cases" mega-page expanded significantly, now cross-linking to all new role-specific guides.

- **[openai.com/academy/how-finance-teams-use-codex/](pages/openai.com/academy/how-finance-teams-use-codex/index.md)** (+713 chars) — Finance teams guide updated with new related-content links pointing to the freshly published sales, data science, and business operations guides.

- Multiple other Codex Academy pages (codex-automations, codex-plugins-and-skills, what-is-codex, working-with-codex, etc.) received smaller updates (+43 to +299 chars) — primarily new "Explore Codex for work" navigation links and updated related-article cards pointing to the new role-specific guides.

All other timestamp changes (350+ URLs) show zero substantive content change — consistent with a routine CMS cache-invalidation sweep.

### Removed from Sitemap (1)

- **`https://openai.com/amex-chatgpt-business/`** — Cleanup: this URL was replaced by `/business/amex-chatgpt-business-credit/` in the May 14 run; the stale entry lingered in the sitemap one extra day before being removed.

**Stats:** 1,313 total URLs | +5 added | 391 updated (lastmod) | -1 removed | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-16T09-15Z/diff.json](runs/2026-05-16T09-15Z/diff.json) | [runs/2026-05-16T09-15Z/analysis.md](runs/2026-05-16T09-15Z/analysis.md)*

---

## 2026-05-15T09-15Z

**Fetch time:** 2026-05-15T09:17:53Z UTC | **Baseline:** 2026-05-14T09-15Z

**TL;DR:** Three parallel storylines dominated today. First, **Codex keeps expanding**: a new `codex/for-work/` landing page pitches Codex to non-developer business users (knowledge workers) for the first time, the main Codex page now links to it, and a product post announces Codex is coming to the ChatGPT mobile app (in preview) so users can supervise long-running agent tasks from their phones — OpenAI disclosed that 4 million people use Codex every week. Second, **a new advertising-infrastructure legal stack appeared**: three legal documents (Conversion Terms, Conversion DPA, and Conversion Sub-Processor List) were quietly published, indicating OpenAI is formalizing a conversion-tracking tool that lets advertisers share event data with OpenAI for measuring and optimizing ads — structurally similar to the Meta Pixel or Google Ads conversion API. Third, **a notable safety post** explained new ChatGPT features that carry short "safety summaries" across conversation sessions to better catch evolving risk signals in rare high-stakes scenarios (suicide, self-harm, harm-to-others). 395 URLs show updated lastmod timestamps; the vast majority are CMS cache-invalidation artifacts with no substantive content change.

### Anomalies

None detected. *(Note: the script flagged 1 "removed" URL — `https://openai.com/amex-chatgpt-business/` — but this is a stale-file artifact: that URL was genuinely removed in the May 13→14 run, and a legacy-named sub-sitemap file had lingered in `sitemaps/openai.com/sub/latest/`. It does not represent a new removal today.)*

### New Pages (7 added)

**[Codex for Work — "Get more done with Codex"](pages/openai.com/codex/for-work/index.md)** *(lastmod: 2026-05-14T22:45:49Z)* — A new `/codex/for-work/` landing page, distinct from the developer-facing `/codex/` page, aimed at non-technical business users. Pitches Codex as a general productivity layer: it can research topics, synthesize information, draft briefs and presentations, build weekly summaries from calendars/docs, and automate recurring tasks — all without requiring the user to write or understand code. Available as a desktop app for macOS and Windows. The main `/codex/` page was updated to cross-link here with an "Explore Codex for work" CTA.

**[Work with Codex from anywhere](pages/openai.com/index/work-with-codex-from-anywhere/index.md)** *(lastmod: 2026-05-15T08:35:26Z)* — Announces Codex is now in the ChatGPT mobile app (preview), allowing users to monitor and steer ongoing Codex agent sessions from their phones while the work runs on a laptop, a Mac mini, or a remote devbox. Highlights the "4 million people use Codex every week" stat and frames mobile as critical for the emerging human-in-the-loop pattern where quick check-ins prevent unnecessary agent rework. Also covers enterprise deployment modes where Codex runs on managed remote infrastructure.

**[Helping ChatGPT better recognize context in sensitive conversations](pages/openai.com/index/chatgpt-recognize-context-in-sensitive-conversations/index.md)** *(lastmod: 2026-05-15T04:13:15Z)* — Safety post describing two new features. (1) Cross-conversation safety summaries: a separate safety-reasoning model creates short factual notes about prior safety-relevant context (e.g., signs of distress) and passes them into subsequent sessions, scoped narrowly to high-risk scenarios and kept only for a limited time — not for general personalization. (2) Improved in-conversation context recognition trained with mental-health-expert guidance to detect escalating risk cues mid-conversation. Focus areas: suicide, self-harm, harm-to-others. OpenAI emphasizes these features fire rarely and are calibrated to avoid over-triggering on benign conversations.

**[Sea's View on the Future of Agentic Software Development with Codex](pages/openai.com/index/sea-david-chen/index.md)** *(lastmod: 2026-05-15T03:35:04Z)* — Episode 20 of OpenAI's "Executive Function" interview series, featuring David Chen, Co-Founder of Sea (Singapore-based company behind Shopee, Garena, SeaMoney) and Chief Product Officer of Shopee. Chen discusses Sea rolling out Codex across its entire development organization. Strong internal usage reported in code understanding, debugging, and feature development. Sea is also hosting the first regional Codex Hackathon Series across Asia — starting in Singapore then moving to Indonesia, Taiwan, and Vietnam. A notable endorsement from one of Southeast Asia's largest tech companies.

**[Conversion Terms](pages/openai.com/policies/conversion-terms/index.md)** *(effective: 2026-05-14; lastmod: 2026-05-15T09:14:15Z)* — Legal terms governing access to OpenAI's "Conversion Tools," which let advertisers provide "Conversion Data" (user event signals) to OpenAI. OpenAI uses this data to provide "Reporting Data," create custom audiences, and optimize/measure ad delivery. Comparable in structure to Meta's Conversion API or Google's Ads Data Hub. Advertisers must obtain necessary consents and cannot provide sensitive personal data.

**[Conversion Data Processing Addendum](pages/openai.com/policies/conversion-dpa/index.md)** *(effective: 2026-05-14; lastmod: 2026-05-15T08:45:20Z)* — The GDPR-facing DPA supplement to the Conversion Terms. Designates OpenAI and the customer as independent data controllers for most processing, with OpenAI acting as processor only for "Restricted Processing." References the Conversion Sub-Processor List for downstream data sharing.

**[Conversion Sub-Processor List](pages/openai.com/policies/conversion-subprocessors/index.md)** *(lastmod: 2026-05-15T08:15:37Z)* — Lists the third-party sub-processors OpenAI uses when handling Conversion Data in its processor capacity.

### Notable Page Updates

- **[openai.com/](pages/openai.com/index.md)** — Homepage hero carousel rotated: now surfaces "Work with Codex from anywhere" and "Helping ChatGPT better recognize context in sensitive conversations" (both new today). The prior featured items — "GPT-5.5 Instant" and the Amazon Bedrock/AWS partnership card — rolled off the front-page spotlight.

- **[openai.com/codex/](pages/openai.com/codex/index.md)** — Added "Explore Codex for work" link pointing to the new `/codex/for-work/` page (+228 chars). Now also shows macOS/Windows download availability explicitly.

- **[openai.com/business/](pages/openai.com/business/index.md)** — Minor update (+114 chars) mentioning Codex among the workspace-agent capabilities available on ChatGPT Business/Enterprise.

All other 390+ URL timestamp changes show zero substantive content change on the representative sample tested — consistent with a CMS-wide cache-invalidation sweep.

**Stats:** 1,308 total URLs | +7 added | 395 updated (lastmod) | 0 genuine removals | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-15T09-15Z/diff.json](runs/2026-05-15T09-15Z/diff.json) | [runs/2026-05-15T09-15Z/analysis.md](runs/2026-05-15T09-15Z/analysis.md)*
---

## 2026-05-14T09-15Z

**Fetch time:** 2026-05-14T09:15:53Z UTC | **Baseline:** 2026-05-13T09-15Z

**TL;DR:** The headline today is a security disclosure: OpenAI published a detailed account of how two employee laptops were infected via the "Mini Shai-Hulud" supply chain attack against the TanStack npm library on May 11, exposing limited internal source code and code-signing certificates for iOS, macOS, and Windows apps. No user data was compromised, but **macOS users must update all OpenAI apps by June 12, 2026** or they will stop working. Two other new pages arrived alongside it: a deep-dive engineering post explaining how OpenAI built a custom Windows sandbox for the Codex coding agent, and a refreshed co-branded American Express page (the old `/amex-chatgpt-business/` URL was retired and replaced with `/business/amex-chatgpt-business-credit/` offering $300/year in statement credits for Amex Business Platinum/Gold cardholders). 340 URL timestamps refreshed but a representative sample shows no substantive content changes.

### Anomalies

Two existing pages show `lastmod` timestamps ~15–22 seconds ahead of our fetch time — a benign race condition where the CMS updated those pages' timestamps while the sitemap was mid-generation:

- **near-future_lastmod** (CMS timing): `https://openai.com/index/accelerating-cyber-defense-ecosystem/` — lastmod `2026-05-14T09:16:15Z` vs. fetch at `2026-05-14T09:15:53Z` (22 sec gap)
- **near-future_lastmod** (CMS timing): `https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/` — lastmod `2026-05-14T09:16:11Z` vs. fetch at `2026-05-14T09:15:53Z` (18 sec gap)

Both are known, existing cybersecurity-related pages. These are the same pages whose related-article carousels were updated to surface today's new security disclosure.

### New Pages (3 added)

**[Our Response to the TanStack npm Supply Chain Attack](pages/openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/index.md)** — A security disclosure published May 13, 2026. The "Mini Shai-Hulud" attack compromised the TanStack npm library; two OpenAI employee devices were infected, leading to unauthorized access of a limited set of internal source code repositories. Code-signing certificates for iOS, macOS, and Windows were included in the exposed repos. OpenAI found no evidence of user data exposure or production system compromise. Key user action: **macOS users must update ChatGPT Desktop, Codex App, Codex CLI, and Atlas by June 12, 2026** — apps signed with the old certificate will stop launching after that date when it is revoked. (Windows and iOS users need not act.) OpenAI notes this is a repeat pattern, referencing the prior "Axios incident," and is accelerating supply-chain defenses.

**[Building a Safe, Effective Sandbox to Enable Codex on Windows](pages/openai.com/index/building-codex-windows-sandbox/index.md)** — An engineering deep-dive by David Wiesen (Member of Technical Staff), published May 13, 2026. Before this work, Windows Codex users had to choose between approving every agent command (tedious) or granting full access (risky). The post walks through why Windows AppContainer, Windows Sandbox VM, and Mandatory Integrity Control labeling were all unsuitable, then describes the two-phase custom sandbox OpenAI built — starting with an "unelevated sandbox" using ACLs and low-integrity tokens, then redesigning as an "elevated sandbox" for better enterprise compatibility. The result brings Windows Codex to parity with macOS/Linux: writes limited to the workspace, no internet by default, without admin prompts.

**[The First-of-Its-Kind ChatGPT Business Credit (Amex)](pages/openai.com/business/amex-chatgpt-business-credit/index.md)** — A refreshed co-branded landing page for American Express Business Platinum and Business Gold cardholders, offering up to $300/year in statement credits on US purchases of ChatGPT Business. This page replaces the old `/amex-chatgpt-business/` URL (removed), moving the content into the `/business/` URL hierarchy and adding specific "Business Credit" framing. Survey data cited: 87% of small business owners using AI save time, 81% reduce manual work, 73% improve productivity (Amex Trendex).

### Removed from Sitemap (1)

- **`https://openai.com/amex-chatgpt-business/`** — Retired and replaced by `https://openai.com/business/amex-chatgpt-business-credit/` (see above). Last known lastmod: 2026-05-12T16:14:03Z.

### Notable Page Updates

The homepage (`https://openai.com/`) received a minor CTA update: the hero section's quick-access button row now leads with a new **"Learn about ChatGPT Business"** link and dropped the **"Stories"** shortcut. The row now reads: Learn about ChatGPT Business | Talk with ChatGPT | Research | API Platform.

The related-article carousels on the cybersecurity pages `/index/gpt-5-5-with-trusted-access-for-cyber/` and `/index/accelerating-cyber-defense-ecosystem/` were refreshed to surface today's two new security/engineering posts (TanStack and Codex Windows Sandbox) in place of older articles.

All other 340 URL timestamp changes appear to be CMS cache-invalidation artifacts (zero substantive content changes found in the representative sample tested).

**Stats:** 1,301 total URLs | +3 added | 340 updated (lastmod) | −1 removed | 2 anomalies (benign timing) | 32 sub-sitemaps

---

## 2026-05-13T09-15Z

**Fetch time:** 2026-05-13T09:19:46Z UTC | **Baseline:** 2026-05-12T09-15Z

**TL;DR:** Today's dominant story is a large sitemap restructure: OpenAI quietly dropped two "internal-use" sub-sitemaps that housed 152 B2B customer-story and brand-story URLs, de-indexing 121 enterprise case-study pages (Stripe, Klarna, Morgan Stanley, Cisco, Canva, Uber, Zendesk, and many more) while migrating 31 others into purpose-named sub-sitemaps. The net result is a leaner sitemap — 1,178 URLs, down from 1,294 — and those customer stories are no longer surfaced to search engines via the sitemap. Separately, a burst of five new Codex-focused pages signals an accelerating push: NVIDIA and AutoScout24 published case studies featuring Codex with GPT‑5.5, OpenAI added a finance-teams Codex guide, and the results of the "Parameter Golf" ML competition were published.

### Anomalies

Two form pages have `lastmod` timestamps set to within 160 milliseconds of our fetch time — in other words, to the instant the sitemap was generated. This is a CMS artifact where the sitemap generator writes the current timestamp as `lastmod` on every build for these pages, rather than recording a genuine edit time. Both timestamps are functionally simultaneous with the fetch, not evidence of a real future modification.

- **future_lastmod** (CMS artifact): `https://openai.com/form/chatgpt-pro-community/` — lastmod `2026-05-13T09:19:46.160Z` vs. fetch at `2026-05-13T09:19:46Z` (160 ms gap)
- **future_lastmod** (CMS artifact): `https://openai.com/form/100-chats-book-request/` — lastmod `2026-05-13T09:19:46.096Z` vs. fetch at `2026-05-13T09:19:46Z` (96 ms gap)

### Sitemap Restructure: 121 Customer Stories De-indexed

OpenAI's sitemap index dropped from 34 to 32 sub-sitemaps. The two removed sub-sitemaps — named `internal-use-show-on-b2b-customer-stories-hub` and `internal-use-show-on-brand-stories-hub` — were internal-facing classification buckets that contained 152 total URLs. Of those:

- **31 URLs were migrated** to appropriate product-branded sub-sitemaps (`brand-stories-chatgpt`, `brand-stories-api`, `sora`, `startup`, `api`, `page`) — mostly GPT-5 / o1 brand stories and startup spotlights.
- **121 URLs were completely removed** from the sitemap. These are predominantly older B2B enterprise customer-story pages. The pages may still exist on the site, but search engines will no longer find them via the sitemap. Representative removals include:

  - Finance: `morgan-stanley`, `klarna`, `stripe`, `bny`, `singular-bank`, `balyasny-asset-management`
  - Enterprise SaaS: `salesforce`, `cisco`, `zendesk`, `datadog`, `intercom`, `retool`, `typeform`, `notion`
  - Consumer / retail: `canva`, `uber`, `doordash`, `booking-com`, `wayfair`, `estee-lauder`, `lowes`
  - Healthcare / life-sciences: `moderna`, `philips`, `lifespan`, `color-health`, `promega`, `genmab`
  - Education / government: `khan-academy`, `state-of-minnesota`, `government-of-iceland`, `duolingo`, `asu`
  - Japanese companies: `mixi`, `ly-corporation`, `cyberagent`, `dai-nippon-printing`, `eneos-materials`, `taisei`, `zenken`, `mercari`
  - Many others (see [runs/2026-05-13T09-15Z/diff.json](runs/2026-05-13T09-15Z/diff.json) for the full list)

Last snapshots of these pages remain in git history under `pages/openai.com/index/<slug>/index.md`.

### New Pages (Codex Push)

**[How Finance Teams Use Codex](pages/openai.com/academy/how-finance-teams-use-codex/index.md)** — A new OpenAI Academy guide covering 10 detailed Codex use cases tailored to finance teams: monthly business review narratives, variance analysis, planning, and reporting. Includes copy-ready prompts and suggestions for Codex skills/plugins across a finance tech stack. Published ~05:00 UTC May 13.

**[AutoScout24 Customer Story](pages/openai.com/index/autoscout24/index.md)** — Europe's largest online car marketplace (~30 M monthly users, 2,000 employees) adopted Codex for its ~1,000 engineering/data/product builders after a three-month evaluation. ChatGPT was deployed company-wide for AI literacy; Codex handles complex coding tasks in daily engineering workflows. Published ~06:45 UTC May 13.

**[NVIDIA Customer Story](pages/openai.com/index/nvidia/index.md)** — NVIDIA's coding-agents team and AI researchers use Codex with **GPT‑5.5** for production engineering and ML research loops. The page directly quotes NVIDIA engineers praising GPT-5.5's autonomy and tool selection. Key quote: "GPT-5.5 has been a massive unlock as a creative partner, especially when it comes to knowledge work." This is one of the clearest public endorsements of GPT-5.5 from a named enterprise. Published ~06:44 UTC May 13.

**[What Parameter Golf Taught Us](pages/openai.com/index/what-parameter-golf-taught-us/index.md)** — Post-competition analysis of OpenAI's "Parameter Golf" ML challenge (1,000+ participants, 2,000+ submissions). Covers record-track highlights (novel training optimizations), non-record creative approaches (non-autoregressive text modeling, dynamic tokenization), and lessons learned from running the challenge with coding agents. Published ~08:29 UTC May 13.

**[Codex Enterprise Promo Form](pages/openai.com/form/codex-enterprise-promo/index.md)** — A new lead-generation form for enterprise Codex interest. Published ~08:48 UTC May 13.

### Notable Page Updates (130 total)

The 130 updated pages span routine CMS refresh timestamps and genuine edits. Highlights:

- **`/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/`** — Content grew from 38,341 to 38,635 chars; the enterprise AI report was expanded.
- **`/business/guides-and-resources/staying-ahead-in-the-age-of-ai/`** — Grew from 24,175 to 24,469 chars.
- **`/business/guides-and-resources/a-practical-guide-to-building-ai-agents/`** — Shrank from 39,340 to 39,156 chars (some content removed from the agents guide).
- **`/amex-chatgpt-business/`** — Grew from 7,942 to 8,357 chars (the American Express co-branded ChatGPT page expanded).
- **`/academy/codex-for-work/`** and **`/academy/codex-how-to-start/`** — Both expanded, consistent with the Codex content push.
- **`/news/company-announcements/`**, **`/news/engineering/`**, **`/news/product-releases/`**, **`/news/safety-alignment/`**, **`/news/global-affairs/`**, **`/news/security/`** — All hub index pages refreshed.
- Many `/global-affairs/` articles and `/index/` pages had bulk lastmod refreshes with unchanged content (CMS publish-wave artifact).

### Removed from Sitemap (121 URLs)

All 121 removed URLs are B2B enterprise and consumer customer-story pages at `openai.com/index/<company-name>/`. These were classified under the now-dropped `internal-use-show-on-b2b-customer-stories-hub` sub-sitemap. The pages are still in the git snapshot archive. A selection:

`ada`, `altera`, `arco-education`, `asu`, `axios-allison-murphy`, `balyasny-asset-management`, `basis`, `bbva`, `bbva-2025`, `be-my-eyes`, `blue-j`, `bny`, `booking-com`, `canva`, `canva-cam-adams`, `chime-vineet-mehra`, `choco`, `cisco`, `clay`, `cna-walter-fernandez`, `coderabbit`, `color-health`, `commonwealth-bank-of-australia`, `consensus`, `cyberagent`, `dai-nippon-printing`, `datadog`, `decagon`, `digital-green`, `doordash-mariana-garavaglia`, `doppel`, `duolingo`, `eliseai-minna-song`, `endex`, `eneos-materials`, `estee-lauder`, `expedia-jochen-koedijk`, `factory`, `fanatics-betting-gaming-andrea-ellis`, `figma-david-kossnick`, `genmab`, `genspark`, `government-of-iceland`, `grab`, `harvey`, `healthify`, `hebbia`, `hibob`, `holiday-extras`, `hygh`, `indeed`, `indeed-maggie-hulce`, `intercom`, `invideo-ai`, `ironclad`, `jetbrains`, `jetbrains-2025`, `khan-academy`, `klarna`, `launchdarkly-claire-vo`, `lifespan`, `lowes`, `lowes-chandhu-nair`, `ly-corporation`, `match-group`, `mavenagi`, `mercado-libre`, `mercari`, `mirakl`, `mixi`, `moderna`, `morgan-stanley`, `netomi`, `neurogum`, `notion`, `nubank`, `oscar`, `outtake`, `paf`, `paradigm`, `philips`, `plex-coffee`, `podium`, `promega`, `retell-ai`, `retool`, `rogo`, `rox`, `safetykit`, `salesforce`, `san-antonio-spurs`, `scania`, `schoolai`, `scout24`, `singular-bank`, `stadler`, `state-of-minnesota`, `steuerrecht`, `stripe`, `summer-health`, `superhuman`, `taisei`, `trustbank`, `typeform`, `uber`, `uber-enables-outstanding-experiences`, `unify`, `upwork`, `vfl-wolfsburg`, `viable`, `wayfair`, `waymark`, `whoop`, `wix`, `wrtn`, `yabble`, `zalando`, `zelma`, `zendesk`, `zenken`, `10bedicu`

**Stats:** 1,178 total URLs | +5 added | 130 updated | −121 removed | 2 anomalies (CMS artifacts) | 32 sub-sitemaps (was 34)

---

## 2026-05-12T09-15Z

**Two major platform launches dominated today's update: OpenAI officially entered the enterprise cybersecurity market with "Daybreak" — a branded AI-powered vulnerability scanning and cyber defense product — and launched the OpenAI Deployment Company, a new $4 billion majority-owned subsidiary that embeds specialized engineers directly inside enterprises to deploy AI into production workflows.** Together, these represent OpenAI's most significant structural expansion beyond selling model access: it is now offering a named security product and a professional-services company. A batch of 174 page updates accompanied the launches, mostly bulk CMS refreshes across customer stories and global-affairs content, but one notable change was the removal of the K–12 Teachers plan link from the ChatGPT pricing page.

### Anomalies

None detected.

### New Pages

**[OpenAI Daybreak](pages/openai.com/daybreak/index.md)** — A new cybersecurity product combining GPT-5.5, the Codex agentic harness, and security industry partners. It positions OpenAI as an active participant in enterprise cyber defense: finding and patching code vulnerabilities, threat modeling, and remediation at scale. Three model access tiers are offered: standard GPT-5.5, "Trusted Access for Cyber" (for verified defensive security work), and "GPT-5.5-Cyber" (preview access for red teaming and penetration testing). Trust partners listed include Cloudflare, Cisco, CrowdStrike, Palo Alto Networks, Oracle, Zscaler, Akamai, and Fortinet. A [lead-gen form](pages/openai.com/daybreak/request-a-vulnerability-scan/index.md) lets organizations request a vulnerability scan.

**[OpenAI Launches the Deployment Company](pages/openai.com/index/openai-launches-the-deployment-company/index.md)** (dated May 11, 2026) — OpenAI is launching a new majority-owned subsidiary ("DeployCo") to embed Forward Deployed Engineers (FDEs) inside enterprises. It simultaneously announced the acquisition of Tomoro, an applied AI consulting firm (~150 engineers), whose clients include Tesco, Virgin Atlantic, and Supercell. Initial investment exceeds $4 billion, led by TPG with co-leads Advent, Bain Capital, and Brookfield. Consulting partners Bain & Company, Capgemini, and McKinsey & Company are included. The [companion business page](pages/openai.com/business/the-openai-deployment-company/index.md) describes the FDE model: embedding engineers to redesign critical workflows from diagnostic through production deployment.

**[Signals Q1 2026 Research Update](pages/openai.com/signals/research/2026q1-update/index.md)** — OpenAI's economic research arm published Q1 2026 ChatGPT consumer adoption data. Users with typically feminine names now account for over half of gender-inferable users. Over-35 users gained share. Fastest-growing countries by per-capita usage include Dominican Republic, Haiti, Japan, Mexico, and Tanzania — showing broadening beyond Western markets. This page was published within minutes of the monitoring run.

### Notable Updates

**`/chatgpt/pricing/`** — The K–12 Teachers plan link (`/plans/k12-teachers/`) was **removed** from the pricing page navigation. This is a product-tier change affecting educational access visibility on the main pricing page.

**`/business/frontier/`** — Updated to explicitly reference the new OpenAI Deployment Company, replacing "OpenAI Forward Deployed Engineers" with a link to the DeployCo page and adding text explaining the subsidiary's purpose.

**`/about/`** — News carousel rotated; "Advancing voice intelligence with new models in the API" is now the lead story.

**Cyber content sweep (08:33–08:35Z)**: Three cybersecurity pages (`/index/cybersecurity-in-the-intelligence-age/`, `/index/accelerating-cyber-defense-ecosystem/`, `/index/gpt-5-5-with-trusted-access-for-cyber/`) were refreshed in a tight window just before the Daybreak product pages were published — part of a coordinated launch sequence.

### Removals

None.

### Stats

| Metric | Value |
|--------|-------|
| Total URLs | 1,294 |
| Added | 5 |
| Updated | 174 |
| Removed | 0 |
| Anomalies | 0 |
| Sub-sitemaps | 34 |

Full analysis: [runs/2026-05-12T09-15Z/analysis.md](runs/2026-05-12T09-15Z/analysis.md)

---

## 2026-05-11T09-15Z

**Fetch time:** 2026-05-11T09:17:28Z UTC | **Baseline:** 2026-05-10T09-16Z

**TL;DR:** This run catches up on activity from May 7–11. The most important developments: OpenAI launched **Trusted Contact** — a ChatGPT safety feature letting adults designate a trusted person to be notified in crisis situations — and **GPT‑5.5‑Cyber**, a specialized model for defenders of critical infrastructure. The **cookie policy** was updated to add `ads.openai.com` cookies, reflecting the ChatGPT ads rollout. The **OpenAI–Microsoft partnership was restructured**: Microsoft's API license is now non-exclusive, OpenAI can now serve all products on any cloud provider (not just Azure first), and Microsoft no longer pays OpenAI a revenue share. Two new pages appeared today (May 11): an enterprise scaling guide drawing on interviews with European executives, and an OpenAI Campus Network student club interest form. The bulk of the 122 lastmod updates are CMS metadata flushes across ~60 customer story pages with no content changes.

### Anomalies

None detected.

### New Pages

| Page | Date | Summary |
|---|---|---|
| [How enterprises are scaling AI](pages/openai.com/business/guides-and-resources/how-enterprises-are-scaling-ai/index.md) | May 11 | Insights from European enterprise executives (Philips, BBVA, Mirakl, Scout24, JetBrains, Scania) on scaling AI. Five patterns: culture before tooling, governance as enabler, ownership over consumption, quality before scale, protecting judgment work. Downloadable PDF guide. |
| [OpenAI Campus Network: Student club interest form](pages/openai.com/index/openai-campus-network-student-club-interest-form/index.md) | May 11 | OpenAI is partnering with student clubs at universities worldwide. Offers early access to tools, events support, and a global network of student leaders. |

### Notable Updates

- **Cookie policy revised** ([`/policies/cookie-policy/`](pages/openai.com/policies/cookie-policy/index.md)) — Updated May 6, 2026 (lastmod advanced from 2026-02-25 to 2026-05-08). Cookie table now lists `ads.openai.com` and `deploymentsafety.openai.com` as domains, reflecting the ads platform and deployment-safety features. Four other privacy/communications policy pages updated simultaneously on May 7.

- **Microsoft partnership restructured** ([`/index/next-phase-of-microsoft-partnership/`](pages/openai.com/index/next-phase-of-microsoft-partnership/index.md)) — Lastmod refreshed to May 10. Key terms: Microsoft remains primary cloud partner with Azure-first commitment, but **OpenAI can now serve all products on any cloud**; Microsoft's license is now **non-exclusive**; Microsoft no longer pays revenue share to OpenAI; OpenAI's payments to Microsoft continue through 2030 with a total cap; Microsoft stays a major shareholder.

- **Fine-tuning shutdown notices confirmed** — Three fine-tuning pages ([`gpt-4o-fine-tuning`](pages/openai.com/index/gpt-4o-fine-tuning/index.md), [`introducing-vision-to-the-fine-tuning-api`](pages/openai.com/index/introducing-vision-to-the-fine-tuning-api/index.md), [`introducing-improvements-to-the-fine-tuning-api`](pages/openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/index.md)) continue to carry the May 8 notice: *"OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users."* Lastmod refreshed again today — no reversal.

- **OpenAI Academy URL restructuring** — [`/academy/building-with-ai/`](pages/openai.com/academy/building-with-ai/index.md) and [`/academy/chatgpt-for-education/`](pages/openai.com/academy/chatgpt-for-education/index.md) updated: learning track links now point to `academy.openai.com/home/collections/...` instead of `/home/clubs/...` — internal URL migration, same content.

- **Batch CMS refresh** — ~60 `/index/` customer story pages (Uber, Cisco, BBVA, Grab, Harvey, Klarna, etc.) all bumped to lastmod 2026-05-11 with no content changes. Routine metadata flush.

**Stats:** 1289 total URLs | +2 added | 122 updated | -0 removed | 0 anomalies | 34 sub-sitemaps

---



## 2026-05-10T09-16Z

**Fetch time:** 2026-05-10T09:17:38Z UTC | **Baseline:** 2026-05-09T09-15Z

**TL;DR:** The headline story is OpenAI **shutting down its self-serve fine-tuning platform** (announced May 8 via retroactive notices added to three existing fine-tuning pages) — a significant change for developers who relied on training custom models through OpenAI's API since 2023. On the other side of the ledger, OpenAI is doubling down on specialized AI for cybersecurity: GPT-5.5-Cyber launched in limited preview for critical-infrastructure defenders this week, and new posts explain both the technical governance controls for Codex agents and a broader strategy for democratizing AI-powered defense. One new customer story (Simplex, Japan) documents 70% faster screen development using Codex. The rest of the 198 lastmod changes are batch CMS metadata refreshes across Academy, Global Affairs, and customer story pages with no detectable content changes.

### Anomalies

None detected.

**Infrastructure note:** `/sitemap.xml/page/` returned HTTP 503 persistently (4 retry attempts); served from 2026-05-09 cached snapshot. URLs listed only in that sub-sitemap are not diffed this run.

### Notable updates

- **Fine-tuning platform shutdown** (MAJOR) — Three fine-tuning announcement pages ([introducing improvements to the fine-tuning API](pages/openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/index.md), [introducing vision to the fine-tuning API](pages/openai.com/index/introducing-vision-to-the-fine-tuning-api/index.md), [GPT-4o fine-tuning](pages/openai.com/index/gpt-4o-fine-tuning/index.md)) each received an identical retroactive notice:
  > *"OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users but existing users of the fine-tuning platform will be able to create training jobs for the coming months. All fine-tuned models will remain available for inference until their base models are deprecated."*
  The self-serve fine-tuning API has been available since August 2023. Deprecation timeline is on the OpenAI developer docs site.

- **GPT-5.5-Cyber and Trusted Access for Cyber** — [`/index/gpt-5-5-with-trusted-access-for-cyber/`](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) (published May 7, lastmod refreshed today): A specialized cybersecurity model in limited preview for defenders protecting critical infrastructure. Three-tier access system: default GPT-5.5, GPT-5.5 with TAC (Trusted Access for Cyber) for verified defensive workflows, and GPT-5.5-Cyber for the most specialized authorized work (authorized red-teaming, pen-testing). Advanced Account Security (phishing-resistant MFA) required for individual TAC members from June 1, 2026.

- **Running Codex safely at OpenAI** — [`/index/running-codex-safely/`](pages/openai.com/index/running-codex-safely/index.md) (published May 8, metadata refreshed today): OpenAI's internal playbook for governing Codex agents: sandboxed execution environments, human approval gates for high-risk actions, network access policies, managed credential systems, and agent-native audit trails.

- **OpenAI on AWS related-posts refresh** — [`/index/openai-on-aws/`](pages/openai.com/index/openai-on-aws/index.md): Sidebar "keep reading" links rotated to newer content ("Advancing voice intelligence" and "Testing ads in ChatGPT," replacing "GPT-5.5 Instant" and "New ways to buy ChatGPT ads").

- **Batch CMS refreshes** — ~20 Global Affairs pages (all ~18:41 UTC May 8), ~21 Academy pages (May 7–8), ~50 customer story `/index/` pages (all ~07:xx UTC today), 9 form pages (May 8), and 5 policy pages (May 7–8) received lastmod bumps. No content changes detected on any of them.

### New pages (1)

| Page | Date | Summary |
|---|---|---|
| [Simplex](pages/openai.com/index/simplex/index.md) | May 8 | Japanese technology company Simplex adopts ChatGPT Enterprise + Codex as its primary coding agent; reports 70% fewer hours per screen developed, 40% fewer per screen designed, 17% fewer for integration testing; focuses on redesigning the full development process around AI rather than using AI as an assistive overlay |

### Removals

0 pages removed.

**Stats:** 1,287 total URLs | +1 added | 198 lastmod updates | 0 removed | 0 anomalies | 34 sub-sitemaps (1 served from cache)

---

## 2026-05-09T09-15Z

**Fetch time:** 2026-05-09T09:16:02Z UTC | **Baseline:** 2026-05-07T09-15Z

**TL;DR:** A busy two days on openai.com. OpenAI published seven new articles across safety,
security, and developer topics — including new real-time voice API models, a limited preview of
GPT-5.5-Cyber for critical-infrastructure defenders, a "Trusted Contact" crisis-notification
feature for ChatGPT users, and a bilingual English/French privacy explainer aimed at Canadian
audiences. Multiple waves of coordinated updates touched privacy policies, Codex content, and
the OpenAI Academy. One notable structural event: the sub-sitemap that listed ~122 B2B customer
stories began returning HTTP 403 — those pages are still live but are no longer indexed through
that endpoint. One metadata anomaly: the `enterprise-privacy/` page's claimed lastmod jumped 15
months backward with no content change.

### Anomalies

1. **Backwards lastmod — `enterprise-privacy/`**
   The sitemap's `<lastmod>` for `https://openai.com/enterprise-privacy/` regressed from
   `2026-05-04` to `2025-01-31` (roughly 15 months backward). The page content is
   byte-for-byte identical to the prior snapshot and the in-page "Updated: January 8, 2026"
   date is unchanged. This is a CMS/metadata glitch, not a content rollback.

2. **B2B customer-stories sub-sitemap now returns HTTP 403**
   The sub-sitemap `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/`
   (which listed 122 `/index/` customer-story pages) returned HTTP 403 this run. Spot-checks
   confirm the underlying pages (e.g., `/index/canva/`, `/index/cisco/`) remain live and
   fully accessible. OpenAI appears to have restricted the sitemap endpoint itself — possibly
   intentionally, given the "internal-use-" prefix in the sub-sitemap name. All 122 URLs are
   preserved in `state/known_urls.json`.

### New pages (7)

| Page | Date | Summary |
|---|---|---|
| [Advancing voice intelligence with new models in the API](pages/openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/index.md) | May 7 | Three new realtime audio API models: GPT-Realtime-2 (GPT-5-class reasoning in voice), GPT-Realtime-Translate (live 70→13 language translation), GPT-Realtime-Whisper (live streaming transcription) |
| [GPT-5.5 with Trusted Access for Cyber](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) | May 7 | GPT-5.5-Cyber rolled out in limited preview to critical-infrastructure defenders; explains three-tier Trusted Access for Cyber framework; Advanced Account Security (phishing-resistant) required for top-tier access from June 1, 2026 |
| [Running Codex safely at OpenAI](pages/openai.com/index/running-codex-safely/index.md) | May 8 | Technical guide to OpenAI's internal Codex governance: sandboxing, human-approval gates for high-risk actions, network policies, and agent-native audit trails |
| [How ChatGPT learns about the world while protecting privacy](pages/openai.com/index/how-chatgpt-protects-privacy/index.md) | May 6 | Bilingual (English + French) plain-language privacy explainer covering training data practices, personal information handling, and user privacy controls — likely produced for Canadian regulatory context |
| [Introducing Trusted Contact in ChatGPT](pages/openai.com/index/introducing-trusted-contact-in-chatgpt/index.md) | May 7 | New optional safety feature: adults 18+ can nominate a trusted person to receive automated notifications if OpenAI's systems detect serious self-harm risk; extends existing parental-alert system to all users |
| [Advancing youth safety and wellbeing in EMEA](pages/openai.com/index/advancing-youth-safety-in-emea/index.md) | May 5 | European Youth Safety Blueprint (5 pillars for age-appropriate AI policy) and announcement of first EMEA Youth & Wellbeing Grant recipients |
| [Parloa](pages/openai.com/index/parloa/index.md) | May 7 | Customer story: European startup Parloa builds enterprise voice-driven customer service agents using the OpenAI API |

### Notable updates

- **B2B Signals messaging rebrand** — [`signals/b2b/`](pages/openai.com/signals/b2b/index.md):
  "AI advantage" replaced throughout with "frontier advantage"; intro rewritten to be more
  concise. Deliberate positioning shift to align with OpenAI's "frontier model" branding.

- **Privacy policy wave** (all updated May 7–8): `services-privacy-policy`, `communications-privacy-policy`,
  `services-communications-privacy-policy`, `us-privacy-policy`, `cookie-policy`, and `usage-policies`
  — six policy documents updated in a coordinated 24-hour window, coinciding with the new privacy explainer.

- **API page** — new "Enterprise-ready solutions for real impact" section added with a three-tab
  interface linking to use cases, industries, and blueprints.

- **Codex ecosystem refresh** — ~15 Codex-related pages (codex/, codex/get-started/, gpt-5-2-codex through gpt-5-5-instant, introducing-upgrades-to-codex, codex-now-generally-available, etc.) all refreshed May 7–8, coordinated with Codex GA.

- **Academy learning content** — ~21 OpenAI Academy course pages refreshed May 7–8 (codex, building-with-ai, chatgpt-for-education, customer-success, data-analysis, marketing, etc.).

- **FedRAMP Moderate** — [`index/openai-available-at-fedramp-moderate/`](pages/openai.com/index/openai-available-at-fedramp-moderate/index.md):
  Updated (May 9) to note that GPT-5.5 is now available in the FedRAMP environment, and that
  Codex Cloud will soon be accessible via FedRAMP ChatGPT Enterprise workspace.

- **Customer stories hub rotation** — [`business/customer-stories/`](pages/openai.com/business/customer-stories/index.md):
  Added Parloa and Simplex to the featured list; VfL Wolfsburg and Axios Allison Murphy rotated out.

### Removals

0 pages confirmed removed. See anomaly #2 above for the 122 URLs now inaccessible via the
b2b-customer-stories sub-sitemap.

**Stats:** 1,164 current URLs | +7 added | 153 lastmod updates | 122 missing via 403 sub-sitemap (0 confirmed removed) | 2 anomalies | 33/34 sub-sitemaps fetched

---

## 2026-05-07T09-15Z

**Fetch time:** 2026-05-07T09:17:05Z UTC | **Baseline:** 2026-05-07T09-01Z

**TL;DR:** OpenAI's CMS ran a batch regeneration cycle between the bootstrap run and
this one (~14 minutes apart), causing 34 pages to show fresh `<lastmod>` timestamps.
Of those 34, only **one page had a real content change**: the `/index/podium/` customer
story rotated a single "Keep reading" recommended-article link (swapped "Singular Bank"
for "How frontier enterprises are building an AI advantage"). The other 33 were
timestamp-only updates with identical content. No URLs were added or removed. No
anomalies detected.

### The one real content change

- [https://openai.com/index/podium/](pages/openai.com/index/podium/index.md) —
  "Keep reading" carousel updated: swapped out the
  [Singular Bank story](pages/openai.com/index/singular-bank/index.md) in favour of
  [How frontier enterprises are building an AI advantage](pages/openai.com/index/introducing-b2b-signals/index.md)
  (both dated May 6, 2026). Main article body (GPT-5.1 powering AI agents for 10,000+ SMBs) unchanged.

### Notable timestamp-only updates (no content change)

34 pages had `<lastmod>` bumped from ~08:xx UTC to ~09:xx UTC — a CMS batch
re-index signature. The most notable was `/index/our-principles/` (Sam Altman),
whose timestamp crossed a day boundary (May 6 → May 7) but content was identical.
See [runs/2026-05-07T09-15Z/analysis.md](runs/2026-05-07T09-15Z/analysis.md) for the
full list.

**Stats:** 1279 total URLs | +0 added | 34 lastmod changes (1 content change) | -0 removed | 0 anomalies | 34 sub-sitemaps

---

- **Sitemap monitored:** `https://openai.com/sitemap.xml` (sitemap-index → ~34 sub-sitemaps)
- **Routine schedule:** daily
- **What's tracked:** added / removed / updated URLs (per `<lastmod>`),
  plus anomalies like backwards-moving timestamps, future-dated mods,
  reappearing URLs, and similar oddities.
- **Bot defense:** openai.com is fronted by Cloudflare with TLS-fingerprint
  blocking. The conversion tool uses `curl-cffi` with Chrome impersonation
  to bypass the 403 that plain Python clients receive. robots.txt explicitly
  allows scraping (`User-agent: * / Allow: /`).

## Repo layout

| Path | Contents |
| ---- | -------- |
| `README.md` | This file. Newest run entries are PREPENDED below. |
| `sitemaps/openai.com/<run_id>.xml` | Dated root sitemap-index snapshots. |
| `sitemaps/openai.com/latest.xml` | Most recent index — overwritten each run. |
| `sitemaps/openai.com/sub/<run_id>/*.xml` | Dated sub-sitemap snapshots. |
| `sitemaps/openai.com/sub/latest/*.xml` | Most recent sub-sitemaps — overwritten each run. |
| `pages/openai.com/<path>.md` | Current markdown of each page. Git history is the archive. |
| `runs/<run_id>/analysis.md` | Long-form analysis written for that run. |
| `runs/<run_id>/diff.json` | Machine-readable diff vs prior baseline. |
| `state/known_urls.json` | Cumulative URL state: first_seen, last_seen, lastmod history. |
| `tools/html_to_md.py` | Canonical HTML→markdown converter (uses curl-cffi). |
| `tools/url_path.py` | Canonical URL→repo-path mapping. |
| `tools/requirements.txt` | pip dependencies. |

`<run_id>` format is `YYYY-MM-DDTHH-MMZ` (UTC).

## Timestamp discipline

Three distinct timestamps are tracked, never conflated:

- **`<lastmod>`** — what OpenAI *claims* about a page in their sitemap.
- **fetch time** — UTC time *we* actually retrieved the sitemap or page.
- **first_seen** — the earliest `run_id` when a URL appeared here.

Anomalies generally live in the gap between these.

---

## 2026-05-07T09-01Z — Bootstrap

**TL;DR:** Initial baseline captured. Fetched the openai.com sitemap-index,
walked all 34 sub-sitemaps, downloaded 1277
of 1279 pages through curl-cffi (Chrome TLS impersonation; plain Python
hits a Cloudflare 403), converted to markdown, and committed the snapshot.
No diff is possible yet; the next daily run will produce the first real
changelog entry.

- **Fetch time:** 2026-05-07T09:01:08.630082Z
- **Sub-sitemaps:** 34
- **URLs in sitemap:** 1279
- **Pages stored:** 1277
- **Fetch failures:** 2
- **Anomalies (bootstrap-detectable):** see below.

### Bootstrap-detectable anomalies

Even on the bootstrap run, with no prior baseline, two URLs from the sitemap
returned **HTTP 404** when fetched. These are listed in the sitemap-index but
are not actually live pages — a sitemap/site mismatch. The first one is
particularly interesting:

- **`https://openai.com/index/inworld-ai-DO-NOT-PUBLISH/`** — appears in the
  public sitemap but 404s. The literal string `DO-NOT-PUBLISH` in the path
  strongly suggests this is an internal staging slug that leaked from
  OpenAI's CMS into the production sitemap. Worth watching: if the URL ever
  starts returning 200, that's the moment OpenAI accidentally published an
  Inworld-AI–related page (which the routine will then fetch and snapshot).
- **`https://openai.com/brand-old/`** — also in the sitemap, also 404. Likely
  a deprecated brand-guidelines page that was removed from the site but not
  the sitemap.

Both will be re-checked every daily run. State changes (404 → 200, or
disappearance from the sitemap entirely) will be flagged.

See [`runs/2026-05-07T09-01Z/analysis.md`](runs/2026-05-07T09-01Z/analysis.md) for the full bootstrap report.

