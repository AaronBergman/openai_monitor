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

Early AI experiments in job matching

  * Early AI experiments in job matching
  * Fine-tuning the OpenAI API for personalized match explanations
  * GPT personalization leads to demonstrable growth 



# Indeed uses OpenAI to deliver contextual job matching to millions of job seekers

![A white Indeed logo superimposed on an abstract painting with broad strokes of dark and light blues.](https://images.ctfassets.net/kftzwdyauwt9/4Z4HjWDOPAFMnPjXAkL9SJ/353cbeeb2f8df66383151a5c9706cf63/oai_indeed_hero.jpg?w=3840&q=90&fm=webp)

Loading…

Share

[ _Indeed_ ⁠(opens in a new window)](<https://www.indeed.com/about>), whose mission is to help people get jobs, is the world’s #1 job site1. Over 350 million unique visitors2 come to Indeed every month to connect with more than 3.5 million employers and over 32 million jobs. But what’s more is that every three seconds someone gets hired on Indeed3.

Since Indeed’s inception, AI has powered the millions of connections between job seekers and employers on the platform, through features such as ‘Invite to Apply’ which sends AI-based job recommendations to job seekers based on their resume, Indeed Profile, and other qualifications. Improvements in AI—specifically generative AI—are helping match job seekers to jobs in new and exciting ways. Using OpenAI's GPT models and fine-tuning capabilities, Indeed enhanced the personalized language in the ‘Invite to Apply’ feature to better explain why a candidate’s background or previous work experience makes a job a good fit.  


## Early AI experiments in job matching

Indeed's early AI models effectively matched job seekers with employers’ job postings and provided brief explanations for these matches. But Indeed’s product and engineering teams believed that OpenAI’s GPT models could do even more by ingesting natural language to offer better context as to w _hy_ a candidate is receiving a specific job recommendation. __

Adding a more insightful “why” to job recommendations became the goal for the Indeed team to work with OpenAI. 

Indeed’s engineering team started working with OpenAI in 2023, following the OpenAI documentation for the Chat Completions API and iterating on its few-shot prompting. Throughout the development process, the team conducted rigorous A/B testing and continuously monitored and evaluated every change, both during the implementation phase and post-launch.  
  


![Indeed Uses OpenAI > Media > Laptop 2 > Asset](https://images.ctfassets.net/kftzwdyauwt9/4fy9JCSh0XI6f95aswioHv/17c2c7683ae7d419d59bf710117d2070/Devices_in_Use_Laptop_person_working_on_a_laptop_with_coffee_cup_on_the_table_-IOperp_BURNETT-.jpg?w=3840&q=90&fm=webp)

## Fine-tuning the OpenAI API for personalized match explanations

Indeed found that training the model to respond using few-shot-prompting was effective at increasing the relevant “why” in explanations, but at Indeed's massive scale, this was resulting in high token consumption. To increase efficiency, OpenAI and Indeed worked together to fine-tune a smaller GPT model that was able to deliver similarly performing results but with 60% fewer tokens.

As part of the fine-tuning process, they harnessed GPT‑4 for data augmentation, and built out specific content guidelines. The team also built out an annotation operation, which involved labeling LLM-generated output, creating ground truths for facilitating automated evaluation, and adding context to help the models understand nuances.

Further testing validated the value of personalization in job recommendations, increasing the pool of qualified candidates. To scale personalized job recommendations, Indeed worked with OpenAI to adopt dedicated instances which were provisioned in January 2024. The Indeed engineering team successfully deployed the fine-tuned GPT model to these instances, allowing them to personalize employment opportunities to millions more job seekers.

“We have invested in our own AI matching technology for decades to help connect job seekers and employers. Regardless of how good our matching may be, explainability is key to any successful recommendation system. Combining OpenAI's GPT explanations with Indeed's own proprietary AI and vast marketplace data allows us to connect more people to jobs, faster—a win for job seekers, employers, and society,” says Chris Hyams, CEO of Indeed.  


## GPT personalization leads to demonstrable growth 

The effectiveness of GPT‑developed personalized messaging was proven through a multi-stage experiment that expanded to nearly 20 million messages per day over the course of several months. 

“We’re always testing ways to improve the Invite to Apply experience and find relevant opportunities for job seekers. Fine-tuning OpenAI’s GPT models has helped us deliver more personalized recommendations, even as we scaled from 1 million to 20 million messages a day,” says Horatio Lun, Indeed Platform PM.

The Indeed team tested a traditional job matching version of Invite to Apply against the GPT‑powered version that had additional customized context for the applicant. The performance uplift was immediately noticeable:

  * **+20% increase in started job applications**
  * **+13% uplift in downstream success** indicating that not only were more candidates likely to apply, but that employers were finding those applicants to be a good fit, ultimately leading to more hires



![The image shows two job recommendation cards for “Brenda.” The left \(Control\) suggests a caregiver role based on experience at Northern Canal Medical Center. The right \(With OpenAI\) highlights a similar role, emphasizing patient care experience and perks.](https://images.ctfassets.net/kftzwdyauwt9/5zpJwSdvHKSZnkOHW9t4hX/c909734c31505c234708a649078b699f/OAI_Indeed_Product.png?w=3840&q=90&fm=webp)

By leveraging GPT‑powered context for its 'Invite to Apply' feature, Indeed experienced an increase in both qualified candidates and hires, which positively impacted its revenue during testing.

“Importantly, we’re able to leverage OpenAI in an ROI-positive way, so we see a lot of opportunity to continue to invest in this new infrastructure in ways that will help us grow revenue,” says Chris Hyams, CEO of Indeed.

And Invite to Apply is just one example of how Indeed is finding success with OpenAI technology. Nearly a dozen products at Indeed are using OpenAI to deliver more personalized and compelling experiences to help job seekers discover new opportunities and employers hire faster.

## Interested in learning more about ChatGPT for business?

[Talk with our team](</contact-sales/>)

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
