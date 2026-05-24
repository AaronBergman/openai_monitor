# Run Analysis: 2026-05-24T09-15Z

**Fetch time:** 2026-05-24T09:17:46Z  
**Baseline:** 2026-05-23T09-15Z  
**Total URLs in current sitemap:** 1,323  
**Sub-sitemaps fetched:** 32  

---

## Summary

Quiet day. 157 URLs touched by the CMS, but the vast majority are invisible metadata-only updates (126 pages with no rendered content change) plus "related articles" widget rotations across ~17 research/customer-story pages. Thirteen Codex Academy pages had their "Share" button removed. One genuinely new piece of content appeared on the Signals data-download page. One sitemap-reality discrepancy flagged: `deployco/privacy-policy/` listed in the sitemap with today's lastmod but returns HTTP 404.

---

## Anomalies

### Sitemap-reality discrepancy: `deployco/privacy-policy/`
- **URL:** `https://openai.com/deployco/privacy-policy/`
- **Claimed lastmod:** `2026-05-24T05:46:28.870Z` (today)
- **Actual HTTP response:** 404 Not Found
- The sitemap claims this page was modified today, but fetching it returns a 404. The page does not exist despite appearing in the sitemap. This warrants follow-up — either the sitemap is stale or the page was deleted immediately after being modified.
- **Prior content preserved** in git history at `pages/openai.com/deployco/privacy-policy/index.md`

---

## Significant Updates

### 1. Signals data-download: AI Jobs Transition Framework data added
- **URL:** `https://openai.com/signals/data-download/`
- **Lastmod:** `2026-05-23T23:36:03.092Z`
- **Change:** A new section "Report data and methodology" was appended, with a download link:
  > [Download data for the AI Jobs Transition Framework](http://cdn.openai.com/signals/ai-job-transition-framework-data-download.zip)
- This extends the Signals data download section (which previously only contained ChatGPT usage data) to include data from the AI Jobs Transition Framework, a separate research initiative. The prior content (CSV files, data dictionary, and NBER working paper citation) remains unchanged; this is a net addition.
- **Path:** `pages/openai.com/signals/data-download/index.md`

### 2. Research and news index: item reordering
- **URLs:** `https://openai.com/research/index/` and `https://openai.com/news/research/`
- **Change:** "Introducing GPT-5.5" (Product) and "GPT-5.5 System Card" (Safety) swapped display order on the listing pages. Substantively unchanged — both articles still present, just in different positions.

---

## Routine Updates

### CMS "related articles" widget rotation (≈17 pages)
Customer story pages (balyasny-asset-management, bbva-2025, bny, chime-vineet-mehra, commonwealth-bank-of-australia, jetbrains-2025, rakuten, singular-bank, trustbank, gpt-5-lowers-protein-synthesis-cost, and math/physics research pages) all updated their "Related reading" sidebar to replace older articles with:
- "An OpenAI model has disproved a central conjecture in discrete geometry" (May 20, 2026)
- "What Parameter Golf taught us" (May 12, 2026)
- "OpenAI named a Leader in enterprise coding agents by Gartner" (May 22, 2026)
- "How Virgin Atlantic ships faster with Codex" (May 22, 2026)
- "AdventHealth advances whole-person care with OpenAI" (May 21, 2026)

This is a sitewide content widget refresh, not individual page edits.

### Codex Academy pages: "Share" button removed (13 pages)
All Codex-for-work Academy pages had a "Share" button removed from their rendered output. Affected pages:
`codex-automations/`, `codex-for-work/how-business-operations-teams-use-codex/`, `codex-for-work/how-data-science-teams-use-codex/`, `codex-for-work/how-sales-teams-use-codex/`, `codex-how-to-start/`, `codex-plugins-and-skills/`, `codex-settings/`, `how-finance-teams-use-codex/`, `top-10-use-cases-codex-for-work/`, `what-is-codex/`, `working-with-codex/`, and the education article `the-next-phase-of-education-for-countries/`, and `sharing-the-latest-model-spec/`.

### CMS metadata-only touches (126 pages)
126 URLs show a lastmod bump in the sitemap with no rendered content change. The bulk of these are older research papers (GPT-2, DALL-E, Dota 2, robotics papers, etc.) all bumped around 06:34–06:36 UTC, and customer story pages bumped around 07:29–07:31 UTC. This is consistent with a scheduled CMS re-publish or template rebuild, as seen in previous runs (most notably the 2026-05-23 CMS rebuild that touched 1,169 URLs).

---

## Added Pages

None.

---

## Removed Pages

None detected from the previous run's sitemap.

---

## Fetch Failures

| URL | Error |
|-----|-------|
| `https://openai.com/deployco/privacy-policy/` | HTTP 404 — page not found despite sitemap listing |

---

## Notes for Follow-up

1. **`deployco/privacy-policy/` 404**: Verify whether DeployCo's privacy policy page has been permanently removed or if this is a transient error. The page had been accumulating lastmod history since it first appeared.
2. **AI Jobs Transition Framework data**: The new download on `signals/data-download/` references a ZIP file at `cdn.openai.com`. Consider monitoring whether the framework gets its own dedicated page in the sitemap.
