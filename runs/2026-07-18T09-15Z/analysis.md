# Run 2026-07-18T09-15Z — Analysis

**Fetch time:** 2026-07-18T09:16:52Z
**Baseline:** 2026-07-17T09-16Z (consecutive day, no gap)
**Stats:** 1459 total URLs | +1 added | 23 updated (2 with a real content diff) | -0 removed | 0 anomalies | 34 sub-sitemaps

## Anomalies

None. Checked:
- No `<lastmod>` later than fetch time (2026-07-18T09:16:52Z) — latest observed lastmod was `2026-07-18T08:34:05.248Z` (`/devday/terms-and-conditions/`).
- No `<lastmod>` moved backwards vs. the prior snapshot for any of the 23 updated URLs.
- The 1 added URL (`/index/a-scorecard-for-the-ai-age/`) is genuinely new — not present in `state/known_urls.json` from any prior run.
- No URL disappeared and reappeared; removed count is 0.
- No URL migrated between sub-sitemaps.

## Significant updates

- **[`/index/gpt-5-6/`](../../pages/openai.com/index/gpt-5-6/index.md) — the "700,000 A100e GPU hours" figure is back.** On 2026-07-15 this repo flagged that the GPT‑5.6 safety section quietly dropped its specific red-teaming compute figure, going from "approximately 700,000 A100e GPU hours of black-box automated red teaming" to "approximately NVIDIA A100 Tensor Core GPU-equivalent hours of black-box automated red teaming" (no number). As of this run, the number is back: "approximately **700,000** NVIDIA A100 Tensor Core GPU-equivalent hours of black-box automated red teaming." Same figure as originally published, restored after roughly three days without it — looks like the vague phrasing was a copy-editing regression that's now been fixed rather than a deliberate retraction.
- **New company essay: [A scorecard for the AI age](../../pages/openai.com/index/a-scorecard-for-the-ai-age/index.md)** (see Notable additions).
- **[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md)** gained two entries (custom-instructions character limit raised, apps-with-sync now supports EKM workspaces) and, as this is a rolling recent-entries list, dropped its two oldest visible entries (the GPT‑5.6 launch announcement and the original ChatGPT Work announcement, both from Jul 9) off the bottom via a "Load more" pagination boundary. Those are not removals — the source pages for both announcements are still live and tracked; the changelog page just shows a limited window.
- **[`/index/why-teens-deserve-access-safe-ai/`](../../pages/openai.com/index/why-teens-deserve-access-safe-ai/index.md)** — a stat was quietly revised: "expanded those experiences to more than **250 new topics**" became "expanded those experiences to more than **300 topics total**." Note the phrasing changed shape (250 *new* topics added vs. 300 topics *total*) as well as the number, so this isn't simply "50 more topics were added since Jul 16" — it may be a correction to how the stat was framed.

## Routine updates

- **Partner-page nav/template catch-up.** `/business/partners/`, `/business/partners/accenture/`, `/business/partners/bain-and-company/`, `/business/partners/locator/`, and `/business/solutions/operations/` all lost the "New: Introducing ChatGPT Work" promo banner that had been sitting at the top of the page, and several partner pages picked up the "Supply Co." footer link and the redesigned "Research / Products / Business / Developers / Company / Foundation" nav. Both of these template changes were already reported in this log on 2026-07-17 (Supply Co. launch) and earlier; these particular partner pages simply hadn't been re-fetched since, so they show up as "changed" now even though the underlying edit is old news.
- **Cosmetic asset-URL churn.** `accenture/`, `bain-and-company/`, `hcltech/`, `unit8/`, and the `/business/partners/` hub all had partner-tier badge images and/or company logo images swapped for new CDN asset IDs (same visual badge/logo, new Contentful deploy hash or SVG re-export) — no visible content change.
- **`/index/cars24/`** — "Keep reading" carousel swapped one related-post tile for another (added today's new `a-scorecard-for-the-ai-age` tile, dropped the now-older `unlocking-self-improvement-gpt-red` tile). Routine carousel refresh.
- **Table-of-contents rendering artifacts** on `/index/introducing-gpt-5-3-codex/` and `/index/introducing-the-codex-app/` — a client-side ToC sub-list (e.g. "Coding / Web development / Beyond coding" under "Frontier agentic capabilities") that had rendered expanded in the prior snapshot rendered collapsed this time. Same capture-timing artifact noted in prior runs' analyses, not a content edit.
- **9 pages with lastmod bumps but byte-identical markdown**: `/chatgpt-work/`, `/codex/`, `/company/public-policy/`, `/devday/terms-and-conditions/`, `/index/advancing-ai-safety-through-state-and-federal-action/`, `/index/codex-flexible-pricing-for-teams/`, `/index/codex-for-almost-everything/`, `/index/devday-2026/`, `/index/introducing-gpt-5-3-codex-spark/`, `/index/unlocking-self-improvement-gpt-red/`. Sitemap `<lastmod>` moved forward on all of these with no detectable content change — likely a redeploy/cache-purge touching the timestamp without an edit.

## New pages

- **[`/index/a-scorecard-for-the-ai-age/`](../../pages/openai.com/index/a-scorecard-for-the-ai-age/index.md)** (Jul 17, 2026, bylined by CFO Sarah Friar, tagged Company/Enterprise/GPT) — introduces a four-part economic framework OpenAI is calling "Useful Intelligence per Dollar": (1) how much useful work gets done, (2) what a successful task costs, (3) how often AI gets the work right (dependability), and (4) whether each AI dollar buys more work as usage grows. Pitched explicitly at CFOs evaluating AI ROI. Uses GPT‑5.6's three-tier lineup (Sol/Terra/Luna) as the running example of "efficiency + capability" and cites a benchmark claim: GPT‑5.6 Sol with max reasoning hits 72.7% on the DeepSWE v1.1 long-horizon engineering benchmark, above "Claude Fable 5" at 69.9%, at 36.2% lower estimated API cost. This is a companion piece to the ChatGPT Work push and GPT‑5.6 launch covered in this log over the last several days — reads as OpenAI's enterprise-sales pitch for why higher-capability/higher-price models can still be the cheaper choice per completed task.

## Removals

None this run.
