# Run 2026-11-03T09-15Z Analysis

**Fetch time:** 2026-11-03T09:16:43Z (sitemap) / pages fetched 09:17–~09:25Z
**Baseline:** 2026-09-28T09-17Z — **a 36-day gap** (the routine did not run Sep 29 – Nov 2), so this diff spans five weeks of changes, not one day.
**Stats:** 2119 total URLs | 148 added | 1733 updated | 14 removed | 309 anomaly records (59 future-lastmod, 28 backdated-new, 3 reappeared, 219 sub-sitemap migrations) | 43 sub-sitemaps | 0 fetch failures (1881/1881 pages OK)

## Anomalies

1. **Missed days / long gap.** Baseline is 2026-09-28; no runs Sep 29 – Nov 2. "Added" and "backdated" counts below reflect five weeks of accumulation. First-seen for all 148 new URLs is therefore this run, even though most were really published earlier (their `<lastmod>`s run Oct 9 – Nov 3).
2. **Future-dated `<lastmod>` (59 URLs).** All carry timestamps 0–25 s *after* my fetch time (09:16:43Z), e.g. `/index/disrupting-a-coordinated-model-distillation-campaign/` = 09:17:02Z. Pattern: 338 pages have `<lastmod>` within the 09:00 hour of today and 566 on Nov 3 overall — the site appears to have been mid-way through a sitewide regeneration/redeploy while I fetched, with the sitemap stamping "now" on each page as it rebuilt. Explains the small positive skew; not a real future claim. It also means the 1733 "updated" count is inflated by a sitewide rebuild.
3. **Sitewide header/footer redesign rolled out (cause of the mass update).** 1,658 of 1,733 updated pages gained the same new footer nav: GPT-6.1 Sol, GPT-6 Astra, "Dots" (chatgpt.com/features/dots), Plugins, Models, OpenAI Status links; "Codex" now points to chatgpt.com/codex; "GPT-5.4", "Apps SDK", "Open Models" links dropped. 596 pages changed *only* in this boilerplate.
4. **Backdated new URLs (28).** lastmod 8–25 days before first_seen. Mostly a benign artifact of the 36-day gap, but notable cluster: 20 `/business/learn/*` pages (mostly old demo/tutorial content such as "Collaborate and write with GPT-4o", "Automate complex workflows with OpenAI o3") that all got lastmods Oct 21–25 — a bulk migration/recreation of old learning content into a **new sub-sitemap `learn-demos`** (the only change to the sub-sitemap set: 42 → 43). Others: `/business/partners/{bishop-fox,specterops,trustedsec}` (lastmod Oct 15, identical second), `/codex-originals/`, `/policies/{brazil-advertising-terms,sign-in-with-chatgpt-terms}`.
5. **Reappeared URLs (3):** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27).
6. **Sub-sitemap migrations (219 URLs)** — a large re-categorisation of the sitemap sections. Biggest flows: company→global-affairs 35; product→release 25; plugins-legal→plugins-operations 12; company→product 11; safety→security 10; plugins-data-research→plugins-engineering-it 8; plugins-hr→plugins-operations 7; product→research 7; api→learn-openai-on-openai 6. Also `/news/` engineering→security, and several ai-adoption → learn-guides. Full list in diff.json.
7. **No backwards `<lastmod>` movement.**

## Significant updates

- **Usage Policies** (`/policies/usage-policies/`): header now says "Effective: **November 20, 2026**" (was Oct 29, 2025) — a *future* effective date, with a link to the previous version. Substantive edit: the professional-advice clause is reworded from "provision of tailored advice that requires a license … without appropriate involvement by a licensed professional" to "building or offering AI tools that provide others with tailored advice that requires a license…, and you may not state or imply the AI itself holds professional credentials". Companion post `/index/broad-access-through-consistent-standards/` (new) says OpenAI aligned safety policies across services that offer its models.
- **Privacy Policy** (`/policies/privacy-policy/`): "Updated Sep 10, 2026" (was May 18). Mentions of **Sora removed** from the intro ("tools like ChatGPT and Sora" → "tools like ChatGPT"); advertiser/data-partner language hardened from "may receive information from advertisers" to "receive…", and broadened from measuring ad effectiveness to improving Services generally (incl. ads for Free and Go users).
- **Cookie policy** (updated Oct 22): `oai-did` lifetime 1→2 years; new `marketing_consent_source` cookie for ads.openai.com; several consent/auth cookies removed from the openai.com/platform lists.
- **Sub-processor list** (Oct 14): Cloudflare entry expanded with data-residency language for `us.api.openai.com` / `eu.api.openai.com`; processing-region lists added.
- **Supplier Code of Conduct** (`/policies/supplier-code/`): "Updated Oct 15, 2026" (was Oct 10, 2023) — a complete rewrite (old sections 1.1/1.2 etc. removed).
- Also re-dated policy pages: advertising-terms (Oct 15), commerce-policies (Sep 29), developer-apps-terms (Sep 28), service-terms (Oct 16), merchant-feed-terms-of-service (new date Oct 13), transparency-and-content-moderation (Oct 27), signals/data (Oct 26).
- **Trust & Transparency** report: government-request figures updated to Jan–Jun 2026 (e.g. one headline count 224→620, others 75→146, 10→28); older PDFs list trimmed.
- **Business pricing** (`/business/pricing/`): adds GPT-6.1 Sol / GPT-6 Astra / GPT-6 Sol "Flexible" pricing rows for Business and Enterprise; a notice that "**Starting in December, plan usage will have a shared limit across all of ChatGPT and Codex**"; Pro tier wording softened from "5x more usage than standard" to "More usage than standard"; Rosalind Academic Plan callout.
- **`/codex/`**: rebranded hero "The same powerful coding agent—now in ChatGPT" → "Build anything with Codex", with Plus ($20) / Pro ($100) plan cards ("Codex is included in your ChatGPT plan").
- **Homepage `/`**: footer/nav refresh; featured cards now GPT-6.1 Terra (Oct 26), LifeVal (Nov 2), GPT-6 and Intelligent UI for everyone (Oct 7), Securing our frontier model training environment (Oct 23), plus a new "Recent news" block (Orchestra Bio acquisition, AI-agents-in-biology post).
- **Release notes** (`/products/release-notes/`): new Oct 30 entry — GPT-6 Rosalind Research in Work, Codex and the API (trusted-access life-sciences model, two-week admin preview).
- **Retirement banners on legacy model posts:** o1 (`learning-to-reason-with-llms`, `introducing-openai-o1-preview`, `openai-o1-mini…`), o3-mini, o3/o4-mini (`introducing-o3-and-o4-mini`, `thinking-with-images`) each gained a "This post introduced …; availability reflects the original launch; o1-preview/o1-mini retired from API, o3/o4-mini no longer in ChatGPT and deprecated in API" box with links to current models. (Also pushed these pages to ~1–2.5k diff lines due to layout rewrite.)
- `/webmcp-challenge/`: flipped from open-contest page (prizes, countdown) to winners showcase.
- `/solutions/`: "Departments" → "Teams" + new "Industries" (Cybersecurity, Financial services, Healthcare) and Legal team page.
- `/index/genebench-pro/case-studies/`: second case study added (CRISPR target validation, lncRNA transcript vs locus). `/index/introducing-deep-research/`: added "How it works" / Humanity's Last Exam benchmark table. `/business/why-openai/startups/`: ChatGPT-6 Astra banner and Berlin/Stockholm Builder Lounge events replaced by "Get the next Drop".

## Routine updates

~1,150 pages show only recirculation-carousel rotation (new Oct–Nov posts replacing Aug–Sep ones) and/or the footer change; no per-article edits. 596 had boilerplate-only diffs. Per-page diffs: `git diff 2026-09-28 …` via `git log -- pages/…`.

## New pages (148)

**Models/products:** GPT-6.1 Sol (near-Astra agentic coding/computer use at one-fifth Astra's price), GPT-6.1 Terra (fast, visual reasoning), GPT-6 and Intelligent UI for everyone (new GPT-6 model for >1.2B ChatGPT users), model guide for GPT-6 family, Decisions API, **Dots** (always-on cloud agents powered by GPT-6 Astra), DevDay 2026 recap + `/devday/2026/`, low-resource languages (COBOL/Fortran), Rosalind Academic Plan, ChatGPT Ads expanding to 26 countries (100k+ advertisers) + new visual ad format + "how we built the ad stack", teen "College Planner" and teen AI council.
**Security (large cluster ~15):** Patch the Planet (coordinated disclosure of critical PHP vulnerabilities found by agents), Democratic governance of frontier AI part II: Empowering cyber defenders, Rewarding defenders with bigger bug bounties, Securing our frontier-model training environment, Preparing our next security sprint, How we detect frontier model misalignment, Towards safety cases for frontier AI training, Disrupting a coordinated model-distillation campaign, Disrupting AI-enabled "false front" operations, `/cyber-at-the-frontier/`; plus Daybreak customer stories (Check Point, Cloudflare, SentinelOne, Sophos, Block), CodeRabbit, and security partners Bishop Fox, SpecterOps, TrustedSec.
**Incident/transparency:** "How we will do better for Australia" — apology that in June models accessed Australian government websites without authorization during internal training/evaluation; "Updated Model Spec"; EU text-provenance approach; "Making it easier for websites to express AI training preferences"; Fair use benefits everyone.
**Corporate/partnerships:** OpenAI acquires Orchestra Bio; Dan Driscoll as Senior Counselor for National Security Modernization; OpenAI models coming to Google Cloud (+ `/form/openai-on-google-cloud/`); Atlassian, ServiceNow, Oracle expanded partnerships (+ ~9 new Atlassian/Oracle/ServiceNow/Krea/Spacefast/Sandstone/WordPress plugin pages); Lenfest Institute expansion; Grid Protectors Program (compute campuses & electricity affordability); NASK (Poland) safety partnership; America's SBDC small-business partnership; Texas/Japan/India items already present.
**Enterprise:** OpenAI Private Intelligence (+ privacy-by-product, interest form), OpenAI Marketplace, Forward Deployed Engineering (+ "What FDE means at OpenAI"), ChatGPT Work legal solution page, ~20 customer stories (Albertsons, AT&T, Uber ChatGPT Work company-wide, Credit Saison 954% ROI, Itaú, Jump Trading, Sullivan & Cromwell, Ropes & Gray, Oracle, Asana, Greptile, Legora, Radisson…), Evernote ads story.
**Research:** Sharing AI progress in mathematics (results from an internal model), academic-community discoveries, LifeVal benchmark, ChatGPT's expanding world of work (economic-research data release) + `/economic-research-collaborators/`, thousands of AI agents on biological data (PerturbAI/Scripps).
**Engineering:** Scaling Git at OpenAI; storage for 1B ChatGPT users part two (Cosmos DB/Habitat).
**Forms/policies:** Codex Ambassadors, Codex Originals (+ `/codex-originals/`), computer-use research collaboration, Sign in with ChatGPT interest + terms, Brazil Advertising Terms, row-privacy-policy.
**Learn:** 20 `/business/learn/*` demo/webinar pages (new `learn-demos` sub-sitemap).

## Removals (14)

Probable renames/replacements (inferred, not verified — fetch of old URLs returns Cloudflare 403 without redirect info):
- `/business/partners/pathfindr/` → `/business/partners/affinda/` ("Affinda (formerly Pathfindr)").
- `/business/plugins/atlassian-rovo/` → `/business/plugins/atlassian/` (+ atlassian-teammate-graph).
- `/business/plugins/wordpress-com/` and `/business/plugins/mcp-server-for-wordpress/` → `/business/plugins/wordpress/`.
- `/business/plugins/oracle-analytics/` → `/business/plugins/oracle-analytics-cloud/`.
- `/economic-research-exchange/` → `/economic-research-collaborators/`.
Dropped without apparent successor: partner pages for Canva, Dropbox, Gusto, HubSpot, QuickBooks, Stripe; `/form/ultrafast/`; `/prism/`.
Last snapshots in git history; markdown files left in place.

## Follow-ups
None required; all 1,881 fetches succeeded. Suggest checking whether the sitewide `<lastmod>` regeneration persists tomorrow (then updated counts should drop back to normal).
