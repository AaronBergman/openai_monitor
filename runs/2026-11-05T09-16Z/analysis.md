# Run 2026-11-05T09-16Z — Analysis

**Fetch time:** 2026-11-05T09:17:34Z | **Baseline:** 2026-09-28T09-17Z (**38-day gap — the routine missed 37 daily runs**, so this run bundles over five weeks of change)
**Stats:** 2,130 URLs (was 1,985) | 160 added | 1,733 updated | 15 removed | 75 anomalies | 43 sub-sitemaps (was 42)

Pages fetched: 1,893, zero fetch failures.

## Anomalies

1. **Observation gap.** 38 days between snapshots. `first_seen` for all 160 new URLs is therefore today's run, not the true publication date; the real appearance date is somewhere in Sep 29 – Nov 5.
2. **48 × backdated_new_url.** Mostly an artifact of the gap (OpenAI `<lastmod>` 3–27 days before our first observation). Two real clusters:
   - **18 `/business/learn/*` pages** with lastmod Oct 21–25 (e.g. "Writing with canvas in ChatGPT", "GPT‑5: Our best model for work", "Collaborate and write with GPT‑4o"). These are old-model tutorials (GPT‑4o, o3, GPT‑5) and fit with a **new sub-sitemap, `sitemap.xml/learn-demos`** (14 URLs), first seen today. Looks like a "Demos" tab being added to the Learning hub (the `/business/learn/` page now shows Guides / OpenAI on OpenAI / Webinars / Demos). Inference from page structure, not stated by OpenAI.
   - Other pre-dated new pages: `/index/teaching-students-to-think-and-learn-through-questions/` (lastmod Oct 22), `/business/partners/{bishop-fox,specterops,trustedsec}/` (Oct 15), `/business/learn/board-guide-cybersecurity-ai/` (Oct 9).
3. **19 × sitemap_migration** (URL moved between sub-sitemaps; no other change implied):
   - → `learn-guides`: `/index/builders-guide-to-gpt-5-6/`, `/index/ai-native-company-workflows/`, `/index/the-five-ai-value-models-driving-business-reinvention/`, `/index/codex-maxxing-long-running-work/`, `/index/managing-ai-investments-in-agentic-era/`, `/index/unlocking-new-ways-of-working/`, `/business/learn/download-the-chatgpt-work-guide-for-sales-teams/`, `/business/learn/agent-security-enterprise/`
   - → `learn-webinars`: `/business/learn/how-our-finance-team-uses-chatgpt-work/`, `/business/learn/how-our-sales-team-uses-chatgpt-work/`, `/business/learn/intelligence-at-work-cyber/`, `/business/learn/intelligence-at-work-financial-services/`, `/business/enabling-a-data-driven-workforce-webinar/`, `/business/fine-tuning-gpt-4o-webinar/`
   - → `global-affairs-news-listed`: `/index/understanding-ai-and-learning-outcomes/`, `/global-affairs/new-economic-analysis/`, `/index/equipping-workers-with-insights-about-compensation/`, `/index/how-countries-can-end-the-capability-overhang/`
   - → `safety`: `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/`
   Net effect: OpenAI is consolidating "learn" content (guides/webinars/demos) into dedicated sitemaps and moving global-affairs news into a "news-listed" one.
4. **3 × reappeared_url:** `/business/plugins/alpaca/` (last seen 2026-09-24), `/form/codex-ambassadors/` (last seen 2026-06-24), `/policies/row-privacy-policy/` (last seen 2026-05-27). The ROW privacy policy returning (lastmod Nov 3) coincides with the US privacy policy update below.
5. **lastmod_removed:** `/index/advancing-independent-research-ai-alignment/` lost its `<lastmod>` (was 2026-09-25T19:18:24Z); still listed.
6. **4 × new_url_without_lastmod:** `/index/introducing-gpt-6-1-sol/`, `/index/introducing-gpt-6-1-terra/` (both major model launches, so the missing lastmod is odd — likely published/templated outside the normal pipeline), `/ads/customers/evernote/`, `/ads/customers/flipsnack/`.
7. **Bulk lastmod burst:** 538 updated pages carry lastmod 2026-11-05 and 251 carry 2026-11-03 (plus 276 on Nov 1) — consistent with site-wide template deploys (see footer change below). 87 of the new URLs have lastmod on Nov 5 between 00:55Z and 09:02Z, i.e. a huge publishing burst in the ~8 hours before our fetch. No future-dated or backwards-moving lastmod values.
8. **Forward-dated policy text (not a sitemap anomaly):** `/policies/usage-policies/` now states "Effective: November 20, 2026" — i.e. text announcing a change ~15 days after observation.

## Significant updates

- **Site-wide footer/nav rewrite (~1,730 of 1,733 updated pages).** Footer "Latest" list now links GPT‑6.1 Sol and GPT‑6 Astra (GPT‑5.4 dropped); adds Dots, Plugins, Models, OpenAI Status links; Codex now points to chatgpt.com/codex; Apps SDK and Open Models links removed. This is the cause of almost all "updated" counts.
- **Homepage `/`:** adds a "Talk to us" (contact sales) button next to "Try ChatGPT"; Astra hero poster replaced by a "Recent news" section (Images 2.6, LifeVal, "Accelerating engineering for the physical world").
- **`/policies/privacy-policy/`:** updated May 18 → **Sep 10, 2026**. Removes Sora from the intro ("tools like ChatGPT"); ad-partner data language changes from "may receive" to "receive information from advertisers and other data partners" used to measure ads for Free and Go users.
- **`/policies/usage-policies/`:** effective **Nov 20, 2026**. Licensed-advice rule reworded to cover *building tools that offer* tailored licensed advice (and implying the AI itself holds a license); the "national security or intelligence purposes without our review and approval" line is removed.
- **`/business/pricing/`:** adds Rosalind Academic Plan pointer; "5x more usage" → "More usage than standard"; Canvas row removed; extensions row now includes Word.
- **`/products/release-notes/`:** Oct 30 entry — **GPT‑6 Rosalind** (life-sciences reasoning) in Admin Preview for Enterprise; "External access controls" entry from Sep 24 rolled off.
- **`/business/learn/`:** hub redesigned as "Learning hub" with Demos tab and a "Connected Intelligence for In-House Legal" webinar promo.
- **Legacy research posts refreshed** (large diffs): `/index/learning-to-reason-with-llms/` (o1) now carries a deprecation banner ("o1‑preview and o1‑mini retired from the API; o1 deprecated"), likewise `/index/thinking-with-images/` and others — retirement notes added to old model launches.

## Routine updates
~1,600 pages changed only by the footer/nav (plus minor link-label "(opens in a new window)" tweaks). Full list in `diff.json`.

## New pages (160)

**Models / products**
- `/index/introducing-gpt-6-1-sol/` — upgrade nearly matching GPT‑6 Astra on agentic coding/computer use at ~1/5 the price; cached input $0.10/M tokens.
- `/index/introducing-gpt-6-1-terra/` — fast model, API prices 50% below GPT‑5.6 Terra / GPT‑6.1 Sol; visual reasoning, computer use.
- `/index/gpt-6-for-everyone/` — GPT‑6 for ChatGPT's 1.2B weekly users with "Intelligent UI" (interactive answers).
- `/index/practical-guide-building-gpt-6/` — model guide for GPT‑6 family.
- `/index/introducing-dots/` — "always-on agents"; updated Nov 3 to add GPT‑6.1 Terra.
- `/index/introducing-images-2-6/` — Images 2.6 with animated GIFs; 4B images/week.
- `/index/decisions-api/` — Decisions API GA, built on GPT‑6 Luna, up to 10x faster for bounded decisions.
- `/index/introducing-the-rosalind-academic-plan/` — Rosalind for academic labs; `/index/scaling-ai-research-for-complex-biological-data/`.
- `/business/images-api/`, `/index/devday-2026-recap/` (20+ announcements), `/devday/2026/`.

**Corporate / partnerships / M&A**
- Acquisitions: `/index/openai-to-acquire-pierre/` (Pierre Computer Co., Code Storage / Trees & Diffs libraries; pairs with `/index/scaling-git-at-openai/`), `/index/openai-to-acquire-orchestra-bio/` (biopharma coordination, to join Rosalind).
- Partnerships: `/index/openai-models-google-cloud/` (OpenAI models + Codex in Google Cloud Model Garden; `/form/openai-on-google-cloud/`), `/index/atlassian-partnership/`, `/index/openai-servicenow-partnership-expansion/`, `/index/oracle-apps-in-chatgpt/`, `/index/openai-nask-ai-safety-security-partnership/` (Poland).
- Executives: `/index/jill-hazelbaker-chief-corporate-affairs-officer/` (Chief Corporate Affairs Officer), `/index/dan-driscoll-joins-openai/` (Senior Counselor, National Security Modernization).
- Ads: `/index/chatgpt-ads-expands-26-new-countries/` (89 countries, 100k+ advertisers), `/index/new-chatgpt-ads-format-and-measurement/`, `/index/building-chatgpt-ad-stack/`, `/ads/customers/{evernote,flipsnack}/`, `/policies/brazil-advertising-terms/`.
- Enterprise: `/business/private-intelligence/` (+ `privacy-by-product`, interest form), `/business/marketplace/`, `/business/forward-deployed-engineering/` (+ `/index/forward-deployed-engineering-means/`), `/business/solutions/legal/`, `/business/contact-sales-retail/`, `/index/chatgpt-expanding-world-of-work/` (OpenAI Signals data, 165 work activities), `/index/the-future-of-the-firm/`, plus ~30 customer stories (Uber, AT&T, Albertsons, Jump Trading, Oracle, Block, Cisco, etc.).
- ~19 new `/business/plugins/*` pages (Atlassian, ServiceNow, Krea, WordPress, Alpaca, Sandstone, Spacefast, seven Oracle NetSuite/Analytics) and 6 `/business/partners/*` pages.
- Sign-in with ChatGPT: `/form/sign-in-with-chatgpt-interest/`, `/policies/sign-in-with-chatgpt-terms/`.

**Security / safety / policy** (a large cyber push)
- `/cybersecurity/`, `/cyber-at-the-frontier/`, `/index/grid-protectors-program/` (data-centre load flexibility), `/index/coordinated-disclosure-of-critical-vulnerabilities/` ("Patch the Planet"), `/index/rewarding-defenders-with-bigger-bug-bounties/`, `/index/preparing-our-next-security-sprint-to-harden-openai/`, `/index/securing-our-frontier-model-training-environment/`, `/index/a-thousand-fewer-paths-to-root/`, `/index/daybreak-red-aws-govcloud/`, `/index/empowering-cyber-defenders/`, cyber customer stories (Cisco, Cloudflare, Check Point, SentinelOne, Sophos).
- **`/index/disrupting-a-coordinated-model-distillation-campaign/`** — OpenAI says it disrupted a campaign (earliest activity first week of July) extracting protected reasoning from its models; also `/index/disrupting-ai-enabled-false-front-operations/`.
- `/index/updated-model-spec/` (Model Spec 2026-10-29, five values), `/index/how-we-detect-frontier-model-misalignment/`, `/index/towards-safety-cases-for-frontier-ai-training/`, `/index/community-safety-report-and-new-protections-for-teens/`, EU/Australia policy notes (`eu-text-provenance`, `the-eus-next-chapter-in-ai-is-agentic`, `how-we-will-do-better-for-australia`), `/index/fair-use-benefits-everyone/`, `/index/helping-websites-express-ai-training-preferences/`.
- Other: `/codex-originals/` + form, `/form/codex-ambassadors/` (reappeared), `/economic-research-collaborators/`, `/form/computer-use-research-collaboration/`, `/index/sharing-ai-progress-in-mathematics/`, `/index/lifeval/`.

Full URL list: `diff.json` → `added`.

## Removals (15)
Last snapshots in git history. Several look like renames/moves rather than deletions (inference from slugs):
- `/business/partners/pathfindr/` → `/business/partners/affinda/` ("Affinda (formerly Pathfindr)")
- `/business/plugins/oracle-analytics/` → `oracle-analytics-cloud/`; `/business/plugins/wordpress-com/` → `/business/plugins/wordpress/`
- `/economic-research-exchange/` → `/economic-research-collaborators/`
- Genuinely gone from sitemap: partner pages for Canva, Dropbox, Gusto, HubSpot, QuickBooks, Stripe; plugin `atlassian-rovo` (superseded by new `atlassian` pages); `/daybreak/partners-new/`, `/form/ultrafast/`, `/prism/`, `/business/plugins/mcp-server-for-wordpress/`.

Fetch failures: none.
