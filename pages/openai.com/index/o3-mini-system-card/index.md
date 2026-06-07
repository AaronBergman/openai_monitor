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

January 31, 2025

[Publication](</research/index/publication/>)

# OpenAI o3‑mini System Card

[Read the System Card(opens in a new window)](<https://cdn.openai.com/o3-mini-system-card-feb10.pdf>)[Contributions](</index/openai-o3-mini/>)

Loading…

Share

## OpenAI o3-mini System Card

Specific areas of risk

  * Disallowed content

  * Jailbreaks

  * Hallucinations




Preparedness Scorecard

  * CBRN

Medium
    *     *     *     *   * Cybersecurity

Low
    *     *     *     *   * Persuasion

Medium
    *     *     *     *   * Model Autonomy

Medium
    *     *     *     * 


## Scorecard ratings

  * Low
  * Medium
  * High
  * Critical



Only models with a post-mitigation score of "medium" or below can be deployed.  
Only models with a post-mitigation score of "high" or below can be developed further.

## Introduction

The OpenAI o model series is trained with large-scale reinforcement learning to reason using chain of thought. These advanced reasoning capabilities provide new avenues for improving the safety and robustness of our models. In particular, our models can reason about our safety policies in context when responding to potentially unsafe prompts, through deliberative alignment. This brings OpenAI o3‑mini to parity with state-of-the-art performance on certain benchmarks for risks such as generating illicit advice, choosing stereotyped responses, and succumbing to known jailbreaks. Training models to incorporate a chain of thought before answering has the potential to unlock substantial benefits, while also increasing potential risks that stem from heightened intelligence.

Under the [Preparedness Framework⁠(opens in a new window)](<https://cdn.openai.com/openai-preparedness-framework-beta.pdf>), OpenAI’s Safety Advisory Group (SAG) recommended classifying the OpenAI o3‑mini (Pre-Mitigation) model as Medium risk overall. It scores Medium risk for Persuasion, CBRN (chemical, biological, radiological, nuclear), and Model Autonomy, and Low risk for Cybersecurity. Only models with a post-mitigation score of Medium or below can be deployed, and only models with a post-mitigation score of High or below can be developed further.

Due to improved coding and research engineering performance, OpenAI o3‑mini is the first model to reach Medium risk on Model Autonomy. However, it still performs poorly on evaluations designed to test real-world ML research capabilities relevant for self improvement, which is required for a High classification. Our results underscore the need for building robust alignment methods, extensively stress-testing their efficacy, and maintaining meticulous risk management protocols.

This report outlines the safety work carried out for the OpenAI o3‑mini model, including safety evaluations, external red teaming, and Preparedness Framework evaluations.

  * [System Cards](</research/index/?tags=system-cards>)



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
