# Analysis: 2026-06-14T09-17Z

**Fetch time:** 2026-06-14T09:17:12Z  
**Total URLs in current sitemap:** 1,349  
**Baseline (prior run):** 2026-06-13T09-15Z — 1,349 URLs  
**Sub-sitemaps fetched:** 34

## Summary

| Metric | Count |
|--------|-------|
| Added | 0 |
| Removed | 0 |
| Updated (lastmod changed) | 131 |
| Anomalies | 0 |
| Fetch failures | 0 |
| Pages with visible markdown changes | 35 |

## Anomalies

None detected.

---

## Key Finding: Sitewide Website Navigation & Template Redesign

Today's 131 lastmod updates are almost entirely explained by a **sitewide website template and navigation overhaul** that rolled out June 13–14, 2026 in two waves:
- **June 13 wave (39 pages):** News index pages, brand stories, policies, signals — first phase of the rollout.
- **June 14 wave (92 pages):** Research/index pages, older blog posts, product pages — completion of the sitewide rollout.

Only 35 of the 131 pages show any visible change in extracted markdown; the remaining 96 saw changes invisible to html2text (likely CSS, JS bundle hashes, or CMS metadata) that still triggered lastmod bumps.

### 1. Footer navigation restructuring (affects every page)

The sitewide footer navigation was renamed and reorganized:

| Old label | New label | Key change |
|-----------|-----------|------------|
| "Our Research" | "Research" | — |
| "ChatGPT" | "Products" | Expanded with **Codex** and **Release Notes** |
| "For Business" | "Business" | Minor rename |
| *(absent)* | **"Developers"** | Entirely new section |

**Products section** now explicitly lists:
- ChatGPT, ChatGPT Business, ChatGPT Enterprise, ChatGPT for Education
- **Codex** (newly added as a first-class product alongside ChatGPT)
- **Release Notes** (newly added)

**New "Developers" section** includes: Apps SDK, Open Models, Docs, Resources, Developer Forum

**Safety section** gains: "Deployment Safety" link (pointing to `deploymentsafety.openai.com`)

**Removed from footer sitewide:**
- "Research Residency" link (program appears to be de-emphasized or retired)
- "API Pricing" link (from API Platform section)
- "GPT-5.3-Codex" from Latest Advancements carousel

### 2. Article template change (TOC position shift)

On 35+ blog/research post pages, the table of contents now appears in a new DOM position — rendered **before** the article header metadata rather than after. A second "Table of contents" heading is also being injected. This is a layout change, not a content change. The duplicate TOC visible in diffs is an artifact of the template rendering.

### 3. "Pro" pricing link destination change

On multiple pages (computer-using-agent, introducing-operator, introducing-chatgpt-and-whisper-apis, etc.), links to the "Pro" ChatGPT tier changed from the internal relative path `/chatgpt/pricing/` to the absolute external URL `chatgpt.com/pricing`. This signals OpenAI's continued structural separation: ChatGPT lives at chatgpt.com; openai.com is for research/enterprise/developer content.

---

## Page-Level Content Changes (beyond template)

### `introducing-chatgpt-health` — "Related stories" updated
The "Keep reading" section changed:
- **Removed:** "Built to benefit everyone: our plan", "Introducing the OpenAI Economic Research Exchange"
- **Added:** "OpenAI to acquire Ona" (Jun 11), "Access OpenAI models and Codex through your Oracle cloud commitment" (Jun 10)
This is a recency rotation of related articles, not an editorial change to the page body.

### `moderna` — Notion case study title changed
A "related customer stories" card changed its headline:
- **Before:** "Notion's GPT-5 rebuild unlocks autonomous AI workflows"
- **After:** "What Codex unlocks for Notion"
The Notion case study was re-titled to foreground Codex rather than GPT-5. The Notion page itself (`/index/notion/`) had a lastmod change (Jun 13→Jun 14) but showed no visible markdown diff, consistent with a title/metadata-only edit in the CMS.

### `cybersecurity-in-the-intelligence-age` — Related articles rotated
"Keep reading" section updated:
- **Removed:** "Biodefense in the Intelligence Age", "Frontier Safety Blueprint"
- **Added:** "PRC-linked influence operations are targeting AI debates in the US" (Jun 10), "Supporting Europe's work in ensuring a trustworthy AI ecosystem" (Jun 11)

### `teen-safety-freedom-and-privacy` — Related articles rotated
- **Removed:** "Advancing youth safety and opportunity through global leadership", "A shared playbook for trustworthy third party evaluations"
- **Added:** "Confidential submission of draft S-1 to the SEC" (Jun 8), "Access OpenAI models and Codex through your Oracle cloud commitment" (Jun 10)

### `stadler` / `intercom` / `openai-to-acquire-astral` — Related articles rotated
Similar pattern: older related stories replaced with more recent ones (Academy courses, Oracle partnership, Ona acquisition, etc.)

### `model-ml-chaz-englander` — Heading levels changed
Q&A section headings changed from `####` (h4) to `###` (h3) — a minor formatting fix. No substantive content change.

### `research/index/publication` — Two entries reordered
"GPT-5.4 Thinking System Card" and "Reasoning models struggle to control their chains of thought" swapped positions in the list. Minor listing order change.

---

## Strategic Interpretation

**Codex elevated to core product:** Adding Codex explicitly to the sitewide footer Products section — alongside ChatGPT, ChatGPT Business, ChatGPT Enterprise, and ChatGPT for Education — is a significant branding signal. Codex now appears as a distinct, named product in the site's global navigation, not just a feature. This is consistent with the recent acquisition spree focused on Codex infrastructure: Astral (Python packaging/tooling), Ona (persistent cloud execution for agents).

**Research Residency quietly sunset:** Removing "Research Residency" from the sitewide footer likely signals the program is no longer an active recruiting pathway. The Research Residency was how OpenAI brought in promising non-traditional researchers; its removal from primary navigation suggests a shift toward hiring experienced researchers directly rather than training newcomers through the residency pipeline.

**openai.com / chatgpt.com separation accelerating:** The "Pro" link change (relative `/chatgpt/pricing/` → absolute `chatgpt.com/pricing`) and the Products section reorganization reflect an increasingly clear split: chatgpt.com = consumer AI assistant; openai.com = research, enterprise, developer, policy.

**Notion's case study reframed around Codex:** The title change from "GPT-5 rebuild" to "What Codex unlocks for Notion" is a small but telling editorial choice — OpenAI is retroactively foregrounding Codex as the narrative through-line even for partnerships initially framed around GPT-5.

---

## Updated Pages (raw list)


### https://openai.com/news/applied-ai/
- lastmod: `2026-06-12T13:10:19.391Z` → `2026-06-13T15:48:33.615Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/economic-research-exchange/
- lastmod: `2026-06-13T05:03:20.868Z` → `2026-06-13T21:06:48.111Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/
- lastmod: `2026-05-22T19:07:17.499Z` → `2026-06-14T07:18:16.711Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/improved-techniques-for-training-consistency-models/
- lastmod: `2026-06-12T20:23:43.564Z` → `2026-06-14T07:05:16.530Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/engineering/
- lastmod: `2026-06-12T13:09:32.983Z` → `2026-06-13T15:49:03.070Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-baselines-dqn/
- lastmod: `2026-06-12T20:23:59.214Z` → `2026-06-14T07:05:17.235Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-five/
- lastmod: `2026-06-12T20:24:17.447Z` → `2026-06-14T07:05:28.470Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/products/release-notes/
- lastmod: `2026-06-13T07:44:35.180Z` → `2026-06-13T11:55:34.446Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/procgen-benchmark/
- lastmod: `2026-06-12T20:23:43.477Z` → `2026-06-14T07:05:15.552Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/helping-people-when-they-need-it-most/
- lastmod: `2026-06-12T04:52:24.839Z` → `2026-06-14T04:39:52.803Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/introducing-swe-bench-verified/
- lastmod: `2026-06-12T20:24:17.470Z` → `2026-06-14T07:05:36.880Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-baselines-acktr-a2c/
- lastmod: `2026-06-12T20:23:52.452Z` → `2026-06-14T07:05:29.285Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/techniques-for-training-large-neural-networks/
- lastmod: `2026-06-12T20:23:41.295Z` → `2026-06-14T07:05:16.022Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/daybreak/
- lastmod: `2026-06-12T03:58:28.924Z` → `2026-06-14T08:00:52.448Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/safety-gym/
- lastmod: `2026-06-12T20:23:42.621Z` → `2026-06-14T07:05:21.170Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/policies/ad-tools-terms/
- lastmod: `2026-06-13T08:41:05.124Z` → `2026-06-14T08:00:30.785Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/zalando/
- lastmod: `2026-06-12T13:46:01.840Z` → `2026-06-13T10:40:11.697Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/new-and-improved-content-moderation-tooling/
- lastmod: `2026-06-03T18:57:51.370Z` → `2026-06-13T15:49:14.209Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/policies/openai-cve-assignment-policy/
- lastmod: `2026-06-13T06:46:20.498Z` → `2026-06-13T15:51:09.933Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/cybersecurity-in-the-intelligence-age/
- lastmod: `2026-06-12T03:56:34.755Z` → `2026-06-14T07:58:59.754Z`
- Content diff: Removed lines (sample): ['[Biodefense in the Intelligence AgeGlobal AffairsJun 4, 2026](</index/biodefense-in-the-intelligence-age/>)', '![oai 1x1 Biodefense in the Intelligence Age](https://images.ctfassets.net/kftzwdyauwt9/6A4rrCBs9rrlbzm9JWIvSi/8a4ae56849fcd0b16e90b59b8babc613/oai_1x1_Biodefense_in_the_Intelligence_Age.png?w=3840&q=90&fm=webp)', '![Frontier Safety Blueprint > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/6zU111Ouj65b8iZJnswHBe/a705de1c90ab048510532db2f53f12f3/Frame.png?w=3840&q=90&fm=webp)']; Added lines (sample): ['[PRC-linked influence operations are targeting AI debates in the USGlobal AffairsJun 10, 2026](</index/prc-linked-influence-operations-ai-debates/>)', '![PRC-linked influence > Art Card](https://images.ctfassets.net/kftzwdyauwt9/2WkDQ2w51892xwY7QHwkRC/ec5f7b504805e36db928c06cb313f53c/Threat-Intelligence-Repart-ArtCard.png?w=3840&q=90&fm=webp)', '[Supporting Europe’s work in ensuring a trustworthy AI ecosystem Global AffairsJun 11, 2026](</index/supporting-eu-trustworthy-ai-ecosystem/>)']

### https://openai.com/policies/
- lastmod: `2026-06-13T07:23:29.622Z` → `2026-06-13T22:07:00.244Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/elon-musk/
- lastmod: `2026-05-22T19:42:30.076Z` → `2026-06-14T08:51:34.635Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/industrial-policy-for-the-intelligence-age/
- lastmod: `2026-06-13T04:51:53.502Z` → `2026-06-14T00:49:55.774Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/mercado-libre/
- lastmod: `2026-06-12T13:45:51.883Z` → `2026-06-14T06:38:08.542Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/prc-linked-influence-operations-ai-debates/
- lastmod: `2026-06-13T07:14:01.252Z` → `2026-06-13T22:06:40.454Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/endex/
- lastmod: `2026-06-02T15:01:36.835Z` → `2026-06-14T04:10:47.603Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/policies/services-agreement/
- lastmod: `2026-06-13T06:16:19.250Z` → `2026-06-14T08:17:23.944Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/signals/
- lastmod: `2026-06-13T04:14:21.667Z` → `2026-06-13T22:12:25.354Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-canvas/
- lastmod: `2026-05-22T19:03:26.012Z` → `2026-06-13T13:08:14.669Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/nextdoor/
- lastmod: `2026-06-13T04:01:40.560Z` → `2026-06-13T15:48:52.305Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/block-sparse-gpu-kernels/
- lastmod: `2026-06-12T20:23:55.676Z` → `2026-06-14T07:05:23.314Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/the-met-museum/
- lastmod: `2026-06-05T09:12:27.292Z` → `2026-06-13T15:49:42.334Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness/
- lastmod: `2026-06-12T20:23:53.735Z` → `2026-06-14T07:05:19.336Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/computer-using-agent/
- lastmod: `2026-05-18T16:57:38.714Z` → `2026-06-14T04:34:44.366Z`
- Content diff: Removed lines (sample): ['  * [Platform Overview](</api/>)', 'We’ve developed CUA with safety as a top priority to address the challenges posed by an agent having access to the digital world, as detailed in our [Operator System Card](</index/operator-system-card/>). In line with our iterative deployment strategy, we are releasing CUA through a research preview of Operator at [operator.chatgpt.com\u2060(opens in a new window)](<http://operator.chatgpt.com>) for [Pro](</chatgpt/pricing/>) Tier users in the U.S. to start. By gathering real-world feedback, we can refine safety measures and continuously improve as we prepare for a future with increasing use of digital agents.', '  * [Education](<https://chatgpt.com/business/education>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', 'We’ve developed CUA with safety as a top priority to address the challenges posed by an agent having access to the digital world, as detailed in our [Operator System Card](</index/operator-system-card/>). In line with our iterative deployment strategy, we are releasing CUA through a research preview of Operator at [operator.chatgpt.com\u2060(opens in a new window)](<http://operator.chatgpt.com>) for [Pro\u2060(opens in a new window)](<https://chatgpt.com/pricing>) Tier users in the U.S. to start. By gathering real-world feedback, we can refine safety measures and continuously improve as we prepare for a future with increasing use of digital agents.']

### https://openai.com/form/openai-for-science/
- lastmod: `2026-05-22T19:28:05.855Z` → `2026-06-14T07:10:57.206Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/more-on-dota-2/
- lastmod: `2026-06-12T20:24:19.025Z` → `2026-06-14T07:05:23.182Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/scaling-kubernetes-to-7500-nodes/
- lastmod: `2026-06-12T20:23:53.757Z` → `2026-06-14T07:05:32.291Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/wasmer/
- lastmod: `2026-06-13T08:41:04.259Z` → `2026-06-14T06:41:21.143Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-gym-beta/
- lastmod: `2026-06-12T20:24:20.949Z` → `2026-06-14T07:05:24.048Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/research/index/
- lastmod: `2026-06-12T20:24:21.723Z` → `2026-06-14T07:06:06.925Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-baselines-ppo/
- lastmod: `2026-06-12T20:24:10.984Z` → `2026-06-14T07:05:24.237Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/image-gpt/
- lastmod: `2026-05-27T23:30:45.174Z` → `2026-06-14T06:18:11.841Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/signals/b2b/
- lastmod: `2026-06-12T21:30:32.065Z` → `2026-06-13T22:19:49.511Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/model-ml-chaz-englander/
- lastmod: `2026-06-02T15:02:10.717Z` → `2026-06-14T07:10:14.892Z`
- Content diff: Removed lines (sample): ['#### How does Model ML stand out compared to general-purpose AI tools, and how are new model capabilities benefiting your customers?', '#### What are you seeing change inside financial services firms?', '#### How do you keep your team agile as AI evolves so quickly?']; Added lines (sample): ['### What are you seeing change inside financial services firms?', '### How do you keep your team agile as AI evolves so quickly?', '**_Our Executive Function series features perspectives from leaders on the frontier of AI adoption._**']

### https://openai.com/index/introducing-gpt-oss-safeguard/
- lastmod: `2026-05-22T19:15:13.137Z` → `2026-06-14T07:22:19.093Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/new-chatgpt-images-is-here/
- lastmod: `2026-05-22T19:12:30.401Z` → `2026-06-14T06:37:26.894Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/gym-retro/
- lastmod: `2026-06-12T20:23:43.286Z` → `2026-06-14T07:05:29.404Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/a-hazard-analysis-framework-for-code-synthesis-large-language-models/
- lastmod: `2026-06-12T20:23:49.871Z` → `2026-06-14T07:05:15.778Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/research/
- lastmod: `2026-06-12T20:24:04.799Z` → `2026-06-14T07:05:47.858Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/morgan-stanley/
- lastmod: `2026-06-02T15:01:49.490Z` → `2026-06-13T10:40:13.811Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/election-safeguards-2026/
- lastmod: `2026-06-13T07:43:54.425Z` → `2026-06-13T15:49:15.252Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-openai-o1-preview/
- lastmod: `2026-05-15T16:33:28.727Z` → `2026-06-13T13:08:12.828Z`
- Content diff: Removed lines (sample): ['  * [Platform Overview](</api/>)', '  * [Education](<https://chatgpt.com/business/education>)', '  * [Business Overview](</business/>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', '  * [Docs(opens in a new window)](<https://developers.openai.com/>)']

### https://openai.com/policies/ad-tools-dpa/
- lastmod: `2026-06-13T07:04:48.082Z` → `2026-06-14T08:28:22.445Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/policies/ad-tools-subprocessors/
- lastmod: `2026-06-13T07:29:34.526Z` → `2026-06-13T22:07:12.267Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/
- lastmod: `2026-06-12T13:09:34.319Z` → `2026-06-13T15:48:57.671Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/mercari/
- lastmod: `2026-06-12T13:45:51.407Z` → `2026-06-14T04:11:10.595Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/teen-safety-freedom-and-privacy/
- lastmod: `2026-06-12T04:51:15.653Z` → `2026-06-13T21:06:27.727Z`
- Content diff: Removed lines (sample): ['[Advancing youth safety and opportunity through global leadershipGlobal AffairsJun 2, 2026](</index/advancing-youth-safety-and-opportunity-through-global-leadership/>)', '![Technical foundations > Art Card](https://images.ctfassets.net/kftzwdyauwt9/6gugGfSiM1oO6UHxxwnqTk/c7173a5a2c096a8f8a24c258ddfa22dd/ArtCard-TechnicalFoundations.png?w=3840&q=90&fm=webp)', '[A shared playbook for trustworthy third party evaluationsSafetyMay 29, 2026](</index/trustworthy-third-party-evaluations-foundations/>)']; Added lines (sample): ['[Confidential submission of draft S-1 to the SECCompanyJun 8, 2026](</index/openai-submits-confidential-s-1/>)', '![Confidential submission of draft S-1 to the SEC > cover image](https://images.ctfassets.net/kftzwdyauwt9/36doI12YCwUtp1hzD4d8bj/84e67c565f39e7d5ca3ee011efa69756/confidential-submission-of-draft-s-1-to-the-sec-1x1.png?w=3840&q=90&fm=webp)', '[Access OpenAI models and Codex through your Oracle cloud commitmentCompanyJun 10, 2026](</index/openai-on-oracle-cloud/>)']

### https://openai.com/index/dota-2-with-large-scale-deep-reinforcement-learning/
- lastmod: `2026-06-12T20:24:17.564Z` → `2026-06-14T07:05:34.585Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/harvey/
- lastmod: `2026-06-11T09:25:25.235Z` → `2026-06-14T06:51:07.380Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/dall-e-2-pre-training-mitigations/
- lastmod: `2026-06-12T20:23:50.745Z` → `2026-06-14T07:05:18.166Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/stadler/
- lastmod: `2026-06-12T09:04:17.740Z` → `2026-06-13T15:49:28.817Z`
- Content diff: Removed lines (sample): ['![Economic research forum > art card ](https://images.ctfassets.net/kftzwdyauwt9/2DpNjvjdVuCrLKNOrFrWJ7/1aefe1cbe252bcd9ba42035469fc8a0f/art_card.png?w=3840&q=90&fm=webp)', '[Built to benefit everyone: our planCompanyJun 8, 2026](</index/built-to-benefit-everyone-our-plan/>)', '[Confidential submission of draft S-1 to the SECCompanyJun 8, 2026](</index/openai-submits-confidential-s-1/>)']; Added lines (sample): ['![Introducing OpenAI Academy courses > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/2mmXo430NiaNqyi6YrRtnh/715ab11fa5003dd50acff55adcb4a5fd/Frame.png?w=3840&q=90&fm=webp)', '[New OpenAI Academy courses for the next era of workAI AdoptionJun 12, 2026](</index/academy-courses-applying-ai-at-work/>)', '![Supporting Europe’s work in ensuring a trustworthy AI ecosystem  > art card](https://images.ctfassets.net/kftzwdyauwt9/U3OuQtdga2BaxWxb0e2ge/2fdc2fb1cf5c70a8f77fc4b55236aa78/Frame2.png?w=3840&q=90&fm=webp)']

### https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/
- lastmod: `2026-06-12T20:23:58.395Z` → `2026-06-14T07:05:24.334Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-operator/
- lastmod: `2026-05-18T16:57:35.931Z` → `2026-06-14T04:34:13.954Z`
- Content diff: Removed lines (sample): ['  * [Platform Overview](</api/>)', '  * [Education](<https://chatgpt.com/business/education>)', '  * [Business Overview](</business/>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', '  * [Docs(opens in a new window)](<https://developers.openai.com/>)']

### https://openai.com/index/universe/
- lastmod: `2026-06-12T20:23:59.399Z` → `2026-06-14T07:05:33.756Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-five-defeats-dota-2-world-champions/
- lastmod: `2026-06-12T20:23:43.120Z` → `2026-06-14T07:05:18.232Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/glow/
- lastmod: `2026-06-12T20:24:12.449Z` → `2026-06-14T07:05:22.489Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/jukebox/
- lastmod: `2026-06-12T20:23:56.886Z` → `2026-06-14T07:05:51.822Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/signals/data-download/
- lastmod: `2026-06-12T21:23:17.848Z` → `2026-06-13T22:12:28.640Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-to-acquire-astral/
- lastmod: `2026-05-22T18:53:45.317Z` → `2026-06-13T15:49:49.382Z`
- Content diff: Removed lines (sample): ['![dell](https://images.ctfassets.net/kftzwdyauwt9/17U8SngLERoATdFhOjWbDK/da377e6850f8241ea7814a347bad0a3a/Frame.png?w=3840&q=90&fm=webp)', '[OpenAI and Dell Technologies partner to bring Codex to hybrid and on-premises enterprise environmentsCompanyMay 18, 2026](</index/dell-codex-enterprise-partnership/>)', '![Frame](https://images.ctfassets.net/kftzwdyauwt9/32jPyVqUObkTrIIyA6tJV1/4eb384b5bb2f21ccea5de7665858a37a/Frame.png?w=3840&q=90&fm=webp)']; Added lines (sample): ['[Confidential submission of draft S-1 to the SECCompanyJun 8, 2026](</index/openai-submits-confidential-s-1/>)', '![Confidential submission of draft S-1 to the SEC > cover image](https://images.ctfassets.net/kftzwdyauwt9/36doI12YCwUtp1hzD4d8bj/84e67c565f39e7d5ca3ee011efa69756/confidential-submission-of-draft-s-1-to-the-sec-1x1.png?w=3840&q=90&fm=webp)', 'Table of contents']

### https://openai.com/index/openai-on-oracle-cloud/
- lastmod: `2026-06-13T07:08:31.081Z` → `2026-06-13T23:07:54.933Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/business/customer-stories/
- lastmod: `2026-06-12T20:23:52.979Z` → `2026-06-14T07:05:32.982Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/whisper/
- lastmod: `2026-06-12T20:24:13.998Z` → `2026-06-14T07:05:35.909Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/company-announcements/
- lastmod: `2026-06-12T13:10:01.984Z` → `2026-06-13T15:48:54.979Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/learning-to-reason-with-llms/
- lastmod: `2026-05-27T23:30:57.143Z` → `2026-06-14T07:17:09.263Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/roboschool/
- lastmod: `2026-06-12T20:23:56.922Z` → `2026-06-14T07:05:17.335Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/bbva/
- lastmod: `2026-06-13T08:41:09.810Z` → `2026-06-14T05:39:12.864Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/new-tools-for-building-agents/
- lastmod: `2026-04-27T08:32:30.402Z` → `2026-06-14T07:06:15.844Z`
- Content diff: Removed lines (sample): ['Our Research', '  * [Platform Overview](</api/>)', '  * [Business](<https://chatgpt.com/business/business-plan>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', '  * [Docs(opens in a new window)](<https://developers.openai.com/>)']

### https://openai.com/index/openai-five-benchmark-results/
- lastmod: `2026-06-12T20:24:17.613Z` → `2026-06-14T07:05:31.266Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/global-affairs/
- lastmod: `2026-06-12T13:09:33.301Z` → `2026-06-13T15:49:25.979Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/moderna/
- lastmod: `2026-06-04T20:27:40.968Z` → `2026-06-14T06:46:12.853Z`
- Content diff: Removed lines (sample): ['[Notion’s GPT‑5 rebuild unlocks autonomous AI workflowsAPI](</index/notion/>)']; Added lines (sample): ['[What Codex unlocks for NotionAPI](</index/notion/>)']

### https://openai.com/interview-guide/
- lastmod: `2026-05-01T18:09:49.045Z` → `2026-06-13T15:49:19.827Z`
- Content diff: Removed lines (sample): ['Our Research', '  * [Platform Overview](</api/>)', '  * [Business](<https://chatgpt.com/business/business-plan>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', '  * [Docs(opens in a new window)](<https://developers.openai.com/>)']

### https://openai.com/index/preply/
- lastmod: `2026-06-13T07:24:04.371Z` → `2026-06-14T07:13:06.964Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/intercom/
- lastmod: `2026-06-12T09:03:04.678Z` → `2026-06-14T06:53:34.081Z`
- Content diff: Removed lines (sample): ['[What Codex unlocks for NotionJun 9, 2026](</index/notion/>)', '[Industrial policy for the Intelligence AgeGlobal AffairsJun 9, 2026](</index/industrial-policy-for-the-intelligence-age/>)', '[How engineers at Nextdoor use Codex to build without limitsJun 9, 2026](</index/nextdoor/>)']; Added lines (sample): ['![Introducing OpenAI Academy courses > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/2mmXo430NiaNqyi6YrRtnh/715ab11fa5003dd50acff55adcb4a5fd/Frame.png?w=3840&q=90&fm=webp)', '[New OpenAI Academy courses for the next era of workAI AdoptionJun 12, 2026](</index/academy-courses-applying-ai-at-work/>)', '![Supporting Europe’s work in ensuring a trustworthy AI ecosystem  > art card](https://images.ctfassets.net/kftzwdyauwt9/U3OuQtdga2BaxWxb0e2ge/2fdc2fb1cf5c70a8f77fc4b55236aa78/Frame2.png?w=3840&q=90&fm=webp)']

### https://openai.com/index/economic-impacts-research/
- lastmod: `2026-06-12T20:23:59.277Z` → `2026-06-14T07:05:21.982Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-and-reddit-partnership/
- lastmod: `2026-05-22T19:15:36.372Z` → `2026-06-13T15:49:27.753Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/nonlinear-computation-in-deep-linear-networks/
- lastmod: `2026-06-12T20:23:43.729Z` → `2026-06-14T07:05:21.401Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/triton/
- lastmod: `2026-06-12T20:24:18.897Z` → `2026-06-14T07:05:16.095Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/research/index/publication/
- lastmod: `2026-06-12T20:24:06.758Z` → `2026-06-14T07:05:25.655Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/faster-physics-in-python/
- lastmod: `2026-06-12T20:23:56.101Z` → `2026-06-14T07:05:22.891Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/research/index/conclusion/
- lastmod: `2026-06-12T20:24:08.594Z` → `2026-06-14T07:05:48.580Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/cycling-across-antarctica/
- lastmod: `2026-06-13T07:30:04.937Z` → `2026-06-14T09:14:09.045Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/mavenagi/
- lastmod: `2026-05-22T19:06:01.902Z` → `2026-06-14T04:18:13.137Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/scaling-kubernetes-to-2500-nodes/
- lastmod: `2026-06-12T20:23:55.554Z` → `2026-06-14T07:05:28.605Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/openai-submits-confidential-s-1/
- lastmod: `2026-06-12T11:52:37.652Z` → `2026-06-13T15:48:44.100Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/how-ai-training-scales/
- lastmod: `2026-06-12T20:23:58.248Z` → `2026-06-14T07:05:18.394Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-the-model-spec/
- lastmod: `2026-05-22T18:54:32.136Z` → `2026-06-14T06:58:08.549Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/infrastructure-for-deep-learning/
- lastmod: `2026-06-12T20:23:44.096Z` → `2026-06-14T07:05:23.913Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-structured-outputs-in-the-api/
- lastmod: `2026-05-22T19:07:16.863Z` → `2026-06-14T06:26:08.594Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/genmab/
- lastmod: `2026-06-11T17:46:02.734Z` → `2026-06-14T06:37:50.586Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/introducing-chatgpt-health/
- lastmod: `2026-06-06T15:39:54.197Z` → `2026-06-14T04:37:40.082Z`
- Content diff: Removed lines (sample): ['![Built for broad benefit > cover](https://images.ctfassets.net/kftzwdyauwt9/bEe28mW3dEOj9pKJsPp2u/13f7bed9e86b0667ba924479d62f98e4/Art_Card_1080x1080_1.png?w=3840&q=90&fm=webp)', '![Economic research forum > art card ](https://images.ctfassets.net/kftzwdyauwt9/2DpNjvjdVuCrLKNOrFrWJ7/1aefe1cbe252bcd9ba42035469fc8a0f/art_card.png?w=3840&q=90&fm=webp)', '[Introducing the OpenAI Economic Research ExchangeCompanyJun 8, 2026](</index/economic-research-exchange/>)']; Added lines (sample): ['Table of contents', '[Access OpenAI models and Codex through your Oracle cloud commitmentCompanyJun 10, 2026](</index/openai-on-oracle-cloud/>)', '![OpenAI acquires Ona > oai 1x1](https://images.ctfassets.net/kftzwdyauwt9/6SkgXCQ08f4AYarun2I3oU/24414c9962c945767f783bdb63006841/OAI-Ona-ArtCard.png?w=3840&q=90&fm=webp)']

### https://openai.com/index/introducing-parental-controls/
- lastmod: `2026-05-22T19:15:42.524Z` → `2026-06-13T13:07:43.687Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/accelerating-cyber-defense-ecosystem/
- lastmod: `2026-06-13T00:34:30.083Z` → `2026-06-14T08:00:52.245Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/healthbench/
- lastmod: `2026-05-22T18:59:10.116Z` → `2026-06-14T06:37:20.190Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/travelers/
- lastmod: `2026-06-13T09:06:09.836Z` → `2026-06-13T23:31:11.760Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/
- lastmod: `2026-06-12T03:58:25.952Z` → `2026-06-14T08:00:12.682Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/research/index/milestone/
- lastmod: `2026-06-12T20:24:01.830Z` → `2026-06-14T07:05:21.981Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/safety-alignment/
- lastmod: `2026-06-12T13:09:27.933Z` → `2026-06-13T15:50:01.595Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/business/learn/gartner-2026-agentic-coding-leader/
- lastmod: `2026-06-12T20:24:04.862Z` → `2026-06-14T07:05:35.723Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/point-e/
- lastmod: `2026-06-12T20:23:51.469Z` → `2026-06-14T07:05:33.278Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/more-ways-to-work-with-your-team/
- lastmod: `2026-04-27T08:35:16.411Z` → `2026-06-14T06:21:14.936Z`
- Content diff: Removed lines (sample): ['  * [Platform Overview](</api/>)', '#### Recent updates', '[Introducing Advanced Account SecurityProductApr 30, 2026](</index/advanced-account-security/>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', '  * [Docs(opens in a new window)](<https://developers.openai.com/>)']

### https://openai.com/index/mle-bench/
- lastmod: `2026-06-12T20:23:44.738Z` → `2026-06-14T07:05:24.467Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/notion/
- lastmod: `2026-06-13T01:12:52.405Z` → `2026-06-14T07:05:32.485Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-chatgpt-and-whisper-apis/
- lastmod: `2026-05-15T16:33:57.847Z` → `2026-06-14T06:28:10.331Z`
- Content diff: Removed lines (sample): ['Our Research', '  * [Platform Overview](</api/>)', '  * [Business](<https://chatgpt.com/business/business-plan>)']; Added lines (sample): ['  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)', '  * [Open Models](</open-models/>)', '  * [Docs(opens in a new window)](<https://developers.openai.com/>)']

### https://openai.com/gpt-4o-contributions/
- lastmod: `2026-05-22T19:00:43.192Z` → `2026-06-14T07:27:08.701Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/superhuman/
- lastmod: `2026-05-22T19:27:16.082Z` → `2026-06-13T15:49:12.970Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/creating-new-simulations-black-holes/
- lastmod: `2026-06-13T05:30:06.119Z` → `2026-06-14T06:16:09.206Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/introducing-gpts/
- lastmod: `2026-05-22T19:07:30.328Z` → `2026-06-14T04:15:06.011Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/simplifying-stabilizing-and-scaling-continuous-time-consistency-models/
- lastmod: `2026-06-12T20:24:18.541Z` → `2026-06-14T07:05:35.550Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/consistency-models/
- lastmod: `2026-06-12T20:24:01.179Z` → `2026-06-14T07:05:18.524Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/better-exploration-with-parameter-noise/
- lastmod: `2026-06-12T20:23:50.922Z` → `2026-06-14T07:05:22.139Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/signals/data/
- lastmod: `2026-06-12T21:22:45.067Z` → `2026-06-13T22:11:41.627Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/mixi/
- lastmod: `2026-06-12T09:02:43.893Z` → `2026-06-14T04:21:18.350Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/global-affairs/introducing-chatgpt-gov/
- lastmod: `2026-05-22T19:00:56.920Z` → `2026-06-14T08:02:12.573Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/product-releases/
- lastmod: `2026-06-12T13:09:31.581Z` → `2026-06-13T15:49:36.762Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/improving-model-safety-behavior-with-rule-based-rewards/
- lastmod: `2026-05-22T19:15:14.681Z` → `2026-06-14T06:49:07.022Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/index/openai-lp/
- lastmod: `2026-06-10T12:28:31.478Z` → `2026-06-13T21:06:12.341Z`
- Content diff: Added lines (sample): ['Table of contents']

### https://openai.com/news/security/
- lastmod: `2026-06-12T13:09:27.250Z` → `2026-06-13T15:48:58.442Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/signals/research/
- lastmod: `2026-06-12T21:22:41.949Z` → `2026-06-13T22:12:24.714Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/index/reptile/
- lastmod: `2026-06-12T20:24:16.642Z` → `2026-06-14T07:05:28.545Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/news/ai-adoption/
- lastmod: `2026-06-12T13:09:33.505Z` → `2026-06-13T15:48:53.161Z`
- Content diff: No substantive text changes (whitespace/ordering only)

### https://openai.com/research/index/release/
- lastmod: `2026-06-12T20:24:08.938Z` → `2026-06-14T07:05:43.727Z`
- Content diff: No substantive text changes (whitespace/ordering only)
