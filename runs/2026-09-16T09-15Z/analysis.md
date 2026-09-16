# openai.com sitemap monitor — analysis for run 2026-09-16T09-15Z

Fetch time (this run): 2026-09-16T09:15Z–09:23Z (UTC). Baseline: prior run `2026-09-15T09-16Z`.

Sitemap index: 38 sub-sitemaps (unchanged). Total unique URLs across all sections: 1,709 (up from 1,706).

Diff stats: **3 added, 367 lastmod-updated (168 with an actual content diff, 199 lastmod-only/no visible content change), 0 removed, 1 section migration, 0 timestamp anomalies, 0 fetch failures** (370/370 page fetches succeeded via curl-cffi Chrome impersonation).

This was a busier day than the recent stretch (which had been running 0–250 lastmod touches/day) — 367 URLs bumped `<lastmod>`, likely tied to a batch CMS re-render alongside three genuine additions.

## Anomalies

No future-dated or backwards-moving `<lastmod>` values were found anywhere in the 1,709-URL set, and none of the 3 new URLs previously existed in `state/known_urls.json` (i.e., none are reappearances). One **section migration** was detected:

- `https://openai.com/business/plugins/jam-dev/` moved from sub-sitemap `plugins-productivity` to `plugins-engineering-it`. Confirmed by content diff: the page's own "Use case" tag changed from **Productivity** to **Engineering & IT**. This is a deliberate recategorization by OpenAI, not a fetch glitch.

## Notable new page: undisclosed "Sponsored Agents" ad program (with HubSpot)

`/form/sponsored-agents-hubspot/` is a lead-capture form titled **"Register your interest in Sponsored Agents with HubSpot."** The page copy reveals a beta program OpenAI has not otherwise announced on the site:

> "Interested in testing Sponsored Agents for your business? ... Advertisers may need to meet eligibility criteria to participate in the beta, including creative automation, automatic bidding, and a minimum daily ad spend for 28 days."

The form also asks whether the registrant already has a **"ChatGPT Ads account."** This is the first sighting in this monitor's history of the phrase "ChatGPT Ads account" or "Sponsored Agents" anywhere on openai.com — it points to an in-development advertising/sponsored-placement product for ChatGPT agents, with HubSpot as a design partner, gated behind a minimum ad-spend threshold. No corresponding public product-announcement page exists yet in the sitemap.

## Significant updates

### Release notes: two new entries
`/products/release-notes/` gained two entries that push the existing changelog down:
1. **"Updated permissions for new Health connections"** (ChatGPT, GA, Sep 14, 2026): new Health plugin connections now default to the user's global Plugins permission setting (default "Allow low-risk actions" — ChatGPT can use connected Health data without asking each time, except for sensitive actions). OpenAI cites that "more than 70% of Health users already choose to allow ChatGPT to use data connected in Health without asking for permission each time" as the rationale.
2. **"Retiring automatic switching to Thinking in ChatGPT"** (ChatGPT, Sunset): OpenAI is retiring automatic switching from Instant to Thinking (reasoning) mode for ChatGPT Plus and Pro users globally, and removing the "Higher intelligence" setting from ChatGPT on the web for these plans. Users can still manually pick Thinking in the model picker; automatic switching for safety purposes is retained.

### New partner: EXL Service
`/business/partners/exl-service/` is a new partner profile page, and EXL Service was also added to the partner-logo grid on `/business/partners/` (confirmed via diff — same logo asset appears in two listings on that page). EXL is described as a global data-and-AI company (68,000+ employees, $2.24B trailing-12-month revenue, delivery centers on 6 continents) running an agentic platform ("EXLerate.ai") built on OpenAI models for insurers, banks, healthcare payers, and life-sciences firms; the page also notes EXL's 2026 acquisition of iMerit for data annotation, model evaluation, and red-teaming services to frontier AI labs.

### New gated report: Gartner Magic Quadrant
`/business/learn/gartner-2026-enterprise-ai-assistants-leader/` is a lead-gen landing page announcing OpenAI was named a **Leader in the 2026 Gartner® Magic Quadrant™ for Enterprise AI Assistants**, and ranked **#1 for Agentic Workflows Use Case** in the accompanying Critical Capabilities report (citing Gartner analysts Max Goss, Jason Wong, Olga Martí, Justin Tung, Cory Decker, dated September 2, 2026).

## Noise explaining most of the 168 real content diffs

1. **"Keep reading" / story-carousel reshuffle (~30+ pages).** Listing widgets on `/research/index/`, `/research/index/publication/`, `/news/research/`, and numerous `/index/*` customer-story and product-announcement pages reshuffled to surface already-known recent items (GPT-6 Astra, Fyxer, Paul Christiano board appointment, Navier–Stokes solution, GPT-Live-1, etc.). No new information beyond what these already-catalogued pages contain.
2. **Continuing plugin-directory UI rollout (~130 pages under `/business/plugins/*`).** The inline prompt-chip icon/link change first seen on ~40 plugin pages yesterday (2026-09-15) continued rolling out to the rest of the plugin directory today — chips are now clickable links to a pre-filled ChatGPT prompt, each with a small icon. Purely a UI/interaction polish, not new functionality or copy.
3. **Stale "GPT-6" footer-nav catch-up (~15 pages).** More pages (`introducing-codex`, `gpt-5-3-codex-system-card`, `research/index/conclusion`, `policies/health-privacy-policy`, and others) picked up the "GPT-6" link in the "Latest Advancements" footer that was added site-wide back on 2026-09-10/11 — still just re-render catch-up, not new.
4. **`/safety/` page reflow.** Three small category icons (Child Safety, Private Information, Deep Fakes) were dropped from an illustration row, and a static list of four older system-card links (o3/o4-mini System Card and its two addenda, GPT-4o image-gen addendum) was replaced by a "Load more" pagination control — the content is presumably still reachable via pagination, just no longer statically rendered. Combined with the routine GPT-6 footer-nav addition. Net effect: cosmetic/UI reflow, not a content removal.
5. **Testimonial-quote repositioning.** On a few Codex pages (e.g. `scaling-codex-to-enterprises-worldwide`, `introducing-upgrades-to-codex`), a customer pull-quote block that previously rendered inline within the article body now renders after the site footer instead — same exact quote text, just a different DOM position (a global/shared testimonial widget), not a content edit.

## New pages (3)

| URL | Category (inferred) |
|---|---|
| `/form/sponsored-agents-hubspot/` | Marketing/lead-gen — undisclosed ad program signup |
| `/business/partners/exl-service/` | Business partner profile |
| `/business/learn/gartner-2026-enterprise-ai-assistants-leader/` | Marketing/lead-gen — analyst report |

See "Significant updates" and "Notable new page" sections above for summaries.

## Routine updates (not itemized individually)

- 199 URLs had a `<lastmod>` bump with **no visible content diff** in the rendered markdown (re-render/build noise).
- ~130 `/business/plugins/*` pages continued the prompt-chip icon/link rollout described above.
- ~30 index/listing pages reshuffled "Keep reading" / research-listing widgets with no new information.
- ~15 pages picked up the already-known "GPT-6" footer-nav link.

## Removals

None.

## Fetch failures

None — all 370 added/updated URLs fetched successfully.
