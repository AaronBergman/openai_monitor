# Analysis — Run 2026-08-14T09-19Z

**Fetch time:** 2026-08-14T09:19:59Z UTC
**Baseline:** 2026-08-13T09-16Z (consecutive day)
**Totals:** 1,582 total URLs (baseline 1,577) | +5 added | 343 updated | -0 removed | 35 sub-sitemaps | 0 fetch failures

## Anomalies

None triggered under this repo's defined checks:
- No `<lastmod>` later than fetch time (0 future-dated entries across all 1,582 current URLs).
- No `<lastmod>` moved backwards on any of the 343 updated URLs.
- No newly-added URL had a `<lastmod>` predating its `first_seen` by more than a few days (all 5 new URLs carry `<lastmod>` timestamps from within hours of this run).
- No URL reappeared after having been previously removed (checked all 5 added URLs against `state/known_urls.json`).
- No genuine sub-sitemap migrations. **Correction to detection methodology this run:** a same-value-per-URL diff (last-sub-sitemap-wins) falsely flagged 4 URLs (`how-countries-can-end-the-capability-overhang`, `understanding-ai-and-learning-outcomes`, `equipping-workers-with-insights-about-compensation`, `global-affairs/new-economic-analysis`) as "migrated" between `global-affairs` and `global-affairs-news-listed`. Direct inspection of both the current and git-HEAD-committed sub-sitemap XML shows all 4 URLs are — and have been — **cross-listed in both sub-sitemaps simultaneously**, not moved. This was likely misreported as a migration in the 2026-08-13 run's analysis for the same reason. Detection was rewritten this run to compare full sub-sitemap *membership sets* per URL rather than a single last-observed value; it found zero true migrations.

## Significant findings

### GPT-5.6 "Ultrafast mode" launch (headline story)
Three new pages, all published within hours of this run's fetch:
- [`/index/previewing-ultrafast/`](../../pages/openai.com/index/previewing-ultrafast/index.md) — "Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed." A new, faster inference tier for GPT-5.6 Sol.
- [`/form/ultrafast/`](../../pages/openai.com/form/ultrafast/index.md) — signup/waitlist form for Ultrafast mode access.
- [`/index/builders-guide-to-gpt-5-6/`](../../pages/openai.com/index/builders-guide-to-gpt-5-6/index.md) — a developer-facing guide to building with GPT-5.6.

The existing `/index/gpt-5-6/` and `/index/advancing-the-price-performance-frontier-with-gpt-5-6/` pages also picked up fresh `<lastmod>` timestamps today, but on inspection their body copy is unchanged — only their "related articles" widget rotated to point at the new Ultrafast announcement (routine, not counted as a substantive update).

### New Chief Revenue Officer
[`/index/dali-rajic-chief-revenue-officer/`](../../pages/openai.com/index/dali-rajic-chief-revenue-officer/index.md) — new page announcing Dali Rajic as OpenAI's Chief Revenue Officer, dated Aug 13.

### New IBM partner listing
[`/business/partners/ibm/`](../../pages/openai.com/business/partners/ibm/index.md) — new partner directory page; IBM's logo was added to the partner grid on [`/business/partners/`](../../pages/openai.com/business/partners/index.md) (confirmed present between HCLTech and Infosys in the current fetch, absent from the prior snapshot).

### Business section: two competing page designs confirmed live simultaneously
This repo has tracked a "nav flip-flop" anomaly since 2026-08-08 — pages alternating between an old-style header (`Why OpenAI / Solutions / Resources / Customers / Pricing`, "Try OpenAI" + "Contact sales") and a new-style header (`Research / Business / Developers / Company / Foundation`, "Log in" + "Try ChatGPT"). It recurred on 14 pages this run: `staying-ahead-in-the-age-of-ai`, `partners/altudo`, `partners/cognita-reply`, `partners/fellow-intelligence`, `partners/globant`, `partners/infosys`, `partners/kpmg`, `plugins/figma`, `plugins/klaviyo`, `plugins/microsoft-outlook-calendar`, `plugins/snowflake`, `solutions/cybersecurity`, `why-openai/startups`, `solutions/industries/government`.

**New evidence this run:** the `/business/` homepage itself flipped between the two variants, and it's not just the nav bar — the *entire* hero and page structure differs:
- Old variant: hero "Frontier intelligence everywhere you work," a customer-logo carousel (Cisco, Morgan Stanley, BNY, Moderna, Uber), and an "Introducing ChatGPT Work" callout.
- New variant: hero "The next era of work is here / Create, code, and innovate with OpenAI's tools and APIs," a two-column "ChatGPT for Business" / "API Platform" layout with a bulleted feature list.

This confirms the flip-flop is not a trivial nav-caching bug but genuinely **two full alternate page designs being served for the same URL** — most consistent with an in-progress redesign rollout or live A/B test at the edge (Cloudflare), not a content bug. Re-flagging under the existing tracked anomaly rather than as a new one since the underlying phenomenon (unversioned template variance) is the same; the scope just turned out to be broader than previously known.

### Global nav/mega-menu expansion (sitewide)
Across roughly 50 pages the primary navigation gained several new items simultaneously: a **"Supply Co."** link (`/supply/`, OpenAI's merchandise store — the store's product pages already existed in the sitemap, this is a new *nav* entry pointing to it), plus **"Customer Stories"**, **"Partner Network"**, **"GPT-5.6"**, and **"GPT-5.3 Instant"** entries added to submenus. This is consistent with — and likely part of — the same page-template rollout described above, rather than a separate event.

### Plugin directory data cleanup
Across roughly 40 `/business/plugins/<app>/` pages, the "Made by:" and "Website:" metadata fields were normalized to a consistent bare-domain / short-name format, e.g.:
- `Made by: Adobe Acrobat` → `Made by: Adobe`; `Made by: Asana, Inc.` → `Made by: Asana`; `Made by: Daloopa, Inc.` → `Made by: Daloopa`
- `Website: https://www.adobe.com/acrobat.html` → `Website: https://adobe.com`; `Website: https://www.hubspot.com/` → `Website: https://hubspot.com`
- One outlier looks like a data error rather than cleanup: [`/business/plugins/spaceship/`](../../pages/openai.com/business/plugins/spaceship/index.md) changed from `Made by: Spaceship, Inc` / `spaceship.com` to `Made by: Namecheap` / `namecheap.com` — Spaceship is a Namecheap-owned domain registrar, so this may be a legitimate rebrand-of-record rather than an error, but it's the one case where the "cleanup" changed the actual vendor name rather than just its formatting.

The [`/business/plugins/`](../../pages/openai.com/business/plugins/index.md) directory grid also gained one-line descriptions under each app card (e.g. "Salesforce — Review CRM records and update sales workflows"), and swapped GitLab Issues out for HubSpot in the featured row.

### Continuing rollout: "Joint partners" → "Program partners" relabel
18 more partner pages picked up the relabel first spotted 2026-08-13 (which converted 6 pages then): `blend360`, `booz-allen-hamilton`, `capco`, `cgi`, `cdw`, `deepsense-ai`, `dentsu-japan`, and others — section heading only, no change to the partner list itself.

### "Introducing ChatGPT Work" promo card rollout
New promo card appeared on [`/business/frontier/`](../../pages/openai.com/business/frontier/index.md), [`/business/partners/dropbox/`](../../pages/openai.com/business/partners/dropbox/index.md), and [`/solutions/industries/retail/`](../../pages/openai.com/solutions/industries/retail/index.md), among others — continuing the ChatGPT Work marketing push from the 2026-08-13 rebrand.

## Routine, low-signal updates

Of the 343 lastmod-updated URLs:
- **116** had zero non-widget textual difference — pure "related articles" card rotation (image + link swaps), no body-copy change.
- **42** had their only non-nav-menu, non-widget difference be one or more of the new global nav items (Supply Co. / GPT-5.6 / GPT-5.3 Instant / Customer Stories / Partner Network) — i.e., page body unchanged, only the shared nav template differs.
- **14** were the nav-variant flip-flop described above.
- **18** were the partner "Program partners" relabel.
- Remainder (~93 pages) were a mix of: the plugin metadata cleanup (~40 pages, above), minor template-order artifacts on older article pages where the date/title/share-button block re-renders in a different position without any text change (e.g. `introducing-openai-for-singapore`, `group-chats-in-chatgpt`, `introducing-indqa`, `safety-bug-bounty`, `taisei`, `indeed-maggie-hulce`) — likely the same underlying template-variance issue as the nav flip-flop, just manifesting lower on the page — and a handful of one-off cosmetic tweaks: `/business/solutions/data/` swapped its "Upcoming webinar" date from an already-past Aug 11 session to a new Sep 10 session; `/policies/sub-processor-list/` changed its subscribe-form link from an internal `/form/` path to an external HubSpot share link; `/products/release-notes/` reordered three already-known entries (Aug 5–7) with no new content added.

## New pages

- [`/index/previewing-ultrafast/`](../../pages/openai.com/index/previewing-ultrafast/index.md) — GPT-5.6 Sol Ultrafast mode announcement.
- [`/form/ultrafast/`](../../pages/openai.com/form/ultrafast/index.md) — Ultrafast mode signup form.
- [`/index/builders-guide-to-gpt-5-6/`](../../pages/openai.com/index/builders-guide-to-gpt-5-6/index.md) — developer guide for GPT-5.6.
- [`/index/dali-rajic-chief-revenue-officer/`](../../pages/openai.com/index/dali-rajic-chief-revenue-officer/index.md) — new CRO announcement.
- [`/business/partners/ibm/`](../../pages/openai.com/business/partners/ibm/index.md) — new IBM partner directory page.

## Removals

None this run.

## Fetch failures

None — all 348 added/updated URLs fetched and converted successfully.
