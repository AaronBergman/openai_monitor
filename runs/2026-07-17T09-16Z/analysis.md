# Analysis — Run 2026-07-17T09-16Z

**Fetch time (this run):** 2026-07-17T09:17Z (sitemaps); page fetches completed by ~09:23Z
**Baseline:** 2026-07-15T09-16Z (no run executed on 2026-07-16 — this diff spans ~2 days)
**Sub-sitemaps:** 34/34 fetched successfully, no errors
**Totals:** 1458 URLs (was 1443) | +19 added | 184 updated (~84 with a real/notable markdown diff, ~100 lastmod-only template noise) | -4 removed | 0 anomalies | 0 fetch failures

## Anomalies

None detected by automated checks: no future-dated `<lastmod>`, no backwards-moving `<lastmod>` vs the last known value, no new URL backdated relative to its first_seen, no URL reappearance, no sub-sitemap migrations.

Two removals immediately correspond to same-day additions with identical content and are treated as **renames**, not genuine removal+addition pairs (see below).

## Significant updates

### New research: GPT‑Red, an automated red-teaming model, hardens GPT‑5.6 against prompt injection
New publication [`/index/unlocking-self-improvement-gpt-red/`](../../pages/openai.com/index/unlocking-self-improvement-gpt-red/index.md) (July 15, 2026, Safety). OpenAI describes training **GPT‑Red**, an internal automated red-teaming model built at "the compute scale of some of our largest post-training runs," used to generate adversarial prompt-injection attacks and directly incorporate them into the training process of production models. Headline claim: GPT‑5.6 Sol — trained adversarially against GPT‑Red — achieves **6x fewer failures** on OpenAI's hardest direct prompt-injection benchmark compared to their best production model from four months earlier. Framed explicitly as "a crucial form of self-improvement for safety: using today's models to directly help make future models safer." Promoted immediately to the homepage and `/news/`.

### New policy essay: "Why teens deserve access to safe AI"
New page [`/index/why-teens-deserve-access-safe-ai/`](../../pages/openai.com/index/why-teens-deserve-access-safe-ai/index.md) (July 16, 2026, Safety). Argues teens should have AI access paired with age-appropriate protections rather than being excluded until adulthood ("nearly 9 in 10 teens on ChatGPT use it for learning... in a single week"). Reiterates four "key commitments" from OpenAI's Model Spec teen-protections update (teen safety first, encourage real-world support, treat teens as teens, be transparent) and recaps this year's teen-safety work: age prediction, expanded Parental Controls, family resources, and learning-oriented features. Reads as a policy/PR piece ahead of likely regulatory or media scrutiny on teen AI use.

### New global-affairs essay: "The US is advancing AI safety through state and federal action"
New page [`/index/advancing-ai-safety-through-state-and-federal-action/`](../../pages/openai.com/index/advancing-ai-safety-through-state-and-federal-action/index.md) (July 15, 2026, Global Affairs), bylined by **Chris Lehane, Chief Global Affairs Officer**. Argues California, New York, and Illinois frontier-safety laws are building a "reverse federalism" toward a de facto US national AI safety standard, which OpenAI frames as the basis for a future US-led global framework. Cites documented safety frameworks with public risk assessments, serious-incident reporting, and independent audits as the core elements states are converging on.

### Ads Policies substantially rewritten and expanded (July 15, 2026 update)
[`/policies/ad-policies/`](../../pages/openai.com/policies/ad-policies/index.md) — "Updated" date bumped from June 4 to **July 15, 2026**, with the largest content change of any page in this run (92 substantive added/removed lines). Two changes stand out:
- **New "Advertiser policies" section (§3)**: formal, detailed standards on advertiser identity (truthful identity/affiliation, IP/brand use, destination integrity), advertiser trustworthiness (anti-fraud, business conduct, required licensing/certifications), and advertiser eligibility (permitted categories, geographic compliance) — none of this existed in the prior version.
- **Financial and health ad categories opened up with specificity, replacing vague blanket restrictions.** Previously: "Ads for financial products and services are restricted. At this time, we may allow ads from approved financial advertisers" and "Ads for regulated medical products, services... are currently disallowed." Now: explicit **US-only, case-by-case** allow-lists — finance (auto loans, credit cards, credit monitoring, deposit accounts, financial planning, insurance, investment services/brokerages, mortgages, personal loans, payment services) and health (consumer medical devices/wearables, dental, dietary supplements, disease-awareness campaigns, health insurance, hospitals/urgent care, medical testing, minimally invasive cosmetic procedures, vision products), with licensure proof required and non-US financial/health ads "generally prohibited."
- Also added a new "Review & monitoring" / "Enforcement & reporting" structure describing ML-based review with human escalation, ongoing post-approval monitoring, and a new user/advertiser reporting channel.

This reads as OpenAI formalizing and considerably widening its ad-sales program (first launched in ChatGPT earlier this year) into previously-restricted, revenue-dense financial and health verticals — worth watching for actual ads appearing in these categories.

### OpenAI Supply Co. — new consumer merch storefront launches
11 new `/supply/product/<slug>/` pages appeared (Bloop Tote, Blossom Hat, Blossom Socks, ChatGPT Basketball, ChatGPT Long Sleeve, Codex Bubble Cap, Codex Build Hoodie, Codex Distressed Tee, Good Research Tee, Pixel Nalgene, Research Half-Zip), hosted on a Shopify-backed subsection with its own nav (Co-Lab / Shop / Archive / About / FAQ). None carry a `<lastmod>` (consistent with the storefront sitting outside the main CMS). A "Supply Co." link was simultaneously added to the sitewide footer nav on effectively every page touched this run — this single footer addition, not independent content edits, explains most of the "routine" lastmod bumps below.

### Partner Network gains a new Elite-tier-adjacent entrant, two renames, and a full logo refresh
- **New partner:** [`/business/partners/epam/`](../../pages/openai.com/business/partners/epam/index.md) — EPAM Systems joins as an **Advanced Partner**, pitched around "forward-deployed engineering" for Global 2000 enterprises (cites 20+ AI agents reaching production in under 3 months for one client).
- **Renames** (treated as rename, not remove+add — identical body copy, same logo asset, only the URL slug and page title changed):
  - `/business/partners/reply/` → [`/business/partners/cognita-reply/`](../../pages/openai.com/business/partners/cognita-reply/index.md) ("Reply" → "Cognita Reply")
  - `/business/partners/thinking-machines-data-science-inc/` → [`/business/partners/thinking-machines-data-science/`](../../pages/openai.com/business/partners/thinking-machines-data-science/index.md) (dropped "-inc" suffix)
- The `/business/partners/` directory page itself replaced nearly every partner's logo image with a new consistently-formatted square SVG ("...-square-light.svg"), and finished syncing the "Eliza Solutions Corp" → "Eliza" label rename first reported on 2026-07-14/07-15 (the directory list text had lagged the URL rename until now).

### New customer story: Cars24
New page [`/index/cars24/`](../../pages/openai.com/index/cars24/index.md) (July 16, 2026) — Indian used-car marketplace Cars24 reports 1M+ monthly AI-agent conversation minutes, 50% higher support-resolution rates, 80% faster turnaround on key service workflows, and recovering 12% of previously-lost sales leads using OpenAI's API, ChatGPT, and Codex.

### New page: "Our approach to public policy"
New hub page [`/company/public-policy/`](../../pages/openai.com/company/public-policy/index.md) laying out OpenAI's stated public-policy principles (Democratization, Empowerment, Prosperity, Resilience, Adaptability) with a newsletter subscribe link. Distinct from the older `/index/public-policy-agenda/` page (June 2026), which remains live and is now cross-linked as related content from several safety/policy pages — the two appear to be a hub page (new) vs. a specific dated announcement (old), not a replacement.

### `/products/release-notes/` gains three new entries, pushing older ones off the visible list
The rolling changelog added, in order:
- **"Search across chats, projects, images, and files in ChatGPT"** (Jul 14) — new cross-content search from the ChatGPT sidebar on web/iOS/Android.
- **"ChatGPT returns to WhatsApp in the EEA"** (Jul 13) — service resumes in the European Economic Area via the verified 1-800-CHATGPT number; also newly available on **Kakao (South Korea)** and **Viber** in supported markets.
- **"ChatGPT for iOS updates: Codex inline visualizations and task controls"** (Jul 13) — inline visualizations in Codex tasks, more reliable task-creation links, improved tool-activity/progress styling, and several bug fixes (autocomplete/swipe-gesture responsiveness).

To keep the page at a fixed length, older entries fell off the bottom, including "Retiring group chats in ChatGPT" (previously visible) — the removal is a display-window effect, not a retraction; git history retains the prior snapshot.

### Business-site nav A/B test is non-monotonic — one page flipped back to the old nav
Continuing the "Why OpenAI / Solutions / Resources / Customers / Pricing" nav experiment tracked in prior runs: `/solutions/industries/financial-services/` **gained** the new nav + "Introducing ChatGPT Work" banner this run (joining the pages that adopted it 2026-07-11 to 07-15). But `/business/solutions/sales/` moved the **opposite direction**, reverting from the new nav back to the classic "Research / Products / Business / Developers / Company" nav and losing its "ChatGPT Work" promo banner. This mirrors the `/stories/` page's reversal noted on 2026-07-15 — the nav test is being run/rolled back non-uniformly across the site, not converging in one direction.

### Minor real edits
- `/devday/terms-and-conditions/` — the two support contact addresses changed from plain text (`help@devday.openai.com`, `press@devday.openai.com`) to proper `mailto:` links, and the help contact address itself changed to `devday@openai.com`.

## Routine updates (site-wide template refresh, catching up on prior-week changes)

The large majority of the 184 lastmod-bumped pages carried only mechanical footer/template changes, no unique body content:
- **"Supply Co." added to the footer nav** — new this run, sitewide (see above).
- **"GPT-5.3 Instant" → "GPT-5.6" in the "Latest Advancements" footer list** — many of today's updated pages hadn't been re-fetched since before this swap first appeared (2026-07-15), so it shows up as "new" on them now even though it was already reported site-wide two runs ago.
- **"Customer Stories" and "Partner Network" footer links** — same catch-up effect; first reported 2026-07-14, appearing today only on pages that hadn't been touched since.
- **Related-content carousels refreshed** (Global Affairs, Product, Safety, Research "related articles" strips) to surface the new pages listed above — expected consequence of new content being published, not independent edits.
- **"Table of contents" duplicate/relabeled block** appearing/disappearing, and footnote numbering reformatting (inline "1." vs. list-item "1.") on model-launch pages like `/index/gpt-5-6/` — a client-side hydration/rendering-timing artifact consistent with prior runs' notes, not a content edit.
- **`/index/introducing-openai-partner-network/`**, **`/index/introducing-gpt-5-4/`**, **`/index/previewing-gpt-5-6-sol/`**, **`/devday/`** and several other pages had only single-item related-carousel swaps (1-3 lines) with no other change.
- ~100 of the 184 updated URLs had a bumped `<lastmod>` but a markdown diff limited entirely to the noise patterns above (Supply Co. link / GPT-5.6 footer swap / TOC flicker / blank lines).

## New pages

- **[`/index/unlocking-self-improvement-gpt-red/`](../../pages/openai.com/index/unlocking-self-improvement-gpt-red/index.md)** — GPT‑Red automated red-teaming research; see above.
- **[`/index/why-teens-deserve-access-safe-ai/`](../../pages/openai.com/index/why-teens-deserve-access-safe-ai/index.md)** — teen safety policy essay; see above.
- **[`/index/advancing-ai-safety-through-state-and-federal-action/`](../../pages/openai.com/index/advancing-ai-safety-through-state-and-federal-action/index.md)** — Chris Lehane essay on state/federal AI policy; see above.
- **[`/company/public-policy/`](../../pages/openai.com/company/public-policy/index.md)** — new public-policy hub page; see above.
- **[`/index/cars24/`](../../pages/openai.com/index/cars24/index.md)** — Cars24 customer story; see above.
- **[`/business/partners/epam/`](../../pages/openai.com/business/partners/epam/index.md)** — new Advanced Partner; see above.
- **[`/business/partners/cognita-reply/`](../../pages/openai.com/business/partners/cognita-reply/index.md)** — rename of `/business/partners/reply/`; see Removals.
- **[`/business/partners/thinking-machines-data-science/`](../../pages/openai.com/business/partners/thinking-machines-data-science/index.md)** — rename of `/business/partners/thinking-machines-data-science-inc/`; see Removals.
- **11× `/supply/product/<slug>/` pages** — OpenAI Supply Co. merch launch; see above. Full list: [bloop-tote](../../pages/openai.com/supply/product/bloop-tote/index.md), [blossom-hat](../../pages/openai.com/supply/product/blossom-hat/index.md), [blossom-socks](../../pages/openai.com/supply/product/blossom-socks/index.md), [chatgpt-basketball](../../pages/openai.com/supply/product/chatgpt-basketball/index.md), [chatgpt-longsleeve](../../pages/openai.com/supply/product/chatgpt-longsleeve/index.md), [codex-bubble-cap](../../pages/openai.com/supply/product/codex-bubble-cap/index.md), [codex-build-hoodie](../../pages/openai.com/supply/product/codex-build-hoodie/index.md), [codex-distressed-tee](../../pages/openai.com/supply/product/codex-distressed-tee/index.md), [good-research-tee](../../pages/openai.com/supply/product/good-research-tee/index.md), [pixel-nalgene](../../pages/openai.com/supply/product/pixel-nalgene/index.md), [research-half-zip](../../pages/openai.com/supply/product/research-half-zip/index.md).

## Removals

- `business/partners/reply/` — renamed to `business/partners/cognita-reply/`, see above. Not a genuine removal.
- `business/partners/thinking-machines-data-science-inc/` — renamed to `business/partners/thinking-machines-data-science/`, see above. Not a genuine removal.
- `codex/get-started/` — a standalone "Get started with Codex" onboarding walkthrough (sign-in, project setup) removed with no direct URL replacement. Continues the pattern (flagged 2026-07-15) of narrow Codex how-to pages being consolidated away from openai.com. Last snapshot in git history.
- `tokens-of-appreciation/` — "Tokens of Appreciation Program 2026," a promotional awards page for top API users (tiered by total lifetime token usage: Silver 100B+, plus higher tiers), removed with no replacement found in this run's added/updated set. Last snapshot in git history.

## Fetch failures

None. All 34/34 sub-sitemaps and 203/203 changed/new pages fetched successfully on the first attempt.
