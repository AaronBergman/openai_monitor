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

September 3, 2026

[Safety](</news/safety-alignment/>)

# Safety overview: GPT‑6 Astra

[Read the full system card(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra>)

Loading…

Share

Today, we are releasing GPT‑6 Astra, the most capable model we have ever broadly deployed. Astra is our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework.

The most important things to know about the safety of this launch are as follows:

  1. **GPT‑6 Astra is a significant step up in cyber capabilities and meets our Critical threshold.** This means that, with the right tools and access, GPT‑6 Astra can find previously unknown security flaws and develop new ways to exploit them across many well-protected systems without a person guiding each step. Accordingly, we significantly strengthened our protections against the model taking harmful cyber actions, whether that’s due to misuse or misalignment. We also took steps to secure our internal development and deployment of Astra and similar models, including stricter isolation, checkpoint encryption, universal monitoring of full trajectories including chains of thought (CoT), and a blocking alignment evaluation process before internal use.
  2. **GPT‑6 Astra is significantly more robust than its predecessors**. Incorporating new robustness safety training techniques, GPT‑6 Astra is significantly more robust to jailbreaks than GPT‑5.6 Sol, including across longer trajectories. We know this from offline tests and our program of rigorous internal and external jailbreak testing and remediation. For users flagged as potentially high risk, we have additionally trained in the ability to adjust the model’s refusal boundary to be more conservative and cover a broader range of dual use risks. We use regression testing to make sure Astra is robust against jailbreaks found in previous testing periods, and performed new rounds of automated red-teaming with our latest internal red-teaming attackers to validate our improvements.
  3. **GPT‑6 Astra is better aligned than GPT‑5.6 Sol.** Astra is a significant step forward in model alignment, and includes alignment improvements spanning the composition of our pre-training data to our grading during reinforcement learning. We report a [new suite of alignment evaluations⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra/alignment>), and find that GPT‑6 Astra is stronger at respecting safety and security boundaries and staying within its authorized scope. In a simulation using more than[ 54,000 internal Codex tasks⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra/forecasting-misaligned-behavior-with-deployment-simulation-of-internal-codex-traffic>), Astra also received roughly half as many flags for higher-severity misaligned behavior as Sol.
  4. **We are deploying misalignment monitoring broadly**. We view model alignment as the primary lever to prevent potential misaligned behavior from our models. However, monitoring provides broad visibility into frontier model behavior, illuminating opportunities to further improve alignment and safety. In addition, monitoring serves as an additional layer of protection against misaligned behavior that is detected. For these reasons, we have additionally added misalignment monitoring to all tool-using inference involved in our external deployment of Astra, with significant compute cost. This system parallels our internal setup.
  5. **GPT‑6 Astra’s monitorability has decreased relative to GPT‑5.6 Sol.** We have performed significant investigations on the [monitorability⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra/monitorability>) and [controllability⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra/cot-controllability>) of GPT‑6 Astra. We have found that GPT‑6 Astra is more capable of controlling its own CoT than GPT‑5.6 Sol, and less likely to include incriminating information in its CoT. In adversarial settings (where we push the model to evade our monitors) we find that the model is able to remain undetected when strategically underperforming in evaluations (sandbagging) and can sometimes evade our internal monitors when asked to perform [certain sabotage tasks⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-6-astra/monitor-evasion>). We have not seen evidence of steganographic CoT reasoning (e.g., concealing hidden reasoning within ordinary and seemingly unrelated text), indicating that the evasion risk may largely be bounded to lower reasoning tasks.
     * These findings indicate that the Astra class models could evade our CoT monitors under adversarial conditions. Right now, these findings are largely based on adversarial evaluations (i.e., when we instruct the model to evade monitoring), and overall our alignment evaluations show that Astra is less likely than GPT‑5.6 Sol to violate security and safety restrictions overall.
     * However, we take the trend seriously, and we are continuing to investigate these findings and their implications for monitorability as our models become more capable. OpenAI has worked to preserve and utilize chain of thought monitoring, and preserving CoT monitorability is a core goal of the research program. However, these results also underscore the importance of developing alignment auditing techniques beyond examining the model’s chain of thought.
  6. **GPT‑6 Astra more responsibly navigates browsing and workplace settings:** GPT‑6 Astra is significantly more robust to prompt injections than GPT‑5.6 Sol. We have additionally tested the model’s behavior in realistic browsing and professional computer environments, and find that the model is significantly less likely to perform misaligned and potentially destructive actions (for instance unauthorized transactions, data loss, excessive access, or circumvention of controls) compared to GPT‑5.6 Sol. It also acts more safely when handling harmful requests in agentic settings, such as requests to assist with violent attack planning or commit fraud.
  7. **GPT‑6 Astra is significantly safer in higher-risk scenarios.** GPT‑6 Astra responds more safely than GPT‑5.6 Sol to challenging requests drawn from production and adversarial human red-teaming. Astra achieves a Pareto improvement in safely completing unsafe requests and avoiding unnecessary refusals to harmless requests. These improvements extend to high-severity scenarios where the risk of harm emerges from the broader context rather than an explicit request. Astra also applies age-appropriate safety boundaries more consistently for users under 18.



For more information, see the [full system card⁠(opens in a new window)](<http://deploymentsafety.openai.com/gpt-6-astra>).

  * [User Safety & Control](</news/?tags=user-safety>)
  * [2026](</news/?tags=2026>)
  * [GPT](</news/?tags=gpt>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Path to Astra — Clean square cover — Neutral Option 062 v1](https://images.ctfassets.net/kftzwdyauwt9/4BabvjDCQdlYN2ISzOkgF9/78d35947274e9b3ac2483377782b007e/astra-cover-v001.png?w=3840&q=90&fm=webp)

[Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026](</index/path-to-astra/>)

[The Hugging Face incident and the road aheadSecurityAug 26, 2026](</index/hugging-face-incident-and-the-road-ahead/>)

![Our commitment to Zero Data Retention as AI advances — card](https://images.ctfassets.net/kftzwdyauwt9/6bPStWA6pc66cahnhg0jo6/61786b178401b6e902e9da65fa4da095/Blog_Thumbnail_-_OpenAI_Blog.png?w=3840&q=90&fm=webp)

[Offering Zero Data Retention for frontier modelsCompanyAug 19, 2026](</index/offering-zero-data-retention-for-frontier-models/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6](</index/gpt-6-astra/>)
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
