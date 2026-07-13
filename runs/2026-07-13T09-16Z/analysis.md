# Analysis — run 2026-07-13T09-16Z

Fetch window: 2026-07-13T09:16Z – 2026-07-13T09:22Z (UTC).
Baseline: prior run 2026-07-12T09-16Z.

## Summary

Quiet run on the surface (0 URLs added, 0 removed, 25 lastmod bumps, 0 sitemap
migrations), but digging into the 25 "updated" pages surfaced the most
interesting anomaly of the week: a live, still-in-progress A/B test / canary
rollout on the `/business/` vertical, first flagged 2026-07-11, has both
**progressed** (a previously-minority nav variant is now dominant on two more
pages) and **revealed a brand-new, more substantial redesign variant** of the
`/business/` landing page itself that this run caught in a single fetch out
of eleven.

## Anomalies

### 1. `/business/` momentarily served a wholesale page redesign — not yet stable, caught once in ~11 fetches

During the scripted fetch of the 25 updated URLs, `https://openai.com/business/`
came back with a page that shares nothing with its previously known content
except the URL. To check whether this was a one-off render or the new steady
state, it was re-fetched **11 more times** in immediate succession:
**10 of 11 returned the old/known content; exactly 1 (the original scripted
fetch) returned the new redesign.** That's consistent with a very-low-percentage
canary or experiment bucket, not a completed rollout — flagging for continued
observation rather than reporting as "the business page changed."

What the rare variant looks like, for the record:
- Headline changes from **"Frontier intelligence everywhere you work"** /
  "Introducing ChatGPT Work" to **"Create, code, and innovate with OpenAI's
  tools and APIs"**, strapline "The next era of work is here."
- Restructures the page around two pillars — **"ChatGPT for Business"** and
  **"API Platform"** — replacing the ChatGPT-Work-centric hero of the current
  live page.
- Adds a new customer-logo strip/case-study section: **Notion, Zendesk,
  Booking.com, Estée Lauder** (linking to `/index/notion/`, `/index/zendesk/`,
  `/index/booking-com/`, `/index/estee-lauder/` — all pre-existing case-study
  pages, just newly surfaced here).
- Adds explicit **"Enterprise-grade data privacy, security, and admin
  controls"** and **"Guides and resources for integrating AI into your
  business"** sections, plus a Harvey customer quote.
- Nav nomenclature in this variant: `Research / Products / Business /
  Developers / Company / Foundation` (a third distinct nav, different from
  both variants tracked since 2026-07-11 — see below).
- Footer solutions list shortens from the current 8 items (Finance, Data
  analytics, Sales, Marketing, Operations, Engineering, Design, Security) to
  5 broader categories (Coding, Content Creation, Research, Agents, Data
  analysis).

This reads as a preview of an upcoming `/business/` redesign that broadens
the page's framing from "ChatGPT Work" specifically to "OpenAI's tools and
APIs" generally — plausibly to give the API Platform equal billing on the
business landing page. Worth checking again tomorrow to see if the
occurrence rate grows.

### 2. The 2026-07-11 business-nav A/B test has progressed: the "Why OpenAI" variant is now dominant, and has spread to two more pages

On 2026-07-11 this log first documented a live, cookieless A/B test splitting
traffic between two global-nav variants on business pages:
- **"Old" nav**: `Research / Business / Developers / Company` + `Log in` /
  `Try ChatGPT` (no promo banner)
- **"New" nav**: `Why OpenAI / Solutions / Resources / Customers / Pricing` +
  `Try OpenAI` / `Contact sales`, plus a **"New: Introducing ChatGPT Work"**
  promo banner linking to `/chatgpt-work/`

At the time, only 5 of 11 business pages showed the "new" variant, and the
note said this was "worth watching over the next few days to see whether the
new variant proportion grows."

Today's data supports that it is growing:
- `https://openai.com/business/solutions/data/` and
  `https://openai.com/business/solutions/design/` — both still on the "old"
  nav as of the 2026-07-12 baseline — now return the "Why OpenAI" +
  ChatGPT Work banner variant as their **dominant** response (2/3 and 3/3 in
  spot-checks respectively).
- `https://openai.com/business/` itself, already showing the "Why OpenAI"
  variant as of yesterday's baseline, continues to show it in 10/11 fetches
  today (the 11th being the new redesign in anomaly #1 above).
- Repeated fetching (8 consecutive requests) of `/business/` all returned the
  "Why OpenAI" variant, reinforcing that it is now the heavily-weighted
  default rather than a 50/50 split.

Net effect on the saved snapshots: `pages/openai.com/business/solutions/data/index.md`
and `.../solutions/design/index.md` are updated this run to reflect the now-
dominant variant (nav + ChatGPT Work banner added). `pages/openai.com/business/index.md`
is unchanged from yesterday (0-byte diff against the dominant variant).

These are the only three URLs among the 25 lastmod-bumped ones with any
actual content difference from their prior snapshot; see below.

## Updates: real content change

| URL | Nature of change |
|---|---|
| `/business/solutions/data/` | Nav variant converged to "Why OpenAI" + ChatGPT Work banner (see anomaly #2) |
| `/business/solutions/design/` | Same as above |
| `/business/` | No net change to saved snapshot (dominant variant matches prior); see anomaly #1 for the rare alternate variant caught once |

## Updates: lastmod bumped, zero content change (22 of 25)

The remaining 22 URLs with an updated `<lastmod>` came back **byte-identical**
to their previously saved markdown:

`/build-week/`, `/business-data/`, `/business/partners/dropbox/`,
`/business/solutions/finance/`, `/business/solutions/marketing/`,
`/business/solutions/sales/`, `/chatgpt-work/`, `/codex/`,
`/codex/get-started/`, `/form/share-your-story/`,
`/index/chatgpt-for-your-most-ambitious-work/`,
`/index/codex-flexible-pricing-for-teams/`,
`/index/codex-for-almost-everything/`,
`/index/codex-for-every-role-tool-workflow/`, `/index/devday-2026/`,
`/index/gpt-5-6-preferred-model-microsoft-365-copilot/`, `/index/gpt-5-6/`,
`/index/introducing-gpt-5-3-codex-spark/`, `/index/introducing-gpt-5-3-codex/`,
`/index/introducing-the-codex-app/`, `/index/previewing-gpt-5-6-sol/`,
`/index/separating-signal-from-noise-coding-evaluations/`

Most of these lastmods clustered tightly:
- The Codex/GPT-5.6 cluster (10 URLs) bumped within a ~20-minute window,
  07:53–08:11Z on 2026-07-13.
- The `/business/*` cluster (7 URLs, excluding the two real changes above)
  bumped within a ~3.5-hour window, 18:33–22:16Z on 2026-07-12.

Consistent with prior runs' observations (e.g. 2026-07-12), this pattern —
lastmod touched, content unchanged — matches a scheduled CMS/CDN rebuild or
cache revalidation rather than an editorial change.

## New pages

None. 0 URLs added to any sub-sitemap this run.

## Removals

None. 0 URLs removed from any sub-sitemap this run.

## Sitemap migrations

None detected — every URL present in both runs stayed in the same
sub-sitemap file.

## Fetch failures

None. All 25 fetches via `tools/html_to_md.py` succeeded (no Cloudflare
challenge pages, no undersized responses).

## Stats

- Total URLs in current snapshot: 1412
- Sub-sitemaps: 34
- Added: 0
- Removed: 0
- Updated (lastmod changed): 25
- Updated with real content change: 2 (`/business/solutions/data/`, `/business/solutions/design/`)
- Anomalies: 2 (rare `/business/` redesign variant; A/B nav test progression)
- Fetch failures: 0
