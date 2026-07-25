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

October 11, 2016

[Publication](</research/index/publication/>)

# Transfer from simulation to real world through learning deep inverse dynamics model

[Read paper(opens in a new window)](<https://arxiv.org/abs/1610.03518>)

![Transfer From Simulation To Real World Through Learning Deep Inverse Dynamics Model](https://images.ctfassets.net/kftzwdyauwt9/acb523f5-9654-4428-27c0c2a1b229/aa1209a6c10fde5e44e7fec37a5fa463/image-14.webp?w=3840&q=90&fm=webp)

Loading…

Share

## Abstract

Developing control policies in simulation is often more practical and safer than directly running experiments in the real world. This applies to policies obtained from planning and optimization, and even more so to policies obtained from reinforcement learning, which is often very data demanding. However, a policy that succeeds in simulation often doesn’t work when deployed on a real robot. Nevertheless, often the overall gist of what the policy does in simulation remains valid in the real world. In this paper we investigate such settings, where the sequence of states traversed in simulation remains reasonable for the real world, even if the details of the controls are not, as could be the case when the key differences lie in detailed friction, contact, mass and geometry properties. During execution, at each time step our approach computes what the simulation-based control policy would do, but then, rather than executing these controls on the real robot, our approach computes what the simulation expects the resulting next state(s) will be, and then relies on a learned deep inverse dynamics model to decide which real-world action is most suitable to achieve those next states. Deep models are only as good as their training data, and we also propose an approach for data collection to (incrementally) learn the deep inverse dynamics model. Our experiments shows our approach compares favorably with various baselines that have been developed for dealing with simulation to real world model discrepancy, including output error control and Gaussian dynamics adaptation.

  * [Robotics](</research/index/?tags=robotics>)



## Authors

Paul Christiano, Zain Shah, Igor Mordatch, Jonas Schneider, Trevor Blackwell, Josh Tobin, Pieter Abbeel, Wojciech Zaremba

## Related articles

[View all](</news/>)

![Outstretched robot arm solving a Rubik's cube in its palm in front of a cloudy purple background](https://images.ctfassets.net/kftzwdyauwt9/9267c72e-6cc1-42f6-d23abb5fa261/3bb199192cd8749d8adc83a71751833c/solving-rubiks-cube.jpg?w=3840&q=90&fm=webp)

[Solving Rubik’s Cube with a robot handMilestoneOct 15, 2019](</index/solving-rubiks-cube/>)

![Learning Dexterity](https://images.ctfassets.net/kftzwdyauwt9/296c85d3-a3a1-448a-083f6b2029b1/695e55d1e8c1f265c5e8d9b1e9fda631/learning-dexterity.jpg?w=3840&q=90&fm=webp)

[Learning dexterityMilestoneJul 30, 2018](</index/learning-dexterity/>)

![Multi Goal Reinforcement Learning Challenging Robotics Environments And Request For Research](https://images.ctfassets.net/kftzwdyauwt9/bf0d1994-27c2-4cfa-f062b70d11c9/37d2a2c11b1486a6fe1685c1a79adfb5/image-55.webp?w=3840&q=90&fm=webp)

[Multi-Goal Reinforcement Learning: Challenging robotics environments and request for researchPublicationFeb 26, 2018](</index/multi-goal-reinforcement-learning/>)

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
