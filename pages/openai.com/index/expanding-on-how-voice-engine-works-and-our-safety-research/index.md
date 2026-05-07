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

  * How Voice Engine works
  * We’ve been developing the model for over a year
  * Building Voice Engine safely is a top priority
  * Future synthetic voice safety



June 7, 2024

[Safety](</news/safety-alignment/>)

# Expanding on how Voice Engine works and our safety research

Exploring the technology behind our text-to-speech model.

![Abstract painting with a mix of pastel colors, including pink, orange, purple, and green, resembling a vibrant landscape.](https://images.ctfassets.net/kftzwdyauwt9/1F9YYY34lTeNq289xLAF6G/097bda3f5ef7b71943baada651f4b09f/abstract-pastel.jpg?w=3840&q=90&fm=webp)

Loading…

Share

We’re providing more insight into how Voice Engine works and our safety research to keep everyone updated on our progress. Voice Engine is a model capable of creating custom voices.

It's important that people around the world understand where this technology is headed, whether we ultimately deploy it widely ourselves or not. Which is why we want to explain how the model works, how we use it for research and education, and how we are implementing our safety measures around it. Voice Engine is not widely available yet.

## How Voice Engine works

The voice capability is powered by a text-to-speech (TTS) model, capable of generating human-like audio from just text and 15-seconds of sample speech. 

The TTS system is developed by helping the model understand the nuances of speech from paired audio and transcriptions. The model learns to predict the most probable sounds a speaker will make for a given text transcript, taking into account different voices, accents, and speaking styles. After this, the model can generate not just spoken versions of text, but also spoken utterances that reflect how different types of speakers would say them.

From there, generating audio with the TTS model requires just a 15-second sample from the speaker and the corresponding text. The model is not fine-tuned for any specific speaker, there is no model customization involved. Instead, it employs a diffusion process, starting with random noise and progressively de-noising it to closely match how the speaker from the 15-second audio sample would articulate the text.

## We’ve been developing the model for over a year

We first developed Voice Engine in late 2022. Early on, to assess the capabilities and limitations of our Voice Engine model, we tested it internally using a mix of public and private voice samples. This internal prototype was essential for our alignment and safety research, informing our safeguards, and is a continuation of our commitment to understand the technical frontier.

Importantly, these outputs were reserved for internal testing, not for training the models that power our products.

As part of our iterative deployment framework, this early prototype also played a valuable role in helping policymakers understand the capabilities of synthetic voice models. For instance, starting last summer we showed global policymakers at the highest levels the technology's potential and discussed the associated risks with them. 

[ _In September of 2023_ ⁠](<https://openai.com/index/chatgpt-can-now-see-hear-and-speak/>), we used Voice Engine to power ChatGPT’s Voice Mode feature. Because these capabilities also presented new risks, we launched it only for this specific use case. Voice Mode was created solely from real voices, [_carefully selected_ ⁠](<https://openai.com/index/how-the-voices-for-chatgpt-were-chosen/>) through a detailed process that began in May 2023 involving professional voice actors, talent agencies, casting directors, and industry advisors.

[_In November of 2023_ ⁠](<https://openai.com/index/new-models-and-developer-products-announced-at-devday/>), we released a simple [_TTS API_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/text-to-speech>) also powered by Voice Engine. We chose another limited release where we worked with professional voice actors to create 15-second audio samples to power each of the six preset voices in the API. Developers can build these into their websites to read blog posts out loud, for example.

[_In March of this year_ ⁠](<https://openai.com/index/navigating-the-challenges-and-opportunities-of-synthetic-voices/>), we previewed Voice Engine’s capability of creating custom voices with a small set of trusted partners. This initiative aimed to raise awareness about the capabilities of synthetic voices and support the following goals:

  * Phasing out voice based authentication as a security measure for accessing bank accounts and other sensitive information
  * Exploring policies to protect the use of individuals' voices in AI
  * Educating the public in understanding the capabilities and limitations of AI technologies, including the possibility of deceptive AI content
  * Accelerating the development and adoption of techniques for tracking the origin of audiovisual content, so it's always clear when you're interacting with a real person or with an AI



These small scale deployments are also helping to inform our approach, safeguards, and thinking on how Voice Engine could be used for good across various industries.

## Building Voice Engine safely is a top priority

We continue to engage with U.S. and international partners from across government, media, entertainment, education, civil society and beyond to ensure we are incorporating their feedback as we build.

The partners testing Voice Engine have agreed to usage policies that prohibit impersonation without consent and require explicit approval from the original speaker, and require that any AI-generated voices are disclosed to listeners as such. Additionally, [_safety measures like watermarking and proactive monitoring_ ⁠](<https://openai.com/index/navigating-the-challenges-and-opportunities-of-synthetic-voices/>) are in place to trace and oversee the use of the technology.

## Future synthetic voice safety

Omnimodels such as GPT‑4o, with native audio capabilities, enable new interactions that previous models like Voice Engine could not. We also recognize that the audio modality of GPT‑4o introduces several new risks, particularly in voice generation. We are actively red-teaming GPT‑4o to identify and address both known and unforeseen risks across various fields such as social psychology, bias and fairness, and misinformation. We are building in multiple layers of mitigations such as refining model behaviors, adapting existing text-based systems for GPT‑4o’s architecture, and developing new classifiers.

Consistent with our cautious approach to releasing Voice Engine, we will restrict GPT‑4o’s audio outputs to a selection of preset voices for general release. These voices were sourced from professional voice actors that were selected through a carefully considered casting process. We will share additional information about audio-related risks and mitigations in the forthcoming GPT‑4o system card.

  * [Alignment](</news/?tags=alignment>)
  * [Framework](</news/?tags=framework>)
  * [2024](</news/?tags=2024>)



## Author

OpenAI

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
