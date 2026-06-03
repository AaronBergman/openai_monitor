# Analysis — 2026-06-03T09-15Z

**Fetch time:** 2026-06-03T09:22:47Z
**Baseline:** 2026-06-01T09-15Z
**Total current URLs:** 1320

## Summary
- Added: 9 URLs
- Updated: 296 URLs (sitemap lastmod changed)
- Removed: 0 URLs
- Anomalies: 0
- Content changes (actual markdown diff): 51 pages
- Fetch failures: 0

---

## Anomalies

None detected. All `<lastmod>` timestamps are plausible and none moved backwards.

---

## Significant Content Changes

### 1. Service Terms — major update (Updated June 2, 2026)
**URL:** `https://openai.com/policies/service-terms/`
**Path:** `pages/openai.com/policies/service-terms/index.md`

**Date change:** Updated January 9, 2026 → Updated **June 2, 2026**

**Substantive change:** A new **Section 10 "Licensed Materials"** was added. This section governs scenarios where customers download and install OpenAI software, packages, code, containers, or other modules onto their own systems ("Customer Systems"). The license is described as limited, non-exclusive, non-transferable, non-sublicensable, and terminates at end of term. Customers may not modify, redistribute, or sublicense Licensed Materials. Open source components may grant additional rights.

**Significance:** This is the first appearance of on-premises/self-hosted deployment language in OpenAI's Service Terms. It strongly suggests OpenAI is formalizing (or beginning to offer) deployments where enterprise customers run models or software locally. This fits with recent enterprise demand for data locality controls, especially for regulated industries (healthcare, finance, government).

**Also:** Formatting was standardized throughout — bold section headers gained trailing periods, internal markdown links gained italics and full absolute URLs, a new `#### For Builders of GPTs:` subheading was added.

### 2. Sub-processor List — updated (Updated June 2, 2026)
**URL:** `https://openai.com/policies/sub-processor-list/`
**Path:** `pages/openai.com/policies/sub-processor-list/index.md`

**Date change:** Last updated February 11, 2026 → Last updated **June 2, 2026**

**Substantive changes:**
- **Cloudflare added "Web Hosting" purpose:** Cloudflare's entry now includes "Web Hosting" — defined as "Hosting of ChatGPT Sites created web pages. Applicable subprocessors may run security and safety classifiers on web pages and share results with OpenAI." This directly corresponds to the new ChatGPT Sites feature and its new Terms of Service page.
- **Moderation provider location change:** A moderation/content-safety provider's geographic scope changed from "Canada / Philippines" to "United States / Canada / Philippines" — suggesting expanded US-based content moderation.
- **Notification form link changed:** The "subscribe to new sub-processors" link changed from an OpenAI-hosted form to a HubSpot form (`share.hsforms.com`).

### 3. Intelligence at Work page — event concluded
**URL:** `https://openai.com/business/intelligence-at-work/`
**Path:** `pages/openai.com/business/intelligence-at-work/index.md`

**Change:** Page shifted from pre-event registration to post-event mode. Prior: "Register to watch live on June 2 / June 2, 2026 11:30 a.m. ET" with a register button. Now: "Thanks for watching / If you would like to learn more about bringing transformative AI into your organization, contact us." The June 2 Intelligence at Work livestream — featuring Sam Altman (CEO) and Denise Dresser (CRO) — has concluded.

### 4. Homepage + News/Listings — Codex content now leads
**URLs:** `https://openai.com/`, `https://openai.com/news/company-announcements/`, `https://openai.com/about/`

**Change:** The featured hero article on the homepage and company-announcements listing changed from "Introducing GPT-5.5" (Apr 23) to "Codex for every role, tool, and workflow" (Jun 2). The About page now features "GPT-5.5 Instant System Card" instead of the "GPT-5.5 Instant: smarter, clearer, and more personalized" product piece. Reflects editorial rotation to surface Codex's expansion as the current flagship story.

Research/news listing reordering: "GPT-5.5 Instant" (Product) and "GPT-5.5 Instant System Card" (Safety) swapped positions — same pattern previously noted in the June 1 run for GPT-5.5 entries.

### 5. Customer Stories — Travelers added, AutoScout24 rotated out
**URL:** `https://openai.com/business/customer-stories/`

**Change:** Travelers (AI Claims Assistant) now appears as the top story, pushing AutoScout24 down/out of the featured rotation. The Travelers story itself is a new page (see New Pages section).

### 6. ~25 customer story pages — bulk image URL refresh
**Affected pages:** ~25 existing customer story pages under `/index/` (braintrust, virgin-atlantic, uber, trustbank, steuerrecht, singular-bank, scout24, scania, safetykit, ramp, rakuten, philips, mufg, jetbrains-2025, endava, cisco, choco, chime-vineet-mehra, bny, bbva-2025, adventhealth, expedia-jochen-koedijk, commonwealth-bank-of-australia, and others)

**Change:** Image asset URLs changed (Contentful CDN hash rotation) with identical 12-line diff patterns. No substantive content changed — only the image asset identifiers. This is the same mass-CMS-update pattern observed in prior runs.

---

## New Pages (9 total)

### 1. Codex for every role, tool, and workflow
**URL:** `https://openai.com/index/codex-for-every-role-tool-workflow/`
**Path:** `pages/openai.com/index/codex-for-every-role-tool-workflow/index.md`
**lastmod:** 2026-06-02T12:48:22Z

Major Codex product update. Key announcements:
- **5 million+ weekly active users** (up 6x since February desktop launch)
- **Non-developers are ~20% of users** and growing 3x faster than developers
- **6 new role-specific plugins** (for analysts, marketers, finance, legal, etc.) — no coding required
- **Annotations** — refine AI output in-place
- **ChatGPT Sites preview** — create and share interactive websites/apps via URL within your workspace
- Enterprise examples: Zapier teams use it for incident postmortems; NVIDIA for ML research workflows

### 2. Codex is becoming a productivity tool for everyone (Knowledge Work Report)
**URL:** `https://openai.com/index/codex-for-knowledge-work/`
**Path:** `pages/openai.com/index/codex-for-knowledge-work/index.md`
**lastmod:** 2026-06-02T12:48:22Z

Announces "The Next Era of Knowledge Work" report (PDF). Key stats:
- 5M+ weekly users, 6x growth since February
- Top knowledge-worker tasks: reports, spreadsheets, presentations, contracts, data analysis
- Fastest-growing: data analysis, research, knowledge artifact creation
- Users increasingly running multiple Codex tasks in parallel

### 3. OpenAI frontier models and Codex are now available on AWS
**URL:** `https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/`
**Path:** `pages/openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/index.md`
**lastmod:** 2026-06-02T07:36:35Z

General availability of OpenAI frontier models and Codex on AWS. Targets enterprise customers running within existing AWS security, compliance, procurement, and governance workflows. Available in both Commercial and GovCloud regions.

### 4. Building the infrastructure for the Intelligence Age in Michigan (Stargate)
**URL:** `https://openai.com/index/stargate-michigan-data-center/`
**Path:** `pages/openai.com/index/stargate-michigan-data-center/index.md`
**lastmod:** 2026-06-02T18:42:34Z

Groundbreaking for **"The Barn"** — a 1GW data center campus in Saline, Michigan. Partners: Oracle, Related Digital, Walbridge, Governor Gretchen Whitmer. Commitments: infrastructure costs not passed to ratepayers, closed-loop cooling, **2,500+ union construction jobs** + 450 permanent jobs, **$10M contribution** to Saline Recreation Center, **$1B projected tax revenue** over lease term.

### 5. Travelers deploys AI-powered claims countrywide with OpenAI
**URL:** `https://openai.com/index/travelers/`
**Path:** `pages/openai.com/index/travelers/index.md`
**lastmod:** 2026-06-02T07:36:35Z

Customer story. Travelers Insurance built a fully autonomous AI Claim Assistant using **OpenAI Realtime API** for voice-based auto claims filing. **85–90% of customers** using the assistant complete their claim through AI. Launched in 8 states, expanded countrywide within 2 months. Handles 100K+ claims in surge events; 1.5M+ claims/year overall.

### 6. Advancing youth safety and opportunity through global leadership
**URL:** `https://openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership/`
**Path:** `pages/openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership/index.md`
**lastmod:** 2026-06-02T20:27:26Z

Policy piece ahead of G7 Leaders' Summit in Évian, France. OpenAI calls for an **international youth AI safety institute** — a sustained body to share research, evidence, and guidance across governments, industry, and civil society. References Estonia's national ChatGPT school rollout and Common Sense Media's Youth AI Safety Institute (supported by OpenAI Foundation).

### 7. Our views on AI policy and political advocacy
**URL:** `https://openai.com/index/our-views-on-ai-policy-and-political-advocacy/`
**Path:** `pages/openai.com/index/our-views-on-ai-policy-and-political-advocacy/index.md`
**lastmod:** 2026-06-02T22:57:14Z

Transparency statement on OpenAI's political engagement:
- No super PAC donations, no employee-funded PAC, no candidate/campaign donations
- Greg Brockman's support for Leading the Future (LTF) is "in a personal capacity, not on behalf of the company"
- OpenAI "does not direct the activities of LTF, or have visibility into their operations"
- Calls on all AI policy advocates to "not use tactics like astroturfing"

### 8. ChatGPT Sites Terms (new policy document)
**URL:** `https://openai.com/policies/chatgpt-sites-terms/`
**Path:** `pages/openai.com/policies/chatgpt-sites-terms/index.md`
**lastmod:** 2026-06-02T22:39:25Z

New legal terms for the ChatGPT Sites feature (website/app creation). Key terms: you retain ownership of Website Content; you grant OpenAI a royalty-free worldwide license to host/reproduce/display it; you're solely responsible for your sites and end users; indemnity covers third-party claims.

### 9. EU Services Privacy Policy
**URL:** `https://openai.com/policies/eu-services-privacy-policy/`
**Path:** `pages/openai.com/policies/eu-services-privacy-policy/index.md`
**lastmod:** 2026-06-02T07:36:35Z

EU/EEA/UK/Switzerland-specific privacy policy. Notably mentions "For Free and Go users, to personalize the ads you see on our Services" — confirming an ad-supported tier for EU users.

---

## Removed Pages

None.

---

## Fetch Failures

None.

---

## Updated URL Timestamps (notable)

- `https://openai.com/` → 2026-06-02T16:01:49Z
- `https://openai.com/about/` → 2026-06-03T04:01:49Z
- `https://openai.com/business/intelligence-at-work/` → 2026-06-03T09:16:24Z
- `https://openai.com/policies/service-terms/` → 2026-06-02T20:47:18Z
- `https://openai.com/policies/sub-processor-list/` → 2026-06-03T07:35:59Z
- `https://openai.com/codex/` → 2026-06-02T07:37:23Z
