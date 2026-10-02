Skip to main content

[](</>)[](</business/>)

  * Why OpenAI
  * Products
  * Solutions
  * Resources
  * [Customers](</business/customer-stories/>)
  * [Pricing](</business/pricing/>)



Try OpenAI[Contact sales](</contact-sales/>)

  * Why OpenAI
  * Products
  * Solutions
  * Resources
  * [Customers](</business/customer-stories/>)
  * [Pricing](</business/pricing/>)



[Contact sales](</contact-sales/>)Try OpenAI

OpenAI

[Plugins](</business/plugins/>)

![](https://files.openai.com/content?id=file_00000000fb6081f7aa3f621147713ad6&cdn=1&cp=pi&ma=30844800&ts=0&p=pi&cid=8&sig=7b7a02db1929ca7e8aebd24b459d525b6ac1ae88b282b387816507320645a98d&v=0)![](https://files.openai.com/content?id=file_00000000fb6081f7aa3f621147713ad6&cdn=1&cp=pi&ma=30844800&ts=0&p=pi&cid=8&sig=7b7a02db1929ca7e8aebd24b459d525b6ac1ae88b282b387816507320645a98d&v=0)

# Databricks Genie

Analyze lakehouse data and dashboards with natural language.

[Install plugin(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e24c86b19248191a8c6abb5bc115819>)[Contact sales](</contact-sales/>)

Capabilities
    Interactive, Read, Write

Category
    [Data](</business/plugins/?tab=plugins-data-research>)

Developer
    OpenAI

Website
    [(opens in a new window)](<https://www.databricks.com/>)

![](https://files.openai.com/content?id=file_00000000a06481f6b01ef561cffb7a27&cdn=1&cp=pi&ma=31708800&ts=0&p=pi&cid=8&sig=361dece7ef5ee83a94bd0a3362b6e9db0384316cfed471514d48be0228d20d15&v=0)Databricks analyze last month’s customer retention, find the biggest drop-offs, and recommend three actions backed by the data.

![](https://files.openai.com/content?id=file_00000000a06481f6b01ef561cffb7a27&cdn=1&cp=pi&ma=31708800&ts=0&p=pi&cid=8&sig=361dece7ef5ee83a94bd0a3362b6e9db0384316cfed471514d48be0228d20d15&v=0)Databricks analyze last month’s customer retention, find the biggest drop-offs, and recommend three actions backed by the data.

## Conversation response

## August 2026 customer retention

**Retention fell to 84%, down 4 percentage points from July.** August lost 176 customers. New customers had the sharpest cohort decline; small businesses accounted for most losses.

Retention means month-start paid customers who remain paid at month-end, divided by the month-start population. In-month signups are excluded. Data: July–August 2026, `analytics.customer_month_status`.

### Where retention fell

“New customers” joined in the prior calendar month: July for August’s cohort. “Established” customers joined earlier.

![Retention by customer cohort: new customers fell from 75% in July to 65% in August; established customers fell from 91.25% to 88.75%.](https://cdn.openai.com/business/plugins/conversations/databricks/retention-cohorts-2026-08-v1.png)

Cohort| July retained / starting| July retention| August retained / starting| August retention| Change  
---|---|---|---|---|---  
New customers| 150 / 200| 75.0%| 143 / 220| 65.0%| −10.0 pp  
Established| 730 / 800| 91.3%| 781 / 880| 88.8%| −2.5 pp  
**Total**| **880 / 1,000**| **88.0%**| **924 / 1,100**| **84.0%**| **−4.0 pp**  
  
### Where customers were lost

Segment| July retention| August retained / starting| August retention| August losses  
---|---|---|---|---  
Small business| 83%| 480 / 600| 80%| 120  
Mid-market| 93%| 276 / 300| 92%| 24  
Enterprise| 93%| 168 / 200| 84%| 32  
  
Small businesses represented **68.2% of August losses** : 120 of 176. Enterprise had the largest segment decline, at 9 percentage points. Cohort and segment tables describe the same customers; their losses should not be added together.

### Three recommended actions

  1. **Test guided setup for new customers.** Among August’s new-customer cohort, 85 of 100 customers who completed the key workflow by August 1 were retained, versus 58 of 120 who had not: 85% versus 48.3%. Run a randomized test of guided setup and compare first-full-month retention. This association does not prove that setup caused better retention.
  2. **Review the 120 small-business losses before choosing a retention offer.** Group cancellation reasons and usage patterns to distinguish onboarding problems, product gaps, and price concerns. This is the largest pool of losses; the current data does not identify their causes.
  3. **Audit the 32 enterprise losses.** Losses rose from 14 in July to 32 in August despite an unchanged starting population of 200. Review renewal outcomes and account notes before deciding which intervention fits.



Customer growth masks the decline: August ended with **1,120 paid customers** , comprising 924 retained customers plus 196 new customers still active at month-end, up from 1,100 in July.

I can turn the guided-setup recommendation into a test plan with eligibility criteria, a control group, and a first-full-month retention measure.

## How it works

Connect Databricks to ChatGPT to inspect governed lakehouse data, ask analytics questions, generate SQL, summarize dashboards or Genie outputs, and package insights for teams.

## What else can you do?

  * ### Explore lakehouse data faster

![](https://files.openai.com/content?id=file_00000000a06481f6b01ef561cffb7a27&cdn=1&cp=pi&ma=31708800&ts=0&p=pi&cid=8&sig=361dece7ef5ee83a94bd0a3362b6e9db0384316cfed471514d48be0228d20d15&v=0)Databricks Genie Find the main drivers of last week's change in [metric]. Show the query path, summarize the result, and note caveats.

[Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e24c86b19248191a8c6abb5bc115819?install&prompt=Find%20the%20main%20drivers%20of%20last%20week's%20change%20in%20%5Bmetric%5D.%20Show%20the%20query%20path%2C%20summarize%20the%20result%2C%20and%20note%20caveats.&surface=work>)

  * ### Generate and review SQL

![](https://files.openai.com/content?id=file_00000000a06481f6b01ef561cffb7a27&cdn=1&cp=pi&ma=31708800&ts=0&p=pi&cid=8&sig=361dece7ef5ee83a94bd0a3362b6e9db0384316cfed471514d48be0228d20d15&v=0)Databricks Genie Draft SQL to calculate [metric] by [dimension] for the last 90 days. Explain the joins and filters, and list checks for missing data or unexpected values.

[Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e24c86b19248191a8c6abb5bc115819?install&prompt=Draft%20SQL%20to%20calculate%20%5Bmetric%5D%20by%20%5Bdimension%5D%20for%20the%20last%2090%20days.%20Explain%20the%20joins%20and%20filters%2C%20and%20list%20checks%20for%20missing%20data%20or%20unexpected%20values.&surface=work>)

  * ### Package insights for stakeholders

![](https://files.openai.com/content?id=file_00000000a06481f6b01ef561cffb7a27&cdn=1&cp=pi&ma=31708800&ts=0&p=pi&cid=8&sig=361dece7ef5ee83a94bd0a3362b6e9db0384316cfed471514d48be0228d20d15&v=0)Databricks Genie Review this dashboard and explain what changed most versus the prior period, with likely drivers and follow-up checks.

[Try in ChatGPT Work(opens in a new window)](<https://chatgpt.com/plugins/Plugin_1e24c86b19248191a8c6abb5bc115819?install&prompt=Review%20this%20dashboard%20and%20explain%20what%20changed%20most%20versus%20the%20prior%20period%2C%20with%20likely%20drivers%20and%20follow-up%20checks.&surface=work>)




## What’s included

### Skills

  * databricks
  * databricks-dashboards



## Resources

### [Help centerLearn more](<https://help.openai.com/en/articles/11487775-connectors-in-chatgpt>)

### [Plugin supportLearn more](<https://help.databricks.com>)

### [Privacy policyLearn more](<https://www.databricks.com/legal/privacynotice>)

## Add the Databricks Genie plugin in a few clicks

Availability depends on the plugin, your plan, and workspace settings. Some connections require admin setup or approval. Contact your workspace admin if access is blocked.

[View the setup guide](<https://learn.chatgpt.com/docs/plugins>)

## Explore related plugins

[![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&sig=faa8e9a07b2b67ac2907c704f195addb0cca5e7d0a06d3ade1fd063cbe37ea08&v=0)![](https://files.openai.com/content?id=file_00000000589081fd837e2d8fbfc1a83d&cdn=1&cp=pi&ma=30153600&ts=0&p=pi&cid=8&sig=faa8e9a07b2b67ac2907c704f195addb0cca5e7d0a06d3ade1fd063cbe37ea08&v=0)DataTurn data into clear decisions.](</business/plugins/data/>)[![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&sig=8645995b849ceccce60bf2b798fdb25428471458f32025c66606df1c7046ec07&v=0)![](https://files.openai.com/content?id=file_000000005c608230b877bc897fa75256&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=1&sig=8645995b849ceccce60bf2b798fdb25428471458f32025c66606df1c7046ec07&v=0)Product DesignTurn product ideas into designs and research artifacts.](</business/plugins/product-design/>)[![](https://files.openai.com/content?id=file_00000000a7a881f79bd3e0bdaf6f44d8&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=8&sig=3681847b083c03ec3f94453b15bea76630d8877224f486882867c1affcde9821&v=0)![](https://files.openai.com/content?id=file_00000000a7a881f79bd3e0bdaf6f44d8&cdn=1&cp=pi&ma=32400000&ts=0&p=pi&cid=8&sig=3681847b083c03ec3f94453b15bea76630d8877224f486882867c1affcde9821&v=0)DBTWork with dbt projects](</business/plugins/dbt/>)[![](https://files.openai.com/content?id=file_000000002c9871f88886c70ee05182be&cdn=1&cp=pi&ma=30585600&ts=0&p=pi&cid=1&sig=d9f82aa7ff5946d7b3572fb9749746956a02925ce49b4f256a1d6bb1575ef7cb&v=0)![](https://files.openai.com/content?id=file_000000002c9871f88886c70ee05182be&cdn=1&cp=pi&ma=30585600&ts=0&p=pi&cid=1&sig=d9f82aa7ff5946d7b3572fb9749746956a02925ce49b4f256a1d6bb1575ef7cb&v=0)AlationGoverned Knowledge Layer](</business/plugins/alation/>)[![](https://files.openai.com/content?id=file_00000000f92071f79930229160a6ca3b&cdn=1&cp=pi&ma=30585600&ts=0&p=pi&cid=8&sig=6faeb8bbf3cc92b5d0996a82dd40d42ac8b54a7aa3afa8c7950b2f36720a3de7&v=0)![](https://files.openai.com/content?id=file_000000001bf871f7959c46e1bd9802cd&cdn=1&cp=pi&ma=31708800&ts=0&p=pi&cid=8&sig=64ebef30bd218a7048400d20b79b338a5efea8ec72de36dfbf0754fe82ec178e&v=0)DeepnoteRun data workflows with agents](</business/plugins/deepnote/>)[![](https://files.openai.com/content?id=file_00000000305c81f592476d99e3faab61&cdn=1&cp=pi&ma=32313600&ts=0&p=pi&cid=8&sig=64c45bfe23621d0cb193310b6fc5cded6a470a131c891a40a6dca4c7198340d4&v=0)![](https://files.openai.com/content?id=file_00000000dda481f58d27cff6712efd6e&cdn=1&cp=pi&ma=31622400&ts=0&p=pi&cid=8&sig=0f9a40070454550d86b04a4023fefbd1dbcceb54dc9defdb316dfc7467777022&v=0)TableauSee and understand data](</business/plugins/tableau/>)

## Get started with plugins

Bring your organization’s data and tools into OpenAI products and accelerate what your teams can do.

[Try ChatGPT Business(opens in a new window)](<https://chatgpt.com/team-sign-up>)[Contact sales](</contact-sales/>)

Research

  * [Research Index](</research/index/>)
  * [Research Overview](</research/>)
  * [Economic Research](</signals/>)



Latest Advancements

  * [GPT-6.1 Sol](</index/introducing-gpt-6-1-sol/>)
  * [GPT-6 Astra](</index/gpt-6-astra/>)
  * [GPT-5.6](</index/gpt-5-6/>)
  * [GPT-5.5](</index/introducing-gpt-5-5/>)



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
  * [Codex](<https://chatgpt.com/codex/>)
  * [Dots(opens in a new window)](<https://chatgpt.com/features/dots>)
  * [Release Notes](</products/release-notes/>)



API Platform

  * [Overview](</api/>)
  * [API Log In(opens in a new window)](<https://platform.openai.com/login>)
  * [Docs(opens in a new window)](<https://developers.openai.com/api/docs>)



Business

  * [Overview](</business/>)
  * [Solutions](</solutions/>)
  * [Resources](</business/learn/>)
  * [Plugins](</business/plugins/>)
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

### 1Find the Databricks Genie plugin1Find the Databricks Genie plugin

Browse for plugins that support your team’s tools and tasks.

![ChatGPT plugin directory showing Google Drive, Slack, and Google Calendar.](https://images.ctfassets.net/kftzwdyauwt9/6yJgeQSCr32uzNSynka2cc/f5da877c4684cb18ecb9babf62723e2b/1.png?w=3840&q=90&fm=webp)

### 2Install and connect2Install and connect

Install the plugin, then follow the prompts to review permissions and connect any required apps.

![Select the add button to install the Gmail plugin.](https://images.ctfassets.net/kftzwdyauwt9/7gNt7Pk3s8Mf0ql8JAedDS/c533bb5268aef1bed2ef56d5f5ccb06f/2.png?w=3840&q=90&fm=webp)

### 3Put it to work3Put it to work

Start a new chat in ChatGPT Work or Codex, describe the result you need, and ask it to use plugins.

![Ask ChatGPT to prepare a meeting brief using Google Calendar, Gmail, and Slack.](https://images.ctfassets.net/kftzwdyauwt9/tQaC60CeLrMeEalZJnAwl/b4419ccddbaed0103124a22854097e81/3.png?w=3840&q=90&fm=webp)
