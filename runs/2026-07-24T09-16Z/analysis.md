# Run 2026-07-24T09-16Z — Analysis

- Fetch time (sitemap + sub-sitemaps): 2026-07-24 ~09:17 UTC
- Baseline: 2026-07-23T09-17Z (previous run)
- Total URLs in current snapshot: 1472 (baseline: 1470)
- Sub-sitemaps: 34/34 fetched successfully (200 OK, no parse errors)
- Page fetches attempted: 53 (2 new + 51 updated) — 53/53 succeeded, 0 blocked/failed

## Anomalies

**None detected this run.** Specifically checked and clear:
- No `<lastmod>` later than fetch time (no claimed future modifications).
- No `<lastmod>` moved backwards vs. the prior snapshot.
- No new URL backdated (lastmod predating first_seen by more than a few days). Both new URLs have lastmods within ~1 day of first_seen.
- No URL reappeared after previously disappearing (0 removed this run, and both new URLs are confirmed absent from all prior `state/known_urls.json` history).
- No URL migrated between sub-sitemaps.

## Significant updates (real content changes, not just a lastmod bump)

Of the 51 URLs whose `<lastmod>` changed, only 27 had an actual content diff; the other 24 were byte-identical to their prior snapshot (routine re-touch of `lastmod` with no visible body change — consistent with the pattern noted in prior runs). The substantive changes:

1. **"Health in ChatGPT" launches to general availability.** The biggest news of the run. OpenAI shipped a new [Health in ChatGPT](../../pages/openai.com/index/health-in-chatgpt/index.md) announcement (new page, dated Jul 23) rolling the previously waitlisted "ChatGPT Health" experience out to all logged-in U.S. users 18+ (Free, Go, Plus, Pro; web + iOS). Key mechanics:
   - Users can connect Apple Health and supported medical records (One Medical, Function Health, U.S. hospital systems) so ChatGPT can draw on that context across *any* conversation, not just inside a dedicated Health space — a change driven by their own data showing >70% of health-related conversations happened outside the dedicated space during the earlier limited test.
   - Connected medical data and any conversation using it is excluded from model training and ad targeting, with a 30-day deletion window on disconnect.
   - GPT‑5.6 Sol is positioned as "our strongest model yet for health," said to outperform GPT‑5.5 on HealthBench Professional; GPT‑5.5 Instant remains the free-tier health model.
   - The original **[Introducing ChatGPT Health](../../pages/openai.com/index/introducing-chatgpt-health/index.md)** post (the limited-waitlist announcement) was retroactively edited with an editor's note pointing to today's GA post, and its "Join the waitlist" link was removed — the waitlist is over.
   - **[Release notes](../../pages/openai.com/products/release-notes/index.md)** got a matching "GA" entry for the same rollout, plus a separate iOS Codex app update (Mermaid diagram rendering in task transcripts, interactive forms in Codex tasks, prompt recovery when switching tasks/hosts/workspaces).
   - This is now the headline story across the site: it's the new "Recent news" / "Keep reading" lead item on the homepage and on roughly a dozen unrelated pages we fetched today (a routine content-recirculation pattern seen on every major announcement day, not a per-page content change).

2. **ChatGPT Sites Terms of Service updated to allow e-commerce (Jul 9 → Jul 23).** [`/policies/chatgpt-sites-terms/`](../../pages/openai.com/policies/chatgpt-sites-terms/index.md) added a brand-new **Section 2.6 "E-Commerce"**: site builders may now integrate third-party payment providers to sell goods/services and collect payments directly through a ChatGPT Site, with the builder bearing responsibility for fulfillment, refunds, tax remittance, and compliance. The previous terms explicitly *prohibited* "money transfers, cryptocurrency transfers, or other financial or investment transactions" on ChatGPT Sites (old §2.5(e)); that blanket ban is now narrowed to carve out payment-provider-mediated e-commerce. The terms also added sanctions/export-control representations (builders and end users must not be sanctioned parties) and extended the HIPAA/PCI-DSS carve-out to cover data handled solely by a third-party payment processor. Read together with the ongoing "Supply Co." merch-store footer rollout (first spotted 2026-07-23), this looks like the legal groundwork for letting ChatGPT Sites function as storefronts — a notable expansion of what the platform allows.

3. **"ChatGPT Work" promo continues winding down / rotating to other CTAs.** Following yesterday's removal of the old promo banner from two pages, today `/business/learn/` and `/business/solutions/design/` also dropped the "Introducing ChatGPT Work" banner with no replacement. Separately, `/chatgpt-work/` itself reordered its events section (added a new "Academy webinars" card pointing to an OpenAI Academy events feed, alongside existing "Build Hour" and "OpenAI Build Week" cards) and **removed the caveat "Web and mobile access is rolling out to Plus, Pro, Business, and Enterprise users"** from its task-management feature description — read together, this suggests that ChatGPT Work's web/mobile task access has now fully rolled out rather than being partial.

4. **"How Codex became a collaborator for OpenAI's creative team" — new "OpenAI on OpenAI" case study** (new page, `/index/codex-collaborator-creative-team/`, page-dated Jul 16 but only appearing in the sitemap today with lastmod Jul 23 — a several-day gap between the stated publish date and its first appearance in our crawl, though not large enough to trip the formal backdating anomaly threshold). Profiles Chad Nelson, an OpenAI Creative Specialist, describing how he uses Codex (not just ChatGPT) to build custom creative tooling — sliders/controls for camera composition, lighting, and shadow depth — grounded in brand books, style guides, and campaign briefs. It replaced an older "Building OpenAI with OpenAI" story in the `/business/learn/` carousel, continuing that recurring internal-dogfooding content series.

5. **Signals resource library refreshed.** `/signals/` and `/signals/research/` added a new report, **"The AI jobs transition framework for the EU"** (dated June 2026 despite appearing today — a PDF mapping near-term AI job impacts in the EU labor market), and added an event-replay video "Inside OpenAI: How OpenAI teams use Codex to do more" (from a Jul 14 livestream) to the Recent News rail. The older "Unlocking economic opportunity" (Jul 2025) report was dropped from the reports list — rolling-window pagination, not a retraction.

6. **Site-wide nav churn continues.** As in prior runs: "GPT-5.6" added / "GPT-5.3 Instant" removed from the Products flyout "Latest Advancements" list on several pages (careers, open-model-feedback, api-scale-tier, form/copyright-disputes, guides-and-resources); "Customer Stories" and "Partner Network" links added to the Business footer column on the same pages; "Supply Co." footer link continues spreading to pages that hadn't picked it up yet (careers, open-model-feedback, api-scale-tier, copyright-disputes form, deep-research, what-parameter-golf-taught-us, signals, signals/research, chatgpt-sites-terms, all guide/case-study pages fetched today). This is the same nav/footer template rollout first spotted 2026-07-23, still propagating page-by-page as pages get re-rendered.

7. **Copyright disputes form (`/form/copyright-disputes/`) lost a field**: the "Please provide a link/URL to the material claimed to be infringing" input (shown under the "Material that is accessible through a link... in ChatGPT search or Browse, or SearchGPT" category) disappeared from today's snapshot. Flagging with lower confidence than other findings — this could be a real field removal, or it could be an artifact of the form rendering a different default category selection on this particular fetch (conditional fields tied to a dropdown state can render differently run-to-run without any policy change). Will watch for whether it stays gone on the next run.

8. **"Related reading" / "Recent news" carousels refreshed** on the homepage and ~10 index/ pages to surface today's new Health in ChatGPT and (secondarily) OpenAI Presence / national-science stories in place of older items — routine content-recirculation, expected whenever a major story ships.

## Routine updates (lastmod bumped, byte-identical content)

24 URLs re-touched `lastmod` with no visible change: `/`, several `/business/*` and `/index/*` pages already covered above under their "changed" counterparts, plus (among others) `/index/a-scorecard-for-the-ai-age/`, `/index/hugging-face-model-evaluation-security-incident/`, `/index/safety-alignment-long-horizon-models/`, `/index/introducing-chatgpt-small-business-program/`, `/index/david-velez-robin-vince-join-openai-boards/`, `/index/devday-2026/`, `/index/openai-scholars/`, `/business/*` solutions/why-openai pages, `/business-data/`, `/business/openai-presence/`, `/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/`, `/business/why-openai/{enterprises,small-business,startups}/`, `/contact-sales/`, `/form/{codex-project-showcase-and-feedback,trademark-counterfeit-disputes}/`, `/index/{advancing-the-next-era-of-national-science,building-ai-infrastructure-with-the-effingham-county-community,how-news-organizations-are-using-ai,introducing-openai-presence}/`, `/solutions/`. These read as backend cache-invalidation / republish timestamp bumps with no visible content change.

## New pages (2)

- **[Launching Health in ChatGPT](../../pages/openai.com/index/health-in-chatgpt/index.md)** — see item 1 above. The GA rollout announcement for Health in ChatGPT.
- **[How Codex became a collaborator for OpenAI's creative team](../../pages/openai.com/index/codex-collaborator-creative-team/index.md)** — see item 4 above. "OpenAI on OpenAI" internal case study.

## Removals

None.

## Fetch failures

None. All 53 URLs (2 new + 51 updated) fetched successfully via `tools/html_to_md.py` (curl-cffi, Chrome impersonation); no Cloudflare challenge pages encountered.

## Summary

A moderate day dominated by one real product launch (Health in ChatGPT going GA) and one notable legal/policy change (ChatGPT Sites Terms now permit e-commerce via third-party payment providers). Total URL count ticked up by 2 (1470 → 1472), 51 lastmod changes but only 27 with substantive diffs — the rest were routine re-touches or continued propagation of the nav/footer template rollout first seen 2026-07-23. No anomalies.
