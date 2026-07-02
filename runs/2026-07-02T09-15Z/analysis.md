# Run Analysis: 2026-07-02T09-15Z

**Fetch time:** 2026-07-02T09:17:52Z
**Baseline:** 2026-07-01T09-15Z
**Total current URLs:** 1386
**Baseline URLs:** 1386

---

## ANOMALIES

**None detected.** No future-dated lastmod, no backwards-moving lastmod, no added/removed URLs (so no disappear/reappear cases), no genuine sub-sitemap migrations (checked with set-based membership tracking per the fix landed 2026-07-01).

---

## SIGNIFICANT UPDATES

**None.** Of the 13 URLs whose `<lastmod>` changed, 12 are byte-for-byte identical to the prior snapshot in `pages/openai.com/` — the timestamp moved but the rendered page content did not, consistent with the "related articles / Keep Reading" CMS sidebar-refresh pattern documented in prior runs (e.g. 2026-06-26, 2026-06-29 entries).

## ROUTINE UPDATES (13 lastmod bumps, 1 real content change)

| URL | Old lastmod | New lastmod | Content diff |
|---|---|---|---|
| `/index/gpt-5-immunology-mystery/` | 2026-07-01T09:06:46Z | 2026-07-01T09:42:26Z | none |
| `/index/how-chatgpt-adoption-has-expanded/` | 2026-06-30T16:01:46Z | 2026-07-01T18:21:26Z | none |
| `/policies/professional-services-security-measures/` | 2026-06-30T16:29:32Z | 2026-07-01T18:51:37Z | none |
| `/form/trademark-counterfeit-disputes/` | 2026-06-29T13:02:33Z | 2026-07-01T19:55:27Z | none |
| `/index/how-agents-are-transforming-work/` | 2026-07-01T04:50:26Z | 2026-07-01T22:45:29Z | none |
| `/business-data/` | 2026-07-01T08:53:41Z | 2026-07-01T23:03:47Z | none |
| `/index/previewing-gpt-5-6-sol/` | 2026-06-30T18:42:04Z | 2026-07-01T23:15:29Z | none |
| `/index/hp-frontier-partnership/` | 2026-07-01T04:57:26Z | 2026-07-01T23:23:03Z | none |
| `/codex/` | 2026-07-01T09:13:47Z | 2026-07-01T23:33:31Z | none |
| `/index/openai-broadcom-jalapeno-inference-chip/` | 2026-07-01T08:21:03Z | 2026-07-02T06:28:47Z | none |
| `/index/core-dump-epidemiology-data-infrastructure-bug/` | 2026-07-01T08:16:04Z | 2026-07-02T08:57:34Z | none |
| `/index/genebench-pro/case-studies/` | 2026-07-01T09:16:08Z | 2026-07-02T09:08:14Z | none |
| `/index/introducing-genebench-pro/` | 2026-07-01T09:16:07Z | 2026-07-02T09:08:27Z | **1-line link swap** |

### `/index/introducing-genebench-pro/` — citation link update

The "Read the paper" link changed from a self-hosted CDN PDF (`cdn.openai.com/pdf/.../genebench-pro.pdf`) to the canonical bioRxiv preprint URL (`biorxiv.org/content/10.64898/2026.06.29.735386v2`). This mirrors how the original *GeneBench* v1 paper is already cited on the same page (also a bioRxiv link), so this reads as OpenAI swapping a placeholder/internal link for the final external preprint citation now that the paper has posted to bioRxiv — not a substantive change to the announcement itself.

## NEW PAGES

None. 0 added.

## REMOVALS

None. 0 removed.

---

## Notes

- All 34 sub-sitemaps fetched successfully (200 OK), same set of sections as prior run.
- URL universe is exactly stable at 1386 (0 added, 0 removed) — the quietest run on record so far this log.
- No fetch failures.
