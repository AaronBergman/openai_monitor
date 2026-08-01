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

February 1, 2025

# Operation “Peer Review”: AI-assisted surveillance planning

OpenAI banned likely China-origin accounts using AI to draft surveillance-tool pitches, analyze documents, and debug code.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _February 2025_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf>)_report._

##  Summary

## Actor

We banned a cluster of ChatGPT accounts that, based on behavioral patterns and other findings, likely originated in China. They were using our models to assist with analyzing documents, generating sales pitches and descriptions of tools for monitoring social media activity powered by non-OpenAI models, editing and debugging code for those tools, and researching political actors and topics. Based on this network’s behavior in promoting and reviewing surveillance tooling, we have dubbed it “Peer Review.”

## Behavior

This network consisted of ChatGPT accounts that operated in a time pattern consistent with mainland Chinese business hours, prompted our models in Chinese, and used our tools with a volume and variety consistent with manual prompting, rather than automation. In one instance, we believe the same account may have been used by multiple operators.

Within the cluster, the operators performed a number of primary tasks. One was to use the model as a basic research tool, in a way similar to which earlier generations would have used search engines. This included, for example, searching for publicly available information about think tanks in the United States, and politicians and government officials in countries including Australia, Cambodia, and the United States.

Another workstream consisted of using our models to read, translate, and analyze screenshots of English-language documents. Some of these images were announcements of Uyghur rights protests in a range of Western cities, and were potentially copied from social media. Others appeared to concern diplomatic and government topics in the Indo-Pacific region. There is insufficient evidence to determine whether these documents were authentic, or to show how the operators obtained them.

A third workstream consisted of using ChatGPT to generate short- to medium-length comments about Chinese dissident organizations, notably the Falun Gong, and about US policies and politics. Occasionally, the actors asked the model to assume the persona of an English-speaker called “Thompson.” We were not able to identify these comments posted online.

Fourth, the operators used our model to edit and debug code and generate promotional materials for what appeared to be an AI-powered social media listening tool. We did not see evidence of this tool being run on our models. The details of this activity are described below.

## Completions

One of this operation’s main activities was generating detailed descriptions, consistent with sales pitches, for what they described as the “Qianyue Overseas Public Opinion AI Assistant” (“千阅境外舆情AI助手”). According to the descriptions, which we cannot independently verify, this was designed to ingest and analyze posts and comments from platforms such as X, Facebook, YouTube, Instagram, Telegram, and Reddit.

Again according to the descriptions, one purpose of this tooling was to identify social media conversations related to Chinese political and social topics, especially any online calls to attend demonstrations about human rights in China, and to feed the resulting insights to Chinese authorities. The operators used our models to proofread claims that their insights had been sent to Chinese embassies abroad, and to intelligence agents monitoring protests in countries including the United States, Germany, and the United Kingdom.

A separate account in the same cluster also referenced the social-media monitoring tool, but in the context of editing and debugging code. This operator used ChatGPT to debug and modify code that appeared designed to run the social-media monitoring tool. This code most frequently named Meta’s llama3.1:8b deployed via Ollama as the driver of the tool’s analysis and generation. We do not have visibility into whether, how, or where this code may have been deployed.

The same account debugged code apparently intended for malware analysis, and referred to other models like Qwen (built by Alibaba Cloud) and an unspecified model by DeepSeek. It also used our models to generate what appeared to be an end-of-year performance review, which claimed that the actor had generated phishing emails on behalf of unspecified clients in China. We did not see evidence or claims that this email-related activity had been powered by AI.

## Impact

Very little of this operation’s activity appeared to be designed for publication on social media or other distribution platforms. A few generations did resemble social media comments, but we were not able to identify them being posted online. Significantly more content appeared to be for capability development, such as code debugging, or for internal purposes, such as image analysis and the development of promotional materials.

Assessing the impact of this activity would require inputs from multiple stakeholders, including operators of any open-source models who can shed a light on this activity.

## Author

OpenAI

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
