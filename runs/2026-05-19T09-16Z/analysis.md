# Run 2026-05-19T09-16Z Analysis

**Fetch time:** 2026-05-19T09:19:02Z  
**Baseline:** 2026-05-18T09-15Z  
**Total current URLs:** 1309  
**Added:** 0  **Updated:** 106  **Removed:** 7  
**Anomalies:** 0  **Fetch failures:** 0

---

## Removals — Most Significant Signal

Seven core ChatGPT **product/marketing pages** have been removed from the sitemap today. All were present since the start of monitoring (first seen 2026-05-07) and last confirmed 2026-05-18:

| URL | Title | Last lastmod |
|-----|-------|-------------|
| `/chatgpt/overview/` | Get answers. Find inspiration. Be more productive. | 2026-05-10 |
| `/chatgpt/pricing/` | Pricing | 2026-05-12 |
| `/chatgpt/team/` | ChatGPT for business, powered by OpenAI's most advanced models | 2026-05-12 |
| `/chatgpt/enterprise/` | Frontier AI built for enterprise | 2026-05-07 |
| `/chatgpt/desktop/` | ChatGPT on your desktop | 2026-04-09 |
| `/chatgpt/education/` | Bring AI to campus at scale | 2026-04-22 |
| `/chatgpt/use-cases/student-writing-guide/` | A Student's Guide to Writing with ChatGPT | 2026-04-20 |

These were in the `/sitemap.xml/page/` sub-sitemap, which now has 362 URLs (vs ~369 before). The chatgpt sub-sitemap itself (`/sitemap.xml/chatgpt/`) already only ever contained article/story links, not product pages.

**What still exists under `/chatgpt/`:** `/chatgpt/download/`, `/chatgpt/use-cases/writing-with-ai/`, `/chatgpt/search-product-discovery/` remain indexed. The main product section pages (overview, pricing, team plans, enterprise) and the desktop page are the notable absences.

**Interpretation:** This appears to be a deliberate restructuring or pruning of the ChatGPT product section. Notably, `/business/chatgpt-pricing/` remains in the sitemap — the pricing content may have migrated to the `/business/` path. Similarly, `/academy/chatgpt-for-education/` remains for the education angle. The core `/chatgpt/overview/` and `/chatgpt/team/` pages had recent lastmod dates (May 10–12), suggesting they were actively maintained up until removal. Worth monitoring whether these URLs now redirect.

---

## Updated Pages — 106 Metadata-Only Refreshes

All 106 updated pages showed **0 content length change** — these are pure lastmod timestamp bumps with no visible text changes. Three clusters:

### Cluster 1: Codex Academy (11 pages, ~07:55 UTC today)
All Codex for Work tutorial and guide pages had their lastmod bumped from ~2026-05-16 to ~2026-05-19T07:55Z in a tightly synchronized batch (~20-second window). Consistent with an automated CMS republish.

Pages: `codex-automations/`, `codex-for-work/how-business-operations-teams-use-codex/`, `codex-for-work/how-data-science-teams-use-codex/`, `codex-for-work/how-sales-teams-use-codex/`, `codex-how-to-start/`, `codex-plugins-and-skills/`, `codex-settings/`, `how-finance-teams-use-codex/`, `top-10-use-cases-codex-for-work/`, `what-is-codex/`, `working-with-codex/`

### Cluster 2: Global Affairs (25 pages, ~09:38–09:39 UTC yesterday)
All global-affairs articles bumped from ~2026-05-15 to ~2026-05-18T09:38-39Z. Same automated-sweep pattern. Covers policy posts, country blueprints, election commentary, AI governance documents.

### Cluster 3: Index + News (70 pages, scattered)
64 `/index/` pages and 6 `/news/` pages updated. Covers wide range: teen/child safety posts, GPT-5.5 cyber page, economic blueprints, safety/security content, product announcements. Timestamped throughout 2026-05-18.

---

## Anomalies

None detected.

---

## Sub-sitemap Naming Note

The current run saved dated sub-sitemaps using the `run_monitor.py` legacy naming convention (`https___openai.com_sitemap.xml_*`) in `sitemaps/openai.com/sub/2026-05-19T09-16Z/`, while the `sub/latest/` directory continues to use the `_openai.com_sitemap.xml_*` convention established in the 2026-05-18 migration. Both file sets contain identical content — only naming differs.
