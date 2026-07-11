# Run analysis — 2026-07-11T09-15Z

Fetch time (UTC, observed by this run): **2026-07-11T09:16:52Z**
Baseline: 2026-07-10T09-16Z run
Sub-sitemaps: 34/34 fetched successfully. Pages fetched/converted: 89/89 succeeded (0 fetch failures, 0 blocked).

Totals: 1 added, 88 updated, 0 removed, 2 anomalies.

## Anomalies

### 1. `/form/codex-app/` reappeared after yesterday's removal
This URL was one of the 69 URLs that dropped out of the sitemap in the 2026-07-10T09-16Z run. It is back today, listed under the `page` sub-sitemap with `lastmod = 2026-07-09T17:08:59.066Z` — a timestamp that is *earlier* than the run that detected its removal. The page content itself (a "Sign up for the Codex app" waitlist form, scoped to Linux) is unchanged from its last known-good snapshot. Most likely explanation: a transient sitemap-generation glitch rather than a real edit — the page was probably never actually taken down, just briefly dropped from the generated sitemap XML. Flagging for continued observation; if it disappears again tomorrow that would strengthen the "flaky sitemap" theory over a "real republish" theory.

### 2. Live A/B test on business-site navigation + a "ChatGPT Work" promo banner
Five business pages — `/business/partners/`, `/business/why-openai/startups/`, `/business/solutions/data/`, `/business/solutions/design/`, `/business/plugins/clay/` — came back this run with a different global header/nav than their lastmod-neighbors:
- Old nav: `Research / Business / Developers / Company` + `Log in` / `Try ChatGPT`
- New nav: `Why OpenAI / Solutions / Resources / Customers / Pricing` + `Try OpenAI` / `Contact sales`
- New nav variant also carries a promo banner not present in the old one: **"New: Introducing ChatGPT Work — A new agent in ChatGPT that helps teams turn ambitious goals into finished work—with enterprise controls and governance built in." → links to `/chatgpt-work/`**

Critically, sibling pages of the *same template* — `/business/`, `/business/pricing/`, `/business/solutions/{engineering,finance,marketing,operations,sales}` — were fetched in this same run and came back **byte-identical** to yesterday, still on the old nav. Since it's implausible OpenAI would permanently ship a new global nav to only 5 of 11 business pages, this reads as a live, randomized (cookieless) A/B test of a business-site redesign rather than a completed rollout. Worth watching over the next few days to see whether the new variant proportion grows.

## Significant updates (real content, not template noise)

### `/products/release-notes/` — four new entries land
This is the day's real news, surfaced via the release-notes changelog (its own lastmod moved from Jul 9 → Jul 10 within the page body, i.e. it's now current through Jul 9 per the dated entries):
- **Introducing the GPT-5.6 model family**: GPT‑5.6 rolling out globally across ChatGPT, Codex, and the API (full availability within ~24h of announcement). Family includes GPT‑5.6 Sol (frontier), Terra (balanced), and Luna (efficient/high-volume). The `gpt-5.6` API alias routes to `gpt-5.6-sol`. New API capabilities: Programmatic Tool Calling, explicit prompt-caching controls, persisted reasoning, max reasoning effort, Pro mode, and beta multi-agent orchestration for the Responses API; images now accepted at original dimensions.
- **Introducing ChatGPT Work**: a new ChatGPT agent for longer, more involved tasks — can research, work across connected apps/files, and produce finished documents, spreadsheets, presentations, reports, and Sites. Supports Scheduled Tasks (once/repeating/triggered/monitoring). Rolling out to paid plans except Free and Go; Pro/Pro Lite/Enterprise/Edu get it first, Plus/Business follow. Enterprise/Edu workspaces get a two-week opt-out preview window. Also: the **App Directory is being replaced by a Plugin Directory** (existing app connections unaffected).
- **ChatGPT desktop app unifies Chat, Work, and Codex**: new desktop app (macOS/Windows, global) merges conversational Chat, the new Work agent, and Codex software-development agent into one app. Desktop Work can access local files/apps with permission and browse the web. Codex in the new app adds inline diff editing, PR review in a side panel, faster Computer Use, and multi-repo support in one project. The previous standalone app persists as "ChatGPT Classic" for existing Enterprise capabilities while new agent features ship only in the new app. This directly explains why `/form/codex-app/` is still alive as a *Linux-only* waitlist — Codex now ships bundled into the desktop app for macOS/Windows, but Linux users still need to sign up separately.
- **ChatGPT Sites public beta**: Business/Enterprise customers can now publish Sites (dashboards, trackers, prototypes, internal portals, reports built via ChatGPT) publicly via a shareable URL, not just within their workspace.

This entry also pushed several prior release-notes items (GPT‑Realtime‑2.1, GPT‑5.5 Instant Mini, ChatGPT for PowerPoint GA + workspace-agent token pricing, ChatGPT for iOS updates) further down the page — no other content in those items changed, just displaced.

### `/index/gpt-5-6/` — minor benchmark correction
The GPT‑5.6 launch/benchmark page had the **CyberGym row removed** from its benchmark comparison table (previously showed 84.5% for GPT‑5.6 vs. comparison models). No accompanying explanation; looks like a data-quality retraction rather than a new claim.

### `/form/share-your-story/` — form simplified
The "share your story" intake form dropped its explicit "What OpenAI products do you/they use? (ChatGPT / Codex / Sora / Atlas / OpenAI API)" checkbox question, and simplified its intro copy from naming specific products ("...ChatGPT, Sora, Codex, and our API...") to generic "OpenAI products."

## Routine updates (template/navigation noise, not real content changes)

The remaining ~80 "updated" pages fall into three template-level patterns, confirmed by diffing after stripping known boilerplate:

1. **New in-page table of contents on article/blog pages** (e.g. `/index/building-codex-windows-sandbox/`, `/index/frontierscience/`, `/index/consensus/`, `/index/wrtn/`, `/index/introducing-company-knowledge/`, `/index/understanding-ai-and-learning-outcomes/`, `/index/how-people-are-using-chatgpt/`, `/index/introducing-b2b-signals/`) — these pages gained a "Table of contents" / duplicated hero block, with no change to the article's actual prose.
2. **Recirculation ("related posts") carousels refreshed** to surface newer content — pages like `/index/economic-research-exchange/`, `/index/first-proof-submissions/`, `/index/new-result-theoretical-physics/`, `/index/scaling-social-science-research/`, `/index/how-countries-can-end-the-capability-overhang/`, `/index/equipping-workers-with-insights-about-compensation/`, `/global-affairs/new-economic-analysis/`, `/index/introducing-gpt-5-4/`, `/index/introducing-gpt-5-5/`, `/index/how-chatgpt-adoption-has-expanded/`, `/index/codex-for-every-role-tool-workflow/`, `/index/introducing-openai-partner-network/` now link out to GPT‑5.6, ChatGPT Work, ChatGPT desktop, and other pages published Jul 8–10 in their "related" modules. Own body content unchanged.
3. **Global footer link swap**: `GPT-5.3 Instant` link replaced by `GPT-5.6` in the product-links footer, and `Customer Stories` / `Partner Network` links added to the footer, across many otherwise-unrelated pages (`/business/partners/`, `/form/codex-app/`, `/form/share-your-story/`, `/index/economic-research-exchange/`).

Everything else in the 88-URL updated set (`/`, `/api/`, `/codex/`, most `/business/...`, most `/index/introducing-gpt-5-*`, `/news/*` hub pages, `/policies/*`, `/signals/*`, academy pages) came back **byte-identical** in markdown despite a bumped `<lastmod>` — consistent with a CDN/CMS touch (cache revalidation, template propagation) with no visible content change.

## New pages

None net-new; the sole `added` URL (`/form/codex-app/`) is a reappearance of a previously-known page (see Anomaly #1), not new content.

## Removals

None this run.

## Needs follow-up

- Watch `/form/codex-app/` for another disappearance — would confirm sitemap flakiness vs. a deliberate churn.
- Watch business pages for whether the "Why OpenAI" nav + ChatGPT Work banner variant spreads to the remaining business pages (would confirm the A/B test converging into a permanent rollout) or reverts everywhere (would confirm it was a fluke render).
