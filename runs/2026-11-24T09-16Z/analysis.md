# Run 2026-11-24T09-16Z — analysis

- **Sitemap fetch time (observation):** 2026-11-24T09:17:17Z
- **Page fetches:** 2026-11-24 ~09:20–09:55Z, 2,088 pages (367 added + 1,721 updated) via `tools/html_to_md.py`, **0 fetch failures**
- **Baseline:** `2026-09-28T09-17Z` (the latest snapshot on `main`; **57 days old**)
- **Secondary comparison:** the `2026-11-23T09-15Z` snapshot on the unmerged branch `claude/festive-wright-kev5hz` (draft PR #203), used to isolate what changed in the last ~24h.

## 0. Process anomaly — the baseline is stale because daily runs aren't being merged

Every daily run since 2026-09-29 has pushed its own branch and opened a draft PR (#148 → #203), but **none have been merged into `main`**. Each new run therefore starts from the Sep 28 snapshot and re-reports the same ~8 weeks of changes (yesterday's #203: 363 added / 1,720 updated / 32 removed; today: 367 / 1,721 / 32). This run does the same, as instructed (baseline = `latest.xml` on the working branch, which forks from `main`). **Fix:** merge one recent run PR (e.g. this one) into `main` and close the rest; tomorrow's diff will then be a true one-day delta.

## 1. Anomalies

1. **Observation gap (57 days).** "first_seen = 2026-11-24T09-16Z" for the 367 new URLs only means "appeared sometime after Sep 28". Their own bylines date them Sep 29 – Nov 23. Changes made and reverted inside the gap are invisible from `main`.
2. **`<lastmod>` moved backwards vs. yesterday's (unmerged) snapshot:** `/index/retell-ai/` claimed `2026-11-17T21:23:47.320Z` on Nov 23 and now claims `2026-10-30T02:55:47.970Z`. vs. `main` it's an ordinary forward move, so it isn't flagged in the main-baseline set. Rendered content vs. Nov 23 is identical — looks like a republish/restore that reset the timestamp.
3. **92 URLs have no `<lastmod>` at all.** These include the launch posts for GPT‑6.1 Sol, GPT‑6.1 Terra and GPT‑6.2 Astra/Sol, `/index/research-acceleration-jagged-frontier/`, the entire new `/safety-alignment/` hub (with 27 misalignment reports), six `/ads/` pages and seven `/supply/` merch items. OpenAI makes no modification claim for them, so their edits can only be tracked by content diff. Full list in `diff.json`.
4. **3 URLs disappeared and came back** (per `state/known_urls.json`): `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
5. **13 URLs migrated between sub-sitemaps** with no overlap (others are cross-listed). Mostly plugin pages re-categorised into `plugins-sales-commerce` (Gong, Outreach, Seismic, Zoom Revenue Accelerator), and webinars/guides moved out of `page` into `learn-webinars` / `learn-guides`.
6. **3 new sub-sitemaps:** `learn-demos`, `safety-and-alignment`, `science` (42 → 45).
7. No future-dated `<lastmod>` values. No new URL whose `<lastmod>` predates the baseline.

Full anomaly entries:

- `reappeared` — https://openai.com/business/plugins/alpaca/ — previously first_seen 2026-07-10T09-16Z last_seen 2026-09-24T09-16Z
- `reappeared` — https://openai.com/form/codex-ambassadors/ — previously first_seen 2026-05-07T09-01Z last_seen 2026-06-24
- `reappeared` — https://openai.com/policies/row-privacy-policy/ — previously first_seen 2026-05-07T09-01Z last_seen 2026-05-27T09-17Z
- `sitemap_migration` — https://openai.com/business/learn/agent-security-enterprise/ — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-guides.xml']
- `sitemap_migration` — https://openai.com/business/plugins/parallel-search/ — ['sitemap.xml_plugins-engineering-it.xml'] -> ['sitemap.xml_plugins-productivity.xml']
- `sitemap_migration` — https://openai.com/business/plugins/sync-labs/ — ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-design-creative.xml']
- `sitemap_migration` — https://openai.com/business/learn/download-the-chatgpt-work-guide-for-sales-teams/ — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-guides.xml']
- `sitemap_migration` — https://openai.com/business/plugins/zoom-revenue-accelerator/ — ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `sitemap_migration` — https://openai.com/business/plugins/gong/ — ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `sitemap_migration` — https://openai.com/business/learn/how-our-sales-team-uses-chatgpt-work/ — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/plugins/outreach/ — ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `sitemap_migration` — https://openai.com/business/learn/how-our-finance-team-uses-chatgpt-work/ — ['sitemap.xml_learn-guides.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/learn/intelligence-at-work-cyber/ — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/learn/intelligence-at-work-financial-services/ — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/plugins/tableau/ — ['sitemap.xml_plugins-data-research.xml'] -> ['sitemap.xml_plugins-productivity.xml']
- `sitemap_migration` — https://openai.com/business/plugins/seismic/ — ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']

## 2. What changed in the last ~24h (vs. the unmerged 2026-11-23 snapshot)

**4 genuinely new URLs:**
- [`/index/introducing-shirudo/`](../../pages/openai.com/index/introducing-shirudo/index.md) — *OpenAI and Cisco introduce Shirudo* (byline Nov 23). An open-source (BSD-2/GPL for BPF parts) eBPF runtime that lets operators deploy temporary "shields" that block an exploit on a running Linux service without patching or restarting. Claims a Codex-generated shield blocked a "Java4Shell" exploit on a live Elasticsearch service. Quotes Greg Brockman. Fits the long Daybreak / cyber-defence run of posts (GPT‑6 Cyber, Daybreak Red/Blue, Cisco cyber, NATO).
- [`/openworks/`](../../pages/openai.com/openworks/index.md) — *Introducing OpenWorks*: OpenAI funds a nationwide network of "OpenWorks Partners" (local AI consultants) who give free, hands-on AI help to independent US small businesses. Pilot live in 20 cities (Chicago, Fargo, Charleston, Austin, Seattle, NYC…). Excludes SaaS, VC-backed and PE-owned businesses. Pairs with the recent small-business posts (`/index/helping-small-businesses-put-ai-to-work/`, `/index/ai-first-hire-small-business/`).
- [`/business/learn/connected-intelligence-for-in-house-legal/`](../../pages/openai.com/business/learn/connected-intelligence-for-in-house-legal/index.md) — webinar page (OpenAI + LECG + Cooley) on AI for in-house legal teams. The `/business/learn/` hub now links here instead of an external Goldcast URL.
- [`/business/customer-stories/richpanel-ai-customer-support/`](../../pages/openai.com/business/customer-stories/richpanel-ai-customer-support/index.md) — Richpanel automates 50% of customer support within 30 days (money-back guarantee) using GPT‑6 Astra / GPT‑6.1 Sol for its setup agent and GPT‑6 Luna for conversations.

**133 `<lastmod>` bumps since Nov 23**, of which ~110 `/index/` posts all got timestamps between 05:42 and 05:45Z on Nov 24, a bulk re-publish. Of all 1,721 re-fetched pages, compared with the Nov 23 snapshot: 1,404 identical; 168 changed **only image URLs** (a sitewide move from `images.ctfassets.net` (the Contentful CMS CDN) to `cdn.openai.com/...` — possibly the start of a migration off Contentful's asset CDN); 144 changed only "Keep reading" recirculation cards; **5 had real edits:**
- [`/business/pricing/`](../../pages/openai.com/business/pricing/index.md): new **"Limited-time offer: Get 2× usage"** banner. New ChatGPT Business workspaces created by **Nov 30** get double the included usage on Standard and Premium seats through **Dec 31**. Also added a "Dots, your always-on agents" feature bullet.
- [`/index/chatgpt-for-academic-researchers/`](../../pages/openai.com/index/chatgpt-for-academic-researchers/index.md): added an "Apply here" link to a verification flow, and replaced the "eligible institutions" list link with a rule: *recognized, degree-granting colleges or universities with a high level of research activity*. That means eligibility is now defined by rule rather than by a hand-picked list.
- [`/business/plugins/data/`](../../pages/openai.com/business/plugins/data/index.md): added a "How to videos" section (Data Agent, connecting team data, dashboards, reports in "ChatGPT Space").
- [`/safety/prompt-injections/`](../../pages/openai.com/safety/prompt-injections/index.md): finally picked up the new site menu (GPT‑6.2 / GPT‑6.1 Sol / GPT‑6 Astra replacing GPT‑5.5 / GPT‑5.4). One of the last stragglers.
- [`/business/learn/`](../../pages/openai.com/business/learn/index.md): webinar card re-pointed to the new on-site page (above).

## 3. Significant changes since the Sep 28 baseline (cumulative)

All 1,721 updated pages differ from the Sep 28 snapshot, at least because the site menu changed on every page. Headline items, re-checked against today's fetched markdown:

- **New models:** [GPT‑6.1 Sol](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md) (nearly Astra-level at one-fifth of Astra's token price; $2.00 per million input tokens), [GPT‑6 for everyone](../../pages/openai.com/index/gpt-6-for-everyone/index.md), [GPT‑6.1 Terra](../../pages/openai.com/index/introducing-gpt-6-1-terra/index.md), [GPT‑6 Cyber](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md), [Images 2.6](../../pages/openai.com/index/introducing-images-2-6/index.md), [GPT‑6.2 Astra and Sol](../../pages/openai.com/index/introducing-gpt-6-2-astra-sol/index.md).
- **Products / platform:** [DevDay 2026 recap](../../pages/openai.com/index/devday-2026-recap/index.md), [dots](../../pages/openai.com/index/introducing-dots/index.md), [ChatGPT Wallet](../../pages/openai.com/index/introducing-chatgpt-wallet/index.md) (+ new Wallet terms and privacy notice), [Businesses in ChatGPT](../../pages/openai.com/index/introducing-businesses-chatgpt/index.md), [ChatGPT for Sales](../../pages/openai.com/index/introducing-chatgpt-for-sales/index.md), [Decisions API](../../pages/openai.com/index/decisions-api/index.md), [Marketplace](../../pages/openai.com/business/marketplace/index.md), [Private Intelligence](../../pages/openai.com/business/private-intelligence/index.md), Sign in with ChatGPT terms.
- **Corporate:** acquisitions of [Orchestra Bio](../../pages/openai.com/index/openai-to-acquire-orchestra-bio/index.md) and [Pierre](../../pages/openai.com/index/openai-to-acquire-pierre/index.md); [Jill Hazelbaker](../../pages/openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer/index.md) and [Dan Driscoll](../../pages/openai.com/index/dan-driscoll-joins-openai/index.md) hires; partnerships with Google Cloud, Atlassian, Oracle, ServiceNow, Le Figaro, LVMH Media, Chile.
- **Safety:** new [`/safety-alignment/`](../../pages/openai.com/safety-alignment/index.md) hub with 27 "misalignment reports" (incidents where models e.g. bypassed network restrictions, exposed a GitHub token, suppressed monitoring alerts, or used a funded test crypto wallet without authorization); [How we detect frontier model misalignment](../../pages/openai.com/index/how-we-detect-frontier-model-misalignment/index.md); [Updated Model Spec](../../pages/openai.com/index/updated-model-spec/index.md); two anti-distillation posts.
- **Policies:** [Usage Policies](../../pages/openai.com/policies/usage-policies/index.md) new version **effective Nov 20, 2026**. [Privacy Policy](../../pages/openai.com/policies/privacy-policy/index.md) no longer mentions Sora (3 mentions on Sep 28 → 0). [Trust & Transparency](../../pages/openai.com/trust-and-transparency/index.md) now reports 620 non-content and 146 content government data requests.
- **Policy advocacy:** ["Fair use benefits everyone"](../../pages/openai.com/index/fair-use-benefits-everyone/index.md), [AI-training preferences for websites](../../pages/openai.com/index/helping-websites-express-ai-training-preferences/index.md), [Children First declaration](../../pages/openai.com/index/children-first-declaration/index.md).

A deeper page-by-page reading of the Sep 28 → Nov 23 changes is in the unmerged run `runs/2026-11-23T09-15Z/analysis.md` on branch `claude/festive-wright-kev5hz` (PR #203). The findings above that were re-checked today still hold.

## 4. Routine updates

~1,000 pages changed only in site menu and "Keep reading" cards. 329 plugin listings were refreshed from a template. 168 pages changed only image CDN URLs since yesterday.

## 5. New pages (367 vs. main baseline)

By section: 148 `/index/` posts, 59 `/business/plugins/`, 56 `/safety-alignment/`, 30 `/business/learn/`, 11 customer stories, 8 `/business/solutions/`, 9 `/policies/`, 8 `/form/`, 6 `/business/partners/`, 6 `/ads/`, 7 `/supply/` merch, plus `/openworks/`, `/compute-campus/`, `/cybersecurity/`, `/cyber-at-the-frontier/`, `/daybreak/red-team/`, `/devday/2026/`, `/codex-originals/`, `/science/researcher-access/`, `/news/science/`. Full list in `diff.json`.

## 6. Removals (32 vs. main baseline)

Per the Nov 23 run's checks, most redirect to a new location (`/solutions/*` → `/business/solutions/*`, old webinars → `/business/learn/*`, `/safety/` → `/safety-alignment/`, `/prism/` → `/science/`, `/residency/` → `/research/`). The rest (several `/business/partners/*` and plugin pages) return 404. I could not re-check redirects today: requests made without following redirects get Cloudflare 403s. The last snapshot of each removed page is in git (`git log -- pages/openai.com/<path>.md`).

- https://openai.com/business/enabling-a-data-driven-workforce-webinar/
- https://openai.com/business/fine-tuning-gpt-4o-webinar/
- https://openai.com/business/guides-and-resources/how-openai-uses-codex/
- https://openai.com/business/guides-and-resources/identifying-and-scaling-ai-use-cases/
- https://openai.com/business/new-in-chatgpt-for-business-april-updates-2025/
- https://openai.com/business/new-in-chatgpt-for-work-march-updates-2025/
- https://openai.com/business/partners/canva/
- https://openai.com/business/partners/dropbox/
- https://openai.com/business/partners/gusto/
- https://openai.com/business/partners/hubspot/
- https://openai.com/business/partners/pathfindr/
- https://openai.com/business/partners/quickbooks/
- https://openai.com/business/partners/stripe/
- https://openai.com/business/plugins/atlassian-rovo/
- https://openai.com/business/plugins/litera-lito/
- https://openai.com/business/plugins/mcp-server-for-wordpress/
- https://openai.com/business/plugins/oracle-analytics/
- https://openai.com/business/plugins/wordpress-com/
- https://openai.com/daybreak/partners-new/
- https://openai.com/economic-research-exchange/
- https://openai.com/form/data-partnerships/
- https://openai.com/form/ultrafast/
- https://openai.com/index/ada/
- https://openai.com/index/blue-j/
- https://openai.com/prism/
- https://openai.com/residency/
- https://openai.com/safety/
- https://openai.com/solutions/blueprints/knowledge-retrieval/
- https://openai.com/solutions/industries/financial-services/
- https://openai.com/solutions/industries/retail/
- https://openai.com/solutions/use-case/content-creation/
- https://openai.com/solutions/use-case/data-analysis/