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

# Priority Processing for API Customers

Priority processing offers reliable, high-speed performance with the flexibility to pay-as-you-go.

By choosing Priority processing, you can unlock:

  * **Predictably low latency:** Priority processing generates tokens faster and at a more consistent speed than the Standard processing service, even during peak demand.
  * **Easy-to-use flexibility:** Like Standard processing, Priority processing can be accessed on a flexible, pay-as-you-go basis instead of requiring advance provisioning.



| Price per 1M input tokens| Price per 1M input tokens (cached)| Price per 1M output tokens| Uptime SLA3| Latency SLA3  
---|---|---|---|---|---  
GPT-5.6 Solexcludes long context1| $10.00| $1.00| $60.00| 99.9%| 99% > 50 tokens per second2  
GPT-5.6 Terraexcludes long context1| $5.00| $0.50| $30.00| 99.9%| 99% > 70 tokens per second2  
GPT-5.6 Lunaexcludes long context1| $2.00| $0.20| $12.00| 99.9%| 99% > 100 tokens per second2  
GPT-5.5excludes long context1| $12.50| $1.250| $75.00| 99.9%| 99% > 50 tokens per second2  
GPT-5.4 miniexcludes long context1| $1.50| $0.150| $9.00| 99.9%| 99% > 100 tokens per second2  
GPT-5.4excludes long context1| $5.00| $0.500| $30.00| 99.9%| 99% > 50 tokens per second2  
GPT-5.2| $3.50| $0.350| $28.00| 99.9%| 99% > 50 tokens per second2  
GPT-5.1| $2.50| $0.250| $20.00| 99.9%| 99% > 50 tokens per second2  
GPT-5| $2.50| $0.250| $20.00| 99.9%| 99% > 50 tokens per second2  
GPT-5 mini| $0.45| $0.045| $3.60| 99.9%| 99% > 80 tokens per second2  
GPT-5.1 codex| $2.50| $0.250| $20.00| 99.9%| 99% > 50 tokens per second2  
GPT-5 codex| $2.50| $0.250| $20.00| 99.9%| 99% > 50 tokens per second2  
GPT-4.1| $3.50| $0.875| $14.00| 99.9%| 99% > 80 tokens per second2  
GPT-4.1 mini| $0.70| $0.175| $2.80| 99.9%| 99% > 90 tokens per second2  
GPT-4.1 nano| $0.20| $0.050| $0.80| 99.9%| 99% > 100 tokens per second2  
GPT-4ogpt-4o-2024-11-20gpt-4o-2024-08-06| $4.25| $2.125| $17.00| 99.9%| 99% > 80 tokens per second2  
gpt-4o-2024-05-13| $8.75| —| $26.25| 99.9%| 99% > 80 tokens per second2  
GPT-4o mini| $0.25| $0.125| $1.00| 99.9%| 99% > 90 tokens per second2  
o3| $3.50| $0.875| $14.00| 99.9%| 99% > 80 tokens per second2  
o4-mini| $2.00| $0.500| $8.00| 99.9%| 99% > 90 tokens per second2  
  
1Requests estimated at >272K prompt tokens

2Calculated as p50 request latency on a per 5 minute basis. For customers with existing enterprise agreements that have latency SLAs calculated as p50 request latency on a per minute basis, the prior SLAs are also still applicable.

3This is applicable to Enterprise customers only

## How it works

Customers can direct traffic to Priority processing on a per request basis using the existing service_tier parameter, with the option **service_tier = “priority”.**

Tokens served by Priority processing will be billed on a per-token basis, priced at a premium relative to Standard processing rates. 

In addition to being configured at the request level, you can also default a project to Priority in Project settings → Default Service Tier: Priority. You can still override per request.

## Limitations

  * Priority processing rate limits are shared with other service tiers. 
  * In rare cases, rapid increases to your Priority processing Tokens per Minute can lead to hitting ramp rate limits. If you exceed the ramp rate limit, then additional traffic may be sent to Standard processing instead.



#### Pricing

#### Models

#### Rate limits

#### Reliability

#### Policies

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

### (For Enterprise customers) How does this interact with Scale Tier?

Scale Tier will remain separate from Priority processing.

Requests sent to Priority processing will be billed separately and will not count against your purchased Scale Tier TPM bundles.

### (For Enterprise customers) Can I automatically send my Scale Tier spill-over traffic to Priority processing?

No. Traffic sent to Scale Tier will not automatically spill over to Priority processing.

### (For Enterprise customers) Is my annual commitment tied to a specific processing mode?

No. All processing modes count against your annual enterprise spend commitment.

### Do I still get a discount on Cached input tokens?

Yes! For a given model, Cached Inputs receive the same 50%, 75%, or 90% discount as they do in Standard processing.

### How do I view my Priority processing usage and spend?

To view tokens processed by Priority processing, go to the Usage dashboard, select Chat Completions or Responses, and Group by Service Tier.

To view Priority processing cost, go to the Usage dashboard, and select Group by Line Item.

### Is Priority processing available for long context, fine-tuned models, embeddings, etc.?

Not at this time. We will evaluate in the future whether to offer Priority processing on additional products beyond our latest models.

### How do other modalities work with Priority processing?

Priority processing supports the same multimodal capabilities available on Standard. In particular, images can be used as inputs to Priority processing and are processed with the same fast latency.

### Will future models be supported?

Yes. We plan to offer Priority processing on new GPT models. We don’t guarantee that every model will be supported.

### What are the rate limits?

Priority processing consumption is treated the same as standard API traffic for rate limits.

### What are the ramp rate limits?

Priority processing has ramp rate limits to ensure consistently high performance for all customers, while still providing flexible, on-demand pricing. If (a) Priority processing performance is degraded AND (b) a customer’s traffic is ramping too quickly, then some Priority requests may be downgraded to Standard processing instead.

The current Priority processing ramp rate limit is defined as processing at least 1M TPM, and increasing traffic by >50% Tokens Per Minute in less than 15 minutes.

Requests processed by Standard service tier will be billed at standard rates, and are not eligible for Priority processing Service Level Objectives.

Requests processed by Standard service tier will include service_tier=”Default” in the response.

  
**Best practices for staying within your ramp rate limit**

  1. Gradually increase traffic when changing models. For example, if your application is transitioning from a previous snapshot to a new one, use a feature flag to transition traffic over the course of a few hours rather than all at once.

  2. Avoid running large data processing or asynchronous jobs on Priority processing. These jobs can ramp traffic very quickly, and often do not need the improved performance of Priority processing.

  3. If you routinely encounter ramp rate limits, consider purchasing Scale Tier capacity instead or in addition.




### Are ramp rate limits shared across my projects or organizations?

Yes. All of your traffic contributes to the same ramp rate limit.

### (For Enterprise customers) What happens if it’s not meeting the latency target?

For Enterprise customers, please reach out to your AD with any questions or concerns. 

Priority processing SLAs will be treated the same as Scale Tier SLAs; service credits will be offered should we fail to meet those SLAs for customers on enterprise agreements during a given time window.

### Is Priority processing compatible with Data Residency?

Yes

### Is Priority processing compatible with ZDR and the BAA?

Yes
