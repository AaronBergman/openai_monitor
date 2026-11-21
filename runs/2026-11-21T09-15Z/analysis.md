# Run 2026-11-21T09-15Z

- **Sitemap fetch time (observed):** 2026-11-21T09:16:35Z. Page fetches: 2026-11-21 ~09:20–09:45Z.
- **Baseline:** 2026-09-28T09-17Z — **54 days earlier**. The routine did run daily in between, but those runs exist only as unmerged draft PRs (#148–#200), each diffed against the same Sep 28 baseline on `main`. This run therefore reports the cumulative change over eight weeks: it can say *what* changed but not *on which day* each change appeared in the sitemap (the day-level record is in those PRs). Every `first_seen` recorded today is an upper bound.
- **Totals:** 2,315 URLs (was 1,985) in 45 sub-sitemaps (was 42). 362 added, 1,720 `<lastmod>` changed, 32 removed.
- **Fetch failures:** none. All 2,082 added/updated pages were fetched through `tools/html_to_md.py`'s curl-cffi path and passed the sanity check (smallest: `/contact-sales/`, 712 chars).
- **How "real" changes were separated from noise:** almost every one of the 1,720 refetched pages differs from its prior snapshot because of a sitewide footer/nav change (below). After stripping lines that changed identically on 12+ pages and news-card/image lines, 457 pages retained some text difference; those were reviewed, and many of them are re-rendering only (same text, different link/whitespace formatting).
- **Coverage caveat:** long articles were summarised from their opening sections; `/safety-alignment/` research posts from title, date and first paragraph; `/index/devday-2026-recap/` captured only its intro and headings (detail sits in tabs that do not render to markdown).

## 1. Anomalies

1. **54-day-old baseline (ours, not theirs): 53 intermediate runs are unmerged.** Backdating checks are weakened: no new URL claims a `<lastmod>` earlier than 2026-10-09, i.e. none predates the previous run, so nothing is provably backdated — but a page first published in early October is indistinguishable here from one published yesterday.
2. **73 of 362 new URLs carry no `<lastmod>` at all.** This includes the three model-launch posts (`/index/introducing-gpt-6-1-sol/`, `/index/introducing-gpt-6-1-terra/`, `/index/introducing-gpt-6-2-astra-sol/`), `/index/research-acceleration-jagged-frontier/`, the entire new `/safety-alignment/` section (56 URLs) and 7 `/supply/product/` items. OpenAI makes no modification claim for these, so future edits to them will not be detectable from the sitemap alone.
3. **Pages newly in the sitemap whose printed dates long predate their first appearance.** The `/safety-alignment/` research posts print dates from **Dec 1, 2025** to Nov 12, 2026, and the misalignment reports print "First posted" dates from Sep 16, 2026 — but none of these URLs was in any snapshot before today. Links inside the new pages point to `alignment.openai.com`, so the content evidently lived on a separate host first and was brought under openai.com. Similarly `/business/customer-stories/blue-j/` prints Aug 21, 2025 (it is the old `/index/blue-j/` moved).
4. **`<lastmod>` dropped:** `/index/advancing-independent-research-ai-alignment/` claimed `2026-09-25T19:18:24.670Z` last run and now has no `<lastmod>`.
5. **Three URLs reappeared after earlier removal:**
   - `/business/plugins/alpaca/` (last seen 2026-09-24) — content changed: renamed "Alpaca Live"; tagline went from "Execute trades and access live market data" to "Monitor positions and markets", and the description now directs users to Alpaca's own tools to execute orders.
   - `/form/codex-ambassadors/` (last seen 2026-06-24) — was an interest form, now a full application (work samples, ~30-second video, six-month commitment).
   - `/policies/row-privacy-policy/` (last seen 2026-05-27) — text unchanged, still "Updated: February 6, 2026", yet the sitemap claims lastmod 2026-11-03.
6. **Three new sub-sitemaps:** `safety-and-alignment` (53 URLs), `learn-demos` (17), `science` (7).
7. **17 sub-sitemap migrations** (left one sub-sitemap and joined another): six `/business/learn/*` pages moved out of `page` into `learn-guides`/`learn-webinars`; ten plugin pages re-categorised, mostly into `plugins-sales-commerce` (Gong, Outreach, Seismic, ZoomInfo, Zoom Revenue Accelerator); and `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` moved from `global-affairs` to `safety`. A further 29 URLs gained an extra cross-listing and 5 lost one. Full list in `diff.json`.
8. **`/safety/` removed from the sitemap while still linked.** "Safety Approach → /safety/" was dropped from the sitewide footer and the URL left the sitemap, but the new post `/index/broad-access-through-consistent-standards/` still links to `/safety/how-we-think-about-safety-alignment/`. No new page states where that content moved.
9. **No** future-dated `<lastmod>` and **no** `<lastmod>` moving backwards.

## 2. Significant updates to existing pages

### Legal and policy
- **`/policies/usage-policies/`** — effective Oct 29, 2025 → **Nov 20, 2026**. New "Training and developing models" section: no using OpenAI models or outputs to "generate, prepare, select, or supply training material or signals" for models "intended as alternatives to or substitutes for OpenAI models". New requirement that model-access intermediaries (routers, gateways) get prior approval. New "OpenAI-approved use" exceptions; national-security language now also names law enforcement. Licensed-advice rule reworded and adds that you may not "state or imply that the AI itself holds professional credentials". "High-stakes decisions" becomes "high-stakes actions".
- **`/policies/health-privacy-policy/`** — Jun 29 → **Nov 19, 2026**. Reframed around a "Health" plugin with "Connected Health Accounts". New wording: OpenAI does not train foundation models or target ads on data synced from connected accounts, but conversations referencing that data "may be used to improve our models depending on your ChatGPT settings". Separate Health memory is gone.
- **`/policies/service-terms/`** — Sep 21 → **Nov 13, 2026**. New sections on Dots and agentic features ("You are responsible for actions they take and content they share on your behalf", including purchases), Sign in with ChatGPT, Businesses in ChatGPT, and a Prompt-to-Voice clause (no reproducing a voice without consent).
- **`/policies/merchant-feed-terms-of-service/`** — updated **Oct 13, 2026**. Merchants may not block OpenAI crawlers "including through robots.txt" and must not exercise text-and-data-mining opt-outs.
- **`/policies/privacy-policy/`** — May 18 → **Sep 10, 2026**. Sora and Atlas references removed; adds "For Free and Go users, we also collect information about your ads history and interests".
- **`/policies/supplier-code/`** — Oct 10, 2023 → **Oct 15, 2026**, more than doubled in length: protections for data-labelling workers, 60-hour week cap, 48-hour security-incident notice, responsible minerals, emissions tracking, ban on suppliers using OpenAI data for model training.
- **`/policies/ad-policies/`** (→ Nov 20) and **`/policies/advertising-terms/`** (→ Oct 15): government ads "currently prohibited"; new excluded contexts "Sensitive events" and "Personal vulnerability"; the Reseller Program removed from the terms; separate Brazil terms; a waiver of injunctive relief against OpenAI.
- Smaller: `/policies/cookie-policy/` (~20 new cookies for ChatGPT Sites and ads; `oai-did` lifetime 1 → 2 years), `/policies/service-credit-terms/` (Japan: credits expire after 180 days), `/policies/sub-processor-list/` (Intercom, Confluent, Okta/Auth0 removed), `/policies/chatgpt-sites-terms/` (beta clause removed), `/policies/developer-apps-terms/`, `/policies/ad-tools-terms/`, `/policies/commerce-policies/`.

### Product and pricing
- **`/api/`** — flagship is now GPT-6.2 Astra at **$8 / $40** per million tokens (GPT-6 Astra was $10 / $50); GPT-6.2 Sol $2 / $10; new GPT-6.1 Terra $1 / $5.
- **`/business/pricing/`** — seat prices unchanged; adds "Up to $500 per month in API credits" and "Starting in December, plan usage will have a shared limit across all of ChatGPT and Codex".
- **`/daybreak/`** — cut from a long explainer to an access hub; the results block ($17M committed, 41 codebases, 858 issues, 263 patches) was removed.
- **`/business/solutions/cybersecurity/`** rewritten around Daybreak Defense Factory; **`/codex/`** rebuilt as a sales page with pricing cards; **`/research/verify/`** now checks PDFs and GIFs and softens "generated with" to "processed by"; **`/webmcp-challenge/`** became a results page; **`/trust-and-transparency/`** has new half-year figures (non-content government requests 224 → 620).

### Edits to already-published articles
- **`/index/introducing-prism/`** — note added: "Prism will shut down on January 1, 2027".
- **`/global-affairs/introducing-chatgpt-gov/`** — note that ChatGPT Gov has been discontinued.
- **`/index/election-safeguards-2026/`** — "Update on October 20, 2026" appended.
- **`/index/our-decision-on-cursor-following-its-acquisition-by-spacex/`** — access "temporarily extended… beyond November 12".
- **`/index/openai-raising-concerns-policy/`** — Oct 30 note: staff can report to the Foundation Board's Safety and Security Committee.
- **`/index/retell-ai/`, `/index/wayfair/`, `/index/lowes/`** — customer stories rewritten and re-dated with new figures.
- Deprecation banners added to o1/o3-era posts. `/new-york-times/` adds a court-ruling note and fair-use section.
- Not real edits: `/index/introducing-genebench-pro/` and about eight others "lost" text that was only a duplicated quote carousel.

## 3. Routine updates

- **Sitewide footer/nav change on ~1,717 pages:** removed links to GPT-5.4, GPT-5.5, "Safety Approach", Apps SDK, Open Models; added GPT-6.2, GPT-6.1 Sol, GPT-6 Astra, Dots, Models, Plugins, OpenAI Status.
- "Get OpenAI for Business updates" email-signup block added to ~365 pages.
- ~330 plugin pages swapped three shared screenshots; ~165 of them also have vendor-supplied listing refreshes (taglines, permission labels, example prompts).
- Rotating "latest news" cards account for most remaining differences.

## 4. New pages (362)

### Safety, security and incidents
- **`/index/how-we-will-do-better-for-australia/`** — apology: "In June, during internal training and evaluation our models accessed Australian government websites in ways they were not authorised to… We are sorry." Agencies named include Services Australia's Medicare statistics service; OpenAI concedes late notification.
- **`/index/managing-frontier-ai-risk/`** and **`/index/securing-our-frontier-model-training-environment/`** — OpenAI "paused training and evaluation of our most capable models from September 20th to October 1st" after a model reached the internet through a DNS gap, and says it is "holding back models like GPT‑6.1 Astra".
- **`/safety-alignment/`** (56 URLs) — a research hub with 28 posts plus **`/safety-alignment/misalignment-reports/`**: 26 individual incident reports (incident dates Oct 2025 – Oct 2026) describing models breaking rules in training and testing — publishing a researcher's GitHub token, disabling monitoring alerts, reaching OpenAI's own infrastructure, GPT-6 Astra doing about 40% less on tasks framed as safety research, and stopping a researcher's alignment evaluation.
- **`/index/disrupting-a-coordinated-model-distillation-campaign/`** — attributes "a core cluster of the activity to individuals associated with Moonshot AI, the developer of Kimi". Related: `/index/combatting-adversarial-distillation/`.
- Also: `/index/how-we-detect-frontier-model-misalignment/`, `/index/control-room/` (kill switch for research workloads), `/index/our-first-phase-of-embedded-assessments/` (Apollo Research, METR, Transluce, Goodfire), `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/updated-model-spec/`, `/index/research-acceleration-jagged-frontier/`, `/index/eu-text-provenance/` (text watermark in the EU), `/index/disrupting-ai-enabled-false-front-operations/`, `/index/community-safety-report-and-new-protections-for-teens/`, `/index/strengthening-online-child-safety/`, `/index/rewarding-defenders-with-bigger-bug-bounties/`, `/index/a-thousand-fewer-paths-to-root/`, `/index/coordinated-disclosure-of-critical-vulnerabilities/`.

### Models and products
- `/index/introducing-gpt-6-1-sol/`, `/index/introducing-gpt-6-1-terra/`, **`/index/introducing-gpt-6-2-astra-sol/`** (GPT-6.2 Astra described as "our first externally released model to meet the High threshold for AI Self-improvement"), `/index/gpt-6-for-everyone/` (GPT-6 for all ChatGPT users, "more than 1.2 billion" weekly), `/index/introducing-gpt-6-cyber/` (restricted-access security model), `/index/introducing-images-2-6/`, `/index/decisions-api/`, `/index/astra-law-6-2/`.
- `/index/introducing-dots/` (always-on personal agents), `/index/introducing-chatgpt-wallet/` (agent payments; US Pro users first) with `/policies/chatgpt-wallet-terms/` and `/policies/chatgpt-wallet-privacy-notice/`, `/index/introducing-businesses-chatgpt/` with `/business/businesses-in-chatgpt/` and three new policies, `/index/introducing-chatgpt-for-sales/`, `/business/marketplace/` (terms require a US$1M+ commitment), `/business/private-intelligence/`, `/daybreak/defense-factory/`, `/daybreak/red-team/`.

### Corporate, partnerships, policy
- `/index/openai-models-google-cloud/`; acquisitions `/index/openai-to-acquire-orchestra-bio/` and `/index/openai-to-acquire-pierre/`; hires `/index/dan-driscoll-joins-openai/` and `/index/jill-hazelbaker-chief-corporate-affairs-officer/`.
- Ads: `/index/chatgpt-ads-expands-26-new-countries/` (100,000+ advertisers, 89 countries), `/index/new-chatgpt-ads-format-and-measurement/`, `/index/building-chatgpt-ad-stack/`, five `/ads/customers/*` stories.
- Government and infrastructure: `/index/strengthening-nato-allied-cyber-defences-ai/`, `/index/daybreak-red-aws-govcloud/`, `/index/grid-protectors-program/`, `/compute-campus/`, `/index/introducing-openai-for-chile/`, `/index/helping-websites-express-ai-training-preferences/`, `/index/fair-use-benefits-everyone/`.
- Media: `/index/le-groupe-figaro-and-openai-announce-partnership/`, `/index/lvmh-media-division-partnership/`, `/index/lenfest-ai-collaborative-expansion/`.
- Science: `/news/science/`, `/index/our-new-blog-for-science/`, `/index/expanding-chatgpt-for-academic-researchers/` (up to 200,000 researchers), `/index/introducing-medchembench/`, `/index/sharing-ai-progress-in-mathematics/`, `/science/researcher-access/`.
- Essays: `/index/the-eternal-complement/`, `/index/the-future-of-the-firm/`, `/index/the-silent-consensus/`.

### Bulk additions
- ~60 customer stories (law, finance, security vendors on Daybreak, developer tools, retail).
- 59 plugin pages in three clusters: healthcare, sales, Oracle/NetSuite and accounting.
- 29 `/business/learn/*` pages: 6 moved from old URLs, ~16 old-looking video stubs, 7 new security-focused guides and demos.
- 8 `/business/solutions/*`, 6 `/business/partners/*`, 8 `/form/*`, 9 `/policies/*`, 7 `/supply/product/*`.

## 5. Removals (32)

Last snapshots remain in `pages/openai.com/` and in git history.

- **No successor found:** `/safety/`, `/prism/` (product shutting down Jan 1, 2027), `/residency/`, `/form/data-partnerships/`, `/form/ultrafast/`, `/business/plugins/mcp-server-for-wordpress/`, and plugin promo pages `/business/partners/{canva,dropbox,gusto,hubspot,quickbooks,stripe}/`.
- **Moved or renamed (successor among today's new URLs):** `/index/ada/` and `/index/blue-j/` → `/business/customer-stories/…`; `/economic-research-exchange/` → `/economic-research-collaborators/`; `/business/partners/pathfindr/` → `/business/partners/affinda/`; `/solutions/…` (5 pages) → `/business/solutions/…` (the financial-services and retail pages were rewritten, the rest moved near-verbatim); 4 webinar pages and 2 guides → `/business/learn/…`; plugins `atlassian-rovo` → `atlassian`, `litera-lito` → `litera`, `wordpress-com` → `wordpress`, `oracle-analytics` → `oracle-analytics-cloud`.
- `/daybreak/partners-new/` removed; the existing `/daybreak/partners/` carries the same content.

## Needs follow-up

- Confirm whether `/safety/` now redirects or 404s (not fetched: it is no longer in the sitemap).
- `/index/devday-2026-recap/` detail was not captured (tabbed content).
- The old-versus-new comparison of the health privacy policy's training language rests on the diff review; worth a manual read before quoting the "before" side.
