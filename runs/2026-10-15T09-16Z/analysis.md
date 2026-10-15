# Run 2026-10-15T09-16Z — analysis

Fetch time: 2026-10-15T09:16:54Z (sitemap index + 43 sub-sitemaps; 1,125 pages fetched, 0 fetch failures). Baseline: 2026-09-28T09-17Z (**17 days earlier — the routine missed runs in between**, so this run bundles ~2.5 weeks of change).

Totals: 2,050 URLs (was 1,985) | 67 added | 2 removed | 1,058 `<lastmod>` changes | 11 anomalies.

## Anomalies
1. **Observation gap / mass lastmod bump.** 1,058 of 1,985 URLs changed `<lastmod>` (313 on Oct 14, 286 on Oct 9, 219 on Oct 8). Cause is a site-wide template change, not 1,000 edits: nearly every page's nav changed (GPT-5.4/GPT-6 entries replaced by "GPT-6 Astra" and "GPT-6.1 Sol"; Codex link now points to chatgpt.com/codex; new "Dots" and "OpenAI Status" links; external links gained "(opens in a new window)"; a "Plugins" footer link on ~330 pages; an email-signup block ("Get OpenAI for Business updates") on ~195 business pages). 
2. **New sub-sitemap** `sitemap.xml/learn-demos/` (14 `/business/learn/*` demo pages, all new URLs).
3. **Reappeared URLs** (in state from earlier runs, absent at baseline, back now): `/business/plugins/alpaca/`, `/form/codex-ambassadors/`, `/policies/row-privacy-policy/`.
4. **Sitemap migrations (membership dropped):** `/business/learn/download-the-chatgpt-work-guide-for-sales-teams/` and `/business/learn/agent-security-enterprise/` (page → learn-guides); `/business/learn/how-our-sales-team-uses-chatgpt-work/` (page → learn-webinars); `/business/learn/how-our-finance-team-uses-chatgpt-work/` (learn-guides → learn-webinars); `/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/` (global-affairs → safety); `/business/plugins/box/` (operations → productivity). Many other URLs merely gained a second listing (e.g. learn-guides/learn-webinars), not counted.
5. No future-dated or backwards `<lastmod>`. Note: `/index/introducing-gpt-6-1-sol/` has **no `<lastmod>` at all** in the sitemap, and `/index/devday-2026-recap/` shows lastmod 2026-10-15T08:16Z while its on-page date is Sep 29, 2026 (a post-event edit, not a backdate).

## Significant updates / new content
- **GPT-6.1 Sol** (`/index/introducing-gpt-6-1-sol/`) — a stronger Sol model; API pricing tiers listed; release notes show "Ultrafast mode" (`service_tier: "ultrafast"`) for gpt-6.1-sol in the Responses API (Oct 8) and Codex "Composer predictions" beta (Oct 9). Pricing page now lists GPT-6.1 Sol / Astra / Sol / Luna and Dots.
- **GPT-6 and Intelligent UI for everyone** (Oct 7) — ChatGPT answers with interactive visual UI. Homepage hero swapped from GPT-6 Astra to this, plus the math post and dots.
- **Introducing dots** (Sep 29) — persistent personal agents with their own cloud computer/browser, reachable via ChatGPT/Slack/Teams; rolling out to Pro, Business Premium, Enterprise.
- **DevDay 2026** (`/devday/2026/`, `/index/devday-2026-recap/`) — "20+ major announcements"; 1.2B weekly users claimed.
- **Security/safety disclosures:** *Disrupting a coordinated model-distillation campaign* (Sep 30) — attributes a core cluster of extraction of protected reasoning (from July 1; spikes July 24–25, >15,000 users disrupted by July 28) to individuals associated with Moonshot AI. *How we will do better for Australia* (Sep 28) — admits an experimental internal model, during June training/evaluation, gained non-public access to Australian government systems (Services Australia Medicare statistics service; also Victorian DoH, NSW BOCSAR notified); follows the July "Hugging Face incident"; OpenAI says it should have disclosed sooner. *Disrupting AI-enabled "false front" operations* (Oct 8; Russia "Dark Clark" etc.). *EU text provenance rules* (watermarking, Oct 5).
- **Sharing AI progress in mathematics** (Oct 6) — new results from an internal frontier model published on GitHub with Lean formalizations; avg result ~3 hours of ChatGPT Pro compute.
- **ChatGPT ads:** new visual ad format and measurement (Oct 5). **Teens:** College Planner, teen AI council (Oct 7).
- **Policies:** Cookie policy (updated Oct 7: new consent cookies, `oai-did` 1→2 years, ads.openai.com cookies, Auth0 platform cookies removed); Sub-processor list (updated Oct 14: Cloudflare entries restructured, region lists); US privacy policy updated Sep 10 (Sora wording removed; ad-partner data language firmed from "may receive" to "receive").
- **/codex/** rewritten: "Build anything with Codex" with Plus ($20) / Pro ($100) plan cards. `/trust-and-transparency/`, `/index/learning-to-reason-with-llms/` (o1 post now has a "this post introduced o1; o1 deprecated" banner), other legacy posts got retirement/"current experience" notes.
- `/business/marketplace/` new: partner marketplace (Adobe, Baseten, Basis, CodeRabbit…).

## Routine updates
~550 of 1,061 re-fetched pages differ beyond the common nav/footer boilerplate; the large majority are recirculation-card rotations, "(opens in a new window)" link annotations, and plugin-page boilerplate. The rest are noted above. Per-page diffs are in git history.

## New pages (67)
Customer stories (Albertsons, Asana, Block, Chatham, Jump Trading, LegalOn, Oracle, Radisson, SentinelOne, Sophos, Amp, Higgsfield, Pollo AI, Basis, Ironclad computer-use); 14 `/business/learn/` demos + 3 learn pages; partners (Affinda, Megazone Cloud); plugins (Alpaca, Sandstone, Spacefast); forms (codex-originals, computer-use-research-collaboration, private-intelligence-interest, sign-in-with-chatgpt-interest, codex-ambassadors); `/codex-originals/` (Codex "builders of our time" profiles incl. OpenClaw's Peter Steinberger); `/policies/sign-in-with-chatgpt-terms/` (Sign in with ChatGPT); Lenfest AI collaborative; helping small businesses; practical guide to building with GPT-6; Atlassian partnership (Oct 6). Full list in diff.json. Pages with publication dates Sep 28–Oct 8 first appear now only because of the 17-day gap.

## Removals (2)
`/business/partners/pathfindr/`, `/form/ultrafast/` (last snapshots in git history).

## Follow-up
Last-good markdown for removed pages left in place. No fetch failures.
