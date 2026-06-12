# Run Analysis: 2026-06-12T09-15Z

**Fetch time:** 2026-06-12T09:16:36Z  
**Baseline:** 2026-06-11T09-16Z  
**URLs:** 1345 baseline → 1347 current  
**Added:** 2 | **Removed:** 0 | **Updated (lastmod):** 273 | **Anomalies:** 0 | **Fetch failures:** 0

---

## 1. Anomalies

None detected. All `<lastmod>` timestamps are within normal range (none future-dated, none backwards from baseline).

---

## 2. New Pages (2)

### `https://openai.com/index/openai-to-acquire-ona/` ⭐ HIGH SIGNAL
- **lastmod:** 2026-06-12T07:41:04.991Z
- **Summary:** OpenAI announces the acquisition of **Ona** (ona.com), a cloud execution and orchestration company. Ona has helped 2 million developers work in secure, reproducible cloud environments. The acquisition is framed as expanding Codex with "persistent, customer-controlled cloud infrastructure" for long-running agents. Key context: Codex now has 5 million weekly users (up 400% since earlier this year). Ona's technology allows Codex agents to continue running inside a customer's own cloud environment even after the initiating session ends—addressing the "laptop is closed" problem for enterprise deployments. The acquisition is subject to regulatory approval; until closing, the companies remain independent.
- **Quotes:**
  - Johannes Landgraf (Ona CEO): "Agents need more than intelligence; they need a trusted workspace."
  - Thibault Sottiaux (OpenAI Core Products Lead): "Enterprises want powerful agents that can do real work while meeting the security and control requirements of their environments."
- **Context:** Fits with the enterprise-infrastructure push seen since May (Dell Codex partnership, Oracle cloud commitment, S-1 filing). This is OpenAI's latest acquisition in the run-up to IPO.
- **Path:** `pages/openai.com/index/openai-to-acquire-ona/index.md`

### `https://openai.com/index/preply/`
- **lastmod:** 2026-06-12T09:06:02.159Z
- **Summary:** New brand story (customer case study) for **Preply**, a language learning platform combining AI and human tutors. Key metrics: 95% ChatGPT weekly active usage among Preply employees; 70%+ tutors actively use AI-powered Lesson Insights feature. Products: ChatGPT, API, Codex. Company size: Mid-market. Industry: Technology/Education. Global region. The case study focuses on AI-generated lesson summaries providing personalized feedback.
- **Context:** The 6th brand story added in recent weeks (following BBVA, Choco, Cisco, Datadog, Canva, etc.), continuing a steady drumbeat of customer success stories supporting the IPO narrative.
- **Path:** `pages/openai.com/index/preply/index.md`

---

## 3. Significant Substantive Updates (pages with actual content changes)

### `https://openai.com/index/built-to-benefit-everyone-our-plan/`
- **lastmod:** 2026-06-12T03:25:24.735Z (was 2026-06-11T08:47:28.705Z)
- **Change:** "Keep reading" section at the bottom rotated to feature the new Ona acquisition announcement as the lead story, replacing the S-1 filing. Oracle cloud commitment replaced the Economic Research Exchange announcement; the S-1 filing itself moved down one slot. Old Dell/Codex story rotated off. This is a standard "recently published" news ticker rotation, not a substantive content change to the article itself.

### `https://openai.com/business/customer-stories/`
- **lastmod:** 2026-06-12T09:03:03.664Z (was 2026-06-11T04:56:59.580Z)
- **Change:** Added a new **BBVA banking** customer story card ("BBVA puts AI at the core of banking with OpenAI") to the featured grid. Removed the **Warp** story ("Warp's big bet on building open source with GPT-5.5") from the grid. (The Warp page itself remains in the sitemap—just deprioritized in this listing.)

### `https://openai.com/index/10bedicu/`
- **lastmod:** 2026-06-12T09:02:56.779Z (was 2026-06-10T22:51:15.129Z)
- **Change:** Minor structural reordering in the page—the header section (logo, summary, share) appears to have moved relative to an added table of contents. No substantive content change.

---

## 4. Routine lastmod Updates (no substantive content change)

273 URLs showed `<lastmod>` changes. Spot-checking 12 of these pages found **zero substantive content differences** vs the prior snapshot. The pattern is consistent with a CMS-wide template refresh or cache invalidation on 2026-06-11 and 2026-06-12. The affected URLs span nearly every sub-sitemap section: `/index/`, `/academy/`, `/business/`, `/api/`, `/global-affairs/`, `/about/`, etc.

Notable groups in this batch:
- **Pricing pages** (`/business/pricing/`, `/business/chatgpt-pricing/`, `/api/pricing/`): lastmod updated but no content changes detected. Pricing remains unchanged as of this fetch.
- **Academy pages** (champion-programs, codex-for-work guides, how-to-use-codex-for-everyday-work): lastmod bumped, no content change.
- **About page** (`/about/`): lastmod updated, no content change detected.
- **Daybreak page** (`/daybreak/`): lastmod updated, no content change detected.
- **Security pages** (~37 URLs): mass lastmod bump, likely from a template rebuild.
- **Safety pages** (~101 URLs): same pattern.

**Assessment:** The 273 `lastmod` changes are almost entirely CMS artifact / CDN rebuild noise, not editorial changes. The two new pages and the customer-stories grid swap are the only user-visible changes.

---

## 5. Removals

None.

---

## Summary

The headline event is **OpenAI's acquisition of Ona**, announced June 11. This is a strategic infrastructure move to give Codex persistent, enterprise-controlled cloud execution environments—directly enabling long-running agentic workflows without tethering to a user's device. With 5M weekly Codex users and an IPO on the horizon, the acquisition signals OpenAI's intent to compete for enterprise security-conscious deployments at production scale. The Preply brand story is a routine customer case study addition. The 273 lastmod updates appear to be a CMS sweep with no editorial substance.
