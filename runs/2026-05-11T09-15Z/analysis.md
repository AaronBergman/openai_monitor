# Run 2026-05-11T09-15Z Analysis

**Fetch time:** 2026-05-11T09:17:28Z  
**Baseline:** 2026-05-10T09-16Z  
**Total current URLs:** 1289  
**Added:** 2  **Updated:** 122  **Removed:** 0  
**Anomalies:** 0  **Fetch failures:** 0

---

## Anomalies

None detected.

---

## Significant Updates

### Fine-tuning platform shutdown notices (confirmed this run)
Three pages — `/index/introducing-vision-to-the-fine-tuning-api/`, `/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/`, and `/index/gpt-4o-fine-tuning/` — all carry the retroactive shutdown notice added on May 8, 2026:

> *"OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users but existing users of the fine-tuning platform will be able to create training jobs for the coming months. All fine-tuned models will remain available for inference until their base models are deprecated."*

These pages were lastmod-refreshed again today (2026-05-11), suggesting CMS metadata churn. The core content is unchanged from the May 8 snapshot. This was first caught in the 2026-05-10 run.

### OpenAI Academy — link URL scheme change
`/academy/building-with-ai/` and `/academy/chatgpt-for-education/` both received small content changes. The diff shows the same learning track links now point to `(opens in a new window)` URLs under `academy.openai.com/home/collections/...` instead of `academy.openai.com/home/clubs/...`. This is an internal Academy URL restructuring — same content, new URL paths.

### Microsoft partnership amendment — `/index/next-phase-of-microsoft-partnership/`
Page was refreshed (lastmod 2026-05-09 → 2026-05-10). Key terms from the page: Microsoft remains primary cloud partner; OpenAI's products ship first on Azure but OpenAI can now serve products on **any cloud provider**; Microsoft's license is now **non-exclusive** (was exclusive); Microsoft no longer pays revenue share to OpenAI; OpenAI's revenue share payments to Microsoft continue through 2030 subject to a total cap; Microsoft continues as major shareholder. This was published earlier but the sitemap refresh suggests possible minor edit.

### Privacy policy cluster update (May 7)
Five policy pages updated simultaneously:
- `/policies/cookie-policy/` — lastmod advanced from 2026-02-25 to 2026-05-08; "Last updated: May 6, 2026" now shown in-page. Cookie table now includes entries for `deploymentsafety.openai.com` and `ads.openai.com` domains, reflecting the ads platform rollout.
- `/policies/communications-privacy-policy/` — 2026-05-05 → 2026-05-07
- `/policies/services-communications-privacy-policy/` — 2026-05-05 → 2026-05-07
- `/policies/services-privacy-policy/` — 2026-04-29 → 2026-05-07
- `/policies/us-privacy-policy/` — 2026-05-05 → 2026-05-07

The cookie policy update is the most substantive: adding `ads.openai.com` to the necessary cookies table aligns with the "Testing ads in ChatGPT" announcement from May 7 (not yet in the sitemap but referenced in page footers).

### Startups page refreshed today
`/startups/` lastmod advanced to 2026-05-11. Content unchanged from prior snapshot (same size), suggesting a related-posts block rotation.

### Mass customer-story metadata refresh
~60 `/index/` customer story pages (e.g., `/index/uber/`, `/index/cisco/`, `/index/bbva/`, `/index/grab/`, etc.) all show lastmod bumped from 2026-05-10 to 2026-05-11. Content lengths are unchanged. This is a routine CMS template/metadata flush, consistent with what was seen on prior runs. No editorial changes to customer story content.

### Signals section refresh (May 8)
All five `/signals/` pages (`/signals/`, `/signals/data/`, `/signals/data-download/`, `/signals/b2b/`, `/signals/research/`) received a synchronized lastmod bump (2026-05-06 → 2026-05-08). Content sizes appear unchanged — likely a CMS template update.

### Healthcare and Coding Solutions pages
`/solutions/industries/healthcare/` (2026-04-26 → 2026-05-08) and `/solutions/use-case/coding/` (2026-05-05 → 2026-05-08) updated. Consistent with the broader Codex/GPT-5 push this week.

---

## New Pages

### https://openai.com/business/guides-and-resources/how-enterprises-are-scaling-ai/
- **lastmod:** 2026-05-11T05:31:50.678Z
- **Sub-sitemap:** `/sitemap.xml/learn-guides/`
- **Title:** How enterprises are scaling AI
- **Published:** May 11, 2026 (same day as first_seen)
- **Summary:** A new enterprise guide drawing on interviews with executives at Philips, BBVA, Mirakl, Scout24, JetBrains, and Scania. Documents five patterns observed across organizations successfully scaling AI: (1) culture/literacy before tooling; (2) governance as an enabler — security, legal, and compliance brought in early; (3) ownership over consumption — teams redesigning workflows rather than just "using" AI; (4) quality before scale — defining what "good" means and investing in evaluation; (5) protecting judgment work — hybrid workflows keeping human oversight. Links to a downloadable PDF ("Frontiers of AI Executive Guide"). Targeted at European enterprise leaders, part of OpenAI's B2B content strategy.

### https://openai.com/index/openai-campus-network-student-club-interest-form/
- **lastmod:** 2026-05-11T05:49:05.071Z
- **Sub-sitemap:** `/sitemap.xml/company/`
- **Title:** OpenAI Campus Network: Student club interest form
- **Published:** May 11, 2026
- **Summary:** OpenAI is partnering with student clubs at universities worldwide. Form collects university name, country, club name, and club type. Benefits include hands-on AI learning resources, support for student-led events/workshops/research, early access to tools and programs, and connection to other student leaders. Referenced in the footer of the recently updated `/index/next-phase-of-microsoft-partnership/` page. Represents an expansion of OpenAI's educational footprint beyond the Academy formal content.

---

## Removed URLs

None.

---

## Fetch Failures

None.

---

## Pattern Notes

This run catches up on changes across May 7–11 from the prior baseline (2026-05-10). The dominant themes:

1. **Codex everywhere** — Codex pages, forms, Academy tracks, and customer stories all refreshed. Codex was made generally available around May 7 (per `/index/codex-now-generally-available/`).
2. **Ads infrastructure** — Cookie policy now lists `ads.openai.com`; the "Testing ads in ChatGPT" post from May 7 is referenced in multiple page footers but not yet a standalone URL in the sitemap.
3. **Fine-tuning wind-down** — The self-serve fine-tuning platform is shutting down; pages are carrying shutdown notices.
4. **Microsoft partnership restructured** — Non-exclusive license, any-cloud serving, revenue share capped.
5. **Safety product launch** — "Trusted Contact" for ChatGPT (May 7) lets users designate a trusted person to be notified in crisis situations.
6. **DevDay 2026** — September 29 in San Francisco. Sign-up live at `/index/devday-2026/`.
7. **GPT-5.5-Cyber** — Specialized model for critical-infrastructure defenders, limited preview.
