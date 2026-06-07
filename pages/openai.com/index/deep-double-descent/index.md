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

Model-wise double descent

  * Model-wise double descent
  * Sample-wise non-monotonicity
  * Epoch-wise double descent



December 5, 2019

[Publication](</research/index/publication/>)

# Deep double descent

[Read paper(opens in a new window)](<https://arxiv.org/abs/1912.02292>)

![Deep Double Descent](https://images.ctfassets.net/kftzwdyauwt9/a8317cae-e4cd-4e11-06eb4c242127/c357e1b6b2bea69afe57a536168bd87f/image_130.png?w=3840&q=90&fm=webp)

Loading…

Share

We show that the [double⁠(opens in a new window)](<https://arxiv.org/abs/1812.11118>) [descent⁠(opens in a new window)](<https://arxiv.org/abs/1710.03667>) [phenomenon⁠(opens in a new window)](<https://arxiv.org/abs/1809.09349>) occurs in CNNs, ResNets, and transformers: performance first improves, then gets worse, and then improves again with increasing model size, data size, or training time. This effect is often avoided through careful regularization. While this behavior appears to be fairly universal, we don’t yet fully understand why it happens, and view further study of this phenomenon as an important research direction.

![Frame 1 3 ](https://images.ctfassets.net/kftzwdyauwt9/34a66965-6618-46a6-429bbcc55716/a065079573c8d4f491fb3e3479547ad0/Frame-1--3-.png?w=3840&q=90&fm=webp)

Many classes of modern deep learning models, including CNNs, ResNets, and transformers, exhibit the previously-observed [double⁠(opens in a new window)](<https://arxiv.org/abs/1812.11118>) [descent⁠(opens in a new window)](<https://arxiv.org/abs/1710.03667>) [phenomenon⁠(opens in a new window)](<https://arxiv.org/abs/1809.09349>) when not using early stopping or regularization. The peak occurs predictably at a “critical regime,” where the models are barely able to fit the training set. As we increase the number of parameters in a neural network, the test error initially decreases, increases, and, just as the model is able to fit the train set, undergoes a second descent.

Neither classical statisticians’ conventional wisdom that  _too large models are worse_ nor the modern ML paradigm that  _bigger models are better_ uphold. We find that double descent also occurs over train epochs. Surprisingly, we show these phenomena can lead to a regime where more data hurts, and training a deep network on a larger train set actually performs worse.

## Model-wise double descent

1\. There is a regime where bigger models are worse.

![Graph and test and train error based on ResNet18 width parameter](https://images.ctfassets.net/kftzwdyauwt9/9b1defbc-a847-4a59-131ef795a083/9e9efe8767bdb54428099a3ab543b0e2/modeldd.svg?w=3840&q=90)

The model-wise double descent phenomenon can lead to a regime where training on more data hurts. In the chart above, the peak in test error occurs around the interpolation threshold, when the models are just barely large enough to fit the train set.

In all cases we’ve observed, changes which affect the interpolation threshold (such as changing the optimization algorithm, the number of train samples, or the amount of label noise) also affect the location of the test error peak correspondingly. The double descent phenomena is most prominent in settings with added label noise; without it, the peak is smaller and easy to miss. Adding label noise amplifies this general behavior and allows us to easily investigate.

## Sample-wise non-monotonicity

2\. There is a regime where more samples hurts.

![Graph of cross-entropy test loss based on model size for 4k train samples and 18k train samples](https://images.ctfassets.net/kftzwdyauwt9/fdb3dcfc-44e7-4687-68a775781c03/9a90f98b87ce5541452e656acbcaa837/fig_data_hurts.svg?w=3840&q=90)

The above chart shows transformers trained on a language-translation task with no added label noise. As expected, increasing the number of samples shifts the curve downwards towards lower test error. However, since more samples require larger models to fit, increasing the number of samples also shifts the interpolation threshold (and peak in test error) to the right.

For intermediate model sizes (red arrows), these two effects combine, and we see that training on 4.5x more samples actually hurts test performance.

## Epoch-wise double descent

3\. There is a regime where training longer reverses overfitting.

![Epoch Train](https://images.ctfassets.net/kftzwdyauwt9/5eff858a-bc2f-4c24-29e1b10640ed/83a7fde3099b98bc93720fff528766eb/epoch_train.png?w=3840&q=90&fm=webp)

![Epoch Test](https://images.ctfassets.net/kftzwdyauwt9/8989a3e0-f876-4b38-09f8dd104c95/4115a76f4b0df8a31c7fc8de0600ce58/epoch_test.png?w=3840&q=90&fm=webp)

The charts above show test and train error as a function of both model size and number of optimization steps. For a given number of optimization steps (fixed y-coordinate), test and train error exhibit model-size double descent. For a given model size (fixed x-coordinate), as training proceeds, test and train error decreases, increases, and decreases again; we call this phenomenon epoch-wise double descent.

_In general, the peak of test error appears systematically when models are just barely able to fit the train set._

Our intuition is that, for models at the interpolation threshold, there is effectively only one model that fits the train data, and forcing it to fit even slightly noisy or misspecified labels will destroy its global structure. That is, there are no “good models” which both interpolate the train set and perform well on the test set. However, in the over-parameterized regime, there are many models that fit the train set and there exist such good models. Moreover, the implicit bias of stochastic gradient descent (SGD) leads it to such good models, for reasons we don’t yet understand.

We leave fully understanding the mechanisms behind double descent in deep neural networks as an important open question.

  * [Compute Scaling](</research/index/?tags=compute-scaling>)



## Authors

Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang, Boaz Barak, Ilya Sutskever

## Acknowledgments

Thanks to Mikhail Belkin and Chris Olah for helpful discussions and feedback throughout this work. An expanded version of this post can also be found on Boaz Barak’s blog, [Windows on Theory⁠(opens in a new window)](<https://windowsontheory.org/2019/12/05/deep-double-descent/>).

## Related articles

[View all](</news/>)

![Scaling Laws For Neural Language Models](https://images.ctfassets.net/kftzwdyauwt9/61740968-bc64-4d6b-6505acf65f0e/f477935fcd8199015f371454b61c4814/image-18.webp?w=3840&q=90&fm=webp)

[Scaling laws for neural language modelsPublicationJan 23, 2020](</index/scaling-laws-for-neural-language-models/>)

![How AI Training Scales](https://images.ctfassets.net/kftzwdyauwt9/249cc8d1-7545-4156-97856278c58d/1b83d4be7ca2e6f3e800497968035196/image-40.webp?w=3840&q=90&fm=webp)

[How AI training scalesMilestoneDec 14, 2018](</index/how-ai-training-scales/>)

![Jetbrains > Hero > Media item > Asset](https://images.ctfassets.net/kftzwdyauwt9/46d99f08-c849-4c73-5a6c7b83ea9c/6e0eaaaf815df2a53f997b36ce57ad13/jetbrains.png?w=3840&q=90&fm=webp)

[Embedding AI into developer softwareMar 21, 2024](</index/jetbrains/>)

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
