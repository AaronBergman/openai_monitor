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

Table of contents

  * Design workflows with Agent Builder
  * Embed agentic chat experiences with ChatKit
  * Measure agent performance with new Evals capabilities
  * Push agent performance with reinforcement fine-tuning
  * Pricing & availability



October 6, 2025

[Product](</news/product-releases/>)

# Introducing AgentKit

New tools for building, deploying, and optimizing agents.

Loading…

Share

** _Update on June 3, 2026:_**_OpenAI is winding down the Agent Builder and Evals products. From November 30, 2026 onward, they will no longer be available on the OpenAI platform. For workflows that should continue as code, we recommend the_[ _Agents SDK_ ⁠(opens in a new window)](<https://developers.openai.com/api/docs/guides/agents>)_. For use cases better suited to natural language prompting, we recommend_[ _Workspace Agents in ChatGPT_ ⁠](<https://openai.com/index/introducing-workspace-agents-in-chatgpt/>) _._

* * *

Today we’re launching AgentKit, a complete set of tools for developers and enterprises to build, deploy, and optimize agents. Until now, building agents meant juggling fragmented tools—complex orchestration with no versioning, custom connectors, manual eval pipelines, prompt tuning, and weeks of frontend work before launch. With AgentKit, developers can now design workflows visually and embed agentic UIs faster using new building blocks like:

  * **Agent Builder:** a visual canvas for creating and versioning multi-agent workflows
  * **Connector Registry:** a central place for admins to manage how data and tools connect across OpenAI products
  * **ChatKit:** a toolkit for embedding customizable chat-based agent experiences in your product 



We’re also expanding evaluation capabilities with new features like datasets, trace grading, automated prompt optimization, and third-party model support to measure and improve agent performance.

Since releasing the [Responses API and Agents SDK⁠](<https://openai.com/index/new-tools-for-building-agents/>) in March, we’ve seen developers and enterprises build end-to-end agentic workflows for deep research, customer support, and more. Klarna [built a support agent⁠](<https://openai.com/index/klarna/>) that handles two-thirds of all tickets and Clay [10x’ed growth⁠](<https://openai.com/index/clay/>) with a sales agent. AgentKit builds on the Responses API to help developers build agents more efficiently and reliably.

## Design workflows with Agent Builder

As agent workflows grow more complex, developers need clearer visibility into how they work. [_Agent Builder_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/agents/agent-builder>) provides a visual canvas for composing logic with drag-and-drop nodes, connecting tools, and configuring custom guardrails. It supports preview runs, inline eval configuration, and full versioning—ideal for fast iteration.

![Interface view of a customer service automation flow in a visual builder tool. The canvas shows connected nodes labeled Start, Jailbreak guardrail, Classification agent, If/else, Return agent, Retention agent, Information agent, Hallucination guardrail, and End. A sidebar on the left lists available node types such as Agent, Note, File search, Guardrails, MCP, and User approval. Top controls include options for Evaluate, Code, Preview, and Publish.](https://images.ctfassets.net/kftzwdyauwt9/4VjOJxeZ7prpcZftRJ5MPd/582d98bb0151362f998b44d473dacae0/Visual__Agent_Builder_Template_Assets.png?w=3840&q=90&fm=webp)

Builders can get started with a blank canvas or with prebuilt templates.

At Ramp, the team went from a blank canvas to a buyer agent in just a few hours:

> Agent Builder transformed what once took months of complex orchestration, custom code, and manual optimizations into just a couple of hours. The visual canvas keeps product, legal, and engineering on the same page, slashing iteration cycles by 70% and getting an agent live in two sprints rather than two quarters.”

— Ramp

Similarly, LY Corporation—a leading Japanese technology and internet services company—built a work assistant agent with Agent Builder in less than two hours.

> "Agent Builder allowed us to orchestrate agents in a whole new way, with engineers and subject matter experts collaborating all in one interface. We built our first multi-agentic workflow and ran it in less than two hours, dramatically accelerating the time to create and deploy agents."

— LY Corporation

We’re also launching a Connector Registry for enterprises to govern and maintain data across multiple workspaces and organizations. The [_Connector Registry_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/agents/connector-registry>) consolidates data sources into a single admin panel across ChatGPT and the API. The registry includes all pre-built connectors like Dropbox, Google Drive, Sharepoint, and Microsoft Teams, as well as third-party MCPs.

Developers can also enable [_Guardrails_ ⁠(opens in a new window)](<https://openai.github.io/openai-guardrails-python/>) in Agent Builder—an open-source, modular safety layer that helps protect agents against unintended or malicious behavior. Guardrails can mask or flag PII, detect jailbreaks, and apply other safeguards, making it easier to build and deploy reliable, safe agents. Guardrails can be deployed standalone or via the guardrails library for [_Python_ ⁠(opens in a new window)](<https://openai.github.io/openai-guardrails-python/>) and [_JavaScript_ ⁠(opens in a new window)](<https://openai.github.io/openai-guardrails-js/>).

## Embed agentic chat experiences with ChatKit

Deploying chat UIs for agents can be surprisingly complex— handling streaming responses, managing threads, showing the model thinking, and designing engaging in-chat experiences. [ChatKit⁠(opens in a new window)](<https://platform.openai.com/docs/guides/chatkit>) makes it simple to embed chat-based agents that feel native to your product. It can be embedded into apps or websites and customized to match your theme or brand.

CanvaLegalOnHubSpot

> "We saved over two weeks of time building a support agent for our Canva Developers community with ChatKit, and integrated it in less than an hour. This support agent will transform the way developers engage with our docs by turning it into a conversational experience, making it easy to build apps and integrations on Canva."

— Canva

ChatKit already powers a range of use cases, from internal knowledge assistants and onboarding guides to customer support and research agents. [_HubSpot_ ⁠(opens in a new window)](<https://www.hubspot.com/>)’s customer support agent is one example:

RampAlbertsonsHubSpotCanvaActivelyLegalOnEvernoteTaboola

![Dashboard view of the Ramp platform showing an expense management interface. The main panel greets the user, Daniel, and lists requests such as ‘Request for ChatGPT Business’ \(pending review\) and ‘Request for HubSpot’ \(draft\), along with recent expenses for airlines, rideshares, and software. On the right, a software request form is open for ChatGPT Business, detailing 5 seats at $125 per month from October 1, 2025, to October 1, 2026, with a yellow ‘Submit request’ button.](https://images.ctfassets.net/kftzwdyauwt9/7vwlxChvkUc64SIHHhozCr/7a23aa2fee0840430c95c090ac6c1363/Customers_UI_Ramp.png?w=3840&q=90&fm=webp)

## Measure agent performance with new Evals capabilities

Building reliable, production-ready agents requires rigorous performance evaluations. Last year, we launched [_Evals_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/evals>) to help developers test prompts and measure model behavior. We’re now adding four new capabilities that make it even easier to build evals:

  * **Datasets** –rapidly build agent evals from scratch and expand them over time with automated graders and human annotations..
  * **Trace grading** –run end-to-end assessments of agentic workflows and automate grading to pinpoint shortcomings.
  * **Automated prompt optimization** –generate improved prompts based on human annotations and grader outputs.
  * **Third-party model support** –evaluate models from other providers within the OpenAI Evals platform.



We’ve already seen major performance gains from customers using Evals.

CarlyleRipplingBoxBain & Company

> "The evaluation platform cut development time on our multi-agent due diligence framework by over 50%, and increased agent accuracy 30%."

— Carlyle

DatasetsPrompt optimizerTrace grading

![Interface showing a dataset table with columns for Rating, Tone, Feedback, and Accuracy. Rows display entries with thumbs-up or thumbs-down icons, tone tags such as Professional, Friendly, Rude, and Bad, and accuracy results labeled Pass or Fail with a score of 3.5. The top toolbar includes options for Upload, Columns, Grade, Generate output, and Save.](https://images.ctfassets.net/kftzwdyauwt9/3eaVkVTr4Q4xbXqVJN7UBh/5c90216e9aa153fd5a6cd8f1d2f13e5f/Eval_static-Datasets__1_.png?w=3840&q=90&fm=webp)

## Push agent performance with reinforcement fine-tuning

[ _Reinforcement fine-tuning_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/reinforcement-fine-tuning>) (RFT) lets developers customize our reasoning models. It is generally available on OpenAI o4-mini and in private beta for GPT‑5. We are working closely with dozens of customers to refine the RFT for GPT‑5 before wider release.

Today, we’re introducing two new features in that RFT beta designed to push agent performance even further:__

  * **Custom tool calls** –train models to call the right tools at the right time for better reasoning 
  * **Custom graders** –set custom evaluation criteria for what matters most in your use case



## Pricing & availability

Starting today, ChatKit and the new Evals capabilities are generally available to all developers. Agent Builder is available in beta, and Connector Registry is beginning its beta rollout to some API, ChatGPT Enterprise and Edu customers with a [Global Admin Console⁠(opens in a new window)](<https://help.openai.com/en/articles/12289294-coming-soon-global-admin-console>) _(_ where Global Owners can manage domains, SSO, multiple API orgs). The Global Admin console is a pre-requisite to enabling Connector Registry. All of these tools are included with standard API model pricing.

We plan to add a standalone Workflows API and agent deployment options to ChatGPT soon.

We can’t wait to see what you build.

  * [2025](</news/?tags=2025>)
  * [DevDay](</news/?tags=devday>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Art Card 1080x1080 \(3\)](https://images.ctfassets.net/kftzwdyauwt9/3JLNH7ejJFnxLmX2LpzoKD/19f9e3c4d36cc9d677ba88e842ad2db2/Art_Card_1080x1080__4_.png?w=3840&q=90&fm=webp)

Better memory for a more helpful ChatGPT

[Dreaming: Better memory for a more helpful ChatGPTResearchJun 4, 2026](</index/chatgpt-memory-dreaming/>)

![Rosalind5.5 ArtCard](https://images.ctfassets.net/kftzwdyauwt9/6USIQM1B7TggUvvTFxxwoi/0176ac6633c8bdc24641d25d1d2db824/GPT-Rosalind_ArtCard.png?w=3840&q=90&fm=webp)

[Introducing new capabilities to GPT-RosalindProductJun 3, 2026](</index/introducing-new-capabilities-to-gpt-rosalind/>)

![1 1 Art Card](https://images.ctfassets.net/kftzwdyauwt9/4xugzd9dTDMUzIUmuamtO3/1f40af4e50ab8b2bdd64d5b491964961/1_1_Art_Card.png?w=3840&q=90&fm=webp)

[Codex for every role, tool, and workflowProductJun 2, 2026](</index/codex-for-every-role-tool-workflow/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)
  * [GPT-5.3 Instant](</index/gpt-5-3-instant/>)



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



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
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
