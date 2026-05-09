# Run Analysis: 2026-05-09T09-15Z

**Fetch time:** 2026-05-09T09:16:02Z  
**Baseline:** 2026-05-07T09-15Z (1,279 URLs)  
**Current:** 1,164 URLs (net −115)  
**Sub-sitemaps fetched:** 33 of 34 (1 returned HTTP 403)

---

## ANOMALIES

### 1. BACKWARDS LASTMOD — `enterprise-privacy/`
- **URL:** `https://openai.com/enterprise-privacy/`
- **Old lastmod (2026-05-07 run):** `2026-05-04T08:38:21.081Z`
- **New lastmod (this run):** `2025-01-31T01:52:00.485Z`
- **Delta:** ~15 months backward
- **Page content:** No visible change — the rendered markdown is byte-for-byte identical to the prior snapshot. The "Updated: January 8, 2026" text inside the page has not changed.
- **Assessment:** This is a CMS/sitemap metadata glitch. The claimed lastmod regressed to what appears to be a historical CMS date (possibly the original publication or a prior version date), while the actual content is unchanged. Not a content rollback.

### 2. SUB-SITEMAP `internal-use-show-on-b2b-customer-stories-hub` RETURNED HTTP 403
- All 122 URLs previously indexed under this sub-sitemap are now "missing" from the current snapshot.
- **However:** Spot-checking confirms these pages still resolve as live content (e.g., `https://openai.com/index/canva/` returns full page, ~9KB markdown).
- **Assessment:** OpenAI has restricted access to this specific sub-sitemap endpoint. The 122 customer-story pages have NOT been removed — they are still live. This is a sitemap governance change, not a content removal. The sub-sitemap name begins with "internal-use-" suggesting OpenAI may have intentionally locked it down. All 122 URLs have been preserved in `state/known_urls.json` with their last known state.

---

## NEW PAGES (7)

All 7 new URLs appeared in the `page` or relevant sub-sitemaps for the first time this run.

### 1. `advancing-voice-intelligence-with-new-models-in-the-api/` (May 7, 2026)
- **Path:** `pages/openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/index.md`
- **Category:** Product / Release
- **Summary:** Announces three new audio models in the OpenAI API:
  - **GPT-Realtime-2**: First voice model with GPT-5-class reasoning, handles harder requests in real-time conversation.
  - **GPT-Realtime-Translate**: Live translation from 70+ input languages to 13 output languages, keeping pace with the speaker.
  - **GPT-Realtime-Whisper**: Streaming speech-to-text that transcribes live as the speaker talks.
- **Context:** Follows the broader GPT-5 ecosystem rollout and Codex launches of the past week. Positioned as developer infrastructure for a new class of voice apps.

### 2. `gpt-5-5-with-trusted-access-for-cyber/` (May 7, 2026)
- **Path:** `pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md`
- **Category:** Security
- **Summary:** Details the rollout of GPT-5.5-Cyber in limited preview to defenders responsible for securing critical infrastructure. Explains the "Trusted Access for Cyber" (TAC) tiered access framework:
  - GPT-5.5 (standard): General use
  - GPT-5.5 with TAC: Verified defensive work (vulnerability triage, malware analysis, detection engineering)
  - GPT-5.5-Cyber: Limited preview for specialized authorized workflows (red teaming, pen testing)
- As of June 1, 2026, TAC users accessing the most capable models must enable phishing-resistant "Advanced Account Security."
- **Context:** Relates to `cybersecurity-in-the-intelligence-age` action plan published the same week and `advanced-account-security` page (updated May 9).

### 3. `running-codex-safely/` (May 8, 2026)
- **Path:** `pages/openai.com/index/running-codex-safely/index.md`
- **Category:** Security / Safety
- **Summary:** Technical guide on how OpenAI internally deploys Codex with governance controls: sandboxing, human-approval workflows for high-risk actions, network policies, and agent-native audit trails. Positioned as both a transparency document and a template for enterprise customers deploying Codex.
- **Context:** Companion piece to Codex's general availability and the broader Codex ecosystem launch; also part of the security narrative alongside the cybersecurity action plan.

### 4. `how-chatgpt-protects-privacy/` (May 6, 2026)
- **Path:** `pages/openai.com/index/how-chatgpt-protects-privacy/index.md`
- **Category:** Global Affairs
- **Summary:** Bilingual (English + French) plain-language explainer on ChatGPT's training data practices, personal information handling, and user privacy controls. The French section is a full translation, suggesting this was produced specifically for Canadian regulatory/consumer audiences.
- **Context:** Coincides with a wave of privacy policy updates (services-privacy-policy, us-privacy-policy, cookie-policy all updated May 7-8), suggesting a coordinated privacy communication push.

### 5. `introducing-trusted-contact-in-chatgpt/` (May 7, 2026)
- **Path:** `pages/openai.com/index/introducing-trusted-contact-in-chatgpt/index.md`
- **Category:** Safety
- **Summary:** Introduces "Trusted Contact," an optional safety feature for ChatGPT adults. Users can nominate a trusted person (friend, family member, caregiver) to be notified if OpenAI's automated systems detect serious self-harm risk signals. Extends existing parental-controls safety alerts to all adults 18+. Clinical guidance from CDC on social connection as protective factor.
- **Context:** Extends `parental controls safety notifications` launched earlier; OpenAI expanding its safety alert system beyond minors.

### 6. `advancing-youth-safety-in-emea/` (May 5, 2026)
- **Path:** `pages/openai.com/index/advancing-youth-safety-in-emea/index.md`
- **Category:** Safety / Global Affairs
- **Summary:** Announces (a) OpenAI's European Youth Safety Blueprint — a policy framework with five pillars for age-appropriate AI use — and (b) the first recipients of the EMEA Youth & Wellbeing Grant. Blueprint addresses: responsible AI in education, age-appropriate safeguards with privacy-preserving age assurance, under-18 safety policies, protections against manipulative AI outputs, and accessible parental controls.
- **Context:** Related to `teen-safety-policies-gpt-oss-safeguard` (updated May 7) and broader EU/EMEA regulatory engagement. Appears to be timed to EU policy discussions.

### 7. `parloa/` (May 7, 2026)
- **Path:** `pages/openai.com/index/parloa/index.md`
- **Category:** Startup (customer story)
- **Summary:** Profile of Parloa, a European startup building enterprise voice-driven customer service agents using OpenAI models. Uses OpenAI API for simulation, evaluation, and live voice service systems. First appeared on the customer stories hub in this run.
- **Context:** Immediately appeared on the `business/customer-stories/` hub, replacing the VfL Wolfsburg and Axios Allison Murphy entries in the visible list. Parloa is notable as a European API-based customer — aligns with OpenAI's Germany/France/EU push.

---

## SIGNIFICANT UPDATES

### B2B Signals page — messaging rebrand
- **URL:** `https://openai.com/signals/b2b/`
- **Lastmod:** `2026-05-06T21:25:24.938Z` → `2026-05-08T23:06:40.627Z`
- **Change:** The phrase "AI advantage" was systematically replaced with "frontier advantage" throughout the page. The introductory framing was also rewritten to be more concise, cutting the explanation of the "capability overhang" analogy and simplifying to a cleaner statement of the product's purpose.
- **Significance:** This is a deliberate messaging/positioning choice — shifting from the generic "AI advantage" to "frontier advantage" to align with OpenAI's "frontier model" brand positioning.

### Customer Stories hub rotation
- **URL:** `https://openai.com/business/customer-stories/`
- **Change:** Added Parloa (Startup, May 7) and Simplex (May 7) to the featured list. Removed VfL Wolfsburg (Mar 5) and Axios/Allison Murphy (Mar 4) from the visible carousel. Uber (May 6) was reshuffled in ordering.

### API page — new enterprise section
- **URL:** `https://openai.com/api/`
- **Change:** Added new "Enterprise-ready solutions for real impact" section with a "See all solutions" link, presenting a three-tab interface (Use cases / Industries / Blueprints).

### Privacy policy wave (May 7-8)
Multiple privacy/policy documents updated in a coordinated wave:
- `policies/services-privacy-policy/` (→ May 7)
- `policies/communications-privacy-policy/` (→ May 7)
- `policies/services-communications-privacy-policy/` (→ May 7)
- `policies/us-privacy-policy/` (→ May 7)
- `policies/cookie-policy/` (→ May 8)
- `policies/usage-policies/` (→ May 7)
All six policy documents updated within a 24-hour window, coordinated with the `how-chatgpt-protects-privacy` privacy explainer launch.

### Codex ecosystem refreshes (May 7-8)
Multiple Codex pages received lastmod updates on May 7-8, suggesting a coordinated content refresh following Codex GA:
- `codex/` (→ May 8)
- `codex/get-started/` (→ May 8)
- `index/gpt-5-2-codex/` through `gpt-5-5-instant/` — multiple model announcement pages refreshed
- `index/introducing-upgrades-to-codex/`, `index/codex-now-generally-available/`, etc.

### Academy learning content (May 7-8)
All OpenAI Academy course pages received updates (21 URLs), suggesting a content or platform refresh:
- `academy/codex/`, `academy/building-with-ai/`, `academy/chatgpt-for-education/`
- `academy/customer-success/`, `academy/data-analysis/`, `academy/marketing/`, etc.

### Microsoft partnership page (May 9)
- **URL:** `https://openai.com/index/next-phase-of-microsoft-partnership/`
- **Lastmod:** → `2026-05-09T07:31:30.317Z` (most recently updated page in this run)
- No visible content change in fetched markdown vs prior snapshot.

### FedRAMP Moderate (May 9)
- **URL:** `https://openai.com/index/openai-available-at-fedramp-moderate/`
- Page now explicitly mentions GPT-5.5 availability in FedRAMP environment and upcoming Codex Cloud access via FedRAMP ChatGPT Enterprise workspace.

---

## ROUTINE UPDATES

Many pages received minor lastmod bumps (likely CMS metadata touches without visible content changes):
- Global affairs pages: ~30+ pages in the global-affairs namespace received coordinated updates around May 8 18:41-18:44 UTC (likely a batch CMS publish)
- News hub pages: `news/`, `news/engineering/`, `news/global-affairs/`, `news/product-releases/`, etc.
- Form pages: 8 form pages (codex-labs, codex-app, learning-lab, etc.) all bumped ~May 8 13:32-13:45 UTC

---

## REMOVED PAGES (0 confirmed)

No pages are confirmed removed. The 122 "removed" URLs are an artifact of the `internal-use-show-on-b2b-customer-stories-hub` sub-sitemap returning HTTP 403. All spot-checked pages remain live. Their state has been preserved in `known_urls.json`.

---

## FETCH FAILURES

- `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/` → HTTP 403 (not a page fetch; this is the sub-sitemap index endpoint itself)

---

## STATS

| Metric | Value |
|---|---|
| Baseline URLs | 1,279 |
| Current URLs | 1,164 |
| Net change | −115 |
| Added | 7 |
| Confirmed removed | 0 |
| Missing (403 sub-sitemap) | 122 |
| Updated | 153 |
| Anomalies | 2 |
| Sub-sitemaps (of 34) | 33 fetched, 1 × 403 |
| Fetch failures (pages) | 0 |
