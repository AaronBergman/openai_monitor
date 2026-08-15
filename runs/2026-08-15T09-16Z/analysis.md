# Analysis — Run 2026-08-15T09-16Z

**Fetch time:** 2026-08-15T09:21:20Z UTC (sitemap fetch started 09:16Z, page fetches completed ~09:21Z)
**Baseline:** 2026-08-14T09-19Z (consecutive day)
**Totals:** 1,584 total URLs (baseline 1,582) | +4 added | -2 removed | 128 updated | 35 sub-sitemaps | 0 fetch failures

## Anomalies

No anomalies under the repo's automated checks (future-dated `<lastmod>`, backwards `<lastmod>`, backdated new URLs, reappeared URLs, sub-sitemap migrations) — all counts came back 0 across all 1,584 current URLs and all 128 updated URLs.

One editorial inconsistency worth flagging even though it isn't a timestamp anomaly:

- **[`/index/introducing-chatgpt-atlas/`](../../pages/openai.com/index/introducing-chatgpt-atlas/index.md)** picked up a new banner reading *"This post introduced ChatGPT Atlas. Atlas has since been deprecated,"* pointing readers to ChatGPT Work instead — yet the same page still displays a live "Download for macOS" button for Atlas immediately above the banner. Either the deprecation banner was applied to the wrong page/template, or Atlas is being wound down while the page hasn't been fully updated to match. Worth a follow-up check on the next run to see if the download CTA is removed.

**Continuing tracked anomaly — nav/template A/B flip:** The two-variant page-template flip-flop first spotted 2026-08-08 (an old-style header: "Why OpenAI / Solutions / Resources / Customers / Pricing" + "Try OpenAI"/"Contact sales", vs. a new-style header: "Research / Business / Developers / Company / Foundation" + "Log in"/"Try ChatGPT") recurred on 3 more pages this run: [`business/partners/cognizant/`](../../pages/openai.com/business/partners/cognizant/index.md) (old→new), [`business/plugins/microsoft-teams/`](../../pages/openai.com/business/plugins/microsoft-teams/index.md) (old→new), and [`business/plugins/snowflake/`](../../pages/openai.com/business/plugins/snowflake/index.md) (new→old — it had flipped the other direction as recently as 2026-08-14). `snowflake` and `partners/kpmg`-adjacent pages have now flipped on multiple separate days, confirming this is an unstable, ongoing A/B/edge-cache condition rather than a one-time migration.

## Significant findings

### Sitewide initiative: historical "legacy launch" banners added to ~29 old announcement pages
The single biggest pattern in today's diff. OpenAI added a short editorial banner to the top of roughly 29 old `/index/` and `/codex/` announcement posts — explicitly marking them as historical and pointing readers to current docs/pricing instead. Examples of the banner text, verbatim:

- [`/index/chatgpt/`](../../pages/openai.com/index/chatgpt/index.md) — "This post introduced ChatGPT in 2022. ChatGPT has evolved substantially since then."
- [`/index/gpt-4/`](../../pages/openai.com/index/gpt-4/index.md) — "This post introduced GPT-4 in 2023."
- [`/index/hello-gpt-4o/`](../../pages/openai.com/index/hello-gpt-4o/index.md) — "This post introduced GPT-4o in 2024."
- [`/index/dall-e-2/`](../../pages/openai.com/index/dall-e-2/index.md) / [`dall-e-3`](../../pages/openai.com/index/dall-e-3/index.md) — "This post introduced DALL·E 2 / 3."
- [`/index/whisper/`](../../pages/openai.com/index/whisper/index.md) — "This post introduced Whisper in 2022."
- [`/index/openai-api/`](../../pages/openai.com/index/openai-api/index.md) — "This post introduced the OpenAI API in 2020," with an added FAQ block from the original 2020 launch restored/re-surfaced above the fold.
- [`/index/chatgpt-plus/`](../../pages/openai.com/index/chatgpt-plus/index.md) — "This post covers the original Plus launch," linking to current ChatGPT pricing.
- [`/index/introducing-gpt-5/`](../../pages/openai.com/index/introducing-gpt-5/index.md), [`introducing-gpt-4-5`](../../pages/openai.com/index/introducing-gpt-4-5/index.md), [`introducing-gpt-5-5`](../../pages/openai.com/index/introducing-gpt-5-5/index.md) — each labeled as introducing that specific model version, now superseded.
- [`/index/introducing-operator/`](../../pages/openai.com/index/introducing-operator/index.md), [`introducing-canvas`](../../pages/openai.com/index/introducing-canvas/index.md), [`introducing-codex`](../../pages/openai.com/index/introducing-codex/index.md), [`introducing-the-codex-app`](../../pages/openai.com/index/introducing-the-codex-app/index.md), [`/codex/`](../../pages/openai.com/codex/index.md) — each flagged with "This post introduced X" / "This launch post is outdated."
- [`/index/introducing-chatgpt-atlas/`](../../pages/openai.com/index/introducing-chatgpt-atlas/index.md) — see Anomalies above; the only one asserting the underlying product itself is "deprecated," not just the post being old.
- [`/index/introducing-workspace-agents-in-chatgpt/`](../../pages/openai.com/index/introducing-workspace-agents-in-chatgpt/index.md) — took a different form: rather than "this is old," it added a note that Workspace agents are "**now generally available** in ChatGPT Business, Enterprise, and Edu," i.e. a GA-status update layered onto the original announcement.
- Also touched: `introducing-apps-in-chatgpt`, `introducing-chatgpt-agent`, `introducing-chatgpt-edu`, `introducing-chatgpt-health`, `introducing-chatgpt-search`, `introducing-chatgpt-small-business-program`, `introducing-4o-image-generation`, `new-chatgpt-images-is-here`, `start-using-chatgpt-instantly`, `gpt-4o-and-more-tools-to-chatgpt-free`.

This reads as a deliberate content-hygiene push: OpenAI's announcement archive stretches back to 2020, and many of those pages still displayed stale pricing, outdated CTAs, or superseded model names as if current. The new banners retroactively frame them as historical record and redirect traffic to live docs/pricing/release-notes pages. Notably, pages for products that are *still* current and actively marketed — Sora, Sora 2, the GPT Store, GPT-5.6 — did **not** get this banner, suggesting the banner rollout is being applied selectively to genuinely superseded launches rather than uniformly to every old post.

### ChatGPT release notes: five new entries (Aug 13)
[`/products/release-notes/`](../../pages/openai.com/products/release-notes/index.md) rolled forward, dropping four Aug 6–10 entries off the visible list and adding five dated Aug 13:
- **Ultrafast mode for GPT-5.6 Sol** (Preview) — the new low-latency API tier previewed on 2026-08-14 (see prior run) now has an official release-notes entry: "up to 14x faster than Standard processing... available in limited preview to select customers."
- **Google Drive is now in Library** (GA) — Drive files/folders browsable directly in ChatGPT's Library, with in-place Docs/Sheets/Slides viewing and folder-level querying. Shared Drives not yet included.
- **Chat model defaults** (GA) — workspace admins can now set an org-wide default chat model/reasoning level, or leave it to "user's last choice," from Workspace settings.
- **Updated model picker for Enterprise and Edu** (GA) — refreshed model-picker/composer UI for workspace members.
- **Audit logs in the Global Admin Console** (GA) — admins can review supported audit events directly from the Global Admin Console.

### Government solutions page: AWS GovCloud reaches FedRAMP High + IL5
[`/solutions/industries/government/`](../../pages/openai.com/solutions/industries/government/index.md) had its compliance table updated: "AWS GovCloud API" now shows checkmarks across **FedRAMP Low, Moderate, High, and IL5** (Impact Level 5) — previously listed as "Coming soon" across the board. The old "AWS GovCloud Stateful/Stateless Runtime" rows were consolidated into a single "AWS GovCloud API" row; "AWS GovCloud Codex" remains "Coming soon." The page also gained an extensive 17-question government-focused FAQ (products/features, security/compliance, cloud providers, pricing/procurement) that wasn't present before, including details on the $1/month GSA OneGov ChatGPT Enterprise offer (through end of September 2026) and confirmation that OpenAI operates on the GSA Multiple Award Schedule.

### New: ChatGPT Work sales-team marketing push
Two new lead-gen pages continue the "ChatGPT Work" B2B campaign flagged in prior runs:
- [`/business/learn/how-our-sales-team-uses-chatgpt-work/`](../../pages/openai.com/business/learn/how-our-sales-team-uses-chatgpt-work/index.md) — webinar signup form, "a behind-the-scenes look at how OpenAI uses ChatGPT Work across the sales organization."
- [`/business/learn/download-the-chatgpt-work-guide-for-sales-teams/`](../../pages/openai.com/business/learn/download-the-chatgpt-work-guide-for-sales-teams/index.md) — gated PDF guide covering "three connected workflows OpenAI's Sales team uses."

### Plugin directory: two URL slug renames (content unchanged)
- `/business/plugins/azure-boards/` → **[`/business/plugins/azure-devops/`](../../pages/openai.com/business/plugins/azure-devops/index.md)** (same page content, byte-for-byte, just a shorter/more accurate slug — the plugin has always been "Azure DevOps" branded in its body copy).
- `/business/plugins/data-analytics/` → **[`/business/plugins/data/`](../../pages/openai.com/business/plugins/data/index.md)** (same content; slug shortened from "data-analytics" to "data").

Both old slugs disappeared from the sitemap this run (counted as "removed" below) and are superseded by the new slugs (counted as "added"). This mirrors the `/business/plugins/microsoft-teams/` page's title shortening from "Microsoft Teams" to "Teams" spotted in this same run's nav-flip diff — a small ongoing naming-simplification pass across the plugin directory.

## Routine, low-signal updates

Of the 128 `<lastmod>`-updated URLs, 76 had an actual markdown content diff; the other 52 changed only their `<lastmod>` timestamp with byte-identical content (a "related articles" widget rotation or similar server-side re-render with no visible diff — html2text output was unchanged).

Of the 76 pages with real diffs, the overwhelming majority (roughly 60) share one recurring three-part pattern, unrelated to the page's own subject matter:
1. A duplicated "Table of contents" block was de-duplicated/reflowed (cosmetic template fix, no content change).
2. The "Latest Advancements" sidebar module was updated to list **GPT-5.6** and drop **GPT-5.3 Instant**.
3. The global nav gained **"Customer Stories"** and **"Partner Network"** under Business, and **"Supply Co."** under the main menu — continuing the sitewide nav/mega-menu expansion first spotted 2026-08-14.

Pages carrying only this routine three-part pattern (no other content change): `openai-on-aws`, `chatgpt-plus`, `chatgpt`, `gpt-4`, `sora`, `sora-2`, `superhuman`, `holiday-extras`, `introducing-the-gpt-store`, `introducing-gpts`, `introducing-child-safety-blueprint`, `introducing-the-teen-safety-blueprint`, `teen-safety-freedom-and-privacy`, `teen-safety-policies-gpt-oss-safeguard`, `japan-teen-safety-blueprint`, `our-commitment-to-community-safety`, `our-approach-to-age-prediction`, `update-on-mental-health-related-work`, `updating-model-spec-with-teen-protections`, `building-more-helpful-chatgpt-experiences-for-everyone`, `building-towards-age-prediction`, `helping-people-when-they-need-it-most`, `optimizing-chatgpt`, `how-chatgpt-protects-privacy`, `chatgpt-study-mode`, `ai-literacy-resources-for-teens-and-parents`, `introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock`, `expanding-daybreak-as-the-cyber-defense-window-narrows`, `putting-frontier-cyber-models-in-more-trusted-hands`, and several plugin/partner pages that only flipped their nav variant (see Anomalies).

The 8 partner pages with a 1-line diff (`accenture`, `accenture-federal-services`, `capgemini`, `cognizant`, `ernst-and-young`, `ibm`, `kpmg`, `pwc`) and `form/business/premium-offer` changed only a Contentful asset build-hash (`?dpl=dpl_...` query string on the "Advanced Partner" badge SVG) — a redeploy artifact, not a content change.

## New pages

- [`/business/learn/how-our-sales-team-uses-chatgpt-work/`](../../pages/openai.com/business/learn/how-our-sales-team-uses-chatgpt-work/index.md) — see Significant findings.
- [`/business/learn/download-the-chatgpt-work-guide-for-sales-teams/`](../../pages/openai.com/business/learn/download-the-chatgpt-work-guide-for-sales-teams/index.md) — see Significant findings.
- [`/business/plugins/azure-devops/`](../../pages/openai.com/business/plugins/azure-devops/index.md) — slug rename of `azure-boards`, see Significant findings.
- [`/business/plugins/data/`](../../pages/openai.com/business/plugins/data/index.md) — slug rename of `data-analytics`, see Significant findings.

## Removals

- `/business/plugins/azure-boards/` — superseded by `/business/plugins/azure-devops/` (slug rename, not a real removal).
- `/business/plugins/data-analytics/` — superseded by `/business/plugins/data/` (slug rename, not a real removal).

Both prior snapshots remain in git history (`git log -- pages/openai.com/business/plugins/azure-boards/index.md`, `git log -- pages/openai.com/business/plugins/data-analytics/index.md`).
