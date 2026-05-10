# Run Analysis: 2026-05-10T09-16Z

**Fetch time:** 2026-05-10T09:17:38Z  
**Baseline:** 2026-05-09T09-15Z  
**Sub-sitemaps fetched:** 34 (19 initially returned 503, all recovered on retry; `/sitemap.xml/page/` served from prior cached snapshot due to persistent 503s)  
**Total current URLs:** 1287 (+1 vs 1286 baseline)

## Summary

1 URL added, 198 URL timestamps updated, 0 removed. The dominant narrative is OpenAI's strategic pivot in two directions: (a) **shutting down the self-serve fine-tuning platform**, a major developer-facing change announced via retroactive banner updates, and (b) **expanding its cybersecurity offering** with a new specialized model (GPT-5.5-Cyber) and a Trusted Access for Cyber framework. A new customer story (Simplex) demonstrates Codex adoption at an Asia-Pacific technology firm.

---

## ANOMALIES

**None detected** — no future lastmods, no backwards lastmods, no URL disappearances/reappearances, no sub-sitemap migrations observed.

**Infrastructure note:** `/sitemap.xml/page/` returned HTTP 503 persistently across all 4 retry attempts. The sub-sitemap was served from the most recent cached copy (2026-05-09T09-15Z snapshot). URLs in the `/page/` sub-sitemap will not reflect any changes since the prior run. Noted as a partial-fetch event, not a hard failure.

---

## SIGNIFICANT UPDATES

### 1. Fine-Tuning Platform Shutdown (MAJOR) — 3 pages updated May 8, 2026

OpenAI added identical shutdown notices to three fine-tuning-related pages. The notice text:

> **Update on May 8, 2026**: OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users but existing users of the fine-tuning platform will be able to create training jobs for the coming months. All fine-tuned models will remain available for inference until their base models are deprecated.

**Affected pages:**
- [`/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/`](../../pages/openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/index.md) — original April 2024 announcement of the fine-tuning API. lastmod: `2026-04-29 → 2026-05-09`
- [`/index/introducing-vision-to-the-fine-tuning-api/`](../../pages/openai.com/index/introducing-vision-to-the-fine-tuning-api/index.md) — vision fine-tuning announcement. lastmod updated.
- [`/index/gpt-4o-fine-tuning/`](../../pages/openai.com/index/gpt-4o-fine-tuning/index.md) — GPT-4o fine-tuning announcement. lastmod updated.

**Significance:** The self-serve fine-tuning API was a key developer tool available since August 2023. This shutdown affects any developer or organization that relied on creating custom fine-tuned models through OpenAI's platform. Existing models remain available for inference, but no new training jobs for new users going forward. The deprecation timeline is linked from developer documentation.

### 2. GPT-5.5-Cyber and Trusted Access for Cyber Framework

[`/index/gpt-5-5-with-trusted-access-for-cyber/`](../../pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) — lastmod: `2026-05-07 → 2026-05-10T08:13Z`. No content changes detected (only metadata refresh). This page was published May 7, 2026 and describes:

- **GPT-5.5-Cyber**: A specialized model in limited preview for defenders protecting critical infrastructure. More permissive for authorized security workflows (authorized red-teaming, penetration testing, controlled validation).
- **Trusted Access for Cyber (TAC)**: An identity/trust verification framework with three tiers:
  - GPT-5.5 (default): Standard safeguards
  - GPT-5.5 with TAC: More precise safeguards for verified defensive work
  - GPT-5.5-Cyber: Most permissive, for specialized authorized workflows
- Starting June 1, 2026: Individual TAC members must enable Advanced Account Security (phishing-resistant MFA).

### 3. Accelerating Cyber Defense Ecosystem — Related Posts Updated

[`/index/accelerating-cyber-defense-ecosystem/`](../../pages/openai.com/index/accelerating-cyber-defense-ecosystem/index.md) — lastmod: `2026-05-09 → 2026-05-10T06:43Z`. Content change: the "Keep reading" sidebar updated from pointing to "GPT-5.5 Instant System Card" and "Introducing Advanced Account Security" to pointing to "Running Codex safely at OpenAI" and "Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber."

### 4. Running Codex Safely at OpenAI — Post Confirmed

[`/index/running-codex-safely/`](../../pages/openai.com/index/running-codex-safely/index.md) — lastmod: `2026-05-09T08:17 → 2026-05-10T08:48Z`. No content changes detected (only metadata refresh). This page (published May 8, 2026) explains how OpenAI deploys Codex internally with governance controls:
- **Sandboxing and approvals**: Codex operates inside bounded technical environments
- **Network policies**: Restricted network access
- **Identity and credentials**: Managed credential systems
- **Managed configs**: Standardized deployment configurations
- **Agent-native telemetry and audit trails**: Logging for accountability

### 5. OpenAI on AWS — Related Posts Updated

[`/index/openai-on-aws/`](../../pages/openai.com/index/openai-on-aws/index.md) — lastmod: `2026-05-08 → 2026-05-09T13:14Z`. Content change: sidebar updated from "GPT-5.5 Instant: smarter, clearer, and more personalized" and "New ways to buy ChatGPT ads" to "Advancing voice intelligence with new models in the API" and "Testing ads in ChatGPT." The page itself is unchanged.

---

## ROUTINE UPDATES (Batch Operations)

The following appear to be infrastructure/CMS metadata updates rather than individual content changes. No content changes were detected by diff for most of these.

### Academy Pages (21 pages, updated May 7–8, 2026)
All OpenAI Academy sub-pages received lastmod bumps around 2026-05-07T12:28Z–2026-05-08T21:45Z:
- applications-of-ai, brainstorming, building-with-ai, chatgpt-for-education, codex, customer-success, data-analysis, finance, financial-services, getting-started, healthcare, managers, marketing, operations, research, responsible-and-safe-use, sales, skills, what-is-ai, writing

### Global Affairs Pages (~20 pages, updated May 8, 2026)
All Global Affairs articles received lastmod bumps around 2026-05-08T18:41Z–18:44Z (batch time ~18:41–18:44 UTC). Consistent with a CMS republish event.

### Customer Story Index Pages (~50 pages, updated May 10, 2026, ~07:14–07:23 UTC)
Many `/index/` customer stories (bbva, bny, balyasny, chime, cna, commonwealth-bank, cred, endex, gradient-labs, hebbia, hygh, jetbrains, klarna, mercado-libre, model-ml, morgan-stanley, neurogum, nubank, o1-economics, plex-coffee, podium, rakuten, rogo, singular-bank, steuerrecht, trustbank, vfl-wolfsburg, and many more) received lastmod bumps today around 07:14–07:23 UTC. These appear to be a single batch CMS operation affecting the customer/brand story hub.

### Form Pages (9 pages, updated May 8, 2026 ~13:32–13:34 UTC)
All `/form/` pages received lastmod bumps: 100-chats-book-request, codex-ambassadors, codex-app, codex-labs, learning-lab, openai-on-aws (form), share-your-story, showcase-submission, subscribe-to-new-sub-processors.

### Policy Pages (5 pages, updated May 7–8, 2026)
cookie-policy, communications-privacy-policy, services-communications-privacy-policy, services-privacy-policy, us-privacy-policy — received lastmod bumps. Cookie policy had the most notable jump (from Feb 2026 to May 8).

### Signals Pages (4 pages, updated May 8, 2026)
/signals/, /signals/b2b/, /signals/data/, /signals/data-download/, /signals/research/ — all updated May 8.

### Other Individual Updates
- `https://openai.com/` (homepage): May 6 → May 7. No content changes detected.
- `/api/`: May 7 → May 8. No content changes detected.
- `/api/pricing/`: May 2 → May 7. No content changes detected.
- `/business/`: May 5 → May 8. No content changes detected.
- `/careers/`: May 7 → May 8. No content changes detected.
- `/chatgpt/enterprise/`: May 6 → May 7. No content changes detected.
- `/chatgpt/overview/`: May 5 → May 10. No content changes detected.
- `/startups/`: May 7 → May 8. No content changes detected.
- `/news/` and news sub-pages: May 7 → May 8. No content changes detected.

---

## NEW PAGES

### 1. Simplex — New Customer Story

**URL:** [`/index/simplex/`](../../pages/openai.com/index/simplex/index.md)  
**lastmod:** 2026-05-08T00:25:49Z  
**first_seen:** 2026-05-10T09-16Z (this run)

**Summary:** Simplex is a Japanese technology company (consulting, systems development, operations) that has adopted ChatGPT Enterprise and Codex as its primary coding agent. Key quantified results:
- **70%** fewer hours to develop each screen
- **40%** fewer hours to design each screen  
- **17%** fewer hours for internal integration testing

The case study focuses on "AI-native delivery" — redesigning the software development process around AI rather than using AI as an assistive overlay. Simplex is exploring fully automated workflows from RFP to product for simple systems. Industry: Technology; Region: Asia-Pacific & Oceania; Company size: Enterprise.

**Context:** Fits with the active Codex push (Codex generally available announced May 7; "Running Codex safely at OpenAI" published May 8; multiple Codex-related GPT-5.5 model variants). This is the first Japanese enterprise Codex-specific customer story.

---

## REMOVALS

No URLs removed from the sitemap in this run.

---

## FETCH FAILURES

| Sub-sitemap | Issue |
|---|---|
| `https://openai.com/sitemap.xml/page/` | Persistent HTTP 503 across 4 retry attempts; served from cached 2026-05-09 snapshot. |

No page-level fetch failures (all fetched pages passed sanity check of >100 chars and no Cloudflare challenge page content).

---

## STATS

| Metric | Count |
|---|---|
| Total current URLs | 1287 |
| URLs added | 1 |
| URLs updated (lastmod) | 198 |
| URLs removed | 0 |
| Anomalies | 0 |
| Sub-sitemaps | 34 |
| Sub-sitemap 503 recoveries | 1 served from cache (page/) |
