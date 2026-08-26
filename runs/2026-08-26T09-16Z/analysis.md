# Run 2026-08-26T09-16Z — Analysis

**Fetch time:** 2026-08-26T09:17:13Z UTC
**Baseline:** 2026-08-25T09-15Z (consecutive day)
**Totals:** 1,614 URLs (1,608 baseline → 1,614 current) | 6 added | 187 updated | 0 removed | 36 sub-sitemaps | 0 fetch failures

Headline of the day: **Jalapeño**, OpenAI's first custom inference chip (previously only
announced), now has first measured performance results, paired with a CFO strategy post framing
it as part of a "full-stack" compute advantage. Alongside that, ChatGPT Business **Premium seats**
moved from limited/waitlist to generally available, with a new tiered pricing page ($20/mo
Standard vs. $100/mo Premium), and age prediction began rolling out in the EU. A new Admin plugin
for ChatGPT Work/Codex was also introduced. Everything else this run was template noise: a
site-wide footer nav swap (GPT‑5.6 replacing GPT‑5.3 Instant, a new "Supply Co." merch link) and a
"related articles" carousel refresh that touched dozens of unrelated archive pages without
changing their actual content.

## Anomalies

**None.**

- No `<lastmod>` values later than the fetch time (checked all 1,614 current URLs).
- No `<lastmod>` values that moved backwards versus the prior snapshot (checked all 187 updated
  URLs).
- All 6 new URLs carry same-day/prior-day `<lastmod>` timestamps (Aug 25–26, 2026) — none
  predates its `first_seen` run, and none was previously known in `state/known_urls.json`
  (checked for disappearance/reappearance — no matches).
- No URL changed sub-sitemap section membership, checked against the persistent `sub_sitemaps`
  list stored per-URL in `state/known_urls.json` (not a same-run map, which the 2026-08-25 run
  noted produces false-positive "migrations" for URLs that are legitimately cross-listed in more
  than one section at once).
- All 193 added/updated page fetches (6 new + 187 updated) succeeded on the first pass — 0 fetch
  failures, 0 Cloudflare-challenge responses.

## New pages

- **[`/index/jalapeno-first-results/`](../../pages/openai.com/index/jalapeno-first-results/index.md)**
  ("Jalapeño's first results show industry-leading speed and efficiency in AI inference," Aug 25,
  2026, Engineering). First measured performance data for Jalapeño, OpenAI's first custom
  inference chip (previously only announced as a project). Tested on InferenceX (a public
  SemiAnalysis benchmark) across GPT‑OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T, Jalapeño
  delivered 1.5–1.9x more AI work per watt at peak throughput and 1.7–3.6x lower end-to-end
  latency than comparison systems (2.1–4.1x higher performance on highly interactive workloads).
  The chip is rated at 700W but measured sustained power at or below 550W. OpenAI credits AI
  itself with accelerating the chip's design (tapeout in 9 months) and says Codex/GPT‑Astra
  brought three additional open-weight model families to high performance within two months,
  with AI-generated kernel implementations running 1.5–1.8x faster than human-expert code for
  selected blocks. Deployment inside OpenAI's own infrastructure is planned by year-end; Gen 2 is
  "deep in development" and Gen 3 "taking shape." OpenAI is explicit this supplements, not
  replaces, NVIDIA and other third-party accelerators.
- **[`/index/the-full-stack-behind-abundant-intelligence/`](../../pages/openai.com/index/the-full-stack-behind-abundant-intelligence/index.md)**
  ("The full stack behind abundant intelligence," Aug 25, 2026, Company, by CFO Sarah Friar).
  Companion strategy piece to the Jalapeño results post. Frames OpenAI's compute strategy as one
  integrated system (data centers, chips, models, developer platform, products, devices) where
  each layer strengthens the next, with Jalapeño as evidence of a "credible first-party" hardware
  path alongside third-party partners (Microsoft, NVIDIA, AWS, AMD, Broadcom, Cerebras,
  CoreWeave, Oracle, SB Energy, SoftBank). Cites GPT‑5.6 Sol reaching a new high on the Artificial
  Analysis Coding Agent Index using 54% fewer output tokens than a competing model, and invokes
  Jevons paradox — cheaper/more capable intelligence expands total usage and revenue rather than
  just cutting cost.
- **[`/index/introducing-admin-plugin/`](../../pages/openai.com/index/introducing-admin-plugin/index.md)**
  ("Introducing the Admin plugin for ChatGPT Work and Codex," Aug 25, 2026, AI Adoption). New
  plugin letting workspace admins review usage/adoption, manage members and groups, review and
  change permissions, and approve/deny spending requests conversationally inside ChatGPT Work and
  Codex, plus automate recurring admin workflows (e.g., routing approvals to Slack/Teams). Pitched
  as permission-aware (it doesn't grant broader access than the admin already has). OpenAI cites
  its own IT team's usage: a ChatGPT Work Slack agent resolving ~45% of employee IT ticket volume.
- **[`/index/loveholidays/`](../../pages/openai.com/index/loveholidays/index.md)**
  Customer story: online travel company loveholidays using Codex to let non-engineers ship code
  changes. Headline stats: AI-assisted code changes grew from 7% to 79% of changes in a year, a
  73% increase in deployment frequency without growing the engineering team, and a jump in Data
  Platform change success rate from 58% to 93%.
- **[`/webmcp-challenge/`](../../pages/openai.com/webmcp-challenge/index.md)**
  A 10-day hackathon ("The WebMCP Challenge," registration via Devpost) built around WebMCP, an
  experimental open web standard (from the WebMachineLearning community group) that lets websites
  expose structured tools for agents to call directly instead of navigating the UI. Prize
  incentive for apps that get "meaningfully better" when used by people and their agents together.
- **[`/business/learn/intelligence-at-work-cyber/`](../../pages/openai.com/business/learn/intelligence-at-work-cyber/index.md)**
  Registration page for a livestreamed keynote, "Intelligence at Work: Cyber," Sept 3, 2026,
  1:00–2:00pm PDT — OpenAI security-team content on using frontier models for cyber defense.

## Significant updates

- **ChatGPT Business Premium seats go generally available, with a new tiered pricing page.**
  [`/business/pricing/`](../../pages/openai.com/business/pricing/index.md) replaced its old
  single "$20/user/month" plan copy with two seat tiers: **Standard seat** ($20/mo billed
  annually, $25/mo billed monthly) and **Premium seat** ($100/mo billed annually, $125/mo billed
  monthly, "5x more usage than standard, with no 5-hour limit"), pitched as "mix and match seat
  types for any budget." This is corroborated by two other pages updated the same day:
  [`/index/premium-seats-chatgpt-business/`](../../pages/openai.com/index/premium-seats-chatgpt-business/index.md)
  added a banner — "Update on August 25, 2026: Premium seats are now available on ChatGPT
  Business. The promotion to earn workspace credits for your first premium seats has ended" — and
  [`/form/business/premium-offer/`](../../pages/openai.com/form/business/premium-offer/index.md)
  changed its closed-signup notice from "Premium seats are coming soon" to "Premium seats are now
  available," linking to the new pricing page. Together these mark Premium seats moving from a
  limited-access promotion to a standard purchasable tier.
- **Age prediction begins rolling out in the EU.**
  [`/index/our-approach-to-age-prediction/`](../../pages/openai.com/index/our-approach-to-age-prediction/index.md)
  (an existing policy post) added an update banner: "Update on August 25, 2026: Age prediction
  has begun rolling out in the EU, helping us deliver age-appropriate experiences to even more
  teens around the world." No new standalone post — just an addendum to the existing explainer.
- **EU services privacy policy revised (effective Aug 25, 2026, superseding the June 4, 2026
  version).**
  [`/policies/eu-services-privacy-policy/`](../../pages/openai.com/policies/eu-services-privacy-policy/index.md)
  — notable wording changes beyond a version-date bump: the "User Content" bullet dropped the
  specific "Sora characters" data-type example (the rest of the Content definition is unchanged);
  the Usage Data bullet now folds in Free/Go users' ad-interest data collection directly (previously
  covered by a separate "Ads data" bullet, which was removed as its own heading) and changed
  "Atlas browser" to the more generic "in-app browser"; ad-partner data language changed from
  "purposes including to help us measure" to "purposes described in this Policy including to help
  us measure and improve the effectiveness of our Services"; a new "Other Users and Third Parties
  You Interact or Share Information With" bullet was added, covering shared ChatGPT conversations
  and third-party search/shopping partners. Net effect reads as a consolidation/generalization
  pass rather than a new data-collection practice.
- **`/education/` CTA link retargeted.** The "Learn more" link on the education landing page now
  points to `chatgpt.com/students/2026/` instead of `chatgpt.com/college-students/` — consistent
  with a dated, presumably annually-refreshed landing page for the student offer.
- **Build Week Challenge winners announced.** [`/build-week/`](../../pages/openai.com/build-week/index.md)
  flipped from a "submit your project" call-to-action to a winners showcase. First place in the
  Education track: **Mechanica**, an interactive digital museum bringing ancient Chinese machines
  to life via physics-based 3D reconstructions (built by Weiying Zhu, Yukun Li, and Shan Wei),
  with further winners listed below it. The challenge (Codex-built projects, judged Jul 22–Aug 24)
  has now concluded.
- **Old content-provenance post gets a forward pointer.**
  [`/index/understanding-the-source-of-what-we-see-and-hear-online/`](../../pages/openai.com/index/understanding-the-source-of-what-we-see-and-hear-online/index.md)
  (a 2024 post) added a note: "This post outlined our approach to content provenance in 2024. For
  our latest work," linking to a public verification tool (`/research/verify/`) and a newer post,
  "advancing-content-provenance." Archival correction, not new news itself.

## Routine updates (noise, not reported individually)

179 of the 187 lastmod-touched pages turned out to be pure template/boilerplate/cosmetic churn
once diffed against yesterday's markdown:

- **102 pages** were **byte-identical** to yesterday's saved markdown — lastmod bumped with zero
  visible content change (metadata-only re-saves or non-rendered field edits).
- **14 pages** changed *only* in the global footer nav: the flagship-model footer link swapped
  from "GPT‑5.3 Instant" to "GPT‑5.6," and a new "Supply Co." link (OpenAI's merchandise store,
  `/supply/`) was added; some pages also gained "Customer Stories" and "Partner Network" links
  under the Business footer column. Purely a global template change, unrelated to each page's own
  content — but notable as a site-wide signal that GPT‑5.6 has now displaced GPT‑5.3 Instant as
  the featured flagship model in navigation.
- **45 pages** changed *only* via a "related articles" carousel refresh or an exact-duplicate/
  reordered table-of-contents block (mostly older `/index/...security`, `/index/...cyber`, and
  research-archive pages), plus 4 partner pages whose only change was a CDN cache-bust query
  parameter (`?dpl=...`) on an otherwise-identical partner-tier badge image. No change to any
  page's own body content in this group.
- **18 pages** had cosmetic-only body edits: 13 where a client-rendered table-of-contents block
  appears to populate/expand for the first time on an older, previously-TOC-less post (likely a
  widget-rendering artifact of the fetch timing rather than a deliberate content edit — the
  visible prose is unchanged) and 5 where the only change was straight apostrophes (`'`) becoming
  curly ones (`'`) — a copy-editing/CMS re-save with no wording change (e.g.
  `/index/hardening-atlas-against-prompt-injection/`, `/index/security-on-the-path-to-agi/`,
  `/index/scaling-trusted-access-for-cyber-defense/`, `/index/axios-developer-tool-compromise/`,
  `/global-affairs/disrupting-malicious-uses-of-ai/`).

## Removals

None this run.
