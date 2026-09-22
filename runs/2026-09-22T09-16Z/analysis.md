# Run 2026-09-22T09-16Z — analysis

**Baseline:** 2026-09-21T09-17Z (consecutive day)
**Sitemap fetch time:** 2026-09-22T09:17:31Z UTC
**Page fetches:** 2026-09-22T09:17:31Z–09:18:14Z UTC (472 pages fetched, 8-way concurrency, 0 blocked/errored)
**Totals:** 1,993 URLs across 42 sub-sitemaps (baseline: 1,974 URLs / 42 sub-sitemaps) → **+21 added, 2 removed, net +19**
**Updated:** 451 URLs got a `<lastmod>` bump. Of those, 81 had any visible markdown diff; of those, 29 had a genuine content diff (the other 52 were whitespace-reflow or CDN-asset-hash-only noise). The remaining 370 "updated" URLs are the sitewide footer-nav change only (see Notable updates below) with zero other diff.

## Anomalies

1. **Future lastmod (negligible).** `https://openai.com/index/introducing-the-agents-api/` claims `lastmod = 2026-09-22T09:17:36.855Z`, five seconds after our sitemap fetch (`09:17:31Z`). This is clock-skew-scale, not a real "modified in the future" claim — the page was almost certainly regenerated essentially concurrently with our fetch. Flagging per protocol, but not treating as suspicious.
2. **Sitemap "migration" false positives (4) — same known issue as 2026-09-21.** `understanding-ai-and-learning-outcomes`, `equipping-workers-with-insights-about-compensation`, `global-affairs/new-economic-analysis`, and `how-countries-can-end-the-capability-overhang` were flagged as moving from `global-affairs` → `global-affairs-news-listed`. Verified: all four are cross-listed in **both** sub-sitemaps in **both** yesterday's and today's snapshots. Not a real change — an artifact of this run's diff script only tracking one sub-sitemap per URL (fixed for future runs; see note below).
3. **Real cross-listing additions (2, not really "anomalies" — see Notable updates):** `business/plugins/midpage/` and `business/plugins/legal-data-hunter/` gained a second sitemap listing under `plugins-legal` (in addition to their existing `plugins-education` listing) — part of today's legal-plugins expansion.

No backwards-moving `<lastmod>` values. No backdated new URLs (all 21 new URLs have `<lastmod>` within the last day). No reappeared URLs (checked against `state/known_urls.json`).

**Process note for future runs:** the diff script used this run (`build_membership`) collapses a URL's sub-sitemap membership to a single value, which produces false "migration" anomalies for URLs that are legitimately cross-listed in multiple sections (this has now happened on both 2026-09-21 and 2026-09-22, always in `global-affairs`/`global-affairs-news-listed`). Future runs should track membership as a **set** per URL and only flag a real migration when the set actually shrinks/moves rather than just reorders.

## Removed pages

- `https://openai.com/business/guaranteed-capacity/` and `https://openai.com/form/guaranteed-capacity/` — the "OpenAI Guaranteed Capacity" product page and its associated lead-gen form disappeared from the sitemap. Last snapshot (from 2026-09-21) pitched "long-term access to OpenAI compute" for large customers. Last good copy: `git show 4f8b2e06:pages/openai.com/business/guaranteed-capacity/index.md`. Cause unknown — could be a page consolidated elsewhere, or a product offering being retired/renamed; worth checking again on future runs for a possible reappearance under a new URL.

## Significant updates (real content changes)

- **`business/plugins/` ecosystem rebrand, continuing from prior runs' partial rollout, now essentially complete:** every plugin-detail page that changed today switched its CTA from "Add plugin" to "Install plugin," renamed the "Common use cases" section heading to "What else can you do?", and changed example try-it links from generic "(opens in a new window)" to "Try in ChatGPT Work(opens in a new window)" with a `surface=work` query param. The plugins hub page (`business/plugins/`) hero copy changed from "Work across your favorite apps **from** ChatGPT" to "Work across your favorite apps **in** ChatGPT."
- **"Apps" directory folded into "Plugins."** Three solutions pages — `business/solutions/design/`, `business/solutions/education/`, `business/solutions/engineering/` — had their embedded app-icon strips repointed from `/business/apps/<slug>/` to `/business/plugins/<slug>/` (and the education page's "View apps" link became "View plugins"). Combined with yesterday's and today's nav change (see below), OpenAI appears to be consolidating the "Apps" and "Plugins" concepts into a single "Plugins" surface.
- **Sitewide footer nav: added a "Plugins" link.** The footer's business-sitemap column now includes `* [Plugins](/business/plugins/)`. This single addition is responsible for 370 of the 451 lastmod-bumped URLs having a nonzero diff, spread across essentially the whole site (any page using the standard footer).
- **[Advisory Group on Mathematics and Artificial Intelligence](../../pages/openai.com/index/advisory-group-on-mathematics-and-ai/index.md)** (new page) — OpenAI discloses that an internal model ("Astra"), since August 28, has resolved **more than 100 long-standing open problems across most areas of mathematics** (following its Navier–Stokes Millennium Prize solution). In response to an open letter ("A Severe Misalignment of AI in Mathematics," mathandai.org) raising concerns about AI companies treating open problems as benchmarks, OpenAI is standing up an independent advisory group of mathematicians — hosted at the Institute for Advanced Study — including **Edward Witten**, Timothy Gowers, Martin Hairer, Ravi Vakil, and six others. The group can publish criticism of OpenAI unprompted and is explicitly *not* being asked to help pace OpenAI's internal math research.
- **[Building standards for the next phase of AI](../../pages/openai.com/index/building-standards-next-phase-ai/index.md)** (new page, Global Affairs) — a policy essay arguing the US should lead an international effort on technical standards for frontier AI, explicitly including **recursive self-improvement (RSI)**. States "fully autonomous RSI is not happening today" but frames it as approaching, and references the previously-disclosed Hugging Face security incident as "a preview of the kinds of risks that could become much more severe without robust safeguards." Proposes leveraging the CAISI-led international AI safety institute network and common incident-reporting protocols.
- **13 new legal-industry ChatGPT plugins launched**, expanding the `plugins-legal` sub-sitemap from 21 to 37 entries: Everlaw, Courtroom5, UniCourt, GC AI, Boardwise, Consolio Aurora, Definely, Descrybe, Lawve AI, PandaDoc, Patlytics, The L Suite (Lloyd and TopCounsel), and Trellis Law. Two existing plugins (Midpage, Legal Data Hunter) were also newly cross-listed into `plugins-legal` (previously only under `plugins-education`).
- **[`consumer-privacy`](../../pages/openai.com/consumer-privacy/index.md) page rewritten** — headline changed from "Privacy that puts you in control" to "Clear privacy choices, with protections built in"; added a direct link to the new `chatgpt.com/privacy-center`; restructured into three explicit commitments ("We don't sell your data," "We secure your information," "You control your data") replacing the previous more abstract framing.
- **[`daybreak/`](../../pages/openai.com/daybreak/index.md)** (the AI-for-cybersecurity initiative) — primary CTA changed from "Contact Cyber sales" to "Apply for Daybreak," suggesting a shift from a sales-led to an application-based intake process.
- **[`collective-cyberdefense/`](../../pages/openai.com/collective-cyberdefense/index.md)** — 26 new named organizations joined the Collective Cyberdefense member list, including Illumio, SailPoint, Contrast Security, and Supabase.
- **[`policies/service-terms/`](../../pages/openai.com/policies/service-terms/index.md)** — "Updated" date moved from Sep 10 to Sep 21, 2026; text now also references new standalone **Credit Score Terms**, implying a forthcoming/new credit-score-related feature under the Financial Services umbrella (no separate `credit-score-terms` page found in this sitemap snapshot yet — worth checking next run).
- **[`how-openai-uses-codex`](../../pages/openai.com/business/guides-and-resources/how-openai-uses-codex/index.md)** — lost a block of ~8 internal-engineer testimonial quotes about using Codex (e.g., "Codex swapped every legacy `getUserById()` for our new service pattern..."). Content removed, not replaced.
- **`business/plugins/highlevel`, `hex`, `hugging-face`, `jam-dev`, `klaviyo`** — same CTA/heading rebrand as above plus example-prompt card reshuffles (new prompts swapped in).

## Pattern worth watching (ambiguous — flagged, not asserted)

Several older `index/*` research and blog posts (`evaluating-chain-of-thought-monitorability`, `frontierscience`, `gdpval`, `introducing-indqa`, `improving-model-safety-behavior-with-rule-based-rewards`) lost embedded illustrative-example content blocks (verbatim prompts, example chain-of-thought transcripts, example completions) in this run's diff, while a handful of unrelated old posts (`arco-education`, `finding-gpt4s-mistakes-with-gpt-4`, `mavenagi`) picked up a stray `GPT-6` cross-link with no other change. Both patterns are consistent with a shared template/rendering-component change (e.g., an interactive example widget that changed how it server-renders, or now lazy-loads client-side) rather than deliberate editorial removal of those specific examples — but it cannot be ruled out from static HTML alone. Recommend a follow-up run to see if these blocks reappear (would confirm rendering artifact) or stay gone (would confirm real removal).

## Routine updates (lastmod bump, no or cosmetic-only diff)

- 370 URLs: footer-nav "Plugins" link addition only (see above) — no other change.
- 49 URLs: whitespace/blank-line reflow only, no textual diff.
- 3 URLs: partner-badge SVG CDN deploy-hash (`dpl=dpl_...`) changed, image content identical (`exl-service`, `quantiphi`, `sdg-group`).

## New pages (routine, no further flag)

- `business/learn/download-the-chatgpt-work-guide-for-data-teams/`, `business/learn/how-our-data-analytics-team-uses-chatgpt-work/` — gated webinar/guide landing pages, part of the ongoing "ChatGPT Work" enterprise-brand push.
- `index/expanding-openai-academy-with-new-learning-paths/` — OpenAI Academy adds role-based learning paths (employees, developers, leaders, educators, students).
- `index/higgsfield-from-prompt-to-production-with-astra/`, `index/v7/` — startup customer case studies (Higgsfield AI video-ad generation; V7 "institutional memory" for AI agents, 89% accuracy on graph-query tests), both attributed to GPT-6 Astra.

## Fetch failures

None. All 472 targeted fetches (21 added + 451 updated) succeeded on the first attempt.
