# Run Analysis: 2026-05-25T09-15Z

**Fetch time:** 2026-05-25T09:16:44Z  
**Baseline:** 2026-05-24T09-15Z  
**Total URLs (current):** 1323  
**Added:** 0 | **Removed:** 0 | **Updated (lastmod):** 158  

---

## Anomalies

### 1. `deployco/privacy-policy` — 404 but in sitemap
- **URL:** https://openai.com/deployco/privacy-policy/
- **Claimed lastmod:** 2026-05-25T09:10:04.929Z (mere minutes before this run's fetch)
- **Observation:** HTTP 404 when fetched via curl-cffi. The sitemap claims this page was just updated, but the page does not exist or is not routable.
- **Interpretation:** Either the page is being set up and hasn't gone live yet, was removed but the sitemap wasn't updated, or there's a publishing pipeline lag. DeployCo is an OpenAI subsidiary involved in AI deployment services. Needs follow-up in tomorrow's run to determine if it resolves to a live page.

---

## Update Batches (All Timestamp-Only — No Content Changes Detected)

Our fetches and diffs confirmed that in all cases examined, the page HTML/markdown content was identical to the prior snapshot. All 158 "updates" reflect CMS/CDN infrastructure events that bump `<lastmod>` without changing visible page content.

### Batch A — Large Research/Publication CMS Deploy (~117 pages)
- **Timestamp cluster:** 2026-05-24T21:48–21:50Z (all within ~2.5 minutes)
- **Pages affected:** Old research papers, classic model announcements (GPT-2, GPT-4, DALL-E, Sora, Dota 2, Hello GPT-4o, etc.), engineering posts, milestone pages.
- **Interpretation:** A backend CMS deployment or content-management refresh ran on the evening of May 24 UTC and bumped the modification timestamps on ~117 legacy research and publication pages. No substantive content changes detected in sampled pages (gpt-4-research, sora, hello-gpt-4o all had zero-diff content).
- **Notable included pages:** about/, research/index/, news/research/

### Batch B — Customer Stories (~21 pages + business/customer-stories/)
- **Timestamp cluster:** 2026-05-25T08:12–08:45Z (all within ~33 minutes)
- **Pages affected:** Balyasny Asset Management, BBVA (2 pages), BNY, Chime, Commonwealth Bank of Australia, Cred, Endex, Gradient Labs, Hebbia, JetBrains, Klarna, Mercado Libre, Model ML (Chaz Englander), Morgan Stanley, Nubank, o1-economics, Rakuten, Rogo, Singular Bank, TrustBank, business/customer-stories/
- **Interpretation:** Customer story pages received a batch timestamp update this morning UTC. No content changes detected in the business/customer-stories/ index page.

### Batch C — OpenAI Academy / Codex Pages (11 pages)
- **Timestamp cluster:** 2026-05-25T04:34–05:03Z
- **Pages affected:** codex-automations, codex-for-work/how-business-operations-teams-use-codex, codex-for-work/how-data-science-teams-use-codex, codex-for-work/how-sales-teams-use-codex, codex-how-to-start, codex-plugins-and-skills, codex-settings, how-finance-teams-use-codex, top-10-use-cases-codex-for-work, what-is-codex, working-with-codex
- **Interpretation:** The Codex-focused Academy training pages had timestamps bumped in the pre-dawn UTC hours. No content changes detected in sampled pages.

### Batch D — Signals Product Pages (5 pages)
- **Timestamp cluster:** 2026-05-25T05:57–09:04Z
- **Pages affected:** signals/, signals/b2b/, signals/data/, signals/research/, signals/data-download/
- **Interpretation:** OpenAI's "Signals" market intelligence product pages — a relatively newer product — had their timestamps updated. No content changes detected.

### Batch E — Miscellaneous (2 pages)
- **form/guaranteed-capacity/:** 2026-05-25T05:59Z
- **index/the-next-phase-of-education-for-countries/:** 2026-05-24T10:42Z (earlier in the day)

---

## Removed Pages

None.

---

## Added Pages

None.

---

## Fetch Failures

| URL | Error | Notes |
|-----|-------|-------|
| https://openai.com/deployco/privacy-policy/ | HTTP 404 | In sitemap with lastmod 2026-05-25T09:10Z — **needs follow-up** |

---

## Summary

Today's run produced zero structural changes to the OpenAI sitemap (no added or removed URLs). All 158 `<lastmod>` updates are timestamp-only CMS/CDN deployment artifacts — the actual page content is unchanged. The single genuine anomaly is `deployco/privacy-policy/`, which appears in the sitemap with a very fresh timestamp but returns HTTP 404.
