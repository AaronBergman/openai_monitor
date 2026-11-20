# Run 2026-11-20T09-15Z — analysis

- **Sitemap fetch time:** 2026-11-20T09:16:56Z (root index + 44 sub-sitemaps)
- **Page fetches:** 60 pages (7 added + 53 updated), 09:17–09:20Z, via `tools/html_to_md.py` (curl-cffi). 0 failures.
- **Baseline:** 2026-11-19T09-15Z (consecutive day).

## A note on the baseline

`main` still ends at the 2026-09-28T09-17Z run: the daily draft PRs since then (#148 onward) have not been merged, so every run since has diffed against Sep 28. To get a real day-over-day diff, this run's branch was fast-forwarded onto the 2026-11-19T09-15Z run's branch (`claude/festive-wright-91bj62`, which contains the Sep 28 → Nov 19 catch-up diff) and diffed against that run's snapshot. This branch therefore contains **both** the Nov 19 catch-up run and this run. Merging this PR brings `main` up to date.

## Totals

| | Count |
|---|---|
| URLs in sitemap | 2,257 (was 2,251) |
| Sub-sitemaps | 44 (unchanged set) |
| Added | 7 |
| Removed | 1 |
| `<lastmod>` updated | 53 (10 with rendered content change, 43 identical) |
| Anomalies | 3 (2 low-signal, 1 contextual) |
| Fetch failures | 0 |

## 1. Anomalies

- **2 new URLs carry no `<lastmod>`:** `/ads/customers/portland-leather/` and `/ads/customers/weightwatchers/`. This continues the pattern seen on 2026-11-19, where all `/ads/` pages lacked lastmod. Both pages are dated "November 19, 2026" on-page. Low signal: it's how that section is published.
- **`/form/data-partnerships/` removed alongside a related edit.** The sign-up form left the sitemap. In the same window `/index/data-partnerships/` (lastmod 2026-11-04 → 2026-11-20T00:08Z) lost both of its "Submit interest" links to that form and gained an editor's note: *"OpenAI Data Partnerships is not accepting submissions at the moment."* The form had been in the sitemap since this repo's first snapshot (2026-05-07). The removal is consistent with the program pausing, so it isn't really an anomaly, but it is flagged because the removal and the edit were coordinated.
- None of the other checks fired: no future-dated `<lastmod>` (the newest is 2026-11-20T09:10:13Z, 6 minutes before fetch), no backwards `<lastmod>`, no reappearances, no sub-sitemap migrations or cross-listings, and no new URL with a lastmod more than 3 days before first_seen.

## 2. Significant updates

### Health privacy notice ([`/policies/health-privacy-policy/`](../../pages/openai.com/policies/health-privacy-policy/index.md)): rewritten; health chats can now be used for training by default
Header changed from "Updated: June 29, 2026" to "Updated: November 19, 2026". Changes:
- **Model training stance changed.**
  - *Old:* "By default, we do not use the following data to improve our foundational models … medical records and health data received from third-party accounts …, conversations in ChatGPT Health, and conversations when Health Connect is enabled."
  - *New:* "We do not train our foundation models or target ads on data synced via Connected Health Accounts. … conversations that reference Connected Health Accounts data, and content derived from it, **may be used to improve our models depending on your ChatGPT settings**. You can review or turn off model improvement at any time in Settings → Data Controls."
  - Net effect: raw synced records stay excluded (and an explicit no-ad-targeting promise is added), but health *conversations*, which used to be excluded by default, now follow the general opt-out setting. A matching "Model Training" choice bullet was added.
- **Product renamed and restructured.** The product goes from "ChatGPT Health / Connect Health (Health Features)" to "Health in ChatGPT", described as a "Health" plugin. The defined term "Connected Health Accounts" now explicitly covers medical providers, Apple Health **and Android Health Connect** (new).
- **Separate health memory removed.** The old notice described ChatGPT Health's own siloed memory ("Your main ChatGPT account will not access memories you create just within ChatGPT Health"). The new one says health conversations create ordinary ChatGPT memories if memory is enabled.
- **New uses and disclosures.** "Proactive updates" are added, e.g. when new records sync or "a new health trend is detected in your data". The disclosure list gains "with users and third parties you choose to interact or share information with". Health history now explicitly includes "your family's health history" and "medications you take".

### Cookie policy ([`/policies/cookie-policy/`](../../pages/openai.com/policies/cookie-policy/index.md))
"Last updated" changed from Oct 22 to Nov 19, 2026. Five first-party cookies were added: `oai-mweb-route` (7 days) and `oai-mweb-origin` (session) on chatgpt.com for "service functionality"; `analytics_consent_source` (180 days) on ads.openai.com; `__session` (365 days) on help.openai.com; and `oai-did-first-seen` (365 days, **Analytics**) on chatgpt.com. Two vendor links were also fixed (Swoogo, Google).

### Data Partnerships paused ([`/index/data-partnerships/`](../../pages/openai.com/index/data-partnerships/index.md))
See anomaly above: an editor's note says submissions are not being accepted, and the form links were removed.

### ChatGPT for Financial Services page ([`/business/solutions/financial-services/`](../../pages/openai.com/business/solutions/financial-services/index.md))
- The banner for the Nov 18 Nubank webinar (now past) was removed, along with the "GPT‑6 Astra … our most intelligent model" hero block.
- The feature list was refreshed: new "Company Research" (screeners to find companies) and "Company Profiles" (financials plus peers) sections, and "Earnings Calls & Live Events" (recordings paired with transcripts) replaces "Build, check, and visualize financial models".
- Screenshots were replaced, now showing a built-in financial-data menu with filings, financials, earnings calls and market data.

### Release notes ([`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md))
- New entry dated Nov 17 (API, beta): **discounted background completion windows in the Responses API**. A 2-hour window costs 30% less than Standard and an 8-hour window 40% less.
- The Nov 12 entry "Change users' email addresses in Admin Console" was **removed** from the page. It may have been retracted, or the list may just have been trimmed. Its help-center links remain the source of record.

## 3. Routine updates

- [`/index/astra-for-law/`](../../pages/openai.com/index/astra-for-law/index.md): added a short "Astra for Law update" box pointing to the November update post (`/index/astra-law-6-2/`, added on the 11-19 run).
- [`/business/solutions/accounting/`](../../pages/openai.com/business/solutions/accounting/index.md): trailing periods dropped from headings; a fifth customer quote/logo added (Hannah Bartel, Granite Peak Veterinary Advisors).
- [`/solutions/`](../../pages/openai.com/solutions/index.md): the index now lists the IT and Accounting solution pages.
- `/index/inside-the-codex-sandbox/`, `/index/jiostar-vijay-seshadri/`: only the "keep reading" carousels changed, now pointing at today's new posts.
- **43 URLs** bumped `<lastmod>` with byte-identical markdown (homepage, `/api/`, `/business/pricing/`, GPT‑6 Astra pages, ChatGPT Wallet, Businesses-in-ChatGPT terms, Wallet terms, `/signals/`, `/research/verify/`, `/trust-and-transparency/`, etc.). This is CMS/cache regeneration noise. Full list in `diff.json`.

## 4. New pages

- [**How OpenAI's Performance Factory keeps ChatGPT fast**](../../pages/openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/index.md) (Engineering, dated Nov 19). Describes an internal system in which Codex agents are woken by performance alerts. The agents find when a ChatGPT latency or availability regression began, identify the root cause, and propose a fix for an engineer to review. The system has a task service, a dispatch loop, Codex in the cloud, and subscriptions that wake agents on events such as a GitHub review or a deploy. OpenAI says that in a manual review of 100 root-cause suggestions, 70% were graded accurate. It fits the series of "how we use Codex internally" engineering posts (e.g. `/index/inside-the-codex-sandbox/`).
- **ChatGPT Ads case studies** (both dated Nov 19), extending the `/ads/` section added during the gap:
  - [Portland Leather](../../pages/openai.com/ads/customers/portland-leather/index.md): "93% of visitors from ChatGPT Ads were new visitors" according to Triple Whale.
  - [WeightWatchers](../../pages/openai.com/ads/customers/weightwatchers/index.md): attributed CPA 15.3% below its blended paid-search benchmark (DV Rockerbox), and about 30% lower cost per signup after switching to conversion optimisation.
  - These are the first named advertiser testimonials in this log.
- **Daybreak (cybersecurity) learning material**, following the GPT‑6 Cyber / Daybreak launches recorded on 11-19:
  - [Deploying Daybreak Red](../../pages/openai.com/business/learn/deploying-daybreak-red/index.md) (guide): links a PDF reference architecture for "supervised security investigations" in an isolated environment.
  - [Get started with Daybreak Blue](../../pages/openai.com/business/learn/daybreak-blue-onboarding-demo/index.md) (onboarding demo video).
  - [Explore the Codex Security Plugin](../../pages/openai.com/business/learn/codex-security-plugin-demo/index.md) (demo).
  - [See PR scans in action](../../pages/openai.com/business/learn/pr-scans-demo/index.md) (demo).
  - The three demo pages are thin wrappers around an embedded video.

## 5. Removals

- `https://openai.com/form/data-partnerships/`: the Data Partnerships interest form (see anomalies). Last snapshot: `git log -- pages/openai.com/form/data-partnerships/index.md`.
