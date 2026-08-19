# Analysis — Run 2026-08-19T09-16Z

**Baseline:** 2026-08-18T09-16Z (consecutive day)
**Fetch time (root sitemap index + all 35 sub-sitemaps):** 2026-08-19T09:16:53Z UTC
**Sub-sitemaps fetched:** 35/35, no errors.
**Total URLs in union:** 1,592 (was 1,585)
**Page fetches attempted:** 221 (7 added + 214 updated). **Failures: 0.**

## 1. Anomalies

None detected.

- No `<lastmod>` values later than fetch time (no future-dated pages).
- No `<lastmod>` values that moved backwards vs. the prior snapshot.
- All 7 newly-added URLs have `<lastmod>` within 1 day of first_seen (no backdating).
- No URL that disappeared in a prior run and reappeared today.
- 4 URLs moved between sub-sitemap categories (all `global-affairs` → `global-affairs-news-listed`, the same new bucket that appeared for the first time yesterday, 2026-08-18):
  - `/global-affairs/new-economic-analysis/`
  - `/index/equipping-workers-with-insights-about-compensation/`
  - `/index/how-countries-can-end-the-capability-overhang/`
  - `/index/understanding-ai-and-learning-outcomes/`
  This reads as OpenAI continuing to migrate global-affairs "news" posts into the bucket introduced yesterday — routine taxonomy cleanup, not flagged as suspicious.

## 2. Significant updates (real content changes, ranked by importance)

### OpenAI discloses a temporary RL-training pause tied to a "Critical" cyber-capability model (new page)
**[`/index/pacing-model-development-cyber-capabilities/`](../../pages/openai.com/index/pacing-model-development-cyber-capabilities/index.md)** — the most substantively important item in this run. OpenAI states that over "the past several weeks," two developments — the previously-disclosed OpenAI–Hugging Face security incident (first covered here 2026-07-21/22) and preliminary evidence that an upcoming model codenamed **Astra** may meet the **"Critical" cybersecurity capability** threshold under OpenAI's Preparedness Framework — pushed them to temporarily slow scaling. Concretely: a **two-week pause in reinforcement-learning (RL) training** on models intended for deployment while they hardened research-cluster security and expanded monitoring; their **largest planned frontier RL run remains on hold**. New measures described: stricter workload/network isolation ("sandboxes") for untrusted code, continuous automated red-teaming of internal boundaries, a new multistage chain-of-thought monitoring system (activation classifiers → automated investigators → human paging within 30 minutes for critical-boundary violations, adding ~20% inference-compute overhead), and expanded alignment training (anti reward-hacking, honesty, unauthorized-access reduction). OpenAI says it determined Astra "may have critical cyber capabilities" as of **August 7, 2026**, and promises a technical report "in the coming weeks" plus involvement of external organizations. This is a direct continuation of the Hugging Face incident / Daybreak cyber-model storyline this repo has tracked since mid-July.

### ChatGPT for Teachers: free period extended a full year
**[`/index/chatgpt-for-teachers/`](../../pages/openai.com/index/chatgpt-for-teachers/index.md)** — every reference to the free-access deadline for verified U.S. K-12 educators was updated from **June 2027 to June 2028**, extending the commitment by a year. Also added a new "Looking for current education solutions?" CTA block linking to `/business/solutions/education/` and `/contact-sales/`, and updated a "higher education" link to point at `chatgpt.com/business/education`.

### Business Partners page: CTA sections restyled
**[`/business/partners/`](../../pages/openai.com/business/partners/index.md)** — the "Become a partner" and "Find a partner" sections were converted from plain heading+paragraph+link blocks into combined heading-link card components with slightly reworded copy ("Enroll in the OpenAI Partner Network" → "Join the OpenAI Partner Network to build, co-sell, and deliver with OpenAI..."). Layout/copy polish, no substantive change in offering.

## 3. Routine, low-signal updates (dominant pattern this run — explained once, not itemized per-page)

Three sitewide template/rotation patterns account for the overwhelming majority of today's 214 lastmod-updated URLs. None represent real content changes to the affected pages:

1. **Global nav/footer refresh (~90 pages).** The site nav swapped its "Latest Advancements" link from **GPT-5.3 Instant** to **GPT-5.6**, and the footer gained three new links: **Customer Stories**, **Partner Network**, and **Supply Co.** This is a single sitewide template change that happened to touch the `<lastmod>` of every page it re-rendered — includes dozens of old research posts (Dota 2, CLIP, Rubik's Cube, DALL-E, GPT-4o/o1 system cards) and 2018-2021 company-history posts (OpenAI Fellows/Scholars cohorts, leadership announcements) that otherwise have zero content change.
2. **"Keep reading" / related-articles carousel refresh (dozens of pages).** Many pages' bottom "Keep reading" card carousel was updated to surface yesterday's (2026-08-18) new posts (Asana, ChatGPT Ads Europe, ChatGPT for Teens, Pacing Model Development, Partnering with CodeAI, Strengthening Democratic Oversight, NVIDIA case study) in place of older cards. This is expected daily churn as the carousel algorithm surfaces recent content — not a change to the hosting page's own content.
3. **Table-of-contents block re-ordering (many long-form pages).** A duplicated/positioned TOC block moved position within the page (appears twice, in different order) with no textual change to its contents — a template quirk, not a content edit.
4. **Partner-badge deploy-ID churn (41 `/business/partners/<company>/` pages).** Only the `dpl_...` query-string cache-buster on the partner-tier badge SVG changed — a deployment artifact with zero visible change. Two of the 41 (**cognita-reply**, **infosys**) additionally flipped from the old-style global nav to the new-style nav — continuing the same unstable nav-template condition first flagged 2026-08-08.

Legal/policy documents checked for substantive text changes and found unchanged (only nav/TOC noise): `/policies/may-2025-business-terms/`, `/policies/nov-2023-business-terms/`, `/policies/services-agreement/`, `/policies/ad-tools-subprocessors/`.

Pages with a `<lastmod>` bump but **zero** content difference (pure server-side re-render, 56 of 214): includes `/index/healthbench/`, `/index/introducing-gpt-oss-safeguard/`, `/trust-and-transparency/`, and most `/business/plugins/*` pages.

## 4. New pages (7)

- **[Asana cleared 5 years of engineering work in 2 weeks with Codex](../../pages/openai.com/index/asana/index.md)** (Company/customer story) — Asana used OpenAI Codex to replace an outdated testing system in two weeks for ~$12K.
- **[ChatGPT Ads expands across Europe](../../pages/openai.com/index/chatgpt-ads-expands-across-europe/index.md)** (Product/Company) — six months after U.S. ad testing began, ChatGPT Ads expands to 31 European markets.
- **[Introducing ChatGPT for Teens: Built for learning, backed by protections](../../pages/openai.com/index/chatgpt-for-teens/index.md)** (Product/Safety) — a teen-oriented ChatGPT experience emphasizing learning support and stronger built-in safety protections.
- **[How NVIDIA scales expertise with ChatGPT Work](../../pages/openai.com/index/nvidia/chatgpt-work/index.md)** (Company/customer story) — NVIDIA teams use ChatGPT Work to reduce manual tasks and scale workflows globally.
- **[Pacing model development in an era of cyber-critical capabilities](../../pages/openai.com/index/pacing-model-development-cyber-capabilities/index.md)** (Company/Publication) — see §2 above; the run's top story.
- **[Partnering with CodeAI to prepare the first AI generation](../../pages/openai.com/index/partnering-with-codeai/index.md)** (Company) — partnership framed around helping students critically evaluate AI outputs rather than just use them.
- **[Strengthening democratic oversight in national security](../../pages/openai.com/index/strengthening-democratic-oversight-in-national-security/index.md)** (Global Affairs) — new initiative to help democratic oversight bodies build expertise to understand and oversee government use of AI for national security.

All seven are dated Aug 17-19, 2026 and consistently appear in each other's "Keep reading" carousels — a single coordinated content-release batch.

## 5. Removals

None this run (0 URLs removed from the sitemap).

## 6. Fetch failures

None. All 221 targeted fetches (7 added + 214 updated) succeeded via `tools/html_to_md.py`.
