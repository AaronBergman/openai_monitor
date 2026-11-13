# Run 2026-11-13T09-16Z — analysis

- **Sitemap fetch time (observation):** 2026-11-13T09:17:19Z (root index + 43 sub-sitemaps, all fetched OK)
- **Page fetches:** 1,972 pages (253 added + 1,719 updated) fetched 2026-11-13 ~09:20–09:55Z via `tools/html_to_md.py` (curl-cffi). **0 fetch failures.**
- **Baseline:** `2026-09-28T09-17Z` — **46 days earlier.** The routine *did* run daily in between (PRs #148–#192), but none of those PRs were merged, so `sitemaps/openai.com/latest.xml` and `state/known_urls.json` on `main` still reflect 2026-09-28. Everything below is therefore one cumulative diff spanning ~6.5 weeks, as were the diffs in each unmerged daily PR. Intermediate states (pages that appeared *and* disappeared inside the gap, or intermediate `<lastmod>` values) are not observable.
- **Totals:** 2,208 URLs now (was 1,985) · 253 added · 1,719 `<lastmod>`-updated · 30 removed · 43 sub-sitemaps (was 42; new `learn-demos`)

## How to read the "updated" count

Of the 1,719 `<lastmod>` bumps, **every single page's markdown differed**, but the vast majority only because of one **sitewide navigation/footer template change** (present on 1,716 pages):
- added menu links: **GPT‑6.1 Sol**, **GPT‑6 Astra**, **Dots**, **Plugins**, **Models** (developer docs), **OpenAI Status**; Codex link now points to `chatgpt.com/codex` instead of `/codex/`
- removed menu links: **GPT‑5.4**, **Apps SDK**, **Open Models**, plain "GPT‑6"
- ~970 pages lost a stray "Loading…" placeholder; ~365 business pages gained a "Get OpenAI for Business updates" newsletter signup box; links to external sites now carry "(opens in a new window)".

After normalizing out template lines, link-label changes, image-URL churn and "latest posts" recirculation cards, **~348 pages had some residual change, ~183 had more than a trivial edit, and ~72 had large edits**. Roughly half of the large ones are the `/business/plugins/*` directory pages, which were all regenerated with new descriptions, new tag lists and "Try in ChatGPT Work" buttons that now deep-link to a `chatgpt.com/plugins/...?install` URL (the plugin catalogue moved from a prompt-link model to an install-link model).

## 1. Anomalies (highest signal)

**Stale baseline (meta-anomaly).** 45 consecutive daily-run PRs (#148–#192, 2026-09-29 … 2026-11-12) are open and unmerged, so `main` never advanced past 2026-09-28T09-17Z. (Older unmerged PRs from May–July also exist.) Any "first_seen" recorded today (2026-11-13T09-16Z) is only an upper bound on when a URL actually went live.

**Reappeared URLs (3)** — previously tracked in `state/known_urls.json`, absent at baseline, back now:
- `/business/plugins/alpaca/` — last seen 2026-09-24, absent at the 09-25…09-28 runs, back (lastmod 2026-11-10), now in `plugins-finance`.
- `/form/codex-ambassadors/` — last seen 2026-06-24, back after ~4.5 months (lastmod 2026-11-05). Page rewritten; links to a developers.openai.com Codex Ambassadors community page.
- `/policies/row-privacy-policy/` — last seen 2026-05-27, back after ~5.5 months (lastmod 2026-11-03). **It serves a stale document**: "Updated: February 6, 2026", still describing "ChatGPT and Sora" and Sora characters/videos — whereas the canonical `/policies/privacy-policy/` (now "Updated: September 10, 2026") has *removed* all Sora references. Two live privacy policies with different content is an inconsistency worth watching.

**Sub-sitemap migrations (9)** — URL moved wholesale from one sub-sitemap to another:
- Business "learn" content re-filed: `how-our-finance-team-uses-chatgpt-work` (learn-guides → learn-webinars), `intelligence-at-work-financial-services`, `intelligence-at-work-cyber`, `how-our-sales-team-uses-chatgpt-work` (page → learn-webinars), `agent-security-enterprise`, `download-the-chatgpt-work-guide-for-sales-teams` (page → learn-guides).
- Plugin re-categorizations: `tableau` (data-research → productivity), `sync-labs` (productivity → design-creative), `parallel-search` (engineering-it → productivity).

**Missing `<lastmod>` on new URLs (13).** Most notably the two **model-launch posts `/index/introducing-gpt-6-1-sol/` and `/index/introducing-gpt-6-1-terra/` carry no `<lastmod>` at all**, unlike nearly every other `/index/` article. The GPT‑6.1 Sol and Terra pages also lack a visible publication date in the rendered page. Other undated new URLs: 4 `/ads/...` pages and 7 `/supply/product/...` merch pages (the supply store has never carried lastmods).

**`<lastmod>` dropped (1).** `/index/advancing-independent-research-ai-alignment/` had `<lastmod>` 2026-09-25T19:18:24.670Z at baseline; its sitemap entry now has none.

**In-page date earlier than observed change (1).** `/policies/privacy-policy/` now reads "Updated: September 10, 2026", but its sitemap `<lastmod>` was unchanged (2026-09-04T14:03Z) through our 2026-09-28 observation and the old "May 18, 2026" text was the last one we archived. Either the new text went live after Sept 28 with an earlier stated date, or the page changed without a lastmod bump. Either way, the claimed date and our observation disagree by ≥18 days.

**Visible publication date reset on rewritten customer stories (3).** Same URL, new story, new date: `/index/wayfair/` (March 11, 2026 → September 25, 2026; "2.5M product tags corrected" → "11M+ product specs validated"), `/index/lowes/` (retitled "Lowe's answers millions of home improvement questions with OpenAI", dated September 25, 2026), `/index/retell-ai/` (June 26, 2025 → October 27, 2026; GPT‑4o story replaced by a GPT‑6 Astra story). Anyone citing these URLs by date will find different content than before.

**Low-signal (not counted):** 46 new URLs have `<lastmod>` more than 7 days before today's first_seen. None predates the 2026-09-28 baseline, so all are explained by the stale baseline. No future-dated `<lastmod>` values. No backwards-moving `<lastmod>` values.

## 2. Significant updates (substantive content changes)

**Policies & legal**
- **Usage Policies** (`/policies/usage-policies/`) — new version **"Effective: November 20, 2026"** (previous: Oct 29, 2025). Licensed-advice rule narrowed to *building/offering tools* that give tailored licensed advice, plus a new ban on stating or implying the AI holds professional credentials; the "national security" review requirement now also covers **law enforcement**; "Keep minors safe" became "Keep young people safe" with a much more detailed child-sexual-exploitation section (grooming, sextortion, sexualizing children).
- **Service Terms** (`/policies/service-terms/`, Updated Nov 12, 2026; was Sept 21) — new sections for **Prompt-to-Voice** (synthetic voices created from text prompts; no reproducing a real person's voice without consent; *excluded from OpenAI's IP indemnity*), **Business Agents** (alongside GPTs), **§14 Dots and Agentic Features** (user is responsible for actions agents take, oversight, and purchases made on their behalf) and **§15 Sign in with ChatGPT**.
- **Privacy Policy** (`/policies/privacy-policy/`, Updated Sept 10, 2026; was May 18) — all **Sora** references removed (products list, Sora characters, Sora videos); advertiser-data language broadened ("we receive information from advertisers… to measure and improve the effectiveness of our Services, including ads") (the third-party ad-promotion choice is no longer listed in the quick user-choices bullet, though still described elsewhere in the policy); the **Atlas** browser is no longer mentioned anywhere in the policy.
- **Merchant Feed Terms** (`/policies/merchant-feed-terms-of-service/`, Updated Oct 13, 2026) — new clause: merchants **may not block OpenAI's web crawlers via robots.txt** or similar, and must allowlist OpenAI's signed **Web Bot Auth** agent traffic.
- **Sub-processor list** (Oct 14, 2026) — Cloudflare added (Regional Services for `us.api` / `eu.api` TLS termination), new processing countries (Belgium, Denmark, Malaysia, New Zealand, Singapore), new contracting entity **OAI International, Inc.**
- **Supplier Code of Conduct** — full rewrite (Oct 15, 2026; previous Oct 10, 2023), now aligned to the Responsible Business Alliance code, UNGPs and ILO principles.
- **Advertising Terms** (Oct 15, 2026) — restructured; Brazil customers now governed by new **Brazil Advertising Terms**. Also updated: Developer Apps Terms (Sept 28), Commerce Policies (Sept 29), Service Credit Terms (Nov 12), Cookie Policy (Oct 22), ChatGPT Sites Terms (Nov 6).

**Pricing & product pages**
- **Business pricing** (`/business/pricing/`) — new line: **"Starting in December, plan usage will have a shared limit across all of ChatGPT and Codex."** The Pro-tier claim "5x more usage than standard" softened to "More usage than standard". Model rows now GPT‑6.1 Sol / GPT‑6 Astra / GPT‑6 Sol / GPT‑6 Luna; **Dots** row added (Business Premium / Enterprise); **Canvas** row removed; Office extensions now include Word.
- **Codex** (`/codex/`) — rebuilt as "Build anything with Codex" with on-page plan pricing (Plus $20, Pro $100, Business $20/user/mo), cloud tasks, automatic PR review, plugins.
- **Daybreak** (`/daybreak/`) — restructured into **Daybreak Blue** (defensive) and **Daybreak Red** (authorized red teaming/exploit validation) access tiers with an application process; headline "**$1 billion in Daybreak credits**" removed — the $1B is now described as "subsidized Daybreak access, training, technical support, and partnerships".
- **Business home** (`/business/`) — DevDay countdown replaced by "What's new for business" grid (Cyber at the Frontier keynote Nov 12, Businesses in ChatGPT, Private Intelligence, GPT‑6.1 Terra/Sol, dots, webinars).
- **Homepage** (`/`) — adds a "Talk to us" button and a "Our latest Daybreak announcements — Event Nov 12, 2026" feature.
- **Release notes** (`/products/release-notes/`) — newest entries through Nov 10, 2026 (GPT‑6 Luna inference residency in India/Japan/Australia; Business Hub).

**News-post updates (editor's notes added)**
- `/index/our-decision-on-cursor-following-its-acquisition-by-spacex/` — "Update on November 12, 2026: We've temporarily extended Cursor's access to our models beyond November 12."
- `/index/apple-is-getting-this-wrong/` — "October 14, 2026 update: Read our court filing regarding our concerns that Apple has obtained OpenAI trade secret and confidential information."
- `/new-york-times/` — new entries: "The court grants our motion to strike" and amicus support for fair use (links new post *Fair use benefits everyone*, Oct 30).
- `/index/election-safeguards-2026/` — Oct 20 update ahead of U.S. midterms: Democracy Works voter-info integration, AP live vote counts (U.S. and Brazil), cartoon-style "stylization" for election-interference image requests.
- `/index/gpt-6-astra/` — banner pointing to GPT‑6.1 Sol. `/index/introducing-dots/` — Nov 3 note: dots can now also run on GPT‑6.1 Terra.
- **Legacy model archival notes**: five more launch posts — `learning-to-reason-with-llms`, `introducing-openai-o1-preview`, `openai-o1-mini-advancing-cost-efficient-reasoning`, `openai-o3-mini`, `introducing-o3-and-o4-mini` — gained "This post introduced … no longer available in ChatGPT and deprecated in the API" banners (24 archived `/index/` posts now carry such a banner).
- `/collective-cyberdefense/` — signatory wall reformatted (inline comma list → bulleted list; self-serve "Add your organization" form removed).

## 3. Routine updates

~1,370 pages changed only by the sitewide nav/footer template, "Loading…" placeholder removal, newsletter box, external-link labels, image CDN URL rotation, or "latest posts" recirculation widgets. ~89 plugin directory pages were regenerated (new copy/tags/install links) without meaningful policy content. Full list in `diff.json`.

## 4. New pages (253) — themes

Dates in brackets are the article's own visible date (OpenAI's claim); all were first observed by this repo at 2026-11-13T09-16Z.

**New models**
- **GPT‑6.1 Sol** (`/index/introducing-gpt-6-1-sol/`, undated) — "near‑Astra intelligence for a fifth of the price": API $2 / $10 per M input/output tokens, $0.10 cached (vs GPT‑6 Astra $10/$50, GPT‑6 Luna $0.10/$0.50). Referenced by a Sept 29 banner on the GPT‑6 Astra post, so likely launched around DevDay (Sept 29).
- **GPT‑6.1 Terra** (`/index/introducing-gpt-6-1-terra/`, undated; dots note dates it ≤ Nov 3) — fast/cheap model for computer use and visual reasoning; API prices 50% below GPT‑5.6 Terra and GPT‑6.1 Sol.
- **GPT‑6 for everyone + "Intelligent UI"** (`/index/gpt-6-for-everyone/`, [Oct 7]) — GPT‑6 rolled out to free ChatGPT users (1.2B weekly users); answers can now render interactive UIs.
- **GPT‑6 Cyber** (`/index/introducing-gpt-6-cyber/`, [Nov 5]) — cybersecurity model, +51% relative on ExploitGym vs GPT‑5.6 Cyber.
- **Images 2.6** [Nov 4] (GIF/motion output); **Decisions API** [Oct 22] (fast, cheap classification/routing calls); model guide for the GPT‑6 family [Oct 2].

**DevDay 2026 (Sept 29) and agents**
- `/index/devday-2026-recap/` [Sept 29] — "20+ major announcements"; `/devday/2026/` hub page.
- **Dots** (`/index/introducing-dots/` [Sept 29]) — always-on GPT‑6 Astra-powered agents with their own cloud computer, 4,000+ app plugins, available in ChatGPT/Slack/Teams and Microsoft Agent 365.
- **Businesses in ChatGPT** (`/index/introducing-businesses-chatgpt/` [Nov 10], `/business/businesses-in-chatgpt/`, plus 3 new policies: Businesses in ChatGPT, its Terms, and a Business Agents Policy) — businesses can claim a profile via "Business Hub" and deploy "Business Agents" in ChatGPT.
- **ChatGPT Wallet** — new Terms and Privacy Notice (lastmod Nov 13): users can save a payment card and have ChatGPT use a linked payment credential to buy from merchants. No announcement post yet in the sitemap.
- **Sign in with ChatGPT** — new Terms + interest form.
- **OpenAI Marketplace** (`/business/marketplace/` + Customer Program Terms) — buy third-party partner products using existing OpenAI spend commitments.
- **OpenAI Private Intelligence** (`/business/private-intelligence/`, `/privacy-by-product/`, interest form) — privacy/control tier for sensitive enterprise work.

**Cybersecurity push (Daybreak)** — the single largest theme
- "A thousand fewer paths to root" [Nov 4]: an autonomous pipeline validated and patched **948 Linux local-privilege-escalation bugs for $1.2M** in API cost.
- **Patch the Planet** coordinated PHP disclosure ("PHP2Shell") [Oct 21]; Daybreak Red in AWS GovCloud [Nov 4]; bigger bug bounties, Hacktron partnership, next internal security sprint with Cathedral [Nov 2–6]; *Securing our frontier model training environment* [Oct 23]; *Disrupting a coordinated model-distillation campaign* [Sept 30]; *Disrupting AI-enabled "false front" operations* [Oct 8]; *Democratic governance of frontier AI, part II: Empowering cyber defenders* [Oct 21].
- New product pages `/daybreak/defense-factory/`, `/daybreak/red-team/`, `/cybersecurity/`, `/cyber-at-the-frontier/` (Nov 12 keynote), 3 new security-firm partner pages (Bishop Fox, SpecterOps, TrustedSec) and ~10 customer stories (Block, Cisco, Cloudflare, Check Point, SentinelOne, Sophos, Cogent, CodeRabbit, Greptile…).

**Safety, alignment & policy**
- *How we will do better for Australia* [Sept 28] — **apology**: "In June, during internal training and evaluation our models accessed Australian government websites in ways they were not authorised to." (Fits with the September *Hugging Face incident and misalignment* page.)
- *How we detect frontier model misalignment* [Oct 29]; *Control Room* (undated) — system to detect issues and "stop models in their tracks"; *Towards safety cases for frontier AI training* [Sept 28]; **updated Model Spec** [Oct 29]; *Broad access through consistent standards* (Usage Policies update) [Oct 21]; EU text-provenance approach [Oct 5]; community safety report + firearms restrictions for teens [Oct 30]; $2M pledge on AI and children's safety [Nov 12].
- *Fair use benefits everyone* [Oct 30]; *Making it easier for websites to express AI training preferences* [Oct 30].

**Corporate**
- **Acquisitions:** Orchestra Bio (drug-development platform, folded into Rosalind) [Oct 20]; **Pierre Computer Company** (Code Storage, Git tooling for Codex) [Nov 4].
- **Hires:** Jill Hazelbaker, Chief Corporate Affairs Officer [Nov 3]; Dan Driscoll, Senior Counselor for National Security Modernization [Nov 2].
- **Partnerships/distribution:** OpenAI models coming to **Google Cloud** (Model Garden) [Oct 21]; ChatGPT Enterprise in **AWS Marketplace** [Nov 9]; Oracle apps in ChatGPT [Oct 27]; ServiceNow [Oct 28]; Atlassian [Oct 6]; Poland's NASK [Oct 23]; Uber rolling ChatGPT Work to 30,000+ employees [Oct 22].
- **Infrastructure:** Grid Protectors Program [Nov 2]; *Setting a new standard for responsible AI infrastructure* [Nov 5] + `/compute-campus/`.
- **Ads business:** ChatGPT Ads in 26 more countries, 100k+ advertisers [Oct 21]; new visual ad format [Oct 5]; Aleph as exclusive reseller in 44 countries [Nov 12]; engineering post on the ad stack [Oct 21]; 3 ad customer stories.
- **Research:** LifeVal benchmark [Nov 2]; BioBasicsBench [Nov 6]; new math results [Oct 6] and three discoveries with academic communities [Oct 26]; physical-world engineering [Nov 3]; COBOL/Fortran low-resource languages [Oct 19]; Rosalind Academic Plan [Oct 15]; Upwork freelance study [Nov 10]; Signals work-activities data [Oct 26]; two essays in the new "Intelligence Age" series.
- **Engineering blog:** Scaling Git at OpenAI ("Pando") [Nov 2]; storage at 1B users part II [Oct 23].
- Plus ~50 customer stories, 47 new plugin directory pages, 25 relocated/new `/business/learn/` items, 6 new `/business/solutions/` pages (most are relocations from `/solutions/`), 7 merch products (incl. a GPT‑6 longsleeve and "dots" tee/tote).

## 5. Removals (30)

Checked each removed URL live (2026-11-13, curl-cffi, no redirect following):
- **Relocations (308/307 redirects; content lives on at the new URL):** 6 business webinars/guides → `/business/learn/...`; `/solutions/...` (5) → `/business/solutions/...`; `/index/ada/` and `/index/blue-j/` → `/business/customer-stories/...`; `/business/partners/pathfindr/` → `/business/partners/affinda/` (company renamed); `/business/plugins/wordpress-com/` → `/business/plugins/wordpress/`; `/economic-research-exchange/` → `/economic-research-collaborators/`; `/form/ultrafast/` → developer docs "Ultrafast mode" guide.
- **Folded into hubs:** **`/prism/`** (the free AI LaTeX/scientific-writing workspace) → 308 to `/science/`; **`/residency/`** (OpenAI Residency program) → 307 (temporary) to `/research/`.
- **Gone (404):** partner pages for **Canva, Dropbox, Gusto, HubSpot, QuickBooks, Stripe**; plugin pages `atlassian-rovo`, `litera-lito`, `mcp-server-for-wordpress`, `oracle-analytics` (successors `atlassian`, `litera`, `wordpress`, `oracle-analytics-cloud` were added); `/daybreak/partners-new/` (staging copy of the Daybreak Defense Network page).

Last snapshots: `git log -- pages/openai.com/<path>/index.md`.

## Appendix A — all anomalies (machine list)

- `reappeared_url` — https://openai.com/business/plugins/alpaca/ — previously seen first_seen=2026-07-10T09-16Z last_seen=2026-09-24T09-16Z; absent from baseline, back now
- `reappeared_url` — https://openai.com/form/codex-ambassadors/ — previously seen first_seen=2026-05-07T09-01Z last_seen=2026-06-24; absent from baseline, back now
- `reappeared_url` — https://openai.com/policies/row-privacy-policy/ — previously seen first_seen=2026-05-07T09-01Z last_seen=2026-05-27T09-17Z; absent from baseline, back now
- `sitemap_migration` — https://openai.com/business/learn/how-our-finance-team-uses-chatgpt-work/ — moved from ['sitemap.xml_learn-guides.xml'] to ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/learn/intelligence-at-work-financial-services/ — moved from ['sitemap.xml_page.xml'] to ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/learn/agent-security-enterprise/ — moved from ['sitemap.xml_page.xml'] to ['sitemap.xml_learn-guides.xml']
- `sitemap_migration` — https://openai.com/business/plugins/tableau/ — moved from ['sitemap.xml_plugins-data-research.xml'] to ['sitemap.xml_plugins-productivity.xml']
- `sitemap_migration` — https://openai.com/business/plugins/sync-labs/ — moved from ['sitemap.xml_plugins-productivity.xml'] to ['sitemap.xml_plugins-design-creative.xml']
- `sitemap_migration` — https://openai.com/business/learn/how-our-sales-team-uses-chatgpt-work/ — moved from ['sitemap.xml_page.xml'] to ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/plugins/parallel-search/ — moved from ['sitemap.xml_plugins-engineering-it.xml'] to ['sitemap.xml_plugins-productivity.xml']
- `sitemap_migration` — https://openai.com/business/learn/intelligence-at-work-cyber/ — moved from ['sitemap.xml_page.xml'] to ['sitemap.xml_learn-webinars.xml']
- `sitemap_migration` — https://openai.com/business/learn/download-the-chatgpt-work-guide-for-sales-teams/ — moved from ['sitemap.xml_page.xml'] to ['sitemap.xml_learn-guides.xml']
- `missing_lastmod_new_url` — https://openai.com/ads/blog/chatgpt-ads-increases-its-market-presence/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/ads/customers/evernote/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/ads/customers/flipsnack/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/ads/customers/vistaprint/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/index/introducing-gpt-6-1-sol/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/index/introducing-gpt-6-1-terra/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/blossom-tee-gray/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/dots-tee/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/dots-tote/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/gpt-6-longsleeve/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/modretro-chromatic-case-codex-edition/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/modretro-codex-cartridge/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `missing_lastmod_new_url` — https://openai.com/supply/product/theresetcompany-hoodie/ — new URL listed in sitemap with no <lastmod> at all (most /index/ posts carry one)
- `lastmod_dropped` — https://openai.com/index/advancing-independent-research-ai-alignment/ — <lastmod> was 2026-09-25T19:18:24.670Z at baseline; now the sitemap entry has no <lastmod>
- `in_page_date_predates_observation` — https://openai.com/policies/privacy-policy/ — page now says 'Updated: September 10, 2026', but sitemap <lastmod> stayed 2026-09-04T14:03:36Z through our 2026-09-28T09:17Z observation; new text first observed this run (current <lastmod> 2026-10-23T23:55:38.296Z)
- `in_page_date_reset` — https://openai.com/index/wayfair/ — customer story rewritten under same URL; visible publication date changed March 11, 2026 -> September 25, 2026
- `in_page_date_reset` — https://openai.com/index/lowes/ — customer story rewritten under same URL; visible publication date changed (undated) -> September 25, 2026
- `in_page_date_reset` — https://openai.com/index/retell-ai/ — customer story rewritten under same URL; visible publication date changed June 26, 2025 -> October 27, 2026
- `stale_page_reappeared` — https://openai.com/policies/row-privacy-policy/ — reappeared URL serves an older privacy policy ('Updated: February 6, 2026') that still references Sora, while the main /policies/privacy-policy/ (Updated Sept 10, 2026) has removed Sora references

_(+46 low-signal `lastmod_predates_first_seen_gap` entries in diff.json)_

## Appendix B — all added URLs

| URL | sitemap `<lastmod>` | title | file |
|---|---|---|---|
| /ads/blog/chatgpt-ads-increases-its-market-presence/ | — | ChatGPT Ads increases its market presence in 44 countries | [md](../../pages/openai.com/ads/blog/chatgpt-ads-increases-its-market-presence/index.md) |
| /ads/customers/evernote/ | — | Evernote turns AI-driven discovery into paid subscriptions | [md](../../pages/openai.com/ads/customers/evernote/index.md) |
| /ads/customers/flipsnack/ | — | Flipsnack grows product signups with conversion optimization | [md](../../pages/openai.com/ads/customers/flipsnack/index.md) |
| /ads/customers/vistaprint/ | — | How VistaPrint helps small businesses get the word out | [md](../../pages/openai.com/ads/customers/vistaprint/index.md) |
| /business/businesses-in-chatgpt/ | 2026-11-13T00:45:08.317Z | Your business, in ChatGPT | [md](../../pages/openai.com/business/businesses-in-chatgpt/index.md) |
| /business/contact-sales-retail/ | 2026-10-22T09:35:52.893Z | Contact retail sales | [md](../../pages/openai.com/business/contact-sales-retail/index.md) |
| /business/customer-stories/ada/ | 2026-11-10T21:22:00.575Z | Ada uses GPT‑4 to deliver a new customer service standard | [md](../../pages/openai.com/business/customer-stories/ada/index.md) |
| /business/customer-stories/amplitude/ | 2026-11-13T08:44:57.090Z | How Amplitude ships product improvements in 1–2 days with OpenAI | [md](../../pages/openai.com/business/customer-stories/amplitude/index.md) |
| /business/customer-stories/blue-j/ | 2026-11-10T21:25:49.512Z | Blue J’s approach for scaling fast in complex, regulated domains | [md](../../pages/openai.com/business/customer-stories/blue-j/index.md) |
| /business/customer-stories/gondola/ | 2026-11-13T08:36:43.222Z | Gondola doubles revenue as its team builds more with Codex | [md](../../pages/openai.com/business/customer-stories/gondola/index.md) |
| /business/customer-stories/holidays-extras-codex/ | 2026-11-13T06:10:58.891Z | Holiday Extras is rethinking what it can build with Codex | [md](../../pages/openai.com/business/customer-stories/holidays-extras-codex/index.md) |
| /business/forward-deployed-engineering/ | 2026-11-10T19:32:33.484Z | Forward Deployed Engineering | [md](../../pages/openai.com/business/forward-deployed-engineering/index.md) |
| /business/images-api/ | 2026-11-06T06:29:00.578Z | Build with the state-of-the-art image generation models | [md](../../pages/openai.com/business/images-api/index.md) |
| /business/learn/automate-complex-workflows-with-openai-o3/ | 2026-10-23T00:34:42.478Z | Automate complex workflows with OpenAI o3 | [md](../../pages/openai.com/business/learn/automate-complex-workflows-with-openai-o3/index.md) |
| /business/learn/board-guide-cybersecurity-ai/ | 2026-10-09T07:16:10.956Z | Download the board guide to cybersecurity and AI | [md](../../pages/openai.com/business/learn/board-guide-cybersecurity-ai/index.md) |
| /business/learn/collaborate-and-write-with-gpt-4o/ | 2026-10-23T04:35:53.989Z | Collaborate and write with GPT‑4o | [md](../../pages/openai.com/business/learn/collaborate-and-write-with-gpt-4o/index.md) |
| /business/learn/connect-internal-knowledge-from-google-drive/ | 2026-10-22T22:58:48.763Z | Connect internal knowledge from Google Drive | [md](../../pages/openai.com/business/learn/connect-internal-knowledge-from-google-drive/index.md) |
| /business/learn/create-on-brand-visuals-with-image-generation/ | 2026-10-23T09:21:55.298Z | Create on-brand visuals with image generation | [md](../../pages/openai.com/business/learn/create-on-brand-visuals-with-image-generation/index.md) |
| /business/learn/creating-a-contextual-workspace-in-chatgpt/ | 2026-10-21T16:04:20.339Z | Creating a contextual workspace in ChatGPT | [md](../../pages/openai.com/business/learn/creating-a-contextual-workspace-in-chatgpt/index.md) |
| /business/learn/delegate-work-to-chatgpt-agent/ | 2026-10-21T15:52:32.152Z | Delegate work to ChatGPT agent | [md](../../pages/openai.com/business/learn/delegate-work-to-chatgpt-agent/index.md) |
| /business/learn/enabling-a-data-driven-workforce-webinar/ | 2026-11-10T21:25:43.585Z | Enabling a data-driven workforce | [md](../../pages/openai.com/business/learn/enabling-a-data-driven-workforce-webinar/index.md) |
| /business/learn/fine-tuning-gpt-4o-webinar/ | 2026-11-10T21:09:49.430Z | Fine-tuning GPT‑4o | [md](../../pages/openai.com/business/learn/fine-tuning-gpt-4o-webinar/index.md) |
| /business/learn/gpt-5-our-best-model-for-work/ | 2026-10-23T08:06:52.377Z | GPT‑5: Our best model for work | [md](../../pages/openai.com/business/learn/gpt-5-our-best-model-for-work/index.md) |
| /business/learn/gpt-live-1-webinar/ | 2026-10-22T02:48:44.212Z | Building with GPT‑Live‑1 and Cognition | [md](../../pages/openai.com/business/learn/gpt-live-1-webinar/index.md) |
| /business/learn/how-openai-uses-chatgpt-atlas-at-work/ | 2026-10-25T16:53:23.411Z | How OpenAI uses ChatGPT Atlas at work | [md](../../pages/openai.com/business/learn/how-openai-uses-chatgpt-atlas-at-work/index.md) |
| /business/learn/how-openai-uses-codex/ | 2026-11-10T21:24:20.344Z | How OpenAI uses Codex | [md](../../pages/openai.com/business/learn/how-openai-uses-codex/index.md) |
| /business/learn/identifying-and-scaling-ai-use-cases/ | 2026-11-10T21:24:23.149Z | Identifying and scaling AI use cases | [md](../../pages/openai.com/business/learn/identifying-and-scaling-ai-use-cases/index.md) |
| /business/learn/market-research-with-chatgpt/ | 2026-10-21T17:07:06.880Z | Market research with ChatGPT | [md](../../pages/openai.com/business/learn/market-research-with-chatgpt/index.md) |
| /business/learn/new-in-chatgpt-for-business-april-updates-2025/ | 2026-11-10T21:25:25.666Z | New in ChatGPT for Business: April 2025 | [md](../../pages/openai.com/business/learn/new-in-chatgpt-for-business-april-updates-2025/index.md) |
| /business/learn/new-in-chatgpt-for-work-march-updates-2025/ | 2026-11-10T21:25:02.878Z | New in ChatGPT for Business: March 2025 | [md](../../pages/openai.com/business/learn/new-in-chatgpt-for-work-march-updates-2025/index.md) |
| /business/learn/personalize-chatgpt-with-custom-instructions/ | 2026-10-21T16:15:58.111Z | Personalize ChatGPT with custom instructions | [md](../../pages/openai.com/business/learn/personalize-chatgpt-with-custom-instructions/index.md) |
| /business/learn/php2shell-webinar/ | 2026-11-04T23:00:35.005Z | PHP2Shell: What to know now and prepare for next | [md](../../pages/openai.com/business/learn/php2shell-webinar/index.md) |
| /business/learn/prototyping-with-canvas-in-chatgpt/ | 2026-10-21T15:05:27.118Z | Prototyping with canvas in ChatGPT | [md](../../pages/openai.com/business/learn/prototyping-with-canvas-in-chatgpt/index.md) |
| /business/learn/shipping-code-to-your-ide-with-chatgpt/ | 2026-10-21T16:15:26.286Z | Shipping code to your IDE with ChatGPT | [md](../../pages/openai.com/business/learn/shipping-code-to-your-ide-with-chatgpt/index.md) |
| /business/learn/strategic-planning-with-chatgpt/ | 2026-10-22T22:51:04.962Z | Strategic planning with ChatGPT | [md](../../pages/openai.com/business/learn/strategic-planning-with-chatgpt/index.md) |
| /business/learn/using-codex-across-the-software-development-lifecycle/ | 2026-10-25T19:49:54.121Z | Using Codex across the software development lifecycle | [md](../../pages/openai.com/business/learn/using-codex-across-the-software-development-lifecycle/index.md) |
| /business/learn/vision-and-voice-in-chatgpt/ | 2026-10-23T00:37:50.720Z | Vision and voice in ChatGPT | [md](../../pages/openai.com/business/learn/vision-and-voice-in-chatgpt/index.md) |
| /business/learn/writing-with-canvas-in-chatgpt/ | 2026-10-21T13:41:25.709Z | Writing with canvas in ChatGPT | [md](../../pages/openai.com/business/learn/writing-with-canvas-in-chatgpt/index.md) |
| /business/marketplace/ | 2026-11-09T18:33:34.396Z | OpenAI Marketplace | [md](../../pages/openai.com/business/marketplace/index.md) |
| /business/partners/affinda/ | 2026-10-29T05:53:37.906Z | Affinda (formerly Pathfindr) | [md](../../pages/openai.com/business/partners/affinda/index.md) |
| /business/partners/bishop-fox/ | 2026-10-15T21:09:24.263Z | Bishop Fox | [md](../../pages/openai.com/business/partners/bishop-fox/index.md) |
| /business/partners/insight-enterprises/ | 2026-10-20T12:59:45.833Z | Insight Enterprises | [md](../../pages/openai.com/business/partners/insight-enterprises/index.md) |
| /business/partners/megazonecloud/ | 2026-10-29T06:08:41.362Z | MegazoneCloud | [md](../../pages/openai.com/business/partners/megazonecloud/index.md) |
| /business/partners/specterops/ | 2026-10-15T21:09:56.433Z | SpecterOps | [md](../../pages/openai.com/business/partners/specterops/index.md) |
| /business/partners/trustedsec/ | 2026-10-15T21:09:24.410Z | TrustedSec | [md](../../pages/openai.com/business/partners/trustedsec/index.md) |
| /business/plugins/actively/ | 2026-11-12T22:58:22.571Z | Actively | [md](../../pages/openai.com/business/plugins/actively/index.md) |
| /business/plugins/aiva/ | 2026-11-12T06:08:32.986Z | Aiva | [md](../../pages/openai.com/business/plugins/aiva/index.md) |
| /business/plugins/alpaca/ | 2026-11-10T21:22:19.669Z | Alpaca Live | [md](../../pages/openai.com/business/plugins/alpaca/index.md) |
| /business/plugins/atlassian-teammate-graph/ | 2026-11-01T02:47:45.082Z | Atlassian Teamwork Graph CLI | [md](../../pages/openai.com/business/plugins/atlassian-teammate-graph/index.md) |
| /business/plugins/atlassian/ | 2026-10-31T20:25:40.630Z | Atlassian | [md](../../pages/openai.com/business/plugins/atlassian/index.md) |
| /business/plugins/backstory/ | 2026-11-13T01:24:17.450Z | Backstory | [md](../../pages/openai.com/business/plugins/backstory/index.md) |
| /business/plugins/bill/ | 2026-11-12T22:58:23.038Z | BILL | [md](../../pages/openai.com/business/plugins/bill/index.md) |
| /business/plugins/campfire/ | 2026-11-12T22:58:23.377Z | Campfire | [md](../../pages/openai.com/business/plugins/campfire/index.md) |
| /business/plugins/cargo/ | 2026-11-12T22:58:46.973Z | Cargo | [md](../../pages/openai.com/business/plugins/cargo/index.md) |
| /business/plugins/chili-piper/ | 2026-11-12T22:58:32.759Z | Chili Piper | [md](../../pages/openai.com/business/plugins/chili-piper/index.md) |
| /business/plugins/common-room/ | 2026-11-13T04:17:43.560Z | Common Room | [md](../../pages/openai.com/business/plugins/common-room/index.md) |
| /business/plugins/crayon/ | 2026-11-12T22:58:34.748Z | Crayon | [md](../../pages/openai.com/business/plugins/crayon/index.md) |
| /business/plugins/crossbeam/ | 2026-11-12T22:58:53.878Z | Crossbeam | [md](../../pages/openai.com/business/plugins/crossbeam/index.md) |
| /business/plugins/freshbooks/ | 2026-11-12T22:58:48.509Z | FreshBooks | [md](../../pages/openai.com/business/plugins/freshbooks/index.md) |
| /business/plugins/guru/ | 2026-11-12T22:58:23.777Z | Guru | [md](../../pages/openai.com/business/plugins/guru/index.md) |
| /business/plugins/klue/ | 2026-11-12T22:58:50.744Z | Klue | [md](../../pages/openai.com/business/plugins/klue/index.md) |
| /business/plugins/krea/ | 2026-11-01T00:21:14.837Z | Krea | [md](../../pages/openai.com/business/plugins/krea/index.md) |
| /business/plugins/leandata/ | 2026-11-12T22:58:39.521Z | LeanData MCP | [md](../../pages/openai.com/business/plugins/leandata/index.md) |
| /business/plugins/lemlist/ | 2026-11-12T22:58:49.666Z | lemlist | [md](../../pages/openai.com/business/plugins/lemlist/index.md) |
| /business/plugins/lightfield/ | 2026-11-12T22:58:42.813Z | Lightfield | [md](../../pages/openai.com/business/plugins/lightfield/index.md) |
| /business/plugins/litera/ | 2026-11-05T19:27:02.488Z | Litera | [md](../../pages/openai.com/business/plugins/litera/index.md) |
| /business/plugins/loopio-eu/ | 2026-11-12T22:58:37.875Z | Loopio EU | [md](../../pages/openai.com/business/plugins/loopio-eu/index.md) |
| /business/plugins/loopio/ | 2026-11-12T22:58:49.059Z | Loopio | [md](../../pages/openai.com/business/plugins/loopio/index.md) |
| /business/plugins/luma-health/ | 2026-11-12T06:08:34.258Z | Luma Health | [md](../../pages/openai.com/business/plugins/luma-health/index.md) |
| /business/plugins/meticulate/ | 2026-11-12T22:58:42.014Z | Meticulate | [md](../../pages/openai.com/business/plugins/meticulate/index.md) |
| /business/plugins/nooks/ | 2026-11-12T22:58:52.962Z | Nooks | [md](../../pages/openai.com/business/plugins/nooks/index.md) |
| /business/plugins/oracle-analytics-cloud/ | 2026-11-01T04:40:00.946Z | Oracle Analytics | [md](../../pages/openai.com/business/plugins/oracle-analytics-cloud/index.md) |
| /business/plugins/oracle-netsuite-ai-companion/ | 2026-11-01T00:53:54.747Z | NetSuite AI Companion | [md](../../pages/openai.com/business/plugins/oracle-netsuite-ai-companion/index.md) |
| /business/plugins/oracle-netsuite-finance-analyst/ | 2026-11-01T03:15:13.444Z | NetSuite Finance Analyst | [md](../../pages/openai.com/business/plugins/oracle-netsuite-finance-analyst/index.md) |
| /business/plugins/oracle-netsuite-quickstart/ | 2026-11-05T19:23:35.915Z | QuickStart | [md](../../pages/openai.com/business/plugins/oracle-netsuite-quickstart/index.md) |
| /business/plugins/oracle-netsuite-suitecloud/ | 2026-11-01T02:28:22.985Z | NetSuite SuiteCloud | [md](../../pages/openai.com/business/plugins/oracle-netsuite-suitecloud/index.md) |
| /business/plugins/oracle-netsuite-suiteskills/ | 2026-11-05T19:22:40.333Z | NetSuite SuiteSkills | [md](../../pages/openai.com/business/plugins/oracle-netsuite-suiteskills/index.md) |
| /business/plugins/pipedrive/ | 2026-11-13T05:43:28.623Z | Pipedrive | [md](../../pages/openai.com/business/plugins/pipedrive/index.md) |
| /business/plugins/responsive/ | 2026-11-12T22:58:23.639Z | Responsive | [md](../../pages/openai.com/business/plugins/responsive/index.md) |
| /business/plugins/rillet/ | 2026-11-12T22:58:35.318Z | Rillet | [md](../../pages/openai.com/business/plugins/rillet/index.md) |
| /business/plugins/rox/ | 2026-11-13T03:59:12.921Z | Rox | [md](../../pages/openai.com/business/plugins/rox/index.md) |
| /business/plugins/salesloft/ | 2026-11-13T01:20:17.128Z | Salesloft | [md](../../pages/openai.com/business/plugins/salesloft/index.md) |
| /business/plugins/sandstone/ | 2026-10-31T23:26:30.974Z | Sandstone | [md](../../pages/openai.com/business/plugins/sandstone/index.md) |
| /business/plugins/servicenow/ | 2026-11-03T13:42:39.622Z | ServiceNow | [md](../../pages/openai.com/business/plugins/servicenow/index.md) |
| /business/plugins/spacefast/ | 2026-11-10T20:46:18.918Z | Spacefast | [md](../../pages/openai.com/business/plugins/spacefast/index.md) |
| /business/plugins/stedi/ | 2026-11-12T06:08:32.945Z | Stedi | [md](../../pages/openai.com/business/plugins/stedi/index.md) |
| /business/plugins/subsalt/ | 2026-11-12T06:08:32.963Z | Subsalt | [md](../../pages/openai.com/business/plugins/subsalt/index.md) |
| /business/plugins/turquoise-health/ | 2026-11-12T06:08:33.880Z | Turquoise | [md](../../pages/openai.com/business/plugins/turquoise-health/index.md) |
| /business/plugins/uptodate-expert-ai/ | 2026-11-12T06:08:34.254Z | UpToDate Expert AI | [md](../../pages/openai.com/business/plugins/uptodate-expert-ai/index.md) |
| /business/plugins/wordpress/ | 2026-11-10T22:49:40.230Z | WordPress | [md](../../pages/openai.com/business/plugins/wordpress/index.md) |
| /business/plugins/workiva/ | 2026-11-12T22:58:22.773Z | Workiva | [md](../../pages/openai.com/business/plugins/workiva/index.md) |
| /business/plugins/yardi-virtuoso/ | 2026-11-12T22:58:35.867Z | Yardi Virtuoso | [md](../../pages/openai.com/business/plugins/yardi-virtuoso/index.md) |
| /business/private-intelligence/ | 2026-11-07T09:38:24.607Z | OpenAI Private Intelligence | [md](../../pages/openai.com/business/private-intelligence/index.md) |
| /business/private-intelligence/privacy-by-product/ | 2026-11-04T21:45:17.962Z | Privacy by product | [md](../../pages/openai.com/business/private-intelligence/privacy-by-product/index.md) |
| /business/solutions/content-creation/ | 2026-11-10T21:22:51.489Z | Content creation for everyone in your company | [md](../../pages/openai.com/business/solutions/content-creation/index.md) |
| /business/solutions/data-analysis/ | 2026-11-10T21:25:04.246Z | Connect every dataset and team with intelligence that scales | [md](../../pages/openai.com/business/solutions/data-analysis/index.md) |
| /business/solutions/financial-services/ | 2026-11-11T04:57:56.838Z | Frontier intelligence. Built for financial services. | [md](../../pages/openai.com/business/solutions/financial-services/index.md) |
| /business/solutions/knowledge-retrieval/ | 2026-11-10T21:06:49.068Z | Trusted answers, backed by your data | [md](../../pages/openai.com/business/solutions/knowledge-retrieval/index.md) |
| /business/solutions/legal/ | 2026-11-03T00:35:04.801Z | Connected intelligence for ambitious legal teams | [md](../../pages/openai.com/business/solutions/legal/index.md) |
| /business/solutions/retail/ | 2026-11-10T21:23:45.259Z | Stay ahead as AI reshapes shopping | [md](../../pages/openai.com/business/solutions/retail/index.md) |
| /codex-originals/ | 2026-10-24T03:16:35.181Z | Codex Originals | [md](../../pages/openai.com/codex-originals/index.md) |
| /compute-campus/ | 2026-11-11T01:39:38.706Z | Building AI infrastructure that works for America | [md](../../pages/openai.com/compute-campus/index.md) |
| /cyber-at-the-frontier/ | 2026-11-13T09:16:08.313Z | Cyber at the Frontier | [md](../../pages/openai.com/cyber-at-the-frontier/index.md) |
| /cybersecurity/ | 2026-11-10T07:55:30.298Z | Cybersecurity research | [md](../../pages/openai.com/cybersecurity/index.md) |
| /daybreak/defense-factory/ | 2026-11-13T02:08:30.822Z | Turn your security backlog into fixes | [md](../../pages/openai.com/daybreak/defense-factory/index.md) |
| /daybreak/red-team/ | 2026-11-12T23:13:46.480Z | AI penetration testing for web applications | [md](../../pages/openai.com/daybreak/red-team/index.md) |
| /devday/2026/ | 2026-11-12T16:00:33.124Z |  | [md](../../pages/openai.com/devday/2026/index.md) |
| /economic-research-collaborators/ | 2026-10-30T12:34:39.411Z | OpenAI Economic Research Collaborators | [md](../../pages/openai.com/economic-research-collaborators/index.md) |
| /form/codex-ambassadors/ | 2026-11-05T11:53:06.545Z | Codex Ambassador application form | [md](../../pages/openai.com/form/codex-ambassadors/index.md) |
| /form/codex-originals/ | 2026-11-12T18:40:31.078Z | Are you a Codex Original? | [md](../../pages/openai.com/form/codex-originals/index.md) |
| /form/computer-use-research-collaboration/ | 2026-10-19T11:11:45.835Z | Computer-use research collaboration | [md](../../pages/openai.com/form/computer-use-research-collaboration/index.md) |
| /form/daybreak-red-team/ | 2026-11-12T22:26:00.720Z | Register your interest in Daybreak Red Team | [md](../../pages/openai.com/form/daybreak-red-team/index.md) |
| /form/openai-on-google-cloud/ | 2026-11-07T10:04:32.839Z | Get access to OpenAI frontier models on Google Cloud | [md](../../pages/openai.com/form/openai-on-google-cloud/index.md) |
| /form/private-intelligence-interest/ | 2026-10-30T07:26:05.177Z | Register your interest in Private Intelligence | [md](../../pages/openai.com/form/private-intelligence-interest/index.md) |
| /form/sign-in-with-chatgpt-interest/ | 2026-10-30T18:51:00.428Z | Sign in with ChatGPT interest form | [md](../../pages/openai.com/form/sign-in-with-chatgpt-interest/index.md) |
| /index/a-thousand-fewer-paths-to-root/ | 2026-11-12T23:54:29.743Z | A thousand fewer paths to root | [md](../../pages/openai.com/index/a-thousand-fewer-paths-to-root/index.md) |
| /index/accelerating-engineering-for-the-physical-world/ | 2026-11-10T18:04:42.427Z | Accelerating engineering for the physical world | [md](../../pages/openai.com/index/accelerating-engineering-for-the-physical-world/index.md) |
| /index/advancing-computer-use-with-ironclad/ | 2026-11-08T12:36:54.760Z | Advancing computer use with Ironclad | [md](../../pages/openai.com/index/advancing-computer-use-with-ironclad/index.md) |
| /index/ai-effect-on-freelance-work/ | 2026-11-12T23:54:30.538Z | Work at the Frontier: | [md](../../pages/openai.com/index/ai-effect-on-freelance-work/index.md) |
| /index/albertsons-reimagining-retail/ | 2026-11-12T23:54:48.995Z | How Albertsons Companies is reimagining retail from the inside out | [md](../../pages/openai.com/index/albertsons-reimagining-retail/index.md) |
| /index/amp-beyond-coding/ | 2026-11-09T22:47:45.815Z | Amp puts AI agents to work beyond code with OpenAI models | [md](../../pages/openai.com/index/amp-beyond-coding/index.md) |
| /index/anima/ | 2026-11-09T22:47:39.264Z | Anima helps clinics cut call waits by 75% with GPT‑6 and GPT‑Live | [md](../../pages/openai.com/index/anima/index.md) |
| /index/asana-browser-agent/ | 2026-11-09T23:00:45.598Z | Asana cuts model costs 76x in browser tests with GPT‑6.1 Sol | [md](../../pages/openai.com/index/asana-browser-agent/index.md) |
| /index/atlassian-partnership/ | 2026-11-10T09:52:34.075Z | Atlassian and OpenAI expand partnership to turn enterprise knowledge into action | [md](../../pages/openai.com/index/atlassian-partnership/index.md) |
| /index/att-legal/ | 2026-11-09T22:50:10.628Z | How AT&T is rethinking in-house legal work with OpenAI | [md](../../pages/openai.com/index/att-legal/index.md) |
| /index/australian-universities-ai-native-graduates/ | 2026-11-13T09:12:10.368Z | Australian universities are creating AI-native graduates | [md](../../pages/openai.com/index/australian-universities-ai-native-graduates/index.md) |
| /index/basis-tax-workbook-with-astra/ | 2026-11-09T22:49:41.044Z | Basis completes a tax workbook 2x faster with GPT‑6 Astra | [md](../../pages/openai.com/index/basis-tax-workbook-with-astra/index.md) |
| /index/benefit-street-partners/ | 2026-11-09T22:50:14.046Z | Benefit Street Partners answers questions faster with Codex | [md](../../pages/openai.com/index/benefit-street-partners/index.md) |
| /index/block-ai-powered-security/ | 2026-11-09T22:46:15.453Z | How Block is building AI-powered security with OpenAI technology | [md](../../pages/openai.com/index/block-ai-powered-security/index.md) |
| /index/bloomsbury-football-foundation/ | 2026-11-13T05:22:40.172Z | Using ChatGPT to accelerate a charity’s growth | [md](../../pages/openai.com/index/bloomsbury-football-foundation/index.md) |
| /index/broad-access-through-consistent-standards/ | 2026-11-10T10:45:31.039Z | Broad access through consistent standards | [md](../../pages/openai.com/index/broad-access-through-consistent-standards/index.md) |
| /index/building-chatgpt-ad-stack/ | 2026-11-12T23:55:14.148Z | How we built ChatGPT’s novel ad stack for user trust and relevance | [md](../../pages/openai.com/index/building-chatgpt-ad-stack/index.md) |
| /index/building-scientific-understanding-with-academic-communities/ | 2026-11-12T23:55:05.943Z | Working with academic communities to build scientific understanding | [md](../../pages/openai.com/index/building-scientific-understanding-with-academic-communities/index.md) |
| /index/chatgpt-ads-expands-26-new-countries/ | 2026-11-10T12:56:56.431Z | ChatGPT Ads expands to 26 new countries as over 100,000 advertisers have used the platform | [md](../../pages/openai.com/index/chatgpt-ads-expands-26-new-countries/index.md) |
| /index/chatgpt-enterprise-aws-marketplace/ | 2026-11-12T23:54:33.853Z | ChatGPT Enterprise now available in AWS Marketplace | [md](../../pages/openai.com/index/chatgpt-enterprise-aws-marketplace/index.md) |
| /index/chatgpt-expanding-world-of-work/ | 2026-11-12T23:54:34.620Z | ChatGPT’s expanding world of work | [md](../../pages/openai.com/index/chatgpt-expanding-world-of-work/index.md) |
| /index/chatgpt-plus-for-veterans/ | 2026-11-12T23:54:28.349Z | ChatGPT Plus for veterans and servicemembers | [md](../../pages/openai.com/index/chatgpt-plus-for-veterans/index.md) |
| /index/chatham-financial/ | 2026-11-09T22:53:36.672Z | Chatham scales its capital markets expertise with OpenAI | [md](../../pages/openai.com/index/chatham-financial/index.md) |
| /index/check-point-daybreak/ | 2026-11-09T22:46:11.461Z | How Check Point accelerates vulnerability research with Daybreak | [md](../../pages/openai.com/index/check-point-daybreak/index.md) |
| /index/children-first-declaration/ | 2026-11-13T08:54:58.748Z | Supporting research on AI and children’s safety | [md](../../pages/openai.com/index/children-first-declaration/index.md) |
| /index/cisco-cyber/ | 2026-11-12T23:54:31.595Z | How Cisco defends at machine speed with OpenAI | [md](../../pages/openai.com/index/cisco-cyber/index.md) |
| /index/closing-ai-guidance-gap-education/ | 2026-11-10T22:04:58.188Z | Closing the AI guidance gap in education | [md](../../pages/openai.com/index/closing-ai-guidance-gap-education/index.md) |
| /index/cloudflare-cyber/ | 2026-11-09T22:48:38.487Z | Cloudflare links vulnerability discovery to defense with OpenAI | [md](../../pages/openai.com/index/cloudflare-cyber/index.md) |
| /index/coderabbit-codex-daybreak/ | 2026-11-12T23:54:46.455Z | CodeRabbit scales agentic software development and ships 20x more | [md](../../pages/openai.com/index/coderabbit-codex-daybreak/index.md) |
| /index/cogent-security/ | 2026-11-13T05:52:21.198Z | Cogent and OpenAI build cyber defense factories for enterprises | [md](../../pages/openai.com/index/cogent-security/index.md) |
| /index/community-safety-report-and-new-protections-for-teens/ | 2026-11-12T23:54:57.725Z | Community safety report and new protections for teens | [md](../../pages/openai.com/index/community-safety-report-and-new-protections-for-teens/index.md) |
| /index/control-room/ | 2026-11-12T23:54:47.666Z | Control Room | [md](../../pages/openai.com/index/control-room/index.md) |
| /index/coordinated-disclosure-of-critical-vulnerabilities/ | 2026-11-10T21:22:02.316Z | Patch the Planet: global response coordination as agents uncover critical vulnerabilities | [md](../../pages/openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/index.md) |
| /index/credit-saison/ | 2026-11-12T23:54:38.012Z | Credit Saison achieves 954% ROI in a ChatGPT Enterprise pilot | [md](../../pages/openai.com/index/credit-saison/index.md) |
| /index/cultfit-builds-with-codex/ | 2026-11-11T20:26:09.196Z | Cult.fit builds operational muscle with Codex | [md](../../pages/openai.com/index/cultfit-builds-with-codex/index.md) |
| /index/dan-driscoll-joins-openai/ | 2026-11-12T23:54:32.323Z | OpenAI appoints Dan Driscoll as Senior Counselor for National Security Modernization | [md](../../pages/openai.com/index/dan-driscoll-joins-openai/index.md) |
| /index/daybreak-red-aws-govcloud/ | 2026-11-12T23:54:34.019Z | Daybreak Red is now available in AWS GovCloud (US-East) | [md](../../pages/openai.com/index/daybreak-red-aws-govcloud/index.md) |
| /index/decisions-api/ | 2026-11-10T21:21:59.591Z | Build more responsive apps with the Decisions API | [md](../../pages/openai.com/index/decisions-api/index.md) |
| /index/devday-2026-recap/ | 2026-11-12T16:00:44.429Z | DevDay 2026 Recap | [md](../../pages/openai.com/index/devday-2026-recap/index.md) |
| /index/devrev-enterprise-self-service/ | 2026-11-09T22:49:27.209Z | DevRev delivers autonomous self-service with GPT‑6.1 Sol | [md](../../pages/openai.com/index/devrev-enterprise-self-service/index.md) |
| /index/disrupting-a-coordinated-model-distillation-campaign/ | 2026-11-12T23:54:49.592Z | Disrupting a coordinated model-distillation campaign | [md](../../pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md) |
| /index/disrupting-ai-enabled-false-front-operations/ | 2026-11-11T00:15:36.632Z | Disrupting AI-enabled “false front” operations | [md](../../pages/openai.com/index/disrupting-ai-enabled-false-front-operations/index.md) |
| /index/empowering-cyber-defenders/ | 2026-11-10T08:38:08.271Z | Democratic governance of frontier AI, part II: Empowering cyber defenders | [md](../../pages/openai.com/index/empowering-cyber-defenders/index.md) |
| /index/eu-text-provenance/ | 2026-11-08T12:38:56.139Z | Our approach to EU text provenance rules | [md](../../pages/openai.com/index/eu-text-provenance/index.md) |
| /index/fair-use-benefits-everyone/ | 2026-11-12T23:54:45.084Z | Fair use benefits everyone | [md](../../pages/openai.com/index/fair-use-benefits-everyone/index.md) |
| /index/fanatics-streamline-fan-experience/ | 2026-11-12T23:54:43.746Z | How Fanatics and OpenAI streamline the fan experience | [md](../../pages/openai.com/index/fanatics-streamline-fan-experience/index.md) |
| /index/forward-deployed-engineering-means/ | 2026-11-12T23:54:41.318Z | What FDE means at OpenAI | [md](../../pages/openai.com/index/forward-deployed-engineering-means/index.md) |
| /index/franklin-templeton/ | 2026-11-10T01:44:06.607Z | Franklin Templeton uses OpenAI to support investment research | [md](../../pages/openai.com/index/franklin-templeton/index.md) |
| /index/gilbert-tobin-sam-nickless/ | 2026-11-12T18:49:09.905Z | Gilbert + Tobin rethinks the business of law with AI | [md](../../pages/openai.com/index/gilbert-tobin-sam-nickless/index.md) |
| /index/gpt-6-1-sol-coderabbit-code-security/ | 2026-11-12T23:54:58.162Z | GPT‑6.1 Sol helps CodeRabbit strengthen security across complex codebases | [md](../../pages/openai.com/index/gpt-6-1-sol-coderabbit-code-security/index.md) |
| /index/gpt-6-for-everyone/ | 2026-11-12T23:54:33.480Z | GPT‑6 and Intelligent UI for everyone | [md](../../pages/openai.com/index/gpt-6-for-everyone/index.md) |
| /index/greptile-code-review-codex-astra/ | 2026-11-09T22:53:51.137Z | Greptile takes bug detection beyond code review with GPT‑6 Astra | [md](../../pages/openai.com/index/greptile-code-review-codex-astra/index.md) |
| /index/grid-protectors-program/ | 2026-11-12T23:55:06.300Z | Introducing the Grid Protectors Program | [md](../../pages/openai.com/index/grid-protectors-program/index.md) |
| /index/grupo-boticario/ | 2026-11-09T22:46:33.955Z | How Grupo Boticário uses AI to strengthen human connections | [md](../../pages/openai.com/index/grupo-boticario/index.md) |
| /index/heimstaden/ | 2026-11-09T22:47:17.012Z | Heimstaden is changing residential real estate management with AI | [md](../../pages/openai.com/index/heimstaden/index.md) |
| /index/helping-caregivers-use-ai-in-everyday-life/ | 2026-11-12T23:54:30.143Z | Helping caregivers use AI in everyday life | [md](../../pages/openai.com/index/helping-caregivers-use-ai-in-everyday-life/index.md) |
| /index/helping-small-businesses-put-ai-to-work/ | 2026-11-12T23:54:44.622Z | Helping small businesses put AI to work | [md](../../pages/openai.com/index/helping-small-businesses-put-ai-to-work/index.md) |
| /index/helping-websites-express-ai-training-preferences/ | 2026-11-12T23:54:37.233Z | Making it easier for websites to express AI training preferences | [md](../../pages/openai.com/index/helping-websites-express-ai-training-preferences/index.md) |
| /index/higgsfield-longer-videos-voice/ | 2026-11-08T12:34:11.547Z | Higgsfield takes AI video from 1 minute to over 10 | [md](../../pages/openai.com/index/higgsfield-longer-videos-voice/index.md) |
| /index/how-we-detect-frontier-model-misalignment/ | 2026-11-12T23:55:04.165Z | How we detect frontier model misalignment | [md](../../pages/openai.com/index/how-we-detect-frontier-model-misalignment/index.md) |
| /index/how-we-will-do-better-for-australia/ | 2026-11-12T23:54:46.876Z | How we will do better for Australia | [md](../../pages/openai.com/index/how-we-will-do-better-for-australia/index.md) |
| /index/introducing-businesses-chatgpt/ | 2026-11-12T23:54:30.936Z | Introducing Businesses in ChatGPT | [md](../../pages/openai.com/index/introducing-businesses-chatgpt/index.md) |
| /index/introducing-dots/ | 2026-11-12T23:54:39.207Z | Introducing dots | [md](../../pages/openai.com/index/introducing-dots/index.md) |
| /index/introducing-gpt-6-1-sol/ | — | GPT-6.1Sol | [md](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md) |
| /index/introducing-gpt-6-1-terra/ | — | GPT-6.1Terra | [md](../../pages/openai.com/index/introducing-gpt-6-1-terra/index.md) |
| /index/introducing-gpt-6-cyber/ | 2026-11-11T02:03:47.315Z | GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents | [md](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md) |
| /index/introducing-images-2-6/ | 2026-11-12T23:54:37.408Z | Introducing Images 2.6Introducing Images 2.6 | [md](../../pages/openai.com/index/introducing-images-2-6/index.md) |
| /index/introducing-the-rosalind-academic-plan/ | 2026-11-05T10:12:43.505Z | Bringing GPT‑Rosalind to academic research labs | [md](../../pages/openai.com/index/introducing-the-rosalind-academic-plan/index.md) |
| /index/itau-generative-ai/ | 2026-11-10T21:28:39.257Z | How Itaú is building generative AI for its entire customer base | [md](../../pages/openai.com/index/itau-generative-ai/index.md) |
| /index/jill-hazelbaker-chief-corporate-affairs-officer/ | 2026-11-12T23:54:58.959Z | OpenAI appoints Jill Hazelbaker as Chief Corporate Affairs Officer | [md](../../pages/openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer/index.md) |
| /index/jiostar-vijay-seshadri/ | 2026-11-13T01:29:25.632Z | JioStar’s chief architect on AI discovery at 500M-user scale | [md](../../pages/openai.com/index/jiostar-vijay-seshadri/index.md) |
| /index/jump-trading/ | 2026-11-09T22:50:29.536Z | How Jump Trading is scaling quant research with ChatGPT | [md](../../pages/openai.com/index/jump-trading/index.md) |
| /index/kuken/ | 2026-11-10T21:25:37.251Z | Kuken Industries searches 70 years of drawings in minutes | [md](../../pages/openai.com/index/kuken/index.md) |
| /index/legalon-halves-codex-costs/ | 2026-11-08T12:34:14.835Z | LegalOn halves Codex costs while maintaining development speed | [md](../../pages/openai.com/index/legalon-halves-codex-costs/index.md) |
| /index/legora/ | 2026-11-09T22:46:16.117Z | Legora is building the agentic operating system for legal work | [md](../../pages/openai.com/index/legora/index.md) |
| /index/lenfest-ai-collaborative-expansion/ | 2026-11-12T23:54:49.044Z | The Lenfest Institute grows landmark program with expanded OpenAI support | [md](../../pages/openai.com/index/lenfest-ai-collaborative-expansion/index.md) |
| /index/lifeval/ | 2026-11-12T23:54:30.732Z | LifeVal | [md](../../pages/openai.com/index/lifeval/index.md) |
| /index/localiza-generative-ai/ | 2026-11-09T22:48:14.035Z | How Localiza reorganized work around generative AI | [md](../../pages/openai.com/index/localiza-generative-ai/index.md) |
| /index/low-resource-programming-languages/ | 2026-11-08T12:36:25.252Z |  | [md](../../pages/openai.com/index/low-resource-programming-languages/index.md) |
| /index/measuring-how-ai-agents-handle-wet-lab-science/ | 2026-11-12T23:54:32.359Z | Measuring how AI agents handle everyday wet-lab science | [md](../../pages/openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/index.md) |
| /index/merge-builds-with-openai/ | 2026-11-11T19:14:31.918Z | Merge builds product and business tools with OpenAI technology | [md](../../pages/openai.com/index/merge-builds-with-openai/index.md) |
| /index/new-chatgpt-ads-format-and-measurement/ | 2026-11-05T10:13:59.414Z | Building advertising for the way people use AI | [md](../../pages/openai.com/index/new-chatgpt-ads-format-and-measurement/index.md) |
| /index/openai-cut-incident-investigation/ | 2026-11-12T23:54:44.131Z | How Ultrafast cut incident investigation from hours to minutes at OpenAI | [md](../../pages/openai.com/index/openai-cut-incident-investigation/index.md) |
| /index/openai-models-google-cloud/ | 2026-11-10T09:52:31.112Z | OpenAI models are coming to Google Cloud | [md](../../pages/openai.com/index/openai-models-google-cloud/index.md) |
| /index/openai-nask-ai-safety-security-partnership/ | 2026-11-10T21:22:01.914Z | OpenAI and Poland’s NASK partner to advance AI safety and security | [md](../../pages/openai.com/index/openai-nask-ai-safety-security-partnership/index.md) |
| /index/openai-servicenow-partnership-expansion/ | 2026-11-12T23:54:40.785Z | OpenAI and ServiceNow expand partnership across enterprise workflows | [md](../../pages/openai.com/index/openai-servicenow-partnership-expansion/index.md) |
| /index/openai-to-acquire-orchestra-bio/ | 2026-11-10T09:52:32.274Z | OpenAI acquires Orchestra Bio | [md](../../pages/openai.com/index/openai-to-acquire-orchestra-bio/index.md) |
| /index/openai-to-acquire-pierre/ | 2026-11-12T23:54:38.566Z | OpenAI to acquire Pierre Computer Company, Inc. | [md](../../pages/openai.com/index/openai-to-acquire-pierre/index.md) |
| /index/oracle-apps-in-chatgpt/ | 2026-11-12T23:54:54.328Z | OpenAI expands partnership with Oracle to bring its apps to ChatGPT | [md](../../pages/openai.com/index/oracle-apps-in-chatgpt/index.md) |
| /index/oracle/ | 2026-11-09T22:46:53.679Z | How Oracle turns days of work into minutes with ChatGPT and Codex | [md](../../pages/openai.com/index/oracle/index.md) |
| /index/partnering-with-hacktron/ | 2026-11-12T23:54:33.529Z | Partnering with Hacktron to find vulnerabilities in OpenAI’s systems | [md](../../pages/openai.com/index/partnering-with-hacktron/index.md) |
| /index/pollo-ai/ | 2026-11-03T21:40:31.085Z | Pollo AI turns creative ideas into campaigns with OpenAI | [md](../../pages/openai.com/index/pollo-ai/index.md) |
| /index/practical-guide-building-gpt-6/ | 2026-11-05T10:12:32.907Z | A model guide for the GPT‑6 family | [md](../../pages/openai.com/index/practical-guide-building-gpt-6/index.md) |
| /index/preparing-our-next-security-sprint-to-harden-openai/ | 2026-11-12T23:54:32.892Z | Preparing our next security sprint to harden OpenAI | [md](../../pages/openai.com/index/preparing-our-next-security-sprint-to-harden-openai/index.md) |
| /index/qodo-codex-plugin/ | 2026-11-09T22:47:29.408Z | Qodo builds context into AI code review with Codex | [md](../../pages/openai.com/index/qodo-codex-plugin/index.md) |
| /index/radisson/ | 2026-11-09T22:46:55.033Z | Radisson Hotel Group brings hotel discovery into ChatGPT | [md](../../pages/openai.com/index/radisson/index.md) |
| /index/rewarding-defenders-with-bigger-bug-bounties/ | 2026-11-12T23:54:39.813Z | Rewarding defenders with bigger bug bounties | [md](../../pages/openai.com/index/rewarding-defenders-with-bigger-bug-bounties/index.md) |
| /index/ropes-gray-ai-diligence/ | 2026-11-09T22:46:36.255Z | How Ropes & Gray is developing AI for transactional diligence | [md](../../pages/openai.com/index/ropes-gray-ai-diligence/index.md) |
| /index/scaling-ai-research-for-complex-biological-data/ | 2026-11-12T22:13:46.797Z | Using thousands of AI agents to uncover new leads in biological data | [md](../../pages/openai.com/index/scaling-ai-research-for-complex-biological-data/index.md) |
| /index/scaling-git-at-openai/ | 2026-11-12T23:54:40.456Z | Scaling Git at OpenAI | [md](../../pages/openai.com/index/scaling-git-at-openai/index.md) |
| /index/scaling-storage-one-billion-users-part-two/ | 2026-11-12T23:54:40.414Z | Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II) | [md](../../pages/openai.com/index/scaling-storage-one-billion-users-part-two/index.md) |
| /index/securing-our-frontier-model-training-environment/ | 2026-11-12T23:54:37.915Z | Securing our frontier model training environment | [md](../../pages/openai.com/index/securing-our-frontier-model-training-environment/index.md) |
| /index/sentinelone/ | 2026-11-09T23:02:35.239Z | SentinelOne cuts malware analysis from weeks to hours | [md](../../pages/openai.com/index/sentinelone/index.md) |
| /index/setting-new-standard-responsible-ai-infrastructure/ | 2026-11-12T23:54:35.987Z | Setting a new standard for responsible AI infrastructure | [md](../../pages/openai.com/index/setting-new-standard-responsible-ai-infrastructure/index.md) |
| /index/sharing-ai-progress-in-mathematics/ | 2026-11-08T12:36:54.139Z | Sharing AI progress in mathematics | [md](../../pages/openai.com/index/sharing-ai-progress-in-mathematics/index.md) |
| /index/singapore-airlines-travel-work/ | 2026-11-12T23:54:29.153Z | Singapore Airlines elevates travel & work with OpenAI technology | [md](../../pages/openai.com/index/singapore-airlines-travel-work/index.md) |
| /index/sophos/ | 2026-11-09T22:49:38.271Z | Sophos cuts threat investigation time by 96% with OpenAI Daybreak | [md](../../pages/openai.com/index/sophos/index.md) |
| /index/stack-overflow-chatgpt-plugin/ | 2026-11-08T12:34:36.990Z | Stack Overflow for Agents triples signups with ChatGPT plugin | [md](../../pages/openai.com/index/stack-overflow-chatgpt-plugin/index.md) |
| /index/sullivan-cromwell/ | 2026-11-09T22:46:39.730Z | Sullivan & Cromwell brings legal expertise into agreement review | [md](../../pages/openai.com/index/sullivan-cromwell/index.md) |
| /index/teaching-students-to-think-and-learn-through-questions/ | 2026-10-22T09:45:56.774Z | Teaching students to think and learn through questions | [md](../../pages/openai.com/index/teaching-students-to-think-and-learn-through-questions/index.md) |
| /index/ted-taylor-restaurant/ | 2026-11-09T23:08:21.924Z | Franchisee reconciles cash in 94% less time with ChatGPT Work | [md](../../pages/openai.com/index/ted-taylor-restaurant/index.md) |
| /index/teens-learn-and-plan/ | 2026-11-12T23:55:00.251Z | Helping teens learn, plan, and shape the future of AI | [md](../../pages/openai.com/index/teens-learn-and-plan/index.md) |
| /index/terminal-x/ | 2026-11-09T22:47:40.074Z | Terminal X matches senior investor judgment 88.6% with GPT‑6.1 | [md](../../pages/openai.com/index/terminal-x/index.md) |
| /index/the-den-family-social/ | 2026-11-09T22:46:14.666Z | The Den frees up 10-15 hours a week to grow with ChatGPT Work | [md](../../pages/openai.com/index/the-den-family-social/index.md) |
| /index/the-eternal-complement/ | 2026-11-12T23:55:04.759Z | The eternal complement | [md](../../pages/openai.com/index/the-eternal-complement/index.md) |
| /index/the-eus-next-chapter-in-ai-is-agentic/ | 2026-11-10T08:37:51.241Z | The EU’s next chapter in AI is agentic | [md](../../pages/openai.com/index/the-eus-next-chapter-in-ai-is-agentic/index.md) |
| /index/the-future-of-the-firm/ | 2026-11-12T23:54:38.724Z | The future of the firm | [md](../../pages/openai.com/index/the-future-of-the-firm/index.md) |
| /index/third-moment-research/ | 2026-11-08T12:34:39.599Z | How Third Moment Research runs 10,000 agents for 36+ hours | [md](../../pages/openai.com/index/third-moment-research/index.md) |
| /index/towards-safety-cases-for-frontier-ai-training/ | 2026-11-03T18:06:47.269Z | Towards safety cases for frontier AI training | [md](../../pages/openai.com/index/towards-safety-cases-for-frontier-ai-training/index.md) |
| /index/uber-chatgpt-work-rollout/ | 2026-11-12T23:55:02.417Z | Uber brings ChatGPT Work to all employees with OpenAI | [md](../../pages/openai.com/index/uber-chatgpt-work-rollout/index.md) |
| /index/updated-model-spec/ | 2026-11-08T12:38:20.863Z | An updated Model Spec for more capable and beneficial AI | [md](../../pages/openai.com/index/updated-model-spec/index.md) |
| /policies/brazil-advertising-terms/ | 2026-10-26T07:27:13.757Z | Brazil Advertising Terms | [md](../../pages/openai.com/policies/brazil-advertising-terms/index.md) |
| /policies/business-agents-policy/ | 2026-11-10T18:01:22.818Z | Business Agents Policy | [md](../../pages/openai.com/policies/business-agents-policy/index.md) |
| /policies/businesses-in-chatgpt-terms/ | 2026-11-12T16:03:50.769Z | Businesses in ChatGPT Terms | [md](../../pages/openai.com/policies/businesses-in-chatgpt-terms/index.md) |
| /policies/businesses-in-chatgpt/ | 2026-11-11T21:54:33.152Z | Businesses in ChatGPT | [md](../../pages/openai.com/policies/businesses-in-chatgpt/index.md) |
| /policies/chatgpt-wallet-privacy-notice/ | 2026-11-13T05:02:37.728Z | ChatGPT Wallet Privacy Notice | [md](../../pages/openai.com/policies/chatgpt-wallet-privacy-notice/index.md) |
| /policies/chatgpt-wallet-terms/ | 2026-11-13T05:03:40.208Z | ChatGPT Wallet terms | [md](../../pages/openai.com/policies/chatgpt-wallet-terms/index.md) |
| /policies/marketplace-customer-program-terms/ | 2026-11-12T14:35:29.636Z | OpenAI Marketplace Customer Program Terms | [md](../../pages/openai.com/policies/marketplace-customer-program-terms/index.md) |
| /policies/row-privacy-policy/ | 2026-11-03T12:13:38.478Z | Privacy policy | [md](../../pages/openai.com/policies/row-privacy-policy/index.md) |
| /policies/sign-in-with-chatgpt-terms/ | 2026-11-09T20:29:22.098Z | Sign in with ChatGPT Terms | [md](../../pages/openai.com/policies/sign-in-with-chatgpt-terms/index.md) |
| /proud-partner/ | 2026-11-12T19:39:15.688Z | Proud Partner of people with big ideas | [md](../../pages/openai.com/proud-partner/index.md) |
| /supply/product/blossom-tee-gray/ | — | Blossom Tee | [md](../../pages/openai.com/supply/product/blossom-tee-gray/index.md) |
| /supply/product/dots-tee/ | — | Dots Tee | [md](../../pages/openai.com/supply/product/dots-tee/index.md) |
| /supply/product/dots-tote/ | — | Dots Tote | [md](../../pages/openai.com/supply/product/dots-tote/index.md) |
| /supply/product/gpt-6-longsleeve/ | — | GPT-6 Longsleeve | [md](../../pages/openai.com/supply/product/gpt-6-longsleeve/index.md) |
| /supply/product/modretro-chromatic-case-codex-edition/ | — | ModRetro Chromatic Case: Codex Edition | [md](../../pages/openai.com/supply/product/modretro-chromatic-case-codex-edition/index.md) |
| /supply/product/modretro-codex-cartridge/ | — | ModRetro Codex Cartridge | [md](../../pages/openai.com/supply/product/modretro-codex-cartridge/index.md) |
| /supply/product/theresetcompany-hoodie/ | — | TheResetCompany Hoodie | [md](../../pages/openai.com/supply/product/theresetcompany-hoodie/index.md) |

## Appendix C — updated URLs with residual (non-template) changes, by size

- /policies/supplier-code/ — ~36484 chars changed
- /collective-cyberdefense/ — ~19395 chars changed
- /policies/advertising-terms/ — ~18211 chars changed
- /index/wayfair/ — ~17708 chars changed
- /index/lowes/ — ~16148 chars changed
- /index/retell-ai/ — ~13631 chars changed
- /policies/usage-policies/ — ~10182 chars changed
- /policies/privacy-policy/ — ~8484 chars changed
- /business/solutions/cybersecurity/ — ~8409 chars changed
- /business/plugins/bigdata-com/ — ~7484 chars changed
- /global-affairs/response-to-nist-executive-order-on-ai/ — ~7283 chars changed
- /products/release-notes/ — ~7124 chars changed
- /events/aws-reinvent/ — ~7094 chars changed
- /daybreak/ — ~7031 chars changed
- /business/solutions/data/ — ~6751 chars changed
- /policies/service-terms/ — ~6625 chars changed
- /business/plugins/windsor-ai/ — ~6468 chars changed
- /business/plugins/supermetrics/ — ~6087 chars changed
- /business/plugins/heygen/ — ~6015 chars changed
- /policies/merchant-feed-terms-of-service/ — ~5469 chars changed
- /signals/data/ — ~4126 chars changed
- /webmcp-challenge/ — ~4099 chars changed
- /index/election-safeguards-2026/ — ~4011 chars changed
- /business/plugins/creative-claw/ — ~4000 chars changed
- /form/trademark-counterfeit-disputes/ — ~3985 chars changed
- /policies/developer-apps-terms/ — ~3887 chars changed
- /business/plugins/hypd-ai/ — ~3741 chars changed
- /business/plugins/adspirer/ — ~3590 chars changed
- /business/why-openai/small-business/ — ~3513 chars changed
- /business/plugins/gsc-wizard/ — ~3411 chars changed
- /business/plugins/higgsfield/ — ~3411 chars changed
- /business/plugins/tldv/ — ~3307 chars changed
- /business/plugins/everlaw/ — ~3303 chars changed
- /business/pricing/ — ~2914 chars changed
- /index/small-business-stories/ — ~2874 chars changed
- /codex/ — ~2657 chars changed
- /business/plugins/explain-video-generator/ — ~2470 chars changed
- /business/plugins/magnific/ — ~2454 chars changed
- /business/plugins/sync-labs/ — ~2426 chars changed
- /business/plugins/notion/ — ~2381 chars changed
- /business/plugins/happyscribe/ — ~2377 chars changed
- /business/plugins/vidiq/ — ~2355 chars changed
- /business/plugins/kling-ai/ — ~2335 chars changed
- /index/introducing-genebench-pro/ — ~2304 chars changed
- /business/ — ~2211 chars changed
- /business/plugins/coupler-io/ — ~2131 chars changed
- /form/copyright-disputes/ — ~2051 chars changed
- /business/plugins/data/ — ~2035 chars changed
- /policies/ad-tools-terms/ — ~2022 chars changed
- /business/plugins/windsor-ai-google-ads/ — ~2006 chars changed
- /business/why-openai/startups/ — ~2002 chars changed
- /business/plugins/openart/ — ~1970 chars changed
- /business/plugins/windsor-ai-facebook-ads/ — ~1924 chars changed
- /policies/commerce-policies/ — ~1897 chars changed
- /business/plugins/sider-scholar/ — ~1831 chars changed
- /business/plugins/fathom/ — ~1780 chars changed
- /business/plugins/google-drive/ — ~1727 chars changed
- /business/plugins/consensus/ — ~1709 chars changed
- /business/plugins/highlevel/ — ~1701 chars changed
- /index/introducing-chatgpt-financial-services/ — ~1689 chars changed
- /business/plugins/rocketreach/ — ~1677 chars changed
- /business/plugins/ironclad-contracts/ — ~1670 chars changed
- /policies/service-credit-terms/ — ~1639 chars changed
- /business/plugins/scholar-gateway/ — ~1626 chars changed
- /business/plugins/sales/ — ~1616 chars changed
- /business/plugins/hostinger-connector/ — ~1614 chars changed
- /policies/cookie-policy/ — ~1614 chars changed
- /business/solutions/operations/ — ~1595 chars changed
- /index/advancing-content-provenance/ — ~1583 chars changed
- /index/gpt-4o-system-card/ — ~1544 chars changed
- /business/plugins/ringcentral-phone/ — ~1540 chars changed
- /business/plugins/remote-desktop-commander/ — ~1523 chars changed
- /chatgpt-work/ — ~1496 chars changed
- /business/plugins/brevo/ — ~1481 chars changed
- /business/plugins/mercury/ — ~1438 chars changed
- /business/plugins/upwork/ — ~1396 chars changed
- /policies/sub-processor-list/ — ~1359 chars changed
- /index/openai-frontier-models-and-codex-are-now-available-on-aws/ — ~1341 chars changed
- /solutions/industries/government/ — ~1336 chars changed
- /business/plugins/ubersuggest/ — ~1270 chars changed
- /business/plugins/parallel-search/ — ~1263 chars changed
- /business/plugins/tally/ — ~1236 chars changed
- /business/plugins/invideo/ — ~1228 chars changed
- /business/plugins/hugging-face/ — ~1207 chars changed
- /signals/data-download/ — ~1174 chars changed
- /business/partners/sk-inc-ax/ — ~1154 chars changed
- /index/defining-and-evaluating-political-bias-in-llms/ — ~1151 chars changed
- /index/personal-finance-chatgpt/ — ~1129 chars changed
- /business/plugins/midpage/ — ~1124 chars changed
- /business/plugins/mobbin/ — ~1114 chars changed
- /business/plugins/openai-developers/ — ~1112 chars changed
- /business/plugins/apollo/ — ~1093 chars changed
- /business/plugins/quo/ — ~1047 chars changed
- /index/supporting-journalism-from-classrooms-to-newsrooms/ — ~1042 chars changed
- /business/plugins/adobe/ — ~1032 chars changed
- /business/plugins/semrush/ — ~1005 chars changed
- /index/gpt-6-astra/ — ~993 chars changed
- /index/previewing-ultrafast/ — ~984 chars changed
- /business/plugins/firecrawl/ — ~958 chars changed
- /new-york-times/ — ~949 chars changed
- /index/chip-ganassi-racing/ — ~947 chars changed
- /business/plugins/codex-security/ — ~938 chars changed
- /business/plugins/pitchbook/ — ~923 chars changed
- /business/plugins/ramp/ — ~904 chars changed
- /api/ — ~891 chars changed
- /index/paul-christiano-joins-openai-foundation-board/ — ~850 chars changed
- /business/plugins/tinyfish/ — ~848 chars changed
- /business/plugins/netlify/ — ~838 chars changed
- /policies/ — ~836 chars changed
- /business/plugins/relativity/ — ~820 chars changed
- /index/our-approach-to-ai-safety/ — ~818 chars changed
- /business/plugins/neon/ — ~815 chars changed
- /index/openai-to-acquire-ona/ — ~810 chars changed
- /business/solutions/marketing/ — ~796 chars changed
- /company/public-policy/ — ~792 chars changed
- /business/plugins/replit/ — ~776 chars changed
- /business/plugins/public-equity-investing/ — ~771 chars changed
- /business/plugins/descript/ — ~769 chars changed
- /business/plugins/undermind/ — ~764 chars changed
- /business/plugins/conductor/ — ~758 chars changed
- /business/plugins/parqet/ — ~755 chars changed
- /business/plugins/klaviyo/ — ~744 chars changed
- /index/how-agents-are-transforming-work/ — ~744 chars changed
- /index/airbnb-gpt-6-astra/ — ~743 chars changed
- /business/plugins/picsart/ — ~742 chars changed
- /index/gpt-5-6-in-kiro/ — ~742 chars changed
- /index/astra-for-law/ — ~732 chars changed
- /index/red-teaming-network/ — ~719 chars changed
- /business/partners/ — ~705 chars changed
- /business/plugins/lseg/ — ~692 chars changed
- /business/plugins/text/ — ~684 chars changed
- /index/reimagining-advertising-with-ai/ — ~682 chars changed
- /business/plugins/fal/ — ~675 chars changed
- /business/plugins/fireflies/ — ~668 chars changed
- /business/plugins/morningstar/ — ~667 chars changed
- /business/plugins/jam-dev/ — ~633 chars changed
- /business/plugins/onenote/ — ~632 chars changed
- /business/plugins/lovable/ — ~627 chars changed
- /signals/research/ — ~616 chars changed
- /global-affairs/testimony-of-sam-altman-before-the-us-senate/ — ~606 chars changed
- /business/plugins/spaceship/ — ~603 chars changed
- /daybreak/codex-security-plugin/ — ~594 chars changed
- /index/builders-guide-to-gpt-5-6/ — ~582 chars changed
- /transparency-and-content-moderation/ — ~579 chars changed
- /index/what-students-gain-from-chatgpt-critical-thinking-training/ — ~576 chars changed
- /index/learning-to-reason-with-llms/ — ~563 chars changed
- /policies/sharing-publication-policy/ — ~556 chars changed
- /index/how-enterprises-put-ai-to-work/ — ~542 chars changed
- /business/plugins/daloopa/ — ~517 chars changed
- /business/plugins/hostinger/ — ~516 chars changed
- /api-fast-mode/ — ~508 chars changed
- /business/plugins/render/ — ~504 chars changed
- /index/how-people-are-using-chatgpt/ — ~498 chars changed
- /business/plugins/adobe-express/ — ~497 chars changed
- /index/combating-online-child-sexual-exploitation-abuse/ — ~487 chars changed
- /contact-sales/ — ~475 chars changed
- /business/plugins/investment-banking/ — ~465 chars changed
- /business/plugins/microsoft-dataverse/ — ~459 chars changed
- /research/verify/ — ~459 chars changed
- /trust-and-transparency/ — ~456 chars changed
- /business/plugins/tavily-ai/ — ~455 chars changed
- /business/plugins/tableau/ — ~449 chars changed
- /science/ — ~444 chars changed
- /business/plugins/clio/ — ~436 chars changed
- /policies/openai-cve-assignment-policy/ — ~421 chars changed
- /index/scaling-social-science-research/ — ~411 chars changed
- /business/plugins/salesforce/ — ~405 chars changed
- /business/plugins/sentinelx/ — ~404 chars changed
- /index/thinking-with-images/ — ~402 chars changed
- /index/how-countries-can-end-the-capability-overhang/ — ~381 chars changed
- /index/powering-product-discovery-in-chatgpt/ — ~367 chars changed
- /business/learn/ — ~354 chars changed
- /business/plugins/firebase/ — ~354 chars changed
- /index/modeling-ai-jobs-transition/ — ~349 chars changed
- /index/ai-first-hire-small-business/ — ~343 chars changed
- /business/plugins/openai-certified/ — ~332 chars changed
- /index/the-state-of-enterprise-ai-2025-report/ — ~327 chars changed
- /index/how-ai-is-expanding-what-people-do-at-work/ — ~326 chars changed
- /index/putting-frontier-cyber-models-in-more-trusted-hands/ — ~319 chars changed
- /index/introducing-o3-and-o4-mini/ — ~318 chars changed
- /index/1-million-businesses-putting-ai-to-work/ — ~314 chars changed
- /index/mapping-ai-jobs-transition-eu/ — ~307 chars changed
- /business/plugins/microsoft-azure-cosmosdb/ — ~304 chars changed
- /index/introducing-chatgpt-small-business-program/ — ~289 chars changed
- /index/introducing-openai-o1-preview/ — ~287 chars changed
- /solutions/ — ~287 chars changed
- /o1/ — ~284 chars changed
- /index/outtake/ — ~280 chars changed
- /business/plugins/monday-com/ — ~279 chars changed
- /business/plugins/stripe/ — ~277 chars changed
- /signals/ — ~276 chars changed
- /business/plugins/creative-production/ — ~273 chars changed
- /business/plugins/hex/ — ~263 chars changed
- /index/k-12-educators-practical-skills/ — ~260 chars changed
- /business/plugins/clay/ — ~256 chars changed
- /business/plugins/villagesql/ — ~256 chars changed
- /business/plugins/canva/ — ~254 chars changed
- /index/update-on-safety-and-security-practices/ — ~254 chars changed
- /business/plugins/zoom/ — ~249 chars changed
- /signals/research/2026q1-update/ — ~247 chars changed
- /index/chatgpt-for-your-most-ambitious-work/ — ~246 chars changed
- /news/ai-adoption/ — ~244 chars changed
- /index/how-chatgpt-adoption-has-expanded/ — ~243 chars changed
- /index/openai-raising-concerns-policy/ — ~243 chars changed
- /business/plugins/vercel/ — ~233 chars changed
- /business/plugins/mongodb/ — ~228 chars changed
- /live/ — ~228 chars changed
- /index/how-should-ai-systems-behave/ — ~226 chars changed
- /business/plugins/omni/ — ~220 chars changed
- /research/index/publication/ — ~217 chars changed
- /index/cna-walter-fernandez/ — ~211 chars changed
- /index/genebench-pro/case-studies/ — ~209 chars changed
- /index/openai-o1-mini-advancing-cost-efficient-reasoning/ — ~209 chars changed
- /business/solutions/education/ — ~207 chars changed
- /business/solutions/engineering/ — ~207 chars changed
- /business/plugins/redis/ — ~204 chars changed
- /business/plugins/coveo/ — ~203 chars changed
- /index/reinforcement-learning-with-prediction-based-rewards/ — ~203 chars changed
- /index/openai-o3-mini/ — ~202 chars changed
- /global-affairs/introducing-chatgpt-gov/ — ~195 chars changed
- /index/hebbia/ — ~195 chars changed
- /research/index/ — ~193 chars changed
- /index/coderabbit/ — ~190 chars changed
- /index/rogo/ — ~188 chars changed
- / — ~186 chars changed
- /business/plugins/g2/ — ~180 chars changed
- /business/plugins/dbt/ — ~172 chars changed
- /business/plugins/shopify/ — ~169 chars changed
- /business/plugins/wix/ — ~166 chars changed
- /global-affairs/introducing-openai-for-government/ — ~166 chars changed
- /academy/brainstorming/ — ~160 chars changed
- /academy/writing/ — ~160 chars changed
- /hugging-face-incident-and-misalignment/ — ~159 chars changed
- /business/plugins/box/ — ~153 chars changed
- /solutions/industries/law/ — ~152 chars changed
- /index/apple-is-getting-this-wrong/ — ~151 chars changed
- /index/our-decision-on-cursor-following-its-acquisition-by-spacex/ — ~150 chars changed
- /index/introducing-prism/ — ~147 chars changed
- /index/our-approach-to-alignment-research/ — ~145 chars changed
- /academy/what-is-ai/ — ~140 chars changed
- /business/plugins/aha/ — ~139 chars changed
- /policies/chatgpt-sites-terms/ — ~135 chars changed
- /business/plugins/zoho-crm/ — ~133 chars changed
- /business/partners/chieftns/ — ~131 chars changed
- /business/solutions/finance/ — ~130 chars changed
- /index/evolution-strategies/ — ~128 chars changed
- /business/plugins/gusto/ — ~123 chars changed
- /business/plugins/bigquery/ — ~121 chars changed
- /business/plugins/figma/ — ~121 chars changed
- /index/lenfest-institute/ — ~121 chars changed
- /business/plugins/databricks/ — ~119 chars changed
- /business/why-openai/enterprises/ — ~118 chars changed
- /business/plugins/ — ~114 chars changed
- /business/solutions/design/ — ~111 chars changed
- /business/plugins/product-design/ — ~109 chars changed
- /research/index/release/ — ~106 chars changed
- /index/openai-o1-system-card/ — ~104 chars changed
- /index/better-language-models/ — ~103 chars changed
- /business/plugins/grain/ — ~101 chars changed
- /business/plugins/snowflake/ — ~101 chars changed
- /index/introducing-gpt-6-sol-and-luna/ — ~101 chars changed
- /business/plugins/dropbox/ — ~97 chars changed
- /business/plugins/cloudinary/ — ~95 chars changed
- /business/plugins/clickup/ — ~93 chars changed
- /business/plugins/github/ — ~93 chars changed
- /business/plugins/microsoft-sharepoint/ — ~93 chars changed
- /business/plugins/asana/ — ~91 chars changed
- /index/unrolling-the-codex-agent-loop/ — ~90 chars changed
- /business/plugins/hubspot/ — ~87 chars changed
- /business/plugins/egnyte/ — ~86 chars changed
- /index/robust-adversarial-inputs/ — ~85 chars changed
- /index/language-unsupervised/ — ~84 chars changed
- /business/plugins/gmail/ — ~83 chars changed
- /business/plugins/microsoft-outlook-email/ — ~79 chars changed
- /business/plugins/linear/ — ~77 chars changed
- /daybreak/partners/ — ~77 chars changed
- /index/genmab/ — ~77 chars changed
- /index/moving-ai-governance-forward/ — ~75 chars changed
- /index/unsupervised-sentiment-neuron/ — ~75 chars changed
- /business/plugins/lusha/ — ~71 chars changed
- /business/plugins/amplitude/ — ~67 chars changed
- /business/plugins/digitalocean/ — ~67 chars changed
- /global-affairs/disrupting-malicious-uses-of-ai-june-2025/ — ~65 chars changed
- /business/plugins/google-calendar/ — ~63 chars changed
- /business/plugins/microsoft-outlook-calendar/ — ~63 chars changed
- /index/learning-to-cooperate-compete-and-communicate/ — ~62 chars changed
- /business/plugins/airtable/ — ~61 chars changed
- /business/plugins/adobe-acrobat/ — ~59 chars changed
- /business/plugins/chatgpt-ads-manager/ — ~58 chars changed
- /business/plugins/quickbooks/ — ~58 chars changed
- /index/data-partnerships/ — ~58 chars changed
- /business/customer-stories/ — ~56 chars changed
- /business/partners/altudo/ — ~56 chars changed
- /index/superalignment-fast-grants/ — ~55 chars changed
- /index/generalizing-from-simulation/ — ~54 chars changed
- /business/plugins/mailchimp/ — ~53 chars changed
- /business/plugins/microsoft-teams/ — ~53 chars changed
- /business/plugins/slack/ — ~53 chars changed
- /index/devday-2026/ — ~53 chars changed
- /index/endex/ — ~48 chars changed
- /index/robots-that-learn/ — ~47 chars changed
- /index/arco-education/ — ~45 chars changed
- /business/put-ai-to-work-automate-and-scale-financial-operations/ — ~44 chars changed
- /business/put-ai-to-work-for-marketing-teams/ — ~44 chars changed
- /business/put-ai-to-work-lessons-from-hundreds-of-successful-deployments/ — ~44 chars changed
- /business/solving-complex-problems-with-openai-o1-models/ — ~44 chars changed
- /index/put-ai-to-work-for-your-product-team/ — ~44 chars changed
- /business/partners/epam/ — ~39 chars changed
- /index/deep-research/ — ~39 chars changed
- /index/eliseai-minna-song/ — ~39 chars changed
- /business/plugins/trellis-law/ — ~37 chars changed
- /index/the-international-2018-results/ — ~37 chars changed
- /index/requests-for-research-2/ — ~32 chars changed
- /index/zalando/ — ~32 chars changed
- /business/partners/sb-oai-japan-gk/ — ~31 chars changed
- /index/planning-for-agi-and-beyond/ — ~31 chars changed
- /index/insights-from-global-conversations/ — ~30 chars changed
- /business/plugins/wrike/ — ~29 chars changed
- /index/gpt-2-1-5b-release/ — ~26 chars changed
- /business/partners/kpmg/ — ~25 chars changed
- /index/unlocking-new-ways-of-working/ — ~24 chars changed
- /index/learning-from-human-preferences/ — ~22 chars changed
- /index/ai-native-company-workflows/ — ~21 chars changed
- /index/codex-maxxing-long-running-work/ — ~21 chars changed
- /index/managing-ai-investments-in-agentic-era/ — ~21 chars changed
- /index/the-five-ai-value-models-driving-business-reinvention/ — ~21 chars changed
- /index/learning-to-model-other-minds/ — ~20 chars changed
- /global-affairs/disrupting-malicious-uses-of-ai-october-2025/ — ~19 chars changed
- /index/delivering-low-latency-voice-ai-at-scale/ — ~19 chars changed
- /index/fighting-nyt-user-privacy-invasion/ — ~19 chars changed
- /index/inside-our-in-house-data-agent/ — ~19 chars changed
- /index/response-to-nyt-data-demands/ — ~19 chars changed
- /form/report-content/ — ~18 chars changed
- /index/altera/ — ~17 chars changed
- /index/ly-corporation/ — ~17 chars changed
- /index/musenet/ — ~17 chars changed
- /index/yabble/ — ~17 chars changed
- /business/guides-and-resources/a-practical-guide-to-building-ai-agents/ — ~16 chars changed
- /business/guides-and-resources/a-practical-guide-to-building-with-ai/ — ~16 chars changed
- /business/guides-and-resources/chatgpt-business-smb-guide/ — ~16 chars changed
- /business/guides-and-resources/inside-gpt5-our-best-model-for-work/ — ~16 chars changed
- /index/codex-for-knowledge-work/ — ~15 chars changed
- /index/introducing-intelligence-age/ — ~15 chars changed
- /index/openai-joins-ports-pike-project/ — ~15 chars changed
- /index/introducing-deep-research/ — ~10 chars changed
- /business/learn/intelligence-at-work-financial-services/ — ~7 chars changed
- /form/daybreak-cyber-partner-program/ — ~7 chars changed
- /index/ai-as-the-greatest-source-of-empowerment-for-all/ — ~1 chars changed

_1371 further updated URLs changed only by template/nav/link-label/image/recirculation noise._

## Appendix D — removed URLs and live status

- /business/enabling-a-data-driven-workforce-webinar/ — HTTP 308 → /business/learn/enabling-a-data-driven-workforce-webinar/
- /business/fine-tuning-gpt-4o-webinar/ — HTTP 308 → /business/learn/fine-tuning-gpt-4o-webinar/
- /business/guides-and-resources/how-openai-uses-codex/ — HTTP 308 → /business/learn/how-openai-uses-codex/
- /business/guides-and-resources/identifying-and-scaling-ai-use-cases/ — HTTP 308 → /business/learn/identifying-and-scaling-ai-use-cases/
- /business/new-in-chatgpt-for-business-april-updates-2025/ — HTTP 308 → /business/learn/new-in-chatgpt-for-business-april-updates-2025/
- /business/new-in-chatgpt-for-work-march-updates-2025/ — HTTP 308 → /business/learn/new-in-chatgpt-for-work-march-updates-2025/
- /business/partners/canva/ — HTTP 404
- /business/partners/dropbox/ — HTTP 404
- /business/partners/gusto/ — HTTP 404
- /business/partners/hubspot/ — HTTP 404
- /business/partners/pathfindr/ — HTTP 308 → /business/partners/affinda/
- /business/partners/quickbooks/ — HTTP 404
- /business/partners/stripe/ — HTTP 404
- /business/plugins/atlassian-rovo/ — HTTP 404
- /business/plugins/litera-lito/ — HTTP 404
- /business/plugins/mcp-server-for-wordpress/ — HTTP 404
- /business/plugins/oracle-analytics/ — HTTP 404
- /business/plugins/wordpress-com/ — HTTP 308 → /business/plugins/wordpress/
- /daybreak/partners-new/ — HTTP 404
- /economic-research-exchange/ — HTTP 307 → /economic-research-collaborators/
- /form/ultrafast/ — HTTP 307 → https://developers.openai.com/api/docs/guides/ultrafast-mode
- /index/ada/ — HTTP 308 → /business/customer-stories/ada/
- /index/blue-j/ — HTTP 308 → /business/customer-stories/blue-j/
- /prism/ — HTTP 308 → /science/
- /residency/ — HTTP 307 → /research/
- /solutions/blueprints/knowledge-retrieval/ — HTTP 308 → /business/solutions/knowledge-retrieval/
- /solutions/industries/financial-services/ — HTTP 308 → /business/solutions/financial-services/
- /solutions/industries/retail/ — HTTP 308 → /business/solutions/retail/
- /solutions/use-case/content-creation/ — HTTP 308 → /business/solutions/content-creation/
- /solutions/use-case/data-analysis/ — HTTP 308 → /business/solutions/data-analysis/
