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

June 21, 2016

[Publication](</research/index/publication/>)

# Concrete AI safety problems

[Read Paper(opens in a new window)](<https://arxiv.org/abs/1606.06565>)

![Concrete AI Safety Problems](https://images.ctfassets.net/kftzwdyauwt9/0aff0ce5-9c07-4b0a-4c54e76f57b4/89443b196e0c2d6f3c83d1efec8dfdfe/image_144.png?w=3840&q=90&fm=webp)

Loading…

Share

We (along with researchers from Berkeley and Stanford) are co-authors on today’s paper led by Google Brain researchers, [Concrete Problems in AI Safety⁠(opens in a new window)](<https://arxiv.org/abs/1606.06565>). The paper explores many research problems around ensuring that modern machine learning systems operate as intended.

We (along with researchers from Berkeley and Stanford) are co-authors on today’s paper led by Google Brain researchers, [Concrete Problems in AI Safety⁠(opens in a new window)](<https://arxiv.org/abs/1606.06565>). The paper explores many research problems around ensuring that modern machine learning systems operate as intended. (The problems are very practical, and we’ve already seen some being integrated into [OpenAI Gym⁠(opens in a new window)](<https://gym.openai.com/envs#safety>).)

Advancing AI requires making AI systems smarter, but it also requires preventing accidents—that is, ensuring that AI systems do what people actually want them to do. There’s been an increasing focus on [safety research⁠(opens in a new window)](<http://futureoflife.org/background/benefits-risks-of-artificial-intelligence/>) from the machine learning community, such as a recent [paper⁠(opens in a new window)](<https://intelligence.org/files/Interruptibility.pdf>) from [DeepMind⁠(opens in a new window)](<https://deepmind.com/>) and [FHI⁠(opens in a new window)](<https://www.fhi.ox.ac.uk/>). Still, many machine learning researchers have wondered just how much safety research can be done today.

The authors discuss five areas:

  * **Safe exploration**.  _Can_ [ _reinforcement learning_ ⁠(opens in a new window)](<http://karpathy.github.io/2016/05/31/rl/>)  _(RL) agents learn about their environment without executing catastrophic actions?_ For example, can an RL agent learn to navigate an environment without ever falling off a ledge?
  * **Robustness to distributional shift**.  _Can machine learning systems be robust to changes in the data distribution, or at least fail gracefully?_ For example, can we build [image classifiers⁠(opens in a new window)](<https://www.tensorflow.org/versions/r0.9/tutorials/deep_cnn/index.html>) that indicate appropriate uncertainty when shown new kinds of images, instead of confidently trying to use its [potentially inapplicable⁠(opens in a new window)](<http://arxiv.org/abs/1412.6572>) learned model?
  * **Avoiding negative side effects**.  _Can we transform an RL agent’s_ [ _reward function_ ⁠(opens in a new window)](<https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node9.html>)  _to avoid undesired effects on the environment?_ For example, can we build a robot that will move an object while avoiding knocking anything over or breaking anything, without manually programming a separate penalty for each possible bad behavior?
  * **Avoiding “reward hacking” and “**[**wireheading** ⁠(opens in a new window)](<http://www.agroparistech.fr/mmip/maths/laurent_orseau/papers/ring-orseau-AGI-2011-delusion.pdf>)**”**.  _Can we prevent agents from “gaming” their reward functions, such as by distorting their observations?_ For example, can we train an RL agent to minimize the number of dirty surfaces in a building, without causing it to avoid looking for dirty surfaces or to create new dirty surfaces to clean up?
  * **Scalable oversight**.  _Can RL agents efficiently achieve goals for which feedback is very expensive?_ For example, can we build an agent that tries to clean a room in the way the user would be happiest with, even though feedback from the user is very rare and we have to use cheap approximations (like the presence of visible dirt) during training? The divergence between cheap approximations and what we actually care about is an important source of accident risk.



Many of the problems are not new, but the paper explores them in the context of cutting-edge systems. We hope they’ll inspire more people to work on AI safety research, whether [at OpenAI⁠](</careers/>) or elsewhere.

We’re particularly excited to have participated in this paper as a cross-institutional collaboration. We think that broad AI safety collaborations will enable everyone to build better machine learning systems. [Let us know⁠(opens in a new window)](<https://gitter.im/openai/research>) if you have a future paper you’d like to collaborate on!

  * [Ethics & Safety](</research/index/?tags=ethics-safety>)



## Authors

Paul Christiano, Greg Brockman

## Related articles

[View all](</news/>)

![Disrupting malicious > media](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc5bc7bde3fddfc68462/45.png?w=3840&q=90&fm=webp)

[Disrupting malicious uses of AI by state-affiliated threat actorsSecurityFeb 14, 2024](</index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/>)

![](https://images.ctfassets.net/kftzwdyauwt9/ec66425e-99ca-4314-d04b087f8727/de7341b6a5281c2a220b93a737ce19b0/building-an-early-warning-system-for-llm-aided-biological-threat-creation.jpg?w=3840&q=90&fm=webp)

[Building an early warning system for LLM-aided biological threat creationPublicationJan 31, 2024](</index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/>)

![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d631/6f4dd4542898a35d0a91b137f85c9834/Democratic_inputs_to_AI_grant_program_lessons_learned_and_implementation_plans.jpg?w=3840&q=90&fm=webp)

[Democratic inputs to AI grant program: lessons learned and implementation plansSafetyJan 16, 2024](</index/democratic-inputs-to-ai-grant-program-update/>)

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
