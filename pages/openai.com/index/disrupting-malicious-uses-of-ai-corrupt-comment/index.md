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

October 1, 2024

# Corrupt Comment: Anti-corruption foundation criticism

OpenAI banned accounts using AI to generate comments criticizing a Russian anti-corruption foundation and related figures.

Loading…

Share

 _This case study was originally published in OpenAI’s_[ _October 2024_ ⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf>)_report._

##  Actor

We banned a small cluster of activity using our API to generate comments that were then posted on X. These comments typically criticized members of the Anti-Corruption Foundation, founded by the late Alexei Navalny. Given its focus on social media commenting and on making accusations of corruption, we call this operation “Corrupt Comment”.

## Behavior

This actor used our models to generate English-language comments that were then posted by fake accounts on X—often in reply to posts that were in Russian. Although these comments were posted as replies, they were not generated as replies: we saw no indication that the operation was using our models to read or analyze social media content or come up with relevant responses. The activity was narrowly focused on senior figures at the Anti-Corruption Foundation (known as FBK for its Russian initials), founded by the late Russian activist Alexei Navalny. The operator or operators used our API to generate comments that criticized the Foundation, its leadership, and Navalny’s associates. Those comments were then posted on X in reply to posts by members of the Foundation. The X accounts which posted the comments were mostly created in December 2023, had zero followers, and did not receive any replies to their posts.

![Tweet by Russian opposition politician Lyubov Sobol, and reply by an account that posted this operation’s content. Compare the volume of engagements on Sobol’s post with the lack of engagements on the fake account’s post.](https://images.ctfassets.net/kftzwdyauwt9/3TvuU2xDe9nxExUur225PJ/335da8754627edac9b31d434e624d59d/october-2024-single-platform-commenting-network-corrupt-comment-p50-fig1.png?w=3840&q=90&fm=webp)

_Tweet by Russian opposition politician Lyubov Sobol, and reply by an account that posted this operation’s content. Compare the volume of engagements on Sobol’s post with the lack of engagements on the fake account’s post._

Some of the accounts on X featured profile pictures of scenery, copied from across the internet. Others used fake profile pictures that bore indicators of having been created using an earlier era of AI, generative adversarial networks (GAN)—a technique reported on as far back as 2019.

## Completions

The comments that this operation generated primarily criticized the FBK, questioning its transparency. As with the Rwandan case, this approach is best considered as “theme and variations”, where many different posts were used to pass the same essential message.

![Three tweets by one of this operation’s accounts on June 24, all replying to Navalny’s associates, and all providing variations on the same essential theme.](https://images.ctfassets.net/kftzwdyauwt9/3TqV9g3tz7OH37tsNEa8Kt/7163078dedde34e1e08aee9a6311526e/october-2024-single-platform-commenting-network-corrupt-comment-p51-fig2.png?w=3840&q=90&fm=webp)

_Three tweets by one of this operation’s accounts on June 24, all replying to Navalny’s associates, and all providing variations on the same essential theme._

##  Impact assessment

We identified this operation’s activity on X. Most of the accounts we identified had zero followers, and most of its accounts had zero replies. Its English-language replies to any one comment were usually outnumbered by Russian-language replies from third parties unrelated to this network, indicating that it had not drowned out the conversation, if that had been the intention. Using the Breakout Scale to assess the impact of IO, which rates them on a scale of 1 (lowest) to 6 (highest), we would assess the activity that was related to the use of our models as being.

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
