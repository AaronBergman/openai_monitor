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

September 8, 2026

# 1Password increases engineering productivity 21% with Codex

Engineers at 1Password use Codex to rapidly build new features and internal tools, reaching production-readiness while maintaining rigorous security policies.

[Contact sales](</contact-sales/>)

![OpenAI and 1Password logos alongside dark woven fibers.](https://images.ctfassets.net/kftzwdyauwt9/6IJsWuQa1blfxNfvbdIF1m/0868067102440aea5fd1ad35ba436a77/square.png?w=3840&q=90&fm=webp)

Company size: Enterprise

Region: North America

Industry: Technology

Products: Codex

20.9%

Measured productivity improvement among the Codex user cohort

10.9%

Reduction in median pull request cycle time

~90%

Reduction in investigation time on a complex, multi-service production issue

$0.8M

Estimated annual engineering capacity value from Codex

Loading…

Share

One-shotting new features with Codex

  * One-shotting new features with Codex
  * Codex across the software delivery lifecycle
  * Results at a glance
  * Maintaining security as the speed of development rises
  * What's next



  * One-shotting new features with Codex
  * Codex across the software delivery lifecycle
  * Results at a glance
  * Maintaining security as the speed of development rises
  * What's next



1Password has integrated Codex across the software delivery lifecycle to compress the time between planning and production, allowing it to build new features at a rapid pace. The 1Password team has cut median pull request cycle time by nearly 11% and improved engineering productivity by almost 21% for its core user cohort.

Based on engineering's results, 1Password's leadership team is expanding access to Codex to other functions, enabling teams such as finance and marketing to build their own tools and features. Throughout, 1Password maintained its rigorous security standards, ensuring there's no tradeoff between increasing its speed and protecting its data.

> “What’s been really eye-opening for a lot of our engineers is shortening the lifecycle between planning and being able to see a feature in production.”

—Nancy Wang, CTO, 1Password

## One-shotting new features with Codex

1Password is using Codex to move ideas from planning to implementation faster, helping engineers turn well-defined user stories into working features.

“Previously, you would go into a project, think about how to break it down into different sprints, and assign different sprints to engineering scrum teams,” explains Nancy Wang, CTO at 1Password. “With Codex, you can actually one-shot, going from an idea to a prototype to a feature that works fully in production.”

“For our workflow, Codex made it faster and easier to one-shot features by giving it a user story and instructions about what we want the user to experience, reducing the iteration required before engineering review,” Wang says.

This work has resulted in numerous new features, both internal tools and customer-facing products. One example is Knox, a fully agentic frontend design system that helps teams at 1Password build new interfaces. Other examples include an internal AI site reliability engineering (SRE) agent and an AI spend management tool.

1Password gives Codex room to work autonomously inside clearly defined engineering and security boundaries. “Codex will actually break the requested feature down into functional specs and build a near-final prototype that then we can hand to our systems engineers to build into our backend,” Wang says. This approach reduced handoff time and improved engineering productivity. Engineers are writing code faster and spending less time on the handoffs between planning, implementation, and review.

## Codex across the software delivery lifecycle

Codex touches every step from planning to production:

  * Planning and technical design: Turns requests into specs, dependency checks, and work items.
  * Implementation across stacks: Helps engineers navigate unfamiliar Rust and TypeScript code via CLI; parallel worktrees run tasks simultaneously.
  * Pull request review: Reviews changes before a human, flags logic issues and missing context.
  * Testing and release readiness: Runs acceptance criteria and automated tests in parallel with other work.
  * Security and access: Ties into 1Password's internal AppSec harness; secret references keep plaintext credentials out of model context.
  * Production investigation: Pulls evidence across incident management, telemetry, source control, paging, and feature flags.



## Results at a glance

![1Password modeled annual engineering capacity value with Codex: $783,750. Model assumptions are provided in the caption.](https://images.ctfassets.net/kftzwdyauwt9/1Yw8uIdULnssM69f1VakL3/5c50a23cd7bb8e5325c5138ec2d1595b/1password-results-requested.png?w=3840&q=90&fm=webp)

Modeled annual engineering capacity value: $783,750, based on 50 consistently active Codex developers, a $250,000 fully loaded annual cost per developer, 20.9% measured productivity improvement, 40% directional Codex attribution, and 75% realization of productive capacity.

As 1Password integrated Codex across its software development lifecycle, engineering teams recorded a 20.9% productivity improvement and a 10.9% reduction in median pull request cycle time. An engineer contributing outside their usual stack cut a typical three-day merge down to one day, and a team facing a fixed beta launch date completed four release-critical tickets instead of the roughly two they would normally expect.

For a defect spanning more than 10 microservices, investigation time fell from about two hours to 5–20 minutes. For a modeled cohort of 50 Codex users, 1Password estimates approximately $784,000 in annual engineering capacity and a 553% ROI, with capacity reinvested in product development and internal innovation. At 100 consistent users, the modeled annual capacity value could reach approximately $3.1 million, assuming Codex accounts for a larger share of the measured productivity improvement.

> “If we can actually speed up that feedback loop between customer feedback and making quick changes in our UI, that’s going to really unlock a lot of things for the business.”

—Nancy Wang, CTO, 1Password

## Maintaining security as the speed of development rises

1Password is also rolling out OpenAI tools to finance, marketing, and other teams, where the chat interface has become second nature.

For 1Password, its security model is a design requirement for adoption, not a control to add after usage expands. “We have a very stringent security posture in terms of how we build products,” Wang says. Any product that touches credentials or secrets, for example, needs to adhere to a zero-knowledge architecture designed so that only the customer can decrypt and access their sensitive data.

1Password implements that principle by keeping secret references, rather than credentials, in repositories. When Codex calls an approved internal tool, 1Password resolves and injects the credential at the point of action, so the plaintext value never enters the model context.

To further strengthen security, 1Password engineers have also taken the company's security policies and “baked that into reusable AppSec skills,” allowing the company's standards to travel with the development workflow, Wang explains. “That's been a game changer.”

## What's next

Wang and the 1Password team see software production becoming more accessible in the near future through “democratized building”: more roles can build software. If the first wave was about engineers becoming AI-assisted builders, Wang says, “We're now squarely in the second wave. Everyone in product, design, research, and development is becoming builders. PMs are starting to ship products, and designers are starting to ship front-end code.”

Wang predicts this trend spreading across every role. “I think the last mile is actually getting everybody in a company to build,” she says. “That's what we're going to see over the next 12 months, folks who are traditionally not writing code or who don't think of themselves as builders becoming so comfortable with AI tools that they can ship code confidently.”

## Join the new era of work

More than 1 million businesses around the world are achieving meaningful results with OpenAI.

[Contact sales](</contact-sales/>)

## Keep reading

![How Codex helps run quantum computing experiments — Art card](https://images.ctfassets.net/kftzwdyauwt9/2Kovot5B2upbAxiLOfbEIO/464b5e73306e047fa31f8456acb34fa3/art-card.png?w=3840&q=90&fm=webp)

[How GPT-5.6 Sol helps run quantum computing experimentsApplied AISep 8, 2026](</index/codex-quantum-computing-experiments/>)

![The Work Now Within Reach — clean cover](https://images.ctfassets.net/kftzwdyauwt9/5iHLTPM4ZhKe4dAwOPfpy2/347b9d804542685bb13dbb63e985d91e/c3f562e2b08a0bfc.png?w=3840&q=90&fm=webp)

[The Work Now Within ReachCompanySep 8, 2026](</index/the-work-now-within-reach/>)

![images2point5 1-1](https://images.ctfassets.net/kftzwdyauwt9/6C1icjo4Zz6MzpbQl1K2qx/8bf8ec06aae235d81019c24f6098d2f0/images2point5_1-1c.png?w=3840&q=90&fm=webp)

[Introducing ChatGPT Images 2.5ProductSep 8, 2026](</index/introducing-chatgpt-images-2-5/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6](</index/gpt-6-astra/>)
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
