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

July 8, 2026

[Product](</news/product-releases/>)[Release](</research/index/release/>)

# Introducing GPT‑Live

A new generation of voice models for natural human-AI interaction, now powering ChatGPT Voice.

Loading…

Share

 _**Update July 31, 2026:**__Supported audio generated with GPT‑Live through ChatGPT Voice and the OpenAI API now includes SynthID watermarking._[_Our public verification tool_](</research/verify/>) _can now detect OpenAI provenance signals in supported audio files, and we’ve introduced API access for verification so developers and organizations can incorporate provenance checks into their own workflows. These updates build on the safety approach described below and our broader work to make OpenAI-generated content easier to identify._

We’re launching GPT‑Live, a new generation of voice models that make talking with AI feel much more like having a real conversation.

GPT‑Live is built on a full-duplex architecture, meaning it can listen and speak at the same time. During conversations, GPT‑Live can show it’s paying attention with phrases like “mhmm” or “yeah”, engage in quick back-and-forth, or just stay quiet when you need a moment to think. The result is a voice experience that is refreshingly easy to talk to.

GPT‑Live is also our smartest voice model yet. For questions that require web search, deeper reasoning, or more complex work, it delegates to our latest frontier model behind the scenes and brings the result back into the conversation when it’s ready. While it works, GPT‑Live can keep talking with you and maintain the flow of conversation. At launch, GPT‑Live will use GPT‑5.5 in the background. As we release new frontier models, we’ll continuously update the model used by GPT‑Live.

These advances power a new ChatGPT Voice experience that is more intelligent and natural to use. Over time, we believe this research will also unlock the ability to use voice for increasingly complex, longer-running, and more agentic work.

We’re beginning to roll out two versions of GPT‑Live – **GPT‑Live‑1** and **GPT‑Live‑1 mini** – to ChatGPT users globally today. We also plan to bring them to the API soon, and developers and enterprises can sign up to be notified using this [_form_ ⁠](<https://openai.com/form/gpt-live-1-in-the-api/>).

## Entering a new era of human-AI interaction

Our vision is to enable truly natural human–AI interaction: a world where collaborating with AI feels as fluid and responsive as working with another person, while reasoning and complex task execution happen seamlessly in the background.

### Previous approaches

Older generations of voice AI systems brought us closer to that vision, but with important tradeoffs.

### Cascaded voice systems

Cascaded voice systems rely on a series of models acting one after another to process each turn. The [_original ChatGPT Voice_](</index/chatgpt-can-now-see-hear-and-speak/>) chained three models together: a speech-to-text model to transcribe your speech, a large language model to produce a response, and a text-to-speech model to convert it back into speech. This approach enabled us to talk to frontier AI models for the first time, but the complexity came at a cost: information could be lost across models, and responses were slow and stilted.

### Cascaded voice system

Slow and stilted responses, long pauses

STT

GPT-5.5

TTS

STT

GPT-5.5

TTS

Transcript

Example conversation with Standard Voice Mode, using GPT-5.5 Instant

### Turn-based voice models

Turn-based voice models like [_ChatGPT Advanced Voice Mode_](</index/hello-gpt-4o/>) processed and generated audio within a single model, reducing latency and making conversations smoother — but they still operated through discrete turns. The model had to wait for the user to stop speaking before responding, resulting in rigid back-and-forth. In addition, because turn detection is based on silence, even a brief pause or background noise could be mistaken for the end of turn — causing the model to interrupt at unnatural times.

### Turn-based voice model

Slightly faster and smoother responses, but back-and-forth with the model still feels rigid

Transcript

Example conversation with ChatGPT Advanced Voice Mode

### Our new approach

**GPT‑Live** addresses these limitations through two architectural changes.

### Continuous interaction

First, we built GPT‑Live for continuous interaction using a full-duplex architecture**.** Instead of processing a sequence of separate messages, GPT‑Live continuously processes input while generating output. The model can therefore make interaction decisions many times per second: whether to speak, continue listening, pause, interrupt, or invoke a tool.

This allows the model to engage in more natural back-and-forth, maintain a better sense of time, and even perform live translation.

### Continuous interaction

Fast, natural, expressive responses and more active listening

User

GPT-Live-1

Transcript

Example conversation with GPT-Live-1, using GPT-5.5 Instant

### Delegation for deeper work

Second, we decoupled GPT‑Live — which handles continuous interaction — from deeper work. When a question requires search, reasoning, or more agentic capabilities, GPT‑Live can delegate the task to another model like GPT‑5.5. This allows it to keep the conversation going, even as it handles multiple tasks in the background.

This architectural change also allows GPT‑Live to continuously use the latest models and agents, combining frontier intelligence with natural interaction.

### Delegation for deeper work

GPT-Live provides fast, natural responses, while GPT-5.5 handles search in the background

User

GPT-Live-1

GPT-5.5

Search + reason

Transcript

Example conversation with GPT-Live-1, using GPT-5.5 Instant

### Evaluations

We built new human evaluations to measure pleasantness and the flow of conversation. In these head-to-head comparisons, GPT‑Live‑1 and GPT‑Live‑1 mini are strongly preferred over Advanced Voice Mode in matched 5–10 minute conversations that measure overall preference, turn-taking, interruptions, conversational flow, and how natural each interaction felt.

  * GPQA: GPT‑Live‑1 substantially outperforms Advanced Voice Mode on GPQA, which tests expert-level scientific reasoning across biology, chemistry, and physics.
  * BrowseComp: GPT‑Live‑1 shows strong gains over Advanced Voice Mode on BrowseComp, which tests agentic web search and the ability to find difficult-to-locate information.
  * τ³-Voice Telecom (internal variant)**: GPT‑Live‑1 outperforms Advanced Voice Mode on τ³-Voice Telecom, which tests voice agents on realistic, multi-turn telecom support tasks.



* GPT‑Live‑1 (instant) and GPT‑Live‑1 mini use the GPT‑5.5 Instant model in the background, while GPT‑Live‑1 Medium and GPT‑Live‑1 High use the GPT‑5.5 Thinking model with medium and high reasoning effort.

** We used a customized user model, powered by our latest reasoning models, for this eval.

## A new ChatGPT Voice experience

Each week, more than 150 million people talk to ChatGPT using features like Voice and Dictation. They use it to get hands-free everyday help, to practice languages, tell bedtime stories, or just chat during their commute.

Starting today, when you tap the Voice button to talk with ChatGPT, you’ll get an improved experience powered by GPT‑Live—with more natural conversations, smarter answers, better listening, and visual responses.

### More natural conversations

Talking with ChatGPT should now feel much more like a real conversation. You can interrupt with a question, pause to gather your thoughts, or ask ChatGPT to slow down. It naturally acknowledges what you’re saying with phrases like “mhmm” or “got it,” so you know it’s following along. We’ve also remastered the nine distinct voices in ChatGPT for GPT‑Live.

### Smarter answers

ChatGPT Voice can now draw on our latest frontier models, giving you smarter answers when you need them. You can also choose the level of reasoning that fits your needs: Instant for fast responses, or Medium and High when you want ChatGPT to spend more time thinking.

### Better listening

If you take a moment to think, ChatGPT Voice now waits instead of jumping in and interrupting. If you ask it to stay quiet and listen, it will. And when there’s background noise, like passing traffic or nearby conversations, ChatGPT is better at focusing on your voice instead of getting distracted.

### Visual answers at a glance

Some answers are more useful when you can see them. While you’re talking, ChatGPT can now show rich visual cards for topics like weather, stocks, sports, and more. Voice also continues to support search, memory, images, and file uploads.

![ChatGPT Voice displaying a weather forecast for Denver, Colorado.](https://images.ctfassets.net/kftzwdyauwt9/38TRAE6B8AS3hNkoQuKSOl/729b7c415ed4c1b62027449799cead86/gpt-live-visual-answer-weather.png?w=3840&q=90&fm=webp)

![ChatGPT Voice displaying upcoming international football matches.](https://images.ctfassets.net/kftzwdyauwt9/7IWfPZwH8SaJVikq4PScQP/f327d0d73d35b3989b8d504d5e9fa782/gpt-live-visual-answer-sports.png?w=3840&q=90&fm=webp)

![ChatGPT Voice displaying a map with nearby soccer pubs.](https://images.ctfassets.net/kftzwdyauwt9/GLkTfEhJSFJZ77FHnN1f6/b1ab29d652268636a226246f5b1766cc/gpt-live-visual-answer-maps.png?w=3840&q=90&fm=webp)

The result is a ChatGPT Voice experience that feels more natural, more capable, and more useful in everyday life.

## Safety designed for voice

GPT‑Live was designed to be safe by default. It builds on the safety advances from our latest models while adding dedicated safety training across key risk areas and new safeguards designed specifically for voice.

### Expanded safety testing

To better reflect how people use voice in real-life settings, we began by expanding our safety testing to include new audio-native evaluations. We also created synthetic evaluations that use generated audio to focus more intensively on key safety areas, drawing on what we learned from Advanced Voice Mode. Those areas include self-harm, psychosis and mania, [_emotional reliance on AI_](</index/strengthening-chatgpt-responses-in-sensitive-conversations/>) , violence, and sexual content. Internal experts also red-teamed the model for risks unique to voice.

In our testing, GPT‑Live performed comparably to or better than Advanced Voice Mode across nearly all of the areas we evaluated. You can read more about our testing and safeguards in the GPT‑Live [_system card_ ⁠(opens in a new window)](<https://deploymentsafety.openai.com/gpt-live>).

### Built-in safeguards

Because voice conversations unfold in real time, we also built safeguards that can act while the model is speaking. When the system detects potentially unsafe output, it can steer the model toward a safer response, surface additional safety messaging or resources, or end the voice conversation in higher-risk cases. For conversations involving self-harm, we adapted ChatGPT’s support flows for voice, including offering expert-vetted crisis helpline support.

We designed additional protections to support teen users, and trained age-appropriate behavior directly into the model to reduce the risk of inappropriate responses. Parents can choose whether their teen can use ChatGPT Voice through Parental Controls, and linked parents may be notified in higher-risk situations involving signs of potential self-harm or suicidal intent.

### Learning from real-world use

We’re also rolling out longer-term measurement and post-launch monitoring focused on emotional reliance to continue improving our understanding and refining safeguards. Building on our previous research into [_affective use and emotional well-being_](</index/affective-use-study/>) , this will help us identify emerging patterns and improve how the system responds in emotionally sensitive interactions.

Finally, GPT‑Live is designed for conversation, not voice impersonation. It uses a set of predefined voices in ChatGPT, with safeguards to prevent it from imitating a real person’s voice.

We’re committed to supporting safety and well-being and will keep strengthening these protections as we learn from real-world use.

## Availability & limitations

GPT‑Live is rolling out now to ChatGPT users globally across iOS, Android, and [_ChatGPT.com_ ⁠(opens in a new window)](<https://chatgpt.com/>). GPT‑Live‑1 will become the default model powering ChatGPT Voice for Go, Plus, and Pro users, and GPT‑Live‑1 mini will become the default for Free users. More availability details can be found in our [_Help Center_ ⁠(opens in a new window)](<https://help.openai.com/articles/20001274>).

We’ve optimized GPT‑Live for some of the most popular languages in ChatGPT. For certain languages, the model may have a non-native accent or gaps in fluency. We’re actively working to improve the experience across languages.

At launch, GPT‑Live will not support voice with video or screen sharing in ChatGPT, but we’re working to introduce these capabilities soon. You can still access legacy versions of ChatGPT Voice, including Standard and Advanced Voice Mode, where these features are available.

  * [2026](</news/?tags=2026>)
  * [ChatGPT](</news/?tags=chatgpt>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Healthcare hero and SEO — original blue icon on white, smaller icon](https://images.ctfassets.net/kftzwdyauwt9/7pfIDODSObT8A9BTlfXyVc/43262863eeb33d7f4f8e191fe4783cab/healthcare-exact-smaller-icon-hero-2x.png?w=3840&q=90&fm=webp)

[ChatGPT can now connect to healthcare sourcesProductSep 1, 2026](</index/chatgpt-connects-health-records-and-healthcare-sources/>)

![Expanding access to AI > Cover image](https://images.ctfassets.net/kftzwdyauwt9/x3ij3VqMj60KcdHucQvNc/414ce018aafcf0916557e004ee112d71/expanding-access-to-ai--art-card-purple-v001.png?w=3840&q=90&fm=webp)

[A milestone in expanding access to AIProductAug 31, 2026](</index/expanding-access-to-ai-with-chatgpt-ads/>)

![ChatGPT for Teachers district expansion | Original neutral library cover](https://images.ctfassets.net/kftzwdyauwt9/4jHps0gmVQfIrnl2shwDBi/35e47854409876d353f3bb502a164317/teachers-original-neutral-listing.png?w=3840&q=90&fm=webp)

[Bringing ChatGPT for Teachers to more U.S. school districtsProductAug 26, 2026](</index/bringing-chatgpt-for-teachers-to-more-us-school-districts/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)
  * [GPT-5.4](</index/introducing-gpt-5-4/>)



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
  * [Supply Co.](</supply/>)
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
