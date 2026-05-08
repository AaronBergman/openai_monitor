# Run Analysis: 2026-05-08T09-15Z

**Fetch time:** 2026-05-08T09:16:42Z UTC  
**Baseline:** 2026-05-07T09-01Z  
**Sub-sitemaps:** 34 listed in index; 33 successfully fetched  
**Baseline URLs:** 1,279 | **Current URLs (from 33 sitemaps):** 1,161  

---

## ANOMALIES

### 1. Near-future `<lastmod>` on Microsoft Partnership page

- **URL:** `https://openai.com/index/next-phase-of-microsoft-partnership/`
- **Kind:** `future_lastmod`
- **Sitemap claimed lastmod:** `2026-05-08T09:16:43.129Z`
- **Our fetch time:** `2026-05-08T09:16:42.532587Z`
- **Delta:** +0.60 seconds

The sitemap index was downloaded, then sub-sitemaps were fetched sequentially. By the time the sub-sitemap containing this URL was fetched and parsed, its `<lastmod>` was 0.6 seconds in the future relative to when we fetched the root index. This is almost certainly a CMS timestamp race — OpenAI's CMS updated the entry milliseconds after we started the fetch. The page content diff (vs yesterday's snapshot) shows only a "related articles" sidebar change (new articles rotated in), not a substantive content edit. **Likely benign, but documented per protocol.**

### 2. Sub-sitemap 403 Fetch Failure (needs follow-up)

- **Affected sub-sitemap:** `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/`
- **Error:** HTTP 403 Forbidden, all 4 retry attempts failed
- **Impact:** 122 URLs from yesterday's snapshot of this sub-sitemap could not be verified today. They are **NOT classified as removed** — status unknown.
- **Needs follow-up:** Monitor whether this sub-sitemap recovers access in subsequent runs. It may be geo-restricted, rate-limited, or intentionally restricted.
- **The 122 URLs** are all of the form `https://openai.com/index/<customer-story-slug>/` (brand/B2B case studies). Their pages remain available in `pages/openai.com/index/` as of the last successful snapshot (2026-05-07T09-01Z).

---

## SIGNIFICANT UPDATES

### API Pricing: Three New Realtime Audio Models Added

**Page:** `https://openai.com/api/pricing/`  
**Lastmod change:** 2026-05-02 → 2026-05-07  

Pricing page now reflects the new realtime audio model suite:

| Model | Change |
|---|---|
| `GPT-realtime-1.5` | **Replaced** by `GPT-Realtime-2` |
| GPT-Realtime-2 | Output price: $24.00/1M tokens (vs $16.00/1M for GPT-realtime-1.5 — **+50%**) |
| `GPT-Realtime-Translate` | **New** — $0.034/min ($0.00057/sec) |
| `GPT-Realtime-Whisper` | **New** — $0.017/min ($0.00028/sec) |

This is tied directly to the new "Advancing Voice Intelligence" blog post (see New Pages section).

### Advanced Account Security: Platform Language Broadened

**Page:** `https://openai.com/index/advanced-account-security/`  
**Lastmod change:** 2026-05-05 → 2026-05-08  

Two small but potentially meaningful edits: removed the phrase "on web" from two references to where users can enroll in Advanced Account Security. The text previously said users can enroll "on web starting today" — now it just says "starting today." This suggests the feature may now be available on mobile or other platforms, not just web. Also, a new "related articles" sidebar entry now links to the GPT-5.5-Cyber post.

### B2B Signals Article Title Rename

**Propagated across ~6 pages:**  
`"How frontier enterprises are building an AI advantage"` → `"How frontier firms are pulling ahead"`

This title change for `https://openai.com/index/introducing-b2b-signals/` propagated to all pages that display this article as related/sidebar content, causing those pages' `<lastmod>` timestamps to update. The rename is more punchy and less corporate. This appears to account for a significant fraction of the 127 "updated" URL count.

### Four Privacy Policy Pages Updated

All four updated on 2026-05-07 (evening UTC):
- `https://openai.com/policies/services-privacy-policy/`
- `https://openai.com/policies/communications-privacy-policy/`
- `https://openai.com/policies/services-communications-privacy-policy/`
- `https://openai.com/policies/us-privacy-policy/`

Page content diff showed no visible text changes in the rendered markdown — likely metadata/CMS update or backend reformatting. Could be related to adding Trusted Contact feature (which involves new data processing for notification contacts). **Recommend reviewing actual policy text in detail on next run.**

---

## NEW PAGES (4 added)

### 1. Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber

- **URL:** `https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/`
- **Lastmod:** 2026-05-07T23:41:12Z
- **Path:** `pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md`
- **Category:** Security

OpenAI is rolling out **GPT-5.5-Cyber** in limited preview for cybersecurity defenders. The post introduces a tiered "Trusted Access for Cyber" (TAC) framework:

| Access Level | Target Users | What Changes |
|---|---|---|
| GPT-5.5 (default) | General users | Standard safeguards |
| GPT-5.5 with TAC | Verified defenders | Lower refusal rates for vulnerability triage, malware analysis, reverse engineering, detection engineering, patch validation |
| GPT-5.5-Cyber | Specialized authorized workflows | Most permissive; for red teaming, penetration testing, controlled validation |

Users with elevated access are required to enable **phishing-resistant account security** (Advanced Account Security) by June 1, 2026. Partners announced: Cisco, CrowdStrike, Palo Alto Networks, Zscaler, Cloudflare, Akamai, Fortinet.

The post explicitly states GPT-5.5-Cyber is "not intended to significantly increase cyber capability beyond GPT-5.5 — it's primarily trained to be more permissive on security-related tasks." This is an iterative deployment for defender feedback loops.

This post follows the "Cybersecurity in the Intelligence Age" action plan published the prior week.

### 2. Advancing Voice Intelligence with New Models in the API

- **URL:** `https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/`
- **Lastmod:** 2026-05-08T08:54:11Z
- **Path:** `pages/openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/index.md`
- **Category:** Product / Release

Three new audio API models announced:

1. **GPT-Realtime-2** — First voice model with GPT-5-class reasoning. Key improvements: parallel tool calls, 128K context window (up from 32K), preamble support ("let me check that"), adjustable reasoning effort (minimal/low/medium/high/xhigh). Scores 15.2% higher on Big Bench Audio vs GPT-Realtime-1.5. Early partners: Zillow, Glean, Genspark, Bluejay, Intercom, Priceline, Foundation Health.

2. **GPT-Realtime-Translate** — Live speech translation, 70+ input languages, 13 output languages. Partners: BolnaAI, Vimeo, Deutsche Telekom.

3. **GPT-Realtime-Whisper** — Streaming speech-to-text for live transcription.

The post introduces a taxonomy of three voice AI patterns: voice-to-action (user speaks → system reasons and acts), systems-to-voice (software narrates updates), and voice-to-voice (real-time cross-language conversation).

### 3. Introducing Trusted Contact in ChatGPT

- **URL:** `https://openai.com/index/introducing-trusted-contact-in-chatgpt/`
- **Lastmod:** 2026-05-08T08:53:10Z
- **Path:** `pages/openai.com/index/introducing-trusted-contact-in-chatgpt/index.md`
- **Category:** Safety

New optional safety feature: users can nominate one trusted adult (friend, family member, caregiver) who may be notified if OpenAI's systems detect the user is discussing self-harm in a way that "indicates a serious safety concern."

How it works:
- User opts in from ChatGPT settings → nominates a contact → contact must accept within one week
- If automated monitoring flags a conversation, ChatGPT warns the user and may trigger a human review
- A small trained team reviews before any notification is sent (target: under 1 hour)
- Notification sent to Trusted Contact does NOT include chat transcripts — just a brief alert to check in

Developed with American Psychological Association, OpenAI's Global Physicians Network (260+ physicians in 60 countries), and Expert Council on Well-Being and AI. Extends existing parental control notifications (which already cover linked teen accounts) to all adults globally.

### 4. Parloa (Customer / Startup Story)

- **URL:** `https://openai.com/index/parloa/`
- **Lastmod:** 2026-05-08T03:27:48Z
- **Path:** `pages/openai.com/index/parloa/index.md`
- **Category:** Startup

Profile of Berlin-based Parloa, which builds an AI Agent Management Platform (AMP) for enterprise customer service. Parloa uses GPT-4.1, GPT-5-mini, and GPT-5.4 to simulate, evaluate, and run voice-driven customer service agents. Notable for its "evaluation-first approach" — they run production agent simulations before any model goes live. Appeared around the same time as the new voice intelligence post; likely a coordinated customer story for the voice API launch.

---

## ROUTINE UPDATES

The following categories of pages updated primarily due to new articles rotating into "Related" / "Recently published" sidebars, not substantive content changes:

- **Academy pages (20 updated):** Many Academy learning modules updated between 2026-05-07 and 2026-05-08. Likely reflect the Codex-focused content from recent days propagating through the Academy CMS.
- **Global Affairs pages (25+ updated):** Timestamp updates in the range 2026-05-08T08:00–08:07Z suggest a batch CMS operation. Content diffs show only sidebar article rotation (the B2B Signals title rename propagated here).
- **News section pages:** `/news/`, `/news/product-releases/`, `/news/safety-alignment/`, etc. all updated — expected as new articles are published.
- **Signals pages:** `/signals/`, `/signals/b2b/`, `/signals/data/`, `/signals/research/` — sidebar link title updated (B2B Signals article rename).
- **Codex pages:** `/codex/`, `/codex/get-started/`, multiple `/index/` Codex-related posts — all updated around 2026-05-08T05:24–05:26Z in a batch.

---

## REMOVED PAGES

**None confirmed.** The 122 URLs that appeared absent from today's diff are entirely accounted for by the HTTP 403 failure on the `internal-use-show-on-b2b-customer-stories-hub` sub-sitemap. No URLs were verified as actually removed from the site.

---

## STATISTICS

| Metric | Count |
|---|---|
| Total current URLs (verified) | 1,161 |
| Sub-sitemaps fetched | 33 of 34 |
| URLs added | 4 |
| URLs truly removed | 0 |
| URLs with lastmod updated | 127 |
| Anomalies | 1 (near-future timestamp, benign) |
| Fetch failures (sub-sitemap) | 1 (HTTP 403) |
| URL status unknown (from failed sitemap) | 122 |
