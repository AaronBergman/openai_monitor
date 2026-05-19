# openai_monitor

Daily changelog of [openai.com](https://openai.com)'s public website,
maintained by a Claude Code routine. Each run diffs the current sitemap
against the prior one, fetches changed pages, and writes a plain-language
summary that a smart layperson can follow.

## 2026-05-19T09-16Z

**Fetch time:** 2026-05-19T09:19:02Z UTC | **Baseline:** 2026-05-18T09-15Z

**TL;DR:** The most notable event today is the removal of 7 core ChatGPT product pages from OpenAI's sitemap — including the `/chatgpt/overview/`, `/chatgpt/pricing/`, `/chatgpt/team/`, `/chatgpt/enterprise/`, `/chatgpt/desktop/`, `/chatgpt/education/`, and a student writing guide. These were major marketing/product pages, all present since the start of monitoring on May 7, with several having been actively updated as recently as May 12. Some content appears to have migrated to parallel paths (`/business/chatgpt-pricing/`, `/academy/chatgpt-for-education/` remain indexed), but the main `/chatgpt/` product section — the hub for ChatGPT plan-shopping and desktop/education pages — has been deindexed. The other 106 changes are all metadata-only timestamp refreshes with no visible text changes: 11 Codex Academy pages were swept at ~07:55 UTC, 25 global-affairs articles were swept yesterday at ~09:38 UTC, and 70 index/news pages were updated throughout May 18. No anomalies.

### Removed from Sitemap (7 — significant)

All removed from the `/sitemap.xml/page/` sub-sitemap. Present in every daily run since 2026-05-07.

| URL | Last known title | Last lastmod |
|-----|-----------------|-------------|
| [`/chatgpt/overview/`](pages/openai.com/chatgpt/overview/index.md) | Get answers. Find inspiration. Be more productive. | 2026-05-10 |
| [`/chatgpt/pricing/`](pages/openai.com/chatgpt/pricing/index.md) | Pricing | 2026-05-12 |
| [`/chatgpt/team/`](pages/openai.com/chatgpt/team/index.md) | ChatGPT for business, powered by OpenAI's most advanced models | 2026-05-12 |
| [`/chatgpt/enterprise/`](pages/openai.com/chatgpt/enterprise/index.md) | Frontier AI built for enterprise | 2026-05-07 |
| [`/chatgpt/desktop/`](pages/openai.com/chatgpt/desktop/index.md) | ChatGPT on your desktop | 2026-04-09 |
| [`/chatgpt/education/`](pages/openai.com/chatgpt/education/index.md) | Bring AI to campus at scale | 2026-04-22 |
| [`/chatgpt/use-cases/student-writing-guide/`](pages/openai.com/chatgpt/use-cases/student-writing-guide/index.md) | A Student's Guide to Writing with ChatGPT | 2026-04-20 |

The `/chatgpt/` path is not fully gone — `/chatgpt/download/`, `/chatgpt/use-cases/writing-with-ai/`, and `/chatgpt/search-product-discovery/` remain indexed. Last-good snapshots of all removed pages are preserved in git history.

### Updated Pages (106 — all metadata-only)

All 106 pages showed zero content change; only lastmod timestamps moved. Three sweep clusters:

- **Codex Academy (11 pages, ~07:55 UTC today):** All Codex for Work tutorials refreshed from ~May 16 to today. Automated CMS republish pattern — 11 pages touched in a 60-second window.
- **Global Affairs (25 pages, ~09:38 UTC yesterday):** All global-affairs policy/governance posts swept from ~May 15 to ~May 18.
- **Index + News (70 pages, throughout May 18):** Wide sweep of product announcements, safety/security content, economic blueprints, and teen-safety posts. Includes GPT-5.5 cyber page, Stargate announcement, and many others. No text changes detected.

Full list in [runs/2026-05-19T09-16Z/analysis.md](runs/2026-05-19T09-16Z/analysis.md).

**Stats:** 1,309 total URLs | +0 added | 106 updated (all metadata) | −7 removed | 0 anomalies | 32 sub-sitemaps

---

## 2026-05-17T09-15Z

**Fetch time:** 2026-05-17T09:15:42Z UTC | **Baseline:** 2026-05-16T09-15Z

**TL;DR:** One new article today: Malta and OpenAI announced a "world's first" national partnership under the OpenAI for Countries program — every Maltese citizen can get free ChatGPT Plus for one year after completing a government-backed AI literacy course developed by the University of Malta. The initiative, called "AI for All," is managed by the Malta Digital Innovation Authority and launches in May 2026. George Osborne is identified as "Head of OpenAI for Countries," signaling this is a named, dedicated OpenAI program (already active in Estonia and Greece for education). Elsewhere, 33 URLs received lastmod updates, but content diffs show only one substantive change: the Astral acquisition article's "Keep reading" recommendation carousel rotated to show more recent articles (TanStack npm security post, Deployment Company launch, Campus Network interest form), and the global-affairs news hub now lists the Malta article. All other timestamp bumps — including a batch sweep of 16 teen-safety pages at ~05:35 UTC and a sweep of news hubs, policy pages, and the podcast page — show no visible content change. The `amex-chatgpt-business/` URL continues to appear as "removed" due to a legacy-file artifact in the repository; it has been absent from OpenAI's live sitemap since May 14. No anomalies.

### Anomalies

None detected.

### New Pages (1 added)

**[OpenAI and Malta partner to bring ChatGPT Plus to all citizens](pages/openai.com/index/malta-chatgpt-plus-partnership/index.md)** *(lastmod: 2026-05-16T10:31:32Z; Global Affairs)* — Malta and OpenAI announced what they call the world's first national partnership of this type: Maltese citizens who complete a free AI literacy course (developed by the University of Malta, covering what AI is, what it can't do, and how to use it responsibly at home and work) unlock one year of ChatGPT Plus at no cost to them. Distribution is managed by the Malta Digital Innovation Authority; the first phase launches in May 2026. The partnership is branded as part of **OpenAI for Countries** — a named program designed to take governments from early AI interest to strategic national adoption, with tailored priorities (education, workforce training, AI literacy) rather than a one-size-fits-all model. Malta's angle is civic AI literacy at population scale, with the University-designed course as the gating mechanism. The article explicitly positions this as a model for other countries: "Where Malta leads, I hope others will follow" (George Osborne, Head of OpenAI for Countries). Malta joins Estonia and Greece already cited as OpenAI for Countries partners.

### Notable Page Updates

- **[openai.com/index/openai-to-acquire-astral/](pages/openai.com/index/openai-to-acquire-astral/index.md)** — "Keep reading" recommendation carousel at the bottom of the page rotated. Previous recommendations (from May 6 and Apr 27 posts) replaced with: "Our response to the TanStack npm supply chain attack" (May 13), "OpenAI Campus Network: Student club interest form" (May 11), and "OpenAI launches the Deployment Company" (May 11). Article content unchanged.

- **[openai.com/news/global-affairs/](pages/openai.com/news/global-affairs/index.md)** — Malta article now appears in the hub listing. The older Cloudflare OpenAI Agent Cloud article (Apr 13) rotated off the featured section.

- **16 teen-safety and child-safety pages** received simultaneous lastmod bumps around 05:35 UTC with no visible content change — consistent with a CMS batch refresh of the teen-safety content cluster published in recent weeks.

- **Policy pages** (`/policies/conversion-dpa/`, `/policies/conversion-subprocessors/`, `/policies/conversion-terms/`, `/policies/kr-privacy-policy/`) and **`/podcast/`** received lastmod updates with no visible content change.

### Removed from Sitemap (1, artifact)

- **`https://openai.com/amex-chatgpt-business/`** — Recurring artifact: this URL has been absent from OpenAI's live sitemap since May 14. It keeps appearing in the baseline because legacy-named files from early runs remain in `sitemaps/openai.com/sub/latest/`. State records `last_seen = 2026-05-13T09-15Z`.

**Stats:** 1,314 total URLs | +1 added | 33 updated (lastmod) | 1 removed (artifact) | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-17T09-15Z/diff.json](runs/2026-05-17T09-15Z/diff.json) | [runs/2026-05-17T09-15Z/analysis.md](runs/2026-05-17T09-15Z/analysis.md)*

---

## 2026-05-18T09-15Z

**Fetch time:** 2026-05-18T09:16:52Z UTC | **Baseline:** 2026-05-17T09-15Z

**TL;DR:** No new pages or removals today. The 36 `<lastmod>` updates break into three clusters: (1) a **teen/child safety content sweep** — 15 safety-section pages had their sitemap timestamps refreshed again around 08:33 UTC (this is the third consecutive daily batch sweep of this cluster; content diffs show only the "Keep reading" recommendation carousels rotating, not new substantive text); (2) a **routine CMS refresh** of six news-hub landing pages and four product pages including `running-codex-safely`, `work-with-codex-from-anywhere`, and the GPT-5.5 article (the GPT-5.5 "Keep reading" box swapped out the "Testing ads in ChatGPT" link for "A new personal finance experience in ChatGPT," reflecting the May 15 launch); and (3) a **Conversion policy trio** (`conversion-terms`, `conversion-dpa`, `conversion-subprocessors`) quietly refreshed early this morning — the published date still reads May 14 and no text changed, so this looks like a backend CMS touch rather than a legal update. The `introducing-prism` page also got a lastmod bump (from May 5 → May 18) but no visible content change was detected. No anomalies.

### Anomalies

None detected.

### Notable Page Updates

- **Teen/child safety cluster (15 pages)** — For the third day running, the entire teen-safety content cluster received a simultaneous lastmod sweep (~08:33–34 UTC). Pages include `introducing-the-teen-safety-blueprint`, `updating-model-spec-with-teen-protections`, `teen-safety-policies-gpt-oss-safeguard`, `ai-literacy-resources-for-teens-and-parents`, `japan-teen-safety-blueprint`, and nine more. Content diffs show no substantive change; the `Keep reading` carousels rotated to surface more recent articles. This is likely an automated CMS republish triggered whenever the teen-safety content cluster is touched (possibly as OpenAI continues rolling out related work behind the scenes).

- **[/index/introducing-gpt-5-5/](pages/openai.com/index/introducing-gpt-5-5/index.md)** — The "Keep reading" section at the bottom of the GPT-5.5 release page was updated. The "Testing ads in ChatGPT" (May 7) recommendation was replaced with "A new personal finance experience in ChatGPT" (May 15). The main article content is unchanged. This is a routine carousel rotation.

- **[/index/introducing-prism/](pages/openai.com/index/introducing-prism/index.md)** — lastmod jumped from `2026-05-05` to `2026-05-18T08:05Z` — a 13-day gap, larger than other sweep items. No text differences detected in the rendered markdown. Could be a backend metadata or asset update. Prism is OpenAI's free AI-native scientific writing platform (a LaTeX workspace powered by GPT-5.2, built on the acquired Crixet platform).

- **[/form/enterprise-trusted-access-for-cyber/](pages/openai.com/form/enterprise-trusted-access-for-cyber/index.md)** — The "Trusted Access for Cyber" application form was refreshed (lastmod `2026-05-17T09:40Z`). This form lets vetted enterprise customers and cybersecurity practitioners apply for access to OpenAI's higher-risk dual-use cybersecurity capabilities — the pitch is that these tools are "powerful force multipliers for network defenders." Applicants must prove identity, professional use case, and OpenAI organization ID. This update follows the recent Axios and TanStack npm supply-chain security disclosures published on the same site.

- **[/form/codex-for-oss/](pages/openai.com/form/codex-for-oss/index.md)** — The open-source maintainer access form for Codex was also refreshed (lastmod `2026-05-17T09:39Z`). Selected maintainers get 6 months of ChatGPT Pro (includes Codex), conditional access to Codex Security, and API credits for coding/maintenance workflows.

- **Security posts** (`/index/axios-developer-tool-compromise/`, `/index/our-response-to-the-tanstack-npm-supply-chain-attack/`) — Both received lastmod bumps around 07:26 UTC with no visible content change. The Axios post advises macOS users to update apps before May 8 (already past); the TanStack post covers a North Korea-linked supply chain attack on the TanStack npm package.

- **Conversion policy trio** (`/policies/conversion-terms/`, `/policies/conversion-dpa/`, `/policies/conversion-subprocessors/`) — All three refreshed between 05:13–09:14 UTC. Published dates unchanged (May 14); no text differences detected. These govern how advertisers provide conversion data to OpenAI (part of OpenAI's advertising/measurement infrastructure launched with the Conversion Tools product).

**Stats:** 1,314 total URLs | +0 added | 36 updated (lastmod) | 0 removed | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-18T09-15Z/diff.json](runs/2026-05-18T09-15Z/diff.json) | [runs/2026-05-18T09-15Z/analysis.md](runs/2026-05-18T09-15Z/analysis.md)*

---

## 2026-05-16T09-15Z

**Fetch time:** 2026-05-16T09:17:04Z UTC | **Baseline:** 2026-05-15T09-15Z

**TL;DR:** Two headline launches today. First, OpenAI unveiled a **personal finance experience in ChatGPT** — Pro users in the U.S. can now connect their bank accounts and investment portfolios (via Plaid, 12,000+ institutions) and ask ChatGPT context-grounded questions about spending, goals, and tradeoffs. This is a major product step into personal financial services, directly competing with apps like Mint/Copilot/Monarch Money. Second, **Databricks published a case study** showing GPT-5.5 is now state-of-the-art on their OfficeQA Pro enterprise benchmark — 50% accuracy, 46% error reduction vs. GPT-5.4 — particularly for parsing scanned PDFs and legacy enterprise documents in long-running agent workflows. On the educational content side, OpenAI's Codex-for-work academy section kept expanding: three new role-specific guides appeared (for sales, data science, and business operations teams), and several existing Codex Academy pages were substantially expanded with cross-links and additional use cases. The stale `/amex-chatgpt-business/` URL (replaced by a `/business/`-hierarchy URL in the May 14 run) was finally cleaned from the sitemap. No anomalies.

### Anomalies

None detected.

### New Pages (5 added)

**[A new personal finance experience in ChatGPT](pages/openai.com/index/personal-finance-chatgpt/index.md)** *(lastmod: 2026-05-15T22:55:41Z)* — Announces a preview of a major new ChatGPT capability: Pro users in the U.S. can securely connect their financial accounts through Plaid (Intuit support coming), see a live dashboard of spending/portfolio/subscriptions, and ask ChatGPT questions grounded in their real financial data. The page touts ChatGPT's existing scale (200 million monthly users already asking money questions) and positions GPT-5.5's stronger reasoning as enabling more nuanced financial analysis. Supports saving "Financial memories" (e.g., ongoing savings goals) so context carries across conversations. OpenAI explicitly notes this is not a replacement for professional financial advice. Currently rolling out as a preview to Pro users before expanding to Plus and free tiers. Homepage carousel has been updated to feature this launch prominently.

**[Databricks brings GPT‑5.5 to enterprise agent workflows](pages/openai.com/index/databricks/index.md)** *(lastmod: 2026-05-16T00:28:31Z)* — Customer case study published May 15. Databricks integrated GPT-5.5 into their production agent harness after the model set a new state-of-the-art on OfficeQA Pro, their benchmark for complex enterprise document tasks (scanned PDFs, legacy files, long-context). Key metrics: **50% accuracy** on OfficeQA Pro (first model to cross that threshold) and **46% error reduction** vs. GPT-5.4. The gains are concentrated in parsing-heavy workflows where earlier models lost numerical precision on scanned digits. Databricks is now making GPT-5.5 available to their customer agent workflow builders.

**[How business operations teams use Codex](pages/openai.com/academy/codex-for-work/how-business-operations-teams-use-codex/index.md)** *(lastmod: 2026-05-16T07:17:13Z)* — Third entry in OpenAI Academy's role-specific Codex guides (the section was introduced May 14–15). Covers five use cases: off-track initiative briefs, strategic initiative health updates, leadership decision packets, board/company progress updates, and scenario/tradeoff models. Each use case shows how Codex aggregates scattered inputs (project trackers, KPI dashboards, meeting notes, Slack threads, spreadsheets) and produces the first working draft, with human judgment still owning the final recommendation.

**[How data science teams use Codex](pages/openai.com/academy/codex-for-work/how-data-science-teams-use-codex/index.md)** *(lastmod: 2026-05-16T07:17:12Z)* — Five use cases for data teams: KPI root-cause analysis, business impact readouts, analytics request agents, executive KPI reviews, and dashboard builder/monitor. Framing emphasizes that Codex handles the scaffolding (query structure, result formatting, presentation prep) while the data scientist owns analytical interpretation.

**[How sales teams use Codex](pages/openai.com/academy/codex-for-work/how-sales-teams-use-codex/index.md)** *(lastmod: 2026-05-16T07:17:06Z)* — Five use cases for sales: pipeline prioritization from underworked accounts, meeting prep and follow-up, forecast review and commit risk monitoring, strategic account plan refresh, and stalled deal diagnosis. Part of the same wave of role-specific Academy content; together these three guides represent OpenAI systematically building enablement material for the Codex-for-work non-developer audience introduced May 14.

### Notable Page Updates

- **[openai.com/](pages/openai.com/index.md)** (+68 chars) — Hero carousel rotated again: now leads with the personal finance feature ("A new personal finance experience in ChatGPT"). The previous featured story rolled off.

- **[openai.com/academy/codex-for-work/](pages/openai.com/academy/codex-for-work/index.md)** (+1,343 chars) — Hub page for the Codex-for-work section substantially expanded: now shows cards/previews for all three new role-specific guides (sales, data science, business operations) alongside the existing finance-teams guide.

- **[openai.com/academy/top-10-use-cases-codex-for-work/](pages/openai.com/academy/top-10-use-cases-codex-for-work/index.md)** (+3,479 chars) — The "Top 10 use cases" mega-page expanded significantly, now cross-linking to all new role-specific guides.

- **[openai.com/academy/how-finance-teams-use-codex/](pages/openai.com/academy/how-finance-teams-use-codex/index.md)** (+713 chars) — Finance teams guide updated with new related-content links pointing to the freshly published sales, data science, and business operations guides.

- Multiple other Codex Academy pages (codex-automations, codex-plugins-and-skills, what-is-codex, working-with-codex, etc.) received smaller updates (+43 to +299 chars) — primarily new "Explore Codex for work" navigation links and updated related-article cards pointing to the new role-specific guides.

All other timestamp changes (350+ URLs) show zero substantive content change — consistent with a routine CMS cache-invalidation sweep.

### Removed from Sitemap (1)

- **`https://openai.com/amex-chatgpt-business/`** — Cleanup: this URL was replaced by `/business/amex-chatgpt-business-credit/` in the May 14 run; the stale entry lingered in the sitemap one extra day before being removed.

**Stats:** 1,313 total URLs | +5 added | 391 updated (lastmod) | -1 removed | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-16T09-15Z/diff.json](runs/2026-05-16T09-15Z/diff.json) | [runs/2026-05-16T09-15Z/analysis.md](runs/2026-05-16T09-15Z/analysis.md)*

---

## 2026-05-15T09-15Z

**Fetch time:** 2026-05-15T09:17:53Z UTC | **Baseline:** 2026-05-14T09-15Z

**TL;DR:** Three parallel storylines dominated today. First, **Codex keeps expanding**: a new `codex/for-work/` landing page pitches Codex to non-developer business users (knowledge workers) for the first time, the main Codex page now links to it, and a product post announces Codex is coming to the ChatGPT mobile app (in preview) so users can supervise long-running agent tasks from their phones — OpenAI disclosed that 4 million people use Codex every week. Second, **a new advertising-infrastructure legal stack appeared**: three legal documents (Conversion Terms, Conversion DPA, and Conversion Sub-Processor List) were quietly published, indicating OpenAI is formalizing a conversion-tracking tool that lets advertisers share event data with OpenAI for measuring and optimizing ads — structurally similar to the Meta Pixel or Google Ads conversion API. Third, **a notable safety post** explained new ChatGPT features that carry short "safety summaries" across conversation sessions to better catch evolving risk signals in rare high-stakes scenarios (suicide, self-harm, harm-to-others). 395 URLs show updated lastmod timestamps; the vast majority are CMS cache-invalidation artifacts with no substantive content change.

### Anomalies

None detected. *(Note: the script flagged 1 "removed" URL — `https://openai.com/amex-chatgpt-business/` — but this is a stale-file artifact: that URL was genuinely removed in the May 13→14 run, and a legacy-named sub-sitemap file had lingered in `sitemaps/openai.com/sub/latest/`. It does not represent a new removal today.)*

### New Pages (7 added)

**[Codex for Work — "Get more done with Codex"](pages/openai.com/codex/for-work/index.md)** *(lastmod: 2026-05-14T22:45:49Z)* — A new `/codex/for-work/` landing page, distinct from the developer-facing `/codex/` page, aimed at non-technical business users. Pitches Codex as a general productivity layer: it can research topics, synthesize information, draft briefs and presentations, build weekly summaries from calendars/docs, and automate recurring tasks — all without requiring the user to write or understand code. Available as a desktop app for macOS and Windows. The main `/codex/` page was updated to cross-link here with an "Explore Codex for work" CTA.

**[Work with Codex from anywhere](pages/openai.com/index/work-with-codex-from-anywhere/index.md)** *(lastmod: 2026-05-15T08:35:26Z)* — Announces Codex is now in the ChatGPT mobile app (preview), allowing users to monitor and steer ongoing Codex agent sessions from their phones while the work runs on a laptop, a Mac mini, or a remote devbox. Highlights the "4 million people use Codex every week" stat and frames mobile as critical for the emerging human-in-the-loop pattern where quick check-ins prevent unnecessary agent rework. Also covers enterprise deployment modes where Codex runs on managed remote infrastructure.

**[Helping ChatGPT better recognize context in sensitive conversations](pages/openai.com/index/chatgpt-recognize-context-in-sensitive-conversations/index.md)** *(lastmod: 2026-05-15T04:13:15Z)* — Safety post describing two new features. (1) Cross-conversation safety summaries: a separate safety-reasoning model creates short factual notes about prior safety-relevant context (e.g., signs of distress) and passes them into subsequent sessions, scoped narrowly to high-risk scenarios and kept only for a limited time — not for general personalization. (2) Improved in-conversation context recognition trained with mental-health-expert guidance to detect escalating risk cues mid-conversation. Focus areas: suicide, self-harm, harm-to-others. OpenAI emphasizes these features fire rarely and are calibrated to avoid over-triggering on benign conversations.

**[Sea's View on the Future of Agentic Software Development with Codex](pages/openai.com/index/sea-david-chen/index.md)** *(lastmod: 2026-05-15T03:35:04Z)* — Episode 20 of OpenAI's "Executive Function" interview series, featuring David Chen, Co-Founder of Sea (Singapore-based company behind Shopee, Garena, SeaMoney) and Chief Product Officer of Shopee. Chen discusses Sea rolling out Codex across its entire development organization. Strong internal usage reported in code understanding, debugging, and feature development. Sea is also hosting the first regional Codex Hackathon Series across Asia — starting in Singapore then moving to Indonesia, Taiwan, and Vietnam. A notable endorsement from one of Southeast Asia's largest tech companies.

**[Conversion Terms](pages/openai.com/policies/conversion-terms/index.md)** *(effective: 2026-05-14; lastmod: 2026-05-15T09:14:15Z)* — Legal terms governing access to OpenAI's "Conversion Tools," which let advertisers provide "Conversion Data" (user event signals) to OpenAI. OpenAI uses this data to provide "Reporting Data," create custom audiences, and optimize/measure ad delivery. Comparable in structure to Meta's Conversion API or Google's Ads Data Hub. Advertisers must obtain necessary consents and cannot provide sensitive personal data.

**[Conversion Data Processing Addendum](pages/openai.com/policies/conversion-dpa/index.md)** *(effective: 2026-05-14; lastmod: 2026-05-15T08:45:20Z)* — The GDPR-facing DPA supplement to the Conversion Terms. Designates OpenAI and the customer as independent data controllers for most processing, with OpenAI acting as processor only for "Restricted Processing." References the Conversion Sub-Processor List for downstream data sharing.

**[Conversion Sub-Processor List](pages/openai.com/policies/conversion-subprocessors/index.md)** *(lastmod: 2026-05-15T08:15:37Z)* — Lists the third-party sub-processors OpenAI uses when handling Conversion Data in its processor capacity.

### Notable Page Updates

- **[openai.com/](pages/openai.com/index.md)** — Homepage hero carousel rotated: now surfaces "Work with Codex from anywhere" and "Helping ChatGPT better recognize context in sensitive conversations" (both new today). The prior featured items — "GPT-5.5 Instant" and the Amazon Bedrock/AWS partnership card — rolled off the front-page spotlight.

- **[openai.com/codex/](pages/openai.com/codex/index.md)** — Added "Explore Codex for work" link pointing to the new `/codex/for-work/` page (+228 chars). Now also shows macOS/Windows download availability explicitly.

- **[openai.com/business/](pages/openai.com/business/index.md)** — Minor update (+114 chars) mentioning Codex among the workspace-agent capabilities available on ChatGPT Business/Enterprise.

All other 390+ URL timestamp changes show zero substantive content change on the representative sample tested — consistent with a CMS-wide cache-invalidation sweep.

**Stats:** 1,308 total URLs | +7 added | 395 updated (lastmod) | 0 genuine removals | 0 anomalies | 32 sub-sitemaps

*Full machine-readable diff: [runs/2026-05-15T09-15Z/diff.json](runs/2026-05-15T09-15Z/diff.json) | [runs/2026-05-15T09-15Z/analysis.md](runs/2026-05-15T09-15Z/analysis.md)*
---

## 2026-05-14T09-15Z

**Fetch time:** 2026-05-14T09:15:53Z UTC | **Baseline:** 2026-05-13T09-15Z

**TL;DR:** The headline today is a security disclosure: OpenAI published a detailed account of how two employee laptops were infected via the "Mini Shai-Hulud" supply chain attack against the TanStack npm library on May 11, exposing limited internal source code and code-signing certificates for iOS, macOS, and Windows apps. No user data was compromised, but **macOS users must update all OpenAI apps by June 12, 2026** or they will stop working. Two other new pages arrived alongside it: a deep-dive engineering post explaining how OpenAI built a custom Windows sandbox for the Codex coding agent, and a refreshed co-branded American Express page (the old `/amex-chatgpt-business/` URL was retired and replaced with `/business/amex-chatgpt-business-credit/` offering $300/year in statement credits for Amex Business Platinum/Gold cardholders). 340 URL timestamps refreshed but a representative sample shows no substantive content changes.

### Anomalies

Two existing pages show `lastmod` timestamps ~15–22 seconds ahead of our fetch time — a benign race condition where the CMS updated those pages' timestamps while the sitemap was mid-generation:

- **near-future_lastmod** (CMS timing): `https://openai.com/index/accelerating-cyber-defense-ecosystem/` — lastmod `2026-05-14T09:16:15Z` vs. fetch at `2026-05-14T09:15:53Z` (22 sec gap)
- **near-future_lastmod** (CMS timing): `https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/` — lastmod `2026-05-14T09:16:11Z` vs. fetch at `2026-05-14T09:15:53Z` (18 sec gap)

Both are known, existing cybersecurity-related pages. These are the same pages whose related-article carousels were updated to surface today's new security disclosure.

### New Pages (3 added)

**[Our Response to the TanStack npm Supply Chain Attack](pages/openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/index.md)** — A security disclosure published May 13, 2026. The "Mini Shai-Hulud" attack compromised the TanStack npm library; two OpenAI employee devices were infected, leading to unauthorized access of a limited set of internal source code repositories. Code-signing certificates for iOS, macOS, and Windows were included in the exposed repos. OpenAI found no evidence of user data exposure or production system compromise. Key user action: **macOS users must update ChatGPT Desktop, Codex App, Codex CLI, and Atlas by June 12, 2026** — apps signed with the old certificate will stop launching after that date when it is revoked. (Windows and iOS users need not act.) OpenAI notes this is a repeat pattern, referencing the prior "Axios incident," and is accelerating supply-chain defenses.

**[Building a Safe, Effective Sandbox to Enable Codex on Windows](pages/openai.com/index/building-codex-windows-sandbox/index.md)** — An engineering deep-dive by David Wiesen (Member of Technical Staff), published May 13, 2026. Before this work, Windows Codex users had to choose between approving every agent command (tedious) or granting full access (risky). The post walks through why Windows AppContainer, Windows Sandbox VM, and Mandatory Integrity Control labeling were all unsuitable, then describes the two-phase custom sandbox OpenAI built — starting with an "unelevated sandbox" using ACLs and low-integrity tokens, then redesigning as an "elevated sandbox" for better enterprise compatibility. The result brings Windows Codex to parity with macOS/Linux: writes limited to the workspace, no internet by default, without admin prompts.

**[The First-of-Its-Kind ChatGPT Business Credit (Amex)](pages/openai.com/business/amex-chatgpt-business-credit/index.md)** — A refreshed co-branded landing page for American Express Business Platinum and Business Gold cardholders, offering up to $300/year in statement credits on US purchases of ChatGPT Business. This page replaces the old `/amex-chatgpt-business/` URL (removed), moving the content into the `/business/` URL hierarchy and adding specific "Business Credit" framing. Survey data cited: 87% of small business owners using AI save time, 81% reduce manual work, 73% improve productivity (Amex Trendex).

### Removed from Sitemap (1)

- **`https://openai.com/amex-chatgpt-business/`** — Retired and replaced by `https://openai.com/business/amex-chatgpt-business-credit/` (see above). Last known lastmod: 2026-05-12T16:14:03Z.

### Notable Page Updates

The homepage (`https://openai.com/`) received a minor CTA update: the hero section's quick-access button row now leads with a new **"Learn about ChatGPT Business"** link and dropped the **"Stories"** shortcut. The row now reads: Learn about ChatGPT Business | Talk with ChatGPT | Research | API Platform.

The related-article carousels on the cybersecurity pages `/index/gpt-5-5-with-trusted-access-for-cyber/` and `/index/accelerating-cyber-defense-ecosystem/` were refreshed to surface today's two new security/engineering posts (TanStack and Codex Windows Sandbox) in place of older articles.

All other 340 URL timestamp changes appear to be CMS cache-invalidation artifacts (zero substantive content changes found in the representative sample tested).

**Stats:** 1,301 total URLs | +3 added | 340 updated (lastmod) | −1 removed | 2 anomalies (benign timing) | 32 sub-sitemaps

---

## 2026-05-13T09-15Z

**Fetch time:** 2026-05-13T09:19:46Z UTC | **Baseline:** 2026-05-12T09-15Z

**TL;DR:** Today's dominant story is a large sitemap restructure: OpenAI quietly dropped two "internal-use" sub-sitemaps that housed 152 B2B customer-story and brand-story URLs, de-indexing 121 enterprise case-study pages (Stripe, Klarna, Morgan Stanley, Cisco, Canva, Uber, Zendesk, and many more) while migrating 31 others into purpose-named sub-sitemaps. The net result is a leaner sitemap — 1,178 URLs, down from 1,294 — and those customer stories are no longer surfaced to search engines via the sitemap. Separately, a burst of five new Codex-focused pages signals an accelerating push: NVIDIA and AutoScout24 published case studies featuring Codex with GPT‑5.5, OpenAI added a finance-teams Codex guide, and the results of the "Parameter Golf" ML competition were published.

### Anomalies

Two form pages have `lastmod` timestamps set to within 160 milliseconds of our fetch time — in other words, to the instant the sitemap was generated. This is a CMS artifact where the sitemap generator writes the current timestamp as `lastmod` on every build for these pages, rather than recording a genuine edit time. Both timestamps are functionally simultaneous with the fetch, not evidence of a real future modification.

- **future_lastmod** (CMS artifact): `https://openai.com/form/chatgpt-pro-community/` — lastmod `2026-05-13T09:19:46.160Z` vs. fetch at `2026-05-13T09:19:46Z` (160 ms gap)
- **future_lastmod** (CMS artifact): `https://openai.com/form/100-chats-book-request/` — lastmod `2026-05-13T09:19:46.096Z` vs. fetch at `2026-05-13T09:19:46Z` (96 ms gap)

### Sitemap Restructure: 121 Customer Stories De-indexed

OpenAI's sitemap index dropped from 34 to 32 sub-sitemaps. The two removed sub-sitemaps — named `internal-use-show-on-b2b-customer-stories-hub` and `internal-use-show-on-brand-stories-hub` — were internal-facing classification buckets that contained 152 total URLs. Of those:

- **31 URLs were migrated** to appropriate product-branded sub-sitemaps (`brand-stories-chatgpt`, `brand-stories-api`, `sora`, `startup`, `api`, `page`) — mostly GPT-5 / o1 brand stories and startup spotlights.
- **121 URLs were completely removed** from the sitemap. These are predominantly older B2B enterprise customer-story pages. The pages may still exist on the site, but search engines will no longer find them via the sitemap. Representative removals include:

  - Finance: `morgan-stanley`, `klarna`, `stripe`, `bny`, `singular-bank`, `balyasny-asset-management`
  - Enterprise SaaS: `salesforce`, `cisco`, `zendesk`, `datadog`, `intercom`, `retool`, `typeform`, `notion`
  - Consumer / retail: `canva`, `uber`, `doordash`, `booking-com`, `wayfair`, `estee-lauder`, `lowes`
  - Healthcare / life-sciences: `moderna`, `philips`, `lifespan`, `color-health`, `promega`, `genmab`
  - Education / government: `khan-academy`, `state-of-minnesota`, `government-of-iceland`, `duolingo`, `asu`
  - Japanese companies: `mixi`, `ly-corporation`, `cyberagent`, `dai-nippon-printing`, `eneos-materials`, `taisei`, `zenken`, `mercari`
  - Many others (see [runs/2026-05-13T09-15Z/diff.json](runs/2026-05-13T09-15Z/diff.json) for the full list)

Last snapshots of these pages remain in git history under `pages/openai.com/index/<slug>/index.md`.

### New Pages (Codex Push)

**[How Finance Teams Use Codex](pages/openai.com/academy/how-finance-teams-use-codex/index.md)** — A new OpenAI Academy guide covering 10 detailed Codex use cases tailored to finance teams: monthly business review narratives, variance analysis, planning, and reporting. Includes copy-ready prompts and suggestions for Codex skills/plugins across a finance tech stack. Published ~05:00 UTC May 13.

**[AutoScout24 Customer Story](pages/openai.com/index/autoscout24/index.md)** — Europe's largest online car marketplace (~30 M monthly users, 2,000 employees) adopted Codex for its ~1,000 engineering/data/product builders after a three-month evaluation. ChatGPT was deployed company-wide for AI literacy; Codex handles complex coding tasks in daily engineering workflows. Published ~06:45 UTC May 13.

**[NVIDIA Customer Story](pages/openai.com/index/nvidia/index.md)** — NVIDIA's coding-agents team and AI researchers use Codex with **GPT‑5.5** for production engineering and ML research loops. The page directly quotes NVIDIA engineers praising GPT-5.5's autonomy and tool selection. Key quote: "GPT-5.5 has been a massive unlock as a creative partner, especially when it comes to knowledge work." This is one of the clearest public endorsements of GPT-5.5 from a named enterprise. Published ~06:44 UTC May 13.

**[What Parameter Golf Taught Us](pages/openai.com/index/what-parameter-golf-taught-us/index.md)** — Post-competition analysis of OpenAI's "Parameter Golf" ML challenge (1,000+ participants, 2,000+ submissions). Covers record-track highlights (novel training optimizations), non-record creative approaches (non-autoregressive text modeling, dynamic tokenization), and lessons learned from running the challenge with coding agents. Published ~08:29 UTC May 13.

**[Codex Enterprise Promo Form](pages/openai.com/form/codex-enterprise-promo/index.md)** — A new lead-generation form for enterprise Codex interest. Published ~08:48 UTC May 13.

### Notable Page Updates (130 total)

The 130 updated pages span routine CMS refresh timestamps and genuine edits. Highlights:

- **`/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/`** — Content grew from 38,341 to 38,635 chars; the enterprise AI report was expanded.
- **`/business/guides-and-resources/staying-ahead-in-the-age-of-ai/`** — Grew from 24,175 to 24,469 chars.
- **`/business/guides-and-resources/a-practical-guide-to-building-ai-agents/`** — Shrank from 39,340 to 39,156 chars (some content removed from the agents guide).
- **`/amex-chatgpt-business/`** — Grew from 7,942 to 8,357 chars (the American Express co-branded ChatGPT page expanded).
- **`/academy/codex-for-work/`** and **`/academy/codex-how-to-start/`** — Both expanded, consistent with the Codex content push.
- **`/news/company-announcements/`**, **`/news/engineering/`**, **`/news/product-releases/`**, **`/news/safety-alignment/`**, **`/news/global-affairs/`**, **`/news/security/`** — All hub index pages refreshed.
- Many `/global-affairs/` articles and `/index/` pages had bulk lastmod refreshes with unchanged content (CMS publish-wave artifact).

### Removed from Sitemap (121 URLs)

All 121 removed URLs are B2B enterprise and consumer customer-story pages at `openai.com/index/<company-name>/`. These were classified under the now-dropped `internal-use-show-on-b2b-customer-stories-hub` sub-sitemap. The pages are still in the git snapshot archive. A selection:

`ada`, `altera`, `arco-education`, `asu`, `axios-allison-murphy`, `balyasny-asset-management`, `basis`, `bbva`, `bbva-2025`, `be-my-eyes`, `blue-j`, `bny`, `booking-com`, `canva`, `canva-cam-adams`, `chime-vineet-mehra`, `choco`, `cisco`, `clay`, `cna-walter-fernandez`, `coderabbit`, `color-health`, `commonwealth-bank-of-australia`, `consensus`, `cyberagent`, `dai-nippon-printing`, `datadog`, `decagon`, `digital-green`, `doordash-mariana-garavaglia`, `doppel`, `duolingo`, `eliseai-minna-song`, `endex`, `eneos-materials`, `estee-lauder`, `expedia-jochen-koedijk`, `factory`, `fanatics-betting-gaming-andrea-ellis`, `figma-david-kossnick`, `genmab`, `genspark`, `government-of-iceland`, `grab`, `harvey`, `healthify`, `hebbia`, `hibob`, `holiday-extras`, `hygh`, `indeed`, `indeed-maggie-hulce`, `intercom`, `invideo-ai`, `ironclad`, `jetbrains`, `jetbrains-2025`, `khan-academy`, `klarna`, `launchdarkly-claire-vo`, `lifespan`, `lowes`, `lowes-chandhu-nair`, `ly-corporation`, `match-group`, `mavenagi`, `mercado-libre`, `mercari`, `mirakl`, `mixi`, `moderna`, `morgan-stanley`, `netomi`, `neurogum`, `notion`, `nubank`, `oscar`, `outtake`, `paf`, `paradigm`, `philips`, `plex-coffee`, `podium`, `promega`, `retell-ai`, `retool`, `rogo`, `rox`, `safetykit`, `salesforce`, `san-antonio-spurs`, `scania`, `schoolai`, `scout24`, `singular-bank`, `stadler`, `state-of-minnesota`, `steuerrecht`, `stripe`, `summer-health`, `superhuman`, `taisei`, `trustbank`, `typeform`, `uber`, `uber-enables-outstanding-experiences`, `unify`, `upwork`, `vfl-wolfsburg`, `viable`, `wayfair`, `waymark`, `whoop`, `wix`, `wrtn`, `yabble`, `zalando`, `zelma`, `zendesk`, `zenken`, `10bedicu`

**Stats:** 1,178 total URLs | +5 added | 130 updated | −121 removed | 2 anomalies (CMS artifacts) | 32 sub-sitemaps (was 34)

---

## 2026-05-12T09-15Z

**Two major platform launches dominated today's update: OpenAI officially entered the enterprise cybersecurity market with "Daybreak" — a branded AI-powered vulnerability scanning and cyber defense product — and launched the OpenAI Deployment Company, a new $4 billion majority-owned subsidiary that embeds specialized engineers directly inside enterprises to deploy AI into production workflows.** Together, these represent OpenAI's most significant structural expansion beyond selling model access: it is now offering a named security product and a professional-services company. A batch of 174 page updates accompanied the launches, mostly bulk CMS refreshes across customer stories and global-affairs content, but one notable change was the removal of the K–12 Teachers plan link from the ChatGPT pricing page.

### Anomalies

None detected.

### New Pages

**[OpenAI Daybreak](pages/openai.com/daybreak/index.md)** — A new cybersecurity product combining GPT-5.5, the Codex agentic harness, and security industry partners. It positions OpenAI as an active participant in enterprise cyber defense: finding and patching code vulnerabilities, threat modeling, and remediation at scale. Three model access tiers are offered: standard GPT-5.5, "Trusted Access for Cyber" (for verified defensive security work), and "GPT-5.5-Cyber" (preview access for red teaming and penetration testing). Trust partners listed include Cloudflare, Cisco, CrowdStrike, Palo Alto Networks, Oracle, Zscaler, Akamai, and Fortinet. A [lead-gen form](pages/openai.com/daybreak/request-a-vulnerability-scan/index.md) lets organizations request a vulnerability scan.

**[OpenAI Launches the Deployment Company](pages/openai.com/index/openai-launches-the-deployment-company/index.md)** (dated May 11, 2026) — OpenAI is launching a new majority-owned subsidiary ("DeployCo") to embed Forward Deployed Engineers (FDEs) inside enterprises. It simultaneously announced the acquisition of Tomoro, an applied AI consulting firm (~150 engineers), whose clients include Tesco, Virgin Atlantic, and Supercell. Initial investment exceeds $4 billion, led by TPG with co-leads Advent, Bain Capital, and Brookfield. Consulting partners Bain & Company, Capgemini, and McKinsey & Company are included. The [companion business page](pages/openai.com/business/the-openai-deployment-company/index.md) describes the FDE model: embedding engineers to redesign critical workflows from diagnostic through production deployment.

**[Signals Q1 2026 Research Update](pages/openai.com/signals/research/2026q1-update/index.md)** — OpenAI's economic research arm published Q1 2026 ChatGPT consumer adoption data. Users with typically feminine names now account for over half of gender-inferable users. Over-35 users gained share. Fastest-growing countries by per-capita usage include Dominican Republic, Haiti, Japan, Mexico, and Tanzania — showing broadening beyond Western markets. This page was published within minutes of the monitoring run.

### Notable Updates

**`/chatgpt/pricing/`** — The K–12 Teachers plan link (`/plans/k12-teachers/`) was **removed** from the pricing page navigation. This is a product-tier change affecting educational access visibility on the main pricing page.

**`/business/frontier/`** — Updated to explicitly reference the new OpenAI Deployment Company, replacing "OpenAI Forward Deployed Engineers" with a link to the DeployCo page and adding text explaining the subsidiary's purpose.

**`/about/`** — News carousel rotated; "Advancing voice intelligence with new models in the API" is now the lead story.

**Cyber content sweep (08:33–08:35Z)**: Three cybersecurity pages (`/index/cybersecurity-in-the-intelligence-age/`, `/index/accelerating-cyber-defense-ecosystem/`, `/index/gpt-5-5-with-trusted-access-for-cyber/`) were refreshed in a tight window just before the Daybreak product pages were published — part of a coordinated launch sequence.

### Removals

None.

### Stats

| Metric | Value |
|--------|-------|
| Total URLs | 1,294 |
| Added | 5 |
| Updated | 174 |
| Removed | 0 |
| Anomalies | 0 |
| Sub-sitemaps | 34 |

Full analysis: [runs/2026-05-12T09-15Z/analysis.md](runs/2026-05-12T09-15Z/analysis.md)

---

## 2026-05-11T09-15Z

**Fetch time:** 2026-05-11T09:17:28Z UTC | **Baseline:** 2026-05-10T09-16Z

**TL;DR:** This run catches up on activity from May 7–11. The most important developments: OpenAI launched **Trusted Contact** — a ChatGPT safety feature letting adults designate a trusted person to be notified in crisis situations — and **GPT‑5.5‑Cyber**, a specialized model for defenders of critical infrastructure. The **cookie policy** was updated to add `ads.openai.com` cookies, reflecting the ChatGPT ads rollout. The **OpenAI–Microsoft partnership was restructured**: Microsoft's API license is now non-exclusive, OpenAI can now serve all products on any cloud provider (not just Azure first), and Microsoft no longer pays OpenAI a revenue share. Two new pages appeared today (May 11): an enterprise scaling guide drawing on interviews with European executives, and an OpenAI Campus Network student club interest form. The bulk of the 122 lastmod updates are CMS metadata flushes across ~60 customer story pages with no content changes.

### Anomalies

None detected.

### New Pages

| Page | Date | Summary |
|---|---|---|
| [How enterprises are scaling AI](pages/openai.com/business/guides-and-resources/how-enterprises-are-scaling-ai/index.md) | May 11 | Insights from European enterprise executives (Philips, BBVA, Mirakl, Scout24, JetBrains, Scania) on scaling AI. Five patterns: culture before tooling, governance as enabler, ownership over consumption, quality before scale, protecting judgment work. Downloadable PDF guide. |
| [OpenAI Campus Network: Student club interest form](pages/openai.com/index/openai-campus-network-student-club-interest-form/index.md) | May 11 | OpenAI is partnering with student clubs at universities worldwide. Offers early access to tools, events support, and a global network of student leaders. |

### Notable Updates

- **Cookie policy revised** ([`/policies/cookie-policy/`](pages/openai.com/policies/cookie-policy/index.md)) — Updated May 6, 2026 (lastmod advanced from 2026-02-25 to 2026-05-08). Cookie table now lists `ads.openai.com` and `deploymentsafety.openai.com` as domains, reflecting the ads platform and deployment-safety features. Four other privacy/communications policy pages updated simultaneously on May 7.

- **Microsoft partnership restructured** ([`/index/next-phase-of-microsoft-partnership/`](pages/openai.com/index/next-phase-of-microsoft-partnership/index.md)) — Lastmod refreshed to May 10. Key terms: Microsoft remains primary cloud partner with Azure-first commitment, but **OpenAI can now serve all products on any cloud**; Microsoft's license is now **non-exclusive**; Microsoft no longer pays revenue share to OpenAI; OpenAI's payments to Microsoft continue through 2030 with a total cap; Microsoft stays a major shareholder.

- **Fine-tuning shutdown notices confirmed** — Three fine-tuning pages ([`gpt-4o-fine-tuning`](pages/openai.com/index/gpt-4o-fine-tuning/index.md), [`introducing-vision-to-the-fine-tuning-api`](pages/openai.com/index/introducing-vision-to-the-fine-tuning-api/index.md), [`introducing-improvements-to-the-fine-tuning-api`](pages/openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/index.md)) continue to carry the May 8 notice: *"OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users."* Lastmod refreshed again today — no reversal.

- **OpenAI Academy URL restructuring** — [`/academy/building-with-ai/`](pages/openai.com/academy/building-with-ai/index.md) and [`/academy/chatgpt-for-education/`](pages/openai.com/academy/chatgpt-for-education/index.md) updated: learning track links now point to `academy.openai.com/home/collections/...` instead of `/home/clubs/...` — internal URL migration, same content.

- **Batch CMS refresh** — ~60 `/index/` customer story pages (Uber, Cisco, BBVA, Grab, Harvey, Klarna, etc.) all bumped to lastmod 2026-05-11 with no content changes. Routine metadata flush.

**Stats:** 1289 total URLs | +2 added | 122 updated | -0 removed | 0 anomalies | 34 sub-sitemaps

---



## 2026-05-10T09-16Z

**Fetch time:** 2026-05-10T09:17:38Z UTC | **Baseline:** 2026-05-09T09-15Z

**TL;DR:** The headline story is OpenAI **shutting down its self-serve fine-tuning platform** (announced May 8 via retroactive notices added to three existing fine-tuning pages) — a significant change for developers who relied on training custom models through OpenAI's API since 2023. On the other side of the ledger, OpenAI is doubling down on specialized AI for cybersecurity: GPT-5.5-Cyber launched in limited preview for critical-infrastructure defenders this week, and new posts explain both the technical governance controls for Codex agents and a broader strategy for democratizing AI-powered defense. One new customer story (Simplex, Japan) documents 70% faster screen development using Codex. The rest of the 198 lastmod changes are batch CMS metadata refreshes across Academy, Global Affairs, and customer story pages with no detectable content changes.

### Anomalies

None detected.

**Infrastructure note:** `/sitemap.xml/page/` returned HTTP 503 persistently (4 retry attempts); served from 2026-05-09 cached snapshot. URLs listed only in that sub-sitemap are not diffed this run.

### Notable updates

- **Fine-tuning platform shutdown** (MAJOR) — Three fine-tuning announcement pages ([introducing improvements to the fine-tuning API](pages/openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/index.md), [introducing vision to the fine-tuning API](pages/openai.com/index/introducing-vision-to-the-fine-tuning-api/index.md), [GPT-4o fine-tuning](pages/openai.com/index/gpt-4o-fine-tuning/index.md)) each received an identical retroactive notice:
  > *"OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users but existing users of the fine-tuning platform will be able to create training jobs for the coming months. All fine-tuned models will remain available for inference until their base models are deprecated."*
  The self-serve fine-tuning API has been available since August 2023. Deprecation timeline is on the OpenAI developer docs site.

- **GPT-5.5-Cyber and Trusted Access for Cyber** — [`/index/gpt-5-5-with-trusted-access-for-cyber/`](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) (published May 7, lastmod refreshed today): A specialized cybersecurity model in limited preview for defenders protecting critical infrastructure. Three-tier access system: default GPT-5.5, GPT-5.5 with TAC (Trusted Access for Cyber) for verified defensive workflows, and GPT-5.5-Cyber for the most specialized authorized work (authorized red-teaming, pen-testing). Advanced Account Security (phishing-resistant MFA) required for individual TAC members from June 1, 2026.

- **Running Codex safely at OpenAI** — [`/index/running-codex-safely/`](pages/openai.com/index/running-codex-safely/index.md) (published May 8, metadata refreshed today): OpenAI's internal playbook for governing Codex agents: sandboxed execution environments, human approval gates for high-risk actions, network access policies, managed credential systems, and agent-native audit trails.

- **OpenAI on AWS related-posts refresh** — [`/index/openai-on-aws/`](pages/openai.com/index/openai-on-aws/index.md): Sidebar "keep reading" links rotated to newer content ("Advancing voice intelligence" and "Testing ads in ChatGPT," replacing "GPT-5.5 Instant" and "New ways to buy ChatGPT ads").

- **Batch CMS refreshes** — ~20 Global Affairs pages (all ~18:41 UTC May 8), ~21 Academy pages (May 7–8), ~50 customer story `/index/` pages (all ~07:xx UTC today), 9 form pages (May 8), and 5 policy pages (May 7–8) received lastmod bumps. No content changes detected on any of them.

### New pages (1)

| Page | Date | Summary |
|---|---|---|
| [Simplex](pages/openai.com/index/simplex/index.md) | May 8 | Japanese technology company Simplex adopts ChatGPT Enterprise + Codex as its primary coding agent; reports 70% fewer hours per screen developed, 40% fewer per screen designed, 17% fewer for integration testing; focuses on redesigning the full development process around AI rather than using AI as an assistive overlay |

### Removals

0 pages removed.

**Stats:** 1,287 total URLs | +1 added | 198 lastmod updates | 0 removed | 0 anomalies | 34 sub-sitemaps (1 served from cache)

---

## 2026-05-09T09-15Z

**Fetch time:** 2026-05-09T09:16:02Z UTC | **Baseline:** 2026-05-07T09-15Z

**TL;DR:** A busy two days on openai.com. OpenAI published seven new articles across safety,
security, and developer topics — including new real-time voice API models, a limited preview of
GPT-5.5-Cyber for critical-infrastructure defenders, a "Trusted Contact" crisis-notification
feature for ChatGPT users, and a bilingual English/French privacy explainer aimed at Canadian
audiences. Multiple waves of coordinated updates touched privacy policies, Codex content, and
the OpenAI Academy. One notable structural event: the sub-sitemap that listed ~122 B2B customer
stories began returning HTTP 403 — those pages are still live but are no longer indexed through
that endpoint. One metadata anomaly: the `enterprise-privacy/` page's claimed lastmod jumped 15
months backward with no content change.

### Anomalies

1. **Backwards lastmod — `enterprise-privacy/`**
   The sitemap's `<lastmod>` for `https://openai.com/enterprise-privacy/` regressed from
   `2026-05-04` to `2025-01-31` (roughly 15 months backward). The page content is
   byte-for-byte identical to the prior snapshot and the in-page "Updated: January 8, 2026"
   date is unchanged. This is a CMS/metadata glitch, not a content rollback.

2. **B2B customer-stories sub-sitemap now returns HTTP 403**
   The sub-sitemap `https://openai.com/sitemap.xml/internal-use-show-on-b2b-customer-stories-hub/`
   (which listed 122 `/index/` customer-story pages) returned HTTP 403 this run. Spot-checks
   confirm the underlying pages (e.g., `/index/canva/`, `/index/cisco/`) remain live and
   fully accessible. OpenAI appears to have restricted the sitemap endpoint itself — possibly
   intentionally, given the "internal-use-" prefix in the sub-sitemap name. All 122 URLs are
   preserved in `state/known_urls.json`.

### New pages (7)

| Page | Date | Summary |
|---|---|---|
| [Advancing voice intelligence with new models in the API](pages/openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/index.md) | May 7 | Three new realtime audio API models: GPT-Realtime-2 (GPT-5-class reasoning in voice), GPT-Realtime-Translate (live 70→13 language translation), GPT-Realtime-Whisper (live streaming transcription) |
| [GPT-5.5 with Trusted Access for Cyber](pages/openai.com/index/gpt-5-5-with-trusted-access-for-cyber/index.md) | May 7 | GPT-5.5-Cyber rolled out in limited preview to critical-infrastructure defenders; explains three-tier Trusted Access for Cyber framework; Advanced Account Security (phishing-resistant) required for top-tier access from June 1, 2026 |
| [Running Codex safely at OpenAI](pages/openai.com/index/running-codex-safely/index.md) | May 8 | Technical guide to OpenAI's internal Codex governance: sandboxing, human-approval gates for high-risk actions, network policies, and agent-native audit trails |
| [How ChatGPT learns about the world while protecting privacy](pages/openai.com/index/how-chatgpt-protects-privacy/index.md) | May 6 | Bilingual (English + French) plain-language privacy explainer covering training data practices, personal information handling, and user privacy controls — likely produced for Canadian regulatory context |
| [Introducing Trusted Contact in ChatGPT](pages/openai.com/index/introducing-trusted-contact-in-chatgpt/index.md) | May 7 | New optional safety feature: adults 18+ can nominate a trusted person to receive automated notifications if OpenAI's systems detect serious self-harm risk; extends existing parental-alert system to all users |
| [Advancing youth safety and wellbeing in EMEA](pages/openai.com/index/advancing-youth-safety-in-emea/index.md) | May 5 | European Youth Safety Blueprint (5 pillars for age-appropriate AI policy) and announcement of first EMEA Youth & Wellbeing Grant recipients |
| [Parloa](pages/openai.com/index/parloa/index.md) | May 7 | Customer story: European startup Parloa builds enterprise voice-driven customer service agents using the OpenAI API |

### Notable updates

- **B2B Signals messaging rebrand** — [`signals/b2b/`](pages/openai.com/signals/b2b/index.md):
  "AI advantage" replaced throughout with "frontier advantage"; intro rewritten to be more
  concise. Deliberate positioning shift to align with OpenAI's "frontier model" branding.

- **Privacy policy wave** (all updated May 7–8): `services-privacy-policy`, `communications-privacy-policy`,
  `services-communications-privacy-policy`, `us-privacy-policy`, `cookie-policy`, and `usage-policies`
  — six policy documents updated in a coordinated 24-hour window, coinciding with the new privacy explainer.

- **API page** — new "Enterprise-ready solutions for real impact" section added with a three-tab
  interface linking to use cases, industries, and blueprints.

- **Codex ecosystem refresh** — ~15 Codex-related pages (codex/, codex/get-started/, gpt-5-2-codex through gpt-5-5-instant, introducing-upgrades-to-codex, codex-now-generally-available, etc.) all refreshed May 7–8, coordinated with Codex GA.

- **Academy learning content** — ~21 OpenAI Academy course pages refreshed May 7–8 (codex, building-with-ai, chatgpt-for-education, customer-success, data-analysis, marketing, etc.).

- **FedRAMP Moderate** — [`index/openai-available-at-fedramp-moderate/`](pages/openai.com/index/openai-available-at-fedramp-moderate/index.md):
  Updated (May 9) to note that GPT-5.5 is now available in the FedRAMP environment, and that
  Codex Cloud will soon be accessible via FedRAMP ChatGPT Enterprise workspace.

- **Customer stories hub rotation** — [`business/customer-stories/`](pages/openai.com/business/customer-stories/index.md):
  Added Parloa and Simplex to the featured list; VfL Wolfsburg and Axios Allison Murphy rotated out.

### Removals

0 pages confirmed removed. See anomaly #2 above for the 122 URLs now inaccessible via the
b2b-customer-stories sub-sitemap.

**Stats:** 1,164 current URLs | +7 added | 153 lastmod updates | 122 missing via 403 sub-sitemap (0 confirmed removed) | 2 anomalies | 33/34 sub-sitemaps fetched

---

## 2026-05-07T09-15Z

**Fetch time:** 2026-05-07T09:17:05Z UTC | **Baseline:** 2026-05-07T09-01Z

**TL;DR:** OpenAI's CMS ran a batch regeneration cycle between the bootstrap run and
this one (~14 minutes apart), causing 34 pages to show fresh `<lastmod>` timestamps.
Of those 34, only **one page had a real content change**: the `/index/podium/` customer
story rotated a single "Keep reading" recommended-article link (swapped "Singular Bank"
for "How frontier enterprises are building an AI advantage"). The other 33 were
timestamp-only updates with identical content. No URLs were added or removed. No
anomalies detected.

### The one real content change

- [https://openai.com/index/podium/](pages/openai.com/index/podium/index.md) —
  "Keep reading" carousel updated: swapped out the
  [Singular Bank story](pages/openai.com/index/singular-bank/index.md) in favour of
  [How frontier enterprises are building an AI advantage](pages/openai.com/index/introducing-b2b-signals/index.md)
  (both dated May 6, 2026). Main article body (GPT-5.1 powering AI agents for 10,000+ SMBs) unchanged.

### Notable timestamp-only updates (no content change)

34 pages had `<lastmod>` bumped from ~08:xx UTC to ~09:xx UTC — a CMS batch
re-index signature. The most notable was `/index/our-principles/` (Sam Altman),
whose timestamp crossed a day boundary (May 6 → May 7) but content was identical.
See [runs/2026-05-07T09-15Z/analysis.md](runs/2026-05-07T09-15Z/analysis.md) for the
full list.

**Stats:** 1279 total URLs | +0 added | 34 lastmod changes (1 content change) | -0 removed | 0 anomalies | 34 sub-sitemaps

---

- **Sitemap monitored:** `https://openai.com/sitemap.xml` (sitemap-index → ~34 sub-sitemaps)
- **Routine schedule:** daily
- **What's tracked:** added / removed / updated URLs (per `<lastmod>`),
  plus anomalies like backwards-moving timestamps, future-dated mods,
  reappearing URLs, and similar oddities.
- **Bot defense:** openai.com is fronted by Cloudflare with TLS-fingerprint
  blocking. The conversion tool uses `curl-cffi` with Chrome impersonation
  to bypass the 403 that plain Python clients receive. robots.txt explicitly
  allows scraping (`User-agent: * / Allow: /`).

## Repo layout

| Path | Contents |
| ---- | -------- |
| `README.md` | This file. Newest run entries are PREPENDED below. |
| `sitemaps/openai.com/<run_id>.xml` | Dated root sitemap-index snapshots. |
| `sitemaps/openai.com/latest.xml` | Most recent index — overwritten each run. |
| `sitemaps/openai.com/sub/<run_id>/*.xml` | Dated sub-sitemap snapshots. |
| `sitemaps/openai.com/sub/latest/*.xml` | Most recent sub-sitemaps — overwritten each run. |
| `pages/openai.com/<path>.md` | Current markdown of each page. Git history is the archive. |
| `runs/<run_id>/analysis.md` | Long-form analysis written for that run. |
| `runs/<run_id>/diff.json` | Machine-readable diff vs prior baseline. |
| `state/known_urls.json` | Cumulative URL state: first_seen, last_seen, lastmod history. |
| `tools/html_to_md.py` | Canonical HTML→markdown converter (uses curl-cffi). |
| `tools/url_path.py` | Canonical URL→repo-path mapping. |
| `tools/requirements.txt` | pip dependencies. |

`<run_id>` format is `YYYY-MM-DDTHH-MMZ` (UTC).

## Timestamp discipline

Three distinct timestamps are tracked, never conflated:

- **`<lastmod>`** — what OpenAI *claims* about a page in their sitemap.
- **fetch time** — UTC time *we* actually retrieved the sitemap or page.
- **first_seen** — the earliest `run_id` when a URL appeared here.

Anomalies generally live in the gap between these.

---

## 2026-05-07T09-01Z — Bootstrap

**TL;DR:** Initial baseline captured. Fetched the openai.com sitemap-index,
walked all 34 sub-sitemaps, downloaded 1277
of 1279 pages through curl-cffi (Chrome TLS impersonation; plain Python
hits a Cloudflare 403), converted to markdown, and committed the snapshot.
No diff is possible yet; the next daily run will produce the first real
changelog entry.

- **Fetch time:** 2026-05-07T09:01:08.630082Z
- **Sub-sitemaps:** 34
- **URLs in sitemap:** 1279
- **Pages stored:** 1277
- **Fetch failures:** 2
- **Anomalies (bootstrap-detectable):** see below.

### Bootstrap-detectable anomalies

Even on the bootstrap run, with no prior baseline, two URLs from the sitemap
returned **HTTP 404** when fetched. These are listed in the sitemap-index but
are not actually live pages — a sitemap/site mismatch. The first one is
particularly interesting:

- **`https://openai.com/index/inworld-ai-DO-NOT-PUBLISH/`** — appears in the
  public sitemap but 404s. The literal string `DO-NOT-PUBLISH` in the path
  strongly suggests this is an internal staging slug that leaked from
  OpenAI's CMS into the production sitemap. Worth watching: if the URL ever
  starts returning 200, that's the moment OpenAI accidentally published an
  Inworld-AI–related page (which the routine will then fetch and snapshot).
- **`https://openai.com/brand-old/`** — also in the sitemap, also 404. Likely
  a deprecated brand-guidelines page that was removed from the site but not
  the sitemap.

Both will be re-checked every daily run. State changes (404 → 200, or
disappearance from the sitemap entirely) will be flagged.

See [`runs/2026-05-07T09-01Z/analysis.md`](runs/2026-05-07T09-01Z/analysis.md) for the full bootstrap report.