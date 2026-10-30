# Analysis — 2026-10-30T09-17Z

Fetch time: 2026-10-30T09:18:51Z (sitemap), pages fetched immediately after (1,847 pages, 0 fetch failures).
Baseline: 2026-09-28T09-17Z — **a 32-day gap** (no runs are in the repo for 09-29..10-29), so this diff aggregates a month.

## Anomalies
1. **Baseline gap (32 days).** Changes below span a month, not a day; first_seen for new URLs is therefore 10-30 even if they went live earlier (their `<lastmod>` / on-page dates show Oct 2026 launches, e.g. Oct 22–29).
2. **Site-wide `<lastmod>` refresh.** 1,711 of 1,985 baseline URLs changed `<lastmod>`; 385 carry timestamps from the 09:xx hour of today and 188 from 08:xx — i.e. timestamps essentially equal to the fetch time. A shared template change (nav/footer) explains it: 1,711 pages gained the same diff (see below).
3. **Two "future" lastmods** (`/index/gpt-5-1-codex-max/`, `/index/updated-model-spec/`): 1–2 s after the run-start timestamp. The sitemap stamps some lastmods at request time; not a true future date. The gpt-5-1-codex-max timestamp is notable because it is an old page.
4. **Re-appeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
5. **Sub-sitemap migrations (219 URLs).** Largest: company→global-affairs (35), product→release (25), plugins-legal→plugins-operations (12), company→product (11), safety→security (10), plugins-data-research→plugins-engineering-it (8), plugins-hr→plugins-operations (7), product→research (7), api→learn-openai-on-openai (6). A taxonomy re-sort; also a new sub-sitemap `learn-demos` (14 URLs).
6. **21 URLs have no `<lastmod>`**: `/supply/product/*` (merch store, 18), `/ads/customers/evernote/`, and the brand-new `/index/introducing-gpt-6-1-sol/` and `/index/introducing-gpt-6-1-terra/`.
7. No lastmod moved backwards.
8. `/cyber-at-the-frontier/` renders as an ASCII-noise puzzle page (content is obfuscated characters) — likely an intentional teaser.

## Significant updates
- **Global nav/footer change on 1,711 pages:** the "Latest" model links now read GPT-6.1 Sol / GPT-6 Astra (GPT-5.4 and GPT-6 removed); Codex now points to chatgpt.com/codex; Open Models and Apps SDK links dropped; new links to Plugins, Models, OpenAI Status, and Dots (chatgpt.com/features/dots); "Subscribe / Get OpenAI for Business updates" block added to ~374 pages; ~319 pages show help-center links with "(opens in a new window)".
- **Listing/related-card refreshes** on ~900 pages: recent-post cards now show Oct 23–29 items (Model Spec update, ServiceNow, Oracle, NASK, Ropes & Gray, GPT-6.1 Terra), replacing Sep 22 cards (GPT-6 Sol and Luna, prompt caching).
- Heavy content diffs on a few older pages (e.g. `/index/learning-to-reason-with-llms/`, `/index/introducing-deep-research/`, `/policies/supplier-code/`, `/policies/cookie-policy/`) are large-line-count but mostly re-rendering/format churn; not individually reviewed. Pages with substantive-looking diffs after removing shared nav lines: 942 (most are the recent-post cards).

## New pages (136)
Headline launches: GPT-6.1 Sol (near GPT-6 Astra on agentic coding at ~1/5 the price; cached input $0.10/M tokens); GPT-6.1 Terra (fast/cheap, computer use, visual reasoning); **Dots** (always-on agents on GPT-6 Astra with own cloud computer, 4,000+ app connections via plugins); GPT-6 and "Intelligent UI" for all ChatGPT users (1.2B weekly); DevDay 2026 recap (20+ announcements) and `/devday/2026/`; Decisions API; updated Model Spec (Oct 29; five values); OpenAI models coming to Google Cloud Model Garden; Orchestra Bio acquisition (folds into Rosalind life-sciences); ServiceNow, Oracle, Atlassian, Uber ChatGPT Work partnerships; OpenAI Private Intelligence; OpenAI Marketplace; ChatGPT Ads expanding to 26 countries + new ads formats/ad-stack engineering post; security/safety posts (frontier-model misalignment detection, securing training environment, distillation-campaign disruption, false-front operations, Patch the Planet, safety cases); Codex Originals / Ambassadors; policies (Brazil advertising terms, Sign in with ChatGPT terms, ROW privacy policy); ~25 customer stories and ~13 new plugin pages (Oracle NetSuite suite, Atlassian, Krea, Alpaca, WordPress.com…); 14 `learn-demos` pages; 6 new partner pages (Bishop Fox, SpecterOps, TrustedSec, Insight, MegazoneCloud, Affinda).

## Removals (14)
Partner pages canva, dropbox, gusto, hubspot, quickbooks, stripe, pathfindr (→ replaced by `/business/partners/affinda/`, "formerly Pathfindr"); plugins atlassian-rovo (→ atlassian), mcp-server-for-wordpress and wordpress-com (→ `/business/plugins/wordpress/`), oracle-analytics (→ oracle-analytics-cloud); `/economic-research-exchange/` (→ `/economic-research-collaborators/`); `/form/ultrafast/`; `/prism/`. Last snapshots are in git history.
