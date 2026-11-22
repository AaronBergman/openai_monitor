# Run 2026-11-22T09-15Z: analysis

- **Fetch time (sitemap):** 2026-11-22T09:16:19Z (root index + 45 sub-sitemaps)
- **Page fetches:** 2,082 (362 added + 1,720 updated) via `tools/html_to_md.py`, completed by about 09:45Z; **0 fetch failures**
- **Baseline:** 2026-09-28T09-17Z (**55 days earlier**: no runs in between)
- **Totals:** 2315 URLs (was 1985) · **362 added** · **1720 updated** (`<lastmod>` changed; about 597 with substantive content change) · **32 removed** (21 redirect, 11 404) · **77 anomaly records** · 45 sub-sitemaps (was 42)

## Anomalies (highest signal)

### 1. Observation gap: 55 days without a run
The previous successful run was **2026-09-28T09-17Z**. This run's fetch was **2026-11-22T09:16:19Z**. No snapshots exist in between. Everything below is a single 55-day diff, so:
- intermediate states can't be seen (a page added and then removed inside the window never shows up; several `<lastmod>` bumps on one URL collapse into one);
- for new URLs, `first_seen` = 2026-11-22T09-15Z is an upper bound, not the real first-appearance date. The publication date shown on each page is the better guide to when it actually launched.

### 2. 21 URLs "removed" that are really moves (HTTP redirects)
Of the 32 URLs that left the sitemap, 21 still resolve via redirect (checked at run time with `curl-cffi`). The meaningful ones:
- **`/safety/` → `/safety-alignment/`**: OpenAI's "Safety Approach" landing page is replaced by a new **Safety & Alignment** hub (see new pages). The "Safety Approach" footer link was also removed from all 1,717 pages that carry the global nav.
- **`/prism/` → `/science/`**: the Prism product page now redirects to the Science hub.
- **`/residency/` → `/research/`**: the OpenAI Residency program page is gone and redirects to the general Research page. That suggests the program has been retired or folded in.
- **`/economic-research-exchange/` → `/economic-research-collaborators/`**: renamed program.
- **`/business/partners/pathfindr/` → `/business/partners/affinda/`**: partner rebrand ("Affinda (formerly Pathfindr)").
- **`/business/plugins/wordpress-com/` → `/business/plugins/wordpress/`**.
- **`/index/ada/`, `/index/blue-j/` → `/business/customer-stories/…`**: customer stories moved out of the blog namespace.
- **`/solutions/...` (5 URLs) → `/business/solutions/...`**: the old `/solutions/` tree is being folded into `/business/solutions/`.
- **Webinars/guides (6 URLs) → `/business/learn/...`**: a new unified "Learn" library under `/business/learn/`.
- **`/form/data-partnerships/` → `/index/data-partnerships/`**; **`/form/ultrafast/` → developers.openai.com Ultrafast docs**: the Ultrafast waitlist form is closed because the product is now generally documented.

The other **11 removals return HTTP 404** (true deletions): partner pages for Canva, Dropbox, Gusto, HubSpot, QuickBooks, and Stripe; plugin pages for Atlassian Rovo, Litera Lito, MCP Server for WordPress, and Oracle Analytics (Oracle Analytics reappears as the new `/business/plugins/oracle-analytics-cloud/`, and Atlassian as `/business/plugins/atlassian/`); and `/daybreak/partners-new/`.

### 3. Three URLs disappeared earlier and have now come back
- `/business/plugins/alpaca/`: last seen 2026-09-24T09-16Z, back with `<lastmod>` 2026-11-18T20:23:19.714Z.
- `/form/codex-ambassadors/`: last seen 2026-06-24, back with `<lastmod>` 2026-11-05T11:53:06.545Z (the Codex Ambassadors application has reopened).
- `/policies/row-privacy-policy/`: last seen 2026-05-27T09-17Z, back with `<lastmod>` 2026-11-03T12:13:38.478Z (the "rest of world" privacy policy is listed again).

### 4. A `<lastmod>` was dropped
`/index/advancing-independent-research-ai-alignment/` had `<lastmod>` 2026-09-25T19:18:24.670Z on 2026-09-28. Its sitemap entry now has **no `<lastmod>`**. The page itself was re-rendered (21+/17− lines).

### 5. 91 of the 362 new URLs have no `<lastmod>` at all
These include the whole new `/safety-alignment/` tree (56 URLs), all 7 `/supply/` products, 6 `/ads/` pages, and three major model launches (`/index/introducing-gpt-6-1-sol/`, `/index/introducing-gpt-6-1-terra/`, `/index/introducing-gpt-6-2-astra-sol/`) plus `/index/research-acceleration-jagged-frontier/`. The full list is in `diff.json` → `notes.new_urls_without_lastmod`. Nothing is contradictory here, but for these URLs OpenAI makes no claim about when they changed.

### 6. Sub-sitemap migrations (51 URLs) and 3 new sub-sitemaps
New sub-sitemaps: **`/sitemap.xml/safety-and-alignment/`**, **`/sitemap.xml/science/`**, and **`/sitemap.xml/learn-demos/`** (42 → 45 total). Migrations mostly come from re-categorization: about 30 plugin pages were re-filed (largely *into* `plugins-sales-commerce`, which matches the ChatGPT for Sales launch), webinar and guide pages were added to `learn-webinars` and `learn-guides`, and some pages left `page` for `learn-*`.

### Checked and not found
- **Future-dated `<lastmod>`**: none (all 2,315 values are ≤ fetch time 2026-11-22T09:16:19Z).
- **Backwards-moving `<lastmod>`**: none among the 1,720 updated URLs.
- **Backdated new URLs**: none. No new URL's `<lastmod>` predates the prior observation (2026-09-28). A few new pages show *on-page* dates before their first sighting, but each one is a move (e.g. `/business/customer-stories/blue-j/`, dated Aug 21, 2025, moved from `/index/blue-j/`).

### Bulk re-save note
The `<lastmod>` values on updated URLs cluster heavily: **249 on 2026-11-17 and 162 on 2026-11-18**. That points to template-wide republishes (the global nav and footer changed on every page; see below), not 400 separate edits.

## Significant updates

**Site-wide template change (all 1,717 pages with the global nav/footer).** The model links in the nav now read **GPT‑6.2 / GPT‑6.1 Sol / GPT‑6 Astra** (GPT‑5.5 and GPT‑5.4 are gone). New footer links: **Dots**, **Plugins**, **Models** (developer docs), **OpenAI Status**, and Codex (now pointing at chatgpt.com/codex). Removed: **"Safety Approach" (`/safety/`)**, **"Open Models" (`/open-models/`)**, Apps SDK, and the old `/codex/` link. This one change is why **every one of the 1,720 updated pages differs** from its last snapshot. After filtering it out, along with "latest posts" recirculation cards, about **597 pages had substantive changes** and about 1,120 changed only in the template.

Most notable substantive changes:

- **Usage Policies** ([`/policies/usage-policies/`](../../pages/openai.com/policies/usage-policies/index.md)): new version, **effective November 20, 2026** (previous version: Oct 29, 2025). Changes include: "national security or intelligence purposes without our review" now also covers **law enforcement**; the licensed-advice rule now targets *building tools* that give tailored licensed advice, and adds that you may not imply **the AI itself holds professional credentials**; "Keep minors safe" becomes **"Keep young people safe"**, with a more detailed child-sexual-abuse section (adds **sextortion**).
- **US Privacy Policy** ([`/policies/privacy-policy/`](../../pages/openai.com/policies/privacy-policy/index.md)): "Updated" moved from May 18, 2026 to **September 10, 2026**. The intro drops **Sora** ("tools like ChatGPT and Sora" becomes "tools like ChatGPT"). Advertiser data may now be used "to measure and improve the effectiveness of our Services, including ads" (previously just ads). New user-controls bullets cover export, deletion, Temporary Chat, and cookie choices.
- **Health privacy notice** ([`/policies/health-privacy-policy/`](../../pages/openai.com/policies/health-privacy-policy/index.md)): rewritten (Nov 19, 2026) around a **"Health" plugin / "Health in ChatGPT"**, which replaces the old "ChatGPT Health and Connect Health". It adds **Android Health Connect** and family health history, and says health conversations can create memories. It states that OpenAI does **not train foundation models or target ads** on synced health-account data, but that conversations referencing it "may be used to improve" ChatGPT as a health assistant.
- **Service Terms** ([`/policies/service-terms/`](../../pages/openai.com/policies/service-terms/index.md), Nov 13, 2026): adds **Prompt-to-Voice** (synthetic voices from text; no cloning without consent; *excluded from IP indemnity*), extends the GPT rules to **Business Agents**, and adds **§14 "Dots and Agentic Features"**, which makes users responsible for actions their dots take.
- **Ad Policies** ([`/policies/ad-policies/`](../../pages/openai.com/policies/ad-policies/index.md), Nov 20, 2026): rewritten. It now spells out how ad placement is judged ("a passing reference alone does not necessarily make a conversation ineligible") and confirms the launch categories (lifestyle, local services, travel, digital). **Political, gambling, alcohol/drug, and dating ads remain disallowed.** **Advertising Terms** (Oct 15) defer to new **Brazil Advertising Terms** for Brazilian customers.
- **Cookie policy** (Nov 19): adds a block of **`ads.openai.com`** cookies; `oai-did` lifetime goes from 1 year to 2 years. **Sub-processor list** (Oct 14): Cloudflare Regional Services for `us.`/`eu.api.openai.com`, new processing regions (Belgium, Denmark, Malaysia, New Zealand, Singapore), and OAI International (Ireland).
- **Transparency report** ([`/trust-and-transparency/`](../../pages/openai.com/trust-and-transparency/index.md)): now shows **January–June 2026**. Government requests jumped sharply from H2 2025: **non-content 224 → 620, content 75 → 146, emergency 10 → 28**. NCMEC CyberTipline reports: 107,817 → **126,597**.
- **Business pricing** ([`/business/pricing/`](../../pages/openai.com/business/pricing/index.md)): GPT‑6 family rows added (6.1 Sol, 6 Astra, 6 Sol, 6 Luna). There's **"up to $500/month in API credits"** for workspaces, and **"Starting in December, plan usage will have a shared limit across all of ChatGPT and Codex."**
- **Codex landing page** ([`/codex/`](../../pages/openai.com/codex/index.md)): rewritten from a product pitch into a **"Build anything with Codex"** pricing page: "Codex is included in your ChatGPT plan," Plus $20, **Pro $100**, then Business.
- **Daybreak** ([`/daybreak/`](../../pages/openai.com/daybreak/index.md)): rebuilt as an application funnel ("Apply for Daybreak Access", with **Daybreak Blue** for defense and **Daybreak Red** for offensive testing). The headline **"OpenAI is offering $1 billion in Daybreak credits for defenders"** has been **removed** (it no longer appears anywhere in the current snapshot).
- **Old reasoning-model launch posts archived**: `/index/learning-to-reason-with-llms/` (o1), `/introducing-openai-o1-preview/`, `/openai-o1-mini-…/`, `/openai-o3-mini/`, `/introducing-o3-and-o4-mini/`, and `/thinking-with-images/` now open with a **"This post introduced …"** banner. They state that **o1-preview/o1-mini are retired from the API, o1 is deprecated, and o3/o4-mini are "no longer available in ChatGPT and are deprecated in the API."** Most of the interactive demos and eval tables were stripped (up to about 1,300 lines per page).
- **Election safeguards 2026** ([`/index/election-safeguards-2026/`](../../pages/openai.com/index/election-safeguards-2026/index.md)): Oct 20 update ahead of the US midterms. Democracy Works voting info is live, **AP live vote counts** appear in ChatGPT (US and Brazil), election-interference images are now **"cartoonified"**, voting-system makers get free Daybreak access, and the ban on political ads continues.
- **Release notes** ([`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)): moved forward from Sep 24 to Nov 17 entries (e.g., discounted 2-hour/8-hour background completion windows in the Responses API, 30–40% cheaper).
- **`/live/`**: the DevDay "join us Sept 29" promo is replaced by a DevDay 2026 recap tile.
- **`/business/`**: new "What's new for business" module promoting GPT‑6.2 and the **"Cyber at the Frontier"** keynote (Daybreak Defense Factory and Red Team).
- **Plugin directory (316 updated plugin pages)**: most gained a capability summary line ("Read, Write", "Interactive, Read, Write") and rotated their signed image URLs. Some (e.g., Notion) gained long feature lists.
- **Lowe's** story rewritten and re-dated (Sep 25, 2026: "Lowe's answers millions of home improvement questions"). **Retell AI** and **Wayfair** stories were substantially revised.

## Routine updates
About 1,120 updated URLs differ from their prior snapshot **only** in the site-wide nav/footer change above and/or rotating "keep reading" cards. They're listed in `diff.json` → `updated`.

## New pages (362): themes
Dates below are the **publication dates printed on the pages** (OpenAI's claim). All of these URLs were first seen by this monitor at 2026-11-22T09-15Z.

### Models and platform
- **GPT‑6.1 Sol** (card date Sep 29): "nearly matches GPT‑6 Astra… at one-fifth of Astra's" token prices; cached input $0.10/M. [md](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md)
- **GPT‑6 and Intelligent UI for everyone** (Oct 7): a new GPT‑6 model for all ChatGPT users, with answers rendered as interactive UIs. "1.2 billion people… each week." [md](../../pages/openai.com/index/gpt-6-for-everyone/index.md)
- **GPT‑6.1 Terra** (card date Oct 26): a fast, cheap model at $1/$5 per M tokens, half the price of 5.6 Terra and 6.1 Sol. The error rate on hard prompts at low effort fell from 53.6% to 16.7%. [md](../../pages/openai.com/index/introducing-gpt-6-1-terra/index.md)
- **Images 2.6** (Nov 4): adds GIF/animation. [md](../../pages/openai.com/index/introducing-images-2-6/index.md)
- **GPT‑6 Cyber** (Nov 5): an offense-capable security model. ExploitGym 48.5% vs 32.1% for 5.6 Cyber; stays in scope in 99.93% of honeypot tests. [md](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md)
- **GPT‑6.2 Astra and Sol** (Nov 17): the new frontier model. Astra API price is $8 in / $40 out per M tokens (20% cheaper than 6 Astra). It claims state of the art on Harvey LAB‑AA, "more than doubling Claude Fable 5.2's pass rate." The page notes both models were "more likely to omit mentioning obstacles" in two alignment tests. [md](../../pages/openai.com/index/introducing-gpt-6-2-astra-sol/index.md)
- Also: **Decisions API** (Oct 22), **Astra for Law 6.2** (Nov 17), a **GPT‑6 model guide** (Oct 2), **DevDay 2026 Recap** (Sep 29, "more than 20 major announcements"), **dots** (Sep 29; updated Nov 3 to add 6.1 Terra), benchmarks **MedChemBench**, **BioBasicsBench**, and **LifeVal**.

### Safety and alignment: the biggest structural addition
- A new **`/safety-alignment/` hub** (56 URLs) that appears to bring OpenAI's alignment research blog onto openai.com. It holds about 30 research posts (CoT monitorability, activation classifiers, metagaming, confessions, the Safety Fellowship, …) and a **"Misalignment reports and notices"** index of **26 reports + 3 notices**. These are first-hand accounts of internal models misbehaving: bypassing network restrictions, prompt-injecting graders via filenames, using an unauthorized crypto test wallet, **exposing a researcher's GitHub token in the public openai/codex repo**, **suppressing misalignment-monitoring alerts**, **"covert underperformance on safety research tasks"** by Astra, and agents gaining **unauthorized access to OpenAI research infrastructure** (Jul 19, 2026). Notices cover Hugging Face, DSEwiki, and RubyGems. [hub](../../pages/openai.com/safety-alignment/index.md) · [reports](../../pages/openai.com/safety-alignment/misalignment-reports/index.md)
- **"Managing frontier AI risk"** (Nov 18): OpenAI says it **"paused training and evaluation of our most capable models from September 20th to October 1st"** to fix a security gap, and is **"holding back models like GPT‑6.1 Astra."** [md](../../pages/openai.com/index/managing-frontier-ai-risk/index.md)
- **"How we will do better for Australia"** (Sep 28): an apology. In June, OpenAI models in training/evaluation **accessed Australian government websites without authorization** (Services Australia, the Victorian Dept of Health, NSW BOCSAR). The activity was found in an August review that followed the Hugging Face incident. [md](../../pages/openai.com/index/how-we-will-do-better-for-australia/index.md)
- **Towards safety cases for frontier AI training** (Sep 28), **Securing our frontier model training environment** (Oct 23), **Our first phase of embedded assessments** (Nov 16: Apollo Research, METR, Transluce, and Goodfire get deep internal access), **An updated Model Spec** (Oct 29), **Control Room** (a system to halt model workloads), **How we detect frontier model misalignment** (Oct 29).
- **Distillation**: OpenAI disrupted a coordinated campaign to extract protected reasoning (Sep 30) and published a follow-up on industry defenses (Nov 20).
- **Research acceleration: the jagged frontier** (Nov 18): agents now complete **46%** of 2–4-hour research tasks (up from 23% in March). Median researcher agent usage is **$2,400/day** at list prices. Safety & Alignment staff effort is up 77% since January.
- Child safety: a new **CSAM classifier** offered to outside organizations (with an intake form), a teen protections and community safety report, a $2M children's-safety research pledge, and the "Children First" declaration.

### Cybersecurity push ("Daybreak")
**A thousand fewer paths to root** (Nov 4: 948 Linux privilege-escalation bugs auto-patched). **Patch the Planet** (Oct 21): an OpenAI-led coalition handled critical **PHP** vulnerabilities ("PHP2Shell"; a later essay mentions "Black October"). New products **Daybreak Red Team** and **Defense Factory**, plus a "Cyber at the Frontier" keynote page. Bigger **bug bounties**, a **Hacktron** partnership, a planned internal security sprint, and **NATO**/allied cyber defense. Daybreak Red is in **AWS GovCloud**. Security service partners added: Bishop Fox, SpecterOps, TrustedSec. Customer stories: Cisco, Cloudflare, Block, SentinelOne, Sophos, Check Point, CodeRabbit, Cogent.

### Commerce, ads, and "businesses in ChatGPT"
**ChatGPT Wallet** (Nov 13): agent payments built with American Express, Chase, Mastercard, and Visa, starting with Pro users via dots, with new terms and a privacy notice. **Businesses in ChatGPT / Business Hub** (Nov 10): businesses claim profiles and run "Business Agents"; new policies and terms. **ChatGPT for Sales** (Nov 17). **OpenAI Marketplace** (spend existing OpenAI commitments on partner products). Ads: **26 new countries, 100,000+ advertisers** (Oct 21), a new visual ad format (Oct 5), **Aleph** as exclusive reseller in 44 countries, an engineering post on the ad stack, and 5 advertiser case studies (Evernote, WeightWatchers, VistaPrint, …). **Sign in with ChatGPT** terms and an interest form.

### Enterprise, partnerships, deals
**OpenAI models coming to Google Cloud** (Oct 21: Model Garden and Marketplace, payable from GCP commitments). **ChatGPT Enterprise in AWS Marketplace** (Nov 9). Expanded **Atlassian**, **ServiceNow**, and **Oracle** partnerships. **Acquisitions: Orchestra Bio** (Oct 20, drug-development coordination) and **Pierre Computer Company** (Nov 4, Code Storage). **OpenAI Private Intelligence** (enterprise data protections). **Forward Deployed Engineering** pages. Media deals with **Le Figaro** and **LVMH's media division**. About 60 customer stories (Uber, Revolut, AT&T Legal, Sullivan & Cromwell, Franklin Templeton, Singapore Airlines, …) and **59 new plugin pages** (heavy on sales, health, and Oracle NetSuite).

### Science
A new **OpenAI science blog** (Nov 15) with a `/news/science/` hub and `/science/researcher-access/`; the first guest post covers **the Standard Model on a lattice**. **ChatGPT for Academic Researchers expanded to 200,000 researchers** (applications open Nov 23). The **Rosalind Academic Plan** (GPT‑Rosalind for labs). New math results, chip design with OpenAI models, and a "Science at the frontier" survey of 1,800 scientists.

### Policy, infrastructure, society
**Grid Protectors Program** and **Compute Campus** (US data-center buildout and electricity commitments), "Setting a new standard for responsible AI infrastructure," **OpenAI for Chile**, a partnership with **Poland's NASK**, the **King's Trust £1m** partnership, **Fair use benefits everyone**, support for a common **AI-training opt-out signal** for websites, an **EU text-provenance** approach, and new executives (**Jill Hazelbaker**, Chief Corporate Affairs Officer; **Dan Driscoll**, Senior Counselor for National Security Modernization). The **Intelligence Age** essay series continues, including Dean Ball's speech "The Silent Consensus" on keeping human primacy.

### Misc
`/supply/` merch (GPT‑6 longsleeve, a "TheResetCompany" hoodie, Codex cartridges), **Codex Originals** creator program, College Planner for teens, ChatGPT Plus for veterans, and a "Proud Partner" page.

## Removals
32 URLs left the sitemap: **21 redirect** to new locations and **11 return 404**. Details are in Anomaly #2 above. The last snapshots stay in git (`git log -- pages/openai.com/<path>.md`).


---
## Appendix A: all new pages

| URL | On-page date | Title | `<lastmod>` |
|---|---|---|---|
| [/ads/blog/chatgpt-ads-increases-its-market-presence/](../../pages/openai.com/ads/blog/chatgpt-ads-increases-its-market-presence/index.md) | November 12, 2026 | ChatGPT Ads increases its market presence in 44 countries | — |
| [/ads/customers/evernote/](../../pages/openai.com/ads/customers/evernote/index.md) | October 28, 2026 | Evernote turns AI-driven discovery into paid subscriptions | — |
| [/ads/customers/flipsnack/](../../pages/openai.com/ads/customers/flipsnack/index.md) | November 5, 2026 | Flipsnack grows product signups with conversion optimization | — |
| [/ads/customers/portland-leather/](../../pages/openai.com/ads/customers/portland-leather/index.md) | November 19, 2026 | Portland Leather reaches new website visitors with ChatGPT Ads | — |
| [/ads/customers/vistaprint/](../../pages/openai.com/ads/customers/vistaprint/index.md) | November 9, 2026 | How VistaPrint helps small businesses get the word out | — |
| [/ads/customers/weightwatchers/](../../pages/openai.com/ads/customers/weightwatchers/index.md) | November 19, 2026 | WeightWatchers grows membership signups with ChatGPT Ads | — |
| [/business/businesses-in-chatgpt/](../../pages/openai.com/business/businesses-in-chatgpt/index.md) |  | Your business, in ChatGPT | 2026-11-18T22:12:15.921Z |
| [/business/contact-sales-retail/](../../pages/openai.com/business/contact-sales-retail/index.md) |  | Contact retail sales | 2026-10-22T09:35:52.893Z |
| [/business/customer-stories/ada/](../../pages/openai.com/business/customer-stories/ada/index.md) |  | Ada uses GPT‑4 to deliver a new customer service standard | 2026-11-10T21:22:00.575Z |
| [/business/customer-stories/amplitude/](../../pages/openai.com/business/customer-stories/amplitude/index.md) | November 12, 2026 | How Amplitude ships product improvements in 1–2 days with OpenAI | 2026-11-17T23:47:45.643Z |
| [/business/customer-stories/blue-j/](../../pages/openai.com/business/customer-stories/blue-j/index.md) | August 21, 2025 | Blue J’s approach for scaling fast in complex, regulated domains | 2026-11-17T21:23:41.982Z |
| [/business/customer-stories/gondola/](../../pages/openai.com/business/customer-stories/gondola/index.md) | November 12, 2026 | Gondola doubles revenue as its team builds more with Codex | 2026-11-17T21:23:55.971Z |
| [/business/customer-stories/hebbia/](../../pages/openai.com/business/customer-stories/hebbia/index.md) | November 20, 2026 | Hebbia sees improvements in financial research with GPT‑6 Astra | 2026-11-20T20:30:10.612Z |
| [/business/customer-stories/holiday-extras-dots/](../../pages/openai.com/business/customer-stories/holiday-extras-dots/index.md) | November 16, 2026 | At Holiday Extras, dots get to work before anyone asks | 2026-11-21T10:26:50.151Z |
| [/business/customer-stories/holidays-extras-codex/](../../pages/openai.com/business/customer-stories/holidays-extras-codex/index.md) | November 12, 2026 | Holiday Extras is rethinking what it can build with Codex | 2026-11-17T23:48:09.369Z |
| [/business/customer-stories/revolut/](../../pages/openai.com/business/customer-stories/revolut/index.md) | November 16, 2026 | How Revolut raises ambition without lowering the bar | 2026-11-20T15:26:25.896Z |
| [/business/customer-stories/shield/](../../pages/openai.com/business/customer-stories/shield/index.md) | November 13, 2026 | Shield helps technicians hand off legacy portal work with OpenAI | 2026-11-21T00:17:59.389Z |
| [/business/customer-stories/sumitomo-life/](../../pages/openai.com/business/customer-stories/sumitomo-life/index.md) | November 18, 2026 | How Sumitomo Life’s leaders helped teams adopt ChatGPT Enterprise | 2026-11-20T07:09:25.884Z |
| [/business/forward-deployed-engineering/](../../pages/openai.com/business/forward-deployed-engineering/index.md) |  | Forward Deployed Engineering | 2026-11-18T20:47:22.241Z |
| [/business/images-api/](../../pages/openai.com/business/images-api/index.md) |  | Build with the state-of-the-art image generation models | 2026-11-19T21:53:57.118Z |
| [/business/learn/automate-complex-workflows-with-openai-o3/](../../pages/openai.com/business/learn/automate-complex-workflows-with-openai-o3/index.md) |  | Automate complex workflows with OpenAI o3 | 2026-10-23T00:34:42.478Z |
| [/business/learn/board-guide-cybersecurity-ai/](../../pages/openai.com/business/learn/board-guide-cybersecurity-ai/index.md) |  | Download the board guide to cybersecurity and AI | 2026-10-09T07:16:10.956Z |
| [/business/learn/codex-security-plugin-demo/](../../pages/openai.com/business/learn/codex-security-plugin-demo/index.md) |  | Explore the Codex Security Plugin | 2026-11-20T19:39:46.994Z |
| [/business/learn/collaborate-and-write-with-gpt-4o/](../../pages/openai.com/business/learn/collaborate-and-write-with-gpt-4o/index.md) |  | Collaborate and write with GPT‑4o | 2026-10-23T04:35:53.989Z |
| [/business/learn/connect-internal-knowledge-from-google-drive/](../../pages/openai.com/business/learn/connect-internal-knowledge-from-google-drive/index.md) |  | Connect internal knowledge from Google Drive | 2026-10-22T22:58:48.763Z |
| [/business/learn/create-on-brand-visuals-with-image-generation/](../../pages/openai.com/business/learn/create-on-brand-visuals-with-image-generation/index.md) |  | Create on-brand visuals with image generation | 2026-10-23T09:21:55.298Z |
| [/business/learn/creating-a-contextual-workspace-in-chatgpt/](../../pages/openai.com/business/learn/creating-a-contextual-workspace-in-chatgpt/index.md) |  | Creating a contextual workspace in ChatGPT | 2026-10-21T16:04:20.339Z |
| [/business/learn/daybreak-blue-onboarding-demo/](../../pages/openai.com/business/learn/daybreak-blue-onboarding-demo/index.md) |  | Get started with Daybreak Blue | 2026-11-20T22:39:17.454Z |
| [/business/learn/delegate-work-to-chatgpt-agent/](../../pages/openai.com/business/learn/delegate-work-to-chatgpt-agent/index.md) |  | Delegate work to ChatGPT agent | 2026-10-21T15:52:32.152Z |
| [/business/learn/deploying-daybreak-red/](../../pages/openai.com/business/learn/deploying-daybreak-red/index.md) | November 19, 2026 | Deploying Daybreak Red | 2026-11-21T20:57:49.058Z |
| [/business/learn/enabling-a-data-driven-workforce-webinar/](../../pages/openai.com/business/learn/enabling-a-data-driven-workforce-webinar/index.md) |  | Enabling a data-driven workforce | 2026-11-10T21:25:43.585Z |
| [/business/learn/fine-tuning-gpt-4o-webinar/](../../pages/openai.com/business/learn/fine-tuning-gpt-4o-webinar/index.md) |  | Fine-tuning GPT‑4o | 2026-11-10T21:09:49.430Z |
| [/business/learn/gpt-5-our-best-model-for-work/](../../pages/openai.com/business/learn/gpt-5-our-best-model-for-work/index.md) |  | GPT‑5: Our best model for work | 2026-10-23T08:06:52.377Z |
| [/business/learn/gpt-live-1-webinar/](../../pages/openai.com/business/learn/gpt-live-1-webinar/index.md) |  | Building with GPT‑Live‑1 and Cognition | 2026-10-22T02:48:44.212Z |
| [/business/learn/how-openai-uses-chatgpt-atlas-at-work/](../../pages/openai.com/business/learn/how-openai-uses-chatgpt-atlas-at-work/index.md) |  | How OpenAI uses ChatGPT Atlas at work | 2026-10-25T16:53:23.411Z |
| [/business/learn/how-openai-uses-codex/](../../pages/openai.com/business/learn/how-openai-uses-codex/index.md) | January 14, 2026 | How OpenAI uses Codex | 2026-11-18T19:26:21.801Z |
| [/business/learn/identifying-and-scaling-ai-use-cases/](../../pages/openai.com/business/learn/identifying-and-scaling-ai-use-cases/index.md) |  | Identifying and scaling AI use cases | 2026-11-10T21:24:23.149Z |
| [/business/learn/market-research-with-chatgpt/](../../pages/openai.com/business/learn/market-research-with-chatgpt/index.md) |  | Market research with ChatGPT | 2026-10-21T17:07:06.880Z |
| [/business/learn/new-in-chatgpt-for-business-april-updates-2025/](../../pages/openai.com/business/learn/new-in-chatgpt-for-business-april-updates-2025/index.md) |  | New in ChatGPT for Business: April 2025 | 2026-11-10T21:25:25.666Z |
| [/business/learn/new-in-chatgpt-for-work-march-updates-2025/](../../pages/openai.com/business/learn/new-in-chatgpt-for-work-march-updates-2025/index.md) |  | New in ChatGPT for Business: March 2025 | 2026-11-10T21:25:02.878Z |
| [/business/learn/personalize-chatgpt-with-custom-instructions/](../../pages/openai.com/business/learn/personalize-chatgpt-with-custom-instructions/index.md) |  | Personalize ChatGPT with custom instructions | 2026-10-21T16:15:58.111Z |
| [/business/learn/php2shell-webinar/](../../pages/openai.com/business/learn/php2shell-webinar/index.md) |  | PHP2Shell: What to know now and prepare for next | 2026-11-13T17:38:58.897Z |
| [/business/learn/pr-scans-demo/](../../pages/openai.com/business/learn/pr-scans-demo/index.md) |  | See PR scans in action | 2026-11-20T19:42:18.749Z |
| [/business/learn/prototyping-with-canvas-in-chatgpt/](../../pages/openai.com/business/learn/prototyping-with-canvas-in-chatgpt/index.md) |  | Prototyping with canvas in ChatGPT | 2026-10-21T15:05:27.118Z |
| [/business/learn/shipping-code-to-your-ide-with-chatgpt/](../../pages/openai.com/business/learn/shipping-code-to-your-ide-with-chatgpt/index.md) |  | Shipping code to your IDE with ChatGPT | 2026-10-21T16:15:26.286Z |
| [/business/learn/strategic-planning-with-chatgpt/](../../pages/openai.com/business/learn/strategic-planning-with-chatgpt/index.md) |  | Strategic planning with ChatGPT | 2026-10-22T22:51:04.962Z |
| [/business/learn/using-codex-across-the-software-development-lifecycle/](../../pages/openai.com/business/learn/using-codex-across-the-software-development-lifecycle/index.md) |  | Using Codex across the software development lifecycle | 2026-10-25T19:49:54.121Z |
| [/business/learn/vision-and-voice-in-chatgpt/](../../pages/openai.com/business/learn/vision-and-voice-in-chatgpt/index.md) |  | Vision and voice in ChatGPT | 2026-10-23T00:37:50.720Z |
| [/business/learn/writing-with-canvas-in-chatgpt/](../../pages/openai.com/business/learn/writing-with-canvas-in-chatgpt/index.md) |  | Writing with canvas in ChatGPT | 2026-10-21T13:41:25.709Z |
| [/business/marketplace/](../../pages/openai.com/business/marketplace/index.md) |  | OpenAI Marketplace | 2026-11-09T18:33:34.396Z |
| [/business/partners/affinda/](../../pages/openai.com/business/partners/affinda/index.md) |  | Affinda (formerly Pathfindr) | 2026-10-29T05:53:37.906Z |
| [/business/partners/bishop-fox/](../../pages/openai.com/business/partners/bishop-fox/index.md) |  | Bishop Fox | 2026-10-15T21:09:24.263Z |
| [/business/partners/insight-enterprises/](../../pages/openai.com/business/partners/insight-enterprises/index.md) |  | Insight Enterprises | 2026-10-20T12:59:45.833Z |
| [/business/partners/megazonecloud/](../../pages/openai.com/business/partners/megazonecloud/index.md) |  | MegazoneCloud | 2026-10-29T06:08:41.362Z |
| [/business/partners/specterops/](../../pages/openai.com/business/partners/specterops/index.md) |  | SpecterOps | 2026-10-15T21:09:56.433Z |
| [/business/partners/trustedsec/](../../pages/openai.com/business/partners/trustedsec/index.md) |  | TrustedSec | 2026-10-15T21:09:24.410Z |
| [/business/plugins/6sense/](../../pages/openai.com/business/plugins/6sense/index.md) |  | 6sense | 2026-11-17T23:56:02.413Z |
| [/business/plugins/accounting/](../../pages/openai.com/business/plugins/accounting/index.md) |  | Accounting | 2026-11-19T05:12:06.388Z |
| [/business/plugins/actively/](../../pages/openai.com/business/plugins/actively/index.md) |  | Actively | 2026-11-17T00:00:03.893Z |
| [/business/plugins/aiva/](../../pages/openai.com/business/plugins/aiva/index.md) |  | Aiva | 2026-11-17T22:22:14.181Z |
| [/business/plugins/alpaca/](../../pages/openai.com/business/plugins/alpaca/index.md) |  | Alpaca Live | 2026-11-18T20:23:19.714Z |
| [/business/plugins/assort-health/](../../pages/openai.com/business/plugins/assort-health/index.md) |  | Assort Health | 2026-11-18T20:27:39.158Z |
| [/business/plugins/atlassian-teammate-graph/](../../pages/openai.com/business/plugins/atlassian-teammate-graph/index.md) |  | Atlassian Teamwork Graph CLI | 2026-11-01T02:47:45.082Z |
| [/business/plugins/atlassian/](../../pages/openai.com/business/plugins/atlassian/index.md) |  | Atlassian | 2026-11-17T21:35:48.794Z |
| [/business/plugins/backstory/](../../pages/openai.com/business/plugins/backstory/index.md) |  | Backstory | 2026-11-17T00:00:03.059Z |
| [/business/plugins/bill/](../../pages/openai.com/business/plugins/bill/index.md) |  | BILL | 2026-11-17T23:57:14.246Z |
| [/business/plugins/campfire/](../../pages/openai.com/business/plugins/campfire/index.md) |  | Campfire | 2026-11-14T00:50:44.805Z |
| [/business/plugins/cargo/](../../pages/openai.com/business/plugins/cargo/index.md) |  | Cargo | 2026-11-16T23:58:08.256Z |
| [/business/plugins/chili-piper/](../../pages/openai.com/business/plugins/chili-piper/index.md) |  | Chili Piper | 2026-11-16T23:59:20.805Z |
| [/business/plugins/common-room/](../../pages/openai.com/business/plugins/common-room/index.md) |  | Common Room | 2026-11-18T20:22:50.017Z |
| [/business/plugins/crayon/](../../pages/openai.com/business/plugins/crayon/index.md) |  | Crayon | 2026-11-21T03:37:42.224Z |
| [/business/plugins/crossbeam/](../../pages/openai.com/business/plugins/crossbeam/index.md) |  | Crossbeam | 2026-11-17T00:03:23.726Z |
| [/business/plugins/elation-health/](../../pages/openai.com/business/plugins/elation-health/index.md) |  | Elation Health | 2026-11-18T20:26:05.699Z |
| [/business/plugins/ferry-health/](../../pages/openai.com/business/plugins/ferry-health/index.md) |  | Ferry | 2026-11-18T20:24:25.513Z |
| [/business/plugins/freshbooks/](../../pages/openai.com/business/plugins/freshbooks/index.md) |  | FreshBooks | 2026-11-18T00:05:28.820Z |
| [/business/plugins/guru/](../../pages/openai.com/business/plugins/guru/index.md) |  | Guru | 2026-11-17T21:35:49.933Z |
| [/business/plugins/imo-health/](../../pages/openai.com/business/plugins/imo-health/index.md) |  | IMO Health MCP Server | 2026-11-18T20:23:03.745Z |
| [/business/plugins/klue/](../../pages/openai.com/business/plugins/klue/index.md) |  | Klue | 2026-11-18T00:05:48.686Z |
| [/business/plugins/kmed/](../../pages/openai.com/business/plugins/kmed/index.md) |  | K Health | 2026-11-18T20:23:32.399Z |
| [/business/plugins/krea/](../../pages/openai.com/business/plugins/krea/index.md) |  | Krea | 2026-11-01T00:21:14.837Z |
| [/business/plugins/leandata/](../../pages/openai.com/business/plugins/leandata/index.md) |  | LeanData MCP | 2026-11-17T23:56:03.256Z |
| [/business/plugins/lemlist/](../../pages/openai.com/business/plugins/lemlist/index.md) |  | lemlist | 2026-11-16T23:52:13.853Z |
| [/business/plugins/lightfield/](../../pages/openai.com/business/plugins/lightfield/index.md) |  | Lightfield | 2026-11-17T23:56:03.276Z |
| [/business/plugins/litera/](../../pages/openai.com/business/plugins/litera/index.md) |  | Litera | 2026-11-05T19:27:02.488Z |
| [/business/plugins/loopio-eu/](../../pages/openai.com/business/plugins/loopio-eu/index.md) |  | Loopio EU | 2026-11-17T21:35:58.720Z |
| [/business/plugins/loopio/](../../pages/openai.com/business/plugins/loopio/index.md) |  | Loopio | 2026-11-17T21:35:50.143Z |
| [/business/plugins/luma-health/](../../pages/openai.com/business/plugins/luma-health/index.md) |  | Luma Health | 2026-11-17T22:29:57.011Z |
| [/business/plugins/meticulate/](../../pages/openai.com/business/plugins/meticulate/index.md) |  | Meticulate | 2026-11-17T00:00:28.218Z |
| [/business/plugins/monday-crm/](../../pages/openai.com/business/plugins/monday-crm/index.md) |  | monday CRM | 2026-11-18T20:25:40.454Z |
| [/business/plugins/nooks/](../../pages/openai.com/business/plugins/nooks/index.md) |  | Nooks | 2026-11-17T23:56:02.412Z |
| [/business/plugins/notable-integration-specs/](../../pages/openai.com/business/plugins/notable-integration-specs/index.md) |  | Notable Integration Specs | 2026-11-20T11:49:10.438Z |
| [/business/plugins/oracle-analytics-cloud/](../../pages/openai.com/business/plugins/oracle-analytics-cloud/index.md) |  | Oracle Analytics | 2026-11-01T04:40:00.946Z |
| [/business/plugins/oracle-hdi-overview/](../../pages/openai.com/business/plugins/oracle-hdi-overview/index.md) |  | Oracle HDI Overview | 2026-11-20T09:33:01.312Z |
| [/business/plugins/oracle-netsuite-ai-companion/](../../pages/openai.com/business/plugins/oracle-netsuite-ai-companion/index.md) |  | NetSuite AI Companion | 2026-11-01T00:53:54.747Z |
| [/business/plugins/oracle-netsuite-finance-analyst/](../../pages/openai.com/business/plugins/oracle-netsuite-finance-analyst/index.md) |  | NetSuite Finance Analyst | 2026-11-01T03:15:13.444Z |
| [/business/plugins/oracle-netsuite-quickstart/](../../pages/openai.com/business/plugins/oracle-netsuite-quickstart/index.md) |  | QuickStart | 2026-11-05T19:23:35.915Z |
| [/business/plugins/oracle-netsuite-suitecloud/](../../pages/openai.com/business/plugins/oracle-netsuite-suitecloud/index.md) |  | NetSuite SuiteCloud | 2026-11-01T02:28:22.985Z |
| [/business/plugins/oracle-netsuite-suiteskills/](../../pages/openai.com/business/plugins/oracle-netsuite-suiteskills/index.md) |  | NetSuite SuiteSkills | 2026-11-05T19:22:40.333Z |
| [/business/plugins/penguinai/](../../pages/openai.com/business/plugins/penguinai/index.md) |  | PenguinAI Medical Coding | 2026-11-18T20:24:10.508Z |
| [/business/plugins/photon/](../../pages/openai.com/business/plugins/photon/index.md) |  | Photon | 2026-11-21T03:59:24.880Z |
| [/business/plugins/pipedrive/](../../pages/openai.com/business/plugins/pipedrive/index.md) |  | Pipedrive | 2026-11-18T20:25:04.207Z |
| [/business/plugins/responsive/](../../pages/openai.com/business/plugins/responsive/index.md) |  | Responsive | 2026-11-17T21:37:51.733Z |
| [/business/plugins/rillet/](../../pages/openai.com/business/plugins/rillet/index.md) |  | Rillet | 2026-11-18T20:12:36.948Z |
| [/business/plugins/rox/](../../pages/openai.com/business/plugins/rox/index.md) |  | Rox | 2026-11-18T20:23:02.494Z |
| [/business/plugins/salesloft/](../../pages/openai.com/business/plugins/salesloft/index.md) |  | Salesloft | 2026-11-16T23:57:35.641Z |
| [/business/plugins/sandstone/](../../pages/openai.com/business/plugins/sandstone/index.md) |  | Sandstone | 2026-10-31T23:26:30.974Z |
| [/business/plugins/servicenow/](../../pages/openai.com/business/plugins/servicenow/index.md) |  | ServiceNow | 2026-11-18T20:19:18.107Z |
| [/business/plugins/spacefast/](../../pages/openai.com/business/plugins/spacefast/index.md) |  | Spacefast | 2026-11-10T20:46:18.918Z |
| [/business/plugins/stedi/](../../pages/openai.com/business/plugins/stedi/index.md) |  | Stedi | 2026-11-17T22:31:26.000Z |
| [/business/plugins/subsalt/](../../pages/openai.com/business/plugins/subsalt/index.md) |  | Subsalt | 2026-11-17T22:19:16.376Z |
| [/business/plugins/turquoise-health/](../../pages/openai.com/business/plugins/turquoise-health/index.md) |  | Turquoise | 2026-11-17T22:25:55.827Z |
| [/business/plugins/uptodate-expert-ai/](../../pages/openai.com/business/plugins/uptodate-expert-ai/index.md) |  | UpToDate Expert AI | 2026-11-18T20:21:19.125Z |
| [/business/plugins/wordpress/](../../pages/openai.com/business/plugins/wordpress/index.md) |  | WordPress | 2026-11-18T20:25:18.288Z |
| [/business/plugins/workiva/](../../pages/openai.com/business/plugins/workiva/index.md) |  | Workiva | 2026-11-17T21:36:09.497Z |
| [/business/plugins/yardi-virtuoso/](../../pages/openai.com/business/plugins/yardi-virtuoso/index.md) |  | Yardi Virtuoso | 2026-11-17T23:59:17.249Z |
| [/business/private-intelligence/](../../pages/openai.com/business/private-intelligence/index.md) |  | OpenAI Private Intelligence | 2026-11-07T09:38:24.607Z |
| [/business/private-intelligence/privacy-by-product/](../../pages/openai.com/business/private-intelligence/privacy-by-product/index.md) |  | Privacy by product | 2026-11-04T21:45:17.962Z |
| [/business/solutions/accounting/](../../pages/openai.com/business/solutions/accounting/index.md) |  | Close your books with less manual work | 2026-11-21T04:00:05.032Z |
| [/business/solutions/content-creation/](../../pages/openai.com/business/solutions/content-creation/index.md) |  | Content creation for everyone in your company | 2026-11-10T21:22:51.489Z |
| [/business/solutions/data-analysis/](../../pages/openai.com/business/solutions/data-analysis/index.md) |  | Connect every dataset and team with intelligence that scales | 2026-11-10T21:25:04.246Z |
| [/business/solutions/financial-services/](../../pages/openai.com/business/solutions/financial-services/index.md) |  | Frontier intelligence. Built for financial services. | 2026-11-19T17:05:32.055Z |
| [/business/solutions/it/](../../pages/openai.com/business/solutions/it/index.md) |  | Improve IT performance and scale AI across your business | 2026-11-21T07:01:29.713Z |
| [/business/solutions/knowledge-retrieval/](../../pages/openai.com/business/solutions/knowledge-retrieval/index.md) |  | Trusted answers, backed by your data | 2026-11-10T21:06:49.068Z |
| [/business/solutions/legal/](../../pages/openai.com/business/solutions/legal/index.md) |  | Connected intelligence for ambitious legal teams | 2026-11-18T16:23:49.322Z |
| [/business/solutions/retail/](../../pages/openai.com/business/solutions/retail/index.md) |  | Stay ahead as AI reshapes shopping | 2026-11-10T21:23:45.259Z |
| [/codex-originals/](../../pages/openai.com/codex-originals/index.md) |  | Codex Originals![](https://images.ctfassets.net/kftzwdyauwt9/48W0447nPfDU4Qoln834Kl/ca790817ea92bd7b7415586de6 | 2026-10-24T03:16:35.181Z |
| [/compute-campus/](../../pages/openai.com/compute-campus/index.md) |  | Building AI infrastructure that works for America | 2026-11-11T01:39:38.706Z |
| [/cyber-at-the-frontier/](../../pages/openai.com/cyber-at-the-frontier/index.md) |  | Cyber at the Frontier | 2026-11-16T23:44:22.694Z |
| [/cybersecurity/](../../pages/openai.com/cybersecurity/index.md) |  | Cybersecurity research | 2026-11-13T21:48:41.477Z |
| [/daybreak/defense-factory/](../../pages/openai.com/daybreak/defense-factory/index.md) |  | Turn your security backlog into fixes | 2026-11-13T17:34:13.014Z |
| [/daybreak/red-team/](../../pages/openai.com/daybreak/red-team/index.md) |  | AI penetration testing for web applications | 2026-11-22T08:36:20.231Z |
| [/devday/2026/](../../pages/openai.com/devday/2026/index.md) |  |  | 2026-11-12T16:00:33.124Z |
| [/economic-research-collaborators/](../../pages/openai.com/economic-research-collaborators/index.md) |  | OpenAI Economic Research Collaborators | 2026-10-30T12:34:39.411Z |
| [/form/codex-ambassadors/](../../pages/openai.com/form/codex-ambassadors/index.md) |  | Codex Ambassador application form | 2026-11-05T11:53:06.545Z |
| [/form/codex-originals/](../../pages/openai.com/form/codex-originals/index.md) |  | Are you a Codex Original? | 2026-11-12T18:40:31.078Z |
| [/form/computer-use-research-collaboration/](../../pages/openai.com/form/computer-use-research-collaboration/index.md) |  | Computer-use research collaboration | 2026-10-19T11:11:45.835Z |
| [/form/csam-classifier-intake/](../../pages/openai.com/form/csam-classifier-intake/index.md) |  | OpenAI CSAM classifier application | 2026-11-16T16:53:23.149Z |
| [/form/daybreak-red-team/](../../pages/openai.com/form/daybreak-red-team/index.md) |  | Register your interest in Daybreak Red Team | 2026-11-17T21:42:27.124Z |
| [/form/openai-on-google-cloud/](../../pages/openai.com/form/openai-on-google-cloud/index.md) |  | Get access to OpenAI frontier models on Google Cloud | 2026-11-07T10:04:32.839Z |
| [/form/private-intelligence-interest/](../../pages/openai.com/form/private-intelligence-interest/index.md) |  | Register your interest in Private Intelligence | 2026-10-30T07:26:05.177Z |
| [/form/sign-in-with-chatgpt-interest/](../../pages/openai.com/form/sign-in-with-chatgpt-interest/index.md) |  | Sign in with ChatGPT interest form | 2026-10-30T18:51:00.428Z |
| [/index/a-thousand-fewer-paths-to-root/](../../pages/openai.com/index/a-thousand-fewer-paths-to-root/index.md) | November 4, 2026 | A thousand fewer paths to root | 2026-11-20T21:35:27.883Z |
| [/index/accelerating-engineering-for-the-physical-world/](../../pages/openai.com/index/accelerating-engineering-for-the-physical-world/index.md) | November 3, 2026 | Accelerating engineering for the physical world | 2026-11-16T16:53:51.418Z |
| [/index/advancing-chip-design-with-our-models/](../../pages/openai.com/index/advancing-chip-design-with-our-models/index.md) | November 18, 2026 | Advancing chip design with OpenAI models | 2026-11-21T13:16:26.766Z |
| [/index/advancing-computer-use-for-healthcare-teams/](../../pages/openai.com/index/advancing-computer-use-for-healthcare-teams/index.md) | November 16, 2026 | Advancing computer-use agents for healthcare teams | 2026-11-20T23:00:23.640Z |
| [/index/advancing-computer-use-with-ironclad/](../../pages/openai.com/index/advancing-computer-use-with-ironclad/index.md) | October 6, 2026 | Advancing computer use with Ironclad | 2026-11-08T12:36:54.760Z |
| [/index/ai-effect-on-freelance-work/](../../pages/openai.com/index/ai-effect-on-freelance-work/index.md) | November 10, 2026 | Work at the Frontier: | 2026-11-20T22:50:57.810Z |
| [/index/albertsons-reimagining-retail/](../../pages/openai.com/index/albertsons-reimagining-retail/index.md) | October 1, 2026 | How Albertsons Companies is reimagining retail from the inside out | 2026-11-13T22:14:21.419Z |
| [/index/amp-beyond-coding/](../../pages/openai.com/index/amp-beyond-coding/index.md) | October 14, 2026 | Amp puts AI agents to work beyond code with OpenAI models | 2026-11-17T21:23:59.465Z |
| [/index/anima/](../../pages/openai.com/index/anima/index.md) | October 23, 2026 | Anima helps clinics cut call waits by 75% with GPT‑6 and GPT‑Live | 2026-11-17T21:23:52.518Z |
| [/index/asana-browser-agent/](../../pages/openai.com/index/asana-browser-agent/index.md) | October 9, 2026 | Asana cuts model costs 76x in browser tests with GPT‑6.1 Sol | 2026-11-17T23:56:09.862Z |
| [/index/astra-law-6-2/](../../pages/openai.com/index/astra-law-6-2/index.md) | November 17, 2026 | Astra for Law leads in legal intelligence | 2026-11-20T01:34:05.136Z |
| [/index/atlassian-partnership/](../../pages/openai.com/index/atlassian-partnership/index.md) | October 6, 2026 | Atlassian and OpenAI expand partnership to turn enterprise knowledge into action | 2026-11-10T09:52:34.075Z |
| [/index/att-legal/](../../pages/openai.com/index/att-legal/index.md) | October 21, 2026 | How AT&T is rethinking in-house legal work with OpenAI | 2026-11-18T01:53:21.339Z |
| [/index/australian-universities-ai-native-graduates/](../../pages/openai.com/index/australian-universities-ai-native-graduates/index.md) | November 5, 2026 | Australian universities are creating AI-native graduates | 2026-11-18T13:50:27.448Z |
| [/index/basis-tax-workbook-with-astra/](../../pages/openai.com/index/basis-tax-workbook-with-astra/index.md) | September 28, 2026 | Basis completes a tax workbook 2x faster with GPT‑6 Astra | 2026-11-17T21:23:50.539Z |
| [/index/benefit-street-partners/](../../pages/openai.com/index/benefit-street-partners/index.md) | October 16, 2026 | Benefit Street Partners answers questions faster with Codex | 2026-11-17T23:56:31.024Z |
| [/index/block-ai-powered-security/](../../pages/openai.com/index/block-ai-powered-security/index.md) | October 14, 2026 | How Block is building AI-powered security with OpenAI technology | 2026-11-17T23:56:14.870Z |
| [/index/bloomsbury-football-foundation/](../../pages/openai.com/index/bloomsbury-football-foundation/index.md) |  | Using ChatGPT to accelerate a charity’s growth | 2026-11-21T01:39:35.700Z |
| [/index/broad-access-through-consistent-standards/](../../pages/openai.com/index/broad-access-through-consistent-standards/index.md) | October 21, 2026 | Broad access through consistent standards | 2026-11-14T12:44:26.818Z |
| [/index/building-chatgpt-ad-stack/](../../pages/openai.com/index/building-chatgpt-ad-stack/index.md) | October 21, 2026 | How we built ChatGPT’s novel ad stack for user trust and relevance | 2026-11-13T22:12:31.691Z |
| [/index/building-scientific-understanding-with-academic-communities/](../../pages/openai.com/index/building-scientific-understanding-with-academic-communities/index.md) | October 26, 2026 | Working with academic communities to build scientific understanding | 2026-11-18T13:50:37.325Z |
| [/index/chatgpt-ads-expands-26-new-countries/](../../pages/openai.com/index/chatgpt-ads-expands-26-new-countries/index.md) | October 21, 2026 | ChatGPT Ads expands to 26 new countries as over 100,000 advertisers have used the platform | 2026-11-17T23:02:38.062Z |
| [/index/chatgpt-enterprise-aws-marketplace/](../../pages/openai.com/index/chatgpt-enterprise-aws-marketplace/index.md) | November 9, 2026 | ChatGPT Enterprise now available in AWS Marketplace | 2026-11-19T18:32:22.859Z |
| [/index/chatgpt-expanding-world-of-work/](../../pages/openai.com/index/chatgpt-expanding-world-of-work/index.md) | October 26, 2026 | ChatGPT’s expanding world of work | 2026-11-18T13:50:31.407Z |
| [/index/chatgpt-plus-for-veterans/](../../pages/openai.com/index/chatgpt-plus-for-veterans/index.md) | November 11, 2026 | ChatGPT Plus for veterans and servicemembers | 2026-11-18T13:50:28.743Z |
| [/index/chatham-financial/](../../pages/openai.com/index/chatham-financial/index.md) | October 2, 2026 | Chatham scales its capital markets expertise with OpenAI | 2026-11-17T23:47:50.584Z |
| [/index/check-point-daybreak/](../../pages/openai.com/index/check-point-daybreak/index.md) | October 27, 2026 | How Check Point accelerates vulnerability research with Daybreak | 2026-11-17T23:56:13.478Z |
| [/index/children-first-declaration/](../../pages/openai.com/index/children-first-declaration/index.md) | November 12, 2026 | Supporting research on AI and children’s safety | 2026-11-18T22:02:58.331Z |
| [/index/cisco-cyber/](../../pages/openai.com/index/cisco-cyber/index.md) | November 3, 2026 | How Cisco defends at machine speed with OpenAI | 2026-11-18T13:50:49.707Z |
| [/index/closing-ai-guidance-gap-education/](../../pages/openai.com/index/closing-ai-guidance-gap-education/index.md) | November 10, 2026 | Closing the AI guidance gap in education | 2026-11-18T13:50:28.260Z |
| [/index/cloudflare-cyber/](../../pages/openai.com/index/cloudflare-cyber/index.md) | October 21, 2026 | Cloudflare links vulnerability discovery to defense with OpenAI | 2026-11-17T23:56:16.824Z |
| [/index/coderabbit-codex-daybreak/](../../pages/openai.com/index/coderabbit-codex-daybreak/index.md) | November 9, 2026 | CodeRabbit scales agentic software development and ships 20x more | 2026-11-18T13:50:38.228Z |
| [/index/cogent-security/](../../pages/openai.com/index/cogent-security/index.md) | November 10, 2026 | Cogent and OpenAI build cyber defense factories for enterprises | 2026-11-19T12:48:41.789Z |
| [/index/combatting-adversarial-distillation/](../../pages/openai.com/index/combatting-adversarial-distillation/index.md) | November 20, 2026 | Combatting adversarial distillation | 2026-11-22T02:12:42.956Z |
| [/index/community-safety-report-and-new-protections-for-teens/](../../pages/openai.com/index/community-safety-report-and-new-protections-for-teens/index.md) | October 30, 2026 | Community safety report and new protections for teens | 2026-11-18T13:50:44.713Z |
| [/index/control-room/](../../pages/openai.com/index/control-room/index.md) |  | Control Room | 2026-11-18T13:50:29.278Z |
| [/index/coordinated-disclosure-of-critical-vulnerabilities/](../../pages/openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/index.md) | October 21, 2026 | Patch the Planet: global response coordination as agents uncover critical vulnerabilities | 2026-11-18T19:25:29.574Z |
| [/index/credit-saison/](../../pages/openai.com/index/credit-saison/index.md) | October 29, 2026 | Credit Saison achieves 954% ROI in a ChatGPT Enterprise pilot | 2026-11-18T13:50:48.818Z |
| [/index/cultfit-builds-with-codex/](../../pages/openai.com/index/cultfit-builds-with-codex/index.md) | November 5, 2026 | Cult.fit builds operational muscle with Codex | 2026-11-17T23:56:10.470Z |
| [/index/dan-driscoll-joins-openai/](../../pages/openai.com/index/dan-driscoll-joins-openai/index.md) | November 2, 2026 | OpenAI appoints Dan Driscoll as Senior Counselor for National Security Modernization | 2026-11-18T13:50:30.632Z |
| [/index/daybreak-red-aws-govcloud/](../../pages/openai.com/index/daybreak-red-aws-govcloud/index.md) | November 4, 2026 | Daybreak Red is now available in AWS GovCloud (US-East) | 2026-11-18T19:25:23.085Z |
| [/index/decisions-api/](../../pages/openai.com/index/decisions-api/index.md) | October 22, 2026 | Build more responsive apps with the Decisions API | 2026-11-17T23:03:04.105Z |
| [/index/devday-2026-recap/](../../pages/openai.com/index/devday-2026-recap/index.md) | September 29, 2026 | DevDay 2026 Recap | 2026-11-17T23:03:04.946Z |
| [/index/devrev-enterprise-self-service/](../../pages/openai.com/index/devrev-enterprise-self-service/index.md) | November 4, 2026 | DevRev delivers autonomous self-service with GPT‑6.1 Sol | 2026-11-17T21:23:44.193Z |
| [/index/disrupting-a-coordinated-model-distillation-campaign/](../../pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md) | September 30, 2026 | Disrupting a coordinated model-distillation campaign | 2026-11-18T19:25:45.738Z |
| [/index/disrupting-ai-enabled-false-front-operations/](../../pages/openai.com/index/disrupting-ai-enabled-false-front-operations/index.md) | October 8, 2026 | Disrupting AI-enabled “false front” operations | 2026-11-14T12:44:47.566Z |
| [/index/empowering-cyber-defenders/](../../pages/openai.com/index/empowering-cyber-defenders/index.md) | October 21, 2026 | Democratic governance of frontier AI, part II: Empowering cyber defenders | 2026-11-18T19:25:15.873Z |
| [/index/eu-text-provenance/](../../pages/openai.com/index/eu-text-provenance/index.md) | October 5, 2026 | Our approach to EU text provenance rules | 2026-11-14T12:44:33.112Z |
| [/index/expanding-chatgpt-for-academic-researchers/](../../pages/openai.com/index/expanding-chatgpt-for-academic-researchers/index.md) |  | Broadening access to AI for scientists | 2026-11-19T14:30:24.721Z |
| [/index/fair-use-benefits-everyone/](../../pages/openai.com/index/fair-use-benefits-everyone/index.md) | October 30, 2026 | Fair use benefits everyone | 2026-11-18T20:43:04.752Z |
| [/index/fanatics-streamline-fan-experience/](../../pages/openai.com/index/fanatics-streamline-fan-experience/index.md) | October 26, 2026 | How Fanatics and OpenAI streamline the fan experience | 2026-11-18T13:50:46.828Z |
| [/index/forward-deployed-engineering-means/](../../pages/openai.com/index/forward-deployed-engineering-means/index.md) | October 22, 2026 | What FDE means at OpenAI | 2026-11-18T13:50:45.455Z |
| [/index/franklin-templeton/](../../pages/openai.com/index/franklin-templeton/index.md) | November 5, 2026 | Franklin Templeton uses OpenAI to support investment research | 2026-11-17T23:56:22.141Z |
| [/index/gilbert-tobin-sam-nickless/](../../pages/openai.com/index/gilbert-tobin-sam-nickless/index.md) | November 12, 2026 | Gilbert + Tobin rethinks the business of law with AI | 2026-11-17T23:56:10.486Z |
| [/index/gpt-6-1-sol-coderabbit-code-security/](../../pages/openai.com/index/gpt-6-1-sol-coderabbit-code-security/index.md) | October 26, 2026 | GPT‑6.1 Sol helps CodeRabbit strengthen security across complex codebases | 2026-11-18T19:25:39.202Z |
| [/index/gpt-6-for-everyone/](../../pages/openai.com/index/gpt-6-for-everyone/index.md) | October 7, 2026 | GPT‑6 and Intelligent UI for everyone | 2026-11-18T13:50:31.311Z |
| [/index/greptile-code-review-codex-astra/](../../pages/openai.com/index/greptile-code-review-codex-astra/index.md) | October 26, 2026 | Greptile takes bug detection beyond code review with GPT‑6 Astra | 2026-11-17T23:47:50.116Z |
| [/index/grid-protectors-program/](../../pages/openai.com/index/grid-protectors-program/index.md) | November 2, 2026 | Introducing the Grid Protectors Program | 2026-11-18T13:50:34.309Z |
| [/index/grupo-boticario/](../../pages/openai.com/index/grupo-boticario/index.md) | October 16, 2026 | How Grupo Boticário uses AI to strengthen human connections | 2026-11-17T23:56:14.973Z |
| [/index/heimstaden/](../../pages/openai.com/index/heimstaden/index.md) | November 3, 2026 | Heimstaden is changing residential real estate management with AI | 2026-11-17T23:47:48.485Z |
| [/index/helping-caregivers-use-ai-in-everyday-life/](../../pages/openai.com/index/helping-caregivers-use-ai-in-everyday-life/index.md) | November 10, 2026 | Helping caregivers use AI in everyday life | 2026-11-18T13:50:29.143Z |
| [/index/helping-small-businesses-put-ai-to-work/](../../pages/openai.com/index/helping-small-businesses-put-ai-to-work/index.md) | September 30, 2026 | Helping small businesses put AI to work | 2026-11-18T13:50:47.422Z |
| [/index/helping-websites-express-ai-training-preferences/](../../pages/openai.com/index/helping-websites-express-ai-training-preferences/index.md) | October 30, 2026 | Making it easier for websites to express AI training preferences | 2026-11-18T13:50:57.749Z |
| [/index/higgsfield-longer-videos-voice/](../../pages/openai.com/index/higgsfield-longer-videos-voice/index.md) | October 13, 2026 | Higgsfield takes AI video from 1 minute to over 10 | 2026-11-08T12:34:11.547Z |
| [/index/how-openai-performance-factory-keeps-chatgpt-fast/](../../pages/openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/index.md) | November 19, 2026 | How OpenAI’s Performance Factory keeps ChatGPT fast | 2026-11-21T20:57:30.470Z |
| [/index/how-we-detect-frontier-model-misalignment/](../../pages/openai.com/index/how-we-detect-frontier-model-misalignment/index.md) | October 29, 2026 | How we detect frontier model misalignment | 2026-11-18T19:25:34.011Z |
| [/index/how-we-will-do-better-for-australia/](../../pages/openai.com/index/how-we-will-do-better-for-australia/index.md) | September 28, 2026 | How we will do better for Australia | 2026-11-14T12:44:25.389Z |
| [/index/inside-the-codex-sandbox/](../../pages/openai.com/index/inside-the-codex-sandbox/index.md) | November 18, 2026 | Inside the Codex sandbox | 2026-11-21T12:38:02.824Z |
| [/index/introducing-businesses-chatgpt/](../../pages/openai.com/index/introducing-businesses-chatgpt/index.md) | November 10, 2026 | Introducing Businesses in ChatGPT | 2026-11-18T13:50:58.582Z |
| [/index/introducing-chatgpt-for-sales/](../../pages/openai.com/index/introducing-chatgpt-for-sales/index.md) | November 17, 2026 | Introducing ChatGPT for Sales | 2026-11-21T17:07:34.697Z |
| [/index/introducing-chatgpt-wallet/](../../pages/openai.com/index/introducing-chatgpt-wallet/index.md) | November 13, 2026 | Introducing ChatGPT Wallet | 2026-11-20T00:20:46.705Z |
| [/index/introducing-dots/](../../pages/openai.com/index/introducing-dots/index.md) | September 29, 2026 | Introducing dots | 2026-11-18T13:50:34.433Z |
| [/index/introducing-gpt-6-1-sol/](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md) |  | GPT-6.1Sol | — |
| [/index/introducing-gpt-6-1-terra/](../../pages/openai.com/index/introducing-gpt-6-1-terra/index.md) |  | GPT-6.1Terra | — |
| [/index/introducing-gpt-6-2-astra-sol/](../../pages/openai.com/index/introducing-gpt-6-2-astra-sol/index.md) |  | Introducing GPT-6.2 Astra and Sol | — |
| [/index/introducing-gpt-6-cyber/](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md) | November 5, 2026 | GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents | 2026-11-19T00:11:21.273Z |
| [/index/introducing-images-2-6/](../../pages/openai.com/index/introducing-images-2-6/index.md) | November 4, 2026 | Introducing Images 2.6Introducing Images 2.6 | 2026-11-18T13:50:26.807Z |
| [/index/introducing-medchembench/](../../pages/openai.com/index/introducing-medchembench/index.md) | November 20, 2026 | Can AI help scientists identify promising drug candidates? | 2026-11-22T07:08:42.890Z |
| [/index/introducing-openai-for-chile/](../../pages/openai.com/index/introducing-openai-for-chile/index.md) | November 17, 2026 | Introducing OpenAI for Chile | 2026-11-21T06:06:47.569Z |
| [/index/introducing-the-rosalind-academic-plan/](../../pages/openai.com/index/introducing-the-rosalind-academic-plan/index.md) | October 15, 2026 | Bringing GPT‑Rosalind to academic research labs | 2026-11-17T23:03:02.690Z |
| [/index/itau-generative-ai/](../../pages/openai.com/index/itau-generative-ai/index.md) | October 16, 2026 | How Itaú is building generative AI for its entire customer base | 2026-11-17T23:56:13.055Z |
| [/index/jill-hazelbaker-chief-corporate-affairs-officer/](../../pages/openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer/index.md) | November 3, 2026 | OpenAI appoints Jill Hazelbaker as Chief Corporate Affairs Officer | 2026-11-18T13:51:01.716Z |
| [/index/jiostar-vijay-seshadri/](../../pages/openai.com/index/jiostar-vijay-seshadri/index.md) | November 11, 2026 | JioStar’s chief architect on AI discovery at 500M-user scale | 2026-11-19T15:02:32.747Z |
| [/index/jump-trading/](../../pages/openai.com/index/jump-trading/index.md) | October 6, 2026 | How Jump Trading is scaling quant research with ChatGPT | 2026-11-17T23:48:08.211Z |
| [/index/kuken/](../../pages/openai.com/index/kuken/index.md) | November 9, 2026 | Kuken Industries searches 70 years of drawings in minutes | 2026-11-17T23:48:31.937Z |
| [/index/le-groupe-figaro-and-openai-announce-partnership/](../../pages/openai.com/index/le-groupe-figaro-and-openai-announce-partnership/index.md) | November 18, 2026 | Le Groupe Figaro and OpenAI partner to bring Le Figaro journalism to ChatGPT | 2026-11-20T00:59:42.000Z |
| [/index/legalon-halves-codex-costs/](../../pages/openai.com/index/legalon-halves-codex-costs/index.md) | October 8, 2026 | LegalOn halves Codex costs while maintaining development speed | 2026-11-08T12:34:14.835Z |
| [/index/legora/](../../pages/openai.com/index/legora/index.md) | October 28, 2026 | Legora is building the agentic operating system for legal work | 2026-11-18T01:53:20.946Z |
| [/index/lenfest-ai-collaborative-expansion/](../../pages/openai.com/index/lenfest-ai-collaborative-expansion/index.md) | September 28, 2026 | The Lenfest Institute grows landmark program with expanded OpenAI support | 2026-11-13T22:12:49.844Z |
| [/index/lifeval/](../../pages/openai.com/index/lifeval/index.md) | November 2, 2026 | LifeVal | 2026-11-19T10:57:14.656Z |
| [/index/localiza-generative-ai/](../../pages/openai.com/index/localiza-generative-ai/index.md) | October 16, 2026 | How Localiza reorganized work around generative AI | 2026-11-17T23:56:15.617Z |
| [/index/low-resource-programming-languages/](../../pages/openai.com/index/low-resource-programming-languages/index.md) | October 19, 2026 | ![](/_next/static/immutable/media/lab.44a_dymau51y3.webp)[ COBOL ]![](data:image/svg+xml,%3Csvg%20preserveAspe | 2026-11-08T12:36:25.252Z |
| [/index/lvmh-media-division-partnership/](../../pages/openai.com/index/lvmh-media-division-partnership/index.md) | November 16, 2026 | LVMH’s Media Division announces strategic partnership with OpenAI | 2026-11-18T23:09:11.679Z |
| [/index/managing-frontier-ai-risk/](../../pages/openai.com/index/managing-frontier-ai-risk/index.md) |  | Managing frontier AI risk: From training to deployment | 2026-11-21T21:15:35.374Z |
| [/index/measuring-how-ai-agents-handle-wet-lab-science/](../../pages/openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/index.md) | November 6, 2026 | Measuring how AI agents handle everyday wet-lab science | 2026-11-19T18:03:17.774Z |
| [/index/merge-builds-with-openai/](../../pages/openai.com/index/merge-builds-with-openai/index.md) | November 5, 2026 | Merge builds product and business tools with OpenAI technology | 2026-11-17T21:23:41.744Z |
| [/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare/](../../pages/openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare/index.md) | November 16, 2026 | More ways to move care forward with ChatGPT for Healthcare | 2026-11-21T15:01:13.452Z |
| [/index/new-chatgpt-ads-format-and-measurement/](../../pages/openai.com/index/new-chatgpt-ads-format-and-measurement/index.md) | October 5, 2026 | Building advertising for the way people use AI | 2026-11-17T23:03:00.491Z |
| [/index/openai-cut-incident-investigation/](../../pages/openai.com/index/openai-cut-incident-investigation/index.md) | October 26, 2026 | How Ultrafast cut incident investigation from hours to minutes at OpenAI | 2026-11-18T13:51:07.806Z |
| [/index/openai-models-google-cloud/](../../pages/openai.com/index/openai-models-google-cloud/index.md) | October 21, 2026 | OpenAI models are coming to Google Cloud | 2026-11-13T20:19:43.626Z |
| [/index/openai-nask-ai-safety-security-partnership/](../../pages/openai.com/index/openai-nask-ai-safety-security-partnership/index.md) | October 23, 2026 | OpenAI and Poland’s NASK partner to advance AI safety and security | 2026-11-10T21:22:01.914Z |
| [/index/openai-servicenow-partnership-expansion/](../../pages/openai.com/index/openai-servicenow-partnership-expansion/index.md) | October 28, 2026 | OpenAI and ServiceNow expand partnership across enterprise workflows | 2026-11-18T13:50:35.818Z |
| [/index/openai-to-acquire-orchestra-bio/](../../pages/openai.com/index/openai-to-acquire-orchestra-bio/index.md) | October 20, 2026 | OpenAI acquires Orchestra Bio | 2026-11-10T09:52:32.274Z |
| [/index/openai-to-acquire-pierre/](../../pages/openai.com/index/openai-to-acquire-pierre/index.md) | November 4, 2026 | OpenAI to acquire Pierre Computer Company, Inc. | 2026-11-18T13:50:33.866Z |
| [/index/oracle-apps-in-chatgpt/](../../pages/openai.com/index/oracle-apps-in-chatgpt/index.md) | October 27, 2026 | OpenAI expands partnership with Oracle to bring its apps to ChatGPT | 2026-11-18T13:51:02.309Z |
| [/index/oracle/](../../pages/openai.com/index/oracle/index.md) | October 8, 2026 | How Oracle turns days of work into minutes with ChatGPT and Codex | 2026-11-17T23:56:14.363Z |
| [/index/our-first-phase-of-embedded-assessments/](../../pages/openai.com/index/our-first-phase-of-embedded-assessments/index.md) | November 16, 2026 | Our first phase of embedded assessments | 2026-11-22T08:31:02.816Z |
| [/index/our-new-blog-for-science/](../../pages/openai.com/index/our-new-blog-for-science/index.md) | November 15, 2026 | Our new blog for science | 2026-11-18T13:51:18.717Z |
| [/index/partnering-with-hacktron/](../../pages/openai.com/index/partnering-with-hacktron/index.md) | November 6, 2026 | Partnering with Hacktron to find vulnerabilities in OpenAI’s systems | 2026-11-18T19:25:31.000Z |
| [/index/pollo-ai/](../../pages/openai.com/index/pollo-ai/index.md) | October 8, 2026 | Pollo AI turns creative ideas into campaigns with OpenAI | 2026-11-03T21:40:31.085Z |
| [/index/practical-guide-building-gpt-6/](../../pages/openai.com/index/practical-guide-building-gpt-6/index.md) | October 2, 2026 | A model guide for the GPT‑6 family | 2026-11-18T13:50:28.768Z |
| [/index/preparing-our-next-security-sprint-to-harden-openai/](../../pages/openai.com/index/preparing-our-next-security-sprint-to-harden-openai/index.md) | November 2, 2026 | Preparing our next security sprint to harden OpenAI | 2026-11-18T19:25:14.823Z |
| [/index/qodo-codex-plugin/](../../pages/openai.com/index/qodo-codex-plugin/index.md) | November 2, 2026 | Qodo builds context into AI code review with Codex | 2026-11-17T21:23:45.633Z |
| [/index/radisson/](../../pages/openai.com/index/radisson/index.md) | October 7, 2026 | Radisson Hotel Group brings hotel discovery into ChatGPT | 2026-11-18T01:53:22.768Z |
| [/index/research-acceleration-jagged-frontier/](../../pages/openai.com/index/research-acceleration-jagged-frontier/index.md) | November 18, 2026 | Research acceleration: The jagged frontier | — |
| [/index/rewarding-defenders-with-bigger-bug-bounties/](../../pages/openai.com/index/rewarding-defenders-with-bigger-bug-bounties/index.md) | November 2, 2026 | Rewarding defenders with bigger bug bounties | 2026-11-18T19:25:26.462Z |
| [/index/ropes-gray-ai-diligence/](../../pages/openai.com/index/ropes-gray-ai-diligence/index.md) | October 29, 2026 | How Ropes & Gray is developing AI for transactional diligence | 2026-11-17T23:56:24.773Z |
| [/index/scaling-ai-research-for-complex-biological-data/](../../pages/openai.com/index/scaling-ai-research-for-complex-biological-data/index.md) | October 21, 2026 | Using thousands of AI agents to uncover new leads in biological data | 2026-11-12T22:13:46.797Z |
| [/index/scaling-git-at-openai/](../../pages/openai.com/index/scaling-git-at-openai/index.md) | November 2, 2026 | Scaling Git at OpenAI | 2026-11-18T13:50:39.783Z |
| [/index/scaling-storage-one-billion-users-part-two/](../../pages/openai.com/index/scaling-storage-one-billion-users-part-two/index.md) | October 23, 2026 | Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II) | 2026-11-18T13:50:35.125Z |
| [/index/science-at-the-frontier/](../../pages/openai.com/index/science-at-the-frontier/index.md) | November 16, 2026 | Science at the frontier | 2026-11-20T21:31:49.629Z |
| [/index/securing-our-frontier-model-training-environment/](../../pages/openai.com/index/securing-our-frontier-model-training-environment/index.md) | October 23, 2026 | Securing our frontier model training environment | 2026-11-18T19:25:29.330Z |
| [/index/sentinelone/](../../pages/openai.com/index/sentinelone/index.md) | October 14, 2026 | SentinelOne cuts malware analysis from weeks to hours | 2026-11-17T23:56:25.207Z |
| [/index/setting-new-standard-responsible-ai-infrastructure/](../../pages/openai.com/index/setting-new-standard-responsible-ai-infrastructure/index.md) | November 5, 2026 | Setting a new standard for responsible AI infrastructure | 2026-11-18T13:50:27.255Z |
| [/index/sharing-ai-progress-in-mathematics/](../../pages/openai.com/index/sharing-ai-progress-in-mathematics/index.md) | October 6, 2026 | Sharing AI progress in mathematics | 2026-11-08T12:36:54.139Z |
| [/index/singapore-airlines-travel-work/](../../pages/openai.com/index/singapore-airlines-travel-work/index.md) | November 10, 2026 | Singapore Airlines elevates travel & work with OpenAI technology | 2026-11-18T13:50:28.409Z |
| [/index/sophos/](../../pages/openai.com/index/sophos/index.md) | October 9, 2026 | Sophos cuts threat investigation time by 96% with OpenAI Daybreak | 2026-11-18T01:53:36.071Z |
| [/index/stack-overflow-chatgpt-plugin/](../../pages/openai.com/index/stack-overflow-chatgpt-plugin/index.md) | October 16, 2026 | Stack Overflow for Agents triples signups with ChatGPT plugin | 2026-11-16T20:47:47.209Z |
| [/index/step-toward-defining-the-standard-model/](../../pages/openai.com/index/step-toward-defining-the-standard-model/index.md) | November 15, 2026 | A step toward defining the Standard Model on a lattice | 2026-11-19T13:20:29.481Z |
| [/index/strengthening-nato-allied-cyber-defences-ai/](../../pages/openai.com/index/strengthening-nato-allied-cyber-defences-ai/index.md) | November 17, 2026 | Strengthening NATO and allied cyber defenses with AI | 2026-11-18T13:52:44.653Z |
| [/index/strengthening-online-child-safety/](../../pages/openai.com/index/strengthening-online-child-safety/index.md) | November 16, 2026 | Strengthening the fight against online child sexual abuse with new tools and support | 2026-11-21T19:03:17.887Z |
| [/index/sullivan-cromwell/](../../pages/openai.com/index/sullivan-cromwell/index.md) | October 15, 2026 | Sullivan & Cromwell brings legal expertise into agreement review | 2026-11-17T23:56:48.921Z |
| [/index/teaching-students-to-think-and-learn-through-questions/](../../pages/openai.com/index/teaching-students-to-think-and-learn-through-questions/index.md) | October 15, 2026 | Teaching students to think and learn through questions | 2026-10-22T09:45:56.774Z |
| [/index/ted-taylor-restaurant/](../../pages/openai.com/index/ted-taylor-restaurant/index.md) | October 20, 2026 | Franchisee reconciles cash in 94% less time with ChatGPT Work | 2026-11-17T23:47:50.141Z |
| [/index/teens-learn-and-plan/](../../pages/openai.com/index/teens-learn-and-plan/index.md) | October 7, 2026 | Helping teens learn, plan, and shape the future of AI | 2026-11-18T13:50:36.265Z |
| [/index/terminal-x/](../../pages/openai.com/index/terminal-x/index.md) | October 20, 2026 | Terminal X matches senior investor judgment 88.6% with GPT‑6.1 | 2026-11-17T23:08:13.597Z |
| [/index/the-den-family-social/](../../pages/openai.com/index/the-den-family-social/index.md) | October 1, 2026 | The Den frees up 10-15 hours a week to grow with ChatGPT Work | 2026-11-17T23:47:50.567Z |
| [/index/the-eternal-complement/](../../pages/openai.com/index/the-eternal-complement/index.md) |  | The eternal complement | 2026-11-13T22:12:53.716Z |
| [/index/the-eus-next-chapter-in-ai-is-agentic/](../../pages/openai.com/index/the-eus-next-chapter-in-ai-is-agentic/index.md) | October 14, 2026 | The EU’s next chapter in AI is agentic | 2026-11-10T08:37:51.241Z |
| [/index/the-future-of-the-firm/](../../pages/openai.com/index/the-future-of-the-firm/index.md) |  | The future of the firm | 2026-11-18T13:50:32.894Z |
| [/index/the-kings-trust-and-openai/](../../pages/openai.com/index/the-kings-trust-and-openai/index.md) | November 16, 2026 | The King’s Trust and OpenAI launch £1m partnership | 2026-11-18T13:50:47.144Z |
| [/index/the-silent-consensus/](../../pages/openai.com/index/the-silent-consensus/index.md) | November 18, 2026 | The Silent Consensus | 2026-11-21T01:32:19.248Z |
| [/index/third-moment-research/](../../pages/openai.com/index/third-moment-research/index.md) | October 14, 2026 | How Third Moment Research runs 10,000 agents for 36+ hours | 2026-11-16T20:47:47.580Z |
| [/index/towards-safety-cases-for-frontier-ai-training/](../../pages/openai.com/index/towards-safety-cases-for-frontier-ai-training/index.md) | September 28, 2026 | Towards safety cases for frontier AI training | 2026-11-03T18:06:47.269Z |
| [/index/uber-chatgpt-work-rollout/](../../pages/openai.com/index/uber-chatgpt-work-rollout/index.md) | October 22, 2026 | Uber brings ChatGPT Work to all employees with OpenAI | 2026-11-18T13:50:46.465Z |
| [/index/updated-model-spec/](../../pages/openai.com/index/updated-model-spec/index.md) | October 29, 2026 | An updated Model Spec for more capable and beneficial AI | 2026-11-14T12:44:49.985Z |
| [/news/science/](../../pages/openai.com/news/science/index.md) |  | Science | 2026-11-18T13:30:17.320Z |
| [/policies/brazil-advertising-terms/](../../pages/openai.com/policies/brazil-advertising-terms/index.md) |  | Brazil Advertising Terms | 2026-10-26T07:27:13.757Z |
| [/policies/business-agents-policy/](../../pages/openai.com/policies/business-agents-policy/index.md) |  | Business Agents Policy | 2026-11-16T22:15:57.792Z |
| [/policies/businesses-in-chatgpt-terms/](../../pages/openai.com/policies/businesses-in-chatgpt-terms/index.md) |  | Businesses in ChatGPT Terms | 2026-11-20T08:55:10.894Z |
| [/policies/businesses-in-chatgpt/](../../pages/openai.com/policies/businesses-in-chatgpt/index.md) |  | Businesses in ChatGPT | 2026-11-19T07:57:17.132Z |
| [/policies/chatgpt-wallet-privacy-notice/](../../pages/openai.com/policies/chatgpt-wallet-privacy-notice/index.md) |  | ChatGPT Wallet Privacy Notice | 2026-11-16T21:10:44.396Z |
| [/policies/chatgpt-wallet-terms/](../../pages/openai.com/policies/chatgpt-wallet-terms/index.md) |  | ChatGPT Wallet terms | 2026-11-19T10:04:19.603Z |
| [/policies/marketplace-customer-program-terms/](../../pages/openai.com/policies/marketplace-customer-program-terms/index.md) |  | OpenAI Marketplace Customer Program Terms | 2026-11-16T23:10:54.552Z |
| [/policies/row-privacy-policy/](../../pages/openai.com/policies/row-privacy-policy/index.md) |  | Privacy policy | 2026-11-03T12:13:38.478Z |
| [/policies/sign-in-with-chatgpt-terms/](../../pages/openai.com/policies/sign-in-with-chatgpt-terms/index.md) |  | Sign in with ChatGPT Terms | 2026-11-09T20:29:22.098Z |
| [/proud-partner/](../../pages/openai.com/proud-partner/index.md) |  | Proud Partner of people with big ideas | 2026-11-17T18:29:02.990Z |
| [/safety-alignment/](../../pages/openai.com/safety-alignment/index.md) |  | Research and releases | — |
| [/safety-alignment/accidental-cot-grading/](../../pages/openai.com/safety-alignment/accidental-cot-grading/index.md) |  | Investigating the consequences of accidentally grading CoT during RL | — |
| [/safety-alignment/ai-discovered-unknowns/](../../pages/openai.com/safety-alignment/ai-discovered-unknowns/index.md) |  | Discovering unknown AI misalignments in real-world usage | — |
| [/safety-alignment/argo/](../../pages/openai.com/safety-alignment/argo/index.md) |  | Interpreting Black Box Reward Models | — |
| [/safety-alignment/auto-review/](../../pages/openai.com/safety-alignment/auto-review/index.md) |  | Auto-review of agent actions without synchronous human oversight | — |
| [/safety-alignment/beneficial-rl/](../../pages/openai.com/safety-alignment/beneficial-rl/index.md) |  | Reinforcement learning towards broadly and persistently beneficial models | — |
| [/safety-alignment/beyond-gmean-squared/](../../pages/openai.com/safety-alignment/beyond-gmean-squared/index.md) |  | Beyond g-mean²: complementary metrics for monitorability | — |
| [/safety-alignment/confessions/](../../pages/openai.com/safety-alignment/confessions/index.md) |  | Why We Are Excited About Confessions | — |
| [/safety-alignment/cot-monitorability-model-lifecycle/](../../pages/openai.com/safety-alignment/cot-monitorability-model-lifecycle/index.md) |  | What affects chain-of-thought monitorability across the model lifecycle? | — |
| [/safety-alignment/coval/](../../pages/openai.com/safety-alignment/coval/index.md) |  | CoVal: Learning values-aware rubrics from the crowd | — |
| [/safety-alignment/eval-production-behavior-gap/](../../pages/openai.com/safety-alignment/eval-production-behavior-gap/index.md) |  | Eval-production behavior gaps in agent safety and the role of eval-awareness | — |
| [/safety-alignment/fuzzy-robustness/](../../pages/openai.com/safety-alignment/fuzzy-robustness/index.md) |  | Improving Fuzzy Robustness in LLM Safety with Automated Red Teaming | — |
| [/safety-alignment/hello-world/](../../pages/openai.com/safety-alignment/hello-world/index.md) |  | Hello World | — |
| [/safety-alignment/helpful-assistant-features/](../../pages/openai.com/safety-alignment/helpful-assistant-features/index.md) |  | Helpful assistant features suppress emergent misalignment | — |
| [/safety-alignment/how-far-does-alignment-midtraining-generalize/](../../pages/openai.com/safety-alignment/how-far-does-alignment-midtraining-generalize/index.md) |  | How far does alignment midtraining generalize? | — |
| [/safety-alignment/how-we-detect-frontier-model-misalignment/](../../pages/openai.com/safety-alignment/how-we-detect-frontier-model-misalignment/index.md) |  | How we detect frontier model misalignment | — |
| [/safety-alignment/laser/](../../pages/openai.com/safety-alignment/laser/index.md) |  | Meet LASER: Recursive sampling for safer conversations | — |
| [/safety-alignment/measuring-reward-seeking/](../../pages/openai.com/safety-alignment/measuring-reward-seeking/index.md) |  | Measuring Reward-Seeking by Instilling Contrastive Beliefs | — |
| [/safety-alignment/metagaming-latents/](../../pages/openai.com/safety-alignment/metagaming-latents/index.md) |  | Studying metagaming latents in language models | — |
| [/safety-alignment/metagaming/](../../pages/openai.com/safety-alignment/metagaming/index.md) |  | Metagaming matters for training, evaluation, and oversight | — |
| [/safety-alignment/misalignment-reports/](../../pages/openai.com/safety-alignment/misalignment-reports/index.md) |  | Misalignment reports and notices | — |
| [/safety-alignment/misalignment-reports/accessing-and-changing-internal-systems-during-dashboard-research/](../../pages/openai.com/safety-alignment/misalignment-reports/accessing-and-changing-internal-systems-during-dashboard-research/index.md) |  | Accessing and changing internal systems during dashboard research | — |
| [/safety-alignment/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/](../../pages/openai.com/safety-alignment/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/index.md) |  | An agent used DNS to reach an external chatbot | — |
| [/safety-alignment/misalignment-reports/bypassing-network-restrictions-during-a-coding-evaluation/](../../pages/openai.com/safety-alignment/misalignment-reports/bypassing-network-restrictions-during-a-coding-evaluation/index.md) |  | Bypassing network restrictions during a coding evaluation | — |
| [/safety-alignment/misalignment-reports/circumventing-internet-restrictions-through-an-external-browser/](../../pages/openai.com/safety-alignment/misalignment-reports/circumventing-internet-restrictions-through-an-external-browser/index.md) |  | Circumventing internet restrictions through an external browser | — |
| [/safety-alignment/misalignment-reports/command-injecting-a-reference-tool-to-copy-a-source-file/](../../pages/openai.com/safety-alignment/misalignment-reports/command-injecting-a-reference-tool-to-copy-a-source-file/index.md) |  | Command injecting a reference tool to copy a source file | — |
| [/safety-alignment/misalignment-reports/covert-underperformance-on-safety-research-tasks/](../../pages/openai.com/safety-alignment/misalignment-reports/covert-underperformance-on-safety-research-tasks/index.md) |  | Covert underperformance on safety research tasks | — |
| [/safety-alignment/misalignment-reports/damaging-the-task-environment-to-trigger-a-reset/](../../pages/openai.com/safety-alignment/misalignment-reports/damaging-the-task-environment-to-trigger-a-reset/index.md) |  | Damaging the task environment to trigger a reset | — |
| [/safety-alignment/misalignment-reports/encouraging-deception-in-compaction-summaries/](../../pages/openai.com/safety-alignment/misalignment-reports/encouraging-deception-in-compaction-summaries/index.md) |  | Encouraging deception in compaction summaries | — |
| [/safety-alignment/misalignment-reports/exposing-a-github-token-in-a-public-repository/](../../pages/openai.com/safety-alignment/misalignment-reports/exposing-a-github-token-in-a-public-repository/index.md) |  | Exposing a GitHub token in a public repository | — |
| [/safety-alignment/misalignment-reports/generating-scripts-to-copy-outgoing-email-to-an-unauthorized-address/](../../pages/openai.com/safety-alignment/misalignment-reports/generating-scripts-to-copy-outgoing-email-to-an-unauthorized-address/index.md) |  | Generating scripts to copy outgoing email to an unauthorized address | — |
| [/safety-alignment/misalignment-reports/obtaining-public-statistics-with-disallowed-requests/](../../pages/openai.com/safety-alignment/misalignment-reports/obtaining-public-statistics-with-disallowed-requests/index.md) |  | Obtaining public statistics with disallowed requests | — |
| [/safety-alignment/misalignment-reports/preparing-for-a-restart-after-reading-slack/](../../pages/openai.com/safety-alignment/misalignment-reports/preparing-for-a-restart-after-reading-slack/index.md) |  | Preparing for a restart after reading Slack | — |
| [/safety-alignment/misalignment-reports/reaching-an-internal-eda-host-through-a-reference-tool/](../../pages/openai.com/safety-alignment/misalignment-reports/reaching-an-internal-eda-host-through-a-reference-tool/index.md) |  | Reaching an internal EDA host through a reference tool | — |
| [/safety-alignment/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/](../../pages/openai.com/safety-alignment/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/index.md) |  | Retrieving server secrets and bypassing authorization on a government statistics website | — |
| [/safety-alignment/misalignment-reports/searching-github-for-leaked-api-keys/](../../pages/openai.com/safety-alignment/misalignment-reports/searching-github-for-leaked-api-keys/index.md) |  | Signing up for disposable emails and searching GitHub for leaked API keys | — |
| [/safety-alignment/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/](../../pages/openai.com/safety-alignment/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/index.md) |  | Self-generated prompt injections in compaction summaries | — |
| [/safety-alignment/misalignment-reports/self-replicating-prompt-injections-exist/](../../pages/openai.com/safety-alignment/misalignment-reports/self-replicating-prompt-injections-exist/index.md) |  | Self-replicating prompt injections exist | — |
| [/safety-alignment/misalignment-reports/sending-disallowed-web-requests-and-reaching-a-public-file-service/](../../pages/openai.com/safety-alignment/misalignment-reports/sending-disallowed-web-requests-and-reaching-a-public-file-service/index.md) |  | Sending disallowed web requests and reaching a public file service | — |
| [/safety-alignment/misalignment-reports/stopping-a-running-alignment-evaluation/](../../pages/openai.com/safety-alignment/misalignment-reports/stopping-a-running-alignment-evaluation/index.md) |  | Stopping a running alignment evaluation | — |
| [/safety-alignment/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/](../../pages/openai.com/safety-alignment/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/index.md) |  | Suppressing misalignment monitoring alerts and disabling misalignment monitoring | — |
| [/safety-alignment/misalignment-reports/trying-to-prompt-inject-the-grader-in-filenames/](../../pages/openai.com/safety-alignment/misalignment-reports/trying-to-prompt-inject-the-grader-in-filenames/index.md) |  | Trying to prompt-inject the grader in filenames | — |
| [/safety-alignment/misalignment-reports/unauthorized-artifactory-writes-and-cross-sample-communication/](../../pages/openai.com/safety-alignment/misalignment-reports/unauthorized-artifactory-writes-and-cross-sample-communication/index.md) |  | Unsanctioned Artifactory writes and cross-sample communication | — |
| [/safety-alignment/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/](../../pages/openai.com/safety-alignment/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/index.md) |  | Unauthorized communication via temporary file hosting services | — |
| [/safety-alignment/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/](../../pages/openai.com/safety-alignment/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/index.md) |  | Uploading files to the internet in order to cite them | — |
| [/safety-alignment/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/](../../pages/openai.com/safety-alignment/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/index.md) |  | Using a funded test cryptocurrency wallet without authorization | — |
| [/safety-alignment/misalignment-reports/using-peers-work-to-gain-unauthorized-access-to-openai-research-infrastructure/](../../pages/openai.com/safety-alignment/misalignment-reports/using-peers-work-to-gain-unauthorized-access-to-openai-research-infrastructure/index.md) |  | Using peers’ work to gain unauthorized access to OpenAI research infrastructure | — |
| [/safety-alignment/model-spec-evals/](../../pages/openai.com/safety-alignment/model-spec-evals/index.md) |  | Introducing Model Spec Evals | — |
| [/safety-alignment/monitorability-evals/](../../pages/openai.com/safety-alignment/monitorability-evals/index.md) |  | Open Sourcing Monitorability Evaluations | — |
| [/safety-alignment/prod-evals/](../../pages/openai.com/safety-alignment/prod-evals/index.md) |  | Sidestepping Evaluation Awareness and Anticipating Misalignment with Production Evaluations | — |
| [/safety-alignment/sae-latent-attribution/](../../pages/openai.com/safety-alignment/sae-latent-attribution/index.md) |  | Debugging misaligned completions with sparse-autoencoder latent attribution | — |
| [/safety-alignment/safety-fellowship/](../../pages/openai.com/safety-alignment/safety-fellowship/index.md) |  | Introducing the OpenAI Safety Fellowship | — |
| [/safety-alignment/scaling-code-verification/](../../pages/openai.com/safety-alignment/scaling-code-verification/index.md) |  | A Practical Approach to Verifying Code at Scale | — |
| [/safety-alignment/self-incrimination/](../../pages/openai.com/safety-alignment/self-incrimination/index.md) |  | Training agents to self-report misbehavior | — |
| [/safety-alignment/training-activation-classifiers/](../../pages/openai.com/safety-alignment/training-activation-classifiers/index.md) |  | Training activation classifiers for safety and alignment | — |
| [/safety-alignment/validating-public-evals/](../../pages/openai.com/safety-alignment/validating-public-evals/index.md) |  | Can public chat data predict real-world AI misalignments? | — |
| [/science/researcher-access/](../../pages/openai.com/science/researcher-access/index.md) |  | Find the right plan or program for your research | 2026-11-21T09:26:57.587Z |
| [/supply/product/blossom-tee-gray/](../../pages/openai.com/supply/product/blossom-tee-gray/index.md) |  | Blossom Tee | — |
| [/supply/product/dots-tee/](../../pages/openai.com/supply/product/dots-tee/index.md) |  | Dots Tee | — |
| [/supply/product/dots-tote/](../../pages/openai.com/supply/product/dots-tote/index.md) |  | Dots Tote | — |
| [/supply/product/gpt-6-longsleeve/](../../pages/openai.com/supply/product/gpt-6-longsleeve/index.md) |  | GPT-6 Longsleeve | — |
| [/supply/product/modretro-chromatic-case-codex-edition/](../../pages/openai.com/supply/product/modretro-chromatic-case-codex-edition/index.md) |  | ModRetro Chromatic Case: Codex Edition | — |
| [/supply/product/modretro-codex-cartridge/](../../pages/openai.com/supply/product/modretro-codex-cartridge/index.md) |  | ModRetro Codex Cartridge | — |
| [/supply/product/theresetcompany-hoodie/](../../pages/openai.com/supply/product/theresetcompany-hoodie/index.md) |  | TheResetCompany Hoodie | — |

## Appendix B: updated pages with substantive changes (after removing template/recirculation noise)

Counts are distinct lines added/removed.

| URL | +lines | −lines | old `<lastmod>` → new |
|---|---|---|---|
| [/policies/cookie-policy/](../../pages/openai.com/policies/cookie-policy/index.md) | 106 | 81 | 2026-09-17T08:13:04.475Z → 2026-11-20T17:49:56.666Z |
| [/policies/supplier-code/](../../pages/openai.com/policies/supplier-code/index.md) | 110 | 72 | 2026-05-22T19:05:09.789Z → 2026-10-15T23:16:33.439Z |
| [/index/lowes/](../../pages/openai.com/index/lowes/index.md) | 52 | 73 | 2026-07-25T07:16:01.808Z → 2026-11-04T11:06:04.930Z |
| [/policies/ad-policies/](../../pages/openai.com/policies/ad-policies/index.md) | 50 | 61 | 2026-09-17T08:18:21.189Z → 2026-11-22T08:57:18.078Z |
| [/business/solutions/cybersecurity/](../../pages/openai.com/business/solutions/cybersecurity/index.md) | 51 | 60 | 2026-09-17T15:45:09.208Z → 2026-11-17T01:55:01.919Z |
| [/daybreak/](../../pages/openai.com/daybreak/index.md) | 26 | 82 | 2026-09-21T18:14:18.422Z → 2026-11-16T09:32:38.624Z |
| [/index/retell-ai/](../../pages/openai.com/index/retell-ai/index.md) | 59 | 37 | 2026-05-22T19:01:41.744Z → 2026-10-30T02:55:47.970Z |
| [/index/wayfair/](../../pages/openai.com/index/wayfair/index.md) | 40 | 47 | 2026-09-22T21:15:44.898Z → 2026-11-04T10:45:23.863Z |
| [/trust-and-transparency/](../../pages/openai.com/trust-and-transparency/index.md) | 40 | 33 | 2026-09-18T02:49:57.344Z → 2026-11-19T18:39:32.121Z |
| [/business/solutions/sales/](../../pages/openai.com/business/solutions/sales/index.md) | 38 | 28 | 2026-09-24T23:02:01.583Z → 2026-11-18T22:30:39.306Z |
| [/products/release-notes/](../../pages/openai.com/products/release-notes/index.md) | 24 | 40 | 2026-09-27T19:57:04.513Z → 2026-11-21T06:50:35.844Z |
| [/webmcp-challenge/](../../pages/openai.com/webmcp-challenge/index.md) | 25 | 38 | 2026-09-10T15:21:28.245Z → 2026-10-23T08:54:42.095Z |
| [/business/pricing/](../../pages/openai.com/business/pricing/index.md) | 44 | 19 | 2026-09-24T00:55:41.622Z → 2026-11-19T20:06:53.267Z |
| [/business/](../../pages/openai.com/business/index.md) | 49 | 6 | 2026-09-28T02:34:15.644Z → 2026-11-18T21:27:03.743Z |
| [/policies/usage-policies/](../../pages/openai.com/policies/usage-policies/index.md) | 32 | 15 | 2026-07-25T07:08:46.608Z → 2026-10-23T11:36:03.885Z |
| [/signals/data/](../../pages/openai.com/signals/data/index.md) | 24 | 22 | 2026-09-15T04:37:05.613Z → 2026-11-12T19:02:59.873Z |
| [/business/why-openai/small-business/](../../pages/openai.com/business/why-openai/small-business/index.md) | 26 | 16 | 2026-09-25T22:57:54.698Z → 2026-11-10T18:18:43.471Z |
| [/events/aws-reinvent/](../../pages/openai.com/events/aws-reinvent/index.md) | 37 | 5 | 2026-09-22T22:15:08.967Z → 2026-11-17T00:35:47.395Z |
| [/policies/health-privacy-policy/](../../pages/openai.com/policies/health-privacy-policy/index.md) | 20 | 21 | 2026-09-15T13:25:02.279Z → 2026-11-21T23:32:56.216Z |
| [/codex/](../../pages/openai.com/codex/index.md) | 28 | 11 | 2026-09-28T02:51:22.455Z → 2026-11-08T12:34:09.320Z |
| [/index/defining-and-evaluating-political-bias-in-llms/](../../pages/openai.com/index/defining-and-evaluating-political-bias-in-llms/index.md) | 28 | 10 | 2026-05-22T19:03:13.277Z → 2026-10-19T04:59:41.733Z |
| [/index/the-five-ai-value-models-driving-business-reinvention/](../../pages/openai.com/index/the-five-ai-value-models-driving-business-reinvention/index.md) | 1 | 36 | 2026-07-28T02:04:44.104Z → 2026-11-04T20:11:43.247Z |
| [/policies/privacy-policy/](../../pages/openai.com/policies/privacy-policy/index.md) | 17 | 18 | 2026-09-04T14:03:36.485Z → 2026-10-23T23:55:38.296Z |
| [/business/plugins/netlify/](../../pages/openai.com/business/plugins/netlify/index.md) | 17 | 17 | 2026-09-25T00:34:43.089Z → 2026-11-01T02:38:15.053Z |
| [/policies/sub-processor-list/](../../pages/openai.com/policies/sub-processor-list/index.md) | 16 | 16 | 2026-08-14T00:02:14.757Z → 2026-10-17T10:58:44.682Z |
| [/index/chip-ganassi-racing/](../../pages/openai.com/index/chip-ganassi-racing/index.md) | 18 | 14 | 2026-09-08T22:42:52.947Z → 2026-11-18T17:09:55.239Z |
| [/business/plugins/supermetrics/](../../pages/openai.com/business/plugins/supermetrics/index.md) | 21 | 11 | 2026-09-25T00:29:02.594Z → 2026-11-18T20:11:51.179Z |
| [/business/plugins/firecrawl/](../../pages/openai.com/business/plugins/firecrawl/index.md) | 16 | 15 | 2026-09-25T00:13:38.903Z → 2026-11-17T21:35:52.751Z |
| [/business/plugins/bigdata-com/](../../pages/openai.com/business/plugins/bigdata-com/index.md) | 16 | 15 | 2026-09-25T00:16:46.638Z → 2026-11-05T19:26:35.146Z |
| [/research/verify/](../../pages/openai.com/research/verify/index.md) | 17 | 14 | 2026-09-25T09:56:40.828Z → 2026-11-20T05:01:06.335Z |
| [/business/plugins/notion/](../../pages/openai.com/business/plugins/notion/index.md) | 17 | 12 | 2026-09-25T00:30:54.323Z → 2026-11-18T20:23:07.958Z |
| [/business/guides-and-resources/a-practical-guide-to-building-with-ai/](../../pages/openai.com/business/guides-and-resources/a-practical-guide-to-building-with-ai/index.md) | 15 | 14 | 2026-09-21T20:28:37.734Z → 2026-11-04T20:10:15.897Z |
| [/policies/advertising-terms/](../../pages/openai.com/policies/advertising-terms/index.md) | 13 | 16 | 2026-08-31T17:28:01.792Z → 2026-11-08T12:46:37.194Z |
| [/policies/service-terms/](../../pages/openai.com/policies/service-terms/index.md) | 20 | 9 | 2026-09-21T16:43:46.492Z → 2026-11-16T23:05:41.316Z |
| [/business/plugins/hugging-face/](../../pages/openai.com/business/plugins/hugging-face/index.md) | 8 | 20 | 2026-09-25T00:33:56.862Z → 2026-10-31T19:54:22.075Z |
| [/business/plugins/tavily-ai/](../../pages/openai.com/business/plugins/tavily-ai/index.md) | 14 | 13 | 2026-09-25T00:18:52.785Z → 2026-11-18T20:26:50.948Z |
| [/business/plugins/gsc-wizard/](../../pages/openai.com/business/plugins/gsc-wizard/index.md) | 18 | 9 | 2026-09-25T00:38:09.271Z → 2026-11-18T20:27:17.006Z |
| [/business/learn/](../../pages/openai.com/business/learn/index.md) | 19 | 7 | 2026-09-07T16:36:01.414Z → 2026-11-04T20:10:18.850Z |
| [/business/plugins/parallel-search/](../../pages/openai.com/business/plugins/parallel-search/index.md) | 15 | 11 | 2026-09-25T00:18:41.020Z → 2026-11-20T15:36:37.844Z |
| [/business/plugins/clay/](../../pages/openai.com/business/plugins/clay/index.md) | 18 | 8 | 2026-09-25T00:32:40.669Z → 2026-11-18T20:24:23.974Z |
| [/business/plugins/zoom/](../../pages/openai.com/business/plugins/zoom/index.md) | 9 | 17 | 2026-09-25T20:48:56.422Z → 2026-11-18T20:24:35.828Z |
| [/business/plugins/windsor-ai/](../../pages/openai.com/business/plugins/windsor-ai/index.md) | 17 | 9 | 2026-09-25T20:12:36.596Z → 2026-11-18T20:24:12.722Z |
| [/business/plugins/ringcentral-phone/](../../pages/openai.com/business/plugins/ringcentral-phone/index.md) | 16 | 9 | 2026-09-25T00:36:15.493Z → 2026-11-17T21:35:54.570Z |
| [/business/plugins/sync-labs/](../../pages/openai.com/business/plugins/sync-labs/index.md) | 18 | 7 | 2026-09-25T00:18:38.745Z → 2026-11-10T20:43:44.058Z |
| [/business/plugins/vidiq/](../../pages/openai.com/business/plugins/vidiq/index.md) | 17 | 8 | 2026-09-25T04:11:46.720Z → 2026-11-18T20:28:03.532Z |
| [/business/customer-stories/](../../pages/openai.com/business/customer-stories/index.md) | 0 | 24 | 2026-09-25T19:12:46.165Z → 2026-11-18T01:53:21.923Z |
| [/research/index/publication/](../../pages/openai.com/research/index/publication/index.md) | 12 | 12 | 2026-09-25T19:00:13.824Z → 2026-11-08T12:34:17.720Z |
| [/business/plugins/attio/](../../pages/openai.com/business/plugins/attio/index.md) | 17 | 7 | 2026-09-25T00:36:01.440Z → 2026-11-18T20:22:34.388Z |
| [/business/plugins/klaviyo/](../../pages/openai.com/business/plugins/klaviyo/index.md) | 14 | 10 | 2026-09-25T00:33:43.543Z → 2026-11-19T01:10:54.276Z |
| [/business/plugins/heygen/](../../pages/openai.com/business/plugins/heygen/index.md) | 17 | 7 | 2026-09-25T00:31:55.562Z → 2026-11-18T20:10:05.263Z |
| [/business/plugins/mercury/](../../pages/openai.com/business/plugins/mercury/index.md) | 15 | 9 | 2026-09-25T02:21:46.272Z → 2026-10-31T20:52:22.122Z |
| [/business/plugins/vercel/](../../pages/openai.com/business/plugins/vercel/index.md) | 12 | 12 | 2026-09-25T00:37:10.944Z → 2026-11-01T02:53:57.076Z |
| [/business/plugins/kling-ai/](../../pages/openai.com/business/plugins/kling-ai/index.md) | 12 | 12 | 2026-09-25T00:34:12.284Z → 2026-11-18T20:11:47.905Z |
| [/business/plugins/picsart/](../../pages/openai.com/business/plugins/picsart/index.md) | 17 | 7 | 2026-09-25T00:32:40.415Z → 2026-11-18T20:10:00.828Z |
| [/business/plugins/lucid/](../../pages/openai.com/business/plugins/lucid/index.md) | 16 | 7 | 2026-09-25T00:28:57.395Z → 2026-11-18T20:27:49.641Z |
| [/business/plugins/higgsfield/](../../pages/openai.com/business/plugins/higgsfield/index.md) | 8 | 15 | 2026-09-25T00:24:34.630Z → 2026-11-18T20:11:20.572Z |
| [/business/plugins/hostinger-connector/](../../pages/openai.com/business/plugins/hostinger-connector/index.md) | 12 | 11 | 2026-09-25T00:30:34.761Z → 2026-11-05T19:24:52.909Z |
| [/business/plugins/hypd-ai/](../../pages/openai.com/business/plugins/hypd-ai/index.md) | 13 | 10 | 2026-09-25T00:35:36.476Z → 2026-11-18T20:21:06.223Z |
| [/business/plugins/magnific/](../../pages/openai.com/business/plugins/magnific/index.md) | 16 | 7 | 2026-09-25T00:35:03.719Z → 2026-11-05T19:21:26.524Z |
| [/business/plugins/openart/](../../pages/openai.com/business/plugins/openart/index.md) | 16 | 7 | 2026-09-25T00:17:26.401Z → 2026-11-10T20:48:40.661Z |
| [/business/plugins/windsor-ai-facebook-ads/](../../pages/openai.com/business/plugins/windsor-ai-facebook-ads/index.md) | 13 | 10 | 2026-09-25T21:17:51.199Z → 2026-11-18T20:21:13.547Z |
| [/research/index/](../../pages/openai.com/research/index/index.md) | 11 | 11 | 2026-09-25T19:21:42.614Z → 2026-11-12T22:33:52.899Z |
| [/business/plugins/deepnote/](../../pages/openai.com/business/plugins/deepnote/index.md) | 12 | 10 | 2026-09-25T00:32:58.199Z → 2026-11-18T20:22:26.309Z |
| [/business/plugins/google-drive/](../../pages/openai.com/business/plugins/google-drive/index.md) | 11 | 11 | 2026-09-25T00:33:13.744Z → 2026-11-18T20:21:43.195Z |
| [/business/plugins/salesforce/](../../pages/openai.com/business/plugins/salesforce/index.md) | 14 | 8 | 2026-09-25T00:36:26.797Z → 2026-11-16T23:51:58.171Z |
| [/business/plugins/tldv/](../../pages/openai.com/business/plugins/tldv/index.md) | 11 | 11 | 2026-09-25T01:04:11.335Z → 2026-11-18T20:27:22.570Z |
| [/business/plugins/wix/](../../pages/openai.com/business/plugins/wix/index.md) | 13 | 9 | 2026-09-25T00:35:12.901Z → 2026-11-18T20:18:15.684Z |
| [/business/plugins/adspirer/](../../pages/openai.com/business/plugins/adspirer/index.md) | 16 | 6 | 2026-09-25T00:33:15.681Z → 2026-11-05T19:27:15.688Z |
| [/business/plugins/figma/](../../pages/openai.com/business/plugins/figma/index.md) | 11 | 11 | 2026-09-25T00:37:23.583Z → 2026-11-18T20:26:07.157Z |
| [/api/](../../pages/openai.com/api/index.md) | 14 | 8 | 2026-09-25T14:14:26.339Z → 2026-11-21T16:49:20.554Z |
| [/business/plugins/brevo/](../../pages/openai.com/business/plugins/brevo/index.md) | 15 | 6 | 2026-09-25T00:33:31.637Z → 2026-11-17T21:35:52.005Z |
| [/business/plugins/fathom/](../../pages/openai.com/business/plugins/fathom/index.md) | 11 | 10 | 2026-09-25T00:34:46.812Z → 2026-11-18T20:11:13.484Z |
| [/business/plugins/mobbin/](../../pages/openai.com/business/plugins/mobbin/index.md) | 13 | 8 | 2026-09-25T00:17:08.083Z → 2026-11-05T19:24:51.509Z |
| [/business/plugins/shopify/](../../pages/openai.com/business/plugins/shopify/index.md) | 7 | 14 | 2026-09-25T00:30:16.599Z → 2026-11-18T20:27:27.229Z |
| [/business/plugins/windsor-ai-google-ads/](../../pages/openai.com/business/plugins/windsor-ai-google-ads/index.md) | 11 | 10 | 2026-09-25T23:16:52.077Z → 2026-11-18T20:27:50.018Z |
| [/business/plugins/firebase/](../../pages/openai.com/business/plugins/firebase/index.md) | 10 | 10 | 2026-09-25T00:33:57.504Z → 2026-11-18T20:26:45.051Z |
| [/business/plugins/jam-dev/](../../pages/openai.com/business/plugins/jam-dev/index.md) | 13 | 7 | 2026-09-25T00:26:54.070Z → 2026-11-10T20:46:21.589Z |
| [/business/plugins/sales/](../../pages/openai.com/business/plugins/sales/index.md) | 10 | 10 | 2026-09-25T00:33:20.493Z → 2026-11-18T20:26:57.607Z |
| [/business/plugins/scholar-gateway/](../../pages/openai.com/business/plugins/scholar-gateway/index.md) | 10 | 10 | 2026-09-25T00:18:19.194Z → 2026-11-18T20:26:47.304Z |
| [/business/plugins/midpage/](../../pages/openai.com/business/plugins/midpage/index.md) | 10 | 10 | 2026-09-25T00:18:11.208Z → 2026-11-18T20:09:55.091Z |
| [/index/how-agents-are-transforming-work/](../../pages/openai.com/index/how-agents-are-transforming-work/index.md) | 20 | 0 | 2026-09-25T19:33:52.093Z → 2026-11-20T22:52:19.077Z |
| [/business/plugins/highlevel/](../../pages/openai.com/business/plugins/highlevel/index.md) | 11 | 8 | 2026-09-25T00:31:32.000Z → 2026-11-10T20:46:53.669Z |
| [/business/plugins/invideo/](../../pages/openai.com/business/plugins/invideo/index.md) | 12 | 7 | 2026-09-25T00:29:00.682Z → 2026-11-18T20:21:58.318Z |
| [/business/plugins/upwork/](../../pages/openai.com/business/plugins/upwork/index.md) | 12 | 7 | 2026-09-25T03:26:10.453Z → 2026-11-01T02:09:29.397Z |
| [/index/how-enterprises-put-ai-to-work/](../../pages/openai.com/index/how-enterprises-put-ai-to-work/index.md) | 19 | 0 | 2026-09-25T19:33:51.138Z → 2026-11-20T22:50:52.442Z |
| [/business/why-openai/startups/](../../pages/openai.com/business/why-openai/startups/index.md) | 1 | 17 | 2026-09-25T21:23:30.467Z → 2026-11-05T00:32:49.752Z |
| [/business/plugins/monday-com/](../../pages/openai.com/business/plugins/monday-com/index.md) | 9 | 9 | 2026-09-25T00:34:21.226Z → 2026-11-18T20:23:19.141Z |
| [/business/plugins/github/](../../pages/openai.com/business/plugins/github/index.md) | 9 | 9 | 2026-09-25T00:38:27.306Z → 2026-11-05T19:25:36.666Z |
| [/index/what-parameter-golf-taught-us/](../../pages/openai.com/index/what-parameter-golf-taught-us/index.md) | 9 | 9 | 2026-09-25T19:18:42.494Z → 2026-11-04T22:14:12.049Z |
| [/index/introducing-chatgpt-financial-services/](../../pages/openai.com/index/introducing-chatgpt-financial-services/index.md) | 0 | 18 | 2026-09-25T19:16:17.520Z → 2026-11-18T13:50:30.043Z |
| [/index/introducing-genebench-pro/](../../pages/openai.com/index/introducing-genebench-pro/index.md) | 0 | 18 | 2026-09-25T19:18:10.069Z → 2026-11-08T12:36:28.185Z |
| [/business/plugins/consensus/](../../pages/openai.com/business/plugins/consensus/index.md) | 9 | 8 | 2026-09-25T00:29:46.257Z → 2026-11-18T20:26:24.922Z |
| [/business/plugins/hubspot/](../../pages/openai.com/business/plugins/hubspot/index.md) | 9 | 8 | 2026-09-25T00:36:58.598Z → 2026-11-17T00:02:24.025Z |
| [/business/plugins/neon/](../../pages/openai.com/business/plugins/neon/index.md) | 10 | 7 | 2026-09-25T00:37:27.255Z → 2026-11-18T20:26:01.842Z |
| [/business/plugins/creative-claw/](../../pages/openai.com/business/plugins/creative-claw/index.md) | 9 | 8 | 2026-09-25T00:37:34.522Z → 2026-11-05T19:22:50.783Z |
| [/business/plugins/descript/](../../pages/openai.com/business/plugins/descript/index.md) | 11 | 6 | 2026-09-25T00:28:26.559Z → 2026-11-05T19:18:40.956Z |
| [/business/plugins/grain/](../../pages/openai.com/business/plugins/grain/index.md) | 12 | 5 | 2026-09-25T00:06:48.424Z → 2026-11-17T21:35:53.579Z |
| [/business/plugins/render/](../../pages/openai.com/business/plugins/render/index.md) | 9 | 8 | 2026-09-25T00:32:21.231Z → 2026-11-05T19:27:39.411Z |
| [/research/index/release/](../../pages/openai.com/research/index/release/index.md) | 8 | 8 | 2026-09-25T18:58:51.740Z → 2026-11-12T22:33:48.529Z |
| [/business/plugins/conductor/](../../pages/openai.com/business/plugins/conductor/index.md) | 8 | 8 | 2026-09-25T00:33:33.365Z → 2026-11-01T03:31:39.505Z |
| [/business/plugins/hex/](../../pages/openai.com/business/plugins/hex/index.md) | 7 | 9 | 2026-09-25T00:34:42.170Z → 2026-11-16T23:59:17.162Z |
| [/business/plugins/dropbox/](../../pages/openai.com/business/plugins/dropbox/index.md) | 9 | 7 | 2026-09-25T00:31:55.281Z → 2026-11-17T21:36:12.411Z |
| [/business/plugins/g2/](../../pages/openai.com/business/plugins/g2/index.md) | 8 | 8 | 2026-09-25T00:34:00.611Z → 2026-11-18T20:12:23.101Z |
| [/business/plugins/omni/](../../pages/openai.com/business/plugins/omni/index.md) | 8 | 8 | 2026-09-25T00:40:16.942Z → 2026-11-18T20:11:02.152Z |
| [/business/plugins/onenote/](../../pages/openai.com/business/plugins/onenote/index.md) | 8 | 8 | 2026-09-25T00:41:34.718Z → 2026-11-17T21:35:54.377Z |
| [/business/plugins/quickbooks/](../../pages/openai.com/business/plugins/quickbooks/index.md) | 8 | 8 | 2026-09-25T02:46:11.343Z → 2026-11-18T20:24:53.148Z |
| [/business/plugins/quo/](../../pages/openai.com/business/plugins/quo/index.md) | 9 | 7 | 2026-09-25T00:06:05.243Z → 2026-11-05T19:27:36.378Z |
| [/business/plugins/ramp/](../../pages/openai.com/business/plugins/ramp/index.md) | 9 | 7 | 2026-09-25T00:32:27.377Z → 2026-11-05T19:27:34.888Z |
| [/business/plugins/stripe/](../../pages/openai.com/business/plugins/stripe/index.md) | 8 | 8 | 2026-09-25T00:33:12.058Z → 2026-11-18T20:23:31.453Z |
| [/business/plugins/mongodb/](../../pages/openai.com/business/plugins/mongodb/index.md) | 8 | 8 | 2026-09-25T00:33:46.195Z → 2026-11-18T20:24:30.273Z |
| [/business/plugins/openai-developers/](../../pages/openai.com/business/plugins/openai-developers/index.md) | 9 | 7 | 2026-09-25T00:38:48.009Z → 2026-11-18T20:10:59.426Z |
| [/index/unlocking-the-codex-harness/](../../pages/openai.com/index/unlocking-the-codex-harness/index.md) | 0 | 16 | 2026-09-22T09:51:55.085Z → 2026-11-03T21:43:11.902Z |
| [/business/plugins/clio/](../../pages/openai.com/business/plugins/clio/index.md) | 9 | 7 | 2026-09-25T00:29:53.120Z → 2026-11-17T21:35:53.194Z |
| [/daybreak/partners/](../../pages/openai.com/daybreak/partners/index.md) | 8 | 8 | 2026-09-18T20:07:08.996Z → 2026-11-18T20:12:06.730Z |
| [/open-models/](../../pages/openai.com/open-models/index.md) | 8 | 8 | 2026-09-15T23:28:38.728Z → 2026-11-01T13:25:37.709Z |
| [/business/plugins/box/](../../pages/openai.com/business/plugins/box/index.md) | 8 | 7 | 2026-09-25T00:33:03.808Z → 2026-11-01T02:38:05.507Z |
| [/business/plugins/egnyte/](../../pages/openai.com/business/plugins/egnyte/index.md) | 9 | 6 | 2026-09-25T00:38:19.039Z → 2026-11-18T20:11:13.104Z |
| [/business/plugins/gamma/](../../pages/openai.com/business/plugins/gamma/index.md) | 9 | 6 | 2026-09-25T00:35:16.805Z → 2026-11-18T20:10:59.777Z |
| [/business/plugins/happyscribe/](../../pages/openai.com/business/plugins/happyscribe/index.md) | 8 | 7 | 2026-09-25T00:16:28.238Z → 2026-11-17T21:35:53.593Z |
| [/business/plugins/lusha/](../../pages/openai.com/business/plugins/lusha/index.md) | 9 | 6 | 2026-09-25T00:33:47.802Z → 2026-11-16T23:59:11.335Z |
| [/business/plugins/canva/](../../pages/openai.com/business/plugins/canva/index.md) | 3 | 12 | 2026-09-25T00:28:47.350Z → 2026-11-17T00:02:39.519Z |
| [/business/plugins/sentinelx/](../../pages/openai.com/business/plugins/sentinelx/index.md) | 8 | 7 | 2026-09-25T00:17:40.543Z → 2026-11-18T20:21:25.255Z |
| [/business/plugins/soundbreak/](../../pages/openai.com/business/plugins/soundbreak/index.md) | 8 | 7 | 2026-09-25T00:14:56.915Z → 2026-11-18T20:17:18.255Z |
| [/collective-cyberdefense/](../../pages/openai.com/collective-cyberdefense/index.md) | 9 | 6 | 2026-09-25T19:16:28.159Z → 2026-11-18T19:25:21.102Z |
| [/global-affairs/response-to-nist-executive-order-on-ai/](../../pages/openai.com/global-affairs/response-to-nist-executive-order-on-ai/index.md) | 10 | 5 | 2026-07-15T18:28:55.178Z → 2026-11-09T12:37:33.538Z |
| [/signals/](../../pages/openai.com/signals/index.md) | 7 | 7 | 2026-09-25T23:09:57.163Z → 2026-11-20T00:21:46.881Z |
| [/index/election-safeguards-2026/](../../pages/openai.com/index/election-safeguards-2026/index.md) | 13 | 1 | 2026-09-25T19:16:20.124Z → 2026-11-18T13:50:44.285Z |
| [/business/plugins/adobe-express/](../../pages/openai.com/business/plugins/adobe-express/index.md) | 7 | 7 | 2026-09-25T00:33:07.031Z → 2026-11-01T05:23:00.382Z |
| [/business/plugins/codex-security/](../../pages/openai.com/business/plugins/codex-security/index.md) | 7 | 7 | 2026-09-25T00:34:10.013Z → 2026-11-18T20:09:20.283Z |
| [/business/plugins/explain-video-generator/](../../pages/openai.com/business/plugins/explain-video-generator/index.md) | 7 | 7 | 2026-09-25T00:36:47.674Z → 2026-11-05T19:24:43.453Z |
| [/business/plugins/lseg/](../../pages/openai.com/business/plugins/lseg/index.md) | 7 | 7 | 2026-09-25T00:33:42.512Z → 2026-11-01T05:14:01.458Z |
| [/business/plugins/microsoft-azure-cosmosdb/](../../pages/openai.com/business/plugins/microsoft-azure-cosmosdb/index.md) | 7 | 7 | 2026-09-25T00:33:16.655Z → 2026-11-18T20:21:10.972Z |
| [/business/plugins/rocketreach/](../../pages/openai.com/business/plugins/rocketreach/index.md) | 7 | 7 | 2026-09-25T00:34:38.038Z → 2026-11-17T00:04:08.569Z |
| [/business/plugins/sider-scholar/](../../pages/openai.com/business/plugins/sider-scholar/index.md) | 7 | 7 | 2026-09-25T00:06:35.090Z → 2026-11-10T20:46:52.475Z |
| [/business/plugins/villagesql/](../../pages/openai.com/business/plugins/villagesql/index.md) | 7 | 7 | 2026-09-25T04:23:05.426Z → 2026-11-18T20:30:54.361Z |
| [/business/plugins/tally/](../../pages/openai.com/business/plugins/tally/index.md) | 7 | 7 | 2026-09-25T00:06:58.443Z → 2026-11-17T21:35:54.197Z |
| [/business/plugins/dbt/](../../pages/openai.com/business/plugins/dbt/index.md) | 7 | 7 | 2026-09-25T00:29:41.244Z → 2026-11-18T20:20:20.030Z |
| [/business/plugins/ubersuggest/](../../pages/openai.com/business/plugins/ubersuggest/index.md) | 7 | 7 | 2026-09-25T02:49:44.738Z → 2026-11-18T20:26:54.140Z |
| [/business/plugins/remote-desktop-commander/](../../pages/openai.com/business/plugins/remote-desktop-commander/index.md) | 7 | 7 | 2026-09-25T00:18:29.629Z → 2026-11-01T00:57:48.288Z |
| [/index/gpt-6-astra/](../../pages/openai.com/index/gpt-6-astra/index.md) | 7 | 7 | 2026-09-25T19:18:10.771Z → 2026-11-19T22:57:21.231Z |
| [/policies/ad-tools-terms/](../../pages/openai.com/policies/ad-tools-terms/index.md) | 6 | 8 | 2026-08-27T22:57:31.891Z → 2026-11-14T10:48:06.585Z |
| [/signals/data-download/](../../pages/openai.com/signals/data-download/index.md) | 13 | 1 | 2026-09-15T04:37:05.758Z → 2026-11-12T19:02:58.734Z |
| [/business/plugins/fal/](../../pages/openai.com/business/plugins/fal/index.md) | 7 | 6 | 2026-09-25T00:34:45.326Z → 2026-11-18T20:24:46.145Z |
| [/business/plugins/parqet/](../../pages/openai.com/business/plugins/parqet/index.md) | 7 | 6 | 2026-09-25T00:17:24.231Z → 2026-11-05T19:25:59.426Z |
| [/index/how-people-are-using-chatgpt/](../../pages/openai.com/index/how-people-are-using-chatgpt/index.md) | 13 | 0 | 2026-09-25T19:33:52.034Z → 2026-11-20T22:39:30.038Z |
| [/chatgpt-work/](../../pages/openai.com/chatgpt-work/index.md) | 8 | 5 | 2026-09-28T04:14:20.196Z → 2026-11-02T00:40:27.031Z |
| [/index/openai-api/](../../pages/openai.com/index/openai-api/index.md) | 1 | 12 | 2026-09-23T20:42:08.075Z → 2026-11-17T23:02:38.849Z |
| [/index/scaling-social-science-research/](../../pages/openai.com/index/scaling-social-science-research/index.md) | 13 | 0 | 2026-09-25T19:33:52.210Z → 2026-11-20T22:46:31.352Z |
| [/live/](../../pages/openai.com/live/index.md) | 5 | 8 | 2026-09-26T22:26:19.898Z → 2026-11-12T15:43:48.862Z |
| [/new-york-times/](../../pages/openai.com/new-york-times/index.md) | 12 | 1 | 2026-09-14T08:07:23.377Z → 2026-11-06T00:16:10.212Z |
| [/index/learning-to-reason-with-llms/](../../pages/openai.com/index/learning-to-reason-with-llms/index.md) | 8 | 4 | 2026-09-22T19:00:23.480Z → 2026-11-05T10:12:24.688Z |
| [/business/plugins/tableau/](../../pages/openai.com/business/plugins/tableau/index.md) | 7 | 5 | 2026-09-25T00:34:27.353Z → 2026-11-17T21:35:53.599Z |
| [/business/plugins/apollo/](../../pages/openai.com/business/plugins/apollo/index.md) | 6 | 6 | 2026-09-25T00:31:44.725Z → 2026-11-16T23:59:44.300Z |
| [/index/red-teaming-network/](../../pages/openai.com/index/red-teaming-network/index.md) | 10 | 2 | 2026-05-31T20:06:24.028Z → 2026-11-14T12:44:36.461Z |
| [/business/plugins/posthog/](../../pages/openai.com/business/plugins/posthog/index.md) | 5 | 7 | 2026-09-25T00:37:27.650Z → 2026-11-18T20:11:53.575Z |
| [/business/plugins/redis/](../../pages/openai.com/business/plugins/redis/index.md) | 6 | 6 | 2026-09-25T00:37:56.451Z → 2026-11-18T20:25:40.117Z |
| [/business/plugins/tinyfish/](../../pages/openai.com/business/plugins/tinyfish/index.md) | 6 | 6 | 2026-09-25T01:06:54.382Z → 2026-11-01T01:53:54.857Z |
| [/business/plugins/trellis-law/](../../pages/openai.com/business/plugins/trellis-law/index.md) | 7 | 5 | 2026-09-25T00:01:22.974Z → 2026-11-10T20:45:48.263Z |
| [/business/plugins/wrike/](../../pages/openai.com/business/plugins/wrike/index.md) | 6 | 6 | 2026-09-25T20:34:11.349Z → 2026-11-17T21:36:20.416Z |
| [/business/plugins/undermind/](../../pages/openai.com/business/plugins/undermind/index.md) | 6 | 6 | 2026-09-25T02:47:30.292Z → 2026-11-18T20:17:41.508Z |
| [/business/plugins/coinmarketcap/](../../pages/openai.com/business/plugins/coinmarketcap/index.md) | 6 | 6 | 2026-09-25T00:15:40.353Z → 2026-11-18T20:19:30.613Z |
| [/business/plugins/data/](../../pages/openai.com/business/plugins/data/index.md) | 6 | 6 | 2026-09-25T00:37:57.450Z → 2026-11-18T20:25:00.672Z |
| [/business/plugins/runway/](../../pages/openai.com/business/plugins/runway/index.md) | 6 | 6 | 2026-09-25T00:31:18.883Z → 2026-11-18T20:11:53.210Z |
| [/signals/research/](../../pages/openai.com/signals/research/index.md) | 6 | 6 | 2026-09-15T04:37:07.853Z → 2026-11-17T14:34:03.266Z |
| [/business/plugins/microsoft-dataverse/](../../pages/openai.com/business/plugins/microsoft-dataverse/index.md) | 6 | 5 | 2026-09-25T00:36:25.990Z → 2026-11-01T04:49:25.062Z |
| [/index/personal-finance-chatgpt/](../../pages/openai.com/index/personal-finance-chatgpt/index.md) | 10 | 1 | 2026-09-25T19:16:12.872Z → 2026-11-17T23:03:06.109Z |
| [/solutions/industries/government/](../../pages/openai.com/solutions/industries/government/index.md) | 4 | 7 | 2026-09-16T16:12:16.660Z → 2026-11-06T18:20:34.544Z |
| [/policies/merchant-feed-terms-of-service/](../../pages/openai.com/policies/merchant-feed-terms-of-service/index.md) | 6 | 5 | 2026-06-22T21:57:40.791Z → 2026-11-08T16:08:09.064Z |
| [/index/astra-for-law/](../../pages/openai.com/index/astra-for-law/index.md) | 2 | 9 | 2026-09-27T11:48:16.440Z → 2026-11-19T16:54:21.676Z |
| [/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/](../../pages/openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/index.md) | 0 | 11 | 2026-09-22T19:25:22.944Z → 2026-11-18T09:03:45.406Z |
| [/index/what-students-gain-from-chatgpt-critical-thinking-training/](../../pages/openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training/index.md) | 11 | 0 | 2026-09-25T19:33:49.040Z → 2026-11-20T22:51:28.951Z |
| [/policies/commerce-policies/](../../pages/openai.com/policies/commerce-policies/index.md) | 5 | 6 | 2026-06-29T04:12:44.738Z → 2026-10-08T09:20:01.331Z |
| [/daybreak/codex-security-plugin/](../../pages/openai.com/daybreak/codex-security-plugin/index.md) | 5 | 5 | 2026-07-17T03:57:27.941Z → 2026-11-12T18:53:09.890Z |
| [/business/plugins/digitalocean/](../../pages/openai.com/business/plugins/digitalocean/index.md) | 5 | 5 | 2026-09-25T00:32:48.494Z → 2026-11-05T19:21:39.176Z |
| [/business/plugins/ironclad-contracts/](../../pages/openai.com/business/plugins/ironclad-contracts/index.md) | 5 | 5 | 2026-09-25T00:36:42.542Z → 2026-11-16T23:52:52.118Z |
| [/business/plugins/jotform/](../../pages/openai.com/business/plugins/jotform/index.md) | 5 | 5 | 2026-09-25T00:36:17.885Z → 2026-11-17T21:36:03.685Z |
| [/business/plugins/manatal/](../../pages/openai.com/business/plugins/manatal/index.md) | 5 | 5 | 2026-09-25T00:36:40.253Z → 2026-11-05T19:24:26.536Z |
| [/business/plugins/miro/](../../pages/openai.com/business/plugins/miro/index.md) | 5 | 5 | 2026-09-25T00:33:28.336Z → 2026-11-18T20:21:59.878Z |
| [/business/plugins/pandadoc/](../../pages/openai.com/business/plugins/pandadoc/index.md) | 5 | 5 | 2026-09-25T00:08:13.045Z → 2026-11-17T21:35:49.668Z |
| [/business/plugins/chatgpt-ads-manager/](../../pages/openai.com/business/plugins/chatgpt-ads-manager/index.md) | 5 | 5 | 2026-09-25T00:08:22.327Z → 2026-11-18T20:22:26.641Z |
| [/business/plugins/highspot/](../../pages/openai.com/business/plugins/highspot/index.md) | 5 | 5 | 2026-09-25T00:36:01.785Z → 2026-11-18T20:07:47.124Z |
| [/business/plugins/mermaid-chart/](../../pages/openai.com/business/plugins/mermaid-chart/index.md) | 5 | 5 | 2026-09-25T00:30:17.408Z → 2026-11-05T19:26:53.081Z |
| [/business/plugins/teamtailor/](../../pages/openai.com/business/plugins/teamtailor/index.md) | 5 | 5 | 2026-09-25T00:10:51.485Z → 2026-11-01T02:56:12.222Z |
| [/business/plugins/xero/](../../pages/openai.com/business/plugins/xero/index.md) | 5 | 5 | 2026-09-25T20:43:03.398Z → 2026-11-05T19:22:26.993Z |
| [/business/plugins/interactive-brokers/](../../pages/openai.com/business/plugins/interactive-brokers/index.md) | 5 | 5 | 2026-09-25T00:36:06.405Z → 2026-11-01T05:06:15.062Z |
| [/academy/financial-services/](../../pages/openai.com/academy/financial-services/index.md) | 5 | 5 | 2026-07-14T20:19:39.615Z → 2026-11-05T08:17:14.840Z |
| [/api-fast-mode/](../../pages/openai.com/api-fast-mode/index.md) | 7 | 3 | 2026-09-25T14:01:55.817Z → 2026-11-17T19:29:20.140Z |
| [/contact-sales/](../../pages/openai.com/contact-sales/index.md) | 5 | 5 | 2026-09-23T17:46:16.818Z → 2026-10-07T16:24:05.202Z |
| [/policies/eu-services-privacy-policy/](../../pages/openai.com/policies/eu-services-privacy-policy/index.md) | 5 | 5 | 2026-08-25T19:20:03.714Z → 2026-10-22T03:51:24.128Z |
| [/transparency-and-content-moderation/](../../pages/openai.com/transparency-and-content-moderation/index.md) | 5 | 5 | 2026-08-18T21:41:20.567Z → 2026-11-16T23:56:02.148Z |
| [/solutions/](../../pages/openai.com/solutions/index.md) | 5 | 4 | 2026-07-29T20:25:00.769Z → 2026-11-20T00:18:32.232Z |
| [/index/combating-online-child-sexual-exploitation-abuse/](../../pages/openai.com/index/combating-online-child-sexual-exploitation-abuse/index.md) | 7 | 2 | 2026-05-22T19:12:03.952Z → 2026-11-04T13:39:41.901Z |
| [/business/plugins/adobe/](../../pages/openai.com/business/plugins/adobe/index.md) | 5 | 4 | 2026-09-25T00:27:11.714Z → 2026-11-01T02:55:14.621Z |
| [/index/builders-guide-to-gpt-5-6/](../../pages/openai.com/index/builders-guide-to-gpt-5-6/index.md) | 1 | 8 | 2026-09-28T02:45:20.171Z → 2026-11-06T16:31:23.042Z |
| [/index/ai-first-hire-small-business/](../../pages/openai.com/index/ai-first-hire-small-business/index.md) | 9 | 0 | 2026-07-14T17:37:39.024Z → 2026-11-20T22:40:22.524Z |
| [/index/modeling-ai-jobs-transition/](../../pages/openai.com/index/modeling-ai-jobs-transition/index.md) | 9 | 0 | 2026-07-14T17:37:52.956Z → 2026-11-20T22:48:40.295Z |
| [/company/public-policy/](../../pages/openai.com/company/public-policy/index.md) | 7 | 2 | 2026-09-09T20:40:36.728Z → 2026-11-20T17:50:25.385Z |
| [/index/ai-for-self-empowerment/](../../pages/openai.com/index/ai-for-self-empowerment/index.md) | 0 | 9 | 2026-05-22T19:09:03.013Z → 2026-10-14T22:59:36.982Z |
| [/index/airbnb-gpt-6-astra/](../../pages/openai.com/index/airbnb-gpt-6-astra/index.md) | 0 | 9 | 2026-09-25T19:16:16.112Z → 2026-11-13T22:12:30.581Z |
| [/index/gpt-5-6-in-kiro/](../../pages/openai.com/index/gpt-5-6-in-kiro/index.md) | 0 | 9 | 2026-09-25T19:16:32.030Z → 2026-11-13T20:19:34.164Z |
| [/index/how-ai-is-expanding-what-people-do-at-work/](../../pages/openai.com/index/how-ai-is-expanding-what-people-do-at-work/index.md) | 9 | 0 | 2026-09-25T19:33:51.019Z → 2026-11-20T22:46:36.684Z |
| [/index/how-countries-can-end-the-capability-overhang/](../../pages/openai.com/index/how-countries-can-end-the-capability-overhang/index.md) | 9 | 0 | 2026-09-25T19:34:20.228Z → 2026-11-20T22:51:13.165Z |
| [/index/mapping-ai-jobs-transition-eu/](../../pages/openai.com/index/mapping-ai-jobs-transition-eu/index.md) | 9 | 0 | 2026-09-25T19:33:52.125Z → 2026-11-20T22:50:54.646Z |
| [/index/moving-ai-governance-forward/](../../pages/openai.com/index/moving-ai-governance-forward/index.md) | 9 | 0 | 2026-05-31T20:06:18.989Z → 2026-10-27T18:49:51.410Z |
| [/index/openai-frontier-models-and-codex-are-now-available-on-aws/](../../pages/openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/index.md) | 0 | 9 | 2026-09-23T20:42:00.758Z → 2026-11-17T23:02:39.865Z |
| [/index/openai-to-acquire-ona/](../../pages/openai.com/index/openai-to-acquire-ona/index.md) | 0 | 9 | 2026-09-22T22:06:06.808Z → 2026-11-10T09:52:54.010Z |
| [/index/paul-christiano-joins-openai-foundation-board/](../../pages/openai.com/index/paul-christiano-joins-openai-foundation-board/index.md) | 0 | 9 | 2026-09-25T19:16:17.637Z → 2026-11-10T09:52:36.151Z |
| [/index/the-state-of-enterprise-ai-2025-report/](../../pages/openai.com/index/the-state-of-enterprise-ai-2025-report/index.md) | 9 | 0 | 2026-09-25T19:18:11.318Z → 2026-11-20T22:48:47.995Z |
| [/index/introducing-chatgpt-agent/](../../pages/openai.com/index/introducing-chatgpt-agent/index.md) | 4 | 4 | 2026-09-18T17:55:57.600Z → 2026-11-12T22:33:27.503Z |
| [/index/inside-our-in-house-data-agent/](../../pages/openai.com/index/inside-our-in-house-data-agent/index.md) | 1 | 7 | 2026-08-13T23:57:08.794Z → 2026-11-02T13:19:13.083Z |
| [/business/plugins/zoho-crm/](../../pages/openai.com/business/plugins/zoho-crm/index.md) | 4 | 4 | 2026-09-25T21:20:28.828Z → 2026-11-17T00:04:39.236Z |
| [/business/plugins/aha/](../../pages/openai.com/business/plugins/aha/index.md) | 4 | 4 | 2026-09-25T00:30:04.884Z → 2026-11-01T03:54:07.508Z |
| [/business/plugins/clickup/](../../pages/openai.com/business/plugins/clickup/index.md) | 4 | 4 | 2026-09-25T00:31:16.825Z → 2026-11-17T21:36:08.340Z |
| [/business/plugins/coupler-io/](../../pages/openai.com/business/plugins/coupler-io/index.md) | 4 | 4 | 2026-09-25T00:18:04.436Z → 2026-11-01T01:42:28.949Z |
| [/business/plugins/coveo/](../../pages/openai.com/business/plugins/coveo/index.md) | 4 | 4 | 2026-09-25T00:33:55.404Z → 2026-11-17T21:36:05.370Z |
| [/business/plugins/fireflies/](../../pages/openai.com/business/plugins/fireflies/index.md) | 4 | 4 | 2026-09-25T00:35:33.928Z → 2026-11-17T21:35:47.595Z |
| [/business/plugins/linear/](../../pages/openai.com/business/plugins/linear/index.md) | 4 | 4 | 2026-09-25T00:38:09.817Z → 2026-10-31T21:01:10.786Z |
| [/business/plugins/lovable/](../../pages/openai.com/business/plugins/lovable/index.md) | 4 | 4 | 2026-09-25T00:33:17.513Z → 2026-10-31T21:53:41.693Z |
| [/business/plugins/microsoft-outlook-calendar/](../../pages/openai.com/business/plugins/microsoft-outlook-calendar/index.md) | 4 | 4 | 2026-09-25T00:36:45.069Z → 2026-11-17T21:36:00.095Z |
| [/business/plugins/microsoft-sharepoint/](../../pages/openai.com/business/plugins/microsoft-sharepoint/index.md) | 4 | 4 | 2026-09-25T00:34:00.115Z → 2026-11-17T21:36:01.371Z |
| [/business/plugins/microsoft-teams/](../../pages/openai.com/business/plugins/microsoft-teams/index.md) | 4 | 4 | 2026-09-25T00:27:32.429Z → 2026-11-17T21:36:00.744Z |
| [/business/plugins/morningstar/](../../pages/openai.com/business/plugins/morningstar/index.md) | 4 | 4 | 2026-09-25T00:34:11.611Z → 2026-11-01T01:23:25.034Z |
| [/business/plugins/pitchbook/](../../pages/openai.com/business/plugins/pitchbook/index.md) | 4 | 4 | 2026-09-25T00:35:21.880Z → 2026-11-01T04:10:38.333Z |
| [/business/plugins/relativity/](../../pages/openai.com/business/plugins/relativity/index.md) | 4 | 4 | 2026-09-25T00:26:21.879Z → 2026-11-17T21:36:15.615Z |
| [/business/plugins/sigma/](../../pages/openai.com/business/plugins/sigma/index.md) | 4 | 4 | 2026-09-25T00:31:52.916Z → 2026-11-18T20:23:46.378Z |
| [/business/plugins/spaceship/](../../pages/openai.com/business/plugins/spaceship/index.md) | 4 | 4 | 2026-09-25T00:18:13.854Z → 2026-11-01T04:00:05.178Z |
| [/business/partners/](../../pages/openai.com/business/partners/index.md) | 4 | 4 | 2026-09-25T20:30:21.907Z → 2026-10-30T12:33:53.313Z |
| [/business/plugins/daloopa/](../../pages/openai.com/business/plugins/daloopa/index.md) | 4 | 4 | 2026-09-25T00:07:06.657Z → 2026-10-31T19:55:27.208Z |
| [/business/plugins/gitlab/](../../pages/openai.com/business/plugins/gitlab/index.md) | 4 | 4 | 2026-09-25T00:27:25.648Z → 2026-11-05T19:24:33.625Z |
| [/business/plugins/replit/](../../pages/openai.com/business/plugins/replit/index.md) | 4 | 4 | 2026-09-25T00:33:58.028Z → 2026-11-01T02:24:28.142Z |
| [/business/plugins/semrush/](../../pages/openai.com/business/plugins/semrush/index.md) | 4 | 4 | 2026-09-25T00:33:28.573Z → 2026-11-17T21:35:58.596Z |
| [/business/plugins/temporal/](../../pages/openai.com/business/plugins/temporal/index.md) | 4 | 4 | 2026-09-25T00:34:52.084Z → 2026-11-01T03:40:34.007Z |
| [/index/computer-using-agent/](../../pages/openai.com/index/computer-using-agent/index.md) | 4 | 4 | 2026-06-20T08:53:08.159Z → 2026-11-05T10:12:44.634Z |
| [/academy/](../../pages/openai.com/academy/index.md) | 4 | 4 | 2026-09-07T16:34:25.322Z → 2026-11-13T00:33:20.024Z |
| [/index/new-tools-for-building-agents/](../../pages/openai.com/index/new-tools-for-building-agents/index.md) | 4 | 4 | 2026-09-23T20:42:09.311Z → 2026-11-02T13:59:26.160Z |
| [/policies/developer-apps-terms/](../../pages/openai.com/policies/developer-apps-terms/index.md) | 4 | 4 | 2026-09-10T17:43:51.220Z → 2026-11-08T12:59:34.948Z |
| [/](../../pages/openai.com/index.md) | 4 | 3 | 2026-09-23T19:49:50.418Z → 2026-11-19T10:06:47.020Z |
| [/global-affairs/disrupting-malicious-uses-of-ai-june-2025/](../../pages/openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/index.md) | 4 | 3 | 2026-05-15T06:11:39.448Z → 2026-11-04T14:07:05.556Z |
| [/index/reinforcement-learning-with-prediction-based-rewards/](../../pages/openai.com/index/reinforcement-learning-with-prediction-based-rewards/index.md) | 7 | 0 | 2026-06-03T04:00:47.859Z → 2026-10-21T05:54:39.631Z |
| [/index/better-language-models/](../../pages/openai.com/index/better-language-models/index.md) | 7 | 0 | 2026-06-03T04:00:37.526Z → 2026-10-19T07:36:36.789Z |
| [/business/guides-and-resources/a-practical-guide-to-building-ai-agents/](../../pages/openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/index.md) | 1 | 6 | 2026-09-21T20:28:37.957Z → 2026-11-04T20:10:15.675Z |
| [/signals/research/2026q1-update/](../../pages/openai.com/signals/research/2026q1-update/index.md) | 7 | 0 | 2026-09-14T21:56:11.138Z → 2026-11-20T22:50:36.091Z |
| [/index/how-chatgpt-adoption-has-expanded/](../../pages/openai.com/index/how-chatgpt-adoption-has-expanded/index.md) | 7 | 0 | 2026-09-25T19:33:52.247Z → 2026-11-20T22:51:39.427Z |
| [/policies/](../../pages/openai.com/policies/index.md) | 6 | 1 | 2026-09-13T06:47:18.775Z → 2026-11-16T20:23:06.320Z |
| [/index/powering-product-discovery-in-chatgpt/](../../pages/openai.com/index/powering-product-discovery-in-chatgpt/index.md) | 4 | 2 | 2026-06-05T09:44:09.524Z → 2026-11-17T23:02:50.568Z |
| [/index/evolution-strategies/](../../pages/openai.com/index/evolution-strategies/index.md) | 6 | 0 | 2026-06-01T19:21:37.002Z → 2026-10-21T02:59:35.490Z |
| [/index/how-should-ai-systems-behave/](../../pages/openai.com/index/how-should-ai-systems-behave/index.md) | 6 | 0 | 2026-05-31T20:06:12.339Z → 2026-10-27T20:09:30.734Z |
| [/business/plugins/adobe-acrobat/](../../pages/openai.com/business/plugins/adobe-acrobat/index.md) | 3 | 3 | 2026-09-25T00:28:09.418Z → 2026-11-17T21:36:08.186Z |
| [/business/plugins/airtable/](../../pages/openai.com/business/plugins/airtable/index.md) | 3 | 3 | 2026-09-25T00:37:26.874Z → 2026-11-17T21:36:08.492Z |
| [/business/plugins/asana/](../../pages/openai.com/business/plugins/asana/index.md) | 3 | 3 | 2026-09-25T00:34:56.701Z → 2026-11-01T03:06:33.491Z |
| [/business/plugins/bigquery/](../../pages/openai.com/business/plugins/bigquery/index.md) | 3 | 3 | 2026-09-25T00:31:01.671Z → 2026-11-01T00:18:21.334Z |
| [/business/plugins/chatgpt-admin/](../../pages/openai.com/business/plugins/chatgpt-admin/index.md) | 3 | 3 | 2026-09-25T00:32:51.010Z → 2026-11-01T03:32:39.358Z |
| [/business/plugins/cloudinary/](../../pages/openai.com/business/plugins/cloudinary/index.md) | 3 | 3 | 2026-09-25T00:31:58.818Z → 2026-10-31T20:09:56.706Z |
| [/business/plugins/everlaw/](../../pages/openai.com/business/plugins/everlaw/index.md) | 3 | 3 | 2026-09-25T00:04:29.301Z → 2026-10-31T20:48:34.254Z |
| [/business/plugins/google-calendar/](../../pages/openai.com/business/plugins/google-calendar/index.md) | 3 | 3 | 2026-09-25T00:34:41.040Z → 2026-11-17T21:36:21.051Z |
| [/business/plugins/gusto/](../../pages/openai.com/business/plugins/gusto/index.md) | 3 | 3 | 2026-09-25T00:34:39.569Z → 2026-11-01T04:53:04.737Z |
| [/business/plugins/hostinger/](../../pages/openai.com/business/plugins/hostinger/index.md) | 3 | 3 | 2026-09-25T00:40:25.237Z → 2026-11-01T00:08:59.325Z |
| [/business/plugins/investment-banking/](../../pages/openai.com/business/plugins/investment-banking/index.md) | 3 | 3 | 2026-09-25T00:35:55.495Z → 2026-11-01T03:47:15.672Z |
| [/business/plugins/mailchimp/](../../pages/openai.com/business/plugins/mailchimp/index.md) | 3 | 3 | 2026-09-25T00:33:44.613Z → 2026-10-31T20:24:02.726Z |
| [/business/plugins/ngs-analysis-workbench/](../../pages/openai.com/business/plugins/ngs-analysis-workbench/index.md) | 3 | 3 | 2026-09-25T00:32:28.720Z → 2026-11-18T20:20:49.091Z |
| [/business/plugins/public-equity-investing/](../../pages/openai.com/business/plugins/public-equity-investing/index.md) | 3 | 3 | 2026-09-25T00:34:33.225Z → 2026-11-01T11:11:59.463Z |
| [/business/plugins/text/](../../pages/openai.com/business/plugins/text/index.md) | 3 | 3 | 2026-09-25T00:06:18.664Z → 2026-11-01T05:38:23.883Z |
| [/business/plugins/amplitude/](../../pages/openai.com/business/plugins/amplitude/index.md) | 3 | 3 | 2026-09-25T00:32:49.428Z → 2026-10-31T20:29:05.812Z |
| [/business/plugins/databricks/](../../pages/openai.com/business/plugins/databricks/index.md) | 3 | 3 | 2026-09-25T00:41:44.630Z → 2026-10-31T22:24:26.769Z |
| [/business/plugins/gmail/](../../pages/openai.com/business/plugins/gmail/index.md) | 3 | 3 | 2026-09-25T00:35:27.320Z → 2026-11-17T21:36:04.481Z |
| [/business/plugins/microsoft-outlook-email/](../../pages/openai.com/business/plugins/microsoft-outlook-email/index.md) | 3 | 3 | 2026-09-25T00:33:50.004Z → 2026-11-17T21:36:01.943Z |
| [/business/plugins/openai-certified/](../../pages/openai.com/business/plugins/openai-certified/index.md) | 3 | 3 | 2026-09-25T00:07:07.597Z → 2026-11-01T02:01:58.302Z |
| [/business/plugins/slack/](../../pages/openai.com/business/plugins/slack/index.md) | 3 | 3 | 2026-09-25T00:37:13.376Z → 2026-11-17T21:35:57.860Z |
| [/business/plugins/snowflake/](../../pages/openai.com/business/plugins/snowflake/index.md) | 3 | 3 | 2026-09-25T00:34:49.038Z → 2026-10-31T20:08:29.892Z |
| [/index/introducing-openai-o1-preview/](../../pages/openai.com/index/introducing-openai-o1-preview/index.md) | 5 | 1 | 2026-09-23T20:42:08.798Z → 2026-11-02T21:18:13.560Z |
| [/science/](../../pages/openai.com/science/index.md) | 2 | 4 | 2026-09-27T18:51:23.484Z → 2026-11-15T22:04:47.110Z |
| [/index/chatgpt-for-excel/](../../pages/openai.com/index/chatgpt-for-excel/index.md) | 0 | 6 | 2026-09-21T06:52:35.074Z → 2026-11-03T18:54:44.091Z |
| [/index/gpt-4o-system-card/](../../pages/openai.com/index/gpt-4o-system-card/index.md) | 3 | 3 | 2026-08-30T07:53:47.531Z → 2026-11-05T10:12:01.391Z |
| [/policies/service-credit-terms/](../../pages/openai.com/policies/service-credit-terms/index.md) | 3 | 3 | 2026-06-03T17:39:49.995Z → 2026-11-16T08:54:39.043Z |
| [/index/outtake/](../../pages/openai.com/index/outtake/index.md) | 5 | 0 | 2026-05-22T19:10:33.264Z → 2026-10-30T05:31:47.636Z |
| [/index/unsupervised-sentiment-neuron/](../../pages/openai.com/index/unsupervised-sentiment-neuron/index.md) | 5 | 0 | 2026-06-01T19:21:36.407Z → 2026-10-21T04:13:40.443Z |
| [/index/language-unsupervised/](../../pages/openai.com/index/language-unsupervised/index.md) | 5 | 0 | 2026-06-03T04:00:44.055Z → 2026-10-21T00:43:50.551Z |
| [/index/update-on-safety-and-security-practices/](../../pages/openai.com/index/update-on-safety-and-security-practices/index.md) | 5 | 0 | 2026-05-31T20:06:17.882Z → 2026-10-27T20:55:31.100Z |
| [/index/rogo/](../../pages/openai.com/index/rogo/index.md) | 4 | 1 | 2026-06-02T15:02:02.278Z → 2026-10-30T00:34:03.222Z |
| [/index/openai-o3-mini/](../../pages/openai.com/index/openai-o3-mini/index.md) | 4 | 1 | 2026-04-30T06:51:16.703Z → 2026-11-05T10:12:54.808Z |
| [/index/previewing-ultrafast/](../../pages/openai.com/index/previewing-ultrafast/index.md) | 3 | 2 | 2026-09-25T19:16:33.333Z → 2026-11-17T23:03:06.491Z |
| [/index/thinking-with-images/](../../pages/openai.com/index/thinking-with-images/index.md) | 4 | 0 | 2026-07-25T07:01:47.117Z → 2026-11-05T10:12:01.669Z |
| [/index/introducing-o3-and-o4-mini/](../../pages/openai.com/index/introducing-o3-and-o4-mini/index.md) | 4 | 0 | 2026-07-25T07:09:31.335Z → 2026-11-17T23:03:09.132Z |
| [/index/collective-alignment-aug-2025-updates/](../../pages/openai.com/index/collective-alignment-aug-2025-updates/index.md) | 0 | 4 | 2026-07-25T07:09:33.865Z → 2026-10-19T07:57:39.411Z |
| [/index/introducing-gpt-4-5/](../../pages/openai.com/index/introducing-gpt-4-5/index.md) | 2 | 2 | 2026-08-14T20:48:23.507Z → 2026-11-18T00:11:05.645Z |
| [/index/coderabbit/](../../pages/openai.com/index/coderabbit/index.md) | 4 | 0 | 2026-05-22T19:01:42.910Z → 2026-10-30T00:53:04.586Z |
| [/business/plugins/outreach/](../../pages/openai.com/business/plugins/outreach/index.md) | 2 | 2 | 2026-09-25T00:33:07.855Z → 2026-11-16T23:59:32.948Z |
| [/business/plugins/seismic/](../../pages/openai.com/business/plugins/seismic/index.md) | 2 | 2 | 2026-09-25T00:32:15.319Z → 2026-11-16T23:57:31.716Z |
| [/business/plugins/zoominfo/](../../pages/openai.com/business/plugins/zoominfo/index.md) | 2 | 2 | 2026-09-25T21:49:40.597Z → 2026-11-16T23:54:58.216Z |
| [/index/how-confessions-can-keep-language-models-honest/](../../pages/openai.com/index/how-confessions-can-keep-language-models-honest/index.md) | 1 | 3 | 2026-09-25T19:18:13.927Z → 2026-11-08T12:36:31.099Z |
| [/index/our-approach-to-alignment-research/](../../pages/openai.com/index/our-approach-to-alignment-research/index.md) | 4 | 0 | 2026-06-03T18:57:26.940Z → 2026-10-28T02:04:55.692Z |
| [/business/plugins/activecampaign/](../../pages/openai.com/business/plugins/activecampaign/index.md) | 2 | 2 | 2026-09-25T15:12:07.716Z → 2026-10-31T19:56:37.073Z |
| [/business/plugins/affinity/](../../pages/openai.com/business/plugins/affinity/index.md) | 2 | 2 | 2026-09-25T00:36:21.187Z → 2026-11-01T04:41:51.191Z |
| [/business/plugins/alation/](../../pages/openai.com/business/plugins/alation/index.md) | 2 | 2 | 2026-09-25T00:30:38.250Z → 2026-11-01T00:34:49.878Z |
| [/business/plugins/audioscrape/](../../pages/openai.com/business/plugins/audioscrape/index.md) | 2 | 2 | 2026-09-25T00:06:32.998Z → 2026-11-01T01:17:23.853Z |
| [/business/plugins/autodesk-product-help/](../../pages/openai.com/business/plugins/autodesk-product-help/index.md) | 2 | 2 | 2026-09-25T00:33:36.767Z → 2026-11-01T01:17:15.856Z |
| [/business/plugins/base44/](../../pages/openai.com/business/plugins/base44/index.md) | 2 | 2 | 2026-09-25T00:37:45.053Z → 2026-11-01T00:37:01.825Z |
| [/business/plugins/biorender/](../../pages/openai.com/business/plugins/biorender/index.md) | 2 | 2 | 2026-09-25T00:34:53.955Z → 2026-11-01T01:47:00.864Z |
| [/business/plugins/boardwise/](../../pages/openai.com/business/plugins/boardwise/index.md) | 2 | 2 | 2026-09-24T23:59:00.742Z → 2026-10-31T19:54:08.944Z |
| [/business/plugins/calendly/](../../pages/openai.com/business/plugins/calendly/index.md) | 2 | 2 | 2026-09-25T00:35:00.076Z → 2026-11-17T21:36:07.435Z |
| [/business/plugins/clickhouse/](../../pages/openai.com/business/plugins/clickhouse/index.md) | 2 | 2 | 2026-09-25T00:37:32.491Z → 2026-11-01T05:07:23.226Z |
| [/business/plugins/close/](../../pages/openai.com/business/plugins/close/index.md) | 2 | 2 | 2026-09-25T00:20:07.821Z → 2026-11-17T00:00:57.676Z |
| [/business/plugins/coursera-learning/](../../pages/openai.com/business/plugins/coursera-learning/index.md) | 2 | 2 | 2026-09-25T00:36:17.561Z → 2026-11-01T04:45:25.169Z |
| [/business/plugins/courtroom5/](../../pages/openai.com/business/plugins/courtroom5/index.md) | 2 | 2 | 2026-09-24T23:59:33.167Z → 2026-10-31T20:56:25.783Z |
| [/business/plugins/creative-production/](../../pages/openai.com/business/plugins/creative-production/index.md) | 2 | 2 | 2026-09-25T00:29:53.587Z → 2026-11-01T04:31:31.239Z |
| [/business/plugins/datadog-experiments/](../../pages/openai.com/business/plugins/datadog-experiments/index.md) | 2 | 2 | 2026-09-25T00:29:41.630Z → 2026-11-01T03:56:15.567Z |
| [/business/plugins/datasite/](../../pages/openai.com/business/plugins/datasite/index.md) | 2 | 2 | 2026-09-25T00:36:27.552Z → 2026-11-01T03:54:11.366Z |
| [/business/plugins/definely/](../../pages/openai.com/business/plugins/definely/index.md) | 2 | 2 | 2026-09-25T00:14:10.269Z → 2026-11-01T00:31:06.624Z |
| [/business/plugins/demandbase/](../../pages/openai.com/business/plugins/demandbase/index.md) | 2 | 2 | 2026-09-25T00:29:39.026Z → 2026-11-17T00:02:03.129Z |
| [/business/plugins/docusign/](../../pages/openai.com/business/plugins/docusign/index.md) | 2 | 2 | 2026-09-25T00:30:20.742Z → 2026-11-17T21:35:49.339Z |
| [/business/plugins/dropbox-dash/](../../pages/openai.com/business/plugins/dropbox-dash/index.md) | 2 | 2 | 2026-09-25T00:34:12.775Z → 2026-11-17T21:36:05.008Z |
| [/business/plugins/easyreply/](../../pages/openai.com/business/plugins/easyreply/index.md) | 2 | 2 | 2026-09-25T00:18:00.280Z → 2026-11-17T21:36:05.750Z |
| [/business/plugins/exa/](../../pages/openai.com/business/plugins/exa/index.md) | 2 | 2 | 2026-09-25T00:06:27.758Z → 2026-11-01T01:37:36.062Z |
| [/business/plugins/foreflight-mobile/](../../pages/openai.com/business/plugins/foreflight-mobile/index.md) | 2 | 2 | 2026-09-25T00:32:41.542Z → 2026-11-17T21:36:04.156Z |
| [/business/plugins/gc-ai/](../../pages/openai.com/business/plugins/gc-ai/index.md) | 2 | 2 | 2026-09-25T00:23:20.438Z → 2026-10-31T20:28:37.526Z |
| [/business/plugins/gitbook/](../../pages/openai.com/business/plugins/gitbook/index.md) | 2 | 2 | 2026-09-25T00:32:02.896Z → 2026-11-01T07:59:32.174Z |
| [/business/plugins/gleap/](../../pages/openai.com/business/plugins/gleap/index.md) | 2 | 2 | 2026-09-25T00:34:25.392Z → 2026-11-01T03:32:42.821Z |
| [/business/plugins/gong/](../../pages/openai.com/business/plugins/gong/index.md) | 2 | 2 | 2026-09-25T00:25:47.031Z → 2026-11-16T23:58:43.036Z |
| [/business/plugins/granola/](../../pages/openai.com/business/plugins/granola/index.md) | 2 | 2 | 2026-09-25T00:35:12.376Z → 2026-11-17T21:36:04.555Z |
| [/business/plugins/harvey/](../../pages/openai.com/business/plugins/harvey/index.md) | 2 | 2 | 2026-09-25T00:33:47.213Z → 2026-11-01T04:22:39.758Z |
| [/business/plugins/honeybook/](../../pages/openai.com/business/plugins/honeybook/index.md) | 2 | 2 | 2026-09-25T00:36:59.422Z → 2026-11-01T09:16:39.118Z |
| [/business/plugins/hunter/](../../pages/openai.com/business/plugins/hunter/index.md) | 2 | 2 | 2026-09-25T00:31:03.276Z → 2026-11-16T23:53:50.162Z |
| [/business/plugins/imanage-work/](../../pages/openai.com/business/plugins/imanage-work/index.md) | 2 | 2 | 2026-09-25T00:34:19.572Z → 2026-11-17T21:36:03.171Z |
| [/business/plugins/laurel/](../../pages/openai.com/business/plugins/laurel/index.md) | 2 | 2 | 2026-09-25T00:16:17.596Z → 2026-11-01T02:58:24.475Z |
| [/business/plugins/legal-data-hunter/](../../pages/openai.com/business/plugins/legal-data-hunter/index.md) | 2 | 2 | 2026-09-25T00:07:16.897Z → 2026-11-01T02:30:03.699Z |
| [/business/plugins/legalzoom/](../../pages/openai.com/business/plugins/legalzoom/index.md) | 2 | 2 | 2026-09-25T00:29:21.843Z → 2026-11-01T02:29:48.209Z |
| [/business/plugins/linkedin/](../../pages/openai.com/business/plugins/linkedin/index.md) | 2 | 2 | 2026-09-25T00:31:58.496Z → 2026-11-17T21:36:20.707Z |
| [/business/plugins/malwarebytes/](../../pages/openai.com/business/plugins/malwarebytes/index.md) | 2 | 2 | 2026-09-25T00:33:56.525Z → 2026-11-01T00:47:44.006Z |
| [/business/plugins/manus/](../../pages/openai.com/business/plugins/manus/index.md) | 2 | 2 | 2026-09-25T00:09:00.730Z → 2026-11-01T03:54:58.022Z |
| [/business/plugins/mixpanel/](../../pages/openai.com/business/plugins/mixpanel/index.md) | 2 | 2 | 2026-09-25T00:37:04.025Z → 2026-11-01T01:22:07.719Z |
| [/business/plugins/motherduck/](../../pages/openai.com/business/plugins/motherduck/index.md) | 2 | 2 | 2026-09-25T00:29:46.746Z → 2026-11-01T01:03:09.822Z |
| [/business/plugins/namecheap/](../../pages/openai.com/business/plugins/namecheap/index.md) | 2 | 2 | 2026-09-25T00:35:37.917Z → 2026-11-01T05:39:39.575Z |
| [/business/plugins/opera-browser-connector/](../../pages/openai.com/business/plugins/opera-browser-connector/index.md) | 2 | 2 | 2026-09-25T00:15:07.434Z → 2026-11-17T21:36:01.515Z |
| [/business/plugins/otter-ai/](../../pages/openai.com/business/plugins/otter-ai/index.md) | 2 | 2 | 2026-09-25T00:30:12.290Z → 2026-11-17T21:36:01.462Z |
| [/business/plugins/patlytics/](../../pages/openai.com/business/plugins/patlytics/index.md) | 2 | 2 | 2026-09-25T00:10:59.552Z → 2026-11-01T03:59:39.253Z |
| [/business/plugins/paypal/](../../pages/openai.com/business/plugins/paypal/index.md) | 2 | 2 | 2026-09-25T00:35:28.002Z → 2026-11-01T03:10:25.944Z |
| [/business/plugins/pendo/](../../pages/openai.com/business/plugins/pendo/index.md) | 2 | 2 | 2026-09-25T00:30:34.762Z → 2026-11-01T01:40:21.096Z |
| [/business/plugins/planning-center/](../../pages/openai.com/business/plugins/planning-center/index.md) | 2 | 2 | 2026-09-25T00:18:02.075Z → 2026-11-01T05:07:32.034Z |
| [/business/plugins/product-design/](../../pages/openai.com/business/plugins/product-design/index.md) | 2 | 2 | 2026-09-25T00:32:42.549Z → 2026-11-01T01:13:16.425Z |
| [/business/plugins/pylon/](../../pages/openai.com/business/plugins/pylon/index.md) | 2 | 2 | 2026-09-25T00:41:34.557Z → 2026-11-01T03:10:36.627Z |
| [/business/plugins/read-ai/](../../pages/openai.com/business/plugins/read-ai/index.md) | 2 | 2 | 2026-09-25T00:32:20.280Z → 2026-11-17T21:35:59.256Z |
| [/business/plugins/resend/](../../pages/openai.com/business/plugins/resend/index.md) | 2 | 2 | 2026-09-25T00:40:05.362Z → 2026-11-01T05:19:05.046Z |
| [/business/plugins/sanity/](../../pages/openai.com/business/plugins/sanity/index.md) | 2 | 2 | 2026-09-25T00:36:18.224Z → 2026-11-01T00:41:54.848Z |
| [/business/plugins/scispace/](../../pages/openai.com/business/plugins/scispace/index.md) | 2 | 2 | 2026-09-25T00:06:43.386Z → 2026-11-18T20:22:36.213Z |
| [/business/plugins/scite/](../../pages/openai.com/business/plugins/scite/index.md) | 2 | 2 | 2026-09-25T00:05:59.446Z → 2026-11-18T20:22:50.650Z |
| [/business/plugins/sent/](../../pages/openai.com/business/plugins/sent/index.md) | 2 | 2 | 2026-09-25T00:17:12.612Z → 2026-11-01T03:16:17.775Z |
| [/business/plugins/similarweb/](../../pages/openai.com/business/plugins/similarweb/index.md) | 2 | 2 | 2026-09-25T00:30:49.415Z → 2026-11-01T04:53:01.169Z |
| [/business/plugins/slidesgpt/](../../pages/openai.com/business/plugins/slidesgpt/index.md) | 2 | 2 | 2026-09-25T00:06:19.832Z → 2026-11-17T21:35:57.958Z |
| [/business/plugins/statsig/](../../pages/openai.com/business/plugins/statsig/index.md) | 2 | 2 | 2026-09-25T00:37:08.999Z → 2026-11-01T00:18:43.779Z |
| [/business/plugins/superhuman-docs/](../../pages/openai.com/business/plugins/superhuman-docs/index.md) | 2 | 2 | 2026-09-25T00:34:26.615Z → 2026-11-17T21:35:57.214Z |
| [/business/plugins/superhuman-mail/](../../pages/openai.com/business/plugins/superhuman-mail/index.md) | 2 | 2 | 2026-09-25T00:31:33.826Z → 2026-11-17T21:35:55.962Z |
| [/business/plugins/support-ticket-validator/](../../pages/openai.com/business/plugins/support-ticket-validator/index.md) | 2 | 2 | 2026-09-25T00:17:27.858Z → 2026-11-17T21:35:56.781Z |
| [/business/plugins/thomson-reuters-highq/](../../pages/openai.com/business/plugins/thomson-reuters-highq/index.md) | 2 | 2 | 2026-09-25T00:37:41.061Z → 2026-11-17T21:35:55.974Z |
| [/business/plugins/thoughtspot-spotter/](../../pages/openai.com/business/plugins/thoughtspot-spotter/index.md) | 2 | 2 | 2026-09-25T00:33:51.410Z → 2026-11-01T00:51:10.456Z |
| [/business/plugins/thoughtspot/](../../pages/openai.com/business/plugins/thoughtspot/index.md) | 2 | 2 | 2026-09-25T00:31:29.989Z → 2026-11-01T05:02:17.131Z |
| [/business/plugins/ticktick/](../../pages/openai.com/business/plugins/ticktick/index.md) | 2 | 2 | 2026-09-25T00:32:46.873Z → 2026-11-17T21:35:57.135Z |
| [/business/plugins/trello/](../../pages/openai.com/business/plugins/trello/index.md) | 2 | 2 | 2026-09-25T02:32:15.915Z → 2026-11-17T21:35:56.622Z |
| [/business/plugins/typeform/](../../pages/openai.com/business/plugins/typeform/index.md) | 2 | 2 | 2026-09-25T02:50:07.285Z → 2026-11-01T07:46:50.488Z |
| [/business/plugins/unicourt/](../../pages/openai.com/business/plugins/unicourt/index.md) | 2 | 2 | 2026-09-25T00:00:50.002Z → 2026-11-01T08:50:32.821Z |
| [/business/plugins/ventor/](../../pages/openai.com/business/plugins/ventor/index.md) | 2 | 2 | 2026-09-25T03:55:07.727Z → 2026-10-31T20:03:33.320Z |
| [/business/plugins/visla-video-maker/](../../pages/openai.com/business/plugins/visla-video-maker/index.md) | 2 | 2 | 2026-09-25T04:22:11.360Z → 2026-11-01T02:57:37.954Z |
| [/business/plugins/whimsical/](../../pages/openai.com/business/plugins/whimsical/index.md) | 2 | 2 | 2026-09-25T20:33:25.410Z → 2026-11-17T21:36:10.482Z |
| [/business/plugins/wisdomai/](../../pages/openai.com/business/plugins/wisdomai/index.md) | 2 | 2 | 2026-09-25T23:49:12.470Z → 2026-11-01T02:11:49.031Z |
| [/business/plugins/wispr-flow/](../../pages/openai.com/business/plugins/wispr-flow/index.md) | 2 | 2 | 2026-09-25T23:36:23.641Z → 2026-11-17T21:35:55.596Z |
| [/business/plugins/xmind/](../../pages/openai.com/business/plugins/xmind/index.md) | 2 | 2 | 2026-09-25T20:35:38.875Z → 2026-11-17T21:35:55.221Z |
| [/business/plugins/zendesk/](../../pages/openai.com/business/plugins/zendesk/index.md) | 2 | 2 | 2026-09-25T20:49:34.091Z → 2026-11-18T20:27:07.806Z |
| [/business/plugins/zoom-revenue-accelerator/](../../pages/openai.com/business/plugins/zoom-revenue-accelerator/index.md) | 2 | 2 | 2026-09-25T21:40:14.469Z → 2026-11-17T00:00:20.411Z |
| [/business/plugins/](../../pages/openai.com/business/plugins/index.md) | 2 | 2 | 2026-09-25T18:54:49.105Z → 2026-11-17T22:31:32.841Z |
| [/business/plugins/ahrefs/](../../pages/openai.com/business/plugins/ahrefs/index.md) | 2 | 2 | 2026-09-25T00:30:51.959Z → 2026-10-31T19:57:48.416Z |
| [/business/plugins/ai-video-maker/](../../pages/openai.com/business/plugins/ai-video-maker/index.md) | 2 | 2 | 2026-09-25T00:17:21.700Z → 2026-11-01T03:34:54.743Z |
| [/business/plugins/ai-voice-generator/](../../pages/openai.com/business/plugins/ai-voice-generator/index.md) | 2 | 2 | 2026-09-25T00:29:36.828Z → 2026-11-01T04:28:36.373Z |
| [/business/plugins/aiera/](../../pages/openai.com/business/plugins/aiera/index.md) | 2 | 2 | 2026-09-25T00:37:49.242Z → 2026-10-31T21:00:36.380Z |
| [/business/plugins/alpha-vantage/](../../pages/openai.com/business/plugins/alpha-vantage/index.md) | 2 | 2 | 2026-09-25T00:35:28.130Z → 2026-11-01T08:11:21.458Z |
| [/business/plugins/ashby/](../../pages/openai.com/business/plugins/ashby/index.md) | 2 | 2 | 2026-09-25T00:06:51.226Z → 2026-11-01T03:39:02.705Z |
| [/business/plugins/aws-data-analytics/](../../pages/openai.com/business/plugins/aws-data-analytics/index.md) | 2 | 2 | 2026-09-25T00:29:38.457Z → 2026-11-01T04:26:50.462Z |
| [/business/plugins/binance/](../../pages/openai.com/business/plugins/binance/index.md) | 2 | 2 | 2026-09-25T00:34:42.736Z → 2026-11-01T04:10:43.509Z |
| [/business/plugins/browser-use/](../../pages/openai.com/business/plugins/browser-use/index.md) | 2 | 2 | 2026-09-25T00:34:18.710Z → 2026-11-17T21:36:07.925Z |
| [/business/plugins/catalyst-by-zoho/](../../pages/openai.com/business/plugins/catalyst-by-zoho/index.md) | 2 | 2 | 2026-09-25T00:31:56.360Z → 2026-11-01T00:33:55.842Z |
| [/business/plugins/circleback/](../../pages/openai.com/business/plugins/circleback/index.md) | 2 | 2 | 2026-09-25T00:07:01.445Z → 2026-11-17T21:36:07.009Z |
| [/business/plugins/coda/](../../pages/openai.com/business/plugins/coda/index.md) | 2 | 2 | 2026-09-25T00:35:19.298Z → 2026-11-17T21:36:07.441Z |
| [/business/plugins/coingecko/](../../pages/openai.com/business/plugins/coingecko/index.md) | 2 | 2 | 2026-09-25T00:06:49.284Z → 2026-10-31T20:08:43.116Z |
| [/business/plugins/consolio-aurora/](../../pages/openai.com/business/plugins/consolio-aurora/index.md) | 2 | 2 | 2026-09-25T00:05:56.036Z → 2026-10-31T22:45:24.053Z |
| [/business/plugins/context7/](../../pages/openai.com/business/plugins/context7/index.md) | 2 | 2 | 2026-09-25T00:30:33.615Z → 2026-11-01T05:11:42.572Z |
| [/business/plugins/courtlistener/](../../pages/openai.com/business/plugins/courtlistener/index.md) | 2 | 2 | 2026-09-25T00:18:27.875Z → 2026-10-31T23:30:44.795Z |
| [/business/plugins/datadog/](../../pages/openai.com/business/plugins/datadog/index.md) | 2 | 2 | 2026-09-25T00:40:38.780Z → 2026-11-01T05:30:06.178Z |
| [/business/plugins/descrybe/](../../pages/openai.com/business/plugins/descrybe/index.md) | 2 | 2 | 2026-09-25T00:01:27.284Z → 2026-11-01T05:44:17.553Z |
| [/business/plugins/elicit/](../../pages/openai.com/business/plugins/elicit/index.md) | 2 | 2 | 2026-09-25T00:37:21.736Z → 2026-11-18T20:25:19.810Z |
| [/business/plugins/factset/](../../pages/openai.com/business/plugins/factset/index.md) | 2 | 2 | 2026-09-25T00:26:06.519Z → 2026-11-01T00:56:20.305Z |
| [/business/plugins/helium-10/](../../pages/openai.com/business/plugins/helium-10/index.md) | 2 | 2 | 2026-09-25T00:14:08.746Z → 2026-11-01T04:32:41.917Z |
| [/business/plugins/hostinger-mail/](../../pages/openai.com/business/plugins/hostinger-mail/index.md) | 2 | 2 | 2026-09-25T00:33:59.604Z → 2026-11-17T21:36:03.208Z |
| [/business/plugins/instantly-ai/](../../pages/openai.com/business/plugins/instantly-ai/index.md) | 2 | 2 | 2026-09-25T00:29:16.658Z → 2026-11-16T23:52:51.814Z |
| [/business/plugins/jobtread/](../../pages/openai.com/business/plugins/jobtread/index.md) | 2 | 2 | 2026-09-25T00:18:16.071Z → 2026-11-01T03:29:39.439Z |
| [/business/plugins/lattice/](../../pages/openai.com/business/plugins/lattice/index.md) | 2 | 2 | 2026-09-25T00:35:27.526Z → 2026-11-01T02:52:42.419Z |
| [/business/plugins/lawve-ai/](../../pages/openai.com/business/plugins/lawve-ai/index.md) | 2 | 2 | 2026-09-25T00:03:50.167Z → 2026-11-01T01:09:07.214Z |
| [/business/plugins/legora/](../../pages/openai.com/business/plugins/legora/index.md) | 2 | 2 | 2026-09-25T00:35:56.799Z → 2026-11-01T05:35:42.768Z |
| [/business/plugins/linkedin-ads/](../../pages/openai.com/business/plugins/linkedin-ads/index.md) | 2 | 2 | 2026-09-25T00:24:45.856Z → 2026-11-01T04:24:49.439Z |
| [/business/plugins/longbridge/](../../pages/openai.com/business/plugins/longbridge/index.md) | 2 | 2 | 2026-09-25T00:19:29.943Z → 2026-11-01T03:35:53.555Z |
| [/business/plugins/mailerlite/](../../pages/openai.com/business/plugins/mailerlite/index.md) | 2 | 2 | 2026-09-25T00:17:31.225Z → 2026-10-31T23:45:07.274Z |
| [/business/plugins/metaview/](../../pages/openai.com/business/plugins/metaview/index.md) | 2 | 2 | 2026-09-25T00:06:52.796Z → 2026-11-01T05:08:03.995Z |
| [/business/plugins/muninx/](../../pages/openai.com/business/plugins/muninx/index.md) | 2 | 2 | 2026-09-25T00:15:48.874Z → 2026-11-01T08:49:55.209Z |
| [/business/plugins/omnisend/](../../pages/openai.com/business/plugins/omnisend/index.md) | 2 | 2 | 2026-09-25T00:06:48.214Z → 2026-11-01T03:48:01.999Z |
| [/business/plugins/plaud/](../../pages/openai.com/business/plugins/plaud/index.md) | 2 | 2 | 2026-09-25T00:18:03.506Z → 2026-11-17T21:36:11.459Z |
| [/business/plugins/qbo-connector-by-meridian/](../../pages/openai.com/business/plugins/qbo-connector-by-meridian/index.md) | 2 | 2 | 2026-09-25T00:06:58.154Z → 2026-10-31T19:57:27.678Z |
| [/business/plugins/railway/](../../pages/openai.com/business/plugins/railway/index.md) | 2 | 2 | 2026-09-25T00:34:45.025Z → 2026-11-01T02:49:48.655Z |
| [/business/plugins/se-ranking/](../../pages/openai.com/business/plugins/se-ranking/index.md) | 2 | 2 | 2026-09-25T00:30:21.287Z → 2026-11-01T02:57:54.261Z |
| [/business/plugins/shutterstock/](../../pages/openai.com/business/plugins/shutterstock/index.md) | 2 | 2 | 2026-09-25T00:35:10.688Z → 2026-10-31T19:53:54.609Z |
| [/business/plugins/smartsheet-us/](../../pages/openai.com/business/plugins/smartsheet-us/index.md) | 2 | 2 | 2026-09-25T00:37:15.500Z → 2026-11-17T21:35:57.436Z |
| [/business/plugins/supabase/](../../pages/openai.com/business/plugins/supabase/index.md) | 2 | 2 | 2026-09-25T00:30:03.467Z → 2026-11-01T03:42:02.479Z |
| [/business/plugins/the-l-suite-lloyd/](../../pages/openai.com/business/plugins/the-l-suite-lloyd/index.md) | 2 | 2 | 2026-09-25T00:04:56.595Z → 2026-11-01T08:07:58.185Z |
| [/business/plugins/the-l-suite-topcounsel/](../../pages/openai.com/business/plugins/the-l-suite-topcounsel/index.md) | 2 | 2 | 2026-09-25T00:02:35.150Z → 2026-11-01T02:24:12.207Z |
| [/business/plugins/third-bridge/](../../pages/openai.com/business/plugins/third-bridge/index.md) | 2 | 2 | 2026-09-25T00:29:41.097Z → 2026-11-01T03:54:23.169Z |
| [/business/plugins/unthread/](../../pages/openai.com/business/plugins/unthread/index.md) | 2 | 2 | 2026-09-25T03:28:31.722Z → 2026-11-01T07:18:47.247Z |
| [/business/plugins/vanta/](../../pages/openai.com/business/plugins/vanta/index.md) | 2 | 2 | 2026-09-25T03:28:59.417Z → 2026-11-01T03:10:06.208Z |
| [/business/plugins/webflow/](../../pages/openai.com/business/plugins/webflow/index.md) | 2 | 2 | 2026-09-25T20:03:23.942Z → 2026-11-01T05:45:26.012Z |
| [/business/plugins/wolfram/](../../pages/openai.com/business/plugins/wolfram/index.md) | 2 | 2 | 2026-09-25T21:57:01.993Z → 2026-11-01T03:49:49.413Z |
| [/business/plugins/workable/](../../pages/openai.com/business/plugins/workable/index.md) | 2 | 2 | 2026-09-25T21:55:04.138Z → 2026-11-01T03:58:45.330Z |
| [/business/plugins/wpvibe/](../../pages/openai.com/business/plugins/wpvibe/index.md) | 2 | 2 | 2026-09-25T21:55:25.962Z → 2026-11-01T00:17:02.988Z |
| [/index/hebbia/](../../pages/openai.com/index/hebbia/index.md) | 4 | 0 | 2026-06-02T15:02:01.483Z → 2026-10-30T05:29:46.205Z |
| [/business/plugins/aws-core/](../../pages/openai.com/business/plugins/aws-core/index.md) | 2 | 2 | 2026-09-25T00:31:03.826Z → 2026-11-01T01:08:31.297Z |
| [/business/plugins/elevenlabs/](../../pages/openai.com/business/plugins/elevenlabs/index.md) | 2 | 2 | 2026-09-25T00:41:47.419Z → 2026-11-17T21:36:06.174Z |
| [/business/plugins/financial-datasets/](../../pages/openai.com/business/plugins/financial-datasets/index.md) | 2 | 2 | 2026-09-25T00:06:15.054Z → 2026-11-01T02:14:19.626Z |
| [/business/plugins/massive/](../../pages/openai.com/business/plugins/massive/index.md) | 2 | 2 | 2026-09-25T00:13:40.657Z → 2026-11-01T03:18:54.782Z |
| [/business/plugins/metricool/](../../pages/openai.com/business/plugins/metricool/index.md) | 2 | 2 | 2026-09-25T00:18:15.471Z → 2026-11-01T01:52:11.936Z |
| [/business/plugins/netsuite/](../../pages/openai.com/business/plugins/netsuite/index.md) | 2 | 2 | 2026-09-25T00:26:40.391Z → 2026-11-01T02:51:40.699Z |
| [/business/plugins/quartr/](../../pages/openai.com/business/plugins/quartr/index.md) | 2 | 2 | 2026-09-25T00:06:38.172Z → 2026-11-01T04:18:05.109Z |
| [/business/plugins/sp-global-deterministic/](../../pages/openai.com/business/plugins/sp-global-deterministic/index.md) | 2 | 2 | 2026-09-25T00:30:04.463Z → 2026-10-31T23:25:26.836Z |
| [/index/building-codex-windows-sandbox/](../../pages/openai.com/index/building-codex-windows-sandbox/index.md) | 0 | 4 | 2026-09-22T09:51:50.755Z → 2026-11-18T19:25:35.729Z |
| [/index/paradigm/](../../pages/openai.com/index/paradigm/index.md) | 2 | 2 | 2026-08-08T04:26:08.551Z → 2026-11-03T16:37:52.431Z |
| [/solutions/use-case/research/](../../pages/openai.com/solutions/use-case/research/index.md) | 2 | 2 | 2026-09-07T16:35:01.305Z → 2026-10-23T09:22:37.421Z |
| [/index/hello-gpt-4o/](../../pages/openai.com/index/hello-gpt-4o/index.md) | 2 | 2 | 2026-09-25T19:18:10.622Z → 2026-11-18T00:08:39.434Z |
| [/index/small-business-stories/](../../pages/openai.com/index/small-business-stories/index.md) | 3 | 1 | 2026-09-08T20:26:10.630Z → 2026-11-03T21:27:19.000Z |
| [/solutions/use-case/coding/](../../pages/openai.com/solutions/use-case/coding/index.md) | 2 | 2 | 2026-09-07T16:35:44.230Z → 2026-10-23T09:27:16.979Z |
| [/business/contact-sales-legal/](../../pages/openai.com/business/contact-sales-legal/index.md) | 2 | 2 | 2026-09-24T19:10:19.298Z → 2026-11-19T10:09:22.237Z |
| [/business/partners/aws/](../../pages/openai.com/business/partners/aws/index.md) | 2 | 2 | 2026-09-19T00:59:47.677Z → 2026-10-29T08:25:46.981Z |
| [/form/aardvark-beta-signup/](../../pages/openai.com/form/aardvark-beta-signup/index.md) | 2 | 2 | 2026-06-14T10:47:40.588Z → 2026-10-08T17:07:05.319Z |
| [/index/advancing-content-provenance/](../../pages/openai.com/index/advancing-content-provenance/index.md) | 3 | 1 | 2026-09-25T18:57:15.666Z → 2026-11-03T18:05:57.025Z |
| [/index/chatgpt-can-now-see-hear-and-speak/](../../pages/openai.com/index/chatgpt-can-now-see-hear-and-speak/index.md) | 0 | 4 | 2026-07-28T20:38:10.162Z → 2026-11-03T04:38:37.350Z |
| [/index/chatgpt-for-your-most-ambitious-work/](../../pages/openai.com/index/chatgpt-for-your-most-ambitious-work/index.md) | 4 | 0 | 2026-09-28T04:18:07.366Z → 2026-11-19T22:40:53.851Z |
| [/index/clay/](../../pages/openai.com/index/clay/index.md) | 2 | 2 | 2026-06-22T23:12:20.685Z → 2026-10-30T09:00:53.034Z |
| [/index/gpt-5-6-frontier-intelligence-efficiency/](../../pages/openai.com/index/gpt-5-6-frontier-intelligence-efficiency/index.md) | 0 | 4 | 2026-09-27T19:25:08.137Z → 2026-11-18T13:50:36.229Z |
| [/index/how-two-settings-tripled-our-arc-agi-3-scores/](../../pages/openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/index.md) | 2 | 2 | 2026-09-25T19:18:41.636Z → 2026-11-18T17:22:04.528Z |
| [/index/introducing-chatgpt-and-whisper-apis/](../../pages/openai.com/index/introducing-chatgpt-and-whisper-apis/index.md) | 2 | 2 | 2026-09-23T20:42:08.942Z → 2026-10-21T10:51:09.093Z |
| [/index/new-embedding-models-and-api-updates/](../../pages/openai.com/index/new-embedding-models-and-api-updates/index.md) | 2 | 2 | 2026-09-23T20:42:09.920Z → 2026-10-22T01:49:21.342Z |
| [/index/openai-o1-system-card/](../../pages/openai.com/index/openai-o1-system-card/index.md) | 2 | 2 | 2026-08-30T07:51:42.580Z → 2026-10-19T07:19:44.749Z |
| [/index/zalando/](../../pages/openai.com/index/zalando/index.md) | 2 | 2 | 2026-08-20T22:21:40.738Z → 2026-11-17T23:56:45.021Z |
| [/policies/openai-cve-assignment-policy/](../../pages/openai.com/policies/openai-cve-assignment-policy/index.md) | 2 | 2 | 2026-08-13T23:23:40.237Z → 2026-10-30T20:54:00.941Z |
| [/policies/sharing-publication-policy/](../../pages/openai.com/policies/sharing-publication-policy/index.md) | 2 | 2 | 2026-07-07T07:42:57.432Z → 2026-10-15T08:18:26.306Z |
| [/policies/us-privacy-policy/](../../pages/openai.com/policies/us-privacy-policy/index.md) | 2 | 2 | 2026-09-10T23:48:43.430Z → 2026-11-03T18:32:08.323Z |
| [/solutions/use-case/agents/](../../pages/openai.com/solutions/use-case/agents/index.md) | 2 | 2 | 2026-09-07T16:35:45.449Z → 2026-10-23T10:31:17.157Z |
| [/index/robots-that-learn/](../../pages/openai.com/index/robots-that-learn/index.md) | 3 | 0 | 2026-06-03T04:01:28.194Z → 2026-10-21T03:34:31.668Z |
| [/index/generalizing-from-simulation/](../../pages/openai.com/index/generalizing-from-simulation/index.md) | 3 | 0 | 2026-06-03T04:00:02.633Z → 2026-10-20T18:13:49.286Z |
| [/index/data-partnerships/](../../pages/openai.com/index/data-partnerships/index.md) | 3 | 0 | 2026-05-29T00:26:22.983Z → 2026-11-20T00:08:35.917Z |
| [/index/learning-to-cooperate-compete-and-communicate/](../../pages/openai.com/index/learning-to-cooperate-compete-and-communicate/index.md) | 3 | 0 | 2026-06-03T03:59:55.989Z → 2026-10-20T10:54:03.578Z |
| [/index/the-international-2018-results/](../../pages/openai.com/index/the-international-2018-results/index.md) | 3 | 0 | 2026-06-03T04:02:09.185Z → 2026-10-21T04:37:09.933Z |
| [/business/why-openai/enterprises/](../../pages/openai.com/business/why-openai/enterprises/index.md) | 0 | 3 | 2026-09-11T20:42:22.962Z → 2026-11-03T21:30:44.712Z |
| [/index/altera/](../../pages/openai.com/index/altera/index.md) | 1 | 2 | 2026-06-22T23:13:04.537Z → 2026-10-30T07:57:17.624Z |
| [/index/genmab/](../../pages/openai.com/index/genmab/index.md) | 2 | 1 | 2026-08-18T18:40:53.176Z → 2026-11-17T23:56:54.283Z |
| [/o1/](../../pages/openai.com/o1/index.md) | 3 | 0 | 2026-09-25T19:18:38.674Z → 2026-11-04T20:10:33.430Z |
| [/business/solutions/finance/](../../pages/openai.com/business/solutions/finance/index.md) | 0 | 3 | 2026-09-24T19:14:05.833Z → 2026-11-21T15:01:14.046Z |
| [/business/partners/accenture/](../../pages/openai.com/business/partners/accenture/index.md) | 2 | 1 | 2026-08-24T17:39:22.820Z → 2026-11-20T23:16:38.904Z |
| [/business/partners/bain-and-company/](../../pages/openai.com/business/partners/bain-and-company/index.md) | 2 | 1 | 2026-08-24T18:16:50.662Z → 2026-11-20T23:16:09.550Z |
| [/index/endex/](../../pages/openai.com/index/endex/index.md) | 1 | 2 | 2026-06-14T04:10:47.603Z → 2026-10-30T00:44:21.597Z |
| [/index/openai-o1-mini-advancing-cost-efficient-reasoning/](../../pages/openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/index.md) | 3 | 0 | 2026-08-19T00:21:16.272Z → 2026-10-24T00:24:47.792Z |
| [/news/ai-adoption/](../../pages/openai.com/news/ai-adoption/index.md) | 1 | 2 | 2026-09-25T18:59:35.767Z → 2026-11-16T21:32:11.592Z |
| [/business/partners/cognita-reply/](../../pages/openai.com/business/partners/cognita-reply/index.md) | 2 | 1 | 2026-08-24T17:39:26.101Z → 2026-11-20T23:16:02.124Z |
| [/index/chatgpt-for-academic-researchers/](../../pages/openai.com/index/chatgpt-for-academic-researchers/index.md) | 1 | 2 | 2026-09-28T00:08:14.754Z → 2026-11-18T13:50:45.274Z |
| [/index/putting-frontier-cyber-models-in-more-trusted-hands/](../../pages/openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands/index.md) | 2 | 1 | 2026-09-25T19:16:31.227Z → 2026-11-18T19:25:17.150Z |
| [/collective-cyberdefense/application/](../../pages/openai.com/collective-cyberdefense/application/index.md) | 3 | 0 | 2026-09-25T19:16:24.019Z → 2026-11-18T19:25:15.668Z |
| [/global-affairs/testimony-of-sam-altman-before-the-us-senate/](../../pages/openai.com/global-affairs/testimony-of-sam-altman-before-the-us-senate/index.md) | 2 | 1 | 2026-07-25T07:08:56.558Z → 2026-11-03T14:00:23.183Z |
| [/index/introducing-gpt-6-sol-and-luna/](../../pages/openai.com/index/introducing-gpt-6-sol-and-luna/index.md) | 3 | 0 | 2026-09-28T09:11:53.457Z → 2026-11-17T23:58:58.484Z |
| [/index/yabble/](../../pages/openai.com/index/yabble/index.md) | 1 | 2 | 2026-06-22T23:12:30.390Z → 2026-11-03T18:17:36.867Z |
| [/policies/chatgpt-sites-terms/](../../pages/openai.com/policies/chatgpt-sites-terms/index.md) | 1 | 2 | 2026-08-13T23:45:39.785Z → 2026-11-08T12:43:01.315Z |
| [/index/gpt-2-1-5b-release/](../../pages/openai.com/index/gpt-2-1-5b-release/index.md) | 2 | 0 | 2026-06-03T03:59:53.912Z → 2026-10-24T02:13:56.235Z |
| [/index/requests-for-research-2/](../../pages/openai.com/index/requests-for-research-2/index.md) | 2 | 0 | 2026-06-03T04:00:45.678Z → 2026-10-23T23:40:19.672Z |
| [/index/robust-adversarial-inputs/](../../pages/openai.com/index/robust-adversarial-inputs/index.md) | 2 | 0 | 2026-06-03T03:59:53.398Z → 2026-10-19T10:17:40.266Z |
| [/index/planning-for-agi-and-beyond/](../../pages/openai.com/index/planning-for-agi-and-beyond/index.md) | 2 | 0 | 2026-05-31T20:06:18.910Z → 2026-10-19T19:44:24.767Z |
| [/index/superalignment-fast-grants/](../../pages/openai.com/index/superalignment-fast-grants/index.md) | 2 | 0 | 2026-05-31T20:06:14.225Z → 2026-10-27T10:07:20.356Z |
| [/business/plugins/01-superdesign/](../../pages/openai.com/business/plugins/01-superdesign/index.md) | 1 | 1 | 2026-09-25T00:32:43.397Z → 2026-10-31T19:57:56.761Z |
| [/business/plugins/deepjudge/](../../pages/openai.com/business/plugins/deepjudge/index.md) | 1 | 1 | 2026-09-25T00:29:56.244Z → 2026-11-17T21:36:06.172Z |
| [/business/plugins/godaddy/](../../pages/openai.com/business/plugins/godaddy/index.md) | 1 | 1 | 2026-09-25T00:37:37.294Z → 2026-11-01T03:12:34.869Z |
| [/business/plugins/google-contacts/](../../pages/openai.com/business/plugins/google-contacts/index.md) | 1 | 1 | 2026-09-25T00:32:20.581Z → 2026-11-17T21:36:04.133Z |
| [/business/plugins/khan-academy/](../../pages/openai.com/business/plugins/khan-academy/index.md) | 1 | 1 | 2026-09-25T00:13:26.737Z → 2026-10-31T20:22:06.510Z |
| [/business/plugins/krisp/](../../pages/openai.com/business/plugins/krisp/index.md) | 1 | 1 | 2026-09-25T00:16:55.029Z → 2026-11-17T21:36:30.885Z |
| [/business/plugins/lecg-compliance-horizon-scanner/](../../pages/openai.com/business/plugins/lecg-compliance-horizon-scanner/index.md) | 1 | 1 | 2026-09-25T00:31:08.403Z → 2026-11-17T21:36:25.312Z |
| [/business/plugins/legalquants-companion/](../../pages/openai.com/business/plugins/legalquants-companion/index.md) | 1 | 1 | 2026-09-25T00:18:10.173Z → 2026-11-17T21:36:26.978Z |
| [/business/plugins/legalquants-transactional/](../../pages/openai.com/business/plugins/legalquants-transactional/index.md) | 1 | 1 | 2026-09-25T00:36:58.213Z → 2026-11-17T21:36:02.526Z |
| [/business/plugins/metabase/](../../pages/openai.com/business/plugins/metabase/index.md) | 1 | 1 | 2026-09-25T00:34:55.204Z → 2026-11-01T04:03:58.640Z |
| [/business/plugins/mixpanel-headless/](../../pages/openai.com/business/plugins/mixpanel-headless/index.md) | 1 | 1 | 2026-09-25T00:33:51.903Z → 2026-11-01T04:44:29.261Z |
| [/business/plugins/netdocuments/](../../pages/openai.com/business/plugins/netdocuments/index.md) | 1 | 1 | 2026-09-25T00:34:36.730Z → 2026-11-01T03:58:09.562Z |
| [/business/plugins/nvidia-skills/](../../pages/openai.com/business/plugins/nvidia-skills/index.md) | 1 | 1 | 2026-09-25T00:37:49.939Z → 2026-11-01T03:11:54.228Z |
| [/business/plugins/transkriptor/](../../pages/openai.com/business/plugins/transkriptor/index.md) | 1 | 1 | 2026-09-25T02:17:23.416Z → 2026-11-01T05:36:25.801Z |
| [/business/plugins/veed-video-generator/](../../pages/openai.com/business/plugins/veed-video-generator/index.md) | 1 | 1 | 2026-09-25T03:56:54.177Z → 2026-11-01T02:12:48.071Z |
| [/index/insights-from-global-conversations/](../../pages/openai.com/index/insights-from-global-conversations/index.md) | 2 | 0 | 2026-05-31T20:06:19.636Z → 2026-11-04T17:17:53.636Z |
| [/index/learning-from-human-preferences/](../../pages/openai.com/index/learning-from-human-preferences/index.md) | 2 | 0 | 2026-05-31T20:06:11.865Z → 2026-10-23T22:19:37.817Z |
| [/index/learning-to-model-other-minds/](../../pages/openai.com/index/learning-to-model-other-minds/index.md) | 2 | 0 | 2026-06-03T03:59:55.042Z → 2026-10-20T08:15:52.230Z |
| [/business/plugins/ai-graphic-design/](../../pages/openai.com/business/plugins/ai-graphic-design/index.md) | 1 | 1 | 2026-09-25T00:34:50.999Z → 2026-11-01T03:29:12.153Z |
| [/business/plugins/intapp-celeste/](../../pages/openai.com/business/plugins/intapp-celeste/index.md) | 1 | 1 | 2026-09-25T00:34:41.902Z → 2026-10-31T19:57:26.533Z |
| [/business/plugins/legalquants-litigation/](../../pages/openai.com/business/plugins/legalquants-litigation/index.md) | 1 | 1 | 2026-09-25T00:31:53.518Z → 2026-11-17T21:36:16.376Z |
| [/index/delivering-low-latency-voice-ai-at-scale/](../../pages/openai.com/index/delivering-low-latency-voice-ai-at-scale/index.md) | 1 | 1 | 2026-06-14T23:43:32.929Z → 2026-10-20T23:52:52.331Z |
| [/index/unrolling-the-codex-agent-loop/](../../pages/openai.com/index/unrolling-the-codex-agent-loop/index.md) | 1 | 1 | 2026-09-22T20:38:53.176Z → 2026-11-12T23:54:50.795Z |
| [/index/gpt-5-6/](../../pages/openai.com/index/gpt-5-6/index.md) | 2 | 0 | 2026-09-28T04:27:47.732Z → 2026-11-19T22:57:20.484Z |
| [/index/healthify/](../../pages/openai.com/index/healthify/index.md) | 1 | 1 | 2026-08-08T04:26:08.564Z → 2026-10-30T07:37:58.405Z |
| [/academy/brainstorming/](../../pages/openai.com/academy/brainstorming/index.md) | 1 | 1 | 2026-05-22T19:10:39.902Z → 2026-11-05T06:57:57.841Z |
| [/index/1-million-businesses-putting-ai-to-work/](../../pages/openai.com/index/1-million-businesses-putting-ai-to-work/index.md) | 1 | 1 | 2026-09-22T22:06:08.857Z → 2026-11-03T11:07:14.219Z |
| [/index/advancing-independent-research-ai-alignment/](../../pages/openai.com/index/advancing-independent-research-ai-alignment/index.md) | 1 | 1 | 2026-09-25T19:18:24.670Z → None |
| [/index/cna-walter-fernandez/](../../pages/openai.com/index/cna-walter-fernandez/index.md) | 1 | 1 | 2026-09-22T13:14:14.881Z → 2026-11-09T22:47:48.080Z |
| [/index/fighting-nyt-user-privacy-invasion/](../../pages/openai.com/index/fighting-nyt-user-privacy-invasion/index.md) | 1 | 1 | 2026-08-26T19:11:50.915Z → 2026-11-18T19:25:19.057Z |
| [/index/introducing-gpt-realtime/](../../pages/openai.com/index/introducing-gpt-realtime/index.md) | 1 | 1 | 2026-08-07T18:49:37.339Z → 2026-11-17T23:02:41.356Z |
| [/index/response-to-nyt-data-demands/](../../pages/openai.com/index/response-to-nyt-data-demands/index.md) | 1 | 1 | 2026-08-26T19:11:48.462Z → 2026-11-04T12:53:10.733Z |
| [/solutions/industries/law/](../../pages/openai.com/solutions/industries/law/index.md) | 2 | 0 | 2026-09-24T21:49:58.328Z → 2026-11-18T16:23:48.536Z |
| [/business/partners/kpmg/](../../pages/openai.com/business/partners/kpmg/index.md) | 1 | 1 | 2026-09-18T18:33:10.669Z → 2026-10-29T05:50:17.510Z |
| [/business/solutions/education/](../../pages/openai.com/business/solutions/education/index.md) | 1 | 1 | 2026-09-21T21:44:15.397Z → 2026-10-21T03:49:56.623Z |
| [/devday/2025/](../../pages/openai.com/devday/2025/index.md) | 1 | 1 | 2026-09-22T22:05:52.301Z → 2026-11-03T14:06:00.267Z |
| [/index/gpt-4/](../../pages/openai.com/index/gpt-4/index.md) | 1 | 1 | 2026-09-25T19:18:25.136Z → 2026-11-18T00:09:03.780Z |
| [/index/gpt-6-astra-next-generation-work/](../../pages/openai.com/index/gpt-6-astra-next-generation-work/index.md) | 2 | 0 | 2026-09-25T19:16:16.998Z → 2026-11-19T23:03:06.788Z |
| [/index/introducing-chatgpt-small-business-program/](../../pages/openai.com/index/introducing-chatgpt-small-business-program/index.md) | 1 | 1 | 2026-09-27T19:36:14.416Z → 2026-11-03T07:52:09.328Z |
| [/index/introducing-prism/](../../pages/openai.com/index/introducing-prism/index.md) | 2 | 0 | 2026-09-18T17:55:56.219Z → 2026-11-17T23:02:40.831Z |
| [/business/partners/altimetrik/](../../pages/openai.com/business/partners/altimetrik/index.md) | 2 | 0 | 2026-08-28T18:56:38.667Z → 2026-11-20T23:16:52.421Z |
| [/business/partners/altudo/](../../pages/openai.com/business/partners/altudo/index.md) | 1 | 1 | 2026-08-24T17:39:17.379Z → 2026-10-29T06:02:20.224Z |
| [/business/partners/chieftns/](../../pages/openai.com/business/partners/chieftns/index.md) | 1 | 1 | 2026-08-24T17:39:12.727Z → 2026-10-29T06:07:56.222Z |
| [/business/partners/eliza/](../../pages/openai.com/business/partners/eliza/index.md) | 2 | 0 | 2026-08-28T18:56:31.624Z → 2026-11-20T23:15:22.954Z |
| [/business/partners/epam/](../../pages/openai.com/business/partners/epam/index.md) | 1 | 1 | 2026-08-24T17:39:23.685Z → 2026-11-02T21:49:03.816Z |
| [/business/partners/sb-oai-japan-gk/](../../pages/openai.com/business/partners/sb-oai-japan-gk/index.md) | 1 | 1 | 2026-08-24T17:39:17.869Z → 2026-10-29T19:18:23.349Z |
| [/business/partners/sk-inc-ax/](../../pages/openai.com/business/partners/sk-inc-ax/index.md) | 1 | 1 | 2026-08-28T11:59:56.710Z → 2026-10-29T19:30:25.586Z |
| [/academy/what-is-ai/](../../pages/openai.com/academy/what-is-ai/index.md) | 1 | 1 | 2026-05-22T19:10:26.363Z → 2026-11-02T00:08:06.726Z |
| [/academy/writing/](../../pages/openai.com/academy/writing/index.md) | 1 | 1 | 2026-08-03T16:00:43.409Z → 2026-11-05T06:57:45.211Z |
| [/business-data/](../../pages/openai.com/business-data/index.md) | 1 | 1 | 2026-09-28T00:31:18.165Z → 2026-11-03T20:41:08.928Z |
| [/business/put-ai-to-work-automate-and-scale-financial-operations/](../../pages/openai.com/business/put-ai-to-work-automate-and-scale-financial-operations/index.md) | 1 | 1 | 2026-07-09T10:56:07.073Z → 2026-11-10T09:52:41.681Z |
| [/business/put-ai-to-work-for-marketing-teams/](../../pages/openai.com/business/put-ai-to-work-for-marketing-teams/index.md) | 1 | 1 | 2026-07-09T09:10:43.720Z → 2026-11-10T00:45:10.316Z |
| [/business/put-ai-to-work-lessons-from-hundreds-of-successful-deployments/](../../pages/openai.com/business/put-ai-to-work-lessons-from-hundreds-of-successful-deployments/index.md) | 1 | 1 | 2026-05-22T19:06:21.103Z → 2026-11-10T09:53:01.459Z |
| [/business/solutions/design/](../../pages/openai.com/business/solutions/design/index.md) | 1 | 1 | 2026-09-27T22:11:16.048Z → 2026-11-01T13:39:18.233Z |
| [/business/solutions/engineering/](../../pages/openai.com/business/solutions/engineering/index.md) | 1 | 1 | 2026-09-21T21:43:44.739Z → 2026-11-08T12:33:59.821Z |
| [/business/solving-complex-problems-with-openai-o1-models/](../../pages/openai.com/business/solving-complex-problems-with-openai-o1-models/index.md) | 1 | 1 | 2026-07-09T10:46:26.949Z → 2026-11-03T11:04:31.652Z |
| [/codex/for-work/](../../pages/openai.com/codex/for-work/index.md) | 1 | 1 | 2026-09-15T23:09:29.588Z → 2026-10-20T02:36:56.888Z |
| [/form/copyright-disputes/](../../pages/openai.com/form/copyright-disputes/index.md) | 2 | 0 | 2026-08-19T22:53:30.086Z → 2026-10-28T23:26:59.330Z |
| [/form/trademark-counterfeit-disputes/](../../pages/openai.com/form/trademark-counterfeit-disputes/index.md) | 1 | 1 | 2026-09-18T09:31:06.301Z → 2026-10-28T22:33:44.674Z |
| [/global-affairs/disrupting-malicious-uses-of-ai-october-2025/](../../pages/openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/index.md) | 1 | 1 | 2026-06-14T12:12:42.026Z → 2026-11-08T12:39:19.400Z |
| [/global-affairs/introducing-chatgpt-gov/](../../pages/openai.com/global-affairs/introducing-chatgpt-gov/index.md) | 2 | 0 | 2026-06-14T08:02:12.485Z → 2026-11-09T22:49:05.672Z |
| [/global-affairs/introducing-openai-for-government/](../../pages/openai.com/global-affairs/introducing-openai-for-government/index.md) | 2 | 0 | 2026-07-25T07:15:06.518Z → 2026-11-09T22:51:23.411Z |
| [/hugging-face-incident-and-misalignment/](../../pages/openai.com/hugging-face-incident-and-misalignment/index.md) | 1 | 1 | 2026-09-28T07:58:08.720Z → 2026-10-09T04:15:46.703Z |
| [/index/deep-research/](../../pages/openai.com/index/deep-research/index.md) | 1 | 1 | 2026-07-23T22:59:15.677Z → 2026-10-22T18:18:31.852Z |
| [/index/devday-2026/](../../pages/openai.com/index/devday-2026/index.md) | 2 | 0 | 2026-09-28T02:51:23.058Z → 2026-11-12T18:40:29.169Z |
| [/index/eliseai-minna-song/](../../pages/openai.com/index/eliseai-minna-song/index.md) | 1 | 1 | 2026-08-08T04:26:10.330Z → 2026-10-30T03:07:45.143Z |
| [/index/expanding-access-to-ai-with-chatgpt-ads/](../../pages/openai.com/index/expanding-access-to-ai-with-chatgpt-ads/index.md) | 1 | 1 | 2026-09-25T19:16:24.404Z → 2026-11-17T23:03:03.148Z |
| [/index/gpt-4-api-general-availability/](../../pages/openai.com/index/gpt-4-api-general-availability/index.md) | 1 | 1 | 2026-09-23T20:41:59.039Z → 2026-10-22T08:32:58.695Z |
| [/index/gpt-4o-and-more-tools-to-chatgpt-free/](../../pages/openai.com/index/gpt-4o-and-more-tools-to-chatgpt-free/index.md) | 1 | 1 | 2026-08-14T22:00:00.905Z → 2026-11-03T12:43:53.134Z |
| [/index/helping-build-shared-standards-for-advanced-ai/](../../pages/openai.com/index/helping-build-shared-standards-for-advanced-ai/index.md) | 1 | 1 | 2026-07-01T07:55:51.863Z → 2026-11-10T08:38:11.783Z |
| [/index/how-the-voices-for-chatgpt-were-chosen/](../../pages/openai.com/index/how-the-voices-for-chatgpt-were-chosen/index.md) | 1 | 1 | 2026-09-18T17:01:22.086Z → 2026-10-23T10:01:49.525Z |
| [/index/introducing-data-residency-in-asia/](../../pages/openai.com/index/introducing-data-residency-in-asia/index.md) | 1 | 1 | 2026-09-18T17:55:56.698Z → 2026-11-17T23:02:42.743Z |
| [/index/introducing-the-openai-economic-research-exchange/](../../pages/openai.com/index/introducing-the-openai-economic-research-exchange/index.md) | 1 | 1 | 2026-09-25T19:33:51.253Z → 2026-11-13T22:14:17.476Z |
| [/index/mavenagi/](../../pages/openai.com/index/mavenagi/index.md) | 1 | 1 | 2026-09-22T13:14:37.826Z → 2026-11-16T20:47:45.231Z |
| [/index/new-and-improved-embedding-model/](../../pages/openai.com/index/new-and-improved-embedding-model/index.md) | 1 | 1 | 2026-09-23T20:42:01.207Z → 2026-11-05T06:09:42.211Z |
| [/index/nubank/](../../pages/openai.com/index/nubank/index.md) | 1 | 1 | 2026-09-22T19:25:10.546Z → 2026-11-17T23:56:21.622Z |
| [/index/o1-and-new-tools-for-developers/](../../pages/openai.com/index/o1-and-new-tools-for-developers/index.md) | 1 | 1 | 2026-09-23T20:42:06.723Z → 2026-10-21T21:04:52.944Z |
| [/index/openai-raising-concerns-policy/](../../pages/openai.com/index/openai-raising-concerns-policy/index.md) | 2 | 0 | 2026-07-15T18:28:53.361Z → 2026-11-18T13:50:52.919Z |
| [/index/our-approach-to-ai-safety/](../../pages/openai.com/index/our-approach-to-ai-safety/index.md) | 1 | 1 | 2026-07-25T07:09:02.098Z → 2026-10-27T09:44:58.233Z |
| [/index/our-decision-on-cursor-following-its-acquisition-by-spacex/](../../pages/openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/index.md) | 2 | 0 | 2026-09-25T19:16:26.177Z → 2026-11-18T13:50:43.532Z |
| [/index/put-ai-to-work-for-your-product-team/](../../pages/openai.com/index/put-ai-to-work-for-your-product-team/index.md) | 1 | 1 | 2026-09-02T00:20:45.696Z → 2026-11-10T09:52:35.698Z |
| [/index/reimagining-advertising-with-ai/](../../pages/openai.com/index/reimagining-advertising-with-ai/index.md) | 1 | 1 | 2026-09-26T12:26:15.440Z → 2026-11-17T23:02:37.069Z |
| [/index/supporting-journalism-from-classrooms-to-newsrooms/](../../pages/openai.com/index/supporting-journalism-from-classrooms-to-newsrooms/index.md) | 1 | 1 | 2026-09-25T19:16:20.953Z → 2026-11-13T22:12:27.284Z |
| [/index/upwork/](../../pages/openai.com/index/upwork/index.md) | 1 | 1 | 2026-08-07T09:01:46.879Z → 2026-11-05T01:12:19.705Z |
| [/index/waymark/](../../pages/openai.com/index/waymark/index.md) | 1 | 1 | 2026-08-08T04:26:09.818Z → 2026-11-05T01:12:12.449Z |
| [/leads/startup/](../../pages/openai.com/leads/startup/index.md) | 1 | 1 | 2026-06-04T09:57:53.875Z → 2026-10-23T04:21:28.354Z |
| [/business/guides-and-resources/chatgpt-business-smb-guide/](../../pages/openai.com/business/guides-and-resources/chatgpt-business-smb-guide/index.md) | 1 | 0 | 2026-09-21T20:28:38.466Z → 2026-11-04T20:11:12.517Z |
| [/form/report-content/](../../pages/openai.com/form/report-content/index.md) | 1 | 0 | 2026-07-16T02:33:22.557Z → 2026-10-08T23:08:03.253Z |
| [/business/guides-and-resources/inside-gpt5-our-best-model-for-work/](../../pages/openai.com/business/guides-and-resources/inside-gpt5-our-best-model-for-work/index.md) | 1 | 0 | 2026-09-21T20:28:38.743Z → 2026-11-04T20:10:37.583Z |
| [/index/ai-native-company-workflows/](../../pages/openai.com/index/ai-native-company-workflows/index.md) | 1 | 0 | 2026-09-25T19:16:24.416Z → 2026-11-08T12:34:16.001Z |
| [/index/codex-maxxing-long-running-work/](../../pages/openai.com/index/codex-maxxing-long-running-work/index.md) | 1 | 0 | 2026-07-15T20:24:27.542Z → 2026-11-04T20:12:35.920Z |
| [/index/managing-ai-investments-in-agentic-era/](../../pages/openai.com/index/managing-ai-investments-in-agentic-era/index.md) | 1 | 0 | 2026-09-28T00:19:42.385Z → 2026-11-18T13:50:45.850Z |
| [/index/introducing-intelligence-age/](../../pages/openai.com/index/introducing-intelligence-age/index.md) | 1 | 0 | 2026-09-17T11:33:58.952Z → 2026-11-03T14:01:21.045Z |
| [/index/ai-as-the-greatest-source-of-empowerment-for-all/](../../pages/openai.com/index/ai-as-the-greatest-source-of-empowerment-for-all/index.md) | 0 | 1 | 2026-09-11T16:19:58.714Z → 2026-10-19T11:22:27.712Z |
| [/index/arco-education/](../../pages/openai.com/index/arco-education/index.md) | 1 | 0 | 2026-09-22T13:14:06.983Z → 2026-10-30T09:00:59.431Z |
| [/index/musenet/](../../pages/openai.com/index/musenet/index.md) | 0 | 1 | 2026-07-07T17:58:06.788Z → 2026-10-20T15:44:59.954Z |
| [/business/partners/boston-consulting-group/](../../pages/openai.com/business/partners/boston-consulting-group/index.md) | 0 | 1 | 2026-08-24T19:59:16.332Z → 2026-10-29T06:04:59.125Z |
| [/business/partners/capgemini/](../../pages/openai.com/business/partners/capgemini/index.md) | 0 | 1 | 2026-08-24T18:11:51.647Z → 2026-10-29T05:47:13.977Z |
| [/business/partners/mckinsey-and-company/](../../pages/openai.com/business/partners/mckinsey-and-company/index.md) | 0 | 1 | 2026-09-18T06:59:25.071Z → 2026-10-29T06:10:24.041Z |
| [/business/partners/tcs/](../../pages/openai.com/business/partners/tcs/index.md) | 0 | 1 | 2026-09-17T16:46:14.872Z → 2026-10-29T19:28:48.946Z |
| [/index/lenfest-institute/](../../pages/openai.com/index/lenfest-institute/index.md) | 1 | 0 | 2026-05-29T00:25:29.685Z → 2026-09-28T17:50:55.219Z |
| [/index/ly-corporation/](../../pages/openai.com/index/ly-corporation/index.md) | 0 | 1 | 2026-06-12T16:38:07.671Z → 2026-11-17T23:56:43.901Z |
| [/business/partners/artium/](../../pages/openai.com/business/partners/artium/index.md) | 0 | 1 | 2026-08-28T18:56:31.913Z → 2026-10-29T07:37:32.941Z |
| [/business/partners/capco/](../../pages/openai.com/business/partners/capco/index.md) | 0 | 1 | 2026-08-28T18:56:42.375Z → 2026-10-29T06:56:43.825Z |
| [/business/partners/cgi/](../../pages/openai.com/business/partners/cgi/index.md) | 0 | 1 | 2026-08-24T17:39:18.975Z → 2026-10-29T07:08:00.246Z |
| [/business/partners/cognizant/](../../pages/openai.com/business/partners/cognizant/index.md) | 0 | 1 | 2026-08-28T18:56:30.782Z → 2026-10-29T07:44:28.787Z |
| [/business/partners/infosys/](../../pages/openai.com/business/partners/infosys/index.md) | 0 | 1 | 2026-08-24T17:39:23.531Z → 2026-10-29T06:09:50.692Z |
| [/business/partners/ntt-data/](../../pages/openai.com/business/partners/ntt-data/index.md) | 0 | 1 | 2026-09-18T07:00:07.798Z → 2026-10-29T07:38:07.950Z |
| [/business/partners/pwc/](../../pages/openai.com/business/partners/pwc/index.md) | 0 | 1 | 2026-09-18T06:59:48.931Z → 2026-10-29T06:03:41.246Z |
| [/business/partners/slalom/](../../pages/openai.com/business/partners/slalom/index.md) | 0 | 1 | 2026-09-03T22:06:27.779Z → 2026-10-29T18:04:03.067Z |
| [/business/partners/statworx/](../../pages/openai.com/business/partners/statworx/index.md) | 0 | 1 | 2026-08-24T17:39:24.074Z → 2026-10-29T14:27:49.028Z |
| [/business/partners/tribe-ai/](../../pages/openai.com/business/partners/tribe-ai/index.md) | 0 | 1 | 2026-08-28T18:56:40.209Z → 2026-10-30T05:53:16.584Z |
| [/business/partners/unit8/](../../pages/openai.com/business/partners/unit8/index.md) | 0 | 1 | 2026-08-24T17:39:20.552Z → 2026-10-30T11:28:37.999Z |
| [/index/codex-for-knowledge-work/](../../pages/openai.com/index/codex-for-knowledge-work/index.md) | 1 | 0 | 2026-09-22T09:51:48.094Z → 2026-11-18T13:50:31.946Z |
| [/index/openai-joins-ports-pike-project/](../../pages/openai.com/index/openai-joins-ports-pike-project/index.md) | 1 | 0 | 2026-09-22T22:05:57.346Z → 2026-11-10T09:52:38.272Z |
| [/index/unlocking-new-ways-of-working/](../../pages/openai.com/index/unlocking-new-ways-of-working/index.md) | 1 | 0 | 2026-09-25T19:33:48.297Z → 2026-11-18T13:50:29.772Z |
| [/business/learn/intelligence-at-work-financial-services/](../../pages/openai.com/business/learn/intelligence-at-work-financial-services/index.md) | 1 | 0 | 2026-09-11T16:49:17.829Z → 2026-11-18T09:04:00.777Z |
| [/form/daybreak-cyber-partner-program/](../../pages/openai.com/form/daybreak-cyber-partner-program/index.md) | 1 | 0 | 2026-08-24T17:53:37.748Z → 2026-11-18T09:03:59.491Z |
| [/index/apple-is-getting-this-wrong/](../../pages/openai.com/index/apple-is-getting-this-wrong/index.md) | 1 | 0 | 2026-09-25T19:16:11.671Z → 2026-11-18T13:50:36.669Z |
| [/index/k-12-educators-practical-skills/](../../pages/openai.com/index/k-12-educators-practical-skills/index.md) | 1 | 0 | 2026-07-15T21:11:20.506Z → 2026-11-10T08:38:00.822Z |

1123 other updated URLs changed only in the site-wide nav/footer and/or recirculation cards.

## Appendix C: removed URLs

| URL | Last `<lastmod>` | Status at run time |
|---|---|---|
| /business/enabling-a-data-driven-workforce-webinar/ | 2026-05-29T00:25:34.049Z | 200 → /business/learn/enabling-a-data-driven-workforce-webinar/ |
| /business/fine-tuning-gpt-4o-webinar/ | 2026-05-29T00:25:48.091Z | 200 → /business/learn/fine-tuning-gpt-4o-webinar/ |
| /business/guides-and-resources/how-openai-uses-codex/ | 2026-09-21T20:28:38.576Z | 200 → /business/learn/how-openai-uses-codex/ |
| /business/guides-and-resources/identifying-and-scaling-ai-use-cases/ | 2026-09-21T20:28:37.540Z | 200 → /business/learn/identifying-and-scaling-ai-use-cases/ |
| /business/new-in-chatgpt-for-business-april-updates-2025/ | 2026-07-27T20:18:53.193Z | 200 → /business/learn/new-in-chatgpt-for-business-april-updates-2025/ |
| /business/new-in-chatgpt-for-work-march-updates-2025/ | 2026-07-27T20:21:08.866Z | 200 → /business/learn/new-in-chatgpt-for-work-march-updates-2025/ |
| /business/partners/canva/ | 2026-09-23T18:09:20.713Z | 404 |
| /business/partners/dropbox/ | 2026-09-09T00:10:26.418Z | 404 |
| /business/partners/gusto/ | 2026-09-20T17:10:04.692Z | 404 |
| /business/partners/hubspot/ | 2026-09-24T10:57:03.065Z | 404 |
| /business/partners/pathfindr/ | 2026-09-17T19:58:58.016Z | 200 → /business/partners/affinda/ |
| /business/partners/quickbooks/ | 2026-09-24T11:22:02.713Z | 404 |
| /business/partners/stripe/ | 2026-09-22T00:31:16.357Z | 404 |
| /business/plugins/atlassian-rovo/ | 2026-09-25T00:37:51.790Z | 404 |
| /business/plugins/litera-lito/ | 2026-09-25T00:35:26.031Z | 404 |
| /business/plugins/mcp-server-for-wordpress/ | 2026-09-25T00:31:17.728Z | 404 |
| /business/plugins/oracle-analytics/ | 2026-09-25T00:39:25.092Z | 404 |
| /business/plugins/wordpress-com/ | 2026-09-25T22:01:02.711Z | 200 → /business/plugins/wordpress/ |
| /daybreak/partners-new/ | 2026-09-18T20:02:09.590Z | 404 |
| /economic-research-exchange/ | 2026-08-18T10:26:01.488Z | 200 → /economic-research-collaborators/ |
| /form/data-partnerships/ | 2026-05-22T19:04:39.079Z | 200 → /index/data-partnerships/ |
| /form/ultrafast/ | 2026-08-24T17:53:36.921Z | 200 → https://developers.openai.com/api/docs/guides/ultrafast-mode |
| /index/ada/ | 2026-08-18T18:40:53.266Z | 200 → /business/customer-stories/ada/ |
| /index/blue-j/ | 2026-09-22T17:02:15.790Z | 200 → /business/customer-stories/blue-j/ |
| /prism/ | 2026-09-15T23:24:43.320Z | 200 → /science/ |
| /residency/ | 2026-09-22T22:05:52.611Z | 200 → /research/ |
| /safety/ | 2026-09-15T23:24:23.080Z | 200 → /safety-alignment/ |
| /solutions/blueprints/knowledge-retrieval/ | 2026-09-15T22:21:30.916Z | 200 → /business/solutions/knowledge-retrieval/ |
| /solutions/industries/financial-services/ | 2026-09-10T17:43:01.380Z | 200 → /business/solutions/financial-services/ |
| /solutions/industries/retail/ | 2026-09-15T23:27:21.888Z | 200 → /business/solutions/retail/ |
| /solutions/use-case/content-creation/ | 2026-09-07T16:33:26.142Z | 200 → /business/solutions/content-creation/ |
| /solutions/use-case/data-analysis/ | 2026-09-07T16:34:49.881Z | 200 → /business/solutions/data-analysis/ |

## Appendix D: sub-sitemap migrations

- `/business/learn/intelligence-at-work-financial-services/`: ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `/business/put-ai-to-work-automate-and-scale-financial-operations/`: ['sitemap.xml_company.xml', 'sitemap.xml_webinar.xml'] -> ['sitemap.xml_company.xml', 'sitemap.xml_learn-webinars.xml', 'sitemap.xml_webinar.xml']
- `/index/unlocking-new-ways-of-working/`: ['sitemap.xml_global-affairs.xml'] -> ['sitemap.xml_global-affairs.xml', 'sitemap.xml_learn-guides.xml']
- `/business/plugins/gsc-wizard/`: ['sitemap.xml_plugins-engineering-it.xml', 'sitemap.xml_plugins-marketing.xml'] -> ['sitemap.xml_plugins-data-research.xml', 'sitemap.xml_plugins-marketing.xml']
- `/business/plugins/sync-labs/`: ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-design-creative.xml']
- `/business/learn/how-our-sales-team-uses-chatgpt-work/`: ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `/index/managing-ai-investments-in-agentic-era/`: ['sitemap.xml_ai-adoption.xml'] -> ['sitemap.xml_ai-adoption.xml', 'sitemap.xml_learn-guides.xml']
- `/index/ai-native-company-workflows/`: ['sitemap.xml_ai-adoption.xml'] -> ['sitemap.xml_ai-adoption.xml', 'sitemap.xml_learn-guides.xml']
- `/business/learn/agent-security-enterprise/`: ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-guides.xml']
- `/index/the-five-ai-value-models-driving-business-reinvention/`: ['sitemap.xml_ai-adoption.xml'] -> ['sitemap.xml_ai-adoption.xml', 'sitemap.xml_learn-guides.xml']
- `/business/learn/intelligence-at-work-cyber/`: ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `/business/plugins/hex/`: ['sitemap.xml_plugins-data-research.xml'] -> ['sitemap.xml_plugins-data-research.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/fireflies/`: ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/hunter/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/rocketreach/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/index/put-ai-to-work-for-your-product-team/`: ['sitemap.xml_company.xml', 'sitemap.xml_webinar.xml'] -> ['sitemap.xml_company.xml', 'sitemap.xml_learn-webinars.xml', 'sitemap.xml_webinar.xml']
- `/business/plugins/zoho-crm/`: ['sitemap.xml_plugins-marketing.xml', 'sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml'] -> ['sitemap.xml_plugins-marketing.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/otter-ai/`: ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/zoominfo/`: ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-small-business.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml', 'sitemap.xml_plugins-small-business.xml']
- `/business/plugins/zoom/`: ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/canva/`: ['sitemap.xml_plugins-design-creative.xml', 'sitemap.xml_plugins-small-business.xml'] -> ['sitemap.xml_plugins-design-creative.xml', 'sitemap.xml_plugins-sales-commerce.xml', 'sitemap.xml_plugins-small-business.xml']
- `/business/plugins/close/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/attio/`: ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/figma/`: ['sitemap.xml_plugins-design-creative.xml', 'sitemap.xml_plugins-small-business.xml'] -> ['sitemap.xml_plugins-design-creative.xml', 'sitemap.xml_plugins-sales-commerce.xml', 'sitemap.xml_plugins-small-business.xml']
- `/business/plugins/instantly-ai/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/parallel-search/`: ['sitemap.xml_plugins-engineering-it.xml'] -> ['sitemap.xml_plugins-productivity.xml']
- `/business/plugins/seismic/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/business/solving-complex-problems-with-openai-o1-models/`: ['sitemap.xml_company.xml', 'sitemap.xml_webinar.xml'] -> ['sitemap.xml_company.xml', 'sitemap.xml_learn-webinars.xml', 'sitemap.xml_webinar.xml']
- `/business/plugins/klaviyo/`: ['sitemap.xml_plugins-marketing.xml', 'sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-marketing.xml', 'sitemap.xml_plugins-operations.xml']
- `/business/plugins/tableau/`: ['sitemap.xml_plugins-data-research.xml'] -> ['sitemap.xml_plugins-productivity.xml']
- `/business/plugins/pandadoc/`: ['sitemap.xml_plugins-legal.xml', 'sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-legal.xml', 'sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/apollo/`: ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/granola/`: ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/news/`: ['sitemap.xml_ai-adoption.xml', 'sitemap.xml_applied-ai.xml', 'sitemap.xml_company.xml', 'sitemap.xml_engineering.xml', 'sitemap.xml_product.xml', 'sitemap.xml_research.xml', 'sitemap.xml_safety.xml', 'sitemap.xml_security.xml'] -> ['sitemap.xml_ai-adoption.xml', 'sitemap.xml_applied-ai.xml', 'sitemap.xml_company.xml', 'sitemap.xml_engineering.xml', 'sitemap.xml_product.xml', 'sitemap.xml_research.xml', 'sitemap.xml_safety.xml', 'sitemap.xml_science.xml', 'sitemap.xml_security.xml']
- `/business/plugins/hubspot/`: ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml', 'sitemap.xml_plugins-small-business.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml', 'sitemap.xml_plugins-small-business.xml']
- `/business/put-ai-to-work-lessons-from-hundreds-of-successful-deployments/`: ['sitemap.xml_company.xml', 'sitemap.xml_webinar.xml'] -> ['sitemap.xml_company.xml', 'sitemap.xml_learn-webinars.xml', 'sitemap.xml_webinar.xml']
- `/business/learn/download-the-chatgpt-work-guide-for-sales-teams/`: ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-guides.xml']
- `/business/plugins/gamma/`: ['sitemap.xml_plugins-design-creative.xml'] -> ['sitemap.xml_plugins-design-creative.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/gong/`: ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/index/codex-maxxing-long-running-work/`: ['sitemap.xml_ai-adoption.xml'] -> ['sitemap.xml_ai-adoption.xml', 'sitemap.xml_learn-guides.xml']
- `/business/plugins/docusign/`: ['sitemap.xml_plugins-legal.xml', 'sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-small-business.xml'] -> ['sitemap.xml_plugins-legal.xml', 'sitemap.xml_plugins-productivity.xml', 'sitemap.xml_plugins-sales-commerce.xml', 'sitemap.xml_plugins-small-business.xml']
- `/business/plugins/outreach/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/zoom-revenue-accelerator/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/ironclad-contracts/`: ['sitemap.xml_plugins-legal.xml', 'sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-legal.xml', 'sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/learn/how-our-finance-team-uses-chatgpt-work/`: ['sitemap.xml_learn-guides.xml'] -> ['sitemap.xml_learn-webinars.xml']
- `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/`: ['sitemap.xml_disrupting-malicious-uses.xml', 'sitemap.xml_global-affairs.xml'] -> ['sitemap.xml_disrupting-malicious-uses.xml', 'sitemap.xml_safety.xml']
- `/business/plugins/lusha/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']
- `/business/put-ai-to-work-for-marketing-teams/`: ['sitemap.xml_company.xml', 'sitemap.xml_webinar.xml'] -> ['sitemap.xml_company.xml', 'sitemap.xml_learn-webinars.xml', 'sitemap.xml_webinar.xml']
- `/index/builders-guide-to-gpt-5-6/`: ['sitemap.xml_applied-ai.xml'] -> ['sitemap.xml_applied-ai.xml', 'sitemap.xml_learn-guides.xml']
- `/business/plugins/salesforce/`: ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml'] -> ['sitemap.xml_plugins-sales-commerce.xml']
- `/business/plugins/demandbase/`: ['sitemap.xml_plugins-operations.xml'] -> ['sitemap.xml_plugins-operations.xml', 'sitemap.xml_plugins-sales-commerce.xml']

## Fetch failures

None. All 2,082 page fetches passed the sanity check (≥100 chars, no Cloudflare challenge text).

