# Run 2026-07-23T09-17Z — Analysis

- Fetch time (sitemap + sub-sitemaps): 2026-07-23 ~09:17 UTC
- Baseline: 2026-07-22T09-16Z (previous run)
- Total URLs in current snapshot: 1470 (baseline: 1464)
- Sub-sitemaps: 34/34 fetched successfully (200 OK, no parse errors)
- Page fetches attempted: 54 (6 new + 48 updated) — 54/54 succeeded, 0 blocked/failed

## Anomalies

**None detected this run.** Specifically checked and clear:
- No `<lastmod>` later than fetch time (no claimed future modifications).
- No `<lastmod>` moved backwards vs. the prior snapshot.
- No new URL backdated (lastmod predating first_seen by more than a few days).
- No URL reappeared after previously disappearing.
- No URL migrated between sub-sitemaps.

## Significant updates (real content changes, not just a lastmod bump)

Of the 48 URLs whose `<lastmod>` changed, only 25 had an actual content diff; the other 23 were byte-identical to their prior snapshot (OpenAI appears to re-touch `lastmod` on some pages — e.g. via shared component/nav updates — without changing the page body). The 25 substantive changes:

1. **New global footer link: "Supply Co."** Added to the footer navigation on many pages (business/solutions pages, customer-stories, forms, etc.), between "Academy" and "Livestreams". The `/supply/` merch-store section itself already existed in the sitemap (11 product pages, unchanged), so this is a promotion of an existing section into the global footer nav, not a new page.

2. **"ChatGPT Work" webinar series launched across business/solutions pages.** The old generic "Introducing ChatGPT Work" promo banner was replaced on five team-specific solutions pages with a **live webinar** banner + a "Watch webinar" resource block, each with a distinct date:
   - `/business/solutions/data/` → Aug 11, 2026, 9:30am PT (Data Analytics team)
   - `/business/solutions/finance/` → Aug 4, 2026 (Finance team)
   - `/business/solutions/marketing/` → Aug 25, 2026 (Marketing team)
   - `/business/solutions/operations/` → Aug 18, 2026 (Business Operations team)
   - `/business/solutions/sales/` → Jul 30, 2026 (Sales team)
   - `/business/why-openai/enterprises/` and `/solutions/` dropped the old promo banner entirely (no replacement banner on those two).
   This reads as a coordinated marketing push turning the ChatGPT Work launch into a recurring webinar series, one per business function.

3. **"Life Sciences" rebrand/re-routing on the Enterprises solutions page.** `/business/why-openai/enterprises/` changed its "Life Sciences" card: image swapped (generic "1x1" placeholder → photo of people in lab coats) and the link target changed from `/solutions/industries/life-sciences/` to **`/gpt-rosalind/`**. GPT-Rosalind (OpenAI's bioscience-focused model, launched ~June 4, 2026) is now the enterprise entry point for the Life Sciences vertical, superseding the older generic solutions page. Consistent with today's new Genesis Mission announcement (see below) which also name-checks GPT-Rosalind for national-lab biology work.

4. **Nav model list refreshed:** "GPT-5.6" added to the Products flyout menu on several form pages; "GPT-5.3 Instant" removed from the same list. Reflects the site's current-model roster shrinking/rotating as usual.

5. **Release notes updated** (`/products/release-notes/`): added a new **API** entry dated Jul 20, 2026 (GA) — *"Organization and project spend limits for the OpenAI API platform"* (monthly spend caps / hard enforcement so API calls fail once a limit is hit). The page keeps a rolling window, so the oldest visible entry, *"ChatGPT returns to WhatsApp in the EEA"* (Jul 13), dropped off the bottom — not a retraction, just pagination.

6. **Automated red-teaming paper published**: `/index/unlocking-self-improvement-gpt-red/` swapped its "we will be releasing a pre-print with more details later this week" placeholder for a working link to the actual PDF (*gpt-red-automated-red-teaming-via-self-play-at-scale.pdf*) — the paper referenced in that announcement has now shipped.

7. **Customer-stories carousel** (`/business/customer-stories/`): NTT DATA Group case study (see new pages below) added to the front of the carousel; the older Wasmer story rotated off. Routine content-carousel churn, not a removal of the Wasmer page itself (it's simply no longer featured there).

8. **Enterprise cyber-access form** (`/form/enterprise-trusted-access-for-cyber/`): removed the required "OpenAI Organization ID" field — form is now easier to submit without already being a paying API org.

9. **Small-business leads form** (`/leads/small-business/`): minor copy tweak (dropped "AI guidance" language for generic "guidance"/"AI"), and the "Title" field changed from required to optional.

10. **Trademark/counterfeit disputes form** (`/form/trademark-counterfeit-disputes/`): added a required "link/URL to the content" field, section headers changed weight, and the country-picker list was re-localized (parenthetical/full country names, e.g. "Congo (DRC)", "Turkey" instead of "Türkiye") — looks like a country-picker library/data update rather than a policy change.

11. **Homepage and several article "related reading" rails refreshed** to surface today's new stories (OpenAI Presence, David Vélez/Robin Vince board news, national-science commitment, Effingham County) in place of older items — routine content-recirculation, expected on every run with new publications.

## New pages (6)

- **[Introducing OpenAI Presence](../../pages/openai.com/index/introducing-openai-presence/index.md)** — Announcement of **OpenAI Presence**, a new enterprise product for deploying "trusted AI agents" (voice + chat) into customer-facing and internal workflows, with policy/guardrail/escalation controls and a Codex-driven continuous-improvement loop. Paired with a dedicated landing page (`/business/openai-presence/`, also new today) featuring customer quotes from BBVA Mexico, SoftBank, and IAG (an Australian insurer) as design partners. This is the biggest news of the run — a new named enterprise product line.
- **[OpenAI Presence landing page](../../pages/openai.com/business/openai-presence/index.md)** — Sales-facing companion page to the announcement above (`/business/openai-presence/`), with a "Contact sales" CTA.
- **[Advancing the next era of national science](../../pages/openai.com/index/advancing-the-next-era-of-national-science/index.md)** — OpenAI commits to the U.S. Department of Energy's Genesis Mission: $4M in Codex access for ~2,000 researchers at National Labs/universities, $3M in API support for two large scientific campaigns, up to $10M in API usage matching $2.5M spent, GPT-Rosalind bioscience access for eligible national-lab biology projects, and expanded cyber-research access. Part of a broader public-sector/government-science push (Global Affairs).
- **[Building AI infrastructure with the Effingham County community](../../pages/openai.com/index/building-ai-infrastructure-with-the-effingham-county-community/index.md)** — Announces **Project Camellia**, a new 3.2-gigawatt data-center project in Effingham County, Georgia (with Georgia Power), phased 2028–2032. Commits: no rate increases for local residents, closed-loop (low) water use, $80M in community benefits, up to $71M in Codex credits for Georgia students, and an independent annual audit. Same playbook as prior data-center community-commitment posts (e.g. Abilene, TX). Public open house was scheduled for Jul 23 (today).
- **[How news organizations are using AI](../../pages/openai.com/index/how-news-organizations-are-using-ai/index.md)** — Company/PR roundup of news-industry partners (AP, POLITICO, Axios, Philadelphia Inquirer, Axel Springer, Le Monde, PRISA Media, Daily Beast, American Journalism Project, etc.) describing how each uses OpenAI tools in reporting/business workflows. References a renewed American Journalism Project local-news partnership announced the same day via Axios.
- **[NTT DATA Group cuts incident analysis to 30 minutes with Codex](../../pages/openai.com/index/ntt-data/index.md)** — New enterprise customer story: NTT DATA expanded Codex to ~9,000 employees after companywide ChatGPT Enterprise adoption; headline claim is a -99.3% time reduction on an incident-analysis task (5 engineers × 3 days → 30 minutes with Codex).

## Routine updates

Covered inline above (nav "Supply Co." link addition, related-articles carousel refreshes, GPT-5.6/5.3 nav swap) — no separate purely-cosmetic changes beyond what's listed.

## Removals

None. 0 URLs disappeared from the sitemap this run.

## Fetch failures

None. All 34 sub-sitemaps and 54 page fetches succeeded.
