# Run 2026-08-10T09-19Z Analysis

**Fetch time:** 2026-08-10T09:19:57Z
**Baseline:** 2026-08-09T09-16Z (consecutive day; `sitemaps/openai.com/latest.xml` + `sub/latest/` prior to this run)
**Stats:** 1,561 total URLs | 0 added | 83 updated | 0 removed | 0 anomalies | 35 sub-sitemaps

## Anomalies

None triggered. Checked and clear:

- **Future-dated `<lastmod>`:** none. Newest `<lastmod>` among all 1,561 current URLs is well before the 09:19:57Z fetch time.
- **Backwards-moving `<lastmod>`:** none among the 83 updated URLs — every new `<lastmod>` is later than its prior value.
- **Backdated new URLs:** not applicable — 0 URLs added this run.
- **Reappeared URLs:** not applicable — 0 URLs removed this run, so nothing to reappear.
- **Sub-sitemap migrations:** none detected — no URL moved from one sub-sitemap file to another between this run and the prior baseline.

**Continuing pattern, not a new anomaly — nav-template flip-flop:** first flagged 2026-08-08, still active on 2026-08-10 with a new set of affected pages. `cognizant`, `infosys`, `samsung-sds`, and `tredence` (all `/business/partners/<slug>/`) flipped from the older business-specific nav ("Why OpenAI / Products / Solutions / Resources / Customers / Pricing") to the current sitewide nav ("Research / Products / Business / Developers / Company / Foundation"). This is the identical template swap logged on 2026-08-08 (pathfindr, statworx, cognita-reply, dentsu-japan) and 2026-08-09 (capco, pathfindr, statworx flipping back). Today's four pages are a new batch — none of yesterday's flippers (capco, pathfindr, statworx) moved again today; they were stable. Consistent with flaky template caching or an in-progress A/B test on the partner-page builder, not deliberate content edits.

## Updated pages with real (markdown-visible) content changes

Verified via `git diff` against the committed HEAD version of each page (not just `<lastmod>`), 5 of 83 updated URLs actually changed body content:

### `/business/partners/cognizant/`, `/business/partners/infosys/`, `/business/partners/samsung-sds/`, `/business/partners/tredence/`
- Nav template flip old→sitewide (see Anomalies above). No other content change beyond the nav block and the partner-tier badge cache-buster hash (same as the routine-noise pages below).

### `/index/gpt-5-6-frontier-intelligence-efficiency/`
- lastmod: `2026-08-04T21:36:27.601Z` → `2026-08-09T13:32:02.805Z`
- The "related articles" carousel at the bottom of the piece rotated: `openai-and-apa-partner-to-advance-responsible-ai` (Aug 6, APA/youth-safety partnership) and `how-the-world-is-putting-chatgpt-to-work` (Aug 6, ChatGPT usage report) now appear, displacing `continuous-voice-interaction-with-gpt-live` and `building-abundant-intelligence`. `apple-is-getting-this-wrong` stayed in the rotation. Pure related-content propagation as newer posts get folded into the widget — not a change to the article itself.

## Routine, zero-content-change updates (78 of 83)

- **~57 `/business/partners/*` pages** — partner-tier-badge cache-busting query parameter refresh only (`?dpl=dpl_...` hash changes on the badge SVG), no body-text change. Standard daily churn in this section, consistent with every prior run.
- **~13 `/index/*` article pages** — `chatgpt-for-academic-researchers`, `hsp-gruppe`, `ten-advances-in-mathematics`, `third-party-cyber-evaluations-involving-openai-models`, `responding-next-frontier-critical-cyber-capabilities`, `improving-gpt-5-6-sol-in-chatgpt`, `introducing-the-openai-economic-research-exchange`, `advancing-responsible-ai-across-europe`, `building-abundant-intelligence`, `continuous-voice-interaction-with-gpt-live`, `openai-and-apa-partner-to-advance-responsible-ai`, `how-the-world-is-putting-chatgpt-to-work` — `<lastmod>` bumped with **zero detectable markdown-visible change** (confirmed via `git diff`: no working-tree changes for these files after refetch).
- **Other pages with a `<lastmod>`-only bump:** `/business/partners/` (index), `products/release-notes/`, `education/`, `leads/small-business/`, `business/solutions/education/`, `business/solutions/finance/workflows/`, `form/enterprise-trusted-access-for-cyber/`, `science/`, `solutions/industries/healthcare/`, `signals/data/`.

## New Pages

None (0 added).

## Removed Pages

None (0 removed).

## Fetch Failures

None. All 83 pages fetched successfully via `tools/html_to_md.py` (curl-cffi, Chrome impersonation).
