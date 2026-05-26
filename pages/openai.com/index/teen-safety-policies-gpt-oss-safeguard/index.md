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

  * Building on our broader work to protect young people
  * Translating teen safety into clear, usable policies
  * Helping developers operationalize teen safety
  * Developed with input from external experts
  * A starting point, not a complete solution
  * The road forward 



March 24, 2026

[Safety](</news/safety-alignment/>)

# Helping developers build safer AI experiences for teens

Introducing a set of teen safety policies formatted as prompts for gpt-oss-safeguard

Loading…

Today, we’re releasing prompt-based [_safety policies_ ⁠(opens in a new window)](<https://github.com/openai/teen-safety-policy-pack>) to help developers create age-appropriate protections for teens. Built to work with our open-weight safety model, [_gpt-oss-safeguard_ ⁠(opens in a new window)](<https://huggingface.co/openai/gpt-oss-safeguard-20b>), these policies simplify how developers turn safety requirements into usable classifiers for real-world systems.

We released open weight models to democratize access to powerful AI and support broad innovation. At the same time, we believe safety and innovation go hand in hand, and that developers should have access to capable models as well as the tools and policies to deploy them safely and responsibly. We developed these policies to support developers in their safety efforts to protect young users, with input from trusted external organizations including [_Common Sense Media_ ⁠(opens in a new window)](<https://www.commonsensemedia.org>) and [_everyone.ai_ ⁠(opens in a new window)](<http://everyone.ai>).

We recognize that teens and adults have different needs, and that teens need additional protections. These policies are designed to help developers account for those differences and build experiences that are both empowering and appropriate for younger users.

#### Building on our broader work to protect young people

We have long been committed to building AI that expands opportunities for young people while keeping them safe. As part of this work, we updated our [_Model Spec_ ⁠(opens in a new window)](<https://model-spec.openai.com/2025-12-18.html>)—the guidelines that define the intended behavior of OpenAI’s models—to include [_Under-18 (U18) principles_ ⁠(opens in a new window)](<https://model-spec.openai.com/2025-12-18.html#chatgpt_u18>), and introduced product-level safeguards such as [_parental controls_ ⁠](<https://openai.com/index/introducing-parental-controls/>) and [_age prediction_ ⁠](<https://openai.com/index/our-approach-to-age-prediction/>) to better protect younger users. We have also called for industry-wide protections through our [_Teen Safety Blueprint_ ⁠](<https://openai.com/index/introducing-the-teen-safety-blueprint/>).

Today’s release builds on that foundation. We’re making these safety policies available to developers to support them in deploying safety protections for teens and helping democratize access across the open weights ecosystem. 

#### Translating teen safety into clear, usable policies

While safety classifiers like gpt-oss-safeguard can detect harmful content, they depend on clear definitions of what that content is. In practice, one of the biggest challenges developers face is defining policies that accurately capture teen-specific risks and can be consistently applied in real systems.   
  
Even experienced teams often struggle to translate high-level safety goals into precise, operational rules, especially since it requires both subject matter expertise and deep AI knowledge. This can lead to gaps in protection, inconsistent enforcement, or overly broad filtering. Clear, well-scoped policies are a critical foundation for effective safety systems.

#### Helping developers operationalize teen safety

To address this challenge, we are releasing a set of [_safety policies_ ⁠(opens in a new window)](<https://github.com/openai/teen-safety-policy-pack>), tailored to common risks faced by teens and informed by careful review of existing research about teens’ unique developmental differences. These policies are structured as prompts that can be directly used with [_gpt-oss-safeguard_ ⁠(opens in a new window)](<https://huggingface.co/openai/gpt-oss-safeguard-20b>) and other reasoning models, enabling developers to more easily apply consistent safety standards across their systems. 

The initial release includes policies covering:

  * Graphic violent content
  * Graphic sexual content
  * Harmful body ideals and behaviors
  * Dangerous activities and challenges
  * Romantic or violent roleplay
  * Age-restricted goods and services



These policies can be used for real-time content filtering, as well as offline analysis of user-generated content.

By structuring policies as prompts, developers can more easily integrate them into existing workflows, adapt them to their use cases, and iterate over time.

![Diagram depicting teen safety policy categories and teen-related content feeding into a GPT-OSS safeguard system, which produces policy decisions informed by internal reasoning.](https://images.ctfassets.net/kftzwdyauwt9/tpc83mGxV22vPETJsE3DO/998e3a19c99a6dc13bb285282a4dd583/Translating_safety_policies_into_enforceable_safeguards.png?w=3840&q=90&fm=webp)

#### Developed with input from external experts

We worked with external organizations including [_Common Sense Media_ ⁠(opens in a new window)](<https://www.commonsensemedia.org>) and [_everyone.ai_ ⁠(opens in a new window)](<http://everyone.ai>) to inform the development of these policies. Their expertise helped shape the scope of content to cover, strengthen the structure of the prompts, and refine the edge cases to consider when evaluating them. 

This work reflects an ongoing effort to collaborate with experts and the broader ecosystem to improve how AI systems support young people.

_“One of the biggest gaps in AI safety for teens has been the lack of clear, operational policies that developers can build from. Many times, developers are starting from scratch. These prompt-based policies help set a meaningful safety floor across the ecosystem, and because they 're released as open source, they can be adapted and improved over time. We're encouraged to see this kind of infrastructure being made available broadly, and we hope it catalyzes more shared youth-safety starting points across the industry.” _

—**Robbie Torney, Head of AI & Digital Assessments, Common Sense Media**

 _“Efforts like this that make youth safety policies more operational are valuable because they help translate expert knowledge into guidance that can be used in real systems. Content policies are an important first step, and they also open the door to broader work on how model behavior can shape youth-relevant risks over time. Inspired by this work and our own research,_[_everyone.ai_ ⁠(opens in a new window)](<http://everyone.ai/>)_has also created an initial behavioral policy focused on risks like exclusivity and overreliance. "_

_—_**Dr. Mathilde Cerioli, Chief Scientist at everyone.AI**

####  A starting point, not a complete solution

The policies are intended as a starting point, not as a comprehensive or final definition or guarantee of teen safety. Each application has unique risks, audiences and contexts, and developers are best positioned to understand the risks that their products and AI integrations may present. We strongly encourage developers to adapt and extend these policies based on their specific needs and combine them with other safeguards such as product design decisions, user controls, teen-friendly transparency, monitoring systems and thoughtful, age-appropriate responses. 

We believe a layered [_defense in depth⁠_ ⁠](<https://openai.com/safety/how-we-think-about-safety-alignment/#defense-in-depth>) approach is essential to building safer AI systems. These policies draw from our internal experience, but they do not reflect the full extent of OpenAI’s internal policies or safeguards. 

#### The road forward 

We are releasing these policies as open source through the [_ROOST Model Community_ ⁠(opens in a new window)](<https://github.com/roostorg/model-community>) to encourage collaboration and iteration. To contribute, provide feedback, or share additional teen safety policies, visit the [_RMC GitHub repository._ ⁠(opens in a new window)](<https://github.com/roostorg/open-models>)

Developers and organizations can adapt these policies to their specific applications, translate them into different languages, and extend them to cover additional risk areas. Over time, we hope this contributes to a more robust and shared foundation for implementing safety policies in AI systems.

To get started with gpt-oss-safeguard, download it from [_Hugging Face_ ⁠(opens in a new window)](<https://huggingface.co/collections/openai/gpt-oss-safeguard>).

## Keep reading

[View all](</news/>)

![Art card \(4\)](https://images.ctfassets.net/kftzwdyauwt9/26wgJNYWk0soRoyZvBmYmo/dc80fc33c0a60bd566816f2323f31dc2/Art_card__4_.png?w=3840&q=90&fm=webp)

[Advancing content provenance for a safer, more transparent AI ecosystemSafetyMay 19, 2026](</index/advancing-content-provenance/>)

![Helping ChatGPT better recognize context in sensitive conversations > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/7x4viZ0DsQtxQpAgnYYheQ/8dfe028356aceac9e83da6cb837d6864/Saftey-Art-Card-1080x1080.png?w=3840&q=90&fm=webp)

[Helping ChatGPT better recognize context in sensitive conversationsSafetyMay 14, 2026](</index/chatgpt-recognize-context-in-sensitive-conversations/>)

![Running Codex safely at OpenAI > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/76rTHgn2J3y6srtNd3ZrRs/71fc86af978baecda10b212fdb5d3609/Frame.png?w=3840&q=90&fm=webp)

[Running Codex safely at OpenAISecurityMay 8, 2026](</index/running-codex-safely/>)

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
