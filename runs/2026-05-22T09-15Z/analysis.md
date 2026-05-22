# Run Analysis: 2026-05-22T09-15Z

**Fetch time:** 2026-05-22T09:16:28Z  
**Baseline:** 2026-05-21T09-15Z  
**Sub-sitemaps fetched:** 32  
**Total current URLs:** 1,320 (baseline: 1,318)

---

## Summary

- **3 added**, **1 removed**, **131 updated** (lastmod changed), **0 anomalies**
- Of the 131 updated: **20 had true content changes**, **110 were timestamp-only** (CMS touch, no diff)
- **3 fetch failures** (all DeployCo pages returning HTTP 404)

---

## 1. Anomalies

**None detected.** No future-dated lastmods, no backwards lastmod movements, no disappeared-then-reappeared URLs.

---

## 2. Fetch Failures (Needs Follow-up)

### DeployCo — Third Day, Still 404

**`https://openai.com/deployco/`** (updated, HTTP 404)  
**`https://openai.com/deployco/privacy-policy/`** (new, HTTP 404)  
**`https://openai.com/deployco/terms-of-use/`** (new, HTTP 404)

DeployCo (`/deployco/`) first appeared in the sitemap on **2026-05-20** (first_seen: `2026-05-20T09-16Z`) and has returned HTTP 404 on every fetch attempt since. Today, two new sub-pages were added to the sitemap — a **Privacy Policy** and **Terms of Use** — both also 404. The presence of legal pages strongly suggests this is a full product entity (or newly-acquired company) being staged for launch, not just a placeholder. The parent URL also received a fresh lastmod update today (`2026-05-22T00:07:03.558Z`), indicating ongoing backend CMS activity.

**Pattern:** sitemap entries present → HTTP 404 on all three days → now adding legal pages  
**Assessment:** Imminent launch likely within days. "DeployCo" could relate to enterprise deployment tooling given OpenAI's current trajectory with Codex and business customers.

---

## 3. Significant Updates (True Content Changes)

### 3a. Retail Industry Solutions Page — Major Expansion

**URL:** `https://openai.com/solutions/industries/retail/`  
**Change:** +3,355 chars — six new use-case sections added at the bottom

New sections added:
1. **Change how consumers shop** — promotes ChatGPT shopping research for in-depth product comparisons; links to `/index/chatgpt-shopping-research/`
2. **Equip store teams with an intelligent companion** — associates get instant, multilingual product/policy answers
3. **Accelerate and localize marketing creative** — AI-generated marketing assets for any channel/market
4. **Create conversational shopping experiences** — shoppers describe needs in natural language for product suggestions
5. **Strengthen supplier negotiations** — AI synthesizes sales, margin, inventory data into negotiation talking points
6. **Optimize store visits with actionable insights** — turns field notes/photos into prioritized action plans

**Significance:** This substantially deepens OpenAI's retail vertical pitch, moving from generic AI claims to concrete, named workflows. Retail now has a more comprehensive solutions page comparable to healthcare and finance verticals.

---

### 3b. Agents Use Case Page — Four New Examples

**URL:** `https://openai.com/solutions/use-case/agents/`  
**Change:** +2,039 chars — four new agent workflow examples added

New examples:
1. **Qualify and route inbound leads** — research prospects, score, personalize outreach, update CRM
2. **Review and respond to IT requests** — evaluate tool requests, compare against approved systems, respond in Slack, document decisions
3. **Create draft marketing content at scale** — brief → blog posts, social, emails, landing pages
4. **Analyze feedback and surface product priorities** — aggregate signals from support/forums, generate summaries, create product tickets

**Significance:** Agents page is being filled out with concrete enterprise workflow examples rather than abstract capability descriptions. All four examples are multi-step, cross-tool workflows — aligns with OpenAI's push to position Codex and agent-based products for business automation.

---

### 3c. Guaranteed Capacity Form — Significant Redesign

**URL:** `https://openai.com/form/guaranteed-capacity/`  
**Change:** -72 chars net, but substantive restructuring

**Workload options changed:**
- Before: Customer-facing product / Internal workflow / Platform / infrastructure / Codex BYOK / Not sure
- After: API production environment / API internal workflow / Codex / ChatGPT / Not sure

**Endpoint/region options expanded dramatically:**
- Before: US endpoint / Global endpoint / Non-US data residency required
- After: US / EU / UK / Middle East / Japan / Korea / India / ANZ / ASEAN / Other Global endpoint

**Removed:** The "Estimated guaranteed capacity need" field (which had TPM tiers: <100M, 100-250M, 250-500M, 500M-1B TPM) was eliminated entirely.

**Significance:** The endpoint expansion from 3 to 10+ regions signals OpenAI is actively selling Guaranteed Capacity to enterprise customers across Asia-Pacific, Middle East, and Europe — not just US/global. Removing the TPM estimate field may mean they're qualifying customers differently (by use case rather than raw volume), or it's handled in follow-up. The "Codex BYOK" option being renamed simply to "Codex" suggests BYOK is no longer a distinct offering.

---

### 3d. Academy Codex Pages — "Keep Reading" Reordering (10 pages)

**URLs:** 10 OpenAI Academy pages (codex-automations, codex-for-work/*, codex-how-to-start, codex-plugins-and-skills, codex-settings, how-finance-teams-use-codex, top-10-use-cases-codex-for-work, what-is-codex, working-with-codex)

**Change:** "How sales teams use Codex" article moved to top of the "Keep reading" section on all these pages (minor reordering of related links, same total length). No substantive content changed.

---

### 3e. Index Articles — "Keep Reading" Refreshed

**URLs:** Several index articles (gpt-5-2-codex, introducing-gpt-5-2-codex, databricks, nvidia, introducing-gpt-5-4, new-ways-to-buy-chatgpt-ads, powering-product-discovery-in-chatgpt)

**Change:** "Keep reading" sidebar sections refreshed to show newer articles (AdventHealth case study now appearing as a recommendation; older articles rotated out). Minor text tweaks elsewhere (+14–23 chars on a few pages).

---

## 4. New Pages

### AdventHealth Case Study

**URL:** `https://openai.com/index/adventhealth/`  
**First seen:** 2026-05-22T09-15Z  
**Published:** May 21, 2026  
**File:** `pages/openai.com/index/adventhealth/index.md`

AdventHealth, a hospital system spanning 9 states, deployed ChatGPT for Healthcare to reduce administrative burden. Key details:
- **80% reduction in time spent on administrative tasks** (headline stat)
- Use case: physician advisors reviewing utilization management cases — AI generates structured chart summaries and drafts rationales; clinician retains final judgment
- Metric of success: "messages per user per business day" treated as a KPI like any other operational metric
- Quote: "We chose OpenAI because we weren't looking for a demo. We were looking for enterprise infrastructure."
- Quote: "Adoption is not 'go use the product.' It's change leadership."
- Also used in: Finance, HR, IT, document drafting, policy summarization
- Product: ChatGPT Enterprise → ChatGPT for Healthcare

**Context:** Third healthcare case study in recent weeks, alongside broad enterprise push. Fits with the pattern of OpenAI building out vertical-specific product variants (ChatGPT for Healthcare, etc.).

---

## 5. Removed Pages

### Plugin Terms of Use

**URL removed from sitemap:** `https://openai.com/policies/plugin-terms/`

ChatGPT Plugins were deprecated in 2024. This appears to be final cleanup of the plugin-era legal document from the sitemap. The page may still be accessible directly but is no longer indexed. The git history will preserve the last snapshot.

---

## 6. Routine Updates (Timestamp-Only)

**110 URLs** had their `<lastmod>` timestamps updated with no corresponding content change. These are CMS-level touches (likely metadata, cache invalidation, or minor template updates). Grouped breakdown:
- ~10 `/academy/codex-*` pages: all same-minute timestamp (~21:32 UTC May 21)
- ~20 `/form/*` pages: all around 21:41–21:42 UTC May 21
- ~30 `/index/*` pages: various times on May 21
- ~10 `/security/*`, `/safety/*`, `/solutions/*` pages: May 21 timestamps
- Remaining: scattered pages across verticals

All confirmed identical content to prior snapshot.

---

## Stats

| Metric | Count |
|--------|-------|
| Total URLs in sitemap | 1,320 |
| Added | 3 |
| Updated (lastmod changed) | 131 |
| True content changes | 20 |
| Timestamp-only | 110 |
| Removed | 1 |
| Anomalies | 0 |
| Fetch failures | 3 |
| Sub-sitemaps | 32 |
