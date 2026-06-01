# Analysis — 2026-06-01T09-15Z

**Fetch time:** 2026-06-01T09:17:27Z
**Baseline:** 2026-05-31T09-17Z
**Total current URLs:** 1311

## Summary
- Added: 0 URLs
- Updated: 245 URLs (sitemap lastmod timestamps changed; 2 pages with actual content change)
- Removed: 0 URLs
- Anomalies: 0
- Fetch failures: 0

## Anomalies

None detected.

## Actual Content Changes (vs. git HEAD)

Despite 245 sitemap `lastmod` timestamp updates, only **2 pages** had measurable HTML/Markdown content changes when compared against the prior committed snapshots:

### 1. Research News Listing — `https://openai.com/news/research/`
**Path:** pages/openai.com/news/research/index.md

**Change:** The display order of two Apr 23, 2026 entries was swapped. Previously, "GPT-5.5 System Card" (Safety category) appeared above "Introducing GPT-5.5" (Product category). Now "Introducing GPT-5.5" appears first. This appears to be a deliberate editorial reordering to lead with the product announcement rather than the safety document.

### 2. Research Hub — `https://openai.com/research/index/`
**Path:** pages/openai.com/research/index/index.md

**Change:** Same reordering as above — "Introducing GPT-5.5" (Product, Apr 23) and "GPT-5.5 System Card" (Safety, Apr 23) swapped positions. "Introducing GPT-5.5" now appears first on this research hub page.

## Interpretation of Mass Lastmod Update

The 245-URL `lastmod` timestamp bump (covering ~19% of the 1,311 total URLs) is consistent with a CMS-level batch operation — likely a template update, CDN cache-busting, or metadata refresh that causes Contentful to regenerate timestamps without substantive content changes. This pattern has been observed repeatedly: May 31 saw 271 updated, similar storms on prior dates. The actual visible content change is just the GPT-5.5 entry reordering on two research listing pages.

## New Pages

None.

## Removed Pages

None.

## Fetch Failures

None.

## Notable Pages With Lastmod Bumped (no content change)
- `https://openai.com/codex/` — lastmod to 2026-06-01T09:06:25Z
- `https://openai.com/about/` — lastmod to 2026-06-01T01:14:20Z
- `https://openai.com/index/gpt-5-first-look/` — lastmod to 2026-06-01T09:12:36Z
- `https://openai.com/index/gpt-5-amgen/`, `gpt-5-coding-design/`, `gpt-5-cursor/` — lastmod bumped
- `https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/` — lastmod bumped
- `https://openai.com/form/rosalind-biodefense-program/` — lastmod 2026-06-01T09:17:23Z (close to fetch time)
- `https://openai.com/form/stargate-infrastructure/` — lastmod bumped
- `https://openai.com/safety/` and `https://openai.com/trust-and-transparency/` — lastmod bumped

## Updated Pages (245 total lastmod changes)

- `https://openai.com/about/` — lastmod: 2026-05-31T08:03:50.040Z → 2026-06-01T01:14:20.392Z
- `https://openai.com/business/customer-stories/` — lastmod: 2026-05-31T08:45:13.748Z → 2026-06-01T08:56:27.408Z
- `https://openai.com/codex/` — lastmod: 2026-05-31T06:20:34.090Z → 2026-06-01T09:06:25.002Z
- `https://openai.com/daybreak/request-a-vulnerability-scan/` — lastmod: 2026-05-30T22:02:00.800Z → 2026-06-01T08:18:58.724Z
- `https://openai.com/form/100-chats-book-request/` — lastmod: 2026-05-29T16:36:21.207Z → 2026-05-31T17:20:15.364Z
- `https://openai.com/form/chatgpt-pro-community/` — lastmod: 2026-05-29T16:37:48.917Z → 2026-05-31T17:20:19.168Z
- `https://openai.com/form/codex-enterprise-promo/` — lastmod: 2026-05-26T22:49:37.203Z → 2026-06-01T08:18:48.386Z
- `https://openai.com/form/life-sciences-access/` — lastmod: 2026-05-31T07:54:09.207Z → 2026-06-01T08:18:22.501Z
- `https://openai.com/form/rosalind-biodefense-program/` — lastmod: 2026-05-31T07:23:16.487Z → 2026-06-01T09:17:23.092Z
- `https://openai.com/form/stargate-infrastructure/` — lastmod: 2026-05-22T18:55:32.239Z → 2026-06-01T08:18:51.469Z
- `https://openai.com/form/subscribe-to-new-sub-processors/` — lastmod: 2026-05-26T22:49:53.696Z → 2026-06-01T08:19:01.900Z
- `https://openai.com/form/vc-partnerships-application/` — lastmod: 2026-05-31T05:08:00.092Z → 2026-06-01T05:02:18.443Z
- `https://openai.com/index/10bedicu/` — lastmod: 2026-05-31T08:45:00.656Z → 2026-06-01T08:55:51.291Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/a-hazard-analysis-framework-for-code-synthesis-large-language-models/` — lastmod: 2026-05-30T05:12:54.619Z → 2026-05-31T20:06:10.562Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/ada/` — lastmod: 2026-05-31T08:44:38.234Z → 2026-06-01T08:56:08.811Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/adventhealth/` — lastmod: 2026-05-30T06:57:58.497Z → 2026-05-31T12:40:20.406Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/adversarial-attacks-on-neural-network-policies/` — lastmod: 2026-05-30T05:12:51.341Z → 2026-05-31T20:06:15.701Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/adversarial-training-methods-for-semi-supervised-text-classification/` — lastmod: 2026-05-30T05:13:02.420Z → 2026-05-31T20:06:13.874Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/ai-and-compute/` — lastmod: 2026-05-31T08:03:31.047Z → 2026-05-31T21:40:25.368Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/ai-and-efficiency/` — lastmod: 2026-05-31T08:02:38.761Z → 2026-05-31T21:40:40.582Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/ai-safety-needs-social-scientists/` — lastmod: 2026-05-30T05:13:07.952Z → 2026-05-31T20:06:13.399Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/asymmetric-actor-critic-for-image-based-robot-learning/` — lastmod: 2026-05-31T08:03:39.599Z → 2026-05-31T21:40:29.941Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/attacking-machine-learning-with-adversarial-examples/` — lastmod: 2026-05-30T05:12:57.375Z → 2026-05-31T20:06:17.360Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/basis/` — lastmod: 2026-05-31T08:44:21.823Z → 2026-06-01T08:55:33.621Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/` — lastmod: 2026-05-30T05:12:51.002Z → 2026-05-31T20:06:11.131Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/best-practices-for-deploying-language-models/` — lastmod: 2026-05-30T05:12:51.552Z → 2026-05-31T20:06:23.458Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/better-exploration-with-parameter-noise/` — lastmod: 2026-05-31T08:02:35.958Z → 2026-05-31T21:40:30.238Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/better-language-models/` — lastmod: 2026-05-31T08:03:26.073Z → 2026-06-01T01:12:41.453Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/block-sparse-gpu-kernels/` — lastmod: 2026-05-31T08:02:47.915Z → 2026-05-31T21:40:43.746Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/blue-j/` — lastmod: 2026-05-31T08:44:15.959Z → 2026-06-01T08:55:37.989Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/building-self-improving-tax-agents-with-codex/` — lastmod: 2026-05-30T10:08:25.847Z → 2026-06-01T04:02:23.655Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/child-safety-adopting-sbd-principles/` — lastmod: 2026-05-30T05:13:06.592Z → 2026-05-31T20:06:14.979Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/chip-ganassi-racing/` — lastmod: 2026-05-31T09:08:12.031Z → 2026-06-01T09:14:16.709Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/cisco/` — lastmod: 2026-05-31T08:44:15.365Z → 2026-06-01T08:55:37.958Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/clip/` — lastmod: 2026-05-31T08:02:55.166Z → 2026-06-01T01:13:07.640Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/cna-walter-fernandez/` — lastmod: 2026-05-31T08:44:42.225Z → 2026-06-01T08:56:00.472Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/competitive-self-play/` — lastmod: 2026-05-31T08:03:33.070Z → 2026-06-01T01:13:00.986Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/computational-limitations-in-robust-classification-and-win-win-results/` — lastmod: 2026-05-31T08:02:36.853Z → 2026-05-31T21:40:18.593Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/concrete-ai-safety-problems/` — lastmod: 2026-05-30T05:12:51.915Z → 2026-05-31T20:06:17.178Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/confidence-building-measures-for-artificial-intelligence/` — lastmod: 2026-05-30T05:12:54.917Z → 2026-05-31T20:06:12.457Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/cooperation-on-safety/` — lastmod: 2026-05-30T05:12:50.708Z → 2026-05-31T20:06:18.145Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/critiques/` — lastmod: 2026-05-30T05:12:50.252Z → 2026-05-31T20:06:11.167Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/dall-e-3-system-card/` — lastmod: 2026-05-30T05:12:59.847Z → 2026-05-31T20:06:12.419Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/dall-e/` — lastmod: 2026-05-31T08:03:12.762Z → 2026-06-01T01:13:07.233Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/debate/` — lastmod: 2026-05-30T05:12:51.124Z → 2026-05-31T20:06:13.955Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/deep-double-descent/` — lastmod: 2026-05-31T08:03:38.114Z → 2026-05-31T21:40:33.240Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/deep-research/` — lastmod: 2026-05-31T08:16:58.801Z → 2026-06-01T09:12:20.685Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/deliberative-alignment/` — lastmod: 2026-05-30T05:12:53.283Z → 2026-05-31T20:06:15.592Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/democratic-inputs-to-ai-grant-program-update/` — lastmod: 2026-05-30T05:12:54.343Z → 2026-05-31T20:06:26.582Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/digital-green/` — lastmod: 2026-05-31T08:44:25.291Z → 2026-06-01T08:55:54.561Z
  - Minor changes (whitespace/formatting). Added 0 lines, removed 0 lines.
- `https://openai.com/index/discovering-types-for-entity-disambiguation/` — lastmod: 2026-05-31T08:03:39.121Z → 2026-05-31T21:40:26.153Z
- `https://openai.com/index/disrupting-a-covert-iranian-influence-operation/` — lastmod: 2026-05-30T05:12:56.457Z → 2026-05-31T20:06:17.128Z
- `https://openai.com/index/domain-randomization-and-generative-models-for-robotic-grasping/` — lastmod: 2026-05-31T08:03:48.630Z → 2026-05-31T21:40:12.623Z
- `https://openai.com/index/doordash-mariana-garavaglia/` — lastmod: 2026-05-31T08:44:16.144Z → 2026-06-01T08:55:33.808Z
- `https://openai.com/index/dota-2-with-large-scale-deep-reinforcement-learning/` — lastmod: 2026-05-31T08:03:03.658Z → 2026-05-31T21:40:22.724Z
- `https://openai.com/index/dota-2/` — lastmod: 2026-05-31T08:03:39.319Z → 2026-06-01T01:12:43.761Z
- `https://openai.com/index/early-access-for-safety-testing/` — lastmod: 2026-05-30T05:12:53.015Z → 2026-05-31T20:06:12.015Z
- `https://openai.com/index/economic-impacts/` — lastmod: 2026-05-30T05:12:51.745Z → 2026-05-31T20:06:18.796Z
- `https://openai.com/index/efficient-training-of-language-models-to-fill-in-the-middle/` — lastmod: 2026-05-31T08:03:32.648Z → 2026-05-31T21:40:07.608Z
- `https://openai.com/index/eliseai-minna-song/` — lastmod: 2026-05-31T08:44:16.146Z → 2026-06-01T08:56:12.827Z
- `https://openai.com/index/emergent-tool-use/` — lastmod: 2026-05-31T08:03:02.152Z → 2026-06-01T01:13:22.751Z
- `https://openai.com/index/endava/` — lastmod: 2026-05-31T08:45:15.030Z → 2026-06-01T08:55:38.076Z
- `https://openai.com/index/energy-based-models/` — lastmod: 2026-05-31T08:02:37.778Z → 2026-05-31T21:40:38.932Z
- `https://openai.com/index/evolution-through-large-models/` — lastmod: 2026-05-31T08:02:56.775Z → 2026-05-31T21:40:08.811Z
- `https://openai.com/index/evolved-policy-gradients/` — lastmod: 2026-05-31T08:02:33.995Z → 2026-06-01T01:12:43.315Z
- `https://openai.com/index/expanding-on-how-voice-engine-works-and-our-safety-research/` — lastmod: 2026-05-30T05:13:05.284Z → 2026-05-31T20:06:48.248Z
- `https://openai.com/index/expedia-jochen-koedijk/` — lastmod: 2026-05-31T08:44:43.078Z → 2026-06-01T08:55:54.116Z
- `https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/` — lastmod: 2026-05-31T08:02:48.875Z → 2026-05-31T21:40:27.398Z
- `https://openai.com/index/fanatics-betting-gaming-andrea-ellis/` — lastmod: 2026-05-31T08:44:39.644Z → 2026-06-01T08:55:50.788Z
- `https://openai.com/index/faster-physics-in-python/` — lastmod: 2026-05-31T08:03:34.118Z → 2026-05-31T21:40:26.617Z
- `https://openai.com/index/faulty-reward-functions/` — lastmod: 2026-05-30T05:12:51.254Z → 2026-05-31T20:06:16.683Z
- `https://openai.com/index/ffjord/` — lastmod: 2026-05-31T08:03:41.520Z → 2026-05-31T21:40:41.215Z
- `https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/` — lastmod: 2026-05-30T05:13:03.702Z → 2026-05-31T20:06:25.335Z
- `https://openai.com/index/fine-tuning-gpt-2/` — lastmod: 2026-05-30T05:12:49.821Z → 2026-05-31T20:06:41.680Z
- `https://openai.com/index/first-proof-submissions/` — lastmod: 2026-05-31T08:03:15.052Z → 2026-05-31T21:40:28.395Z
- `https://openai.com/index/forecasting-misuse/` — lastmod: 2026-05-30T05:12:48.394Z → 2026-05-31T20:06:10.865Z
- `https://openai.com/index/formal-math/` — lastmod: 2026-05-31T08:03:28.015Z → 2026-06-01T01:12:42.734Z
- `https://openai.com/index/frontier-ai-regulation/` — lastmod: 2026-05-30T05:13:00.586Z → 2026-05-31T20:06:12.938Z
- `https://openai.com/index/frontier-builders/` — lastmod: 2026-05-31T08:17:36.447Z → 2026-06-01T09:12:38.366Z
- `https://openai.com/index/frontier-model-forum/` — lastmod: 2026-05-30T05:12:57.745Z → 2026-05-31T20:06:14.481Z
- `https://openai.com/index/frontier-risk-and-preparedness/` — lastmod: 2026-05-30T05:12:53.011Z → 2026-05-31T20:06:25.411Z
- `https://openai.com/index/gamepad/` — lastmod: 2026-05-31T08:02:31.805Z → 2026-05-31T21:40:23.452Z
- `https://openai.com/index/gathering-human-feedback/` — lastmod: 2026-05-31T08:02:49.034Z → 2026-05-31T21:40:12.154Z
- `https://openai.com/index/generalizing-from-simulation/` — lastmod: 2026-05-31T08:03:31.673Z → 2026-05-31T21:40:40.969Z
- `https://openai.com/index/generative-language-modeling-for-automated-theorem-proving/` — lastmod: 2026-05-31T08:03:24.954Z → 2026-05-31T21:40:35.600Z
- `https://openai.com/index/glow/` — lastmod: 2026-05-31T08:04:54.149Z → 2026-06-01T01:12:42.131Z
- `https://openai.com/index/gotta-learn-fast/` — lastmod: 2026-05-31T08:03:28.182Z → 2026-05-31T21:40:39.942Z
- `https://openai.com/index/governance-of-superintelligence/` — lastmod: 2026-05-30T05:12:54.304Z → 2026-05-31T20:06:14.753Z
- `https://openai.com/index/government-of-iceland/` — lastmod: 2026-05-31T08:44:58.026Z → 2026-06-01T08:55:53.835Z
- `https://openai.com/index/gpt-2-1-5b-release/` — lastmod: 2026-05-31T08:03:38.113Z → 2026-05-31T21:40:39.939Z
- `https://openai.com/index/gpt-2-6-month-follow-up/` — lastmod: 2026-05-31T08:03:27.999Z → 2026-05-31T21:40:08.278Z
- `https://openai.com/index/gpt-4-research/` — lastmod: 2026-05-31T08:03:33.477Z → 2026-06-01T01:18:19.687Z
- `https://openai.com/index/gpt-4o-system-card/` — lastmod: 2026-05-30T05:13:45.398Z → 2026-05-31T20:06:48.971Z
- `https://openai.com/index/gpt-4v-system-card/` — lastmod: 2026-05-30T05:13:20.408Z → 2026-05-31T20:06:13.502Z
- `https://openai.com/index/gpt-5-amgen/` — lastmod: 2026-05-31T08:17:46.197Z → 2026-06-01T09:13:05.821Z
- `https://openai.com/index/gpt-5-coding-design/` — lastmod: 2026-05-31T08:17:46.020Z → 2026-06-01T09:13:05.385Z
- `https://openai.com/index/gpt-5-cursor/` — lastmod: 2026-05-31T08:17:46.599Z → 2026-06-01T09:13:01.553Z
- `https://openai.com/index/gpt-5-first-look/` — lastmod: 2026-05-31T08:17:11.481Z → 2026-06-01T09:12:36.711Z
- `https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/` — lastmod: 2026-05-31T08:03:46.826Z → 2026-06-01T09:03:31.808Z
- `https://openai.com/index/gpts-are-gpts/` — lastmod: 2026-05-31T08:02:33.137Z → 2026-05-31T21:40:07.160Z

... and 145 more updated pages (see diff.json)

## Removed Pages (0 removed)


## Fetch Failures (0)
