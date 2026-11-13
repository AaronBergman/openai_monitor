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

November 10, 2026

Startup

# Cogent and OpenAI build cyber defense factories for enterprises

Cogent combines OpenAI models with enterprise context to help automatically remediate vulnerabilities with agents.

[Start building with OpenAI](</startups/>)

![White Cogent logo over a dark brushed-metal surface with a warm sienna reflection.](https://images.ctfassets.net/kftzwdyauwt9/1b77wWqxMlNBg59VRDTuuQ/46601ae75270e4d037359127eb09a76c/cogent-security-cover-sienna.png?w=3840&q=90&fm=webp)

Company size: Startup

Region: North America

Industry: Technology

Products: API, Codex, Daybreak

75%

Lower mean time to remediate vulnerabilities

5x

More vulnerabilities triaged

Share

Giving agents context and permission to act

  * Giving agents context and permission to act
  * From vulnerability disclosure to verified fixes
  * Why Cogent builds with OpenAI models and Codex
  * Expanding autonomous cyber defense



  * Giving agents context and permission to act
  * From vulnerability disclosure to verified fixes
  * Why Cogent builds with OpenAI models and Codex
  * Expanding autonomous cyber defense



As [Cogent Security⁠(opens in a new window)](<https://www.cogent.com/>) sees enterprises facing more security risks than ever, it has found that the hardest part is not finding vulnerabilities, but fixing them. Remediation work is complex and spans multiple teams. It requires contextual understanding of a company’s environment: how could an attacker exploit a vulnerability, which business systems are at stake, and what changes can be made safely.

Cogent builds Cyber Defense Factories for enterprises to autonomously find and eliminate those risks. The factories are designed to help defenders move at machine speed, in response to the acceleration in vulnerability discovery and exploitation.

The company’s AI agents combine GPT‑6.1 Sol and GPT‑5.6 with its enterprise context and controls to handle investigation through verified remediation. The agents assess exposures, execute permitted changes, and confirm the risk has been eliminated. Cogent also conducts internal research with Cyber and Daybreak, exploring attack paths and defensive capabilities.

> “The ability of OpenAI models to sustain long-running tasks unlocks a new level of autonomy in enterprise defense: AI agents can now carry work from investigation through verified remediation.”

—Geng Sng, Co-founder and CTO, Cogent

![Cogent Cyber Defense Factory connects enterprise cloud, code, endpoints, identity, and scanner data to agents that investigate, prioritize, remediate, and verify risk, powered by OpenAI models, context, and customer controls.](https://images.ctfassets.net/kftzwdyauwt9/78WRVzMMXnkXRcl48nSNt/b37e2ab0da4eadbeca2e6a5ae384d248/cogent-security-diagram-light.png?w=3840&q=90&fm=webp)

## Giving agents context and permission to act

For each customer, Cogent’s Context Engine maintains an enterprise knowledge graph of assets, vulnerabilities, identities, ownership, and dependencies. Specialized background agents continuously reconcile information across security tools and systems, giving investigation and remediation agents a shared understanding of the environment.

GPT‑6 Astra handles upfront planning and complex reasoning for that work. This enables what Geng Sng, Co-founder and CTO of Cogent, describes as a “memory harness for the enterprise.” He says, “We don’t have to relearn what the world looks like every time a new task happens.” Reusing context reduces latency, inference costs, and inconsistent results.

Cogent’s Agent Policies define each enterprise’s permitted changes and approval requirements, and its policy-enforcement engine, TRACE, checks tool calls against the policies before execution. The checks are deterministic and require no separate model inference.

An Agent Gateway independently checks authorization, and higher-risk work can run in isolated sandboxes. Customers can delegate investigation, require approval for changes, or permit bounded autonomous remediation.

## From vulnerability disclosure to verified fixes

When critical security flaws known as PHP2Shell were disclosed in PHP, a programming language used to run websites, customers turned to the Cyber Defense Factories that Cogent had already deployed in their environments.

GPT‑6.1 Sol and GPT‑6 Astra provided the deep reasoning for investigation and remediation planning. Using Cogent’s context layer, agents identified affected systems, assessed exposure, and developed plans that accounted for application dependencies and operational constraints. Then they orchestrated fixes using customer-defined approval and execution workflows and verified the resolution.

Cogent reports that customers are using its Cyber Defense Factories to resolve vulnerabilities faster and expand investigation capacity. With Cogent, a Fortune 1000 automotive customer reduced its mean time to remediate critical vulnerabilities by 75%, and a Fortune 500 IT services customer achieved 5× vulnerability-triage throughput.

Trading platform MarketAxess says Cogent helps it decide which exposures to fix first: “Cogent sees our environment the way an attacker would. It traces the route from the internet to a vulnerable system and checks controls on the way. Our remediation work now focuses on the greatest risks and the paths an adversary could use to break in,” says Vijay Bala, Global CISO at MarketAxess.

## Why Cogent builds with OpenAI models and Codex

Cogent continuously evaluates closed-source and open-source alternatives and reports stronger reasoning on long-running security tasks, higher fidelity, fewer hallucinations on technical codebases, and more reliable execution with OpenAI models. The models can chain tool calls sequentially and in parallel while retaining context across remediation workflows.

Cogent prioritizes reasoning quality for complex investigations and cost for more straightforward work. It uses GPT‑6.1 Sol for general execution and GPT‑5.6 for routine vulnerability-management tasks where advanced reasoning is less critical.

> “OpenAI models are more cost-efficient relative to the other providers. That’s a big plus for us, especially if we’re running these huge agent swarms.”

—Geng Sng, Co-founder and CTO, Cogent

Using OpenAI models has also reduced the supporting software Cogent needs to build for remediation and patching. “A lot of the work that we had to do at the harness level is no longer required,” Geng says. He also shared that OpenAI APIs have “streamlined request routing and agent orchestration, significantly reducing internal engineering overhead and accelerating our time-to-market for complex security workflows.”

Most of Cogent’s engineers also choose Codex for development. Geng says they’re more productive pairing Codex with OpenAI models vs. using the same models in an open-source coding environment. “Codex just comes with tools that we don’t have to build ourselves,” says Geng.

## Expanding autonomous cyber defense

Through Trusted Access for Cyber and Daybreak, Cogent receives technical support for its internal red-teaming and attack-path research. Daybreak Red, an access tier within Daybreak, provides the team with specialized OpenAI models for authorized offensive and vulnerability research. “Good defense requires good offense,” Geng says.

> “Through Trusted Access for Cyber and Daybreak, we can explore how vulnerabilities could be chained across identities, resources, and network controls. We use that research to understand what our agents can do and which defensive capabilities to build next.”

—Geng Sng, Co-founder and CTO, Cogent

Cogent plans to expand its capabilities as the key partner for enterprises to build their own Cyber Defense Factories. Its roadmap includes increasingly autonomous remediation, broadening the range and complexity of fixes agents can execute, from straightforward configuration changes to multi-step workflows spanning different enterprise systems.

The company is also developing autonomous discovery and validation. Its goal is a closed-loop system that finds and eliminates risk while continuously learning from every vulnerability to improve future investigations and fixes.

## OpenAI <3 startups

[Join the community](</leads/startup/>)[Start building(opens in a new window)](</startups>)

## Keep reading

[View all](</news/>)

![Gondola — art card and hero](https://images.ctfassets.net/kftzwdyauwt9/5B8tYqcVtztQ9PNAvMLPLO/8f2fc1472cb497b2d2b8ff82c0c1eeba/Gondola-Option-A-Art-Card-1080x1080.png?w=3840&q=90&fm=webp)

[Gondola doubles revenue as its team builds more with CodexStartupNov 12, 2026](</business/customer-stories/gondola/>)

![CodeRabbit — Indigo texture art card](https://images.ctfassets.net/kftzwdyauwt9/1YFM9mFKP6ZzABichElFUi/9a6569f02f982f80d80941019f522a99/coderabbit-art-card-1080x1080.png?w=3840&q=90&fm=webp)

[CodeRabbit scales agentic software development and ships 20x moreStartupNov 9, 2026](</index/coderabbit-codex-daybreak/>)

![DevRev — Layered paper art card](https://images.ctfassets.net/kftzwdyauwt9/36lbF0ijotVJ7zCUyEf21D/842824cd2382520c374de4bad52759fb/square.png?w=3840&q=90&fm=webp)

[DevRev delivers autonomous self-service with GPT-6.1 SolStartupNov 4, 2026](</index/devrev-enterprise-self-service/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)



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
  * [Codex](<https://chatgpt.com/codex/>)
  * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Plugins](</business/plugins/>)
  * [Customer Stories](</business/customer-stories/>)
  * [Partner Network](</business/partners/>)
  * [Contact Sales](</contact-sales/>)



Developers

  * [Plugins(opens in a new window)](<https://developers.openai.com/plugins>)
  * [Models(opens in a new window)](<https://developers.openai.com/api/docs/models>)
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
  * [OpenAI Status(opens in a new window)](<https://status.openai.com>)



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
