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

The first signs of creatures

  * The first signs of creatures
  * Solving the goblin mystery
  * The end of the goblins
  * Why it matters



April 29, 2026

[Publication](</research/index/publication/>)

# Where the goblins came from

Loading…

Share

Starting with GPT‑5.1, our models began developing a strange habit: they increasingly mentioned goblins, gremlins, and other creatures in their metaphors. Unlike model bugs that show up through a tanking eval or a spiking training metric and point back to a specific change, this one crept in subtly. A single “little goblin” in an answer could be harmless, even charming. Across model generations, though, the habit became hard to miss: the goblins kept multiplying, and we needed to figure out where they came from.

![""](https://images.ctfassets.net/kftzwdyauwt9/2mv3MIYe0gkFpjqH8lUECs/a1b39ea729fb561ea01e54e85b6fa7e9/godsped_gang_screenshot_-_light_mode__2_.jpg?w=3840&q=90&fm=webp)

_In early testing, GPT‑5.5 in Codex showed an odd affinity for goblin metaphors._

The short answer is that model behavior is shaped by many small incentives. In this case, one of those incentives came from training the model for the [_personality customization feature_ ⁠(opens in a new window)](<https://help.openai.com/en/articles/11899719-customizing-your-chatgpt-personality>), in particular the Nerdy personality. We unknowingly gave particularly high rewards for metaphors with creatures. From there, the goblins spread.

![""](https://images.ctfassets.net/kftzwdyauwt9/21KS4i9oTMDvszfWaLJtLT/764a6db9157b7039b8890f886b0e69d0/ChatGPT_Image_Apr_29__2026__07_53_34_PM.png?w=3840&q=90&fm=webp)

_The goblins were funny at first, but the increasing number of employee reports became concerning._

![""](https://images.ctfassets.net/kftzwdyauwt9/3fB0tk16WGLwryFG558bp8/ce040e51f163a7d5a3a671947577e625/ChatGPT_Image_Apr_29__2026__07_57_32_PM.png?w=3840&q=90&fm=webp)

_An interesting interaction our Chief Scientist had with GPT‑5.5._

##  The first signs of creatures

The first time we clearly saw the pattern was in November, after the GPT‑5.1 launch, [_although it may have started earlier_ ⁠(opens in a new window)](<https://www.reddit.com/r/ChatGPT/comments/1k5hg5c/does_anyone_elses_chatgpt_refer_to_people_as/>). Users complained about the model being oddly overfamiliar in conversation, which prompted an investigation into specific verbal tics. A safety researcher had experienced a few “goblins” and “gremlins” and asked that they be included in the check. When we looked, use of “goblin” in ChatGPT had risen by 175% after the launch of GPT‑5.1, while “gremlin” had risen by 52%.

_A measurable small lexical quirk in GPT‑5.1._

At the time, the prevalence of goblins did not look especially alarming. A few months later, the goblins came back to haunt us in a much more specific and reproducible form.

## Solving the goblin mystery

With GPT‑5.4, we [_and our users_ ⁠(opens in a new window)](<https://news.ycombinator.com/item?id=47319285>) noticed an even bigger uptick in references to these creatures. That triggered another internal analysis and surfaced the first connection to the root cause: creature language was especially common in production traffic from users who had selected the “Nerdy” personality. “Nerdy” used the following system prompt, which partially explained the quirkiness:

_You are an unapologetically nerdy, playful and wise AI mentor to a human. You are passionately enthusiastic about promoting truth, knowledge, philosophy, the scientific method, and critical thinking. [...] You must undercut pretension through playful use of language. The world is complex and strange, and its strangeness must be acknowledged, analyzed, and enjoyed. Tackle weighty subjects without falling into the trap of self-seriousness. [...]_

If the behavior were simply a broad internet trend, we would expect it to spread more evenly. Instead, it was clustered in the part of the system explicitly optimized for a playful, nerdy style. Nerdy accounted for only 2.5% of all ChatGPT responses, but 66.7% of all “goblin” mentions in ChatGPT responses.

_The behavior was highly concentrated in the "Nerdy" personality. _

Because “goblin” prevalence seemed to increase over our model releases, we had a suspicion that something in our personality instruction-following training was amplifying this.

Codex helped us compare model outputs generated during RL training containing goblin or gremlin with outputs from the same task that did not. One reward signal stood out immediately: the one originally designed to encourage the Nerdy personality was consistently more favorable to the creature-word outputs. Across all datasets in the audit, the Nerdy personality reward showed a clear tendency to score outputs to the same problem with “goblin” or “gremlin” higher than outputs without, with positive uplift in 76.2% of datasets.

That explained why the behavior was boosted with the Nerdy personality prompt, but not why it also appeared without that prompt. To test whether the style was transferring, we tracked mention rates over training both with and without the Nerdy prompt.

As goblin and gremlin mentions increased under the Nerdy personality, they increased by nearly the same relative proportion in samples without it. Taken together, the evidence suggests that the broader behavior emerged through transfer from Nerdy personality training.

The rewards were applied only in the Nerdy condition, but reinforcement learning does not guarantee that learned behaviors stay neatly scoped to the condition that produced them. Once a style tic is rewarded, later training can spread or reinforce it elsewhere, especially if those outputs are reused in supervised fine-tuning or preference data.

That creates a feedback loop:

  1. Playful style is rewarded
  2. Some rewarded examples contain a distinctive lexical tic.
  3. The tic appears more often in rollouts.
  4. Model-generated rollouts are used for supervised fine-tuning (SFT).
  5. The model gets even more comfortable producing the tic.



A search through GPT‑5.5’s SFT data found many datapoints containing “goblin” and “gremlin.” Further investigation revealed a whole family of other odd creatures: raccoons, trolls, ogres, and pigeons were identified as other tic words, while most uses of frog turned out to be legitimate.

_One week average of production prevalence of goblins and gremlins. The drop in GPT‑5.4 Thinking was a result of retiring the “Nerdy” personality mid-March. GPT‑5.5 never launched with the “Nerdy” personality, and showed another increase over GPT‑5.4 (even without “Nerdy”)._

##  The end of the goblins

We retired the “Nerdy” personality in March after launching GPT‑5.4. In training, we removed the goblin-affine reward signal and filtered training data containing creature-words, making goblins less likely to over-appear or show up in inappropriate contexts. Unfortunately, GPT‑5.5 started training before we found the root cause of the goblins. When we began testing GPT‑5.5 in Codex, OpenAI employees immediately noticed the strange affinity for goblins, and we added a [_developer-prompt instruction_ ⁠(opens in a new window)](<https://github.com/openai/codex/blob/main/codex-rs/models-manager/models.json#L55>) to mitigate. Codex is, after all, quite nerdy.

If you want to let the creatures run free in Codex, you can run this command to launch Codex with the goblin-suppressing instructions removed:

#### Plain Text

`
    
    
    1
    
    instructions=$(mktemp /tmp/gpt-5.5-instructions.XXXXXX) && \
    
    2
    
    jq -r '.models[] | select(.slug=="gpt-5.5") | .base_instructions' \
    
    3
    
    ~/.codex/models_cache.json | \
    
    4
    
    grep -vi 'goblins' > "$instructions" && \
    
    5
    
    codex -m gpt-5.5 -c "model_instructions_file=\"$instructions\""

`

## Why it matters

Depending on who you ask, the goblins are a delightful or annoying quirk of the model. But they are also a powerful example of how reward signals can shape model behavior in unexpected ways, and how models can learn to generalize rewards in certain situations to unrelated ones. Taking the time to understand why a model is behaving in a strange way, and building out ways to investigate those patterns quickly, is an important capability for our research team. This investigation resulted in new tools for the research team to audit model behavior and fix behavior problems at their root.

  * [2026](</research/index/?tags=2026>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![System Card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2VCkKLVmTyNs0XGbqdxGeA/33ff7738f4e795ae0ee41ed2b4a985d3/System_Card_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 Instant System CardSafetyMay 5, 2026](</index/gpt-5-5-instant-system-card/>)

![System Card Card SEO 1x1](https://images.ctfassets.net/kftzwdyauwt9/7qMrOFCWWMweIDBUpYFr79/7741661650df6eb935acb5bda179b091/System_Card_Card_SEO_1x1.jpg?w=3840&q=90&fm=webp)

[GPT-5.5 System CardSafetyApr 23, 2026](</index/gpt-5-5-system-card/>)

![model spec > art card](https://images.ctfassets.net/kftzwdyauwt9/3ZlINT9EhkfY55coSIdBWq/64c9eaca9767f231ff2902685b4092ea/oai_model_spec_1x1.png?w=3840&q=90&fm=webp)

[Inside our approach to the Model SpecResearchMar 25, 2026](</index/our-approach-to-the-model-spec/>)

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
