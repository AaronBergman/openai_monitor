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

August 5, 2025

[Publication](</research/index/publication/>)[Safety](</news/safety-alignment/>)

# gpt-oss-120b & gpt-oss-20b Model Card

[Read the model card(opens in a new window)](<https://arxiv.org/abs/2508.10925>)

Share

## Introduction

We introduce gpt-oss-120b and gpt-oss-20b, two open-weight reasoning models available under the Apache 2.0 license and our gpt-oss usage policy. Developed with feedback from the open-source community, these text-only models are compatible with our Responses API and are designed to be used within agentic workflows with strong instruction following, tool use like web search and Python code execution, and reasoning capabilities—including the ability to adjust the reasoning effort for tasks that don’t require complex reasoning. The models are customizable, provide full chain-of-thought (CoT), and support Structured Outputs.

Safety is foundational to our approach to open models. They present a different risk profile than proprietary models: Once they are released, determined attackers could fine-tune them to bypass safety refusals or directly optimize for harm without the possibility for OpenAI to implement additional mitigations or to revoke access.

In some contexts, developers and enterprises will need to implement extra safeguards in order to replicate the system-level protections built into models served through our API and products. We’re terming this document a model card, rather than a system card, because the gpt-oss models will be used as part of a wide range of systems, created and maintained by a wide range of stakeholders. While the models are designed to follow OpenAI’s safety policies by default, other stakeholders will also make and implement their own decisions about how to keep those systems safe.

We ran scalable capability evaluations on gpt-oss-120b, and confirmed that the default model does not reach our indicative thresholds for High capability in any of the three Tracked Categories of our Preparedness Framework (Biological and Chemical capability, Cyber capability, and AI Self-Improvement). We also investigated two additional questions:

  * _Could adversarial actors fine-tune gpt-oss-120b to reach High capability in the Biological and Chemical or Cyber domains?_ Simulating the potential actions of an attacker, we adversarially fine-tuned the gpt-oss-120b model for these two categories. OpenAI’s Safety Advisory Group (“SAG”) reviewed this testing and concluded that, even with robust fine-tuning that leveraged OpenAI’s field-leading training stack, gpt-oss-120b did not reach High capability in Biological and Chemical Risk or Cyber risk.

  * _Would releasing gpt-oss-120b significantly advance the frontier of biological capabilities in open foundation models?_ We found that the answer is no: For most of the evaluations, the default performance of one or more existing open models comes near to matching the adversarially fine-tuned performance of gpt-oss-120b.




As part of this launch, OpenAI is reaffirming its commitment to advancing beneficial AI and raising safety standards across the ecosystem.

  * [System Cards](</research/index/?tags=system-cards>)
  * [2025](</research/index/?tags=2025>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Safety cases for frontier AI training > Card image](https://images.ctfassets.net/kftzwdyauwt9/1XyYuz1U7KqnQDU3dz8Ig9/aea6b4ea875a8dd7ee89e57cd9c3caef/safetfy-cases-for-frontier-ai-training-cover.png?w=3840&q=90&fm=webp)

[Towards safety cases for frontier AI trainingSafetySep 28, 2026](</index/towards-safety-cases-for-frontier-ai-training/>)

![How we will do better for Australia — Cover](https://images.ctfassets.net/kftzwdyauwt9/3SiXxEkdWUe8tQHvZb54qo/16b56e5dc615e45cd29845671386e74d/our-response-to-the-incidents-affecting-australian-government-agencies-cover.png?w=3840&q=90&fm=webp)

[How we will do better for AustraliaCompanySep 28, 2026](</index/how-we-will-do-better-for-australia/>)

![Sam Altman’s remarks at the United Nations Security Council cover image](https://images.ctfassets.net/kftzwdyauwt9/4O6fFZArVSBeCoNjTFwXXZ/cc5e374a6b62b8f328555f002b3bca49/sam-altman-s-remarks-at-the-united-nations-security-council-cover.png?w=3840&q=90&fm=webp)

[Sam Altman’s remarks at the United Nations Security CouncilGlobal AffairsSep 23, 2026](</index/sam-altman-un-security-council-remarks/>)

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
