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

November 19, 2025

[Research](</news/research/>)

# How evals drive the next chapter in AI for businesses

This primer teaches business leaders how evaluation frameworks (“evals”) turn business objectives into consistent results.

Loading…

Share

How evals work: Specify → Measure → Improve

  * How evals work: Specify → Measure → Improve
    * 1\. Specify: Define what “great” means
    * 2\. Measure: Test against real-world conditions
    * 3\. Improve: Learn from errors
  * What evals mean for business leaders



  * How evals work: Specify → Measure → Improve
    * 1\. Specify: Define what “great” means
    * 2\. Measure: Test against real-world conditions
    * 3\. Improve: Learn from errors
  * What evals mean for business leaders



Over [_one million businesses_ ⁠](<https://openai.com/index/1-million-businesses-putting-ai-to-work/>) around the world are leveraging AI to drive greater efficiency and value creation. But some organizations have struggled to get the results they are expecting. What is causing the gap?

At OpenAI we are leveraging AI internally to achieve our ambitious goals. One key set of tools we use are **evals** , methods to measure and improve the ability of an AI system to meet expectations. 

Similar to product requirement documents, evals make fuzzy goals and abstract ideas specific and explicit. Using evals strategically can make a customer-facing product or internal tool more reliable at scale, decrease high-severity errors, protect against downside risk, and give an organization a measurable path to higher ROI. 

At OpenAI, our models are our products, so our researchers use rigorous [**_frontier evals_** ⁠(opens in a new window)](<https://evals.openai.com/>) 1 to measure how well the models perform in different domains. While frontier evals help us ship better models faster, they cannot reveal all the nuances required to ensure the model will perform on a specific workflow in a specific business setting. That is why internal teams have also created dozens of **contextual evals** designed to assess performance within a specific product or internal workflow. It is also why business leaders should learn how to create contextual evals specific to their organization’s needs and operating environment. 

This is a primer for business leaders looking to apply evals in their organizations. Contextual evals, each crafted for a specific organization’s workflow or product, are an active area of development and definitive processes have yet to emerge. As a result, this article provides a broad framework that we have seen work across many situations. We expect this field to evolve and for more frameworks to emerge that address specific business contexts and goals. For example, an excellent eval for a cutting-edge, AI-enabled consumer product might require a different process than an eval for an internal automation based around a standard operating procedure. We believe that the framework presented below will serve as a collection of best practices in both cases, and will be a useful guide as you build evals tailored to your organization’s needs.

## How evals work: Specify → Measure → Improve

![Diagram titled “Eval Blog” showing a flow of evaluation components and processes, set on a light background with colored blocks and arrows representing model evaluation logic.](https://images.ctfassets.net/kftzwdyauwt9/5NnfoyNbQcCkWHbaqG8bMS/d0a168d37e76d73168878675a4d20b1e/Eval_Blog_Diagram_Desktop_Light.svg?w=3840&q=90)

### 1\. Specify: Define what “great” means

Start with a small, empowered team that can write down the purpose of your AI system in plain terms, for example: “Convert qualified inbound emails into scheduled demos while staying on brand.”

This team should be a mix of individuals with technical and domain expertise (in the given example, you’d want sales experts on the team). They should be able to state the most important outcomes to measure, outline the workflow end-to-end, and identify each important decision point your AI system will encounter. For every step in that workflow, the team should define what success looks like and what to avoid. This process will create a mapping of dozens of example inputs (e.g. inbound emails) to the outputs they want the system to produce. The resulting **golden set** of examples should be a living, authoritative reference of your most skilled experts’ judgement and taste for what “great” looks like.

Do not get overwhelmed with a cold start or try to solve it all at once. The process is iterative and messy. Early prototyping can help immensely. Reviewing 50 to 100 outputs from an early version of the system will uncover how and when your system is failing. This “error analysis” will result in a taxonomy of different errors (and their frequencies) to track as your system improves.

This process is not purely technical—it’s cross-functional and centered on defining business goals and desired processes. Technical teams should not be asked in isolation to judge what best serves customers or the needs of other teams like product, sales, or HR. Consequently, domain experts, technical leads, and other key stakeholders should share ownership. 

### 2\. Measure: Test against real-world conditions

The next step is to measure. The goal of measurement is to reliably surface concrete examples of how and when the system is failing. To do that, create a dedicated test environment that closely mirrors real-world conditions—not just a demo or prompt playground. Evaluate performance against your golden set and error analysis under the same pressures and edge cases your system will actually face.

Rubrics can help bring concreteness to judging outputs from your system, but it is possible to over-emphasize superficial items at the expense of your overall goals. Further, some qualities are difficult or impossible to measure. In some cases, traditional business metrics will be important. In others, you’ll need to invent new metrics. Keep your subject matter experts in the loop throughout, and tightly align the process with your core objectives.

To actually test the system, use examples drawn from real-world situations whenever possible, and include or invent edge cases that are rare but costly if mishandled. 

Some evals can be scaled through the use of an **LLM grader** , an AI model that grades outputs the same way an expert would; yet, it is still important to keep a human in the loop. Your domain expert needs to regularly audit LLM graders for accuracy and should also directly review logs of your system’s behavior. 

Evals can help you decide when a system is ready to launch, but they do not stop at launch. You should continuously measure the quality of your system's real outputs generated from real inputs. As with any product, signals from your end-users (whether external or internal) are especially important and should be built into your eval.

### 3\. Improve: Learn from errors

The last step is to set up a process for continuous improvement. Addressing problems uncovered by your eval can take on many forms: refining prompts, adjusting data access, updating the eval itself to better reflect your goals, and so forth. As you uncover new types of errors, add them to your error analysis and address them. Each iteration compounds upon the last: new criteria and clearer expectations of system behavior help reveal new edge cases and subtle, stubborn issues to correct.

To support this iteration, build a data flywheel. Log inputs, outputs, and outcomes; sample those logs on a schedule and automatically route ambiguous or costly cases to expert review. Add these expert judgements to your eval and error analysis, then use them to update prompts, tools, or models. Through this loop you will more clearly define your expectations for the system, align it tighter to those expectations, and identify additional relevant outputs and outcomes to track. Deploying this process at scale yields a large, differentiated, context-specific dataset that is hard to copy—a valuable asset your organization can leverage as you build the best product or process in your market. 

While evals create a systematic way to improve your AI system, new failure modes can arise. In practice, as models, data, and business goals evolve, evals must also be continuously maintained, expanded, and stress-tested.

For external-facing deployments, evals do not replace more traditional A/B tests and product experimentation. They are complements to traditional experimentation that can help guide each other and provide visibility into how changes you make impact real-world performance. 

## What evals mean for business leaders

Every major technology shift reshapes operational excellence and competitive advantage. Frameworks like OKRs and KPIs have helped organizations orient themselves around “measuring what matters” for their business in the age of big data analytics. Evals are the natural extension of measurement for the age of AI.

Working with probabilistic systems requires new kinds of measurement and deeper consideration of trade-offs. Leaders must decide when precision is essential, when they can be more flexible, and how to balance velocity and reliability.

Evals are difficult to implement for the same reason that building great products is difficult; they require rigor, vision, and taste. If done well, evals become unique differentiators. **In a world where information is freely available across the world and expertise is democratized, your advantage hinges on how well your systems can execute inside your context.** Robust evals create compounding advantages and institutional know-how as your systems improve. 

At their core, evals are about a deep understanding of business context and objectives. If you cannot define what “great” means for your use case, you’re unlikely to achieve it. In this sense, evals highlight a key lesson of the AI era: management skills are AI skills. Clear goals, direct feedback, prudent judgment, and a clear understanding of your value proposition, strategy, and processes still matter, perhaps even more than ever.

As more best practices and frameworks emerge, we will be sharing them. In the meantime, we encourage you to experiment with evals and discover what processes work best for your needs. To get started, identify the problem to be solved and your domain expert, round up your small team, and, if you are building on our API, explore our [_Platform Docs_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/evals?api-mode=responses>).

Don’t hope for “great.” Specify it, measure it, and improve toward it.

  * [2025](</news/?tags=2025>)



## Author

OpenAI

## Footnotes

  1. 1

If you would like to support our work building the next generation of AI models, we invite you to contribute to [_GDPVal_ ⁠](<https://openai.com/index/gdpval/>), our latest benchmark of how AI models perform on real-world tasks. If you’re an industry expert interested in contributing to GDPval, please [_show your interest here_ ⁠](<https://openai.com/form/real-world-knowledge-work/>). If you’re a customer working with OpenAI and you'd like to contribute to a future round of GDPval, please [_express interest here_ ⁠](<https://openai.com/form/gdpval-customer-contribution/>). 




## Keep reading

[View all](</news/>)

![Separating signal from noise > Art Card](https://images.ctfassets.net/kftzwdyauwt9/7j6M3prKIsTmV6cbMaHjhZ/e66f7cdd98c66c99546853cbc22cfe84/Seperating-signal-from-noise-card.png?w=3840&q=90&fm=webp)

[Separating signal from noise in coding evaluationsResearchJul 8, 2026](</index/separating-signal-from-noise-coding-evaluations/>)

![Introducing GeneBench-Pro > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7sbJaKBi5qLXAqbewh72aK/93197556e903eac9df6f077eb12b7581/GenebenchPro_Blog_ArtCard.png?w=3840&q=90&fm=webp)

[Introducing GeneBench-ProResearchJun 30, 2026](</index/introducing-genebench-pro/>)

![A near-autonomous AI chemist improves a challenging reaction](https://images.ctfassets.net/kftzwdyauwt9/QgPPg4etNE5C4Ao0G94sk/e5f2a50e5de4619d0e0fe8483698718b/molecule-one-art-card.png?w=3840&q=90&fm=webp)

[A near-autonomous AI chemist improves a challenging reaction in medicinal chemistryResearchJun 17, 2026](</index/ai-chemist-improves-reaction/>)

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
