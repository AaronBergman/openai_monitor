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

August 25, 2026

[Global Affairs](</news/global-affairs/>)

# Disrupting a new covert influence campaign from Russia

Loading…

Share

Actor

  * Actor
  * AI activity
  * Non-AI activity
  * Impact



  * Actor
  * AI activity
  * Non-AI activity
  * Impact



Our mission is to ensure that artificial general intelligence benefits all of humanity. We advance this mission by deploying our innovations to build AI tools that help people solve hard problems. This includes building tools that enable us to detect, investigate, disrupt and expose covert influence operations (IO): deceptive attempts to manipulate public opinion or influence political outcomes without revealing the true identity or intentions of the actors behind them.

We recently banned a cluster of ChatGPT accounts originating in Russia that were being used to promote the International Burke Institute (IBI), a self-described “expert community” based in Israel. What began as an investigation into AI-generated social media posts led us to a much broader influence operation, built around a website containing copied and misattributed academic work, a “sovereignty” index that cast Russia in a favourable light, and efforts to disguise the operators’ Russian origins. Although the campaign appears to have reached relatively small audiences, its elaborate construction distinguishes it from other [Russia-linked⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/threat-intel-report-may-2024.pdf>) [influence⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf>) [operations⁠(opens in a new window)](<https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf>) we have [disrupted⁠(opens in a new window)](<https://cdn.openai.com/pdf/df438d70-e3fe-4a6c-a403-ff632def8f79/disrupting-malicious-uses-of-ai.pdf>) since the start of the war in Ukraine. This report explains how the operation worked, where ChatGPT fit into it, and what we did to disrupt it.

## Actor

We banned a cluster of ChatGPT accounts that very likely originated in Russia. The operators prompted in Russian to generate social media comments that were posted on Substack, Telegram, X, Facebook and LinkedIn. Most of the comments they generated were in English, and the operators instructed ChatGPT to hide any linguistic clues that they were Russian. As we do not allow access to our models from Russia, they used VPNs to access our platform.

Much of the generated content was to promote a self-described “expert community” called the International Burke Institute (IBI). The IBI brand was associated with a website which was registered in February 2025. This site claimed that the Institute was based in Israel. Articles published on the site were not generated from our models. Many were copied from real academic writings, sometimes with false attribution; some appear to have been drafted by a Slavic speaker and machine translated. As an example, the screenshot below from the IBI website uses an unnatural phrase that is most readily explained as a literal machine translation from a Slavic language.

![Screenshot from an IBI website article about Germany using the phrase the Svetofor coalition.](https://images.ctfassets.net/kftzwdyauwt9/1FycKER90DjXKmUHMkQVrQ/ed1d728ad1f0edc26d68ef4d6e286265/covert-influence-campaign-russia-figure-1.png?w=3840&q=90&fm=webp)

_Screenshot from an article about Germany on the IBI website. The phrase “the Svetofor coalition” is meant to refer to Germany’s coalition of socialists, liberals and greens, known from their party colors of red, yellow and green as the “traffic-light coalition” or, in German, “Ampelkoalition”. The word “svetofor” (светофор) means “traffic light” in a number of Slavic languages, including Russian, but is exceptionally unlikely to occur to an English or German speaker to describe the coalition: it was likely machine translated from a Slavic original._

This is, to the best of our knowledge, a new and previously unreported covert influence campaign. Its most notable feature is its creation of the “sovereignty index” promoted by the ostensible “think tank” to praise Russia and denigrate Western countries. This is the first time we have disrupted an influence operation tied to Russia that went to such elaborate lengths.

## AI activity

The operation’s main use of ChatGPT was to generate social media posts that promoted articles on the IBI website. We identified these posts on X, LinkedIn, Facebook, Substack and Telegram. Some were posted by accounts that bore the IBI name and logo; others appeared to come from everyday users (likely inauthentic) whose main activity consisted of posting IBI articles.

![LinkedIn post generated by the operation and posted on the platform.](https://images.ctfassets.net/kftzwdyauwt9/an1JJ5Js4alSy9lIIVob6/e90026fa445d657919bc03ee24f53be0/covert-influence-campaign-russia-figure-2.png?w=3840&q=90&fm=webp)

_LinkedIn post generated by this operation and posted on the platform_

Alongside these proactive posts, the operators also generated replies to posts by real Substack users on a range of topics. These replies typically included a request to follow the IBI channel, and were posted on Substack by the IBI account.

![Substack comment generated by the operation in reply to a post.](https://images.ctfassets.net/kftzwdyauwt9/1oHAR2ctypBsnp7hf5acGS/7caf06d81707d5e6afc54ceb56689eca/covert-influence-campaign-russia-figure-3.png?w=3840&q=90&fm=webp)

_Substack comment generated by this operation in reply to a post on the platform._

As well as generating content about IBI, one of the operators generated German-language posts that were posted on a Telegram channel called “Lahme Ente” (“lame duck”). These posts routinely criticized Ukraine, the EU and the German government, and advocated for better relations with Russia.

A second operator, alongside their IBI-related content, generated logos for a dozen Telegram channels (including Lahme Ente) focused on Germany, the USA, France, Poland and Türkiye. Some of these channels sometimes posted about IBI, or shared IBI’s own posts. The second operator also repeatedly asked for Russian-language summaries of these channels’ activity. One of the US-focused channels, posing as an American outlet, featured a bio that included multiple indicators of non-native language.

![Telegram profile for American Observer with non-idiomatic English in the bio.](https://images.ctfassets.net/kftzwdyauwt9/1kDpxY5AWXIn3mETVOyzjd/8c4655c4864e1b6335b1d4eceb2ebf26/covert-influence-campaign-russia-figure-4.png?w=3840&q=90&fm=webp)

_Profile of the Telegram account “American Observer”. One of the ChatGPT users in this case generated a profile picture for the channel and repeatedly asked for Russian-language summaries. Note the non-idiomatic English, including the mysterious, “a totally unhackneyed perspective on hazzy”._

##  Non-AI activity

The core of this operation appeared to be the International Burke Institute (IBI), although the activity we disrupted was focused on social media content promoting or linking to the website rather than content hosted directly on its website.

The site presented itself as an “expert community” with a street address in Israel. As of 17 July, its website claimed a wide range of world-class experts, including luminaries such as Francis Fukuyama and Noam Chomsky, and published a wide array of research. However, in a review of a sample of 36 articles linked to experts on the IBI website and published between September 2025 and May 2026, 34 of the articles were copied from elsewhere on the internet.

Some of these articles were years old; others were attributed to the wrong authors. For example, one article on the China-Pakistan Economic Corridor appears to have been copied from a Cambridge University Press original, but incorrectly attributed to a professor at the University of Nottingham whose expertise is in South Asian politics.

![IBI website article attributed to Professor Katharine Adeney of Nottingham University.](https://images.ctfassets.net/kftzwdyauwt9/1yWr5NlDJlQQZP6gj9FYim/63f750bf32c55c72b4db825a83952147/covert-influence-campaign-russia-figure-5.png?w=3840&q=90&fm=webp)

_Article on the_[ _IBI website_ ⁠(opens in a new window)](<https://web.archive.org/web/20260706102507/https://ibi.institute/read/the-china-pakistan-economic-corridor-the-politics-of-development?type=research>)_, attributed to_[ _Professor Katharine Adeney of Nottingham University_ ⁠(opens in a new window)](<https://www.nottingham.ac.uk/politics/people/katharine.adeney>)_and dated 28 December 2025_

![Cambridge University Press original article by Professor Emeritus Yunas Samad.](https://images.ctfassets.net/kftzwdyauwt9/4BPGqMHKAd7APLIPJdtdzm/ff3e7c135d5322bebe368ac9f3d75636/covert-influence-campaign-russia-figure-6.png?w=3840&q=90&fm=webp)

 _The original of the article, written by Professor Emeritus Yunas Samad of Bradford University and published by_[ _Cambridge University Press_ ⁠(opens in a new window)](<https://www.cambridge.org/core/journals/critical-pakistan-studies/article/chinapakistan-economic-corridor-the-politics-of-development/FA5BEA0227E911EDE2561D14D83EE206>)_on 7 July, 2025._

Another article on migration governance appears to have been copied from the Migration Policy Institute, but misattributed to an Australian professor of food science. This behavior suggests a desire to make the IBI website look more legitimate by stocking it with authentic content while obfuscating that content’s actual source.

![IBI author page for Kate Howell with an article dated 21 January 2026.](https://images.ctfassets.net/kftzwdyauwt9/5cws2bjVZyj1Jur9fY4hRb/1e4c8c404b4ce5edcbde4faf76a54b5c/covert-influence-campaign-russia-figure-7.png?w=3840&q=90&fm=webp)

_Screenshot of an_[ _author page_ ⁠(opens in a new window)](<https://web.archive.org/web/20260706103716/https://ibi.institute/experts/kate-howell>)_on the IBI website, including an article dated 21 January 2026, and attributed to Kate Howell, ostensibly an expert at the Migration Policy Institute._

![Migration Policy Institute original article by Meghan Benton, Natalia Banulescu-Bogdan, and Kate Hooper.](https://images.ctfassets.net/kftzwdyauwt9/143jvnutaE21MgW08aZI4G/ff541730af980e5e4676850d7728ca25/covert-influence-campaign-russia-figure-8.png?w=3840&q=90&fm=webp)

_Original of the article, published by the_[ _Migration Policy Institute_ ⁠(opens in a new window)](<https://www.migrationpolicy.org/research/migration-governance-population-change>)_in April 2025 and written by Meghan Benton, Natalia Banulescu-Bogdan and Kate Hooper._

![Speaker page for Kate Howell from 2017 showing the same photo used on the IBI page.](https://images.ctfassets.net/kftzwdyauwt9/1TC9VAFAXh5xW8lmvRCjjt/2a8f50830da153c0b10cad729cd84bb7/covert-influence-campaign-russia-figure-9.png?w=3840&q=90&fm=webp)

[_Speaker page_ ⁠(opens in a new window)](<https://ausme-2017.p.asnevents.com.au/speaker/188246>)_for Kate Howell, who is actually an Australian_[ _professor in food chemistry_ ⁠(opens in a new window)](<https://findanexpert.unimelb.edu.au/profile/192335-kate-howell>)_, from 2017, including the identical photo to the IBI page._

Alongside these articles, the IBI website included reports on different countries and their sovereignty, as measured by the institute’s index. These were not generated using our models. Some of these reports were pitched as comparisons between two countries. Others focused on single countries, especially those which criticize Russia’s war on Ukraine such as France and Germany, and the European Union. The operation promoted similar narratives about the United States. These reports were typically critical, veering into the polemic; samples include:

  * [France⁠(opens in a new window)](<https://web.archive.org/web/20260706160710/https://ibi.institute/read/the-macron-decade-the-sovereignty-that-was-doomed-to-failure-why-does-france-need-a-sixth-republic?type=research>): “Ten years of Macronism produced exactly the result that a manager who came to the Elysée Palace from the Rothschild Bank must have given: France was opened like a safe with historical capital, and now it is being sold off in parts.”
  * [USA⁠(opens in a new window)](<https://web.archive.org/web/20260706161552/https://ibi.institute/read/trumps-visit-to-china-what-really-happened?type=research>): “Trump arrived [in Beijing] with the No. 1 sovereignty index in the world and left after taking a number of steps that [...] can be qualified as a voluntary reduction in autonomy.”
  * [Germany⁠(opens in a new window)](<https://web.archive.org/web/20260706162212/https://ibi.institute/read/requiem-for-germany-how-germany-sovereignty-melted-into-thin-air?type=research>): “Germany needs an industrial policy that protects jobs, not just stock prices. The country needs an honest discussion about identity, without taboos and hysteria. It needs real military sovereignty, not dependence on American bases. And she needs politicians whose first loyalty is to the German people, not to corporate boards of directors in New York.”
  * [EU⁠(opens in a new window)](<https://web.archive.org/web/20260706162404/https://ibi.institute/read/slovakia-vs-italy-the-paradoxes-of-the-sovereignty-of-the-hostage-countries-of-the-big-union?type=research>): “Slovakia vs Italy: The paradoxes of the Sovereignty of the Hostage-Countries of the ‘Big’ Union”



While the social media content promoting the IBI was generated by ChatGPT users in Russia who took pains to hide their origins, and much of the content on the IBI website appeared copied from elsewhere, some online traces suggest that a handful of real individuals in Israel may also have represented the IBI in article submissions and at conferences. We are not in a position to determine the relationship between these individuals, the IBI, and the operators in Russia.

## Impact

The operation’s immediate impact appears to have been limited: typical social media posts only received low numbers of views, and the official IBI accounts had low subscriber numbers. The operation’s Telegram channels appear to have attracted more subscribers, generally counting 10-20,000 followers each. Using the Brookings [Breakout Scale⁠(opens in a new window)](<https://www.brookings.edu/articles/the-breakout-scale-measuring-the-impact-of-influence-operations/>) to assess the impact of this operation, we would assess it as at the lower end of **Category Three** (multiple platforms, with some indications of breakout to authentic audiences).

The significance of the operation lies less in the audience it reached, however, than in the infrastructure it had built. While the actors only used ChatGPT to produce isolated promotional posts, those posts pointed to an otherwise credible-appearing institution, complete with purported experts, republished academic work and a purported proprietary risk index. This illustrates how influence actors can use AI as a supporting tool within a broader effort to manufacture authority, obscure the source of favored narratives, and establish assets that could be scaled over time. It also illustrates how their supporting use of AI can lead to the broader operation being exposed.

  * [2026](</news/?tags=2026>)



## Author

OpenAI

## Keep reading

[View all](</news/>)

![Strengthening Democratic Oversight in National Security — card image](https://images.ctfassets.net/kftzwdyauwt9/1qebg0OnHIh4dqr84zXR3Q/dba2f0e83ba4615a71894fd7fd1656e1/openai-democratic-oversight-page-cover-v002.png?w=3840&q=90&fm=webp)

[Strengthening Democratic Oversight in National SecurityGlobal AffairsAug 18, 2026](</index/strengthening-democratic-oversight-in-national-security/>)

![OpenAI joins PORTS-Pike project, expanding community investment and supporting thousands of Southern Ohio jobs — card image](https://images.ctfassets.net/kftzwdyauwt9/6RUPcXx0eTGghDpM851Qy1/ab11d2d0849ad9544249bf7b77ee46fe/openai-joins-ports-pike-project-cover-v001.png?w=3840&q=90&fm=webp)

[OpenAI joins PORTS-Pike projectGlobal AffairsAug 17, 2026](</index/openai-joins-ports-pike-project/>)

![New policy ideas for the Intelligence Age — Card image](https://images.ctfassets.net/kftzwdyauwt9/AJqxrcFJn4IUKHIkwneFA/979315f3b490abc2e2055be12d97c9bb/new-policy-ideas-for-the-intelligence-age--cover-v001.png?w=3840&q=90&fm=webp)

[New policy ideas for the Intelligence AgeGlobal AffairsAug 17, 2026](</index/new-policy-ideas-for-the-intelligence-age/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6](</index/gpt-6-astra/>)
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
