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

  * Dynamics randomization
  * From vision to action
  * Costs



October 19, 2017

[Publication](</research/index/publication/>)

# Generalizing from simulation

[Read paper (dynamics randomization)(opens in a new window)](<https://arxiv.org/abs/1710.06537>)[Read paper (image-based learning)(opens in a new window)](<https://arxiv.org/abs/1710.06542>)

![Colorful 3D render of a robot simulation interacting with a red cube on a platform](https://images.ctfassets.net/kftzwdyauwt9/231bd1f1-8591-44b1-9ee13ba4e96a/9d4d29b4855ab09282bfd04c332f653f/generalizing-from-simulation.jpg?w=3840&q=90&fm=webp)

Loading…

Share

Our latest robotics techniques allow robot controllers, trained entirely in simulation and deployed on physical robots, to react to unplanned changes in the environment as they solve simple tasks. That is, we’ve used these techniques to build closed-loop systems rather than open-loop ones as before.

The simulator need not match the real-world in appearance or dynamics; instead, we randomize relevant aspects of the environment, from friction to action delays to sensor noise. Our new results provide more evidence that general-purpose robots can be built by training entirely in simulation, followed by a small amount of self-calibration in the real world.

Loading...

## Dynamics randomization

We developed [dynamics randomization⁠(opens in a new window)](<https://arxiv.org/abs/1710.06537>) to train a robot to adapt to unknown real-world dynamics. During training, we randomize a large set of ninety-five properties that determine the dynamics of the environment, such as altering the mass of each link in the robot’s body; the friction and damping of the object it is being trained on; the height of the table the object is on; the latency between actions; the noise in its observations; and so on.

We used this approach to train an [LSTM⁠(opens in a new window)](<http://colah.github.io/posts/2015-08-Understanding-LSTMs/>)-based policy to push a hockey puck around a table. Our feed-forward networks [fail⁠](</index/generalizing-from-simulation/#pusher_fail>) at this task, whereas LSTMs can use their past observations to analyze the dynamics of the world and adjust their behavior accordingly.

## From vision to action

We also trained a robot end-to-end in simulation using reinforcement learning (RL), and deployed the resulting policy on a physical robot. The resulting system maps vision directly to action without special sensors, and can adapt to visual feedback.

Loading...

The abundance of RL results with simulated robots can make it seem like RL easily solves most robotics tasks. But common RL algorithms work well only on tasks where small perturbations to your action can provide an incremental change to the reward. Some robotics tasks have simple rewards, like walking, where you can be scored on distance traveled. But most tasks do [not⁠](</index/learning-from-human-preferences/>)—to define a dense reward for block stacking, you’d need to encode that the arm is close to the block, that the arm approaches the block in the correct orientation, that the block is lifted off the ground, the distance of block to the desired position, etc.

We spent a number of months unsuccessfully trying to get conventional RL algorithms working on pick-and-place tasks before ultimately developing a new reinforcement learning algorithm, [Hindsight Experience Replay⁠(opens in a new window)](<https://arxiv.org/pdf/1707.01495.pdf>) (HER), which allows agents to learn from a binary reward by pretending that a failure was what they wanted to do all along and learning from it accordingly. (By analogy, imagine looking for a gas station but ending up at a pizza shop. You still don’t know where to get gas, but you’ve now learned where to get pizza.) We also used [domain randomization⁠](</index/spam-detection-in-the-physical-world/>) on the visual shapes to learn a vision system robust enough for the physical world.

Our HER implementation uses the actor-critic technique with asymmetric information. (The  _actor_ is the policy, and the  _critic_ is a network which receives action/state pairs and estimates their Q-value, or sum of future rewards, providing training signal to the actor.) While the critic has access to the full state of the simulator, the actor only has access to RGB and depth data. Thus the critic can provide fully accurate feedback, while the actor uses only data present in the real world.

## Costs

Both techniques increase the computational requirements: dynamics randomization slows training down by a factor of 3x, while learning from images rather than states is about 5–10x slower.

We see three approaches to building general-purpose robots: training on huge fleets of physical robots, making simulators increasingly match the real world, and randomizing the simulator to allow the model to generalize to the real-world. We increasingly believe that the third will be the most important part of the solution.

If you’re interested in helping us push towards general-purpose robots, consider [joining our team at OpenAI⁠](</careers/>).

Loading...

  * [Simulated Environments](</research/index/?tags=simulated-environments>)
  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Robotics](</research/index/?tags=robotics>)



## Authors

Xue Bin Peng, Lerrel Pinto, Alex Ray, Bob McGrew, Jonas Schneider, Josh Tobin, Marcin Andrychowicz, Peter Welinder, Pieter Abbeel, Wojciech Zaremba

## Related articles

[View all](</news/>)

![CLIP](https://images.ctfassets.net/kftzwdyauwt9/5e490f66-703f-4228-221ca64049ed/8ed4358ba4b9f8779e07a2b15d7256e1/image_125.png?w=3840&q=90&fm=webp)

[CLIP: Connecting text and imagesMilestoneJan 5, 2021](</index/clip/>)

![Outstretched robot arm solving a Rubik's cube in its palm in front of a cloudy purple background](https://images.ctfassets.net/kftzwdyauwt9/9267c72e-6cc1-42f6-d23abb5fa261/3bb199192cd8749d8adc83a71751833c/solving-rubiks-cube.jpg?w=3840&q=90&fm=webp)

[Solving Rubik’s Cube with a robot handMilestoneOct 15, 2019](</index/solving-rubiks-cube/>)

![Learning Dexterity](https://images.ctfassets.net/kftzwdyauwt9/296c85d3-a3a1-448a-083f6b2029b1/695e55d1e8c1f265c5e8d9b1e9fda631/learning-dexterity.jpg?w=3840&q=90&fm=webp)

[Learning dexterityMilestoneJul 30, 2018](</index/learning-dexterity/>)

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
