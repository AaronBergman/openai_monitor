# Run Analysis: 2026-05-23T09-15Z

**Fetch time:** 2026-05-23T09:16:10Z  
**Baseline:** 2026-05-22T09-15Z  
**Sub-sitemaps fetched:** 32  
**Total URLs (current):** 1,323  
**Total URLs (baseline):** 1,320  

---

## 1. ANOMALIES (Highest Signal)

### ANOMALY: Mass CMS Rebuild / Timestamp Flood
**Kind:** mass_lastmod_update  
**Scope:** 1,169 of 1,323 URLs (88%)

Between 2026-05-22T18:00Z and 2026-05-23T09:00Z, OpenAI's CMS updated lastmod timestamps on 88% of all indexed pages. The largest cluster (886 URLs) moved to 2026-05-22T18:00–19:59Z, with a secondary wave (266 URLs) updated 2026-05-23T00:00–08:59Z.

Spot-checking sampled pages (home `/`, `/about/`) showed **no detectable content change** — the HTML was byte-for-byte identical to prior snapshots. This is consistent with a CMS-wide rebuild, cache purge, or sitemap regeneration event, not a mass content edit.

**Significance:** This pattern makes it harder to identify real content changes from timestamp inspection alone. For this run, content was fetched for all new URLs and a representative sample of updated URLs.

---

### ANOMALY: Deployco Pages Return HTTP 404 (Sitemap Ghost URLs)
**Kind:** sitemap_url_404  

Two URLs appeared in the sitemap with freshly-updated lastmod timestamps but returned HTTP 404 when fetched:

- `https://openai.com/deployco/privacy-policy/` — lastmod: 2026-05-23T08:57:23Z
- `https://openai.com/deployco/terms-of-use/` — lastmod: 2026-05-23T03:12:43Z

These are not new pages — Deployco is a product that has appeared in previous runs. The 404s could indicate: (a) a deployment in progress, (b) pages moved to a different path, or (c) content pulled temporarily. **Needs follow-up** on next run to determine if these resurface.

---

## 2. SIGNIFICANT UPDATES

### `/daybreak/` — Codex Security Feature Additions
**URL:** https://openai.com/daybreak/  
**Lastmod changed:** 2026-05-18T20:43:27Z → 2026-05-23T07:08:43Z

Real content change confirmed. The page received a new section describing three Codex Security capabilities:
- **"Find and fix vulnerabilities"** — builds an editable threat model from a repository, focusing on realistic attack paths and high-impact code.
- **"Burn down the backlog"** — validates likely vulnerabilities in an isolated environment, prioritizing real, reproducible issues over noisy alerts.
- **"Automate detection and response"** — uses AI to spot higher-risk vulnerabilities and automate monitoring end-to-end.

Additionally, one image asset URL was updated (the Trusted Access for Cyber art card).

This aligns with OpenAI's ongoing push to position Codex as an enterprise security tool alongside its coding-agent capabilities.

---

### `/business/customer-stories/` — Significant Rotation
**URL:** https://openai.com/business/customer-stories/  
**Lastmod changed:** 2026-05-14T10:32:22Z → 2026-05-23T08:10:52Z

**Added (new stories visible on listing page):**
- Virgin Atlantic — "How Virgin Atlantic ships faster with Codex" (May 22, 2026)
- AdventHealth — "AdventHealth advances whole-person care with OpenAI" (May 21, 2026)
- Ramp — "How Ramp engineers accelerate code review with Codex" (May 20, 2026)
- Databricks — "Databricks brings GPT-5.5 to enterprise agent workflows" (May 15, 2026)
- Simplex — "Simplex rethinks software development with Codex" (May 7, 2026)

**Rotated off (still exist individually, just off the listing page):**
- CyberAgent (Apr 9), Gradient Labs (Apr 1), STADLER (Mar 27), Wayfair (Mar 11)

The listing page shows approximately the 5 most recent stories and rotates older ones off. The 5 new additions are all Codex-focused, reinforcing the enterprise Codex push.

---

## 3. NEW PAGES (3 Added)

### `https://openai.com/index/gartner-2026-agentic-coding-leader/`
**Lastmod:** 2026-05-22T18:52:24.731Z  
**Sub-sitemap:** ai-adoption  

Press release / news post announcing OpenAI was named a **Leader in the Gartner® Magic Quadrant™ for Enterprise AI Coding Agents** (published May 20, 2026). Key claims:
- Codex used by more than **4 million people per week**
- Enterprise customers include Cisco, Datadog, Dell Technologies, NVIDIA
- Gartner recognized Codex strengths: agentic software development, enterprise governance, sandboxing, flexible deployment
- Since Gartner's evaluation, Codex was further improved with GPT-5.5, stronger tool use, faster performance
- Cisco used Codex to develop "the majority of its AI Defense security platform," shortening delivery from several quarters to weeks
- Promotion announced: until June 12, eligible enterprise accounts can get **2 months of free Codex** for new users

Quote from Denise Dresser (CRO, OpenAI): "Codex [is] now one of OpenAI's fastest-growing enterprise products."

**Context:** Codex is now OpenAI's flagship enterprise B2B product. This Gartner recognition is a major marketing milestone, appearing alongside recent additions like the Virgin Atlantic story and Codex Security.

**Saved to:** [pages/openai.com/index/gartner-2026-agentic-coding-leader/index.md](../../pages/openai.com/index/gartner-2026-agentic-coding-leader/index.md)

---

### `https://openai.com/business/learn/gartner-2026-agentic-coding-leader/`
**Lastmod:** 2026-05-22T18:52:39.501Z  
**Sub-sitemap:** api  

Lead generation landing page paired with the Gartner announcement. Contains a form (work email, name, company, size, existing customer status) to download the 2026 Gartner Magic Quadrant for Enterprise AI Coding Agents report. This is the gated download; the `/index/` version is the public announcement.

**Saved to:** [pages/openai.com/business/learn/gartner-2026-agentic-coding-leader/index.md](../../pages/openai.com/business/learn/gartner-2026-agentic-coding-leader/index.md)

---

### `https://openai.com/index/virgin-atlantic/`
**Lastmod:** 2026-05-22T22:35:27.493Z  
**Sub-sitemap:** brand-stories-api  

Customer story: **Virgin Atlantic using Codex** to ship software faster. Key metrics:
- 78–80% codebase size reduction on legacy refactors
- ~100% unit test coverage on new mobile app
- 30 minutes to refactor legacy codebases (down from 2 weeks)
- Shipped revamped mobile app for Christmas travel rush with **zero P1 defects at launch**

Quotes from:
- Neil Letchford (VP Digital Engineering): "The ability to utilize Codex to improve the quality of the application before it got into the hands of our customers was a game-changer."
- Richard Masters (VP Data and AI): "Trajectory of Codex is thinking beyond pure engineers. It's moving into a real tool for everyone."

**Context:** Follows the AdventHealth story (May 21), continuing a rapid cadence of enterprise Codex customer stories. All recent stories emphasize Codex rather than ChatGPT.

**Saved to:** [pages/openai.com/index/virgin-atlantic/index.md](../../pages/openai.com/index/virgin-atlantic/index.md)

---

## 4. REMOVALS

None. 0 URLs removed from sitemap.

---

## 5. FETCH FAILURES

| URL | Error |
|-----|-------|
| https://openai.com/deployco/privacy-policy/ | HTTP 404 — in sitemap but page not accessible |
| https://openai.com/deployco/terms-of-use/ | HTTP 404 — in sitemap but page not accessible |

Both Deployco pages were not overwritten (preserving prior-good snapshot, though they were not present in git — no prior snapshot to preserve). Needs follow-up next run.

---

## Summary

- **3 new URLs** — Gartner Magic Quadrant Leader announcement (Codex), gated report download form, Virgin Atlantic customer story
- **0 removals**
- **1,169 updated lastmod** — mass CMS rebuild, no real content change on sampled pages
- **Real content changes confirmed on:** `/daybreak/` (Codex Security feature additions), `/business/customer-stories/` (listing rotation)
- **3 anomalies:** mass CMS timestamp flood, 2× Deployco 404 ghost URLs in sitemap
