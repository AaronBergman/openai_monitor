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

May 24, 2017

[Release](</research/index/release/>)

# OpenAI Baselines: DQN

[View code(opens in a new window)](<https://github.com/openai/baselines>)

![Openai Baselines Dqn](https://images.ctfassets.net/kftzwdyauwt9/cf5c2d2e-70cc-4d37-98d8b9fb9ab5/6fa0eb978a96c3af7b8fca2a67bc3a88/openai-baselines-dqn.jpg?w=3840&q=90&fm=webp)

Illustration: Ben Barry

Loading…

Share

Best practices

  * Best practices

  * Deep Q-Learning

  * Benchmarks




  * Best practices

  * Deep Q-Learning

  * Benchmarks




We’re open-sourcing OpenAI Baselines, our internal effort to reproduce reinforcement learning algorithms with performance on par with published results. We’ll release the algorithms over upcoming months; today’s release includes DQN and three of its variants.

Reinforcement learning results are tricky to reproduce: performance is very noisy, algorithms have many moving parts which allow for subtle bugs, and many papers don’t report all the required tricks. By releasing known-good implementations (and best practices for creating them), we’d like to ensure that apparent RL advances never are due to comparison with buggy or untuned versions of existing algorithms.

This post contains some best practices we use for correct RL algorithm implementations, as well as the details of our first release: [DQN⁠](</index/openai-baselines-dqn/#dqn>) and three of its variants, algorithms developed by DeepMind.

## Best practices

 _Compare to a random baseline:_ in the video below, an agent is taking random actions in the game H.E.R.O. If you saw this behavior in early stages of training, it’d be really easy to trick yourself into believing that the agent is learning. So you should always verify your agent outperforms a random one.

![Image2 1](https://images.ctfassets.net/kftzwdyauwt9/f5cbc5ae-4932-40ea-64c714e201c5/8274fe59e97d92507ef99450bee40d00/image2-1.gif?w=3840&q=90&fm=webp)

_Be wary of non-breaking bugs_ : when we looked through a sample of ten popular reinforcement learning algorithm reimplementations we noticed that six had subtle bugs found by a community member and confirmed by the author. These ranged from mild bugs that [ignored gradients on some examples⁠(opens in a new window)](<https://github.com/devsisters/DQN-tensorflow/issues/16>) or implemented [causal convolutions incorrectly⁠(opens in a new window)](<https://github.com/ibab/tensorflow-wavenet/issues/29>) to serious ones that reported [scores higher than the true result⁠(opens in a new window)](<https://github.com/trigeorgis/mdm/issues/6>).

_See the world as your agent does:_ like most deep learning approaches, for DQN we tend to convert images of our environments to grayscale to reduce the computation required during training. This can create its own bugs: when we ran our DQN algorithm on Seaquest we noticed that our implementation was performing poorly. When we inspected the environment we discovered this was because our post-processed images contained no fish, as this picture shows.

![Fish Img 1](https://images.ctfassets.net/kftzwdyauwt9/7e63dcb9-f487-43bb-011611a591a3/f60b82718c6de792125772905de06979/fish_img_1.jpg?w=3840&q=90&fm=webp)

When transforming the screen images into greyscale we had incorrectly calibrated our coefficients for the green color values, which led to the fish disappearing. After we noticed the bug we tweaked the color values and our algorithm was able to see the fish again.

To debug issues like this in the future, Gym now contains a [play⁠(opens in a new window)](<https://github.com/openai/gym/blob/master/gym/utils/play.py>) function, which lets a researcher easily see the same observations as the AI agent would.

_Fix bugs, then hyperparameters_ : After debugging, we started to calibrate our hyperparameters. We ultimately found that setting the annealing schedule for epsilon, a hyperparameter which controlled the exploration rate, had a huge impact on performance. Our final implementation decreases epsilon to 0.1 over the first million steps and then down to 0.01 over the next 24 million steps. If our implementation contained bugs, then it’s likely we would come up with different hyperparameter settings to try to deal with faults we hadn’t yet diagnosed.

_Double check your interpretations of papers_ : In the DQN [Nature⁠(opens in a new window)](<https://www.nature.com/nature/journal/v518/n7540/full/nature14236.html>) paper the authors write: “We also found it helpful to clip the error term from the update [...] to be between -1 and 1.”. There are two ways to interpret this statement — clip the objective, or clip the multiplicative term when computing gradient. The former seems more natural, but it causes the gradient to be zero on transitions with high error, which leads to suboptimal performance, as found in one [DQN implementation⁠(opens in a new window)](<https://github.com/devsisters/DQN-tensorflow/issues/16>). The latter is correct and has a simple mathematical interpretation — [Huber Loss⁠(opens in a new window)](<https://en.wikipedia.org/wiki/Huber_loss>). You can spot bugs like these by checking that the gradients appear as you expect — this can be easily done within TensorFlow by using [compute_gradients⁠(opens in a new window)](<https://www.tensorflow.org/api_docs/python/tf/train/GradientDescentOptimizer#compute_gradients>).

The majority of bugs in this post were spotted by going over the code multiple times and thinking through what could go wrong with each line. Each bug seems obvious in hindsight, but even experienced researchers tend to underestimate how many passes over the code it can take to find all the bugs in an implementation.

## Deep Q-Learning

  * [**DQN** ⁠(opens in a new window)](<http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html>): A reinforcement learning algorithm that combines Q-Learning with deep neural networks to let RL work for complex, high-dimensional environments, like video games, or robotics.
  * [**Double Q Learning** ⁠(opens in a new window)](<https://arxiv.org/abs/1509.06461>): Corrects the stock DQN algorithm’s tendency to sometimes overestimate the values tied to specific actions.
  * [**Prioritized Replay** ⁠(opens in a new window)](<https://arxiv.org/abs/1511.05952>): Extends DQN’s experience replay function by learning to replay memories where the real reward significantly diverges from the expected reward, letting the agent adjust itself in response to developing incorrect assumptions.
  * [**Dueling DQN** ⁠(opens in a new window)](<https://arxiv.org/abs/1511.06581>): Splits the neural network into two — one learns to provide an estimate of the value at every timestep, and the other calculates potential advantages of each action, and the two are combined for a single action-advantage Q function.



To get started, run the following:

#### Python

`
    
    
    1
    
    pip install baselines
    
    2
    
    # Train model and save the results to cartpole_model.pkl
    
    3
    
    python -m baselines.deepq.experiments.train_cartpole
    
    4
    
    # Load the model saved in cartpole_model.pkl and visualize the learned policy
    
    5
    
    python -m baselines.deepq.experiments.enjoy_cartpole

`

We’ve also provided trained agents, which you can obtain by running:

#### Bash

`
    
    
    1
    
    python -m baselines.deepq.experiments.atari.download_model --blob model-atari-prior-duel-breakout-1 --model-dir /tmp/models
    
    2
    
    python -m baselines.deepq.experiments.atari.enjoy --model-dir /tmp/models/model-atari-prior-duel-breakout-1 --env Breakout --dueling

`

## Benchmarks

![Frames seen by the agent \(millions\)](https://images.ctfassets.net/kftzwdyauwt9/4e324e51-2d4f-479a-2f6e64077f95/958c50d84838c4c53670327d7b2448e4/Pasted-image-at-2017_05_23-02_11-PM-3.png?w=3840&q=90&fm=webp)

We’ve included an [iPython notebook⁠(opens in a new window)](<https://github.com/openai/baselines-results/blob/master/dqn_results.ipynb>) showing the performance of our DQN implementations on Atari games. You can compare the performance of our various algorithms such as Dueling Double Q learning with Prioritized Replay (yellow), Double Q learning with Prioritized Replay (blue), Dueling Double Q learning (green) and Double Q learning (red).

AI is an empirical science, where the ability to do more experiments directly correlates with progress. With Baselines, researchers can spend less time implementing pre-existing algorithms and more time designing new ones. If you’d like to help us refine, extend, and develop AI algorithms then [join us⁠](</careers/>) at OpenAI.

  * [Exploration & Games](</research/index/?tags=exploration-game>)
  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Software & Engineering](</research/index/?tags=software-engineering>)
  * [Simulated Environments](</research/index/?tags=simulated-environments>)



## Authors

Szymon Sidor, John Schulman

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
