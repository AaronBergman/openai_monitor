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

July 30, 2026

[Product](</news/product-releases/>)

# Advancing the price-performance frontier with GPT‑5.6

By making every layer more efficient, OpenAI is delivering stronger performance per dollar across more enterprise workloads.

Loading…

Share

Matching intelligence to the outcome

  * Matching intelligence to the outcome
  * How we advance the efficiency frontier
  * A compute strategy built for scale
  * Availability and pricing



  * Matching intelligence to the outcome
  * How we advance the efficiency frontier
  * A compute strategy built for scale
  * Availability and pricing



Yesterday, we shared how [GPT‑5.6⁠](<https://openai.com/index/gpt-5-6/>) helped make itself [more efficient to run⁠](<https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/>). Today, we’re passing those gains on to customers with lower prices for GPT‑5.6 [Luna⁠(opens in a new window)](<https://developers.openai.com/api/docs/models/gpt-5.6-luna>) and [Terra⁠(opens in a new window)](<https://developers.openai.com/api/docs/models/gpt-5.6-terra>) and faster performance with GPT‑5.6 [Sol⁠](<https://openai.com/index/gpt-5-6/>) in the API. Together, these updates help customers get more from every dollar they invest in AI and move faster when time matters.

Starting today, GPT‑5.6 Luna, our fastest and most affordable model, will cost 80% less, while GPT‑5.6 Terra, our balanced model for everyday work, will cost 20% less. These lower prices for Luna and Terra are also reflected in how usage is counted against paid subscriptions when using Codex and ChatGPT Work. Luna gives businesses a far more cost-effective way to handle high-volume work at very high levels of quality. It can use tools and complete multi-step workflows, making a broader range of AI applications practical to run at scale.

Making advanced intelligence more abundant and affordable is central to OpenAI’s mission to ensure AGI benefits all of humanity. These changes put that commitment into practice. They reflect years of improvements in how our models are built, served, and put to work.

We’re also introducing **Fast mode** in the API, which replaces our Priority Processing offering. For GPT‑5.6 Sol, Fast mode now delivers up to 2.5× faster speeds than Standard processing at twice the price, with no change in intelligence. Fast mode is backward compatible: requests tagged priority will automatically use Fast mode.

1 of 6

> “GPT‑5.6 Luna is the closest we’ve come to intelligence too cheap to meter. I’ve never seen a model this affordable be this powerful — it’s unlocking use cases for Replit we didn’t expect to build for a long time.”

Michele Catasta, President & Head of AI, Replit

> “GPT‑5.6 Terra is a strong fit for everyday work in Notion’s personal agent, including workspace Q&A and scoped tasks where latency matters. In our evaluations, it delivered comparable quality to GPT‑5.5 at half the cost per task and in 60% less time.”

Hoda Noorian, AI Product, Notion

> “We are focused on maximizing outcome per dollar in everything we do, and the GPT‑5.6 series has been a significant step forward in that regard. Terra and Luna lead on cost-efficiency across our internal coding benchmarks, and Luna is now our default model for background agent automations.”

Shaiyon Hariri, Creator of Ramp SWE-Bench

> “GPT‑5.6 Luna is the biggest step change in agentic behavior we’ve seen since putting GPT‑4o mini into production. Luna moved us from a single structured-output call to a full tool-calling agent loop, increasing prompt-cache reuse from 24% to 90%. Across thousands of production calls, Luna handles 2.2× more context with 8.5× fewer output tokens—at 87% lower cost than GPT‑5.4 mini.”

Sid Pardeshi, CTO + Co-Founder, Blitzy

> “GPT‑5.6 Luna is an ideal pair programmer for larger models, handling much of the routine work while striking an ideal balance between cost and intelligence. We’ve incorporated Luna into Devin Fusion to deliver significant cost savings for users without compromising quality.”

Walden Yan, Co-Founder and Chief Product Officer, Cognition

> “We’ve seen meaningful operational improvements since adopting GPT‑5.6 Luna. Given the same agentic tasks, GPT‑5.6 Luna is 40% faster and 40% cheaper than our previous default model, leading to a more responsive experience for users. It delivers an excellent balance of quality, speed and efficiency.”

Stanislas Polu, Co-Founder and CTO, Dust

  * Replit
  * Notion
  * Ramp
  * Blitzy
  * Cognition
  * Dust



## Matching intelligence to the outcome

Using AI efficiently begins with the outcome. The stakes, cost of error, urgency, and scale determine the right balance of intelligence, speed, reliability, and cost. That balance can change from one step of a workflow to the next.

GPT‑5.6 gives businesses much more room to optimize that equation. Luna delivers performance comparable to models that were frontier-class a year ago at roughly 6 cents on the dollar per task, and at nearly nine times the speed. On professional work, as measured by Agents’ Last Exam, Luna outperforms Fable 5 at an estimated cost per task nearly 99% lower.

In practice, businesses can define the outcome and quality standard they need, then use evaluations to determine where additional intelligence materially improves the result and where faster, lower-cost processing can deliver the same quality. A coding workflow, for example, might use Sol to resolve uncertainty and define the plan, then use Luna to implement well-specified changes, write and run tests, and evaluate the results. Another workflow may call for a different balance.

The GPT‑5.6 family expands the range of those choices. Businesses can apply the maximum useful intelligence at every stage while paying the right price for the value it creates.

Delivering that flexibility starts with making every layer behind the models more efficient.

## How we advance the efficiency frontier

Our efficiency edge comes from improving the models, the inference systems that run them, and the agentic harness that connects them to tools and context. GPT‑5.6 models take a more direct path through work. Better routing keeps hardware productive, optimized production software generates tokens more efficiently, and smarter context management helps agents avoid repeating completed work. Together, these improvements let us complete more useful work with the same compute, reducing the time, tokens, and cost required for each result.

GPT‑5.6 Sol is increasingly helping us find and deliver the next round of gains. Within a human-led process, Sol autonomously rewrote and optimized production kernels, designed and ran hundreds of experiments to improve token generation, and monitored training, intervening when problems arose. The kernel work helped reduce the end-to-end cost of serving the model by 20%, while its experiments increased token-generation efficiency by more than 15%. This work continues, creating a tighter feedback loop: as our models improve and are able to work more autonomously, our ability to improve efficiencies accelerates. [Read more⁠](<https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/>) about the engineering behind GPT‑5.6.

## A compute strategy built for scale

Meeting demand for abundant intelligence requires both more compute and more productive compute. We are building a resilient infrastructure portfolio and matching each workload to the systems best suited to run it. That approach supports both ends of the price-performance curve. At the lower-cost end, the new Luna and Terra prices make high-volume work economical at much greater scale. At the frontier end, Fast mode gives API customers faster access to Sol when response time is important.

Enterprises can move more AI into everyday operations without sacrificing speed on their most consequential work. Large-scale document analysis, customer-interaction classification, and routine implementation can become economical to run broadly, while complex Sol workloads can move faster when the premium is justified.

The gains can compound. Within a human-led process, more capable models help our technical team find the next generation of improvements, shortening the path to better performance and lower costs. Our strategy remains focused on advancing both capability and efficiency so each generation of intelligence can accomplish more work at a lower cost.

## Availability and pricing

GPT‑5.6 Terra and Luna remain available in ChatGPT Work, Codex, and the OpenAI API. In ChatGPT Work and Codex, Free and Go users can access Terra, while Plus, Pro, Business, and Enterprise users can choose Terra and Luna.

Starting July 30, API pricing is $2 per million input tokens and $12 per million output tokens for Terra, and $0.20 per million input tokens and $1.20 per million output tokens for Luna. Sol pricing remains unchanged. ChatGPT and Codex subscription prices and quota budgets remain unchanged, while Terra and Luna usage now consumes fewer credits. Pricing changes will begin rolling out in AWS later today.

Fast mode for GPT‑5.6 Sol replaces Priority Processing in the API and aligns with /fast in Codex. Existing API requests tagged priority will continue to work. [View complete API pricing details.⁠](<https://openai.com/business/pricing/#api>)

  * [2026](</news/?tags=2026>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

[Improving GPT‑5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free usersProductAug 6, 2026](</index/improving-gpt-5-6-sol-in-chatgpt/>)

![Edu plugin > card image ](https://images.ctfassets.net/kftzwdyauwt9/5vIZVUmoUSCImIDsK3jJiL/67f1d878e33f6bc5139094e933f454db/ArtCard.png?w=3840&q=90&fm=webp)

[New ways to learn and teach with ChatGPT Work and CodexProductAug 4, 2026](</index/learn-teach-chatgpt-work-codex/>)

![Health in ChatGPT > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/48aIp3cQOKJ57vpQeqOb8y/2e8732bcad5ceea1c7b20cf001bd2823/1_1_Art_Card.png?w=3840&q=90&fm=webp)

[Launching Health in ChatGPT ProductJul 23, 2026](</index/health-in-chatgpt/>)

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
