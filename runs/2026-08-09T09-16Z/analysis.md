# Run 2026-08-09T09-16Z — analysis

**Fetch time:** 2026-08-09T09:16:19Z (sitemap + sub-sitemap pulls), 66 page fetches (0 added + 66 updated) completed by ~09:18Z.
**Baseline:** 2026-08-08T09-16Z (consecutive day)
**Stats:** 1,561 total URLs | +0 added | 66 updated (lastmod changed) | -0 removed | 0 anomalies | 35 sub-sitemaps

Of the 66 URLs with a changed `<lastmod>`, only 4 tracked files actually changed on disk after conversion to markdown; the remaining 62 had zero detectable content difference (pure `<lastmod>` bump from a redeploy — mostly `/business/partners/*` pages whose badge cache-buster parameter or template metadata isn't reflected in rendered markdown this run). 0 URLs are new; 0 removed.

## Anomalies

None of the defined categories triggered this run. Checked and clear:

- **Future-dated `<lastmod>`:** none. The newest `<lastmod>` across all 1,561 current URLs is `https://openai.com/form/enterprise-trusted-access-for-cyber/` at `2026-08-09T08:40:16.724Z`, ~36 minutes before this run's fetch (`2026-08-09T09:16:19Z`) — fresh, not future-dated. (That page had a lastmod bump but zero visible content change — see Fetch failures/Routine below.)
- **Backwards-moving `<lastmod>`:** none among the 66 updated URLs (verified both via the script's automated check and a manual string-compare pass).
- **Backdated new URLs:** N/A — 0 URLs added this run.
- **Reappeared URLs:** N/A — 0 URLs removed this run, so nothing to reappear.
- **Sub-sitemap migrations:** Investigated carefully because a naive diff of "which single sub-sitemap file contains URL X" flagged 119 apparent moves (e.g. 18 URLs appearing to leave `sitemap.xml_security.xml` for `safety`, `product`, `company`, `engineering`, `global-affairs`, `research`). This turned out to be a **false positive of the analysis method, not a real anomaly**: many URLs are cross-listed in *multiple* sub-sitemaps simultaneously in both the old and new snapshots (e.g. `/index/mixpanel-incident/` is listed in both `sitemap.xml_company.xml` and `sitemap.xml_security.xml` in both the 08-08 and 08-09 snapshots). A single-owner mapping built by iterating files in an arbitrary order silently picks whichever file was processed last, manufacturing spurious "migrations" between runs even when nothing changed. Redone as a proper per-URL *set*-membership comparison across all 35 sub-sitemap files for all 1,561 common URLs: **zero real membership changes**. Root sitemap index itself is also unchanged (same 35 sub-sitemap names, byte-identical). Recommend `tools/run_monitor.py` adopt set-membership (not single-file assignment) if this check is automated in the future, to avoid false alarms.

**Not a formal anomaly, but a continuing pattern flagged in the prior run:** the `/business/partners/*` nav-template flip-flop is still active and has now touched a third page.
- `pathfindr` and `statworx`, which flipped **old business nav → current sitewide nav** on 2026-08-08, flipped back to the **old business nav** today (2026-08-09) — a full round-trip in 24 hours.
- `capco` newly joined the flip: **sitewide nav → old business nav**, the same direction `cognita-reply` and `dentsu-japan` took on 08-08.
- All three diffs today are template-only (nav menu items and CTA text swap between "Why OpenAI / Solutions / Resources / Customers / Pricing / Contact sales" and "Research / Products / Business / Developers / Company / Foundation / Log in–Try ChatGPT"); no body content changed.
- This is now observed on at least 5 distinct partner pages across 2 consecutive days, flipping in both directions on different pages on the same day — consistent with flaky template caching, a CDN edge-cache race, or an in-progress A/B test on the partner-page builder, not deliberate content edits. Flagging again for continued tracking; worth checking in a future run whether these pages ever stabilize.

## Significant updates

None. No new posts, product announcements, pricing changes, or policy changes were detected today. The only pages with any visible diff at all were the 3 partner-nav-template flips (above) and one widget-rotation update:

- [`/index/circles/`](../../pages/openai.com/index/circles/index.md) — the "Keep reading" card rotation swapped out `/index/openai-and-apa-partner-to-advance-responsible-ai/` and `/index/how-the-world-is-putting-chatgpt-to-work/` for the previously-logged [`/index/responding-next-frontier-critical-cyber-capabilities/`](../../pages/openai.com/index/responding-next-frontier-critical-cyber-capabilities/index.md) (Astra critical-cyber disclosure, logged 2026-08-08) and the new [`/index/hsp-gruppe/`](../../pages/openai.com/index/hsp-gruppe/index.md) customer story (see New pages, below — this is the only genuinely new page-adjacent content surfaced today, though it wasn't in the Added set because it was already fetched/tracked as part of yesterday's or an earlier run's widget churn... actually confirmed: `/index/hsp-gruppe/` is NOT in today's `added` list, meaning it was already present in the baseline URL set; only its appearance in this widget rotation is new). No wording changes on the `/index/circles/` page itself otherwise.

## Routine updates

- **~58 `/business/partners/*` pages** refetched with a `<lastmod>` bump and **zero visible markdown diff** — the recurring partner-tier-badge image cache-busting pattern noted in every prior run, except this time the cache-buster values that changed didn't happen to be among the ones surfaced in the rendered markdown (or the change was purely to non-rendered metadata).
- **`products/release-notes/`** refetched — no new entries detected; content byte-identical to yesterday's snapshot.
- **`/education/`, `/business/solutions/education/`, `/business/solutions/finance/workflows/`, `/solutions/industries/healthcare/`, `/signals/`, `/signals/b2b/`, `/signals/data/`, `/signals/data-download/`, `/signals/research/`, `/economic-research-exchange/`, `/leads/small-business/`, `/form/enterprise-trusted-access-for-cyber/`** and several `/index/*` posts (`improving-gpt-5-6-sol-in-chatgpt`, `introducing-gpt-5-4-mini-and-nano`, `our-approach-to-the-model-spec`, `continuous-voice-interaction-with-gpt-live`, `introducing-the-openai-economic-research-exchange`, `openai-and-apa-partner-to-advance-responsible-ai`, `how-the-world-is-putting-chatgpt-to-work`, `parloa`, `third-party-cyber-evaluations-involving-openai-models`, `hsp-gruppe`) — all refetched with a `<lastmod>` bump and zero visible content diff. Likely template/build metadata (e.g. Contentful revalidation timestamps) not reflected in the rendered markdown.

## New pages

None this run.

## Removals

None this run.

## Fetch failures

None — all 66 targeted fetches (0 added + 66 updated) succeeded via `tools/html_to_md.py`.

## Tooling note

Re-verified `tools/run_monitor.py`'s sitemap fetch (fixed in the 08-08 run for the `curl_cffi` CA-bundle issue) works correctly; no fetch errors this run. Added a manual set-based sub-sitemap-membership cross-check this run (see Anomalies) after the script's simpler per-file diff produced a large false-positive migration list; the script itself was not modified, since the false positive was in ad hoc analysis, not in `run_monitor.py`'s own (correct, but migration-check-less) diff logic.
