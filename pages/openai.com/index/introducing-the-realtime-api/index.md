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

  * How it works
  * Availability & pricing
  * Safety & privacy
  * Getting started
  * What’s next



October 1, 2024

[Product](</news/product-releases/>)

# Introducing the Realtime API

Developers can now build fast speech-to-speech experiences into their applications

![DALL·E generated impressionist oil painting of undulating orange audio waves creating a harmonious, layered composition](https://images.ctfassets.net/kftzwdyauwt9/139I6Ga8xl6qTXGPL9lWyc/82838b1ef1a26a4946a27d656de0c806/01_Realtime_API.png?w=3840&q=90&fm=webp)

Share

 _Update on August 28, 2025: We announced the general availability of the Realtime API._[_Learn more here_](</index/introducing-gpt-realtime/>) _._

* * *

_Update on February 3, 2025: We no longer limit the number of simultaneous sessions on the Realtime API. Please refer to our_[ _docs_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/rate-limits?tier=free>)_for the latest rate limits on the Realtime API._

* * *

_Update on October 30, 2024: We 've added five new voices with greater range and expressiveness_. _Cached pricing is now also available for text and audio inputs, lowering the price to $2.50/1M cached text input tokens and $20/1M cached audio input tokens._[_Learn more here_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/realtime>)_._

* * *

_Update on October 17, 2024: Audio inputs and outputs are now available in the Chat Completions API._[_Get started here_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/audio>)_._

* * *

Today, we're introducing a public beta of the Realtime API, enabling all paid developers to build low-latency, multimodal experiences in their apps. Similar to ChatGPT’s Advanced Voice Mode, the Realtime API supports natural speech-to-speech conversations using the [_six preset voices_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/text-to-speech>) already supported in the API.

We’re also introducing audio input and output in the [_Chat Completions API_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/chat-completions>) to support use cases that don’t require the low-latency benefits of the Realtime API. With this update, developers can pass any text or audio inputs into [_GPT‑4o_ ⁠](<https://openai.com/index/hello-gpt-4o/>) and have the model respond with their choice of text, audio, or both.

From language apps and educational software to customer support experiences, developers have already been leveraging voice experiences to connect with their users. Now with the Realtime API and soon with audio in the Chat Completions API, developers no longer have to stitch together multiple models to power these experiences. Instead, you can build natural conversational experiences with a single API call.

## How it works

Previously, to create a similar voice assistant experience, developers had to transcribe audio with an automatic speech recognition model like [_Whisper_ ⁠](<https://openai.com/index/whisper/>), pass the text to a text model for inference or reasoning, and then play the model’s output using a [_text-to-speech_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/text-to-speech>) model. This approach often resulted in loss of emotion, emphasis and accents, plus noticeable latency. With the Chat Completions API, developers can handle the entire process with a single API call, though it remains slower than human conversation. The Realtime API improves this by streaming audio inputs and outputs directly, enabling more natural conversational experiences. It can also handle interruptions automatically, much like Advanced Voice Mode in ChatGPT.

Under the hood, the Realtime API lets you create a persistent WebSocket connection to exchange messages with GPT‑4o. The API supports [_function calling_ ⁠(opens in a new window)](<https://platform.openai.com/docs/guides/function-calling>), which makes it possible for voice assistants to respond to user requests by triggering actions or pulling in new context. For example, a voice assistant could place an order on behalf of the user or retrieve relevant customer information to personalize its responses. 

### Powering customer support agents, language learning assistants, and more

As part of our iterative deployment strategy, we’ve been testing the Realtime API with a handful of partners to gather feedback while we build. A couple of promising early use cases include:

Healthify, a nutrition and fitness coaching app, uses the Realtime API to enable natural conversations with its AI coach Ria, while involving human dietitians when needed for personalized support.

Speak, a language learning app, uses Realtime API to power its role-play feature, encouraging users to practice conversations in a new language.

## Availability & pricing

The Realtime API will begin rolling out today in public beta to all paid developers. Audio capabilities in the Realtime API are powered by the new GPT‑4o model `gpt-4o-realtime-preview`.

Audio in the Chat Completions API will be released in the coming weeks, as a new model `gpt-4o-audio-preview`. With `gpt-4o-audio-preview`, developers can input text or audio into GPT‑4o and receive responses in text, audio, or both.

The Realtime API uses both text tokens and audio tokens. Text input tokens are priced at $5 per 1M and $20 per 1M output tokens. Audio input is priced at $100 per 1M tokens and output is $200 per 1M tokens. This equates to approximately $0.06 per minute of audio input and $0.24 per minute of audio output. Audio in the Chat Completions API will be the same price.

## Safety & privacy

The Realtime API uses multiple layers of safety protections to mitigate the risk of API abuse, including automated monitoring and human review of flagged model inputs and outputs. The Realtime API is built on the same version of GPT‑4o that powers Advanced Voice Mode in ChatGPT, which we carefully assessed using both automated and human evaluations, including evaluations according to our [_Preparedness Framework_ ⁠](<https://openai.com/preparedness>), detailed in the [_GPT‑4o System Card_ ⁠](<https://openai.com/index/gpt-4o-system-card/#observed-safety-challenges-evaluations-and-mitigations>). The Realtime API also leverages the same audio safety infrastructure we built for Advanced Voice Mode, which our testing shows has helped to reduce the potential for harm. 

It is against our [_usage policies_ ⁠](<https://openai.com/policies/usage-policies/>) to repurpose or distribute output from our services to spam, mislead, or otherwise harm others – and we actively monitor for potential abuse. Our policies also require developers to make it clear to their users that they are interacting with AI, unless it's obvious from the context. 

Prior to launch, we tested the Realtime API with our external red teaming network and found that the Realtime API didn’t introduce any high-risk gaps not covered by our existing mitigations. As with all API services, the Realtime API is subject to our [_Enterprise privacy_ ⁠](<https://openai.com/enterprise-privacy/>) commitments. We do not train our models on the inputs or outputs used in this service without your explicit permission. 

## Getting started

Developers can start building with the Realtime API over the coming days in the [_Playground_ ⁠(opens in a new window)](<https://platform.openai.com/playground/realtime>), or by using our [_docs_ ⁠(opens in a new window)](<http://platform.openai.com/docs/guides/realtime>) and the [_reference client_ ⁠(opens in a new window)](<https://github.com/openai/openai-realtime-api-beta>).

We’ve also worked with [_LiveKit_ ⁠(opens in a new window)](<https://docs.livekit.io/agents/openai/>) and [_Agora_ ⁠(opens in a new window)](<https://www.agora.io/en/products/agora-openai-conversational-ai-sdk/>) to create client libraries of audio components like echo cancellation, reconnection, and sound isolation, and [_Twilio_ ⁠(opens in a new window)](<https://www.twilio.com/en-us/blog/twilio-openai-realtime-api-launch-integration>) to integrate the Realtime API with [Twilio’s Voice APIs⁠(opens in a new window)](<https://www.twilio.com/en-us/voice>) which enable developers to seamlessly build, deploy and connect AI virtual agents to customers via voice calls.

## What’s next

As we work towards general availability, we’re actively collecting feedback to improve the Realtime API. Some of the capabilities we plan to introduce include:

  * **More modalities:** To start, the Realtime API will support voice, and we plan to add additional modalities like vision and video over time.
  * **Increased rate limits** : Today the API is rate limited to approximately 100 simultaneous sessions for Tier 5 developers, with lower limits for Tiers 1-4. We will increase these limits over time to support larger deployments.
  * **Official SDK support** : We will integrate support for Realtime API into the OpenAI Python and Node.js SDKs.
  * **Prompt Caching:** We will add support for [_Prompt Caching_ ⁠(opens in a new window)](<http://platform.openai.com/docs/guides/prompt-caching>) so previous conversation turns can be reprocessed at a discount.
  * **Expanded model support** : The Realtime API will also support GPT‑4o mini in upcoming versions of that model.



We're looking forward to seeing how developers leverage these new capabilities to create compelling new audio experiences for their users across a variety of use cases from education to translation, customer service, accessibility and beyond. 

  * [API Platform](</news/?tags=api-platform>)
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
