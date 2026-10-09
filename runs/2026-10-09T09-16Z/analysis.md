# Run 2026-10-09T09-16Z Analysis

**Fetch time:** 2026-10-09T09:16:50Z  
**Baseline:** 2026-09-28T09-17Z  
**Total current URLs:** 2026  
**Added:** 42  **Updated:** 952  **Removed:** 1  
**Anomalies:** 5  **Fetch failures:** 0

## Summary

First run in 11 days (prior baseline 2026-09-28T09-17Z), so a big batch. OpenAI's DevDay 2026 (pages [/devday/2026/](pages/openai.com/devday/2026/index.md), [recap](pages/openai.com/index/devday-2026-recap/index.md)) landed, with ~20 announcements. Headline pages: **GPT-6.1 Sol** ([page](pages/openai.com/index/introducing-gpt-6-1-sol/index.md); claims near-GPT-6-Astra capability on coding/computer use at about one-fifth the price, cached input $0.10/M tokens); **dots** ([page](pages/openai.com/index/introducing-dots/index.md); persistent always-on agents with their own cloud computer, rolling out on Pro/Business Premium/Enterprise); **GPT-6 and "Intelligent UI" for everyone** ([page](pages/openai.com/index/gpt-6-for-everyone/index.md); interactive answers for ChatGPT's 1.2B weekly users); a **new visual ad format in ChatGPT** ([page](pages/openai.com/index/new-chatgpt-ads-format-and-measurement/index.md); testing on Free/Go plans during image generation, US, later this month); and two security reports: a **coordinated model-distillation campaign** ([page](pages/openai.com/index/disrupting-a-coordinated-model-distillation-campaign/index.md); attackers tried to extract protected reasoning starting July 1) and **AI-enabled "false front" operations** ([page](pages/openai.com/index/disrupting-ai-enabled-false-front-operations/index.md)). Also new: a Business marketplace and three plugin pages, Atlassian/Ironclad/Oracle/Jump Trading/Albertsons customer stories, and several interest forms (Private Intelligence, Sign in with ChatGPT, Codex Originals, computer-use research collaboration). 952 existing pages were touched, mostly site-wide nav/footer changes (GPT-6.1 Sol, dots and Plugins links added; Codex/GPT-5.4 links dropped). Counts: +42 added, 952 updated, -1 removed (/form/ultrafast/, first seen 2026-08-20), 5 anomalies (see below).

Note: the 11-day gap since baseline explains the large added/updated counts. No fetch failures.

## Anomalies (Highest Signal)

- **future_lastmod**: `https://openai.com/form/copyright-disputes/`
  - lastmod 2026-10-09T09:16:50.288Z is after fetch time 2026-10-09T09:16:50Z
- **backdated_new_url**: `https://openai.com/codex-originals/`
  - New URL has lastmod 2026-10-01T18:38:17.113Z which is 8 days before first_seen 2026-10-09T09-16Z
- **backdated_new_url**: `https://openai.com/form/private-intelligence-interest/`
  - New URL has lastmod 2026-10-01T03:03:00.758Z which is 8 days before first_seen 2026-10-09T09-16Z
- **reappeared_url**: `https://openai.com/business/plugins/alpaca/`
  - URL was previously seen (last_seen: 2026-09-24T09-16Z, first_seen: 2026-07-10T09-16Z), disappeared, and reappeared
- **reappeared_url**: `https://openai.com/policies/row-privacy-policy/`
  - URL was previously seen (last_seen: 2026-05-27T09-17Z, first_seen: 2026-05-07T09-01Z), disappeared, and reappeared

## Updated Pages

### https://openai.com/
- lastmod: `2026-09-23T19:49:50.418Z` → `2026-10-07T18:39:11.912Z`
- Content length: 9810 → 10125 chars (delta: +315)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Intelligent-UI Art-Card 16x9](https://images.ctfassets.net/kftzwdyauwt9/5frqtUAWccstAbVrCFraH6/5ae9b6bfbc3f3dff8001ed2
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Learn about ChatGPT Business](</business/>)[Talk with ChatGPT(opens in a new window)](<https://chatgpt.com/?mode=voice>
  + [Advancing computer use with IroncladPublicationOct 6, 2026](</index/advancing-computer-use-with-ironclad/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - [Learn about ChatGPT Business](</business/>)[Talk with ChatGPT](<https://chatgpt.com/?mode=voice>)[Research](</research/
  - [Paul Christiano joins OpenAI Foundation BoardCompanySep 9, 2026](</index/paul-christiano-joins-openai-foundation-board/
  - ![Paul Christiano joins OpenAI Foundation Board — card](https://images.ctfassets.net/kftzwdyauwt9/4PcDbhz75I70TjyGat7oHl

### https://openai.com/about/
- lastmod: `2026-09-25T18:59:48.324Z` → `2026-10-09T04:30:21.082Z`
- Content length: 6769 → 6834 chars (delta: +65)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [GPT‑6 Sol and GPT‑6 Luna: October 2026 updateSafetyOct 7, 2026(opens in a new window)](<https://deploymentsafety.openai
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  - [Build more natural voice experiences with GPT‑Live‑1 in the APIProductSep 10, 2026](</index/introducing-gpt-live-1-in-t
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  -   * [Codex](</codex/>)
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)

### https://openai.com/academy/chatgpt-sites/
- lastmod: `2026-07-09T17:38:27.739Z` → `2026-10-05T21:12:23.998Z`
- Content length: 12511 → 12917 chars (delta: +406)
- Sample new content lines:
  + ![Academy > Getting started > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/1Xk9723QKj2Vb9dC6RMebS/5e588c112042
  + [How data science teams use ChatGPT Work | OpenAIOpenAI AcademyJul 14, 2026](</academy/chatgpt-work/how-data-science-tea
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![How data science teams use Codex > card image](https://images.ctfassets.net/kftzwdyauwt9/xyevYnp4Ptaa1eMgBDNjS/75fea80
- Sample removed content lines:
  - [Settings | OpenAIOpenAI AcademyApr 23, 2026](</academy/codex-settings/>)
  -   * [Codex](</codex/>)
  - [Plugins and skills | OpenAIOpenAI AcademyApr 23, 2026](</academy/codex-plugins-and-skills/>)
  - [Automations | OpenAIOpenAI AcademyApr 23, 2026](</academy/codex-automations/>)
  - ![Automations > card image](https://images.ctfassets.net/kftzwdyauwt9/WWbNfZvQUCV942pR9wPFw/69567e99135e87f695b94809ac02

### https://openai.com/api-fast-mode/
- lastmod: `2026-09-25T14:01:55.817Z` → `2026-09-30T19:31:35.037Z`
- Content length: 12153 → 12393 chars (delta: +240)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + GPT-6.1 Sol| $4.00| $0.20| $20.00| $8.00| $0.40| $30.00| —| —  
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/api-reserved-tier/
- lastmod: `2026-09-23T21:18:33.666Z` → `2026-10-09T05:24:12.828Z`
- Content length: 8841 → 9017 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/api-scale-tier/
- lastmod: `2026-09-10T15:58:18.784Z` → `2026-10-09T05:32:05.577Z`
- Content length: 13285 → 13503 chars (delta: +218)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/api/
- lastmod: `2026-09-25T14:14:26.339Z` → `2026-10-09T08:28:23.826Z`
- Content length: 11169 → 11683 chars (delta: +514)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Learn more(opens in a new window)(opens in a new window)](<https://developers.openai.com/api/docs/models/gpt-6-astra>)[!
  + [Register now(opens in a new window)](<https://webinar.openai.com/register/voice-assistants-everyday-apps/?utm_source=we
  + Join us October 13 at 9:30 AM PDT to hear how Cognition integrated GPT‑Live‑1 into Devin—and saw 40% more sessions.
- Sample removed content lines:
  -   * Knowledge cut-off: Apr 20, 2026
  - Learn more(opens in a new window)(opens in a new window)](<https://developers.openai.com/api/docs/models/gpt-6-sol>)[![]
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/approach-to-patents/
- lastmod: `2026-06-11T17:39:16.362Z` → `2026-10-06T22:55:31.999Z`
- Content length: 3941 → 4188 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/brand/
- lastmod: `2026-09-02T04:44:32.790Z` → `2026-10-06T23:06:01.022Z`
- Content length: 17852 → 18105 chars (delta: +253)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/build-week/
- lastmod: `2026-09-07T16:35:59.779Z` → `2026-10-09T04:53:35.561Z`
- Content length: 9026 → 9238 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business-data/
- lastmod: `2026-09-28T00:31:18.165Z` → `2026-10-09T02:40:17.576Z`
- Content length: 13854 → 14053 chars (delta: +199)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [OpenAI Trust PortalLearn more(opens in a new window)](<https://trust.openai.com/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [OpenAI Trust PortalLearn more](<https://trust.openai.com/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/
- lastmod: `2026-09-28T02:34:15.644Z` → `2026-10-09T06:11:39.353Z`
- Content length: 8445 → 8644 chars (delta: +199)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Join the livestream on September 29\--d : --h : --m(opens in a new window)](<https://devday.openai.com/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Join the livestream on September 29\--d : --h : --m](<https://devday.openai.com/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/contact-sales-financial-services/
- lastmod: `2026-09-21T16:34:06.213Z` → `2026-10-06T12:16:07.157Z`
- Content length: 3865 → 4041 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/contact-sales-legal/
- lastmod: `2026-09-24T19:10:19.298Z` → `2026-10-06T12:16:07.849Z`
- Content length: 3902 → 4078 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/customer-stories/
- lastmod: `2026-09-25T19:12:46.165Z` → `2026-10-09T05:55:57.573Z`
- Content length: 10144 → 10294 chars (delta: +150)
- Sample new content lines:
  + ![Jump Trading — Layered ink art card](https://images.ctfassets.net/kftzwdyauwt9/205v65rL5MtphsvognlJEK/d76a782480cf109c
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Chatham Financial — Art card, Getty texture](https://images.ctfassets.net/kftzwdyauwt9/01pb50tQohDn4kZa58YtWh/2a35d510
- Sample removed content lines:
  - ![Fyxer customer story 1x1 image](https://images.ctfassets.net/kftzwdyauwt9/7LbXXCnX1NLyS1i8mHGF1i/d75fdf2bf63cf463ce2e7
  - [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  - [How Cooley is accelerating IPO work with ChatGPTSep 17, 2026](</index/cooley-gopublic/>)
  - ![Perplexity customer story art card](https://images.ctfassets.net/kftzwdyauwt9/wGvW7AaxivnlRvLvZU7CE/146fd791b18b52b67d
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/guides-and-resources/identifying-and-scaling-ai-use-cases/
- lastmod: `2026-09-21T20:28:37.540Z` → `2026-10-08T19:09:18.346Z`
- Content length: 33388 → 33524 chars (delta: +136)
- Sample new content lines:
  + [The builder’s guide to GPT‑5.6Applied AIAug 13, 2026](</index/builders-guide-to-gpt-5-6/>)
  + ![A model guide for the GPT-6 family — Card image](https://images.ctfassets.net/kftzwdyauwt9/4I32Z0klAF95wPuspoHaxb/7388
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [How to manage AI investments in the agentic eraAI AdoptionJul 14, 2026](</index/managing-ai-investments-in-agentic-era/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [ChatGPT usage and adoption patterns at workGuidesJan 22, 2026](</business/guides-and-resources/chatgpt-usage-and-adopti
  - ![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168b
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/guides-and-resources/inside-gpt5-our-best-model-for-work/
- lastmod: `2026-09-21T20:28:38.743Z` → `2026-10-09T00:24:29.461Z`
- Content length: 12184 → 12320 chars (delta: +136)
- Sample new content lines:
  + [The builder’s guide to GPT‑5.6Applied AIAug 13, 2026](</index/builders-guide-to-gpt-5-6/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [How to manage AI investments in the agentic eraAI AdoptionJul 14, 2026](</index/managing-ai-investments-in-agentic-era/
  + ![The builder’s guide to GPT-5.6 — Card image — Neutral Option 075](https://images.ctfassets.net/kftzwdyauwt9/4jmIFt2vH2
- Sample removed content lines:
  - [ How enterprises are scaling AIGuidesMay 11, 2026](</business/guides-and-resources/how-enterprises-are-scaling-ai/>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [ChatGPT usage and adoption patterns at workGuidesJan 22, 2026](</business/guides-and-resources/chatgpt-usage-and-adopti
  - ![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168b

### https://openai.com/business/intelligence-at-work/
- lastmod: `2026-08-24T17:54:01.809Z` → `2026-10-06T12:16:06.564Z`
- Content length: 3751 → 3998 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/
- lastmod: `2026-09-07T16:36:01.414Z` → `2026-10-08T22:54:10.031Z`
- Content length: 21003 → 21259 chars (delta: +256)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ## [A model guide for the GPT‑6 familyPractical tips for getting the best results from GPT‑6 models while managing time 
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The state of enterprise AIWhat we’re learning about AI at work.](</business/guides-and-resources/the-state-of-enterpris
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![purpe background with text saying 2025 report](https://images.ctfassets.net/kftzwdyauwt9/4ZGABEHtog5MoDmj5V6OY1/e0fbf3

### https://openai.com/business/learn/agent-security-enterprise/
- lastmod: `2026-09-21T20:10:21.464Z` → `2026-10-05T20:14:34.773Z`
- Content length: 3619 → 3795 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/download-the-chatgpt-work-guide-for-data-teams/
- lastmod: `2026-09-21T20:52:44.954Z` → `2026-10-06T01:26:21.020Z`
- Content length: 3604 → 3780 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/download-the-chatgpt-work-guide-for-finance-teams/
- lastmod: `2026-09-17T22:27:30.594Z` → `2026-10-06T01:32:45.000Z`
- Content length: 3539 → 3751 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/download-the-chatgpt-work-guide-for-marketing-teams/
- lastmod: `2026-09-17T22:20:34.823Z` → `2026-10-06T03:33:01.161Z`
- Content length: 3544 → 3756 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/download-the-chatgpt-work-guide-for-sales-teams/
- lastmod: `2026-08-24T10:11:07.526Z` → `2026-10-05T20:15:47.184Z`
- Content length: 3489 → 3736 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/gartner-2026-agentic-coding-leader/
- lastmod: `2026-09-23T20:42:03.314Z` → `2026-10-09T06:33:29.685Z`
- Content length: 4500 → 4676 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/gartner-2026-enterprise-ai-assistants-leader/
- lastmod: `2026-09-15T23:19:03.904Z` → `2026-10-08T20:59:20.884Z`
- Content length: 5014 → 5231 chars (delta: +217)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/how-our-data-analytics-team-uses-chatgpt-work/
- lastmod: `2026-09-26T16:04:20.874Z` → `2026-10-08T20:54:39.927Z`
- Content length: 3649 → 3825 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/how-our-marketing-team-uses-chatgpt-work/
- lastmod: `2026-09-26T16:01:45.565Z` → `2026-10-07T19:35:51.361Z`
- Content length: 3592 → 3768 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/how-our-sales-team-uses-chatgpt-work/
- lastmod: `2026-09-15T01:06:06.116Z` → `2026-10-08T19:22:09.298Z`
- Content length: 3649 → 3861 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/intelligence-at-work-cyber/
- lastmod: `2026-09-09T07:45:12.889Z` → `2026-10-06T06:39:06.660Z`
- Content length: 3723 → 3935 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/learn/intelligence-at-work-financial-services/
- lastmod: `2026-09-11T16:49:17.829Z` → `2026-10-06T05:37:01.682Z`
- Content length: 3626 → 3838 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/model/
- lastmod: `2026-09-19T16:58:03.156Z` → `2026-10-09T08:45:24.582Z`
- Content length: 8082 → 8294 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/
- lastmod: `2026-09-25T20:30:21.907Z` → `2026-10-08T00:17:47.531Z`
- Content length: 45886 → 46586 chars (delta: +700)
- Sample new content lines:
  + ### [Virgin Atlantic Joins OpenAI and Tomoro to Launch the World’s First Airline Experience in ChatGPTLearn more(opens i
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Enterprise AI Adoption: Moving from Experimentation to Transformation with Bain & CompanyLearn more(opens in a new 
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Context engineering with OpenAI: How enterprises make AI agents production-readyLearn more(opens in a new window)](
- Sample removed content lines:
  - ### [Context engineering with OpenAI: How enterprises make AI agents production-readyLearn more](<https://fractal.ai/blo
  -   * [Codex](</codex/>)
  - ### [Virgin Atlantic Joins OpenAI and Tomoro to Launch the World’s First Airline Experience in ChatGPTLearn more](<https
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Enterprise AI Adoption: Moving from Experimentation to Transformation with Bain & CompanyLearn more](<https://forum

### https://openai.com/business/partners/altimetrik/
- lastmod: `2026-08-28T18:56:38.667Z` → `2026-10-08T19:01:27.873Z`
- Content length: 4331 → 4578 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/artium/
- lastmod: `2026-08-28T18:56:31.913Z` → `2026-10-08T19:01:27.673Z`
- Content length: 4437 → 4684 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/blend360/
- lastmod: `2026-08-24T17:39:13.252Z` → `2026-10-08T19:01:27.815Z`
- Content length: 4472 → 4719 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_7297xwZ764mVMEJDxDT2nr35Qnfp)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/canva/
- lastmod: `2026-09-23T18:09:20.713Z` → `2026-10-09T08:29:56.823Z`
- Content length: 10429 → 10605 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/cloudwerx/
- lastmod: `2026-08-28T18:56:40.572Z` → `2026-10-08T19:01:27.726Z`
- Content length: 4446 → 4693 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3bW43)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/cognizant/
- lastmod: `2026-08-28T18:56:30.782Z` → `2026-10-08T19:01:25.312Z`
- Content length: 4495 → 4742 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/deepsense-ai/
- lastmod: `2026-08-28T18:56:37.985Z` → `2026-10-08T19:01:26.604Z`
- Content length: 4810 → 5057 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/distyl-ai/
- lastmod: `2026-09-11T15:13:57.834Z` → `2026-10-08T19:01:23.640Z`
- Content length: 4529 → 4741 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_A9S7ia9F893jG5rZXgoZ3i2uZZWt)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/eliza/
- lastmod: `2026-08-28T18:56:31.624Z` → `2026-10-08T19:01:26.310Z`
- Content length: 4309 → 4556 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/endava/
- lastmod: `2026-09-18T06:59:45.816Z` → `2026-10-08T00:17:48.994Z`
- Content length: 4467 → 4679 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_DytABQsw94uz64J9325cLDf1x
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/exl-service/
- lastmod: `2026-09-25T20:30:15.402Z` → `2026-10-08T19:01:24.090Z`
- Content length: 4642 → 4818 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_FQVT5KKASWjBBFjsRNgKJ7PnGJVy)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/fractal/
- lastmod: `2026-08-28T18:56:32.023Z` → `2026-10-08T19:01:27.802Z`
- Content length: 4682 → 4929 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/gusto/
- lastmod: `2026-09-20T17:10:04.692Z` → `2026-10-07T18:07:49.072Z`
- Content length: 9765 → 9977 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/hubspot/
- lastmod: `2026-09-24T10:57:03.065Z` → `2026-10-08T18:42:09.300Z`
- Content length: 11308 → 11484 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/merantix-momentum/
- lastmod: `2026-08-28T18:56:39.104Z` → `2026-10-08T19:01:26.766Z`
- Content length: 4356 → 4603 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3bW43)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/nablon-ai/
- lastmod: `2026-08-28T18:56:31.929Z` → `2026-10-08T19:01:26.091Z`
- Content length: 4445 → 4692 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3bW43)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/quantiphi/
- lastmod: `2026-09-21T17:12:48.709Z` → `2026-10-08T19:01:24.402Z`
- Content length: 4625 → 4801 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_6oMMtnEaoU34WkDpyaWsCF5Gv8CA)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/quantium/
- lastmod: `2026-09-17T19:22:30.073Z` → `2026-10-07T00:09:11.100Z`
- Content length: 4343 → 4555 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_DytABQsw94uz64J9325cLDf1x65x)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/quickbooks/
- lastmod: `2026-09-24T11:22:02.713Z` → `2026-10-08T18:48:15.402Z`
- Content length: 10780 → 10956 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/sia/
- lastmod: `2026-08-28T18:56:31.175Z` → `2026-10-08T19:01:27.141Z`
- Content length: 4409 → 4656 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/slalom/
- lastmod: `2026-09-03T22:06:27.779Z` → `2026-10-08T19:01:24.401Z`
- Content length: 4628 → 4840 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_A14pXtnVVdwRZKa69XezyxJEd
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/snorkel-ai/
- lastmod: `2026-08-28T18:56:39.614Z` → `2026-10-08T19:01:27.401Z`
- Content length: 4320 → 4567 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3bW43)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/stripe/
- lastmod: `2026-09-22T00:31:16.357Z` → `2026-10-08T12:11:39.441Z`
- Content length: 10225 → 10401 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/tcs/
- lastmod: `2026-09-17T16:46:14.872Z` → `2026-10-08T00:19:04.157Z`
- Content length: 4894 → 5106 chars (delta: +212)
- Sample new content lines:
  + ![Elite Partner](/images/partner-tier-badges/OAI_PartnerNetwork_ElitePartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - ![Elite Partner](/images/partner-tier-badges/OAI_PartnerNetwork_ElitePartner.svg?dpl=dpl_DytABQsw94uz64J9325cLDf1x65x)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/tredence/
- lastmod: `2026-08-28T18:56:29.396Z` → `2026-10-08T19:01:25.301Z`
- Content length: 4349 → 4596 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiXrfV)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Select Partner](/images/partner-tier-badges/OAI_PartnerNetwork_SelectPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3bW43)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/partners/tribe-ai/
- lastmod: `2026-08-28T18:56:40.209Z` → `2026-10-08T19:01:27.500Z`
- Content length: 4678 → 4925 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_2s25yhRNvVXuY6zXzEYiSXTiX
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Advanced Partner](/images/partner-tier-badges/OAI_PartnerNetwork_AdvancedPartner.svg?dpl=dpl_8zRkpxed5hBwdqpwBygFpwR3b
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/plugins/
- lastmod: `2026-09-25T18:54:49.105Z` → `2026-10-09T06:01:13.936Z`
- Content length: 25447 → 25597 chars (delta: +150)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [![](https://files.openai.com/content?id=file_00000000990481fd9c316ee59df47fc5&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=8&s
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000990481fd9c316ee59df47fc5&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=8&s
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/plugins/activecampaign/
- lastmod: `2026-09-25T15:12:07.716Z` → `2026-10-08T01:48:09.417Z`
- Content length: 12103 → 12665 chars (delta: +562)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4fb1116fe4819198f372bd1dc45b
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4fb1116fe4819198f372bd1dc45b
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4fb1116fe4819198f372bd1dc45b
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_000000009c7c81f78f1a1b859cb8fad3&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://community.activecampaign.com/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40ActiveCampaign+Prepare+a+brief+on+l
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40ActiveCampaign+Compare+my+latest+fi

### https://openai.com/business/plugins/adobe-acrobat/
- lastmod: `2026-09-25T00:28:09.418Z` → `2026-10-08T01:47:37.511Z`
- Content length: 12029 → 12577 chars (delta: +548)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.adobe.com/privacy/policy.html>)
  + [![](https://files.openai.com/content?id=file_000000000c1871f5a6cfddb62a46e9de&cdn=1&cp=pi&ma=31363200&ts=0&p=pi&cid=1&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6938a7d323f48191aeabaf579802bf
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000e4a8720c9b8cba8aaa6e4f70&cdn=1&cp=pi&ma=30672000&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Adobe+Acrobat+Convert+this+scanned+
  - [![](https://files.openai.com/content?id=file_000000000c1871f5a6cfddb62a46e9de&cdn=1&cp=pi&ma=31363200&ts=0&p=pi&cid=1&s

### https://openai.com/business/plugins/adobe-express/
- lastmod: `2026-09-25T00:33:07.031Z` → `2026-10-08T01:46:48.787Z`
- Content length: 12080 → 11873 chars (delta: -207)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_699d522f170c81919c824678c7c037
  +   * ![](https://files.openai.com/content?id=file_00000000e3a881f5870707d01fe1a4c3&cdn=1&cp=pi&ma=32313600&ts=0&p=pi&cid=
  + [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_699d522f170c81919c824678c7c037
  + Create flyers, posts, and graphics quickly
- Sample removed content lines:
  -   * ![](https://files.openai.com/content?id=file_00000000939071f7bfd24cf1e8d5f5fb&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Adobe+Express+Build+a+simple+templa
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Adobe+Express+Create+holiday+themed
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)

### https://openai.com/business/plugins/adobe/
- lastmod: `2026-09-25T00:27:11.714Z` → `2026-10-08T01:46:45.406Z`
- Content length: 13102 → 13846 chars (delta: +744)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69312da8e4dc81919370cb86fd172b
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69312da8e4dc81919370cb86fd172b
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.adobe.com/privacy/policy.html>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Adobe+Retouch+this+set+of+photos+by
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Adobe+Create+a+flyer+for+a+local+yo

### https://openai.com/business/plugins/adspirer/
- lastmod: `2026-09-25T00:33:15.681Z` → `2026-10-08T01:47:55.844Z`
- Content length: 12589 → 13189 chars (delta: +600)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69461dc91ee48191ae4a14eb9bde1c
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.adspirer.com/privacy>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69461dc91ee48191ae4a14eb9bde1c
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Adspirer+Compare+spend%2C+clicks%2C
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - ### [Privacy policyLearn more](<https://www.adspirer.com/privacy>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/affinity/
- lastmod: `2026-09-25T00:36:21.187Z` → `2026-10-08T01:34:14.850Z`
- Content length: 12290 → 12895 chars (delta: +605)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000972881f4b656fa26a2a6961c&cdn=1&cp=pi&ma=31363200&ts=0&p=pi&cid=8&s
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69f3d73626a48191bbd357acfd04db
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Affinity+Prepare+a+brief+for+this+a
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Affinity+Review+my+open+deals+and+i
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.affinity.co/legal/privacy-policy>)

### https://openai.com/business/plugins/aha/
- lastmod: `2026-09-25T00:30:04.884Z` → `2026-10-08T01:34:17.675Z`
- Content length: 11011 → 11654 chars (delta: +643)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.aha.io/privacy>)
  + [![](https://files.openai.com/content?id=file_00000000d94481f7a5d7fe678c79e2d3&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.aha.io/privacy>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Aha%21+What+features+are+scheduled+
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Aha%21+Draft+release+notes+for+the+

### https://openai.com/business/plugins/ahrefs/
- lastmod: `2026-09-25T00:30:51.959Z` → `2026-10-08T01:47:20.020Z`
- Content length: 12497 → 13083 chars (delta: +586)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6966958473488191b775fdb667c52e
  + ### [Privacy policyLearn more(opens in a new window)](<https://ahrefs.com/legal/privacy-policy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://ahrefs.com/legal/privacy-policy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://support@ahrefs.com>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/aiera/
- lastmod: `2026-09-25T00:37:49.242Z` → `2026-10-08T14:59:54.811Z`
- Content length: 11423 → 12001 chars (delta: +578)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_000000002b7871f5a267251ef905a906&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=1&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6967ddccc88881918a3733322b6bdf
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help@aiera.com>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Aiera+Assess+this+investment+thesis
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/airtable/
- lastmod: `2026-09-25T00:37:26.874Z` → `2026-10-08T01:47:54.755Z`
- Content length: 11263 → 11846 chars (delta: +583)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693ca6ce2db08191bb52d66743c651
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693ca6ce2db08191bb52d66743c651
  + [![](https://files.openai.com/content?id=file_000000005c2481fd858f93b128aaef20&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Airtable+Summarize+our+%5Bbase%5D+i
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Privacy policyLearn more](<https://www.airtable.com/company/privacy>)

### https://openai.com/business/plugins/alpha-vantage/
- lastmod: `2026-09-25T00:35:28.130Z` → `2026-10-08T14:59:54.563Z`
- Content length: 12761 → 13299 chars (delta: +538)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.alphavantage.co/privacy/>)
  + [![](https://files.openai.com/content?id=file_00000000fba471f48bacd72c83ca6ee3&cdn=1&cp=pi&ma=31190400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.alphavantage.co/support/>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000fba471f48bacd72c83ca6ee3&cdn=1&cp=pi&ma=31190400&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.alphavantage.co/privacy/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/amplitude/
- lastmod: `2026-09-25T00:32:49.428Z` → `2026-10-08T01:51:53.809Z`
- Content length: 11303 → 11817 chars (delta: +514)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690e2dabf430819196f8b3701ec83
  + Search and analyze analytics data
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Amplitude+Write+a+weekly+growth+ins
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Amplitude+Compare+experiment+varian

### https://openai.com/business/plugins/apollo/
- lastmod: `2026-09-25T00:31:44.725Z` → `2026-10-08T01:47:36.602Z`
- Content length: 11843 → 12447 chars (delta: +604)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69bd664f2a908191a3a0a47eca8559
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.apollo.io/submit-a-request>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Apollo.io+Enrich+these+twenty+compa
  - ### [Plugin supportLearn more](<https://www.apollo.io/submit-a-request>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/asana/
- lastmod: `2026-09-25T00:34:56.701Z` → `2026-10-08T01:48:02.766Z`
- Content length: 11079 → 11668 chars (delta: +589)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://asana.com/support>)
  + [![](https://files.openai.com/content?id=file_0000000017e0722f80510fbdbf0832a1&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://asana.com/privacy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69616780bd208191b4fb44ba44f72b
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://asana.com/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Asana+What+should+I+work+on+today%3
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Asana+Use+completed+tasks+and+comme

### https://openai.com/business/plugins/atlassian-rovo/
- lastmod: `2026-09-25T00:37:51.790Z` → `2026-10-08T01:47:45.940Z`
- Content length: 11287 → 11839 chars (delta: +552)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_692de805e3ec8191834719067174a
  + Manage Jira and Confluence fast
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.atlassian.com/>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://support.atlassian.com/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000fba081f5a22f635536f8fa4a&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=8&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/audioscrape/
- lastmod: `2026-09-25T00:06:32.998Z` → `2026-10-09T06:00:44.393Z`
- Content length: 11936 → 12525 chars (delta: +589)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a59f09745e481918959f434e0d6be
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a59f09745e481918959f434e0d6be
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_000000005df071f49a2c109d0c06a6fc&cdn=1&cp=pi&ma=32745600&ts=0&p=pi&cid=8&s
  - ### [Privacy policyLearn more](<https://www.audioscrape.com/legal/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Audioscrape+Compare+what+these+spea

### https://openai.com/business/plugins/bigdata-com/
- lastmod: `2026-09-25T00:16:46.638Z` → `2026-10-08T15:00:17.084Z`
- Content length: 14686 → 15347 chars (delta: +661)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69491eceef3c8191beb70788b78404
  + ### [Privacy policyLearn more(opens in a new window)](<https://bigdata.com/privacy-policy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69491eceef3c8191beb70788b78404
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Bigdata.com+Research+the+risks+to+t
  - ### [Privacy policyLearn more](<https://bigdata.com/privacy-policy>)

### https://openai.com/business/plugins/bigquery/
- lastmod: `2026-09-25T00:31:01.671Z` → `2026-10-08T01:46:00.410Z`
- Content length: 11182 → 11779 chars (delta: +597)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://policies.google.com/privacy>)
  + [![](https://files.openai.com/content?id=file_00000000dd3481f789a6831e32ea8ef6&cdn=1&cp=pi&ma=32486400&ts=0&p=pi&cid=8&s
  + ### [Plugin supportLearn more(opens in a new window)](<https://cloud.google.com/bigquery/docs>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_b1cefad35a80819184ba7ed35d
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://policies.google.com/privacy>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - Explore BigQuery data and generate SQL from natural language.

### https://openai.com/business/plugins/binance/
- lastmod: `2026-09-25T00:34:42.736Z` → `2026-10-08T14:59:54.243Z`
- Content length: 12031 → 12607 chars (delta: +576)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.binance.com/en/privacy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6965faefe2b081919a998e14aa25f7
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.binance.com/en/support>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Binance+Create+a+snapshot+of+these+
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Binance+Compare+the+current+prices%

### https://openai.com/business/plugins/boardwise/
- lastmod: `2026-09-24T23:59:00.742Z` → `2026-10-06T01:43:48.391Z`
- Content length: 11714 → 12378 chars (delta: +664)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a04f4233fe88191b0249cfebdf5e7
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_000000004c0c81f78746051c8894e9f0&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a04f4233fe88191b0249cfebdf5e7
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://boardwise.online/privacy-policy>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40BoardWise+Find+CE+audit+guidance+fo

### https://openai.com/business/plugins/box/
- lastmod: `2026-09-25T00:33:03.808Z` → `2026-10-08T01:48:09.025Z`
- Content length: 11739 → 12291 chars (delta: +552)
- Sample new content lines:
  +     [Productivity](</business/plugins/?tab=plugins-productivity>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_695bfc98071c8191bac7bc479aa27d
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/12368225-box-connector>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.box.com/legal/privacy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Box+Search+for+where+the+contract+m
  - ### [Privacy policyLearn more](<https://www.box.com/legal/privacy>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/canva/
- lastmod: `2026-09-25T00:28:47.350Z` → `2026-10-08T01:45:47.975Z`
- Content length: 11974 → 12283 chars (delta: +309)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_68df33b1a2d081918778431a9cfca
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * canva-bulk-create
  -   * canva-implement-feedback
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Privacy policyLearn more](<https://www.canva.com/policies/privacy-policy/>)
  -   * canva-branded-presentation

### https://openai.com/business/plugins/chatgpt-admin/
- lastmod: `2026-09-25T00:32:51.010Z` → `2026-10-08T01:51:43.028Z`
- Content length: 11492 → 12047 chars (delta: +555)
- Sample new content lines:
  + ![](https://files.openai.com/content?id=file_00000000908082308dff497411ee632a&cdn=1&cp=pi&ma=31190400&ts=0&p=pi&cid=8&si
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_e4d796f7afc48191bf6af2220a
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - ![](https://files.openai.com/content?id=file_0000000019a481f79bfa0fc50a0ac411&cdn=1&cp=pi&ma=32313600&ts=0&p=pi&cid=8&si
  - ![](https://files.openai.com/content?id=file_0000000019a481f79bfa0fc50a0ac411&cdn=1&cp=pi&ma=32313600&ts=0&p=pi&cid=8&si
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)

### https://openai.com/business/plugins/chatgpt-ads-manager/
- lastmod: `2026-09-25T00:08:22.327Z` → `2026-10-08T01:34:21.403Z`
- Content length: 11946 → 12601 chars (delta: +655)
- Sample new content lines:
  + ![](https://files.openai.com/content?id=file_00000000c2fc81f69802de525db52cae&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=8&si
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_2eb0f69766cc81919c6912b2a2
  + ![](https://files.openai.com/content?id=file_00000000c2fc81f69802de525db52cae&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=8&si
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40ChatGPT+Ads+Manager+Summarize+this+
  - [![](https://files.openai.com/content?id=file_00000000341081fda1cf8dbbd8717af9&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)

### https://openai.com/business/plugins/clay/
- lastmod: `2026-09-25T00:32:40.669Z` → `2026-10-08T01:34:15.899Z`
- Content length: 11118 → 11547 chars (delta: +429)
- Sample new content lines:
  + Find and engage prospects
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69377d07cd9c8191a988f06f15b8c6
  + GTM Data and Functions
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Clay+For+the+contacts+in+this+searc
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://www.clay.com/faq>)

### https://openai.com/business/plugins/clickup/
- lastmod: `2026-09-25T00:31:16.825Z` → `2026-10-08T01:48:34.436Z`
- Content length: 10917 → 11482 chars (delta: +565)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69431e6d26b88191b4029488aeb42f
  + [![](https://files.openai.com/content?id=file_00000000b7b8720c8deac386c4a94323&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.clickup.com/hc/en-us>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69431e6d26b88191b4029488aeb42f
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40ClickUp+Summarize+the+current+proje
  -   * [Codex](</codex/>)
  - Sync ClickUp tasks and docs for use in ChatGPT.
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s

### https://openai.com/business/plugins/cloudinary/
- lastmod: `2026-09-25T00:31:58.818Z` → `2026-10-08T01:46:00.873Z`
- Content length: 11534 → 12138 chars (delta: +604)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_691f245d4070819184e05b4889161b
  + ### [Plugin supportLearn more(opens in a new window)](<https://cloudinary.com/documentation>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_691f245d4070819184e05b4889161b
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://cloudinary.com/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_000000007edc71f5b6e71a05d16220aa&cdn=1&cp=pi&ma=30585600&ts=0&p=pi&cid=1&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/codex-security/
- lastmod: `2026-09-25T00:34:10.013Z` → `2026-10-08T01:48:16.594Z`
- Content length: 11370 → 11807 chars (delta: +437)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e648473be9c8191a91ac3947151af55?instal
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  +   * ![](https://files.openai.com/content?id=file_00000000283c820da5a336f9b88011ab&cdn=1&cp=pi&ma=30758400&ts=0&p=pi&cid=
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e648473be9c8191a91ac3947151af55?instal
  + ![](https://files.openai.com/content?id=file_00000000970c81f58269d6e931c58865&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=8&si
- Sample removed content lines:
  - ![](https://files.openai.com/content?id=file_0000000009fc8230ae12def58fd21498&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=8&si
  - [![](https://files.openai.com/content?id=file_0000000009fc8230ae12def58fd21498&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=8&s
  - ![](https://files.openai.com/content?id=file_0000000009fc8230ae12def58fd21498&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=8&si
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)

### https://openai.com/business/plugins/coingecko/
- lastmod: `2026-09-25T00:06:49.284Z` → `2026-10-08T15:00:19.251Z`
- Content length: 11628 → 12192 chars (delta: +564)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4f02d735388191959c8328877e0b
  + [![](https://files.openai.com/content?id=file_000000006a847207bb3c3fc1549c3787&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4f02d735388191959c8328877e0b
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40CoinGecko+Create+a+snapshot+of+thes
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40CoinGecko+Compare+the+current+price

### https://openai.com/business/plugins/coinmarketcap/
- lastmod: `2026-09-25T00:15:40.353Z` → `2026-10-08T14:59:53.343Z`
- Content length: 12785 → 13319 chars (delta: +534)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [![](https://files.openai.com/content?id=file_00000000507881f58e9671544573a3b7&cdn=1&cp=pi&ma=30499200&ts=0&p=pi&cid=8&s
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a172fe86f5481919f73cbc3bc3ad5
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://coinmarketcap.com/privacy/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://support-chat.coinmarketcap.com/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/conductor/
- lastmod: `2026-09-25T00:33:33.365Z` → `2026-10-08T01:46:47.852Z`
- Content length: 11477 → 12187 chars (delta: +710)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a6a413007988191a083457966e3ff
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![](https://files.openai.com/content?id=file_00000000e95471f6bca857c08854b722&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=7&si
  + ![](https://files.openai.com/content?id=file_00000000e95471f6bca857c08854b722&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=7&si
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.conductor.com/legal/privacy-policy/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Conductor+Identify+the+top+prompts+
  - ![](https://files.openai.com/content?id=file_00000000df28722f805f38afa570951c&cdn=1&cp=pi&ma=30844800&ts=0&p=pi&cid=1&si
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Conductor+Analyze+sentiment+and+con

### https://openai.com/business/plugins/consensus/
- lastmod: `2026-09-25T00:29:46.257Z` → `2026-10-09T06:00:45.447Z`
- Content length: 12660 → 13257 chars (delta: +597)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6943e6f4a928819195962de16fb9ff
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [![](https://files.openai.com/content?id=file_00000000c0cc71f7abb7f7391ab3a82e&cdn=1&cp=pi&ma=32486400&ts=0&p=pi&cid=7&s
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Privacy policyLearn more](<https://consensus.app/home/privacy-policy/>)

### https://openai.com/business/plugins/consolio-aurora/
- lastmod: `2026-09-25T00:05:56.036Z` → `2026-10-06T20:24:06.702Z`
- Content length: 11892 → 12452 chars (delta: +560)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://mcp-docs.ai.consilio.com/docs/trust/privacy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a271a3048848191bc4bb54e66eafe
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://mcp-docs.ai.consilio.com/docs/trust/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Aurora+Find+active+matters+for+%5Bc
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/coupler-io/
- lastmod: `2026-09-25T00:18:04.436Z` → `2026-10-08T01:57:17.575Z`
- Content length: 11653 → 13784 chars (delta: +2131)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6939ea66e1588191af5f9d2a52964d
  + Analyze data from 400+ apps
  + [![](https://files.openai.com/content?id=file_0000000027d4720cb3c6276cd8072cbf&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6939ea66e1588191af5f9d2a52964d
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.coupler.io/privacy-policy>)
- Sample removed content lines:
  - Connect and analyze data from 400+ apps.
  - [![](https://files.openai.com/content?id=file_0000000027d4720cb3c6276cd8072cbf&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - ### [Plugin supportLearn more](<https://help.coupler.io/>)

### https://openai.com/business/plugins/coursera-learning/
- lastmod: `2026-09-25T00:36:17.561Z` → `2026-10-09T06:00:45.953Z`
- Content length: 12241 → 12825 chars (delta: +584)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_000000004c0c81f78746051c8894e9f0&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://about.coursera.org/contact/>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_68e01e8c1c2081918b4567a0b959d3
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://www.coursera.org/about/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Coursera+Learning+Find+Coursera+cou
  - [![](https://files.openai.com/content?id=file_000000004c0c81f78746051c8894e9f0&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/courtlistener/
- lastmod: `2026-09-25T00:18:27.875Z` → `2026-10-09T06:00:45.229Z`
- Content length: 11986 → 12584 chars (delta: +598)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.courtlistener.com/contact/?issue_type=mcp>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a393898430881918250b54d31c879
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40CourtListener+Check+the+case+citati
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40CourtListener+Find+federal+appeals+
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/courtroom5/
- lastmod: `2026-09-24T23:59:33.167Z` → `2026-10-06T01:45:56.437Z`
- Content length: 13391 → 14066 chars (delta: +675)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_000000003fa081f7ad2f4a34170c6fc4&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://courtroom5.com/privacy/>)
  + [![](https://files.openai.com/content?id=file_000000004c0c81f78746051c8894e9f0&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a30d2fd05c88191adc78db28e2444
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_000000003fa081f7ad2f4a34170c6fc4&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Courtroom5+I+was+served+with+%5Bciv

### https://openai.com/business/plugins/coveo/
- lastmod: `2026-09-25T00:33:55.404Z` → `2026-10-08T01:47:53.007Z`
- Content length: 11470 → 11999 chars (delta: +529)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693251083bf48191a69098fd0ba36f
  + Search your enterprise content
  + [![](https://files.openai.com/content?id=file_00000000280c71f581d1b587fe4e3273&cdn=1&cp=pi&ma=32659200&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693251083bf48191a69098fd0ba36f
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://www.coveo.com/en/contact>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Coveo+Find+the+best+answer+to+the+b
  - Search and retrieve answers from your enterprise content in ChatGPT using Coveo to find relevant documents and source pa
  - [![](https://files.openai.com/content?id=file_00000000280c71f581d1b587fe4e3273&cdn=1&cp=pi&ma=32659200&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)

### https://openai.com/business/plugins/creative-claw/
- lastmod: `2026-09-25T00:37:34.522Z` → `2026-10-08T01:55:39.113Z`
- Content length: 13412 → 14274 chars (delta: +862)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a2528e2c49c8191a8015ba5475f17
  +   * Creative Claw — Edit Existing Media
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * 9 more
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Creative+Claw+Create+a+product+hero
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Creative+Claw+Generate+three+distin

### https://openai.com/business/plugins/creative-production/
- lastmod: `2026-09-25T00:29:53.587Z` → `2026-10-08T01:35:22.683Z`
- Content length: 11110 → 11558 chars (delta: +448)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_9e6ca248b5248191ac8c599038990ad9?instal
  + Use the Creative Production plugin in ChatGPT to create, adapt, and review marketing assets, campaign concepts, ads, and
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://help.openai.com/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Creative+Production+Turn+this+top+p
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/daloopa/
- lastmod: `2026-09-25T00:07:06.657Z` → `2026-10-08T14:59:51.569Z`
- Content length: 10866 → 11414 chars (delta: +548)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_692f6343042c8191b6617e8352444
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_692f6343042c8191b6617e8352444
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://daloopa.ai/support>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://daloopa.ai/privacy>)
- Sample removed content lines:
  - Access financial KPIs with source links.
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Daloopa+Summarize+the+trend+in+unit
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Daloopa+Create+a+quick+benchmarking

### https://openai.com/business/plugins/data/
- lastmod: `2026-09-25T00:37:57.450Z` → `2026-10-08T01:55:19.381Z`
- Content length: 13343 → 14570 chars (delta: +1227)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_fc9843a6fb34819195d6c7802398a8a7?instal
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + Answer questions with data
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_fc9843a6fb34819195d6c7802398a8a7?instal
- Sample removed content lines:
  - Turn data into clear decisions.
  - ### [Plugin supportLearn more](<https://help.openai.com/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Data+Design+a+KPI+framework+for+thi

### https://openai.com/business/plugins/databricks/
- lastmod: `2026-09-25T00:41:44.630Z` → `2026-10-08T01:52:18.480Z`
- Content length: 11460 → 11938 chars (delta: +478)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.databricks.com>)
  + Analyze lakehouse data and dashboards with natural language
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e24c86b19248191a8c6abb5bc115819?instal
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Databricks+Genie+Find+the+main+driv
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Plugin supportLearn more](<https://help.databricks.com>)

### https://openai.com/business/plugins/definely/
- lastmod: `2026-09-25T00:14:10.269Z` → `2026-10-06T01:41:52.446Z`
- Content length: 12642 → 13269 chars (delta: +627)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [![](https://files.openai.com/content?id=file_00000000e4a8720c9b8cba8aaa6e4f70&cdn=1&cp=pi&ma=30672000&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a1e9f6b731c8191b663ba549f85df
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_0000000060e48230a9cba1a5cc373c8b&cdn=1&cp=pi&ma=31449600&ts=0&p=pi&cid=8&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Definely+Find+the+closest+precedent
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/demandbase/
- lastmod: `2026-09-25T00:29:39.026Z` → `2026-10-08T01:34:36.475Z`
- Content length: 13527 → 14058 chars (delta: +531)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_0000000028f471f682a1f579e6adabe2&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=8&s
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_698ebfa1aadc81918b3bb13ae2118a
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.demandbase.com/privacy/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://www.demandbase.com/privacy/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Demandbase+Prepare+an+account+brief
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Demandbase+Show+me+my+accounts+with

### https://openai.com/business/plugins/descrybe/
- lastmod: `2026-09-25T00:01:27.284Z` → `2026-10-09T06:00:42.961Z`
- Content length: 12159 → 12693 chars (delta: +534)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://descrybe.com/support>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a3899f86a748191b0c9b26f4b258c
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://descrybe.com/support>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Descrybe+Legal+Engine+Research+%5Bl

### https://openai.com/business/plugins/docusign/
- lastmod: `2026-09-25T00:30:20.742Z` → `2026-10-08T01:46:49.842Z`
- Content length: 11257 → 11778 chars (delta: +521)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_000000008040722fab99266f6882677e&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=1&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.docusign.com/privacy>)
  - [![](https://files.openai.com/content?id=file_000000008040722fab99266f6882677e&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=1&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/dropbox/
- lastmod: `2026-09-25T00:31:55.281Z` → `2026-10-08T01:48:05.011Z`
- Content length: 12266 → 12865 chars (delta: +599)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.dropbox.com/support>)
  + [![](https://files.openai.com/content?id=file_00000000b45c71f797469228048098cf&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=8&s
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Find and access your stored files
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Dropbox+Pull+all+docs+related+to+%5
  - ### [Privacy policyLearn more](<https://www.dropbox.com/privacy>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Dropbox+Summarize+the+latest+quarte
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/egnyte/
- lastmod: `2026-09-25T00:38:19.039Z` → `2026-10-08T01:45:17.946Z`
- Content length: 11327 → 11923 chars (delta: +596)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_691f749cd9088191befeb1d543c37
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.egnyte.com/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Egnyte+Show+recent+file+activity%2C
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - Explore and analyyze your content.
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Egnyte+Open+%5Bfile%5D+and+summariz

### https://openai.com/business/plugins/elicit/
- lastmod: `2026-09-25T00:37:21.736Z` → `2026-10-09T06:00:46.045Z`
- Content length: 11928 → 12473 chars (delta: +545)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help@elicit.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69fcf53d4d8481919b65501a96bbed
  + ### [Privacy policyLearn more(opens in a new window)](<https://elicit.com/operations/privacy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Elicit+Search+for+research+addressi
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Elicit+Find+recent+research+on+this
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/everlaw/
- lastmod: `2026-09-25T00:04:29.301Z` → `2026-10-08T01:48:56.768Z`
- Content length: 13354 → 13435 chars (delta: +81)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.everlaw.com/customer-resources/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a95f81c026081918845945f1d0179
  + Connect ChatGPT to live matter data in Everlaw to search, retrieve, and analyze evidence using natural language. Everlaw
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000046081f79c1b5f390ba482fd&cdn=1&cp=pi&ma=30326400&ts=0&p=pi&cid=8&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/explain-video-generator/
- lastmod: `2026-09-25T00:36:47.674Z` → `2026-10-09T06:00:45.604Z`
- Content length: 12704 → 13259 chars (delta: +555)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69c50381a40081919232f5027201be
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://scrimba.com/privacy-policy>)
  + [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Explain+Video+Generator+Create+a+tw
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Explain+Video+Generator+Create+a+90

### https://openai.com/business/plugins/factset/
- lastmod: `2026-09-25T00:26:06.519Z` → `2026-10-08T15:00:07.023Z`
- Content length: 12192 → 12706 chars (delta: +514)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_699727751b1c819193883394649579
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.factset.com/GenAI-Governance-and-Security>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://www.factset.com/GenAI-Governance-and-Security>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://www.factset.com/support-numbers>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/figma/
- lastmod: `2026-09-25T00:37:23.583Z` → `2026-10-08T01:34:32.191Z`
- Content length: 11665 → 12166 chars (delta: +501)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_68df038e0ba48191908c8434991bb
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_68df038e0ba48191908c8434991bb
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_68df038e0ba48191908c8434991bb
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Figma+create+a+competitive+analysis
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Figma+Convert+this+user+journey+tex
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/financial-datasets/
- lastmod: `2026-09-25T00:06:15.054Z` → `2026-10-08T15:00:10.494Z`
- Content length: 11997 → 12449 chars (delta: +452)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69cacd9394a88191ba6564e1bb0430
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69cacd9394a88191ba6564e1bb0430
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://financialdatasets.ai/contact>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Financial+Datasets+Compare+revenue+
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/firecrawl/
- lastmod: `2026-09-25T00:13:38.903Z` → `2026-10-08T01:48:34.094Z`
- Content length: 11618 → 12166 chars (delta: +548)
- Sample new content lines:
  + Search the web and access data providers and specialized indexes through Alexandria. Research companies, compare product
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.firecrawl.dev/support>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a314a73f8ac819195b0d55e36b9c6
  + ### Skill
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a314a73f8ac819195b0d55e36b9c6
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Firecrawl+Search+and+read+this+docu
  - [![](https://files.openai.com/content?id=file_00000000065881f4a641d2723fc2def5&cdn=1&cp=pi&ma=32745600&ts=0&p=pi&cid=8&s
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * 5 more
  -   * firecrawl-download

### https://openai.com/business/plugins/fireflies/
- lastmod: `2026-09-25T00:35:33.928Z` → `2026-10-08T01:40:24.768Z`
- Content length: 11351 → 12245 chars (delta: +894)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_6912075cb358819187346bcafb601
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.fireflies.ai/>)
  + Search meeting transcripts
- Sample removed content lines:
  - Search meeting transcripts.
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Fireflies+From+the+meeting+transcri

### https://openai.com/business/plugins/gamma/
- lastmod: `2026-09-25T00:35:16.805Z` → `2026-10-08T01:49:20.102Z`
- Content length: 11982 → 12601 chars (delta: +619)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_698a098735908191989f5788d7ee31
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_698a098735908191989f5788d7ee31
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_0000000046e481f7a7a7312d61b66ab1&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=8&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://gamma.app/privacy>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.gamma.app>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Privacy policyLearn more](<https://gamma.app/privacy>)

### https://openai.com/business/plugins/gc-ai/
- lastmod: `2026-09-25T00:23:20.438Z` → `2026-10-06T02:11:49.568Z`
- Content length: 12039 → 12665 chars (delta: +626)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a57ec753e988191bcba94f5507329
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://gc.ai/contact>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://gc.ai/contact>)
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40GC+AI+Use+our+NDA+playbook+to+revie

### https://openai.com/business/plugins/github/
- lastmod: `2026-09-25T00:38:27.306Z` → `2026-10-08T01:50:19.495Z`
- Content length: 11691 → 12241 chars (delta: +550)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11145903-connecting-github-to-ch
  + ### [Plugin supportLearn more(opens in a new window)](<https://docs.github.com/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40GitHub+Using+this+repository%E2%80%
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  - ### [Privacy policyLearn more](<https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement>)
  - Access repositories, issues, and pull requests.

### https://openai.com/business/plugins/gleap/
- lastmod: `2026-09-25T00:34:25.392Z` → `2026-10-08T01:45:06.437Z`
- Content length: 11928 → 12547 chars (delta: +619)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000b25481f6a16ac0c2f2b554f3&cdn=1&cp=pi&ma=32572800&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a84539026a88191aa8c1db752eec1
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.gleap.io/legal/privacy-policy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Gleap+Read+this+ticket+and+summariz
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Gleap+Review+my+open+support+ticket
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Gleap+Review+up+to+fifty+recent+sup

### https://openai.com/business/plugins/gmail/
- lastmod: `2026-09-25T00:35:27.320Z` → `2026-10-08T01:46:24.861Z`
- Content length: 11477 → 12034 chars (delta: +557)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://policies.google.com/privacy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_95d39881713c8191931482a62d
  + Find and reference emails from your inbox
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_95d39881713c8191931482a62d
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Gmail+Turn+my+latest+customer+escal
  - ### [Privacy policyLearn more](<https://policies.google.com/privacy>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://support.google.com/mail/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)

### https://openai.com/business/plugins/godaddy/
- lastmod: `2026-09-25T00:37:37.294Z` → `2026-10-08T01:48:22.554Z`
- Content length: 12106 → 12698 chars (delta: +592)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_697b9ea0c7f0819183c54233b42cd3
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_697b9ea0c7f0819183c54233b42cd3
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)
  - [![](https://files.openai.com/content?id=file_00000000651071f6b83a1e63cf9ed138&cdn=1&cp=pi&ma=30499200&ts=0&p=pi&cid=7&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/google-calendar/
- lastmod: `2026-09-25T00:34:41.040Z` → `2026-10-08T01:48:00.915Z`
- Content length: 11148 → 11729 chars (delta: +581)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://policies.google.com/privacy>)
  + [![](https://files.openai.com/content?id=file_00000000970481f5b8b68deb912e6bc5&cdn=1&cp=pi&ma=32572800&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://policies.google.com/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000970481f5b8b68deb912e6bc5&cdn=1&cp=pi&ma=32572800&ts=0&p=pi&cid=8&s
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/google-drive/
- lastmod: `2026-09-25T00:33:13.744Z` → `2026-10-08T01:45:12.488Z`
- Content length: 12361 → 12978 chars (delta: +617)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://policies.google.com/privacy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [![](https://files.openai.com/content?id=file_00000000d44881f79ef4a45a9ca31665&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://policies.google.com/privacy>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Google+Drive+Use+our+brand+guidelin
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/granola/
- lastmod: `2026-09-25T00:35:12.376Z` → `2026-10-08T01:47:40.320Z`
- Content length: 12261 → 12850 chars (delta: +589)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_697761cab6f48191b5ed345919a3ce
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_000000002bd8720c8e4bfaefb735cfeb&cdn=1&cp=pi&ma=30326400&ts=0&p=pi&cid=1&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://help.granola.ai/article/privacy-policy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Granola+Review+last+week%27s+meetin
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Granola+Review+up+to+five+recent+cu

### https://openai.com/business/plugins/gsc-wizard/
- lastmod: `2026-09-25T00:38:09.271Z` → `2026-10-08T01:52:45.783Z`
- Content length: 13230 → 13820 chars (delta: +590)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a258ab1e0908191aa647c33299ad1
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a258ab1e0908191aa647c33299ad1
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40GSC+Wizard+Compare+the+last+28+comp
  - ### [Privacy policyLearn more](<https://www.gscwizard.com/privacy.html>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)

### https://openai.com/business/plugins/gusto/
- lastmod: `2026-09-25T00:34:39.569Z` → `2026-10-08T15:00:15.134Z`
- Content length: 11464 → 12027 chars (delta: +563)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000ac7471f5938c2faf47e7f4c3&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69375d9f172c8191b23d73be410712
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.gusto.com/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Privacy policyLearn more](<https://gusto.com/legal/privacy>)
  - [![](https://files.openai.com/content?id=file_00000000ac7471f5938c2faf47e7f4c3&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s

### https://openai.com/business/plugins/hex/
- lastmod: `2026-09-25T00:34:42.170Z` → `2026-10-08T01:46:45.972Z`
- Content length: 10939 → 11468 chars (delta: +529)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://hex.tech/docs>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690a9430a270819196671dcb4c958
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690a9430a270819196671dcb4c958
  + [![](https://files.openai.com/content?id=file_00000000fcb4720ca56d2ab5ac6ac7b8&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://hex.tech/docs>)
  - Ask data questions and start new analyses from Hex.
  - [![](https://files.openai.com/content?id=file_00000000fcb4720ca56d2ab5ac6ac7b8&cdn=1&cp=pi&ma=31795200&ts=0&p=pi&cid=1&s

### https://openai.com/business/plugins/higgsfield/
- lastmod: `2026-09-25T00:24:34.630Z` → `2026-10-08T01:57:43.730Z`
- Content length: 14585 → 14789 chars (delta: +204)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a3293e129088191abf0875820e839
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a3293e129088191abf0875820e839
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Higgsfield+Create+a+product+hero+im
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://discord.com/invite/higgsfield>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/highlevel/
- lastmod: `2026-09-25T00:31:32.000Z` → `2026-10-08T01:49:17.035Z`
- Content length: 11161 → 11994 chars (delta: +833)
- Sample new content lines:
  + Interact with your CRM business data
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.gohighlevel.com/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69402343886881919c40ceb13a6ea1
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69402343886881919c40ceb13a6ea1
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - Securely bring HighLevel CRM data into ChatGPT to review contacts, opportunities, appointments, and conversations and ge
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.gohighlevel.com/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/highspot/
- lastmod: `2026-09-25T00:36:01.785Z` → `2026-10-08T01:48:21.592Z`
- Content length: 11756 → 12298 chars (delta: +542)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.highspot.com/support/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69f0ffe2c6008191aaf507e1d354b2
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Highspot+Find+approved+content+addr
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Highspot+Find+sales+content+relevan
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/hostinger/
- lastmod: `2026-09-25T00:40:25.237Z` → `2026-10-08T01:40:23.114Z`
- Content length: 11633 → 12248 chars (delta: +615)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_698ae2bbd3e08191ace34d672e1d58
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_698ae2bbd3e08191ace34d672e1d58
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.hostinger.com/legal/privacy-policy>)
- Sample removed content lines:
  - Hostinger Horizons lets you build real websites and apps just by describing what you want. Designed for people with no t
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Hostinger+Create+a+three-page+websi
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Hostinger+Build+a+prototype+for+tra

### https://openai.com/business/plugins/hubspot/
- lastmod: `2026-09-25T00:36:58.598Z` → `2026-10-08T01:47:43.849Z`
- Content length: 11520 → 12040 chars (delta: +520)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://hubs.la/Q03XWR7C0>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://legal.hubspot.com/privacy-policy>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40HubSpot+For+my+next+customer+call%2
  - ### [Plugin supportLearn more](<https://hubs.la/Q03XWR7C0>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/hugging-face/
- lastmod: `2026-09-25T00:33:56.862Z` → `2026-10-08T01:45:53.427Z`
- Content length: 11218 → 11820 chars (delta: +602)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://huggingface.co/privacy>)
  + [![](https://files.openai.com/content?id=file_00000000390071f5999f6ff280280bb2&cdn=1&cp=pi&ma=32572800&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - Connect to the Hugging Face Hub in ChatGPT to explore models, datasets, and metadata and inspect options without manual 
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Hugging+Face+I+need+a+model+for+mul
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/intapp-celeste/
- lastmod: `2026-09-25T00:34:41.902Z` → `2026-10-08T14:59:53.653Z`
- Content length: 11160 → 11700 chars (delta: +540)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://intapp.com/privacy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Intapp+Celeste+Find+the+DealCloud+r
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/interactive-brokers/
- lastmod: `2026-09-25T00:36:06.405Z` → `2026-10-08T14:59:55.305Z`
- Content length: 11704 → 12112 chars (delta: +408)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://gdcdyn.interactivebrokers.com/Universal/servlet/Registrat
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.interactivebrokers.com/support>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://gdcdyn.interactivebrokers.com/Universal/servlet/Registration_v2.formSampleView?f
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://www.interactivebrokers.com/support>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/investment-banking/
- lastmod: `2026-09-25T00:35:55.495Z` → `2026-10-08T15:00:12.458Z`
- Content length: 13497 → 13887 chars (delta: +390)
- Sample new content lines:
  + M&A, valuation, and financing
  + Investment banking workflows for M&A, coverage, sponsors, ECM/DCM, LevFin, restructuring, capital advisory, valuation, b
  + [![](https://files.openai.com/content?id=file_00000000179c722f9e8a66d8ff27e98b&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_68c39ea2b3888191827c933053f3a1d1?instal
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000179c722f9e8a66d8ff27e98b&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  - ### [Plugin supportLearn more](<https://help.openai.com/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000ce8481f7986ba74ddb54af68&cdn=1&cp=pi&ma=31881600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/ironclad-contracts/
- lastmod: `2026-09-25T00:36:42.542Z` → `2026-10-08T01:47:53.556Z`
- Content length: 12797 → 13352 chars (delta: +555)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + [![](https://files.openai.com/content?id=file_00000000ab2c81f79ce02f9c44c322c0&cdn=1&cp=pi&ma=30240000&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000ab2c81f79ce02f9c44c322c0&cdn=1&cp=pi&ma=30240000&ts=0&p=pi&cid=8&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Ironclad+Contracts+Find+vendor+agre

### https://openai.com/business/plugins/jam-dev/
- lastmod: `2026-09-25T00:26:54.070Z` → `2026-10-08T01:46:33.202Z`
- Content length: 11277 → 12014 chars (delta: +737)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000b9a881f4b4467ce174b2723c&cdn=1&cp=pi&ma=30412800&ts=0&p=pi&cid=8&s
  + Investigate bug reports
  + ### [Privacy policyLearn more(opens in a new window)](<https://jam.dev/privacy>)
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_6923e677f37c8191845e4e0b658dd
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Jam+Turn+this+Jam+recording+into+a+
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Jam+Open+this+Jam+recording%3A+%5Bl
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/khan-academy/
- lastmod: `2026-09-25T00:13:26.737Z` → `2026-10-09T06:00:44.860Z`
- Content length: 12058 → 12658 chars (delta: +600)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.khanacademy.org/about/privacy-policy>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69127e3e55288191a8b5c2b401fb73
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69127e3e55288191a8b5c2b401fb73
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Khan+Academy+Prepare+a+ten-question
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Khan+Academy+Create+two+Khan+Academ
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)

### https://openai.com/business/plugins/klaviyo/
- lastmod: `2026-09-25T00:33:43.543Z` → `2026-10-08T01:45:28.346Z`
- Content length: 12250 → 12996 chars (delta: +746)
- Sample new content lines:
  + Skip manual analysis with marketing campaign and flow performance, explanations, and recommendations directly in ChatGPT
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_694421e60cc88191a1e5bb4aa79950
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_694421e60cc88191a1e5bb4aa79950
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Klaviyo+Compare+email+and+SMS+campa
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Klaviyo+Give+me+a+campaign+performa
  - [![](https://files.openai.com/content?id=file_000000001c74722fbf559d66b947677a&cdn=1&cp=pi&ma=30758400&ts=0&p=pi&cid=1&s

### https://openai.com/business/plugins/lawve-ai/
- lastmod: `2026-09-25T00:03:50.167Z` → `2026-10-06T00:47:49.722Z`
- Content length: 12201 → 12792 chars (delta: +591)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a07517af0d48191bde4ae526305f8
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a07517af0d48191bde4ae526305f8
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Lawve+Select+a+legal+writing+skill+
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/legal-data-hunter/
- lastmod: `2026-09-25T00:07:16.897Z` → `2026-10-09T06:00:44.189Z`
- Content length: 12837 → 13391 chars (delta: +554)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a09fca2104c8191b160df27196228
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a09fca2104c8191b160df27196228
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://legaldatahunter.com/privacy>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Legal+Data+Hunter+Compare+how+Spain
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - ### [Plugin supportLearn more](<https://legaldatahunter.com/support>)

### https://openai.com/business/plugins/life-sciences-ngs-analysis/
- lastmod: `2026-09-25T00:06:27.088Z` → `2026-10-09T06:00:42.540Z`
- Content length: 12585 → 13129 chars (delta: +544)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [![](https://files.openai.com/content?id=file_0000000028d0720c8c056a13d057bf25&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=1&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_271fcfe114788191b30908b85bd9ade6?instal
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - [![](https://files.openai.com/content?id=file_0000000028d0720c8c056a13d057bf25&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=1&s
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Life+Sciences+NGS+Analysis+Review+t

### https://openai.com/business/plugins/linear/
- lastmod: `2026-09-25T00:38:09.817Z` → `2026-10-08T01:48:10.335Z`
- Content length: 11112 → 11696 chars (delta: +584)
- Sample new content lines:
  + Find and reference issues and projects
  + ### [Plugin supportLearn more(opens in a new window)](<https://linear.app/docs>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - Find and reference issues and projects.
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://linear.app/privacy>)
  - [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Linear+Triage+or+update+relevant+is

### https://openai.com/business/plugins/linkedin-ads/
- lastmod: `2026-09-25T00:24:45.856Z` → `2026-10-08T01:45:29.043Z`
- Content length: 13049 → 13623 chars (delta: +574)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69cdf9990c90819185974d8727ef9d
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.linkedin.com/legal/privacy-policy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://www.linkedin.com/help/lms>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.linkedin.com/legal/privacy-policy>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/longbridge/
- lastmod: `2026-09-25T00:19:29.943Z` → `2026-10-08T15:00:12.848Z`
- Content length: 12587 → 13127 chars (delta: +540)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a2baf2fad748191812393c3e00308
  + ### [Plugin supportLearn more(opens in a new window)](<https://longbridge.com/sg/support/>)
  + [![](https://files.openai.com/content?id=file_00000000a0dc81f79a9d3200446bd6c9&cdn=1&cp=pi&ma=32572800&ts=0&p=pi&cid=8&s
  + [![](https://files.openai.com/content?id=file_00000000179c722f9e8a66d8ff27e98b&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Longbridge+Review+my+open+orders.+S
  - ### [Plugin supportLearn more](<https://longbridge.com/sg/support/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/lovable/
- lastmod: `2026-09-25T00:33:17.513Z` → `2026-10-08T01:46:26.749Z`
- Content length: 11078 → 11976 chars (delta: +898)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://lovable.ai/support>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693a0a79ffe48191901173077edcf9
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Lovable+Add+a+dashboard+page+with+c
  - ### [Privacy policyLearn more](<https://lovable.ai/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - Create functional apps and websites in ChatGPT by describing what you want and iterating on the result through natural l

### https://openai.com/business/plugins/lseg/
- lastmod: `2026-09-25T00:33:42.512Z` → `2026-10-08T14:59:50.663Z`
- Content length: 11208 → 11970 chars (delta: +762)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.lseg.com/contact-us>)
  + [![](https://files.openai.com/content?id=file_00000000e45471f5b5de13a805b0fb63&cdn=1&cp=pi&ma=32486400&ts=0&p=pi&cid=1&s
  + [![](https://files.openai.com/content?id=file_00000000179c722f9e8a66d8ff27e98b&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.lseg.com/privacy-statement>)
  + Data and analytics
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.lseg.com/privacy-statement>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40LSEG+Get+the+latest+EURUSD+spot+plu

### https://openai.com/business/plugins/mailchimp/
- lastmod: `2026-09-25T00:33:44.613Z` → `2026-10-08T01:47:05.770Z`
- Content length: 11315 → 11863 chars (delta: +548)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693b20fccbac8191bdc178bb493de3
  + [![](https://files.openai.com/content?id=file_000000006100822fba053a7663790f13&cdn=1&cp=pi&ma=30412800&ts=0&p=pi&cid=8&s
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://mailchimp.com/about/privacy-rights/>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://mailchimp.com/help/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://mailchimp.com/about/privacy-rights/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_000000006100822fba053a7663790f13&cdn=1&cp=pi&ma=30412800&ts=0&p=pi&cid=8&s
  - ### [Plugin supportLearn more](<https://mailchimp.com/help/>)

### https://openai.com/business/plugins/malwarebytes/
- lastmod: `2026-09-25T00:33:56.525Z` → `2026-10-08T01:45:26.115Z`
- Content length: 12229 → 12823 chars (delta: +594)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.malwarebytes.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.malwarebytes.com/legal/privacy-policy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6943d1778c8c81918f4c9ddf4849ca
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Malwarebytes+Check+this+sender+doma
  - ### [Plugin supportLearn more](<https://help.malwarebytes.com>)

### https://openai.com/business/plugins/manatal/
- lastmod: `2026-09-25T00:36:40.253Z` → `2026-10-08T01:49:09.964Z`
- Content length: 11578 → 12208 chars (delta: +630)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a86e63a115481919e1692b9e96a72
  + [![](https://files.openai.com/content?id=file_000000003be48209b76a7fbc96074048&cdn=1&cp=pi&ma=32659200&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://www.manatal.com/contact-us>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Manatal+Review+the+pipeline+for+thi
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Manatal+Prepare+a+brief+for+this+ca

### https://openai.com/business/plugins/manus/
- lastmod: `2026-09-25T00:09:00.730Z` → `2026-10-08T01:47:50.006Z`
- Content length: 12540 → 13150 chars (delta: +610)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + [![](https://files.openai.com/content?id=file_00000000f0b071f6b09577c7605bf79b&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=1&s
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.manus.im/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_694e289261b08191b244259e30ce08
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://manus.im/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Manus+Create+a+six-slide+presentati
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/massive/
- lastmod: `2026-09-25T00:13:40.657Z` → `2026-10-08T14:59:53.110Z`
- Content length: 12455 → 12950 chars (delta: +495)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://massive.com/contact>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4d14f6bfa48191a49bc4f42980ae
  + [![](https://files.openai.com/content?id=file_00000000179c722f9e8a66d8ff27e98b&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://massive.com/privacy>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Massive+Review+the+last+month%27s+d
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://massive.com/contact>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/mercury/
- lastmod: `2026-09-25T02:21:46.272Z` → `2026-10-08T15:00:25.717Z`
- Content length: 11954 → 12562 chars (delta: +608)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a17ae803744819187a3079d37479d
  + [![](https://files.openai.com/content?id=file_00000000ac7881f59a95b718896b7902&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://mercury.com/legal/privacy>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Mercury+what%E2%80%99s+the+current+
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Mercury+what+did+we+spend+on+softwa

### https://openai.com/business/plugins/microsoft-outlook-calendar/
- lastmod: `2026-09-25T00:36:45.069Z` → `2026-10-08T01:48:11.448Z`
- Content length: 11547 → 12132 chars (delta: +585)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_fd0f4f41caa88191a9456514bb
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/12512241-outlook-email-and-calen
  + Look up events and availability
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Outlook+Calendar+Use+the+event+deta
  - ### [Privacy policyLearn more](<https://privacy.microsoft.com>)
  - Look up events and availability.
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/microsoft-outlook-email/
- lastmod: `2026-09-25T00:33:50.004Z` → `2026-10-08T01:47:33.219Z`
- Content length: 11724 → 12241 chars (delta: +517)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_6bcb5879c73c819196abc70016
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.microsoft.com/outlook>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Outlook+Email+Summarize+the+most+re
  - ### [Privacy policyLearn more](<https://privacy.microsoft.com>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Outlook+Email+Find+the+top+5+emails

### https://openai.com/business/plugins/microsoft-sharepoint/
- lastmod: `2026-09-25T00:34:00.115Z` → `2026-10-08T01:56:14.286Z`
- Content length: 11434 → 12038 chars (delta: +604)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_dca009ae2c848191ae14df3a47
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_dca009ae2c848191ae14df3a47
  + Search and pull from shared sites and OneDrive
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/12143177-sharepoint-connectors-on-chatgpt>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40SharePoint+Use+the+approved+templat
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://privacy.microsoft.com>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/microsoft-teams/
- lastmod: `2026-09-25T00:27:32.429Z` → `2026-10-08T01:46:39.628Z`
- Content length: 11453 → 12112 chars (delta: +659)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_000000002d7481f7a628052e560e80a1&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=8&s
  + Look up chats and messages
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_eba8b52fe53881918408d4b46b
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://support.microsoft.com/teams>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://privacy.microsoft.com>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Teams+I+joined+mid-project.+Review+
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/midpage/
- lastmod: `2026-09-25T00:18:11.208Z` → `2026-10-09T06:00:45.054Z`
- Content length: 11692 → 12270 chars (delta: +578)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_0000000091a481f4a129f34a97e52ddf&cdn=1&cp=pi&ma=30499200&ts=0&p=pi&cid=8&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.midpage.ai/privacy-policy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_699cc1a043688191a3ee44e6a2c2eb
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.midpage.ai/privacy-policy>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Midpage+Legal+Research+Research+thi

### https://openai.com/business/plugins/monday-com/
- lastmod: `2026-09-25T00:34:21.226Z` → `2026-10-08T01:45:35.978Z`
- Content length: 11006 → 11545 chars (delta: +539)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690aabb71bf481918b8d5b614ed3f
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + Manage work in monday.com
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Monday.com+Turn+this+chat+into+mond
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Monday.com+Update+these+items+to+re
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://support.monday.com/>)

### https://openai.com/business/plugins/morningstar/
- lastmod: `2026-09-25T00:34:11.611Z` → `2026-10-08T14:59:50.801Z`
- Content length: 11793 → 12540 chars (delta: +747)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.morningstar.com/company/privacy-policy>)
  + Investment and market insights
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69248819fa4c81918047c4b42b1f88
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://www.morningstar.com/views/contact-us>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://www.morningstar.com/company/privacy-policy>)
  - Bring Morningstar research and market data into workflows to analyze investments, screen opportunities, and answer portf

### https://openai.com/business/plugins/namecheap/
- lastmod: `2026-09-25T00:35:37.917Z` → `2026-10-08T01:56:20.335Z`
- Content length: 12502 → 13094 chars (delta: +592)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + [![](https://files.openai.com/content?id=file_00000000be0071f6a1a959f96d2fdc34&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://www.namecheap.com/legal/general/privacy-policy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000be0071f6a1a959f96d2fdc34&cdn=1&cp=pi&ma=31104000&ts=0&p=pi&cid=1&s
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/neon/
- lastmod: `2026-09-25T00:37:27.255Z` → `2026-10-08T01:46:39.703Z`
- Content length: 11447 → 12541 chars (delta: +1094)
- Sample new content lines:
  + ![](https://files.openai.com/content?id=file_00000000768081f98d4a28dfe71cff47&cdn=1&cp=pi&ma=30758400&ts=0&p=pi&cid=8&si
  + Manage Neon projects directly through ChatGPT. Run SQL and transactions on Lakebase Postgres, inspect and diff table sch
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69e0086d87088191a3edc052fa50c2
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Capabilities
- Sample removed content lines:
  - ![](https://files.openai.com/content?id=file_000000004258720ca379d601da78f1ba&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&si
  - [![](https://files.openai.com/content?id=file_000000004258720ca379d601da78f1ba&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Neon+Investigate+this+database+erro

### https://openai.com/business/plugins/netlify/
- lastmod: `2026-09-25T00:34:43.089Z` → `2026-10-08T01:46:30.392Z`
- Content length: 11276 → 12091 chars (delta: +815)
- Sample new content lines:
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  + ![](https://files.openai.com/content?id=file_00000000ce988243b0042cc99afe8459&cdn=1&cp=pi&ma=30844800&ts=0&p=pi&cid=8&si
  +   * netlify-deploy
  +   * netlify-config
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * AI Gateway
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Netlify+Create+a+new+site+from+my+G
  -   * 4 more
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Netlify+List+all+environment+variab

### https://openai.com/business/plugins/ngs-analysis-workbench/
- lastmod: `2026-09-25T00:32:28.720Z` → `2026-10-08T01:45:54.982Z`
- Content length: 11942 → 12446 chars (delta: +504)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_32edf73dc4f48191980d50e2cad2b3e4?instal
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![](https://files.openai.com/content?id=file_00000000386c81f7a6d0cdc14218dc8b&cdn=1&cp=pi&ma=32745600&ts=0&p=pi&cid=8&si
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40NGS+Analysis+Workbench+Review+this+
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40NGS+Analysis+Workbench+Inspect+thes

### https://openai.com/business/plugins/notion/
- lastmod: `2026-09-25T00:30:54.323Z` → `2026-10-08T01:49:17.782Z`
- Content length: 12123 → 11825 chars (delta: -298)
- Sample new content lines:
  + Search and reference your Notion pages
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![](https://files.openai.com/content?id=file_00000000dca471f5a61c7e4a3fab77a4&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=1&si
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  - Search and reference your Notion pages.
  - ![](https://files.openai.com/content?id=file_0000000035e081f78f1775acc52fc7e9&cdn=1&cp=pi&ma=32227200&ts=0&p=pi&cid=8&si
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * ![](https://files.openai.com/content?id=file_00000000c8f881f6a3b24213526245e4&cdn=1&cp=pi&ma=30844800&ts=0&p=pi&cid=

### https://openai.com/business/plugins/omnisend/
- lastmod: `2026-09-25T00:06:48.214Z` → `2026-10-08T01:41:09.296Z`
- Content length: 11675 → 12201 chars (delta: +526)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69ce67bdd5308191a2840b993cf325
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.omnisend.com/privacy/>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Omnisend+Prepare+a+brief+on+last+mo
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Omnisend+Compare+my+latest+five+ema
  - ### [Plugin supportLearn more](<https://www.omnisend.com/contact-us/support/>)

### https://openai.com/business/plugins/openai-certified/
- lastmod: `2026-09-25T00:07:07.597Z` → `2026-10-09T06:00:41.854Z`
- Content length: 11828 → 12224 chars (delta: +396)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://platform.openai.com/docs>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_693022c8c0088191a7c7572aee832a
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Plugin supportLearn more](<https://platform.openai.com/docs>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - Give teams a clear, applied path to AI fluency with role-aware guidance, practical exercises, and OpenAI-issued certific

### https://openai.com/business/plugins/openai-developers/
- lastmod: `2026-09-25T00:38:48.009Z` → `2026-10-08T01:47:42.518Z`
- Content length: 11862 → 12453 chars (delta: +591)
- Sample new content lines:
  + Use OpenAI Developers to build AI applications and agents. Optimize your existing API integration with our latest models
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + Develop AI apps and agents with OpenAI best practices
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_1p_32dba5a7095c8191adca04ee30
- Sample removed content lines:
  - Use OpenAI Developers in Codex to build AI applications, agents, and ChatGPT Apps. Build agents with the Agents API and 
  - ![](https://files.openai.com/content?id=file_00000000cb9081fda39403490b8d54cc&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=8&si
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - Develop AI apps, agents, and ChatGPT Apps with OpenAI best practices

### https://openai.com/business/plugins/openart/
- lastmod: `2026-09-25T00:17:26.401Z` → `2026-10-08T01:46:43.671Z`
- Content length: 12134 → 12822 chars (delta: +688)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  +   * ![](https://files.openai.com/content?id=file_00000000a33882309ac5cf9e72475e58&cdn=1&cp=pi&ma=31881600&ts=0&p=pi&cid=
  + ![](https://files.openai.com/content?id=file_00000000f0a082309d28cf77e97a68ee&cdn=1&cp=pi&ma=30931200&ts=0&p=pi&cid=8&si
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a42dbbe74c081918a592a0aad65ca
  + Create images and video on OpenArt without leaving ChatGPT. Just describe what you want, add reference images if you lik
- Sample removed content lines:
  -   * ![](https://files.openai.com/content?id=file_0000000020f881f7af2b761b1c59ebce&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=
  - ![](https://files.openai.com/content?id=file_00000000579c81f59643529ca5c68e65&cdn=1&cp=pi&ma=30412800&ts=0&p=pi&cid=8&si
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40OpenArt+Create+a+15-second+launch+v
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40OpenArt+Generate+three+distinct+cam
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)

### https://openai.com/business/plugins/pandadoc/
- lastmod: `2026-09-25T00:08:13.045Z` → `2026-10-08T01:46:47.095Z`
- Content length: 11396 → 11955 chars (delta: +559)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a96ec86423c8191a13c7369bba452
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40PandaDoc+Create+a+draft+%5Bagreemen
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40PandaDoc+Update+%5Bproposal%5D+with
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/parqet/
- lastmod: `2026-09-25T00:17:24.231Z` → `2026-10-08T14:59:53.599Z`
- Content length: 11538 → 12018 chars (delta: +480)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69b68652f0308191a27d7c7096cab4
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://faq.parqet.com/article/79-wo-erhalte-ich-hilfe-bei-parqet
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Parqet+Summarize+my+current+holding
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Parqet+Review+my+open+orders.+Summa
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/patlytics/
- lastmod: `2026-09-25T00:10:59.552Z` → `2026-10-06T01:25:28.806Z`
- Content length: 12704 → 13291 chars (delta: +587)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a84b1b40d3481919f11600f4c7932
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://www.patlytics.ai>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/paypal/
- lastmod: `2026-09-25T00:35:28.002Z` → `2026-10-08T15:00:17.808Z`
- Content length: 11828 → 12396 chars (delta: +568)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a9b5923744081919700d462374ad1
  + [![](https://files.openai.com/content?id=file_000000001f24820c8690d15377467396&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a9b5923744081919700d462374ad1
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://www.paypal.com/us/legalhub/paypal/privacy-full>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40PayPal+Create+an+invoice+for+%24150
  - ### [Plugin supportLearn more](<https://www.paypal.com/us/cshelp/contact-us>)

### https://openai.com/business/plugins/pitchbook/
- lastmod: `2026-09-25T00:35:21.880Z` → `2026-10-08T14:59:50.742Z`
- Content length: 11187 → 12201 chars (delta: +1014)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [![](https://files.openai.com/content?id=file_00000000a4fc722f948ccb2caa4885dc&cdn=1&cp=pi&ma=31190400&ts=0&p=pi&cid=1&s
  + ### [Plugin supportLearn more(opens in a new window)](<https://pitchbook.com/contact>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://pitchbook.com/privacy-policy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://pitchbook.com/privacy-policy>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40PitchBook+Build+a+due+diligence+fac
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40PitchBook+Give+me+a+clean+company+p

### https://openai.com/business/plugins/product-design/
- lastmod: `2026-09-25T00:32:42.549Z` → `2026-10-08T01:45:21.728Z`
- Content length: 10936 → 11368 chars (delta: +432)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_fa77aec24fc08191bc6e57f377126d76?instal
  + [![](https://files.openai.com/content?id=file_00000000fbf481f482108795756c37c9&cdn=1&cp=pi&ma=30240000&ts=0&p=pi&cid=8&s
  + Turn product ideas into designs and research artifacts
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_fa77aec24fc08191bc6e57f377126d76?instal
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000fbf481f482108795756c37c9&cdn=1&cp=pi&ma=30240000&ts=0&p=pi&cid=8&s
  - ### [Plugin supportLearn more](<https://help.openai.com/>)
  - [![](https://files.openai.com/content?id=file_00000000bdb4720caff269fd259bbdff&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)

### https://openai.com/business/plugins/public-equity-investing/
- lastmod: `2026-09-25T00:34:33.225Z` → `2026-10-08T15:00:04.459Z`
- Content length: 13228 → 13978 chars (delta: +750)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + Public equity research
  + [![](https://files.openai.com/content?id=file_00000000328881f5bcf6af410729fa0d&cdn=1&cp=pi&ma=32486400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Public+Equity+Investing+Pressure-te
  - ### [Plugin supportLearn more](<https://help.openai.com/>)
  - Support company research and deal analysis.
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)

### https://openai.com/business/plugins/qbo-connector-by-meridian/
- lastmod: `2026-09-25T00:06:58.154Z` → `2026-10-08T14:59:51.830Z`
- Content length: 11599 → 12031 chars (delta: +432)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a59480048788191838477826d4ee9
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://qbo-connector.meridian.pilot.com/privacy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + [![](https://files.openai.com/content?id=file_0000000044d471f7bd79325f5c4b62b0&cdn=1&cp=pi&ma=30412800&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40QBO+Connector+by+Meridian+Show+me+a
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40QBO+Connector+by+Meridian+How+much+
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/quartr/
- lastmod: `2026-09-25T00:06:38.172Z` → `2026-10-08T14:59:52.270Z`
- Content length: 11661 → 12133 chars (delta: +472)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://quartr.com/terms-of-service/privacy-policy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69b2bc50b4c0819189d86013d62ecc
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Plugin supportLearn more](<https://quartr.com/support>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Quartr+Find+this+company%27s+latest

### https://openai.com/business/plugins/quickbooks/
- lastmod: `2026-09-25T02:46:11.343Z` → `2026-10-08T14:59:54.922Z`
- Content length: 12046 → 12629 chars (delta: +583)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  + [![](https://files.openai.com/content?id=file_000000001e20722faa250d589f9cc0a7&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_697aea3231288191b28a0061066e51
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Intuit+QuickBooks+Compare+my+busine
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/ramp/
- lastmod: `2026-09-25T00:32:27.377Z` → `2026-10-08T15:00:20.404Z`
- Content length: 11983 → 12987 chars (delta: +1004)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69250fb6281c819195b52a1556b006
  + [![](https://files.openai.com/content?id=file_00000000a9cc722fb923cc9523b65b7d&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Ramp+As+a+finance+admin%2C+summariz
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Ramp+What+is+my+current+card+balanc
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/relativity/
- lastmod: `2026-09-25T00:26:21.879Z` → `2026-10-08T01:48:08.219Z`
- Content length: 11776 → 12392 chars (delta: +616)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a7f2ee21b748191ab9ae65f8228f2
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a7f2ee21b748191ab9ae65f8228f2
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://community.relativity.com/s/support>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://help.relativity.com/RelativityOne/Content/Relativity/MCP/RelativityOne_MCP.htm#p
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Relativity+Generate+a+workspace+sto

### https://openai.com/business/plugins/replit/
- lastmod: `2026-09-25T00:33:58.028Z` → `2026-10-08T01:46:02.933Z`
- Content length: 10695 → 11659 chars (delta: +964)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6934801c799081918131791660f028
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://replit.com/site/privacy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - Build real web or mobile apps in ChatGPT by describing what you want, see a live version right away, and iterate through
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - Turn your ideas into real apps.
  - ### [Plugin supportLearn more](<https://docs.replit.com/>)

### https://openai.com/business/plugins/sales/
- lastmod: `2026-09-25T00:33:20.493Z` → `2026-10-08T01:55:50.285Z`
- Content length: 12788 → 13308 chars (delta: +520)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_af5b4b796b588191b3f2c610aa093799?instal
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000e8c081f59ddb247fd01e2217&cdn=1&cp=pi&ma=32140800&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_af5b4b796b588191b3f2c610aa093799?instal
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://help.openai.com/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Sales+Turn+these+meeting+notes+into
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Sales+Build+an+account+plan+for+%5B

### https://openai.com/business/plugins/salesforce/
- lastmod: `2026-09-25T00:36:26.797Z` → `2026-10-08T01:45:21.929Z`
- Content length: 11792 → 12310 chars (delta: +518)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_697d413990c88191a2bf4799604f8f
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_697d413990c88191a2bf4799604f8f
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - Use the Salesforce plugin to review permitted CRM records, understand accounts and deals, summarize pipeline risk, and p
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  - ### [Privacy policyLearn more](<https://www.salesforce.com/company/legal/privacy/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Salesforce+Review+my+open+opportuni

### https://openai.com/business/plugins/scholar-gateway/
- lastmod: `2026-09-25T00:18:19.194Z` → `2026-10-09T06:00:42.933Z`
- Content length: 12609 → 12348 chars (delta: -261)
- Sample new content lines:
  + ![](https://files.openai.com/content?id=file_0000000091ec81f5ad161cd18917605e&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=8&si
  + [![](https://files.openai.com/content?id=file_0000000091ec81f5ad161cd18917605e&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://support.scholargateway.ai/>)
  - ### [Privacy policyLearn more](<https://www.wiley.com/privacy/>)
  - ![](https://files.openai.com/content?id=file_00000000641c71f69c2f11d1ff05cca2&cdn=1&cp=pi&ma=30326400&ts=0&p=pi&cid=7&si

### https://openai.com/business/plugins/scispace/
- lastmod: `2026-09-25T00:06:43.386Z` → `2026-10-09T06:00:44.546Z`
- Content length: 12518 → 13121 chars (delta: +603)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69439d715a7c8191aed9e2f6649e10
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [![](https://files.openai.com/content?id=file_00000000dd8071f6bd9c760f32588469&cdn=1&cp=pi&ma=32659200&ts=0&p=pi&cid=7&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [![](https://files.openai.com/content?id=file_00000000dd8071f6bd9c760f32588469&cdn=1&cp=pi&ma=32659200&ts=0&p=pi&cid=7&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40SciSpace+Compare+the+studies+on+thi

### https://openai.com/business/plugins/scite/
- lastmod: `2026-09-25T00:05:59.446Z` → `2026-10-09T06:00:43.709Z`
- Content length: 11046 → 11609 chars (delta: +563)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.researchsolutions.com/hc/en-us>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://scite.ai/policy>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6952b3a3f1e881918951582d59483c
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://scite.ai/policy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Scite+Find+influential+AI+drug+disc
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Scite+Review+CRISPR+treatments+for+

### https://openai.com/business/plugins/se-ranking/
- lastmod: `2026-09-25T00:30:21.287Z` → `2026-10-08T01:50:25.883Z`
- Content length: 12363 → 12931 chars (delta: +568)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://api@seranking.com>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://seranking.com/legal/privacy-policy.html>)
  + [![](https://files.openai.com/content?id=file_00000000ac3471fab9a6891fb34fde02&cdn=1&cp=pi&ma=31536000&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a0b262d5c0c8191953dd94ba05412
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40SE+Ranking+Compare+our+domain+with+
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/plugins/seismic/
- lastmod: `2026-09-25T00:32:15.319Z` → `2026-10-08T01:56:32.690Z`
- Content length: 12968 → 13578 chars (delta: +610)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.seismic.com/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69dd1d0f73b48191ac4fadf206ad9a
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.seismic.com/legal/policies/privacy-policy/>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000b92071f7981daf071f865701&cdn=1&cp=pi&ma=32227200&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Seismic+Find+approved+content+addre
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Seismic+Find+sales+content+relevant

### https://openai.com/business/plugins/semrush/
- lastmod: `2026-09-25T00:33:28.573Z` → `2026-10-08T01:45:04.732Z`
- Content length: 11530 → 12601 chars (delta: +1071)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.semrush.com/legal/privacy-policy/>)
  + The Semrush MCP provides structured, quantitative SEO and traffic data for domains, keywords, backlinks, and market-leve
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Plugin supportLearn more](<https://www.semrush.com/kb/>)

### https://openai.com/business/plugins/sent/
- lastmod: `2026-09-25T00:17:12.612Z` → `2026-10-08T01:46:43.090Z`
- Content length: 11153 → 11724 chars (delta: +571)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000a7a881f7aa2192e2d1173745&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a764790fbc48191a2b4ba1af90404
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Sent+Find+an+approved+template%2C+p
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://docs.sent.dm/start/reference-guides/support>)
  - ### [Privacy policyLearn more](<https://www.sent.dm/legal/privacy-policy>)

### https://openai.com/business/plugins/sentinelx/
- lastmod: `2026-09-25T00:17:40.543Z` → `2026-10-08T01:47:32.709Z`
- Content length: 12619 → 13192 chars (delta: +573)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69f63e01766881919640f03b5e7912
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://sentinelx.app/support>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40SentinelX+List+all+my+SentinelX+hos
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000591881f7857f80a9b5b758d4&cdn=1&cp=pi&ma=30844800&ts=0&p=pi&cid=8&s
  - ### [Plugin supportLearn more](<https://sentinelx.app/support>)

### https://openai.com/business/plugins/shopify/
- lastmod: `2026-09-25T00:30:16.599Z` → `2026-10-08T01:45:15.989Z`
- Content length: 12265 → 12816 chars (delta: +551)
- Sample new content lines:
  +   * shopify-polaris-checkout-extensions
  +   * shopify-custom-data
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * shopify-pos-ui
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  -   * Shopify Custom Data
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Shopify+Show+my+store%27s+weekly+sa
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Shopify+Check+stock+for+the+product
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * Shopify Admin

### https://openai.com/business/plugins/sider-scholar/
- lastmod: `2026-09-25T00:06:35.090Z` → `2026-10-09T06:00:43.799Z`
- Content length: 13685 → 14272 chars (delta: +587)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://sider.ai/policies/privacy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6948b485f5bc8191adb4df13f369ce
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [![](https://files.openai.com/content?id=file_00000000aeb071f68c578d1acc629d05&cdn=1&cp=pi&ma=31190400&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Sider+Scholar+Compare+the+studies+o
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/slack/
- lastmod: `2026-09-25T00:37:13.376Z` → `2026-10-08T01:46:05.480Z`
- Content length: 11501 → 12061 chars (delta: +560)
- Sample new content lines:
  + ### [Privacy policyLearn more(opens in a new window)](<https://slack.com/privacy-policy>)
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69a1d78e929881919bba0dbda1f643
  + ### [Plugin supportLearn more(opens in a new window)](<https://slack.com/help>)
  + Look up chats and messages
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://slack.com/help>)
  - ### [Privacy policyLearn more](<https://slack.com/privacy-policy>)
  - [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/snowflake/
- lastmod: `2026-09-25T00:34:49.038Z` → `2026-10-08T01:46:53.362Z`
- Content length: 11160 → 11643 chars (delta: +483)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://docs.snowflake.com/>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.snowflake.com/en/legal/privacy/privacy-statement/>)
- Sample removed content lines:
  - ### [Plugin supportLearn more](<https://docs.snowflake.com/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Snowflake+Summarize+the+latest+quer
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/sp-global-deterministic/
- lastmod: `2026-09-25T00:30:04.463Z` → `2026-10-08T14:59:54.851Z`
- Content length: 11590 → 12012 chars (delta: +422)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6980f65d75b881918eaa6d65477d87
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6980f65d75b881918eaa6d65477d87
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40S%26P+Global+-+Deterministic+Compar
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40S%26P+Global+-+Deterministic+Resear

### https://openai.com/business/plugins/spaceship/
- lastmod: `2026-09-25T00:18:13.854Z` → `2026-10-08T01:53:16.215Z`
- Content length: 12098 → 13050 chars (delta: +952)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://spaceship.com/help>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_692e119561848191979b13cc5c0603
  + Spaceship's app enables domain name availability checking and pricing lookup for single or multiple domains. Users can s
  + ### [Privacy policyLearn more(opens in a new window)](<https://spaceship.com/privacy>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000973c720c9d9b1fabee04c427&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=1&s
  - ### [Privacy policyLearn more](<https://spaceship.com/privacy>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Spaceship+Compare+these+domain+opti
  - Search and check domain name availability in ChatGPT with pricing information using Spaceship.
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)

### https://openai.com/business/plugins/stripe/
- lastmod: `2026-09-25T00:33:12.058Z` → `2026-10-08T15:00:09.212Z`
- Content length: 11249 → 11814 chars (delta: +565)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690ab09fa43c8191bca40280e4563
  + ### [Privacy policyLearn more(opens in a new window)](<https://stripe.com/privacy>)
  + Use the Stripe plugin for ChatGPT to analyze live revenue, customers, subscriptions, disputes, and refunds, and build pa
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Stripe+List+disputed+charges+and+dr
  - Use the Stripe plugin for ChatGPT to analyze live revenue, customers, subscriptions, disputes, and refunds, and build pa
  - ### [Plugin supportLearn more](<https://support.stripe.com/>)
  -   * [Codex](</codex/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)

### https://openai.com/business/plugins/tavily-ai/
- lastmod: `2026-09-25T00:18:52.785Z` → `2026-10-08T01:47:31.117Z`
- Content length: 12541 → 13124 chars (delta: +583)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69f271663a288191ac98f46bed7cb0
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.tavily.com/privacy>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Tavily+AI+Find+the+five+most+releva
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Tavily+AI+Find+current+official+doc
  - Real-time web data for agents

### https://openai.com/business/plugins/text/
- lastmod: `2026-09-25T00:06:18.664Z` → `2026-10-08T01:34:54.895Z`
- Content length: 12259 → 12946 chars (delta: +687)
- Sample new content lines:
  + [![](https://files.openai.com/content?id=file_0000000070d081f4b9603b224824bb9f&cdn=1&cp=pi&ma=30672000&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.text.com/legal/privacy-policy/>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Text+Read+this+ticket+and+summarize
  - ### [Plugin supportLearn more](<https://www.text.com/>)

### https://openai.com/business/plugins/the-l-suite-lloyd/
- lastmod: `2026-09-25T00:04:56.595Z` → `2026-10-06T00:37:00.508Z`
- Content length: 12567 → 13070 chars (delta: +503)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a302d66c90c8191911800010290bf
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.lsuite.co/privacy-policy>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://support@thesuite.com>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Lloyd+by+The+L+Suite+Find+peer+disc
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Lloyd+by+The+L+Suite+Find+Braintrus

### https://openai.com/business/plugins/the-l-suite-topcounsel/
- lastmod: `2026-09-25T00:02:35.150Z` → `2026-10-06T00:37:00.118Z`
- Content length: 12024 → 12562 chars (delta: +538)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a2145dc4a0c8191b680935f4edc2e
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.lsuite.co/privacy-policy>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40TopCounsel+Find+lawyers+who+handle+
  - ### [Plugin supportLearn more](<https://support@thesuite.com>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/third-bridge/
- lastmod: `2026-09-25T00:29:41.097Z` → `2026-10-08T14:59:54.368Z`
- Content length: 11873 → 12411 chars (delta: +538)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://www.thirdbridge.com/en-us/about-us/contact-us>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6983505f8b9c8191a2e6f104325b1f
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_000000006f8c8211a7de4892c907f7d9&cdn=1&cp=pi&ma=31276800&ts=0&p=pi&cid=8&s
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Third+Bridge+Find+recent+source+mat
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/transkriptor/
- lastmod: `2026-09-25T02:17:23.416Z` → `2026-10-09T06:00:42.835Z`
- Content length: 12984 → 13545 chars (delta: +561)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_695bd6eb834881918b4f94586de7e9
  + [![](https://files.openai.com/content?id=file_000000009b7871f7a12460345bfad320&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=8&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://transkriptor.com/privacy-policy/>)
- Sample removed content lines:
  - ### [Privacy policyLearn more](<https://transkriptor.com/privacy-policy/>)
  - [![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)

### https://openai.com/business/plugins/trellis-law/
- lastmod: `2026-09-25T00:01:22.974Z` → `2026-10-06T00:53:11.302Z`
- Content length: 11858 → 12476 chars (delta: +618)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://trellis.law/contact>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://trellis.law/privacy-policy>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4438da388081919a4222e44c6cd1
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Trellis+Law+Find+state+trial+court+
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Trellis+Law+Find+%5Bopposing+counse
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s

### https://openai.com/business/plugins/ubersuggest/
- lastmod: `2026-09-25T02:49:44.738Z` → `2026-10-08T01:48:11.009Z`
- Content length: 13235 → 13063 chars (delta: -172)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69457f8444848191918f7c00fea680
  + Ubersuggest helps users research SEO opportunities from ChatGPT, including keyword ideas, domain and page traffic metric
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69457f8444848191918f7c00fea680
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Ubersuggest+Compare+keyword+opportu
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Ubersuggest+Find+keyword+ideas+for+
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_00000000041c71f6901e5042ff41cc0e&cdn=1&cp=pi&ma=30931200&ts=0&p=pi&cid=7&s

### https://openai.com/business/plugins/undermind/
- lastmod: `2026-09-25T02:47:30.292Z` → `2026-10-08T01:47:18.770Z`
- Content length: 11197 → 11960 chars (delta: +763)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a60df60877081919ad4a8109d2753
  + [![](https://files.openai.com/content?id=file_00000000772481f781f782a5166361fb&cdn=1&cp=pi&ma=32745600&ts=0&p=pi&cid=8&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + Bring the scientific literature into ChatGPT: \- Searches comprehensively for relevant papers \- Reads and understands f
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Undermind+Search+for+research+addre
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  -   * ![](https://files.openai.com/content?id=file_00000000684882308fa241e02f361659&cdn=1&cp=pi&ma=32227200&ts=0&p=pi&cid=
  - ![](https://files.openai.com/content?id=file_00000000d38c81f79d41b48aa586e429&cdn=1&cp=pi&ma=32659200&ts=0&p=pi&cid=8&si

### https://openai.com/business/plugins/unicourt/
- lastmod: `2026-09-25T00:00:50.002Z` → `2026-10-06T01:42:21.261Z`
- Content length: 11933 → 12561 chars (delta: +628)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6aa1a3efb4088191ad24d1f65edc2b
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6aa1a3efb4088191ad24d1f65edc2b
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40UniCourt+Find+%5Bcase+name+or+numbe
  - ### [Privacy policyLearn more](<https://unicourt.com/privacy-policy>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/ventor/
- lastmod: `2026-09-25T03:55:07.727Z` → `2026-10-08T01:34:05.157Z`
- Content length: 12516 → 13117 chars (delta: +601)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a343f0d5c048191aa3ebd840ab4c5
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a343f0d5c048191aa3ebd840ab4c5
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a343f0d5c048191aa3ebd840ab4c5
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Ventor+Summarize+chat+metrics+for+t
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://www.ventorchat.com/panel/soporte>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/vercel/
- lastmod: `2026-09-25T00:37:10.944Z` → `2026-10-08T01:47:45.937Z`
- Content length: 11276 → 11824 chars (delta: +548)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690a90ec05c881918afb6a55dc9bb
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * Build Agents
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_connector_690a90ec05c881918afb6a55dc9bb
  +   * CDN Caching
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![](https://files.openai.com/content?id=file_00000000e96c722f90c74485f78831eb&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=1&si
  -   * AI Elements
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Vercel+List+all+domains+for+my+team
  - ![](https://files.openai.com/content?id=file_00000000e96c722f90c74485f78831eb&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=1&si

### https://openai.com/business/plugins/vidiq/
- lastmod: `2026-09-25T04:11:46.720Z` → `2026-10-08T01:46:27.354Z`
- Content length: 11963 → 13130 chars (delta: +1167)
- Sample new content lines:
  + Grow on YouTube, IG & TikTok
  + ![](https://files.openai.com/content?id=file_00000000c15081fb859b4b3326e155b1&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=8&si
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![](https://files.openai.com/content?id=file_00000000c15081fb859b4b3326e155b1&cdn=1&cp=pi&ma=31968000&ts=0&p=pi&cid=8&si
  + Find your next video idea, learn from other creators, and improve your content with vidIQ in ChatGPT. With vidIQ, you ca
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40vidIQ+Analyze+this+channel%27s+rece
  - ### [Privacy policyLearn more](<https://vidiq.com/privacy>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - vidIQ gives you instant access to channel analytics, video performance data, keyword research, and SEO scores. Ask about

### https://openai.com/business/plugins/windsor-ai-facebook-ads/
- lastmod: `2026-09-25T21:17:51.199Z` → `2026-10-08T01:44:00.995Z`
- Content length: 12032 → 12517 chars (delta: +485)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4252575f388191b53f59b232cd07
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.windsor.ai>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://windsor.ai/privacy-statement/>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a4252575f388191b53f59b232cd07
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Windsor.ai+Facebook+Ads+Compare+spe
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://windsor.ai/privacy-statement/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/windsor-ai-google-ads/
- lastmod: `2026-09-25T23:16:52.077Z` → `2026-10-08T01:47:18.004Z`
- Content length: 12129 → 12685 chars (delta: +556)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a566480e04081918043d497d3680a
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.windsor.ai>)
  + ### [Privacy policyLearn more(opens in a new window)](<https://windsor.ai/privacy-statement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Privacy policyLearn more](<https://windsor.ai/privacy-statement/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Windsor.ai+Google+Ads+Find+campaign

### https://openai.com/business/plugins/windsor-ai/
- lastmod: `2026-09-25T20:12:36.596Z` → `2026-10-08T01:47:51.732Z`
- Content length: 13209 → 13809 chars (delta: +600)
- Sample new content lines:
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.windsor.ai>)
  + [![](https://files.openai.com/content?id=file_0000000011848211a4273d3f89547d51&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=8&s
  + ### [Privacy policyLearn more(opens in a new window)](<https://windsor.ai/privacy-statement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_694a52cfaa3c819192bea84eaa2549
- Sample removed content lines:
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [![](https://files.openai.com/content?id=file_0000000011848211a4273d3f89547d51&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=8&s
  - ### [Privacy policyLearn more](<https://windsor.ai/privacy-statement/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/plugins/wolfram/
- lastmod: `2026-09-25T21:57:01.993Z` → `2026-10-09T06:00:43.610Z`
- Content length: 12068 → 12595 chars (delta: +527)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69fe0bf66c8481919c513d79940643
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Wolfram+Evaluate+this+quantitative+
  - ### [Privacy policyLearn more](<https://www.wolfram.com/legal/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Wolfram+Analyze+the+relationship+be

### https://openai.com/business/plugins/xero/
- lastmod: `2026-09-25T20:43:03.398Z` → `2026-10-08T14:59:51.858Z`
- Content length: 11526 → 12082 chars (delta: +556)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a7ee05cee1881918dbfaba26fb555
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.xero.com/legal/privacy/>)
  + [![](https://files.openai.com/content?id=file_00000000179c722f9e8a66d8ff27e98b&cdn=1&cp=pi&ma=31017600&ts=0&p=pi&cid=1&s
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Xero+Review+outstanding+customer+in
  - ### [Plugin supportLearn more](<https://central.xero.com/0/>)
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Xero+Summarize+my+current+cash+posi

### https://openai.com/business/plugins/zoho-crm/
- lastmod: `2026-09-25T21:20:28.828Z` → `2026-10-08T01:48:58.959Z`
- Content length: 11033 → 11611 chars (delta: +578)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a193ef5e804819197c25f88d92d6b
  + Connect to sync Zoho CRM records and activities for use in ChatGPT
  + ### [Privacy policyLearn more(opens in a new window)](<https://www.zoho.com/privacy.html>)
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_6a193ef5e804819197c25f88d92d6b
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
- Sample removed content lines:
  - [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/?surface=work&q=%40Zoho+CRM+Create+a+new+lead+from+thi
  - ### [Privacy policyLearn more](<https://www.zoho.com/privacy.html>)
  -   * [Codex](</codex/>)
  - Connect to sync Zoho CRM records and activities for use in ChatGPT.
  - [![](https://files.openai.com/content?id=file_00000000ea6871f587f4d6459490197f&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=1&s

### https://openai.com/business/plugins/zoom/
- lastmod: `2026-09-25T20:48:56.422Z` → `2026-10-08T01:46:51.080Z`
- Content length: 11426 → 11756 chars (delta: +330)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/plugin_asdk_app_69373a13116c819189d046aea12788
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Plugin supportLearn more(opens in a new window)](<https://support.zoom.us/>)
  + [![](https://files.openai.com/content?id=file_00000000191081f79dfeddb7b502b1bf&cdn=1&cp=pi&ma=32054400&ts=0&p=pi&cid=8&s
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -     Interactive, Read, Write
  - Capabilities
  -   * /build-zoom-bot
  -   * Zoom General

### https://openai.com/business/plugins/zotero/
- lastmod: `2026-09-25T21:35:35.298Z` → `2026-10-09T06:00:43.746Z`
- Content length: 11394 → 11964 chars (delta: +570)
- Sample new content lines:
  + [Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_a572ec6bf27481919ce6fa6e5651eb7b?instal
  + [![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&s
  + ### [Plugin supportLearn more(opens in a new window)](<https://help.openai.com/en/articles/6614161-how-can-i-contact-sup
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [Help centerLearn more(opens in a new window)](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
- Sample removed content lines:
  - [![](https://files.openai.com/content?id=file_00000000a854722fb6f04466d0f95466&cdn=1&cp=pi&ma=30672000&ts=0&p=pi&cid=1&s
  - ### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)
  -   * [Codex](</codex/>)
  - ### [Plugin supportLearn more](<https://help.openai.com/en/articles/6614161-how-can-i-contact-support>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/business/pricing/
- lastmod: `2026-09-24T00:55:41.622Z` → `2026-10-09T08:58:12.263Z`
- Content length: 20829 → 22081 chars (delta: +1252)
- Sample new content lines:
  + Flexible**Plan: Enterprise, Feature: GPT-6.1 Sol, Flexible**
  + ###### Excel, Word, PowerPoint, and Google Sheets extensions
  + Plan: Enterprise, Feature: Excel, Word, PowerPoint, and Google Sheets extensions, Yes
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Plan: Business, Feature: Discover & use Plugins, Yes
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Plan: Business, Feature: Create & share GPTs, Yes
  - ###### Excel, PowerPoint, and Google Sheets extensions
  - Plan: Enterprise, Feature: Discover & use GPTs, Yes
  - Plan: Business, Feature: Share GPTs with your workspace, Yes

### https://openai.com/business/solutions/cybersecurity/
- lastmod: `2026-09-17T15:45:09.208Z` → `2026-10-08T23:40:24.984Z`
- Content length: 12005 → 12217 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/solutions/data/
- lastmod: `2026-09-28T00:29:22.431Z` → `2026-10-08T19:03:26.405Z`
- Content length: 29633 → 29809 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/solutions/design/
- lastmod: `2026-09-27T22:11:16.048Z` → `2026-10-09T01:31:18.199Z`
- Content length: 9871 → 10084 chars (delta: +213)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Help me design a new calendar featureHelp me design a new calendar feature
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - Help me design a new calendar feature
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/solutions/education/
- lastmod: `2026-09-21T21:44:15.397Z` → `2026-10-08T11:04:24.083Z`
- Content length: 8829 → 9097 chars (delta: +268)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Compare course offerings against the skills employers are hiring for.Compare course offerings against the skills employe
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - Compare course offerings against the skills employers are hiring for.
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Contact sales](</contact-sales/>)[OpenAI for K12](<https://chatgpt.com/plans/k12-teachers/>)

### https://openai.com/business/solutions/engineering/
- lastmod: `2026-09-21T21:43:44.739Z` → `2026-10-09T01:31:17.785Z`
- Content length: 10756 → 11001 chars (delta: +245)
- Sample new content lines:
  + Investigate this issue and prepare the smallest tested fix for reviewInvestigate this issue and prepare the smallest tes
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  -   * [Codex](</codex/>)
  - Investigate this issue and prepare the smallest tested fix for review

### https://openai.com/business/solutions/finance/
- lastmod: `2026-09-24T19:14:05.833Z` → `2026-10-08T23:54:13.068Z`
- Content length: 16965 → 17190 chars (delta: +225)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT(opens in a new window)](<https://chatgpt.com/?prompt=Review%20this%20financial%20model%20and%20source%20
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - [Try in ChatGPT(opens in a new window)](<https://chatgpt.com/?surface=work&q=Review+this+financial+model+and+source+mate
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/solutions/finance/workflows/
- lastmod: `2026-09-21T06:46:57.280Z` → `2026-10-08T18:46:01.547Z`
- Content length: 11429 → 11641 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/solutions/marketing/
- lastmod: `2026-09-24T19:44:41.718Z` → `2026-10-08T16:07:07.588Z`
- Content length: 16672 → 16899 chars (delta: +227)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Try in ChatGPT(opens in a new window)](<https://chatgpt.com/?prompt=Using%20our%20product%20roadmap%2C%20customer%20res
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - [Try in ChatGPT(opens in a new window)](<https://chatgpt.com/?surface=work&q=Using+our+product+roadmap%2C+customer+resea
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/solutions/sales/
- lastmod: `2026-09-24T23:02:01.583Z` → `2026-10-09T00:45:23.175Z`
- Content length: 18681 → 18880 chars (delta: +199)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Try in ChatGPT(opens in a new window)](<https://chatgpt.com/?prompt=Find%20my%20highest-priority%20accounts%20this%20we
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - [Try in ChatGPT(opens in a new window)](<https://chatgpt.com/?surface=work&q=Find+my+highest-priority+accounts+this+week
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/updates-to-chatgpt-business-plans-livestream-june-2025/
- lastmod: `2026-06-14T10:06:21.878Z` → `2026-10-07T00:57:09.983Z`
- Content length: 3418 → 3665 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/why-openai/enterprises/
- lastmod: `2026-09-11T20:42:22.962Z` → `2026-10-09T06:40:14.725Z`
- Content length: 10113 → 10325 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/business/why-openai/small-business/
- lastmod: `2026-09-25T22:57:54.698Z` → `2026-10-09T07:32:00.940Z`
- Content length: 14645 → 16063 chars (delta: +1418)
- Sample new content lines:
  + #### Focus on what matters most
  + Create your best work with frontier models by OpenAI. Explore new possibilities, handle complex problems, and create wor
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### Codex
  + # What small businesses only get on ChatGPT Business
- Sample removed content lines:
  - [Learn more](</business/model/>)
  - ![Abstract visualization for an article about AI expanding work.](https://images.ctfassets.net/kftzwdyauwt9/3JAh8VK98LHk
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ## [How AI is expanding what people do at work(opens in a new window)](<https://openai.com/index/how-ai-is-expanding-wha
  - Move fast with powerful AI in a secure workspace with admin controls, SSO, roles, encryption, and no training on your bu

### https://openai.com/business/why-openai/startups/
- lastmod: `2026-09-25T21:23:30.467Z` → `2026-10-01T14:55:02.200Z`
- Content length: 26775 → 26069 chars (delta: -706)
- Sample new content lines:
  + ![](https://images.ctfassets.net/kftzwdyauwt9/79MdLFS1h6y5WexLk2Xgva/b17b0b715d6f60516c032686d119c116/Latent.svg)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  + ### [Penn × First Round (September 24)Join fellow Penn students for an evening with First Round, DRF, and OpenAI in Phil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Builder Lounge: Stockholm (September 15)Join us for an evening of hands-on building, live demos, and networking, co
- Sample removed content lines:
  - ![](https://images.ctfassets.net/kftzwdyauwt9/7tmEeVXWIHcYVmmn885EVK/df2d1348d4250c8a8dadf8234568ec5d/n8n.svg?w=3840&q=9
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### [Columbia × Thrive Capital (September 25)Join fellow Columbia students for an evening with Thrive Capital and OpenAI
  - ![](https://images.ctfassets.net/kftzwdyauwt9/225jV7mulZwMItRaxMtVNv/cf41f6c98aa299244dd47b288cb0e235/Abridge.svg?w=3840
  - ![](https://images.ctfassets.net/kftzwdyauwt9/23ETts8Xjs6vKNNkBCG8k/6014ba3f9a376b5cd1e5d04764c6e24a/Netomi.svg?w=3840&q

### https://openai.com/business/workspace-agents/
- lastmod: `2026-09-09T20:41:41.364Z` → `2026-10-08T22:00:17.492Z`
- Content length: 9618 → 9830 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/charter/
- lastmod: `2026-06-14T14:15:30.890Z` → `2026-10-07T00:20:41.147Z`
- Content length: 6033 → 6280 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/chatgpt-work/
- lastmod: `2026-09-28T04:14:20.196Z` → `2026-10-09T07:47:18.124Z`
- Content length: 11770 → 12779 chars (delta: +1009)
- Sample new content lines:
  + ChatGPT can turn context from your tools and files into documents, presentations, and analyses, using your templates and
  + ### Build on it with your team
  + Schedule one-time or recurring tasks for yourself. With team tasks, delegate shared work like weekly reports and custome
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Growth marketing team space showing a bar chart of first actions and repeat use, with collaborator labels for Jin and 
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ChatGPT Work gathers context, plans the approach, and takes action across your tools, files, and desktop apps to create 
  - ChatGPT can turn context from your tools and files into polished documents, presentations, and analyses that better foll
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ### Create share-ready work

### https://openai.com/chatgpt/use-cases/writing-with-ai/
- lastmod: `2026-09-02T04:44:08.289Z` → `2026-10-07T01:03:06.020Z`
- Content length: 19232 → 19492 chars (delta: +260)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/codex/
- lastmod: `2026-09-28T02:51:22.455Z` → `2026-10-09T07:52:56.507Z`
- Content length: 9777 → 15882 chars (delta: +6105)
- Sample new content lines:
  + Higher usage limits to power full workdays across multiple projects.
  + ### Scale code review confidently
  + ![Codex code review showing edited files and a request to add tests.](https://images.ctfassets.net/kftzwdyauwt9/10UstIzf
  + Codex keeps going when you close your laptop, with reusable cloud environments for every repo. Start tasks, follow progr
  + ![](https://images.ctfassets.net/kftzwdyauwt9/1ISOgL209vkQDcu4Eul8R3/3df6056a21d573629e6e41420fa748ff/supabase.png)
- Sample removed content lines:
  - From routine pull requests to your hardest problems, Codex reliably completes tasks end to end, like building features, 
  - The same powerful coding agent—now in ChatGPT.
  - Schedule Codex to pick up routine but important work like issue triage, alert monitoring, CI/CD, and more, so your team 
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Codex interface showing an engineering task with progress details and a changed-files review panel on a soft gradient 

### https://openai.com/codex/for-work/
- lastmod: `2026-09-15T23:09:29.588Z` → `2026-09-29T17:34:29.557Z`
- Content length: 10146 → 10404 chars (delta: +258)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [Codex](<https://chatgpt.com/codex/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Available on [macOS](<https://persistent.oaistatic.com/codex-app-prod/Codex.dmg>) and [Windows](<https://get.microsoft.c
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/collective-cyberdefense/
- lastmod: `2026-09-25T19:16:28.159Z` → `2026-10-09T06:21:02.157Z`
- Content length: 27800 → 27994 chars (delta: +194)
- Sample new content lines:
  +   * Maze
  +   * Known
  +   * SecureCyber
  +   * MENTUM
  +   * Shepherd AI
- Sample removed content lines:
  - 1Password, 7AI, 27Street, 360 Skills, Abnormal AI, Above Security, Abstract Security, Acalvio, Accenture, ACME Brains, A

### https://openai.com/collective-cyberdefense/application/
- lastmod: `2026-09-25T19:16:24.019Z` → `2026-10-09T06:21:01.841Z`
- Content length: 4122 → 4298 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/company/public-policy/
- lastmod: `2026-09-09T20:40:36.728Z` → `2026-10-08T21:23:57.428Z`
- Content length: 7682 → 7940 chars (delta: +258)
- Sample new content lines:
  + ### [The next era of knowledge workHow Codex is helping people navigate the complexity of modern work.Learn more(opens i
  + ### [Industrial policy for the Intelligence AgeA people-first agenda for navigating the transition to increasingly capab
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [The next era of knowledge workHow Codex is helping people navigate the complexity of modern work.Learn more](<https
  - ### [Industrial policy for the Intelligence AgeA people-first agenda for navigating the transition to increasingly capab
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/consumer-privacy/
- lastmod: `2026-09-22T16:54:03.322Z` → `2026-10-07T16:23:29.950Z`
- Content length: 9433 → 9609 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/contact-sales/
- lastmod: `2026-09-23T17:46:16.818Z` → `2026-10-07T16:24:05.202Z`
- Content length: 690 → 712 chars (delta: +22)
- Sample new content lines:
  +   * SSO, provisioning, role-based access, and admin controls
  +   * Enterprise-grade security and privacy
  +   * Deployment support for large organizations
  + Get help evaluating and deploying ChatGPT and OpenAI’s models across your organization.
  +   * Company knowledge and app access controls
- Sample removed content lines:
  -   * Unlimited use of our best model for work
  -   * Easy member, role, and billing management
  -   * No training on data
  -   * Integrations with Google Drive and more
  - Have a small team? Get started with [ChatGPT Business](<https://chatgpt.com/business/business-plan/>).

### https://openai.com/daybreak/
- lastmod: `2026-09-21T18:14:18.422Z` → `2026-10-09T07:10:01.554Z`
- Content length: 11167 → 11346 chars (delta: +179)
- Sample new content lines:
  + 458
  + 65
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + 661
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - 858
  - 41
  - ![Grid of logos for partners in OpenAI's Daybreak program](https://images.ctfassets.net/kftzwdyauwt9/5DNXdTp2BCly1OpsJ3Q

### https://openai.com/daybreak/contact-cyber-sales/
- lastmod: `2026-09-03T19:26:42.817Z` → `2026-10-07T16:31:17.344Z`
- Content length: 4081 → 4293 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/daybreak/partners-new/
- lastmod: `2026-09-18T20:02:09.590Z` → `2026-10-07T16:38:10.973Z`
- Content length: 19864 → 20076 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/daybreak/partners/
- lastmod: `2026-09-18T20:07:08.996Z` → `2026-10-08T16:43:27.039Z`
- Content length: 27729 → 28103 chars (delta: +374)
- Sample new content lines:
  + ### [Elastic Brings OpenAI GPT Cyber Models Into Elastic Security to Help Defenders Investigate and Remediate Threats Fa
  + ### [How Abnormal and OpenAI are Detecting and Responding to Rogue AI in the CloudLearn more(opens in a new window)](<ht
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ### [Elastic Brings OpenAI GPT Cyber Models Into Elastic Security to Help Defenders Investigate and Remediate Threats Fa
  -   * [Codex](</codex/>)
  - ### [Proofpoint Brings OpenAI GPT Cyber Models into Security Operations to Help Defenders Investigate Threats FasterLear
  - ### [Cloudflare Partners with OpenAI Daybreak Models to Redefine Vulnerability Management with AI-Powered Edge DefenseLe
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/devday/2025/
- lastmod: `2026-09-22T22:05:52.301Z` → `2026-10-09T06:07:49.315Z`
- Content length: 16016 → 16191 chars (delta: +175)
- Sample new content lines:
  +   * [Learn about OpenAI DevDay 2026(opens in a new window)](</index/devday-2026-recap>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Learn about OpenAI DevDay 2026(opens in a new window)](<https://devday.openai.com>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/devday/terms-and-conditions/
- lastmod: `2026-08-24T14:39:01.625Z` → `2026-10-08T08:40:20.065Z`
- Content length: 6470 → 6726 chars (delta: +256)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/economic-research-exchange/
- lastmod: `2026-08-18T10:26:01.488Z` → `2026-10-08T17:49:45.865Z`
- Content length: 7822 → 8069 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/education/
- lastmod: `2026-09-07T16:29:18.720Z` → `2026-10-09T01:25:12.644Z`
- Content length: 11040 → 11252 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/elon-musk/
- lastmod: `2026-09-25T22:18:22.356Z` → `2026-10-08T20:10:31.701Z`
- Content length: 5714 → 5890 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/enterprise-privacy/
- lastmod: `2026-09-25T14:00:02.303Z` → `2026-10-08T18:00:15.473Z`
- Content length: 18163 → 18339 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/events/aws-reinvent/
- lastmod: `2026-09-22T22:15:08.967Z` → `2026-09-29T08:11:00.648Z`
- Content length: 4789 → 4965 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/100-chats-book-request/
- lastmod: `2026-09-18T09:31:07.978Z` → `2026-10-09T09:16:49.969Z`
- Content length: 7038 → 7250 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/aardvark-beta-signup/
- lastmod: `2026-06-14T10:47:40.588Z` → `2026-10-08T17:07:05.319Z`
- Content length: 5691 → 5987 chars (delta: +296)
- Sample new content lines:
  + [Click here(opens in a new window)](<https://platform.openai.com/settings/organization/general>) to find yours
  + Information submitted to us via this form will be handled in accordance with OpenAI’s [Privacy Policy(opens in a new win
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Click here](<https://platform.openai.com/settings/organization/general>) to find yours
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  -   * [Codex](</codex/>)
  - Information submitted to us via this form will be handled in accordance with OpenAI’s [Privacy Policy](</policies/privac

### https://openai.com/form/business/premium-offer/
- lastmod: `2026-09-10T15:41:01.626Z` → `2026-10-09T05:57:18.227Z`
- Content length: 3559 → 3771 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/chatgpt-pro-community/
- lastmod: `2026-09-18T09:31:08.911Z` → `2026-10-09T09:16:47.785Z`
- Content length: 8616 → 8828 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/codex-for-oss/
- lastmod: `2026-08-24T17:53:53.764Z` → `2026-10-08T17:52:50.361Z`
- Content length: 6305 → 6555 chars (delta: +250)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/codex-open-source-fund/
- lastmod: `2026-08-19T22:39:14.569Z` → `2026-10-06T02:00:01.899Z`
- Content length: 4797 → 5044 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/codex-project-showcase-and-feedback/
- lastmod: `2026-09-01T23:40:41.466Z` → `2026-09-29T08:11:04.649Z`
- Content length: 4711 → 4958 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/copyright-disputes/
- lastmod: `2026-08-19T22:53:30.086Z` → `2026-10-09T09:16:50.288Z`
- Content length: 5762 → 8064 chars (delta: +2302)
- Sample new content lines:
  + Where are you asserting rights? *
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Select a country…AfghanistanAland IslandsAlbaniaAlgeriaAndorraAngolaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAus
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/daybreak-cyber-partner-program/
- lastmod: `2026-08-24T17:53:37.748Z` → `2026-10-08T18:41:30.881Z`
- Content length: 4113 → 4360 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/enterprise-trusted-access-for-cyber/
- lastmod: `2026-09-04T23:02:54.813Z` → `2026-10-06T12:16:08.924Z`
- Content length: 4668 → 4882 chars (delta: +214)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/eu-ai-act/
- lastmod: `2026-08-19T22:53:51.704Z` → `2026-10-08T22:46:20.259Z`
- Content length: 6363 → 6610 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/gdpval-customer-contribution/
- lastmod: `2026-06-14T09:57:50.313Z` → `2026-10-08T22:49:19.150Z`
- Content length: 5244 → 5491 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/gpt-live-1-in-the-api/
- lastmod: `2026-08-24T17:53:52.352Z` → `2026-10-07T16:23:22.643Z`
- Content length: 3460 → 3707 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/openai-on-aws/
- lastmod: `2026-08-30T08:28:12.921Z` → `2026-10-08T23:13:49.263Z`
- Content length: 4366 → 4613 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/real-world-knowledge-work/
- lastmod: `2026-06-14T11:57:48.157Z` → `2026-10-08T23:01:22.077Z`
- Content length: 5238 → 5487 chars (delta: +249)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/report-content/
- lastmod: `2026-07-16T02:33:22.557Z` → `2026-10-08T23:08:03.253Z`
- Content length: 7651 → 7918 chars (delta: +267)
- Sample new content lines:
  + ChatGPT Space file
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/rosalind-biodefense-program/
- lastmod: `2026-09-18T09:31:08.477Z` → `2026-10-09T09:16:32.612Z`
- Content length: 11918 → 12130 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/share-your-story/
- lastmod: `2026-09-01T23:40:38.365Z` → `2026-10-08T23:42:10.459Z`
- Content length: 5475 → 5722 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/sponsored-agents-hubspot/
- lastmod: `2026-09-24T05:09:06.127Z` → `2026-10-09T09:16:46.029Z`
- Content length: 6571 → 6747 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/stargate-infrastructure/
- lastmod: `2026-08-24T17:53:37.517Z` → `2026-10-08T23:26:35.530Z`
- Content length: 4245 → 4492 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/subscribe-to-new-sub-processors/
- lastmod: `2026-09-01T23:40:41.052Z` → `2026-10-08T23:30:26.214Z`
- Content length: 3464 → 3711 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/trademark-counterfeit-disputes/
- lastmod: `2026-09-18T09:31:06.301Z` → `2026-10-09T09:16:42.342Z`
- Content length: 7787 → 8050 chars (delta: +263)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Select a country…AfghanistanAland IslandsAlbaniaAlgeriaAndorraAngolaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAus
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - Select a country…AfghanistanAland IslandsAlbaniaAlgeriaAndorraAngolaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAus
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/usage-policy-update/
- lastmod: `2026-06-09T03:28:51.400Z` → `2026-10-08T23:35:26.590Z`
- Content length: 3471 → 3718 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/form/vc-partnerships-application/
- lastmod: `2026-08-24T17:53:52.384Z` → `2026-10-08T23:42:05.689Z`
- Content length: 4023 → 4270 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/global-affairs/a-primer-on-the-eu-ai-act/
- lastmod: `2026-09-22T22:05:58.582Z` → `2026-10-09T00:44:24.564Z`
- Content length: 20165 → 20341 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/global-affairs/accelerating-ai-uptake-in-europe/
- lastmod: `2026-08-19T00:22:56.076Z` → `2026-10-09T06:07:30.863Z`
- Content length: 9484 → 9795 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/argentinas-ai-opportunity/
- lastmod: `2026-06-14T09:18:30.417Z` → `2026-10-09T00:48:02.653Z`
- Content length: 8187 → 8498 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/brazil-ai-moment-is-here/
- lastmod: `2026-08-19T00:13:04.683Z` → `2026-10-09T06:07:30.997Z`
- Content length: 6580 → 6891 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/
- lastmod: `2026-06-14T12:12:42.026Z` → `2026-10-09T01:11:51.186Z`
- Content length: 6433 → 6745 chars (delta: +312)
- Sample new content lines:
  + ## Authors
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
- Sample removed content lines:
  - ## Author
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 

### https://openai.com/global-affairs/eu-code-of-practice/
- lastmod: `2026-08-19T00:32:22.603Z` → `2026-10-09T06:07:30.813Z`
- Content length: 15332 → 15656 chars (delta: +324)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/introducing-chatgpt-gov/
- lastmod: `2026-06-14T08:02:12.485Z` → `2026-10-09T01:53:06.244Z`
- Content length: 8877 → 9132 chars (delta: +255)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/global-affairs/introducing-openai-for-government/
- lastmod: `2026-07-25T07:15:06.518Z` → `2026-10-09T02:17:55.526Z`
- Content length: 8317 → 8632 chars (delta: +315)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/new-economic-analysis/
- lastmod: `2026-09-25T19:34:07.552Z` → `2026-10-09T04:44:03.796Z`
- Content length: 9467 → 9585 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/global-affairs/open-weights-and-ai-for-all/
- lastmod: `2026-06-15T02:52:27.664Z` → `2026-10-09T04:10:01.102Z`
- Content length: 9538 → 9849 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/openai-and-uk-government-partnership/
- lastmod: `2026-07-25T07:19:19.146Z` → `2026-10-09T04:59:26.688Z`
- Content length: 9440 → 9754 chars (delta: +314)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/openai-for-australia/
- lastmod: `2026-09-22T17:02:25.599Z` → `2026-10-09T06:07:29.828Z`
- Content length: 10360 → 10656 chars (delta: +296)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Building standards for the next phase of AIGlobal AffairsSep 21, 2026](</index/building-standards-next-phase-ai/>)
  - ![Helping older adults use AI in everyday life — art card](https://images.ctfassets.net/kftzwdyauwt9/6ewlK5oKVHp0phTezeh
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Helping older adults use AI in everyday lifeGlobal AffairsSep 16, 2026](</index/helping-older-adults-use-ai-in-everyday

### https://openai.com/global-affairs/openai-for-countries/
- lastmod: `2026-09-24T05:22:50.314Z` → `2026-10-09T06:07:30.086Z`
- Content length: 8539 → 8715 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/global-affairs/openai-for-germany/
- lastmod: `2026-07-15T18:27:29.297Z` → `2026-10-03T13:05:46.851Z`
- Content length: 8359 → 8670 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/openai-for-greece/
- lastmod: `2026-07-15T18:27:00.386Z` → `2026-10-03T13:05:22.469Z`
- Content length: 10866 → 11181 chars (delta: +315)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/global-affairs/openais-eu-economic-blueprint/
- lastmod: `2026-09-22T22:05:58.308Z` → `2026-10-09T06:07:33.694Z`
- Content length: 9304 → 9480 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/global-affairs/strategic-collaboration-with-japan-digital-agency/
- lastmod: `2026-07-15T18:29:15.453Z` → `2026-10-03T13:05:44.646Z`
- Content length: 6701 → 7012 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/gpt-5-bio-bug-bounty/
- lastmod: `2026-06-12T22:19:25.585Z` → `2026-10-03T13:05:42.566Z`
- Content length: 6837 → 6749 chars (delta: -88)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/gpt-5/
- lastmod: `2026-09-15T23:12:08.357Z` → `2026-10-08T22:56:50.033Z`
- Content length: 12018 → 12230 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/gpt-tv/
- lastmod: `2026-09-09T22:12:37.901Z` → `2026-10-07T02:53:34.876Z`
- Content length: 717 → 763 chars (delta: +46)
- Sample new content lines:
  + [BLOG(opens in a new window)](<https://openai.com/index/gpt-6-astra/>)[Launch(opens in a new window)](<https://chatgpt.c
- Sample removed content lines:
  - [BLOG](<https://openai.com/index/gpt-6-astra/>)[Launch](<https://chatgpt.com/>)

### https://openai.com/hugging-face-incident-and-misalignment/
- lastmod: `2026-09-28T07:58:08.720Z` → `2026-10-09T04:15:46.703Z`
- Content length: 8570 → 8747 chars (delta: +177)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + # The Hugging Face incident and other third-party impacts from misaligned models
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - # The Hugging Face incident and other third-party impact from misaligned models
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/1-million-businesses-putting-ai-to-work/
- lastmod: `2026-09-22T22:06:08.857Z` → `2026-10-09T06:07:36.408Z`
- Content length: 10636 → 10691 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/1password/
- lastmod: `2026-09-24T12:47:02.989Z` → `2026-10-09T05:55:56.552Z`
- Content length: 12694 → 12709 chars (delta: +15)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/
- lastmod: `2026-09-23T20:41:58.729Z` → `2026-10-09T09:16:48.417Z`
- Content length: 11820 → 11952 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/a-scorecard-for-the-ai-age/
- lastmod: `2026-09-28T02:10:47.928Z` → `2026-10-09T06:20:57.791Z`
- Content length: 14939 → 15071 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/accelerating-antibiotic-discovery/
- lastmod: `2026-09-26T10:16:00.616Z` → `2026-10-07T16:05:13.372Z`
- Content length: 11292 → 11468 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/accelerating-cyber-defense-ecosystem/
- lastmod: `2026-09-25T19:16:31.319Z` → `2026-10-05T19:23:12.729Z`
- Content length: 9143 → 9164 chars (delta: +21)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/accelerating-science-gpt-5/
- lastmod: `2026-07-21T02:31:05.924Z` → `2026-10-08T01:11:19.187Z`
- Content length: 32195 → 32470 chars (delta: +275)
- Sample new content lines:
  + ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Pacing model development in an era of cyber-critical capabilitiesCompanyAug 18, 2026](</index/pacing-model-development-
  - ![math-breakthroughs art-card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2zkd5RIOug4FcEj62mdSF4/3ea9e19c0456289c69f0
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Ten advances in mathematics and theoretical computer sciencePublicationAug 1, 2026](</index/ten-advances-in-mathematics

### https://openai.com/index/accelerating-the-next-phase-ai/
- lastmod: `2026-08-13T23:42:20.362Z` → `2026-10-09T04:53:39.276Z`
- Content length: 13521 → 13591 chars (delta: +70)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/accenture-partnership/
- lastmod: `2026-09-22T22:06:10.713Z` → `2026-10-09T06:07:37.916Z`
- Content length: 9251 → 9306 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/advanced-account-security/
- lastmod: `2026-08-26T19:11:48.958Z` → `2026-10-05T19:23:15.748Z`
- Content length: 11051 → 11231 chars (delta: +180)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/advancing-content-provenance/
- lastmod: `2026-09-25T18:57:15.666Z` → `2026-10-09T06:26:48.124Z`
- Content length: 13370 → 13505 chars (delta: +135)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + Update July 31, 2026:**__We’re expanding this work beyond images. Supported audio generated with OpenAI tools, including
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/advancing-independent-research-ai-alignment/
- lastmod: `2026-09-25T19:18:24.670Z` → `2026-10-08T12:06:53.219Z`
- Content length: 9778 → 9771 chars (delta: -7)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)

### https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/
- lastmod: `2026-09-27T19:39:48.055Z` → `2026-10-09T07:34:37.633Z`
- Content length: 13681 → 13675 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- lastmod: `2026-09-23T20:42:01.849Z` → `2026-10-09T04:44:53.903Z`
- Content length: 18433 → 18427 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/advancing-youth-safety-in-emea/
- lastmod: `2026-09-25T18:57:12.011Z` → `2026-10-01T15:52:33.239Z`
- Content length: 11421 → 11343 chars (delta: -78)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2

### https://openai.com/index/adventhealth/
- lastmod: `2026-09-22T21:15:50.477Z` → `2026-10-09T02:20:19.150Z`
- Content length: 13421 → 13529 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/advisory-group-on-mathematics-and-ai/
- lastmod: `2026-09-25T19:16:10.371Z` → `2026-10-09T08:10:39.430Z`
- Content length: 7981 → 8128 chars (delta: +147)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - [Expanding OpenAI Academy with new learning pathsCompanySep 21, 2026](</index/expanding-openai-academy-with-new-learning

### https://openai.com/index/ai-agent-link-safety/
- lastmod: `2026-08-26T19:11:48.475Z` → `2026-10-08T19:32:06.548Z`
- Content length: 11605 → 12149 chars (delta: +544)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-
  - ![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cah
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/ai-as-the-greatest-source-of-empowerment-for-all/
- lastmod: `2026-09-11T16:19:58.714Z` → `2026-10-03T13:05:25.904Z`
- Content length: 16954 → 17175 chars (delta: +221)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![The Work Now Within Reach — clean cover](https://images.ctfassets.net/kftzwdyauwt9/5iHLTPM4ZhKe4dAwOPfpy2/347b9d804542
  -   * [Codex](</codex/>)
  - [The Work Now Within ReachCompanySep 8, 2026](</index/the-work-now-within-reach/>)
  - ![Supporting journalism from classrooms to newsrooms — listing card](https://images.ctfassets.net/kftzwdyauwt9/2uvvRNdvF
  - # 

### https://openai.com/index/ai-first-hire-small-business/
- lastmod: `2026-07-14T17:37:39.024Z` → `2026-10-09T08:24:20.984Z`
- Content length: 10098 → 10590 chars (delta: +492)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Our approach to government and national security partnerships > Cover image](https://images.ctfassets.net/kftzwdyauwt9
  -   * [Codex](</codex/>)
  - [How ChatGPT adoption has expandedGlobal AffairsJun 30, 2026](</index/how-chatgpt-adoption-has-expanded/>)
  - [Our approach to government and national security partnershipsGlobal AffairsJul 8, 2026](</index/government-national-sec
  - ![Helping K–12 educators build practical AI skills > Cover image](https://images.ctfassets.net/kftzwdyauwt9/190wMCP1bPt9

### https://openai.com/index/ai-for-self-empowerment/
- lastmod: `2026-05-22T19:09:03.013Z` → `2026-10-09T08:58:01.657Z`
- Content length: 9335 → 9241 chars (delta: -94)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/ai-literacy-resources-for-teens-and-parents/
- lastmod: `2026-08-14T13:51:44.402Z` → `2026-10-09T06:07:44.907Z`
- Content length: 5880 → 6375 chars (delta: +495)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [Plugins](</business/plugins/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-
  - ![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cah
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/ai-mental-health-research-grants/
- lastmod: `2026-09-25T18:56:55.196Z` → `2026-10-09T06:07:57.461Z`
- Content length: 12282 → 12347 chars (delta: +65)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - [Sam Altman’s remarks at the United Nations Security CouncilGlobal AffairsSep 23, 2026](</index/sam-altman-un-security-c

### https://openai.com/index/ai-native-company-workflows/
- lastmod: `2026-09-25T19:16:24.416Z` → `2026-10-09T05:55:59.433Z`
- Content length: 14083 → 14259 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/ai-policy-window/
- lastmod: `2026-09-25T19:16:14.192Z` → `2026-10-08T23:51:57.311Z`
- Content length: 20914 → 21032 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/ai-progress-and-recommendations/
- lastmod: `2026-09-22T22:06:07.294Z` → `2026-10-09T06:07:35.375Z`
- Content length: 13841 → 13896 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/airbnb-gpt-6-astra/
- lastmod: `2026-09-25T19:16:16.112Z` → `2026-10-08T22:03:32.299Z`
- Content length: 7978 → 8101 chars (delta: +123)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/amazon-partnership/
- lastmod: `2026-09-22T22:06:05.836Z` → `2026-10-09T04:10:53.707Z`
- Content length: 10335 → 10390 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/an-alien-mind/
- lastmod: `2026-09-25T19:18:08.420Z` → `2026-10-08T12:06:42.439Z`
- Content length: 25695 → 25710 chars (delta: +15)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/announcing-the-stargate-project/
- lastmod: `2026-08-31T19:59:26.146Z` → `2026-10-03T13:05:50.613Z`
- Content length: 6358 → 6605 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/apple-is-getting-this-wrong/
- lastmod: `2026-09-25T19:16:11.671Z` → `2026-10-09T01:10:23.383Z`
- Content length: 21420 → 21552 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/approach-to-data-and-ai/
- lastmod: `2026-09-25T18:57:06.833Z` → `2026-10-01T00:45:07.989Z`
- Content length: 15070 → 15246 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/arco-education/
- lastmod: `2026-09-22T13:14:06.983Z` → `2026-10-08T16:37:00.665Z`
- Content length: 11050 → 11226 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/arvind-kc-chief-people-officer/
- lastmod: `2026-09-22T22:06:04.924Z` → `2026-10-03T13:14:07.138Z`
- Content length: 7079 → 7134 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/asana/
- lastmod: `2026-09-25T22:15:19.134Z` → `2026-10-09T05:55:58.481Z`
- Content length: 7667 → 7709 chars (delta: +42)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - [Proaction boosts sales 60% and saves 75+ hours with CodexSep 25, 2026](</index/proaction/>)
  - ![Proaction customer story art card - Option A](https://images.ctfassets.net/kftzwdyauwt9/46K6EGB5ApjTSkngvI7uU7/ce0c43f
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/astra-for-law/
- lastmod: `2026-09-27T11:48:16.440Z` → `2026-10-09T06:21:05.041Z`
- Content length: 24063 → 24195 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/atv-big-air-tour/
- lastmod: `2026-09-22T21:15:34.204Z` → `2026-10-09T09:02:14.737Z`
- Content length: 11738 → 11846 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/australian-payments-plus/
- lastmod: `2026-09-22T21:15:45.595Z` → `2026-10-09T05:56:02.409Z`
- Content length: 12952 → 13060 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/australian-youth-safety-blueprint/
- lastmod: `2026-09-26T15:28:43.733Z` → `2026-10-09T06:21:22.974Z`
- Content length: 6551 → 6683 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/avatarin/
- lastmod: `2026-09-22T21:15:42.796Z` → `2026-10-08T22:45:56.028Z`
- Content length: 12009 → 12117 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/aws-and-openai-partnership/
- lastmod: `2026-09-22T22:06:10.030Z` → `2026-10-09T06:07:37.268Z`
- Content length: 8819 → 8874 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/axios-developer-tool-compromise/
- lastmod: `2026-08-26T19:11:50.475Z` → `2026-10-09T09:04:10.444Z`
- Content length: 12195 → 12751 chars (delta: +556)
- Sample new content lines:
  + [Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![GPT-Daybreak > Cover](https://images.ctfassets.net/kftzwdyauwt9/2iqsbTTLvgMNteNampw3gW/a38ed04432ee5548c4aec6c7b7a506f
  - [The Defender’s WindowSecurityAug 17, 2026](</index/the-defenders-window/>)
  -   * [Codex](</codex/>)
  - ![The Defender’s Window > Cover](https://images.ctfassets.net/kftzwdyauwt9/2We7bguC4FuOofZ8Lu6LUZ/02049fcee47c460695acab
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

### https://openai.com/index/bbva-2025/
- lastmod: `2026-09-22T21:15:43.227Z` → `2026-10-08T22:48:49.014Z`
- Content length: 8661 → 8769 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/bbva-collaboration-expansion/
- lastmod: `2026-08-13T23:26:49.587Z` → `2026-10-09T06:07:58.282Z`
- Content length: 8374 → 8685 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/index/bbva/
- lastmod: `2026-09-22T21:15:39.424Z` → `2026-10-08T22:48:50.284Z`
- Content length: 14084 → 14192 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/better-prompt-caching-for-gpt-6/
- lastmod: `2026-09-27T14:11:27.620Z` → `2026-10-09T06:33:47.323Z`
- Content length: 11952 → 11941 chars (delta: -11)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/beyond-rate-limits/
- lastmod: `2026-09-22T09:51:45.975Z` → `2026-10-09T05:56:01.299Z`
- Content length: 14583 → 14759 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/bio-bug-bounty/
- lastmod: `2026-09-25T18:56:56.814Z` → `2026-10-01T15:52:32.222Z`
- Content length: 6923 → 6904 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/blue-j/
- lastmod: `2026-09-22T17:02:15.790Z` → `2026-10-03T13:15:19.965Z`
- Content length: 11568 → 11842 chars (delta: +274)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Close-up of copper wire strands with glowing reflections, overlaid with the white Intercom logo centered in the frame.
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  - ![Intercom cover image](https://images.ctfassets.net/kftzwdyauwt9/32rIG6b83UB8GU0atjwCLp/2859930e037889e03ffc8ca685d00d5
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/bny/
- lastmod: `2026-09-22T21:15:48.314Z` → `2026-10-08T22:48:55.347Z`
- Content length: 15662 → 15770 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/booking-com/
- lastmod: `2026-09-22T13:14:11.683Z` → `2026-10-06T17:53:43.817Z`
- Content length: 14071 → 14284 chars (delta: +213)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Nubank elevates customer experiences with OpenAI](https://images.ctfassets.net/kftzwdyauwt9/5Dw4XKiVAmmDUIMaZzyl7E/f6c
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - ![Cover Image](https://images.ctfassets.net/kftzwdyauwt9/5Dw4XKiVAmmDUIMaZzyl7E/f6c8e08c3f6ae5457e8d90abe3c63621/oai_nub
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/boston-childrens-hospital/
- lastmod: `2026-09-22T21:15:50.070Z` → `2026-10-08T22:48:46.671Z`
- Content length: 11419 → 11527 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/braintrust/
- lastmod: `2026-09-22T21:15:49.641Z` → `2026-10-09T05:56:04.802Z`
- Content length: 7885 → 8036 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts/
- lastmod: `2026-09-25T19:16:34.097Z` → `2026-10-09T06:33:33.122Z`
- Content length: 18149 → 18143 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/browsecomp/
- lastmod: `2026-09-25T19:18:40.461Z` → `2026-10-09T06:07:33.700Z`
- Content length: 18375 → 18551 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/bug-bounty-program/
- lastmod: `2026-09-25T18:57:18.337Z` → `2026-10-01T00:45:04.513Z`
- Content length: 7779 → 7955 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/builders-guide-to-gpt-5-6/
- lastmod: `2026-09-28T02:45:20.171Z` → `2026-10-09T06:35:21.332Z`
- Content length: 16200 → 16396 chars (delta: +196)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  + [A practical guide to building with GPT-6ProductOct 2, 2026](</index/practical-guide-building-gpt-6/>)
  + Applied AIGuides
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Derya Unutmaz card image](https://images.ctfassets.net/kftzwdyauwt9/6By12NX9sglstfwFKQTzYB/a28d6f84e91a8dae838f240db4c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Applied AI
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/building-abundant-intelligence/
- lastmod: `2026-09-25T19:16:25.412Z` → `2026-10-09T06:21:27.758Z`
- Content length: 12800 → 12932 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/building-an-ai-native-finance-function/
- lastmod: `2026-09-22T22:05:59.540Z` → `2026-10-08T17:58:47.375Z`
- Content length: 18395 → 18450 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/building-chatgpt-atlas/
- lastmod: `2026-06-17T19:45:16.167Z` → `2026-10-03T13:05:22.864Z`
- Content length: 18230 → 18584 chars (delta: +354)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![UI label with a branching-icon and the text ‘sora/android,’ centered on a starry night-sky background.](https://images
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![1 x 1](https://images.ctfassets.net/kftzwdyauwt9/38dcecW4JVMBEDqex7AmLJ/4dd8e32fc9e06a82c20310d1f83645f3/OpenAI_SoraAn
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/building-codex-windows-sandbox/
- lastmod: `2026-09-22T09:51:50.755Z` → `2026-10-09T05:56:06.870Z`
- Content length: 29092 → 29346 chars (delta: +254)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![Path to Astra — Clean square cover — Neutral Option 062 v1](https://images.ctfassets.net/kftzwdyauwt9/4BabvjDCQdlYN2IS

### https://openai.com/index/building-more-helpful-chatgpt-experiences-for-everyone/
- lastmod: `2026-09-18T17:55:56.024Z` → `2026-10-03T13:05:25.957Z`
- Content length: 10842 → 10828 chars (delta: -14)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/building-openai-with-openai/
- lastmod: `2026-09-14T21:28:01.975Z` → `2026-10-06T17:53:51.575Z`
- Content length: 8625 → 8842 chars (delta: +217)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/building-self-improving-tax-agents-with-codex/
- lastmod: `2026-09-22T09:51:49.622Z` → `2026-10-09T05:56:05.666Z`
- Content length: 23526 → 23702 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/building-standards-next-phase-ai/
- lastmod: `2026-09-27T11:55:50.463Z` → `2026-10-09T06:21:04.256Z`
- Content length: 17874 → 17992 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/building-towards-age-prediction/
- lastmod: `2026-09-25T18:57:05.690Z` → `2026-10-08T17:01:02.118Z`
- Content length: 7914 → 7767 chars (delta: -147)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/

### https://openai.com/index/buy-it-in-chatgpt/
- lastmod: `2026-06-08T17:59:52.690Z` → `2026-10-09T04:45:01.246Z`
- Content length: 11094 → 11032 chars (delta: -62)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/canva/
- lastmod: `2026-09-22T13:14:14.336Z` → `2026-10-03T13:15:25.993Z`
- Content length: 9238 → 9414 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/cars24/
- lastmod: `2026-09-22T21:15:46.421Z` → `2026-10-09T05:56:02.908Z`
- Content length: 12527 → 12635 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/chatgpt-ads-expands-across-europe/
- lastmod: `2026-09-25T19:16:15.745Z` → `2026-10-09T06:33:29.789Z`
- Content length: 9002 → 8891 chars (delta: -111)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
- lastmod: `2026-09-24T02:01:30.125Z` → `2026-10-09T09:08:06.761Z`
- Content length: 9316 → 9367 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/chatgpt-agent-system-card/
- lastmod: `2026-09-25T19:10:40.199Z` → `2026-10-03T13:21:04.591Z`
- Content length: 6268 → 6266 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/chatgpt-can-now-see-hear-and-speak/
- lastmod: `2026-07-28T20:38:10.162Z` → `2026-10-09T04:08:52.960Z`
- Content length: 11569 → 12043 chars (delta: +474)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113a

### https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
- lastmod: `2026-09-25T19:16:24.915Z` → `2026-10-09T06:33:54.904Z`
- Content length: 14437 → 14454 chars (delta: +17)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/chatgpt-enterprise-spend-controls/
- lastmod: `2026-09-22T17:02:25.236Z` → `2026-10-09T06:33:46.131Z`
- Content length: 9277 → 9328 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/chatgpt-for-academic-researchers/
- lastmod: `2026-09-28T00:08:14.754Z` → `2026-10-09T08:50:27.469Z`
- Content length: 14234 → 14410 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/chatgpt-for-excel/
- lastmod: `2026-09-21T06:52:35.074Z` → `2026-10-08T20:34:45.787Z`
- Content length: 15278 → 15355 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/chatgpt-for-teachers/
- lastmod: `2026-09-22T17:02:43.481Z` → `2026-10-09T06:33:51.334Z`
- Content length: 16576 → 16627 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/chatgpt-for-teens/
- lastmod: `2026-09-25T17:46:08.226Z` → `2026-10-09T06:33:33.045Z`
- Content length: 16528 → 16381 chars (delta: -147)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/

### https://openai.com/index/chatgpt-for-veterans/
- lastmod: `2026-09-02T00:20:44.032Z` → `2026-10-09T06:07:44.373Z`
- Content length: 6997 → 7129 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  - [OpenAI supports California’s bill to advance youth AI safetyCompanyAug 31, 2026](</index/supporting-california-bill-adv
  -   * [Codex](</codex/>)
  - ![Our decision on Cursor following its acquisition by SpaceX — cover](https://images.ctfassets.net/kftzwdyauwt9/3gFEgHvt
  - ![California youth AI safety — cover](https://images.ctfassets.net/kftzwdyauwt9/3CsHxgcoiHHUUaYOB1FNiq/38e90de831dad7959

### https://openai.com/index/chatgpt-for-your-most-ambitious-work/
- lastmod: `2026-09-28T04:18:07.366Z` → `2026-10-09T08:23:19.500Z`
- Content length: 21909 → 22369 chars (delta: +460)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [GPT-6 and Intelligent UI for everyoneProductOct 7, 2026](</index/gpt-6-for-everyone/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ## Explore more ways to work together
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/chatgpt-memory-dreaming/
- lastmod: `2026-09-25T19:18:12.961Z` → `2026-10-09T06:33:36.823Z`
- Content length: 34920 → 34867 chars (delta: -53)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/chatgpt-shopping-research/
- lastmod: `2026-07-25T07:08:53.435Z` → `2026-10-08T01:32:36.014Z`
- Content length: 14238 → 14043 chars (delta: -195)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/chatgpt-whatsapp-transition/
- lastmod: `2026-09-18T17:55:56.408Z` → `2026-10-03T13:05:26.672Z`
- Content length: 6619 → 6622 chars (delta: +3)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
- Sample removed content lines:
  - [Introducing Astra for LawCompanySep 17, 2026](</index/astra-for-law/>)
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/chatgpt/
- lastmod: `2026-08-14T20:20:32.658Z` → `2026-10-09T06:33:29.134Z`
- Content length: 16993 → 17472 chars (delta: +479)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113a

### https://openai.com/index/chime-vineet-mehra/
- lastmod: `2026-09-22T21:15:50.602Z` → `2026-10-08T22:49:02.059Z`
- Content length: 13777 → 13885 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/chip-ganassi-racing/
- lastmod: `2026-09-08T22:42:52.947Z` → `2026-10-09T08:56:36.684Z`
- Content length: 13446 → 13580 chars (delta: +134)
- Sample new content lines:
  + ![An OpenAI number 10 pit sign beside the racing circuit.](https://images.ctfassets.net/kftzwdyauwt9/35f2bCjeUVEipAglfs5
  + ![An orange R&D Co. OpenAI pin on blue racing merchandise.](https://images.ctfassets.net/kftzwdyauwt9/5V1cziPDHgltMfrxGH
  + ![A stylized visualization of the front wheel and suspension of a race car.](https://images.ctfassets.net/kftzwdyauwt9/6
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ## Limited-edition merch
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![A black IndyCar race car with OpenAI branding speeds on a track, viewed from above, with motion blur emphasizing its f
  - Off to a hot start, the CGR team looks to continue their momentum and help driver Alex Palou bring home his first win at
  - ![A blue IndyCar race car with OpenAI branding is being towed on a racing street circuit lined with spectators on both s
  - ![A group of five people, four men in white racing suits with OpenAI logos and one woman in a white shirt and black pant

### https://openai.com/index/circles/
- lastmod: `2026-09-22T21:15:38.900Z` → `2026-10-09T05:56:00.082Z`
- Content length: 11975 → 12083 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/cisco/
- lastmod: `2026-09-22T21:15:39.691Z` → `2026-10-09T05:56:00.805Z`
- Content length: 10972 → 11080 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/codex-collaborator-creative-team/
- lastmod: `2026-09-22T09:51:45.894Z` → `2026-10-09T05:56:01.837Z`
- Content length: 10645 → 10821 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/codex-flexible-pricing-for-teams/
- lastmod: `2026-09-28T02:51:21.751Z` → `2026-10-09T06:53:14.125Z`
- Content length: 7166 → 7160 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/codex-for-almost-everything/
- lastmod: `2026-09-28T02:51:20.729Z` → `2026-10-09T06:53:12.428Z`
- Content length: 9984 → 9978 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/codex-for-every-role-tool-workflow/
- lastmod: `2026-09-22T09:51:46.101Z` → `2026-10-09T06:33:53.686Z`
- Content length: 46774 → 42025 chars (delta: -4749)
- Sample new content lines:
  + ![](https://images.ctfassets.net/kftzwdyauwt9/2baLN2AEXCHyCuaWV7Rxp1/9407ee14a5d2867c817aa5b6329305c2/Calendly-icon.png)
  + ![](https://images.ctfassets.net/kftzwdyauwt9/J3WgRb8CkUgwhLwQc9SoM/3db2abfe24c3c4243aa5246a16ec307b/Similarweb-icon.png
  + ![](https://images.ctfassets.net/kftzwdyauwt9/7hlI2Ah6VFQXc5UA4xO3dJ/1609e428e487f2dd56815e4179a44676/Moodys-icon.png)
  + ![](https://images.ctfassets.net/kftzwdyauwt9/76ksqYxVsKQnSZzktpwQ4h/2cbd51ef2fbd9025eaccd98a0c7148d2/Quartr-icon.png)
  + ![](https://images.ctfassets.net/kftzwdyauwt9/RJ8DfEys6DtH4MzH97r33/540a8e5376d34cbbcc127865eacaa9d6/Chronograph-icon.pn
- Sample removed content lines:
  - ![](https://images.ctfassets.net/kftzwdyauwt9/3WWKQXRdiC4GIyPAMKI0CM/00d0d188c0b340d674b85a1e429616ed/Morningstar-icon.p
  - ![](https://images.ctfassets.net/kftzwdyauwt9/3d4CaGZAPxpmD0iKgWzTbq/0b04b3c611b713956a974c34d1ffd9ee/Granola-icon.png?w
  - ![](https://images.ctfassets.net/kftzwdyauwt9/4JhQzAJiB6fMWaPwuQM5Yt/abd942e97c6c019fa1a353072033a1d5/GMail-icon.png?w=3
  - ![](https://images.ctfassets.net/kftzwdyauwt9/6Uxb4FbhhqBJTVDMVU6Tex/c5201911b5a952fc306ebd0c1a42b3e2/Hubspot-icon.png?w
  - ![](https://images.ctfassets.net/kftzwdyauwt9/7qxEB5vRm1XLvgAPctRVsF/414605b475141299b48d8d2a3508f710/Zoom-icon.png?w=38

### https://openai.com/index/codex-for-knowledge-work/
- lastmod: `2026-09-22T09:51:48.094Z` → `2026-10-09T05:56:06.454Z`
- Content length: 5572 → 6952 chars (delta: +1380)
- Sample new content lines:
  + [View all](</news/>)
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/codex-maxxing-long-running-work/
- lastmod: `2026-07-15T20:24:27.542Z` → `2026-10-09T09:11:00.026Z`
- Content length: 5314 → 5631 chars (delta: +317)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How AI-native companies turn workflows into operating capabilityAI AdoptionSep 1, 2026](</index/ai-native-company-workf
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [Introducing the ChatGPT for small business programAI AdoptionJul 21, 2026](</index/introducing-chatgpt-small-business-p
  -   * [Codex](</codex/>)
  - [How to manage AI investments in the agentic eraAI AdoptionJul 14, 2026](</index/managing-ai-investments-in-agentic-era/
  - [AI Adoption](</news/ai-adoption/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/codex-now-generally-available/
- lastmod: `2026-09-22T09:51:51.486Z` → `2026-10-09T05:56:07.361Z`
- Content length: 11276 → 11327 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/codex-quantum-computing-experiments/
- lastmod: `2026-09-25T19:16:15.416Z` → `2026-10-09T05:55:58.908Z`
- Content length: 12233 → 12409 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/codex-security-now-in-research-preview/
- lastmod: `2026-09-25T19:16:29.374Z` → `2026-10-09T06:33:31.899Z`
- Content length: 15119 → 15113 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/cognition-devin-testing-with-astra/
- lastmod: `2026-09-22T13:14:02.182Z` → `2026-10-07T23:42:31.028Z`
- Content length: 6897 → 7071 chars (delta: +174)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/commonwealth-bank-of-australia/
- lastmod: `2026-09-22T21:15:39.454Z` → `2026-10-08T22:48:50.544Z`
- Content length: 5929 → 6037 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/computer-using-agent/
- lastmod: `2026-06-20T08:53:08.159Z` → `2026-10-09T04:45:34.861Z`
- Content length: 32074 → 32518 chars (delta: +444)
- Sample new content lines:
  + Computer use| OSWorld| 38.1%| [22.0%(opens in a new window)](<https://www.anthropic.com/news/3-5-models-and-computer-use
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Browser use| WebArena| 58.1%| [36.2%(opens in a new window)](<https://huggingface.co/spaces/ServiceNow/browsergym-leader
- Sample removed content lines:
  - Evaluation details are described [here](<https://cdn.openai.com/cua/CUA_eval_extra_information.pdf>)
  -   * [Codex](</codex/>)
  - Computer use| OSWorld| 38.1%| [22.0%](<https://www.anthropic.com/news/3-5-models-and-computer-use>)| -| [72.4%](<https:/
  - WebVoyager| 87.0%| [56.0%](<https://www.trykura.com/benchmarks>)| [87.0%](<https://www.trykura.com/benchmarks>)| -  
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/consensus/
- lastmod: `2026-07-28T15:55:17.123Z` → `2026-10-08T16:37:03.296Z`
- Content length: 11972 → 11925 chars (delta: -47)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/continuing-microsoft-partnership/
- lastmod: `2026-09-22T22:05:59.833Z` → `2026-10-09T09:04:32.783Z`
- Content length: 7720 → 7775 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/continuous-voice-interaction-with-gpt-live/
- lastmod: `2026-09-25T19:16:22.290Z` → `2026-10-09T09:11:20.427Z`
- Content length: 25039 → 25171 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/cooley-gopublic/
- lastmod: `2026-09-26T15:05:09.956Z` → `2026-10-08T22:48:49.747Z`
- Content length: 10441 → 10440 chars (delta: -1)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - [Proaction boosts sales 60% and saves 75+ hours with CodexSep 25, 2026](</index/proaction/>)
  - ![Proaction customer story art card - Option A](https://images.ctfassets.net/kftzwdyauwt9/46K6EGB5ApjTSkngvI7uU7/ce0c43f
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug/
- lastmod: `2026-09-17T11:33:59.495Z` → `2026-10-05T19:08:14.567Z`
- Content length: 29063 → 29275 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/creating-new-simulations-black-holes/
- lastmod: `2026-09-08T20:26:05.464Z` → `2026-10-07T16:05:14.521Z`
- Content length: 11389 → 11601 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/cred-swamy-seetharaman/
- lastmod: `2026-09-23T20:42:04.632Z` → `2026-10-08T22:46:04.275Z`
- Content length: 9853 → 10029 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/cycling-across-antarctica/
- lastmod: `2026-09-08T20:26:06.367Z` → `2026-10-07T16:05:15.544Z`
- Content length: 11169 → 11381 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/dai-nippon-printing/
- lastmod: `2026-09-22T21:15:43.120Z` → `2026-10-08T22:48:53.943Z`
- Content length: 13157 → 13265 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/dali-rajic-chief-revenue-officer/
- lastmod: `2026-09-22T22:05:58.233Z` → `2026-10-09T06:21:01.115Z`
- Content length: 7615 → 7670 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/dall-e-2/
- lastmod: `2026-09-25T19:18:10.271Z` → `2026-10-09T04:47:39.740Z`
- Content length: 11405 → 11581 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/dall-e-3/
- lastmod: `2026-09-25T19:18:09.213Z` → `2026-10-09T06:12:10.960Z`
- Content length: 16581 → 16757 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/databricks/
- lastmod: `2026-09-22T21:15:51.465Z` → `2026-10-09T05:56:05.741Z`
- Content length: 7595 → 7746 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/datadog/
- lastmod: `2026-09-22T19:25:18.755Z` → `2026-10-09T05:56:03.818Z`
- Content length: 11166 → 11274 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/david-velez-robin-vince-join-openai-boards/
- lastmod: `2026-09-22T22:06:04.011Z` → `2026-10-03T13:14:06.235Z`
- Content length: 8809 → 8864 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/daybreak-for-frontline-defenders/
- lastmod: `2026-09-25T19:16:20.362Z` → `2026-10-09T06:21:22.421Z`
- Content length: 13916 → 14212 chars (delta: +296)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![The Defender’s Window > Cover](https://images.ctfassets.net/kftzwdyauwt9/2We7bguC4FuOofZ8Lu6LUZ/02049fcee47c460695acab
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [The Defender’s WindowSecurityAug 17, 2026](</index/the-defenders-window/>)

### https://openai.com/index/daybreak-models-are-now-available-on-aws/
- lastmod: `2026-09-18T17:55:47.731Z` → `2026-10-09T06:33:33.975Z`
- Content length: 6955 → 7032 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/daybreak-securing-the-world/
- lastmod: `2026-09-22T22:06:03.708Z` → `2026-10-05T19:23:13.300Z`
- Content length: 22210 → 22392 chars (delta: +182)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/dell-codex-enterprise-partnership/
- lastmod: `2026-09-22T19:25:23.572Z` → `2026-10-09T05:56:06.149Z`
- Content length: 7594 → 7649 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/deployment-simulation/
- lastmod: `2026-09-25T19:18:11.856Z` → `2026-10-09T04:20:01.096Z`
- Content length: 27249 → 27426 chars (delta: +177)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [An OpenAI model proposes a solution to the Navier–Stokes problemResearchSep 8, 2026](</index/navier-stokes-solution/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/descript/
- lastmod: `2026-09-22T13:14:08.040Z` → `2026-10-03T13:15:21.368Z`
- Content length: 13885 → 14089 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/designing-agents-to-resist-prompt-injection/
- lastmod: `2026-09-25T19:16:30.715Z` → `2026-10-05T19:23:12.356Z`
- Content length: 14108 → 14551 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/detecting-wildfires-early/
- lastmod: `2026-09-21T20:26:06.796Z` → `2026-10-07T16:05:15.225Z`
- Content length: 10471 → 10647 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/deutsche-telekom/
- lastmod: `2026-09-22T21:15:46.911Z` → `2026-10-08T22:48:56.239Z`
- Content length: 11006 → 11114 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/devday-2026/
- lastmod: `2026-09-28T02:51:23.058Z` → `2026-10-09T06:53:14.098Z`
- Content length: 3773 → 4052 chars (delta: +279)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + See [everything announced⁠](<https://openai.com/index/devday-2026-recap/>) at DevDay 2026.
  + ## Update
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/
- lastmod: `2026-09-18T17:55:53.516Z` → `2026-10-09T06:33:39.045Z`
- Content length: 9491 → 9703 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/diagnose-rare-childhood-diseases/
- lastmod: `2026-09-17T11:33:58.923Z` → `2026-10-09T09:11:22.155Z`
- Content length: 21424 → 21636 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-ai-uses/
- lastmod: `2026-08-26T19:11:43.923Z` → `2026-10-05T19:23:16.149Z`
- Content length: 5282 → 5826 chars (delta: +544)
- Sample new content lines:
  + [Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![GPT-Daybreak > Cover](https://images.ctfassets.net/kftzwdyauwt9/2iqsbTTLvgMNteNampw3gW/a38ed04432ee5548c4aec6c7b7a506f
  - [The Defender’s WindowSecurityAug 17, 2026](</index/the-defenders-window/>)
  -   * [Codex](</codex/>)
  - ![The Defender’s Window > Cover](https://images.ctfassets.net/kftzwdyauwt9/2We7bguC4FuOofZ8Lu6LUZ/02049fcee47c460695acab
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-a2z/
- lastmod: `2026-09-25T18:57:06.423Z` → `2026-10-01T15:52:21.366Z`
- Content length: 16249 → 16425 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-bad-grammar/
- lastmod: `2026-09-25T18:57:13.488Z` → `2026-10-01T15:52:24.546Z`
- Content length: 10048 → 10224 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-bet-bot/
- lastmod: `2026-09-16T15:53:16.152Z` → `2026-10-06T01:44:14.145Z`
- Content length: 11410 → 11622 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-corrupt-comment/
- lastmod: `2026-09-16T15:59:01.415Z` → `2026-10-06T01:49:05.612Z`
- Content length: 7522 → 7734 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-criminal-scam-operation/
- lastmod: `2026-09-25T18:57:00.417Z` → `2026-10-01T15:52:19.173Z`
- Content length: 12771 → 12947 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-cyber-special-operations/
- lastmod: `2026-09-17T11:39:46.504Z` → `2026-10-07T02:00:15.230Z`
- Content length: 32982 → 33194 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-cyber-threat-actors/
- lastmod: `2026-09-25T18:57:02.694Z` → `2026-10-01T15:52:19.857Z`
- Content length: 7478 → 7654 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-cyberav3ngers/
- lastmod: `2026-09-16T16:02:41.819Z` → `2026-10-06T06:28:07.504Z`
- Content length: 8655 → 8867 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-data-center-bandwagon/
- lastmod: `2026-09-25T18:56:48.673Z` → `2026-10-01T15:52:17.043Z`
- Content length: 10552 → 10728 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-date-bait/
- lastmod: `2026-09-25T18:56:49.991Z` → `2026-10-01T15:52:18.466Z`
- Content length: 10487 → 10663 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-deceptive-employment-scheme/
- lastmod: `2026-09-25T18:56:52.230Z` → `2026-10-01T15:52:24.162Z`
- Content length: 7918 → 8094 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-doppelganger/
- lastmod: `2026-09-25T18:57:12.714Z` → `2026-10-01T15:52:25.483Z`
- Content length: 12063 → 12239 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-false-witness/
- lastmod: `2026-09-25T18:56:49.138Z` → `2026-10-01T15:52:17.248Z`
- Content length: 9276 → 9452 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-fish-food/
- lastmod: `2026-09-25T18:56:50.944Z` → `2026-10-01T15:52:21.226Z`
- Content length: 11520 → 11696 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-ghana-election/
- lastmod: `2026-09-16T16:02:13.482Z` → `2026-10-06T08:29:04.570Z`
- Content length: 8730 → 8942 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-helgoland-bite/
- lastmod: `2026-09-16T15:59:48.160Z` → `2026-10-06T14:28:25.686Z`
- Content length: 7957 → 8169 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-high-five/
- lastmod: `2026-09-16T16:00:51.326Z` → `2026-10-06T14:28:21.322Z`
- Content length: 8705 → 8917 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-hoax-russian-troll/
- lastmod: `2026-09-16T15:53:39.511Z` → `2026-10-06T04:22:20.668Z`
- Content length: 7865 → 8077 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/
- lastmod: `2026-09-25T19:16:19.817Z` → `2026-10-09T06:21:29.091Z`
- Content length: 20182 → 20105 chars (delta: -77)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + [Safety](</news/safety-alignment/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Global Affairs](</news/global-affairs/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-iranian-influence-nexus/
- lastmod: `2026-09-16T15:57:40.340Z` → `2026-10-06T08:49:10.669Z`
- Content length: 9516 → 9728 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-it-workers/
- lastmod: `2026-09-25T18:57:04.618Z` → `2026-10-01T15:52:17.363Z`
- Content length: 8701 → 8877 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-iuvm/
- lastmod: `2026-09-25T18:57:06.066Z` → `2026-10-01T15:52:22.842Z`
- Content length: 6869 → 7045 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-korean-language-malware-support/
- lastmod: `2026-09-25T18:56:52.914Z` → `2026-10-01T15:52:22.393Z`
- Content length: 7489 → 7665 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-nine-emdash-line/
- lastmod: `2026-09-25T18:57:09.722Z` → `2026-10-01T15:52:20.380Z`
- Content length: 11956 → 12132 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-no-bell/
- lastmod: `2026-09-17T11:42:11.283Z` → `2026-10-07T01:49:42.918Z`
- Content length: 12475 → 12687 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-peer-review/
- lastmod: `2026-09-16T16:01:40.374Z` → `2026-10-06T10:31:48.094Z`
- Content length: 9093 → 9305 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-phishing-and-scripting-support/
- lastmod: `2026-09-25T18:57:13.360Z` → `2026-10-01T15:52:20.702Z`
- Content length: 10202 → 10378 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-prc-linked-abuse/
- lastmod: `2026-09-25T18:57:20.250Z` → `2026-10-01T15:52:21.129Z`
- Content length: 9211 → 9387 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-romance-baiting-scam/
- lastmod: `2026-09-25T18:56:52.817Z` → `2026-10-01T15:52:23.835Z`
- Content length: 11437 → 11613 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-romance-scam/
- lastmod: `2026-09-25T18:57:12.529Z` → `2026-10-01T15:52:19.956Z`
- Content length: 11689 → 11865 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-russian-speaking-malware-tooling/
- lastmod: `2026-09-25T18:57:21.846Z` → `2026-10-01T15:52:23.357Z`
- Content length: 8479 → 8655 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-rwandan-election-content/
- lastmod: `2026-09-16T16:03:16.083Z` → `2026-10-06T01:46:14.972Z`
- Content length: 7257 → 7469 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-scam-operations/
- lastmod: `2026-09-25T18:56:51.705Z` → `2026-10-01T15:52:22.934Z`
- Content length: 12617 → 12793 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-scopecreep/
- lastmod: `2026-09-25T18:57:05.025Z` → `2026-10-01T15:52:19.159Z`
- Content length: 8319 → 8495 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-silver-lining-playbook/
- lastmod: `2026-09-25T18:56:49.531Z` → `2026-10-01T15:52:17.984Z`
- Content length: 11130 → 11306 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-sneer-review/
- lastmod: `2026-09-25T18:56:50.937Z` → `2026-10-01T15:52:20.631Z`
- Content length: 11235 → 11411 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-spamouflage/
- lastmod: `2026-09-25T18:56:52.826Z` → `2026-10-01T15:52:24.849Z`
- Content length: 11270 → 11446 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-sponsored-discontent/
- lastmod: `2026-09-16T16:02:24.746Z` → `2026-10-06T10:31:04.930Z`
- Content length: 11501 → 11713 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-stop-news-2024/
- lastmod: `2026-09-16T16:02:51.717Z` → `2026-10-06T02:50:23.423Z`
- Content length: 12070 → 12282 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-stop-news-2025/
- lastmod: `2026-09-25T18:57:20.763Z` → `2026-10-01T15:52:43.110Z`
- Content length: 11634 → 11810 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-storm-0817/
- lastmod: `2026-09-16T15:58:39.528Z` → `2026-10-06T04:27:07.413Z`
- Content length: 8741 → 8953 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-storm-2035-2024/
- lastmod: `2026-09-16T15:54:04.225Z` → `2026-10-06T02:48:44.815Z`
- Content length: 9724 → 9936 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-storm-2035-2025/
- lastmod: `2026-09-16T16:01:05.521Z` → `2026-10-06T12:47:32.272Z`
- Content length: 10473 → 10685 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-sweetspecter/
- lastmod: `2026-09-16T16:02:29.899Z` → `2026-10-06T06:31:53.983Z`
- Content length: 10217 → 10429 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-task-scam/
- lastmod: `2026-09-25T18:56:51.702Z` → `2026-10-01T15:52:22.181Z`
- Content length: 9459 → 9635 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-tech-and-tariffs/
- lastmod: `2026-09-25T18:57:10.068Z` → `2026-10-01T15:52:18.128Z`
- Content length: 14385 → 14561 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-tort-report/
- lastmod: `2026-09-16T16:27:02.548Z` → `2026-10-06T01:38:41.402Z`
- Content length: 6456 → 6668 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-trolling-stone/
- lastmod: `2026-09-17T11:25:35.241Z` → `2026-10-07T01:23:57.615Z`
- Content length: 13274 → 13486 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-uncle-spam/
- lastmod: `2026-09-25T18:56:51.706Z` → `2026-10-01T15:52:21.605Z`
- Content length: 7849 → 8025 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-vague-focus/
- lastmod: `2026-09-25T18:57:05.498Z` → `2026-10-01T15:52:19.286Z`
- Content length: 10063 → 10239 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-vixen-keyhole-panda/
- lastmod: `2026-09-16T15:57:02.675Z` → `2026-10-06T12:37:53.703Z`
- Content length: 8297 → 8509 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-wrong-number/
- lastmod: `2026-09-25T18:56:52.228Z` → `2026-10-01T15:52:24.774Z`
- Content length: 10739 → 10915 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai-zero-zeno/
- lastmod: `2026-09-25T18:56:52.116Z` → `2026-10-01T15:52:23.106Z`
- Content length: 12969 → 13145 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/disrupting-malicious-uses-of-ai/
- lastmod: `2026-09-25T18:59:39.526Z` → `2026-10-01T15:52:20.097Z`
- Content length: 9729 → 9848 chars (delta: +119)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Disrupting a new covert influence campaign from RussiaSafetyAug 25, 2026](</index/disrupting-malicious-uses-of-ai-influ
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [“Data Center Bandwagon” Campaign: US-targeted influence activitySafetyJun 1, 2026](</index/disrupting-malicious-uses-of
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/economic-research-exchange-request-for-proposals/
- lastmod: `2026-07-29T23:13:14.200Z` → `2026-10-08T05:10:04.989Z`
- Content length: 12523 → 12813 chars (delta: +290)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/election-safeguards-2026/
- lastmod: `2026-09-25T19:16:20.124Z` → `2026-10-08T03:26:58.745Z`
- Content length: 15968 → 16086 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/emea-youth-and-wellbeing-grant/
- lastmod: `2026-09-02T14:23:48.670Z` → `2026-10-08T22:09:52.122Z`
- Content length: 11029 → 11361 chars (delta: +332)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/index/endava-frontiers/
- lastmod: `2026-09-22T21:15:41.779Z` → `2026-10-09T05:56:01.213Z`
- Content length: 9718 → 9869 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/endava/
- lastmod: `2026-09-22T21:15:48.543Z` → `2026-10-09T05:56:03.986Z`
- Content length: 10246 → 10397 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/eneos-materials/
- lastmod: `2026-09-22T21:15:40.365Z` → `2026-10-08T22:48:52.690Z`
- Content length: 14171 → 14322 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/equipping-workers-with-insights-about-compensation/
- lastmod: `2026-09-25T19:34:05.903Z` → `2026-10-07T19:26:00.982Z`
- Content length: 8721 → 8839 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/estee-lauder/
- lastmod: `2026-09-24T05:56:31.230Z` → `2026-10-08T22:48:50.105Z`
- Content length: 12626 → 12802 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/estimating-worst-case-frontier-risks-of-open-weight-llms/
- lastmod: `2026-09-25T19:10:30.326Z` → `2026-10-03T13:21:02.878Z`
- Content length: 6004 → 6002 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/
- lastmod: `2026-09-25T19:16:24.404Z` → `2026-10-09T06:33:30.705Z`
- Content length: 10103 → 10097 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/expanding-ai-access-us-government/
- lastmod: `2026-09-25T19:16:16.277Z` → `2026-10-08T21:21:07.438Z`
- Content length: 10885 → 11003 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/expanding-data-residency-access-to-business-customers-worldwide/
- lastmod: `2026-07-15T16:36:14.149Z` → `2026-10-08T22:52:02.484Z`
- Content length: 8627 → 8563 chars (delta: -64)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/
- lastmod: `2026-09-25T19:16:32.190Z` → `2026-10-09T01:54:56.755Z`
- Content length: 19214 → 19235 chars (delta: +21)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/expanding-on-how-voice-engine-works-and-our-safety-research/
- lastmod: `2026-09-25T18:57:21.070Z` → `2026-10-01T00:45:09.332Z`
- Content length: 10592 → 10768 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/expanding-openai-academy-with-new-learning-paths/
- lastmod: `2026-09-27T08:53:31.242Z` → `2026-10-09T09:05:15.624Z`
- Content length: 11597 → 11729 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/expanding-our-presence-in-brazil/
- lastmod: `2026-09-25T19:16:21.975Z` → `2026-10-09T08:54:10.884Z`
- Content length: 15552 → 15684 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/expedia-jochen-koedijk/
- lastmod: `2026-09-22T13:14:13.875Z` → `2026-10-06T17:53:46.131Z`
- Content length: 12779 → 12887 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/expert-council-on-well-being-and-ai/
- lastmod: `2026-09-25T18:56:56.822Z` → `2026-10-09T06:07:36.328Z`
- Content length: 10103 → 10279 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/
- lastmod: `2026-09-25T19:18:13.393Z` → `2026-10-08T12:06:48.293Z`
- Content length: 10854 → 10974 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/fighting-nyt-user-privacy-invasion/
- lastmod: `2026-08-26T19:11:50.915Z` → `2026-10-05T19:23:15.040Z`
- Content length: 12197 → 12763 chars (delta: +566)
- Sample new content lines:
  + [Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)
  + ## Authors
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
- Sample removed content lines:
  - ## Author
  - ![GPT-Daybreak > Cover](https://images.ctfassets.net/kftzwdyauwt9/2iqsbTTLvgMNteNampw3gW/a38ed04432ee5548c4aec6c7b7a506f
  - [The Defender’s WindowSecurityAug 17, 2026](</index/the-defenders-window/>)
  -   * [Codex](</codex/>)
  - ![The Defender’s Window > Cover](https://images.ctfassets.net/kftzwdyauwt9/2We7bguC4FuOofZ8Lu6LUZ/02049fcee47c460695acab

### https://openai.com/index/figma-david-kossnick/
- lastmod: `2026-09-22T13:14:12.105Z` → `2026-10-03T13:15:23.986Z`
- Content length: 15248 → 15501 chars (delta: +253)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [Codex](<https://chatgpt.com/codex/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![EF JohnDeere 1.1](https://images.ctfassets.net/kftzwdyauwt9/ipWlhbJxkXsig8F8AQLY3/b8abf5f2566658a37e74f7bec882f004/EF_
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/first-proof-submissions/
- lastmod: `2026-09-25T19:18:23.653Z` → `2026-10-08T12:06:51.611Z`
- Content length: 9694 → 9871 chars (delta: +177)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [An OpenAI model proposes a solution to the Navier–Stokes problemResearchSep 8, 2026](</index/navier-stokes-solution/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/fishing-for-first-timers/
- lastmod: `2026-09-08T20:26:07.376Z` → `2026-10-07T16:05:15.537Z`
- Content length: 11049 → 11334 chars (delta: +285)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Zalando logo in white, centered over a textured blue surface resembling fabric or a synthetic material.](https://image
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![\[2.0\] Card > Media > Zalando](https://images.ctfassets.net/kftzwdyauwt9/6SOwtELA1S0TYqttuHDBux/39e0d269327c02d3a6cc8
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/five-new-stargate-sites/
- lastmod: `2026-09-22T22:06:09.633Z` → `2026-10-03T13:05:36.809Z`
- Content length: 9970 → 10112 chars (delta: +142)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  -   * [Codex](</codex/>)
  - [Building standards for the next phase of AIGlobal AffairsSep 21, 2026](</index/building-standards-next-phase-ai/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/fyxer/
- lastmod: `2026-09-25T11:21:03.683Z` → `2026-10-07T23:30:40.535Z`
- Content length: 12211 → 12330 chars (delta: +119)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/gartner-2026-agentic-coding-leader/
- lastmod: `2026-09-22T09:51:49.587Z` → `2026-10-09T05:56:06.462Z`
- Content length: 10033 → 10209 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gdpval/
- lastmod: `2026-09-24T07:34:50.942Z` → `2026-10-08T23:15:31.566Z`
- Content length: 22809 → 22929 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gilbert-tobin/
- lastmod: `2026-09-22T21:15:32.299Z` → `2026-10-09T09:04:48.970Z`
- Content length: 13470 → 13621 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/gpt-4-api-general-availability/
- lastmod: `2026-09-23T20:41:59.039Z` → `2026-10-08T17:01:03.716Z`
- Content length: 13437 → 13613 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-4-research/
- lastmod: `2026-06-08T07:35:15.422Z` → `2026-10-09T01:33:42.161Z`
- Content length: 26651 → 26974 chars (delta: +323)
- Sample new content lines:
  + ![White Wix logo on a background of blue and green paint swathes](https://images.ctfassets.net/kftzwdyauwt9/6E3QyNLzuWwK
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![White Digital Green logo on a green background.](https://images.ctfassets.net/kftzwdyauwt9/7b26cc3b-46d8-45b0-f67f6de0
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![WHOOP Coach HIIT](https://images.ctfassets.net/kftzwdyauwt9/163d4817-6436-4d20-83e0963f68f1/ef4bec09f31b32f8ca8a953a09
  - ![Wix cover image](https://images.ctfassets.net/kftzwdyauwt9/6E3QyNLzuWwK3EGBHPw7nQ/fbd0c5a34cc4f4ba096028adbdda8934/oai
  - ![Three farmers using a mobile app outside](https://images.ctfassets.net/kftzwdyauwt9/7b26cc3b-46d8-45b0-f67f6de0c8f8/8b
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-4/
- lastmod: `2026-09-25T19:18:25.136Z` → `2026-10-09T05:05:09.356Z`
- Content length: 7434 → 7610 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
- lastmod: `2026-09-22T19:00:22.776Z` → `2026-10-09T04:35:45.464Z`
- Content length: 11639 → 11815 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-4o-system-card/
- lastmod: `2026-08-30T07:53:47.531Z` → `2026-10-08T23:44:45.871Z`
- Content length: 85643 → 86318 chars (delta: +675)
- Sample new content lines:
  + [View PDF version(opens in a new window)](<https://cdn.openai.com/gpt-4o-system-card.pdf>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Image Source: Rupprecht, Peter & Lewis, Christopher & Helmchen, Fritjof. (2022). Centripetal integration of past events 
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - Image Source: Hochrainer, A., Lahirin, M., Erhard, M., and Zeilinger, A. Hardy's Proposal in three historic experiments 
  - Image Source: Rupprecht, Peter & Lewis, Christopher & Helmchen, Fritjof. (2022). Centripetal integration of past events 
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [View PDF version](<https://cdn.openai.com/gpt-4o-system-card.pdf>)

### https://openai.com/index/gpt-5-1-codex-max-system-card/
- lastmod: `2026-09-25T19:10:33.560Z` → `2026-10-09T06:07:31.837Z`
- Content length: 6223 → 6221 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/gpt-5-1-codex-max/
- lastmod: `2026-09-22T09:51:51.707Z` → `2026-10-09T05:56:07.911Z`
- Content length: 13496 → 13547 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/gpt-5-1-for-developers/
- lastmod: `2026-09-23T20:41:58.633Z` → `2026-10-09T06:33:43.217Z`
- Content length: 17481 → 17475 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/gpt-5-1/
- lastmod: `2026-09-18T17:55:50.528Z` → `2026-10-09T06:33:35.674Z`
- Content length: 24776 → 24853 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/gpt-5-2-codex-system-card/
- lastmod: `2026-06-08T11:09:39.541Z` → `2026-10-08T22:55:30.988Z`
- Content length: 5878 → 6125 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-3-codex-system-card/
- lastmod: `2026-09-22T09:51:51.696Z` → `2026-10-09T07:02:25.306Z`
- Content length: 5849 → 6025 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-3-instant/
- lastmod: `2026-07-25T07:09:10.403Z` → `2026-10-09T05:09:51.556Z`
- Content length: 30924 → 31021 chars (delta: +97)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/gpt-5-5-instant/
- lastmod: `2026-09-18T17:55:57.182Z` → `2026-10-09T04:57:15.580Z`
- Content length: 19472 → 19549 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/gpt-5-5-system-card/
- lastmod: `2026-05-22T19:40:42.310Z` → `2026-10-09T06:21:09.548Z`
- Content length: 5958 → 6246 chars (delta: +288)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Pacing model development in an era of cyber-critical capabilitiesCompanyAug 18, 2026](</index/pacing-model-development-
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-
  - ![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cah

### https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/
- lastmod: `2026-09-25T19:16:31.233Z` → `2026-10-09T06:21:14.222Z`
- Content length: 22429 → 22872 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/
- lastmod: `2026-09-27T19:25:08.137Z` → `2026-10-09T06:20:57.429Z`
- Content length: 16904 → 17036 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-6-in-kiro/
- lastmod: `2026-09-25T19:16:32.030Z` → `2026-10-09T06:33:31.853Z`
- Content length: 8421 → 8415 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/
- lastmod: `2026-09-25T19:16:32.835Z` → `2026-10-09T06:33:32.476Z`
- Content length: 7082 → 7076 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/gpt-5-6/
- lastmod: `2026-09-28T04:27:47.732Z` → `2026-10-09T08:57:18.318Z`
- Content length: 40850 → 40844 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/gpt-5-amgen/
- lastmod: `2026-09-14T21:28:00.101Z` → `2026-10-07T16:05:16.971Z`
- Content length: 3327 → 3539 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-coding-design/
- lastmod: `2026-09-08T20:26:07.372Z` → `2026-10-07T16:05:15.995Z`
- Content length: 3441 → 3653 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-creative-writing/
- lastmod: `2026-09-08T20:26:07.869Z` → `2026-10-07T16:05:17.182Z`
- Content length: 3446 → 3658 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-cursor/
- lastmod: `2026-09-08T20:26:09.603Z` → `2026-10-07T16:05:18.189Z`
- Content length: 3328 → 3540 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-first-look/
- lastmod: `2026-09-08T20:26:09.270Z` → `2026-10-08T09:14:38.810Z`
- Content length: 3336 → 3548 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/
- lastmod: `2026-09-25T19:18:10.781Z` → `2026-10-08T12:06:43.939Z`
- Content length: 16424 → 16544 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-medical-research/
- lastmod: `2026-09-08T20:26:09.105Z` → `2026-10-07T16:05:17.436Z`
- Content length: 3446 → 3658 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-new-era-of-work/
- lastmod: `2026-09-23T20:42:07.028Z` → `2026-10-08T21:57:02.238Z`
- Content length: 7446 → 7440 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/gpt-5-safe-completions/
- lastmod: `2026-09-25T19:10:13.734Z` → `2026-10-09T04:45:49.051Z`
- Content length: 13151 → 13085 chars (delta: -66)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/gpt-5-system-card-addendum-gpt-5-1/
- lastmod: `2026-09-25T19:10:33.997Z` → `2026-10-09T06:07:42.648Z`
- Content length: 6085 → 6261 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/
- lastmod: `2026-09-25T19:10:13.614Z` → `2026-10-03T13:21:05.235Z`
- Content length: 5718 → 5716 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/gpt-5-system-card-sensitive-conversations/
- lastmod: `2026-09-25T19:10:36.615Z` → `2026-10-03T13:21:03.896Z`
- Content length: 6209 → 6207 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/gpt-5-system-card-update-gpt-5-2/
- lastmod: `2026-05-22T19:08:32.740Z` → `2026-10-09T06:07:29.214Z`
- Content length: 4797 → 5044 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-5-system-card/
- lastmod: `2026-09-25T19:10:33.029Z` → `2026-10-03T13:21:04.873Z`
- Content length: 7620 → 7618 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/gpt-6-astra-next-generation-work/
- lastmod: `2026-09-25T19:16:16.998Z` → `2026-10-09T09:06:08.735Z`
- Content length: 14422 → 14598 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-6-astra/
- lastmod: `2026-09-25T19:18:10.771Z` → `2026-10-09T08:44:51.121Z`
- Content length: 38368 → 38690 chars (delta: +322)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + _**Update on September 22, 2026:**__We are expanding our GPT‑6 family with GPT‑6 Sol and GPT‑6 Luna._[_Learn more._](</i
  + * * *
  +  _**Update on September 29, 2026:**__Learn about OpenAI 's latest model: _[_GPT‑6 .1 Sol_ ⁠](</index/introducing-gpt-6-1
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -  _**Update on September 22, 2026:**__We are expanding our GPT‑6 family with GPT‑6 Sol and GPT‑6 Luna._[_Learn more._](</
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/gpt-oss-model-card/
- lastmod: `2026-09-25T19:10:35.231Z` → `2026-10-03T13:21:04.071Z`
- Content length: 7688 → 7686 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/gpt-oss-safeguard-technical-report/
- lastmod: `2026-06-12T02:44:14.982Z` → `2026-10-09T04:56:15.842Z`
- Content length: 6472 → 6719 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/grab-openai-ai-skills-southeast-asia/
- lastmod: `2026-09-27T17:14:43.788Z` → `2026-10-09T06:41:11.689Z`
- Content length: 10455 → 10620 chars (delta: +165)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Building standards for the next phase of AIGlobal AffairsSep 21, 2026](</index/building-standards-next-phase-ai/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![Building shared standards for the next phase of AI - art card](https://images.ctfassets.net/kftzwdyauwt9/aQqo6ytHD8RKL

### https://openai.com/index/gradient-labs/
- lastmod: `2026-09-22T13:14:08.764Z` → `2026-10-08T14:46:04.262Z`
- Content length: 12082 → 12286 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/growing-atv-big-air-tour/
- lastmod: `2026-09-23T20:40:44.761Z` → `2026-10-07T16:05:14.721Z`
- Content length: 12819 → 12995 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/hardening-atlas-against-prompt-injection/
- lastmod: `2026-08-26T19:11:50.526Z` → `2026-10-09T00:24:23.493Z`
- Content length: 22252 → 22799 chars (delta: +547)
- Sample new content lines:
  + [Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![GPT-Daybreak > Cover](https://images.ctfassets.net/kftzwdyauwt9/2iqsbTTLvgMNteNampw3gW/a38ed04432ee5548c4aec6c7b7a506f
  - [The Defender’s WindowSecurityAug 17, 2026](</index/the-defenders-window/>)
  -   * [Codex](</codex/>)
  - ![The Defender’s Window > Cover](https://images.ctfassets.net/kftzwdyauwt9/2We7bguC4FuOofZ8Lu6LUZ/02049fcee47c460695acab
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

### https://openai.com/index/harness-engineering/
- lastmod: `2026-09-22T09:51:48.962Z` → `2026-10-09T05:56:05.429Z`
- Content length: 28344 → 28520 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/harvey-from-context-to-confidence-with-astra/
- lastmod: `2026-09-23T19:00:20.229Z` → `2026-10-07T23:30:19.678Z`
- Content length: 6564 → 6712 chars (delta: +148)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/health-in-chatgpt/
- lastmod: `2026-09-22T17:02:21.102Z` → `2026-10-09T06:33:34.895Z`
- Content length: 19054 → 19105 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/healthbench/
- lastmod: `2026-09-25T19:10:14.752Z` → `2026-10-03T13:21:03.424Z`
- Content length: 37564 → 37740 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/hello-gpt-4o/
- lastmod: `2026-09-25T19:18:10.622Z` → `2026-10-09T05:15:15.723Z`
- Content length: 16061 → 16237 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/helping-older-adults-use-ai-in-everyday-life/
- lastmod: `2026-09-25T19:16:15.172Z` → `2026-10-09T06:59:13.386Z`
- Content length: 7827 → 7945 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/helping-people-when-they-need-it-most/
- lastmod: `2026-09-25T18:56:57.047Z` → `2026-10-08T17:01:05.350Z`
- Content length: 14302 → 14155 chars (delta: -147)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/

### https://openai.com/index/hex-gpt-6-astra/
- lastmod: `2026-09-26T12:23:34.653Z` → `2026-10-07T23:30:40.753Z`
- Content length: 7766 → 7885 chars (delta: +119)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/hibob/
- lastmod: `2026-09-22T21:15:44.331Z` → `2026-10-08T22:45:57.206Z`
- Content length: 10429 → 10537 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/higgsfield-from-prompt-to-production-with-astra/
- lastmod: `2026-09-26T12:05:33.141Z` → `2026-10-07T23:30:24.112Z`
- Content length: 6741 → 6922 chars (delta: +181)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  - ![V7 customer story art card - smaller logo](https://images.ctfassets.net/kftzwdyauwt9/3Av2nLs9MOiSrB5wMXLvL2/35fbde20ac
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/higgsfield/
- lastmod: `2026-09-10T21:23:25.277Z` → `2026-10-09T01:12:09.519Z`
- Content length: 12587 → 12832 chars (delta: +245)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Introducing the Agents APIProductSep 10, 2026](</index/introducing-the-agents-api/>)
  - ![Playco Astra customer story art card - Option B](https://images.ctfassets.net/kftzwdyauwt9/2GBXEJdShwgtUKQZc9Ojsm/ae87
  -   * [Codex](</codex/>)
  - [Legora reviewed 41 documents in minutes with GPT-6 AstraStartupSep 3, 2026](</index/legora-financial-statement-review-w
  - ![Legora customer story art card - Option C](https://images.ctfassets.net/kftzwdyauwt9/13uynVdSWJS9UT4Y7EppMn/7259e4915a

### https://openai.com/index/how-agents-are-transforming-work/
- lastmod: `2026-09-25T19:33:52.093Z` → `2026-10-09T05:56:00.293Z`
- Content length: 13474 → 13654 chars (delta: +180)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/
- lastmod: `2026-09-25T19:33:51.019Z` → `2026-10-09T08:43:40.880Z`
- Content length: 12717 → 12849 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-chatgpt-adoption-has-expanded/
- lastmod: `2026-09-25T19:33:52.247Z` → `2026-10-09T06:21:27.043Z`
- Content length: 11311 → 11429 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/how-confessions-can-keep-language-models-honest/
- lastmod: `2026-09-25T19:18:13.927Z` → `2026-10-08T23:02:56.369Z`
- Content length: 20389 → 20509 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-countries-can-end-the-capability-overhang/
- lastmod: `2026-09-25T19:34:20.228Z` → `2026-10-07T19:26:19.267Z`
- Content length: 10166 → 10284 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/how-enterprises-put-ai-to-work/
- lastmod: `2026-09-25T19:33:51.138Z` → `2026-10-09T09:06:00.290Z`
- Content length: 13622 → 13798 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-people-are-using-chatgpt/
- lastmod: `2026-09-25T19:33:52.034Z` → `2026-10-09T06:07:45.325Z`
- Content length: 9956 → 9949 chars (delta: -7)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)

### https://openai.com/index/how-the-voices-for-chatgpt-were-chosen/
- lastmod: `2026-09-18T17:01:22.086Z` → `2026-10-08T17:01:07.129Z`
- Content length: 9784 → 9996 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-the-world-is-putting-chatgpt-to-work/
- lastmod: `2026-09-25T19:33:52.037Z` → `2026-10-09T06:11:01.909Z`
- Content length: 13468 → 13600 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-to-connect-ai-usage-to-business-value/
- lastmod: `2026-09-25T19:16:12.865Z` → `2026-10-09T08:59:43.704Z`
- Content length: 17299 → 17293 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
- lastmod: `2026-09-25T19:18:41.636Z` → `2026-10-08T12:06:44.783Z`
- Content length: 13614 → 13734 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
- lastmod: `2026-09-25T19:10:11.637Z` → `2026-10-07T19:53:40.015Z`
- Content length: 33001 → 32999 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/hp-frontier-partnership/
- lastmod: `2026-09-22T22:06:01.360Z` → `2026-10-09T06:21:18.640Z`
- Content length: 10663 → 10718 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/hsp-gruppe/
- lastmod: `2026-09-22T21:15:39.395Z` → `2026-10-08T22:45:49.470Z`
- Content length: 15334 → 15485 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- lastmod: `2026-09-25T19:16:25.801Z` → `2026-10-07T21:05:08.618Z`
- Content length: 48030 → 48206 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/hugging-face-model-evaluation-security-incident/
- lastmod: `2026-09-25T19:16:29.416Z` → `2026-10-08T20:53:12.117Z`
- Content length: 15547 → 15990 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/hygh/
- lastmod: `2026-09-22T21:15:52.523Z` → `2026-10-08T22:46:03.881Z`
- Content length: 12354 → 12505 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/image-generation-api/
- lastmod: `2026-09-23T20:42:07.407Z` → `2026-10-09T05:35:19.410Z`
- Content length: 9396 → 9572 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/improvements-to-data-analysis-in-chatgpt/
- lastmod: `2026-09-18T17:01:21.945Z` → `2026-10-08T17:01:06.652Z`
- Content length: 7302 → 7514 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/
- lastmod: `2026-09-22T17:02:20.675Z` → `2026-10-09T06:33:34.232Z`
- Content length: 13909 → 13960 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/improving-health-intelligence-in-chatgpt/
- lastmod: `2026-09-18T17:55:50.913Z` → `2026-10-09T07:07:52.482Z`
- Content length: 15433 → 15510 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/indeed-maggie-hulce/
- lastmod: `2026-09-22T19:25:25.318Z` → `2026-10-08T22:49:07.401Z`
- Content length: 19348 → 19456 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/inside-our-in-house-data-agent/
- lastmod: `2026-08-13T23:57:08.794Z` → `2026-10-05T19:05:03.567Z`
- Content length: 28724 → 28974 chars (delta: +250)
- Sample new content lines:
  + ## Authors
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Scaling Storage for 1 Billion ChatGPT Users \(Part I\) card image](https://images.ctfassets.net/kftzwdyauwt9/2X23NOb0P
- Sample removed content lines:
  - ## Author
  -   * [Codex](</codex/>)
  - ![GPT-5.6 efficiency article — art card](https://images.ctfassets.net/kftzwdyauwt9/5ExPWhZDZXbZgTHE7aeE5d/0526071f749a3b
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [How GPT-5.6 fuses frontier intelligence with frontier efficiencyEngineeringJul 29, 2026](</index/gpt-5-6-frontier-intel

### https://openai.com/index/instruction-following/
- lastmod: `2026-09-25T19:10:39.455Z` → `2026-10-03T13:21:25.875Z`
- Content length: 21347 → 21523 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/instruction-hierarchy-challenge/
- lastmod: `2026-08-30T08:28:42.819Z` → `2026-10-09T04:59:21.570Z`
- Content length: 15187 → 15467 chars (delta: +280)
- Sample new content lines:
  + ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Pacing model development in an era of cyber-critical capabilitiesCompanyAug 18, 2026](</index/pacing-model-development-
  - ![math-breakthroughs art-card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2zkd5RIOug4FcEj62mdSF4/3ea9e19c0456289c69f0
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Ten advances in mathematics and theoretical computer sciencePublicationAug 1, 2026](</index/ten-advances-in-mathematics

### https://openai.com/index/intercom/
- lastmod: `2026-06-14T06:53:12.519Z` → `2026-10-01T14:54:25.938Z`
- Content length: 13357 → 13266 chars (delta: -91)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/introducing-4o-image-generation/
- lastmod: `2026-09-21T22:24:31.355Z` → `2026-10-09T06:33:33.014Z`
- Content length: 58583 → 58759 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-aardvark/
- lastmod: `2026-09-25T19:18:09.104Z` → `2026-10-09T06:33:50.188Z`
- Content length: 11771 → 11718 chars (delta: -53)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-admin-plugin/
- lastmod: `2026-09-25T19:16:22.317Z` → `2026-10-09T06:21:20.738Z`
- Content length: 10272 → 10448 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-agentkit/
- lastmod: `2026-06-05T12:39:10.159Z` → `2026-10-08T23:10:29.490Z`
- Content length: 15164 → 15105 chars (delta: -59)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/introducing-apps-in-chatgpt/
- lastmod: `2026-08-14T21:41:09.139Z` → `2026-10-08T22:56:34.551Z`
- Content length: 12661 → 12593 chars (delta: -68)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/introducing-b2b-signals/
- lastmod: `2026-09-25T19:33:52.725Z` → `2026-10-09T06:21:15.795Z`
- Content length: 12923 → 13056 chars (delta: +133)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/introducing-canvas/
- lastmod: `2026-09-18T17:01:20.877Z` → `2026-10-08T17:01:06.288Z`
- Content length: 12059 → 12271 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-chatgpt-agent/
- lastmod: `2026-09-18T17:55:57.600Z` → `2026-10-09T05:00:19.404Z`
- Content length: 27580 → 27749 chars (delta: +169)
- Sample new content lines:
  + ### [Public transit benchmarkingBenchmarks seven global transit systems vs. Chicago, compiling data and a summary report
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - ### [Planning a dinner partyPlans, shops for, and organizes a six-course dinner based on Romance of the Three Kingdoms.V
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ### [Public transit benchmarkingBenchmarks seven global transit systems vs. Chicago, compiling data and a summary report
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/introducing-chatgpt-atlas/
- lastmod: `2026-09-22T17:02:42.096Z` → `2026-10-09T06:33:34.218Z`
- Content length: 16245 → 16296 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/introducing-chatgpt-edu/
- lastmod: `2026-09-18T17:01:23.367Z` → `2026-10-08T17:01:09.113Z`
- Content length: 7973 → 8185 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-chatgpt-financial-services/
- lastmod: `2026-09-25T19:16:17.520Z` → `2026-10-09T06:33:39.931Z`
- Content length: 20283 → 20277 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-chatgpt-health/
- lastmod: `2026-09-25T19:16:21.270Z` → `2026-10-09T08:35:31.724Z`
- Content length: 17829 → 17718 chars (delta: -111)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/introducing-chatgpt-images-2-0/
- lastmod: `2026-09-25T19:16:25.300Z` → `2026-10-09T06:33:48.060Z`
- Content length: 23999 → 24175 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-chatgpt-images-2-5/
- lastmod: `2026-09-25T19:16:19.735Z` → `2026-10-09T07:37:45.588Z`
- Content length: 21847 → 21841 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-chatgpt-pulse/
- lastmod: `2026-09-18T17:55:49.287Z` → `2026-10-09T06:33:35.129Z`
- Content length: 11132 → 11344 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-chatgpt-search/
- lastmod: `2026-08-14T20:26:26.838Z` → `2026-10-08T01:09:18.152Z`
- Content length: 12892 → 13484 chars (delta: +592)
- Sample new content lines:
  + ![The image shows a minimalist search interface labeled "SearchGPT" with a circular icon next to the text. Below is a se
  + ![A small circular button with a pencil and sparkle symbol in the center, set against a blurred gradient background of w
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Canvas > cover image](https://images.ctfassets.net/kftzwdyauwt9/2ZJmwm7FLSmjnnyqQIuFNY/a34114c80379cf2b84cf6e28332c21c
  -   * [Codex](</codex/>)
  - ![Search GPT > Cover Asset](https://images.ctfassets.net/kftzwdyauwt9/3PW6ybA3KHgTzQRTLewRE0/6b7dbca9baa496dce6cf2d929b0
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-chatgpt-small-business-program/
- lastmod: `2026-09-27T19:36:14.416Z` → `2026-10-09T06:21:19.121Z`
- Content length: 12433 → 12608 chars (delta: +175)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + Get updates on OpenAI events, practical guidance from mentors and peers, and resources to help your business save time a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Get updates on events, practical AI guidance from mentors and peers, and resources to help your business save time and w
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-chatgpt-team/
- lastmod: `2026-09-18T17:55:53.157Z` → `2026-10-08T17:01:06.313Z`
- Content length: 9621 → 10060 chars (delta: +439)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-codex/
- lastmod: `2026-09-22T09:51:55.324Z` → `2026-10-09T04:40:32.676Z`
- Content length: 25253 → 25429 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-company-knowledge/
- lastmod: `2026-09-18T17:55:49.935Z` → `2026-10-08T17:01:02.902Z`
- Content length: 14218 → 14295 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/introducing-data-residency-in-asia/
- lastmod: `2026-09-18T17:55:56.698Z` → `2026-10-09T06:33:44.077Z`
- Content length: 7614 → 7767 chars (delta: +153)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * **Data Processing Addendum (DPA)** : We offer a comprehensive [_DPA_ ⁠](<https://openai.com/policies/data-processing
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  -   * [Codex](</codex/>)
  -   * **Data Processing Addendum (DPA)** : We offer a comprehensive [_DPA_ ⁠(opens in a new window)](<https://openai-dotco

### https://openai.com/index/introducing-data-residency-in-europe/
- lastmod: `2026-09-18T17:55:57.163Z` → `2026-10-09T06:07:45.854Z`
- Content length: 8629 → 8841 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-deep-research/
- lastmod: `2026-07-25T07:21:05.784Z` → `2026-10-09T06:59:21.319Z`
- Content length: 48284 → 48560 chars (delta: +276)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-evmbench/
- lastmod: `2026-09-25T19:18:13.670Z` → `2026-10-08T12:06:49.885Z`
- Content length: 11589 → 11709 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-genebench-pro/
- lastmod: `2026-09-25T19:18:10.069Z` → `2026-10-08T19:28:04.720Z`
- Content length: 24640 → 24760 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-gpt-4-5/
- lastmod: `2026-08-14T20:48:23.507Z` → `2026-10-09T04:51:38.952Z`
- Content length: 21120 → 21373 chars (delta: +253)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-gpt-5-2-codex/
- lastmod: `2026-09-22T09:51:52.557Z` → `2026-10-09T06:08:07.560Z`
- Content length: 15581 → 15515 chars (delta: -66)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/introducing-gpt-5-2/
- lastmod: `2026-09-10T15:55:42.912Z` → `2026-10-09T08:18:44.774Z`
- Content length: 32344 → 32396 chars (delta: +52)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Build more natural voice experiences with GPT‑Live‑1 in the APIProductSep 10, 2026](</index/introducing-gpt-live-1-in-t
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - [Introducing ChatGPT for Financial ServicesProductSep 10, 2026](</index/introducing-chatgpt-financial-services/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/introducing-gpt-5-3-codex-spark/
- lastmod: `2026-09-15T17:50:29.082Z` → `2026-09-29T17:16:52.043Z`
- Content length: 11479 → 11691 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-gpt-5-3-codex/
- lastmod: `2026-09-28T02:51:20.661Z` → `2026-10-09T06:53:13.159Z`
- Content length: 21214 → 21390 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-gpt-5-4-mini-and-nano/
- lastmod: `2026-09-25T19:16:25.722Z` → `2026-10-09T08:12:56.699Z`
- Content length: 12026 → 11915 chars (delta: -111)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/introducing-gpt-5-4/
- lastmod: `2026-09-18T17:55:55.393Z` → `2026-10-09T04:56:51.010Z`
- Content length: 32600 → 32677 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/introducing-gpt-5-5/
- lastmod: `2026-09-25T19:16:32.188Z` → `2026-10-09T06:33:32.362Z`
- Content length: 35824 → 35818 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-gpt-5-for-developers/
- lastmod: `2026-08-08T06:25:36.369Z` → `2026-10-09T06:33:28.014Z`
- Content length: 31466 → 31411 chars (delta: -55)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/introducing-gpt-5/
- lastmod: `2026-09-22T17:02:17.058Z` → `2026-10-09T06:33:58.327Z`
- Content length: 35665 → 35716 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/introducing-gpt-6-sol-and-luna/
- lastmod: `2026-09-28T09:11:53.457Z` → `2026-10-09T06:33:30.502Z`
- Content length: 17883 → 17948 chars (delta: +65)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +  _**Update on September 29, 2026:**__Learn about OpenAI 's latest model: _[_GPT‑6 .1 Sol⁠_ ⁠](</index/introducing-gpt-6-
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/introducing-gpt-live-1-in-the-api/
- lastmod: `2026-09-25T19:16:18.828Z` → `2026-10-09T06:33:48.603Z`
- Content length: 15282 → 15276 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-gpt-live/
- lastmod: `2026-09-25T19:16:21.760Z` → `2026-10-09T06:33:24.513Z`
- Content length: 17844 → 17838 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-gpt-oss-safeguard/
- lastmod: `2026-09-18T17:55:43.510Z` → `2026-10-09T08:00:55.391Z`
- Content length: 17102 → 17314 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-gpt-oss/
- lastmod: `2026-07-25T07:10:19.582Z` → `2026-10-09T04:45:48.739Z`
- Content length: 26560 → 26492 chars (delta: -68)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)
  - ![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4j

### https://openai.com/index/introducing-gpt-realtime/
- lastmod: `2026-08-07T18:49:37.339Z` → `2026-10-09T04:50:03.344Z`
- Content length: 18486 → 18419 chars (delta: -67)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ##  Introducing gpt-realtime
  - ![Learning never stops card image](https://images.ctfassets.net/kftzwdyauwt9/rGBw0SMWP2aaIH5twRBgX/5f8f24d0e5a03eecfc74a
  -   * [Codex](</codex/>)
  - ![GPT-5.6 in Kiro > OpenAI and official Kiro full logo > 1:1 art card](https://images.ctfassets.net/kftzwdyauwt9/31NSq4u
  - [Learning never stops: How AI makes learning continuousProductAug 26, 2026](</index/learning-never-stops/>)

### https://openai.com/index/introducing-gpt-rosalind/
- lastmod: `2026-09-25T19:18:14.533Z` → `2026-10-09T04:50:42.228Z`
- Content length: 17332 → 17167 chars (delta: -165)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Introducing GPT-6.1 SolProductSep 29, 2026](</index/introducing-gpt-6-1-sol/>)
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  - [Build more natural voice experiences with GPT‑Live‑1 in the APIProductSep 10, 2026](</index/introducing-gpt-live-1-in-t
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/introducing-gpts/
- lastmod: `2026-09-23T20:42:16.251Z` → `2026-10-08T17:01:05.789Z`
- Content length: 13731 → 13907 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/
- lastmod: `2026-09-23T20:42:20.415Z` → `2026-10-08T17:01:04.842Z`
- Content length: 13885 → 14061 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-indqa/
- lastmod: `2026-09-25T17:20:54.206Z` → `2026-10-09T06:07:43.491Z`
- Content length: 13849 → 13684 chars (delta: -165)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Introducing GPT-6.1 SolProductSep 29, 2026](</index/introducing-gpt-6-1-sol/>)
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  - [Build more natural voice experiences with GPT‑Live‑1 in the APIProductSep 10, 2026](</index/introducing-gpt-live-1-in-t
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/introducing-intelligence-age/
- lastmod: `2026-09-17T11:33:58.952Z` → `2026-10-01T16:06:43.501Z`
- Content length: 13789 → 14360 chars (delta: +571)
- Sample new content lines:
  + [View all](</news/>)
  + [The eternal complementIntelligence AgeOct 1, 2026](</index/the-eternal-complement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-life-sci-bench/
- lastmod: `2026-09-25T19:18:26.890Z` → `2026-10-08T12:06:44.914Z`
- Content length: 27075 → 27195 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-mentalhealthbench/
- lastmod: `2026-09-25T19:16:12.929Z` → `2026-10-09T00:33:18.886Z`
- Content length: 20941 → 21262 chars (delta: +321)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  - ![Research acceleration: The view inside OpenAI > Cover image](https://images.ctfassets.net/kftzwdyauwt9/5kS3OG1Jfdja5xL
  -   * [Codex](</codex/>)
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Research acceleration: The view inside OpenAIResearchSep 6, 2026](</index/research-acceleration-view-inside-openai/>)

### https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/
- lastmod: `2026-09-25T19:18:12.420Z` → `2026-10-09T06:33:37.728Z`
- Content length: 26322 → 26269 chars (delta: -53)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-o3-and-o4-mini/
- lastmod: `2026-07-25T07:09:31.335Z` → `2026-10-09T04:29:48.647Z`
- Content length: 44866 → 45686 chars (delta: +820)
- Sample new content lines:
  + The availability information reflects the April 2025 launch. o3 and o4-mini are no longer available in ChatGPT and are d
  + [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + Our smartest and most capable models to date with full tool access
  +   * [Plugins](</business/plugins/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-openai-for-nonprofits/
- lastmod: `2026-09-23T20:42:00.861Z` → `2026-10-08T17:01:06.981Z`
- Content length: 9846 → 10022 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-openai-o1-preview/
- lastmod: `2026-09-23T20:42:08.798Z` → `2026-10-07T19:27:15.691Z`
- Content length: 10111 → 10792 chars (delta: +681)
- Sample new content lines:
  + [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + A new series of reasoning models for solving hard problems.
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [Try it in the API(opens in a new window)](<https://platform.openai.com/playground/chat?models=o1-mini>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  -   * [Try it in ChatGPT Plus (opens in a new window)](<https://chatgpt.com/?model=o1>)

### https://openai.com/index/introducing-openai-partner-network/
- lastmod: `2026-09-18T17:55:50.077Z` → `2026-10-09T06:33:35.179Z`
- Content length: 14945 → 15022 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/introducing-openai-presence/
- lastmod: `2026-09-22T22:06:02.677Z` → `2026-10-09T06:33:33.903Z`
- Content length: 13001 → 12935 chars (delta: -66)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/introducing-openai-privacy-filter/
- lastmod: `2026-08-26T19:11:50.913Z` → `2026-10-09T05:07:31.011Z`
- Content length: 15074 → 15423 chars (delta: +349)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  - ![GPT-Daybreak > Cover](https://images.ctfassets.net/kftzwdyauwt9/2iqsbTTLvgMNteNampw3gW/a38ed04432ee5548c4aec6c7b7a506f
  - [The Defender’s WindowSecurityAug 17, 2026](</index/the-defenders-window/>)
  -   * [Codex](</codex/>)
  - ![The Defender’s Window > Cover](https://images.ctfassets.net/kftzwdyauwt9/2We7bguC4FuOofZ8Lu6LUZ/02049fcee47c460695acab
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

### https://openai.com/index/introducing-openai-safety-fellowship/
- lastmod: `2026-09-25T18:57:15.360Z` → `2026-10-01T15:52:30.972Z`
- Content length: 6999 → 6980 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/introducing-our-next-generation-audio-models/
- lastmod: `2026-08-21T00:28:00.727Z` → `2026-10-09T04:31:12.657Z`
- Content length: 13300 → 13547 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-parental-controls/
- lastmod: `2026-09-25T18:57:22.639Z` → `2026-10-08T17:01:05.953Z`
- Content length: 14445 → 14621 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-stargate-norway/
- lastmod: `2026-08-31T19:59:26.068Z` → `2026-10-03T13:05:36.217Z`
- Content length: 8630 → 8837 chars (delta: +207)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  - [OpenAI supports California’s bill to advance youth AI safetyCompanyAug 31, 2026](</index/supporting-california-bill-adv
  -   * [Codex](</codex/>)
  - ![Our decision on Cursor following its acquisition by SpaceX — cover](https://images.ctfassets.net/kftzwdyauwt9/3gFEgHvt
  - ![California youth AI safety — cover](https://images.ctfassets.net/kftzwdyauwt9/3CsHxgcoiHHUUaYOB1FNiq/38e90de831dad7959

### https://openai.com/index/introducing-structured-outputs-in-the-api/
- lastmod: `2026-09-23T20:42:26.842Z` → `2026-10-08T17:01:05.068Z`
- Content length: 43364 → 43540 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-the-adoption-news-channel/
- lastmod: `2026-07-25T07:05:20.351Z` → `2026-10-09T03:52:15.549Z`
- Content length: 7693 → 8042 chars (delta: +349)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How AI-native companies turn workflows into operating capabilityAI AdoptionSep 1, 2026](</index/ai-native-company-workf
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![How to manage AI investments in the agentic era > Cover image](https://images.ctfassets.net/kftzwdyauwt9/1qXMreHMXalbF
  - [How to manage AI investments in the agentic eraAI AdoptionJul 14, 2026](</index/managing-ai-investments-in-agentic-era/
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-the-agents-api/
- lastmod: `2026-09-25T19:16:13.585Z` → `2026-10-09T06:33:30.238Z`
- Content length: 17992 → 17986 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/introducing-the-openai-economic-research-exchange/
- lastmod: `2026-09-25T19:33:51.253Z` → `2026-10-07T19:26:00.903Z`
- Content length: 7506 → 7638 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/
- lastmod: `2026-09-22T19:25:22.944Z` → `2026-10-08T22:49:04.172Z`
- Content length: 8105 → 8160 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/introducing-upgrades-to-codex/
- lastmod: `2026-09-22T09:51:53.113Z` → `2026-10-09T05:56:08.700Z`
- Content length: 18802 → 18853 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/invideo-ai/
- lastmod: `2026-06-12T12:48:13.385Z` → `2026-10-01T14:54:26.414Z`
- Content length: 9751 → 10174 chars (delta: +423)
- Sample new content lines:
  + ![Genspark logo in white against a backdrop of glittering, dark sand and rocks](https://images.ctfassets.net/kftzwdyauwt
  + ![Unify logo in white against a backdrop of dandelion seed heads](https://images.ctfassets.net/kftzwdyauwt9/4Zk21VkqRdhQ
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Unify cover image](https://images.ctfassets.net/kftzwdyauwt9/4Zk21VkqRdhQg95kIcrmKc/9a51d3c304e36df765c60d834f6c8552/o
  - ![Retell AI > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/3FFvZQe1XAebMCD2dir1T4/637ac9168f5cb5aa61b49cbaf695
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![Genspark cover image](https://images.ctfassets.net/kftzwdyauwt9/34tn7du9Vq4ZJdFkFXMCam/fdcf963dec13094b0db74e7166ca116

### https://openai.com/index/invideo-builds-with-gpt-6-astra/
- lastmod: `2026-09-23T21:09:04.344Z` → `2026-10-09T01:12:08.310Z`
- Content length: 7629 → 7732 chars (delta: +103)
- Sample new content lines:
  + ![Playco Astra customer story art card - Option B](https://images.ctfassets.net/kftzwdyauwt9/2GBXEJdShwgtUKQZc9Ojsm/ae87
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
  + [Playco cut manual fixes 50% prototyping games with GPT-6 AstraStartupSep 3, 2026](</index/playco-game-prototyping-with-
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/jalapeno-first-results/
- lastmod: `2026-09-23T01:51:36.903Z` → `2026-10-08T02:51:33.720Z`
- Content length: 17203 → 17258 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/jetbrains-2025/
- lastmod: `2026-09-22T21:15:47.758Z` → `2026-10-08T22:45:46.486Z`
- Content length: 7808 → 7916 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/joint-statement-from-openai-and-microsoft/
- lastmod: `2026-06-09T14:05:57.315Z` → `2026-10-03T13:05:50.137Z`
- Content length: 5349 → 5419 chars (delta: +70)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/leadership-expansion-with-fidji-simo/
- lastmod: `2026-06-11T01:03:09.977Z` → `2026-10-03T13:05:25.903Z`
- Content length: 6402 → 6649 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/learn-teach-chatgpt-work-codex/
- lastmod: `2026-09-18T17:55:47.509Z` → `2026-10-09T06:33:33.645Z`
- Content length: 18145 → 18222 chars (delta: +77)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a6

### https://openai.com/index/learning-a-hierarchy/
- lastmod: `2026-09-25T19:10:36.622Z` → `2026-10-03T13:21:05.397Z`
- Content length: 8977 → 9153 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/learning-never-stops/
- lastmod: `2026-09-25T19:16:28.160Z` → `2026-10-09T06:33:30.915Z`
- Content length: 6658 → 6652 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/learning-to-reason-with-llms/
- lastmod: `2026-09-22T19:00:23.480Z` → `2026-10-09T04:54:14.562Z`
- Content length: 42086 → 40817 chars (delta: -1269)
- Sample new content lines:
  + Average:5
  + First word: Think (5 letters)
  + 8 a
  + Average=19
  + Sum=16, Average=8
- Sample removed content lines:
  - Now we can divide into pairs:  
  - Sum=28, Average=14  
  - Suppose that each plaintext letter corresponds to pair of letters in the ciphertext.  
  - 6 v  
  - 10 z  

### https://openai.com/index/legora-financial-statement-review-with-astra/
- lastmod: `2026-09-22T13:14:03.912Z` → `2026-10-07T23:30:44.879Z`
- Content length: 7827 → 7984 chars (delta: +157)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/lenfest-institute/
- lastmod: `2026-05-29T00:25:29.685Z` → `2026-09-28T17:50:55.219Z`
- Content length: 10119 → 10668 chars (delta: +549)
- Sample new content lines:
  + _Editor’s Note: This news was originally shared by Lenfest Institute and can be read_[ _here_ ⁠(opens in a new window)](
  + ** _Update, September 28, 2026_** _: OpenAI and the Lenfest Institute have announced the_[ _program’s next phase_ ⁠](<ht
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [GPT-5.3 Instant](</index/gpt-5-3-instant/>)
  -  _Editor’s Note: This news was originally shared by Lenfest Institute and can be read_[ _here_ ⁠(opens in a new window)]
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/loveholidays/
- lastmod: `2026-09-22T21:15:36.194Z` → `2026-10-09T05:55:57.359Z`
- Content length: 12962 → 13070 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/lowes-chandhu-nair/
- lastmod: `2026-09-22T21:15:39.782Z` → `2026-10-09T06:07:45.989Z`
- Content length: 12948 → 13056 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/lseg/
- lastmod: `2026-09-22T19:25:14.786Z` → `2026-10-08T22:48:55.955Z`
- Content length: 11547 → 11698 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/managing-ai-investments-in-agentic-era/
- lastmod: `2026-09-28T00:19:42.385Z` → `2026-10-09T06:21:13.401Z`
- Content length: 13267 → 13416 chars (delta: +149)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  + [A practical guide to building with GPT-6ProductOct 2, 2026](</index/practical-guide-building-gpt-6/>)
  + [AI Adoption](</news/ai-adoption/>)Guides
- Sample removed content lines:
  - [Introducing the ChatGPT for small business programAI AdoptionJul 21, 2026](</index/introducing-chatgpt-small-business-p
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [AI Adoption](</news/ai-adoption/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/mapping-ai-jobs-transition-eu/
- lastmod: `2026-09-25T19:33:52.125Z` → `2026-10-07T19:26:19.941Z`
- Content length: 9415 → 9533 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/mavenagi/
- lastmod: `2026-09-22T13:14:37.826Z` → `2026-10-03T13:15:22.918Z`
- Content length: 9989 → 10165 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/memory-and-new-controls-for-chatgpt/
- lastmod: `2026-09-18T17:01:23.306Z` → `2026-10-08T17:01:08.417Z`
- Content length: 13905 → 14344 chars (delta: +439)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/mixi/
- lastmod: `2026-06-14T04:21:13.826Z` → `2026-10-01T14:54:26.541Z`
- Content length: 12599 → 12949 chars (delta: +350)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Close-up of copper wire strands with glowing reflections, overlaid with the white Intercom logo centered in the frame.
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Intercom cover image](https://images.ctfassets.net/kftzwdyauwt9/32rIG6b83UB8GU0atjwCLp/2859930e037889e03ffc8ca685d00d5
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/mixpanel-incident/
- lastmod: `2026-08-26T19:11:47.982Z` → `2026-10-05T19:23:15.812Z`
- Content length: 12145 → 12364 chars (delta: +219)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/model-disproves-discrete-geometry-conjecture/
- lastmod: `2026-09-25T19:18:13.424Z` → `2026-10-08T12:06:51.366Z`
- Content length: 18168 → 18345 chars (delta: +177)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [An OpenAI model proposes a solution to the Navier–Stokes problemResearchSep 8, 2026](</index/navier-stokes-solution/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/model-misalignment-reporting-framework/
- lastmod: `2026-09-28T05:13:27.334Z` → `2026-10-09T06:28:25.497Z`
- Content length: 18051 → 18066 chars (delta: +15)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/model-ml-chaz-englander/
- lastmod: `2026-09-10T21:23:16.046Z` → `2026-10-08T14:46:06.562Z`
- Content length: 13900 → 14112 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/model-ml/
- lastmod: `2026-09-22T13:14:05.250Z` → `2026-10-08T14:46:03.132Z`
- Content length: 14733 → 14937 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/modeling-ai-jobs-transition/
- lastmod: `2026-07-14T17:37:52.956Z` → `2026-10-09T08:14:03.276Z`
- Content length: 12374 → 12872 chars (delta: +498)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Our approach to government and national security partnerships > Cover image](https://images.ctfassets.net/kftzwdyauwt9
  -   * [Codex](</codex/>)
  - [How ChatGPT adoption has expandedGlobal AffairsJun 30, 2026](</index/how-chatgpt-adoption-has-expanded/>)
  - [Our approach to government and national security partnershipsGlobal AffairsJul 8, 2026](</index/government-national-sec
  - ![Helping K–12 educators build practical AI skills > Cover image](https://images.ctfassets.net/kftzwdyauwt9/190wMCP1bPt9

### https://openai.com/index/more-enterprise-grade-features-for-api-customers/
- lastmod: `2026-09-23T20:42:00.372Z` → `2026-10-08T17:01:07.049Z`
- Content length: 10807 → 10983 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/morgan-stanley/
- lastmod: `2026-09-22T19:25:08.677Z` → `2026-10-08T22:48:49.871Z`
- Content length: 12432 → 12608 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/mufg/
- lastmod: `2026-09-22T21:15:41.049Z` → `2026-10-08T22:48:52.069Z`
- Content length: 14469 → 14620 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/my-dog-the-math-tutor/
- lastmod: `2026-09-08T20:26:06.270Z` → `2026-10-08T16:37:02.679Z`
- Content length: 10331 → 10611 chars (delta: +280)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![An abstract expressionist painting of a desk and chair near a window in a warm color palette.](https://images.ctfasset
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  -   * [Codex](</codex/>)
  - ![Media > ChatGPT Education](https://images.ctfassets.net/kftzwdyauwt9/1qCEfO78yhwFeaBFu3kCd6/b57a627f10f4a353443994ed06

### https://openai.com/index/navier-stokes-solution/
- lastmod: `2026-09-28T05:00:16.266Z` → `2026-10-09T08:57:24.320Z`
- Content length: 15597 → 15717 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/navigating-health-questions/
- lastmod: `2026-09-15T10:36:38.113Z` → `2026-10-09T04:36:21.546Z`
- Content length: 4389 → 4601 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/navigating-the-challenges-and-opportunities-of-synthetic-voices/
- lastmod: `2026-09-23T20:42:01.217Z` → `2026-10-09T06:33:38.928Z`
- Content length: 13096 → 13272 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/neurogum/
- lastmod: `2026-09-22T21:15:43.944Z` → `2026-10-08T22:45:57.669Z`
- Content length: 10499 → 10650 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/
- lastmod: `2026-09-18T17:01:22.541Z` → `2026-10-08T17:01:07.799Z`
- Content length: 10751 → 11190 chars (delta: +439)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/new-and-improved-content-moderation-tooling/
- lastmod: `2026-09-23T20:42:18.940Z` → `2026-10-08T17:01:05.800Z`
- Content length: 8101 → 8277 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/new-and-improved-embedding-model/
- lastmod: `2026-09-23T20:42:01.207Z` → `2026-10-08T17:01:07.734Z`
- Content length: 10111 → 10310 chars (delta: +199)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + Dataset: [BEIR(opens in a new window)](<https://github.com/UKPLab/beir>) (ArguAna, ClimateFEVER, DBPedia, FEVER, FiQA201
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  - Dataset: [BEIR](<https://github.com/UKPLab/beir>) (ArguAna, ClimateFEVER, DBPedia, FEVER, FiQA2018, HotpotQA, NFCorpus, 
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/new-chatgpt-images-is-here/
- lastmod: `2026-09-22T21:28:01.964Z` → `2026-10-09T06:33:31.534Z`
- Content length: 28376 → 28552 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/new-policy-ideas-for-the-intelligence-age/
- lastmod: `2026-09-17T11:33:59.455Z` → `2026-10-09T07:22:00.730Z`
- Content length: 15733 → 16025 chars (delta: +292)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Expanding AI access across every level of US governmentGlobal AffairsSep 10, 2026](</index/expanding-ai-access-us-gover
  -   * [Codex](</codex/>)
  - ![Helping older adults use AI in everyday life — art card](https://images.ctfassets.net/kftzwdyauwt9/6ewlK5oKVHp0phTezeh
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Helping older adults use AI in everyday lifeGlobal AffairsSep 16, 2026](</index/helping-older-adults-use-ai-in-everyday

### https://openai.com/index/new-result-theoretical-physics/
- lastmod: `2026-09-25T19:18:24.210Z` → `2026-10-08T12:06:52.122Z`
- Content length: 10797 → 10917 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/new-tools-for-chatgpt-enterprise/
- lastmod: `2026-09-18T17:01:23.289Z` → `2026-10-08T17:01:08.116Z`
- Content length: 14894 → 15106 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/next-chapter-of-microsoft-openai-partnership/
- lastmod: `2026-06-11T17:31:32.192Z` → `2026-10-03T13:05:25.153Z`
- Content length: 8093 → 8437 chars (delta: +344)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/nextdoor/
- lastmod: `2026-09-22T21:15:47.723Z` → `2026-10-09T05:56:03.110Z`
- Content length: 8655 → 8763 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/norad-holiday-collaboration/
- lastmod: `2026-08-14T04:15:24.260Z` → `2026-10-03T13:05:25.907Z`
- Content length: 7529 → 7599 chars (delta: +70)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/notion/
- lastmod: `2026-09-22T21:15:47.311Z` → `2026-10-09T05:56:03.298Z`
- Content length: 8929 → 9080 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/ntt-data/
- lastmod: `2026-09-22T21:15:41.543Z` → `2026-10-09T05:56:00.820Z`
- Content length: 15138 → 15289 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/nubank/
- lastmod: `2026-09-22T19:25:10.546Z` → `2026-10-09T06:07:33.795Z`
- Content length: 9886 → 10062 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/nvidia/
- lastmod: `2026-09-22T19:25:24.912Z` → `2026-10-09T05:56:09.771Z`
- Content length: 9127 → 9235 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/nvidia/chatgpt-work/
- lastmod: `2026-09-22T21:15:33.634Z` → `2026-10-08T22:48:48.182Z`
- Content length: 9922 → 10030 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/o1-coding/
- lastmod: `2026-09-08T20:26:08.495Z` → `2026-10-07T16:05:17.083Z`
- Content length: 3593 → 3805 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/o3-o4-mini-system-card/
- lastmod: `2026-09-25T19:10:14.335Z` → `2026-10-03T13:21:05.039Z`
- Content length: 5369 → 5545 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/offering-zero-data-retention-for-frontier-models/
- lastmod: `2026-09-25T19:16:14.990Z` → `2026-10-08T23:22:09.050Z`
- Content length: 12125 → 12190 chars (delta: +65)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - [Sam Altman’s remarks at the United Nations Security CouncilGlobal AffairsSep 23, 2026](</index/sam-altman-un-security-c

### https://openai.com/index/omio/
- lastmod: `2026-09-22T21:15:38.883Z` → `2026-10-09T05:56:00.340Z`
- Content length: 12294 → 12445 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/one-in-a-million-customers/
- lastmod: `2026-06-04T15:05:44.806Z` → `2026-10-08T21:25:29.061Z`
- Content length: 8477 → 8724 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-and-apa-partner-to-advance-responsible-ai/
- lastmod: `2026-09-22T22:05:59.014Z` → `2026-10-09T06:21:24.881Z`
- Content length: 10528 → 10583 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/
- lastmod: `2026-09-22T22:06:06.147Z` → `2026-10-03T13:05:21.878Z`
- Content length: 8606 → 8661 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/openai-and-journalism/
- lastmod: `2026-09-23T20:41:59.439Z` → `2026-10-08T17:01:03.482Z`
- Content length: 15635 → 15811 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-announces-new-members-to-board-of-directors/
- lastmod: `2026-08-25T20:41:39.279Z` → `2026-10-03T13:14:07.484Z`
- Content length: 8171 → 8639 chars (delta: +468)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![OpenAI and Elon Musk > Media Item](https://images.ctfassets.net/kftzwdyauwt9/2M3VUBzndWoB6PWQ9Uad8u/4abfd8660278a65772

### https://openai.com/index/openai-api/
- lastmod: `2026-09-23T20:42:08.075Z` → `2026-10-09T05:46:17.221Z`
- Content length: 15602 → 15778 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-contract-data-agent/
- lastmod: `2026-09-14T21:27:53.770Z` → `2026-10-06T17:53:44.892Z`
- Content length: 9059 → 9278 chars (delta: +219)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-cybersecurity-grant-program/
- lastmod: `2026-09-22T22:05:54.615Z` → `2026-10-05T19:23:10.627Z`
- Content length: 8867 → 9270 chars (delta: +403)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
  + ![Abstract soft-focus background with a delicate blend of pale peach and a hint of pink.](https://images.ctfassets.net/k
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-deutschland/
- lastmod: `2026-08-25T20:41:41.487Z` → `2026-10-03T13:14:14.343Z`
- Content length: 7610 → 7862 chars (delta: +252)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense/
- lastmod: `2026-09-26T22:35:22.165Z` → `2026-10-09T06:21:30.855Z`
- Content length: 7429 → 7594 chars (delta: +165)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Building standards for the next phase of AIGlobal AffairsSep 21, 2026](</index/building-standards-next-phase-ai/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ![Building shared standards for the next phase of AI - art card](https://images.ctfassets.net/kftzwdyauwt9/aQqo6ytHD8RKL

### https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/
- lastmod: `2026-09-23T20:42:00.758Z` → `2026-10-09T06:33:38.786Z`
- Content length: 10865 → 10859 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/openai-gtm-assistant/
- lastmod: `2026-09-14T21:27:49.975Z` → `2026-10-06T17:53:42.020Z`
- Content length: 9408 → 9624 chars (delta: +216)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-inbound-sales-assistant/
- lastmod: `2026-09-14T21:27:49.975Z` → `2026-10-06T17:53:42.421Z`
- Content length: 10119 → 10337 chars (delta: +218)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-nvidia-systems-partnership/
- lastmod: `2026-06-10T09:36:30.871Z` → `2026-10-03T13:05:49.591Z`
- Content length: 7888 → 7961 chars (delta: +73)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/
- lastmod: `2026-08-19T00:21:16.272Z` → `2026-10-07T19:08:22.092Z`
- Content length: 8889 → 9589 chars (delta: +700)
- Sample new content lines:
  + [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + The ChatGPT access information reflects the September 2024 launch. o1‑mini has been retired from the API. See the [API d
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-o3-mini/
- lastmod: `2026-04-30T06:51:16.703Z` → `2026-10-09T05:04:22.722Z`
- Content length: 19131 → 19824 chars (delta: +693)
- Sample new content lines:
  + [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + The ChatGPT access information reflects the January 2025 launch. o3‑mini is deprecated in the API. See the [API deprecat
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-on-aws/
- lastmod: `2026-09-23T20:42:02.373Z` → `2026-10-09T05:56:05.444Z`
- Content length: 9537 → 9531 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/openai-on-oracle-cloud/
- lastmod: `2026-09-23T20:41:59.718Z` → `2026-10-09T09:07:55.901Z`
- Content length: 6642 → 6774 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-research-assistant/
- lastmod: `2026-09-14T21:27:53.586Z` → `2026-10-06T17:53:44.255Z`
- Content length: 9758 → 9973 chars (delta: +215)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-scholars/
- lastmod: `2026-09-22T22:06:01.344Z` → `2026-10-03T13:14:06.723Z`
- Content length: 10179 → 10582 chars (delta: +403)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Blurred abstract image with a soft fusion of peach, green, and pink hues with a white smudge in the upper region.](htt
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Soft pastel painting depicting a serene sky with wispy clouds, blending aqua, peach, and a hint of yellow at the horiz
  + ![Abstract soft-focus background with a delicate blend of pale peach and a hint of pink.](https://images.ctfassets.net/k
- Sample removed content lines:
  - ![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/f
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-support-model/
- lastmod: `2026-09-14T21:27:52.706Z` → `2026-10-06T17:53:43.424Z`
- Content length: 11704 → 11923 chars (delta: +219)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/openai-to-acquire-ona/
- lastmod: `2026-09-22T22:06:06.808Z` → `2026-10-09T06:39:38.335Z`
- Content length: 10146 → 10201 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/optimizing-chatgpt/
- lastmod: `2026-09-25T18:57:19.818Z` → `2026-10-08T17:01:02.277Z`
- Content length: 9823 → 9676 chars (delta: -147)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/

### https://openai.com/index/our-agreement-with-the-department-of-war/
- lastmod: `2026-08-14T03:37:36.055Z` → `2026-10-07T21:18:36.698Z`
- Content length: 14821 → 14898 chars (delta: +77)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/our-approach-to-advertising-and-expanding-access/
- lastmod: `2026-09-25T19:16:20.869Z` → `2026-10-09T06:33:31.086Z`
- Content length: 10299 → 10188 chars (delta: -111)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/our-approach-to-age-prediction/
- lastmod: `2026-09-25T18:56:55.354Z` → `2026-10-01T15:52:30.704Z`
- Content length: 9138 → 9314 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/our-approach-to-the-model-spec/
- lastmod: `2026-09-25T19:18:30.093Z` → `2026-10-08T12:07:03.523Z`
- Content length: 34633 → 34753 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
- lastmod: `2026-09-25T19:16:26.177Z` → `2026-10-09T06:21:02.657Z`
- Content length: 6789 → 6921 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/
- lastmod: `2026-09-25T19:16:30.636Z` → `2026-10-08T23:55:51.322Z`
- Content length: 13908 → 14167 chars (delta: +259)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/pacing-model-development-cyber-capabilities/
- lastmod: `2026-09-25T19:10:10.453Z` → `2026-10-07T19:53:57.099Z`
- Content length: 15008 → 15150 chars (delta: +142)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/parallel-cuts-time-and-cost-with-astra/
- lastmod: `2026-09-26T22:21:19.281Z` → `2026-10-08T20:19:04.381Z`
- Content length: 7137 → 7312 chars (delta: +175)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  - ![V7 customer story art card - smaller logo](https://images.ctfassets.net/kftzwdyauwt9/3Av2nLs9MOiSrB5wMXLvL2/35fbde20ac
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/parloa/
- lastmod: `2026-09-22T13:14:32.365Z` → `2026-10-09T00:13:50.116Z`
- Content length: 14460 → 14664 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/partnering-with-codeai/
- lastmod: `2026-09-22T22:05:57.114Z` → `2026-10-08T16:37:01.114Z`
- Content length: 10328 → 10383 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/patch-the-planet/
- lastmod: `2026-09-22T18:49:07.311Z` → `2026-10-05T11:17:49.559Z`
- Content length: 18145 → 18588 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/path-to-astra/
- lastmod: `2026-09-25T19:16:27.142Z` → `2026-10-09T06:20:57.863Z`
- Content length: 20070 → 20091 chars (delta: +21)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/paul-christiano-joins-openai-foundation-board/
- lastmod: `2026-09-25T19:16:17.637Z` → `2026-10-09T07:56:24.611Z`
- Content length: 10470 → 10602 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/people-first-ai-fund/
- lastmod: `2026-09-22T22:06:01.069Z` → `2026-10-09T06:07:34.382Z`
- Content length: 12102 → 12244 chars (delta: +142)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  -   * [Codex](</codex/>)
  - [Building standards for the next phase of AIGlobal AffairsSep 21, 2026](</index/building-standards-next-phase-ai/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/perplexity-improving-accuracy-with-astra/
- lastmod: `2026-09-23T22:14:16.528Z` → `2026-10-07T23:30:51.526Z`
- Content length: 6373 → 6411 chars (delta: +38)
- Sample new content lines:
  + [Ringg’s AI agents resolve up to 65% of customer calls with OpenAISep 23, 2026](</index/ringg/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Ringg AI customer story art card and hero](https://images.ctfassets.net/kftzwdyauwt9/6bRPKvsny2bwgyOeg0Pedd/5dd852a286
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/personal-finance-chatgpt/
- lastmod: `2026-09-25T19:16:12.872Z` → `2026-10-09T06:33:30.234Z`
- Content length: 20934 → 21787 chars (delta: +853)
- Sample new content lines:
  +   * **Credit monitoring** to help you track your credit score over time and understand the factors affecting it.
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + **_Update on June 25, 2026:_**_The personal finance experience in ChatGPT is now available to Plus and Pro users in the 
  +   * **Stock watchlists** so you can follow stocks you’re interested in and see how they’re performing.
  +   * **Weekly updates** with insights to help you stay on top of your finances.
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/philips/
- lastmod: `2026-09-22T21:15:42.722Z` → `2026-10-08T22:48:53.193Z`
- Content length: 9152 → 9260 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/playco-game-prototyping-with-astra/
- lastmod: `2026-09-22T13:14:03.656Z` → `2026-10-09T01:12:08.367Z`
- Content length: 7569 → 7773 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/plex-coffee/
- lastmod: `2026-09-22T21:15:40.347Z` → `2026-10-08T22:45:55.138Z`
- Content length: 11491 → 11599 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/podium/
- lastmod: `2026-09-22T21:15:35.926Z` → `2026-10-09T05:50:41.572Z`
- Content length: 10774 → 10882 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/polimill/
- lastmod: `2026-09-22T13:14:04.342Z` → `2026-10-09T05:55:59.298Z`
- Content length: 14117 → 14268 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/praktika/
- lastmod: `2026-09-22T13:14:09.566Z` → `2026-10-08T16:37:01.701Z`
- Content length: 12020 → 12224 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/premium-seats-chatgpt-business/
- lastmod: `2026-09-25T19:16:25.953Z` → `2026-10-09T06:33:26.079Z`
- Content length: 9204 → 9198 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/preply/
- lastmod: `2026-09-22T21:15:45.283Z` → `2026-10-09T05:56:01.959Z`
- Content length: 15971 → 16122 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/previewing-gpt-5-6-sol/
- lastmod: `2026-09-28T00:57:06.099Z` → `2026-10-09T06:33:35.751Z`
- Content length: 59207 → 59201 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/previewing-ultrafast/
- lastmod: `2026-09-25T19:16:33.333Z` → `2026-10-09T06:33:33.231Z`
- Content length: 11103 → 11031 chars (delta: -72)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + Get Access Updates
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - [Get Access Updates](</form/ultrafast/>)
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/

### https://openai.com/index/priorities-principles-third-party-assessments/
- lastmod: `2026-09-27T12:31:42.815Z` → `2026-10-09T06:21:05.492Z`
- Content length: 19863 → 19922 chars (delta: +59)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  - [Funding grants for new research into AI and teen developmentSafetySep 8, 2026](</index/teen-development-research-grants
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/proaction/
- lastmod: `2026-09-25T22:07:15.676Z` → `2026-10-09T05:55:58.820Z`
- Content length: 11265 → 11260 chars (delta: -5)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/prompt-injections/
- lastmod: `2026-09-17T10:07:03.688Z` → `2026-10-09T06:07:33.356Z`
- Content length: 17186 → 17665 chars (delta: +479)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/public-policy-agenda/
- lastmod: `2026-08-25T00:28:22.936Z` → `2026-10-09T04:20:07.101Z`
- Content length: 22187 → 22503 chars (delta: +316)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/index/put-ai-to-work-for-your-product-team/
- lastmod: `2026-09-02T00:20:45.696Z` → `2026-10-03T13:14:14.229Z`
- Content length: 3479 → 3726 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/put-data-to-work/
- lastmod: `2026-09-25T19:16:13.899Z` → `2026-10-09T07:53:42.127Z`
- Content length: 20592 → 20655 chars (delta: +63)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [@Data Diagnose why weekly active users changed last week. Identify likely drivers, compare against prior periods, and r
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [@Data Turn this month’s metrics into a leadership-ready update with actuals, comparisons, drivers, caveats, and recomme
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)

### https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands/
- lastmod: `2026-09-25T19:16:31.227Z` → `2026-10-05T19:23:11.715Z`
- Content length: 16867 → 17126 chars (delta: +259)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/rakuten/
- lastmod: `2026-09-22T21:15:48.835Z` → `2026-10-08T22:48:59.685Z`
- Content length: 10852 → 11003 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/ramp/
- lastmod: `2026-09-22T21:15:48.038Z` → `2026-10-09T05:55:57.461Z`
- Content length: 10051 → 10202 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/reasoning-models-chain-of-thought-controllability/
- lastmod: `2026-09-25T19:18:20.092Z` → `2026-10-08T12:06:44.144Z`
- Content length: 15762 → 15886 chars (delta: +124)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/red-teaming-network/
- lastmod: `2026-05-31T20:06:24.028Z` → `2026-10-09T05:41:08.823Z`
- Content length: 15729 → 16212 chars (delta: +483)
- Sample new content lines:
  + Applications for this phase of the OpenAI Red Teaming Network closed on December 1, 2023.
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [Supply Co.](</supply/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d63
  - ![Disrupting malicious > media](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc
  - **Applications are now closed.** Join us in this mission to build safe AGI that benefits humanity. Apply to be a part of
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/reimagining-advertising-with-ai/
- lastmod: `2026-09-26T12:26:15.440Z` → `2026-10-09T06:33:41.761Z`
- Content length: 10280 → 10274 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/replit/
- lastmod: `2026-09-22T13:14:05.758Z` → `2026-10-03T13:15:19.838Z`
- Content length: 8398 → 8602 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/research-acceleration-view-inside-openai/
- lastmod: `2026-09-28T05:17:06.151Z` → `2026-10-09T06:21:28.288Z`
- Content length: 20713 → 20837 chars (delta: +124)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/
- lastmod: `2026-09-25T19:16:30.000Z` → `2026-10-05T19:23:11.336Z`
- Content length: 8608 → 9051 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/ringcentral/
- lastmod: `2026-09-22T21:15:34.291Z` → `2026-10-09T05:56:18.414Z`
- Content length: 9069 → 9177 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/ringg/
- lastmod: `2026-09-23T23:55:09.949Z` → `2026-10-07T23:30:52.350Z`
- Content length: 14289 → 14365 chars (delta: +76)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Basis customer story art card - slate blue texture](https://images.ctfassets.net/kftzwdyauwt9/3yUNvl0PGh8nEqRYASjSM1/d
  + ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa
  + [Parallel cut research time and cost in half with GPT‑6 AstraStartupSep 22, 2026](</index/parallel-cuts-time-and-cost-wi
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/running-codex-safely/
- lastmod: `2026-09-22T09:51:53.396Z` → `2026-10-09T05:56:09.215Z`
- Content length: 14675 → 14769 chars (delta: +94)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  - [Funding grants for new research into AI and teen developmentSafetySep 8, 2026](</index/teen-development-research-grants
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/safety-alignment-long-horizon-models/
- lastmod: `2026-09-25T18:56:55.836Z` → `2026-10-01T15:52:32.389Z`
- Content length: 16001 → 15982 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/safety-bug-bounty/
- lastmod: `2026-09-25T19:16:30.631Z` → `2026-10-05T19:23:11.837Z`
- Content length: 8730 → 8751 chars (delta: +21)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/safety-overview-gpt-6-astra/
- lastmod: `2026-09-25T19:16:27.583Z` → `2026-10-05T11:17:47.936Z`
- Content length: 11501 → 11482 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/safetykit/
- lastmod: `2026-09-22T21:15:51.917Z` → `2026-10-08T22:46:03.209Z`
- Content length: 11683 → 11791 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/sam-altman-un-security-council-remarks/
- lastmod: `2026-09-23T20:53:34.445Z` → `2026-10-01T21:57:49.432Z`
- Content length: 15161 → 15078 chars (delta: -83)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2

### https://openai.com/index/scaling-ai-for-everyone/
- lastmod: `2026-06-08T07:44:58.295Z` → `2026-10-08T21:54:04.194Z`
- Content length: 8714 → 8784 chars (delta: +70)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/scaling-codex-to-enterprises-worldwide/
- lastmod: `2026-09-22T09:51:52.408Z` → `2026-10-09T05:56:08.888Z`
- Content length: 8839 → 8894 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/scaling-social-science-research/
- lastmod: `2026-09-25T19:33:52.210Z` → `2026-10-08T12:06:50.621Z`
- Content length: 8030 → 8023 chars (delta: -7)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)

### https://openai.com/index/scaling-storage-one-billion-users-part-one/
- lastmod: `2026-09-26T14:25:04.165Z` → `2026-10-09T06:21:05.591Z`
- Content length: 27213 → 27389 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/scaling-trusted-access-for-cyber-defense/
- lastmod: `2026-09-25T17:53:41.262Z` → `2026-10-05T19:23:13.295Z`
- Content length: 16829 → 16850 chars (delta: +21)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/scania/
- lastmod: `2026-09-22T21:15:44.398Z` → `2026-10-08T22:48:54.657Z`
- Content length: 8425 → 8576 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/schoolai/
- lastmod: `2026-09-22T21:15:41.842Z` → `2026-10-08T22:45:49.288Z`
- Content length: 12424 → 12575 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/scientific-computing-agentic-ai/
- lastmod: `2026-09-25T19:18:28.961Z` → `2026-10-08T12:06:44.750Z`
- Content length: 12628 → 12748 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sea-david-chen/
- lastmod: `2026-09-22T09:51:53.769Z` → `2026-10-09T05:56:09.179Z`
- Content length: 13809 → 13917 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/searchgpt-prototype/
- lastmod: `2026-09-18T17:01:19.224Z` → `2026-10-08T17:01:04.413Z`
- Content length: 8018 → 8230 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- lastmod: `2026-09-25T19:18:12.532Z` → `2026-10-09T06:20:59.916Z`
- Content length: 14741 → 14861 chars (delta: +120)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sharing-the-latest-model-spec/
- lastmod: `2026-06-20T10:31:10.220Z` → `2026-10-09T04:35:20.556Z`
- Content length: 12117 → 12370 chars (delta: +253)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/shipping-sora-for-android-with-codex/
- lastmod: `2026-07-25T07:07:34.988Z` → `2026-10-03T13:00:47.313Z`
- Content length: 21307 → 21554 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sora 2 system card](https://images.ctfassets.net/kftzwdyauwt9/2ODeQUACmwUM3lkFQKzWki/426121ad50716c1a1eb4034ecb824c7e/
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Sora 2 system card cover image](https://images.ctfassets.net/kftzwdyauwt9/2ODeQUACmwUM3lkFQKzWki/426121ad50716c1a1eb40
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/singular-bank/
- lastmod: `2026-09-22T21:15:46.403Z` → `2026-10-09T05:56:02.575Z`
- Content length: 10349 → 10457 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/small-business-stories/
- lastmod: `2026-09-08T20:26:10.630Z` → `2026-10-07T16:05:19.282Z`
- Content length: 31335 → 30654 chars (delta: -681)
- Sample new content lines:
  +   * A tamale shop in California![A small street-side tamale stand with a red awning and a neon ‘Tamales Express’ sign is
  +   * A seed farm in South Carolina![Two people walk across a dry agricultural field while a long metal irrigation system 
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  -   * [Codex](</codex/>)
  - A salvage yard in Nevada![A worker wearing a yellow high-visibility vest and hard hat walks through a scrapyard between 

### https://openai.com/index/sora-2-system-card/
- lastmod: `2026-05-22T18:57:44.186Z` → `2026-10-09T05:34:52.755Z`
- Content length: 6210 → 6457 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sora-2/
- lastmod: `2026-09-25T19:18:32.433Z` → `2026-10-09T06:33:33.484Z`
- Content length: 21910 → 22086 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sora-is-here/
- lastmod: `2026-09-18T17:01:19.679Z` → `2026-10-08T17:01:05.252Z`
- Content length: 9659 → 9871 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sora-system-card/
- lastmod: `2026-09-25T19:10:13.921Z` → `2026-10-01T00:45:08.559Z`
- Content length: 36575 → 36751 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sora-vallee-duhamel/
- lastmod: `2026-09-08T20:26:10.180Z` → `2026-10-07T16:05:18.725Z`
- Content length: 3525 → 3737 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/sora/
- lastmod: `2026-09-25T19:18:20.749Z` → `2026-10-08T12:07:01.421Z`
- Content length: 21840 → 22016 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/south-korea-economic-blueprint/
- lastmod: `2026-08-14T01:45:39.148Z` → `2026-10-03T13:05:23.441Z`
- Content length: 11270 → 11436 chars (delta: +166)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/speeding-up-agentic-workflows-with-websockets/
- lastmod: `2026-09-23T20:42:07.190Z` → `2026-10-09T05:56:08.201Z`
- Content length: 15212 → 15388 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/stadler/
- lastmod: `2026-09-22T21:15:49.676Z` → `2026-10-08T22:46:01.279Z`
- Content length: 9699 → 9807 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/stampli/
- lastmod: `2026-09-22T21:15:32.975Z` → `2026-10-09T09:16:07.289Z`
- Content length: 11368 → 11476 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/stargate-advances-with-partnership-with-oracle/
- lastmod: `2026-09-22T22:06:09.089Z` → `2026-10-03T13:05:37.821Z`
- Content length: 8878 → 8979 chars (delta: +101)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - ![""](https://images.ctfassets.net/kftzwdyauwt9/4xr6uwep8z7k2zV7SBBP4A/89f640504c1b915691b6fa9edeb7fa25/IMG_1628.jpg?w=3
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf

### https://openai.com/index/statement-on-openai-nonprofit-and-pbc/
- lastmod: `2026-06-05T04:06:47.500Z` → `2026-10-03T13:05:43.575Z`
- Content length: 7146 → 7216 chars (delta: +70)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Supporting Thailand’s next generation of AI startups > Cover image](https://images.ctfassets.net/kftzwdyauwt9/6ttG55Aq
  -   * [Codex](</codex/>)
  - ![Expanding OpenAI’s presence in Brazil > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7jZgAn4y7ZP5GFx0HimbWT/
  - [Expanding OpenAI’s presence in BrazilCompanyAug 27, 2026](</index/expanding-our-presence-in-brazil/>)
  - ![Better answers, broader thinking: What students gain from ChatGPT and critical-thinking training > Cover image](https:

### https://openai.com/index/steuerrecht/
- lastmod: `2026-09-22T21:15:42.088Z` → `2026-10-08T22:45:55.582Z`
- Content length: 11825 → 11976 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/
- lastmod: `2026-09-25T18:57:08.607Z` → `2026-10-03T13:05:22.678Z`
- Content length: 24179 → 24160 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/strengthening-cyber-resilience/
- lastmod: `2026-09-17T10:07:05.848Z` → `2026-10-09T06:07:33.906Z`
- Content length: 14377 → 14856 chars (delta: +479)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/strengthening-safety-with-external-testing/
- lastmod: `2026-06-04T18:35:22.683Z` → `2026-10-08T23:28:38.157Z`
- Content length: 23093 → 23594 chars (delta: +501)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [Plugins](</business/plugins/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-
  - ![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cah
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/
- lastmod: `2026-09-25T19:18:12.025Z` → `2026-10-09T08:10:37.317Z`
- Content length: 16011 → 15958 chars (delta: -53)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/stripe/
- lastmod: `2026-09-23T20:41:59.724Z` → `2026-10-08T22:48:54.209Z`
- Content length: 9932 → 9947 chars (delta: +15)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/supporting-california-bill-advance-ai-youth-safety/
- lastmod: `2026-09-25T19:16:24.961Z` → `2026-10-05T11:17:46.471Z`
- Content length: 10643 → 10775 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/supporting-independent-journalism-in-ukraine/
- lastmod: `2026-09-25T19:16:19.614Z` → `2026-10-08T03:26:58.328Z`
- Content length: 11116 → 11234 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/supporting-journalism-from-classrooms-to-newsrooms/
- lastmod: `2026-09-25T19:16:20.953Z` → `2026-10-09T06:21:05.055Z`
- Content length: 14049 → 14248 chars (delta: +199)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * OpenAI’s continued support for the **Lenfest Institute for Journalism** ’s AI Collaborative and Fellowship program, 

### https://openai.com/index/supporting-next-generation-ai-startups-thailand/
- lastmod: `2026-09-25T19:16:46.096Z` → `2026-10-05T11:17:46.868Z`
- Content length: 14297 → 14429 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/taisei/
- lastmod: `2026-09-22T19:25:10.853Z` → `2026-10-08T22:48:51.574Z`
- Content length: 9423 → 9574 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/teen-development-research-grants/
- lastmod: `2026-09-25T19:16:14.844Z` → `2026-10-08T23:34:54.229Z`
- Content length: 15593 → 15574 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/teen-safety-freedom-and-privacy/
- lastmod: `2026-09-25T18:56:57.429Z` → `2026-10-03T13:05:24.050Z`
- Content length: 8623 → 8688 chars (delta: +65)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - [Sam Altman’s remarks at the United Nations Security CouncilGlobal AffairsSep 23, 2026](</index/sam-altman-un-security-c

### https://openai.com/index/ten-advances-in-mathematics/
- lastmod: `2026-09-25T19:10:09.734Z` → `2026-10-07T19:53:40.572Z`
- Content length: 10361 → 10497 chars (delta: +136)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  - ![Research acceleration: The view inside OpenAI > Cover image](https://images.ctfassets.net/kftzwdyauwt9/5kS3OG1Jfdja5xL
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Research acceleration: The view inside OpenAIResearchSep 6, 2026](</index/research-acceleration-view-inside-openai/>)

### https://openai.com/index/ten-tiny-canvases/
- lastmod: `2026-09-08T20:26:06.361Z` → `2026-10-07T16:05:15.830Z`
- Content length: 11497 → 11782 chars (delta: +285)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Zalando logo in white, centered over a textured blue surface resembling fabric or a synthetic material.](https://image
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![\[2.0\] Card > Media > Zalando](https://images.ctfassets.net/kftzwdyauwt9/6SOwtELA1S0TYqttuHDBux/39e0d269327c02d3a6cc8
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/testing-ads-in-chatgpt/
- lastmod: `2026-09-25T19:16:20.514Z` → `2026-10-09T06:33:41.212Z`
- Content length: 13350 → 13239 chars (delta: -111)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/index/the-defenders-window/
- lastmod: `2026-09-25T19:16:28.260Z` → `2026-10-09T05:55:59.422Z`
- Content length: 17252 → 17695 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/the-five-ai-value-models-driving-business-reinvention/
- lastmod: `2026-07-28T02:04:44.104Z` → `2026-10-09T09:16:31.481Z`
- Content length: 17672 → 18022 chars (delta: +350)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How AI-native companies turn workflows into operating capabilityAI AdoptionSep 1, 2026](</index/ai-native-company-workf
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [Introducing the ChatGPT for small business programAI AdoptionJul 21, 2026](</index/introducing-chatgpt-small-business-p
  -   * [Codex](</codex/>)
  - [How to manage AI investments in the agentic eraAI AdoptionJul 14, 2026](</index/managing-ai-investments-in-agentic-era/
  - [AI Adoption](</news/ai-adoption/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/the-full-stack-behind-abundant-intelligence/
- lastmod: `2026-09-25T19:16:34.381Z` → `2026-10-09T06:21:13.673Z`
- Content length: 10270 → 10402 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/the-met-museum/
- lastmod: `2026-09-08T20:26:06.184Z` → `2026-10-07T16:05:15.542Z`
- Content length: 4925 → 5137 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/the-next-chapter-for-uk-sovereign-ai/
- lastmod: `2026-08-19T00:31:12.100Z` → `2026-10-09T06:07:55.527Z`
- Content length: 9148 → 9459 chars (delta: +311)
- Sample new content lines:
  + ![OpenAI extends cyber access to Ukraine for civilian defense — cover](https://images.ctfassets.net/kftzwdyauwt9/4NsiJiq
  + ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - ![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0
  -   * [Codex](</codex/>)
  - [Disrupting a new covert influence campaign from RussiaGlobal AffairsAug 25, 2026](</index/disrupting-malicious-uses-of-
  - ![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card 
  - ![DMUA Russia > card image ](https://images.ctfassets.net/kftzwdyauwt9/ciRSLFnJsNyxXYQjdoyqu/ff8ab22ad273ff79a4c9840f0c2

### https://openai.com/index/the-state-of-enterprise-ai-2025-report/
- lastmod: `2026-09-25T19:18:11.318Z` → `2026-10-09T06:07:34.928Z`
- Content length: 11550 → 11570 chars (delta: +20)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  - [Sam Altman’s remarks at the United Nations Security CouncilGlobal AffairsSep 23, 2026](</index/sam-altman-un-security-c

### https://openai.com/index/the-work-now-within-reach/
- lastmod: `2026-09-25T19:16:18.374Z` → `2026-10-09T06:21:22.051Z`
- Content length: 14114 → 14246 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/thinking-with-images/
- lastmod: `2026-07-25T07:01:47.117Z` → `2026-10-09T04:44:50.488Z`
- Content length: 33256 → 34179 chars (delta: +923)
- Sample new content lines:
  + The availability information reflects the April 2025 launch. o3 and o4-mini are no longer available in ChatGPT and are d
  + [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/
- lastmod: `2026-09-25T19:16:28.802Z` → `2026-10-08T20:09:25.797Z`
- Content length: 13004 → 13447 chars (delta: +443)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/thrive-holdings/
- lastmod: `2026-09-22T22:05:58.007Z` → `2026-10-09T06:07:33.258Z`
- Content length: 6653 → 6708 chars (delta: +55)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [Introducing the Australian Youth Safety BlueprintCompanySep 18, 2026](</index/australian-youth-safety-blueprint/>)
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/tolan/
- lastmod: `2026-08-14T04:40:47.037Z` → `2026-10-01T14:55:01.497Z`
- Content length: 13809 → 14152 chars (delta: +343)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Replit expands access to software creation with GPT-5.6 LunaStartupAug 19, 2026](</index/replit/>)
  -   * [Codex](</codex/>)
  - ![Model ML customer story card image](https://images.ctfassets.net/kftzwdyauwt9/3STNMQMrFRC8mFdLYtjkV4/9cc21e9c729b2ae7c
  - [Model ML completes finance work more efficiently with GPT-5.6 SolStartupAug 10, 2026](</index/model-ml/>)
  - ![Warp customer story 1x1 hero art card](https://images.ctfassets.net/kftzwdyauwt9/3DK9g0hpubvAEz7lDs0nUf/713989b24b9d37

### https://openai.com/index/travelers/
- lastmod: `2026-09-22T21:15:46.907Z` → `2026-10-08T22:48:57.162Z`
- Content length: 6144 → 6252 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/trustbank/
- lastmod: `2026-09-22T19:25:13.336Z` → `2026-10-08T22:48:54.334Z`
- Content length: 13075 → 13226 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/trusted-access-for-cyber/
- lastmod: `2026-09-25T19:16:29.039Z` → `2026-10-05T19:23:09.425Z`
- Content length: 10216 → 10237 chars (delta: +21)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- lastmod: `2026-06-23T22:24:30.727Z` → `2026-10-08T23:29:31.324Z`
- Content length: 29261 → 29774 chars (delta: +513)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [Plugins](</business/plugins/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-
  - ![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cah
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/two-blind-brothers/
- lastmod: `2026-09-24T12:11:02.531Z` → `2026-10-08T20:14:11.393Z`
- Content length: 13234 → 13410 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/two-years-of-openai-academy/
- lastmod: `2026-09-28T07:10:24.179Z` → `2026-10-09T06:21:04.585Z`
- Content length: 10585 → 10637 chars (delta: +52)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Expanding OpenAI Academy with new learning pathsCompanySep 21, 2026](</index/expanding-openai-academy-with-new-learning

### https://openai.com/index/uber-enables-outstanding-experiences/
- lastmod: `2026-09-22T13:14:12.953Z` → `2026-10-06T17:54:01.438Z`
- Content length: 13369 → 13545 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/uber/
- lastmod: `2026-09-22T21:15:47.148Z` → `2026-10-08T22:48:57.552Z`
- Content length: 14325 → 14433 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/understanding-ai-and-learning-outcomes/
- lastmod: `2026-09-25T19:34:03.194Z` → `2026-10-08T16:37:03.351Z`
- Content length: 18477 → 18595 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/understanding-the-source-of-what-we-see-and-hear-online/
- lastmod: `2026-09-25T19:18:29.156Z` → `2026-10-08T12:06:43.781Z`
- Content length: 15518 → 15694 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/unive/
- lastmod: `2026-09-22T21:15:36.817Z` → `2026-10-08T22:45:53.025Z`
- Content length: 14427 → 14578 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/unlocking-new-ways-of-working/
- lastmod: `2026-09-25T19:33:48.297Z` → `2026-10-09T06:21:04.170Z`
- Content length: 11816 → 11934 chars (delta: +118)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Grab and OpenAI bring practical AI skills to Southeast Asia — cover](https://images.ctfassets.net/kftzwdyauwt9/54XrkC2
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Grab and OpenAI bring practical AI skills to Southeast AsiaGlobal AffairsSep 23, 2026](</index/grab-openai-ai-skills-so

### https://openai.com/index/unlocking-self-improvement-gpt-red/
- lastmod: `2026-09-25T19:10:12.701Z` → `2026-10-09T06:21:13.894Z`
- Content length: 18394 → 18392 chars (delta: -2)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/index/unlocking-the-codex-harness/
- lastmod: `2026-09-22T09:51:55.085Z` → `2026-10-09T05:56:10.466Z`
- Content length: 28703 → 28879 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/unrolling-the-codex-agent-loop/
- lastmod: `2026-09-22T20:38:53.176Z` → `2026-10-09T05:56:10.676Z`
- Content length: 37066 → 37242 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/update-on-the-openai-foundation/
- lastmod: `2026-09-25T19:16:18.522Z` → `2026-10-08T19:29:57.154Z`
- Content length: 13688 → 13820 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/updating-model-spec-with-teen-protections/
- lastmod: `2026-09-25T18:56:52.009Z` → `2026-10-09T06:07:32.853Z`
- Content length: 12292 → 12357 chars (delta: +65)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - [Sam Altman’s remarks at the United Nations Security CouncilGlobal AffairsSep 23, 2026](</index/sam-altman-un-security-c

### https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials/
- lastmod: `2026-09-25T19:16:17.108Z` → `2026-10-09T05:55:58.855Z`
- Content length: 11369 → 11545 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/using-codex-to-simulate-black-holes/
- lastmod: `2026-08-10T18:19:08.922Z` → `2026-10-09T06:21:20.328Z`
- Content length: 9424 → 10143 chars (delta: +719)
- Sample new content lines:
  + [The builder’s guide to GPT‑5.6Applied AIAug 13, 2026](</index/builders-guide-to-gpt-5-6/>)
  + ![How a researcher uses Codex and ChatGPT to search for new antimicrobial molecules — card image](https://images.ctfasse
  + [How a researcher uses Codex and ChatGPT to search for new antimicrobial moleculesApplied AISep 10, 2026](</index/using-
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Derya Unutmaz card image](https://images.ctfassets.net/kftzwdyauwt9/6By12NX9sglstfwFKQTzYB/a28d6f84e91a8dae838f240db4c
  - ![Boston's Children Hospital NEJM > Cover image](https://images.ctfassets.net/kftzwdyauwt9/1VrF8z79R2Khy4PWmHRKME/380775
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - [Using AI to help physicians diagnose rare genetic diseases affecting childrenApplied AIJun 18, 2026](</index/diagnose-r

### https://openai.com/index/v7/
- lastmod: `2026-09-28T07:19:02.396Z` → `2026-10-08T14:46:02.933Z`
- Content length: 13592 → 13758 chars (delta: +166)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  -   * [Codex](</codex/>)
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/vfl-wolfsburg/
- lastmod: `2026-09-22T17:02:28.069Z` → `2026-10-09T01:12:08.961Z`
- Content length: 10365 → 10473 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/virgin-atlantic-oliver-byers/
- lastmod: `2026-09-22T19:25:23.150Z` → `2026-10-08T22:49:04.469Z`
- Content length: 14447 → 14555 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/virgin-atlantic/
- lastmod: `2026-09-22T21:15:51.002Z` → `2026-10-09T08:34:40.801Z`
- Content length: 9200 → 9308 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/virgin-atlantic/chatgpt-work/
- lastmod: `2026-09-22T21:15:38.428Z` → `2026-10-08T22:48:49.011Z`
- Content length: 9779 → 9887 chars (delta: +108)
- Sample new content lines:
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/warp/
- lastmod: `2026-09-22T13:14:08.852Z` → `2026-10-08T00:05:37.561Z`
- Content length: 11978 → 12182 chars (delta: +204)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Harvey customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/59usTWVI6pc0I3Lb6TL2ol/3d45075f
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Higgsfield AI customer story art card](https://images.ctfassets.net/kftzwdyauwt9/7A0WMEXBwLKT6RUmIz7pfX/c764d19c42285e
  - [Higgsfield AI ships new video features in a day with GPT-6 AstraStartupSep 21, 2026](</index/higgsfield-from-prompt-to-
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [How V7 gives AI agents institutional memoryStartupSep 21, 2026](</index/v7/>)

### https://openai.com/index/wasmer/
- lastmod: `2026-09-22T21:15:43.607Z` → `2026-10-09T05:56:02.265Z`
- Content length: 9203 → 9354 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/wayfair/
- lastmod: `2026-09-22T21:15:44.898Z` → `2026-10-05T19:43:06.024Z`
- Content length: 15699 → 14760 chars (delta: -939)
- Sample new content lines:
  + September 25, 2026
  + > “What’s been most valuable about working with OpenAI is the partnership. It’s not just access to the models. It’s work
  +   * Building a reusable AI system for product attributes
  + On the catalog side, Wayfair validated and corrected attribute data across more than 11 million of its most visible and 
  + [Sophos cuts threat investigation time by 96% with OpenAI DaybreakOct 9, 2026](</index/sophos/>)
- Sample removed content lines:
  - However, Wayfair didn’t simply hand off decisions on correcting product data to the model. “Our objective is to build tr
  - On the catalog side, the company reduced the number of wrong or missing product attribute tags a customer might see—havi
  - Wayfair’s catalog team manages tens of millions of products across nearly a thousand different product classes. Consiste
  - –Graham Ganssle, supplier support operations, Wayfair
  - Building a reusable AI architecture

### https://openai.com/index/what-parameter-golf-taught-us/
- lastmod: `2026-09-25T19:18:42.494Z` → `2026-10-08T12:06:51.396Z`
- Content length: 15123 → 15599 chars (delta: +476)
- Sample new content lines:
  + [#414(opens in a new window)](<https://github.com/openai/parameter-golf/pull/414>)| @signalrush| Used GPTQ-lite to quant
  + [#60(opens in a new window)](<https://github.com/openai/parameter-golf/pull/60>)| @notapplica| Combined prior wins from 
  + [#65(opens in a new window)](<https://github.com/openai/parameter-golf/pull/65>)| @aquariouseworkman| Introduced SmearGa
  + [#1729(opens in a new window)](<https://github.com/openai/parameter-golf/pull/1729>)| @romeerp| Introduced the CaseOps t
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [#1204](<https://github.com/openai/parameter-golf/pull/1204>)| @msisovic| Introduced mini depth recurrence: repeated lay
  - [#1060](<https://github.com/openai/parameter-golf/pull/1060>)| @dexhunter| Built on [#634](<https://github.com/openai/pa

### https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training/
- lastmod: `2026-09-25T19:33:49.040Z` → `2026-10-07T19:26:00.276Z`
- Content length: 11421 → 11553 chars (delta: +132)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Atlassian partnership card — official white SVGs on Neutral 088](https://images.ctfassets.net/kftzwdyauwt9/3fWFo3Rbu3A
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Albertsons | How Albertsons Companies is reimagining retail from the inside out | Cover](https://images.ctfassets.net/
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Advisory Group on Mathematics and Artificial Intelligence — cover](https://images.ctfassets.net/kftzwdyauwt9/7I8A6x8Lf
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/where-the-goblins-came-from/
- lastmod: `2026-09-25T19:10:15.130Z` → `2026-10-07T19:53:48.587Z`
- Content length: 12930 → 13066 chars (delta: +136)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
  + ![Sharing AI progress in mathematics — Cover](https://images.ctfassets.net/kftzwdyauwt9/49FAj0M0Ly8nk84Uu8btWC/9919efdae
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  - ![Research acceleration: The view inside OpenAI > Cover image](https://images.ctfassets.net/kftzwdyauwt9/5kS3OG1Jfdja5xL
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Research acceleration: The view inside OpenAIResearchSep 6, 2026](</index/research-acceleration-view-inside-openai/>)

### https://openai.com/index/whisper/
- lastmod: `2026-09-25T19:18:41.239Z` → `2026-10-09T04:56:32.888Z`
- Content length: 9762 → 9938 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/why-codex-security-doesnt-include-sast/
- lastmod: `2026-09-25T19:16:30.157Z` → `2026-10-09T06:33:31.536Z`
- Content length: 14879 → 14873 chars (delta: -6)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  - ![ChatGPT Ads expands to Southeast Asia and Taiwan — cover](https://images.ctfassets.net/kftzwdyauwt9/2LRApkCOWR8QHAX6Sj
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c

### https://openai.com/index/why-language-models-hallucinate/
- lastmod: `2026-05-22T19:20:55.932Z` → `2026-10-09T05:06:20.129Z`
- Content length: 14500 → 14774 chars (delta: +274)
- Sample new content lines:
  + ![Mental Health Bench art card](https://images.ctfassets.net/kftzwdyauwt9/1GVQAEpVME68kCI7Ol2ApW/abde191546741612492ae27
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Introducing MentalHealthBenchPublicationSep 23, 2026](</index/introducing-mentalhealthbench/>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Pacing model development in an era of cyber-critical capabilitiesCompanyAug 18, 2026](</index/pacing-model-development-
  - ![math-breakthroughs art-card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2zkd5RIOug4FcEj62mdSF4/3ea9e19c0456289c69f0
  - [The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)
  - [Ten advances in mathematics and theoretical computer sciencePublicationAug 1, 2026](</index/ten-advances-in-mathematics

### https://openai.com/index/why-teens-deserve-access-safe-ai/
- lastmod: `2026-09-25T18:57:13.029Z` → `2026-10-08T16:37:01.427Z`
- Content length: 17978 → 17959 chars (delta: -19)
- Sample new content lines:
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6
  - [Our framework for reporting model misalignmentResearchSep 16, 2026](</index/model-misalignment-reporting-framework/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-

### https://openai.com/index/wix/
- lastmod: `2026-09-14T21:27:58.503Z` → `2026-10-06T17:53:48.216Z`
- Content length: 11292 → 11676 chars (delta: +384)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Lowes logo superimposed on an abstract painting with prominent blue brushstrokes.](https://images.ctfassets.net/kftzwd
  + ![San Antonio Spurs logo displayed on a stylized basketball court background with teal, orange, and cream-colored sectio
- Sample removed content lines:
  - ![San Antonio Spurs Cover Image](https://images.ctfassets.net/kftzwdyauwt9/3T53lsDpxxxZkP95bJqGlk/72b9117d5dddf09c24521d
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Lowes > Cover media](https://images.ctfassets.net/kftzwdyauwt9/4X3HwsNsncluAzNEqlXFg3/558227ebd1d4edc388dc325ecbcd75f0
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/work-with-codex-from-anywhere/
- lastmod: `2026-09-22T09:51:50.054Z` → `2026-10-09T05:56:06.130Z`
- Content length: 11248 → 11299 chars (delta: +51)
- Sample new content lines:
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Helping teens learn, plan, and shape the future of AIProductOct 7, 2026](</index/teens-learn-and-plan/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Building advertising for the way people use AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/17prJimIY0iXyzXUbZcA
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba08

### https://openai.com/index/zapier/
- lastmod: `2026-09-22T21:15:33.362Z` → `2026-10-08T22:48:47.807Z`
- Content length: 8946 → 9097 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/index/zendesk/
- lastmod: `2026-09-22T19:25:25.020Z` → `2026-10-08T22:49:06.392Z`
- Content length: 11397 → 11573 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/index/zenken/
- lastmod: `2026-09-22T17:02:15.284Z` → `2026-10-05T19:08:28.857Z`
- Content length: 12718 → 12869 chars (delta: +151)
- Sample new content lines:
  + ![Pollo AI — Cover and hero](https://images.ctfassets.net/kftzwdyauwt9/2d43dWpGGS2PTHZR3ZJtHQ/1b43934d7aae3615455884af04
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [How Oracle turns days of work into minutes with ChatGPT and CodexOct 8, 2026](</index/oracle/>)
  + [Pollo AI turns creative ideas into campaigns with OpenAIStartupOct 8, 2026](</index/pollo-ai/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Better prompt caching for GPT-6ProductSep 22, 2026](</index/better-prompt-caching-for-gpt-6/>)
  - ![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Parallel customer story card image - Option C](https://images.ctfassets.net/kftzwdyauwt9/IE8b4WhSed5XqFQUzyyp7/40124aa

### https://openai.com/leads/small-business/
- lastmod: `2026-08-24T17:53:37.398Z` → `2026-10-08T15:16:35.756Z`
- Content length: 4110 → 4357 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/live/
- lastmod: `2026-09-26T22:26:19.898Z` → `2026-10-08T21:53:06.074Z`
- Content length: 5027 → 5126 chars (delta: +99)
- Sample new content lines:
  + ### [Introducing gpt-realtime and Realtime API updates for production voice agentsAugust 28, 2025Watch the replay](<http
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ### [ This is the new ChatGPT Voice, powered by GPT-LiveJuly 8, 2026Watch the replay(opens in a new window)](<https://ww
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [Introducing ChatGPT Work, powered by Codex and GPT-5.6July 9, 2026Watch the replay(opens in a new window)](<https:/
- Sample removed content lines:
  - ### [Introducing ChatGPT Images 2.0April 21, 2026Watch the replay](<https://www.youtube.com/watch?v=sWkGomJ3TLI>)
  -   * [Codex](</codex/>)
  - ### Join us for the OpenAI DevDay 2026 keynote
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Livestream will begin on Tuesday, September 29 at 10 AM PDT.

### https://openai.com/new-york-times/
- lastmod: `2026-09-14T08:07:23.377Z` → `2026-10-08T21:25:20.778Z`
- Content length: 29699 → 29939 chars (delta: +240)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/news/
- lastmod: `2026-09-25T19:33:50.582Z` → `2026-10-09T08:59:02.261Z`
- Content length: 7013 → 6772 chars (delta: -241)
- Sample new content lines:
  + [Atlassian and OpenAI expand their partnershipCompanyOct 6, 2026](</index/atlassian-partnership/>)
  + [GPT‑6 Sol and GPT‑6 Luna: October 2026 updateSafetyOct 7, 2026(opens in a new window)](<https://deploymentsafety.openai
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Our approach to EU text provenance rulesSafetyOct 5, 2026](</index/eu-text-provenance/>)
  + [Sharing AI progress in mathematicsResearchOct 6, 2026](</index/sharing-ai-progress-in-mathematics/>)
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  - [ChatGPT Ads expands to Southeast Asia and TaiwanProductSep 23, 2026](</index/chatgpt-ads-expands-southeast-asia-taiwan/
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Priorities and principles for effective third party assessmentsSafetySep 22, 2026](</index/priorities-principles-third-
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)

### https://openai.com/news/ai-adoption/
- lastmod: `2026-09-25T18:59:35.767Z` → `2026-10-09T06:58:33.556Z`
- Content length: 6920 → 7096 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/news/applied-ai/
- lastmod: `2026-09-25T18:58:27.052Z` → `2026-10-08T01:12:46.032Z`
- Content length: 5836 → 6012 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/news/company-announcements/
- lastmod: `2026-09-25T19:33:49.750Z` → `2026-10-09T08:57:49.230Z`
- Content length: 9274 → 6427 chars (delta: -2847)
- Sample new content lines:
  + ![Introducing dots — cover art card \(square\)](https://images.ctfassets.net/kftzwdyauwt9/2TCcE1IdEPpWT2vaC3PDWu/e78bceb
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Intelligent-UI Art-Card 16x9](https://images.ctfassets.net/kftzwdyauwt9/5frqtUAWccstAbVrCFraH6/5ae9b6bfbc3f3dff8001ed2
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [DevDay 2026 RecapCompany28 min read](</index/devday-2026-recap/>)
- Sample removed content lines:
  - ![Expanding OpenAI Academy with new learning paths — cover](https://images.ctfassets.net/kftzwdyauwt9/45fB7Wzg6PiQPzz8V4
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Two years of OpenAI AcademyCompanySep 23, 2026](</index/two-years-of-openai-academy/>)
  - Load more
  - [Expanding OpenAI Academy with new learning pathsCompanySep 21, 2026](</index/expanding-openai-academy-with-new-learning

### https://openai.com/news/engineering/
- lastmod: `2026-09-25T19:33:49.030Z` → `2026-10-09T06:21:01.737Z`
- Content length: 6788 → 6964 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/news/global-affairs/
- lastmod: `2026-09-25T19:33:48.988Z` → `2026-10-09T06:21:02.027Z`
- Content length: 7284 → 7424 chars (delta: +140)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Helping small businesses put AI to work — card](https://images.ctfassets.net/kftzwdyauwt9/7DQxQ61fzFDJjB09z1T6Xx/41d00
  + [Helping small businesses put AI to workGlobal AffairsSep 30, 2026](</index/helping-small-businesses-put-ai-to-work/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - [Supporting independent journalism in UkraineGlobal AffairsSep 7, 2026](</index/supporting-independent-journalism-in-ukr
  -   * [GPT-6](</index/gpt-6-astra/>)
  - ![Supporting independent journalism in Ukraine — card image](https://images.ctfassets.net/kftzwdyauwt9/3wATLIxaR9ch8uwHb
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/news/intelligence-age/
- lastmod: `2026-09-25T18:59:37.292Z` → `2026-10-05T19:22:35.347Z`
- Content length: 4219 → 4715 chars (delta: +496)
- Sample new content lines:
  + [The eternal complementIntelligence AgeOct 1, 2026](</index/the-eternal-complement/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [Codex](<https://chatgpt.com/codex/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/news/product-releases/
- lastmod: `2026-09-25T19:33:48.703Z` → `2026-10-09T06:33:32.669Z`
- Content length: 6603 → 6533 chars (delta: -70)
- Sample new content lines:
  + ![A model guide for the GPT-6 family — Card image](https://images.ctfassets.net/kftzwdyauwt9/4I32Z0klAF95wPuspoHaxb/7388
  + [Introducing dotsProductSep 29, 2026](</index/introducing-dots/>)
  + ![Introducing dots — cover art card \(square\)](https://images.ctfassets.net/kftzwdyauwt9/2TCcE1IdEPpWT2vaC3PDWu/e78bceb
  + ![Helping teens learn, plan, and shape the future of AI — Cover](https://images.ctfassets.net/kftzwdyauwt9/3Gg3FDcLbArW4
  + [Building advertising for the way people use AIProductOct 5, 2026](</index/new-chatgpt-ads-format-and-measurement/>)
- Sample removed content lines:
  - [Build more natural voice experiences with GPT‑Live‑1 in the APIProductSep 10, 2026](</index/introducing-gpt-live-1-in-t
  - [Introducing the Agents APIProductSep 10, 2026](</index/introducing-the-agents-api/>)
  - [Now everyone can put data to workProductSep 10, 2026](</index/put-data-to-work/>)
  -   * [Codex](</codex/>)
  - [Introducing ChatGPT for Financial ServicesProductSep 10, 2026](</index/introducing-chatgpt-financial-services/>)

### https://openai.com/news/research/
- lastmod: `2026-09-25T18:59:55.019Z` → `2026-10-09T05:56:09.252Z`
- Content length: 6289 → 6567 chars (delta: +278)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [GPT‑6 Sol and GPT‑6 Luna: October 2026 updateSafetyOct 7, 2026(opens in a new window)](<https://deploymentsafety.openai
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![oai ironclad cua 1x1](https://images.ctfassets.net/kftzwdyauwt9/23y88t0gUd7FSqVFa9n1uq/6d227695a77e7a2cf3e6607bc69e1cf
- Sample removed content lines:
  - ![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9ad
  - ![Research acceleration: The view inside OpenAI > Cover image](https://images.ctfassets.net/kftzwdyauwt9/5kS3OG1Jfdja5xL
  -   * [Codex](</codex/>)
  - [Pacing model development in an era of cyber-critical capabilitiesCompanyAug 18, 2026](</index/pacing-model-development-
  - ![GPT-6 Astra System Card](https://images.ctfassets.net/kftzwdyauwt9/4EPFfixCR8upYpL3fOmjMo/2f995b1b7e03a6938bf5b654fb1d

### https://openai.com/news/safety-alignment/
- lastmod: `2026-09-25T19:33:49.025Z` → `2026-10-03T13:14:06.276Z`
- Content length: 6782 → 7240 chars (delta: +458)
- Sample new content lines:
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  + [Disrupting AI-enabled “false front” operationsSafetyOct 8, 2026](</index/disrupting-ai-enabled-false-front-operations/>
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + ![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/a
  + [GPT‑6 Sol and GPT‑6 Luna: October 2026 updateSafetyOct 7, 2026(opens in a new window)](<https://deploymentsafety.openai
- Sample removed content lines:
  - [Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)
  - [Funding grants for new research into AI and teen developmentSafetySep 8, 2026](</index/teen-development-research-grants
  - ![Research acceleration: The view inside OpenAI > Cover image](https://images.ctfassets.net/kftzwdyauwt9/5kS3OG1Jfdja5xL
  -   * [Codex](</codex/>)
  - ![GPT-6 Astra System Card](https://images.ctfassets.net/kftzwdyauwt9/4EPFfixCR8upYpL3fOmjMo/2f995b1b7e03a6938bf5b654fb1d

### https://openai.com/news/security/
- lastmod: `2026-09-25T19:33:49.033Z` → `2026-10-03T13:14:05.331Z`
- Content length: 6446 → 6680 chars (delta: +234)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + [Disrupting a coordinated model-distillation campaignSecuritySep 30, 2026](</index/disrupting-a-coordinated-model-distil
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![Disrupting a coordinated model-distillation campaign — cover](https://images.ctfassets.net/kftzwdyauwt9/1n8Wz1YN3veGi9
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![Hugging Face Security Incident 1x1](https://images.ctfassets.net/kftzwdyauwt9/1H0bdkoSFFcqNTx4DSNpal/56f4b7575c012f069
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [OpenAI and Hugging Face address security incidentSecurityJul 21, 2026](</index/hugging-face-model-evaluation-security-i
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/o1/
- lastmod: `2026-09-25T19:18:38.674Z` → `2026-10-08T12:06:45.343Z`
- Content length: 4271 → 4857 chars (delta: +586)
- Sample new content lines:
  + [Try ChatGPT(opens in a new window)](<https://chatgpt.com/>)[View current API models(opens in a new window)](<https://de
  + [View current API models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + For the current experience:
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Try it in ChatGPT Plus (opens in a new window)](<https://chatgpt.com/?model=o1>)[Try it in the API(opens in a new windo
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/open-models/
- lastmod: `2026-09-15T23:28:38.728Z` → `2026-10-09T07:40:39.615Z`
- Content length: 7787 → 8183 chars (delta: +396)
- Sample new content lines:
  + ### [Learn about the OpenAI harmony response formatLearn more(opens in a new window)](<https://cookbook.openai.com/artic
  + ### [How to run gpt-oss-20b on Google ColabLearn more(opens in a new window)](<https://cookbook.openai.com/articles/gpt-
  + ### [Find more guides about gpt-ossLearn more(opens in a new window)](<https://cookbook.openai.com/topic/gpt-oss>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
- Sample removed content lines:
  - ### [Verifying gpt-oss implementationsLearn more](<https://cookbook.openai.com/articles/gpt-oss/verifying-implementation
  - ### [How to run gpt-oss locally with OllamaLearn more](<https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama>
  -   * [Codex](</codex/>)
  - ### [Find more guides about gpt-ossLearn more](<https://cookbook.openai.com/topic/gpt-oss>)
  - ### [How to run gpt-oss-20b on Google ColabLearn more](<https://cookbook.openai.com/articles/gpt-oss/run-colab>)

### https://openai.com/our-structure/
- lastmod: `2026-09-23T15:48:34.168Z` → `2026-10-08T16:30:47.655Z`
- Content length: 7888 → 8064 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/podcast/
- lastmod: `2026-08-14T04:29:51.155Z` → `2026-10-09T07:57:19.262Z`
- Content length: 3632 → 3879 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/
- lastmod: `2026-09-13T06:47:18.775Z` → `2026-10-09T05:47:54.997Z`
- Content length: 7956 → 8201 chars (delta: +245)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/ad-credit-terms/
- lastmod: `2026-07-31T15:49:26.689Z` → `2026-10-07T08:47:07.205Z`
- Content length: 6723 → 6970 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/ad-policies/
- lastmod: `2026-09-17T08:18:21.189Z` → `2026-10-08T20:22:42.381Z`
- Content length: 25498 → 25710 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/ad-tools-dpa/
- lastmod: `2026-08-25T00:37:04.614Z` → `2026-10-09T00:13:25.689Z`
- Content length: 15178 → 15444 chars (delta: +266)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/ad-tools-subprocessors/
- lastmod: `2026-08-21T06:51:24.220Z` → `2026-10-08T14:02:01.024Z`
- Content length: 4961 → 5208 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/ad-tools-terms/
- lastmod: `2026-08-27T22:57:31.891Z` → `2026-10-08T21:02:00.016Z`
- Content length: 16585 → 16841 chars (delta: +256)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/advertising-terms/
- lastmod: `2026-08-31T17:28:01.792Z` → `2026-10-09T05:56:16.286Z`
- Content length: 47438 → 47739 chars (delta: +301)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/chatgpt-sites-terms/
- lastmod: `2026-08-13T23:45:39.785Z` → `2026-10-08T21:25:03.159Z`
- Content length: 16914 → 17183 chars (delta: +269)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/commerce-policies/
- lastmod: `2026-06-29T04:12:44.738Z` → `2026-10-08T09:20:01.331Z`
- Content length: 10297 → 10508 chars (delta: +211)
- Sample new content lines:
  + These standards apply to product listings and merchant participation in OpenAI’s shopping experiences. Merchants must al
  + OpenAI’s shopping experiences help people discover products and connect with merchants. These policies establish eligibi
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - Merchants must provide truthful listings and imagery and address customer concerns through the partner platform’s suppor
  - OpenAI reserves the right to remove products or sellers, and to restrict commerce features, for any reason.
  -   * [Codex](</codex/>)
  - This policy defines categories of products and services that are not allowed to be sold, promoted for sale, or facilitat
  - Updated: June 24, 2026

### https://openai.com/policies/communications-privacy-policy/
- lastmod: `2026-09-11T00:00:36.209Z` → `2026-10-08T21:08:40.760Z`
- Content length: 29087 → 29349 chars (delta: +262)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/cookie-policy/
- lastmod: `2026-09-17T08:13:04.475Z` → `2026-10-07T18:01:28.951Z`
- Content length: 26459 → 29295 chars (delta: +2836)
- Sample new content lines:
  + [Bing(opens in a new window)](<https://learn.microsoft.com/en-us/answers/questions/2289901/purposes-of-bing-cookies>)| _
  + [Swoogo⁠⁠(opens in a new window)](<https://swoogo.events/legal/cookies/>)| PHPSESSID| Session| Service functionality| ev
  + [Google(opens in a new window)](<https://policies.google.com/technologies/partner-sites>)⁠⁠| _glc_dc| 90 days| Marketing
  + [Google(opens in a new window)](<https://policies.google.com/technologies/partner-sites/>)| g_state| 6 months| Service f
  + [Snapchat(opens in a new window)](<https://www.snap.com/cookie-policy>)| u_scsid_r| Session| Marketing measurement| chat
- Sample removed content lines:
  - [Cloudflare⁠⁠](<https://www.cloudflare.com/privacypolicy/>)| __cf_bm| 30 min| Security| auth.openai.com  
  - [Cloudflare⁠⁠](<https://www.cloudflare.com/privacypolicy/>)| CF_Authorization| 1 month| Security| chatgpt.com  
  - [Cloudflare⁠⁠](<https://www.cloudflare.com/privacypolicy/>)| _cfuvid| Session| Security| openai.com  
  - [Google](<https://policies.google.com/technologies/partner-sites>)⁠⁠⁠| gclid| 24 hours| Marketing measurement| openai.co
  - [OpenAI](<https://openai.com/policies/privacy-policy/>)| oai-did| 1 year| Service functionality| chatgpt.com  

### https://openai.com/policies/coordinated-vulnerability-disclosure-policy/
- lastmod: `2026-07-31T11:31:15.902Z` → `2026-10-09T04:58:10.336Z`
- Content length: 5351 → 5598 chars (delta: +247)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/developer-apps-terms/
- lastmod: `2026-09-10T17:43:51.220Z` → `2026-10-08T22:59:23.752Z`
- Content length: 28458 → 29042 chars (delta: +584)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * 1.1 _Access_. We may: (a) access and use your API to enable your App within the Services; and (b) allow end users of
  + Updated: September 28, 2026
- Sample removed content lines:
  -   * 1.2 _App Requests_. The Services may send a request to your API (“App Request”) on behalf of a User. You may only co
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * 1.1 _Access_. We may: (a) access and use your API to enable your App within the Services; and (b) allow end users of
  - Updated: July 9, 2026

### https://openai.com/policies/eu-services-privacy-policy/
- lastmod: `2026-08-25T19:20:03.714Z` → `2026-10-09T02:39:08.400Z`
- Content length: 41337 → 41757 chars (delta: +420)
- Sample new content lines:
  +   * Suggesting conversation topics based on subjects you’ve previously discussed or saved [in your Memory(opens in a new
  +   * If training is enabled (see your data controls [here(opens in a new window)](<https://help.openai.com/articles/77308
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * If [Memory(opens in a new window)](<https://help.openai.com/articles/8590148-memory-faq>) is on, we may remember det
  +   * [Plugins](</business/plugins/>)
- Sample removed content lines:
  -   * Suggesting conversation topics based on subjects you’ve previously discussed or saved [in your Memory](<https://help
  -   * If training is enabled (see your data controls [here](<https://help.openai.com/articles/7730893-data-controls-faq>))
  -   * [Codex](</codex/>)
  -   * Using information you add in [Custom Instructions](<https://help.openai.com/articles/8096356-chatgpt-custom-instruct
  -   * If [Memory](<https://help.openai.com/articles/8590148-memory-faq>) is on, we may remember details you’ve shared acro

### https://openai.com/policies/feb-2024-data-processing-addendum/
- lastmod: `2026-08-14T00:24:16.841Z` → `2026-10-08T20:08:04.082Z`
- Content length: 36399 → 36700 chars (delta: +301)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/kr-privacy-policy/
- lastmod: `2026-09-10T23:59:53.544Z` → `2026-10-09T08:41:49.671Z`
- Content length: 29153 → 29416 chars (delta: +263)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/may-2025-business-terms/
- lastmod: `2026-08-18T17:37:48.917Z` → `2026-10-09T05:29:15.072Z`
- Content length: 50027 → 50351 chars (delta: +324)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/merchant-feed-terms-of-service/
- lastmod: `2026-06-22T21:57:40.791Z` → `2026-10-08T19:30:49.657Z`
- Content length: 21813 → 22096 chars (delta: +283)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/privacy-policy/
- lastmod: `2026-09-04T14:03:36.485Z` → `2026-10-09T04:52:51.146Z`
- Content length: 37347 → 37095 chars (delta: -252)
- Sample new content lines:
  +   * For Free and Go users, you can use the advertising controls in your account settings to control what data we use to 
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * You can easily[ _choose whether your Content can be used to improve and train our models_ ⁠(opens in a new window)](
  +   * _Other Users and Third Parties You Interact or Share Information With_ : Certain Services allow you to interact or s
  +   * **Information we delete automatically:** In some cases, Personal Data will be deleted automatically. For example,[ _
- Sample removed content lines:
  -   * _Log Data_ : We collect information that your browser or device automatically sends when you use our Services. Log d
  -   * You can export your ChatGPT history and data in your account’s data controls.
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * _Other Users and Third Parties You Interact or Share Information With_ : Certain Services allow you to interact or s
  -   * **Information we retain until you delete it:** Some of our Services allow you to delete Personal Data stored in your

### https://openai.com/policies/row-terms-of-use/
- lastmod: `2026-01-01T18:03:37.711Z` → `2026-10-09T05:43:03.477Z`
- Content length: 25140 → 25412 chars (delta: +272)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/service-terms/
- lastmod: `2026-09-21T16:43:46.492Z` → `2026-10-09T06:30:11.044Z`
- Content length: 19185 → 20874 chars (delta: +1689)
- Sample new content lines:
  + (b)**Oversight.** You are responsible for providing oversight appropriate to the task and its potential consequences. Th
  + If you are a user connecting your account to a service using SIWC, you agree to share information necessary to authentic
  + ## 15\. Sign in with ChatGPT
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - Updated: September 21, 2026
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ChatGPT Sites is a feature that enables users to create, publish, and maintain websites or web applications. The use of 

### https://openai.com/policies/services-agreement/
- lastmod: `2026-09-25T13:58:18.707Z` → `2026-10-08T21:24:50.006Z`
- Content length: 49428 → 49604 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/services-communications-privacy-policy/
- lastmod: `2026-07-30T02:23:12.410Z` → `2026-10-08T20:44:20.878Z`
- Content length: 28919 → 29218 chars (delta: +299)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/terms-of-use/
- lastmod: `2026-09-10T11:45:31.937Z` → `2026-10-04T06:17:13.158Z`
- Content length: 25175 → 25412 chars (delta: +237)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/policies/us-privacy-policy/
- lastmod: `2026-09-10T23:48:43.430Z` → `2026-10-09T08:43:47.653Z`
- Content length: 36782 → 37095 chars (delta: +313)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * Improve and develop our Services and conduct research, including using your Content to train our models (subject to 
  +   * For Free and Go users, subject to your controls, to personalize the ads you see on our Services and measure the effe
- Sample removed content lines:
  -   * For Free and Go users, subject to your controls, to personalize the ads you see on our Services and measure the effe
  -   * [Codex](</codex/>)
  -   * Improve and develop our Services and conduct research, including using your Content to train our models (subject to 
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/products/release-notes/
- lastmod: `2026-09-27T19:57:04.513Z` → `2026-10-09T09:09:09.568Z`
- Content length: 8904 → 8457 chars (delta: -447)
- Sample new content lines:
  +   * Fixed task lists remaining empty after connecting.
  + New features
  +   * Redesigned the approval picker with clearer permission choices.
  + [View source(opens in a new window)](<https://developers.openai.com/api/docs/models/chat-latest>)[Platform docs(opens in
  +   * Find plugins from a single Plugins entry in the composer’s plus menu.
- Sample removed content lines:
  - Sep 23, 2026
  - We’re introducing GPT‑6 Sol and GPT‑6 Luna in ChatGPT Work and Codex. These models are separate from the models availabl
  -   * New iPad split view keeps your task list beside the open task in landscape.
  -   * [GPT-6](</index/gpt-6-astra/>)
  - You can now create interactive flashcards in ChatGPT. Ask for flashcards on a topic you want to learn, or upload your no

### https://openai.com/research/
- lastmod: `2026-09-27T22:57:15.300Z` → `2026-09-29T18:13:44.153Z`
- Content length: 7148 → 7333 chars (delta: +185)
- Sample new content lines:
  + [Complex coding and professional work at a lower costReleaseSep 29, 202612 min read](</index/introducing-gpt-6-1-sol/>)
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ![GPT-6-1-Sol_Blog 1x1](https://images.ctfassets.net/kftzwdyauwt9/7reVkD9GZT81EppPxXgW4D/44c5d09530a17bf45d153b86760ee30
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ![Hero Art Card SEO 1x1](https://images.ctfassets.net/kftzwdyauwt9/cut4wyUCuBENXfd5CSI7Z/d934ffb49d8b39abea0bc33bb1a5b91
  -   * [Codex](</codex/>)
  - [A new class of intelligence for real workReleaseApr 23, 202612 min read](</index/introducing-gpt-5-5/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/research/index/
- lastmod: `2026-09-25T19:21:42.614Z` → `2026-10-09T07:33:44.809Z`
- Content length: 5989 → 6031 chars (delta: +42)
- Sample new content lines:
  + [GPT-6 and Intelligent UI for everyoneGPT‑6 is rolling out globally in ChatGPT with Intelligent UI, delivering faster re
  + Oct 7, 2026
  + Oct 6, 2026
  + [Advancing computer use with IroncladLearn how OpenAI and Ironclad are training and evaluating AI agents on complex cont
  + [Introducing GPT-6.1 SolMeet GPT-6.1 Sol: near-Astra intelligence for coding, computer use, and professional work at one
- Sample removed content lines:
  - Sep 6, 2026
  -   * [Codex](</codex/>)
  - Sep 3, 2026
  - [An OpenAI model proposes a solution to the Navier–Stokes problemWe’re sharing an AI-generated solution to the Navier–St
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/research/index/conclusion/
- lastmod: `2026-09-25T18:59:21.275Z` → `2026-09-28T16:13:13.379Z`
- Content length: 6956 → 7132 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/research/index/milestone/
- lastmod: `2026-09-25T19:36:02.193Z` → `2026-09-28T16:12:56.878Z`
- Content length: 6011 → 6187 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/research/index/publication/
- lastmod: `2026-09-25T19:00:13.824Z` → `2026-10-03T12:34:25.177Z`
- Content length: 6102 → 6066 chars (delta: -36)
- Sample new content lines:
  + Oct 7, 2026
  + Oct 6, 2026
  + [Advancing computer use with IroncladLearn how OpenAI and Ironclad are training and evaluating AI agents on complex cont
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  - [Ten advances in mathematics and theoretical computer scienceOpenAI shares new results on long-standing open problems in
  - [Scientific computing in the age of agentic AIA new field report shows how scientists use AI coding agents to modernize 
  -   * [Codex](</codex/>)
  - Aug 1, 2026
  -   * [GPT-6](</index/gpt-6-astra/>)

### https://openai.com/research/index/release/
- lastmod: `2026-09-25T18:58:51.740Z` → `2026-10-09T05:56:10.252Z`
- Content length: 5911 → 6051 chars (delta: +140)
- Sample new content lines:
  + [GPT-6 and Intelligent UI for everyoneGPT‑6 is rolling out globally in ChatGPT with Intelligent UI, delivering faster re
  + Oct 7, 2026
  + [Introducing GPT-6.1 SolMeet GPT-6.1 Sol: near-Astra intelligence for coding, computer use, and professional work at one
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  + Sep 29, 2026
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Jun 4, 2026
  - [Dreaming: Better memory for a more helpful ChatGPTChatGPT introduces a new memory system to better remember preferences
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/research/verify/
- lastmod: `2026-09-25T09:56:40.828Z` → `2026-10-09T04:47:03.599Z`
- Content length: 8719 → 9158 chars (delta: +439)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [OpenAI.com/verify](</research/verify/>) does not currently support text verification. Organizations with a qualifying u
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  + ### Can I verify text?
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/residency/
- lastmod: `2026-09-22T22:05:52.611Z` → `2026-10-09T04:17:53.854Z`
- Content length: 10407 → 10583 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/safety/
- lastmod: `2026-09-15T23:24:23.080Z` → `2026-10-09T08:29:08.861Z`
- Content length: 8045 → 8257 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/science/
- lastmod: `2026-09-27T18:51:23.484Z` → `2026-10-08T14:55:14.524Z`
- Content length: 11655 → 12047 chars (delta: +392)
- Sample new content lines:
  + ![A luminous numeral 6 formed from stars against a dark background.](https://images.ctfassets.net/kftzwdyauwt9/fXFJSIYQZ
  + GPT‑6 Astra combines advanced scientific reasoning with state-of-the-art coding and computer use to help researchers tac
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - Explore GPT‑6, OpenAI’s latest model.
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  - Explore GPT-6, OpenAI’s latest model.
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/security-and-privacy/
- lastmod: `2026-09-15T23:12:40.817Z` → `2026-10-01T16:25:52.423Z`
- Content length: 10121 → 10324 chars (delta: +203)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [ChatGPT privacy settings](</consumer-privacy/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - [ChatGPT Privacy Settings | OpenAI](</consumer-privacy/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/signals/
- lastmod: `2026-09-25T23:09:57.163Z` → `2026-10-02T01:10:54.956Z`
- Content length: 13981 → 14272 chars (delta: +291)
- Sample new content lines:
  + ### [Work at the Frontier: How workers are unlocking new ways of workingSeptember 2026 | An analysis of how workers use 
  + ### [The shift to agentic AI: evidence from CodexJune 2026 | An analysis of Codex usage to understand how agentic AI is 
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + ### [The AI jobs transition framework for the EUJune 2026 | A map of near-term job impacts of AI in the EU labor market.
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ### [How organizations use AI: Evidence from ChatGPTAugust 2026 | Research examining how ChatGPT Enterprise has spread w
  - ### [The shift to agentic AI: evidence from CodexJune 2026 | An analysis of Codex usage to understand how agentic AI is 
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/signals/data-download/
- lastmod: `2026-09-15T04:37:05.758Z` → `2026-10-08T21:35:15.531Z`
- Content length: 6699 → 6911 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/signals/data/
- lastmod: `2026-09-15T04:37:05.613Z` → `2026-10-08T21:35:16.903Z`
- Content length: 10433 → 10645 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/signals/enterprise-data/
- lastmod: `2026-09-21T20:28:38.735Z` → `2026-10-09T00:42:37.488Z`
- Content length: 23124 → 23300 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/signals/research/
- lastmod: `2026-09-15T04:37:07.853Z` → `2026-10-08T21:35:15.691Z`
- Content length: 7687 → 8014 chars (delta: +327)
- Sample new content lines:
  + ### [ChatGPT and the price of workMarch 2026 | How Americans use ChatGPT to help them close the wage information gap.Lea
  + ### [The shift to agentic AI: evidence from CodexJune 2026 | An analysis of Codex usage to understand how agentic AI is 
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ### [The shift to agentic AI: evidence from CodexJune 2026 | An analysis of Codex usage to understand how agentic AI is 
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ### [ChatGPT and the price of workMarch 2026 | How Americans use ChatGPT to help them close the wage information gap.Lea

### https://openai.com/solutions/
- lastmod: `2026-07-29T20:25:00.769Z` → `2026-10-08T19:11:09.765Z`
- Content length: 10672 → 10915 chars (delta: +243)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  + [Life sciencesConnect science to patient impact.](</rosalind/>)
- Sample removed content lines:
  - [Life sciencesConnect science to patient impact.](</gpt-rosalind/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/solutions/industries/financial-services/
- lastmod: `2026-09-10T17:43:01.380Z` → `2026-10-08T20:34:46.825Z`
- Content length: 11259 → 11471 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/solutions/industries/government/
- lastmod: `2026-09-16T16:12:16.660Z` → `2026-10-08T19:30:06.195Z`
- Content length: 15212 → 15424 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/solutions/industries/law/
- lastmod: `2026-09-24T21:49:58.328Z` → `2026-10-02T23:03:34.211Z`
- Content length: 12939 → 13115 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/solutions/use-case/agents/
- lastmod: `2026-09-07T16:35:45.449Z` → `2026-10-09T04:55:37.003Z`
- Content length: 11071 → 11329 chars (delta: +258)
- Sample new content lines:
  + ### [OpenAI AcademyLearn how to build, test, and deploy AI-powered applications step by step.Learn more(opens in a new w
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ### [OpenAI AcademyLearn how to build, test, and deploy AI-powered applications step by step.Learn more](<https://academ
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ### [Developer hubDocs, examples, and SDKs for coding with OpenAI models and APIs.Learn more](<https://developers.openai

### https://openai.com/solutions/use-case/coding/
- lastmod: `2026-09-07T16:35:44.230Z` → `2026-10-08T22:53:07.987Z`
- Content length: 12264 → 12545 chars (delta: +281)
- Sample new content lines:
  + ### [OpenAI Academy Learn how to build, test, and deploy AI-powered applications step by step.Learn more(opens in a new 
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Explore apps](</business/plugins/>)[Connect with MCP(opens in a new window)](<https://platform.openai.com/docs/mcp>)
- Sample removed content lines:
  - [Explore apps](</business/plugins/>)[Connect with MCP](<https://platform.openai.com/docs/mcp>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ### [OpenAI Academy Learn how to build, test, and deploy AI-powered applications step by step.Learn more](<https://acade

### https://openai.com/solutions/use-case/content-creation/
- lastmod: `2026-09-07T16:33:26.142Z` → `2026-10-09T02:12:18.958Z`
- Content length: 11741 → 11999 chars (delta: +258)
- Sample new content lines:
  + ### [OpenAI Academy Learn how to build and scale creative workflows with AI. Learn more(opens in a new window)](<https:/
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ### [OpenAI Academy Learn how to build and scale creative workflows with AI. Learn more](<https://academy.openai.com>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ### [Developer hubDocs, examples, and SDKs for coding with OpenAI models and APIs.Learn more](<https://developers.openai

### https://openai.com/solutions/use-case/data-analysis/
- lastmod: `2026-09-07T16:34:49.881Z` → `2026-10-08T23:13:16.122Z`
- Content length: 10378 → 10636 chars (delta: +258)
- Sample new content lines:
  + ### [OpenAI AcademyLearn how to build, test, and deploy AI-powered applications step by step.Learn more(opens in a new w
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  - ### [OpenAI AcademyLearn how to build, test, and deploy AI-powered applications step by step.Learn more](<https://academ
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)
  - ### [Developer hubDocs, examples, and SDKs for coding with OpenAI models and APIs.Learn more](<https://developers.openai

### https://openai.com/solutions/use-case/research/
- lastmod: `2026-09-07T16:35:01.305Z` → `2026-10-09T01:56:40.987Z`
- Content length: 10882 → 11186 chars (delta: +304)
- Sample new content lines:
  + ### [OpenAI Academy Learn how to build, test, and deploy AI-powered applications step by step.Learn more(opens in a new 
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  + [Explore apps](</business/plugins/>)[Connect with MCP(opens in a new window)](<https://platform.openai.com/docs/mcp>)
- Sample removed content lines:
  - [Use deep research](<https://chatgpt.com/?hints=research>)
  - [Explore apps](</business/plugins/>)[Connect with MCP](<https://platform.openai.com/docs/mcp>)
  -   * [Codex](</codex/>)
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/stories/
- lastmod: `2026-09-25T18:59:30.946Z` → `2026-10-08T16:37:04.359Z`
- Content length: 9989 → 10156 chars (delta: +167)
- Sample new content lines:
  + ![White R&D lettering over a purple and orange thermal image of a racing helmet.](https://images.ctfassets.net/kftzwdyau
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [Codex](<https://chatgpt.com/codex/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI-branded Chip Ganassi Racing car on a track with large R&D text over a blurred grandstand.](https://images.ctfas
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Chip Ganassi Racing × OpenAIAPIMay 28, 2026](</index/chip-ganassi-racing/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/stories/api/
- lastmod: `2026-09-25T18:57:30.148Z` → `2026-10-08T16:37:04.830Z`
- Content length: 5205 → 5372 chars (delta: +167)
- Sample new content lines:
  + ![White R&D lettering over a purple and orange thermal image of a racing helmet.](https://images.ctfassets.net/kftzwdyau
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [Codex](<https://chatgpt.com/codex/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  - ![OpenAI-branded Chip Ganassi Racing car on a track with large R&D text over a blurred grandstand.](https://images.ctfas
  -   * [GPT-6](</index/gpt-6-astra/>)
  - [Chip Ganassi Racing × OpenAIAPIMay 28, 2026](</index/chip-ganassi-racing/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/stories/chatgpt/
- lastmod: `2026-09-25T18:59:28.589Z` → `2026-10-08T16:37:04.241Z`
- Content length: 6914 → 7090 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/stories/sora/
- lastmod: `2026-09-25T18:59:27.471Z` → `2026-10-08T09:14:40.655Z`
- Content length: 4074 → 4250 chars (delta: +176)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  +   * [Codex](<https://chatgpt.com/codex/>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/student-collective/
- lastmod: `2026-09-18T09:31:06.326Z` → `2026-10-09T09:16:49.295Z`
- Content length: 18063 → 18275 chars (delta: +212)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/transparency-and-content-moderation/
- lastmod: `2026-08-18T21:41:20.567Z` → `2026-10-08T20:23:15.901Z`
- Content length: 10464 → 10730 chars (delta: +266)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

### https://openai.com/webmcp-challenge/
- lastmod: `2026-09-10T15:21:28.245Z` → `2026-10-08T23:48:18.685Z`
- Content length: 12004 → 12221 chars (delta: +217)
- Sample new content lines:
  +   * [OpenAI Status(opens in a new window)](<https://status.openai.com>)
  +   * [Plugins](</business/plugins/>)
  +   * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  +   * [GPT-6 Astra](</index/gpt-6-astra/>)
  +   * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
- Sample removed content lines:
  -   * [GPT-6](</index/gpt-6-astra/>)
  -   * [Codex](</codex/>)
  -   * [GPT-5.4](</index/introducing-gpt-5-4/>)

## New Pages

- `https://openai.com/business/learn/board-guide-cybersecurity-ai/`
  - Title: **Download the board guide to cybersecurity and AI**
  - lastmod: 2026-10-09T07:16:10.956Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/business/marketplace/`
  - Title: **OpenAI Marketplace**
  - lastmod: 2026-10-08T01:21:48.461Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/business/partners/megazonecloud/`
  - Title: **MegazoneCloud**
  - lastmod: 2026-10-08T17:15:16.589Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/business/plugins/alpaca/`
  - Title: **Alpaca**
  - lastmod: 2026-10-08T18:11:09.298Z
  - Sub-sitemap: https://openai.com/sitemap.xml/plugins-finance/
- `https://openai.com/business/plugins/sandstone/`
  - Title: **Sandstone**
  - lastmod: 2026-10-08T18:00:25.419Z
  - Sub-sitemap: https://openai.com/sitemap.xml/plugins-legal/
- `https://openai.com/business/plugins/spacefast/`
  - Title: **Spacefast**
  - lastmod: 2026-10-08T17:55:23.569Z
  - Sub-sitemap: https://openai.com/sitemap.xml/plugins-engineering-it/
- `https://openai.com/codex-originals/`
  - Title: **Codex Originals![](https://images.ctfassets.net/kftzwdyauwt9/48W0447nPfDU4Qoln834Kl/ca790817ea92bd7b7415586de64cc1f9/codex-originals.svg)**
  - lastmod: 2026-10-01T18:38:17.113Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/devday/2026/`
  - lastmod: 2026-10-08T14:03:11.988Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/form/codex-originals/`
  - Title: **Are you a Codex Original?**
  - lastmod: 2026-10-09T09:16:44.107Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/form/computer-use-research-collaboration/`
  - Title: **Computer-use research collaboration**
  - lastmod: 2026-10-08T15:16:35.763Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/form/private-intelligence-interest/`
  - Title: **Register your interest in Private Intelligence**
  - lastmod: 2026-10-01T03:03:00.758Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/form/sign-in-with-chatgpt-interest/`
  - Title: **Sign in with ChatGPT interest form**
  - lastmod: 2026-10-07T00:50:43.033Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/advancing-computer-use-with-ironclad/`
  - Title: **Advancing computer use with Ironclad**
  - lastmod: 2026-10-09T09:03:12.821Z
  - Sub-sitemap: https://openai.com/sitemap.xml/publication/
- `https://openai.com/index/albertsons-reimagining-retail/`
  - Title: **How Albertsons Companies is reimagining retail from the inside out**
  - lastmod: 2026-10-09T06:21:03.743Z
  - Sub-sitemap: https://openai.com/sitemap.xml/company/
- `https://openai.com/index/atlassian-partnership/`
  - Title: **Atlassian and OpenAI expand partnership to turn enterprise knowledge into action**
  - lastmod: 2026-10-09T06:41:46.582Z
  - Sub-sitemap: https://openai.com/sitemap.xml/company/
- `https://openai.com/index/basis-tax-workbook-with-astra/`
  - Title: **Basis completes a tax workbook 2x faster with GPT‑6 Astra**
  - lastmod: 2026-10-07T23:30:37.170Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/chatham-financial/`
  - Title: **Chatham scales its capital markets expertise with OpenAI**
  - lastmod: 2026-10-09T05:56:13.710Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/devday-2026-recap/`
  - Title: **DevDay 2026 Recap**
  - lastmod: 2026-10-09T06:33:29.840Z
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/`
  - Title: **Disrupting a coordinated model-distillation campaign**
  - lastmod: 2026-10-09T07:57:04.619Z
  - Sub-sitemap: https://openai.com/sitemap.xml/security/
- `https://openai.com/index/disrupting-ai-enabled-false-front-operations/`
  - Title: **Disrupting AI-enabled “false front” operations**
  - lastmod: 2026-10-09T06:57:12.389Z
  - Sub-sitemap: https://openai.com/sitemap.xml/safety/
- `https://openai.com/index/eu-text-provenance/`
  - Title: **Our approach to EU text provenance rules**
  - lastmod: 2026-10-09T06:21:16.670Z
  - Sub-sitemap: https://openai.com/sitemap.xml/safety/
- `https://openai.com/index/gpt-6-for-everyone/`
  - Title: **GPT‑6 and Intelligent UI for everyone**
  - lastmod: 2026-10-09T09:16:18.080Z
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/helping-small-businesses-put-ai-to-work/`
  - Title: **Helping small businesses put AI to work**
  - lastmod: 2026-10-09T06:21:01.148Z
  - Sub-sitemap: https://openai.com/sitemap.xml/global-affairs/
- `https://openai.com/index/how-we-will-do-better-for-australia/`
  - Title: **How we will do better for Australia**
  - lastmod: 2026-10-09T06:21:03.762Z
  - Sub-sitemap: https://openai.com/sitemap.xml/safety/
- `https://openai.com/index/introducing-dots/`
  - Title: **Introducing dots**
  - lastmod: 2026-10-09T06:33:27.345Z
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/introducing-gpt-6-1-sol/`
  - Title: **GPT-6.1Sol**
  - lastmod: None
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/jump-trading/`
  - Title: **How Jump Trading is scaling quant research with ChatGPT**
  - lastmod: 2026-10-08T22:48:48.833Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/legalon-halves-codex-costs/`
  - Title: **LegalOn halves Codex costs while maintaining development speed**
  - lastmod: 2026-10-09T05:55:57.417Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/lenfest-ai-collaborative-expansion/`
  - Title: **The Lenfest Institute grows landmark program with expanded OpenAI support**
  - lastmod: 2026-10-09T06:21:04.175Z
  - Sub-sitemap: https://openai.com/sitemap.xml/company/
- `https://openai.com/index/new-chatgpt-ads-format-and-measurement/`
  - Title: **Building advertising for the way people use AI**
  - lastmod: 2026-10-09T06:33:28.859Z
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/oracle/`
  - Title: **How Oracle turns days of work into minutes with ChatGPT and Codex**
  - lastmod: 2026-10-09T05:55:55.540Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/pollo-ai/`
  - Title: **Pollo AI turns creative ideas into campaigns with OpenAI**
  - lastmod: 2026-10-09T01:12:07.527Z
  - Sub-sitemap: https://openai.com/sitemap.xml/startup/
- `https://openai.com/index/practical-guide-building-gpt-6/`
  - Title: **A model guide for the GPT‑6 family**
  - lastmod: 2026-10-09T07:25:01.870Z
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/radisson/`
  - Title: **Radisson Hotel Group brings hotel discovery into ChatGPT**
  - lastmod: 2026-10-09T09:01:24.532Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/sharing-ai-progress-in-mathematics/`
  - Title: **Sharing AI progress in mathematics**
  - lastmod: 2026-10-09T06:21:17.871Z
  - Sub-sitemap: https://openai.com/sitemap.xml/research/
- `https://openai.com/index/sophos/`
  - Title: **Sophos cuts threat investigation time by 96% with OpenAI Daybreak**
  - lastmod: 2026-10-09T08:31:14.362Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/teens-learn-and-plan/`
  - Title: **Helping teens learn, plan, and shape the future of AI**
  - lastmod: 2026-10-09T06:33:27.883Z
  - Sub-sitemap: https://openai.com/sitemap.xml/product/
- `https://openai.com/index/the-den-family-social/`
  - Title: **The Den frees up 10-15 hours a week to grow with ChatGPT Work**
  - lastmod: 2026-10-08T22:45:51.216Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/index/the-eternal-complement/`
  - Title: **The eternal complement**
  - lastmod: 2026-10-09T06:21:23.883Z
  - Sub-sitemap: https://openai.com/sitemap.xml/intelligence-age/
- `https://openai.com/index/towards-safety-cases-for-frontier-ai-training/`
  - Title: **Towards safety cases for frontier AI training**
  - lastmod: 2026-10-09T06:21:01.047Z
  - Sub-sitemap: https://openai.com/sitemap.xml/safety/
- `https://openai.com/policies/row-privacy-policy/`
  - Title: **Privacy policy**
  - lastmod: 2026-10-09T08:47:55.068Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/
- `https://openai.com/policies/sign-in-with-chatgpt-terms/`
  - Title: **Sign in with ChatGPT Terms**
  - lastmod: 2026-10-06T09:59:18.974Z
  - Sub-sitemap: https://openai.com/sitemap.xml/page/

## Removed URLs

- `https://openai.com/form/ultrafast/`
  - Last snapshot at: `pages/openai.com/form/ultrafast/index.md`
