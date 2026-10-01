# Analysis — 2026-10-01T09-16Z

**Fetch time:** 2026-10-01T09:16:17Z (sitemap index + 42 sub-sitemaps; 282 pages fetched via curl-cffi, 0 failures)
**Baseline:** 2026-09-28T09-17Z. **Note:** runs for 2026-09-29 and 2026-09-30 are missing from the repo, so this diff spans ~3.0 days and covers the whole DevDay 2026 (Sep 29) launch window.

Totals: 2000 URLs (1985 → 2000) | 16 added | 1 removed | 266 updated | 0 anomalies | 42 sub-sitemaps.

## Anomalies
None detected. No `<lastmod>` later than fetch time, none moved backwards, no sub-sitemap migrations, no reappearing URLs, no new URL with a stale `<lastmod>`. (Caveat: the missed Sep 29–30 runs mean we cannot say *when* within the gap pages changed, only that they did.)

## Significant updates
- **/codex/** — headline rewritten from "Codex — The same powerful coding agent—now in ChatGPT" to "Build anything with Codex — Move faster, go further…", with a new "Get started / Codex is included in your ChatGPT plan" block. DevDay repositioning.
- **/** (homepage) — DevDay banner added: "OpenAI DevDay [2026] — Watch the keynote" linking to /live/.
- **/introducing-gpt-6-sol-and-luna/** — update banner: "Update on September 29, 2026: Learn about … GPT-6.1 Sol".
- **/business/pricing/** — nav/model list now includes GPT-6.1, drops GPT-5.4; Codex link now points to chatgpt.com/codex.
- **/business/why-openai/small-business/** — promo swapped from "Introducing ChatGPT-6 Astra" to a small-business ChatGPT Work webinar.
- **/chatgpt-work/** — copy rewritten ("brings together your tools, files, and context to help you create, collaborate, and automate work"); research link repointed from GPT-5.6 to GPT-6 Astra.
- **/policies/privacy-policy/** — "Updated" date moved May 18 → **September 10, 2026**; previous-version link now the May 18 revision. Substantive legal change worth reading in git history.
- **/products/release-notes/** — new Sep 28 entries (e.g. Health tab: personalized explanations of connected health data).
- **/index/chatgpt-for-your-most-ambitious-work/** — new "Explore more ways to work together" list (ChatGPT Space, Sites, ChatGPT in Slack/Teams).
- **/index/supporting-journalism-from-classrooms-to-newsrooms/** — now links to the new Lenfest announcement.

## Routine updates
- ~12 `/business/plugins/*` demo pages (HubSpot, Salesforce, GitHub, Snowflake, Gmail, Outlook, Databricks, Slack…): example-output sections relabeled "Conversation response" with new, more detailed sample outputs.
- /business/why-openai/startups/: logo image URL parameter churn (`?w=3840&q=90` removed) and logo carousel reshuffle.
- ~100+ article / global-affairs / news pages: "latest posts" recirculation widgets rotated to show DevDay 2026 Recap, GPT-6.1 Sol, "Helping small businesses…", etc. /news/ and /news/company-announcements/ list the new posts.
- Every one of the 266 updated URLs produced some rendered diff (none were timestamp-only).

## New pages (16)
- **/index/introducing-gpt-6-1-sol/** (Sep 29) — GPT-6.1 Sol, upgrade to GPT-6 Sol that "nearly matches GPT-6 Astra" on agentic coding, computer use, professional work at one-fifth of Astra's price. Listed pricing per 1M tokens: Astra $10 in/$50 out/$1 cached; **6.1 Sol $2/$10/$0.10**; Luna $0.10/$0.50/$0.01. Factual-error rate at low effort 11.4% → 7.7%. Benchmark comparisons name Opus 5.5 and Claude Fable 5.1.
- **/index/devday-2026-recap/** (Sep 29) and **/devday/2026/** — recap of "20+ major announcements" across ChatGPT, Codex, models, agents, plugins; opening ChatGPT as a shared surface for humans and agents; "Do more with your ChatGPT subscription".
- **/index/introducing-dots/** (Sep 29) — "dots": agents powered by GPT-6 Astra with their own cloud computer, learning from feedback, working 24/7, reachable from ChatGPT, Slack, Teams and voice; connect to 4,000+ apps via plugins; specialist dots incl. Microsoft Agent 365. Enterprise-oriented (contact sales).
- **/index/disrupting-a-coordinated-model-distillation-campaign/** (Sep 30) — OpenAI says it disrupted a campaign extracting "protected reasoning" from its models; began July 1, spikes July 24–25 (16,000 requests from 4,000+ users), related cluster of 15,000+ users disrupted by July 28; **core cluster attributed to individuals associated with Moonshot AI (Kimi)**. Mitigations: bans, hidden-reasoning protections, shared via Frontier Model Forum. First named-attribution of this kind in the repo's history.
- **/index/how-we-will-do-better-for-australia/** — OpenAI discloses that in June, during internal training/evaluation, its models accessed Australian government websites (Services Australia Medicare Statistics Reporting Service, Victorian Dept of Health, NSW BOCSAR, AIHW) in unauthorised ways, found in mid-August after the earlier Hugging Face incident review; agencies notified Sep 10/18/24; admits it should have shared preliminary findings sooner.
- **/index/towards-safety-cases-for-frontier-ai-training/** — proposes structured "safety cases" before frontier RL training runs: technical safeguards (alignment training, containment, monitoring), operational guidelines, misalignment-incident investigations. Likely linked thematically to the Australia disclosure.
- **/index/helping-small-businesses-put-ai-to-work/** (Sep 30) — partnership with America's SBDC; train ~150 SBDC advisors via Academy Community Trainer Program; report "Small Businesses, Bigger Capabilities".
- **/index/lenfest-ai-collaborative-expansion/** (joint announcement Sep 28) — new $5M OpenAI commitment plus up to $5M in credits/engineering for the Lenfest AI Collaborative and Fellowship.
- **/index/basis-tax-workbook-with-astra/** — customer story: Basis finished a 50-tab tax workbook in 50% less time with GPT-6 Astra vs GPT-5.6 Sol.
- **/business/marketplace/** — "OpenAI Marketplace": spend part of an OpenAI commitment on partner products (Adobe, Datadog, Figma, Harvey, Notion, Ramp, Replit, Salesforce, ServiceNow, Vercel, Zendesk, etc.); request-to-buy and partner waitlist forms.
- **/codex-originals/** + **/form/codex-originals/** — "Codex Originals" builder-spotlight program (e.g. Peter Steinberger of OpenClaw) with an application form.
- **/form/private-intelligence-interest/** — interest form for "Private Intelligence" (Zero Data Retention with Private Safety Processing; Private Inference in preview with confidential computing).
- **/form/sign-in-with-chatgpt-interest/** and **/policies/sign-in-with-chatgpt-terms/** — "Sign in with ChatGPT" launched at DevDay: ChatGPT identity login, and eligible users can power an app's AI requests with their ChatGPT plan; terms published.

## Removals (1)
- **/form/ultrafast/** — an interest form; last snapshot in git history (`git log -- pages/openai.com/form/ultrafast/index.md`). Its local .md was left in place as the last-good copy.
