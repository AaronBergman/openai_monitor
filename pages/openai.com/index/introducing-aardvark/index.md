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

  * How Aardvark works
  * Real impact, today
  * Aardvark for Open Source
  * Why it matters
  * Private beta now open



October 30, 2025

[Security](</news/security/>)[Product](</news/product-releases/>)[Research](</news/research/>)[Release](</research/index/release/>)

# Introducing Aardvark: OpenAI’s agentic security researcher

Now in private beta: an AI agent that thinks like a security researcher and scales to meet the demands of modern software.

Loading…

Share

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

Aardvark represents a new defender-first model: an agentic security researcher that partners with teams by delivering continuous protection as code evolves. By catching vulnerabilities early, validating real-world exploitability, and offering clear fixes, Aardvark can strengthen security without slowing innovation. We believe in expanding access to security expertise. We're beginning with a private beta and will broaden availability as we learn.

## Private beta now open

We’re inviting select partners to join the Aardvark private beta. Participants will gain early access and work directly with our team to refine detection accuracy, validation workflows, and reporting experience.

We’re looking to validate performance across a variety of environments. If your organization or open source project is interested in joining, you can [apply here⁠](<https://www.openai.com/form/aardvark-beta-signup>).

  * [2025](</news/?tags=2025>)



## Author

OpenAI

## Contributors

Akshay Bhat, Andy Nguyen, Dave Aitel, Harold Nguyen, Ian Brelinsky, Tiffany Citra, Xin Hu, Matt Knight

## Keep reading

[View all](</news/>)

![1x1](https://images.ctfassets.net/kftzwdyauwt9/6ui4uYfTTbR4xbiFRcqEfo/81d973f14bea720820f692271f6c6834/square.png?w=3840&q=90&fm=webp)

[Strengthening societal resilience with Rosalind BiodefenseProductMay 29, 2026](</index/strengthening-societal-resilience-with-rosalind-biodefense/>)

![Geometry > ArtCard > Polynomial Construction](https://images.ctfassets.net/kftzwdyauwt9/6PqehRMmS1oVuin6e3VWYq/b96f1c7b5a2ac2c08a887591b8486ed3/ArtCard-Polynomial-Construction.png?w=3840&q=90&fm=webp)

[An OpenAI model has disproved a central conjecture in discrete geometryResearchMay 20, 2026](</index/model-disproves-discrete-geometry-conjecture/>)

![Personal finance in ChatGPT > Media > Cover](https://images.ctfassets.net/kftzwdyauwt9/4zSr4YNWXIEYz20piN2bxf/6f9a561be6055802914aee0a3bb671d7/ArtCard-Personal-Finance.png?w=3840&q=90&fm=webp)

[A new personal finance experience in ChatGPTProductMay 15, 2026](</index/personal-finance-chatgpt/>)

Our Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Research Residency](</residency/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)
  * [GPT-5.3 Instant](</index/gpt-5-3-instant/>)
  * [GPT-5.3-Codex](</index/introducing-gpt-5-3-codex/>)



Safety

  * [Safety Approach](</safety/>)
  * [Security & Privacy](</security-and-privacy/>)
  * [Trust & Transparency](</trust-and-transparency/>)



ChatGPT

  * [Explore ChatGPT(opens in a new window)](<https://chatgpt.com/overview>)
  * [Business](<https://chatgpt.com/business/business-plan>)
  * [Enterprise](<https://chatgpt.com/business/enterprise>)
  * [Education](<https://chatgpt.com/business/education>)
  * [Pricing(opens in a new window)](<https://chatgpt.com/pricing>)
  * [Download(opens in a new window)](<https://chatgpt.com/download>)



API Platform

  * [Platform Overview](</api/>)
  * [Pricing](</api/pricing/>)
  * [API log in(opens in a new window)](<https://platform.openai.com/login>)
  * [Documentation(opens in a new window)](<https://developers.openai.com/api/docs>)
  * [Developer Forum(opens in a new window)](<https://community.openai.com/>)



For Business

  * [Business Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Contact Sales](</contact-sales/>)



Company

  * [About Us](</about/>)
  * [Our Charter](</charter/>)
  * [Foundation(opens in a new window)](<https://openaifoundation.org>)
  * [Careers](</careers/>)
  * [Brand](</brand/>)



Support

  * [Help Center(opens in a new window)](<https://help.openai.com/>)



More

  * [News](</news/>)
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
