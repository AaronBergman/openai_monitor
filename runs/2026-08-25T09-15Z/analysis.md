# Run 2026-08-25T09-15Z — Analysis

**Fetch time:** 2026-08-25T09:16:58Z UTC
**Baseline:** 2026-08-24T09-16Z (consecutive day)
**Totals:** 1,608 URLs (1,606 baseline → 1,608 current) | 2 added | 153 updated | 0 removed | 36 sub-sitemaps | 0 fetch failures

The most eventful run in several days. One new public post disclosing a disrupted Russian
influence operation, one new product-partnership post (GPT‑5.6 in Kiro), a full visual/nav
redesign of the `/business/` landing page, a substantive Ad Tools Terms revision, and a real
Codex product-notice (an MCP command deprecation) buried among 153 lastmod-touched pages —
most of which (127) turned out to be zero-content-change noise.

## Anomalies

**None.**

- No `<lastmod>` values later than the fetch time (checked all 1,608 current URLs).
- No `<lastmod>` values that moved backwards versus the prior snapshot (checked all 153 updated URLs).
- Both new URLs carry same-day `<lastmod>` timestamps (2026-08-25T08:04:59Z and 2026-08-24T08:51:48Z)
  — neither is backdated relative to its `first_seen` run, and neither was previously known
  (checked against `state/known_urls.json`), so no reappearance.
- No URL changed sub-sitemap section membership. Section sets were compared against the
  authoritative `sub_sitemaps` list persisted per-URL in `state/known_urls.json` (not a
  same-run single-section map, which the 2026-07-12 run documented as producing false-positive
  "migrations" when a URL is legitimately cross-listed in more than one section at once — e.g.
  nearly every `news/`-tagged article lives in both its topical section and `company`/`product`).
  All ~520 same-run cross-section duplicates observed this run are this same stable,
  persistent cross-listing pattern, not migrations.
- All 155 added/updated page fetches (2 new + 153 updated) succeeded on the first pass — 0 fetch failures.

## New pages

- **[`/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/`](../../pages/openai.com/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/index.md)**
  ("Disrupting a new covert influence campaign from Russia," Aug 25, 2026, Global Affairs). OpenAI
  says it banned a cluster of ChatGPT accounts that very likely originated in Russia, used VPNs to
  evade OpenAI's Russia access ban, and were instructed to hide linguistic tells while generating
  English-language social media comments (posted to Substack, Telegram, X, Facebook, LinkedIn)
  promoting a fake "expert community" called the International Burke Institute (IBI). The IBI
  website (claiming an Israel address, registered Feb 2025) republished real academic articles
  under false authorship (e.g., a Cambridge University Press piece re-attributed to a different,
  real Nottingham professor) and published a made-up "sovereignty index" grading countries —
  polemical, pro-Russia, anti-Western/anti-Ukraine content targeting France, Germany, the US, and
  the EU. OpenAI rates the operation's reach as low-end **Category Three** on the Brookings
  Breakout Scale (Telegram channels drew 10–20k followers each; social posts got little traction).
  OpenAI frames the significance as less about audience reached and more about the fabricated
  "credible-looking institution" infrastructure the operators built around isolated AI-generated
  promotional posts — and notes that reliance on AI is part of what exposed the operation.
- **[`/index/gpt-5-6-in-kiro/`](../../pages/openai.com/index/gpt-5-6-in-kiro/index.md)**
  ("Advancing price-performance for developers with GPT‑5.6 in Kiro," Aug 24, 2026, Product).
  Announces GPT‑5.6 (Sol/Terra/Luna model family) is now available inside Kiro, a third-party
  software-development agent, pitched on better price-performance for long-running agentic coding
  work grounded in a team's requirements and codebase. A partnership/integration post, same genre
  as the day's other builder-tool-integration announcements (cf. recent Amazon Bedrock, CodeAI
  partnership posts).

## Significant updates

- **`/business/` gets a full landing-page redesign.**
  [`/business/`](../../pages/openai.com/business/index.md) — this is not a copy tweak: the global
  nav on this page changed from `Research / Products / Business / Developers / Company` to
  `Why OpenAI / Products / Solutions / Resources / Customers / Pricing`, the primary CTA changed
  from "Try now → Contact sales" to "Try OpenAI / Get started → Contact sales", and the hero
  copy changed from "Create, code, and innovate with OpenAI's tools and APIs" to "Frontier
  intelligence everywhere you work". The old two-column "ChatGPT for Business" / "API Platform"
  pitch and its customer-logo strip were replaced with an "Introducing ChatGPT Work" callout and
  a new "AI for every team" / "A complete AI platform for your business" section (ChatGPT
  Work / Codex / API tabs). Whether this nav change is business-page-scoped or the leading edge
  of a sitewide nav overhaul isn't yet knowable from a single page fetch — worth watching whether
  the same `Why OpenAI / Solutions / Resources` nav shows up on other pages in coming runs.
- **Ad Tools Terms revised, effective Aug 24, 2026** (was July 31, 2026).
  [`/policies/ad-tools-terms/`](../../pages/openai.com/policies/ad-tools-terms/index.md) — beyond
  wording cleanup, this is a substantive rights expansion for OpenAI's advertising Creative Tools:
  the tools may now "select, assemble, or otherwise adapt" ad creatives (not just
  generate/modify/transform/optimize/localize/translate), including "dynamically tailoring them to
  the context of a user's interaction with OpenAI" — i.e., real-time ad-creative personalization
  per conversation. A new defined term, **"Campaign"** (a request submitted through Ads Manager, an
  approved API, or another OpenAI-designated method), replaces the looser "Campaign Parameters"
  concept. A new restriction (2.4/3.4(g)) explicitly bars advertisers from using the Creative
  Tools "to reveal, reproduce, infer, or imply access to non-public information about an OpenAI
  user or the user's interactions with OpenAI" — a privacy guardrail added alongside the
  personalization expansion. Advertiser indemnification is also explicitly extended to cover any
  Generated Creative "applied to your Campaign" (not just ones the advertiser affirmatively
  approves/uses), and Ads Manager controls to manage/disable Creative Tools are now referenced
  directly in the terms.
- **Release notes: Codex MCP server command deprecated.**
  [`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md) — new entry
  dated Aug 24, 2026 (tagged "Sunset"): `codex mcp-server` is deprecated in favor of the new Codex
  app server; users of Codex from Claude Code are directed to "use the Codex plugin for Claude
  Code" instead. Also picked up an Aug 21 "Improved plugin discovery on web and mobile" entry
  (ranking changes favoring plugins people keep using after install) that had rolled off the
  bottom of the visible feed in the prior snapshot.

## Routine, low-signal updates

- **~26 of 153** updated pages carry a genuine (non-dpl-only) markdown diff, but on inspection
  the overwhelming majority of those are bottom-of-page "related articles" / "Keep reading"
  carousel rotations reacting to today's 2 new posts and recent Zero-Data-Retention /
  Ultrafast-mode / GPT-5.6-Kiro posts slotting into carousels across many older `index/*` pages
  (`advancing-content-provenance`, `accelerating-cyber-defense-ecosystem`, `asana`,
  `global-affairs/new-economic-analysis`, `chatgpt-for-excel`, `introducing-gpt-5-4`,
  `new-policy-ideas-for-the-intelligence-age`, `introducing-gpt-5-2`,
  `how-countries-can-end-the-capability-overhang`, `nvidia/chatgpt-work`,
  `openai-joins-ports-pike-project`, `premium-seats-chatgpt-business`, `public-policy-agenda`,
  `stampli`, `previewing-ultrafast`, `thrive-holdings`, `unlocking-self-improvement-gpt-red`,
  `understanding-ai-and-learning-outcomes`, `news/`, `news/product-releases/`) — same pattern
  flagged in every recent run, no reader-facing meaning beyond "these posts are newly cross-linked."
- **`/index/gpt-5-1-for-developers/`** — pure typographic normalization: straight apostrophes
  (`'`) replaced with curly apostrophes (`’`) in three quoted customer testimonials. No wording
  change.
- **`/student-collective/`** — form-copy addition: both video-submission questions now add
  "Videos may be submitted in any language." No other change.
- **`/enterprise-privacy/`** — the enumerated-model list was refreshed (GPT-5.6 added,
  GPT-5.3 Instant dropped off the list) and a "Supply Co." merch-store link was added to a footer
  list (Supply Co. itself isn't new — it's been indexed under `/supply/product/*` since at least
  2026-07-17). Two sentences had straight apostrophes swapped for curly ones. No substantive
  privacy-policy change.
- **64 of 153** updated pages: confirmed to be the recurring Partner Network tier-badge
  `?dpl=dpl_...` deploy-ID churn (same pattern flagged repeatedly in prior runs) — zero visible
  pixel/text change, spanning most of the Partner Network roster (Accenture, Accenture Federal
  Services, Algorithmic Intelligence, Altimetrik, Altudo, AIWorks, Artefact, Artium, Bain &
  Company, Blend360, Blank Metal, Boston Consulting Group, Booz Allen Hamilton, Capco, Capgemini,
  CDW, CGI, Chieftns, Clarinet, Cloudwerx, Cognita Reply, Cognizant, Corca, Deepsense.ai, Dentsu
  Japan, Eliza, Endava, EPAM, Ernst & Young, Fellow Intelligence, Fractal, Fujitsu, Globant, HCLTech,
  IBM, Infosys, Insurgence, KPMG, Mantel, McKinsey & Company, Merantix Momentum, ML6, Nablon AI,
  Nagarro, NTT DATA, Pathfindr, PwC, Quantium, Recursive, Rosetree Solutions, Samsung SDS, SB OAI
  Japan GK, SIA, SK Inc. AX, Slalom, Snorkel AI, Statworx, TCS, Teamlab, Tredence, Tribe AI, Unit8,
  ZS).
- **63 of 153** updated pages: no rendered-text difference whatsoever — a pure lastmod/metadata
  touch, no visible effect (verified via markdown byte-diff against the prior committed snapshot).

## Removals

None this run.

## Fetch failures

None. All 155 targeted fetches (2 new pages + 153 updated pages) succeeded via
`tools/html_to_md.py` on the first attempt.
