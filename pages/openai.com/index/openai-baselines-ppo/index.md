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

July 20, 2017

[Release](</research/index/release/>)

# Proximal Policy Optimization

[View code(opens in a new window)](<https://github.com/openai/baselines>)[Read paper(opens in a new window)](<https://arxiv.org/abs/1707.06347>)

![Openai Baselines Ppo](https://images.ctfassets.net/kftzwdyauwt9/b4073079-b924-447c-00367a362468/d766c62670a5c92f913c54206060ba54/image_140.png?w=3840&q=90&fm=webp)

Illustration: Ben Barry

Loading…

Share

PPO

  * PPO

  * Controllable, complicated robots

  * Baselines: PPO, PPO2, ACER, and TRPO




  * PPO

  * Controllable, complicated robots

  * Baselines: PPO, PPO2, ACER, and TRPO




We’re releasing a new class of reinforcement learning algorithms, Proximal Policy Optimization (PPO), which perform comparably or better than state-of-the-art approaches while being much simpler to implement and tune. PPO has become the default reinforcement learning algorithm at OpenAI because of its ease of use and good performance.

Loading...

[Policy gradient methods⁠(opens in a new window)](<http://karpathy.github.io/2016/05/31/rl/>) are fundamental to recent breakthroughs in using deep neural networks for control, from [video games⁠(opens in a new window)](<https://www.nature.com/nature/journal/v518/n7540/full/nature14236.html>), to [3D locomotion⁠(opens in a new window)](<https://arxiv.org/abs/1506.02438>), to [Go⁠(opens in a new window)](<https://www.nature.com/nature/journal/v529/n7587/full/nature16961.html>). But getting good results via policy gradient methods is challenging because they are sensitive to the choice of stepsize — too small, and progress is hopelessly slow; too large and the signal is overwhelmed by the noise, or one might see catastrophic drops in performance. They also often have very poor sample efficiency, taking millions (or billions) of timesteps to learn simple tasks.

Researchers have sought to eliminate these flaws with approaches like [TRPO⁠(opens in a new window)](<https://arxiv.org/abs/1502.05477>) and [ACER⁠(opens in a new window)](<https://arxiv.org/abs/1611.01224>), by constraining or otherwise optimizing the size of a policy update. These methods have their own trade-offs—ACER is far more complicated than PPO, requiring the addition of code for off-policy corrections and a replay buffer, while only doing marginally better than PPO on the Atari benchmark; TRPO—though useful for continuous control tasks—isn’t easily compatible with algorithms that share parameters between a policy and value function or auxiliary losses, like those used to solve problems in Atari and other domains where the visual input is significant.

## PPO

With supervised learning, we can easily implement the cost function, run gradient descent on it, and be very confident that we’ll get excellent results with relatively little hyperparameter tuning. The route to success in reinforcement learning isn’t as obvious—the algorithms have many moving parts that are hard to debug, and they require substantial effort in tuning in order to get good results. PPO strikes a balance between ease of implementation, sample complexity, and ease of tuning, trying to compute an update at each step that minimizes the cost function while ensuring the deviation from the previous policy is relatively small.

We’ve [previously⁠(opens in a new window)](<https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Deep-Reinforcement-Learning-Through-Policy-Optimization>) detailed a variant of PPO that uses an adaptive [KL⁠(opens in a new window)](<https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence>) penalty to control the change of the policy at each iteration. The new variant uses a novel objective function not typically found in other algorithms:

LCLIP(θ)=E^t[min(rt(θ))A^t,clip(rt(θ),1−ε,1+ε)A^t)]L^{CLIP}(\theta) = \hat{E}_{t}[ min(r_t(\theta))\hat{A}_t, clip(r_t(\theta), 1 - \varepsilon, 1 + \varepsilon) \hat{A}_t ) ]LCLIP(θ)=E^t​[min(rt​(θ))A^t​,clip(rt​(θ),1−ε,1+ε)A^t​)]

  * θ \theta θ is the policy parameter
  * E^t \hat{E}_{t} E^t​ denotes the empirical expectation over timesteps
  * rt r_t rt​ is the ratio of the probability under the new and old policies, respectively
  * A^t \hat{A}_t A^t​ is the estimated advantage at time t t t
  * ε \varepsilon ε is a hyperparameter, usually 0.1 or 0.2



This objective implements a way to do a Trust Region update which is compatible with Stochastic Gradient Descent, and simplifies the algorithm by removing the KL penalty and need to make adaptive updates. In tests, this algorithm has displayed the best performance on continuous control tasks and almost matches ACER’s performance on Atari, despite being far simpler to implement.

## Controllable, complicated robots

Loading...

We’ve created interactive agents based on policies trained by PPO—we can [use the keyboard⁠(opens in a new window)](<https://github.com/openai/roboschool/blob/master/agent_zoo/demo_keyboard_humanoid1.py>) to set new target positions for a robot in an environment within Roboschool; though the input sequences are different from what the agent was trained on, it manages to generalize.

Loading...

## Baselines: PPO, PPO2, ACER, and TRPO

This release of [baselines⁠(opens in a new window)](<https://github.com/openai/baselines>) includes scalable, parallel implementations of PPO and TRPO which both use MPI for data passing. Both use Python3 and TensorFlow. We’re also adding pre-trained versions of the policies used to train the above robots to the [Roboschool⁠](</index/roboschool/>) [agent zoo⁠(opens in a new window)](<https://github.com/openai/roboschool/tree/master/agent_zoo>).

**Update** : We’re also releasing a GPU-enabled implementation of PPO, called PPO2. This runs approximately 3x faster than the current PPO baseline on Atari. In addition, we’re releasing an implementation of Actor Critic with Experience Replay (ACER), a sample-efficient policy gradient algorithm. ACER makes use of a replay buffer, enabling it to perform more than one gradient update using each piece of sampled experience, as well as a Q-Function approximate trained with the Retrace algorithm.

We’re looking for people to help build and optimize our reinforcement learning algorithm codebase. If you’re excited about RL, benchmarking, thorough experimentation, and open source, please [apply⁠(opens in a new window)](<https://jobs.lever.co/openai/5c1b2c12-2d18-42f0-836e-96af2cfca5ef>), and mention that you read the baselines PPO post in your application.

  * [Exploration & Games](</research/index/?tags=exploration-game>)
  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Software & Engineering](</research/index/?tags=software-engineering>)
  * [Robotics](</research/index/?tags=robotics>)
  * [Simulated Environments](</research/index/?tags=simulated-environments>)



## Authors

John Schulman, Oleg Klimov, Filip Wolski, Prafulla Dhariwal, Alec Radford

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
