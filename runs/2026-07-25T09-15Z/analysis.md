# Run 2026-07-25T09-15Z — Analysis

- Fetch time (sitemap + sub-sitemaps): 2026-07-25 ~09:16–09:18 UTC
- Baseline: 2026-07-24T09-16Z (previous run, consecutive day)
- Total URLs in current snapshot: 1484 (baseline: 1472)
- Sub-sitemaps: 34/34 fetched successfully (200 OK, no parse errors)
- Page fetches attempted: 412 (14 new + 398 updated) — 412/412 succeeded, 0 blocked/failed

## Anomalies

**No timestamp-integrity violations** (checked and clear):
- No `<lastmod>` later than fetch time.
- No `<lastmod>` moved backwards vs. the prior snapshot (checked programmatically across all 398 updates — zero instances).
- No new URL backdated (lastmod predating first_seen by more than a few days) — the 14 new URLs all have lastmods within ~1 day of first_seen.
- No URL reappeared after previously disappearing — both removals this run are confirmed first-time removals in `state/known_urls.json`.

**But one large structural anomaly: 122 URLs migrated between sitemap sections in a single run.** This is far above the normal handful-per-week rate and reads as a deliberate CMS taxonomy reorganization, not drift:

| From (top sources) | Count | → | To (top destinations) | Count |
|---|---|---|---|---|
| `company` | 57 | | `global-affairs` | 34 |
| `product` | 34 | | `release` | 30 |
| `api` | 9 | | `security` | 18 |
| `safety` | 7 | | `product` | 11 |
| `global-affairs` | 5 | | `learn-openai-on-openai` | 6 |
| `conclusion` | 4 | | `research` | 6 |
| `engineering` | 2 | | `webinar` | 5 |
| `brand-stories-sora` | 2 | | `global-affairs-news-listed` | 4 |

Reading the from/to pairs together, this looks like OpenAI broke its old catch-all `company` bucket (and, to a lesser extent, `product`) into more specific verticals:
- Policy/economic/government posts (national economic "blueprints," Stargate site announcements, Senate testimony, nonprofit-commission material) moved `company` → `global-affairs`.
- Product-launch announcements (GPT‑5.x family, Codex, o3/o4-mini, image/audio model launches) moved `product`/`company` → the new `release` type.
- Security-flavored posts previously scattered across `safety`, `product`, and `company` (Aardvark, the Hugging Face incident writeup, Codex sandboxing, cyber-defense/trusted-access posts, the Tanstack npm supply-chain response) consolidated into a new `security` type.
- Internal "OpenAI on OpenAI" dogfooding case studies moved `api` → `learn-openai-on-openai`.
- A `global-affairs-news-listed` subtype was carved out of `global-affairs` (looks like a "news roundup" vs. "long-form position" split).

This is a backend taxonomy change, not new or deleted content — every migrated URL still resolves to the same page. Filed here per the routine's explicit instruction to flag sub-sitemap migrations, and because of its unusual scale.

**Related, not independently anomalous:** the migration event coincides with a mass `<lastmod>` bump — 299 of the 398 updates cluster in the single 07:00–07:45 UTC hour today (see histogram below), plus a separate 72-page cluster at 16:00–17:00 UTC *yesterday* (2026-07-24, first visible in this run because it postdates yesterday's 09:17 UTC fetch). Both clusters carry legitimate, monotonically-increasing lastmods (no future or backdated values), so they don't trip the strict anomaly rules — but the scale (⅓ of the entire crawled site touched in a 45-minute window) is far outside normal daily variance and is best explained as one coordinated frontend/CMS redeploy. See "What actually changed" below for what a content diff sample showed this redeploy did.

```
Updated-page lastmod-hour histogram (UTC):
2026-07-24 13:00   3
2026-07-24 15:00   2
2026-07-24 16:00  72   <- business/plugins/* catalog refresh
2026-07-24 18:00   1
2026-07-24 19:00   1
2026-07-24 20:00   1
2026-07-24 23:00   1
2026-07-25 00:00   2
2026-07-25 06:00   9
2026-07-25 07:00 299   <- sitewide template/taxonomy redeploy
2026-07-25 08:00   6
2026-07-25 09:00   1
```

## What actually changed (content diff, not just lastmod)

Of the 398 URLs whose `<lastmod>` changed, 374 had a byte-level content diff and 24 were byte-identical to the prior snapshot (pure re-touch, no visible change — see Routine updates). A diff-size-ranked sample of the 374 (filtering out known nav/footer boilerplate lines) shows the *large majority* of the diffs are non-substantive, falling into four repeating buckets:

1. **Smart-quote/apostrophe normalization** — e.g. `'re` → `’re`, `'s` → `’s` — scattered through body copy on dozens of otherwise-static historical pages (`/index/ada/`, `/index/o1/`, etc.) with no other change.
2. **Heading-level and table-of-contents markup shifts** — e.g. `/index/openai-anthropic-safety-evaluation/` had every `####` become `###` and its TOC/date/title block duplicated once (the rendered content is identical, just the HTML structure feeding our markdown converter changed).
3. **Section-nav correction** — several `/business/guides-and-resources/*` and `/business/solutions/*` pages that were previously rendering with the generic sitewide top nav now correctly render the Business-section subnav (Why OpenAI / Products / Solutions / Resources / Customers / Pricing) and picked up their hero header for the first time in our snapshots (e.g. `/business/guides-and-resources/inside-gpt5-our-best-model-for-work/`). Reads like a template-assignment bug fix, not a content edit.
4. **Nav/footer propagation** (continuing the rollout first spotted 2026-07-23/24): "GPT‑5.6" in the Products flyout, "Customer Stories"/"Partner Network" in the Business footer column, "Supply Co." in the global footer — now reaching effectively every remaining page that hadn't picked it up yet, which is why this run's update count is 8x a normal day.
5. **Carousel/"Keep reading" rotation** — routine content recirculation reflecting new posts, as on every publish day.

Given the volume, this run did **not** manually diff all 374 pages line-by-line; a representative sample (the 40 largest post-noise-filtered diffs, plus all 14 new pages and the two most-migrated categories) was reviewed in depth. The following are the genuine, substantive changes found:

### 1. New API product: "Reserved Tier" launches, Scale Tier frozen to pre-GPT‑5.6 models

- **New page:** [`/api-reserved-tier/`](../../pages/openai.com/api-reserved-tier/index.md) — a new Enterprise-only capacity product. Customers pre-purchase provisioned throughput denominated in **dollars per minute** for a specific model (not tokens/minute like the old Scale Tier), usable flexibly across Standard/Priority processing, context lengths, and regions; overage bills at normal pay-as-you-go rates. Sales-contact only, no self-serve signup.
- **[`/api-scale-tier/`](../../pages/openai.com/api-scale-tier/index.md) updated** to reflect the split: a new banner states *"Scale Tier is available on models released before GPT‑5.6. For GPT‑5.6 and future model releases, see Reserved Tier."* Several other Scale Tier mechanics changed at the same time:
  - Top-tier minimum throughput raised from 50 to **100 tokens/second**.
  - Capacity management moved from a separate developer-console purchase flow to **Organization Settings → Capacity Management**; enabling Scale Tier on a project is now a **toggle in Project Settings** ("Scale Tier Enabled") rather than the old opt-in mechanism.
  - Billing changed from separate monthly-arrears invoicing to being **folded into the standard OpenAI bill**.
  - New **overage/"spillover" behavior**: for customers with Scale Tier purchases active before July 21, 2026, over-limit usage bills at Standard (not Priority) pay-as-you-go rates unless they contact sales to opt into the new behavior — a grandfather clause tied to an exact date, suggesting a billing-mechanics change took effect July 21.

This is the one clearly deliberate, customer-facing product/pricing change in today's run, independent of the redeploy noise above.

### 2. `/business/plugins/*` catalog: "ChatGPT Work" banner fully removed (batch of ~72 pages, dated yesterday 2026-07-24 ~16:30 UTC)

Every page under `/business/plugins/` (Notion, Slack, Salesforce, GitHub, Figma, Snowflake, etc. — the full third-party integrations directory) dropped the "New — Introducing ChatGPT Work" promo banner that had been present since ChatGPT Work's launch, with no replacement CTA, and picked up the "Supply Co." footer link. This completes the wind-down documented partially in the 2026-07-22 through 2026-07-24 runs (banner removed piecemeal from `/business/learn/`, solutions pages, etc.) — it's now gone from the entire plugins catalog in one batch.

### 3. 13 new partner-directory listings

New pages under `/business/partners/`: **Blank Metal, Blend360, Cloudwerx, Corca, Fujitsu, Globant, Insurgence, Merantix Momentum, Nablon AI, Rosetree Solutions, Snorkel AI, Tredence, ZS.** Standard partner-locator template (About blurb, website link, "Back to OpenAI Partner Locator"). Fujitsu is the only large, widely-recognized enterprise name in this batch (Japanese IT/digital-transformation conglomerate, ~100,000 employees, reports ¥3.5T FY revenue on its own page). Minor content-quality note: the Blank Metal listing has one visibly mis-encoded em dash (renders as `‚Äî`, a UTF-8/Latin-1 mojibake artifact) in its About paragraph — isolated to that one new page, not present on any other partner page (old or new), so it's a copy-paste/encoding slip on that specific listing rather than a systemic issue.

### 4. Two removals

- `/business/plugins/gitlab-issues/` (GitLab Issues plugin listing, first seen 2026-07-10) — removed from the plugins catalog the same day the rest of the catalog got its banner-removal refresh (#2 above). Possibly deprecated/consolidated into a broader GitLab integration listing; no replacement URL found in the diff.
- `/form/partnerintake/` (a partner-intake lead form, present since bootstrap/2026-05-07) — removed with no obvious replacement in this snapshot.

## Routine updates (lastmod bumped, byte-identical content)

24 URLs re-touched `lastmod` with no visible content change: `/api/pricing/`, `/business/openai-presence/`, `/business/partners/locator/`, `/business/pricing/`, `/chatgpt-work/`, `/form/copyright-disputes/`, `/form/hackathon-support/`, `/form/trademark-counterfeit-disputes/`, `/form/showcase-submission/`, `/global-affairs/disrupting-malicious-uses-of-ai/`, `/index/advancing-the-next-era-of-national-science/`, `/index/building-ai-infrastructure-with-the-effingham-county-community/`, `/index/health-in-chatgpt/`, `/index/how-news-organizations-are-using-ai/`, `/index/how-confessions-can-keep-language-models-honest/`, `/index/launchdarkly-claire-vo/`, `/index/ntt-data/`, `/index/openai-scholars/`, `/index/safety-alignment-long-horizon-models/`, `/index/unlocking-self-improvement-gpt-red/`, `/podcast/`, `/policies/chatgpt-sites-terms/`, `/products/release-notes/`, `/signals/research/`. Backend cache-invalidation / republish noise, no visible change.

## New pages (14)

1. [`/api-reserved-tier/`](../../pages/openai.com/api-reserved-tier/index.md) — see item 1 above.
2–14. The 13 partner listings under `/business/partners/` — see item 3 above: [blank-metal](../../pages/openai.com/business/partners/blank-metal/index.md), [blend360](../../pages/openai.com/business/partners/blend360/index.md), [cloudwerx](../../pages/openai.com/business/partners/cloudwerx/index.md), [corca](../../pages/openai.com/business/partners/corca/index.md), [fujitsu](../../pages/openai.com/business/partners/fujitsu/index.md), [globant](../../pages/openai.com/business/partners/globant/index.md), [insurgence](../../pages/openai.com/business/partners/insurgence/index.md), [merantix-momentum](../../pages/openai.com/business/partners/merantix-momentum/index.md), [nablon-ai](../../pages/openai.com/business/partners/nablon-ai/index.md), [rosetree-solutions](../../pages/openai.com/business/partners/rosetree-solutions/index.md), [snorkel-ai](../../pages/openai.com/business/partners/snorkel-ai/index.md), [tredence](../../pages/openai.com/business/partners/tredence/index.md), [zs](../../pages/openai.com/business/partners/zs/index.md).

## Removals (2)

- `/business/plugins/gitlab-issues/` — see item 4 above. Last snapshot: `git log -- pages/openai.com/business/plugins/gitlab-issues/index.md`.
- `/form/partnerintake/` — see item 4 above. Last snapshot: `git log -- pages/openai.com/form/partnerintake/index.md`.

## Fetch failures

None. All 412 fetches (14 new + 398 updated) succeeded and passed the block-detection sanity check.
