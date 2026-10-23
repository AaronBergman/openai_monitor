# Run 2026-10-23T09-15Z Analysis

**Fetch time:** 2026-10-23T09:16:17Z (sitemaps) · pages fetched immediately after, 1,784 of 1,784 OK (0 failures)
**Baseline:** 2026-09-28T09-17Z — **25-day gap** (routine did not run 2026-09-29 → 2026-10-22; all changes in that window arrive in this one diff)
**Stats:** 2,086 total URLs (was 1,985) | 106 added | 1,678 updated | 5 removed | 36 anomaly records | 43 sub-sitemaps (was 42)

## Anomalies

- **Missed-days gap.** 25 days of changes landed at once. `<lastmod>` histogram of the 1,678 updates: 1 on 09-28, ~270 between 10-06 and 10-18, 59 on 10-19, 130 on 10-20, 208 on 10-21, 360 on 10-22, **767 on 10-23 (today, hours before fetch)** — a site-wide rebuild was rolling out as we fetched.
- **Site-wide template change.** 1,675 of the 1,678 updated pages changed nav/footer: new header links GPT-6.1 Sol and GPT-6 Astra (GPT-5.4 and "GPT-6" labels dropped), "Codex" now points to `https://chatgpt.com/codex/`, new footer links to Dots (`chatgpt.com/features/dots`), Plugins (`developers.openai.com/plugins`), Models, OpenAI Status; "Open Models" and "Apps SDK" links removed; external links now carry "(opens in a new window)". Carousel/“latest posts” widgets rotated and image alt-texts/CDN signatures were rewritten on hundreds of pages (e.g. generic alt text replacing descriptive names). All of this is noise for content purposes; ~1,069 pages have non-nav diffs, ~526 after also stripping carousels/images.
- **New sub-sitemap:** `sitemap.xml/learn-demos` (13 URLs, `/business/learn/*` demo videos such as "Automate complex workflows with OpenAI o3", "GPT‑5: Our best model for work"). Many of these are old (2024–25) demo pages that only now have sitemap entries.
- **19 URLs migrated between sub-sitemaps**, nearly all into the Learn family: 5 into `learn-guides` (from ai-adoption/applied-ai/global-affairs — e.g. `/index/managing-ai-investments-in-agentic-era/`, `/index/builders-guide-to-gpt-5-6/`), 7 into `learn-webinars` (from company/page/learn-guides — e.g. the two GPT‑4o-era webinars, `intelligence-at-work-*`), 4 from `global-affairs` into `global-affairs-news-listed`, 1 from global-affairs to `safety`. The Learn hub is being reorganised into guides/webinars/demos.
- **Reappeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27 — returns as a standalone "Privacy policy" for rest-of-world users).
- **Backdated new URLs (7)** (lastmod >7 days before first_seen, i.e. appeared in the sitemap well after claimed edit): `/form/private-intelligence-interest/` (lastmod 10-01, 22d), `/codex-originals/` (10-01, 21d), `/form/sign-in-with-chatgpt-interest/` (10-07, 16d), `/devday/2026/` (10-08, 14d), `/business/learn/board-guide-cybersecurity-ai/` (10-09, 14d), `/index/lenfest-ai-collaborative-expansion/` (10-09, 13d), `/index/teens-learn-and-plan/` (10-14, 8d). Unsurprising given the 25-day observation gap; first_seen here is the first *observation*, not the true go-live.
- **"Future" lastmods (5, benign):** `/signals/`, `/signals/research/`, `/collective-cyberdefense/application/`, `/index/introducing-gpt-live/`, `/index/strengthening-societal-resilience-with-rosalind-biodefense/` carry lastmods of 09:16:17–09:16:43Z, 0–26 s after run start but before those sub-sitemaps were fetched. The sitemap is generated live; these pages were being edited at that moment. No backwards lastmods.
- **Policy dated in the future:** `/policies/usage-policies/` now says "Effective: November 20, 2026" (28 days ahead) — published in advance with a link to the prior version. (Not a lastmod anomaly, but a forward-dated claim.)

## Significant updates

- **Usage Policies** (`policies/usage-policies/`): new version effective Nov 20, 2026 (prev Oct 29, 2025). Notable edit: the "tailored advice that requires a license" prohibition is reframed from *providing* such advice to *building or offering AI tools that provide others* such advice without licensed-professional involvement, plus a ban on stating/implying the AI itself holds professional credentials. Intro principles reworded.
- **Privacy policy** (`policies/privacy-policy/`): updated Sep 10, 2026 (was May 18). Sora dropped from the intro; ad-data language hardened from "may receive information from advertisers… to measure ads shown to Free and Go users" to "receive… for purposes described in this Policy including… improve our Services".
- **Cookie policy:** "Last updated" Sep 10 → Oct 7, 2026. New cookies for ads.openai.com (`oai-did`, `oai-anon-id`, `marketing_consent_source`), `oai-logged-out-consent-chosen`; `oai-did` lifetime 1y → 2y; Auth0 cookies on platform.openai.com removed.
- **Advertising Terms:** Aug 25 → Oct 15, 2026; points Brazil customers to the new `/policies/brazil-advertising-terms/`; Advertising-Intermediary clauses restructured (2.1 split into Authority and "Advertiser Vetting"). Together with new pages *ChatGPT Ads expands to 26 new countries* and *Building ChatGPT's ad stack*, ads is the most active policy area.
- **Service Terms:** Sep 21 → Oct 16; adds **Prompt-to-Voice** (synthetic voices from text prompts; no voice cloning of real people; excluded from OpenAI's IP indemnity).
- **Sub-processor list:** Jul 9 → Oct 14, 2026 (Cloudflare row split, region list; `us.api`/`eu.api` residency note). **Supplier Code of Conduct:** "Updated: Oct 10, 2023" → Oct 15, 2026, whole document rewritten.
- **Trust & transparency:** H1-2026 report data added (government requests; one metric 224 → 620).
- **Pricing (`business/pricing/`):** GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol, GPT-6 Luna and **Dots** added to plan feature tables ("Flexible" credits); Rosalind Academic Plan callout.
- **Codex landing (`codex/`):** retitled "Build anything with Codex", now shows Plus ($20/mo) and Pro ($100/mo) plan cards and "Codex is included in your ChatGPT plan."
- **Homepage:** hero cards now GPT-6 and Intelligent UI for everyone (Oct 7), Sharing AI progress in mathematics (Oct 6), Introducing dots (Sep 29).
- **`index/gpt-6-astra`, `introducing-gpt-6-sol-and-luna`:** banner "Update on September 29, 2026 — learn about GPT‑6.1 Sol".
- **`index/sharing-ai-progress-in-mathematics`:** update Oct 15 — OpenAI contributing $5M to a new Simons Foundation initiative.
- **`index/election-safeguards-2026`:** Oct 20 update ahead of U.S. midterms — Democracy Works and AP vote-count integrations, "cartoonified" stylization of election-interference images, Daybreak offers to election authorities, political-ads section.
- **Legacy-model banners:** 7 pages (o1-preview, o1-mini, o3-mini, o3/o4-mini, "Learning to reason with LLMs", "Thinking with images", `/o1/`) now open with "This post introduced…; o3 and o4-mini are no longer available in ChatGPT and are deprecated in the API", with links to current models — apparent systematic deprecation labelling, and the interactive demo content on several was stripped.
- **Customer stories rewritten:** `index/lowes` (now dated Sep 25, 2026, "answers millions of home-improvement questions", structured results block), `index/wayfair`, `solutions/industries/{retail,financial-services}`, `business/why-openai/small-business` (now "ChatGPT Work" framing + small-business webinar banner), `chatgpt-work` (GPT-5.6 → GPT-6 Astra link).
- **`webmcp-challenge`:** converted from live contest ("10 days", prizes) to winners/gallery page.
- **Release notes:** Oct 21 API entry "Service tier controls for API projects"; Sep 24 ChatGPT Business "External access controls" preview entry rotated out.
- **`daybreak`:** headline stats grew (e.g. 858 → 1,885; 263 → 661; 143 → 458; 41 → 65).
- **`previewing-ultrafast`:** the `/form/ultrafast/` sign-up form was removed from the sitemap and its links stripped from the post.
- **Plugins (302 pages under `/business/plugins/`):** "Try in ChatGPT Work" deep links changed from `chatgpt.com/?surface=work&q=@Name…` to `chatgpt.com/plugins/plugin_asdk_app_…?install&prompt=…` (one-click install), with descriptions refreshed (e.g. Netlify now "Read, Write" access, new skill description).

## Routine updates

~1,000 further pages: nav/footer/carousel/image-alt churn only. 28-ish pages with legacy-article footer tweaks ("Share", "Loading…" widgets, Author/Keep reading headings).

## New pages (106)

**Models & products**
- `/index/introducing-gpt-6-1-sol/` — GPT-6.1 Sol: nearly matches GPT-6 Astra on agentic coding/computer use at ~1/5 the price; follows GPT-6 Astra (Sep) and Sol/Luna (Sep 22).
- `/index/gpt-6-for-everyone/` (Oct 7) — a GPT-6 model for the 1.2 B weekly ChatGPT users, with "Intelligent UI" (interactive answers). `/index/practical-guide-building-gpt-6/` — model guide for the family.
- `/index/introducing-dots/` (Sep 29) — "always-on agents" with own cloud computer, 4,000+ app connections, via ChatGPT/Slack/Teams. `/index/decisions-api/` — low-latency Decisions API with GPT-Live. `/index/devday-2026-recap/` + `/devday/2026/` — DevDay (Sep 29), "20+ announcements".
- `/index/introducing-the-rosalind-academic-plan/`, `/index/openai-to-acquire-orchestra-bio/` (acquisition; drug-development coordination → Rosalind), `/index/scaling-ai-research-for-complex-biological-data/` (thousands of agents on biological data).

**Partnerships & business**
- `/index/openai-models-google-cloud/` + `/form/openai-on-google-cloud/` — OpenAI frontier models and Codex coming to Google Cloud. `/index/atlassian-partnership/` + new Atlassian plugin pages (and `atlassian-rovo` removed). `/business/marketplace/` — spend OpenAI commitment on partner products. `/business/forward-deployed-engineering/` + `/index/forward-deployed-engineering-means/`. 6 new partner pages (Affinda ex-Pathfindr, Bishop Fox, SpecterOps, TrustedSec, Insight, MegazoneCloud — security-heavy), `/business/solutions/legal/`, `/business/contact-sales-retail/`.
- ~25 customer stories (Uber, Oracle, AT&T, Albertsons, Itaú, Radisson, Sophos, SentinelOne, Block, Cloudflare, Sullivan & Cromwell, Jump Trading, Asana, Higgsfield, Pollo AI, etc.), several citing GPT-6.x / ChatGPT Work / Daybreak.
- Plugins: Alpaca, Atlassian, Atlassian Teamwork Graph CLI, Jetpack, Sandstone, Spacefast, WordPress.com.

**Ads & policies**
- `/index/chatgpt-ads-expands-26-new-countries/` (100,000+ advertisers), `/index/new-chatgpt-ads-format-and-measurement/`, `/index/building-chatgpt-ad-stack/`, `/policies/brazil-advertising-terms/`, `/policies/row-privacy-policy/`, `/policies/sign-in-with-chatgpt-terms/` + `/form/sign-in-with-chatgpt-interest/` (a "Sign in with ChatGPT" product is coming).

**Safety, security, policy**
- `/index/disrupting-a-coordinated-model-distillation-campaign/` (campaign to extract protected reasoning, first activity early July), `/index/disrupting-ai-enabled-false-front-operations/`, `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet": PHP vulnerabilities found with GPT, PHP checker Codex skill), `/index/empowering-cyber-defenders/`, `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/broad-access-through-consistent-standards/`, `/index/eu-text-provenance/`, `/index/the-eus-next-chapter-in-ai-is-agentic/`, `/index/how-we-will-do-better-for-australia/`, `/index/openai-nask-ai-safety-security-partnership/`, `/index/teens-learn-and-plan/`, `/index/helping-small-businesses-put-ai-to-work/`, `/index/lenfest-ai-collaborative-expansion/`.
- Other: `/codex-originals/` + 2 forms (Codex community programmes), `/form/computer-use-research-collaboration/`, `/form/private-intelligence-interest/` ("Private Intelligence" product interest), `/index/sharing-ai-progress-in-mathematics/`, `/index/low-resource-programming-languages/` (COBOL), `/index/the-eternal-complement/`.
- 13 Learn demo pages (new `learn-demos` sub-sitemap) + guides/webinars (board guide to cybersecurity & AI, GPT-Live-1 webinar with Cognition, "How OpenAI uses ChatGPT Atlas", Codex across the SDLC).

## Removals (5)

- `/business/partners/pathfindr/` (renamed Affinda — new page `/business/partners/affinda/` "formerly Pathfindr")
- `/business/plugins/atlassian-rovo/` (replaced by `/business/plugins/atlassian/`)
- `/business/plugins/mcp-server-for-wordpress/` and `/business/plugins/wordpress-com/` (replaced by `/business/plugins/wordpress/`)
- `/form/ultrafast/` (Ultrafast preview sign-up closed)
Last snapshots in git history.
