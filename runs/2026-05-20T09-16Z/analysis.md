# Run Analysis: 2026-05-20T09-16Z

**Fetch time:** 2026-05-20T09:16:48Z  
**Baseline:** 2026-05-18T09-15Z  
**Total URLs (current):** 1316  
**Total URLs (baseline):** 1314  
**Added:** 9 | **Removed:** 7 | **Updated:** 148 | **Anomalies:** 0

---

## 1. Anomalies

None detected this run.

## 2. Notable Fetch Failures

- **https://openai.com/deployco/** — URL appeared in the sitemap (lastmod: 2026-05-20T03:43:12.046Z) but returned HTTP 404 when fetched. This is an *in-sitemap, not-yet-live* page — possibly a new product landing page being staged. Worth monitoring; should appear or disappear in the next 24–48 hours.

## 3. Major Structural Change: /chatgpt/* section removed from sitemap

**7 URLs removed** from openai.com's sitemap, all under /chatgpt/:

| Removed URL | Last Modified |
|---|---|
| /chatgpt/desktop/ | 2026-04-09 |
| /chatgpt/education/ | 2026-04-22 |
| /chatgpt/enterprise/ | 2026-05-07 |
| /chatgpt/overview/ | 2026-05-10 |
| /chatgpt/pricing/ | 2026-05-12 |
| /chatgpt/team/ | 2026-05-12 |
| /chatgpt/use-cases/student-writing-guide/ | 2026-04-20 |

**Interpretation:** These pages are migrating from openai.com to chatgpt.com. Evidence: the business page changed its enterprise link from `openai.com/chatgpt/enterprise/` to `https://chatgpt.com/business/enterprise`. Similarly, the education and team pages appear to be redirecting to chatgpt.com equivalents. This is a deliberate consolidation of ChatGPT-specific marketing under the chatgpt.com domain. Pages are still accessible at chatgpt.com — this is not content deletion, it's a domain reorganization.

Markdown snapshots preserved in git at:
- `pages/openai.com/chatgpt/desktop/index.md`
- `pages/openai.com/chatgpt/education/index.md`
- `pages/openai.com/chatgpt/enterprise/index.md`
- `pages/openai.com/chatgpt/overview/index.md`
- `pages/openai.com/chatgpt/pricing/index.md`
- `pages/openai.com/chatgpt/team/index.md`
- `pages/openai.com/chatgpt/use-cases/student-writing-guide/index.md`

## 4. New Pages (9 added)

### 4a. OpenAI Guaranteed Capacity (business/guaranteed-capacity/)
**lastmod:** 2026-05-20T09:10:33Z  
**Summary:** A new enterprise product offering long-term compute commitments. Customers can purchase 1–3 year capacity commitments with volume discounts, guaranteeing access to OpenAI compute for their most critical AI workflows. This is likely a response to enterprise demand for infrastructure certainty. A companion form page (`/form/guaranteed-capacity/`) was also added simultaneously.

### 4b. /deployco/ (FETCH FAILURE — 404)
**lastmod:** 2026-05-20T03:43:12Z  
**Summary:** URL appeared in sitemap but returned 404. Name "deployco" is intriguing — may relate to enterprise deployment or a new product. Needs follow-up in next run.

### 4c. /form/codex-project-showcase-and-feedback/ (new form)
**lastmod:** 2026-05-20T09:07:02Z  
**Summary:** Form for Codex project showcases and user feedback, consistent with the growing Codex ecosystem (4M+ weekly developers noted in the Dell partnership announcement).

### 4d. /form/guaranteed-capacity/ (new form)
**lastmod:** 2026-05-20T09:06:11Z  
**Summary:** Lead-capture form for the new Guaranteed Capacity product.

### 4e. Advancing Content Provenance (index/advancing-content-provenance/)
**lastmod:** 2026-05-20T09:02:24Z (pub: May 19, 2026) — Safety  
**Summary:** Blog post about content provenance technology. OpenAI announces C2PA conformance and integration with Google's SynthID watermarking for images. Ties directly to the new `/research/verify/` tool (see 4i). Part of a broader industry push for AI content attribution and transparency.

### 4f. Dell + Codex Enterprise Partnership (index/dell-codex-enterprise-partnership/)
**lastmod:** 2026-05-20T07:51:18Z (pub: May 18, 2026) — Company  
**Summary:** OpenAI and Dell Technologies partner to deploy Codex in hybrid/on-premises enterprise environments. Codex connects with Dell AI Data Platform (on-prem data storage) and Dell AI Factory (AI workloads). Highlights Codex's rapid growth (4M+ weekly developers) and expansion beyond coding into business workflows.

### 4g. OpenAI for Singapore (index/introducing-openai-for-singapore/)
**lastmod:** 2026-05-20T09:03:53Z (pub: May 19, 2026) — Global Affairs  
**Summary:** OpenAI launches "OpenAI for Singapore" at the ATx Summit, in partnership with Singapore's Ministry of Digital Development and Information (MDDI). Backed by S$300M+ commitment. Three focus areas: frontier AI deployment for national priorities, AI talent development, and broad economic access to AI.

### 4h. Education for Countries update (index/the-next-phase-of-education-for-countries/)
**lastmod:** 2026-05-20T08:39:55Z (pub: May 20, 2026) — Global Affairs  
**Summary:** Update from Education World Forum in London. Singapore joins the "Education for Countries" program. First cohort: Estonia, Greece, Italy's CRUI, Slovakia, Trinidad & Tobago, Kazakhstan, UAE, and Jordan. Focuses on AI in education with government-led research partnerships.

### 4i. Verify OpenAI Images Tool (research/verify/)
**lastmod:** 2026-05-20T08:45:38Z — Research  
**Summary:** New public tool (research preview) to check whether an image was generated with OpenAI tools. Detects C2PA metadata and SynthID watermarks. Works for ChatGPT, OpenAI API, and Codex-generated images. Directly linked to the content provenance initiative announced in 4e.

## 5. Significant Page Updates

### 5a. Homepage (/)
Swapped the featured article card: replaced "Introducing Advanced Account Security" (Apr 30, 2026) with "Advancing content provenance for a safer, more transparent AI ecosystem" (May 19, 2026). Routine homepage card rotation.

### 5b. Business page (/business/)
One meaningful change: the "Learn about ChatGPT Enterprise" button now links to `https://chatgpt.com/business/enterprise` instead of `https://openai.com/chatgpt/enterprise/`. Confirms the chatgpt.com migration noted in section 3.

### 5c. ChatGPT Pricing page (/business/chatgpt-pricing/)
Large new FAQ section appended (8 questions added). Key new content:
- Explicit mention of ChatGPT "Go" plan alongside Plus, Business, Enterprise
- Free plan for verified U.S. K–12 educators through June 2027 (ChatGPT for Teachers)
- ChatGPT Edu for universities
- Nonprofit discounts up to 75% on Business or Enterprise via "OpenAI for Nonprofits"
- Business plans start at 2 users
- Payment options: credit card for Go/Plus/Pro/Business; invoicing available for Enterprise

### 5d. API Pricing page (/api/pricing/)
Large new FAQ section appended (7 questions added). Key new content:
- Model selection guidance (large vs mini, reasoning vs general)
- Enterprise SLA and custom tier information
- Confirmation that Playground usage is billed the same as API usage
- Links to usage dashboard and billing settings
- Clarification that API access is NOT included in ChatGPT Plus/Business/Enterprise/Edu
- Detailed image token pricing calculator revealed

## 6. Routine Updates

- **72 /index/ pages** (blog posts): 41 updated with 2026-05-18 timestamps, 27 with 2026-05-20 timestamps — likely a CMS deployment wave touching metadata across many posts. No significant content changes expected.
- **25 /global-affairs/ pages**: 25 with 2026-05-18 timestamps — same deployment wave.
- **12 /academy/ pages**: Codex Academy content refreshed (all timestamped 2026-05-20), slight updates.
- **12 /form/ pages**: Minor CMS updates, all around 09:07 UTC (same deploy).
- **6 /policies/ pages**: Updated 2026-05-18/19, routine policy maintenance.
