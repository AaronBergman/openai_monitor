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

  * Introducing gpt-realtime
  * New in the Realtime API
  * Safety & privacy
  * Pricing & availability
  * Livestream replay



August 28, 2025

[Product](</news/product-releases/>)[Release](</research/index/release/>)

# Introducing gpt-realtime and Realtime API updates for production voice agents

We’re releasing a more advanced speech-to-speech model and new API capabilities including MCP server support, image input, and SIP phone calling support.

![Stylized interface showing a voice interaction. Centered is a rounded rectangular audio player with a waveform visualization, play/pause button, “Agent online” status indicator, and timestamp of 00:35. White curved lines with dots flow across the image, suggesting live audio or signal movement. The background is a vivid blue with blurred flower shapes in pink and purple tones.](https://images.ctfassets.net/kftzwdyauwt9/2P07oLbgCw1M528pOZGvBn/e47130e97d7d0481f0c58c74c4cdeed3/oai_realtime-api-ga_blog-header.png?w=3840&q=90&fm=webp)

Loading…

Share

Today we’re making the Realtime API generally available with new features that enable developers and enterprises to build reliable, production-ready voice agents. The API now supports remote MCP servers, image inputs, and phone calling through Session Initiation Protocol (SIP), making voice agents more capable through access to additional tools and context.

We’re also releasing our most advanced speech-to-speech model yet—`gpt-realtime`. The new model shows improvements in following complex instructions, calling tools with precision, and producing speech that sounds more natural and expressive. It’s better at interpreting system messages and developer prompts—whether that’s reading disclaimer scripts word-for-word on a support call, repeating back alphanumerics, or switching seamlessly between languages mid-sentence. We’re also releasing two new voices, Cedar and Marin, which are available exclusively in the Realtime API starting today.

Since we first introduced the Realtime API in public beta last October, thousands of developers have built with the API and helped shape the improvements we’re releasing today—optimized for reliability, low latency, and high quality to successfully deploy voice agents in production. Unlike traditional pipelines that chain together multiple models across speech-to-text and text-to-speech, the Realtime API processes and generates audio directly through a single model and API. This reduces latency, preserves nuance in speech, and produces more natural, expressive responses.

ZillowT-MobileStubHubOscar HealthLemonade

“The new speech-to-speech model in OpenAI's Realtime API shows stronger reasoning and more natural speech—allowing it to handle complex, multi-step requests like narrowing listings by lifestyle needs or guiding affordability discussions with tools like our BuyAbility score. This could make searching for a home on Zillow or exploring financing options feel as natural as a conversation with a friend, helping simplify decisions like buying, selling, and renting a home.”

– Josh Weisberg, Head of AI at **Zillow**

##  Introducing gpt-realtime

The new speech-to-speech model—`gpt-realtime`—is our most advanced, production-ready voice model. We trained the model in close collaboration with customers to excel at real-world tasks like customer support, personal assistance, and education—aligning the model to how developers build and deploy voice agents. The model shows improvements across audio quality, intelligence, instruction following, and function calling.

#### Audio quality

Natural-sounding conversation is critical for deploying voice agents in the real world. Models need to speak with the intonation, emotion, and pace of a human to create an enjoyable experience and encourage continuous conversation with users. We trained `gpt-realtime` to produce higher-quality speech that sounds more natural and can follow fine-grained instructions, such as “speak quickly and professionally” or “speak empathetically in a French accent.”

We’re releasing two new voices in the API, Marin and Cedar, with the most significant improvements to natural-sounding speech. We’re also updating our existing eight voices to benefit from these improvements.

Voice sample - Marin

Voice sample - Cedar

#### Intelligence and comprehension

`gpt-realtime` shows higher intelligence and can comprehend native audio with greater accuracy. The model can capture non-verbal cues (like laughs), switch languages mid-sentence, and adapt tone (“snappy and professional” vs. “kind and empathetic”). According to internal evaluations, the model also shows more accurate performance in detecting alphanumeric sequences (such as phone numbers, VINs, etc) in other languages, including Spanish, Chinese, Japanese, and French. On the Big Bench Audio eval measuring reasoning capabilities, `gpt-realtime` scores 82.8% accuracy—beating our previous model from December 2024, which scores 65.6%.

The [Big Bench Audio⁠(opens in a new window)](<https://huggingface.co/datasets/ArtificialAnalysis/big_bench_audio>) benchmark is an evaluation dataset for assessing the reasoning capabilities of language models that support audio input. This dataset adapts questions from Big Bench Hard—chosen for its rigorous testing of advanced reasoning—into the audio domain.

#### Instruction following

When building a speech-to-speech application, developers give a set of instructions to the model on how to behave, including how to speak, what to say in a certain situation, and what to do or not do. We’ve focused our improvements on the adherence to these instructions, so that even minor directions carry more signal for the model. On the MultiChallenge audio benchmark measuring instruction following accuracy, `gpt-realtime` scores 30.5%, a significant improvement over our previous model from December 2024, which scores 20.6%.

[MultiChallenge⁠(opens in a new window)](<https://arxiv.org/abs/2501.17399>) evaluates how well LLMs handle multi-turn conversations with humans. It focuses on four categories of realistic challenges that current frontier models struggle with. These challenges require models to combine instruction-following, context management, and in-context reasoning simultaneously. We converted an audio-friendly subset of the test questions from text-to-speech to create an audio version of this evaluation.

#### Function calling

To build a capable voice agent with a speech-to-speech model, the model needs to be able to call the right tools at the right time to be useful in production. We’ve improved function calling on three axes: calling relevant functions, calling functions at the appropriate time, and calling functions with appropriate arguments (resulting in higher accuracy). On the ComplexFuncBench audio eval measuring function calling performance, `gpt-realtime` scores 66.5%, while our previous model from December 2024 scores 49.7%.

We’ve also made improvements to [asynchronous function calling⁠(opens in a new window)](<http://platform.openai.com/docs/guides/realtime-function-calling>). Long-running function calls will no longer disrupt the flow of a session—the model can continue a fluid conversation while waiting on results. This feature is available natively in `gpt-realtime`, so developers do not need to update their code. 

[ComplexFuncBench⁠(opens in a new window)](<https://github.com/zai-org/ComplexFuncBench>) measures how well models handle challenging function calling tasks. It evaluates performance across scenarios like multi-step calls, reasoning about constraints or implicit parameters, handling very long inputs. We converted the original text prompts into speech to build this evaluation for our model.

## New in the Realtime API

#### Remote MCP server support

You can enable MCP support in a Realtime API session by passing the URL of a remote MCP server into the session configuration. Once connected, the API automatically handles the tool calls for you, so there’s no need to wire up integrations manually.

This setup makes it easy to extend your agent with new capabilities—just point the session to a different MCP server, and those tools become available right away. To learn more about configuring MCP with Realtime, check out [this guide⁠(opens in a new window)](<http://platform.openai.com/docs/guides/realtime-mcp>).

#### JavaScript

`
    
    
    1
    
    // POST /v1/realtime/client_secrets
    
    2
    
    {
    
    3
    
      "session": {
    
    4
    
        "type": "realtime",
    
    5
    
        "tools": [
    
    6
    
          {
    
    7
    
            "type": "mcp",
    
    8
    
            "server_label": "stripe",
    
    9
    
            "server_url": "https://mcp.stripe.com",
    
    10
    
            "authorization": "{access_token}",
    
    11
    
            "require_approval": "never"
    
    12
    
          }
    
    13
    
        ]
    
    14
    
      }
    
    15
    
    }
    
    16
    
      
    

`

#### Image input

With image inputs now supported in `gpt-realtime`, you can add images, photos, and screenshots alongside audio or text to a Realtime API session. Now the model can ground the conversation in what the user is actually seeing, enabling users to ask questions like “what do you see?” or “read the text in this screenshot.”

Instead of treating an image like a live video stream, the system treats it more like adding a picture into the conversation. Your app can decide which images to share with the model and when to share them. This way, you stay in control of what the model sees and when it responds.

Check out our [_docs_ ⁠(opens in a new window)](<http://platform.openai.com/docs/guides/realtime-inputs-outputs>) to get started with image input.

#### JavaScript

`
    
    
    1
    
    {
    
    2
    
        "type": "conversation.item.create",
    
    3
    
        "previous_item_id": null,
    
    4
    
        "item": {
    
    5
    
            "type": "message",
    
    6
    
            "role": "user",
    
    7
    
            "content": [
    
    8
    
                {
    
    9
    
                    "type": "input_image",
    
    10
    
                    "image_url": "data:image/{format(example: png)};base64,{some_base64_image_bytes}"
    
    11
    
                }
    
    12
    
            ]
    
    13
    
        }
    
    14
    
    }
    
    15
    
      
    

`

#### Additional capabilities

We’ve added several other features to make the Realtime API easier to integrate and more flexible for production use. 

  * **Session Initiation Protocol (SIP) support:** Connect your apps to the public phone network, PBX systems, desk phones, and other SIP endpoints with direct support in the Realtime API. [Read about it in docs.⁠(opens in a new window)](<http://platform.openai.com/docs/guides/realtime-sip>)
  * **Reusable prompts:** You can now save and reuse prompts—consisting of developer messages, tools, variables, and example user/assistant messages—across Realtime API sessions, like in the Responses API. [Learn more in docs.⁠(opens in a new window)](<http://platform.openai.com/docs/guides/realtime-models-prompting>)



## Safety & privacy

The Realtime API incorporates multiple layers of safeguards and mitigations to help prevent misuse. You can learn more about our safety approach and system card details in the [beta announcement blog⁠](</index/introducing-the-realtime-api/>). We employ active classifiers over Realtime API sessions, meaning certain conversations can be halted if they are detected as violating our harmful content guidelines. Developers can also easily add their own additional safety guardrails using the [Agents SDK⁠(opens in a new window)](<https://openai.github.io/openai-agents-js/guides/guardrails/>).

Our [usage policies⁠](</policies/usage-policies/>) prohibit repurposing or distributing outputs from our services for spam, deception, or other harmful purposes. Developers must also make it clear to end users when they’re interacting with AI, unless it’s already obvious from the context. The Realtime API uses preset voices to help prevent malicious actors from impersonating others.

The Realtime API fully supports [EU Data Residency⁠(opens in a new window)](<https://platform.openai.com/docs/guides/your-data#data-residency-controls>) for EU-based applications and is covered by our [enterprise privacy commitments⁠](</enterprise-privacy/>).

## Pricing & availability

The generally available Realtime API and new `gpt-realtime` model are available to all developers starting today. We’re reducing prices for `gpt-realtime` by 20% compared to `gpt-4o-realtime-preview`—$32 / 1M audio input tokens ($0.40 for cached input tokens) and $64 / 1M audio output tokens (see [detailed pricing⁠(opens in a new window)](<https://platform.openai.com/docs/pricing#audio-tokens>)). We’ve also added fine-grained control for conversation context to let developers set intelligent token limits and truncate multiple turns at a time, significantly reducing cost for long sessions.

To get started, visit our [Realtime API documentation⁠(opens in a new window)](<https://platform.openai.com/docs/guides/realtime>), test the new model in the [Playground⁠(opens in a new window)](<https://platform.openai.com/audio/realtime>), and view our [Realtime API prompting guide⁠(opens in a new window)](<https://platform.openai.com/docs/guides/realtime-models-prompting>).

## Livestream replay

  * [2025](</news/?tags=2025>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![20250826](https://images.ctfassets.net/kftzwdyauwt9/2H347RfdThVOeTfSBchxDx/8a053f4cfa92faeed7141265dd02e7dd/20250826.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 Instant: smarter, clearer, and more personalizedProductMay 5, 2026](</index/gpt-5-5-instant/>)

![New ways to buy ChatGPT ads > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/3Rxyg8znQWIKixzNDvJtEE/87399a6c50caa6aaadbd664409021f82/ArtCard-ChatGPT-Ads.png?w=3840&q=90&fm=webp)

[New ways to buy ChatGPT adsProductMay 5, 2026](</index/new-ways-to-buy-chatgpt-ads/>)

![Introducing Advanced Account Security ](https://images.ctfassets.net/kftzwdyauwt9/4qS0zHVYqjyQCXbjR0GBgo/afaf8ff54069198f148dec57aa40461b/ArtCard-Introducing_Advanced_Account_Security_for_ChatGPT_accounts.png?w=3840&q=90&fm=webp)

[Introducing Advanced Account SecurityProductApr 30, 2026](</index/advanced-account-security/>)

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
