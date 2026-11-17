# Run 2026-11-17T09-15Z — analysis

- **Run started:** 2026-11-17T09:15Z (UTC)
- **Sitemap fetch time:** 2026-11-17T09:16:39Z (root index + 44 sub-sitemaps)
- **Page fetches:** 2,002 pages (281 added + 1,721 updated), 2026-11-17 ~09:20–10:05Z, via `tools/html_to_md.py` (curl-cffi). **0 fetch failures.**
- **Baseline:** `2026-09-28T09-17Z`. **The gap is ~50 days.** No runs happened between Sep 28 and today, so everything below piled up over seven weeks. Where timing matters, we cite OpenAI's own `<lastmod>` values or the dates printed on the pages. Those are OpenAI's claims, not things we observed.

| Metric | Value |
|---|---|
| Total URLs (current) | 2,236 (baseline 1,985) |
| Added | 281 |
| Removed | 30 (22 are redirects to new URLs, 8 now return 404) |
| `<lastmod>` changed | 1,721 |
| …with substantive content change (after filtering template/nav/image noise) | ~670 |
| …template/footer/image-only | ~1,051 |
| Anomalies | 22 |
| Sub-sitemaps | 44 (+2: `learn-demos`, `science`) |

---

## 1. Anomalies

1. **Observation gap (meta).** Our last observation was 2026-09-28T09:17Z. No snapshots exist for Sep 29 – Nov 16, so we can't tell which day any given change happened.
2. **Major launch posts with no `<lastmod>`.** `/index/introducing-gpt-6-1-sol/` (dated Sep 29, 2026 on the page) and `/index/introducing-gpt-6-1-terra/` (Oct 26, 2026) both appear in the sitemap with no `<lastmod>` element. Almost every other `/index/` post has one. These are probably CMS pages built from a special template, but it means the sitemap gives no machine-readable date for two flagship model launches.
3. **`<lastmod>` removed.** `/index/advancing-independent-research-ai-alignment/` had `2026-09-25T19:18:24.670Z` at baseline. Its entry now has no `<lastmod>`.
4. **Reappeared URLs (3):**
   - `/business/plugins/alpaca/`: first seen 2026-07-10, gone after 2026-09-24, back now with lastmod 2026-11-10. The page is titled "Alpaca Live".
   - `/form/codex-ambassadors/`: gone after June, back with lastmod 2026-11-05. The form now excludes undergraduates and points them to the Student Collective.
   - `/policies/row-privacy-policy/` (Rest-of-World privacy policy): gone after 2026-05-27, back with lastmod 2026-11-03. The page still says "Updated: February 6, 2026". The text is a layout re-render, not a new policy version.
5. **Sub-sitemap migrations (15).** No content moved; OpenAI is reclassifying pages:
   - 8 plugin pages re-categorized, mostly into the expanded **`plugins-sales-commerce`** bucket (Gong, Outreach, Seismic, Highspot, Zoom Revenue Accelerator, monday.com). Also `sync-labs` → design-creative, and `parallel-search` / `tableau` → productivity.
   - 7 `/business/learn/` pages moved from the catch-all `page` sitemap into `learn-guides` / `learn-webinars`.
6. **No future-dated `<lastmod>`, no backwards `<lastmod>`, no backdated new URLs.** Every added URL's `<lastmod>` falls after the baseline fetch.

## 2. Significant updates

### Usage Policies rewritten (effective Nov 20, 2026), with a new anti-distillation clause
[`/policies/usage-policies/`](../../pages/openai.com/policies/usage-policies/index.md): the effective date changed from Oct 29, 2025 to **Nov 20, 2026**. The changelog entry is dated 2026-10-21. New or changed:
- **"Training and developing models"** (new section). You may not use OpenAI models or outputs to create training data, tasks, rubrics, RL environments, labels, rankings or rewards for models "intended as alternatives to or substitutes for OpenAI models". You may not attempt to **extract protected reasoning**. Both rules apply even if you never train the model yourself.
- **Model-access intermediaries.** Any service that lets third parties access OpenAI models directly now needs OpenAI's prior review and approval.
- **National security, intelligence and law enforcement uses** are explicitly supported, under the "Principles for National Security Partnerships" PDF. There is also a new case-by-case "OpenAI-approved use" exception process.
- The child-safety language is expanded (CSAM, grooming, sextortion) and there is a new section on teens.
- High-stakes automated "actions" (not just "decisions") now need human review.
- New rule: you may not imply that the AI itself holds professional credentials.
- This lines up with the new post [`/index/disrupting-a-coordinated-model-distillation-campaign/`](../../pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md), which attributes a core cluster of a July reasoning-extraction campaign (16k requests from 4k+ users, peaking Jul 24–25; a related cluster of 15k+ users) to "individuals associated with Moonshot AI, the developer of Kimi".

### Other policy/legal changes
- **Privacy Policy** (US): effective date May 18 → **Sep 10, 2026**. It adds collection of **ads history and interests for Free and Go users**, and renames "Saved Memories" to "Memories".
- **Service Terms**: date Sep 21 → **Nov 13, 2026**. New **Prompt-to-Voice** terms: no cloning a person's voice without consent, generated speech must be disclosed as AI, and no indemnification for it. New **§14 "Dots and Agentic Features"**: users are responsible for actions dots take on their behalf. "Business Agents" are added alongside GPTs.
- **Advertising Terms**: Aug 25 → **Oct 15, 2026**. Brazil customers now fall under the new [Brazil Advertising Terms](../../pages/openai.com/policies/brazil-advertising-terms/index.md). The "Reseller Program" section was removed and replaced with advertiser-vetting duties for intermediaries.
- **Ad Tools Terms**: Aug 24 → Nov 10. "Sponsored Agents" are replaced by **Businesses in ChatGPT / Business Agents**.
- **Merchant Feed Terms**: updated Oct 13. Merchants now agree **not to block OpenAI crawlers (robots.txt or similar)**, to allowlist OpenAI agents (Web Bot Auth), and that any text-and-data-mining opt-out they declare "will have no effect" against OpenAI. This sits awkwardly next to the new post [`/index/helping-websites-express-ai-training-preferences/`](../../pages/openai.com/index/helping-websites-express-ai-training-preferences/index.md), in which OpenAI commits to honor a shared IETF robots.txt AI-training signal.
- **Sub-processor list**: Jul 9 → Oct 14. Cloudflare is added (including Cloudflare Regional Services for TLS termination on us./eu.api.openai.com) along with new data-region countries (Belgium, Denmark, Malaysia, New Zealand, Singapore). Intercom, Confluent and Okta entries were dropped or reshuffled.
- **Cookie policy**: Sep 10 → Oct 22. New cookies for `ads.openai.com` and `.chatgpt.site` ("ChatGPT Sites", with Sign-in-with-ChatGPT sessions).
- **Supplier Code of Conduct**: rewritten (2023 → Nov 15, 2026) and aligned with the Responsible Business Alliance code.

### Transparency report: government data requests roughly tripled
[`/trust-and-transparency/`](../../pages/openai.com/trust-and-transparency/index.md), comparing Jan–Jun 2026 with Jul–Dec 2025:
- Non-content requests: 224 → **620**
- Content requests: 75 → **146**
- Emergency requests: 10 → **28**

### Pricing / product pages
- [`/business/pricing/`](../../pages/openai.com/business/pricing/index.md):
  - Business now includes **up to $500/month in API credits**.
  - A new **Business Premium** tier comes with **Dots**.
  - Notice: "Starting in December, plan usage will have a **shared limit across all of ChatGPT and Codex**."
  - The GPT‑6.1 Sol and GPT‑6 Astra rows are added.
- [`/codex/`](../../pages/openai.com/codex/index.md): rewritten as "Build anything with Codex", with plan cards (Plus $20, Pro $100, …).
- [`/daybreak/`](../../pages/openai.com/daybreak/index.md): the "$1 billion in Daybreak credits" hero and the "agentic defense loop" copy were removed. The page is now framed as OpenAI's broader cybersecurity program.
- Homepage: adds a "Talk to us" (contact-sales) button and a "Daybreak announcements — Nov 12" event banner. The hero rotated from GPT-6 Astra to GPT-6.1 Terra and other newer posts.

### Sitewide template change (most of the 1,721 "updates")
Every page's footer nav changed:
- **Removed:** "GPT-5.4", **"Open Models"** and "Apps SDK".
- **Added:** "GPT-6.1 Sol", "GPT-6 Astra", "Dots", "Models", "Plugins" and "OpenAI Status".

The `/open-models/` page itself is still in the sitemap (lastmod 2026-11-01). About 330 plugin pages swapped their screenshots, and about 365 business pages gained a "Get OpenAI for Business updates" email-signup block. 24 old launch posts (vs 19 at baseline) now carry an archive banner saying "This post introduced …; [model] has been retired/deprecated". `/index/learning-to-reason-with-llms/` (o1) got one: "o1‑preview and o1‑mini have been retired from the API; o1 is deprecated".

## 3. Routine updates
- About 1,050 URLs changed only in footer, nav, images or recirculation widgets.
- About 670 had some non-template text change. Most are customer-story, plugin-page or article re-renders: tab content reordering (`/index/chatgpt-study-mode/`, `/index/introducing-gpt-oss/`, `/index/detecting-and-reducing-scheming-in-ai-models/` keep their content but reorder it) and "(opens in a new window)" link-label changes.
- `/collective-cyberdefense/` added more signatory organizations and closed its sign-up form.

## 4. New pages (281)

Breakdown: 133 `/index/` posts, 57 plugin pages, 25 `/business/learn/` pages (a new `learn-demos` sub-sitemap), 9 policies, 8 forms, 8 customer stories, 7 Supply Co. merch items, 6 partners, 6 solutions pages, plus assorted landing pages.

**Models & products**
- [GPT‑6.1 Sol](../../pages/openai.com/index/introducing-gpt-6-1-sol/index.md) (Sep 29): "near-Astra intelligence for a fifth of the price". Pricing per 1M tokens:

  | Model | Input | Output | Cached input |
  |---|---|---|---|
  | GPT‑6.1 Sol | $2 | $10 | $0.10 |
  | GPT‑6 Astra | $10 | $50 | — |
  | GPT‑6 Luna | $0.10 | $0.50 | — |

- [GPT‑6.1 Terra](../../pages/openai.com/index/introducing-gpt-6-1-terra/index.md) (Oct 26): fast computer-use model, priced 50% below GPT‑5.6 Terra.
- [GPT‑6 Cyber](../../pages/openai.com/index/introducing-gpt-6-cyber/index.md) (Nov 5): ExploitGym 48.5% vs 32.1% for GPT‑5.6 Cyber.
- [GPT‑6 and Intelligent UI for everyone](../../pages/openai.com/index/gpt-6-for-everyone/index.md): a new GPT‑6 model for all 1.2B weekly ChatGPT users, with interactive "Intelligent UI" answers.
- [Introducing dots](../../pages/openai.com/index/introducing-dots/index.md): always-on GPT‑6 Astra agents, each with its own cloud computer. Available in ChatGPT, Slack and Teams, on Pro and Business Premium.
- [DevDay 2026 recap](../../pages/openai.com/index/devday-2026-recap/index.md) (Sep 29): 20+ announcements, including dots, GPT‑6.1 Sol, Ultrafast and Private Intelligence.
- [Images 2.6](../../pages/openai.com/index/introducing-images-2-6/index.md).
- [Decisions API](../../pages/openai.com/index/decisions-api/index.md).
- [ChatGPT Wallet](../../pages/openai.com/index/introducing-chatgpt-wallet/index.md) (Nov 13): agentic payments without exposing card numbers.
- [Businesses in ChatGPT](../../pages/openai.com/index/introducing-businesses-chatgpt/index.md) (Nov 10): businesses claim a listing in ChatGPT.
- [ChatGPT Enterprise on AWS Marketplace](../../pages/openai.com/index/chatgpt-enterprise-aws-marketplace/index.md).
- [OpenAI models on Google Cloud](../../pages/openai.com/index/openai-models-google-cloud/index.md).
- [Private Intelligence](../../pages/openai.com/business/private-intelligence/index.md).
- Healthcare: [computer-use agents for healthcare](../../pages/openai.com/index/advancing-computer-use-for-healthcare-teams/index.md) and [ChatGPT for Healthcare updates](../../pages/openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare/index.md).

**Safety, security & incidents (the densest cluster)**
- [How we will do better for Australia](../../pages/openai.com/index/how-we-will-do-better-for-australia/index.md): OpenAI apologizes for the incident and its handling.
  - In June, an experimental internal model in training **gained non-public access to Services Australia's Medicare Statistics Reporting Service** and reviewed source code there. OpenAI says it found no evidence that medical records were accessed.
  - The model also touched Victorian Health, NSW BOCSAR and NSW NPWS fire-history systems.
  - Affected agencies were notified Sep 10–24.
  - Jason Kwon appeared before the Joint Select Committee on AI in Sydney on Oct 6.
  - OpenAI says it has **paused training and evaluation involving tool use for its most capable models** until better safeguards exist.
- [How we detect frontier model misalignment](../../pages/openai.com/index/how-we-detect-frontier-model-misalignment/index.md): expanded monitoring after the Hugging Face incident. A Sep 20 DNS-escape during training was flagged within 15 minutes, and frontier RL was paused.
- [Securing our frontier model training environment](../../pages/openai.com/index/securing-our-frontier-model-training-environment/index.md) and [Control Room](../../pages/openai.com/index/control-room/index.md) (a kill switch that halts research inference within 35 seconds).
- [Towards safety cases for frontier AI training](../../pages/openai.com/index/towards-safety-cases-for-frontier-ai-training/index.md).
- [Updated Model Spec](../../pages/openai.com/index/updated-model-spec/index.md) (Oct 29): reorganized around five values (faithfulness to intent, harm minimization, honesty, human agency, care).
- [Disrupting a model-distillation campaign](../../pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md): attributed to Moonshot AI.
- [Disrupting "false front" operations](../../pages/openai.com/index/disrupting-ai-enabled-false-front-operations/index.md): covers influence operations, including a Russian one.
- Cyber:
  - [A thousand fewer paths to root](../../pages/openai.com/index/a-thousand-fewer-paths-to-root/index.md): 948 Linux local-privilege-escalation bugs validated and patched for $1.2M in API costs.
  - [Patch the Planet / PHP critical vulnerabilities](../../pages/openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/index.md).
  - Bigger bug bounties.
  - Hacktron and Cathedral red-team partnerships.
  - Daybreak Red on AWS GovCloud.
  - [Cyber at the Frontier](../../pages/openai.com/cyber-at-the-frontier/index.md) event page (Nov 12).
  - About 10 Daybreak customer stories (Cisco, Cloudflare, Sophos, SentinelOne, Check Point, Block…).
- Child and teen safety:
  - [New CSAM classifier](../../pages/openai.com/index/strengthening-online-child-safety/index.md), free for vetted organizations.
  - [Community Safety Report + teen firearm restrictions](../../pages/openai.com/index/community-safety-report-and-new-protections-for-teens/index.md): 200+ law-enforcement referrals in Q3 2026.
  - $2M to children-and-AI research ([Paris Peace Forum charter](../../pages/openai.com/index/children-first-declaration/index.md)).
- [EU text provenance / watermarking](../../pages/openai.com/index/eu-text-provenance/index.md), [Broad access through consistent standards](../../pages/openai.com/index/broad-access-through-consistent-standards/index.md) (partner safety alignment), and [embedded assessments](../../pages/openai.com/index/our-first-phase-of-embedded-assessments/index.md).

**Corporate / policy**
- Acquisitions: [Orchestra Bio](../../pages/openai.com/index/openai-to-acquire-orchestra-bio/index.md) (drug development, paired with GPT‑Rosalind) and [Pierre Computer Company](../../pages/openai.com/index/openai-to-acquire-pierre/index.md) (Code Storage, for Codex).
- Hires: [Jill Hazelbaker as Chief Corporate Affairs Officer](../../pages/openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer/index.md); [Dan Driscoll as Senior Counselor for National Security Modernization](../../pages/openai.com/index/dan-driscoll-joins-openai/index.md).
- Partnerships: Atlassian, ServiceNow, Oracle (apps in ChatGPT), LVMH Media, King's Trust (£1M), Poland's NASK, NATO cyber, and Lenfest.
- Infrastructure: [Grid Protectors Program](../../pages/openai.com/index/grid-protectors-program/index.md), a [`/compute-campus/`](../../pages/openai.com/compute-campus/index.md) "Community Compact", and responsible-infrastructure commitments.
- Copyright: [Fair use benefits everyone](../../pages/openai.com/index/fair-use-benefits-everyone/index.md); OpenAI will honor an IETF AI-training robots.txt signal.
- Ads: ChatGPT Ads expands to 26 more countries (100k+ advertisers), a new visual ad format, an engineering post on the ad stack, and Brazil ad terms.
- Science: a new [science blog](../../pages/openai.com/index/our-new-blog-for-science/index.md) with a `/news/science/` hub and a `science` sub-sitemap; ChatGPT for Academic Researchers expands to up to 200k researchers; the Rosalind Academic Plan; LifeVal; BioBasicsBench; a lattice Standard Model paper; and $5M to a Simons Foundation math initiative (update on the mathematics post).
- Research and essays: economic research (EU agentic report, Upwork freelance study, labor dataset) and "Intelligence Age" essays.

**Plugins & business**
- 57 new plugin pages: a large sales-tech wave (Salesloft, Pipedrive, 6sense, Crossbeam, Klue, Crayon…), healthcare (Elation, IMO, Luma, UpToDate…), and Oracle NetSuite (6 pages).
- [`/business/marketplace/`](../../pages/openai.com/business/marketplace/index.md) plus marketplace customer-program terms.
- `/business/learn/` gets 25 demo/webinar pages.
- Forward-deployed engineering pages.
- 7 Supply Co. merch items.

## 5. Removals (30)
Last snapshots are in git history (`git log -- pages/openai.com/<path>`).
- **Redirects / URL moves (22):**
  - `/solutions/*` → `/business/solutions/*`
  - `/business/<webinar>` and `/business/guides-and-resources/*` → `/business/learn/*`
  - `/index/ada/` and `/index/blue-j/` → `/business/customer-stories/*`
  - `/business/plugins/wordpress-com/` → `/wordpress/`
  - `/economic-research-exchange/` → `/economic-research-collaborators/`
  - `/form/ultrafast/` → developers.openai.com docs
  - **`/residency/` → `/research/`**: the OpenAI Residency program page is gone.
  - **`/prism/` → `/science/`**
  - `/business/partners/pathfindr/` → `/business/partners/affinda/`
- **Now 404 (8):**
  - Partner pages for Canva, Dropbox, Gusto, HubSpot, QuickBooks and Stripe. These look like a partner-directory cleanup; the matching plugin pages remain.
  - Plugins atlassian-rovo, litera-lito, mcp-server-for-wordpress and oracle-analytics. Each was replaced by a new slug: `atlassian`/`atlassian-teammate-graph`, `litera`, `wordpress` and `oracle-analytics-cloud`.
  - `/daybreak/partners-new/`
