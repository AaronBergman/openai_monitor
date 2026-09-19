# Analysis — 2026-09-19T09-15Z

**Fetch window:** 2026-09-19T09:15Z–09:19Z UTC (sitemap fetch + 42 sub-sitemap fetches + 459 page fetches)
**Baseline:** 2026-09-18T09-15Z (consecutive day)
**Sitemap sections:** 42 (up from 40 — two new sections: `plugins-customer-support`, `plugins-hr`)
**Totals:** 1,974 URLs (up from 1,748) | 226 added | 233 lastmod-updated (109 with a real content diff, 124 with no visible change) | 0 removed | 0 fetch failures

## Anomalies

No future-dated `<lastmod>` values (checked all 1,974 current URLs against fetch time), no backwards-moving `<lastmod>` values (checked all 233 updated URLs against their prior recorded value), no new URL backdated relative to its first_seen date (all 226 added URLs carry `<lastmod>` of 2026-09-18 or 2026-09-19 — same-day or day-before, consistent with a genuine launch), and no reappeared URLs (none of the 226 added URLs were previously tracked in `state/known_urls.json`).

Three structural anomalies, all clearly explained by a single event — a large-scale expansion of the business-plugins directory:

- **New sub-sitemap section `plugins-customer-support`** (9 URLs): Gleap, Muninx, Ventor, Pylon, EasyReply, Unthread, Support Ticket Validator, Zendesk, Text.
- **New sub-sitemap section `plugins-hr`** (8 URLs): Ashby, Workable, Teamtailor, Metaview, Gusto (cross-listed, see below), Lattice, LinkedIn, Upwork, Manatal.
- **Cross-listing addition**: `business/plugins/gusto/` (already listed under plugins-finance, plugins-operations, plugins-small-business) gained a 4th category, plugins-hr — consistent with the new HR category backfilling relevant existing listings rather than only holding brand-new ones.

No section migrations (URLs moving from one category to another) this run, unlike the prior two runs.

## Significant updates (real content diffs)

Ranked by the size of the change:

1. **`business/partners/` (partner directory, similarity 0.49, largest diff of the run)** — every one of the ~140 partner logos in the grid is now a clickable link to that partner's own `/business/partners/<slug>/` profile page (previously plain logo + name, no link). Structural/UX change, not new partners.
2. **`business/plugins/` (plugin directory landing page, similarity 0.66)** — full redesign: new hero copy ("Work across your favorite apps from ChatGPT" replacing "Connect your business plugins to your AI workflows"), a new row of 12 example-prompt cards for flagship plugins (Slack, Gmail, GitHub, HubSpot, Figma, Adobe, Salesforce, Outlook, Databricks, Canva, Snowflake), an expanded category tab list (Customer Support and HR added; Small Business/Legal/Operations/Education reordered), a new "Add plugins in a few clicks" 3-step walkthrough with screenshots (Find a plugin → Install and connect → Put it to work), and a rewritten FAQ block (dropped "which plans include plugins" and MCP-building-for-your-org copy in favor of workspace-admin/access-control framing).
3. **`products/release-notes/` (similarity 0.83)** — 3 new entries dated Sep 17, 2026: **ChatGPT for Word** (GA) — ChatGPT sidebar now in Microsoft Word, joining Excel and PowerPoint, on all plans including Free, with Word access enabled by default starting Oct 1, 2026 for Business/Enterprise/Edu; **multi-account plugin connections** (GA) — ChatGPT can now connect more than one account per plugin (previously limited mostly to Gmail/Calendar/Contacts), letting users mix personal and work accounts in one conversation; **SCIM for API Platform** (GA) — tenant-wide SCIM now provisions API Platform access for Enterprise/Edu admins via synced identity-provider groups.
4. **224 individual `business/plugins/*` pages (~30-37 diff lines each, similarity ~0.93-0.94)** — sitewide template refresh matching the directory redesign: "Add plugin" CTA renamed to "Install plugin"; a new example-prompt teaser section mirroring the directory cards; "Common use cases" renamed "What else can you do?" with descriptive paragraphs trimmed; use-case links changed from generic "(opens in a new window)" to "Try in ChatGPT Work(opens in a new window)" and gained a `surface=work` query parameter; and the "What's included → App" field now shows the human-readable app name (e.g. "Gmail") instead of a raw internal connector ID (e.g. `connector_2128aebfecb84f64a069897515042a44`) — a display bug fix.
5. **`index/astra-for-law/`** — gained a fourth law-firm testimonial: **Skadden** joins Cooley and Ropes & Gray with a quote about building AI tools for regulatory-risk assessment, alongside its logo added to the customer-logo strip.
6. **`api/` (developer platform landing page)** — top nav and hero CTA changed from "Start building → platform.openai.com" to "Try ChatGPT → chatgpt.com"; a minor but notable positioning shift pushing ChatGPT ahead of direct API-platform signup even on the API homepage.
7. **~15 other `/index/*` article pages** — the only change was the "Keep reading" / recent-posts carousel picking up the two new pages published today (see below); no article-body edits. Three partner-profile pages (exl-service, kpmg, quantiphi) changed only a CDN deploy-hash in their partner-tier-badge image URL — no content change.

## New pages

- **[Introducing the Australian Youth Safety Blueprint](../../pages/openai.com/index/australian-youth-safety-blueprint/index.md)** (Sep 18, 2026) — a policy document/PDF laying out six pillars for protecting teens using AI in Australia (AI literacy, age-appropriate safeguards, privacy-protective age assurance, crisis-support links, parental controls, and industry accountability). Ties directly to the ChatGPT for Teens rollout that began in Australia in August.
- **[Hex turns complex analysis into visual reports with GPT‑6 Astra](../../pages/openai.com/index/hex-gpt-6-astra/index.md)** — new startup customer case study: Hex (agentic data platform) uses GPT‑6 Astra to generate interactive data-visualization artifacts; quote from co-founder/CTO Caitlin Colgrove.
- **224 new business-plugin listing pages** — the plugin directory roughly doubled in size in a single day (was ~110 pages as of yesterday's run, now well over 300). This reads as a bulk opening of the directory to MCP-based third-party integrations rather than a curated slow rollout. Notable/recognizable names among the new listings:
  - **Dev/infra tooling**: GitLab, Datadog, Supabase, DigitalOcean, Render, Railway, Neon, Temporal, Sanity, Vanta (security/compliance), Malwarebytes, CircleCI-adjacent (codex-security), Twilio Developer Kit, Context7 (docs lookup), MCP server for WordPress
  - **AI/agent/search tooling**: Manus, Browser Use, Firecrawl, Exa, Tavily AI, Parallel Search, Wolfram, ElevenLabs, Krisp, Otter.ai, Granola, Fathom, Circleback (meeting-notes/transcription cluster)
  - **Finance/markets**: Binance, CoinGecko, CoinMarketCap, Alpha Vantage, Interactive Brokers, Longbridge, Xero, NetSuite, QuickBooks Online connector, FactSet, Quartr, S&P Global (sp-global-deterministic)
  - **Sales/CRM/marketing**: Apollo, Attio, Close, Gong, Outreach, Demandbase, LinkedIn, LinkedIn Ads, Ahrefs, Windsor AI (Facebook/Google Ads), Metricool, ChatGPT Ads Manager
  - **Productivity/creative**: Trello, Webflow, Miro, Lucid, Whimsical, Gamma, Coda, Smartsheet, Typeform, Jotform, Calendly, Zoom Revenue Accelerator, Canva-adjacent design tools (Magnific, Picsart, Shutterstock), video generators (HeyGen, Runway, Kling AI, InVideo, Descript)
  - **HR/recruiting**: Ashby, Workable, Teamtailor, Metaview, Lattice, Upwork, Manatal
  - **Customer support**: Zendesk, Pylon, Unthread, Gleap
  - **Research/academic**: Zotero, Elicit, Consensus, SciSpace, Scite, Khan Academy, Coursera
  Full list of all 226 new URLs (224 plugins + the 2 pages above) in [`diff.json`](diff.json).

## Removed pages

None this run.

## Fetch failures

None — all 459 added/updated pages (226 new + 233 updated) fetched and converted successfully.
