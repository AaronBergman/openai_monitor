# Run 2026-08-13T09-16Z — Analysis

Fetch time: 2026-08-13T09:18:35Z (sitemap index + 35 sub-sitemaps)
Baseline: 2026-08-12T09-19Z
Total URLs (this run): 1,577 across 35 sub-sitemaps
Added: 9 · Removed: 5 · lastmod-updated: 136 · Sub-sitemap migrations: 4 · Fetch failures: 0

## Anomalies / notable observations

### 1. Rename: "Codex for Work" academy content → "ChatGPT Work"
`/academy/codex-for-work/` and its 3 child pages (`how-business-operations-teams-use-codex`,
`how-data-science-teams-use-codex`, `how-sales-teams-use-codex`) disappeared from the sitemap;
identically-named children reappeared under `/academy/chatgpt-work/`. The migrated pages'
copy now reads: *"This webinar was recorded when these workflows lived in the former Codex
app. You can now follow along using ChatGPT Work at chatgpt.com or in the ChatGPT desktop
app."* This is a straight URL rename tracking a product rebrand, not new content — same
webinar recordings, same publish dates (Jul 14, 2026), new home.

### 2. Rename: "Signals B2B data" → "Enterprise Signals data"
`/signals/b2b/` disappeared; `/signals/enterprise-data/` and a new lead form
`/signals/enterprise/intake-form/` appeared. Every page that used to promote "Signals B2B
data" (`/signals/`, `/signals/research/`, `/signals/data/`, `/signals/data-download/`) now
promotes "Enterprise Signals data" with new copy: *"OpenAI's Enterprise Signals tracks AI
adoption across industries and business functions. Explore the frontier gap, agentic work,
and enterprise usage data."* This coincides with a new flagship report — see New pages below.

### 3. Continuing pattern: nav-template flip-flop (first flagged 2026-08-08, still active)
Repeated same-URL fetches return one of **two different global header variants** at random:
- **Old:** nav = Why OpenAI / Solutions / Resources / Customers / Pricing; buttons = "Try
  OpenAI" + "Contact sales"; logo links to `/business/`.
- **New:** nav = Research / Business / Developers / Company / Foundation (links to
  `openaifoundation.org`, opens in new window); buttons = "Log in" + "Try ChatGPT"; logo links
  only to `/`.

This run it hit 9 pages: `kpmg`, `figma`, `microsoft-outlook-calendar`, `netlify` flipped
old-nav→new-nav; `ntt-data`, `microsoft-outlook-email`, `microsoft-teams`,
`public-equity-investing`, `semrush` flipped the other way. Page content is otherwise
identical in every case — only the header/footer nav block toggles between fetches, confirmed
by re-fetching several of these URLs 3× in a row and seeing the variant stay put per-fetch but
disagree with the previously-saved snapshot. Same flaky template-caching/A-B-test behavior
documented in every run since 2026-08-08 (it briefly spread to `/business/plugins/*` on
2026-08-11 and 2026-08-12; today it spans both `/business/plugins/*` and
`/business/partners/*`). Recorded here, as always, so it isn't mistaken for real per-page
edits: of 136 pages with a changed `<lastmod>` this run, ~79 differed only in this nav markup
once normalized.

No timestamp-based anomalies this run (no future-dated `lastmod`, no backward-moving
`lastmod`, no backdated new URLs, no disappeared-then-reappeared URLs).

## Sub-sitemap migrations
4 URLs moved from `global-affairs` to `global-affairs-news-listed`:
- `/index/how-countries-can-end-the-capability-overhang/`
- `/index/understanding-ai-and-learning-outcomes/`
- `/global-affairs/new-economic-analysis/`
- `/index/equipping-workers-with-insights-about-compensation/`

Likely a content-taxonomy reclassification (these move into a "news, listed" bucket) rather
than a substantive change to the articles themselves.

## Significant updates

**New flagship research: "Enterprise Signals" + companion working paper.** The article
`/index/how-enterprises-put-ai-to-work/` ("From assistance to execution: How enterprises put
AI to work") publishes two reports: *Enterprise Signals* (`/signals/enterprise-data/`) and a
working paper *"How Organizations Use AI: Evidence from ChatGPT."* Headline findings: as of
June, Codex generated 64% of combined Codex+ChatGPT enterprise output tokens (up sharply,
evidence of a shift from "assistance" to "execution"); the top-10%-of-usage "frontier firms"
now generate 8.3× the output tokens per active user of typical firms, up from 2.6× in
January; weekly active enterprise Codex users grew 108× in legal, 41× in sales, 41× in
recruiting, 26× in marketing (vs. 5× in engineering) since February; and AI usage is highest
among early-career employees, falling with seniority. This article is now cross-linked as the
"related article" on a dozen-plus other pages, which is why so many otherwise-unrelated pages
(`building-abundant-intelligence`, `openai-on-oracle-cloud`, `testing-ads-in-chatgpt`,
`zapier`, `virgin-atlantic/chatgpt-work`, etc.) show a 1-card "related articles" swap this run
— routine, not independently notable.

**New product release note: ChatGPT Enterprise/EDU retires individual-user connector sync.**
`/products/release-notes/` gained a new top entry (Aug 10, "Sunset" tag): *"Retiring
individual-user sync for connected apps"* — starting Aug 10 new individually-authorized sync
connections are blocked; on Aug 14 existing individual-user sync connections will be disabled
and their synced data deleted. Administrator-managed sync is unaffected. This is an actionable
deadline for ChatGPT Enterprise/EDU admins reading this log.

**Daybreak (OpenAI's cyber/security model line) partner program expands into major
consultancies.** Six "Program partners" (renamed from "Joint partners" — see below) pages
gained Daybreak specifically: Accenture, Capgemini, Cognizant, PwC (each: "AWS and Oracle" →
"AWS, Daybreak, and Oracle"), Ernst & Young (gained "Daybreak" as sole listed program
partner), and KPMG ("Oracle" → "Daybreak and Oracle"). The `/daybreak/`, `/daybreak/partners/`,
and `/daybreak/partners-new/` pages all swapped their partner-logo-grid image, consistent with
new partners being added to the Daybreak Cyber Partner Program. Combined with last run's new
Daybreak articles (AWS availability, "cyber defense window narrows"), this reads as a
continued, active rollout of Daybreak this week.

**Business Premium promo increased.** `/form/business/premium-offer/`: headline changed from
*"Get $100 worth of credits toward your first ChatGPT Business Premium seat"* to *"Get up to
$500 worth of credits toward your first ChatGPT Business Premium Seats"* (note: singular
"seat" → plural "Seats" — the offer may now apply per seat rather than per account).

**Site-wide "Joint partners" → "Program partners" relabel.** Independent of the Daybreak
additions above, roughly a dozen `/business/partners/<name>/` pages (Accenture Federal
Services, Altimetrik, Artefact, Bain & Company, Boston Consulting Group, HCLTech, Fractal,
Infosys, McKinsey & Company, Slalom, Snorkel AI) had the label "Joint partners" replaced with
"Program partners" with no change to the partner list itself — a terminology-only update,
likely site-wide, that happened to land in this run's lastmod-changed set. Several other
partner pages (Artium, Eliza, Pathfindr, SB OAI Japan GK, AIWORKS) only had their partner-tier
badge image asset hash bumped (cosmetic, same badge).

**Build Week deadline extended.** `/build-week/`: judging period pushed from "July 22–August 7"
to "July 22–August 24"; winners announcement moved from August 12 to August 25.

## Routine updates
- `/business/plugins/mailchimp/` and `/business/plugins/replit/`: example ChatGPT prompt copy
  refreshed (marketing copy churn, no functional change).
- `/global-affairs/brazil-ai-moment-is-here/`: "related articles" and footer nav links
  refreshed to current site content.
- Remaining ~57 pages with lastmod changes not detailed above differed only in the nav
  A/B-test markup described in Anomaly #3, once normalized — no substantive content change.

## New pages
- **`/index/how-enterprises-put-ai-to-work/`** — flagship research post, see Significant
  updates above. [saved](../../pages/openai.com/index/how-enterprises-put-ai-to-work/index.md)
- **`/signals/enterprise-data/`** — "Enterprise signals: What frontier firms are doing
  differently" report page (successor to Signals B2B).
  [saved](../../pages/openai.com/signals/enterprise-data/index.md)
- **`/signals/enterprise/intake-form/`** — lead-gen intake form tied to the above.
  [saved](../../pages/openai.com/signals/enterprise/intake-form/index.md)
- **`/index/ringcentral/`** — new customer story: "How RingCentral builds AI-native work from
  engineering to ops," using ChatGPT Work and Codex.
  [saved](../../pages/openai.com/index/ringcentral/index.md)
- **`/business/partners/nagarro/`** — new partner directory page for Nagarro (added to the
  `/business/partners/` logo grid this run).
  [saved](../../pages/openai.com/business/partners/nagarro/index.md)
- **`/academy/chatgpt-work/`** (+ 3 child pages) — rename target, see Anomaly #1.

## Removals
- `/academy/codex-for-work/` (+3 children) — renamed to `/academy/chatgpt-work/`, see Anomaly #1.
- `/signals/b2b/` — renamed to `/signals/enterprise-data/`, see Anomaly #2.

Prior snapshots of all removed pages remain in git history
(`git log -- pages/openai.com/<path>.md`).

## Fetch failures
None. All 145 added/updated pages fetched successfully via `tools/html_to_md.py`.
