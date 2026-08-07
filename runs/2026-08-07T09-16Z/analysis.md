# Run 2026-08-07T09-16Z — analysis

**Fetch time:** 2026-08-07T09:16:39Z (sitemap + sub-sitemap pulls), then 151 page fetches (4 added + 147 updated) completed by ~09:25Z.
**Baseline:** 2026-08-06T09-16Z (consecutive day)
**Stats:** 1,560 total URLs | +4 added | 147 updated (lastmod changed) | -0 removed | 0 anomalies | 35 sub-sitemaps

Of the 147 URLs with a changed `<lastmod>`, 109 tracked files actually changed on disk after conversion to markdown; 38 had zero detectable content difference (pure `<lastmod>` bump from a redeploy, most commonly the recurring partner-tier-badge image cache-buster). 4 URLs are new.

## Anomalies

None this run. Checked and clear:
- No future-dated `<lastmod>` values (all 1,560 current URLs checked against fetch time 2026-08-07T09:16:39Z).
- No backward-moving `<lastmod>` among the 147 updated URLs.
- No newly-added URL with a `<lastmod>` predating today by more than a few days.
- 0 removed this run, so no reappearance case to check.
- No sub-sitemap migrations: full multi-membership tracking across all 35 sub-sitemaps shows 216 URLs legitimately cross-listed in >1 sub-sitemap (same count as yesterday), and membership sets for all 1,556 URLs common to both snapshots are unchanged.

## Significant updates

- **GPT‑5.6 Sol tuned for everyday chat, GPT‑5.6 Luna becomes the free-tier default.** New post [`/index/improving-gpt-5-6-sol-in-chatgpt/`](../../pages/openai.com/index/improving-gpt-5-6-sol-in-chatgpt/index.md) (Aug 6). For Plus/Pro: GPT‑5.6 Sol in the Chat surface is retuned for more focused, less over-formatted answers and a new "reasoning effort" slider; the same model now powers both Instant and deeper-reasoning responses in Chat (previously split between Instant and reasoning models). For Free/Go users: GPT‑5.6 Luna becomes the default model this week, with unlimited text chats and a new "Think" button for harder questions rolling out next week (subject to abuse guardrails; file/image/tool limits still apply). The linked system-card PDF describes additional under-18 safeguards (no romantic roleplay, age-restricted boundaries around sexual content/self-harm/dangerous activities, redirecting distressed teens to trusted people). This ties directly to a pricing-page change same day: **both `/business/pricing/` and `/business/chatgpt-pricing/` dropped their "GPT-5.5 Instant: Unlimited" comparison-table row** for Business/Enterprise plans, and relabeled "Messages and interactions" → "Everyday text chats" — consistent with GPT-5.5 Instant being retired from the plan-comparison surface as GPT-5.6 Sol takes over.
- **First country-by-country ChatGPT usage data, published via OpenAI Signals.** New post [`/index/how-the-world-is-putting-chatgpt-to-work/`](../../pages/openai.com/index/how-the-world-is-putting-chatgpt-to-work/index.md) (Aug 6). Headline findings: people are >2x as likely to use ChatGPT to *do* something (write, code, analyze) at work vs. outside work; the global adoption gap is narrowing as Latin America/Africa/Oceania catch up to early adopters; multimedia use is the fastest-growing use case (7.8% of messages globally, >10% in Brazil/Colombia); usage among people over 35 rose in nearly every country (France and Czechia up >10 points in a year). Data covers individual Free/Go/Plus/Pro accounts only (not managed-org accounts) and is published for download at [`/signals/`](../../pages/openai.com/signals/index.md), which was updated same-day (125 diff lines) along with `/signals/data/` (102 diff lines) to surface the new dataset.
- **OpenAI partners with the American Psychological Association on youth mental health.** New post [`/index/openai-and-apa-partner-to-advance-responsible-ai/`](../../pages/openai.com/index/openai-and-apa-partner-to-advance-responsible-ai/index.md) (Aug 6). Builds on an earlier co-hosted convening with mental-health orgs/researchers/educators/youth reps; APA CEO Arthur C. Evans Jr. and OpenAI's Sara Johansen (head of mental health & well-being product policy) are quoted. Areas of focus: supporting parents/caregivers, supporting practitioners, listening to youth, informed by developmental science. Fits the same-day GPT-5.6 system-card under-18 safeguards above — a coordinated youth-safety push.
- **`/business/solutions/finance/` and `/business/solutions/marketing/` — full page redesigns (278 and 229 diff lines respectively), largest content changes this run.** Both dropped their now-past-dated live-webinar countdown banners (finance's Aug 4 webinar has passed) and were restructured around explicit plugin ecosystems: finance now leads with a named-plugin grid (Data Analytics, Stripe, SharePoint, Google Drive, Salesforce, Gusto, Ramp, Snowflake, Databricks Genie, BigQuery, Outlook, Teams, LSEG, Morningstar, PitchBook) instead of icon-only app tiles, plus new sections ("Better visibility," "Agents that get work done," "Custom tools, better decisions," "Trust in every decision," "AI for every finance function" persona tabs). Marketing got the same plugin-grid treatment (Data Analytics, Product Design, Canva, Adobe, HubSpot, Figma, Mailchimp, Klaviyo, Semrush, etc.) and **newly cross-promotes ChatGPT Ads** ("reach people as they explore and decide with ChatGPT Ads," linking to `ads.openai.com`) as a dedicated capability — the first mention of ChatGPT Ads on `/business/solutions/marketing/`. ChatGPT Ads itself isn't new (this repo has tracked `ads.openai.com` and the removal of the old `/advertisers/` page in prior runs); what's new is OpenAI now marketing it directly to the marketing-vertical solutions audience. Both pages also swapped their bottom customer-story carousels for current stories and reworded closing CTAs.
- **`/api-fast-mode/` FAQ trimmed.** The "Is Fast mode available for long context, fine-tuned models, embeddings, etc.?" Q&A ("Not at this time...") was removed — minor, likely superseded by yesterday's Fast Mode long-context pricing rollout (logged in the 2026-08-06 run).

## Routine updates

- **Sitewide "Related articles" / "Latest posts" widget rotation reaching ~15 older pages.** `/index/where-the-goblins-came-from/` (98 diff lines, Apr 29 post — body text unchanged), `/index/expedia-jochen-koedijk/`, `/index/uber/`, `/index/scout24/`, `/index/endava-frontiers/`, `/index/endava/`, `/index/launchdarkly-claire-vo/`, `/index/uber-enables-outstanding-experiences/`, `/index/apple-is-getting-this-wrong/`, `/index/building-abundant-intelligence/`, `/index/cna-walter-fernandez/`, `/index/how-news-organizations-are-using-ai/`, `/index/doppel/`, `/index/safetykit/`, `/index/scania/`, `/index/unive/`, `/index/circles/`, `/index/steuerrecht/`, `/index/netomi/`, `/index/cisco/`, `/index/introducing-the-openai-economic-research-exchange/`, `/index/continuous-voice-interaction-with-gpt-live/`, `/index/blue-j/`, `/index/grab/`, `/index/state-of-minnesota/`, `/index/match-group/`, `/index/indeed/`, `/index/learn-teach-chatgpt-work-codex/`, `/index/ironclad/`, `/index/10bedicu/` — all just picked up the three new-post cards (HSP GRUPPE, GPT‑5.6 Sol update, APA partnership) in their sidebar/related-articles rotation; no body-text changes detected. `/index/where-the-goblins-came-from/` additionally shows the same TOC-duplication-fix / nav-widget catch-up pattern noted as an anomaly on 2026-08-06 (harmless template drift finally reaching a long-static page).
- **`/` (homepage), `/education/`, `/signals/b2b/`, `/signals/research/`, `/business/customer-stories/`, `/business/solutions/{operations,data,education}/` — minor listing/carousel rotations** to surface the day's new posts and stories; no structural changes.
- **61 `/business/partners/*` pages** refetched: partner-tier-badge image cache-busting parameter (`?dpl=dpl_...`) changed, same recurring redeploy artifact as every prior run; no partner-page body text changed.
- **38 URLs with a `<lastmod>` bump and zero detectable content change**, largely `/business/partners/*` pages not touching the visible badge markup, plus scattered `/index/*`, `/form/*`, and `/business/*` pages that only picked up invisible template/build metadata.
- **`/signals/data-download/`** (32 diff lines) — refreshed alongside the new country-data dataset above.
- **`/form/learning-lab/`, `/form/subscribe-to-new-sub-processors/`** — nav menu updated to show "GPT-5.6" (was "GPT-5.3 Instant") and "Customer Stories" / "Partner Network" / "Supply Co." links, consistent with ongoing nav-template rollout logged in recent runs.

## New pages

- **[`/index/hsp-gruppe/`](../../pages/openai.com/index/hsp-gruppe/index.md)** (Aug 7) — Customer story: HSP GRUPPE, a mid-market European tax-advisory firm, on ChatGPT Enterprise. Claims: 98.6% of employees report higher productivity, 84% weekly active usage, 500,000+ conversations in six months (Feb 1–Jul 14, 2026), 40,000+ estimated annual hours of additional capacity firm-wide.
- **[`/index/improving-gpt-5-6-sol-in-chatgpt/`](../../pages/openai.com/index/improving-gpt-5-6-sol-in-chatgpt/index.md)** (Aug 6) — see Significant updates.
- **[`/index/openai-and-apa-partner-to-advance-responsible-ai/`](../../pages/openai.com/index/openai-and-apa-partner-to-advance-responsible-ai/index.md)** (Aug 6) — see Significant updates.
- **[`/index/how-the-world-is-putting-chatgpt-to-work/`](../../pages/openai.com/index/how-the-world-is-putting-chatgpt-to-work/index.md)** (Aug 6) — see Significant updates.

## Removals

None this run.

## Fetch failures

None — all 151 targeted fetches (4 added + 147 updated) succeeded via `tools/html_to_md.py`.
