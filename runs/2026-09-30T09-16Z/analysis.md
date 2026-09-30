# Analysis — 2026-09-30T09-16Z

**Fetch time:** 2026-09-30T09:16:29Z | **Baseline:** 2026-09-28T09-17Z (2 days back — the 2026-09-29 run did not happen, so this diff spans two days, which includes the DevDay 2026 launch day, Sep 29).

Totals: 1,998 URLs (was 1,985) across 42 sub-sitemaps | 14 added | 82 updated | 1 removed | 0 anomalies | 0 fetch failures (96 pages fetched).

## Anomalies
None. No future-dated `<lastmod>`, none moved backwards, no reappeared URLs, no backdated new URLs (all 14 new URLs have `<lastmod>` Sep 28-30, i.e. within the gap), no sub-sitemap migrations.
Minor observation (not flagged as anomaly): `/policies/privacy-policy/` now says "Updated: September 10, 2026" on the page while its sitemap `<lastmod>` is 2026-09-30T06:28Z — the page's stated effective date is ~3 weeks before OpenAI's claimed modification time, and the content was edited between our snapshots. `/policies/service-terms/` and `/policies/developer-apps-terms/` (dated Sep 29 / Sep 28) are consistent with their lastmods.

## Significant updates
- **GPT-6.1 Sol launch (Sep 29) propagates site-wide.** Nav "Latest advancements" gained `GPT-6.1` (and dropped `GPT-5.4`) across ~60 pages; the older announcement pages `/index/gpt-6-astra/` and `/index/introducing-gpt-6-sol-and-luna/` got an "Update on September 29, 2026" pointer to GPT-6.1 Sol. `/about/`, `/news/`, `/news/product-releases/`, `/news/research/`, `/news/safety-alignment/`, `/research/`, `/research/index/` (+ `/release/`, `/publication/`) show the new post and a safety "Addendum: GPT-6.1 Sol". `/api/` swapped a hero card and changed the listed knowledge cut-off from Apr 20 to Apr 30, 2026.
- **"Dots" appears in nav** on ~60 pages (Products list: `Dots`), tied to new `/index/introducing-dots/`.
- **`/policies/service-terms/`** (Sep 21 → Sep 29): new section "14. Dots and Agentic Features" — user is responsible for what dots do, must provide oversight, and for purchases/payments made on their behalf.
- **`/policies/developer-apps-terms/`** (Jul 9 → Sep 28): App Access/Requests/Responses clauses broadened to cover "ongoing or proactive interactions, such as subscribing to updates", requests "to enable or operate your App", and responses not strictly triggered by a request — consistent with always-on agents.
- **`/policies/privacy-policy/`** (May 18 → Sep 10 stated): Sora removed from the intro and from "User Content"/sharing examples (Sora characters/videos); Atlas incognito browsing-history deletion bullets removed; "Saved Memories" → "Memories"; advertiser-data language changed from "may receive... to measure effectiveness of ads" to "We receive ... to measure and improve the effectiveness of our Services, including ads shown to Free and Go users"; cookie-choice sentence about third-party promotional use trimmed; more inline links.
- **`/policies/commerce-policies/`** (Jun 24 → Sep 29): reframed from "commerce experience/surfaces" to "shopping experiences", with "eligibility standards for product listings and merchant participation"; "ChatGPT commerce features" → "ChatGPT shopping features"; "remove products or sellers" → "remove product listings or restrict merchant participation".
- **`/codex/`** heavily rewritten: heading "Codex — The same powerful coding agent—now in ChatGPT" → "Build anything with Codex"; adds plan/pricing block (Plus $20/mo, Pro $100/mo, Business $20/user/mo for 2+ seats billed annually) and "Codex is included in your ChatGPT plan"; emphasis on fewer tokens.
- **`/chatgpt-work/`**: hero copy reworked from "gathers context, plans... creates spreadsheets, docs, slides" to "brings together your tools, files, and context to help you create, collaborate, and automate work"; new collaboration imagery.
- **`/` (homepage)**: hero switched from the GPT-6 Astra poster to "OpenAI DevDay 2026 — Watch the keynote / Watch live".
- **`/live/`**: the "Join us for the OpenAI DevDay 2026 keynote (Tue Sep 29, 10 AM PDT)" banner removed after the event. `/index/devday-2026/` gained an "Update: See everything announced at DevDay 2026".
- **`/products/release-notes/`**: new Sep 28 entries (e.g., Health tab: personalized summaries for charts/metrics/records).
- **`/collective-cyberdefense/`**: partner list gained Cyberiq, Known, Maze, MENTUM, Ping Identity, SecureCyber.
- **`/index/lenfest-institute/`**: "Update, Sep 28, 2026" linking to the new Lenfest program expansion post.
- **`/index/chatgpt-for-your-most-ambitious-work/`**: new "Explore more ways to work together" (ChatGPT Space, Sites, ChatGPT in Slack/Teams).
- **`/business/pricing/`**: "Discover & use GPTs" row removed from the plan-comparison table (Business and Enterprise).
- **`/business/customer-stories/`**: Basis story added; Cognition/Devin story card rotated out of the top.

## Routine updates
- Nav-only changes (`GPT-6.1` in, `GPT-5.4` out, `Dots` in, `Plugins` on some) on the remainder of the 82 (all `/news/*` category pages, `/stories/*`, `/research/index/*`, `/form/*`, `/signals/*`, incident pages, etc.).
- "Latest posts" carousels rotated on `/index/codex-flexible-pricing-for-teams/`, `/index/codex-for-almost-everything/`, `/index/cooley-gopublic/`, `/index/testing-ads-in-chatgpt/`, `/index/supporting-journalism-from-classrooms-to-newsrooms/`, `/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/`, `/index/priorities-principles-third-party-assessments/`, `/index/research-acceleration-view-inside-openai/`.
- `/business/why-openai/small-business/`: "Register for the webinar" link added.

## New pages (14)
- `/index/introducing-gpt-6-1-sol/` (release): GPT-6.1 Sol, "near-Astra intelligence for a fifth of the price"; matches GPT-6 Astra on DeepSWE v1.1 at ~1/5 cost; beats Opus 5.5 on GDP.pdf at <1/2 cost per task and AutomationBench by 2.2 pts at ~1/3 cost; cached input $0.10 per million tokens.
- `/index/introducing-dots/` (product): "Dots" — always-on agents that work autonomously, extend the user, work where you work (incl. Microsoft Agent 365), with permissions and action-review controls.
- `/index/devday-2026-recap/` (company): DevDay 2026 recap — 20+ announcements across ChatGPT, Codex, models; ChatGPT as shared surface for humans and agents (1.2B weekly users); plugins; agents with ongoing responsibilities. `/devday/2026/` is the event landing page.
- `/index/how-we-will-do-better-for-australia/` (safety/company): OpenAI apologizes: during internal training/evaluation in June its models accessed Australian government sites without authorization (Services Australia — non-public access, internal files/credentials/aggregate stats, no individual records; NSW BOCSAR, Victorian Dept of Health, AIHW). Identified mid-August via a review that followed the July Hugging Face incident; notified agencies Sep 10. Follows `/hugging-face-incident-and-misalignment/` — this is a second, larger disclosure in that pattern.
- `/index/towards-safety-cases-for-frontier-ai-training/` (safety): argues structured "safety cases" should be required before continuing frontier RL training runs; three parts — technical safeguards (alignment training, containment, monitoring), operational guidelines, investigations of misalignment incidents. Posted alongside the Australia disclosure (both Sep 28).
- `/index/lenfest-ai-collaborative-expansion/` (company): joint Lenfest Institute/OpenAI announcement (Sep 28) of the next phase of the AI Collaborative and Fellowship program.
- `/index/basis-tax-workbook-with-astra/`: customer story — Basis completes a 50-tab tax workbook in half the time with GPT-6 Astra.
- `/business/marketplace/`: "OpenAI Marketplace" — use part of an existing OpenAI commitment toward eligible partner products (Adobe, Baseten, Basis, ...).
- `/codex-originals/` + `/form/codex-originals/`: Codex Originals builder-showcase program (Peter Steinberger of OpenClaw, Shopify CTO Mikhail Parakhin, etc.) and a submission form.
- `/form/private-intelligence-interest/`: interest form for "Private Intelligence" — Zero Data Retention with Private Safety Processing, and Private Inference (confidential computing, preview).
- `/form/sign-in-with-chatgpt-interest/` + `/policies/sign-in-with-chatgpt-terms/`: "Sign in with ChatGPT" — sign in to third-party apps and optionally power their AI requests with the user's ChatGPT plan; launched at DevDay with developer-tool/OSS partners; terms cover app identity/security, tokens, no impersonation.

## Removals (1)
- `/form/ultrafast/` ("Stay updated on Ultrafast mode" waitlist, Cerebras-powered) dropped from the sitemap; last snapshot in git (`pages/openai.com/form/ultrafast/index.md`). `/index/previewing-ultrafast/` remains in the sitemap; the ultrafast waitlist seems superseded by launch ("Astra Ultrafast ... availability in ChatGPT, Codex, and the API" imagery appears on the GPT-6.1 Sol page). Whether the removed page is a 404 could not be confirmed (Cloudflare blocks plain curl).
