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

  * Getting started
  * Achieving state-of-the-art performance with GPT-4o fine-tuning
  * Data Privacy and Safety



August 20, 2024

[Product](</news/product-releases/>)

# Fine-tuning now available for GPT‑4o

Fine-tune custom versions of GPT‑4o to increase performance and accuracy for your applications.

![The image shows an abstract painting featuring a grid-like pattern of vertical and horizontal strokes in warm yellows, oranges, and pinks, interspersed with cool blues and purples. The colorful rectangles and lines create a vibrant, layered effect.](https://images.ctfassets.net/kftzwdyauwt9/5dAyNXB6FatGsOQmLvWIim/c75bb2aa4d0e9ce1096e1490b954cca7/FineTuning_1.png?w=3840&q=90&fm=webp)

Loading…

Share

** _Update on May 8, 2026_** _: OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users but existing users of the fine-tuning platform will be able to create training jobs for the coming months. All fine-tuned models will remain available for inference until their base models are_[ _deprecated_ ⁠(opens in a new window)](<https://developers.openai.com/api/docs/deprecations>)_. The full timeline is_[ _here_ ⁠(opens in a new window)](<https://developers.openai.com/api/docs/deprecations>)_._

* * *

Today, we’re launching fine-tuning for [_GPT‑4o_ ⁠](<https://openai.com/index/hello-gpt-4o/>), one of the most requested features from developers. We are also offering 1M training tokens per day for free for every organization through September 23.

Developers can now fine-tune GPT‑4o with custom datasets to get higher performance at a lower cost for their specific use cases. Fine-tuning enables the model to customize structure and tone of responses, or to follow complex domain-specific instructions. Developers can already produce strong results for their applications with as little as a few dozen examples in their training data set.

From coding to creative writing, fine-tuning can have a large impact on model performance across a variety of domains. This is just the start—we’ll continue to invest in expanding our [_model customization_ ⁠](<https://openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/>) options for developers.

## Getting started

GPT‑4o fine-tuning is available today to all developers on all paid [_usage tiers_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/rate-limits/usage-tiers>).

To get started, visit the [_fine-tuning dashboard_ ⁠(opens in a new window)](<https://platform.openai.com/finetune>), click `create`, and select `gpt-4o-2024-08-06` from the base model drop-down. GPT‑4o fine-tuning training costs $25 per million tokens, and inference is $3.75 per million input tokens and $15 per million output tokens.

GPT‑4o mini fine-tuning is also available to all developers on all paid usage tiers. Visit the fine-tuning dashboard and select `gpt-4o-mini-2024-07-18` from the base model drop-down. For GPT‑4o mini, we’re offering 2M training tokens per day for free through September 23. 

To learn more about how to use fine-tuning, visit our [_docs_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/fine-tuning>).

## Achieving state-of-the-art performance with GPT-4o fine-tuning

Over the past couple of months, we’ve worked with a handful of trusted partners to test fine-tuning on GPT‑4o and learn about their use cases. Here are a couple of success stories:

**Cosine achieves state-of-the-art results on the SWE-bench benchmark**

****[ _Cosine_ ⁠(opens in a new window)](<https://cosine.sh/>)’s Genie is an AI software engineering assistant that’s able to autonomously identify and resolve bugs, build features, and refactor code in collaboration with users. It can reason across complex technical problems and make changes to code with higher accuracy and fewer tokens needed. Genie is powered by a fine-tuned GPT‑4o model trained on examples of real software engineers at work, enabling the model to learn to respond in a specific way. The model was also trained to be able to output in specific formats, such as patches that could be committed easily to codebases. 

With a fine-tuned GPT‑4o model, Genie achieves a SOTA score of 43.8% on the new [_SWE-bench_ ⁠(opens in a new window)](<https://www.swebench.com/>) Verified benchmark, [_announced_ ⁠](<https://openai.com/index/introducing-swe-bench-verified/>) last Tuesday. Genie also holds a SOTA score of 30.08% on SWE-bench Full, beating its previous SOTA score of 19.27%, the largest ever improvement in this benchmark. 

**Distyl ranks 1st on BIRD-SQL benchmark**

[ Distyl⁠(opens in a new window)](<https://distyl.ai/>), an AI solutions partner to Fortune 500 companies, recently placed 1st on the [_BIRD-SQL_ ⁠(opens in a new window)](<https://bird-bench.github.io/>) benchmark, the leading text-to-SQL benchmark. Distyl’s fine-tuned GPT‑4o achieved an execution accuracy of 71.83% on the leaderboard and excelled across tasks like query reformulation, intent classification, chain-of-thought, and self-correction, with particularly high performance in SQL generation.  


![The leaderboard shows Execution Accuracy \(EX\) with “Human Performance” at 92.96%. AI models ranked below include “Distillery + GPT-4o” \(71.83%\), “ExSL + granite-34b-code” \(70.37%\), “RECAP + Gemini” \(69.03%\), and “ByteBrain” \(68.87%\).](https://images.ctfassets.net/kftzwdyauwt9/6B538HYvZq1CLIV0GzUjDa/be0884f109227e552f7390fbf3aaa473/Leaderboard_light.png?w=3840&q=90&fm=webp)

## Data Privacy and Safety

Fine-tuned models remain entirely under your control, with full ownership of your business data, including all inputs and outputs. This ensures your data is never shared or used to train other models.

We’ve also implemented layered safety mitigations for fine-tuned models to ensure they aren’t being misused. For example, we continuously run automated safety evals on fine-tuned models and monitor usage to ensure applications adhere to our usage policies.

We’re excited to see what you build by fine-tuning GPT‑4o. If you’d like to explore more model customization options, please [_reach out_ ⁠](<https://openai.com/form/custom-models/>) to our team—we’d be happy to help!  


  * [ChatGPT](</news/?tags=chatgpt>)
  * [2024](</news/?tags=2024>)



## Authors

Andrew Peng, John Allard, Steven Heidel

## Acknowledgements

Adam Wells, Alec Gorge, Andrew Peng, Beth Hoover, Cary Hudson, Derek Chen, Dev Valladares, Elie Georges, Eric Wallace, Freddie Sulit, John Allard, Karen Li, Kevin Whinnery, Krithika Muthukumar, Lauren Workman, Leher Pathak, Lilian Weng, Lindsay McCallum, Lucy Chen, Michael Kolhede, Miles Brundage, Nick Pyne, Olivier Godement, Owen Cambpell-Moore, Pedro Aguilar, Ravi Teja Mullapudi, Scott Lessans, Sean Chang, Shyamal Anadkat, Steven Heidel, Tabarak Khan, Will Hang

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
