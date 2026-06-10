# Analysis: 2026-06-10T09-15Z

**Fetch time:** 2026-06-10T09:18:38Z  
**Total current URLs:** 1338  
**Baseline URLs:** 1365  
**Added:** 2  
**Removed:** 29  
**Updated (sitemap lastmod):** 319  
**Pages with actual visible content changes:** 56  
**Anomalies:** 0  
**Fetch failures:** 0  

---

## Anomalies

None detected.

---

## Significant Removals (29 pages — the day's biggest signal)

Twenty-nine URLs disappeared from the sitemap today. This is the second large batch of removals in three days (28 were removed on June 9). Together these suggest an active cleanup/consolidation effort on OpenAI's public website.

### 1. OpenAI Foundation page removed from openai.com

**URL removed:** `https://openai.com/foundation/`  
**Last content:** Portal page for the OpenAI Foundation, describing a $25 billion commitment across two programs: Life Sciences/Curing Diseases and AI Resilience; plus the $50 million People-First AI Fund. Had a separate navigation and linked to `openaifoundation.org`.

**What this means:** The OpenAI Foundation has fully separated to its own domain (`openaifoundation.org`). The main openai.com navigation now links to it as an **external site** ("Foundation (opens in a new window)") — confirming the Foundation is now organizationally distinct from OpenAI the company. This is consistent with OpenAI's nonprofit-to-PBC restructuring completed earlier in 2026, which created the OpenAI Foundation as a separate nonprofit entity receiving the $6.5B endowment.

### 2. Advertisers page removed

**URL removed:** `https://openai.com/advertisers/`  
**Last content:** "Advertise in ChatGPT" — a landing page for advertisers explaining how to reach users in ChatGPT "as they explore options, compare choices, and make decisions." Linked to `ads.openai.com` for sign-up.

**What this means:** The advertising program appears to have moved to its own subdomain (`ads.openai.com`). The openai.com bridge page is no longer indexed.

### 3. DeployCo pages removed (3 URLs)

**URLs removed:**
- `https://openai.com/deployco/`
- `https://openai.com/deployco/privacy-policy/`
- `https://openai.com/deployco/terms-of-use/`

Together with `https://openai.com/business/the-openai-deployment-company/` (also removed today), all four pages tied to the "OpenAI Deployment Company" / "DeployCo" sub-brand are now gone. DeployCo appeared briefly as a concept for helping enterprises deploy OpenAI technology. Its disappearance suggests this brand/program has been folded into the core offering or discontinued.

### 4. Policy cleanup: Plugin terms, privacy policies, Sora policies removed

**URLs removed:**
- `https://openai.com/policies/plugin-terms/` — Plugin Terms of Service. ChatGPT Plugins were deprecated in 2024; this is final cleanup.
- `https://openai.com/policies/row-privacy-policy/` — Rest of World privacy policy.
- `https://openai.com/policies/services-privacy-policy/` — Services privacy policy.
- `https://openai.com/policies/business-terms/` — Business terms.
- `https://openai.com/policies/sora-usage-policies/` — Sora usage policies.
- `https://openai.com/policies/creating-sora-videos-in-line-with-our-policies/` — Sora video creation guidelines.
- `https://openai.com/policies/invoice-submission-guidelines/` — Invoice submission guidelines.

Multiple privacy policy variants (ROW and Services) being removed suggests consolidation into a unified privacy policy. Sora usage policies being removed may mean they were folded into the general usage policies. Plugin terms removal is final cleanup of the deprecated ChatGPT Plugins ecosystem.

### 5. Agent Platform page removed

**URL removed:** `https://openai.com/agent-platform/`  
The agent platform page was a landing for OpenAI's agentic products/APIs. Its removal likely reflects URL consolidation, with content now living under `/api/` developer docs or the Agents SDK documentation.

### 6. Safety Evaluations Hub removed

**URL removed:** `https://openai.com/safety/evaluations-hub/`  
**Last content:** A portal page for the "Deployment Safety Hub" — listing all GPT-5 series system cards. The hub itself is still active at its own URL; what was removed is the openai.com sitemap entry for the portal/redirect page.

### 7. Science and Healthcare pages removed

**URLs removed:**
- `https://openai.com/science/` — OpenAI's scientific research applications landing page.
- `https://openai.com/solutions/healthcare/` — Healthcare-focused solutions page.

Vertical-specific solution pages appear to be consolidating into the general business pages.

### 8. Other notable removals

- `https://openai.com/chatgpt/download/` — ChatGPT download page (likely redirected to app stores)
- `https://openai.com/chatgpt/search-product-discovery/` — ChatGPT search product discovery
- `https://openai.com/reserved-capacity/` — Reserved capacity page
- `https://openai.com/devday/directory/` — DevDay directory (event over)
- `https://openai.com/form/custom-models/` — Custom models form
- `https://openai.com/contributions/` — Contributions page
- `https://openai.com/newsroom/global-affairs/` and `https://openai.com/newsroom/security/` — Two newsroom category pages
- `https://openai.com/index/gpt-5-2-codex/` — The blog post about GPT-5.2-Codex removed from `/index/`
- `https://openai.com/index/parameter-golf/` — Parameter Golf article
- `https://openai.com/academy/top-10-use-cases-codex-for-work/` — Academy Codex use cases article
- `https://openai.com/business/guides-and-resources/` — Business guides page

---

## New Pages (2)

### 1. LSEG: "From data to decisions: how LSEG is scaling trusted AI"

**URL:** `https://openai.com/index/lseg/`  
**Page:** [pages/openai.com/index/lseg/index.md](../../pages/openai.com/index/lseg/index.md)  
**Published:** June 10, 2026 | **lastmod:** `2026-06-10T00:52:29.509Z`  
**Products:** ChatGPT, API | **Industry:** Finance | **Company size:** Enterprise

LSEG (London Stock Exchange Group) is one of the world's largest financial markets infrastructure and data providers, serving 40,000+ customers and 400,000+ end users across ~190 markets. This customer story describes how LSEG deployed OpenAI across the organization to transform knowledge work:

**Key metrics:**
- Product release cycles: **~6 months → ~2 weeks**
- Customer request to production deployment: **~4 weeks**

**Key quote:**
> "AI is a step change. But the real transformation comes when you rethink how you solve problems—not just how you execute them." — Emily Prince, Group Head of Enterprise AI, LSEG

LSEG combined ChatGPT and the API with their global data platform to accelerate insight generation and decision-making across the organization.

**Context:** Fits the ongoing push of ChatGPT Enterprise adoption by financial services firms. LSEG joins BNY, Balyasny, BBVA, and others on the customer stories page.

---

### 2. Nextdoor: "How engineers at Nextdoor use Codex to build without limits"

**URL:** `https://openai.com/index/nextdoor/`  
**Page:** [pages/openai.com/index/nextdoor/index.md](../../pages/openai.com/index/nextdoor/index.md)  
**Published:** June 9, 2026 | **lastmod:** `2026-06-09T09:47:06.424Z`  
**Products:** Codex | **Industry:** Technology | **Region:** North America

Nextdoor is a neighborhood platform serving 110 million users across 11 countries. This story focuses on how their **platform engineering team** uses Codex:

**Key themes:**
- **Outcome engineering**: Engineers shift from "how to build" to "what outcome to achieve" — giving Codex screenshots, performance targets, or feature descriptions as goals
- **Cross-team compression**: A feature requiring 3 teams (mobile, frontend, backend) can now be built by 1 engineer end-to-end
- **Hard debugging**: Codex investigates complex embedded Rust database issues, race conditions, and Kubernetes pod startup failures
- The bottleneck is no longer engineering capacity, but "the hard strategic questions about what to build next"

**Key quote:**
> "Codex has fundamentally changed how we think about engineering, to the point that we can't even imagine engineering without it." — Cory Dolphin, Head of Engineering, Nextdoor

**Context:** This story specifically showcases Codex for infrastructure and platform engineering (not just feature development), a somewhat new audience angle for Codex case studies.

---

## Significant Updates

### Navigation menu restructured across ~100+ pages

Many product pages had their navigation updated. The changes:

**Old nav (removed/changed):**
- "API log in" (lowercase)
- "Brand" link
- "Business Overview" → chatgpt.com/business/business-plan
- "Documentation" → developers.openai.com/api/do...

**New nav (added):**
- "API Log In" (capitalized)
- "Apps SDK" → developers.openai.com/apps-sdk **(new first-class nav item)**
- "ChatGPT Business" → chatgpt.com/business/
- "ChatGPT Enterprise" → chatgpt.com/business/en
- "ChatGPT for Education" → chatgpt.com/business/...

This nav update elevates "Apps SDK" as a first-class developer navigation item and restructures the ChatGPT business tiers as distinct nav entries.

### Industrial Policy for the Intelligence Age — inbox closed after 400+ submissions

**URL:** `https://openai.com/index/industrial-policy-for-the-intelligence-age/`  
**lastmod:** `2026-06-09T23:15:22.773Z`

New update note added: *"After receiving more than 400 responses, we are no longer accepting additional submissions through the inbox newindustrialpolicy@openai.com and are currently reviewing potential grant recipients."*

The fellowship/grant program (fellowships + up to $100K grants + up to $1M in API credits) received 400+ responses within roughly one day of the June 9 launch and has now closed submissions.

### GPT-5.5 Instant — personalization rolling to Free tier

**URL:** `https://openai.com/index/gpt-5-5-instant/`  
Update note added: *"Update on June 9, 2026: Personalization improvements are now rolling out to ChatGPT Go & Free. Responses on the Free tier will draw from a reduced set of past chats."*

GPT-5.5 Instant's personalization feature is now available to Free tier users (with a reduced set of past chats compared to paid tiers).

### Customer story "Related content" rotated site-wide

Dozens of customer stories and product pages had their "Keep reading" / "Related stories" sections updated:
- **Out:** S-1 filing (Jun 8), "Built to benefit everyone" (Jun 8), Public policy agenda (Jun 3)
- **In:** LSEG story (Jun 10), Nextdoor story (Jun 9), Industrial policy for the Intelligence Age (Jun 9)

This is a cosmetic/automatic rotation affecting ~50 pages simultaneously, explaining the bulk of the 319 sitemap-updated URLs.

### New sub-sitemap: global-affairs-news-listed

A new sub-sitemap `https://openai.com/sitemap.xml/global-affairs-news-listed/` appeared today alongside the existing `global-affairs` sub-sitemap. It contains Global Affairs articles with full `xhtml:link` alternate-language entries. This appears to be a new sitemap section specifically for the listed Global Affairs news articles, likely for improved international SEO coverage.

### CRED customer story — heading hierarchy fixed

**URL:** `https://openai.com/index/cred-swamy-seetharaman/`  
Interview questions changed from H4 (`####`) to H3 (`###`) heading level. Minor formatting normalization.

### Economic Research Exchange form — wording tweak

**URL:** `https://openai.com/form/economic-research-exchange/`  
"Select the question **areas** most relevant to your proposal" changed to "Select the question **area** most relevant to your proposal." (plural → singular). Minor wording change.

---

## Routine Updates

The remaining ~260 pages with updated `<lastmod>` timestamps but no detected content changes are sitemap metadata refreshes — OpenAI's CMS appears to touch timestamps when related content changes (e.g., when a new customer story is added, all customer story pages get a timestamp bump).

---

## Fetch Failures

None.

---

## Infrastructure Note

The sub/latest/ directory was cleaned up this run. Prior runs had accumulated stale sub-sitemap files under multiple different naming conventions (`_openai.com_*.xml`, `_openai_com_*.xml`, `https___*.xml`, etc.). These were removed, leaving only today's 33 canonical files (`sitemap.xml_*.xml`). Future runs should use the consistent `sanitize_filename` convention already in `run_today.py`.
