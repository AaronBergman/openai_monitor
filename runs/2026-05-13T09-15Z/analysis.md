# Run 2026-05-13T09-15Z Analysis

**Fetch time:** 2026-05-13T09:19:46Z  
**Baseline:** 2026-05-12T09-15Z  
**Total current URLs:** 1178  
**Added:** 5  **Updated:** 130  **Removed:** 121  
**Anomalies:** 2  **Fetch failures:** 0

---

## Anomalies (Highest Signal)

Two pages have `lastmod` timestamps set to within milliseconds of the fetch time. This is a CMS artifact — the sitemap generator is writing the current wall-clock time as `lastmod` for these form pages on every build, not a genuine edit timestamp. Not a cause for concern, but a recurring pattern worth noting.

- **future_lastmod** (CMS artifact): `https://openai.com/form/chatgpt-pro-community/`
  - lastmod `2026-05-13T09:19:46.160Z` is 160ms after fetch time `2026-05-13T09:19:46Z`
- **future_lastmod** (CMS artifact): `https://openai.com/form/100-chats-book-request/`
  - lastmod `2026-05-13T09:19:46.096Z` is 96ms after fetch time `2026-05-13T09:19:46Z`

---

## Structural Change: Two Sub-Sitemaps Dropped

OpenAI's sitemap index went from 34 to 32 sub-sitemaps. The two dropped sub-sitemaps were:

1. `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/` — contained 133 B2B customer-story pages
2. `https://openai.com/sitemap.xml/internal-use-show-on-brand-stories-hub/` — contained 30 brand-story and first-person narrative pages

Of the 152 total URLs in these two sub-sitemaps:
- **31 were migrated** to other sub-sitemaps (brand-stories-chatgpt, brand-stories-api, sora, startup, api, page)
- **121 were completely removed** from the sitemap (no longer discoverable by search engines via sitemap)

This does NOT necessarily mean the pages were deleted — they may still exist on the site. But they are no longer indexed via the sitemap, which will gradually reduce search engine crawl frequency.

### Migrated URLs (31)

| URL | Old sub-sitemap | New sub-sitemap |
|-----|-----------------|-----------------|
| `/index/cred-swamy-seetharaman/` | b2b-customer-stories-hub | api |
| `/index/deep-research/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/descript/` | b2b-customer-stories-hub | startup |
| `/index/fishing-for-first-timers/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/frontier-builders/` | brand-stories-hub | brand-stories-api |
| `/index/gpt-5-amgen/` | brand-stories-hub | brand-stories-api |
| `/index/gpt-5-coding-design/` | brand-stories-hub | brand-stories-api |
| `/index/gpt-5-creative-writing/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/gpt-5-cursor/` | brand-stories-hub | brand-stories-api |
| `/index/gpt-5-first-look/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/gpt-5-medical-research/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/gradient-labs/` | b2b-customer-stories-hub | startup |
| `/index/higgsfield/` | b2b-customer-stories-hub | api |
| `/index/my-dog-the-math-tutor/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/navigating-health-questions/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/o1-coding/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/o1-economics/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/o1-genetics/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/o1-quantum-physics/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/parloa/` | b2b-customer-stories-hub | startup |
| `/index/praktika/` | b2b-customer-stories-hub | startup |
| `/index/rakuten-2024/` | b2b-customer-stories-hub | api |
| `/index/rakuten/` | b2b-customer-stories-hub | page |
| `/index/simplex/` | b2b-customer-stories-hub | page |
| `/index/small-business-stories/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/sora-lyndon-barrois/` | brand-stories-hub | brand-stories-sora |
| `/index/sora-minne-atairu/` | brand-stories-hub | sora |
| `/index/sora-vallee-duhamel/` | brand-stories-hub | sora |
| `/index/ten-tiny-canvases/` | brand-stories-hub | brand-stories-chatgpt |
| `/index/the-met-museum/` | brand-stories-hub | brand-stories-api |
| `/index/tolan/` | b2b-customer-stories-hub | startup |

---

## New Pages

### 1. `/academy/how-finance-teams-use-codex/` (lastmod: 2026-05-13T04:53:03.074Z)
**"How finance teams use Codex"** — OpenAI Academy guide with 10 detailed finance use cases for Codex, including monthly business review narratives, variance analysis, and planning. Includes copy-ready prompts and suggested Codex skills/plugins for finance tech stacks. Part of a coordinated Codex-in-the-enterprise push.

### 2. `/index/autoscout24/` (lastmod: 2026-05-13T06:45:37.807Z)
**"AutoScout24 scales engineering with AI-powered workflows"** — AutoScout24 Group (Europe's largest online car marketplace, ~30M monthly users, 2,000 employees) deployed ChatGPT company-wide and Codex for ~1,000 engineers after a three-month evaluation. Pages explicitly mentions Codex was selected for "usability, workflow compatibility, and measurable improvements in productivity and code quality."

### 3. `/index/nvidia/` (lastmod: 2026-05-13T06:44:15.024Z)
**"How NVIDIA engineers and researchers build with Codex"** — NVIDIA's coding-agents team uses Codex with **GPT-5.5** for production engineering. The page is notable for being one of the clearest public endorsements of GPT-5.5 from a named enterprise customer. Quotes NVIDIA senior engineer: "I've personally found Codex with GPT-5.5 to be way more autonomous, with much less handholding." Researchers use it to automate ML research loops on remote machines.

### 4. `/index/what-parameter-golf-taught-us/` (lastmod: 2026-05-13T08:28:39.972Z)
**"What Parameter Golf taught us"** — Post-mortem of OpenAI's "Parameter Golf" public ML challenge: 1,000+ participants, 2,000+ submissions, record-breaking approaches to efficient model training. Highlights record-track submissions (training optimization) and non-record creative approaches (non-autoregressive modeling, dynamic tokenization). Connects to earlier `/index/parameter-golf/` page.

### 5. `/form/codex-enterprise-promo/` (lastmod: 2026-05-13T08:47:56.149Z)
Enterprise interest / lead-gen form for Codex. Accompanies the Codex push.

---

## Significant Updated Pages

### Content changes (by size delta)

- **`/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/`**: 38,341 → 38,635 chars (+294). Enterprise AI report expanded.
- **`/business/guides-and-resources/staying-ahead-in-the-age-of-ai/`**: 24,175 → 24,469 chars (+294). Content expanded.
- **`/amex-chatgpt-business/`**: 7,942 → 8,357 chars (+415). American Express co-branded ChatGPT business page grew substantially.
- **`/academy/codex-for-work/`**: 7,018 → 7,413 chars (+395). Codex for Work guide expanded.
- **`/academy/codex-how-to-start/`**: 6,720 → 6,783 chars (+63). Minor expansion.
- **`/academy/top-10-use-cases-codex-for-work/`**: 22,211 → 22,246 chars (+35). Minor expansion.
- **`/business/guides-and-resources/chatgpt-business-smb-guide/`**: 16,810 → 16,823 chars (+13). Minor update.
- **`/business/guides-and-resources/a-practical-guide-to-building-ai-agents/`**: 39,340 → 39,156 chars (−184). Some content removed from the agents guide.

### Bulk lastmod refreshes (unchanged content, CMS timestamp bump only)

A large number of pages (~100+) had their lastmod updated but content remained identical. These appear to be a CMS-level publish wave affecting:
- All `/academy/` pages
- All `/news/` hub pages (`/news/company-announcements/`, `/news/engineering/`, etc.)
- All `/global-affairs/` articles
- Most `/index/` pages (remaining after the removals)
- API and business landing pages

This is consistent with a CMS republish triggered by the sitemap restructure or a template change.

---

## Removed URLs (121)

All from the `internal-use-show-on-b2b-customer-stories-hub` sub-sitemap. Full list:

`https://openai.com/index/10bedicu/`, `https://openai.com/index/ada/`, `https://openai.com/index/altera/`, `https://openai.com/index/arco-education/`, `https://openai.com/index/asu/`, `https://openai.com/index/axios-allison-murphy/`, `https://openai.com/index/balyasny-asset-management/`, `https://openai.com/index/basis/`, `https://openai.com/index/bbva-2025/`, `https://openai.com/index/bbva/`, `https://openai.com/index/be-my-eyes/`, `https://openai.com/index/blue-j/`, `https://openai.com/index/bny/`, `https://openai.com/index/booking-com/`, `https://openai.com/index/canva-cam-adams/`, `https://openai.com/index/canva/`, `https://openai.com/index/chime-vineet-mehra/`, `https://openai.com/index/choco/`, `https://openai.com/index/cisco/`, `https://openai.com/index/clay/`, `https://openai.com/index/cna-walter-fernandez/`, `https://openai.com/index/coderabbit/`, `https://openai.com/index/color-health/`, `https://openai.com/index/commonwealth-bank-of-australia/`, `https://openai.com/index/consensus/`, `https://openai.com/index/cyberagent/`, `https://openai.com/index/dai-nippon-printing/`, `https://openai.com/index/datadog/`, `https://openai.com/index/decagon/`, `https://openai.com/index/digital-green/`, `https://openai.com/index/doordash-mariana-garavaglia/`, `https://openai.com/index/doppel/`, `https://openai.com/index/duolingo/`, `https://openai.com/index/eliseai-minna-song/`, `https://openai.com/index/endex/`, `https://openai.com/index/eneos-materials/`, `https://openai.com/index/estee-lauder/`, `https://openai.com/index/expedia-jochen-koedijk/`, `https://openai.com/index/factory/`, `https://openai.com/index/fanatics-betting-gaming-andrea-ellis/`, `https://openai.com/index/figma-david-kossnick/`, `https://openai.com/index/genmab/`, `https://openai.com/index/genspark/`, `https://openai.com/index/government-of-iceland/`, `https://openai.com/index/grab/`, `https://openai.com/index/harvey/`, `https://openai.com/index/healthify/`, `https://openai.com/index/hebbia/`, `https://openai.com/index/hibob/`, `https://openai.com/index/holiday-extras/`, `https://openai.com/index/hygh/`, `https://openai.com/index/indeed-maggie-hulce/`, `https://openai.com/index/indeed/`, `https://openai.com/index/intercom/`, `https://openai.com/index/invideo-ai/`, `https://openai.com/index/ironclad/`, `https://openai.com/index/jetbrains-2025/`, `https://openai.com/index/jetbrains/`, `https://openai.com/index/khan-academy/`, `https://openai.com/index/klarna/`, `https://openai.com/index/launchdarkly-claire-vo/`, `https://openai.com/index/lifespan/`, `https://openai.com/index/lowes-chandhu-nair/`, `https://openai.com/index/lowes/`, `https://openai.com/index/ly-corporation/`, `https://openai.com/index/match-group/`, `https://openai.com/index/mavenagi/`, `https://openai.com/index/mercado-libre/`, `https://openai.com/index/mercari/`, `https://openai.com/index/mirakl/`, `https://openai.com/index/mixi/`, `https://openai.com/index/moderna/`, `https://openai.com/index/morgan-stanley/`, `https://openai.com/index/netomi/`, `https://openai.com/index/neurogum/`, `https://openai.com/index/notion/`, `https://openai.com/index/nubank/`, `https://openai.com/index/oscar/`, `https://openai.com/index/outtake/`, `https://openai.com/index/paf/`, `https://openai.com/index/paradigm/`, `https://openai.com/index/philips/`, `https://openai.com/index/plex-coffee/`, `https://openai.com/index/podium/`, `https://openai.com/index/promega/`, `https://openai.com/index/retell-ai/`, `https://openai.com/index/retool/`, `https://openai.com/index/rogo/`, `https://openai.com/index/rox/`, `https://openai.com/index/safetykit/`, `https://openai.com/index/salesforce/`, `https://openai.com/index/san-antonio-spurs/`, `https://openai.com/index/scania/`, `https://openai.com/index/schoolai/`, `https://openai.com/index/scout24/`, `https://openai.com/index/singular-bank/`, `https://openai.com/index/stadler/`, `https://openai.com/index/state-of-minnesota/`, `https://openai.com/index/steuerrecht/`, `https://openai.com/index/stripe/`, `https://openai.com/index/summer-health/`, `https://openai.com/index/superhuman/`, `https://openai.com/index/taisei/`, `https://openai.com/index/trustbank/`, `https://openai.com/index/typeform/`, `https://openai.com/index/uber-enables-outstanding-experiences/`, `https://openai.com/index/uber/`, `https://openai.com/index/unify/`, `https://openai.com/index/upwork/`, `https://openai.com/index/vfl-wolfsburg/`, `https://openai.com/index/viable/`, `https://openai.com/index/wayfair/`, `https://openai.com/index/waymark/`, `https://openai.com/index/whoop/`, `https://openai.com/index/wix/`, `https://openai.com/index/wrtn/`, `https://openai.com/index/yabble/`, `https://openai.com/index/zalando/`, `https://openai.com/index/zelma/`, `https://openai.com/index/zendesk/`, `https://openai.com/index/zenken/`

Last snapshots in git history: `git log -- pages/openai.com/index/<slug>/index.md`

---

## Stats

| Metric | Value |
|--------|-------|
| Total current URLs | 1,178 |
| Added | 5 |
| Updated | 130 |
| Removed | 121 |
| Anomalies | 2 (CMS artifacts) |
| Sub-sitemaps | 32 (was 34) |
| Fetch failures | 0 |
