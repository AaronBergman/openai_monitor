# Run 2026-11-11T09-16Z — analysis

- **Run start:** 2026-11-11T09:16Z UTC
- **Sitemap fetch time:** 2026-11-11T09:17:16Z (root index + 43 sub-sitemaps)
- **Page fetch window:** 2026-11-11T09:17:56Z – 09:20:18Z (1,933 pages via `tools/html_to_md.py`, 10 workers, **0 failures**)
- **Merged baseline:** `2026-09-28T09-17Z` (the last run merged into `main`)
- **Reference snapshot for "what's new today":** `2026-11-10T09-16Z`, from the unmerged branch `claude/festive-wright-vnx9wp`

## Important context: why the baseline is six weeks old

The routine *has* been running every day. But none of its pull requests since 2026-09-28 (about 43 of them, from 2026-09-29 to 2026-11-10) have been merged into `main`. Each new run starts from `main`, so each one diffs against the 2026-09-28 snapshot and reports six weeks of change again. (The 2026-11-10 README entry described this as a "43-day gap" in which the routine "did not run". That's wrong: the runs happened, they just weren't merged.)

This run therefore reports two layers:
1. **The required diff against the merged baseline (2026-09-28):** 214 added, 1,719 updated, 29 removed. This is what goes in `diff.json`, the stats and `state/known_urls.json`.
2. **The changes since yesterday's unmerged snapshot (2026-11-10):** 30 added, 294 `<lastmod>` bumps (139 with a real rendered change, mostly carousel rotation), 13 removed. Those 13 removals are relocations to new URLs. This layer shows what actually happened in the last 24 hours. It is recorded under `since_prior_unmerged_run` in `diff.json`.

## 1. Anomalies (highest signal)

**Since yesterday (2026-11-10 → 2026-11-11):**
- **13 URL relocations (`url_relocation`).** Pages were moved to new URLs, with the old URL removed and the new one added in the same window:
  - Solutions pages moved under `/business/solutions/`: `/solutions/industries/financial-services/`, `/solutions/industries/retail/`, `/solutions/use-case/content-creation/`, `/solutions/use-case/data-analysis/` and `/solutions/blueprints/knowledge-retrieval/` now live at `/business/solutions/{financial-services,retail,content-creation,data-analysis,knowledge-retrieval}/`.
  - Webinars and guides moved under `/business/learn/` (6 pages: two webinars, two `guides-and-resources/` guides, and the 2025 March and April "New in ChatGPT for business" pages).
  - Two customer stories moved from `/index/` to `/business/customer-stories/` (`ada`, `blue-j`).
  This continues the `/business/` information-architecture consolidation seen over recent weeks. It's a reorganisation, not a deletion.
- **`<lastmod>` moved backwards:** `/index/retell-ai/` went from `2026-11-09T22:47:55.896Z` (in the 2026-11-10 snapshot) to `2026-10-30T02:55:47.970Z`, but its rendered content is byte-identical to yesterday's. It looks like a CMS revert or republish of an older revision's timestamp. Against the merged 2026-09-28 baseline (where the URL didn't exist yet) it isn't backwards, so it is logged once with this context.
- **Sub-sitemap migration today:** `/business/plugins/parallel-search/` moved from `plugins-engineering-it` to `plugins-productivity`.

**Cumulative against the merged baseline (2026-09-28), mostly already seen in the unmerged runs:**
- **55 × `backdated_new_url`:** new URLs whose `<lastmod>` is more than 3 days older than this run's first observation. Almost all of this comes from the six-week merge gap, not from OpenAI backdating anything. The one cluster that looks like a real republish is `/business/learn/*` (older-model guides and webinars re-homed under a new section).
- **3 × `reappeared_url`:** `/business/plugins/alpaca/` (last seen 2026-09-24, now retitled "Alpaca Live"), `/form/codex-ambassadors/` (last seen 2026-06-24) and `/policies/row-privacy-policy/` (last seen 2026-05-27).
- **9 × `sub_sitemap_migration`:** six `/business/learn/*` pages moved out of the catch-all `page` sitemap into the `learn-webinars` and `learn-guides` sitemaps, and between those two. Three plugins were recategorised: `tableau` (data-research → productivity), `sync-labs` (productivity → design-creative) and `parallel-search` (engineering-it → productivity, today). The 2026-11-10 run reported "no sub-sitemap migrations", which this run corrects.
- **1 × `new_sub_sitemap`:** `sitemap.xml/learn-demos/` (first appeared during the gap; there are now 43 sub-sitemaps).
- No future-dated `<lastmod>` values.

## 2. Significant updates

**Today:**
- **Legal terms rewritten for "Businesses in ChatGPT"** (in step with the launch below):
  - [`/policies/service-terms/`](../../pages/openai.com/policies/service-terms/index.md): "Updated" date moved from October 16 to **November 10, 2026**. The GPT section is now "Third Party GPTs **and Business Agents**", and the abuse-reporting, Actions and removal clauses now cover Business Agents. There is a new **§16 "Businesses in ChatGPT"**, which points to the new Businesses in ChatGPT Terms.
  - [`/policies/ad-tools-terms/`](../../pages/openai.com/policies/ad-tools-terms/index.md): "Published" date moved from October 21 to **November 10, 2026**. §4 "Business Agents" used to say that agents OpenAI builds for advertisers fall under the GPT-builder provisions of the Service Terms. It is now **§4 "Businesses in ChatGPT"**, which incorporates the new standalone terms by reference.
  - [`/policies/`](../../pages/openai.com/policies/index.md) index: adds Businesses in ChatGPT Terms, the Businesses in ChatGPT policy and the Business agents policy. The "Creating images and videos in line with our policies" (Sora) entry is no longer listed.
- **Promotion of the launch across business pages:** [`/business/`](../../pages/openai.com/business/index.md) gains a "Businesses in ChatGPT" product tile, and [`/business/why-openai/small-business/`](../../pages/openai.com/business/why-openai/small-business/index.md) gets a "New — Introducing Businesses in ChatGPT" banner. [`/business/pricing/`](../../pages/openai.com/business/pricing/index.md) dropped its Rosalind Academic Plan line.
- **Plugin renames:** Supermetrics is now "Supermetrics Marketing Agent", with social-posting and comment-reply abilities added to its description. Alpaca is now "Alpaca Live". About 30 other plugin pages had small listing edits.
- **Testimonial carousels gone from 10 article pages:** two-quote carousels ("1 of 2") no longer appear in our scrape of `gpt-6-astra`, `airbnb-gpt-6-astra`, `astra-for-law`, `atlassian-partnership`, `introducing-chatgpt-financial-services` (Morgan Stanley/Evercore and S&P Global/LSEG quotes), `openai-models-google-cloud` (Brockman/Kurian), `openai-servicenow-partnership-expansion`, `openai-to-acquire-ona`, `paul-christiano-joins-openai-foundation-board` and `uber-chatgpt-work-rollout`. Because the same component vanished on all 10 pages at once, this is most likely a template change (the carousel now renders on the client) rather than editorial removal of the quotes. **Needs follow-up:** check next run whether the quotes come back.

**Cumulative since 2026-09-28** (detailed in the unmerged 2026-10 and 2026-11 runs, and confirmed in this run's page fetches, where every one of the 1,719 updated pages differs from its 2026-09-28 markdown):
- The site-wide header and footer navigation was reworked: GPT-6.1 Sol, GPT-6 Astra, Dots, Plugins and OpenAI Status links were added, and GPT-5.4 and Apps SDK/Open Models links were dropped. This accounts for most of the 1,719 changed pages.
- [Cookie policy](../../pages/openai.com/policies/cookie-policy/index.md) last updated Oct 22, 2026, adding ads- and help-domain cookies. [Usage policies](../../pages/openai.com/policies/usage-policies/index.md) and the [supplier code](../../pages/openai.com/policies/supplier-code/index.md) were also edited.

## 3. Routine updates

- Today: 155 of the 294 `<lastmod>` bumps had byte-identical rendered markdown, which is pure timestamp churn. Most of the remaining 139 are "Keep reading" or recent-news carousels rotating in today's new posts (Veterans, Caregivers, Businesses in ChatGPT, Australian universities), with no editorial change.

## 4. New pages

**Today (30 URLs; 17 are new content, the other 13 are the relocations above):**
- **[Introducing Businesses in ChatGPT](../../pages/openai.com/index/introducing-businesses-chatgpt/index.md)** (dated Nov 10, 2026) and the landing page **[Your business, in ChatGPT](../../pages/openai.com/business/businesses-in-chatgpt/index.md)**. This is a beta launch in which businesses can **claim and verify their listing in ChatGPT** through a new *Business Hub*. Verified businesses get a blue check, can update their details and product feeds (pricing and availability), and see aggregated insights such as how often ChatGPT mentions them, website clicks, and "discovery topics". Eligible businesses can launch a **Business Agent**, a labelled, separate chat in which customers question the business's own agent. Business Agents can be **sponsored as the destination for ChatGPT Ads**. Agents are available first to US e-commerce and online-service businesses. Shopify merchants get a 3-step on-ramp. OpenAI states that claiming "does not guarantee higher placement", and that user conversations are not shared with businesses. Three new policy pages go with it: [Businesses in ChatGPT policy](../../pages/openai.com/policies/businesses-in-chatgpt/index.md), [Business Agents Policy](../../pages/openai.com/policies/business-agents-policy/index.md) and [Businesses in ChatGPT Terms](../../pages/openai.com/policies/businesses-in-chatgpt-terms/index.md). In context, this is the next step in the ads and commerce push documented through October and November (ads in 26 new countries, a new ads format, the ad stack, ad-tools terms). OpenAI is building a local-search/Yelp-style business-listing layer, plus agent-based commerce, inside ChatGPT.
- **[Work at the Frontier: AI's effect on freelance work](../../pages/openai.com/index/ai-effect-on-freelance-work/index.md):** joint OpenAI–Upwork research. Demand is shifting across freelance categories, and AI-related postings combine more varied skills (task mix "45% more diverse", 2023 to 2025) with larger budgets. It's the second "Work at the Frontier" report after the Sep 2026 one on `/signals/`.
- **[ChatGPT Plus for veterans and servicemembers](../../pages/openai.com/index/chatgpt-plus-for-veterans/index.md)** (Nov 11, timed for Veterans Day): more than 20,000 veterans have claimed a free year of Plus, and nearly 1,000 attended trainings.
- **[Helping caregivers use AI in everyday life](../../pages/openai.com/index/helping-caregivers-use-ai-in-everyday-life/index.md):** OpenAI Academy workshops in 5 US cities with the Caregiver Action Network, the Alzheimer's Association and the American Diabetes Association. It cites an estimate of 40M+ weekly US ChatGPT health messages asked on someone else's behalf.
- **Customer stories:** [Cogent Security](../../pages/openai.com/index/cogent-security/index.md) ("cyber defense factories", 75% lower time to remediate vulnerabilities; uses Daybreak), [Singapore Airlines](../../pages/openai.com/index/singapore-airlines-travel-work/index.md) (2× CSAT for the Kris chatbot) and a [Gilbert + Tobin CEO interview](../../pages/openai.com/index/gilbert-tobin-sam-nickless/index.md).
- **Six healthcare plugins on the same day:** [Aiva](../../pages/openai.com/business/plugins/aiva/index.md) (clinician assistant), [Luma Health](../../pages/openai.com/business/plugins/luma-health/index.md) (healthcare admin), [Stedi](../../pages/openai.com/business/plugins/stedi/index.md) (insurance-benefit verification), [Subsalt](../../pages/openai.com/business/plugins/subsalt/index.md) (data analysis), [Turquoise](../../pages/openai.com/business/plugins/turquoise-health/index.md) (healthcare pricing) and [UpToDate Expert AI](../../pages/openai.com/business/plugins/uptodate-expert-ai/index.md) (clinical answers with sources). A clear healthcare-vertical batch, in line with the earlier "OpenAI for Healthcare" and "making ChatGPT better for clinicians" posts.

**Cumulative since 2026-09-28 (214 URLs):** the full list is in Appendix B. Highlights, already analysed in the unmerged runs: GPT-6.1 Sol and Terra, "dots" agents, GPT-6 for everyone, GPT-6 Cyber, the DevDay 2026 recap, OpenAI models on Google Cloud, the Orchestra Bio and Pierre acquisitions, Control Room, an updated Model Spec, a disrupted distillation campaign, the ChatGPT Ads expansion, the Marketplace and Private Intelligence offerings, about 30 customer stories, 21 plugins and 25 `/business/learn/` pages.

## 5. Removals

- **Today:** 13 URLs, all relocations (see Anomalies).
- **Cumulative since 2026-09-28 (29):** the 13 above, plus 16 reported by the 2026-11-10 run: 7 `/business/partners/*` pages (canva, dropbox, gusto, hubspot, pathfindr → affinda, quickbooks, stripe), 5 plugin renames or consolidations (atlassian-rovo → atlassian, litera-lito → litera, oracle-analytics → oracle-analytics-cloud, wordpress-com and mcp-server-for-wordpress → wordpress), `/daybreak/partners-new/`, `/economic-research-exchange/` (→ `/economic-research-collaborators/`), `/form/ultrafast/` and `/prism/`. The last snapshots remain in git history.

## Fetch failures

None. All 1,933 Added and Updated pages were fetched and passed the sanity check (≥100 chars, no Cloudflare challenge text).

## Needs follow-up

- **Merge the backlog of PRs, or close them.** Until `main` advances, every run re-reports the same six weeks of changes as "new".
- Re-check the 10 pages that lost their testimonial carousels.

## Appendix A — All anomalies (machine list)

- **backdated_new_url** — `/business/contact-sales-retail/` — lastmod 2026-10-22T09:35:52.893Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/images-api/` — lastmod 2026-11-06T06:29:00.578Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/automate-complex-workflows-with-openai-o3/` — lastmod 2026-10-23T00:34:42.478Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/board-guide-cybersecurity-ai/` — lastmod 2026-10-09T07:16:10.956Z is 33 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/collaborate-and-write-with-gpt-4o/` — lastmod 2026-10-23T04:35:53.989Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/connect-internal-knowledge-from-google-drive/` — lastmod 2026-10-22T22:58:48.763Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/create-on-brand-visuals-with-image-generation/` — lastmod 2026-10-23T09:21:55.298Z is 18 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/creating-a-contextual-workspace-in-chatgpt/` — lastmod 2026-10-21T16:04:20.339Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/delegate-work-to-chatgpt-agent/` — lastmod 2026-10-21T15:52:32.152Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/gpt-5-our-best-model-for-work/` — lastmod 2026-10-23T08:06:52.377Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/gpt-live-1-webinar/` — lastmod 2026-10-22T02:48:44.212Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/how-openai-uses-chatgpt-atlas-at-work/` — lastmod 2026-10-25T16:53:23.411Z is 16 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/market-research-with-chatgpt/` — lastmod 2026-10-21T17:07:06.880Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/personalize-chatgpt-with-custom-instructions/` — lastmod 2026-10-21T16:15:58.111Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/php2shell-webinar/` — lastmod 2026-11-04T23:00:35.005Z is 6 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/prototyping-with-canvas-in-chatgpt/` — lastmod 2026-10-21T15:05:27.118Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/shipping-code-to-your-ide-with-chatgpt/` — lastmod 2026-10-21T16:15:26.286Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/strategic-planning-with-chatgpt/` — lastmod 2026-10-22T22:51:04.962Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/using-codex-across-the-software-development-lifecycle/` — lastmod 2026-10-25T19:49:54.121Z is 16 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/vision-and-voice-in-chatgpt/` — lastmod 2026-10-23T00:37:50.720Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/learn/writing-with-canvas-in-chatgpt/` — lastmod 2026-10-21T13:41:25.709Z is 20 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/partners/affinda/` — lastmod 2026-10-29T05:53:37.906Z is 13 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/partners/bishop-fox/` — lastmod 2026-10-15T21:09:24.263Z is 26 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/partners/insight-enterprises/` — lastmod 2026-10-20T12:59:45.833Z is 21 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/partners/megazonecloud/` — lastmod 2026-10-29T06:08:41.362Z is 13 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/partners/specterops/` — lastmod 2026-10-15T21:09:56.433Z is 26 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/partners/trustedsec/` — lastmod 2026-10-15T21:09:24.410Z is 26 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **reappeared_url** — `/business/plugins/alpaca/` — first_seen 2026-07-10T09-16Z, last_seen 2026-09-24T09-16Z, now back
- **backdated_new_url** — `/business/plugins/atlassian-teammate-graph/` — lastmod 2026-11-01T02:47:45.082Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/atlassian/` — lastmod 2026-10-31T20:25:40.630Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/krea/` — lastmod 2026-11-01T00:21:14.837Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/litera/` — lastmod 2026-11-05T19:27:02.488Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/oracle-analytics-cloud/` — lastmod 2026-11-01T04:40:00.946Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/oracle-netsuite-ai-companion/` — lastmod 2026-11-01T00:53:54.747Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/oracle-netsuite-finance-analyst/` — lastmod 2026-11-01T03:15:13.444Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/oracle-netsuite-quickstart/` — lastmod 2026-11-05T19:23:35.915Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/oracle-netsuite-suitecloud/` — lastmod 2026-11-01T02:28:22.985Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/oracle-netsuite-suiteskills/` — lastmod 2026-11-05T19:22:40.333Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/sandstone/` — lastmod 2026-10-31T23:26:30.974Z is 10 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/plugins/servicenow/` — lastmod 2026-11-03T13:42:39.622Z is 7 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/private-intelligence/privacy-by-product/` — lastmod 2026-11-04T21:45:17.962Z is 6 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/business/solutions/legal/` — lastmod 2026-11-03T00:35:04.801Z is 8 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/codex-originals/` — lastmod 2026-10-24T03:16:35.181Z is 18 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/devday/2026/` — lastmod 2026-10-31T08:45:29.889Z is 11 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/economic-research-collaborators/` — lastmod 2026-10-30T12:34:39.411Z is 11 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **reappeared_url** — `/form/codex-ambassadors/` — first_seen 2026-05-07T09-01Z, last_seen 2026-06-24, now back
- **backdated_new_url** — `/form/codex-originals/` — lastmod 2026-11-05T11:54:21.956Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/form/computer-use-research-collaboration/` — lastmod 2026-10-19T11:11:45.835Z is 22 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/form/private-intelligence-interest/` — lastmod 2026-10-30T07:26:05.177Z is 12 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/form/sign-in-with-chatgpt-interest/` — lastmod 2026-10-30T18:51:00.428Z is 11 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/index/introducing-the-rosalind-academic-plan/` — lastmod 2026-11-05T10:12:43.505Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/index/new-chatgpt-ads-format-and-measurement/` — lastmod 2026-11-05T10:13:59.414Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/index/pollo-ai/` — lastmod 2026-11-03T21:40:31.085Z is 7 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/index/practical-guide-building-gpt-6/` — lastmod 2026-11-05T10:12:32.907Z is 5 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/index/teaching-students-to-think-and-learn-through-questions/` — lastmod 2026-10-22T09:45:56.774Z is 19 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/index/towards-safety-cases-for-frontier-ai-training/` — lastmod 2026-11-03T18:06:47.269Z is 7 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **backdated_new_url** — `/policies/brazil-advertising-terms/` — lastmod 2026-10-26T07:27:13.757Z is 16 days before first observation 2026-11-11T09:17:16Z (note: baseline is 2026-09-28T09-17Z, so a gap in merged observations inflates this)
- **reappeared_url** — `/policies/row-privacy-policy/` — first_seen 2026-05-07T09-01Z, last_seen 2026-05-27T09-17Z, now back
- **sub_sitemap_migration** — `/business/learn/intelligence-at-work-financial-services/` — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- **sub_sitemap_migration** — `/business/learn/download-the-chatgpt-work-guide-for-sales-teams/` — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-guides.xml']
- **sub_sitemap_migration** — `/business/learn/intelligence-at-work-cyber/` — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- **sub_sitemap_migration** — `/business/plugins/tableau/` — ['sitemap.xml_plugins-data-research.xml'] -> ['sitemap.xml_plugins-productivity.xml']
- **sub_sitemap_migration** — `/business/plugins/sync-labs/` — ['sitemap.xml_plugins-productivity.xml'] -> ['sitemap.xml_plugins-design-creative.xml']
- **sub_sitemap_migration** — `/business/learn/agent-security-enterprise/` — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-guides.xml']
- **sub_sitemap_migration** — `/business/plugins/parallel-search/` — ['sitemap.xml_plugins-engineering-it.xml'] -> ['sitemap.xml_plugins-productivity.xml']
- **sub_sitemap_migration** — `/business/learn/how-our-finance-team-uses-chatgpt-work/` — ['sitemap.xml_learn-guides.xml'] -> ['sitemap.xml_learn-webinars.xml']
- **sub_sitemap_migration** — `/business/learn/how-our-sales-team-uses-chatgpt-work/` — ['sitemap.xml_page.xml'] -> ['sitemap.xml_learn-webinars.xml']
- **new_sub_sitemap** — `sitemap.xml_learn-demos.xml` — sub-sitemap not present in baseline
- **lastmod_backwards** — `/index/retell-ai/` — vs prior (unmerged) 2026-11-10T09-16Z snapshot: 2026-11-09T22:47:55.896Z -> 2026-10-30T02:55:47.970Z; rendered content identical to 2026-11-10 snapshot. Not backwards vs merged baseline 2026-09-28.
- **url_relocation** — `/business/customer-stories/ada/` — replaces https://openai.com/index/ada/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/customer-stories/blue-j/` — replaces https://openai.com/index/blue-j/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/learn/enabling-a-data-driven-workforce-webinar/` — replaces https://openai.com/business/enabling-a-data-driven-workforce-webinar/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/learn/fine-tuning-gpt-4o-webinar/` — replaces https://openai.com/business/fine-tuning-gpt-4o-webinar/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/learn/how-openai-uses-codex/` — replaces https://openai.com/business/guides-and-resources/how-openai-uses-codex/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/learn/identifying-and-scaling-ai-use-cases/` — replaces https://openai.com/business/guides-and-resources/identifying-and-scaling-ai-use-cases/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/learn/new-in-chatgpt-for-business-april-updates-2025/` — replaces https://openai.com/business/new-in-chatgpt-for-business-april-updates-2025/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/learn/new-in-chatgpt-for-work-march-updates-2025/` — replaces https://openai.com/business/new-in-chatgpt-for-work-march-updates-2025/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/solutions/knowledge-retrieval/` — replaces https://openai.com/solutions/blueprints/knowledge-retrieval/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/solutions/financial-services/` — replaces https://openai.com/solutions/industries/financial-services/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/solutions/retail/` — replaces https://openai.com/solutions/industries/retail/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/solutions/content-creation/` — replaces https://openai.com/solutions/use-case/content-creation/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)
- **url_relocation** — `/business/solutions/data-analysis/` — replaces https://openai.com/solutions/use-case/data-analysis/ (removed same day, since 2026-11-10 snapshot); same page relocated to a new URL (likely a site-structure consolidation)

## Appendix B — All added URLs vs merged baseline (214)

- [`/ads/customers/evernote/`](../../pages/openai.com/ads/customers/evernote/index.md)
- [`/ads/customers/flipsnack/`](../../pages/openai.com/ads/customers/flipsnack/index.md)
- [`/ads/customers/vistaprint/`](../../pages/openai.com/ads/customers/vistaprint/index.md)
- [`/business/businesses-in-chatgpt/`](../../pages/openai.com/business/businesses-in-chatgpt/index.md)
- [`/business/contact-sales-retail/`](../../pages/openai.com/business/contact-sales-retail/index.md)
- [`/business/customer-stories/ada/`](../../pages/openai.com/business/customer-stories/ada/index.md)
- [`/business/customer-stories/blue-j/`](../../pages/openai.com/business/customer-stories/blue-j/index.md)
- [`/business/forward-deployed-engineering/`](../../pages/openai.com/business/forward-deployed-engineering/index.md)
- [`/business/images-api/`](../../pages/openai.com/business/images-api/index.md)
- [`/business/learn/automate-complex-workflows-with-openai-o3/`](../../pages/openai.com/business/learn/automate-complex-workflows-with-openai-o3/index.md)
- [`/business/learn/board-guide-cybersecurity-ai/`](../../pages/openai.com/business/learn/board-guide-cybersecurity-ai/index.md)
- [`/business/learn/collaborate-and-write-with-gpt-4o/`](../../pages/openai.com/business/learn/collaborate-and-write-with-gpt-4o/index.md)
- [`/business/learn/connect-internal-knowledge-from-google-drive/`](../../pages/openai.com/business/learn/connect-internal-knowledge-from-google-drive/index.md)
- [`/business/learn/create-on-brand-visuals-with-image-generation/`](../../pages/openai.com/business/learn/create-on-brand-visuals-with-image-generation/index.md)
- [`/business/learn/creating-a-contextual-workspace-in-chatgpt/`](../../pages/openai.com/business/learn/creating-a-contextual-workspace-in-chatgpt/index.md)
- [`/business/learn/delegate-work-to-chatgpt-agent/`](../../pages/openai.com/business/learn/delegate-work-to-chatgpt-agent/index.md)
- [`/business/learn/enabling-a-data-driven-workforce-webinar/`](../../pages/openai.com/business/learn/enabling-a-data-driven-workforce-webinar/index.md)
- [`/business/learn/fine-tuning-gpt-4o-webinar/`](../../pages/openai.com/business/learn/fine-tuning-gpt-4o-webinar/index.md)
- [`/business/learn/gpt-5-our-best-model-for-work/`](../../pages/openai.com/business/learn/gpt-5-our-best-model-for-work/index.md)
- [`/business/learn/gpt-live-1-webinar/`](../../pages/openai.com/business/learn/gpt-live-1-webinar/index.md)
- [`/business/learn/how-openai-uses-chatgpt-atlas-at-work/`](../../pages/openai.com/business/learn/how-openai-uses-chatgpt-atlas-at-work/index.md)
- [`/business/learn/how-openai-uses-codex/`](../../pages/openai.com/business/learn/how-openai-uses-codex/index.md)
- [`/business/learn/identifying-and-scaling-ai-use-cases/`](../../pages/openai.com/business/learn/identifying-and-scaling-ai-use-cases/index.md)
- [`/business/learn/market-research-with-chatgpt/`](../../pages/openai.com/business/learn/market-research-with-chatgpt/index.md)
- [`/business/learn/new-in-chatgpt-for-business-april-updates-2025/`](../../pages/openai.com/business/learn/new-in-chatgpt-for-business-april-updates-2025/index.md)
- [`/business/learn/new-in-chatgpt-for-work-march-updates-2025/`](../../pages/openai.com/business/learn/new-in-chatgpt-for-work-march-updates-2025/index.md)
- [`/business/learn/personalize-chatgpt-with-custom-instructions/`](../../pages/openai.com/business/learn/personalize-chatgpt-with-custom-instructions/index.md)
- [`/business/learn/php2shell-webinar/`](../../pages/openai.com/business/learn/php2shell-webinar/index.md)
- [`/business/learn/prototyping-with-canvas-in-chatgpt/`](../../pages/openai.com/business/learn/prototyping-with-canvas-in-chatgpt/index.md)
- [`/business/learn/shipping-code-to-your-ide-with-chatgpt/`](../../pages/openai.com/business/learn/shipping-code-to-your-ide-with-chatgpt/index.md)
- [`/business/learn/strategic-planning-with-chatgpt/`](../../pages/openai.com/business/learn/strategic-planning-with-chatgpt/index.md)
- [`/business/learn/using-codex-across-the-software-development-lifecycle/`](../../pages/openai.com/business/learn/using-codex-across-the-software-development-lifecycle/index.md)
- [`/business/learn/vision-and-voice-in-chatgpt/`](../../pages/openai.com/business/learn/vision-and-voice-in-chatgpt/index.md)
- [`/business/learn/writing-with-canvas-in-chatgpt/`](../../pages/openai.com/business/learn/writing-with-canvas-in-chatgpt/index.md)
- [`/business/marketplace/`](../../pages/openai.com/business/marketplace/index.md)
- [`/business/partners/affinda/`](../../pages/openai.com/business/partners/affinda/index.md)
- [`/business/partners/bishop-fox/`](../../pages/openai.com/business/partners/bishop-fox/index.md)
- [`/business/partners/insight-enterprises/`](../../pages/openai.com/business/partners/insight-enterprises/index.md)
- [`/business/partners/megazonecloud/`](../../pages/openai.com/business/partners/megazonecloud/index.md)
- [`/business/partners/specterops/`](../../pages/openai.com/business/partners/specterops/index.md)
- [`/business/partners/trustedsec/`](../../pages/openai.com/business/partners/trustedsec/index.md)
- [`/business/plugins/aiva/`](../../pages/openai.com/business/plugins/aiva/index.md)
- [`/business/plugins/alpaca/`](../../pages/openai.com/business/plugins/alpaca/index.md)
- [`/business/plugins/atlassian-teammate-graph/`](../../pages/openai.com/business/plugins/atlassian-teammate-graph/index.md)
- [`/business/plugins/atlassian/`](../../pages/openai.com/business/plugins/atlassian/index.md)
- [`/business/plugins/krea/`](../../pages/openai.com/business/plugins/krea/index.md)
- [`/business/plugins/litera/`](../../pages/openai.com/business/plugins/litera/index.md)
- [`/business/plugins/luma-health/`](../../pages/openai.com/business/plugins/luma-health/index.md)
- [`/business/plugins/oracle-analytics-cloud/`](../../pages/openai.com/business/plugins/oracle-analytics-cloud/index.md)
- [`/business/plugins/oracle-netsuite-ai-companion/`](../../pages/openai.com/business/plugins/oracle-netsuite-ai-companion/index.md)
- [`/business/plugins/oracle-netsuite-finance-analyst/`](../../pages/openai.com/business/plugins/oracle-netsuite-finance-analyst/index.md)
- [`/business/plugins/oracle-netsuite-quickstart/`](../../pages/openai.com/business/plugins/oracle-netsuite-quickstart/index.md)
- [`/business/plugins/oracle-netsuite-suitecloud/`](../../pages/openai.com/business/plugins/oracle-netsuite-suitecloud/index.md)
- [`/business/plugins/oracle-netsuite-suiteskills/`](../../pages/openai.com/business/plugins/oracle-netsuite-suiteskills/index.md)
- [`/business/plugins/sandstone/`](../../pages/openai.com/business/plugins/sandstone/index.md)
- [`/business/plugins/servicenow/`](../../pages/openai.com/business/plugins/servicenow/index.md)
- [`/business/plugins/spacefast/`](../../pages/openai.com/business/plugins/spacefast/index.md)
- [`/business/plugins/stedi/`](../../pages/openai.com/business/plugins/stedi/index.md)
- [`/business/plugins/subsalt/`](../../pages/openai.com/business/plugins/subsalt/index.md)
- [`/business/plugins/turquoise-health/`](../../pages/openai.com/business/plugins/turquoise-health/index.md)
- [`/business/plugins/uptodate-expert-ai/`](../../pages/openai.com/business/plugins/uptodate-expert-ai/index.md)
- [`/business/plugins/wordpress/`](../../pages/openai.com/business/plugins/wordpress/index.md)
- [`/business/private-intelligence/`](../../pages/openai.com/business/private-intelligence/index.md)
- [`/business/private-intelligence/privacy-by-product/`](../../pages/openai.com/business/private-intelligence/privacy-by-product/index.md)
- [`/business/solutions/content-creation/`](../../pages/openai.com/business/solutions/content-creation/index.md)
- [`/business/solutions/data-analysis/`](../../pages/openai.com/business/solutions/data-analysis/index.md)
- [`/business/solutions/financial-services/`](../../pages/openai.com/business/solutions/financial-services/index.md)
- [`/business/solutions/knowledge-retrieval/`](../../pages/openai.com/business/solutions/knowledge-retrieval/index.md)
- [`/business/solutions/legal/`](../../pages/openai.com/business/solutions/legal/index.md)
- [`/business/solutions/retail/`](../../pages/openai.com/business/solutions/retail/index.md)
- [`/codex-originals/`](../../pages/openai.com/codex-originals/index.md)
- [`/compute-campus/`](../../pages/openai.com/compute-campus/index.md)
- [`/cyber-at-the-frontier/`](../../pages/openai.com/cyber-at-the-frontier/index.md)
- [`/cybersecurity/`](../../pages/openai.com/cybersecurity/index.md)
- [`/devday/2026/`](../../pages/openai.com/devday/2026/index.md)
- [`/economic-research-collaborators/`](../../pages/openai.com/economic-research-collaborators/index.md)
- [`/form/codex-ambassadors/`](../../pages/openai.com/form/codex-ambassadors/index.md)
- [`/form/codex-originals/`](../../pages/openai.com/form/codex-originals/index.md)
- [`/form/computer-use-research-collaboration/`](../../pages/openai.com/form/computer-use-research-collaboration/index.md)
- [`/form/openai-on-google-cloud/`](../../pages/openai.com/form/openai-on-google-cloud/index.md)
- [`/form/private-intelligence-interest/`](../../pages/openai.com/form/private-intelligence-interest/index.md)
- [`/form/sign-in-with-chatgpt-interest/`](../../pages/openai.com/form/sign-in-with-chatgpt-interest/index.md)
- [`/index/a-thousand-fewer-paths-to-root/`](../../pages/openai.com/index/a-thousand-fewer-paths-to-root/index.md)
- [`/index/accelerating-engineering-for-the-physical-world/`](../../pages/openai.com/index/accelerating-engineering-for-the-physical-world/index.md)
- [`/index/advancing-computer-use-with-ironclad/`](../../pages/openai.com/index/advancing-computer-use-with-ironclad/index.md)
- [`/index/ai-effect-on-freelance-work/`](../../pages/openai.com/index/ai-effect-on-freelance-work/index.md)
- [`/index/albertsons-reimagining-retail/`](../../pages/openai.com/index/albertsons-reimagining-retail/index.md)
- [`/index/amp-beyond-coding/`](../../pages/openai.com/index/amp-beyond-coding/index.md)
- [`/index/anima/`](../../pages/openai.com/index/anima/index.md)
- [`/index/asana-browser-agent/`](../../pages/openai.com/index/asana-browser-agent/index.md)
- [`/index/atlassian-partnership/`](../../pages/openai.com/index/atlassian-partnership/index.md)
- [`/index/att-legal/`](../../pages/openai.com/index/att-legal/index.md)
- [`/index/australian-universities-ai-native-graduates/`](../../pages/openai.com/index/australian-universities-ai-native-graduates/index.md)
- [`/index/basis-tax-workbook-with-astra/`](../../pages/openai.com/index/basis-tax-workbook-with-astra/index.md)
- [`/index/benefit-street-partners/`](../../pages/openai.com/index/benefit-street-partners/index.md)
- [`/index/block-ai-powered-security/`](../../pages/openai.com/index/block-ai-powered-security/index.md)
- [`/index/broad-access-through-consistent-standards/`](../../pages/openai.com/index/broad-access-through-consistent-standards/index.md)
- [`/index/building-chatgpt-ad-stack/`](../../pages/openai.com/index/building-chatgpt-ad-stack/index.md)
- [`/index/building-scientific-understanding-with-academic-communities/`](../../pages/openai.com/index/building-scientific-understanding-with-academic-communities/index.md)
- [`/index/chatgpt-ads-expands-26-new-countries/`](../../pages/openai.com/index/chatgpt-ads-expands-26-new-countries/index.md)
- [`/index/chatgpt-enterprise-aws-marketplace/`](../../pages/openai.com/index/chatgpt-enterprise-aws-marketplace/index.md)
- [`/index/chatgpt-expanding-world-of-work/`](../../pages/openai.com/index/chatgpt-expanding-world-of-work/index.md)
- [`/index/chatgpt-plus-for-veterans/`](../../pages/openai.com/index/chatgpt-plus-for-veterans/index.md)
- [`/index/chatham-financial/`](../../pages/openai.com/index/chatham-financial/index.md)
- [`/index/check-point-daybreak/`](../../pages/openai.com/index/check-point-daybreak/index.md)
- [`/index/cisco-cyber/`](../../pages/openai.com/index/cisco-cyber/index.md)
- [`/index/closing-ai-guidance-gap-education/`](../../pages/openai.com/index/closing-ai-guidance-gap-education/index.md)
- [`/index/cloudflare-cyber/`](../../pages/openai.com/index/cloudflare-cyber/index.md)
- [`/index/coderabbit-codex-daybreak/`](../../pages/openai.com/index/coderabbit-codex-daybreak/index.md)
- [`/index/cogent-security/`](../../pages/openai.com/index/cogent-security/index.md)
- [`/index/community-safety-report-and-new-protections-for-teens/`](../../pages/openai.com/index/community-safety-report-and-new-protections-for-teens/index.md)
- [`/index/control-room/`](../../pages/openai.com/index/control-room/index.md)
- [`/index/coordinated-disclosure-of-critical-vulnerabilities/`](../../pages/openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/index.md)
- [`/index/credit-saison/`](../../pages/openai.com/index/credit-saison/index.md)
- [`/index/cultfit-builds-with-codex/`](../../pages/openai.com/index/cultfit-builds-with-codex/index.md)
- [`/index/dan-driscoll-joins-openai/`](../../pages/openai.com/index/dan-driscoll-joins-openai/index.md)
- [`/index/daybreak-red-aws-govcloud/`](../../pages/openai.com/index/daybreak-red-aws-govcloud/index.md)
- [`/index/decisions-api/`](../../pages/openai.com/index/decisions-api/index.md)
- [`/index/devday-2026-recap/`](../../pages/openai.com/index/devday-2026-recap/index.md)
- [`/index/devrev-enterprise-self-service/`](../../pages/openai.com/index/devrev-enterprise-self-service/index.md)
- [`/index/disrupting-a-coordinated-model-distillation-campaign/`](../../pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md)
- [`/index/disrupting-ai-enabled-false-front-operations/`](../../pages/openai.com/index/disrupting-ai-enabled-false-front-operations/index.md)
- [`/index/empowering-cyber-defenders/`](../../pages/openai.com/index/empowering-cyber-defenders/index.md)
- [`/index/eu-text-provenance/`](../../pages/openai.com/index/eu-text-provenance/index.md)
- [`/index/fair-use-benefits-everyone/`](../../pages/openai.com/index/fair-use-benefits-everyone/index.md)
- [`/index/fanatics-streamline-fan-experience/`](../../pages/openai.com/index/fanatics-streamline-fan-experience/index.md)
- [`/index/forward-deployed-engineering-means/`](../../pages/openai.com/index/forward-deployed-engineering-means/index.md)
- [`/index/franklin-templeton/`](../../pages/openai.com/index/franklin-templeton/index.md)
- [`/index/gilbert-tobin-sam-nickless/`](../../pages/openai.com/index/gilbert-tobin-sam-nickless/index.md)
- [`/index/gpt-6-1-sol-coderabbit-code-security/`](../../pages/openai.com/index/gpt-6-1-sol-coderabbit-code-security/index.md)
- [`/index/gpt-6-for-everyone/`](../../pages/openai.com/index/gpt-6-for-everyone/index.md)
- [`/index/greptile-code-review-codex-astra/`](../../pages/openai.com/index/greptile-code-review-codex-astra/index.md)
- [`/index/grid-protectors-program/`](../../pages/openai.com/index/grid-protectors-program/index.md)
- [`/index/grupo-boticario/`](../../pages/openai.com/index/grupo-boticario/index.md)
- [`/index/heimstaden/`](../../pages/openai.com/index/heimstaden/index.md)
- [`/index/helping-caregivers-use-ai-in-everyday-life/`](../../pages/openai.com/index/helping-caregivers-use-ai-in-everyday-life/index.md)
- [`/index/helping-small-businesses-put-ai-to-work/`](../../pages/openai.com/index/helping-small-businesses-put-ai-to-work/index.md)
- [`/index/helping-websites-express-ai-training-preferences/`](../../pages/openai.com/index/helping-websites-express-ai-training-preferences/index.md)
- [`/index/higgsfield-longer-videos-voice/`](../../pages/openai.com/index/higgsfield-longer-videos-voice/index.md)
- [`/index/how-we-detect-frontier-model-misalignment/`](../../pages/openai.com/index/how-we-detect-frontier-model-misalignment/index.md)
- [`/index/how-we-will-do-better-for-australia/`](../../pages/openai.com/index/how-we-will-do-better-for-australia/index.md)
- [`/index/introducing-businesses-chatgpt/`](../../pages/openai.com/index/introducing-businesses-chatgpt/index.md)
- [`/index/introducing-dots/`](../../pages/openai.com/index/introducing-dots/index.md)
- [`/index/introducing-gpt-6-1-sol/`](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md)
- [`/index/introducing-gpt-6-1-terra/`](../../pages/openai.com/index/introducing-gpt-6-1-terra/index.md)
- [`/index/introducing-gpt-6-cyber/`](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md)
- [`/index/introducing-images-2-6/`](../../pages/openai.com/index/introducing-images-2-6/index.md)
- [`/index/introducing-the-rosalind-academic-plan/`](../../pages/openai.com/index/introducing-the-rosalind-academic-plan/index.md)
- [`/index/itau-generative-ai/`](../../pages/openai.com/index/itau-generative-ai/index.md)
- [`/index/jill-hazelbaker-chief-corporate-affairs-officer/`](../../pages/openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer/index.md)
- [`/index/jump-trading/`](../../pages/openai.com/index/jump-trading/index.md)
- [`/index/kuken/`](../../pages/openai.com/index/kuken/index.md)
- [`/index/legalon-halves-codex-costs/`](../../pages/openai.com/index/legalon-halves-codex-costs/index.md)
- [`/index/legora/`](../../pages/openai.com/index/legora/index.md)
- [`/index/lenfest-ai-collaborative-expansion/`](../../pages/openai.com/index/lenfest-ai-collaborative-expansion/index.md)
- [`/index/lifeval/`](../../pages/openai.com/index/lifeval/index.md)
- [`/index/localiza-generative-ai/`](../../pages/openai.com/index/localiza-generative-ai/index.md)
- [`/index/low-resource-programming-languages/`](../../pages/openai.com/index/low-resource-programming-languages/index.md)
- [`/index/measuring-how-ai-agents-handle-wet-lab-science/`](../../pages/openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/index.md)
- [`/index/merge-builds-with-openai/`](../../pages/openai.com/index/merge-builds-with-openai/index.md)
- [`/index/new-chatgpt-ads-format-and-measurement/`](../../pages/openai.com/index/new-chatgpt-ads-format-and-measurement/index.md)
- [`/index/openai-cut-incident-investigation/`](../../pages/openai.com/index/openai-cut-incident-investigation/index.md)
- [`/index/openai-models-google-cloud/`](../../pages/openai.com/index/openai-models-google-cloud/index.md)
- [`/index/openai-nask-ai-safety-security-partnership/`](../../pages/openai.com/index/openai-nask-ai-safety-security-partnership/index.md)
- [`/index/openai-servicenow-partnership-expansion/`](../../pages/openai.com/index/openai-servicenow-partnership-expansion/index.md)
- [`/index/openai-to-acquire-orchestra-bio/`](../../pages/openai.com/index/openai-to-acquire-orchestra-bio/index.md)
- [`/index/openai-to-acquire-pierre/`](../../pages/openai.com/index/openai-to-acquire-pierre/index.md)
- [`/index/oracle-apps-in-chatgpt/`](../../pages/openai.com/index/oracle-apps-in-chatgpt/index.md)
- [`/index/oracle/`](../../pages/openai.com/index/oracle/index.md)
- [`/index/partnering-with-hacktron/`](../../pages/openai.com/index/partnering-with-hacktron/index.md)
- [`/index/pollo-ai/`](../../pages/openai.com/index/pollo-ai/index.md)
- [`/index/practical-guide-building-gpt-6/`](../../pages/openai.com/index/practical-guide-building-gpt-6/index.md)
- [`/index/preparing-our-next-security-sprint-to-harden-openai/`](../../pages/openai.com/index/preparing-our-next-security-sprint-to-harden-openai/index.md)
- [`/index/qodo-codex-plugin/`](../../pages/openai.com/index/qodo-codex-plugin/index.md)
- [`/index/radisson/`](../../pages/openai.com/index/radisson/index.md)
- [`/index/rewarding-defenders-with-bigger-bug-bounties/`](../../pages/openai.com/index/rewarding-defenders-with-bigger-bug-bounties/index.md)
- [`/index/ropes-gray-ai-diligence/`](../../pages/openai.com/index/ropes-gray-ai-diligence/index.md)
- [`/index/scaling-ai-research-for-complex-biological-data/`](../../pages/openai.com/index/scaling-ai-research-for-complex-biological-data/index.md)
- [`/index/scaling-git-at-openai/`](../../pages/openai.com/index/scaling-git-at-openai/index.md)
- [`/index/scaling-storage-one-billion-users-part-two/`](../../pages/openai.com/index/scaling-storage-one-billion-users-part-two/index.md)
- [`/index/securing-our-frontier-model-training-environment/`](../../pages/openai.com/index/securing-our-frontier-model-training-environment/index.md)
- [`/index/sentinelone/`](../../pages/openai.com/index/sentinelone/index.md)
- [`/index/setting-new-standard-responsible-ai-infrastructure/`](../../pages/openai.com/index/setting-new-standard-responsible-ai-infrastructure/index.md)
- [`/index/sharing-ai-progress-in-mathematics/`](../../pages/openai.com/index/sharing-ai-progress-in-mathematics/index.md)
- [`/index/singapore-airlines-travel-work/`](../../pages/openai.com/index/singapore-airlines-travel-work/index.md)
- [`/index/sophos/`](../../pages/openai.com/index/sophos/index.md)
- [`/index/stack-overflow-chatgpt-plugin/`](../../pages/openai.com/index/stack-overflow-chatgpt-plugin/index.md)
- [`/index/sullivan-cromwell/`](../../pages/openai.com/index/sullivan-cromwell/index.md)
- [`/index/teaching-students-to-think-and-learn-through-questions/`](../../pages/openai.com/index/teaching-students-to-think-and-learn-through-questions/index.md)
- [`/index/ted-taylor-restaurant/`](../../pages/openai.com/index/ted-taylor-restaurant/index.md)
- [`/index/teens-learn-and-plan/`](../../pages/openai.com/index/teens-learn-and-plan/index.md)
- [`/index/terminal-x/`](../../pages/openai.com/index/terminal-x/index.md)
- [`/index/the-den-family-social/`](../../pages/openai.com/index/the-den-family-social/index.md)
- [`/index/the-eternal-complement/`](../../pages/openai.com/index/the-eternal-complement/index.md)
- [`/index/the-eus-next-chapter-in-ai-is-agentic/`](../../pages/openai.com/index/the-eus-next-chapter-in-ai-is-agentic/index.md)
- [`/index/the-future-of-the-firm/`](../../pages/openai.com/index/the-future-of-the-firm/index.md)
- [`/index/third-moment-research/`](../../pages/openai.com/index/third-moment-research/index.md)
- [`/index/towards-safety-cases-for-frontier-ai-training/`](../../pages/openai.com/index/towards-safety-cases-for-frontier-ai-training/index.md)
- [`/index/uber-chatgpt-work-rollout/`](../../pages/openai.com/index/uber-chatgpt-work-rollout/index.md)
- [`/index/updated-model-spec/`](../../pages/openai.com/index/updated-model-spec/index.md)
- [`/policies/brazil-advertising-terms/`](../../pages/openai.com/policies/brazil-advertising-terms/index.md)
- [`/policies/business-agents-policy/`](../../pages/openai.com/policies/business-agents-policy/index.md)
- [`/policies/businesses-in-chatgpt-terms/`](../../pages/openai.com/policies/businesses-in-chatgpt-terms/index.md)
- [`/policies/businesses-in-chatgpt/`](../../pages/openai.com/policies/businesses-in-chatgpt/index.md)
- [`/policies/marketplace-customer-program-terms/`](../../pages/openai.com/policies/marketplace-customer-program-terms/index.md)
- [`/policies/row-privacy-policy/`](../../pages/openai.com/policies/row-privacy-policy/index.md)
- [`/policies/sign-in-with-chatgpt-terms/`](../../pages/openai.com/policies/sign-in-with-chatgpt-terms/index.md)
- [`/supply/product/blossom-tee-gray/`](../../pages/openai.com/supply/product/blossom-tee-gray/index.md)
- [`/supply/product/dots-tee/`](../../pages/openai.com/supply/product/dots-tee/index.md)
- [`/supply/product/dots-tote/`](../../pages/openai.com/supply/product/dots-tote/index.md)
- [`/supply/product/gpt-6-longsleeve/`](../../pages/openai.com/supply/product/gpt-6-longsleeve/index.md)
- [`/supply/product/modretro-chromatic-case-codex-edition/`](../../pages/openai.com/supply/product/modretro-chromatic-case-codex-edition/index.md)
- [`/supply/product/modretro-codex-cartridge/`](../../pages/openai.com/supply/product/modretro-codex-cartridge/index.md)
- [`/supply/product/theresetcompany-hoodie/`](../../pages/openai.com/supply/product/theresetcompany-hoodie/index.md)

## Appendix C — Removed URLs vs merged baseline (29)

- `/business/enabling-a-data-driven-workforce-webinar/` — last snapshot: `git log -- pages/openai.com/business/enabling-a-data-driven-workforce-webinar/index.md`
- `/business/fine-tuning-gpt-4o-webinar/` — last snapshot: `git log -- pages/openai.com/business/fine-tuning-gpt-4o-webinar/index.md`
- `/business/guides-and-resources/how-openai-uses-codex/` — last snapshot: `git log -- pages/openai.com/business/guides-and-resources/how-openai-uses-codex/index.md`
- `/business/guides-and-resources/identifying-and-scaling-ai-use-cases/` — last snapshot: `git log -- pages/openai.com/business/guides-and-resources/identifying-and-scaling-ai-use-cases/index.md`
- `/business/new-in-chatgpt-for-business-april-updates-2025/` — last snapshot: `git log -- pages/openai.com/business/new-in-chatgpt-for-business-april-updates-2025/index.md`
- `/business/new-in-chatgpt-for-work-march-updates-2025/` — last snapshot: `git log -- pages/openai.com/business/new-in-chatgpt-for-work-march-updates-2025/index.md`
- `/business/partners/canva/` — last snapshot: `git log -- pages/openai.com/business/partners/canva/index.md`
- `/business/partners/dropbox/` — last snapshot: `git log -- pages/openai.com/business/partners/dropbox/index.md`
- `/business/partners/gusto/` — last snapshot: `git log -- pages/openai.com/business/partners/gusto/index.md`
- `/business/partners/hubspot/` — last snapshot: `git log -- pages/openai.com/business/partners/hubspot/index.md`
- `/business/partners/pathfindr/` — last snapshot: `git log -- pages/openai.com/business/partners/pathfindr/index.md`
- `/business/partners/quickbooks/` — last snapshot: `git log -- pages/openai.com/business/partners/quickbooks/index.md`
- `/business/partners/stripe/` — last snapshot: `git log -- pages/openai.com/business/partners/stripe/index.md`
- `/business/plugins/atlassian-rovo/` — last snapshot: `git log -- pages/openai.com/business/plugins/atlassian-rovo/index.md`
- `/business/plugins/litera-lito/` — last snapshot: `git log -- pages/openai.com/business/plugins/litera-lito/index.md`
- `/business/plugins/mcp-server-for-wordpress/` — last snapshot: `git log -- pages/openai.com/business/plugins/mcp-server-for-wordpress/index.md`
- `/business/plugins/oracle-analytics/` — last snapshot: `git log -- pages/openai.com/business/plugins/oracle-analytics/index.md`
- `/business/plugins/wordpress-com/` — last snapshot: `git log -- pages/openai.com/business/plugins/wordpress-com/index.md`
- `/daybreak/partners-new/` — last snapshot: `git log -- pages/openai.com/daybreak/partners-new/index.md`
- `/economic-research-exchange/` — last snapshot: `git log -- pages/openai.com/economic-research-exchange/index.md`
- `/form/ultrafast/` — last snapshot: `git log -- pages/openai.com/form/ultrafast/index.md`
- `/index/ada/` — last snapshot: `git log -- pages/openai.com/index/ada/index.md`
- `/index/blue-j/` — last snapshot: `git log -- pages/openai.com/index/blue-j/index.md`
- `/prism/` — last snapshot: `git log -- pages/openai.com/prism/index.md`
- `/solutions/blueprints/knowledge-retrieval/` — last snapshot: `git log -- pages/openai.com/solutions/blueprints/knowledge-retrieval/index.md`
- `/solutions/industries/financial-services/` — last snapshot: `git log -- pages/openai.com/solutions/industries/financial-services/index.md`
- `/solutions/industries/retail/` — last snapshot: `git log -- pages/openai.com/solutions/industries/retail/index.md`
- `/solutions/use-case/content-creation/` — last snapshot: `git log -- pages/openai.com/solutions/use-case/content-creation/index.md`
- `/solutions/use-case/data-analysis/` — last snapshot: `git log -- pages/openai.com/solutions/use-case/data-analysis/index.md`

## Appendix D — Today-only (since 2026-11-10 snapshot) updated pages with real rendered changes

- [`/`](../../pages/openai.com/index.md) (−7/+7 lines)
- [`/business/`](../../pages/openai.com/business/index.md) (−0/+3 lines)
- [`/business/plugins/alpaca/`](../../pages/openai.com/business/plugins/alpaca/index.md) (−3/+3 lines)
- [`/business/plugins/brevo/`](../../pages/openai.com/business/plugins/brevo/index.md) (−4/+4 lines)
- [`/business/plugins/chatgpt-ads-manager/`](../../pages/openai.com/business/plugins/chatgpt-ads-manager/index.md) (−4/+4 lines)
- [`/business/plugins/clio/`](../../pages/openai.com/business/plugins/clio/index.md) (−1/+1 lines)
- [`/business/plugins/coinmarketcap/`](../../pages/openai.com/business/plugins/coinmarketcap/index.md) (−4/+4 lines)
- [`/business/plugins/data/`](../../pages/openai.com/business/plugins/data/index.md) (−1/+1 lines)
- [`/business/plugins/dbt/`](../../pages/openai.com/business/plugins/dbt/index.md) (−3/+3 lines)
- [`/business/plugins/fathom/`](../../pages/openai.com/business/plugins/fathom/index.md) (−3/+3 lines)
- [`/business/plugins/figma/`](../../pages/openai.com/business/plugins/figma/index.md) (−5/+5 lines)
- [`/business/plugins/firebase/`](../../pages/openai.com/business/plugins/firebase/index.md) (−4/+4 lines)
- [`/business/plugins/firecrawl/`](../../pages/openai.com/business/plugins/firecrawl/index.md) (−5/+5 lines)
- [`/business/plugins/g2/`](../../pages/openai.com/business/plugins/g2/index.md) (−3/+3 lines)
- [`/business/plugins/gsc-wizard/`](../../pages/openai.com/business/plugins/gsc-wizard/index.md) (−3/+3 lines)
- [`/business/plugins/hex/`](../../pages/openai.com/business/plugins/hex/index.md) (−7/+4 lines)
- [`/business/plugins/heygen/`](../../pages/openai.com/business/plugins/heygen/index.md) (−6/+6 lines)
- [`/business/plugins/highlevel/`](../../pages/openai.com/business/plugins/highlevel/index.md) (−11/+15 lines)
- [`/business/plugins/hypd-ai/`](../../pages/openai.com/business/plugins/hypd-ai/index.md) (−3/+3 lines)
- [`/business/plugins/jam-dev/`](../../pages/openai.com/business/plugins/jam-dev/index.md) (−5/+13 lines)
- [`/business/plugins/klaviyo/`](../../pages/openai.com/business/plugins/klaviyo/index.md) (−6/+5 lines)
- [`/business/plugins/kling-ai/`](../../pages/openai.com/business/plugins/kling-ai/index.md) (−3/+3 lines)
- [`/business/plugins/lusha/`](../../pages/openai.com/business/plugins/lusha/index.md) (−5/+8 lines)
- [`/business/plugins/microsoft-azure-cosmosdb/`](../../pages/openai.com/business/plugins/microsoft-azure-cosmosdb/index.md) (−4/+4 lines)
- [`/business/plugins/midpage/`](../../pages/openai.com/business/plugins/midpage/index.md) (−8/+8 lines)
- [`/business/plugins/monday-com/`](../../pages/openai.com/business/plugins/monday-com/index.md) (−3/+3 lines)
- [`/business/plugins/mongodb/`](../../pages/openai.com/business/plugins/mongodb/index.md) (−4/+4 lines)
- [`/business/plugins/neon/`](../../pages/openai.com/business/plugins/neon/index.md) (−6/+5 lines)
- [`/business/plugins/notion/`](../../pages/openai.com/business/plugins/notion/index.md) (−8/+7 lines)
- [`/business/plugins/omni/`](../../pages/openai.com/business/plugins/omni/index.md) (−4/+4 lines)
- [`/business/plugins/openai-developers/`](../../pages/openai.com/business/plugins/openai-developers/index.md) (−4/+5 lines)
- [`/business/plugins/openart/`](../../pages/openai.com/business/plugins/openart/index.md) (−5/+7 lines)
- [`/business/plugins/parallel-search/`](../../pages/openai.com/business/plugins/parallel-search/index.md) (−10/+16 lines)
- [`/business/plugins/picsart/`](../../pages/openai.com/business/plugins/picsart/index.md) (−8/+7 lines)
- [`/business/plugins/quickbooks/`](../../pages/openai.com/business/plugins/quickbooks/index.md) (−4/+4 lines)
- [`/business/plugins/redis/`](../../pages/openai.com/business/plugins/redis/index.md) (−4/+4 lines)
- [`/business/plugins/scholar-gateway/`](../../pages/openai.com/business/plugins/scholar-gateway/index.md) (−3/+3 lines)
- [`/business/plugins/sider-scholar/`](../../pages/openai.com/business/plugins/sider-scholar/index.md) (−4/+4 lines)
- [`/business/plugins/spacefast/`](../../pages/openai.com/business/plugins/spacefast/index.md) (−6/+5 lines)
- [`/business/plugins/supermetrics/`](../../pages/openai.com/business/plugins/supermetrics/index.md) (−17/+17 lines)
- [`/business/plugins/sync-labs/`](../../pages/openai.com/business/plugins/sync-labs/index.md) (−5/+8 lines)
- [`/business/plugins/tavily-ai/`](../../pages/openai.com/business/plugins/tavily-ai/index.md) (−12/+13 lines)
- [`/business/plugins/tldv/`](../../pages/openai.com/business/plugins/tldv/index.md) (−3/+3 lines)
- [`/business/plugins/trellis-law/`](../../pages/openai.com/business/plugins/trellis-law/index.md) (−5/+8 lines)
- [`/business/plugins/villagesql/`](../../pages/openai.com/business/plugins/villagesql/index.md) (−4/+4 lines)
- [`/business/plugins/windsor-ai/`](../../pages/openai.com/business/plugins/windsor-ai/index.md) (−7/+14 lines)
- [`/business/plugins/wordpress/`](../../pages/openai.com/business/plugins/wordpress/index.md) (−6/+6 lines)
- [`/business/plugins/wrike/`](../../pages/openai.com/business/plugins/wrike/index.md) (−5/+6 lines)
- [`/business/pricing/`](../../pages/openai.com/business/pricing/index.md) (−1/+0 lines)
- [`/business/why-openai/small-business/`](../../pages/openai.com/business/why-openai/small-business/index.md) (−0/+4 lines)
- [`/index/advancing-the-price-performance-frontier-with-gpt-5-6/`](../../pages/openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/index.md) (−2/+2 lines)
- [`/index/airbnb-gpt-6-astra/`](../../pages/openai.com/index/airbnb-gpt-6-astra/index.md) (−15/+6 lines)
- [`/index/albertsons-reimagining-retail/`](../../pages/openai.com/index/albertsons-reimagining-retail/index.md) (−4/+4 lines)
- [`/index/apple-is-getting-this-wrong/`](../../pages/openai.com/index/apple-is-getting-this-wrong/index.md) (−6/+6 lines)
- [`/index/astra-for-law/`](../../pages/openai.com/index/astra-for-law/index.md) (−15/+6 lines)
- [`/index/atlassian-partnership/`](../../pages/openai.com/index/atlassian-partnership/index.md) (−13/+4 lines)
- [`/index/australian-universities-ai-native-graduates/`](../../pages/openai.com/index/australian-universities-ai-native-graduates/index.md) (−6/+6 lines)
- [`/index/australian-youth-safety-blueprint/`](../../pages/openai.com/index/australian-youth-safety-blueprint/index.md) (−4/+4 lines)
- [`/index/better-prompt-caching-for-gpt-6/`](../../pages/openai.com/index/better-prompt-caching-for-gpt-6/index.md) (−2/+2 lines)
- [`/index/building-abundant-intelligence/`](../../pages/openai.com/index/building-abundant-intelligence/index.md) (−4/+4 lines)
- [`/index/chatgpt-for-your-most-ambitious-work/`](../../pages/openai.com/index/chatgpt-for-your-most-ambitious-work/index.md) (−2/+2 lines)
- [`/index/closing-ai-guidance-gap-education/`](../../pages/openai.com/index/closing-ai-guidance-gap-education/index.md) (−7/+7 lines)
- [`/index/credit-saison/`](../../pages/openai.com/index/credit-saison/index.md) (−6/+6 lines)
- [`/index/devday-2026-recap/`](../../pages/openai.com/index/devday-2026-recap/index.md) (−6/+6 lines)
- [`/index/expanding-economic-opportunity-with-ai/`](../../pages/openai.com/index/expanding-economic-opportunity-with-ai/index.md) (−4/+4 lines)
- [`/index/expanding-openai-academy-with-new-learning-paths/`](../../pages/openai.com/index/expanding-openai-academy-with-new-learning-paths/index.md) (−6/+6 lines)
- [`/index/expanding-our-presence-in-brazil/`](../../pages/openai.com/index/expanding-our-presence-in-brazil/index.md) (−6/+6 lines)
- [`/index/fair-use-benefits-everyone/`](../../pages/openai.com/index/fair-use-benefits-everyone/index.md) (−6/+6 lines)
- [`/index/fanatics-streamline-fan-experience/`](../../pages/openai.com/index/fanatics-streamline-fan-experience/index.md) (−7/+7 lines)
- [`/index/gpt-5-6-frontier-intelligence-efficiency/`](../../pages/openai.com/index/gpt-5-6-frontier-intelligence-efficiency/index.md) (−6/+6 lines)
- [`/index/gpt-6-astra/`](../../pages/openai.com/index/gpt-6-astra/index.md) (−7/+0 lines)
- [`/index/gpt-6-for-everyone/`](../../pages/openai.com/index/gpt-6-for-everyone/index.md) (−2/+2 lines)
- [`/index/helping-websites-express-ai-training-preferences/`](../../pages/openai.com/index/helping-websites-express-ai-training-preferences/index.md) (−6/+6 lines)
- [`/index/how-agents-are-transforming-work/`](../../pages/openai.com/index/how-agents-are-transforming-work/index.md) (−6/+6 lines)
- [`/index/how-ai-is-expanding-what-people-do-at-work/`](../../pages/openai.com/index/how-ai-is-expanding-what-people-do-at-work/index.md) (−6/+6 lines)
- [`/index/how-to-connect-ai-usage-to-business-value/`](../../pages/openai.com/index/how-to-connect-ai-usage-to-business-value/index.md) (−2/+2 lines)
- [`/index/how-we-will-do-better-for-australia/`](../../pages/openai.com/index/how-we-will-do-better-for-australia/index.md) (−6/+6 lines)
- [`/index/introducing-chatgpt-financial-services/`](../../pages/openai.com/index/introducing-chatgpt-financial-services/index.md) (−20/+2 lines)
- [`/index/introducing-dots/`](../../pages/openai.com/index/introducing-dots/index.md) (−6/+6 lines)
- [`/index/introducing-gpt-6-cyber/`](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md) (−2/+2 lines)
- [`/index/introducing-gpt-live-1-in-the-api/`](../../pages/openai.com/index/introducing-gpt-live-1-in-the-api/index.md) (−2/+2 lines)
- [`/index/introducing-openai-partner-network/`](../../pages/openai.com/index/introducing-openai-partner-network/index.md) (−2/+2 lines)
- [`/index/introducing-the-openai-economic-research-exchange/`](../../pages/openai.com/index/introducing-the-openai-economic-research-exchange/index.md) (−6/+6 lines)
- [`/index/itau-generative-ai/`](../../pages/openai.com/index/itau-generative-ai/index.md) (−6/+6 lines)
- [`/index/jalapeno-first-results/`](../../pages/openai.com/index/jalapeno-first-results/index.md) (−6/+6 lines)
- [`/index/lenfest-ai-collaborative-expansion/`](../../pages/openai.com/index/lenfest-ai-collaborative-expansion/index.md) (−6/+6 lines)
- [`/index/making-chatgpt-better-for-clinicians/`](../../pages/openai.com/index/making-chatgpt-better-for-clinicians/index.md) (−2/+2 lines)
- [`/index/offering-zero-data-retention-for-frontier-models/`](../../pages/openai.com/index/offering-zero-data-retention-for-frontier-models/index.md) (−6/+6 lines)
- [`/index/openai-acquires-tbpn/`](../../pages/openai.com/index/openai-acquires-tbpn/index.md) (−6/+6 lines)
- [`/index/openai-and-apa-partner-to-advance-responsible-ai/`](../../pages/openai.com/index/openai-and-apa-partner-to-advance-responsible-ai/index.md) (−6/+6 lines)
- [`/index/openai-and-foxconn-collaborate/`](../../pages/openai.com/index/openai-and-foxconn-collaborate/index.md) (−6/+6 lines)
- [`/index/openai-appoints-denise-dresser/`](../../pages/openai.com/index/openai-appoints-denise-dresser/index.md) (−5/+4 lines)
- [`/index/openai-broadcom-jalapeno-inference-chip/`](../../pages/openai.com/index/openai-broadcom-jalapeno-inference-chip/index.md) (−6/+6 lines)
- [`/index/openai-for-healthcare/`](../../pages/openai.com/index/openai-for-healthcare/index.md) (−6/+6 lines)
- [`/index/openai-grove/`](../../pages/openai.com/index/openai-grove/index.md) (−6/+6 lines)
- [`/index/openai-joins-ports-pike-project/`](../../pages/openai.com/index/openai-joins-ports-pike-project/index.md) (−6/+6 lines)
- [`/index/openai-models-google-cloud/`](../../pages/openai.com/index/openai-models-google-cloud/index.md) (−9/+0 lines)
- [`/index/openai-on-oracle-cloud/`](../../pages/openai.com/index/openai-on-oracle-cloud/index.md) (−6/+6 lines)
- [`/index/openai-servicenow-partnership-expansion/`](../../pages/openai.com/index/openai-servicenow-partnership-expansion/index.md) (−15/+6 lines)
- [`/index/openai-submits-confidential-s-1/`](../../pages/openai.com/index/openai-submits-confidential-s-1/index.md) (−6/+6 lines)
- [`/index/openai-to-acquire-astral/`](../../pages/openai.com/index/openai-to-acquire-astral/index.md) (−6/+6 lines)
- [`/index/openai-to-acquire-ona/`](../../pages/openai.com/index/openai-to-acquire-ona/index.md) (−15/+6 lines)
- [`/index/openai-to-acquire-promptfoo/`](../../pages/openai.com/index/openai-to-acquire-promptfoo/index.md) (−4/+4 lines)
- [`/index/our-approach-to-advertising-and-expanding-access/`](../../pages/openai.com/index/our-approach-to-advertising-and-expanding-access/index.md) (−6/+6 lines)
- [`/index/our-principles/`](../../pages/openai.com/index/our-principles/index.md) (−6/+6 lines)
- [`/index/our-response-to-the-tanstack-npm-supply-chain-attack/`](../../pages/openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/index.md) (−6/+6 lines)
- [`/index/pacing-model-development-cyber-capabilities/`](../../pages/openai.com/index/pacing-model-development-cyber-capabilities/index.md) (−6/+6 lines)
- [`/index/partnering-with-codeai/`](../../pages/openai.com/index/partnering-with-codeai/index.md) (−4/+4 lines)
- [`/index/paul-christiano-joins-openai-foundation-board/`](../../pages/openai.com/index/paul-christiano-joins-openai-foundation-board/index.md) (−15/+6 lines)
- [`/index/people-first-ai-fund-grantees/`](../../pages/openai.com/index/people-first-ai-fund-grantees/index.md) (−6/+6 lines)
- [`/index/people-first-ai-fund/`](../../pages/openai.com/index/people-first-ai-fund/index.md) (−6/+6 lines)
- [`/index/put-data-to-work/`](../../pages/openai.com/index/put-data-to-work/index.md) (−2/+2 lines)
- [`/index/putting-frontier-cyber-models-in-more-trusted-hands/`](../../pages/openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands/index.md) (−6/+6 lines)
- [`/index/reimagining-advertising-with-ai/`](../../pages/openai.com/index/reimagining-advertising-with-ai/index.md) (−2/+2 lines)
- [`/index/samsung-electronics-chatgpt-codex-deployment/`](../../pages/openai.com/index/samsung-electronics-chatgpt-codex-deployment/index.md) (−6/+6 lines)
- [`/index/scaling-ai-for-everyone/`](../../pages/openai.com/index/scaling-ai-for-everyone/index.md) (−6/+6 lines)
- [`/index/scaling-codex-to-enterprises-worldwide/`](../../pages/openai.com/index/scaling-codex-to-enterprises-worldwide/index.md) (−6/+6 lines)
- [`/index/supporting-california-bill-advance-ai-youth-safety/`](../../pages/openai.com/index/supporting-california-bill-advance-ai-youth-safety/index.md) (−4/+4 lines)
- [`/index/supporting-journalism-from-classrooms-to-newsrooms/`](../../pages/openai.com/index/supporting-journalism-from-classrooms-to-newsrooms/index.md) (−6/+6 lines)
- [`/index/supporting-next-generation-ai-startups-thailand/`](../../pages/openai.com/index/supporting-next-generation-ai-startups-thailand/index.md) (−6/+6 lines)
- [`/index/teens-learn-and-plan/`](../../pages/openai.com/index/teens-learn-and-plan/index.md) (−2/+2 lines)
- [`/index/ten-years/`](../../pages/openai.com/index/ten-years/index.md) (−4/+4 lines)
- [`/index/testing-ads-in-chatgpt/`](../../pages/openai.com/index/testing-ads-in-chatgpt/index.md) (−6/+6 lines)
- [`/index/the-full-stack-behind-abundant-intelligence/`](../../pages/openai.com/index/the-full-stack-behind-abundant-intelligence/index.md) (−6/+6 lines)
- [`/index/the-work-now-within-reach/`](../../pages/openai.com/index/the-work-now-within-reach/index.md) (−4/+4 lines)
- [`/index/thrive-holdings/`](../../pages/openai.com/index/thrive-holdings/index.md) (−6/+6 lines)
- [`/index/two-years-of-openai-academy/`](../../pages/openai.com/index/two-years-of-openai-academy/index.md) (−6/+6 lines)
- [`/index/uber-chatgpt-work-rollout/`](../../pages/openai.com/index/uber-chatgpt-work-rollout/index.md) (−9/+0 lines)
- [`/index/update-on-the-openai-foundation/`](../../pages/openai.com/index/update-on-the-openai-foundation/index.md) (−6/+6 lines)
- [`/index/updating-model-spec-with-teen-protections/`](../../pages/openai.com/index/updating-model-spec-with-teen-protections/index.md) (−6/+6 lines)
- [`/index/what-students-gain-from-chatgpt-critical-thinking-training/`](../../pages/openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training/index.md) (−6/+6 lines)
- [`/news/`](../../pages/openai.com/news/index.md) (−8/+8 lines)
- [`/news/company-announcements/`](../../pages/openai.com/news/company-announcements/index.md) (−6/+6 lines)
- [`/news/product-releases/`](../../pages/openai.com/news/product-releases/index.md) (−2/+2 lines)
- [`/policies/`](../../pages/openai.com/policies/index.md) (−2/+4 lines)
- [`/policies/ad-tools-terms/`](../../pages/openai.com/policies/ad-tools-terms/index.md) (−6/+4 lines)
- [`/policies/service-terms/`](../../pages/openai.com/policies/service-terms/index.md) (−5/+7 lines)
- [`/signals/`](../../pages/openai.com/signals/index.md) (−4/+3 lines)
- [`/signals/research/`](../../pages/openai.com/signals/research/index.md) (−2/+2 lines)

155 other today-updated URLs had byte-identical rendered markdown vs the 2026-11-10 snapshot.
