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

October 30, 2025

[Security](</news/security/>)[Product](</news/product-releases/>)[Research](</news/research/>)[Release](</research/index/release/>)

# Introducing Aardvark: OpenAI’s agentic security researcher

Now in private beta: an AI agent that thinks like a security researcher and scales to meet the demands of modern software.

Loading…

Share

How Aardvark works

  * How Aardvark works
  * Real impact, today
  * Aardvark for Open Source
  * Why it matters
  * Private beta now open



  * How Aardvark works
  * Real impact, today
  * Aardvark for Open Source
  * Why it matters
  * Private beta now open



** _March 6, 2026 Update:_**_Aardvark is now Codex Security, and is available as a research preview._

_Aardvark is now built directly into Codex as Codex Security, and is rolling out to ChatGPT Enterprise, Business, and Edu customers via Codex web with free usage for the next month. Please see our blog_[ _here._ ⁠](</index/codex-security-now-in-research-preview/>)

Today, we’re announcing Aardvark, an agentic security researcher powered by GPT‑5.

Software security is one of the most critical—and challenging—frontiers in technology. Each year, tens of thousands of new vulnerabilities are discovered across enterprise and open-source codebases. Defenders face the daunting tasks of finding and patching vulnerabilities before their adversaries do. At OpenAI, we are working to tip that balance in favor of defenders.

Aardvark represents a breakthrough in AI and security research: an autonomous agent that can help developers and security teams discover and fix security vulnerabilities at scale. Aardvark is now available in private beta to validate and refine its capabilities in the field.

## How Aardvark works

Aardvark continuously analyzes source code repositories to identify vulnerabilities, assess exploitability, prioritize severity, and propose targeted patches.

Aardvark works by monitoring commits and changes to codebases, identifying vulnerabilities, how they might be exploited, and proposing fixes. Aardvark does not rely on traditional program analysis techniques like fuzzing or software composition analysis. Instead, it uses LLM-powered reasoning and tool-use to understand code behavior and identify vulnerabilities. Aardvark looks for bugs as a human security researcher might: by reading code, analyzing it, writing and running tests, using tools, and more.

![Diagram titled “AARDVARK — Vulnerability Discovery Agent Workflow” showing a process flow from Git repository to threat modeling, vulnerability discovery, validation sandbox, patching with Codex, and human review leading to a pull request.](https://images.ctfassets.net/kftzwdyauwt9/4VNAPycxZna8DOgUmlDFuL/27336b0f378c3581ca9d3146bb18d84d/Aardvark_Overview_Diagram_Desktop_Light__2_.svg?w=3840&q=90)

Aardvark relies on a multi-stage pipeline to identify, explain, and fix vulnerabilities:

  * **Analysis** : It begins by analyzing the full repository to produce a threat model reflecting its understanding of the project’s security objectives and design.
  * **Commit scanning** : It scans for vulnerabilities by inspecting commit-level changes against the entire repository and threat model as new code is committed. When a repository is first connected, Aardvark will scan its history to identify existing issues. Aardvark explains the vulnerabilities it finds step-by-step, annotating code for human review.
  * **Validation** : Once Aardvark has identified a potential vulnerability, it will attempt to trigger it in an isolated, sandboxed environment to confirm its exploitability. Aardvark describes the steps taken to help ensure accurate, high-quality, and low false-positive insights are returned to users.
  * **Patching** : Aardvark integrates with OpenAI Codex to help fix the vulnerabilities it finds. It attaches a Codex-generated and Aardvark-scanned patch to each finding for human review and efficient, one-click patching.



Aardvark works alongside engineers, integrating with GitHub, Codex, and existing workflows to deliver clear, actionable insights without slowing development. While Aardvark is built for security, in our testing we’ve found that it can also uncover bugs such as logic flaws, incomplete fixes, and privacy issues.

## Real impact, today

Aardvark has been in service for several months, running continuously across OpenAI’s internal codebases and those of external alpha partners. Within OpenAI, it has surfaced meaningful vulnerabilities and contributed to OpenAI’s defensive posture. Partners have highlighted the depth of its analysis, with Aardvark finding issues that occur only under complex conditions.

In benchmark testing on “golden” repositories, Aardvark identified 92% of known and synthetically-introduced vulnerabilities, demonstrating high recall and real-world effectiveness.

## Aardvark for Open Source

Aardvark has also been applied to open-source projects, where it has discovered and we have responsibly disclosed numerous vulnerabilities—ten of which have received Common Vulnerabilities and Exposures (CVE) identifiers.

As beneficiaries of decades of open research and responsible disclosure, we’re committed to giving back—contributing tools and findings that make the digital ecosystem safer for everyone. We plan to offer pro-bono scanning to select non-commercial open source repositories to contribute to the security of the open source software ecosystem and supply chain.

We recently [_updated_ ⁠](<https://openai.com/index/scaling-coordinated-vulnerability-disclosure/>) our [_outbound coordinated disclosure policy_ ⁠](<https://openai.com/policies/outbound-coordinated-disclosure-policy/>) which takes a developer-friendly stance, focused on collaboration and scalable impact, rather than rigid disclosure timelines that can pressure developers. We anticipate tools like Aardvark will result in the discovery of increasing numbers of bugs, and want to sustainably collaborate to achieve long-term resilience.

## Why it matters

Software is now the backbone of every industry—which means software vulnerabilities are a systemic risk to businesses, infrastructure, and society. Over 40,000 CVEs were reported in 2024 alone. Our testing shows that around 1.2% of commits introduce bugs—small changes that can have outsized consequences.

Aardvark represents a new defender-first model: an agentic security researcher that partners with teams by delivering continuous protection as code evolves. By catching vulnerabilities early, validating real-world exploitability, and offering clear fixes, Aardvark can strengthen security without slowing innovation. We believe in expanding access to security expertise. We’re beginning with a private beta and will broaden availability as we learn.

## Private beta now open

We’re inviting select partners to join the Aardvark private beta. Participants will gain early access and work directly with our team to refine detection accuracy, validation workflows, and reporting experience.

We’re looking to validate performance across a variety of environments. If your organization or open source project is interested in joining, you can [apply here⁠](<https://www.openai.com/form/aardvark-beta-signup>).

  * [2025](</news/?tags=2025>)
  * [Cybersecurity](</news/?tags=cybersecurity>)



## Author

OpenAI

## Contributors

Akshay Bhat, Andy Nguyen, Dave Aitel, Harold Nguyen, Ian Brelinsky, Tiffany Citra, Xin Hu, Matt Knight

## Keep reading

[View all](</news/>)

![images2point5 1-1](https://images.ctfassets.net/kftzwdyauwt9/6C1icjo4Zz6MzpbQl1K2qx/8bf8ec06aae235d81019c24f6098d2f0/images2point5_1-1c.png?w=3840&q=90&fm=webp)

[Introducing ChatGPT Images 2.5ProductSep 8, 2026](</index/introducing-chatgpt-images-2-5/>)

![Navier–Stokes solution — art card](https://images.ctfassets.net/kftzwdyauwt9/2VUQZfeF2GtKRitKYdkoLu/cc96d05424afb2c9adcca0734ecdafb1/navier-stokes-art-card.png?w=3840&q=90&fm=webp)

[An OpenAI model proposes a solution to the Navier–Stokes problemResearchSep 8, 2026](</index/navier-stokes-solution/>)

![An alien mind > Listing card](https://images.ctfassets.net/kftzwdyauwt9/7ut3G8rKt5ia4P3yRqi2qN/6ffb429f70548a881eb46a4e7e61498e/Option_120___1080_1080.png?w=3840&q=90&fm=webp)

[An Alien MindSafetySep 6, 2026](</index/an-alien-mind/>)

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
