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

April 10, 2026

OpenAI Academy

# Using custom GPTs

Build purpose-built ChatGPT assistants that follow your instructions, use your context, and streamline repeatable work.

Loading…

Share

Custom GPTs vs. general chat

  * Custom GPTs vs. general chat
  * Custom GPTs built by the OpenAI team
  * How to build a custom GPT 
    * 1\. Identify strong use cases
    * 2\. Create GPT
    * 3\. Test your GPT’s performance
  * Additional resources 



  * Custom GPTs vs. general chat
  * Custom GPTs built by the OpenAI team
  * How to build a custom GPT 
    * 1\. Identify strong use cases
    * 2\. Create GPT
    * 3\. Test your GPT’s performance
  * Additional resources 



Some versions of ChatGPT let you build **custom GPTs** —purpose-built versions of ChatGPT designed for a specific task or workflow. Instead of starting from a blank chat each time, a custom GPT can follow your preferred format, use your team’s context, and produce more consistent outputs—whether you’re drafting content, analyzing recurring datasets, generating visuals, or answering common questions.

Custom GPTs are powered by tailored instructions that define how the GPT behaves. You can also add knowledge (files you upload) and enable tools (such as web search, data analysis, or connected actions). The result: less re-explaining, less copy/pasting, and fewer “wait—what’s the context again?” moments.

You can explore custom GPTs [_here_ ⁠(opens in a new window)](<https://chatgpt.com/gpts>).

## Custom GPTs vs. general chat

A regular chat is well-suited for quick, one-off tasks—brainstorming ideas, quick rewrites, or answering a question in the moment.

A **custom GPT** is a better fit when you need something repeatable and consistent. For example: 

  * **Automating repeat tasks** : Save a prompt you use often and turn it into a reliable workflow.
  * **Adding tools or integrations** : Pull in more context, analyze files, or use connected apps for deeper answers.
  * **Maintaining consistent context** : Apply the same structure, tone, or instructions without restating them. 



If you find yourself reusing the same prompt, re-uploading the same files, or rewriting the same instructions for teammates—it may be time to build a custom GPT.

## Custom GPTs built by the OpenAI team

**Custom GPT**| **Purpose**  
---|---  
[ _ChatGPT Use Cases for Work_ ⁠(opens in a new window)](<https://chatgpt.com/g/g-h5aUtVu0G-chatgpt-use-cases-for-work>)| Brainstorm role-specific ways to apply ChatGPT  
[ _Professional Writing Coach_ ⁠(opens in a new window)](<https://chatgpt.com/g/g-ZRYV8dzO8-professional-writing-coach>)| Polish emails, reports, and presentations  
[ _Data Analyst_ ⁠(opens in a new window)](<https://chatgpt.com/g/g-HMNcP6w7d-data-analyst>)| Summarize, chart, and explain uploaded data  
[ _Coding Assistant_ ⁠(opens in a new window)](<https://chatgpt.com/g/g-vK4oPfjfp-coding-assistant>)| Generate, review, and debug code snippets  
[ _Visual Designer_ ⁠(opens in a new window)](<https://chatgpt.com/g/g-n7u0emyLB-visual-designer>)| Turn text prompts into on-brand images  
  
## How to build a custom GPT 

### 1\. Identify strong use cases

Good GPTs usually begin with a simple, repeatable need. Focus on workflows that occur regularly—such as drafting the same type of message, summarizing recurring meetings, answering common questions, or turning raw data into a consistent weekly report.

Example use cases:

  * **Knowledge Assistant / FAQ Bot:** Answers questions from documents or internal resources. 
  * **Writing & Editing Assistant:** Rewrites, polishes, or formats text for tone, clarity, and style.
  * **Learning Companion / Tutor:** Explains concepts, quizzes users, and generates study materials.
  * **Project / Workflow Assistant:** Summarizes meetings, tracks progress, and drafts status updates.
  * **Data & Insights Assistant**: Analyzes data, summarizes trends, and generates visual or narrative reports.



### 2\. Create GPT

To get started, open **GPTs** from the ChatGPT sidebar, then select **Create** to open the GPT builder. 

When you open the GPT builder, you will see two tabs: **Create** and **Configure**. In the **Create** tab, you can message the GPT Builder to help you build a new GPT. You can say something like, "Make a creative who helps generate visuals for new products" or "Make a software engineer who helps format my code." Defining clear objectives ensures your GPT stays focused and relevant. 

If you want to define the details of your GPT more precisely, go to the **Configure** tab and complete the required fields:

  * **Name** : Choose a clear, descriptive name so it’s easy to find and its purpose is immediately understood.
  * **Description** : Explain what the GPT does and when to use it.
  * **Instructions** : Define how the GPT should behave, including its functions, tone, and any behaviors to avoid. 
  * **Conversation starters (Optional)** : Provide example prompts that appear when users open the GPT. These help guide users on how to begin their interaction.
  * **Knowledge** : Upload relevant documents to give your GPT the context it needs for accurate answers.
  * **Capabilities** : Enable features such as image generation, data analysis, web search, and canvas.
  * **Custom actions** : Set up actions so your GPT can call third-party APIs to retrieve data, modify external sources, or trigger external processes.



Writing instructions is often the most challenging step, as it requires translating your goals into clear, actionable guidance the GPT can follow. A simple way to move faster is to ask ChatGPT to draft a first version, then refine it based on real examples.

**Tip** _:_ To configure custom actions, see the comprehensive guide on the[ _OpenAI Cookbook._ ⁠(opens in a new window)](<https://cookbook.openai.com/examples/chatgpt/gpt_actions_library/.gpt_action_getting_started>)

### 3\. Test your GPT’s performance

Before[ sharing your GPT⁠(opens in a new window)](<https://help.openai.com/articles/9083988-how-to-share-gpts-within-workspaces>), it is important to check that it works as expected. You can do this with evals, a simple way to assess its outputs.

**Set up your evaluation:**

  * Write 10 to 15 questions that reflect the tasks your GPT should handle.
  * Include the correct answers for each question.
  * Use these questions to see if your GPT gives accurate and reliable responses.
  * Review the results and adjust your GPT’s instructions or knowledge if needed.



**Tip:** When making changes, don’t forget to click**“Update”** in the top right to save them. It’s easy to miss, especially when you’re returning to reconfigure an existing GPT.

Building a custom GPT doesn’t have to be complex. Start with a workflow you already repeat, draft a first version of the instructions, and test it with a small set of examples. You’ll learn quickly what to adjust—and small refinements usually make a big difference. Once it feels reliable, share it with your team so everyone can get to the same quality output faster, with less effort.

## Additional resources 

  * [ _GPT FAQ_ ⁠(opens in a new window)](<https://help.openai.com/articles/8554407-gpts-faq>)
  * [_GPT Building_ ⁠(opens in a new window)](<https://help.openai.com/articles/8554397-creating-a-gpt>)
  * [_GPT Instruction Writing_ ⁠(opens in a new window)](<https://help.openai.com/articles/9358033-key-guidelines-for-writing-instructions-for-custom-gpts>)
  * [_GPT Custom Action Cookbook_ ⁠(opens in a new window)](<https://cookbook.openai.com/examples/chatgpt/gpt_actions_library/.gpt_action_getting_started>)



## Continue learning with OpenAI Academy

Discover additional guides and resources to help you build practical AI skills.

[View all topics](</academy/>)

## Keep reading

[View all](</news/>)

![How data science teams use Codex > card image](https://images.ctfassets.net/kftzwdyauwt9/xyevYnp4Ptaa1eMgBDNjS/75fea80018f321b89809d893f1a5786d/data_science_teams.png?w=3840&q=90&fm=webp)

[How data science teams use ChatGPT Work | OpenAIOpenAI AcademyJul 14, 2026](</academy/chatgpt-work/how-data-science-teams-use-codex/>)

![How sales teams use Codex > card image](https://images.ctfassets.net/kftzwdyauwt9/1O4te2wMh6O77eDV6kapG3/02845b054a09297b9fada40c4cc9a71f/sales_teams.png?w=3840&q=90&fm=webp)

[How sales teams use ChatGPT Work | OpenAIOpenAI AcademyJul 14, 2026](</academy/chatgpt-work/how-sales-teams-use-codex/>)

![Academy > Getting started > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/1Xk9723QKj2Vb9dC6RMebS/5e588c112042794e62178a224eaff418/getting-started.png?w=3840&q=90&fm=webp)

[Getting started with ChatGPT | OpenAIOpenAI AcademyJul 10, 2026](</academy/getting-started/>)

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
