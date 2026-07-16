# Analysis — Run 2026-07-16T09-17Z

**Fetch time (this run):** 2026-07-16T09:17:03Z (sitemaps); page fetches completed by ~09:22Z
**Baseline:** 2026-07-15T09-16Z
**Sub-sitemaps:** 34/34 fetched successfully, no errors
**Totals:** 1456 URLs (was 1443) | +14 added | 174 updated (109 with a non-trivial markdown diff, 65 nav-link-only) | -1 removed | 0 anomalies | 0 fetch failures

## Anomalies

None detected by automated checks: no future-dated `<lastmod>`, no backwards-moving `<lastmod>` vs the last known value, no new URL backdated relative to its first_seen, no URL reappearance, no sub-sitemap migrations. All 14 new URLs are genuinely first-seen (not in `state/known_urls.json` before today).

## Significant updates

### OpenAI launches a merch store: "Supply Co."
Ten new product pages appeared under `/supply/product/<slug>/` — a Shopify-backed apparel/accessories shop (`Co-Lab`, `Shop`, `Archive`, `About`, `FAQ` sections) selling OpenAI/Codex/ChatGPT-branded goods:

- Bloop Tote — $45.00
- Blossom Hat — $40.00
- Blossom Socks
- ChatGPT Basketball — $70.00 (tied to a "Pause. Play. Prompt." campaign)
- ChatGPT Longsleeve
- Codex Bubble Cap
- Codex Build Hoodie — $100.00
- Codex Distressed Tee
- Good Research Tee — $40.00 ("A statement piece for the Research department")
- Pixel Nalgene
- Research Half-Zip

None of these product pages carry a `<lastmod>` (all `None`), and there's no `/supply/` index page in the sitemap yet — only the 10 individual products. This is the reason **65 of today's 174 "updated" pages carry no content change at all**: a `* [Supply Co.](</supply/>)` link was added to the global footer nav across the site to point at the new store, bumping those pages' lastmod with zero body change.

### Ad policies page substantially rewritten
`/policies/ad-policies/` (Updated: June 4 → July 15, 2026) got a real policy expansion, not just a refresh:
- **Financial services**: ads now explicitly allowed (case-by-case, US only) for auto loans/leasing, credit cards, credit monitoring, deposit accounts, financial planning, insurance, investment services/brokerages, mortgages, personal loans, and payment services — advertisers may need to show proof of licensure. Financial ads outside the US are now generally prohibited; cryptocurrency/credit-repair/debt-settlement/alternative-investment ads remain disallowed.
- **Health services** (renamed from "Healthcare & medicine"): similarly opened up (case-by-case, US only) for consumer medical devices/wearables, dental services, dietary supplements, disease-awareness campaigns, health insurance, hospitals/urgent care, medical testing, minimally invasive cosmetic procedures, and vision products — again with possible licensure requirements. Unsafe/unapproved products, unsupported treatment claims, experimental therapies, high-risk procedures, adult sexual-health services, and body-image-exploitative products remain disallowed.
- A brand-new **"Advertiser policies"** section (section 3) was added, covering advertiser identity (truthful identity/affiliation, IP/brand use, destination integrity), trustworthiness (anti-fraud, business conduct, required licensing), and eligibility (permitted categories, geographic compliance).
- The old "Ad integrity" section was restructured and renumbered (now section 4), with review process broken into explicit "Review scope" and "Review & monitoring" subsections describing LLM/classifier-based review plus escalation to human review.
- The old inline "May 2026 update" / "April 2026 update" notes at the top were **not deleted** — they were moved into a new versioned **Changelog** section at the bottom of the page (v1.0 initial publication Mar 2026, v1.1 Apr 2026, v1.2 May 2026, v1.3 Jul 2026 describing today's changes).

Read together, this is OpenAI formalizing and substantially widening what financial and health advertisers can run in ChatGPT, while adding a much more explicit advertiser vetting framework.

### Partner Network roster tweaks
`/business/partners/` (the partner logo carousel, both desktop and mobile instances) changed:
- **Capco** was dropped from the partner logo list entirely (no longer shown as a partner).
- **EPAM** was added as a new partner logo.
- Three existing partners were relabeled with cleaner names: "Eliza Solutions Corp" → "Eliza" (echoing the rename already reflected in that partner's own page slug back on 2026-07-15), "Deepsense" → "deepsense.ai", "Statworx" → "statworx".

### Product release notes: three new entries
`/products/release-notes/` gained three new changelog entries at the top:
- **Search across chats, projects, images, and files in ChatGPT** (Jul 14, GA) — new unified search from the ChatGPT sidebar on web, iOS, and Android, with content-type filters; available on all plans globally.
- **ChatGPT returns to WhatsApp in the EEA** (Jul 13, GA) — users can message the verified 1-800-CHATGPT WhatsApp number without a ChatGPT account; also notes ChatGPT is available on Kakao (South Korea) and Viber in other markets.
- **ChatGPT for iOS updates: Codex inline visualizations and task controls** (Jul 13, GA) — inline visualizations in Codex tasks, plus a list of iOS app improvements/fixes (task creation/linking, tool-activity styling, composer visibility, Fast-mode selection persistence, swipe-gesture fixes).

The GPT-5.6 model family and "Introducing ChatGPT Work" entries from prior runs are still present, just pushed down by date sort — not removed.

### Financial-services solutions page gets a template + banner refresh
`/solutions/industries/financial-services/` picked up the current site nav template ("Why OpenAI / Products / Solutions / Resources / Customers / Pricing" + "Try OpenAI" button), replacing an older nav variant — this specific nav swap wasn't seen on any other page today, so it reads as a one-off upgrade rather than a new site-wide rollout. The page also gained a "New: Introducing ChatGPT Work" promo banner, dropped the BBVA customer-story card from its logo carousel, and reworded the Morgan Stanley card's caption from "Shaping the future of financial services" to "Morgan Stanley is shaping the future of financial services."

### Research paper now public
`/index/deployment-simulation/`'s "Read the paper" link was swapped from an internal CDN PDF to a public arXiv listing (`arxiv.org/abs/2607.07184`) — the underlying paper appears to have just been published to arXiv.

## New pages

- **[`/company/public-policy/`](../../pages/openai.com/company/public-policy/index.md)** — new hub page laying out OpenAI's AI-policy principles (Democratization, Empowerment, Prosperity, Resilience, Adaptability) and priorities, with a newsletter subscribe link to `openaiglobalaffairs.substack.com`.
- **[`/index/advancing-ai-safety-through-state-and-federal-action/`](../../pages/openai.com/index/advancing-ai-safety-through-state-and-federal-action/index.md)** — Global Affairs op-ed by Chris Lehane (Chief Global Affairs Officer) on "reverse federalism": California/New York/Illinois state AI-safety legislation converging with federal efforts toward a US-led global AI governance framework.
- **[`/index/unlocking-self-improvement-gpt-red/`](../../pages/openai.com/index/unlocking-self-improvement-gpt-red/index.md)** — new safety research publication introducing "GPT-Red," a self-play-trained automated red-teaming model aimed at improving robustness against prompt injection.
- 10 `/supply/product/*` pages — see "Supply Co." above.

## Routine updates

The remaining ~103 non-boilerplate-flagged pages all resolved, on inspection, to one of two patterns rather than real content changes:
1. **Footer/carousel churn** — the Supply Co. nav link (65 pages, pure), plus on many pages a rotating "related news" carousel (pointing at yesterday's/today's new articles) and the "Latest Advancements" model-badge list (GPT-5.6 added, GPT-5.3 Instant dropped) changing alongside it.
2. **Markdown-conversion duplication artifact** — a handful of pages (`index/introducing-gpt-5-2/`, `index/introducing-o3-and-o4-mini/`, `index/running-codex-safely/`, `index/chatgpt-for-excel/`, `index/introducing-data-residency-in-asia/`, `index/expanding-data-residency-access-to-business-customers-worldwide/`, `index/openai-pwc-finance-collaboration/`, `index/gpt-5-safe-completions/`, `form/report-content/`) showed large-looking diffs that turned out to be a page-metadata header block (date/tag/title/"Loading…"/"Share") or a table-of-contents/form-field block being emitted twice or in a different order between fetches — no body prose actually changed. This looks like a client-side rendering/hydration timing artifact in the fetch, not a real edit, similar to the "capture-timing artifact" flagged in the 2026-07-14 run. None of these old model-announcement pages were actually rewritten.

## Removals

- **`/codex/get-started/`** — the Codex onboarding walkthrough page was removed from the sitemap with no direct successor found; likely folded into the main `/codex/` page or the docs migration to `learn.chatgpt.com` noted in earlier runs. Last snapshot remains in git history.
