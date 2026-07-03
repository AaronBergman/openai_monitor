# Run 2026-07-03T09-16Z — Analysis

**Fetch time (sitemap index):** 2026-07-03T09:16Z
**Fetch time (page content, this run):** ~2026-07-03T09:17–09:20Z
**Baseline run:** 2026-07-02T09-15Z
**Sub-sitemaps fetched:** 34 / 34 (no failures)
**Total URLs (union):** 1386 (unchanged from prior run)

## Anomalies

None. All 6 lastmod changes are chronologically sane: each new `<lastmod>` is later than the prior recorded value and earlier than this run's fetch time (no future-dated claims, no backwards timestamp moves). No URLs added or removed, so no reappearance or migration checks were triggered. No sub-sitemap membership changes detected for any of the 1386 URLs.

## Significant Updates

### `/index/core-dump-epidemiology-data-infrastructure-bug/` — real copy-edit (typo fix)

Diffing the freshly fetched markdown against the prior git-committed snapshot shows exactly one substantive change, buried in an otherwise identical page:

- Old: "We turned to **Fermat** estimation."
- New: "We turned to **Fermi** estimation."

This is a factual correction, not a cosmetic touch: "Fermi estimation" (order-of-magnitude back-of-envelope reasoning, named for physicist Enrico Fermi) is the correct term in context — the surrounding math is estimating a race-condition probability from order-of-magnitude inputs, which is exactly what Fermi estimation means. "Fermat" (the 17th-century mathematician of Fermat's Last Theorem) doesn't fit the technique being described at all. Someone at OpenAI (or a reader) caught the homophone-adjacent typo and fixed it three days after publication (article dated June 30, lastmod now 2026-07-03T02:39:36Z).

### `/index/omio/` — recirculation widget rotated

The "Keep reading" panel at the bottom of the Omio customer story swapped which three articles it links to — it now surfaces "Inside Genebench-Pro" and "Introducing GeneBench-Pro" more prominently and drops the Rockset case study link. This is the same template-level cross-link refresh pattern documented in prior runs (e.g. 2026-07-01, 2026-06-29); no change to the Omio article's own body copy.

## Routine Updates (lastmod bump only, byte-identical content)

- `/business-data/` (old lastmod 2026-07-01T23:03:47Z → new 2026-07-02T18:42:56Z) — no content diff.
- `/business/` (old 2026-06-30T23:30:35Z → new 2026-07-03T09:12:14Z) — no content diff; this is the top-level Business landing page, timestamp bump only.
- `/index/genebench-pro/case-studies/` (old 2026-07-02T09:08:14Z → new 2026-07-02T22:57:25Z) — no content diff.
- `/index/introducing-genebench-pro/` (old 2026-07-02T09:08:27Z → new 2026-07-03T08:47:32Z) — no content diff.

## New Pages

None. 0 URLs added to the sitemap union this run.

## Removals

None. 0 URLs removed from the sitemap union this run.

## Summary

A quiet run: 0 added, 6 updated (4 pure timestamp bumps, 1 sidebar recirculation rotation, 1 genuine one-word typo fix), 0 removed, 0 anomalies. Total URL count holds steady at 1386 for the third consecutive run.
