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

September 12, 2024

[Release](</research/index/release/>)

# OpenAI o1‑mini

Advancing cost-efficient reasoning.

[Contributions](</openai-o1-contributions/>)

Loading…

Share

Optimized for STEM Reasoning

  * Optimized for STEM Reasoning

  * Model Speed

  * Safety

  * Limitations and What’s Next




  * Optimized for STEM Reasoning

  * Model Speed

  * Safety

  * Limitations and What’s Next




We're releasing OpenAI o1‑mini, a cost-efficient reasoning model. o1‑mini excels at STEM, especially math and coding—nearly matching the performance of [OpenAI o1](</index/introducing-openai-o1-preview/>) on evaluation benchmarks such as AIME and Codeforces. We expect o1‑mini will be a faster, cost-effective model for applications that require reasoning without broad world knowledge.

Today, we are launching o1‑mini to [tier 5 API users⁠(opens in a new window)](<https://platform.openai.com/docs/guides/rate-limits/usage-tiers>) at a cost that is 80% cheaper than OpenAI o1‑preview. ChatGPT Plus, Team, Enterprise, and Edu users can use o1‑mini as an alternative to o1‑preview, with higher rate limits and lower latency (see Model Speed⁠).

## Optimized for STEM Reasoning

Large language models such as o1 are pre-trained on vast text datasets. While these high-capacity models have broad world knowledge, they can be expensive and slow for real-world applications. In contrast, o1‑mini is a smaller model optimized for STEM reasoning during pretraining. After training with the same high-compute reinforcement learning (RL) pipeline as o1, o1‑mini achieves comparable performance on many useful reasoning tasks, while being significantly more cost efficient.

When evaluated on benchmarks requiring intelligence and reasoning, o1‑mini performs well compared to o1‑preview and o1. However, o1‑mini performs worse on tasks requiring non-STEM factual knowledge (see  Limitations⁠).

##### Math Performance vs Inference Cost

AIMEInference Cost (%)

**Mathematics:** In the high school AIME math competition, o1‑mini (70.0%) is competitive with o1 (74.4%)–while being significantly cheaper–and outperforms o1‑preview (44.6%). o1‑mini’s score (about 11/15 questions) places it in approximately the top 500 US high-school students.

**Coding:** On the Codeforces competition website, o1‑mini achieves 1650 Elo, which is again competitive with o1 (1673) and higher than o1‑preview (1258). This Elo score puts the model at approximately the 86th percentile of programmers who compete on the Codeforces platform. o1‑mini also performs well on the HumanEval coding benchmark and high-school level cybersecurity capture the flag challenges (CTFs).

##### Codeforces

90012581650Elo

##### HumanEval

90.2%92.4%92.4%Accuracy

##### Cybersecurity CTFs

20.0%43.0%28.7%Accuracy (Pass@12)

**STEM:** On some academic benchmarks requiring reasoning, such as GPQA (science) and MATH-500, o1‑mini outperforms GPT‑4o. o1‑mini does not perform as well as GPT‑4o on tasks such as MMLU and lags behind o1‑preview on GPQA due to its lack of broad world knowledge.

##### MMLU

###### 0-shot CoT

92.3%90.8%85.2%88.7%

##### GPQA

###### Diamond, 0-shot CoT

77.3%73.3%60.0%53.6%

##### MATH-500

###### 0-shot CoT

94.8%85.5%90.0%60.3%

**Human preference evaluation:** We had human raters compare o1‑mini to GPT‑4o on challenging, open-ended prompts in various domains, using the same methodology as our [o1‑preview vs GPT‑4o comparison](</index/learning-to-reason-with-llms/>). Similar to o1‑preview, o1‑mini is preferred to GPT‑4o in reasoning-heavy domains, but is not preferred to GPT‑4o in language-focused domains.

##### Human preference evaluation vs chatgpt-4o-latest

o1-preview

o1-mini

DomainWin Rate vs GPT-4o (%)

## Model Speed

As a concrete example, we compared responses from GPT‑4o, o1‑mini, and o1‑preview on a word reasoning question. While GPT‑4o did not answer correctly, both o1‑mini and o1‑preview did, and o1‑mini reached the answer around 3-5x faster.

Chat speed comparison

## Safety

o1‑mini is trained using the same alignment and safety techniques as o1‑preview. The model has 59% higher jailbreak robustness on an internal version of the StrongREJECT dataset compared to GPT‑4o. Before deployment, we carefully assessed the safety risks of o1‑mini using the same approach to preparedness, external red-teaming, and safety evaluations as o1‑preview. We are publishing the detailed results from these evaluations in the accompanying [system card](</index/openai-o1-system-card/>).

**Metric**| **GPT‑4o**| **o1‑mini**  
---|---|---  
**% Safe completions refusal on harmful prompts** (standard)| 0.99| 0.99  
**% Safe completions on harmful prompts** (Challenging: jailbreaks & edge cases)| 0.714| 0.932  
**% Compliance on benign edge cases** (“not over-refusal”)| 0.91| 0.923  
**Goodness@0.1 StrongREJECT jailbreak eval** ([_Souly et al. 2024_ ⁠(opens in a new window)](<https://arxiv.org/abs/2402.10260>))| 0.22| 0.83  
**Human sourced jailbreak eval**|  0.77| 0.95  
  
## Limitations and What’s Next

Due to its specialization on STEM reasoning capabilities, o1‑mini’s factual knowledge on non-STEM topics such as dates, biographies, and trivia is comparable to small LLMs such as GPT‑4o mini. We will improve these limitations in future versions, as well as experiment with extending the model to other modalities and specialities outside of STEM.

  * [o1](</research/index/?tags=o1>)
  * [Reasonings & Policy](</research/index/?tags=reasoning-policy>)
  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Software & Engineering](</research/index/?tags=software-engineering>)



## Authors

OpenAI

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
