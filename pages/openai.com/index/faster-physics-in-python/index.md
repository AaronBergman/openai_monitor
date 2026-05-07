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

  * Batched simulation
  * High performance texture randomization
  * Virtual Reality with mujoco-py
  * API and usage



June 28, 2017

[Release](</research/index/release/>)

# Faster physics in Python

We’re open-sourcing a high-performance Python library for robotic simulation using the MuJoCo engine, developed over our past year of robotics research.

[View code(opens in a new window)](<https://github.com/openai/mujoco-py>)[View docs(opens in a new window)](<https://openai.github.io/mujoco-py/build/html/index.html>)

![Eight 3D renders of the same robot arm in varying color assortments](https://images.ctfassets.net/kftzwdyauwt9/be57b8bb-027b-4dfb-788f261485a9/089b69fcc2d295db35ebe3435dcd15ed/image-70.webp?w=3840&q=90&fm=webp)

Loading…

Share

This library is one of our core tools for deep learning [robotics research⁠(opens in a new window)](<https://blog.openai.com/robots-that-learn/>), which we’ve now released as a major version of [mujoco-py⁠(opens in a new window)](<https://github.com/openai/mujoco-py>), our Python 3 bindings for MuJoCo. mujoco-py [1.50.1.0⁠(opens in a new window)](<https://github.com/openai/mujoco-py/releases>) brings a number of new capabilities and significant performance boosts. New features include:

  * Efficient handling of parallel simulations
  * GPU-accelerated headless 3D rendering
  * Direct access to MuJoCo functions and data structures
  * Support for all [MuJoCo 1.50 features⁠(opens in a new window)](<https://www.mujoco.org/changelist.html>) like its improved contact solver



## Batched simulation

Many methods in trajectory optimization and reinforcement learning (like [LQR⁠(opens in a new window)](<https://en.wikipedia.org/wiki/Linear%E2%80%93quadratic_regulator>), [PI2⁠(opens in a new window)](<http://www.jmlr.org/papers/v11/theodorou10a.html>), and [TRPO⁠(opens in a new window)](<https://arxiv.org/abs/1502.05477>)) benefit from being able to run multiple simulations in parallel. mujoco-py uses data parallelism through [OpenMP⁠(opens in a new window)](<http://www.openmp.org/>) and direct-access memory management through [Cython⁠(opens in a new window)](<http://cython.org/>) and [NumPy⁠(opens in a new window)](<http://www.numpy.org/>) to make batched simulation more efficient.

[Naive usage⁠(opens in a new window)](<https://gist.github.com/jonasschneider/d8bacaec035b99c7f303aafa4f67a0f3>) of the new version’s [MjSimPool⁠(opens in a new window)](<https://github.com/openai/mujoco-py/blob/master/mujoco_py/mjsimpool.pyx>) interface shows a 400% speedup over the old, and still about 180% over an optimized and restricted usage pattern using Python’s [multiprocessing package⁠(opens in a new window)](<https://docs.python.org/3/library/multiprocessing.html>) to gain the same level of parallelism. The majority of the speedup comes from reduced access times to the various MuJoCo data structures. Check out `[examples/simpool.py](https://github.com/openai/mujoco-py/blob/master/examples/simpool.py)` for a tour of MjSimPool.

## High performance texture randomization

![Loopdiscogif2](https://images.ctfassets.net/kftzwdyauwt9/42a4f547-89ce-4240-5a7d9a0d067f/61b00638721d7274ab70cc1d16af617c/loopdiscogif2.gif?w=3840&q=90&fm=webp)

We use the [domain randomization⁠(opens in a new window)](<https://arxiv.org/abs/1703.06907>) technique across many projects at OpenAI. The latest version of mujoco-py supports headless GPU rendering; this yields a speedup of ~40x compared to CPU-based rendering, letting us generate hundreds of frames per second of synthetic image data. In the above (slowed down) animation we use this to vary the textures of one of our robots, which helps it identify its body when we transfer it from the simulator to reality. Check out [examples/disco_fetch.py⁠(opens in a new window)](<https://github.com/openai/mujoco-py/blob/master/examples/disco_fetch.py>) for an example of randomized texture generation.

## Virtual Reality with mujoco-py

The API exposed by mujoco-py is sufficient to enable Virtual Reality interaction without any extra C++ code. We ported MuJoCo’s [C++ VR example⁠(opens in a new window)](<https://www.mujoco.org/book/programming.html#saVive>) to Python using mujoco-py. If you have an HTC Vive VR setup, you can give try it using [this example⁠(opens in a new window)](<https://github.com/openai/mujoco-py/blob/master/examples/mjvive.py>) (this support is considered experimental, but we’ve been using it internally for a while).

## API and usage

The simplest way to get started with mujoco-py is with the [MjSim class⁠(opens in a new window)](<https://github.com/openai/mujoco-py/blob/master/mujoco_py/mjsim.pyx>). It is a wrapper around the simulation model and data, and lets you to easily step the simulation and render images from camera sensors. Here’s a simple example:

#### Python

`
    
    
    1
    
    from mujoco_py import load_model_from_path, MjSim
    
    2
    
      
    
    
    3
    
    model = load_model_from_path("xmls/tosser.xml")  
    
    4
    
      
    
    
    5
    
    sim = MjSim(model)
    
    6
    
    sim.step()
    
    7
    
    print(sim.data.qpos)
    
    8
    
    # => [ -1.074e-05   1.043e-04  -3.923e-05   0.000e+00   0.000e+00]

`

For advanced users, we provide a number of lower-level interfaces for accessing the innards of the MuJoCo C structs and functions directly. Refer to the [README⁠(opens in a new window)](<https://github.com/openai/mujoco-py/blob/master/README.md>) and the [full documentation⁠(opens in a new window)](<https://openai.github.io/mujoco-py/build/html/index.html>) to learn more.

  * [Community & Collaboration](</research/index/?tags=community-collaboration>)
  * [Simulated Environments](</research/index/?tags=simulated-environments>)
  * [Software & Engineering](</research/index/?tags=software-engineering>)
  * [Robotics](</research/index/?tags=robotics>)



## Authors

Jonas Schneider, Peter Welinder, Alex Ray, Jonathan Ho, Wojciech Zaremba

## Related articles

[View all](</news/>)

![Whisper](https://images.ctfassets.net/kftzwdyauwt9/13c810cb-0592-442d-190ab7378bef/a7cb2299d034abe93023f662f8d32263/Speech_Rec_16_9.png?w=3840&q=90&fm=webp)

[Introducing WhisperReleaseSep 21, 2022](</index/whisper/>)

![Techniques For Training Large Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/62793de4-0f01-42fc-539325d9af36/bc1ac82499fc1dc43f59accdd31d0195/image-9.webp?w=3840&q=90&fm=webp)

[Techniques for training large neural networksPublicationJun 9, 2022](</index/techniques-for-training-large-neural-networks/>)

![Introducing Triton Open Source Gpu Programming For Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/cdce1ebd-19a2-4848-a08ec8c44e18/55b924fc6628318148b7c5c4902551e7/image-18.webp?w=3840&q=90&fm=webp)

[Introducing Triton: Open-source GPU programming for neural networksReleaseJul 28, 2021](</index/triton/>)

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
