# Run 2026-08-21T09-16Z — Analysis

- **Fetch time (root sitemap-index):** 2026-08-21T09:16:44Z
- **Baseline:** 2026-08-20T09-15Z (prior committed snapshot, 1601 URLs across 35 sub-sitemaps)
- **Current:** 1604 URLs across 36 sub-sitemaps
- **Diff:** 3 added, 0 removed, 118 updated (`<lastmod>` changed), 0 section migrations, 2 anomalies
- **Fetch failures:** none — all 121 added/updated pages fetched cleanly via `tools/html_to_md.py` (curl-cffi, Chrome impersonation)

## Anomalies

1. **New sub-sitemap section: `/sitemap.xml/ai-futures/`.** OpenAI added a 36th sub-sitemap section, `ai-futures`, that did not exist in the prior 35-section index. This corresponds to a brand-new content vertical (see "Notable additions" below). Not a data-integrity anomaly — a genuine structural change to the sitemap.
2. **Future `<lastmod>` (negligible clock skew).** `https://openai.com/business/plugins/investment-banking/` carries `<lastmod>2026-08-21T09:16:47.127Z`, which is ~3 seconds after our fetch time of `2026-08-21T09:16:44Z`. This is consistent with the page being re-rendered/re-deployed in the few seconds between our root-index fetch and our sub-sitemap fetch (likely an active redeploy in progress at fetch time), not a meaningful backdating/future-dating issue. No action needed; flagged for completeness per the routine's timestamp-discipline rule.

No backwards-lastmod, no reappeared URLs, and no cross-sub-sitemap migrations were detected this run.

## Significant updates (real content, not just carousel/nav churn)

Of the 118 URLs whose `<lastmod>` changed, a content diff (prior markdown snapshot in git HEAD vs. freshly fetched markdown, whitespace-normalized) classified 45 as no-op (identical rendered text — pure metadata/timestamp touch) and 73 as containing some rendered-text delta. Of those 73, the overwhelming majority (≈70) are routine template churn:

- **~55 `/business/partners/<name>/` pages**: the only change is a Vercel deployment-ID query parameter on the partner-tier badge SVG (`?dpl=dpl_93RPSLao...` → `?dpl=dpl_3J1J6ZgV...`), i.e. a site-wide redeploy touched every partner page's asset URL with no visible content change. Collapsed here as one line item rather than listed individually.
- **~10 `/index/*` and `/news/*` pages**: only their "related articles" / "latest news" carousel rotated to surface the day's two new posts (Introducing AI Futures, Stampli customer story) in place of older ones. No change to the pages' own body text.
- **`/business/pricing/`**: added a footnote asterisk (`/ user / month*`) pointing to existing billing terms already present lower on the page (2+ users, billed annually; $25/mo if billed monthly). Cosmetic clarification, not a price change.

The two genuinely notable content changes:

- **`https://openai.com/form/business/premium-offer/`** — The ChatGPT Business "Premium seats" promotional signup form has been taken down and replaced with: *"This promotion has ended, and we are no longer accepting submissions. Premium seats are coming soon to ChatGPT Business."* The prior version offered $100 in workspace credits per qualifying Premium seat (up to 5 seats) for the first 10,000 workspaces signing up before August 20, 2026 — i.e. the promotion's own stated deadline. This update landed the day after that deadline, closing the loop.
- **`https://openai.com/business/why-openai/startups/`** — Header nav was swapped to a newer "Why OpenAI / Solutions / Resources / Customers / Pricing" business-section nav (replacing the older global Research/Business/Developers/Company nav), and the page's event list was refreshed: two July webinar listings were replaced with an August 26 "Build Hour: Image Gen 2" session plus five new **"Builder Lounge"** in-person meetups (London Sept 3, Berlin Sept 9, Stockholm Sept 15, Paris Sept 22, Munich Sept 29), each co-hosted with a startup partner (Conduct, Parloa, Lovable, Photoroom, n8n respectively).

## New pages

1. **[`/index/introducing-ai-futures/`](../../pages/openai.com/index/introducing-ai-futures/index.md)** — Long-form post by Dean Ball launching **AI Futures**, the blog of OpenAI's new "Strategic Futures" team. The team's mandate: study how free societies should be restructured to preserve individual rights and agency as transformative AI emerges, with a particular focus on "concentration of power" risk — the risk that AI-enabled automation of force (autonomous systems) and revenue (data-center output vs. human labor) could let a state or actor sustain power without needing broad human cooperation, eroding the traditional check that a government needs its citizens' consent. The post explicitly frames itself as reflecting the author's views, not official OpenAI positions, and states future Strategic Futures output will include papers, videos, and podcasts. This is the top news item of the run — a new institutional/content vertical for OpenAI's policy voice, distinct from the existing Safety and Global Affairs sections.
2. **[`/news/ai-futures/`](../../pages/openai.com/news/ai-futures/index.md)** — The new category/index page for the AI Futures blog, and root of the new `ai-futures` sub-sitemap section. It's now also linked from the main `/news/` navigation alongside the existing categories (Company, Product, Safety, Security, Research, Global Affairs, Applied AI, AI Adoption, Engineering).
3. **[`/index/stampli/`](../../pages/openai.com/index/stampli/index.md)** — Customer story: "Stampli cuts launch hours by 68% using ChatGPT Work." Mid-market fintech company (finance/tech industry, North America) used Codex and ChatGPT Work to compress a product-launch production timeline. Fits the established, high-frequency cadence of ChatGPT-Work customer case studies (Replit, NVIDIA, SafetyKit, and others published in the same week).

## Removals

None this run.

## Fetch failures

None. All 121 added/updated URLs converted cleanly (no Cloudflare challenge-page results, all outputs well above the 100-character sanity threshold).
