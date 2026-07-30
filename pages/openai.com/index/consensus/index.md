Skip to main content

[](</>)

  * [Research](</research/index/>)
  * Products
  * [Business](</business/>)
  * [Developers](</api/>)
  * [Company](</about/>)
  * [Foundation(opens in a new window)](<https://openaifoundation.org>)



Log in[Try ChatGPT(opens in a new window)](<https://chatgpt.com/>)

  * Research
  * Products
  * Business
  * Developers
  * Company
  * [Foundation(opens in a new window)](<https://openaifoundation.org>)



[Try ChatGPT(opens in a new window)](<https://chatgpt.com/>)Login

OpenAI

October 23, 2025

# Consensus uses GPT‑5 and the Responses API to complete weeks of research in minutes

Using GPT‑5 and the Responses API, Consensus designed a multi-agent system that plans, reads, and synthesizes evidence the way researchers do.

![Consensus logo in white centered on a dark teal background with vertical textured panels in varying shades of blue and green.](https://images.ctfassets.net/kftzwdyauwt9/3OI2dbHjhKDXlBLTJhFBKI/df82372767a12801d8ee1387c0fcacbf/oai_Consensus_16x9.png?w=3840&q=90&fm=webp)

Loading…

Share

From search engine to agentic assistant

  * From search engine to agentic assistant
  * Building with Responses API
  * A consumer bet in a world of institutions
  * Scaling with the science



  * From search engine to agentic assistant
  * Building with Responses API
  * A consumer bet in a world of institutions
  * Scaling with the science



Every year, millions of new scientific papers are published—far more than any one person can read. 

For scientists, the challenge isn’t access to knowledge but the overwhelming task of finding, interpreting, and connecting it. Breakthroughs happen at the edge of what’s known, yet researchers spend most of their time just finding the edges instead of pushing past them.

[Consensus⁠(opens in a new window)](<https://consensus.app/>), a research assistant used by more than 8 million people, was built to change that. Founded by Christian Salem and Eric Olson, the platform searches, reads, and synthesizes peer-reviewed literature across more than 220 million papers. Its newest capability, Scholar Agent, is a multi-agent system built on GPT‑5 and the Responses API. It mirrors how researchers actually work, helping them get from question to conclusion in minutes instead of weeks.

But the goal isn’t just faster research—it’s a faster path to discovery. “Science advances when it’s more accessible,” Salem says. “Our job is to give researchers everywhere the ability to find, trust, and act on evidence.”

## From search engine to agentic assistant

The first version of Consensus worked like a vertical search engine for science: it indexed academic papers, retrieved relevant results, and generated summaries grounded in citations. But search alone wasn’t enough. 

“Research isn’t just finding papers,” Salem says. “It’s interpreting results, comparing findings, and connecting ideas. The more time scientists spend searching, reading, and interpreting past knowledge for the right study, the less time they have to discover and createdo real research.”

So the team began re-architecting Consensus around a new concept: a multi-agent system called “Scholar Agent” that works the way a human researcher does.

Built on GPT‑5 and the Responses API, the system now runs a coordinated workflow of agents:

  * **Planning Agent** breaks down the user’s question and decides which actions to take next
  * **Search Agent** combs Consensus’s paper index, a user’s private library, and the citation graph
  * **Reading Agent** interprets papers individually or in batches
  * **Analysis Agent** synthesizes results, determines structure and visuals, and composes the final output



Each agent has a narrow scope, which keeps reasoning precise and minimizes hallucinations. The architecture also allows Consensus to decide when _not_ to answer; if no relevant studies meet its quality threshold, the assistant simply says so.

“By dividing the workflow across agents, we reduce error and make the system far more disciplined,” Salem says. “No one agent has too much responsibility, which turns out to be key for reliability.”

![Agent flow diagram showing how a user query is processed through planning, parallel search, reading, and analysis agents to generate a research-based output.](https://images.ctfassets.net/kftzwdyauwt9/1IVANY7u7WClGLyl5JVVJS/519af8c34ad2904b4728d0e98a06b911/Agent_Flow_Consensus.png?w=3840&q=90&fm=webp)

This approach is what the team calls **context engineering** : assembling the right evidence _before_ generation begins. Every answer comes with a “research context pack”—a structured bundle of papers, metadata, and key findings that trace back to original studies.

“We don’t want researchers wasting time double-checking every claim,” Salem says. “If the system can’t ground an answer in real evidence, it won’t make one up.”

## Building with Responses API

Consensus migrated from Chat Completions to the **Responses API** to support its multi-agent routing. The switch improved both reliability and cost efficiency, giving the team finer control over sub-agent calls. With GPT‑5 long-context reasoning and reliable tool-calling, the choice was clear.

Early evaluations confirmed the bet: GPT‑5 outperformed GPT‑4.1, Sonnet 4, and Gemini 2.5 Pro on tool-calling accuracy and planning stability. That allowed the Consensus team to focus less on prompt gymnastics and more on building agent behaviors that map directly to research workflows.

![Table comparing GPT-5 Research Agent metrics for OAI, Anthropic, and Google models across accuracy, precision, structure, and latency.](https://images.ctfassets.net/kftzwdyauwt9/QZQqMakhCEPTRwpqRyIRs/32b1d412f6c9fe76968e2f1c1368bf33/Eval_Chart_Consensus.png?w=3840&q=90&fm=webp)

## A consumer bet in a world of institutions

From the beginning, Consensus approached the market differently than expected. Rather than selling through institutions, the team focused on the people doing the research itself: students, faculty, and clinicians who needed answers today. That direct-to-researcher focus shaped both the product’s design and its rapid growth.

“Everyone said you can’t go direct-to-consumer in academia, but AI has changed that,” Salem says. “People don’t wait for approval anymore—they use what works.”

That decision shaped the product’s tone and growth curve. Consensus feels more like a modern consumer app than a traditional academic tool: fast onboarding, intuitive design, conversational interface. Adoption spread through word of mouth across campuses and labs.

Graduate students and PhD candidates became the first power users, followed by faculty and private researchers. Then came clinicians, who began using Consensus to surface the latest evidence in their fields. 

“We didn’t set out to build for doctors,” Salem says. “But they need the same thing researchers do: fast access to reliable evidence.”

The company recently signed the Mayo Clinic’s medical library and just launched ‘Medical Mode,’ a new feature designed for practitioners searching for clinical evidence.

## Scaling with the science

In the past year, Consensus has expanded rapidly, growing to more than 8 million researchers worldwide and increasing revenue by 8x.

That growth hasn’t changed the product’s priorities. Every feature still revolves around verifiable, low-hallucination answers. The team has invested heavily in evaluation pipelines that test accuracy, citation traceability, and stylistic consistency across agents.

Consensus’s architecture is intentionally modular, designed so new agents can slot in as models expand and improve—agents that replicate experiments, generate figures, or run statistical analyses.

“We’re building the assistant researchers actually need in a rapidly changing world,” Salem says. “The models keep getting better, the system grows with them, and science moves faster.”

## OpenAI <3 startups. Come build with us.

[Join the community](</leads/startup/>)[Start building(opens in a new window)](<https://platform.openai.com/>)

## Keep reading

![ARC-AGI-3 art-card 1x1](https://images.ctfassets.net/kftzwdyauwt9/71xyJRWnTkM6EW1JKDUc59/91d2690ff9e7abaa975b4a5f64089056/ARC-AGI-3_art-card_1x1.png?w=3840&q=90&fm=webp)

[How enabling two settings tripled our scores on the ARC-AGI-3 benchmarkResearchJul 29, 2026](</index/how-two-settings-tripled-our-arc-agi-3-scores/>)

![oai Science Academic Research Academic Research 1x1](https://images.ctfassets.net/kftzwdyauwt9/59kTmFmujYzNh0VgSvCgwe/e9334dd9944b5309f8ca2d44fdc71b6f/academic-research-card.png?w=3840&q=90&fm=webp)

[Accelerating scientific discovery with ChatGPT for Academic ResearchersCompanyJul 29, 2026](</index/chatgpt-for-academic-researchers/>)

![GPT-5.6 efficiency article — art card](https://images.ctfassets.net/kftzwdyauwt9/5ExPWhZDZXbZgTHE7aeE5d/0526071f749a3b44adff3c45a12322b7/How_GPT-5.6_fuses_frontier_intelligence_with_frontier_efficiency_ART_CARD__1_.png?w=3840&q=90&fm=webp)

[How GPT-5.6 fuses frontier intelligence with frontier efficiencyEngineeringJul 29, 2026](</index/gpt-5-6-frontier-intelligence-efficiency/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)



Safety

  * [Safety Approach](</safety/>)
  * [Deployment Safety(opens in a new window)](<https://deploymentsafety.openai.com/>)
  * [Security & Privacy](</security-and-privacy/>)
  * [Trust & Transparency](</trust-and-transparency/>)



Products

  * [ChatGPT(opens in a new window)](<https://chatgpt.com/>)
  * [ChatGPT Business(opens in a new window)](<https://chatgpt.com/business/>)
  * [ChatGPT Enterprise(opens in a new window)](<https://chatgpt.com/business/enterprise/>)
  * [ChatGPT for Education(opens in a new window)](<https://chatgpt.com/business/education/>)
  * [Codex](</codex/>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Customer Stories](</business/customer-stories/>)
  * [Partner Network](</business/partners/>)
  * [Contact Sales](</contact-sales/>)



Developers

  * [Apps SDK(opens in a new window)](<https://developers.openai.com/apps-sdk>)
  * [Open Models](</open-models/>)
  * [Docs(opens in a new window)](<https://developers.openai.com/>)
  * [Resources(opens in a new window)](<https://developers.openai.com/learn>)
  * [Developer Forum(opens in a new window)](<https://community.openai.com/>)



Company

  * [About Us](</about/>)
  * [Our Charter](</charter/>)
  * [Careers](</careers/>)
  * [News](</news/>)



Support

  * [Help Center(opens in a new window)](<https://help.openai.com/>)



More

  * [Stories](</stories/>)
  * [Academy](</academy/>)
  * [Supply Co.](</supply/>)
  * [Livestreams](</live/>)
  * [Podcast](</podcast/>)
  * [RSS](<https://openai.com/news/rss.xml>)



Terms & Policies

  * [Terms of Use](</policies/terms-of-use/>)
  * [Privacy Policy](</policies/privacy-policy/>)
  * [Other Policies ](</policies/>)



[(opens in a new window)](<https://x.com/OpenAI>)[(opens in a new window)](<https://www.youtube.com/OpenAI>)[(opens in a new window)](<https://www.linkedin.com/company/openai>)[(opens in a new window)](<https://github.com/openai>)[(opens in a new window)](<https://www.instagram.com/openai/>)[(opens in a new window)](<https://www.tiktok.com/@openai>)[(opens in a new window)](<https://discord.gg/openai>)

OpenAI © 2015–2026Your privacy choices

EnglishUnited States
