# Run Analysis: 2026-05-28T09-17Z

**Fetch time:** 2026-05-28T09:17:15.810573Z UTC
**Total URLs in sitemap:** 1326 (across 32 sub-sitemaps)
**Added:** 5 | **Updated:** 805 | **Removed:** 4
**Anomalies:** 2 (CMS timing artifacts, not meaningful) | **Fetch failures:** 3 (all deployco/)

---

## Anomalies

### future_lastmod (x2) — CMS Timing Artifact

- `https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/`
  — lastmod `2026-05-28T09:17:15.839Z` is 0.029s after fetch time `2026-05-28T09:17:15.810573Z`
- `https://openai.com/index/gpt-4o-system-card/`
  — lastmod `2026-05-28T09:17:21.765Z` is ~6s after fetch time

**Assessment:** These are not editorial anomalies. The CMS records lastmod as the current timestamp when regenerating the sitemap. Our fetch time and the CMS generation time differ by single-digit seconds. No action needed. This pattern has appeared previously.

---

## Significant Updates

### Safety page — New public safety commitments
URL: `https://openai.com/safety/`
lastmod: `2026-05-21T02:13:38.551Z` → `2026-05-28T09:16:58.701Z`

Three new bullet points added to OpenAI's public safety commitments section:
- "Improving transparency in AI content."
- "Rigorously evaluating content to avoid reinforcing biases or stereotypes."
- "Partnering with governments to combat disinformation globally."

The third bullet is notable: it was added the same day as the election-safeguards-2026 post (dated May 27, published today), suggesting coordinated messaging around the upcoming election season.

### Privacy policy — URL normalization only
URL: `https://openai.com/policies/privacy-policy/`
lastmod: `2026-02-25T08:58:18.271Z` → `2026-05-28T09:11:27.492Z`

All help.openai.com links changed from `/en/articles/...` to `/articles/...` format. No policy language changed. The large lastmod jump (February to May) is misleading — this was an infrastructure-level URL cleanup, not a policy revision. Flagged to avoid confusing with a material policy change.

### Consumer privacy page — Redirect updated
URL: `https://openai.com/consumer-privacy/`
lastmod: `2026-05-04T08:08:43.432Z` → `2026-05-28T09:10:24.207Z`

The "Privacy policy" link was updated from `/policies/row-privacy-policy/` to `/policies/privacy-policy/`. This confirms the ROW policy consolidation (see Removed section).

---

## New Pages

### 1. Intelligence at Work livestream
URL: `https://openai.com/business/intelligence-at-work/`
lastmod: `2026-05-28T09:17:09.292Z`

Enterprise-focused live event announced for **June 2, 2026 at 11:30am ET / 8:30am PT**. Presenters include Denise Dresser (CRO) and product leadership, with Sam Altman as special guest. The event will preview new enterprise capabilities, live demos, and discuss where enterprise AI is heading. Registration required. This is the first business/enterprise livestream event announced on the site outside of Codex-specific webinars.

### 2. Building self-improving tax agents with Codex
URL: `https://openai.com/index/building-self-improving-tax-agents-with-codex/`
lastmod: `2026-05-28T08:56:04.764Z`

Engineering post by OpenAI forward-deployed engineers (Arthur Fernandes Araujo, John de Wasseige) and Thrive Holdings engineers (Aravind Srinivasan, Samay Shamdasani). Describes a self-improvement loop: production failures by Crete accounting firm users are automatically converted into eval tests, which Codex then uses to improve autonomously. This is documented as a repeatable architecture pattern ("three-part loop") for production agentic systems, with a how-to section for readers to implement it. This is part of OpenAI's forward-deployment / professional services narrative. Closely related to the Codex engineering stories published May 22 (Virgin Atlantic) and May 27 (Cisco).

### 3. Election safeguards 2026
URL: `https://openai.com/index/election-safeguards-2026/`
lastmod: `2026-05-27T17:31:21.574Z` (published May 27)

Global Affairs post. Three stated focus areas: (1) helping voters access authoritative election information through ChatGPT, (2) supporting cyber defenders against AI-enabled influence operations, (3) increasing AI transparency. Follows a pattern established for the 2024 election cycle (`openai.com/index/how-openai-is-approaching-2024-worldwide-elections/`). No specific country elections named in the visible preview.

### 4. How to use Codex for everyday work (Academy)
URL: `https://openai.com/academy/how-to-use-codex-for-everyday-work/`
lastmod: `2026-05-28T08:29:05.385Z`

Replaces the removed `top-10-use-cases-codex-for-work` Academy page (same concept, refreshed). Targets non-technical business users with 8 documented use cases: daily work brief, weekly summary, slide decks, research-to-decision memo, file cleanup/reformatting, spreadsheet consolidation, book-of-business prioritization, month-end financial review. Includes a webinar embed. Part of the Academy's continued expansion of Codex content for enterprise roles.

### 5. Warp customer story
URL: `https://openai.com/index/warp/`
lastmod: `2026-05-27T20:00:01.421Z` (published May 27)

Warp (developer terminal/IDE company) uses GPT-5.5 for agentic open source development workflows. Key stats: 30% fewer tokens per task vs prior models. The story focuses on "Oz," Warp's internal orchestration layer for agents across local, cloud, and open-source repos. Company is a startup in North America. Filed under the "startup" category. The Warp use case positions GPT-5.5 specifically for agentic coding at open source scale, distinct from the enterprise-focused Cisco and Virgin Atlantic stories published earlier this week.

---

## Removed Pages

### Privacy policy consolidation (2 pages)
- `https://openai.com/policies/row-privacy-policy/` — "Rest of World" privacy policy variant removed. The `consumer-privacy` page now redirects to the unified `/policies/privacy-policy/`. Last snapshot: `pages/openai.com/policies/row-privacy-policy/index.md` (check git history: `git log -- pages/openai.com/policies/row-privacy-policy/index.md`).
- `https://openai.com/policies/services-privacy-policy/` — Second legacy variant removed. Last snapshot in git.

**Context:** OpenAI has been consolidating its multiple region-specific privacy pages over the past several months. The EU/UK/Switzerland policy at `/policies/eu-privacy-policy/` remains separate (required by GDPR). The ROW+services policies are now unified under the main US policy.

### Academy page swap
- `https://openai.com/academy/top-10-use-cases-codex-for-work/` — Replaced by `how-to-use-codex-for-everyday-work` (new URL, refreshed content, same concept). This appears to be an intentional URL rename/rebrand, not a content deletion. Last snapshot in git.

### Plugin terms cleanup
- `https://openai.com/policies/plugin-terms/` — ChatGPT plugins were deprecated in April 2024 (replaced by GPTs and the App Store). Removing the terms page is expected housekeeping 13 months post-deprecation. Last snapshot in git.

---

## Fetch Failures

All three failures are `deployco/` URLs — this is a continuing known issue, not new fetch failures.

- `https://openai.com/deployco/` — HTTP error (not live). First seen in sitemap: `2026-05-20T09-16Z` (Day 9).
- `https://openai.com/deployco/privacy-policy/` — HTTP error. First seen: `2026-05-22T09-15Z`.
- `https://openai.com/deployco/terms-of-use/` — HTTP error. First seen: `2026-05-22T09-15Z`.

**Assessment:** The "OpenAI Deployment Company" (DeployCo) has been in the sitemap for 9 days with fresh daily timestamps but is not yet publicly accessible. The daily timestamp refreshes suggest active publishing work behind the scenes. This will likely go live soon.

---

## Routine Updates: CMS Carousel Sweeps (801 pages)

The 801 remaining "updated" pages are all CMS sidebar rotations: "Keep Reading" / related-content carousels were updated to surface today's newly published content (Warp story, Cisco + Codex, building tax agents with Codex). No editorial changes to the pages' core content. The mass lastmod update is the CMS recording the current UTC timestamp when regenerating sidebars site-wide.

Pattern is consistent with prior days: whenever new notable content is published, the CMS sweeps the entire site to add it to relevant carousels.
