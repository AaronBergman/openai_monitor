# Analysis — 2026-09-14T09-16Z

**Fetch time:** 2026-09-14T09:16Z–09:20Z UTC
**Baseline:** 2026-09-13T09-15Z (consecutive day)

## Method note

The root sitemap index (38 sub-sitemaps) was fetched and found byte-identical
to the prior `latest.xml` — no sections added, removed, or renamed. All 38
sub-sitemaps were fetched successfully (0 fetch errors, all valid XML). The
diff below compares the freshly fetched sub-sitemap union against the git
`HEAD` snapshot of `sitemaps/openai.com/sub/latest/*.xml` (i.e. yesterday's
run), **not** against `state/known_urls.json` — that file is a cumulative
historical record that retains entries for URLs removed months ago (their
`last_seen` simply stops advancing), so diffing against it directly would
produce a large false "removed" count. This is a pure diff-methodology note,
not a site anomaly.

## Anomalies

**None.** Checked all 1705 current URLs:
- No `<lastmod>` later than fetch time (future-dated), on either the 1 new
  URL or the 22 updated URLs.
- No `<lastmod>` moved backwards on any of the 22 updated URLs — all moved
  forward.
- The one new URL's `<lastmod>` (2026-09-14T09:01:19Z) is same-day as
  first_seen — no backdating.
- No URL disappeared and reappeared (0 removed this run; the new URL was not
  previously present in `state/known_urls.json` under any prior run).
- No section migrations — every common URL kept the same sub-sitemap
  membership as yesterday.

## New pages (1)

- **[How Fyxer built an AI executive assistant people trust](../../pages/openai.com/index/fyxer/index.md)**
  (`https://openai.com/index/fyxer/`, lastmod 2026-09-14T09:01:19Z) — a
  startup customer-story profile of Fyxer, an AI executive-assistant product
  for email. Notable: the in-page byline reads "August 13, 2026" — a full
  month before this page actually entered the sitemap — suggesting either a
  staged/delayed publish or a backdated editorial date; this is a display-date
  vs. technical-lastmod discrepancy, not a lastmod anomaly under the detection
  rules (lastmod itself is same-day as first_seen, so it isn't flagged above).
  Content: Fyxer runs ~30–50 specialized fine-tuned OpenAI models per email
  (reply-classification, intent-prediction, memory-retrieval, drafting),
  trained on 500k+ hours of human-executive-assistant workflow data plus a
  DPO self-training loop from user edits. Reports 53% of AI drafts accepted
  as-written, 90% 90-day user retention, and 2025 ARR growth from $1M to
  $32M. Fits the ongoing pattern of OpenAI publishing startup case studies
  as social proof for its fine-tuning/API platform (cf. Legora, Playco,
  Replit stories linked in its own "Keep reading" carousel).

## Updated pages (22 total; 0 with real content change)

All 22 pages that bumped `<lastmod>` were re-fetched and byte-diffed
(whitespace-insensitive) against their prior committed markdown. **21 of 22
had zero textual difference whatsoever** — pure CMS republish/lastmod
touches with no visible edit. The remaining one:

- **[`/business/partners/quantiphi/`](../../pages/openai.com/business/partners/quantiphi/index.md)**
  — the only page with any diff at all, and it is trivial: the partner-tier
  badge image URL's build/deploy query hash changed
  (`?dpl=dpl_A9S7ia9F893jG5rZXgoZ3i2uZZWt` → `?dpl=dpl_8pKzYyhdy2ueDi5axMU5KonAoX8y`),
  identical image, no visible or substantive change.

Full list of the 22 updated URLs (all republish-only):
`/business/contact-sales-financial-services/`, `/business/model/`,
`/business/partners/`, `/business/partners/gusto/`,
`/business/partners/hubspot/`, `/business/partners/quantiphi/`,
`/business/partners/quickbooks/`, `/business/partners/stripe/`,
`/business/pricing/`, `/business/solutions/data/`, `/chatgpt-work/`,
`/collective-cyberdefense/application/`, `/index/1password/`,
`/index/ai-native-company-workflows/`,
`/index/codex-quantum-computing-experiments/`,
`/index/gpt-6-astra-next-generation-work/`, `/index/gpt-6-astra/`,
`/index/paul-christiano-joins-openai-foundation-board/`,
`/index/teen-development-research-grants/`, `/index/two-blind-brothers/`,
`/new-york-times/`, `/products/release-notes/`.

Two of these (`/index/gpt-6-astra/`, `/index/paul-christiano-joins-openai-foundation-board/`)
looked newsworthy by name but confirmed as pure lastmod touches with no
content change on inspection — no new GPT-6 Astra announcement or board
news today, just a republish.

## Removed pages

None this run.

## Fetch failures

None — all 38 sub-sitemaps and all 23 page fetches (1 new + 22 updated)
succeeded on the first attempt via `tools/html_to_md.py`.

## Stats

- Total URLs: 1705
- Sub-sitemaps: 38
- Added: 1
- Updated: 22 (1 with real change, and that change was cosmetic)
- Removed: 0
- Anomalies: 0
- Fetch failures: 0
