# Run 2026-05-21T09-15Z

**Fetch time:** 2026-05-21T09:17:12Z  
**Baseline:** 2026-05-20T09-16Z (sitemaps/openai.com/sub/latest/)  
**Total URLs (current):** 1318  
**Sub-sitemaps:** 32 (unchanged from prior run)

## Summary

| Category | Count |
|---|---|
| Added | 2 |
| Updated (lastmod changed) | 174 |
| Removed | 7 |
| Anomalies | 0 |
| Fetch failures | 1 |

---

## Anomalies

None detected. No future lastmods, no backwards-moving timestamps, no reappeared URLs.

---

## Significant Updates — Pattern Analysis

The 174 lastmod changes fall into three distinct clusters. Understanding the pattern matters more than treating each update as independent:

### Cluster A: CMS batch deployment (~02:13 UTC, ~100 pages)

Roughly 100 pages under `/index/` received new lastmod timestamps clustered around `2026-05-21T02:13:xx.xxxZ`. **Content inspection shows zero actual content changes** for the pages checked (e.g., `adversarial-attacks-on-neural-network-policies`, `benchmarking-safe-exploration-in-deep-reinforcement-learning`, and many others). This pattern is characteristic of a site-wide CMS deployment that updates lastmod metadata without modifying page content — possibly a template, sitemap generation, or infrastructure change.

### Cluster B: "Keep reading" carousel refresh (~07:30–09:17 UTC, ~70 pages)

A second cluster of pages across research, product, company, and other sections received fresh timestamps between 07:30 and 09:17 UTC. These pages received a single substantive change: their **"Keep reading"** (related articles) section was updated to surface the new discrete geometry conjecture post and the Ramp brand story in place of older featured articles. The actual body content of each article is unchanged.

Affected pages include: `about/`, `api/`, `deep-research/`, `simplex/`, `nvidia/`, `dall-e/`, `databricks/`, `gpt-4-research/`, `hello-gpt-4o/`, `sora/`, `o1/`, `open-models/`, `stories/*`, `signals/*`, `safety/`, `transparency-and-content-moderation/`, and many more.

### Cluster C: Genuine individual updates (small set)

A handful of pages show real content changes beyond carousel rotation:

- **`/index/the-next-phase-of-education-for-countries/`** (09:13 UTC): A single typographic change — an em-dash with surrounding spaces (`— `) replaced by a tighter em-dash (`—`) in a quote block. Purely cosmetic.
- **`/index/building-codex-windows-sandbox/`** (08:47 UTC): Thumbnail image URL changed (different image hash for a related-card asset). Minor asset update.
- **`/solutions/use-case/content-creation/`**: Added new content block about creating UI/UX mockups with ChatGPT. Substantive addition.
- **`/startups/`**: Added ~20 lines of how-to content (sign-up guide for OpenAI platform). Substantive addition.
- **`/signals/data/`**: Minor wording update in the description of privacy-preserving insights section.
- **`/research/verify/`**: Updated terms of service link text in the file upload section.

---

## New Pages (2)

### 1. `/index/model-disproves-discrete-geometry-conjecture/`
**URL:** https://openai.com/index/model-disproves-discrete-geometry-conjecture/  
**Sitemap lastmod:** 2026-05-21T08:41:21.737Z  
**Saved at:** [pages/openai.com/index/model-disproves-discrete-geometry-conjecture/index.md](../../pages/openai.com/index/model-disproves-discrete-geometry-conjecture/index.md)

**Summary:** Major research milestone. An internal OpenAI reasoning model (not a math-specific system) autonomously **disproved the planar unit distance conjecture** first posed by Paul Erdős in 1946 — an 80-year-old open problem in combinatorial geometry. The result proves that for infinitely many point configurations of size n, the number of unit-distance pairs is at least n^(1+δ) for a fixed δ > 0 (a refinement by Princeton's Will Sawin gives δ = 0.014), disproving the long-standing belief that n^(1+o(1)) was essentially optimal.

The proof draws on deep techniques from **algebraic number theory** (infinite class field towers, Golod–Shafarevich theory) — connections mathematicians had not anticipated. The proof was verified by external mathematicians including Fields medalist Tim Gowers, who writes it "is a milestone in AI mathematics" and would recommend it for the Annals of Mathematics "without any hesitation." Noga Alon and Arul Shankar (Princeton) also called it a genuine AI breakthrough in mathematical reasoning.

**Why it matters:** OpenAI claims this is the first time a prominent open problem central to an active mathematical subfield has been solved autonomously by AI — without special training for the problem or custom scaffolding. OpenAI frames it as evidence that AI can contribute to frontier research and not merely assist it. The companion materials include the full proof PDF, external remarks paper, and abridged model chain-of-thought — all hosted on OpenAI's CDN.

This announcement follows the "Parameter Golf" post (May 12, 2026) and fits a broader OpenAI narrative around AI as a research partner. The article was also added to the Research/Milestone sub-sitemap.

### 2. `/index/ramp/`
**URL:** https://openai.com/index/ramp/  
**Sitemap lastmod:** 2026-05-20T20:26:01.608Z  
**Saved at:** [pages/openai.com/index/ramp/index.md](../../pages/openai.com/index/ramp/index.md)

**Summary:** New brand story / customer case study. Ramp (enterprise finance and expense management platform) describes how their AI Developer Experience team uses **Codex with GPT-5.5** for automated code review and internal agentic tooling (on-call rotation management). Austin Ray (AI DevEx lead at Ramp) is quoted calling Codex code review "industry gold standard" that catches issues other engineers and AI tools miss. The piece highlights Codex's deep codebase reasoning for thorough PR feedback in minutes vs. hours.

This is consistent with OpenAI's push to build brand stories around Codex and enterprise developer use cases — following similar posts about Databricks, Dell, and Sea (David Chen).

---

## Removed Pages (7)

Six of the seven removals are product pages under the `/chatgpt/` path on openai.com. These pages appear to have been **migrated to chatgpt.com**. The footer navigation in pages fetched today routes these links directly to chatgpt.com:

| Removed from openai.com | Likely destination |
|---|---|
| `/chatgpt/desktop/` | `chatgpt.com/download` |
| `/chatgpt/education/` | `chatgpt.com/business/education` |
| `/chatgpt/enterprise/` | `chatgpt.com/business/enterprise` |
| `/chatgpt/overview/` | `chatgpt.com/overview` |
| `/chatgpt/pricing/` | `chatgpt.com/pricing` |
| `/chatgpt/team/` | `chatgpt.com/business/business-plan` |
| `/chatgpt/use-cases/student-writing-guide/` | unclear |

**Interpretation:** OpenAI is continuing to consolidate ChatGPT consumer/business product pages onto the chatgpt.com domain. This is a structural brand separation: openai.com is becoming the research/API/company hub while chatgpt.com handles the product experience. The last snapshots of the removed pages are preserved in git history.

---

## Fetch Failures (1)

- **`https://openai.com/deployco/`**: Page returned content that failed the validity check (Cloudflare-blocked fetch or challenge page returned). The lastmod updated from `2026-05-20T03:43:12Z` to `2026-05-21T00:05:32Z`. Prior snapshot preserved. **Needs follow-up** on next run.

---

## Conclusion

Today's standout event is the discrete geometry conjecture post — a rare instance of OpenAI claiming a genuine AI mathematical breakthrough, not a product launch. The ChatGPT page removals represent a continuing structural website reorganization. The 174 "updated" pages are largely a CMS artifact: ~100 are pure timestamp touches with no content change, and most of the rest reflect only the "Keep reading" carousel rotating in the new geometry post and Ramp story. The only substantive content additions were on `/solutions/use-case/content-creation/` and `/startups/`.
