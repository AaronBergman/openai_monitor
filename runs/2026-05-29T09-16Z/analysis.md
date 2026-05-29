# Run Analysis: 2026-05-29T09-16Z

**Fetch time:** 2026-05-29T09:17:58Z
**Run ID:** 2026-05-29T09-16Z
**Baseline:** 2026-05-28T09-17Z

## Summary

- Total current URLs: 1330
- Added: 4
- Removed: 4
- Updated (lastmod changed): 855
- Anomalies: 0
- Fetch failures: 3 (deployco/* — all 404)
- Sub-sitemaps: 32

---

## Anomalies

None detected. No future lastmods, no backwards lastmods, no reappeared URLs.

---

## Notable Observations

### Mass lastmod-bump waves (not genuine content changes)

855 pages reported lastmod changes, but content diffs show minimal actual changes for the vast majority. The lastmods are concentrated in two waves:
- **May 22 batch:** 366 pages — a prior CMS sweep
- **May 29 batch:** 357 pages — today's CMS redeployment

This is routine CMS behavior: infrastructure changes or deploys cause Contentful to re-publish large batches of pages. The updated-page count is inflated by this; the truly meaningful changes are described below.

### Deployco pages: in sitemap, but returning 404

Three URLs (`/deployco/`, `/deployco/privacy-policy/`, `/deployco/terms-of-use/`) are in the sitemap with lastmods bumped to May 29 but return HTTP 404 when fetched. "Deployco" may be an upcoming product, a recently-removed product, or stale sitemap entries. Worth monitoring in future runs.

---

## New Pages (4)

### 1. OpenAI's Frontier Governance Framework
**URL:** https://openai.com/index/openai-frontier-governance-framework/
**lastmod:** 2026-05-28
**Path:** pages/openai.com/index/openai-frontier-governance-framework/index.md

Published May 28, 2026. A formal governance document explaining how OpenAI's safety and security practices align with emerging AI regulations:
- California's Transparency in Frontier AI Act
- EU AI Act's Code of Practice for General Purpose AI

The framework covers risk assessment and mitigation for cyber offense, CBRN risks, harmful manipulation, and loss of control — plus model reporting, security risk management, incident response, and external expert input. Linked as a PDF on OpenAI's CDN. This is OpenAI's first published document specifically designed to satisfy legal/regulatory compliance obligations.

### 2. MUFG × OpenAI customer story
**URL:** https://openai.com/index/mufg/
**lastmod:** 2026-05-28
**Path:** pages/openai.com/index/mufg/index.md

Mitsubishi UFJ Financial Group has deployed ChatGPT Enterprise to approximately 35,000 employees at Mitsubishi UFJ Bank. The story covers AI-native transformation, employee enablement, and new customer experiences in retail financial services. MUFG is one of the world's largest banks (Asia-Pacific). Published May 28, 2026.

### 3. Chip Ganassi Racing × OpenAI
**URL:** https://openai.com/index/chip-ganassi-racing/
**lastmod:** 2026-05-28
**Path:** pages/openai.com/index/chip-ganassi-racing/index.md

In-depth feature on the multi-year partnership with the IndyCar/IMSA team. Partnership started from a chance meeting at a Women in Motorsports event. Focus is on using AI to analyze sensor data, race data, and pit crew performance for competitive advantages. The homepage now prominently features this story. Published May 28, 2026.

### 4. Endava × OpenAI customer story
**URL:** https://openai.com/index/endava/
**lastmod:** 2026-05-28
**Path:** pages/openai.com/index/endava/index.md

UK-based technology services company Endava uses Codex to scale senior engineering expertise across its full delivery lifecycle. Key claim: weeks of work compressed into days. Published May 28, 2026. Part of ongoing Codex enterprise customer story push.

---

## Removed Pages (4)

1. **https://openai.com/academy/top-10-use-cases-codex-for-work/** — Academy article on Codex use cases; possibly merged or superseded by other Codex Academy content.
2. **https://openai.com/policies/plugin-terms/** — ChatGPT plugin terms of service; expected removal as plugins were deprecated in favor of Apps/GPTs.
3. **https://openai.com/policies/row-privacy-policy/** — Rest-of-World privacy policy variant; likely consolidated into main privacy policy.
4. **https://openai.com/policies/services-privacy-policy/** — Services-specific privacy policy; likely consolidated.

---

## Significant Updated Pages

### Homepage (https://openai.com/)
lastmod: 2026-05-20 → 2026-05-28
New Chip Ganassi Racing × OpenAI takeover/feature section added to homepage.

### OpenAI Academy Codex section
Numerous Codex-related Academy pages had lastmods bumped to May 29 (~01:38 UTC) — coordinated update of the Codex learning section.

---

## Fetch Failures (needs follow-up)

- **https://openai.com/deployco/** — HTTP 404 (in sitemap, lastmod bumped today)
- **https://openai.com/deployco/privacy-policy/** — HTTP 404 (in sitemap, lastmod bumped today)
- **https://openai.com/deployco/terms-of-use/** — HTTP 404 (in sitemap, lastmod bumped today)

"Deployco" appears to be a product name. The pages are listed in the sitemap (in the `page` sub-sitemap) with fresh lastmods but return 404. Possible interpretations: upcoming unreleased product, recently removed product, or infrastructure lag. Monitor in future runs.
