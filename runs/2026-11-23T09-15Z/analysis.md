# Run 2026-11-23T09-15Z — analysis

- **Sitemap fetch time (observed):** 2026-11-23T09:16:19Z (root index + 45 sub-sitemaps)
- **Page fetches (observed):** 2026-11-23 ~09:20Z–09:55Z UTC, 2,083 pages via `tools/html_to_md.py` (curl-cffi), **0 fetch failures**
- **Baseline:** `2026-09-28T09-17Z` — **56 days earlier.** The routine did not run between 2026-09-28 and 2026-11-23. Everything below is a single diff across that whole gap.

| | Count |
|---|---|
| Total URLs now | 2,316 (was 1,985; +331 net) |
| Added | 363 |
| Updated (`<lastmod>` changed) | 1,720 |
| — with any rendered change | 1,720 (every one; sitewide nav changed) |
| — with change beyond sitewide template/recirculation lines | 703 |
| — with >200 chars of page-specific change | 575 (329 of them are `/business/plugins/*` listing refreshes) |
| Removed | 32 (19 redirect to a new URL, 13 return HTTP 404) |
| Anomalies | 59 (51 sub-sitemap migrations, 3 new sub-sitemaps, 3 reappearances, 1 observation gap, 1 backdated policy date) |
| Sub-sitemaps | 45 (was 42) |

---

## 1. Anomalies

### 1a. Observation gap (56 days) — read every date in this run with care
The prior snapshot is from 2026-09-28T09-17Z. All 363 new URLs get `first_seen = 2026-11-23T09-15Z`, but that is only an upper bound: the pages' own bylines show publication dates from **2026-09-28 through 2026-11-22** (154 of the new `/index/` posts carry a visible date; 72 in October, 74 in November, 8 on Sep 28–30). Any intermediate `<lastmod>` values, short-lived pages, or reversals that happened inside the gap were never observed. The `backdated new URL` check is effectively disabled for this run — no new URL had a `<lastmod>` earlier than the prior run, so nothing qualifies anyway.

### 1b. Privacy Policy claims an update date earlier than when it went live
`/policies/privacy-policy/` now reads **"Updated: September 10, 2026"** (previous version link: `revisions/2026-05-18`). But our 2026-09-28T09-17Z snapshot still served the **"Updated: May 18, 2026"** text. The stated update date is therefore at least 18 days earlier than the text was publicly visible. Substantively, the new version **removes every mention of Sora** (e.g. "We build tools like ChatGPT and Sora…" → "We build tools like ChatGPT…", and the Sora-characters / Sora-videos data-collection bullets are gone). `/sora/` itself is not in the sitemap; older Sora blog posts remain.

### 1c. Three URLs disappeared and came back
| URL | Previously | Now |
|---|---|---|
| `/business/plugins/alpaca/` | first_seen 2026-07-10, last_seen 2026-09-24 | back, lastmod 2026-11-18T20:23Z |
| `/form/codex-ambassadors/` | first_seen 2026-05-07, last_seen 2026-06-24 | back, lastmod 2026-11-05T11:53Z |
| `/policies/row-privacy-policy/` | first_seen 2026-05-07, last_seen 2026-05-27 | back, lastmod 2026-11-03T12:13Z |

### 1d. New sub-sitemaps (3)
`/sitemap.xml/safety-and-alignment/`, `/sitemap.xml/science/`, `/sitemap.xml/learn-demos/`. These line up with the new `/safety-alignment/` research hub (replacing `/safety/`), the new science blog (`/news/science/`, "Our new blog for science", Nov 15), and the reorganised `/business/learn/` section.

### 1e. Sub-sitemap migrations (51 URLs)
No URL was dropped from one section and lost; these are re-categorisations:
- ~30 plugin pages were re-filed among `plugins-*` sitemaps, mostly **into `plugins-sales-commerce`** (which coincides with the Nov 17 "ChatGPT for Sales" launch and "30 new and expanded partner plugins").
- 5 webinar pages added to `learn-webinars`; 3 moved `page → learn-webinars`, 2 `page → learn-guides`; 4 `ai-adoption` posts and 1 `global-affairs` post cross-listed into `learn-guides`.
- One heavily cross-listed post gained the new `science` sitemap.
Full list in `diff.json` (`kind: sub_sitemap_migration`).

### 1f. Not detected
No `<lastmod>` in the future relative to fetch time. No `<lastmod>` moved backwards. 92 URLs carry no `<lastmod>` at all — including the launch posts for **GPT‑6.1 Sol, GPT‑6.1 Terra and GPT‑6.2 Astra/Sol** and the entire new `/safety-alignment/*` hub — so their modification history can't be tracked from the sitemap.

---

## 2. Significant updates

### Sitewide navigation overhaul (all 1,717 pages)
The header/footer menu changed on every page:
- **Removed:** `GPT-5.5`, `GPT-5.4`, `Safety Approach` (`/safety/`), `Open Models` (`/open-models/`), `Apps SDK`, `Codex` (pointing at `/codex/`). On 1,062 pages a `GPT-6` link was also replaced.
- **Added:** `GPT-6 Astra`, `GPT-6.1 Sol`, `GPT-6.2`, `Dots` (chatgpt.com/features/dots), `Codex` (now pointing at chatgpt.com/codex), `Plugins` (developers.openai.com/plugins), `Models` (developer docs), `OpenAI Status`.
- `/open-models/` (gpt-oss) still exists and is in the sitemap; it just isn't linked from the global menu any more.

### Old model-launch posts get "retired" banners
`/index/learning-to-reason-with-llms/` (o1), `/index/introducing-openai-o1-preview/`, `/index/openai-o1-mini-advancing-cost-efficient-reasoning/`, `/index/openai-o3-mini/` and `/index/introducing-o3-and-o4-mini/` now open with "## This post introduced OpenAI …" plus a note: o1‑preview and o1‑mini are retired from the API, o1 and o3‑mini are deprecated, and **o3 and o4‑mini are no longer available in ChatGPT and deprecated in the API**. Each links to the API deprecation schedule. (24 pages in total now carry this banner pattern.)

### Policies
- **Usage Policies** (`/policies/usage-policies/`) — new version **effective November 20, 2026** (announced 2026-10-21; previous 2025-10-29). Changelog: clarifies restrictions on **using OpenAI models/outputs to train other models**, clarifies child/teen protections and high-stakes-use requirements, folds in national-security principles, and adds **approval requirements for national-security and law-enforcement uses and for "model-access intermediaries."** Ties directly to the new distillation posts (see §4).
- **Privacy Policy** — Sora removed; see anomaly 1b.
- **Ad Policies** (`/policies/ad-policies/`) — updated Sep 10 → Nov 20, 2026; placement rules rewritten around "brand-unsafe" vs "sensitive user contexts".
- **Advertising Terms** — updated Aug 25 → Oct 15, 2026; Brazil customers now governed by new **Brazil Advertising Terms** (new page); intermediary/vetting clauses restructured.
- **Cookie Policy** — Sep 10 → Nov 19, 2026; `oai-did` lifetime 1 → 2 years; new cookies on `ads.openai.com` and `help.openai.com`.
- **Health Privacy Policy** — Jun 29 → Nov 19, 2026; "ChatGPT Health / Connect Health" renamed to a **"Health" plugin** ("Health in ChatGPT").
- **Service Terms** — Sep 21 → Nov 13, 2026; new **Prompt-to-Voice** section (create synthetic voices from text; may not reproduce a real person's voice without consent; excluded from IP indemnity).
- **Supplier Code of Conduct** — first update since Oct 10, 2023 (now Oct 15, 2026); fully rewritten and aligned to the Responsible Business Alliance code, UNGPs and ILO principles.
- New policy pages: Sign in with ChatGPT terms, ChatGPT Wallet terms + privacy notice, Businesses in ChatGPT policy + terms, Business Agents policy, Marketplace customer program terms, Brazil Advertising Terms.

### Other notable page changes
- **`/business/pricing/`** — "5x more usage than standard" softened to "More usage than standard"; adds "Up to $500 per month in API credits for your workspace"; new line: **"Starting in December, plan usage will have a shared limit across all of ChatGPT and Codex."**
- **`/codex/`** — rewritten from "The same powerful coding agent—now in ChatGPT" to "Build anything with Codex… Codex is included in your ChatGPT plan," with per-plan usage tiers.
- **`/trust-and-transparency/`** — government-request report advanced from Jul–Dec 2025 to **Jan–Jun 2026**: non-content user-data requests 224 → **620**, content requests 75 → **146**.
- **`/products/release-notes/`** — newest entry now Nov 17, 2026 (Responses API discounted background-completion windows: 30%/40% cheaper for 2h/8h windows).
- **Homepage** — lead story is now GPT‑6.2 Astra and Sol (Nov 17); adds a "Talk to us" sales CTA and a Daybreak (cyber) event banner.
- **`/rosalind/`** — researcher CTA now promotes the Rosalind Academic Plan.
- **`/index/wayfair/`** — customer story rewritten and redated (Mar 11 → Sep 25, 2026; "2.5M product tags corrected" → "11M+ product specs validated").
- **`/collective-cyberdefense/`** — signatory list reformatted and expanded.

## 3. Routine updates
- **329 `/business/plugins/*` pages**: listing refresh (new taglines, screenshots, "Try in ChatGPT Work" deep links now use `chatgpt.com/plugins/<id>?install&prompt=…`). Template-driven, not editorial.
- **~1,017 pages** changed only in sitewide nav/footer lines and "Keep reading" recirculation cards (e.g. cards for "Perplexity and Intelligence", "Research acceleration: The jagged frontier", "Le Groupe Figaro" partnership).
- Remaining ~370 pages: minor link-format changes (e.g. external links now marked "(opens in a new window)"), whitespace in table-of-contents entries, small copy tweaks.

---

## 4. New pages (363)

Breakdown: 59 `/business/plugins/*`, 29 `/business/learn/*` (mostly relocated from older URLs), 27 `/safety-alignment/misalignment-reports/*`, ~30 other `/safety-alignment/*`, ~155 `/index/*` posts, 10 customer stories, 8 solutions pages, 7 `/supply/` merch items, 6 `/ads/customers/*`, 6 partners, plus forms and policies.

### Models & products (by byline date)
- **Sep 29 — DevDay 2026** (`/index/devday-2026-recap/`): "more than 20 major announcements"; ChatGPT has **1.2B weekly users**; ChatGPT opened as a surface where developers can launch native experiences.
- **Sep 29 — Dots** (`/index/introducing-dots/`): always-on agents ("dots") that work on their own; specialist dots coming to Microsoft Agent 365; Nov 3 update adds GPT‑6.1 Terra as a dot model.
- **Sep 29 — GPT‑6.1 Sol** (`/index/introducing-gpt-6-1-sol/`, date from recirculation card): "near-Astra intelligence for a fifth of the price" — $2 in / $10 out / $0.10 cached per M tokens (Astra: $10/$50/$1; Luna: $0.10/$0.50/$0.01).
- **Oct 2 — A model guide for the GPT‑6 family.**
- **Oct 7 — GPT‑6 and Intelligent UI for everyone** (`/index/gpt-6-for-everyone/`): GPT‑6 brought to free users; "Intelligent UI" gives more visual, interactive answers.
- **Oct 22 — Decisions API.**
- **Oct 26 — GPT‑6.1 Terra** (`/index/introducing-gpt-6-1-terra/`): fast computer-use model; API prices 50% below GPT‑5.6 Terra and GPT‑6.1 Sol; ~3× faster than Astra/Sol.
- **Nov 4 — Images 2.6.**
- **Nov 5 — GPT‑6 Cyber** (`/index/introducing-gpt-6-cyber/`): a vulnerability-finding model offered through the "Daybreak" trusted-access program, with a system card.
- **Nov 10 — Businesses in ChatGPT**: businesses can claim and manage their listing inside ChatGPT.
- **Nov 13 — ChatGPT Wallet** (`/index/introducing-chatgpt-wallet/`): agent payments built with Amex, Chase, Mastercard and Visa; agents never see card numbers; per-purchase security check; initially for US Pro users via dots.
- **Nov 17 — GPT‑6.2 Astra and Sol** (`/index/introducing-gpt-6-2-astra-sol/`): new frontier model; Astra API prices cut 20% ($8 in / $40 out / $0.40 cached); claims to beat Claude Fable 5.2 on Agents' Last Exam at 5% of the cost.
- **Nov 17 — ChatGPT for Sales**, **Astra for Law**; new `/business/marketplace/` (spend OpenAI commitments on partner products), `/business/private-intelligence/` (enterprise privacy), `/business/images-api/`, `/business/forward-deployed-engineering/`.

### Corporate, acquisitions, people
- **Oct 20 — OpenAI acquires Orchestra Bio** (drug-development coordination platform, folded into Rosalind life-sciences work).
- **Nov 4 — OpenAI to acquire Pierre Computer Company** (Code Storage; its Trees/Diffs libraries already power the Codex app).
- **Nov 2 — Dan Driscoll** joins as Senior Counselor for National Security Modernization (new role).
- **Nov 3 — Jill Hazelbaker** (ex-Uber President & CCAO) appointed Chief Corporate Affairs Officer.
- Partnerships: Atlassian (Oct 6), Google Cloud Model Garden (Oct 21), Oracle apps in ChatGPT (Oct 27), ServiceNow (Oct 28), ChatGPT Enterprise on AWS Marketplace (Nov 9), LVMH Media (Nov 16), Le Groupe Figaro (Nov 18), Poland's NASK (Oct 23), OpenAI for Chile (Nov 17), King's Trust £1m (Nov 16).
- `/compute-campus/` + "Setting a new standard for responsible AI infrastructure" (Nov 5): US data-centre community commitments.

### Safety, security, policy
- **New `/safety-alignment/` hub** replaces `/safety/` (which now redirects): "Research and releases… to understand, align, and secure increasingly capable AI," 59 posts, plus 27 **misalignment reports**. New posts include "How we detect frontier model misalignment" (Oct 29; layered activation probes → model reviewer → investigative agents), "Managing frontier AI risk: from training to deployment" (Nov 18), "Towards safety cases for frontier AI training" (Sep 28), and an **updated Model Spec** (Oct 29, reorganised around core values).
- **Distillation:** "Disrupting a coordinated model-distillation campaign" (Sep 30; activity since early July aimed at extracting protected reasoning) and "Combatting adversarial distillation" (Nov 20). Matches the Usage Policies change.
- **Cyber push ("Daybreak"):** GPT‑6 Cyber, Daybreak Red in AWS GovCloud, "Patch the Planet" coordinated disclosure, bigger bug bounties, Hacktron partnership, NATO cyber defence, Grid Protectors Program, "Securing our frontier model training environment," ~10 security-customer stories (Cisco, Cloudflare, SentinelOne, Sophos, Check Point, Block…), `/cybersecurity/`, `/cyber-at-the-frontier/` (Nov 12 event).
- Influence ops: "Disrupting AI-enabled 'false front' operations" (Oct 8).
- Child safety: teen protections + community safety report (Oct 30), $2M pledge at the Paris Peace Forum (Nov 12), new CSAM-classifier intake form and tools (Nov 16).
- Copyright: **"Fair use benefits everyone"** (Oct 30), explicitly attacking the New York Times lawsuit; "Making it easier for websites to express AI training preferences" (Oct 30); "Our approach to EU text provenance rules" (Oct 5).
- Australia: "How we will do better for Australia" (Sep 28).

### Research & science
- New science blog (`/news/science/`, Nov 15) with "Science at the frontier", lattice Standard Model (Nov 15), wet-lab agent benchmark (Nov 6), MedChemBench (Nov 20), chip design (Nov 18), thousands of agents on biological data (Oct 21), Rosalind Academic Plan (Oct 15).
- **"Research acceleration: The jagged frontier"** (Nov 18): internal measurement of how coding agents accelerate OpenAI's own AI R&D.
- **"Perplexity and Intelligence"** by Chief Scientist Jakub Pachocki (Nov 22).
- Economics: EU agentic adoption report (Oct 14), AI's effect on freelance work (Nov 10), `/economic-research-collaborators/` (replaces "exchange").

### Ads
ChatGPT Ads expands to 26 more countries / 100k+ advertisers (Oct 21), "now in 44 countries" (Nov 12), ad-stack engineering post, new ad format & measurement (Oct 5), 6 advertiser case studies.

---

## 5. Removals (32)

**Redirects (URL moved — content lives on at the new address):**
- 6 `/business/*-webinar/` & `/business/guides-and-resources/*` → `/business/learn/*`
- 5 `/solutions/*` → `/business/solutions/*`
- `/index/ada/`, `/index/blue-j/` → `/business/customer-stories/*`
- `/safety/` → `/safety-alignment/`
- **`/prism/` → `/science/`** (Prism product page folded into Science)
- **`/residency/` → `/research/`** (Residency program page gone)
- `/economic-research-exchange/` → `/economic-research-collaborators/`
- `/form/data-partnerships/` → `/index/data-partnerships/`
- `/form/ultrafast/` → developers.openai.com ultrafast-mode guide
- `/business/partners/pathfindr/` → `/business/partners/affinda/`
- `/business/plugins/wordpress-com/` → `/business/plugins/wordpress/`

**HTTP 404 (gone):** partner pages for **Canva, Dropbox, Gusto, HubSpot, QuickBooks, Stripe**; plugin pages for **Atlassian Rovo, Litera Lito, MCP Server for WordPress, Oracle Analytics**; `/daybreak/partners-new/`.

Last snapshots: `git log -- pages/openai.com/<path>/index.md`.

---

## Fetch failures
None. All 2,083 Added/Updated pages fetched and passed the sanity check (≥100 chars, no Cloudflare challenge).
