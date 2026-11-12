# Run 2026-11-12T09-16Z — analysis

- **Sitemap fetch time (observed):** 2026-11-12T09:17:22Z UTC (root index + 43 sub-sitemaps, all fetched OK)
- **Page fetch window (observed):** 2026-11-12 ~09:17–09:22Z UTC, 1,934 pages via `tools/html_to_md.py` (curl-cffi), **0 fetch failures**
- **Formal baseline:** `2026-09-28T09-17Z`, the last run merged to `main`
- **Day-over-day comparison:** `2026-11-11T09-16Z`, yesterday's snapshot on the unmerged branch `claude/festive-wright-m3wmgn`

> **Why two baselines?** The daily runs from 2026-09-29 to 2026-11-11 were each committed to their own PR branch, and none of those PRs have been merged. So `main` (and the `sitemaps/.../latest` files this run started from) still reflect 2026-09-28. The formal diff (`added`/`removed`/`updated` in `diff.json`) is therefore cumulative over ~6.5 weeks. To report what actually changed **today**, this run also diffed against yesterday's unmerged snapshot (`since_prior_unmerged_run` in `diff.json`). The narrative below focuses on the day-over-day changes.

## 1. Anomalies

### Since yesterday (2026-11-11 → 2026-11-12)
- **None.** No future-dated `<lastmod>`, no `<lastmod>` moving backwards, no removals, no URLs reappearing, no sub-sitemap migrations, no new or missing sub-sitemaps (43 → 43).
- Minor timestamp note: the one new URL, [`/index/jiostar-vijay-seshadri/`](../../pages/openai.com/index/jiostar-vijay-seshadri/index.md), has `<lastmod>` 2026-11-12T05:51:15Z, but the page's own date line reads "November 11, 2026". That's a normal Pacific-time vs UTC publishing offset, not an anomaly.

### Cumulative vs the 2026-09-28 merged baseline (83 flagged; all previously reported by the unmerged runs)
- **56 × backdated_new_url**: new URLs whose `<lastmod>` is more than 3 days older than their first_seen in this repo's merged state. **These are almost all artifacts of the 45-day merge gap** (first_seen can only be recorded once a run's state lands on `main`). Not evidence of backdating by OpenAI.
- **3 × reappeared_url**: `/business/plugins/alpaca/`, `/form/codex-ambassadors/`, `/policies/row-privacy-policy/` (first reported 2026-11-10).
- **23 × sub_sitemap_migration**: mostly `/business/learn/*` pages leaving the catch-all `page` sitemap for the `learn-guides`/`learn-webinars` sitemaps, older `/index/` guides being *added* to `learn-guides` in addition to their existing listing, five plugins re-categorised (gsc-wizard, klaviyo, parallel-search, sync-labs, tableau), and one Russia influence-campaign report moving from `global-affairs` to `safety`. All already present in yesterday's snapshot.
- **1 × new_sub_sitemap**: `learn-demos` (present since at least 2026-11-10).
- Cumulative removals (29) include 13 URL relocations to `/business/...` reported yesterday. See the 2026-11-11 analysis on its branch.

## 2. Significant updates (since yesterday)

### [`/devday/2026/`](../../pages/openai.com/devday/2026/index.md): 8 more session descriptions published
(`<lastmod>` 2026-10-31T08:45Z → 2026-11-11T22:02Z.) The DevDay 2026 hub gained eight session cards, presumably as session recordings and write-ups are posted:
- *Build What's Next on the ChatGPT Platform with Plugins*: bringing tools into ChatGPT **and Codex** as plugin extensions.
- *What Will You Build With Coding Agents That Don't Quit?*: describes **"a Codex run that spent over 1,000 hours keeping builds and tests passing"**, with advice on token budgets and when engineers should step in.
- *Harness-as-a-Service: Building with the Agents API*: run the **Codex harness via an "Agents API"** in your own environment, with long-running tasks and a split between what OpenAI manages and what you manage.
- *Sites and the Next Generation of Web Apps*: interactive web experiences with **Astra, "ChatGPT Sites", and WebMCP**.
- *What Comes After Loops?: Deep Dive Into Agentic Architecture*: from single agent loops to collaborating agents.
- *Codex Security: From Vulnerability to Verified Fix*: OpenAI's cyber models plus an **open-source CLI and SDK** for scanning codebases and PRs and verifying fixes.
- *Building with GPT-Live and Image Generation*: voice agents ("GPT‑Live") that create images and coordinate background work.

All of these product names (ChatGPT Sites, WebMCP, the Agents API, GPT‑Live) already appear elsewhere on the site, so these cards add detail and are not new product reveals.

### [`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md): "Business Hub in ChatGPT" listed as GA (Nov 10)
(`<lastmod>` 2026-11-10T00:01Z → 2026-11-12T02:06Z.) A new top entry dated **Nov 10, 2026, tagged ChatGPT / GA**: "Business Hub" lets business owners claim their business in ChatGPT. After **identity verification with Persona** they can publish business info, connect a product feed, and see insights (mentions, website clicks). Eligible **US e-commerce and online-service businesses** can create a business agent. It's opened from the ChatGPT web sidebar. This is the release-notes counterpart to yesterday's "Introducing Businesses in ChatGPT" post. One notable detail: the blog post called it a **beta**, but the release notes label it **GA**, and the release notes name **Persona** as the identity-verification vendor. The oldest entry (Nov 2 Codex iOS update) rolled off the bottom of the page, which is the normal rolling window.

### [`/index/chatgpt-plus-for-veterans/`](../../pages/openai.com/index/chatgpt-plus-for-veterans/index.md): post-holiday wording edit
The phrase "As Veterans Day approaches," was removed from the intro now that Veterans Day (Nov 11) has passed. The rest of the page is unchanged.

## 3. Routine updates (since yesterday)
- [`/index/australian-universities-ai-native-graduates/`](../../pages/openai.com/index/australian-universities-ai-native-graduates/index.md): footnote markup changed from an asterisk to a numbered footnote ("1"). The survey methodology text (Pureprofile, 1,018 students, 3–7 Aug 2026) is unchanged.
- **24 URLs** bumped `<lastmod>` with **zero rendered-content difference** from yesterday's markdown, which is cache/CMS regeneration noise: `/business/businesses-in-chatgpt/`, `/business/plugins/`, `/business/plugins/aiva/`, `/business/plugins/luma-health/`, `/business/plugins/stedi/`, `/business/plugins/subsalt/`, `/business/plugins/turquoise-health/`, `/business/plugins/uptodate-expert-ai/`, `/company/public-policy/`, `/index/a-thousand-fewer-paths-to-root/`, `/index/ai-effect-on-freelance-work/`, `/index/coderabbit-codex-daybreak/`, `/index/control-room/`, `/index/cultfit-builds-with-codex/`, `/index/gilbert-tobin-sam-nickless/`, `/index/helping-caregivers-use-ai-in-everyday-life/`, `/index/introducing-businesses-chatgpt/`, `/index/lifeval/`, `/index/merge-builds-with-openai/`, `/index/singapore-airlines-travel-work/`, `/policies/businesses-in-chatgpt/`, `/policies/service-terms/`, `/signals/`, `/signals/research/`.
  Note: the six healthcare plugins added yesterday (Aiva, Luma Health, Stedi, Subsalt, Turquoise Health, UpToDate Expert AI) plus `/business/plugins/` all bumped together at ~06:08Z today, consistent with a batch republish of the plugin directory with no visible change.

## 4. New pages (since yesterday)

### [JioStar's chief architect on AI discovery at 500M-user scale](../../pages/openai.com/index/jiostar-vijay-seshadri/index.md)
`/index/jiostar-vijay-seshadri/` · `<lastmod>` 2026-11-12T05:51Z · page dated November 11, 2026 · sub-sitemap `page` · first_seen {RUN}

An "Executive Function" series interview, recorded at OpenAI's Executive Summit in Singapore, with Vijay Seshadri, Chief Architect at JioStar (the Indian streaming/live-sports company behind JioHotstar). Key claims:
- JioStar serves **500M+ consumers** and has peaked at **72.5M concurrent live-sports viewers**.
- Using the **OpenAI API**, they built a voice-and-visual discovery assistant for movies, shows, live-match moments and **cricket statistics**, in **15+ languages, in about eight weeks**, ahead of a major February cricket tournament. OpenAI forward-deployed engineers worked with them, and Codex helped generate eval cases.
- **60%+ of users choose voice over text.**
- Lessons: "evals, evals, and evals", a maker-checker / LLM-as-judge validation design, guardrails defined first, and monitoring of model efficacy in production (not only latency).
- Audience: enterprise executives (Asia-Pacific; tags Media/Entertainment/Sport; products API, Codex).

Context: this fits OpenAI's steady stream of customer stories and executive interviews (yesterday: Gilbert + Tobin CEO interview, Singapore Airlines, Cogent Security). It's the second item in two days tied to the Singapore executive event and APAC enterprise customers.

## 5. Removals (since yesterday)
None.

## Stats
| | vs 2026-09-28 (merged baseline) | vs 2026-11-11 (yesterday, unmerged) |
|---|---|---|
| Total URLs now | 2,171 | 2,171 (was 2,170) |
| Added | {len(d['added'])} | 1 |
| Updated (`<lastmod>` changed) | {len(d['updated'])} | 28 (4 with rendered changes) |
| Removed | {len(d['removed'])} | 0 |
| Anomalies | {len(an)} | 0 |
| Sub-sitemaps | 43 (baseline had 42) | 43 |
| Page fetch failures | 0 / 1,934 | — |
