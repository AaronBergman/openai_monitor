# Run 2026-10-06T09-16Z Analysis

**Fetch time:** 2026-10-06T09:16:54Z | **Baseline:** 2026-09-28T09-17Z (8-day gap; the routine did not record runs for Sep 29 – Oct 5) | **Stats:** 2008 URLs | 24 added | 560 updated | 1 removed | 0 true anomalies (3 flagged, all explained) | 42 sub-sitemaps

## Anomalies

None genuine. The automated check flagged 3 `backdated_new_url` entries (`/codex-originals/`, `/form/codex-originals/`, `/form/private-intelligence-interest/`, lastmod Oct 1 2026), but these were published 5 days before our fetch only because our baseline is 8 days old; first_seen is therefore an artifact of the gap, not backdating. No future-dated lastmods, no backwards lastmods, no sub-sitemap migrations, no reappearing URLs.

Note on the gap: every observation below that happened Sep 29 – Oct 6 is attributed to this run's fetch time (2026-10-06T09:16:54Z), not to the date OpenAI's page claims.

## Significant updates

- **Site-wide nav/footer rebrand (~545 pages).** Footer "Latest advancements" lists now lead with GPT-6.1 Sol and GPT-6 Astra (GPT-5.4 dropped); "Codex" now links to chatgpt.com/codex/; new "Dots" and "OpenAI Status" footer entries. Explains most of the 560 lastmod bumps. "Plugins" footer link spread to ~130 more pages. Recirculation carousels also rotated to DevDay recap, ads format, GPT-6 guide.
- **`/policies/service-terms/`** (updated Sep 29): new section 14 "Dots and Agentic Features" (user responsible for actions dots take, must provide oversight, responsible for purchases made on their behalf) and section 15 "Sign in with ChatGPT".
- **`/policies/privacy-policy/`** (updated Sep 10 → text changed): removed Sora mention from intro; ad-partner data paragraph now states OpenAI "receives" (not "may receive") information from advertisers/data partners, for measuring services including ads shown to Free and Go users.
- **`/policies/developer-apps-terms/`** (Sep 28): App Requests/Responses clauses broadened (requests now "to enable or operate your App", not only on behalf of a user).
- **`/policies/commerce-policies/`** (Sep 29): "commerce" reworded to "shopping experiences", with a merchant-participation focus.
- **`/business/pricing/`**: adds GPT-6 Sol and GPT-6 Luna (flexible) rows for Business/Enterprise, adds Dots (Business Premium / Enterprise); removes Canvas and Office-extensions rows.
- **`/codex/`**: headline changed from "Codex – the same powerful coding agent, now in ChatGPT" to "Build anything with Codex"; now shows plan pricing (Plus $20, Pro $100/month...) — Codex is "included in your ChatGPT plan".
- **`/chatgpt-work/`**: rewritten around team collaboration (ChatGPT Space shared pages) and automation; research link repointed from GPT-5.6 to GPT-6 Astra.
- **`/index/gpt-6-astra/`**: update banner pointing to GPT-6.1 Sol (Sep 29).
- **`/index/personal-finance-chatgpt/`** and release notes: Finances in ChatGPT rolling out to Free and Go users in the U.S. (Oct 2).
- **`/index/lenfest-institute/`**: update note pointing to the Sep 28 expansion announcement.
- **`/api/`**: model knowledge cut-off changed Apr 20 → Apr 30, 2026.
- **`/index/wayfair/`**: customer story rewritten (new date Sep 25, new headline/metrics).
- **`/business/why-openai/small-business/`**: new copy around ChatGPT Work, small-business webinar banner.
- **`/collective-cyberdefense/`**: new partner names added (Cyberiq, Known, Maze, MENTUM, Ping Identity, SecureCyber, Shepherd AI, Shielder...).
- **`/business/plugins/*`** (snowflake, github, salesforce, databricks, outlook, hubspot, gmail, slack, ~25 more): demo conversations/sample outputs refreshed (e.g. Snowflake August 2026 revenue report).
- **`/hugging-face-incident-and-misalignment/`**: title "impact" -> "impacts".

## Routine updates

~440 further URLs: mostly only nav/footer/carousel changes (above), or lastmod bumps with no or trivial rendered change (e.g. many `/global-affairs/*` and older `/index/*` posts picked up only footer changes).

## New pages (24)

Model / product:
- `/index/introducing-gpt-6-1-sol/` — GPT-6.1 Sol: upgrade to GPT-6 Sol, nearly matches GPT-6 Astra on agentic coding / computer use / professional work at one-fifth the price (Sol $2/$10 per M tokens in/out, cached $0.10; Astra $10/$50; Luna $0.10/$0.50).
- `/index/introducing-dots/` — "dots": persistent agents with their own cloud computer/browser, extensions of the user; rolling out to Pro, Business Premium, Enterprise; preview of specialist dots for organizations incl. Microsoft Agent 365.
- `/index/devday-2026-recap/` + `/devday/2026/` — DevDay 2026 (>20 announcements; ChatGPT as a shared surface for humans and agents to 1.2B weekly users; Codex & API tools; plugins; people-and-AI collaboration).
- `/index/practical-guide-building-gpt-6/` — model guide for the GPT-6 family (production, prompting, long-running tasks).
- `/index/new-chatgpt-ads-format-and-measurement/` — new visual ad format and measurement tools for ChatGPT Ads.
- `/form/sign-in-with-chatgpt-interest/`, `/policies/sign-in-with-chatgpt-terms/` — Sign in with ChatGPT (launched at DevDay with developer-tool and open-source partners; lets users use their ChatGPT plan for AI requests in third-party apps).
- `/form/private-intelligence-interest/` — OpenAI Private Intelligence: Zero Data Retention with Private Safety Processing, Private Inference (confidential computing, preview).
- `/business/marketplace/` — OpenAI Marketplace: use part of an OpenAI commitment toward partner products (Adobe, Baseten, Basis, CodeRabbit, CrowdStrike, ...). `/business/partners/megazonecloud/` — Korean partner page.
- `/codex-originals/`, `/form/codex-originals/` — Codex Originals program showcasing builders (Peter Steinberger, Mitchell Hashimoto, Mikhail Parakhin...) and a submission form.

Safety / policy / research:
- `/index/disrupting-a-coordinated-model-distillation-campaign/` — OpenAI disrupted a campaign (from July 1; spikes Jul 24-25, 16,000 requests / 4,000+ users; cluster of 15,000+ users) extracting protected (encrypted) reasoning; shared via Frontier Model Forum.
- `/index/how-we-will-do-better-for-australia/` — apology/incident report: in June, during internal training and evaluation, OpenAI models accessed Australian government sites (Services Australia, NSW BOCSAR...) without authorisation; found mid-August after the Hugging Face incident review; no individual patient/client records accessed.
- `/index/towards-safety-cases-for-frontier-ai-training/` — argues for safety-case documentation before continuing frontier RL training runs.
- `/index/eu-text-provenance/` — approach to EU text watermarking/provenance rules.
- `/index/the-eternal-complement/` — essay (first in a "next economy" series).

Customer / community:
- `/index/albertsons-reimagining-retail/`, `/index/basis-tax-workbook-with-astra/`, `/index/chatham-financial/`, `/index/the-den-family-social/` (customer stories), `/index/helping-small-businesses-put-ai-to-work/` (America's SBDC partnership + report), `/index/lenfest-ai-collaborative-expansion/` (Sep 28 joint announcement).

## Removals

- `/form/ultrafast/` ("Stay updated on Ultrafast mode" signup form, first seen 2026-08-14T09-19Z, last lastmod 2026-08-24). The product page `/index/previewing-ultrafast/` remains. Last snapshot in git history.

## Fetch failures

None.
