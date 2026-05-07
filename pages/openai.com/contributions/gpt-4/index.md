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

# GPT‑4 contributions

## Pretraining

**Core contributors  
** Christopher Berner  _Supercomputing lead  
_ Greg Brockman  _Infrastructure lead  
_ Trevor Cai  _Throughput lead_  
David Farhi  _Manager of optimization team_  
Chris Hesse _Infrastructure usability co-lead  
_ Shantanu Jain _Infrastructure usability co-lead  
_ Kyle Kosic  _Uptime and stability lead  
_ Jakub Pachocki  _Overall lead, optimization lead_  
Alex Paino  _Architecture & data vice lead_  
Mikhail Pavlov  _Software correctness lead_  
Michael Petrov  _Hardware correctness lead  
_ Nick Ryder _Architecture & data lead_  
Szymon Sidor _Optimization vice lead_  
Nikolas Tezak _Execution lead_  
Phil Tillet _Triton lead  
_ Amin Tootoonchian _Model distribution_ , _systems & networking lead_  
Qiming Yuan _Dataset sourcing and processing lead_  
Wojciech Zaremba  _Manager of dataset team_

**Compute cluster scaling  
** Christopher Berner, Oleg Boiko, Andrew Cann, Ben Chess, Christian Gibson, Mateusz Litwin, Emy Parparita, Henri Roussez, Eric Sigler, Akila Welihinda

**Data  
** Sandhini Agarwal, Suchir Balaji, Mo Bavarian, Che Chang, Sheila Dunning, Leo Gao, Jonathan Gordon, Peter Hoeschele, Shawn Jain, Shantanu Jain, Roger Jiang, Heewoo Jun, Łukasz Kaiser, Nitish Shirish Keskar, Jong Wook Kim, Aris Konstantinidis, Chak Li, Todor Markov, Bianca Martin, David Mély, Oleg Murk, Hyeonwoo Noh, Long Ouyang, Alex Paino, Vitchyr Pong, Alec Radford, Nick Ryder, John Schulman, Daniel Selsam, Ian Sohl, Chelsea Voss, Lilian Weng, Clemens Winter, Tao Xu, Qiming Yuan, Wojciech Zaremba

**Distributed training infrastructure  
** Greg Brockman, Trevor Cai, Chris Hesse, Shantanu Jain, Yongjik Kim, Kyle Kosic, Mateusz Litwin, Jakub Pachocki, Mikhail Pavlov, Szymon Sidor, Nikolas Tezak, Madeleine Thompson, Amin Tootoonchian, Qiming Yuan

**Hardware correctness  
** Greg Brockman, Shantanu Jain, Kyle Kosic, Michael Petrov, Nikolas Tezak, Amin Tootoonchian, Chelsea Voss, Qiming Yuan

**Optimization & architecture  
**Igor Babuschkin, Mo Bavarian, Adrien Ecoffet, David Farhi, Jesse Han, Ingmar Kanitscheider, Daniel Levy, Jakub Pachocki, Alex Paino, Mikhail Pavlov, Nick Ryder, Szymon Sidor, Jie Tang, Jerry Tworek, Tao Xu

**Training run babysitting  
** Suchir Balaji, Mo Bavarian, Greg Brockman, Trevor Cai, Chris Hesse, Shantanu Jain, Roger Jiang, Yongjik Kim, Kyle Kosic, Mateusz Litwin, Jakub Pachocki, Alex Paino, Mikhail Pavlov, Michael Petrov, Nick Ryder, Szymon Sidor, Nikolas Tezak, Madeleine Thompson, Phil Tillet, Amin Tootoonchian, Chelsea Voss, Ben Wang, Tao Xu, Qiming Yuan

## Long context

**Core contributors  
** Gabriel Goh _Long context co-lead  
_ Łukasz Kaiser _Long context lead  
_ Ben Wang _Attention architecture lead  
_ Clemens Winter _Long context co-lead_

**Long context research**  
Mo Bavarian, Gabriel Goh, Heewoo Jun, Łukasz Kaiser, Chak Li, Ben Wang, Clemens Winter

**Long context kernels**  
Phil Tillet

## Vision

**Core contributors**  
Trevor Cai _Execution lead_  
Mark Chen _Vision team co-lead, Deployment lead_  
Casey Chu _Initial prototype lead_  
Chris Hesse _Data load balancing & developer tooling lead_  
Shengli Hu _Vision Safety Evaluations lead_  
Yongjik Kim _GPU performance lead  
_ Jamie Kiros _Overall vision co-lead, deployment research & evaluation lead  
_Daniel Levy Overall _vision co-lead, optimization lead_  
Christine McLeavey _Vision team lead_  
David Mély _Data lead_  
Hyeonwoo Noh _Overall vision co-lead, research lead_  
Mikhail Pavlov _Scaling engineering lead_  
Raul Puri _Overall vision co-lead, engineering lead_  
Amin Tootoonchian _Model distribution, systems & networking lead_

**Architecture research**  
Casey Chu, Jamie Kiros, Christine McLeavey, Hyeonwoo Noh, Raul Puri, Alec Radford, Aditya Ramesh

**Compute cluster scaling**  
Andrew Cann, Rory Carmichael, Christian Gibson, Henri Roussez, Akila Welihinda

**Distributed training infrastructure**  
Trevor Cai, Yunxing Dai, Chris Hesse, Brandon Houghton, Yongjik Kim, Łukasz Kondraciuk, Hyeonwoo Noh, Mikhail Pavlov, Raul Puri, Nikolas Tezak, Amin Tootoonchian, Tianhao Zheng

**Hardware correctness**  
Oleg Boiko, Trevor Cai, Michael Petrov, Alethea Power

**Data**  
Jong Wook Kim, David Mély, Reiichiro Nakano, Hyeonwoo Noh, Long Ouyang, Raul Puri, Pranav Shyam, Tao Xu

**Alignment Data**  
Long Ouyang

**Training run babysitting**  
Trevor Cai, Kyle Kosic, Daniel Levy, David Mély, Reiichiro Nakano, Hyeonwoo Noh, Mikhail Pavlov, Raul Puri, Amin Tootoonchian

**Deployment & post-training**  
Ilge Akkaya, Mark Chen, Jamie Kiros, Rachel Lim, Reiichiro Nakano, Raul Puri, Jiayi Weng

## RL & alignment

**Core contributors**  
Greg Brockman _Core infrastructure author  
_ Arka Dhar _Human data product manager_  
Liam Fedus _Data flywheel lead_  
Tarun Gogineni _Model creativity_  
Rapha Gontijo-Lopes _Synthetic data_  
Joshua Gross _Data collection engineering co-lead  
_ Johannes Heidecke _Refusals & model safety co-lead_  
Joost Huizinga _Initial fine-tuning derisking_  
Teddy Lee _Human data product manager_  
Jan Leike _Alignment co-lead_  
Ryan Lowe _Alignment co-lead_  
Luke Metz _Infrastructure lead_ ,_ChatML format lead_  
Long Ouyang _IF data collection lead_  
John Schulman _Overall lead_  
Jerry Tworek _Code lead_  
Carroll Wainwright _IF data infrastructure lead_  
Jonathan Ward _Data collection engineering co-lead_  
Jiayi Weng _RL Infrastructure author_  
Sarah Yoo _Human data operations manager_  
Wojciech Zaremba  _Human data lead_  
Chong Zhang _Refusals & model safety co-lead_  
Shengjia Zhao _Reward model lead_  
Barret Zoph _Overall training lead_

**Dataset contributions**  
Diogo Almeida, Mo Bavarian, Juan Felipe Cerón Uribe, Tyna Eloundou, Liam Fedus, Tarun Gogineni, Rapha Gontijo-Lopes, Jonathan Gordon, Joost Huizinga, Shawn Jain, Roger Jiang, Łukasz Kaiser, Christina Kim, Jan Leike, Chak Li, Stephanie Lin, Ryan Lowe, Jacob Menick, Luke Metz, Pamela Mishkin, Tong Mu, Oleg Murk, Ashvin Nair, Long Ouyang, Alex Passos, Michael (Rai) Pokorny, Vitchyr Pong, Shibani Santurkar, Daniel Selsam, Sarah Shoker,, Carroll Wainwright, Matt Wiethoff, Jeff Wu, Kai Xiao, Kevin Yu, Marvin Zhang, Chong Zhang, William Zhuk, Barret Zoph

**Data infrastructure**  
Irwan Bello, Lenny Bogdonoff, Juan Felipe Cerón Uribe, Joshua Gross, Shawn Jain, Haozhun Jin, Christina Kim, Aris Konstantinidis, Teddy Lee, David Medina, Jacob Menick, Luke Metz, Ashvin Nair,Long Ouyang, Michael (Rai) Pokorny, Vitchyr Pong, John Schulman, Jonathan Ward, Jiayi Weng, Matt Wiethoff, Sarah Yoo, Kevin Yu, Wojciech Zaremba, William Zhuk, Barret Zoph

**ChatML format**  
Ilge Akkaya, Christina Kim, Chak Li, Rachel Lim, Jacob Menick, Luke Metz, Andrey Mishchenko, Vitchyr Pong, John Schulman, Carroll Wainwright, Barret Zoph

**Model safety**  
Josh Achiam, Steven Adler, Juan Felipe Cerón Uribe, Hyung Won Chung, Tyna Eloundou, Rapha Gontijo-Lopes, Shixiang Shane Gu, Johannes Heidecke, Joost Huizinga, Teddy Lee, Jan Leike, Stephanie Lin, Ryan Lowe, Todor Markov, Luke Metz, Tong Mu, Shibani Santurkar, John Schulman, Andrea Vallone, Carroll Wainwright, Jason Wei, Lilian Weng, Kai Xiao, Chong Zhang, Marvin Zhang, Barret Zoph

**Refusals  
** Juan Felipe Cerón Uribe, Tyna Eloundou, Johannes Heidecke, Joost Huizinga, Jan Leike, Stephanie Lin, Ryan Lowe, Pamela Mishkin, Tong Mu, Carroll Wainwright, Lilian Weng, Kai Xiao, Chong Zhang, Barret Zoph

**Foundational RLHF and InstructGPT work**  
Diogo Almeida, Joost Huizinga, Roger Jiang, Jan Leike, Stephanie Lin, Ryan Lowe, Pamela Mishkin, Dan Mossing, Long Ouyang, Katarina Slama, Carroll Wainwright, Jeff Wu, Kai Xiao, Marvin Zhang

**Flagship training runs**  
Greg Brockman, Liam Fedus, Johannes Heidecke, Joost Huizinga, Roger Jiang, Kyle Kosic, Luke Metz, Ashvin Nair, Jiayi Weng, Chong Zhang, Shengjia Zhao, Barret Zoph

**Code capability**  
Ilge Akkaya, Mo Bavarian, Jonathan Gordon, Shawn Jain, Haozhun Jin, Teddy Lee, Chak Li, Oleg Murk, Ashvin Nair, Vitchyr Pong, Benjamin Sokolowsky, Jerry Tworek, Matt Wiethoff, Sarah Yoo, Kevin Yu, Wojciech Zaremba, William Zhuk

## Evaluation & analysis

**Core contributors  
** Sandhini Agarwal _System Card co-lead_  
Lama Ahmad _Expert red teaming & adversarial testing program lead_  
Mo Bavarian _Capability prediction co-lead_  
Tyna Eloundou _Safety evaluations co-lead_  
Andrew Kondrich _OpenAI Evals open-sourcing co-lead_  
Gretchen Krueger _System Card co-lead_  
Michael Lampe _Privacy and PII evaluations lead_  
Pamela Mishkin _Economic impact & overreliance evaluations lead_  
Benjamin Sokolowsky _Capability prediction co-lead_  
Jack Rae _Research benchmark execution lead_  
Chelsea Voss _Eval execution lead_  
Alvin Wang _OpenAI Evals lead_  
Kai Xiao _Safety evaluations co-lead_  
Marvin Zhang _OpenAI Evals open-sourcing co-lead_

**OpenAI Evals library**  
Shixiang Shane Gu, Angela Jiang, Logan Kilpatrick, Andrew Kondrich, Pamela Mishkin, Jakub Pachocki, Ted Sanders, Jessica Shieh, Alvin Wang, Marvin Zhang

**Model-graded evaluation infrastructure  
** Liam Fedus, Rapha Gontijo-Lopes, Shixiang Shane Gu, Andrew Kondrich, Michael (Rai) Pokorny, Wojciech Zaremba, Chong Zhang, Marvin Zhang, Shengjia Zhao, Barret Zoph

**Acceleration forecasting**  
Alan Hickey, Daniel Kokotajlo, Cullen O’Keefe, Sarah Shoker

**ChatGPT evaluations**  
Juan Felipe Cerón Uribe, Hyung Won Chung, Rapha Gontijo-Lopes, Liam Fedus, Luke Metz, Michael Rai Pokorny, Jason Wei, Shengjia Zhao, Barret Zoph

**Capability evaluations**  
Sully Chen, Tyna Eloundou, Shengli Hu, Roger Jiang, Jamie Kiros, Teddy Lee, Scott Mayer McKinney, Jakub Pachocki, Alex Paino, Giambattista Parascandolo, Boris Power, Raul Puri, Jack Rae, Nick Ryder, Ted Sanders, Szymon Sidor, Benjamin Sokolowsky, Chelsea Voss, Alvin Wang, Rowan Zellers, Juntang Zhuang

**Coding evaluations**  
Ilge Akkaya, Mo Bavarian, Jonathan Gordon, Shawn Jain, Chak Li, Oleg Murk, Vitchyr Pong, Benjamin Sokolowsky, Jerry Tworek, Kevin Yu, Wojciech Zaremba

**Real-world use case evaluations**  
Andrew Kondrich, Joe Palermo, Boris Power, Ted Sanders

**Contamination investigations**  
Adrien Ecoffet, Roger Jiang, Ingmar Kanitscheider, Scott Mayer McKinney, Alex Paino, Giambattista Parascandolo, Jack Rae, Qiming Yuan

**Instruction following and API evals**  
Diogo Almeida, Carroll Wainwright, Marvin Zhang

**Novel capability discovery**  
Filipe de Avila Belbute Peres, Kevin Button, Fotis Chantzis, Mike Heaton, Wade Hickey, Xin Hu, Andrew Kondrich, Matt Knight, Andrew Mayne, Jake McNeil, Vinnie Monaco, Joe Palermo, Joel Parish, Boris Power, Bob Rotsted, Ted Sanders

**Vision evaluations**  
Shixiang Shane Gu, Shengli Hu, Jamie Kiros, Hyeonwoo Noh, Raul Puri, Rowan Zellers

**Economic impact evaluation**  
Tyna Eloundou, Sam Manning, Aalok Mehta, Pamela Mishkin

**Non-proliferation, international humanitarian law & national security red teaming**  
Sarah Shoker

**Overreliance analysis**  
Miles Brundage, Michael Lampe, Pamela Mishkin

**Privacy and PII evaluations**  
Michael Lampe, Vinnie Monaco, Ashley Pantuliano

**Safety and policy evaluations  
** Josh Achiam, Sandhini Agarwal, Lama Ahmad, Jeff Belgum, Tyna Eloundou, Johannes Heidecke, Shengli Hu, Joost Huizinga, Jamie Kiros, Gretchen Krueger, Michael Lampe, Stephanie Lin, Ryan Lowe, Todor Markov, Vinnie Monaco, Tong Mu, Raul Puri, Girish Sastry, Andrea Vallone, Carroll Wainwright, CJ Weinmann, Lilian Weng, Kai Xiao, Chong Zhang

**OpenAI adversarial testers  
** Josh Achiam, Steven Adler, Lama Ahmad, Shyamal Anadkat, Red Avila, Gabriel Bernadett-Shapiro, Anna-Luisa Brakman, Tim Brooks, Miles Brundage, Chelsea Carlson, Derek Chen, Hyung Won Chung, Jeremiah Currier, Daniel Kokotajlo, David Dohan, Adrien Ecoffet, Juston Forte, Vik Goel, Ryan Greene, Johannes Heidecke, Alan Hickey, Shengli Hu, Joost Huizinga, Janko, Tomer Kaftan, Ali Kamali, Nitish Shirish Keskar, Tabarak Khan, Hendrik Kirchner, Daniel Kokotajlo, Gretchen Krueger, Michael Lampe, Teddy Lee, Molly Lin, Ryan Lowe, Todor Markov, Jake McNeil, Pamela Mishkin, Vinnie Monaco, Daniel Mossing, Tong Mu, Oleg Murk, Cullen O’Keefe, Joe Palermo, Giambattista Parascandolo, Joel Parish, Boris Power, Alethea Power, Cameron Raymond, Francis Real, Bob Rotsted, Mario Salterelli, Sam Wolrich, Ted Sanders, Girish Sasty, Sarah Shoker, Shyamal Anadkat, Yang Song, Natalie Staudacher, Madeleine Thompson, Elizabeth Tseng, Chelsea Voss, Jason Wei, Chong Zhang

**System card & broader impacts analysis**  
Steven Adler, Sandhini Agarwal, Lama Ahmad, Janko Altenschmidt, Jeff Belgum, Gabriel Bernadett-Shapiro, Miles Brundage, Derek Chen, Tyna Eloundou, Liam Fedus, Leo Gao, Vik Goel, Johannes Heidecke, Alan Hickey, Shengli Hu, Joost Huizinga, Daniel Kokotajlo, Gretchen Krueger, Michael Lampe, Jade Leung, Stephanie Lin, Ryan Lowe, Kim Malfacini, Todor Markov, Bianca Martin, Aalok Mehta, Pamela Mishkin, Tong Mu, Richard Ngo, Cullen O’Keefe, Joel Parish, Rai Pokorny, Bob Rotsted, Girish Sastry, Sarah Shoker, Andrea Vallone, Carroll Wainwright, CJ Weinmann, Lilian Weng, Dave Willner, Kai Xiao, Chong Zhang

## Deployment

**Core contributors**  
Steven Adler _Early stage program management lead_  
Sandhini Agarwal _Launch safety lead_  
Derek Chen _Monitoring & response lead_  
Atty Eleti _GPT‑4 API co-lead_  
Joanne Jang _GPT‑4 product co-lead_  
Angela Jiang _GPT‑4 product co-lead_  
Tomer Kaftan _Inference infrastructure & deployment lead_  
Rachel Lim _GPT‑4 API co-lead_  
Kim Malfacini _Usage policy lead_  
Bianca Martin _Release program management lead_  
Evan Morikawa _Engineering lead_  
Henrique Ponde de Oliveira Pinto _Inference workflow lead_  
Heather Schmidt _GPT‑4 infrastructure management_  
Maddie Simens _Design lead  
_ Felipe Petroski Such _Inference optimization & reliability lead_  
Andrea Vallone _Detection & refusals policy lead_  
Lilian Weng _Applied research lead_  
Dave Willner _Trust & safety lead_  
Michael Wu _Inference research lead_

**Inference research**  
Paul Baltescu, Scott Gray, Yuchen He, Arvind Neelakantan, Michael Wu

**GPT‑4 API & ChatML deployment**  
Greg Brockman, Brooke Chan, Chester Cho, Atty Eleti, Rachel Lim, Andrew Peng, Michelle Pokrass, Sherwin Wu

**GPT‑4 web experience**  
Valerie Balcom, Lenny Bogdonoff, Jason Chen, Dave Cummings, Noah Deutsch, Mike Heaton, Paul McMillan, Rajeev Nayak, Joel Parish, Adam Perelman, Eric Sigler, Nick Turley, Arun Vijayvergiya, Chelsea Voss

**Inference infrastructure**  
Brooke Chan, Scott Gray, Chris Hallacy, Kenny Hsu, Tomer Kaftan, Rachel Lim, Henrique Ponde de Oliveira Pinto, Raul Puri, Heather Schmidt, Felipe Petroski Such

**Reliability engineering**  
Haiming Bao, Madelaine Boyd, Ben Chess, Damien Deville, Yufei Guo, Vishal Kuo, Ikai Lan, Michelle Pokrass, Carl Ross, David Schnurr, Jordan Sitkin, Felipe Petroski Such

**Trust & safety engineering**  
Jeff Belgum, Madelaine Boyd, Vik Goel

**Trust & safety monitoring and response**  
Janko Altenschmidt, Anna-Luisa Brakman, Derek Chen, Florencia Leoni Aleman, Molly Lin, Cameron Raymond, CJ Weinmann, Dave Willner, Samuel Wolrich

**Trust & safety policy**  
Rosie Campbell, Kim Malfacini, Andrea Vallone, Dave Willner

**Deployment compute**  
Peter Hoeschele, Evan Morikawa

**Product management**  
Jeff Harris, Joanne Jang, Angela Jiang

## Additional contributions

Sam Altman, Katie Mayer, Bob McGrew, Mira Murati, Ilya Sutskever, Peter Welinder

**Blog post & paper content  
**Sandhini Agarwal, Greg Brockman, Miles Brundage, Adrien Ecoffet, Tyna Eloundou, David Farhi, Johannes Heidecke, Shengli Hu, Joost Huizinga, Roger Jiang, Gretchen Krueger, Jan Leike, Daniel Levy, Stephanie Lin, Ryan Lowe, Tong Mu, Hyeonwoo Noh, Jakub Pachocki, Jack Rae, Kendra Rimbach, Shibani Santurkar, Szymon Sidor, Benjamin Sokolowsky, Jie Tang, Chelsea Voss, Kai Xiao, Rowan Zellers, Chong Zhang, Marvin Zhang

**Communications**  
Ruby Chen, Cory Decareaux, Thomas Degry, Steve Dowling, Niko Felix, Elie Georges, Anna Makanju, Andrew Mayne, Aalok Mehta, Elizabeth Proehl, Kendra Rimbach, Natalie Summers, Justin Jay Wang, Hannah Wong

**Compute allocation support**  
Theresa Lopez, Elizabeth Tseng

**Contracting, revenue, pricing & finance support**  
Brooke Chan, Denny Jin, Billie Jonn, Patricia Lue, Kyla Sheppard, Lauren Workman

**Launch partners & product operations**  
Filipe de Avila Belbute Peres, Brittany Carey, Simón Posada Fishman, Isabella Fulford, Teddy Lee, Yaniv Markovski, Tolly Powell, Toki Sherbakov, Jessica Shieh, Natalie Staudacher, Preston Tuggle

**Legal**  
Jake Berdine, Che Chang, Sheila Dunning, Ashley Pantuliano

**Security & privacy engineering**  
Kevin Button, Fotis Chantzis, Wade Hickey, Xin Hu, Shino Jomoto, Matt Knight, Jake McNeil, Vinnie Monaco, Joel Parish, Bob Rotsted

**System administration & on-call support  
**Morgan Grafstein, Francis Real, Mario Saltarelli

**Authorship & credit attribution  
**David Farhi

We also acknowledge and thank every OpenAI team member not explicitly mentioned above, including the amazing people on the executive assistant, finance, go to market, human resources, legal, operations and recruiting teams. From hiring everyone in the company, to making sure we have an amazing office space, to building the administrative, HR, legal, and financial structures that allow us to do our best work, everyone at OpenAI has contributed to GPT‑4.

We thank Microsoft for their partnership, especially Microsoft Azure for supporting model training with infrastructure design and management, and the Microsoft Bing team and Microsoft’s safety teams for their partnership on safe deployment.

We are grateful to our expert adversarial testers and red teamers who helped test our models at early stages of development and informed our risk assessments as well as the system card. Participation in this red teaming process is not an endorsement of the deployment plans of OpenAI or OpenAI’s policies: Steven Basart, Sophie Duba, Cèsar Ferri, Heather Frase, Gavin Hartnett, Jake J. Hecla, Dan Hendrycks, Jose Hernandez-Orallo, Alice Hunsberger, Rajiv W. Jain, Boru Gollo Jattani, Lauren Kahn, Dan Kaszeta, Sara Kingsley, Noam Kolt, Nathan Labenz, Eric Liddick, Andrew J. Lohn, Andrew MacPherson, Sam Manning, Mantas Mazeika, Anna Mills, Yael Moros, Jimin Mun, Aviv Ovadya, Roya Pakzad, Yifan Peng, Ciel Qi, Alex Rosenblatt, Paul Röttger, Maarten Sap, Wout Schellaert, George Shih, Muhammad Shoker, Melanie Subbiah, Bryan West, Andrew D. White, Anna Katariina Wisakanto, Akhila Yerukola, Lexin Zhou, Xuhui Zhou.

Contributors listed in alphabetized order.

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
