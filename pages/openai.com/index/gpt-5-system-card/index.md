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

August 7, 2025

[Publication](</research/index/publication/>)[Safety](</news/safety-alignment/>)

# GPT‑5 System Card

[Read the System Card(opens in a new window)](<https://arxiv.org/abs/2601.03267>)[Dive into the data(opens in a new window)](<https://deploymentsafety.openai.com/gpt-5>)

Share

GPT‑5 is a unified system with a smart and fast model that answers most questions, a deeper reasoning model for harder problems, and a real-time router that quickly decides which model to use based on conversation type, complexity, tool needs, and explicit intent (for example, if you say “think hard about this” in the prompt). The router is continuously trained on real signals, including when users switch models, preference rates for responses, and measured correctness, improving over time. Once usage limits are reached, a mini version of each model handles remaining queries. In the near future, we plan to integrate these capabilities into a single model.

In this system card, we label the fast, high-throughput models as gpt-5-main and gpt-5-main-mini, and the thinking models as gpt-5-thinking and gpt-5-thinking-mini. In the API, we provide direct access to the thinking model, its mini version, and an even smaller and faster nano version of the thinking model, made for developers (gpt-5-thinking-nano). In ChatGPT, we also provide access to gpt-5-thinking using a setting that makes use of parallel test time compute; we refer to this as gpt-5-thinking-pro.

  
It can be helpful to think of the GPT‑5 models as successors to previous models:

**Previous model**| **GPT‑5 model**  
---|---  
GPT‑4o| gpt-5-main  
GPT‑4o‑mini| gpt-5-main-mini  
OpenAI o3| gpt-5-thinking  
OpenAI o4-mini| gpt-5-thinking-mini  
GPT‑4.1‑nano| gpt-5-thinking-nano  
OpenAI o3 Pro| gpt-5-thinking-pro  
  
This system card focuses primarily on gpt-5-thinking and gpt-5-main, while evaluations for other models are available in the appendix. The GPT‑5 system not only outperforms previous models on benchmarks and answers questions more quickly, but—more importantly—is more useful for real-world queries. We’ve made significant advances in reducing hallucinations, improving instruction following, and minimizing sycophancy, and have leveled up GPT‑5’s performance in three of ChatGPT’s most common uses: writing, coding, and health. All of the GPT‑5 models additionally feature safe-completions, our latest approach to safety training to prevent disallowed content.

  
Similarly to ChatGPT agent, we have decided to treat gpt-5-thinking as High capability in the Biological and Chemical domain under our [Preparedness Framework](</index/updating-our-preparedness-framework/>), activating the associated safeguards. While we do not have definitive evidence that this model could meaningfully help a novice to create severe biological harm—our [defined threshold⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>) for High capability—we have chosen to take a precautionary approach.

  * [2025](</research/index/?tags=2025>)
  * [System Cards](</research/index/?tags=system-cards>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![oai 1x1](https://images.ctfassets.net/kftzwdyauwt9/7eONRWq61MKUix4tK4t88Y/170085acc9b241a0bdfba429bd217907/oai_1x1.png?w=3840&q=90&fm=webp)

[Advancing youth safety and opportunity through global leadershipGlobal AffairsJun 2, 2026](</index/advancing-youth-safety-and-opportunity-through-global-leadership/>)

![Technical foundations > Art Card](https://images.ctfassets.net/kftzwdyauwt9/6gugGfSiM1oO6UHxxwnqTk/c7173a5a2c096a8f8a24c258ddfa22dd/ArtCard-TechnicalFoundations.png?w=3840&q=90&fm=webp)

[A shared playbook for trustworthy third party evaluationsSafetyMay 29, 2026](</index/trustworthy-third-party-evaluations-foundations/>)

![Frontier Governance Framework > card image ](https://images.ctfassets.net/kftzwdyauwt9/2KoiHuErR5YxXGUnhCU8VY/e392c6249ec4644e07e944edea22e837/Frame2.png?w=3840&q=90&fm=webp)

[OpenAI’s Frontier Governance FrameworkSafetyMay 28, 2026](</index/openai-frontier-governance-framework/>)

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
