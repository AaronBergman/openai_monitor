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

# Download data and methodology

This section is a place to download data and understand the methodology behind what we have published.

[Download CSV files of the data(opens in a new window)](<https://cdn.openai.com/signals/data-download-csv.zip>)[Data dictionary](<https://cdn.openai.com/signals/data-dictionary.pdf>)

We welcome you to use Signals data for your own research. You can download the relevant data via the button “Download CSV files of the data” and learn more about our methodology below.  
  
All Signals data is licensed for use under the [Creative Commons CC BY 4.0 license⁠(opens in a new window)](<https://creativecommons.org/licenses/by/4.0/legalcode.txt>), which allows you to use, share, and adapt the data but requires attribution or citation. If you download and use this data, please cite our work with the following suggested citation: Aaron Chatterji, Thomas Cunningham, David J. Deming, Zoe Hitzig, Christopher Ong, Carl Yan Shan, and Kevin Wadman, “How People Use ChatGPT,” NBER Working Paper 34255 (2025), [https://doi.org/10.3386/w34255⁠(opens in a new window)](<https://doi.org/10.3386/w34255>).

## Methodology

This data is designed to measure how ChatGPT is used globally while maintaining strong privacy protections. Our dataset includes one hundred thousand statistics based on the classifications of consumer ChatGPT messages each month from July 2024 to December 2025 from accounts with an associated declared age of at least 18. It does not include any statistics based on the classifications of enterprise messages and, as a result, these data likely understate business use. In the visualizations presented, all numbers are global unless specified otherwise. 

Researchers did not view raw user message text. Analyses involving message content relied on automated outputs from classifiers applied to de-identified data that was previously scrubbed for personally identifying information (PII). All sharing of Signals data is done in accordance with [_OpenAI’s Privacy Policy_ ⁠](<https://openai.com/policies/row-privacy-policy/>). 

The remainder of this appendix describes our privacy pipeline, sampling approach, and classifier design, as well as any specific information for particular data visualizations.

## Privacy and data-use methods

To study how people use ChatGPT while preserving privacy, we created message-level datasets in which no researcher reads message contents. Instead, messages are processed through a privacy-preserving pipeline: message text is first scrubbed to remove personally identifiable information using an internal LLM-based tool, disassociated from the user account, and then classified with LLM-based classifiers that map messages into a set of pre-defined labels. The most granular label set used in the message-level analyses is based on the O*NET Intermediate Work Activities taxonomy. 

The dataset currently is based on a random draw of 100,000 conversations from each month in our sample comprising 1.8 million conversations overall, subject to pre-specified restrictions. In contrast to the sampling methods in our recent paper “How People Use ChatGPT”, we uniformly sample over messages, rather than randomly selecting a message within a uniform sample of conversations, resulting in some variations in reported shares. The sample includes messages from July 2024 through December 2025, excludes users who opted out of sharing messages for model training, excludes users who self-report an age under 18, and removes content from deleted conversations as well as from users whose accounts were deactivated or banned. Because the sample is drawn from an upstream table that is itself sampled with a sampling rate that varies over time, we adjust sampling weights so that the analyzed sample maintains a consistent relationship to aggregate message volumes.

Classifications used in this paper are the same as those developed by the authors in _How People Use ChatGPT_([Chatterji et al., 2025⁠(opens in a new window)](<https://www.nber.org/system/files/working_papers/w34255/w34255.pdf>)). To provide context about each message in our sample, we provide classifiers with up to the prior 10 messages in a conversation as context. To limit variability associated with very long context windows, each message is truncated to a maximum of 5,000 characters ([_Liu et al., 2023_ ⁠(opens in a new window)](<https://arxiv.org/abs/2307.03172>)). Classifications are generated with the gpt-5-mini model. These design choices are intended to support consistent labeling at scale while maintaining privacy protections through PII scrubbing, controlled labels, and restricted access to underlying text.

We evaluated classifier performance by comparing model-generated labels to human-judged classifications on a sample of conversations from the public WildChat dataset ([_Zhao et al., 2024_ ⁠(opens in a new window)](<https://arxiv.org/abs/2405.01470>)), which consists of conversations with a third-party chatbot that users affirmatively consented to share for research. Our overall approach follows emerging best practice in computational social science for studying chatbot usage without direct inspection of private transcripts, and aligns with recent work that emphasizes automated, privacy-preserving labeling of conversational data (e.g., [_Phang et al., 2025_ ⁠(opens in a new window)](<https://arxiv.org/abs/2504.03888>); [_Eloundou et al., 2025_ ⁠(opens in a new window)](<https://arxiv.org/abs/2410.19803>); [_Handa et al., 2025_ ⁠(opens in a new window)](<https://arxiv.org/abs/2503.04761>); [_Tomlinson et al., 2025_ ⁠(opens in a new window)](<https://arxiv.org/pdf/2507.07935?>)).

Signals also employs differential privacy to add an additional layer of protection. Differential privacy introduces carefully calibrated statistical noise into published aggregates so that the presence or absence of any single individual (or small group) does not meaningfully change the results. In plain terms: even if someone tried to use the published data to infer information about the content of any particular message, the mathematics of differential privacy is designed to make that inference unreliable. This helps ensure that the public reporting remains useful while meaningfully constraining re-identification risk.

## Methodology for typically feminine and masculine names 

Our analysis of inferred gender is based on a global random sample of ChatGPT users’ first names based on commonly available datasets of name-gender associations. We recognize that gender cannot always be correctly inferred from a first name and so this is simply a best approximation since we do not collect data on users’ gender. 

## Methodology for geography

Our analysis of users’ locations for the maps included in Signals is based on coarse IP geolocation metadata attached to each incoming request. This method provides only approximate location and may be inaccurate for VPNs, proxies, or mobile networks.

### Stay updated

If you're interested in learning more about OpenAI's Economic Research work and future updates to this dataset, please sign up below.

First name *

Last name *

Email *

Sign up

![Abstract blue gradient background with soft green and purple hues blending from the corners, forming a smooth, radiant light effect.](https://images.ctfassets.net/kftzwdyauwt9/1kAozxhcP7BMPmhVC5bXkg/ccbbe3dd6779a6cb0d72c3745d23e92f/newsletter.png?w=3840&q=90&fm=webp)

### Discover more

![Signals > Layout > Group > Footer > Cards > Data lab > Media > Asset](https://images.ctfassets.net/kftzwdyauwt9/5d5uaKtcOHDQMTBWrQQz5y/d49a1270ad7911ffe170a63cf30f5021/data_lab.png?w=3840&q=90&fm=webp)

### Signals consumer data

Browse the data to see global consumer ChatGPT adoption patterns, geographic distribution, and work and non-work use.

[Learn more](</signals/data/>)

![Signals > Layout > Group > Footer > Cards > Signals homepage > Media > Asset](https://images.ctfassets.net/kftzwdyauwt9/6wgp9fWFmxEdTyh3cp6LZ3/00b8d5789e1c4d68b8bf1b71b2e3cf34/signals.png?w=3840&q=90&fm=webp)

### OpenAI Signals

A hub for data, research, analysis, and stories from the OpenAI Economic Research and Global Affairs Teams.

[Learn more](</signals/>)

![Signals > Layout > Group > Footer > Cards > Research and analysis > Media > Asset](https://images.ctfassets.net/kftzwdyauwt9/1xbgsNvA9Nhmm22lHNOjZZ/7b7bdc61e147c49d4e440d471ff7f12f/Research_and_analysis.png?w=3840&q=90&fm=webp)

### Research and analysis

Research and analysis on how AI is being adopted and its impact on the economy and society.

[Learn more](</signals/research/>)

![Signals > Layout > Group > Footer > Cards > B2B Signals > Media > Asset](https://images.ctfassets.net/kftzwdyauwt9/dgxKw1vos15b7gFpzM3h2/0d7a2bcf630478821773d64afb29a33b/b2b.png?w=3840&q=90&fm=webp)

### Signals B2B data

Learn how AI is accelerating enterprise advantage through deeper integration, agentic workflows, and scaled adoption.

[Learn more](</signals/b2b/>)

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
