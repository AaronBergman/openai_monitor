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

  * How Reptile works
  * Implementations



March 7, 2018

[Publication](</research/index/publication/>)

# Reptile: A scalable meta-learning algorithm

[Read paper(opens in a new window)](<https://arxiv.org/abs/1803.02999>)[View code(opens in a new window)](<https://github.com/openai/supervised-reptile>)

![Three simple digital outline drawings of a letter, a fish, and a triangle](https://images.ctfassets.net/kftzwdyauwt9/dd315656-1fce-424d-68adabc313db/5e603f8a6c5767f0f4a310f61f996649/image_97.png?w=3840&q=90&fm=webp)

Loading…

Share

We’ve developed a simple meta-learning algorithm called Reptile which works by repeatedly sampling a task, performing stochastic gradient descent on it, and updating the initial parameters towards the final parameters learned on that task. Reptile is the application of the Shortest Descent algorithm to the meta-learning setting, and is mathematically similar to first-order MAML (which is a version of the well-known MAML algorithm) that only needs black-box access to an optimizer such as SGD or Adam, with similar computational efficiency and performance.

Meta-learning is the process of learning how to learn. A meta-learning algorithm takes in a distribution of tasks, where each task is a learning problem, and it produces a quick learner—a learner that can generalize from a small number of examples. One well-studied meta-learning problem is few-shot classification, where each task is a classification problem where the learner only sees 1–5 input-output examples from each class, and then it must classify new inputs. Below, you can try out our interactive demo of 1-shot classification, which uses Reptile.

Loading...

## How Reptile works

Like MAML, Reptile seeks an initialization for the parameters of a neural network, such that the network can be fine-tuned using a small amount of data from a new task. But while MAML unrolls and differentiates through the computation graph of the gradient descent algorithm, Reptile simply performs [stochastic gradient descent (SGD)⁠(opens in a new window)](<https://en.wikipedia.org/wiki/Stochastic_gradient_descent>) on each task in a standard way—it does not unroll a computation graph or calculate any second derivatives. This makes Reptile take less computation and memory than MAML. The pseudocode is as follows:

Loading...

As an alternative to the last step, we can treat Φ−W \Phi - W Φ−W as a gradient and plug it into a more sophisticated optimizer like [Adam⁠(opens in a new window)](<https://arxiv.org/abs/1412.6980>).

It is at first surprising that this method works at all. If k=1 k=1 k=1, this algorithm would correspond to “joint training”—performing SGD on the mixture of all tasks. While joint training can learn a useful initialization in some cases, it learns very little when zero-shot learning is not possible (e.g. when the output labels are randomly permuted). Reptile requires k>1 k>1 k>1, where the update depends on the higher-order derivatives of the loss function; as we show in the paper, this behaves very differently from k=1 k=1 k=1 (joint training).

To analyze why Reptile works, we approximate the update using a [Taylor series⁠(opens in a new window)](<https://en.wikipedia.org/wiki/Taylor_series>). We show that the Reptile update maximizes the inner product between gradients of different minibatches from the same task, corresponding to improved generalization. This finding may have implications outside of the meta-learning setting for explaining the generalization properties of SGD. Our analysis suggests that Reptile and MAML perform a very similar update, including the same two terms with different weights.

In our experiments, we show that Reptile and MAML yield similar performance on the [Omniglot⁠(opens in a new window)](<https://github.com/brendenlake/omniglot>) and [Mini-ImageNet⁠(opens in a new window)](<https://arxiv.org/abs/1606.04080>) benchmarks for few-shot classification. Reptile also converges to the solution faster, since the update has lower variance.

Our analysis of Reptile suggests a plethora of different algorithms that we can obtain using different combinations of the SGD gradients. In the figure below, assume that we perform k steps of SGD on each task using different minibatches, yielding gradients  g1,g2,…,gk g_1, g_2, \dots, g_k  g1​,g2​,…,gk​. The figure below shows the learning curves on Omniglot obtained by using each sum as the meta-gradient.  g2 g_2  g2​​ corresponds to first-order MAML, an algorithm proposed in the original MAML paper. Including more gradients yields faster learning, due to variance reduction. Note that simply using  g1 g_1  g1​​ (which corresponds to k=1 k=1 k=1) yields no progress as predicted for this task since zero-shot performance cannot be improved.

![Reptile Chart](https://images.ctfassets.net/kftzwdyauwt9/63bf934c-82d3-4aba-c3e9ca12a984/db62050b46c37712fbf9d978353f9c8f/reptile-chart.png?w=3840&q=90&fm=webp)

## Implementations

Our implementation of Reptile is [available on GitHub⁠(opens in a new window)](<https://github.com/openai/supervised-reptile>). It uses TensorFlow for the computations involved, and includes code for replicating the experiments on Omniglot and Mini-ImageNet. We’re also releasing [a smaller JavaScript implementation⁠(opens in a new window)](<https://github.com/openai/supervised-reptile/tree/master/web>) that fine-tunes a model pre-trained with TensorFlow—we used this to create the above demo.

Finally, here’s a minimal example of few-shot regression, predicting a random sine wave from 10 (x,y) (x, y) (x,y) pairs. This one uses PyTorch and fits in a gist:

Loading...

Several people have pointed out to us that first-order MAML and Reptile are more closely related than MAML and Reptile. These algorithms take different perspectives on the problem, but end up computing similar updates—and specifically, Reptile’s contribution builds on the history of both Shortest Descent and avoiding second derivatives [in⁠(opens in a new window)](<https://arxiv.org/abs/1606.04474>) [meta⁠(opens in a new window)](<https://openreview.net/pdf?id=rJY0-Kcll>)-[learning⁠(opens in a new window)](<https://arxiv.org/pdf/1703.03400.pdf>). We’ve since updated the first paragraph to reflect this.

  * [Learning Paradigms](</research/index/?tags=learning-paradigms>)
  * [Language](</research/index/?tags=language>)
  * [Software & Engineering](</research/index/?tags=software-engineering>)



## Authors

Alex Nichol, John Schulman

## Related articles

[View all](</news/>)

![Outstretched robot arm solving a Rubik's cube in its palm in front of a cloudy purple background](https://images.ctfassets.net/kftzwdyauwt9/9267c72e-6cc1-42f6-d23abb5fa261/3bb199192cd8749d8adc83a71751833c/solving-rubiks-cube.jpg?w=3840&q=90&fm=webp)

[Solving Rubik’s Cube with a robot handMilestoneOct 15, 2019](</index/solving-rubiks-cube/>)

![Learning Dexterity](https://images.ctfassets.net/kftzwdyauwt9/296c85d3-a3a1-448a-083f6b2029b1/695e55d1e8c1f265c5e8d9b1e9fda631/learning-dexterity.jpg?w=3840&q=90&fm=webp)

[Learning dexterityMilestoneJul 30, 2018](</index/learning-dexterity/>)

![Evolved Policy Gradients](https://images.ctfassets.net/kftzwdyauwt9/d915bb1d-d402-4648-35baa0a0a809/63757b5fc87fe396d4b0bb87a560d833/image_148.png?w=3840&q=90&fm=webp)

[Evolved Policy GradientsMilestoneApr 18, 2018](</index/evolved-policy-gradients/>)

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
