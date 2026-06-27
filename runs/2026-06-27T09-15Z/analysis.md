# Run Analysis: 2026-06-27T09-15Z

**Fetch time:** 2026-06-27T09:16:44Z  
**Baseline:** 2026-06-26T09-15Z  
**Total current URLs:** 1380  
**Baseline URLs:** 1375  

---

## ANOMALIES

### Subsitemap Taxonomy Reorganization (114 migrations)

OpenAI performed a large-scale reorganization of their sitemap taxonomy today. 114 URLs moved between sub-sitemaps to reflect more semantically precise categorizations. Key migration patterns:

- **Release announcements** (GPT-5.X, o3/o4, Codex, Sora): moved from `sitemap.xml_product.xml` and `sitemap.xml_company.xml` → `sitemap.xml_release.xml`
- **Security content**: Codex Security, Daybreak, Mixpanel incident, TanStack npm attack → `sitemap.xml_security.xml`
- **Global affairs**: Stargate expansions (UK, UAE, Norway, Michigan, Korea), economic blueprints, policy comments → `sitemap.xml_global-affairs.xml`
- **Global affairs (news listed)**: Equipping Workers, New Economic Analysis, How Countries Can End the Capability Overhang, Understanding AI and Learning Outcomes → `sitemap.xml_global-affairs-news-listed.xml`
- **Learn-OpenAI-on-OpenAI**: Sales assistant, Contract Data Agent, Research Assistant, GTM assistant, Inbound Sales Assistant, Support Model, Building OpenAI with OpenAI → `sitemap.xml_learn-openai-on-openai.xml`
- **Publications**: dal-e-3, PaperBench, research/index, news/research → `sitemap.xml_publication.xml`
- **Research**: Sora-2, GPT-4.1, Aardvark, Rosalind Biodefense, Memory Dreaming, First Proof Submissions, New Capabilities to GPT-Rosalind → `sitemap.xml_research.xml`
- **Webinars**: Put AI to Work series (marketing, finance ops, complex problems) → `sitemap.xml_webinar.xml`
- **Sora**: Sora Vallée-Duhamel, Sora Minne Atairu → `sitemap.xml_sora.xml`; Disney Sora agreement → `sitemap.xml_sora.xml`
- **Collaboration apps**: Atlassian Rovo moved from `apps-data` → `apps-collaboration`
- **Developer tools**: Alpaca app moved from `apps-finance` → `apps-developer-tools`
- **ChatGPT**: Wayfair/Fiona Tan, Stories → `sitemap.xml_chatgpt.xml`
- **Product**: ChatGPT WhatsApp transition, Shopping Research, Our Approach to Advertising → `sitemap.xml_product.xml`
- **Safety**: openai.com/news/ and confidence-building measures → `sitemap.xml_safety.xml`

This appears to be a deliberate taxonomy cleanup—not a content change—suggesting OpenAI restructured their CMS/editorial categorization system or SEO sitemap strategy.

**None of these migrations indicate removed or new content; the underlying pages are unchanged.**

No future-dated lastmod or backwards-moving lastmod anomalies detected.

---

## SIGNIFICANT NEW PAGES

### 1. GPT-5.6 Sol Preview Announcement ⭐ MAJOR
**URL:** https://openai.com/index/previewing-gpt-5-6-sol/  
**Lastmod:** 2026-06-26 (claimed)  
**File:** pages/openai.com/index/previewing-gpt-5-6-sol/index.md

OpenAI announced GPT-5.6, their most capable model family to date, in a limited preview. Three variants:
- **Sol** – flagship model ("strongest model yet")
- **Terra** – balanced for everyday work, competitive with GPT-5.5, 2× cheaper
- **Luna** – fast and affordable at lowest cost

**Key technical features:**
- New `max` reasoning effort (Sol gets maximum thinking time)
- New `ultra` mode: multi-agent, uses subagents to parallelize complex work
- Sets SOTA on Terminal-Bench 2.1 (coding), GeneBench v1 (biology), ExploitBench (cybersecurity)
- Cybersecurity: competitive with "Mythos Preview" using only ~1/3 the tokens

**Government coordination:** Uniquely, OpenAI previewed plans and model capabilities to the U.S. government before launch. At government request, GPT-5.6 is starting with a limited preview for "a small group of trusted partners whose participation has been shared with the government." OpenAI explicitly states this government-first process should NOT become a "long-term default," but is a short-term measure while they work with the Administration on a cyber Executive Order framework.

**Safety stack:** "Most robust safety stack to date" — strengthened protections for higher-risk activity, sensitive cyber requests, and repeated misuse. Multi-week adversarial red-teaming. Does NOT cross the "Cyber Critical" threshold.

**Broad availability** expected "in the coming weeks."

---

### 2. OpenAI for Education – New Solutions Page
**URL:** https://openai.com/business/solutions/education/  
**File:** pages/openai.com/business/solutions/education/index.md

A new dedicated landing page targeting universities, colleges, and K-12 institutions. Marketing tagline: "AI built for campuses that shape what's next." Three core pillars:
- Build student capability for AI-powered workforce
- Expand faculty and staff capacity (reduce administrative friction)
- Accelerate research and discovery

Includes "FPO placeholder image" text in alt tags, suggesting this page went live very recently and some assets are still placeholders. Links to ChatGPT for K-12 teachers.

---

### 3. Trusted Access for Biology Research
**URL:** https://openai.com/form/trusted-access-for-biology-research/  
**File:** pages/openai.com/form/trusted-access-for-biology-research/index.md

New form for vetted organizations to access OpenAI's "mainline models" for biological and life sciences work. Distinct from the existing GPT-Rosalind access form (for "frontier life sciences research" — that remains a separate program). Application requires: verified organizational identity, institutional affiliation, a biology research purpose consistent with institutional mission, and willingness to provide additional documentation. This extends the trusted access tier to a wider range of biology researchers below the Rosalind tier.

---

### 4. Campus Leaders Interest Form
**URL:** https://openai.com/form/openai-campus-leaders-interest-form/  
**File:** pages/openai.com/form/openai-campus-leaders-interest-form/index.md

Interest form for enrolled students (18+, at least 1 year remaining) to become OpenAI campus leaders—community builders who help peers learn AI. Expected commitment: ~6–8 hours/month. Related to the new Education solutions page and the education push.

---

### 5. Professional Services Security Measures Policy
**URL:** https://openai.com/policies/professional-services-security-measures/  
**File:** pages/openai.com/policies/professional-services-security-measures/index.md

New policy document covering security measures applicable to OpenAI's professional services engagements. Likely tied to enterprise/professional services expansion and related compliance requirements.

---

## SIGNIFICANT UPDATES

### Home Page (openai.com/)
- **Featured article replaced**: "Codex for every role, tool, and workflow" → **"Previewing GPT-5.6 Sol: a next-generation model"**
- Hero image changed to Sol/Terra/Luna visual
- Removed "Dreaming: Better memory for a more helpful ChatGPT" (ChatGPT memory research post) from featured section

### Products Release Notes
- **Added**: "Codex Remote GA and DigitalOcean plugin" (Jun 25, 2026) — Codex Remote is now generally available on all ChatGPT plans. New DigitalOcean Droplet Workspace plugin. Updated QR pairing authentication.
- **Added**: "Memory improvements for ChatGPT Business" (Jun 25, 2026) — Improved memory for Business users, with ability to review memory summaries, see "View Sources" on personalized responses, and correct/delete memory. No additional cost.
- Replaced "Large pastes are now attachments" (Jun 22) and "Retiring GPT-5.2 models" (Jun 12) entries as most-recent featured items.

### Signals Page (openai.com/signals/)
- **New research report added**: "The shift to agentic AI: evidence from Codex" (June 2026) — PDF analysis of how agentic AI is shifting work patterns, especially in organizations and at OpenAI itself. Appears simultaneously in both signals/ and signals/research/

### OpenAI + Broadcom Jalapeño Chip Page
- Page updated (lastmod changed). Contains announcement of "Jalapeño" — OpenAI's first Intelligence Processor (AI inference accelerator), co-developed with Broadcom. Key details:
  - Designed specifically for LLM inference, built in 9 months (accelerated by OpenAI models)
  - Engineering samples running ML workloads at production frequency/power, including GPT-5.3-Codex-Spark
  - Performance per watt "substantially better than current state-of-the-art"
  - Multi-generation partnership with Broadcom and Celestica
  - Will be deployed at gigawatt scale
  - Designed to work with all LLMs industry-wide

### Company Announcements Page
- Featured article updated to GPT-5.6 Sol (replacing "Codex for every role")
- "How agents are transforming work" (Jun 25, 2026) now appears in secondary positions

### Academy / Codex Pages (Bulk Update)
- 12 Academy pages received a bulk lastmod update to 2026-06-27T06:54–06:55 UTC
- Pages include: codex-automations, codex-for-work (3 role pages), codex-how-to-start, codex-plugins-and-skills, codex-settings, how-finance-teams-use-codex, what-is-codex, how-to-use-codex-for-everyday-work, working-with-codex
- Content diff shows no substantive changes — likely a CMS metadata or template refresh

### Pricing Pages
- API pricing, business pricing, and ChatGPT pricing pages all received lastmod updates today (Jun 27)
- Content diffs show no substantive changes (likely pricing page metadata refresh, possibly GPT-5.6 pricing added in backend)

### Business Solutions Pages
- Multiple solutions pages updated (data, design, engineering, finance, hr, legal, marketing, research, sales, small-business, enterprises)
- Engineering: Minor capitalization fix ("codex" → "Codex" in one CTA button)
- Others: Likely CMS template or navigation refresh; no substantive content changes

---

## ROUTINE UPDATES

- Various form pages (100-chats-book-request, chatgpt-pro-community, life-sciences-access, partner-network-interest, rosalind-biodefense-program, trademark-counterfeit-disputes, vc-partnerships-application): lastmod updates, no content changes
- Devday page: Minor lastmod change
- Daybreak and Daybreak/Partners: Lastmod updated; no content changes
- UK Online Safety Act policy: Lastmod updated; no content changes
- Customer stories (Morgan Stanley, LSEG, Omio, Plex/Coffee, Samsung Codex deployment): Lastmod updates, likely "related articles" sidebar changes
- GPT-5 immunology mystery, How agents are transforming work, Helping build shared standards for AI: Related articles sidebar rotations

---

## REMOVALS

None.

---

## FETCH FAILURES

None.

---

## SUMMARY STATS

- Total current URLs: 1380
- Added: 5
- Removed: 0
- Updated: 53
- Anomalies: 114 (all subsitemap taxonomy migrations, not content changes)
- Sub-sitemaps: 34
- Fetch failures: 0
