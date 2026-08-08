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

February 13, 2026

[Engineering](</news/engineering/>)

# Beyond rate limits: scaling access to Codex and Sora

By Jonah Cohen, Member of the Technical Staff

Loading…

Share

Why existing access models fell short

  * Why existing access models fell short
  * Access as a waterfall, not a gate
  * Why we built this in‑house
    * Real‑time correctness
    * Reconcilability and trust
  * Building a high‑scale usage and balance system
  * A provably correct billing system
  * Architecture in service of momentum



  * Why existing access models fell short
  * Access as a waterfall, not a gate
  * Why we built this in‑house
    * Real‑time correctness
    * Reconcilability and trust
  * Building a high‑scale usage and balance system
  * A provably correct billing system
  * Architecture in service of momentum



In the past year, both Codex and Sora have seen rapid adoption, with usage quickly pushing beyond what we originally expected. We’ve seen a consistent pattern: users dive in, find real value, and then run into rate limits.

Rate limits can help smooth demand and ensure fair access; however, when users are getting value, hitting a hard stop can be frustrating. We wanted a way for users to keep going, while protecting system performance and user trust in our approach.

To solve this, we built a real‑time access engine that counts usage. One of the layers in that engine is the ability to purchase credits. When users exceed their rate limits, credits let them keep using our products by spending down their credit balance.

Underneath this is a complex system that fuses limits, real‑time usage tracking, and credit balances in a single access model. This post covers why scaling Codex and Sora required rethinking access control, how a provably correct, real-time system blends rate limits and credits per request, and how that foundation now unlocks additional access for both products.

## Why existing access models fell short

Zooming out, traditional access models tend to force a choice:

  * **Rate limits** can be helpful at first, but leave users with a bad experience when they run out: “come back later”
  * **Usage‑based billing** is flexible, but leaves users paying from the first token—not ideal for supporting early exploration



For Codex and Sora, neither was sufficient on its own. If we simply raised rate limits, we’d lose important demand-smoothing and fairness controls and run out of capacity to serve everyone. If we relied entirely on asynchronous usage billing, we’d introduce lag, overages, or reconciliation issues—exactly the kinds of problems users notice when they’re most engaged.

What we needed instead was a single hybrid system combining real-time limits with pay-as-you-go access:

![Dashboard UI with two buttons labeled “Rate-limits” and “Credits,” and a card below titled “Rate-Limit with Credit Fallback.”](https://images.ctfassets.net/kftzwdyauwt9/6WkV1NDTZ0y1UNjgX3YNdL/288077727d4c63f100d5f5c2f0d31e5c/FinEng_Desktop_Lightmode_Chart-1.svg?w=3840&q=90)

This system had to:

  * Enforce rate limits _until_ they’re reached
  * Seamlessly transition to credits _within the same request_
  * Make that decision in real time
  * Be rigorously accurate and auditable when tracking credit consumption



## Access as a waterfall, not a gate

One of the key conceptual shifts we made was modeling access as a **decision waterfall**. Instead of asking “is this allowed?”, we ask “how much is allowed, and from where?” When counting usage, the system goes through the following sequence:

![Decision tree for evaluating access to our features ](https://images.ctfassets.net/kftzwdyauwt9/5dB7am3vuVbMgNAQG3d9HT/c9a516f529654ed9e871e9ee88db9226/FinEng_Desktop_Lightmode_Chart-2.svg?w=3840&q=90)

This model reflects how users actually experience the product. Rate limits, free tiers, credits, promotions, and enterprise entitlements are all just layers in the same decision stack. From a user’s perspective, they don’t “switch systems”—they just keep using Codex and Sora. That’s why credits feel invisible: they’re just another element in the waterfall.

## Why we built this in‑house

We evaluated third‑party usage billing and metering platforms to handle credit consumption. They’re well‑suited for invoicing and reporting, but didn’t meet two critical requirements:

### Real‑time correctness

When a user hits a limit and has credits available, the system must know _immediately_. Best‑effort or delayed counting shows up as surprise blocks, inconsistent balances, and incorrect charges. For interactive products like Codex and Sora, those failures become visible and frustrating.

### Reconcilability and trust

We also needed to offer transparency into every outcome:

  * Why a request was allowed or blocked
  * How much usage it consumed
  * Which limits or balances were applied



This capability needed to be tightly integrated into our decision waterfall rather than solved in isolation in a separate usage billing platform that only saw one piece of what was happening. To let users access our products without compromising trust, we needed full control over correctness, timing, and observability. That pushed us toward an in‑house solution.

## Building a high‑scale usage and balance system

To power this, we built a distributed usage and balance system designed specifically for synchronous access decisions.

At a high level, the system:

  * Tracks per‑user, per‑feature usage
  * Maintains rate‑limit windows
  * Maintains real‑time credit balances
  * Debits balances idempotently through a streaming async processor



Every request passes through a single evaluation path that makes a real‑time decision about how much usage is allowed by synchronously consuming from rate limits and, if needed, verifying sufficient credits; it then returns one definitive outcome while settling any credit debits asynchronously. This ensures consistent behavior across products and eliminates duplicated logic across teams.

![Access system: Combining real-time rate-limits and asynchronous credit & balance tracking.](https://images.ctfassets.net/kftzwdyauwt9/21kMN9OcVwySOjtyT4VgxQ/137c60985fd463a7507217c9e05d1418/FinEng_Desktop_Lightmode_Chart-3.svg?w=3840&q=90)

## A provably correct billing system

One of the key design principles of this system is that we must be able to _prove_ that our billing is correct. This reflects the roots of our credit support, which originated with enterprise customers. In the above system diagram, we have three separate datasets that all tie together:

  * **Product usage events:** What the user actually did
  * **Monetization events:** What we charge the user for their usage
  * **Balance updates:** How much we adjusted the user’s credit balance and why



These datasets aren’t a casual by-product; they actually drive the system, with each dataset triggering the next. Separating what occurred, any associated charges, and what we debited lets us independently audit, replay, and reconcile every layer. This is an intentional trade-off where we are prioritizing provable correctness, at the cost of credit balance updates being slightly delayed. How we accomplished this:

  * Product usage events are published for all user activity, whether it drives credit consumption or not. This provides an audit trail for user activity and allows us to explain why we charged, or didn’t charge, credits.
  * Every event carries a stable idempotency key, so retries, replays, or worker restarts can never double‑debit a balance, which prevents double‑charging. This also lets us run a batch reconciliation to verify our work offline.
  * We do asynchronous (but still near-real-time) balance updates instead of synchronous updates to create an audit trail. We tolerate a small delay in updating the user’s balance so that we can prove that the system is functioning and assure our users that we are not misbilling them. When that brief delay causes us to overshoot a user’s credit balance, we automatically refund it; we choose provable correctness and user trust over strict enforcement.
  * We decrease the _Credit Balance_ and insert a _Balance Update_ record in a single atomic database transaction. Balance updates are serialized per account, so concurrent requests can never race to spend the same credits. The _Balance Update_ record contains both the debit amount as well as attribution back to the monetization event that triggered the update; wrapping this in a single database transaction guarantees we have an audit trail for every adjustment to the credit balance.



All of this rigor supports one objective: to make access simple and safe. When people are creating or coding, they shouldn’t have to wonder whether a request will go through, if they’ll be overcharged, or whether their balance is accurate. By making usage, billing, and balances provably correct, we give users a system that doesn’t distract from their experience. That’s what lets us replace hard stops with continuous access—and it’s what makes credits usable in the middle of real work, not just on an invoice.

## Architecture in service of momentum

The guiding principle behind our approach is protecting user momentum. Every architectural decision maps back to a user-facing outcome: real-time balances prevent unnecessary interruptions, atomic consumption prevents double-charging, and unified access logic ensures predictable behavior. The result is that people can work longer, explore more deeply, and take projects further without facing hard stops or premature plan changes.

When users are engaged, the system should help them continue, not get in the way. Limits and credits disappear into the background.

Building that experience required rethinking access, usage, and billing as a single system and building infrastructure that treats correctness as a first‑class product feature. The same foundation can extend to more products over time; Codex and Sora are just the beginning.

  * [Codex](</news/?tags=codex>)
  * [Sora](</news/?tags=sora>)
  * [2026](</news/?tags=2026>)



## Author

Jonah Cohen

## Acknowledgements

Special thanks to the entire FinEng team that built credits.

## Keep reading

[View all](</news/>)

![Continuous voice interaction with GPT Live - art card](https://images.ctfassets.net/kftzwdyauwt9/3PyfDzfjOozLbJnaZIkRLD/6aef080bb4e7d6a6b8a6dc23436848db/gpt-live-art-card.png?w=3840&q=90&fm=webp)

[Continuous voice interaction with GPT LiveEngineeringAug 3, 2026](</index/continuous-voice-interaction-with-gpt-live/>)

![GPT-5.6 efficiency article — art card](https://images.ctfassets.net/kftzwdyauwt9/5ExPWhZDZXbZgTHE7aeE5d/0526071f749a3b44adff3c45a12322b7/How_GPT-5.6_fuses_frontier_intelligence_with_frontier_efficiency_ART_CARD__1_.png?w=3840&q=90&fm=webp)

[How GPT-5.6 fuses frontier intelligence with frontier efficiencyEngineeringJul 29, 2026](</index/gpt-5-6-frontier-intelligence-efficiency/>)

![Rockset > Art Card](https://images.ctfassets.net/kftzwdyauwt9/7qv6OiVDfumZUnibH5VTOU/d2d818ac6de1f7cb93dce7a343e456dc/Rockset-Art-Card.png?w=3840&q=90&fm=webp)

[Core dump epidemiology: fixing an 18-year-old bugEngineeringJun 30, 2026](</index/core-dump-epidemiology-data-infrastructure-bug/>)

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
