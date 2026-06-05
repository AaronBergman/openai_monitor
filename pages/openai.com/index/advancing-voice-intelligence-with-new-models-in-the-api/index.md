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

  * Voice as an interface between people and products
  * Realtime voice: helping voice models reason and take action
  * Realtime translation: build live multilingual voice experiences
  * Realtime transcription: build low-latency transcription experiences
  * Safety
  * Pricing & availability
  * Get started



May 7, 2026

[Product](</news/product-releases/>)[Release](</research/index/release/>)

# Advancing voice intelligence with new models in the API

A new generation of realtime voice models that can reason, translate, and transcribe as people speak.

Loading…

Share

We’re introducing three audio models in the API that unlock a new class of voice apps for developers. With these models, developers can build voice experiences that feel more natural, respond more intelligently, and take action in real time:

  * **GPT‑Realtime‑2** , our first voice model with GPT‑5‑class reasoning that can handle harder requests and carry the conversation forward naturally.
  * **GPT‑Realtime‑Translate** , a new live translation model that translates speech from 70+ input languages into 13 output languages while keeping pace with the speaker.
  * **GPT‑Realtime‑Whisper** , a new streaming speech-to-text that transcribes speech live as the speaker talks.



# Try GPT-Realtime-2

Start the session, then talk naturally with GPT-Realtime-2.

Start sessionWhat can I ask?

After you start the session, try saying one of these:

  * I’m hosting a last-minute dinner tonight. I have 30 minutes, two vegetarian friends, one mushroom-hater, and a tiny kitchen. Help me plan a simple menu.
  * I’m welcoming guests to a live event in Japan. Say a warm, natural welcome in Japanese — like a host kicking off something special.
  * My order number is Orbit-742Q. Repeat it back clearly so I can confirm it’s right.
  * Help me practice telling my team we hit our launch milestone. First say it with quiet confidence, then with more excitement.
  * I’m planning trivia for a road trip. Give me three trick questions that sound deceivingly simple, then explain each answer in one sentence.



This demo is time-limited. By using it, you agree to OpenAI's [Terms](</policies/terms-of-use/>) and acknowledge our [Privacy Policy](</policies/privacy-policy/>).

## 

Voice is becoming one of the most natural ways for people to use software. It lets someone ask for help while driving, change a travel plan while walking through an airport, get support in their preferred language, or move through a task without stopping to type.

But building useful voice products takes more than fast turn-taking or a natural-sounding voice. A voice agent needs to understand what someone means, keep track of context, recover when a request changes, use tools while the conversation continues, and respond in a way that feels appropriate to the moment.

Together, the models we are launching move realtime audio from simple call-and-response toward voice interfaces that can actually do work: listen, reason, translate, transcribe, and take action as a conversation unfolds.

## Voice as an interface between people and products

As voice becomes a more natural way to use software, we’re seeing developers build around three emerging patterns in voice AI:

  * **Voice-to-action,** where people can describe what they need and the system can reason through the request, use tools, and complete the task. For example, Zillow is building an assistant that can listen, reason, and act on requests like: “find me homes within my BuyAbility, avoid busy streets, and schedule a tour for Saturday.”
  * **Systems-to-voice,** where software can turn context into live spoken guidance. For example, a travel app could proactively tell a traveler: “Your inbound flight is delayed, but you can still make your connection. I found the new gate, mapped the fastest route through the terminal, and your bag is still expected to transfer.”
  * **Voice-to-voice,** where AI can help live conversations continue across languages, tasks, or changing context. For example, Deutsche Telekom is building voice support experiences where customers can speak in the language they’re most comfortable using, while the model translates the conversation in real time.



![Diagram showing three voice AI workflows: voice-to-action connecting speech to apps like code and dev, shopping, in-car, and scheduling tools; systems-to-voice connecting apps, calendars, CRM, and support dashboards to speech; and voice-to-voice connecting two voice agents.](https://images.ctfassets.net/kftzwdyauwt9/32pQSj9Ayvkt9QSZpOPdky/470716092a7230e92e9670dba0ad410d/OAI_GPT-Realtime-2_Three_ways_to_build_with_voice_AI_desktop-light.svg?w=3840&q=90)

These patterns can also work together. Priceline is working toward a future where travelers can manage entire trips by voice: searching for flights and hotels conversationally, handling changes like adjusting a hotel reservation after a flight delay or getting real-time updates on TSA wait times, and translating conversations once travelers are on the ground.

## Realtime voice: helping voice models reason and take action

GPT‑Realtime‑2 is built for live voice interactions where the model keeps the conversation moving while it reasons through a request, calls tools, handles corrections or interruptions, and responds in a way that fits the moment.

  * **Preambles:** Developers can enable short phrases before a main response, like “let me check that” or “one moment while I look into it,” so users know the agent is working on the request.
  * **Parallel tool calls and tool transparency:** The model can call multiple tools at once and make those actions audible with phrases like “checking your calendar” or “looking that up now,” helping agents stay responsive while completing tasks.
  * **Stronger recovery behavior:** The model can recover more gracefully by saying things like “I’m having trouble with that right now,” instead of failing silently or breaking the conversation.
  * **Longer context for agentic workflows:** We’re increasing the context window from 32K to 128K to support longer, more coherent sessions and more complex task flows.
  * **Stronger domain understanding:** The model better retains specialized terminology, proper nouns, healthcare terms, and other vocabulary that matters in production settings.
  * **More controllable tone and delivery:** The model can better adjust its tone—speaking calmly while resolving an issue, empathetically when a user is frustrated, or upbeat when confirming a successful action.
  * **Adjustable reasoning effort:** Developers can now select from **minimal, low, medium, high, and xhigh** reasoning levels, with **low as the default** , balancing lower latency for straightforward interactions with more deliberate reasoning for complex requests.



The gains show up on audio evals that map closely to production voice agents: GPT‑Realtime‑2 (high) scores 15.2% higher on Big Bench Audio for audio intelligence than GPT‑Realtime‑1.5. GPT‑Realtime‑2 (xhigh) scores 13.8% higher on Audio MultiChallenge for instruction following, improving over GPT‑Realtime‑1.5 and showing stronger reasoning, context management, and control in live conversations.

[Big Bench Audio⁠](< https://artificialanalysis.ai/methodology/speech-to-speech-benchmarking>) evaluates challenging reasoning capabilities in language models that support audio input. [Audio MultiChallenge⁠(opens in a new window)](<https://labs.scale.com/leaderboard/audiomc-audio>) evaluates multi-turn conversational intelligence in spoken dialogue systems, including instruction following, context integration, self-consistency, and handling natural speech corrections.

The magic of GPT‑Realtime‑2 shows up across a variety of different use cases:

Strategic reasoningTone and expressivenessSpatial reasoningAlphanumericsLogic puzzle

Loading realtime example…

During early testing, businesses used GPT‑Realtime‑2 to build voice agents that help customers and employees get things done through natural conversation:

ZillowGleanGensparkBluejayIntercomPricelineFoundation Health

> “What stood out about GPT-Realtime-2 was the intelligence and tool-calling reliability it brings to complex voice interactions. On our hardest adversarial benchmark, this translates to a 26-point lift in call success rate after prompt optimization (95% vs. 69%). GPT-Realtime-2 is also materially more robust on Fair Housing compliance, which is critical for our business. The combination of agentic competence and guardrail strength is what makes it viable for production voice at Zillow.”

— Josh Weisberg, SVP and Head of AI at Zillow

## Realtime translation: build live multilingual voice experiences

GPT‑Realtime‑Translate helps developers build live multilingual voice experiences where each person can speak in their preferred language and hear the conversation translated in real time and read the real time transcriptions. It supports more than 70 input languages and 13 output languages, making it useful for customer support, cross-border sales, education, events, media, and creator platforms serving global audiences.

For developers, live translation needs to preserve meaning while keeping pace with the speaker, even when people speak naturally, switch context, or use regional pronunciation and domain-specific language. For example, Deutsche Telekom is testing the model for multilingual voice interactions, where lower latency and stronger fluency can make cross-language conversations feel more natural.

In this video, Vimeo shows how GPT‑Realtime‑Translate can translate a product education video live as it plays, so global customers can hear updates in their preferred language without waiting for a separately produced version.

BolnaAIVimeoDeutsche Telekom

> “Building voice AI for India means handling diverse regional phonetics. In our evals across Hindi, Tamil, and Telugu, GPT-Realtime-Translate delivered 12.5% lower Word Error Rates than any other model we tested, along with lower fallback rates, higher task completion, and latency that sustained natural conversation. It sets a new standard for multilingual voice AI.”

— Prateek Sachan, Co-founder & CTO at BolnaAI

## Realtime transcription: build low-latency transcription experiences

GPT‑Realtime‑Whisper is a new streaming transcription model built for low-latency speech-to-text. It transcribes audio as people speak, so live products can feel faster, more responsive, and more natural—from captions that appear in the moment, to meeting notes that keep up with the conversation.

The model makes live speech usable inside business workflows as it happens. Teams can power captions for meetings, classrooms, broadcasts, and events; generate notes and summaries while conversations are still in progress; build voice agents that need to understand users continuously; and create faster follow-up workflows for customer support, healthcare, sales, recruiting, and other high-volume spoken interactions.

## Safety

The Realtime API incorporates multiple layers of safeguards and mitigations to help prevent misuse. We employ active classifiers over Realtime API sessions, meaning certain conversations can be halted if they are detected as violating our harmful content guidelines. Developers can also easily add their own additional safety guardrails using the [Agents SDK⁠.⁠(opens in a new window)](<https://openai.github.io/openai-agents-js/guides/guardrails/>)

Our [usage policies⁠⁠](<https://openai.com/policies/usage-policies/>) prohibit repurposing or distributing outputs from our services for spam, deception, or other harmful purposes. Developers must also make it clear to end users when they’re interacting with AI, unless it’s already obvious from the context.

The Realtime API fully supports [EU Data Residency⁠⁠(opens in a new window)](<https://platform.openai.com/docs/guides/your-data#data-residency-controls>) for EU-based applications and is covered by our [enterprise privacy commitments⁠⁠](<https://openai.com/enterprise-privacy/>).

## Pricing & availability

GPT‑Realtime‑2, GPT‑Realtime‑Translate and GPT‑Realtime‑Whisper are available in the Realtime API. GPT‑Realtime‑2 is priced at $32 / 1M audio input tokens ($0.40 for cached input tokens) and $64 / 1M audio output tokens. GPT‑Realtime‑Translate is priced at $0.034 per minute. GPT‑Realtime‑Whisper is priced at $0.017 per minute. 

## Get started

You can test the new realtime voice models in the [Playground⁠(opens in a new window)](<https://platform.openai.com/audio/realtime>). 

To start building, [open this prompt in Codex⁠](<codex://new?prompt=Build+or+add+a+minimal+Realtime+2+WebRTC+voice+agent+using+the+gpt-realtime-2+model.%0A%0AUse+the+latest+OpenAI+Realtime+API+docs+for+the+WebRTC+and+session+setup+patterns.+If+this+folder+already+contains+an+app%2C+add+it+to+the+existing+app.+Otherwise%2C+create+a+small+local+web+app.+Add+a+server-side+session+endpoint+that+uses+OPENAI_API_KEY+and+posts+browser+SDP+to+%2Fv1%2Frealtime%2Fcalls+following+the+docs+exactly%3A+multipart+FormData+fields+named+sdp+and+session%2C+not+file+uploads.+Connect+browser+microphone+input+and+model+audio+output+with+RTCPeerConnection%2C+open+an+oai-events+data+channel%2C+and+register+one+sample+function+tool+with+session.update%3A+check_calendar%28date%2C+time%29%2C+which+returns+whether+the+requested+time+is+available.%0A%0AKeep+it+small+and+include+setup%2Frun+instructions.>) to add GPT‑Realtime‑2 to an existing app or start a new one. If you don’t have Codex yet, download the [Codex app⁠](<https://openai.com/codex/>) first.

  * [2026](</news/?tags=2026>)
  * [API Platform](</news/?tags=api-platform>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Art Card 1080x1080 \(3\)](https://images.ctfassets.net/kftzwdyauwt9/3JLNH7ejJFnxLmX2LpzoKD/19f9e3c4d36cc9d677ba88e842ad2db2/Art_Card_1080x1080__4_.png?w=3840&q=90&fm=webp)

Better memory for a more helpful ChatGPT

[Dreaming: Better memory for a more helpful ChatGPTResearchJun 4, 2026](</index/chatgpt-memory-dreaming/>)

![Rosalind5.5 ArtCard](https://images.ctfassets.net/kftzwdyauwt9/6USIQM1B7TggUvvTFxxwoi/0176ac6633c8bdc24641d25d1d2db824/GPT-Rosalind_ArtCard.png?w=3840&q=90&fm=webp)

[Introducing new capabilities to GPT-RosalindProductJun 3, 2026](</index/introducing-new-capabilities-to-gpt-rosalind/>)

![1 1 Art Card](https://images.ctfassets.net/kftzwdyauwt9/4xugzd9dTDMUzIUmuamtO3/1f40af4e50ab8b2bdd64d5b491964961/1_1_Art_Card.png?w=3840&q=90&fm=webp)

[Codex for every role, tool, and workflowProductJun 2, 2026](</index/codex-for-every-role-tool-workflow/>)

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
