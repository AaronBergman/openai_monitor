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

October 29, 2025

[Safety](</news/safety-alignment/>)[Release](</research/index/release/>)

# gpt-oss-safeguard technical report

Performance and baseline evaluations of gpt-oss-safeguard-120b and gpt-oss-safeguard-20b

[Read technical report(opens in a new window)](<https://cdn.openai.com/pdf/08b7dee4-8bc6-4955-a219-7793fb69090c/Technical_report__Research_Preview_of_gpt_oss_safeguard.pdf>)

Share

## Introduction

gpt-oss-safeguard-120b and gpt-oss-safeguard-20b are two open-weight reasoning models post-trained from the gpt-oss models and trained to reason from a provided policy in order to label content under that policy. They are available under the Apache 2.0 license and our gpt-oss usage policy. Developed with feedback from the open-source community, these text-only models are compatible with our Responses API. The models are customizable, provide full chain-of-thought (CoT), can be used with different reasoning efforts (low, medium, high), and support Structured Outputs.

In this report, we describe gpt-oss-safeguard’s capabilities and provide our baseline safety evaluations on the gpt-oss-safeguard models, using the underlying gpt-oss models as a baseline. For more information about the development and architecture of the underlying gpt-oss models, see the original [gpt-oss model model card⁠](</index/gpt-oss-model-card/>).

We recommend using these models to classify content against a provided policy, and not as the core functionality with which end users interact; the original gpt-oss models are better for those applications. The safety metrics provided below describe how gpt-oss-safeguard models function in chat settings. The gpt-oss-safeguard models are not intended for this use, but since they are open models, it is possible for someone to use the models in this way. Because of that possibility, we wanted to verify that they met our safety standards in such usage; this report shares the results of those tests. We also share an initial evaluation of multi-language performance in a chat setting; note that this does not directly assess performance during content classification with a provided policy.

The gpt-oss-safeguard models are fine-tunes of their gpt-oss counterparts, and were trained without any additional biological or cybersecurity data. As a result, we determined that the previous work [estimating worst case scenarios⁠](</index/estimating-worst-case-frontier-risks-of-open-weight-llms/>) from gpt-oss release cross applies to these new models.

  * [2025](</news/?tags=2025>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![gpt-oss-safeguard Art Card 1.1](https://images.ctfassets.net/kftzwdyauwt9/70DRKmUAlpyn5xyOoZ6Qc3/d56ae272a76f3975dca778837481627a/gpt-oss-safeguard_Art_Card_1.1.png?w=3840&q=90&fm=webp)

[Introducing gpt-oss-safeguardProductOct 29, 2025](</index/introducing-gpt-oss-safeguard/>)

![Open Model SystemCard 1x1](https://images.ctfassets.net/kftzwdyauwt9/3vlhDMtFUrKBwnx6jOeLRb/eddabb8d71e16a0a680e85dfc5de8115/Open_Model_SystemCard_1x1.png?w=3840&q=90&fm=webp)

[gpt-oss-120b & gpt-oss-20b Model CardPublicationAug 5, 2025](</index/gpt-oss-model-card/>)

[Introducing gpt-ossReleaseAug 5, 2025](</index/introducing-gpt-oss/>)

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
