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

  * Helping organizations protect employees most at-risk of cyberattacks
  * Helping users make informed choices about risk
  * What’s next



February 13, 2026

[Safety](</news/safety-alignment/>)[Product](</news/product-releases/>)

# Introducing Lockdown Mode and Elevated Risk labels in ChatGPT

Loading…

Share

 _**Update June 4, 2026:**__Lockdown Mode is rolling out to personal ChatGPT accounts as well as self-serve ChatGPT Business accounts. First introduced for ChatGPT enterprise plans, Lockdown Mode is an optional setting for people and teams who want a more conservative ChatGPT experience when working with sensitive information or connected features._

_Lockdown Mode is designed for users with higher security needs, or for moments when users are willing to trade elements of product functionality for stricter product guardrails. When enabled, it limits or turns off certain features that connect ChatGPT to the web or external services, including live web access, image support in responses, Deep Research including shopping research, Agent Mode, Canvas networking, live connectors, and file downloads. This reduces the ways prompt-injection-style attacks could cause information to be shared outside the conversation. Personal users can turn it on from Settings > Security._

_This is part of our broader defense-in-depth approach: as ChatGPT becomes more capable and connected, we’re continuing to add practical protections that give users more choice over how ChatGPT works with sensitive information and connected features._

* * *

As AI systems take on more complex tasks—especially those that involve the web and connected apps—the security stakes change. 

One emerging risk has become especially important: [_prompt injection_ ⁠](<https://openai.com/index/prompt-injections/>). In these attacks, a third party attempts to mislead a conversational AI system into following malicious instructions or revealing sensitive information.

Today, we’re introducing two new protections designed to help users and organizations mitigate prompt injection attacks, with clearer visibility into risk and stronger controls:

  * **Lockdown Mode** in ChatGPT, an advanced, optional security setting for higher-risk users
  * **“Elevated Risk” labels** for certain capabilities in ChatGPT, ChatGPT Atlas, and Codex that may introduce additional risk



These additions build on our existing protections across the model, product, and system levels. This includes sandboxing, [_protections against URL-based data exfiltration_ ⁠](<https://openai.com/index/ai-agent-link-safety/>), monitoring and enforcement, and [_enterprise controls_ ⁠](<https://openai.com/business-data/>) like role-based access and audit logs. 

## Helping organizations protect employees most at-risk of cyberattacks

Lockdown Mode is an optional, advanced security setting designed for a small set of highly security-conscious users—such as executives or security teams at prominent organizations—who require increased protection against advanced threats. It is not necessary for most users. Lockdown Mode tightly constrains how ChatGPT can interact with external systems to reduce the risk of prompt injection–based data exfiltration.

Lockdown Mode deterministically disables certain tools and capabilities in ChatGPT that an adversary could attempt to exploit to exfiltrate sensitive data from users’ conversations or connected apps via attacks such as prompt injections.

For example, web browsing in Lockdown Mode is limited to cached content, so no live network requests leave OpenAI’s controlled network. This restriction is designed to prevent sensitive data from being exfiltrated to an attacker through browsing. Some features are disabled entirely when we can’t provide strong deterministic guarantees of data safety. 

![Diagram titled “Lockdown mode” showing ChatGPT inside a secured boundary with connections to a Private Web Cache, Download Files, Access Web via Canvas, and Browse Public Web. An external “Attacker” and the Public Web are depicted outside the boundary, with blocked entry points indicating restricted access in lockdown mode.](https://images.ctfassets.net/kftzwdyauwt9/Sd0XJWPIZgNG26UbK70Kl/05d80e59423f9d313c187396a504c9a4/Lockdown_mode__light_mode.png?w=3840&q=90&fm=webp)

Lockdown Mode is a new deterministic setting that helps guard data from being inadvertently shared with third parties by tightly constraining how ChatGPT can interact with certain external systems. 

ChatGPT business plans already provide [_enterprise-grade data security_ ⁠](<https://openai.com/business-data/>). Lockdown Mode builds on those protections and is available for ChatGPT Enterprise, ChatGPT Edu, ChatGPT for Healthcare, and ChatGPT for Teachers. Admins can enable it in [_Workspace Settings_ ⁠(opens in a new window)](<https://chatgpt.com/admin/permissions?tab=roles>) by creating a new [_role_ ⁠(opens in a new window)](<https://help.openai.com/en/articles/11750701-rbac>). When enabled, Lockdown Mode layers additional restrictions on top of existing admin settings. 

Learn more about Lockdown Mode in our [_Help Center_ ⁠(opens in a new window)](<https://help.openai.com/articles/20001061>). 

Because some critical workflows rely on apps, Workspace Admins retain more granular controls. They can choose exactly which apps—and which specific actions within those apps—are available to users in Lockdown Mode. Additionally, and separate from Lockdown Mode, the [_Compliance API Logs Platform_ ⁠(opens in a new window)](<https://help.openai.com/en/articles/9261474-compliance-api-for-enterprise-customers>) provides detailed visibility into app usage, shared data, and connected sources, helping admins maintain oversight.

We plan to make Lockdown Mode available to consumers in the coming months.

## Helping users make informed choices about risk

AI products can be more helpful when connected to your apps and the web, and we’ve invested heavily in [_keeping connected data secure_ ⁠](<https://openai.com/safety/prompt-injections/>). At the same time, some network-related capabilities introduce new risks that aren’t yet fully addressed by the industry’s safety and security mitigations. Some users may be comfortable taking on these risks, and we believe it’s important for users to have the ability to decide whether and how to use them, especially while working with their private data.

Our approach has been to provide in-product guidance for features that may introduce additional risk. To make this clearer and more consistent, we’re standardizing how we label a short list of existing capabilities. These features will now use a consistent “Elevated Risk” label across ChatGPT, ChatGPT Atlas, and Codex, so users receive the same guidance wherever they encounter them. 

For example, in Codex, our coding assistant, developers can grant Codex network access so it can take actions on the web like looking up documentation. The relevant settings screen includes the “Elevated Risk” label, along with a clear explanation of what changes, what risks may be introduced, and when that access is appropriate.

![Settings panel for “Agent internet access” with the toggle set to On, showing options for a domain allowlist, additional allowed domains \(including openai.com\), allowed HTTP methods, and a highlighted warning noting elevated security risks when enabling internet access.](https://images.ctfassets.net/kftzwdyauwt9/2S6DegQI10grUrX1DVMNFH/fad0af938de1c38826c374a9708208e3/Lockdown-Mode_Blog-inline.png?w=3840&q=90&fm=webp)

A screenshot of the Codex settings screen where users can configure what network access Codex has.

## What’s next

We continue to invest in strengthening our safety and security safeguards, especially for novel, emerging, or growing risks. As we strengthen the safeguards for these features, we will remove the “Elevated Risk” label once we determine that security advances have sufficiently mitigated those risks for general use. We will also continue to update which features carry this label over time to best communicate risk to users.

  * [2026](</news/?tags=2026>)



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
