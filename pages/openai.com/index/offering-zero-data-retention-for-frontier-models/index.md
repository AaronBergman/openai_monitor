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

August 19, 2026

[Company](</news/company-announcements/>)[Safety](</news/safety-alignment/>)

# Offering Zero Data Retention for frontier models

Previewing Private Safety Processing, which strengthens safeguards across interactions while remaining compatible with ZDR.

Loading…

Share

Why safety systems need to evolve

  * Why safety systems need to evolve
  * How Private Safety Processing works
  * Privacy and safety built with and for our customers



  * Why safety systems need to evolve
  * How Private Safety Processing works
  * Privacy and safety built with and for our customers



Zero Data Retention gives eligible API customers a clear promise: OpenAI does not retain their prompts or model responses after a request is processed. Customer content is not available to OpenAI personnel for review1, and enterprise customer data is not used to train our models unless customers explicitly opt-in.

As models take on longer, more complex tasks, some serious risks may only become visible across multiple interactions. Existing ZDR-compatible safety systems evaluate each interaction individually. Today, we’re previewing Private Safety Processing, which is designed to identify patterns across related interactions without giving OpenAI personnel access to the underlying content.

For ZDR deployments, customer content remains on infrastructure the customer controls. We are also developing an option in which content is stored on OpenAI infrastructure, encrypted with keys controlled by the customer. In both cases, automated systems can identify potential misuse and return limited safety signals without exposing the underlying prompts or responses to OpenAI personnel.

## Why safety systems need to evolve

The most serious AI safety risks are not always visible in a single interaction. Often, potentially harmful intentions become clear only when multiple interactions are viewed together. Similar risks can arise when bad actors repeatedly probe safeguards, coordinate across accounts, or disguise threats as routine research. Risks can also develop over the course of an agentic task—for example, if a system becomes misaligned with the user’s intent by continuing to act after being told to stop.

As AI systems take on longer and more complex tasks, this broader context becomes increasingly important for distinguishing legitimate activity from misuse and ensuring that AI agents remain within the bounds of their intended authority.

Some recent frontier-model deployments have required customers to allow their AI provider to retain sensitive content for safety monitoring. For many organizations, such requirements conflict with their security obligations or commitments to the people they serve.

Private Safety Processing is designed so we can continue to offer ZDR.

## How Private Safety Processing works

Private Safety Processing builds on the automated protections already used in ZDR and other deployments. Existing ZDR-compatible safety systems evaluate interactions individually. Private Safety Processing extends those protections across related interactions, allowing automated systems to identify patterns without OpenAI personnel having access to retained customer content.

Private Safety Processing utilizes customer content regardless of where it is stored—whether in infrastructure customers control (ZDR deployments) or in storage provided by OpenAI. With OpenAI-provided storage, customer content is encrypted using keys controlled by the customer. OpenAI personnel do not have a copy of those keys, so they cannot access the underlying content.

When a risk is identified, OpenAI receives a narrowly defined signal indicating the type of activity involved, similar to our existing safety systems today. That signal can be used to determine whether enforcement is necessary. OpenAI personnel do not receive access to the customer content even when it is flagged.

Customers can investigate alerts and enforcement decisions using information available in their own systems. If they want to appeal, clarify legitimate activity, or support an investigation into verified abuse, they can choose to share relevant information with OpenAI.

Private Safety Processing is currently being tested with early customers. We are sharing this preview now because we’ve heard our customers loud and clear that they need predictability about how their content will be protected as AI systems become more capable.

![Content Access Controls diagram showing an API request entering Private Safety Processing, with customer-controlled encrypted storage and automated safety review. Customers receive full alerts and may share content with OpenAI; OpenAI otherwise sees only alert category and severity, with no customer content.](https://images.ctfassets.net/kftzwdyauwt9/5ez53xtXgBu05Goa4LHIPO/0dec7c1a82fe6ac27865cdd2bdac9b59/desktop-light.svg?w=3840&q=90)

## Privacy and safety built _with_ and _for_ our customers

Our mission is to ensure that artificial general intelligence benefits all of humanity. Collaboration with customers and partners is essential to how we build effective safeguards. As [our principles](</index/our-principles/>) make clear, no AI lab can address emerging risks alone. Private Safety Processing reflects that approach and is being shaped by customers across industries, regions, and company sizes.

The organizations we work with handle some of the most sensitive information in their sectors, including financial records, health data, confidential business plans, and proprietary research. Protecting that information is essential to meeting regulatory obligations, maintaining customer trust, and preserving their competitive advantage.

Their feedback is helping us build stronger safeguards while keeping their information under their control.

GleanDatabricksAbridgeMicrosoft

“Enterprise AI adoption depends solely on customer control of data, with no direct or derivative use beyond the chosen service. OpenAI’s no-training commitment and ZDR give Glean confidence to build with OpenAI. As models become more capable, OpenAI shows safety can advance without compromising the privacy and control that sustain enterprise trust.”

—Sunil Agrawal, Chief Information Security Officer, Glean

We will continue working with customers on the technical and operational details of our approach. We plan to start rolling out Private Safety Processing, and share a technical white paper, in September. We’ll keep customers informed every step of the way, sharing updates early, explaining what they mean for existing commitments, and providing the time and support customers need to plan ahead.

  * [2026](</news/?tags=2026>)
  * [API Platform](</news/?tags=api-platform>)



## Author

OpenAI

  1. 1

Like other frontier model providers, OpenAI is [required by law⁠(opens in a new window)](<https://uscode.house.gov/view.xhtml?req=%28title%3A18+section%3A2258A+edition%3Aprelim%29>) to report apparent child sexual abuse material (CSAM). Images flagged for potential CSAM will continue to be retained for manual review and reporting purposes, even in Zero Data Retention deployments, as they are today.




## Keep reading

[View all](</news/>)

![The full stack behind abundant intelligence > Cover image](https://images.ctfassets.net/kftzwdyauwt9/4nRoI5iOfeV7qh4O3eAIEB/400545de8860b3c757548f2e3cd275fb/index-full-stack-behind-abundant-intelligence--cover-v001.png?w=3840&q=90&fm=webp)

[The full stack behind abundant intelligenceCompanyAug 25, 2026](</index/the-full-stack-behind-abundant-intelligence/>)

![Jalapeño inference — Art Card](https://images.ctfassets.net/kftzwdyauwt9/26K8mLbrpbaDvoFY0NrE04/8e4ad0b3f28042c22d6d5130bd4f4019/jalapeno-art-card.png?w=3840&q=90&fm=webp)

[Jalapeño’s first results show industry-leading speed and efficiency in AI inferenceEngineeringAug 25, 2026](</index/jalapeno-first-results/>)

![ChatGPT Ads expands across Europe - Card image](https://images.ctfassets.net/kftzwdyauwt9/IMh9E5WMDoVaUJyBJrsEP/697ba885d5e89b6bd27a55b9c9a783ae/chatgpt-ads-europe-readable-card.png?w=3840&q=90&fm=webp)

[ChatGPT Ads expands across EuropeProductAug 18, 2026](</index/chatgpt-ads-expands-across-europe/>)

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
