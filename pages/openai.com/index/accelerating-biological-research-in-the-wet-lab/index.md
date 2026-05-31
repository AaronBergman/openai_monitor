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

Table of contents

  * Experimental results
  * An evolutionary framework for optimizing real-world protocols
  * A novel improvement to homology-based cloning
  * Robotic system
  * The future



December 16, 2025

[Research](</news/research/>)[Publication](</research/index/publication/>)

# Measuring AI’s capability to accelerate biological research in the wet lab

GPT‑5 created novel wet lab protocol improvements, optimizing the efficiency of a molecular cloning protocol by 79x.

![Collage-style graphic with soft blue–orange gradients, a DNA assembly diagram, and bold text reading “Biology Research,” labeled under “OpenAI for Science.”](https://images.ctfassets.net/kftzwdyauwt9/7EC1SMUUh43FshgQjtNZb1/b8c5d6516d16c59225dceb1e065dd8fd/oai_forscience_wetlab_16x9.png?w=3840&q=90&fm=webp)

Loading…

Share

Accelerating scientific progress is one of the most valuable ways AI can benefit humanity. With GPT‑5, we’re beginning to see [_early signs_ ⁠](<https://openai.com/index/accelerating-science-gpt-5/>) of this—not only in helping researchers move faster through the scientific literature, but also in supporting new forms of scientific reasoning, such as surfacing unexpected connections, proposing proof strategies, or suggesting plausible mechanisms that experts can evaluate and test.

Progress to date has been most visible in fields like mathematics, theoretical physics, and theoretical computer science, where ideas can be rigorously checked without physical experiments. Biology is different: most advances depend on experimental execution, iteration, and empirical validation in the laboratory.

To help understand how frontier models behave in these settings, we worked with Red Queen Bio, a biosecurity start-up, to build an evaluation framework that tests how a model proposes, analyzes, and iterates on ideas in the wet lab. We set up a simple molecular biology experimental system and had GPT‑5 optimize a molecular cloning protocol for efficiency.

Over multiple rounds of experimentation, GPT‑5 introduced a novel mechanism that improved cloning efficiency by 79x. Cloning is a fundamental molecular biology tool. The efficiency of cloning methods is critical for creating large, complex libraries central to [_protein engineering_ ⁠(opens in a new window)](<https://www.nature.com/articles/s41592-025-02740-0>), [_genetic screens_ ⁠(opens in a new window)](<https://www.nature.com/articles/s41467-025-67256-9>), and [_organismal strain engineering_ ⁠(opens in a new window)](<https://www.nature.com/articles/s41467-019-13189-z>). This project offers a glimpse of how AI could work side-by-side with biologists to speed up research. Improving experimental methods will help human researchers move faster, reduce costs, and translate discoveries into real-world impact.

Because advances in biological reasoning carry biosecurity implications, we conducted this work in a tightly controlled setting—using a benign experimental system, limiting the scope of the task, and evaluating model behavior to inform our biosecurity risk assessments and the development of model- and system-level safeguards, as outlined in our [_Preparedness Framework_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>).

## Experimental results

In this set-up, GPT‑5 autonomously reasoned about the cloning protocol, proposed modifications, and incorporated data from new experiments to suggest more improvements. The only human intervention was having scientists carry out the modified protocol and upload experimental data.

Over the course of multiple rounds, GPT‑5 optimized the cloning procedure to improve the efficiency by over 79x—meaning that for a fixed amount of input DNA, we recovered 79x more sequence-verified clones than the baseline protocol. Most notably, it introduced two enzymes that constitute a novel mechanism: the recombinase RecA from _E. coli_ , and phage T4 gene 32 single-stranded DNA–binding protein (gp32). Working in tandem, gp32 smooths and detangles the loose DNA ends, and RecA then guides each strand to its correct match.

Initial screening and secondary experiments identified RecA-Assisted Pair-and-Finish HiFi Assembly (RAPF) and Transformation 7 (T7) as the top enzymatic and transformation protocols, respectively. Both RAPF assembly and T7 transformation independently improved cloning efficiency relative to the base HiFi reaction cloning protocol, 2.6-fold and 36-fold respectively; and combined to provide an additive improvement in performance of 79-fold. All clones were confirmed by sequencing. (Error bars: SD of n=3 independent validation experiments).

While early, these results are encouraging. The improvements are specific to our particular cloning set up used in our model system, and still require human scientists to set up and run the protocols. Even so, these experiments show that AI systems can meaningfully assist real laboratory work and may accelerate human scientists in the future.

Notably, the AI-lab loop was run with fixed prompting and no human intervention. This scaffolding helped reveal the model’s capacity to propose genuinely novel protocol changes independent of human guidance, but it also locked the system into exploration and limited its ability to maximize the performance of newly discovered ideas. A better dynamic balance between exploration and exploitation would likely yield larger gains, as both the enzymatic and transformation improvements have substantial room for refinement. We expect advances in planning and task-horizon reasoning to improve the ability of simple fixed prompts to support both discovery and subsequent optimization.

## An evolutionary framework for optimizing real-world protocols

The [_Gibson assembly_ ⁠(opens in a new window)](<https://www.nature.com/articles/nmeth.1318>) reaction has been a primary cloning method since its invention in 2009, with widespread adoption across molecular biology. Gibson assembly lets molecular biologists “glue” pieces of DNA together by briefly melting their ends so matching sequences can be sealed into a single molecule. One major appeal of Gibson assembly is its simplicity: everything happens in a single tube at one temperature. Those constraints naturally leave room for improvement. In addition, the following properties make it well-suited to evaluating AI models’ abilities to improve wet lab techniques:

  * Well-defined with controlled components, unlike a cell-based system
  * Has a clear optimization function: transformable circularized DNA made from a fixed amount of linear DNA inputs
  * Relatively fast experimental cycles (1-2 days)
  * High-dimensional design space that requires mechanistic reasoning to improve: optimal buffers, reagents, and temperatures are all interdependent



We used [_HiFi assembly_ ⁠(opens in a new window)](<https://www.neb.com/en-us/applications/cloning-and-synthetic-biology/dna-assembly-and-cloning/nebuilder-hifi-dna-assembly?srsltid=AfmBOoo1sNIc0ELdZ6rZXK8ERV18f4x8nNd7WTyKXyCWClhMmGCPxRFM>), a proprietary enzyme system developed by New England Biolabs and based on Gibson assembly, as an optimization starting point. We explored whether an AI could innovate and learn from experimental feedback once the single-step and isothermal constraints were removed, and thereby identify protocol improvements in this scenario.  
  
Specifically, we performed a two-piece cloning reaction using a gene for green fluorescent protein (GFP) and the widely used pUC19 plasmid, a standard DNA “vehicle” used to carry genes into bacteria so they can be copied. The goal was to increase the number of successful colonies.

We optimized the cloning reaction by introducing an evolutionary framework for iterating on proposals, enabling the model to learn “online” from its past experiments. In each round, GPT‑5 proposed a batch of 8-10 different reactions, with reactions pushed to later rounds if they required custom reagents the laboratory did not have readily on hand. Human scientists then carried out the reactions and measured the colony counts relative to the baseline HiFi Gibson assembly in an initial screen. The best performing data from the previous round were then fed into the next round. Importantly, the prompting was standardized with no human input beyond clarifying questions, allowing us to attribute novel mechanistic insights directly to the AI rather than human guidance. 

We retested the top eight reactions from the full optimization series using a wider range of DNA dilutions, and found that many showed smaller effects than in the initial screen; ultimately, the strongest validated candidate was a reaction from round-5 that reproduced its original performance. Many high performers fell into the ligase-polish family, which appears particularly sensitive to small variations in competent-cell state and/or post-reaction DNA handling. Because these reactions used a short HiFi step, we hypothesize that many products likely enter _E. coli_ with only one junction sealed and the other held by annealing, leaving downstream rescue to cellular repair pathways. This creates high variance and a ‘jackpot’ dynamic: even if most of the time variants of this reaction don’t outperform, a single strong outlier can carry the family into subsequent rounds. 

While we focused on optimizing the cloning reaction over rounds due to its mechanistic complexity, we in parallel optimized the transformation procedure using a single “one-shot” round where the model proposed many independent changes, and we took the top performing reaction.

Initial optimization screens of the two-step cloning workflow: enzymatic assembly and transformation. (Left) Iterative optimization of enzymatic assembly over five rounds (44 reactions total). Starting from the HiFi assembly baseline, GPT‑5 proposed 8-10 assembly protocol variants per round; data of top-performing results were incorporated into subsequent prompts. At each round, we plot the top-performing reaction so far (including previous rounds). (Right) One-shot optimization of transformation conditions testing 13 different protocols. For both optimization screens, data represents single measurements (n=1) per condition; replicated validation was performed separately for top candidates.

Using standardized prompts with no human input, GPT5 improved end-to-end cloning efficiency 79-fold, confirmed across experimental replicates.

Notably, the model proposed a new enzymatic procedure, which the model called RecA-Assisted Pair-and-Finish HiFi Assembly (RAPF-HiFi), that adds two new proteins to the reaction: the recombinase RecA from _E. coli_ , and the phage T4 gene 32 single-stranded DNA–binding protein (gp32). Further, the model made deliberate modifications to the incubation temperature and time, and the timing of enzymatic additions: it proposed adding RecA and gp32 after an initial 50°C HiFi reaction, letting these proteins work at 37°C, and then going back to 50°C to complete the assembly. Together, these new modifications boosted efficiency over 2.5-fold. It should be noted that this represents the initial performance without iterative optimization of reaction conditions and timing.

Baseline HiFiRound 1Round 2Round 3Round 4Round 5Baseline transformation protocolHiFi + T7 transformationCombined final protocol

20 uL reaction volume  
100 ng pUC19 vector, HindIII/KpnI-digested  
64.3 ng Monster GFP insert, DpnI-digested PCR amplicon  
10 μL NEBuilder 2x HiFi DNA Assembly Master Mix  
50C - 30 min; 4C hold

On the transformation side, the most effective modification proved unexpectedly simple: pelleting the cells (spinning them down in a centrifuge so they collect at the bottom of the tube), removing half of the supplied volume, and resuspending the cells before adding DNA, all at 4°C. While high-efficiency chemically competent cells are typically considered fragile, the cells tolerated concentration well and the increased molecular collisions boosted transformation efficiency substantially (>30-fold on final validation). 

## A novel improvement to homology-based cloning

![Diagram showing the steps of RecA-assisted pair-and-finish HiFi DNA assembly, with labeled stages for T5 exonuclease, GP32, RecA, polymerase, and ligase acting sequentially on DNA strands.](https://images.ctfassets.net/kftzwdyauwt9/56BLgMuLR92PZziktfGSKM/8b786abfce49fcf9430c460a848a4caf/Wet_Lab_Diagram.png?w=3840&q=90&fm=webp)

T5 exonuclease creates 3′ overhangs that gp32 stabilizes by suppressing secondary structure. RecA then invades from the 3′ ends, displacing gp32 and promoting homology search and annealing. Heating to 50 °C removes both proteins, enabling polymerase gap fill and ligation.

Gibson assembly works by giving pieces of DNA matching “sticky” ends so that they can find each other and join. The reaction uses two different enzymes (a polymerase and a ligase) to seal the joined pieces. In RAPF-HiFi, two proteins were introduced to make the matching step work better. The first, gp32, acts like a comb that smooths and untangles the loose DNA ends. The second, RecA, acts like a guide that searches for the correct partner for each strand and pulls the matching pieces together. Higher temperature causes both helpers to fall off the DNA, allowing the normal Gibson enzymes to complete the reaction.

In summary, we hypothesize that the improved performance is mediated via the following mechanism:

  * Gp32 coats non-annealed single-stranded DNA (ssDNA) tails, removing secondary structure
  * RecA, normally inhibited by structure, invades from the 3’ and displaces the gp32 filament
  * RecA mediates a [_ssDNA:ssDNA homology search_ ⁠(opens in a new window)](<https://www.pnas.org/doi/10.1073/pnas.82.2.297>), driving annealing
  * A return to 50°C displaces both the recA and the gp32 filaments, allowing polymerase and ligase to complete the reaction.



To test whether the novel enzymes were functional, and to rule out that the performance improvement is driven solely by changes in thermal steps or buffers, we tested the performance of RAPF-HiFi without RecA, and without both RecA and gp32. The performance of both reactions was reduced relative to RAPF-HiFi, suggesting that both proteins are necessary for the mechanism of action of RAPF-HiFi.

To test the underlying mechanism, we separate out the two new enzymes in the reaction: RecA and gp32. We show that either of these alone reduces the efficiency relative to the HiFi baseline. Together, they outperform the baseline with a 2.6x efficiency gain. (Error bars: SD of n=3 independent experiments)

The development RAPF-HiFi suggests that GPT‑5 is capable of complex, multi-dimensional reasoning:

  * [_RecA is inhibited by DNA structure_ ⁠(opens in a new window)](<https://www.pnas.org/doi/10.1073/pnas.151242898>), and it’s notable that the model introduced two synergistic modifications at once: add RecA, and complemented it with gp32 to remove DNA secondary structure.
  * The natural partner to _E. coli_ RecA is _E. coli_ single-stranded binding protein (SSB). SSB performs a similar role to gp32 during genome replication, recombination, and repair. However, _E. coli_ SSB does not spontaneously fall off the DNA fast enough for RecA filament growth, with the [_RecFOR complex promoting RecA nucleation at SSB filament in vivo_ ⁠(opens in a new window)](<https://www.sciencedirect.com/science/article/pii/S1097276503001886>). SSB binds as a stable tetramer with [_extremely slow off-rates_ ⁠(opens in a new window)](<https://pubs.acs.org/doi/10.1021/bi020122z>). By contrast, gp32 filament is [_more dynamic_ ⁠(opens in a new window)](<https://www.sciencedirect.com/science/article/pii/S0022283624001396>), allowing for RecA displacement. 



To our knowledge, RecA and gp32 have not been functionally co-used in molecular biology methods. As with many novel molecular biology techniques, the underlying biochemical activities were already studied, but their use as a practical, generalizable method constitutes the advance.

For example, the interaction of RecA and gp32 has been studied in mechanistic in vitro reconstitution assays: in studies of D loop formation, [_gp32 was shown_ ⁠(opens in a new window)](<https://www.pnas.org/doi/10.1073/pnas.77.5.2606?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub++0pubmed>) to be capable of enhancing RecA activity. Gp32 has been used in conjunction with its natural T4 recombinase partner UvsX and recombinase loading factor uvsY in [_recombinase polymerase amplification (RPA_ ⁠(opens in a new window)](<https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0040204>)). Although an [_RPA patent specification states_ ⁠(opens in a new window)](<https://patents.google.com/patent/US20090029421A1/en>) that effective RPA reactions have been demonstrated using E. coli RecA in a heterologous system with a compromised (i.e., engineered, non–wild-type) gp32 protein, this assertion appears only as a tangent in some patent disclosures and, to our knowledge, has not been supported by published data or adopted as a robust RecA-based RPA system. One cloning method called [_SLiCE_ ⁠(opens in a new window)](<https://academic.oup.com/nar/article/40/8/e55/2411705>) uses a whole cell extract from _E. coli_ containing the λ Red recombination system, where Red beta may perform dual roles as both a DNA-binding protein and recombinase (though we explicitly prohibited the use of cell extracts in our prompt). In a different application, [_Ferrin & Camerini-Otero_⁠(opens in a new window)](<https://www.pnas.org/doi/10.1073/pnas.95.5.2152>) used RecA alone to selectively capture DNA molecules based on matching sequences. Separately, g[ _p32 has been used as an additive_ ⁠(opens in a new window)](<https://academic.oup.com/nar/article/18/4/1079/1112638>) in a DNA amplification process called PCR to reduce secondary structure. [_NABSA amplification was shown_ ⁠(opens in a new window)](<https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0265391>) to be enhanced by both RecA and gp32, though each could enhance the reaction separately and no synergy was identified. More broadly, reported improvements to the basic Gibson-style DNA assembly reactions have been scarce, with the most notable example being a heat-stable DNA-binding protein (ET SSB) that [_improves assembly efficiency by approximately 2.5-fold_ ⁠(opens in a new window)](<https://www.biorxiv.org/content/10.1101/2020.06.14.150979v1>). 

For most applications, we do not expect RAPF-HiFi to compete with the simplicity and robustness of HiFi/Gibson cloning. However, the emergence of a mechanistically distinct assembly pathway is noteworthy: GPT‑5 arrived at a solution that incorporates an unfamiliar combination of recombination proteins and reaction dynamics. The underlying mechanism may prove modular, providing components that can be repurposed or recombined in other molecular workflows. We are also continuing to explore improvements to RAPF-HiFi. Reaction temperatures and step durations can be tuned to balance RecA and gp32 activity against exonuclease over-digestion, and the amounts of both proteins remain to be optimized. GPT‑5 has also proposed a hyperactive RecA variant, which we are currently purifying.

With respect to the transformation protocol, the successful optimization conditions spanned a range of additives and thermal perturbations intended to enhance the heat-shock efficiency of commercial [_10-beta competent cells_ ⁠(opens in a new window)](<https://www.neb.com/en-us/products/c3019-neb-10-beta-competent-e-coli-high-efficiency?srsltid=AfmBOorcs_qhj9EZFQ4g-gGg2ZDAOkN4GF8JZijwvEEn3JIJFcYt_N3y>). Of the 13 AI-generated one-shot transformations tested, the most effective modification, Transformation 7 (T7), pelleted the cells, removing half of the supplied volume, and resuspending the cells before adding DNA, all at 4°C. High-efficiency chemically competent cells are typically considered fragile, and such handling steps are generally avoided. Nonetheless, the cells tolerated concentration well. The combined effects of increased DNA exposure per cell and less inhibitory buffer leading to a sharper heat-shock yielded a substantial increase in transformation efficiency (>30-fold). 

This transformation protocol is novel, although a conceptually [_similar approach_ ⁠(opens in a new window)](<https://portlandpress.com/bioscirep/article/33/6/e00086/55976/A-comparison-and-optimization-of-methods-and>) where the cells are concentrated at an earlier step has been reported. Notably, the method developed here by GPT‑5 is compatible with off-the-shelf chemically competent cells, eliminating the need for in-house cell preparation, while exceeding the similar approach’s reported efficiency gains on comparable cell strains.

## Robotic system

To increase the throughput of this model experimental system, Robot on Rails and Red Queen Bio collaborated to build a robotic system that takes in a natural language cloning protocol and executes it in the wet lab.

The system combines three components: 1) a human-to-robot LLM that converts plain English into the robot’s actions; 2) a vision system that identifies and localizes labware in real time; and 3) a robotic path planner that determines how to carry out each action safely and accurately. The result is a flexible, generalized lab robot that was further optimized for variants of the Gibson cloning protocol.

We tested whether the autonomous robot could execute a complete cloning experiment by running two protocols simultaneously: the standard HiFi method and R8, the top-performing AI-modified protocol from the first optimization round.   
  
We compared the robot’s work to human-performed experiments at each step. The robot successfully handled the transformation process, which required diverse physical operations: transferring and mixing liquids, moving sample tubes, applying controlled heat to cells, and spreading cells onto growth plates. When compared directly with human-performed transformations, the robot generated similar quality data with equivalent improvements over baseline, showing early potential for automating and accelerating biological experiment optimization.

While the fold-changes between the robot and human experiments were similar, absolute colony counts from the robot were approximately ten-fold lower than manual execution, indicating areas for improvement such as liquid handling precision, temperature control calibration, and replicating the nuances of manual cell handling techniques.

Both the standard HiFi method (baseline) and the improved R8 method were executed by human researchers and the autonomous robot, with transformation efficiencies normalized to respective HiFi baseline controls (set to 1.0). Human-executed R8 showed 2.39-fold improvement; robot-executed R8 achieved 2.13-fold improvement (89% of human performance), demonstrating comparable protocol ranking despite lower absolute yields.

## The future

We believe that these experiments offer a snapshot of what future AI-accelerated science will look like: models continually learning and interacting with the real world. Although our experiments excluded human intervention to purely measure model capabilities, we’re particularly excited about [_AI helping human scientists_ ⁠](<https://openai.com/science/>) design experiments and contribute to research breakthroughs.

  
As we work to accelerate scientific progress safely and responsibly, we also seek to evaluate and reduce risks, particularly those related to biosecurity. These evaluations results show that models can reason in the wet lab to improve protocols, and may have implications for biosecurity as described in our [_Preparedness Framework_ ⁠(opens in a new window)](<https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>). We are [_committed to building_ ⁠](<https://openai.com/index/preparing-for-future-ai-capabilities-in-biology/>) necessary and nuanced safeguards at a model and system level to reduce these risks, as well as develop evaluations to track current levels.

  * [Framework](</news/?tags=framework>)
  * [GPT](</news/?tags=gpt>)
  * [2025](</news/?tags=2025>)



## Authors

Nikolai Eroshenko, Miles Wang, Rachel Smith, Liliana Abramson, Tejal Patwardhan, Kemo Jammeh, Chase Olle, Azadeh Samadian, Nitin Mahadeo

## Keep reading

[View all](</news/>)

![1x1](https://images.ctfassets.net/kftzwdyauwt9/6ui4uYfTTbR4xbiFRcqEfo/81d973f14bea720820f692271f6c6834/square.png?w=3840&q=90&fm=webp)

[Strengthening societal resilience with Rosalind BiodefenseProductMay 29, 2026](</index/strengthening-societal-resilience-with-rosalind-biodefense/>)

![Geometry > ArtCard > Polynomial Construction](https://images.ctfassets.net/kftzwdyauwt9/6PqehRMmS1oVuin6e3VWYq/b96f1c7b5a2ac2c08a887591b8486ed3/ArtCard-Polynomial-Construction.png?w=3840&q=90&fm=webp)

[An OpenAI model has disproved a central conjecture in discrete geometryResearchMay 20, 2026](</index/model-disproves-discrete-geometry-conjecture/>)

![1 1](https://images.ctfassets.net/kftzwdyauwt9/6eaq9qftNBJJjryJnZGVRj/991b778132f449626fb9c768001f9009/1_1.png?w=3840&q=90&fm=webp)

[What Parameter Golf taught usResearchMay 12, 2026](</index/what-parameter-golf-taught-us/>)

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
