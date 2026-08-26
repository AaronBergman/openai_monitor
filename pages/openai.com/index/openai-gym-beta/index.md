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

April 27, 2016

[Release](</research/index/release/>)

# OpenAI Gym Beta

[Read Paper(opens in a new window)](<https://arxiv.org/abs/1606.01540>)

![Openai Gym Beta](https://images.ctfassets.net/kftzwdyauwt9/68408b65-762f-4f71-2d3c9b2dc1da/0d9e1323c7225802bf1fd1ac15b5ad80/image-17.webp?w=3840&q=90&fm=webp)

Loading…

Share

Getting started

  * Getting started
  * Why RL?
  * The environments
  * Evaluations



  * Getting started
  * Why RL?
  * The environments
  * Evaluations



We’re releasing the public beta of OpenAI Gym, a toolkit for developing and comparing reinforcement learning (RL) algorithms. It consists of a growing suite of environments (from simulated robots to Atari games), and a site for comparing and reproducing results.

OpenAI Gym is compatible with algorithms written in any framework, such as [Tensorflow⁠(opens in a new window)](<https://www.tensorflow.org/>) and [Theano⁠(opens in a new window)](<https://github.com/Theano/Theano>). The environments are written in Python, but we’ll soon make them easy to use from any language. We originally built OpenAI Gym as a tool to accelerate our own RL research. We hope it will be just as useful for the broader community.

## Getting started

If you’d like to dive in right away, you can work through our [tutorial⁠(opens in a new window)](<https://gym.openai.com/docs>). You can also help out while learning by [reproducing a result⁠(opens in a new window)](<https://gym.openai.com/evaluations/eval_lEi8I8v2QLqEgzBxcvRIaA>).

## Why RL?

Reinforcement learning (RL) is the subfield of machine learning concerned with decision making and motor control. It studies how an agent can learn how to achieve goals in a complex, uncertain environment. It’s exciting for two reasons:

  * **RL is very general, encompassing all problems that involve making a sequence of decisions** : for example, controlling a robot’s motors so that it’s able to [run⁠(opens in a new window)](<https://gym.openai.com/envs/Humanoid-v0>) and [jump⁠(opens in a new window)](<https://gym.openai.com/envs/Hopper-v0>), making business decisions like pricing and inventory management, or playing [video games⁠(opens in a new window)](<https://gym.openai.com/envs#atari>) and [board games⁠(opens in a new window)](<https://gym.openai.com/envs#board_game>). RL can even be applied to supervised learning problems with [sequential⁠(opens in a new window)](<http://arxiv.org/abs/1511.06732>) [or⁠(opens in a new window)](<http://arxiv.org/abs/0907.0786>) [structured⁠(opens in a new window)](<http://arxiv.org/abs/1601.01705>) outputs.
  * **RL algorithms have started to achieve good results in many difficult environments**. RL has a long history, but until recent advances in deep learning, it required lots of problem-specific engineering. DeepMind’s [Atari results⁠(opens in a new window)](<https://deepmind.com/dqn.html>), [BRETT⁠(opens in a new window)](<http://news.berkeley.edu/2015/05/21/deep-learning-robot-masters-skills-via-trial-and-error/>) from [Pieter Abbeel’s⁠](</index/welcome-pieter-and-shivon/>) group, and [AlphaGo⁠(opens in a new window)](<https://googleblog.blogspot.com/2016/01/alphago-machine-learning-game-go.html>) all used deep RL algorithms which did not make too many assumptions about their environment, and thus can be applied in other settings.



However, RL research is also slowed down by two factors:

  * **The need for better benchmarks**. In supervised learning, progress has been driven by large labeled datasets like [ImageNet⁠(opens in a new window)](<http://www.image-net.org/>). In RL, the closest equivalent would be a large and diverse collection of environments. However, the existing open-source collections of RL environments don’t have enough variety, and they are often difficult to even set up and use.
  * **Lack of standardization of environments used in publications**. Subtle differences in the problem definition, such as the reward function or the set of actions, can drastically alter a task’s difficulty. This issue makes it difficult to reproduce published research and compare results from different papers.



OpenAI Gym is an attempt to fix both problems.

## The environments

OpenAI Gym provides a diverse suite of environments that range from easy to difficult and involve many different kinds of data. We’re starting out with the following collections:

  * [Classic control⁠(opens in a new window)](<https://gym.openai.com/envs#classic_control>) and [toy text⁠(opens in a new window)](<https://gym.openai.com/envs#toy_text>): complete small-scale tasks, mostly from the RL literature. They’re here to get you started.
  * [Algorithmic⁠(opens in a new window)](<https://gym.openai.com/envs#algorithmic>): perform computations such as adding multi-digit numbers and reversing sequences. One might object that these tasks are easy for a computer. The challenge is to learn these algorithms purely from examples. These tasks have the nice property that it’s easy to vary the difficulty by varying the sequence length.
  * [Atari⁠(opens in a new window)](<https://gym.openai.com/envs#atari>): play classic Atari games. We’ve integrated the [Arcade Learning Environment⁠(opens in a new window)](<http://www.arcadelearningenvironment.org/>) (which has had a big impact on reinforcement learning research) in an [easy-to-install⁠(opens in a new window)](<https://github.com/openai/gym#atari>) form.
  * [Board games⁠(opens in a new window)](<https://gym.openai.com/envs#board_games>): play Go on 9x9 and 19x19 boards. Two-player games are fundamentally different than the other settings we’ve included, because there is an adversary playing against you. In our initial release, there is a fixed opponent provided by [Pachi⁠(opens in a new window)](<http://pachi.or.cz/>), and we may add other opponents later (patches welcome!). We’ll also likely expand OpenAI Gym to have first-class support for multi-player games.
  * [2D and 3D robots⁠(opens in a new window)](<https://gym.openai.com/envs#mujoco>): control a robot in simulation. These tasks use the [MuJoCo⁠(opens in a new window)](<https://www.mujoco.org/>) physics engine, which was designed for fast and accurate robot simulation. Included are some environments from a recent [benchmark⁠(opens in a new window)](<http://arxiv.org/abs/1604.06778>) by UC Berkeley researchers (who incidentally will be [joining us⁠](</index/team-plus-plus/>) this summer). MuJoCo is proprietary software, but offers [free trial⁠(opens in a new window)](<https://www.roboti.us/trybuy.html>) licenses.



Over time, we plan to greatly expand this collection of environments. Contributions from the community are more than welcome.

Each environment has a version number (such as [**Hopper-v0** ⁠(opens in a new window)](<https://gym.openai.com/envs/Hopper-v0>)). If we need to change an environment, we’ll bump the version number, defining an entirely new task. This ensures that results on a particular environment are always comparable.

## Evaluations

We’ve made it easy to [upload results⁠(opens in a new window)](<https://gym.openai.com/docs#uploading>) to OpenAI Gym. However, we’ve opted not to create traditional leaderboards. What matters for research isn’t your score (it’s possible to overfit or hand-craft solutions to particular tasks), but instead the generality of your technique.

We’re starting out by maintaining a [curated list⁠(opens in a new window)](<https://gym.openai.com/docs#review>) of contributions that say something interesting about algorithmic capabilities. Long-term, we want this curation to be a community effort rather than something owned by us. We’ll necessarily have to figure out the details over time, and we’d would love your [help⁠(opens in a new window)](<https://gym.openai.com/docs#help>) in doing so.

We want OpenAI Gym to be a community effort from the beginning. We’ve starting working with partners to put together resources around OpenAI Gym:

  * [NVIDIA⁠(opens in a new window)](<http://www.nvidia.com/>): technical [Q&A⁠(opens in a new window)](<https://devblogs.nvidia.com/parallelforall/train-reinforcement-learning-agents-openai-gym>) with John.
  * [Nervana⁠(opens in a new window)](<http://www.nervanasys.com/>): implementation of a [DQN OpenAI Gym agent⁠(opens in a new window)](<http://www.nervanasys.com/openai>).
  * [Amazon Web Services (AWS)⁠(opens in a new window)](<https://aws.amazon.com/>): $250 credit vouchers for select OpenAI Gym users. If you have an evaluation demonstrating the promise of your algorithm and are resource-constrained from scaling it up, [ping us⁠](<mailto:gym@openai.com>) for a voucher. (While supplies last!)



During the public beta, we’re looking for feedback on how to make this into an even better tool for research. If you’d like to help, you can try your hand at improving the state-of-the-art on each environment, reproducing other people’s results, or even implementing your own environments. Also please join us in the [community chat⁠(opens in a new window)](<https://gym.openai.com/chat>)!

  * [Simulated Environments](</research/index/?tags=simulated-environments>)
  * [Exploration & Games](</research/index/?tags=exploration-game>)
  * [Software & Engineering](</research/index/?tags=software-engineering>)
  * [Robotics](</research/index/?tags=robotics>)
  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Community & Collaboration](</research/index/?tags=community-collaboration>)



## Authors

Greg Brockman

## Related articles

[View all](</news/>)

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

[Scaling laws for reward model overoptimizationPublicationOct 19, 2022](</index/scaling-laws-for-reward-model-overoptimization/>)

![Whisper](https://images.ctfassets.net/kftzwdyauwt9/13c810cb-0592-442d-190ab7378bef/a7cb2299d034abe93023f662f8d32263/Speech_Rec_16_9.png?w=3840&q=90&fm=webp)

[Introducing WhisperReleaseSep 21, 2022](</index/whisper/>)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTrainingConclusionJun 23, 2022](</index/vpt/>)

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
