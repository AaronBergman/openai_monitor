# Run analysis — 2026-07-29T09-16Z

**Fetch time (UTC):** 2026-07-29T09:17:36Z
**Baseline:** 2026-07-28T09-16Z
**Total URLs:** 1,483 (was 1,485) | **Added:** 2 | **Removed:** 4 | **Updated (lastmod changed):** 98 | **Anomalies:** 0 | **Sub-sitemaps:** 34/34 fetched OK | **Fetch failures:** 0

## Anomalies

None. Checked for: future-dated `<lastmod>` (none — the latest lastmod observed, `student-collective/` at 09:17:10Z, is still ~26s before our 09:17:36Z fetch), backwards-moving `<lastmod>` vs the immediately prior snapshot (none among the 98 updates), reappearing URLs (none of the 4 removed URLs show a prior removal/reappearance cycle in `state/known_urls.json`), and backdated new URLs (both new URLs carry same-day `<lastmod>` values, consistent with genuine same-day publication).

## No sitemap taxonomy migrations (false-positive check)

A first-pass "last-file-wins" comparison flagged 4 Global Affairs URLs (`/global-affairs/new-economic-analysis/`, `/index/equipping-workers-with-insights-about-compensation/`, `/index/how-countries-can-end-the-capability-overhang/`, `/index/understanding-ai-and-learning-outcomes/`) as migrating from `sitemap.xml/global-affairs/` to `sitemap.xml/global-affairs-news-listed/`. A direct grep of both raw sub-sitemap files (today's and yesterday's) shows all 4 URLs are cross-listed in **both** sections in **both** snapshots — same false positive documented in the 2026-07-27 run. No actual migration occurred.

## Significant updates

### Brazil privacy policy synced to current ad-personalization terms + legal cleanup
[`/policies/br-privacy-policy/`](../../pages/openai.com/policies/br-privacy-policy/index.md) — `lastmod` jumped from April 30, 2026 to July 28, 2026 in a substantial rewrite (69% line-similarity to the prior snapshot, the single largest content diff of the run):
- Adds the same "Free and Go" ad-personalization language that the main US Privacy Policy picked up back on 2026-05-18: OpenAI now says it may collect "ads history and interests" for Free/Go-tier ChatGPT users, receive data from "advertisers and other data partners," and use it "to personalize the ads you see on our Services." An opt-out control is described in account settings. This is not a new feature being announced today — it's the Brazil-localized policy catching up to language the flagship policy already had — but it confirms the ads-in-ChatGPT rollout (Free/Go tiers) is being extended to Brazil's legal terms.
- **Removes an entire mis-included section**: a verbatim "9. Additional U.S. state disclosures" section (California-style CCPA/CPRA rights language — opt-out of "sale/sharing," authorized-agent requests, appeals process) had been sitting in the Brazil policy for no evident reason. It's gone in this version — looks like a copy-paste artifact from the US policy that's now been cleaned up, with sections renumbered accordingly (9→ "Changes to the privacy policy", 10→ "Data controller", etc.)
- Drops references to product surfaces that don't apply to this policy's scope (Atlas browser incognito history, Sora character/video sharing).
- Minor: footer nav picked up the "Supply Co." link (see below).

### New Partner Network story: Accenture × Radisson
[`/business/partners/`](../../pages/openai.com/business/partners/index.md) gained an 8th "partner story" card (was 7): a new pull-quote from Radisson Hotel Group's Chief Commercial Officer describing an Accenture-built OpenAI integration for hotel discovery/booking ("meeting guests in the planning moment ... to find, compare, and book Radisson Hotels properties"). Separately, the "Become a partner" CTA now points to an external `partners.openai.com` portal rather than the (now-removed, see below) on-site interest form.

### New live webinar promo on the Sales solutions page
[`/business/solutions/sales/`](../../pages/openai.com/business/solutions/sales/index.md) added a banner for a "[Live webinar] Join us July 30, 2026 at 9:30 AM PT" session on how OpenAI's own Sales team uses "ChatGPT Work" as an account-context command center, with a registration link. (Minor: "Hubspot" plugin link corrected to "HubSpot".)

## Routine — sitewide nav/footer template sync (~50 pages, no body-text changes)

The remaining ~90 of the 98 lastmod-updates are metadata/template touches with **zero substantive body-text change**, verified by diffing stripped (image-URL-normalized, blank-line-removed) markdown:

- **8 pages are pure image-asset re-uploads** (same alt text, new CDN asset hash — e.g. a cache-busting re-encode) with literally 0 changed text lines: `hackathon-follow-up`, `machine-learning-unconference`, `learning-day`, `openai-five-benchmark`, `procgen-minerl-competitions`, `symposium-2019`, `spinning-up-in-deep-rl-workshop-review`, `why-teens-deserve-access-safe-ai`.
- **~40 older article/customer-story pages** (spanning `chatgpt-can-now-see-hear-and-speak` from 2023 through 2026 safety/teen-safety posts) show only two kinds of change, confirmed by manual diff on a representative sample (`our-commitment-to-community-safety`, `building-towards-age-prediction`, `netomi`, `solutions/industries/healthcare`, `index/chatgpt-can-now-see-hear-and-speak`):
  1. **Footer/nav sync** — these pages' cached templates were stale; they now match the current site nav: "Supply Co." added under content links, "GPT-5.6" added to the model list (displacing older "GPT-5.3 Instant"/"GPT-5.3-Codex" entries), "Customer Stories" + "Partner Network" added under Business, "Deployment Safety" added under Safety, and `/business/apps/` renamed to `/business/plugins/`.
  2. **"Keep reading" / related-articles carousel rotation** — the 2-4 related-article cards at the bottom of each page were swapped to feature the newest July 20-28 articles (Health in ChatGPT, OpenAI Presence, Safety and alignment in an era of long-horizon models, Scientific computing in the age of agentic AI, How AI is expanding what people do at work).
  3. No article body prose changed on any sampled page.
- The `/news/`, `/news/global-affairs/`, `/news/product-releases/`, `/news/security/`, `/news/safety-alignment/` index/hub pages updated their card carousels for the same reason — expected, routine, driven by the new `scientific-computing-agentic-ai` publication landing today.
- `business/customer-stories/`, `business/openai-presence/`, `devday/`, `products/release-notes/`, several `/form/*` pages, and a batch of policy/index pages show the same nav-sync-only pattern.

No further write-up per page; all 98 updated URLs and their old/new `lastmod` are in `diff.json`.

## New pages (2)

- **[OpenAI Student Collective](../../pages/openai.com/student-collective/index.md)** (`/student-collective/`) — replaces the old campus-outreach interest form (see Removals) with a full program page. Recruits undergraduate "Campus Leads" (pairs, per-campus) to run AI workshops and "Studio Hours" project sessions; applications open through August 10, 2026. Reads as a rebrand/expansion of OpenAI's campus-ambassador efforts into a more structured, named program.
- **[Scientific computing in the age of agentic AI](../../pages/openai.com/index/scientific-computing-agentic-ai/index.md)** (`/index/scientific-computing-agentic-ai/`) — a Research/Publication field report (PDF linked) on scientists using coding agents (e.g. Codex-style tools) to modernize legacy scientific software in genomics and other data-rich fields; covers case studies, recurring themes, and the case for long-term stewardship of the resulting code. Fits the ongoing "agentic coding for non-developers" narrative alongside recent Codex-adoption pieces.

## Removals (4)

- **`/form/openai-campus-leaders-interest-form/`** — superseded by the new `/student-collective/` program page above.
- **`/form/partner-network-interest/`** — the Partner Network's on-site interest form is gone; `/business/partners/`'s "Become a partner" CTA now routes to the external `partners.openai.com` portal instead.
- **`/index/chatgpt-plugins/`** and **`/waitlist/plugins/`** — legacy ChatGPT Plugins pages (plugins were deprecated well over a year ago); this looks like overdue sitemap cleanup rather than new news.

## Fetch failures

None. All 34 sub-sitemaps and all 100 added/updated pages fetched successfully via `tools/html_to_md.py`.
