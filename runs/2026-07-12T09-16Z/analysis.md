# Run 2026-07-12T09-16Z — Analysis

**Fetch time:** 2026-07-12T09:16:30Z
**Baseline:** 2026-07-11T09-15Z
**Totals:** 1412 URLs (1412 baseline → 1412 current) | 0 added | 24 updated (1 with visible content change) | 0 removed | 34 sub-sitemaps | 0 fetch failures

The quietest run since monitoring began. No new pages, no removals, no future-dated or backwards-dated lastmods, and no reappearing URLs. Of 24 pages with a bumped `<lastmod>`, only one — `/live/` — actually changed visible content.

## Anomalies

None new this run. One item worth a correction to the running record:

### Correction: the "global-affairs sub-sitemap migration" was never a migration

Runs on 2026-07-09 and 2026-07-10 (and repeated in the 2026-07-10 README entry) flagged the same 4 URLs as having "migrated" from `sitemap.xml/global-affairs/` to `sitemap.xml/global-affairs-news-listed/`:

- `https://openai.com/index/equipping-workers-with-insights-about-compensation/`
- `https://openai.com/index/understanding-ai-and-learning-outcomes/`
- `https://openai.com/index/how-countries-can-end-the-capability-overhang/`
- `https://openai.com/global-affairs/new-economic-analysis/`

This run's diff logic initially flagged the same 4 URLs again. Investigating properly (grepping both raw sub-sitemap XML files, both in today's fresh fetch and in the prior commit via `git show HEAD:...`) shows **all 4 URLs are present in both sub-sitemaps simultaneously**, every day, including today and yesterday's committed snapshot. This is a **persistent duplicate cross-listing**, not a migration in either direction — `sitemap.xml/global-affairs-news-listed/` is a small (4-URL) subset that is always also cross-listed in the much larger `sitemap.xml/global-affairs/` (141 URLs). `state/known_urls.json` already stores `sub_sitemaps` as a list per URL and has correctly recorded both sub-sitemaps for these 4 URLs for some time — the error was in the day-to-day diff scripts (apparently rewritten from scratch most days — see the pile of one-off `run_*.py` scripts at the repo root), which used a `url -> single sub-sitemap` map that silently overwrote itself when a URL appeared twice in the same sitemap-index pass, depending on file-processing order. Retracting the "migration" characterization from prior days' logs; this condition is stable and has probably existed since the URLs were first indexed.

## Notable updates

- **[Live page](../../pages/openai.com/live/index.md)** (`/live/`) — the only page with a real content diff this run. The "This is the new ChatGPT Voice, powered by GPT-Live" replay entry (originally posted July 8) had its embedded YouTube link swapped from `EAN5Cj347PY` to `9f-Ew_lDtxc`. No other text changed. Reads as a housekeeping fix — likely the original video was unlisted/replaced with a corrected upload — not a new livestream.

## Routine updates (no visible content change)

23 of the 24 "updated" pages carry a bumped `<lastmod>` but are byte-identical to yesterday's saved markdown. Roughly ten of them cluster tightly between 09:00:20Z and 09:07:00Z this morning — right before this run's own fetch — and are all pre-existing pages from the Codex / GPT-5.6 launch family:

`/index/separating-signal-from-noise-coding-evaluations/`, `/codex/`, `/codex/get-started/`, `/index/codex-flexible-pricing-for-teams/`, `/index/codex-for-almost-everything/`, `/index/introducing-gpt-5-3-codex-spark/`, `/index/introducing-gpt-5-3-codex/`, `/index/devday-2026/`, `/index/introducing-the-codex-app/`, `/chatgpt-work/`, `/index/gpt-5-6/`.

All of these were already indexed as far back as 2026-05-07 or 2026-06-03 (per `state/known_urls.json` `first_seen`) — none are new. This reads as a scheduled site-wide rebuild/redeploy touching the whole Codex/GPT-5.6 content cluster's lastmod without changing any extractable content — plausibly a build-ID bump, a CDN cache purge, or an internal metadata change not reflected in the rendered markdown.

The remaining routine updates are scattered through the prior 24 hours with no discernible batching:
`/academy/codex-for-work/how-data-science-teams-use-codex/`, `/academy/codex-for-work/how-sales-teams-use-codex/`, `/build-week/`, `/business/chatgpt-pricing/`, `/business/partners/dropbox/`, `/business/plugins/`, `/business/pricing/`, `/form/share-your-story/`, `/index/chatgpt-for-your-most-ambitious-work/`, `/index/codex-for-every-role-tool-workflow/`, `/index/gpt-5-6-preferred-model-microsoft-365-copilot/`, `/policies/chatgpt-sites-terms/` — all byte-identical to their prior saved markdown.

## New pages

None this run.

## Removals

None this run.

## Fetch failures

None — all 24 updated URLs fetched cleanly via `tools/html_to_md.py` (curl-cffi/Chrome impersonation), none hit the Cloudflare challenge page.
