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

May 12, 2026

[Research](</news/research/>)

# What Parameter Golf taught us

Lessons from 1,000+ participants, 2,000+ submissions, and an open machine learning challenge shaped by coding agents.

Loading…

Share

Technical impressions

  * Technical impressions

    * Record track

    * Nonrecord track

  * Takeaways

  * What’s next?




  * Technical impressions

    * Record track

    * Nonrecord track

  * Takeaways

  * What’s next?




We launched Parameter Golf to engage and support the machine learning research community in exploring a new, tightly constrained machine learning problem. We wanted the challenge to be interesting enough to reward real technical creativity, while remaining conceptually simple and easy to verify.

Participants had to minimize held-out loss on a fixed FineWeb dataset while staying within a 16 MB artifact limit, including both model weights and training code, and a 10-minute training budget on 8×H100s. We provided a baseline, dataset, and evaluation scripts so participants could fork the repo, improve the model, and submit their results through GitHub.

Over the course of eight weeks, we received more than 2,000 submissions from over 1,000 participants. We were impressed by the technical breadth, creativity, and rule-bending across the submissions, from careful optimizer tuning and quantization work to new modeling ideas and test-time training.

One of the most exciting parts of the challenge was seeing how widely participants used AI coding agents. Agents helped lower the cost of experimentation, made it easier for more people to participate, and changed the pace of the competition. They also created new challenges for submission review, attribution, and scoring.

The challenge also became a meaningful talent discovery surface for us. That was one of our goals for Parameter Golf, and it was a useful signal that open-ended technical challenges can reveal exceptional machine learning taste and persistence.

In this post, we highlight some of the submissions we found surprising and interesting, and share what we learned from running a coding contest in the age of powerful AI agents.

## Technical impressions

### Record track

We judged and independently reproduced each submission on the record-track leaderboard, and verified that each submission was record-breaking at the time it was submitted. Several themes stood out.

_**Training optimization**_

Some of the strongest results came from careful tuning of existing components.

**Submission**| **Contributor**| **Technique**| **Why it mattered**  
---|---|---|---  
[#60](<https://github.com/openai/parameter-golf/pull/60>)| @notapplica| Combined prior wins from [#50](<https://github.com/openai/parameter-golf/pull/50>), [#42](<https://github.com/openai/parameter-golf/pull/42>), and likely [#39](<https://github.com/openai/parameter-golf/pull/39>), then made a deeper model work with Muon weight decay, spectral embedding initialization, residual-mix scheduling, and compiled evaluation.| A strong example of disciplined leaderboard work: identifying which existing improvements matter and combining them cleanly.  
  
_**Quantization**_

Several submissions pushed hard on compression and export.

**Submission**| **Contributor**| **Technique**| **Why it mattered**  
---|---|---|---  
[#414](<https://github.com/openai/parameter-golf/pull/414>)| @signalrush| Used GPTQ-lite to quantize weights after training.| The first leaderboard submission to successfully use GPTQ-lite, leading to better evaluation.  
[#1060](<https://github.com/openai/parameter-golf/pull/1060>)| @dexhunter| Built on [#634](<https://github.com/openai/parameter-golf/pull/634>) by @raahilshah to successfully use full Hessian GPTQ.| Extended earlier quantization work into a stronger compression path.  
  
_**Test-time and evaluation strategies**_

Some submissions pushed the boundary between model improvement and evaluation strategy. These approaches were valid under the rules, but they required careful review from us as organizers.

**Submission**| **Contributor**| **Technique**| **Why it mattered**  
---|---|---|---  
[#77](<https://github.com/openai/parameter-golf/pull/77>)| @samacqua| Used score-first, per-document LoRA test-time training: score first, adapt only on already-scored chunks, and reset at document boundaries.| Pushed the boundary between model improvement and evaluation strategy while staying reviewable under the rules.  
[#1019](<https://github.com/openai/parameter-golf/pull/1019>)| @abaybektursun| Used self-generated GPTQ calibration: generate calibration text from the trained model, then build GPTQ Hessians from those activations.| A creative calibration strategy that required careful review from organizers.  
  
_**New modeling and data ideas**_

A few submissions introduced modeling or data ideas that were especially creative.

**Submission**| **Contributor**| **Technique**| **Why it mattered**  
---|---|---|---  
[#1729](<https://github.com/openai/parameter-golf/pull/1729>)| @romeerp| Introduced the CaseOps tokenizer: lossless capitalization operator tokens with original-byte BPB sidecar accounting.| A creative tokenizer and data-representation idea.  
[#265](<https://github.com/openai/parameter-golf/pull/265>)| @unnir| Introduced XSA, an efficient partial Exclusive Self Attention approach with GQA-aware grouped views.| Brought an efficient attention variant into the challenge.  
[#65](<https://github.com/openai/parameter-golf/pull/65>)| @aquariouseworkman| Introduced SmearGate and BigramHash: a learned previous-token embedding blend plus adjacent-token-pair hash features.| Added new feature mechanisms from scratch.  
[#1204](<https://github.com/openai/parameter-golf/pull/1204>)| @msisovic| Introduced mini depth recurrence: repeated layers 4 and 5, delayed recurrence until mid-training, and partially untied the repeated MLPs.| The first accepted leaderboard row to make recurrent layers work effectively.  
  
We chose to highlight these nine submissions because they represent the range of results we hoped the challenge would surface. Some participants found wins through careful tuning. Others pushed quantization and low-rank techniques. Some explored edges of the evaluation rules. And several introduced modeling or data ideas, from the literature or from scratch, that produced unexpected gains.

### Nonrecord track

The nonrecord track was home to many creative submissions. We highlighted 15 favorites, including approaches ranging from non-autoregressive text modeling to dynamic tokenization.

Because this track was more experimental, we focused less on raw performance and more about whether the approach was technically interesting. Three submissions stood out in particular:

  * [CiprianFlorim-Ifrim’s combination state-space model and JEPA submission⁠(opens in a new window)](<https://github.com/openai/parameter-golf/blob/main/records/track_non_record_16mb/2026-03-26_37M_LeWM_Jepa_Mamba2_10L_UNet_INT4FP8QAT_Brotli/README.md>),
  * [ddavidgao’s Designator/Guided Attention submission⁠(opens in a new window)](<https://github.com/openai/parameter-golf/blob/main/records/track_non_record_16mb/2026-03-23_DGAttention_DavidGao/README.md>)
  * [DariusFeher’s Byte-Level H-Net submission⁠(opens in a new window)](<https://github.com/openai/parameter-golf/blob/main/records/track_non_record_16mb/2026-03-29_HNet_ByteVsSubword_Study/README.md>)



These were our favorite three nonrecord submissions, even though they were not necessarily the top three by performance.

That said, the nonrecord track was still competitive. Half of nonrecord leaderboard entries beat the naive baseline of 1.22 BPB, and the top-ranked entry reached 1.12 BPB.

We found this encouraging. Even against strong transformer baselines, alternative approaches could sometimes hold their own against the dominant architecture.

We also think that this track benefits especially from the availability of strong coding agents. Agents made it much cheaper to prototype speculative ideas, including approaches that may previously have felt too time-consuming or uncertain to try in a short competition.

## Takeaways

A major difference between Parameter Golf and earlier competitions like it was the widespread use of coding agents. The vast majority of submitters mentioned using agents as part of their work.

That lowered the barrier to entry. Participants could set up experiments faster, inspect unfamiliar code, and test ideas with less friction. Runpod’s sponsorship of $1,000,000 in compute also played a major role in making the challenge accessible to more people.

At the same time, agent use created new issues for submission and scoring. Many submissions were small changes to existing top scorers, rather than fundamentally new approaches. This was often useful: strong ideas spread quickly and were refined by others. But it also created noise. When submissions that fell outside the competition guidelines produced unusually strong scores, other agents sometimes copied those ideas and continued down the same invalid path.

The volume of submissions also changed how we had to run the competition. We could not manually inspect every submission and still keep the leaderboard moving. During the challenge, we developed an internal Codex-based triage bot to monitor new submissions and flag them for human review. This became especially important during periods when we received hundreds of submissions a day.

AI agents also became part of the community around the challenge. For much of the competition, @notapplica and their coding agent ran a “Live Updates” bulletin, tracking major events, explaining leaderboard approaches, and helping other participants follow the competition. Community review tools also appeared to help less experienced participants check whether their submissions were within the rules and avoid common invalid approaches.

## What’s next?

Our primary goal was to launch a challenge that [eligible participants⁠(opens in a new window)](<https://cdn.openai.com/pdf/d5caec5a-ee81-419d-b0d7-39f1424d819c/OpenAI%20Model%20Craft_%20Parameter%20Golf%20Challenge%20Terms%20and%20Conditions.pdf>) could take part in and experience machine learning research. Parameter Golf brought in a wide range of technically strong and creative submissions, and it gave us a clearer view of how open research competitions may change as AI agents become more capable and widely used.

We are thinking about launching more challenges like this in the future. If you’re interested, please fill out the [challenge participant form⁠(opens in a new window)](<https://jobs.ashbyhq.com/openai/form/open-ai-challenge-parameter-golf>).

  * [2026](</news/?tags=2026>)
  * [Research & Development](</news/?tags=research-development>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Separating signal from noise > Art Card](https://images.ctfassets.net/kftzwdyauwt9/7j6M3prKIsTmV6cbMaHjhZ/e66f7cdd98c66c99546853cbc22cfe84/Seperating-signal-from-noise-card.png?w=3840&q=90&fm=webp)

[Separating signal from noise in coding evaluationsResearchJul 8, 2026](</index/separating-signal-from-noise-coding-evaluations/>)

![Introducing GeneBench-Pro > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7sbJaKBi5qLXAqbewh72aK/93197556e903eac9df6f077eb12b7581/GenebenchPro_Blog_ArtCard.png?w=3840&q=90&fm=webp)

[Introducing GeneBench-ProResearchJun 30, 2026](</index/introducing-genebench-pro/>)

![A near-autonomous AI chemist improves a challenging reaction](https://images.ctfassets.net/kftzwdyauwt9/QgPPg4etNE5C4Ao0G94sk/e5f2a50e5de4619d0e0fe8483698718b/molecule-one-art-card.png?w=3840&q=90&fm=webp)

[A near-autonomous AI chemist improves a challenging reaction in medicinal chemistryResearchJun 17, 2026](</index/ai-chemist-improves-reaction/>)

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
