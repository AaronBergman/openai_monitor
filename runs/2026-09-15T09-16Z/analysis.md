# openai.com sitemap monitor — analysis for run 2026-09-15T09-16Z

Fetch time (this run): 2026-09-15T09:16Z (UTC). Baseline: prior run `2026-09-14T09-16Z` (PR #133, merged same day).

Sitemap index: 38 sub-sitemaps (unchanged). Total unique URLs across all sections: 1,706 (up from 1,705).

Diff stats: **1 added, 250 lastmod-updated (129 with an actual content diff, 121 lastmod-only/no visible content change), 0 removed, 0 section migrations, 0 anomalies, 0 fetch failures** (251/251 page fetches succeeded via curl-cffi Chrome impersonation).

## Anomalies

None. No future-dated or backwards-moving `<lastmod>` values, no backdated new URLs, no reappearances, and no section migrations were found in the 1,706-URL set.

## Noise explaining most of the 250 "updated" count

Three site-wide/cosmetic patterns account for the large majority of the 129 real content diffs:

1. **"Keep reading" / customer-stories carousel reshuffle.** The new wildfire-detection story (see below) and yesterday's already-reported stories (Fyxer, Perplexity/Astra, Cognition/Astra) bubbled to the top of "Keep reading" widgets and the `/business/customer-stories/` and `/stories/` listing pages across ~50+ pages. No new information beyond what these listings already point to.
2. **Plugin-directory UI polish (~40 pages under `/business/plugins/*`).** Each plugin page now renders small app icons inline next to its example prompt chips (previously plain text links), and two use-case tag labels were simplified: **"Sales & Commerce" → "Sales"** and **"Data & Research" → "Data"**. Purely cosmetic/copy tightening, not a new feature.
3. **Stale "GPT-6" footer-nav catch-up.** A handful of pages (`estee-lauder`, `how-finance-teams-use-codex`, `managing-ai-investments-in-agentic-era`, `signals/research/2026q1-update`, `business-data`, and others) picked up the "GPT-6" link in the "Latest Advancements" footer that was actually added site-wide back on 2026-09-10/11 — these particular pages just hadn't re-rendered until now. Not new.
4. **Asset cache-bust.** `/business/partners/quantiphi/` changed only its partner-badge image's build-hash query parameter (`dpl=...`) — same image, no visual change.

## Significant updates

### Release notes: admin model-access testing tool
`/products/release-notes/` gained a new entry, **"Test a member's model access"** (ChatGPT, GA, Sep 11, 2026): ChatGPT Business admins can now use Admin Console → Models → Test to look up which models a given member can access and which settings drive that access. Testing is read-only — it doesn't grant access, change permissions, or override seat type/workspace plan. This pushed the whole changelog down by one entry, which is why the raw line-diff for this page looked large (86 lines) despite only one new item.

### Minor copy change
`/academy/marketing/` retitled its `<h1>` from "Learn ChatGPT workflows for marketing teams" to **"ChatGPT for marketing teams"** — a small rebrand toward punchier, less tutorial-sounding page titles (consistent with other `/academy/*` pages).

## New pages (1)

| URL | Category (inferred) |
|---|---|
| `/index/detecting-wildfires-early/` | Applied AI — human-interest story |

**"Using ChatGPT to detect wildfires early"** — profile of Ryan Honary, who as a fifth-grader after the 2018 Camp Fire began building a wildfire-detection science project and has since turned it into **SensoRy AI**: solar-powered field sensors (heat/smoke/flame/plume detection) relayed over a mesh network, with ChatGPT translating raw sensor data into plain-language alerts for firefighters. Includes a ChatGPT-Voice-driven "walkie-talkie" feature letting firefighters ask natural-language questions ("Is this a fire? Where is it? What's the best evacuation route?") and get answers from live sensor data. Quotes the Laguna Beach Fire Department chief and the Irvine Ranch Conservancy. Fits OpenAI's recurring "AI for good / applied AI" story series (same slot as last month's antimicrobial-research piece).

## Routine updates (not itemized individually)

- 121 URLs had a `<lastmod>` bump with **no visible content diff** in the rendered markdown (re-render/build noise).
- ~50 customer-story and listing pages reshuffled their "Keep reading" / story-grid modules to surface the new wildfire story and already-known recent stories (see noise section above).
- ~40 `/business/plugins/*` pages picked up inline prompt-icon rendering and the "Sales"/"Data" tag-label simplification (see noise section above).

## Removals

None.

## Fetch failures

None — all 251 added/updated URLs fetched successfully on the first attempt.
