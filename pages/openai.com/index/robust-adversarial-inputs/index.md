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

  * Scale-invariant adversarial examples
  * Transformation-invariant adversarial examples



July 17, 2017

[Publication](</research/index/publication/>)

# Robust adversarial inputs

[Read paper(opens in a new window)](<https://arxiv.org/abs/1707.07397>)

![Robust Adversarial Inputs](https://images.ctfassets.net/kftzwdyauwt9/b1e44c6c-795c-4d1d-767b1d664b28/196e786ab486c0dca0860dda283118a8/image-68.webp?w=3840&q=90&fm=webp)

Loading…

Share

We’ve created images that reliably fool neural network classifiers when viewed from varied scales and perspectives. This challenges a claim from last week that self-driving cars would be hard to trick maliciously since they capture images from multiple scales, angles, perspectives, and the like.

Loading...

Out-of-the-box [adversarial examples⁠(opens in a new window)](<https://blog.openai.com/adversarial-example-research/>) do fail under image transformations. Below, we show the same cat picture, adversarially perturbed to be incorrectly classified as a desktop computer by [Inception v3⁠(opens in a new window)](<https://arxiv.org/abs/1512.00567>) trained on [ImageNet⁠(opens in a new window)](<http://www.image-net.org/>). A zoom of as little as 1.002 causes the classification probability for the correct label tabby cat to override the adversarial label `desktop computer`.

Loading...

However, we’d suspected that active effort could produce a robust adversarial example, as adversarial examples have been shown to [transfer⁠(opens in a new window)](<https://arxiv.org/pdf/1607.02533.pdf>) to the physical world.

## Scale-invariant adversarial examples

Adversarial examples can be created using an optimization method called projected gradient descent to find small perturbations to the image that arbitrarily fool the classifier.

Instead of optimizing for finding an input that’s adversarial from a single viewpoint, we optimize over a large [ensemble⁠(opens in a new window)](<https://people.eecs.berkeley.edu/~liuchang/paper/transferability_iclr_2017.pdf>) of stochastic classifiers that randomly rescale the input before classifying it. Optimizing against such an ensemble produces robust adversarial examples that are scale-invariant.

Loading...

Even when we restrict ourselves to only modifying pixels corresponding to the cat, we can create a single perturbed image that is simultaneously adversarial at all desired scales.

## Transformation-invariant adversarial examples

By adding random rotations, translations, scales, noise, and mean shifts to our training perturbations, the same technique produces a single input that remains adversarial under any of these transformations.

Loading...

Our transformations are sampled randomly at test time, demonstrating that our example is invariant to the whole distribution of transformations.

  * [Ethics & Safety](</research/index/?tags=ethics-safety>)



## Author

Anish Athalye

## Related articles

[View all](</news/>)

![Point E A System For Generating 3d Point Clouds From Complex Prompts](https://images.ctfassets.net/kftzwdyauwt9/7e4ba260-7655-4049-5a2568c94158/2f2af956a356ee2b507296d01e45e766/image-5.webp?w=3840&q=90&fm=webp)

[Point-E: A system for generating 3D point clouds from complex promptsPublicationDec 16, 2022](</index/point-e/>)

![Multimodal Neurons](https://images.ctfassets.net/kftzwdyauwt9/e16f419f-09bf-4266-7ca3cdd2ae33/0a11dd23053f257828e7c68a815cd632/multimodal-neurons.png?w=3840&q=90&fm=webp)

[Multimodal neurons in artificial neural networksMilestoneMar 4, 2021](</index/multimodal-neurons/>)

![CLIP](https://images.ctfassets.net/kftzwdyauwt9/5e490f66-703f-4228-221ca64049ed/8ed4358ba4b9f8779e07a2b15d7256e1/image_125.png?w=3840&q=90&fm=webp)

[CLIP: Connecting text and imagesMilestoneJan 5, 2021](</index/clip/>)

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
