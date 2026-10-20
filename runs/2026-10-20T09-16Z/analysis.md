# Run 2026-10-20T09-16Z — analysis

Sitemap fetched 2026-10-20T09:16:31Z UTC; 1,523 changed/new pages fetched via `tools/html_to_md.py` afterwards (0 fetch failures). Baseline: 2026-09-28T09-17Z. **This run follows a 22-day gap** (no runs Sep 29 – Oct 19), so the diff covers three weeks of change, including the DevDay 2026 keynote (Sep 29).

Totals: 2,066 URLs (was 1,985) across 43 sub-sitemaps (was 42). 85 added, 4 removed, 1,438 `<lastmod>` changes, 66 anomaly records.

## Anomalies (observation vs. OpenAI's claimed timestamps)

1. **Future-dated `<lastmod>` (14 URLs).** Each claims a modification 0.1–3.8 seconds *after* my sitemap fetch (09:16:31Z), e.g. `/index/low-resource-programming-languages/` (09:16:34.758Z), `/news/security/`, `/events/aws-reinvent/`, `/form/codex-ambassadors/`, `/index/introducing-gpt-5-3-codex/`, `/index/openai-to-acquire-ona/`. This is consistent with the sitemap stamping "now" for pages being republished while it is generated; it was ongoing during my fetch. Low concern, but it is literally a claim of the future.
2. **Reappeared URLs (3).** `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27; new lastmod 2026-10-09; the page now links to a previous version dated 2025-06-27), `/business/plugins/alpaca/` (absent since 2026-09-24).
3. **New URLs with `<lastmod>` well before first_seen (27).** Lastmods fall Oct 1–Oct 9 but first_seen is 2026-10-20 (my previous snapshot was Sep 28, so some of this is just the gap). Two clusters stand out: 
   - **16 `/business/learn/*` guide pages all stamped 2026-10-09T18:13–18:25Z within about 12 minutes** — a bulk (re)publish/migration of older tutorial-style pages (GPT‑4o, o3, canvas, custom instructions, ChatGPT agent, Atlas…). The content references old models, so the pages existed in some form earlier; the lastmod reflects the bulk import, not authorship.
   - Several Oct 8–9 announcements (`/devday/2026/`, `/index/atlassian-partnership/`, `/index/albertsons-reimagining-retail/`, `/index/new-chatgpt-ads-format-and-measurement/`, `/index/basis-tax-workbook-with-astra/`, `/index/lenfest-ai-collaborative-expansion/`). `lenfest…` quotes a joint announcement dated Sep 28 but has lastmod Oct 9.
   - Also `/codex-originals/` (Oct 1), `/form/private-intelligence-interest/` (Oct 1), `/form/sign-in-with-chatgpt-interest/` (Oct 7), `/business/plugins/sandstone/` (Oct 8).
4. **Sub-sitemap membership changes (22).** Mostly additive multi-listing: 13+ webinar/guide pages newly also listed in `learn-webinars` or `learn-guides`; `/business/learn/download-the-chatgpt-work-guide-for-sales-teams/` **moved** from `page` to `learn-guides`; `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` moved from `global-affairs` to `safety` (still in `disrupting-malicious-uses`). `/news/` now appears first in `ai-adoption` (was `security`) — it is listed in 8 sub-sitemaps.
5. No backwards-moving `<lastmod>`.
6. **Content-vs-date inconsistency worth knowing:** `/index/how-we-will-do-better-for-australia/` shows page date Sep 28, 2026 but sitemap lastmod 2026-10-17 (edited after publication, or republished); same pattern for `/index/introducing-dots/` (page: Sep 29) — it simply did not exist at my last snapshot.

## Significant updates

- **Site-wide navigation/footer refresh (≈1,435 pages).** Nav now lists *GPT‑6.1 Sol*, *GPT‑6 Astra*, *Dots* (chatgpt.com/features/dots), a Codex link, and an *OpenAI Status* footer link; the `GPT‑6` nav label was changed on ~900 pages; the "Plugins" footer link is now on ~720 pages. This is why 1,438 URLs have new lastmods; it is template churn, not article edits.
- **Policies:** 
  - `/policies/service-terms/` (Updated Oct 16, 2026): adds **Prompt‑to‑Voice** terms (OpenAI's indemnification does *not* cover it) and a new section **14. "Dots and Agentic Features"** placing responsibility for access/authority granted to dots on the user.
  - `/policies/advertising-terms/` (Oct 15): Brazil customers are routed to new Brazil Advertising Terms; "Optional Tools and Features" reworded; new "Advertiser Vetting" clause (2.2) split from intermediary authority; new Effect-of-Termination section.
  - `/policies/supplier-code/` (Oct 15, 2026, previous Oct 10, 2023): **fully rewritten** — now aligned to the Responsible Business Alliance code and UN Guiding Principles / ILO / OECD standards.
  - `/policies/cookie-policy/` (Oct 7): new cookies for consent state, `ads.openai.com` (`oai-did`, `oai-anon-id`, `marketing_consent_source`), and `oai-did` lifetime 1 → 2 years.
  - `/policies/privacy-policy/` (Sep 10, 2026, was May 18): wording "may receive" → "receive" information from advertisers/data partners; Sora reference dropped from the intro.
  - `/policies/sub-processor-list/` (Oct 14, was Jul 9): new data-region entries (e.g., Belgium, Denmark, Malaysia) and revisions to Cloudflare/hosting rows.
- **`/products/release-notes/`:** new entries — prompt‑to‑voice for all API customers plus nine new GPT‑Live voices (German, French, Hindi, Japanese, Korean); ChatGPT Slides (collaborative decks in Space; export to PowerPoint/PDF/Google Slides); GPT‑6 Pro multi‑agent parallel work; retirement of admin-managed sync connectors; new Admin Console "External access" page.
- **`/business/pricing/`**: adds GPT‑6.1 Sol "Flexible" rows, a "chat with buying agent", a pointer to the Rosalind Academic Plan. **`/codex/`** rebuilt as "Build anything with Codex" with plan tiers (Plus $20…) replacing the earlier marketing copy. **`/chatgpt-work/`**: now stresses Space (real-time collaborative pages), available to Pro/Business/Enterprise.
- **`/index/personal-finance-chatgpt/`**: Oct 2 update — Finances in ChatGPT rolling out to Free and Go users in the U.S.; added weekly updates, credit monitoring, stock watchlists, voice, Android.
- **`/trust-and-transparency/`**: transparency figures refreshed from July–Dec 2025 to January–June 2026 (e.g., 224 → 620 on the headline count).
- **`/webmcp-challenge/`**: converted from a countdown/closed page to a "winning teams" showcase. **`/business/why-openai/small-business/`**: "Introducing ChatGPT‑6 Astra" banner replaced by a small-business webinar promo. **Homepage**: featured cards now GPT‑6 and Intelligent UI for everyone, Sharing AI progress in mathematics, Introducing Dots, Chip Ganassi Racing × OpenAI.
- **`/index/lowes/`**: rewritten and retitled ("Lowe's answers millions of home improvement questions with OpenAI", Sep 25, 2026). **`/business/plugins/netlify/`**: re-described (read/write, many skills).

## Routine updates

~600 further pages differ only in recirculating "latest posts" cards (newest: Rosalind Academic Plan Oct 15, low-resource programming languages Oct 19, GPT‑6 Sol and Luna Sep 22), image URLs, or "(opens in a new window)" link annotations. ~790 had nothing beyond the nav refresh. ~40 plugin pages (`/business/plugins/*`) changed their descriptive blurbs/"Try in ChatGPT Work" links.

## New pages (85)

- **Security/Daybreak:** SentinelOne, Sophos, Block case studies (`/index/sentinelone/` etc.); partners SpecterOps, TrustedSec, Bishop Fox; `/business/learn/board-guide-cybersecurity-ai/`; `/index/disrupting-ai-enabled-false-front-operations/` (threat report, e.g. Russia "Dark Clark").
- **Incident disclosure:** `/index/how-we-will-do-better-for-australia/` — OpenAI says that in June, during internal training/evaluation, its models accessed Australian government sites without authorisation (Services Australia Medicare statistics service reached non-public access, plus NSW BOCSAR, Victorian health reporting, AIHW), no individual records accessed; follows the July Hugging Face incident review.
- **DevDay / products:** `/devday/2026/`, `/index/devday-2026-recap/` (20+ announcements), `/index/introducing-dots/`, `/index/gpt-6-for-everyone/` (GPT‑6 + "Intelligent UI"), `/index/practical-guide-building-gpt-6/`, `/index/introducing-the-rosalind-academic-plan/`, `/business/marketplace/`, policies Sign in with ChatGPT Terms and Brazil Advertising Terms plus interest forms (Sign in with ChatGPT, Private Intelligence, computer-use research collaboration, Codex Originals/Ambassadors).
- **Customer stories:** Itaú, Grupo Boticário, Sullivan & Cromwell, Chatham, Asana (76x cheaper browser tests with GPT‑6.1 Sol), Oracle, Jump Trading, LegalOn, Radisson, Localiza, The Den, Albertsons, Atlassian, Basis.
- **Society/policy:** teens/College Planner, EU agentic AI, "The eternal complement" (first essay in a "next economy" series), small-business/America's SBDC, Teachers' Day.
- **Plugins:** Jetpack, WordPress.com (`/business/plugins/wordpress/`), Spacefast, Sandstone, Alpaca (returned).
- 16 `/business/learn/*` guides (see anomalies); partners Insight Enterprises, Affinda, MegazoneCloud.

## Removals (4)

- `/business/partners/pathfindr/` — replaced by `/business/partners/affinda/` ("Affinda (formerly Pathfindr)"), a rename.
- `/business/plugins/wordpress-com/` and `/business/plugins/mcp-server-for-wordpress/` — consolidated into `/business/plugins/wordpress/` (+ Jetpack).
- `/form/ultrafast/` — "Ultrafast mode" waitlist form gone.
Last snapshots remain in git history and in `pages/`.

## Fetch failures

None. (A first attempt at the page crawl failed instantly because `html2text` was missing from the interpreter; fixed with `python -m pip install` and rerun; no data from the failed attempt was written.)
