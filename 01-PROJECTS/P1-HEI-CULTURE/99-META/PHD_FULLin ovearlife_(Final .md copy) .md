% Title and author information  
% Don't delete. Keep blank if it is not used  
\\mytitle{Understanding Higher Education Institutional Cybersecurity Readiness Through Individual Mental Models of Privacy and Organisational Culture}  
\\mysubtitle{}  
\\author{Md Yeahia Bhuiyan}  
\\myqualification{Doctor of Philosophy in Information Technology} % Change this to your qualification  
\\myinstitution{Federation University Australia}  
\\myschool{Institute of Innovation, Science and Sustainability} % Change this to your school or center or institute  
% \\mysubmissiondate{\\today} % Change this to the submission date  
\\mysubmissiondate{30$^\\text{th}$ March 2026}  
\\affiliationlogo{Figures/FedUni.png} % Change this to the path of your logo file  
\\principalsupervisor{Dr Selena (Sally) Firmin}  
\\associatesupervisor{Dr Taiwo Oseni}

\\abstractcontent{Higher education institutions face escalating cybersecurity risks due to complex organisational structures and large volumes of sensitive information. This study investigated how privacy-related mental models and organisational cultural conditions shape cybersecurity readiness in an Australian regional university. Cybersecurity readiness is an institution's behavioural, cultural, and governance capacity to anticipate and respond to cyber risk. Despite growing technological defences and policy-based controls, limited research has examined how individual interpretations and cultural dynamics jointly influence cybersecurity readiness in higher education. Understanding these influences is critical, as weaknesses in readiness expose institutions to operational disruption, reputational harm, regulatory consequences, and long-term loss of trust.

An explanatory single case study design was adopted across three sequential phases. Semi-structured interviews were conducted with university students, academic staff, senior leaders, and cybersecurity experts. Template analysis guided the identification of individual and organisational factors of readiness, expert validations were used to refine and confirm the practical applicability of the findings. They also deepened Schein's organisational culture model by identifying cybersecurity-related assumptions embedded in daily practice. 

Mental model characteristics emerged from the data. Mental models shape how individuals interpret privacy, assess risk, understand responsibility, and respond to security expectations.  The findings revealed a critical link between individual interpretive patterns and cultural assumptions, leadership practices, and governance processes. Artefacts developed as part of this study include an integrated conceptual framework and a practical cybersecurity readiness checklist for institutional assessment. 

% The findings extend the Protection Motivation Theory by illustrating how cultural conditions influence risk appraisal and protective action in higher education. They also deepened Schein's organisational culture model by identifying cybersecurity-related assumptions embedded in daily practice. The study provides a structured and sustainable framework for strengthening cybersecurity readiness in higher education institutions.  
}

\\chapter{Introduction}  
\\label{chapter:c1}

\\section{Introduction}  
\\label{sec:1.1}

In 2025, global leaders defined cyber risk as the likelihood and impact of unauthorised access, disruption, or data compromise among the top five threats to economic and national stability, as the sophistication of attacks continues to outpace institutional defences\~\\citep{HFK2025, WEF2025}. Organisations in all sectors have faced increasing cybersecurity threats as rapid technological growth expanded digital boundaries and introduced new vulnerabilities\~\\citep{Aldaajeh2022}. As these risks intensify, the ability of institutions to prepare for and manage cyber threats has become critical. Institutional readiness refers to the coordinated ability to anticipate, withstand, respond to, and recover from cyber incidents across people, processes, and technology\~\\citep{Sandi2025}. Closely related to this, cybersecurity resilience emphasises the capacity to sustain operations and restore critical functions during and after disruption. It requires the development of a proactive mindset through sustained understanding and upskilling beyond technological controls\~\\citep{Sandi2025}. Closely related to this, cybersecurity resilience emphasise to the ability to maintain and restore critical functions during and after disruption. This challenges has become more complex under evolving work arrangements, where people increasingly rely on hybrid and remote working environments. The WEF \\citeyearpar{WEF2025} report noted that hybrid work models combine on-site and remote arrangements, thereby expanding the digital attack landscape \\citep{WEF2025}.

Organisations face increasing pressure to improve cyber awareness, both internally among staff and externally to build public trust \~\\citep{alshaikh2020}. Developing strong cybersecurity attitudes has become important for organisations to maintain operational reliability and protect institutional reputation. Higher education institutions (HEIs) are particularly vulnerable, given their open-access systems, diverse user bases, and complex governance\~\\citep{lallie2025, Morrow2024}. A significant incident occurred at Deakin University in Victoria, Australia, resulting in a serious breach that affected the records of approximately 47,000 current and former students. During the same event, 10,000 students were targeted by a smishing attack that sent misleading text messages\~\\citep {Crozier2022, Paganini2022}. \\textit{Smishing}, a form of cybercrime that uses persuasive text messages to extract sensitive information\~\\citep{Paganini2022}, has been found to exploit institutional communication trust within university environments\~\\citep{Morrow2024}. The Deakin incident, which originated from stolen employee login credentials, illustrates the systemic risks posed by simple access failures in the HEI environment\~\\citep{Crozier2022}.

% \\textbf{Why Higher Education?}   
These incidents reflected a wider global trend. In July 2021, Australia recorded more than 3,900 attacks in a single month, representing a 17\\% increase from the previous year\~\\citep{ACSM2021} (see Figure \\ref{fig:1.1}). Another report identified education as the most attacked global sector. In January 2026, organisations in this sector faced approximately 4,364 cyber-attacks per week, exceeding the government (2,759) and telecommunications (2,647) sectors\~\\citep{CPR2026} (see Figure \\ref{fig:1.2}). This trend reinforced the urgent need for reliable institutional defences in the higher education sector.

The 2025 Global Outlook \~\\citep{WEF2025} highlighted the HEI sector's vulnerability to threats such as phishing, credential theft, and ransomware. These weaknesses often stemmed from a decentralised IT infrastructure, inadequate security measures, and overstretched cybersecurity teams \~\\citep{WEF2025}. India, Italy, Israel, Australia, and Turkey were among the most targeted nations, placing HEIs under heightened scrutiny. Figures 1.1 and 1.2 underscore the sector's growing vulnerability and the urgent need to establish rigorous cybersecurity frameworks. Effective cybersecurity depended not only on technical tools but also on how individuals perceived risk and enacted protective behaviour\~\\citep{Aldaajeh2022}.

 \\begin{figure}\[\!ht\] %\[H\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Average weekly Attacks per Organisation in Education\]{%  
    \\textbf{Figure 1.1}\\\\\[1.2em\]  
    \\textit{Average weekly Attacks per Organisation in Education}  
    }  
    \\label{fig:1.1}  
      
    % Average weekly Attacks per Organisation in Education)  
    % \\addcontentsline{lof}{figure}{1.1 \\hspace{0.18cm} Average weekly Attacks per Organisation in Education}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c1/C1.1.png}  
      
    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
        \\textit{\\\\Note.} Image From Australian Cybersecurity Magazine, By\~\\citet{ACSM2021}, Image from (https://australiancybersecuritymagazine.com.au/wp-content/uploads/2021/08/chat-table2.jpg). In the public domain.  
    \\end{minipage}  
\\end{figure}

Recent cybersecurity frameworks are based on formal modelling and cognitive- behavioural metrics \\citep{Houser2025}. These frameworks formalise mental model constructs for cybersecurity tasks. \\textit{Mental models}, conceptualised as developing understanding, enabled individuals to interpret systems, events, and risks\~\\citep{Saucier2025}. Originally formalised by Rouse and Morris (1986), mental models were later recognised as critical cognitive structures for managing complex technological systems and cybersecurity risk\~\\citep{Houser2025}. These modern frameworks specified how users evaluated threats and selected actions under risk conditions\~\\citep{Espinosa2023, Houser2025}. Rouse and Morris' \\citep{Rouse1986} seminal work on mental models demonstrates the complexities of these systems. An individual's mental model shaped whether institutional policies supported or undermined effective cybersecurity behaviour\~\\citep{Aldaajeh2022, LaMere2020, Saucier2025}.

 

 

The Australian Signals Directorate's (ASD) Annual Cyber Threat Report 2024-2025 stated that the Australian Cyber Security Centre responded to over 1,200 incidents (an 11\\% increase) and received 84,700 cybercrime reports; one every six minutes \\citep{ASD2025}. Critical infrastructure accounted for 13\\% of incidents, mainly from scanning, reconnaissance, denial-of-service, and phishing\~\\citep{ASD2025}. Figures \\ref{fig:1.1} and \\ref{fig:1.2} illustrated the increasing vulnerability of the education sector and the need for strengthened cybersecurity governance. Even the most advanced technology cannot compensate for weak cultural foundations.

 

\\begin{figure}\[\!ht\] %\[H\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Global average of weekly attacks per industry 2025 vs 2026\]{%  
    \\textbf{Figure 1.2}\\\\\[1.2em\]  
    \\textit{Global average of weekly attacks per industry 2025 vs 2026}  
    }  
    \\label{fig:1.2}  
      
    % Average weekly Attacks per Organisation in Education)  
    % \\addcontentsline{lof}{figure}{1.2 \\hspace{0.18cm} Global average of weekly attacks per industry 2025 vs 2026}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c1/C1.2.png}  
      
    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
        \\textit{\\\\Note.} Image From Check Point Research, By\~\\cite{CPR2026}, (https://blog.checkpoint.com/wp-content/uploads/2026/02/jan26-monthly-stats-1.png) In the public domain.  
    \\end{minipage}  
\\end{figure}

   
 

Figure \\ref{fig:1.2} shows that the education sector is a primary target for cybercriminals, enduring the highest volume of attacks globally. Check Point Research highlights a 12\\% year-on-year increase in education sector attacks from January 2025 to January 2026\~\\citep{CPR2025, CPR2026}. This persistent rise in the attack rate impacts universities, schools, and educational services, primarily because they are targeted for the collection of sensitive personal information. This trend underscores the critical need for enhanced cybersecurity measures to protect students, faculty, and institutional data.

Human factors were consistently implicated in breach pathways, which means technology alone was insufficient without behavioural alignment\~\\citep{alshaikh2020, khadka2025}. Many existing studies focused predominantly on technological solutions, and offered limited insight into human behaviour within HEI contexts\~\\citep{Cheng2022}. A persistent gap remains in understanding how employees and students interpreted cybersecurity expectations and how those beliefs shaped behaviour. Mental models were essential for making sense of cybersecurity actions in these environments\~\\citep{Xie2025}. As cognitive shortcuts, they influenced compliance, judgement, trust, and behavioural response during critical incidents. By exploring how mental models operate within HEIs, this study addresses an important gap at the intersection of psychology, education, and cybersecurity strategy \~\\citep{Cheng2022, Morrow2024, Tolsdorf2020}.

\\section{Background of the Study}  
\\label{sec:1.2}

The intersection of cybersecurity and organisational culture within higher education institutions (HEIs) underpins this field of inquiry. This study investigated how employees' privacy-related mental models interact with organisational culture to shape the institutional cybersecurity posture. It draws on Schein's model of organisational culture and Protection Motivation Theory (PMT) to examine how individual beliefs, shared values, and embedded assumptions influence behaviour and readiness in institutional settings\~\\citep{Georgiadou2022, Rogers1975, Rogers1983, Schein2017}. Recent evidence has positioned cybersecurity culture as a socio-technical capability that requires norms, leadership, and continuous learning alongside technical controls\~\\citep{mou2022, Uchendu2021}.

Cybersecurity resilience is critical for HEIs as attacks grow in sophistication and volume. In early 2026, the education sector emerged as the most attacked sector globally, with organisations experiencing more than double the global average of 2,090 cyber-attacks per organisation per week (see Figure \\ref{fig:1.2})\~\\citep{CPR2026}. Technical measures alone are not enough; the results also depend on human factors and organisational learning\~\\citep{Marshall2024, Prummer2025, Sutton2025}. Australia remains the most frequently targeted countries, with phishing, ransomware, and identity theft prominent\~\\citep{Morrow2024, WEF2025}. Human factors and organisational learning strongly shaped these attacks, and compliance varied by task; therefore, a purely technical emphasis proved insufficient in higher education institutions\~\\citep {Cheng2022, Datta2024, Patterson2023, Patterson2024, ulven2021}. Recent studies attribute a large share of incidents to human error, including phishing and policy non-adherence, reinforcing the need to integrate behavioural and cultural factors into HEI cybersecurity planning\~\\citep{Alsharida2023, Georgiadou2022, Sharma2022, Uchendu2021}.

Cybersecurity education has been widely recognised to provide an essential foundation for organisational resilience. However, many awareness programmes do not consider how personal beliefs connect with workplace systems and expectations. Recent reviews of behavioural training show that participants often gain knowledge but demonstrate only a limited or short-lived improvement in secure behaviour\~\\citep{Marshall2024, Prummer2025}. Within higher education, translating policy into consistent daily practice remains inconsistent in everyday behaviour, highlighting the importance of culture-sensitive approaches\~\\citep{Georgiadou2022, Yusif2023}. Several current strategies overlook the relationship between employees and their institutions, including the influence of local culture on employee attitudes and actions. As a consequence, organisational frameworks linking individual accountability with institutional readiness remain underdeveloped.

Recent empirical advances reaffirm that organisational culture critically shapes not only the adoption of cybersecurity policies, but also employee day-to-day behaviours\~\\citep{alshaikh2020, Georgiadou2022}. Several studies identified foundational perspectives on cybersecurity culture and behaviour\~\\citep{Georgiadou2022, Lie2021, Ramos2022, Sabbagh2012, Tolsdorf2020}. Sutton and Tompson\~\\citep{Sutton2025} proposed a comprehensive framework that demonstrates that alignment between cultural values and individual action is a central determinant of both compliance and resilience in cyber defence programmes. Similarly, Kannelønning and Katsikas\~\\citeyearpar{Kannelonning2023} systematically reviewed the literature and confirmed that organisational norms and peer influence exert significant predictive power over secure behaviour, with culture-driven interventions outperforming purely technical approaches. These findings highlight the need to incorporate behavioural and cultural considerations into institutional security strategies to maintain protection practices over time.

\~\\citet{Tolsdorf2020} introduced the ‘believing employee mental model'. This model identified office workers who trust their employer's data handling practices without critically assessing privacy risks. However, their research did not investigate how privacy perceptions varied between organisational roles or how institutional pressures moderated these attitudes. Recent evidence reviews show that many security-awareness designs are pedagogically varied, yet rarely evaluate sustained behavioural change, with most studies measuring short-term knowledge or click-through outcomes\~\\citep{Marshall2024, Prummer2025}. Similarly, \~\\citet{Lie2021} argued that employee behaviour is often neglected in organisational security strategies, despite its centrality to overall resilience. Cybersecurity culture comprises shared values and everyday behaviours that embed security within routine work beyond compliance requirements\~\\citep{alshaikh2020, DaVeiga2020, Georgiadou2022, Uchendu2021}. Recent HEI case analyses reinforce these gaps and advocate comprehensive programmes that integrate governance, culture, and training\~\\citep{Ramos2022}.

The importance of privacy-related behaviour zones has been further illustrated by \~\\citet{Bernstein2012}, who warned that without a sense of personal agency, even advanced security systems remain vulnerable. Although influential, this study predates contemporary debates on data ethics. Recent peer-reviewed work linked privacy to risk assessment and cybersecurity decision-making in digital workplace contexts\~\\citep{Fenech2024, khadka2025}. \\citet{Bernstein2012} argued that excessive surveillance or control could lead employees to adopt evasive behaviour, thus reducing transparency. Understanding how privacy mindsets influence accountability, data-sharing, and adherence to security expectations is essential to develop a robust cybersecurity culture\~\\citep{Bernstein2012, Tolsdorf2020}. Studies link optimism bias and everyday balances to reduced protective action, supporting a behavioural focus\~\\citep{Datta2024, Fatoki2024, Marshall2024}. Peer-reviewed studies document security or advice fatigue, where generic or repetitive guidance reduces engagement and can increase risky behaviour; programmes must be customised and usable\~\\citep{Bhana2023}.

Ethical and cultural factors have also been explored in academic settings. Recent HEI-focused work maps security-culture dimensions such as ethics, accountability, and participatory governance, but often stops short of linking these dimensions to observed behavioural change\~\\citep{Albinali2025, Georgiadou2022}. Subsequent cross-disciplinary studies show that values-driven leadership and organisational fairness strengthen compliance and engagement\~\\citep{Bhana2023, Burris2024, Fenech2024}. 

In contrast,\~\\citet{alshaikh2020} and \~\\citet{Alshaikh2021Journal} demonstrated that cybersecurity culture must evolve beyond technical enforcement to include shared norms and internalised beliefs. The synthesis work also connects culture to behaviour change and calls for evaluable interventions informed by theory\~\\citep{Sutton2025}. However, this literature has offered limited validated frameworks explaining how organisational culture shapes, or is shaped by, employees' mental models of privacy\~\\citep{Georgiadou2022, Lie2021}. Holistically, these findings support the claim that ethics and values influence security decisions. However, HEI-specific frameworks that connect culture with privacy-related mental models remain scarce\~\\citep{Georgiadou2022, Uchendu2021}.

These gaps indicate a need for research to integrate individual attitudes and institutional readiness\~\\citep{Albinali2025, Aldaajeh2022}. This study addresses this need by examining how privacy mindsets interact with organisational assumptions, leadership signals, and institutional expectations. By developing a human-centred understanding of cybersecurity in HEIs, the study contributes to discussions on resilience, behavioural design, and cultural transformation. 

\\section{Problem Statement }  
\\label{sec:1.3}

Technical controls like firewalls and access management underpin institutional defences, yet human noncompliance and academic openness routinely undermine them in higher education\~\\citep{Cheng2022, Sandi2025}. Culture, governance, and behaviour shape readiness beyond technology\~\\citep{Albinali2025, DaVeiga2020, Georgiadou2022, Sutton2025, Uchendu2021}. Recent research demonstrates that sustained cybersecurity resilience emerges only when organisational values align with everyday employee behaviour, translating abstract policy into routine practice\~\\citep{Kannelonning2023, Sutton2025}. This problem statement provides five interrelated arguments that outline why this research is important and necessary.

\\textit{Firstly, there is a limited understanding of how employees interpret their responsibility to organisational cybersecurity readiness}. Understanding and strengthening readiness for these attacks is essential\~\\citep{Georgiadou2022,alshaikh2020}. Employee perceptions and interpretations shape protective behaviour and cybersecurity readiness. A systematic review by \~\\citet{Kannelonning2023}, based on twenty-six empirical studies, found that organisational norms and peer dynamics are stronger predictors of positive action than individual awareness alone. Perceptions and interpretations shape judgements of severity, efficacy, and effort that underpin security choices\~\\citep{Fatoki2024, mou2022}. Impact can also influence decisions, since perceived risk often reflects feelings rather than probabilities in cyber contexts\~\\citep{Datta2024}. In practice, individuals often ignore system warnings, reuse weak passwords, or delay updates. When perceptions fail to link risk with personal consequences, cybersecurity readiness is weakened. Experimental evidence also linked mental-model differences to variation in cybersecurity awareness and behavioural action\~\\citep{Xie2025}. Mapping these reasoning frames is therefore essential for designing interventions that produce measurable and sustained improvements in security behaviour.

\\textit{Secondly, cybersecurity is not just about dealing with the technical aspects of an attack}. Although human error drives most cybersecurity incidents, technology-focused literature neglects behavioural and cultural guidance essential for higher education readiness \~\\citep{Cheng2022}. There is a need to understand human and cultural influences, as human error drives most cybersecurity incidents while technology-focused literature neglects essential behavioural guidance for higher education readiness\~\\citep{ulven2021, lallie2025}. Prior research also associates employee understanding of fairness and feasibility with policy adherence\~\\citep{Alraja2023, Bhana2023}. Integrating behaviourally grounded governance is therefore essential to maintain dependable cybersecurity readiness in decentralised environments\~\\citep{Cheng2022, Georgiadou2022, Sutton2025, ulven2021}. \\citet{Sutton2025} found that focusing solely on documentation or once-off training results in superficial improvement unless policies are embedded culturally and operationally. 

\\textit{Thirdly, little is known about how diverse user groups within universities, including students, academic staff, professional staff, researchers, contractors, and external partners, interpret cybersecurity responsibilities} \\citep{ulven2021, lallie2025}. This gap is significant because HEIs comprise diverse user groups with varying roles, expectations, and levels of accountability. This necessitates in-depth investigation. Staff discretion over work practices limits centralised enforcement, making peer leadership more influential than management directives \~\\citep{Kannelonning2023, Yusif2023}. Frequent device changes, varying user permissions, and intermittent remote work compound this complexity. Recent sector studies note inconsistent onboarding and access control, and constant exposure to phishing and social engineering in HEIs\~\\citep{Fouad2021, Georgiadou2022, lallie2025, Morrow2024}. In this context, cultural resilience refers specifically to organisational culture, including shared norms, leadership practices, and informal expectations that shape cybersecurity responsibility\~\\citep{DaVeiga2020, Schein2017}. Within decentralised academic environments, these cultural dynamics influence whether formal controls are reinforced or informally resisted in everyday practice\~\\citep{Georgiadou2022, ulven2021}. These findings indicate that readiness depended as much on organisational cultural resilience as on technical defence.

 % In contrast, successful organisations reinforce alignment through continuous onboarding, visible leadership signals, and incentive systems that bridge the gap between written rules and lived reality\~\\citep{Albinali2025}.%

\\textit{Fourthly, training improves knowledge but rarely sustained behaviour without reinforcement and contextual design.} Security awareness programmes improve conceptual knowledge but often fail to sustain behavioural change\~\\citep{Prummer2025}. Meta-analytic reviews show that employees recall password rules but revert to insecure habits unless reinforcement is ongoing\~\\citep{alshaikh2020, Prummer2025}. Newer studies in higher education settings show stronger results when cybersecurity training is contextualised and reinforced through immediate feedback, peer modelling, and visible leadership involvement\~\\citep{Albinali2025, Cheng2022, Marshall2024}. Research further indicates that task specificity matters: a programme that improves data-handling practice may not automatically improve device-security behaviour\~\\citep{Datta2024, Prummer2025}. Generic annual awareness modules often yielded diminishing returns and, in some cases, encouraged complacency\~\\citep{Alshaikh2021Journal, Bhana2023, Marshall2024}. By contrast, modular, role-based and continuously evaluated programmes produced more durable behavioural improvements and better embedded security practices across organisations\~\\citep{alshaikh2020, Hillman2023, Singh2024}. 

\\textit{Fifth, organisational learning from incidents is inconsistent, justifying embedded feedback procedures within governance.} Although reported incidents are rising, post-incident learning is often episodic and fragmented\~\\citep{DaVeiga2022, Patterson2023, Patterson2024}. Many organisations document events, but lack systematic procedures for cross-unit reflection or policy revision once operations stabilise\~\\citep{Ahmad2019, Alshaikh2021Journal, Patterson2023, Patterson2024}. Reviews and corrective follow-ups are frequently deferred, eroding institutional memory and increasing the risk of recurrence. Emerging best practice integrates structured after-action reviews and formal lesson-closure mechanisms into governance cycles, converting reactive responses into sustained organisational learning. This collective learning capacity, the ability to translate incidents into sustained organisational improvement, directly shapes cybersecurity readiness and long-term resilience\~\\citep{DaVeiga2022, Patterson2023, Patterson2024}.

Consequently, this study examined how mental models related to employee privacy interacted with organisational culture to shape cybersecurity readiness. By situating behaviour within governance and culture, the research focused on mechanisms that translate written policy into reliable practice\~\\citep{DaVeiga2020, Sutton2025, Uchendu2021}. By examining both personal and cultural dimensions, the study contributes to a deeper understanding of human factors in cybersecurity resilience.

\\section{Purpose of the Study}  
\\label{sec:1.4}  
This qualitative case study investigated how individual employees' mental models of privacy interacted with organisational culture to influence cybersecurity readiness in an Australian higher education institution  (HEI)\~\\citep{Albinali2025, Tolsdorf2020, ulven2021}. Protection Motivation Theory (PMT) provided an analytical lens to understand how staff, faculty, and students perceived privacy-related risks and translated those perceptions into protective cybersecurity behaviours\~\\citep{mou2022}. Concurrently, Edgar Schein's model of organisational culture supported exploration of how institutional assumptions, norms, and leadership shaped shared security practices within the organisational environment\~\\citep{Schein2017, Schein2019}. 

The purpose of the study was to develop a conceptual framework explaining how individual privacy beliefs and organisational culture jointly contributed to cybersecurity preparedness. By analysing this interplay, the research identified strategies to improve institutional readiness by better aligning personal privacy values with organisational cybersecurity norms. This was significant because many global education organisations experienced cyber incidents in January 2026\~\\citep{CPR2026}, with behavioural and cultural weaknesses that contributed significantly to institutional risk exposure\~\\citep{Morrow2024, Sutton2025, WEF2025}.  

Empirical data was gathered through semi-structured interviews with academic employees, professional staff, students, and cybersecurity specialists at a regional Australian university. The interview transcripts were analysed using NVivo-supported template analysis, which allowed systematic and transparent interpretation of themes at the individual and institutional levels\~\\citep{Brooks2015, Dejonckheere2019, Kallio2016, King2017, Zamawe2015}.

This study advances an understanding of cybersecurity readiness by producing practical and theoretical insights for higher education institutions. Effective cybersecurity approaches must go beyond technological enforcement and address behavioural intentions and cultural dynamics, which are essential to safeguard sensitive information and institutional resilience \~\\citep{alshaikh2020, DaVeiga2020, Sutton2025}.

\\section{Research Aim and Questions}  
\\label{sec:1.5}  
Cybersecurity breaches in higher education have increasingly come from technical failures and from gaps in human behaviour and cultural alignment\~\\citep{Aldaajeh2022}. Recent studies and sector analyses show that human error and organisational blind spots were the leading causes of incidents in higher education\~\\citep{Aldaajeh2022, Alsharida2023, ulven2021, WEF2025}. To address this, greater attention is needed on how individual mental models of privacy intersect with institutional culture to shape cybersecurity behaviour and readiness.

This study examines the critical interplay between individual privacy perceptions, cybersecurity behaviours, and organisational culture within HEIs, emphasising its importance to advance the field and encourage researcher engagement.\\\\  
\\textbf{The primary aim} of this study was to examine how organisational culture and individual privacy perceptions influence cybersecurity readiness in higher education institutions.

To achieve this aim, the study addressed the following research questions (RQs):

\\begin{enumerate}  
    \\item \\textbf{RQ1:} How do individual mental models of privacy impact individuals' cybersecurity behaviour?   
    \\item \\textbf{RQ2:} How do the organisational culture and individual behavioural intentions impact the cybersecurity practice of higher education institutes?   
    \\item \\textbf{RQ3:} How do organisational culture and individual privacy behaviours influence organisational cybersecurity readiness?  
\\end{enumerate}

\\section{Definitions of Key Terms}  
\\label{sec:1.6}

To maintain readability and uniformity, key terms were defined with reference to academic literature and policy documents. These definitions delimited the scope of the research and were applied consistently throughout data collection, analysis, and interpretation. 

\\begin{description}  
    \\item\[Cybersecurity:\] The organisation of technical, human, and procedural resources designed to protect cyber-enabled systems and information from intentional threats that compromise confidentiality, integrity, or availability\~\\citep{Albinali2025, ISO2023, Niekerk2010}.  
      
    \\item\[Cybersecurity Awareness:\] Understanding and recognition of potential cyber threats and vulnerabilities, including knowledge of safe behaviours and appropriate responses within digital environments\~\\citep{Safa2015, Tsai2016, Xie2025}.  
      
    \\item\[Mental Model:\] An internal representation or framework used to understand, interpret and predict external phenomena, particularly system behaviour or environmental dynamics\~\\citep{Houser2025, Murimi2023, Rouse1986, Saucier2025, Schoenherr2022}.   
      
    \\item\[Mental Model of Privacy:\] A specific form of mental model reflecting how people perceive and responde to the privacy of personal data, associated risks, and protections in organisational contexts\~\\citep{Alge2006, Murimi2023, Schoenherr2022, Tolsdorf2020}.   
      
    \\item\[Organisational Culture:\] A system of shared assumptions, values, beliefs, and practices that shape how members behave and respond to cybersecurity expectations, norms, and leadership signals\~\\citep{DaVeiga2020, Schein2017, Schein2019}.  
      
    \\item\[Organisational Cybersecurity:\] Collective technical, policy and behavioural practices implemented within an organisation to protect data, systems and infrastructure from cyber threats\~\\citep{Aldaajeh2022, Georgiadou2022, Uchendu2021}.  
      
    \\item\[Cybersecurity Readiness:\] The extent to which an organisation is prepared to prevent, detect, respond to and recover from cyber threats, shaped by technological and human-cultural capabilities \~\\citep{Aldaajeh2022, Aliyu2020, Georgiadou2022, Hasan2021, Ozkan2021}.  
      
    \\item\[Personal Data Privacy:\] The right of individuals to control the access, collection, use and dissemination of personally identifiable information within digital and organisational systems \~\\citep{Dienlin2015, Reidenberg2018, Tolsdorf2020}.  
      
    \\item\[Personal Data Protection:\] Measures and policies designed to protect personal data from unauthorised access, misuse, or breach, often based on legal or regulatory frameworks\~\\citep{Aldaajeh2022, Georgiadou2022, OAIC2021, Victoria2014, Uchendu2021}.   
      
    \\item\[Identity Theft:\] A form of cybercrime in which unauthorised individuals access personal information to commit fraud, often resulting in financial loss or reputational harm \~\\citep{ACSC2020, Anderson2010, Franks2020, Hillman2023, Houser2025, WEF2025}.  
\\end{description}

\\section{Assumptions}  
\\label{sec:1.7}

This study is built on key philosophical and practical beliefs that are essential to its qualitative case study approach\~\\citep{yin2018}. Participants' experiences and perspectives are considered genuine and meaningful and are expected to provide insight into privacy and cybersecurity in higher education institutions\~\\citep{Dejonckheere2019, Holloway2017, Lincoln1985}. The study assumed that the participants answered honestly and thoughtfully during the interviews. They shared real-life experiences and interpretations of institutional operations. This aligned with procedures designed to encourage candid, reflective responses\~\\citep{Dejonckheere2019, Kallio2016}.

The study assumed that the participants were currently or had been involved with the institution. They had faced or considered issues related to personal data, cybersecurity, and privacy. Participants were expected to have sufficient familiarity to provide detailed and reflective accounts of their behaviours and observations. This expectation was aligned with the stated sampling approach\~\\citep{Biernacki1981, Noy2008, Parker2019}. 

Philosophically, the study adopted a qualitative explanatory stance, examining perceptions and behaviours and using qualitative evidence to explain mechanisms within their contexts\~\\citep {Brooks2015, Patterson2024}. This alignment allowed the study to begin with a priori theoretical concepts from PMT and Schein's culture model. These guided preliminary coding and pattern matching. Pattern matching, analytic generalisation, and triangulation guided inference\~\\citep{Miles2014, yin2018}. 

These diverse perspectives were not competing truths. They represented valid variations shaped by individual roles and experiences within the organisation. Such insights enabled analytic generalisation\~\\citep{Patterson2024, yin2018}.

The study also assumed that participants had a baseline understanding of privacy-related and cybersecurity terminology. This derives from professional engagement, awareness campaigns, or organisational communication. This assumption is supported by the design of the interview guide and established qualitative interview practices\~\\citep{Dejonckheere2019, Kallio2016}.

\\section{Scope and Delimitations}  
\\label{sec:1.8}

This study investigated the relationship between individual mental models of privacy and organisational culture, and how these factors shape cybersecurity readiness in a regional Australian HEI. The scope included faculty, employees, students, and institutional cybersecurity experts with direct or indirect involvement in organisational privacy and cybersecurity practices. This bounded focus was consistent with the qualitative case study logic for in-depth institutional inquiry\~\\citep{Creswell2018research, Nowell2017, yin2018}.

Geographically, the research was limited to a single HEI in regional Australia. This setting offered a distinct cultural and institutional context that differed from metropolitan universities in resource allocation, governance structures, and user demographics. The findings pursue transferability through detailed description, with an emphasis on conceptual understanding instead of statistical generalisation\~\\citep{Dejonckheere2019, Lincoln1985, Nowell2017}.

Thematically, the study focused on non-technical aspects of cybersecurity, specifically behavioural, perceptual, and cultural dimensions. It excluded system audits, technical infrastructure assessments, and quantitative performance metrics, allowing in-depth exploration of human and organisational influences on security practices. This emphasis is aligned with evidence that culture and behaviour were central to organisational cybersecurity\~\\citep{alshaikh2020, Georgiadou2022, Uchendu2021}.

Demographically, the study included participants who were actively engaged in the institution's cybersecurity environment. Engagement occurred through direct policy experience, awareness programs, or relevant decision-making processes. Individuals with insufficient knowledge or detachment from the institution's privacy and cybersecurity framework were excluded from the sample. This reflects the goal-oriented principles that prioritise information-rich cases\~\\citep{Etikan2016, Palinkas2015, Ramos2022}.

Methodologically, the study used a single-case explanatory framework supported by semi-structured interviews, an expert panel, and template analysis. The research emphasised conceptual transferability and thematic richness within a defined institutional setting. Semi-structured interviewing and template analysis were appropriate for depth and transparent coding in multi-phase qualitative designs\~\\citep{Brooks2015, Dejonckheere2019, Kallio2016, King2012, Lincoln1985, yin2018}. Analytical generalisation, not statistical generalisation, guided inference from case evidence to theory\~\\citep{Miles2014, yin2018}.

\\section{Significance of the Study}  
\\label{sec:1.9}

This study makes contributions in four areas. It links individual sense-making with organisational culture in cybersecurity. It provides practical guidance for culturally aligned strategy, training, onboarding, and communication within HEIs. It demonstrates a robust qualitative design using semi-structured interviews and template analysis. It supports institutional readiness and stakeholder engagement as the threat landscape evolves.

This qualitative single-case explanatory study is significant across theoretical, practical, methodological, and social domains. It contributes to the discourse on the human dimensions of cybersecurity. The study examined the intersection between privacy mental models and organisational cybersecurity culture. This research addressed a recognised gap in the literature that prioritise technology infrastructure while underexamining the behavioural and cultural factors that shape cybersecurity outcomes\~\\citep{alshaikh2020, Cheng2022, Georgiadou2022, Kannelonning2023, Sutton2025}.

From a theoretical standpoint, the study contributed by merging Protection Motivation Theory with Schein's Model of Organisational Culture. Investigates how individual beliefs and institutional cultural layers collectively influence cybersecurity readiness. Although PMT had been widely used to explain digital user behaviour, its application within organisational culture in Australian HEIs remained limited. The study addressed this gap by developing a conceptual framework that interlinks threat assessment, coping mechanisms, cultural artefacts, and shared assumptions. In doing so, it went beyond observable behaviours to examine deeper perceptions and cultural influences shaping institutional cybersecurity responses\~\\citep{Boss2015, mou2022, Schein2017, Schein2019}.

In practice, the research provided actionable insights for institutional leaders, policymakers, and cybersecurity practitioners. It offers a clearer understanding of how privacy-related mental models influence security participation, policy compliance, and employee or student awareness. These insights inform the design of culturally aligned training programmes, more effective onboarding processes, and behaviour-sensitive communication strategies. The findings highlighted cultural strengths and vulnerabilities that influence cybersecurity readiness and allow for closer alignment between policy and everyday institutional practice\~\\citep{Marshall2024, Prummer2025}. 

Methodologically, the study demonstrated the utility of template analysis for analysing complex qualitative data in diverse institutional roles. The structured yet flexible coding approach allowed grounded themes to emerge while maintaining consistency with theoretical constructs. Employing a single-case design, the research offers deep, context-specific insights with potential transferability to comparable educational institutions. The combined use of semi-structured interviews, NVivo, and layered coding reinforced transparency and rigour in qualitative cybersecurity research\~\\citep{Brooks2015, King2012, Miles2014, Nowell2017, yin2018}. 

Socially, the study provides greater awareness and shared responsibility among academic staff, students, and management about the digital privacy and security culture. Its findings underpin the development of privacy-conscious policy frameworks that empowered individuals and strengthened organisational resilience. By clarifying the interaction between personal perception and institutional norms, the study supported movement beyond compliance-based models toward engaged and adaptive cybersecurity cultures.

\\section{Role of the Researcher}  
\\label{sec:1.10}

In qualitative case study research, the researcher playes a crucial role in upholding the study's integrity and trustworthiness. This process encompasses study design, participant participation, data collection and analysis, and interpretation of findings through the theoretical framework of the study and research questions. In this study, the researcher performs key responsibilities, including designing interview protocols, recruiting participants, and interacting with them throughout the three data collection phases. The researcher also handles transcription and conducted analysis using Template Analysis. Using a single explanatory case study approach, the researcher is immersed as an observer within the organisation to develop a contextual understanding of privacy, culture, and readiness. To minimise bias, participants were recruited outside the researcher's professional circles to avoid pre-existing relationships that could create conflicts of interest or undue influence. Ethical standards were upheld through informed consent, confidentiality, and anonymity throughout the study. 

Reflexivity was a continuous process that involved a critical examination of personal assumptions and their potential influence on data interpretation\~\\citep{Berger2015}. The researcher actively avoided language or behaviour that might introduce bias related to gender, ethnicity, age, or professional status. Methodological transparency and rigour were supported by systematic coding, an explicit audit trail, and clear documentation of analytic decisions\~\\citep{King2017, Miles2014, Nowell2017}. These practices ensured that the researcher's role improved the validity of the study's conclusions and safeguarded methodological integrity.

\\section{Contributions to Knowledge and Practice}  
\\label{sec:1.11}  
This section brings together the key contributions of the study in theory, practice, and the development of assessment tools for cybersecurity readiness in HEIs.

\\subsection{Contributions to Theory}

This research provides new theoretical insight into cybersecurity behaviour in HEIs in the Australian context. It highlighted the relationship between individual privacy mental models and organisational culture, an interaction often overlooked in technology or compliance-focused studies. By addressing this intersection, the research broadened the existing literature to include socio-cultural influences shaping cybersecurity readiness\~\\citep{Cheng2022, Georgiadou2022, Kannelonning2023}.

The study integrates Protection Motivation Theory (PMT) with Schein's Model of organisational culture. It identifies 13 empirically validated characteristics of individual perception within organisational conditions. This integration provided a comprehensive explanation of individual mental and motivational processes. These mental and motivational processes interact with institutional assumptions, values and artefacts to shape cybersecurity intentions and behaviors\~\\citep{DelsoVicente2025, Herath2009, Schein2017, Uchendu2021}. 

Using a single qualitative explanatory case study and template analysis, the research bridges theoretical constructs with lived institutional experience. The findings demonstrate how privacy perceptions, insufficient organisational support, workload intensity, and cultural reinforcement conditioned the translation of intention into sustained behaviour. The study extends PMT by identifying insufficient support as a moderating factor. It refines Schein's model by operationalising observable cultural mechanisms relevant to cybersecurity governance.

Finally, the study adds originality by examining an Australian regional HEI. Theoretical integration and cross-phase validation are formalised within the integrated conceptual framework presented in Chapter \\ref{chapter:c8}. 

\\subsection{Contributions to Practice}

In practice, the research offers implications for policy makers, institutional leaders, and cybersecurity experts seeking to improve organisational preparedness. It demonstrated that effective cybersecurity management required alignment between privacy-related mental models, organisational culture, and leadership reinforcement.

The findings indicated that privacy-related mental models shaped engagement with cybersecurity measures in distinct roles. The study thus provides an operational evaluative lens based on 13 characteristics of mental models, allowing institutions to assess common reasoning patterns and adapt support accordingly.

The research develops an organisational cybersecurity readiness checklist from cross-phase evidence. It allows institutions to diagnose structural friction, prioritise interventions, and monitor behavioural indicators beyond the completion of policies or training. Cultural facilitators and barriers, including leadership visibility, psychological safety, accountability clarity, and workload feasibility, determined readiness stability.

The study offers evidence-based organisational recommendations derived from behavioural and cultural mechanisms, supporting differentiated readiness strategies and strengthening reporting confidence. Collectively, these outcomes provide a structured pathway for HEIs to move from compliance visibility to sustained behavioural consistency.  

\\subsection{Research Artefacts Developed by the Study}

\\begin{itemize}  
    \\item \\textbf{Thirteen Mental Model Characteristics:} A cross-phase synthesis of recurring privacy-related reasoning orientations operationalised for assessment and practical application (see Section\~\\ref{sec:8.3}, \~\\ref{sec:8.4} and Appendix\~\\ref{appendix:G}).  
    \\item \\textbf{Integrated Final Conceptual Framework:} A validated framework explaining how mental model characteristics, PMT constracts, and organisational cultural layers interact to shape readiness (see Section\~\\ref{sec:8.3} and Figure\~\\ref{fig:8.3}).  
    \\item \\textbf{Organisational Cybersecurity Readiness Checklist and Indicators:} A structured diagnostic tool for self-assessment and prioritisation grounded in cross-phase evidence (see Section \~\\ref{sec:8.4.2} and Appendix\~\\ref{appendix:G}).  
    \\item \\textbf{Organisational Cybersecurity Readiness Recommendations:} Evidence-based governance, leadership, training, and process interventions derived from empirical findings (see Section \~\\ref{sec:8.4.3}).  
\\end{itemize}

   
\\section{Outline of Thesis}  
\\label{sec:1.12}

This thesis is organised into nine chapters and structured around three sequential research phases. Each chapter builds on the previous to progressively examine the relationship between individual privacy mental models, organisational culture, and cybersecurity readiness in HEIs. The chapters are summarised below to guide the reader through the structure and analytical progression of the study (Table\\ref{tab:1.1}).

    
\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none, font={stretch=1.3}  
}

\\begingroup  
\\begin{spacing}{1.0} 

\\begin{longtable}\[\!ht\]{c p{2.8cm} p{3.5cm} p{5.5cm}}  
   
\\caption\[Chapter Roadmap: Titles, Objectives, and Core Content\]{%  
\\\\\[1.2em\]  
\\textit{Chapter Roadmap: Titles, Objectives, and Core Content}  
\\label{tab:1.1}  
}  
\\\\  
   
\\hline  
\\textbf{Chapter} & \\textbf{Title} & \\textbf{Objective} & \\textbf{Core Content and Evidence} \\\\ \\hline  
\\endfirsthead  
   
\\hline  
\\textbf{Chapter} & \\textbf{Title} & \\textbf{Objective} & \\textbf{Core Content and Evidence} \\\\ \\hline  
\\endhead  
   
1 & Introduction & Establish research context, aims, questions, and structure & Problem context in HEIs; significance; theoretical framing (PMT and Schein); scope; assumptions; contributions; thesis roadmap \\\\ \\hline  
   
2 & Literature Review & Position the study within existing scholarship and identify the research gap & Cybersecurity behaviour; privacy; organisational culture; PMT constructs; Schein's cultural layers; sector evidence; justification for integration \\\\ \\hline  
   
3 & Research Design & Define philosophical stance and overall study architecture & Explanatory single-case rationale; qualitative positivist positioning; multi-phase logic; theoretical alignment; research questions \\\\ \\hline  
   
4 & Implementation of the Research Design & Detail data collection and analytical procedures & Sampling; ethics; semi-structured interviews; template analysis; NVivo procedures; trustworthiness; cross-phase integration strategy \\\\  
   
5 & Phase 1 Data Findings and Discussion & Examine how individual mental models influence cybersecurity intention & PMT-linked themes; emergence of mental model characteristics; workload and support influences \\\\ \\hline  
   
6 & Phase 2 Data Findings and Discussion & Analyse how organisational culture shapes readiness & Schein-based thematic analysis; leadership signals; governance structures; onboarding, training, reporting mechanisms \\\\ \\hline  
   
7 & Phase 3 Data Findings and Discussion & Validate and refine cross-phase mechanisms & Expert confirmation; refinement of insufficient support and workload effects; validation of framework and practical artefacts \\\\ \\hline  
   
8 & Overall Discussion and Research Contribution & Integrate findings and formalise contributions & Cross-phase synthesis; integrated conceptual framework; extension of PMT; refinement of Schein; mental model characteristics; readiness checklist; organisational recommendations; methodological contribution; nature of knowledge claim \\\\ \\hline  
   
9 & Conclusion & Summarise findings and outline future directions & Final synthesis; implications for HEIs; limitations; recommendations for future research \\\\ \\hline  
   
\\end{longtable}  
\\end{spacing}  
\\endgroup

\\section{Summary and Conclusion}  
\\label{sec:1.13}  
This chapter introduced the context, rationale and objectives of the study and highlighted the need to examine human and cultural dimensions of the cybersecurity culture of organisations in HEIs. It explained behavioural and organisational influences on cybersecurity readiness in Australian higher education and outlined structural pressures experienced throughout the sector. The chapter identified a gap in the literature where individual privacy mental models and organisational culture had not been systematically integrated within cybersecurity research. It articulated the research problem, objectives, and questions and presented the theoretical framework through Protection Motivation Theory (PMT) and Schein's model. 

Key terms are defined to ensure conceptual clarity and consistency. The scope, boundaries, and assumptions of the study are specified. The following chapter \\ref{chapter:c2} reviews the literature by examining cybersecurity behaviour, privacy, and organisational culture, establishing the theoretical foundations, and identifying the conceptual and empirical gaps addressed by the study. The thesis structure is clarified to reflect a sequential multi-phase design that culminates in an integrated cross-phase contribution in Chapter \\ref{chapter:c8}.

By examining how privacy-related mental models interacted with organisational values, leadership signals, and governance practices, the study developed a structured account of cybersecurity readiness in higher education. The central argument established that technical controls alone were insufficient to ensure secure behaviour. Readiness depends on the alignment between individual judgment, cultural reinforcement, and institutional practice.

   
\\chapter{Literature Review}  
\\label{chapter:c2}

\\section{Introduction}  
\\label{sec:2.1}

Cybersecurity threats have spread rapidly across sectors, exposing organisations to consequences such as data breaches, ransomware attacks, phishing campaigns, and unauthorised access to institutional systems\~\\citep{CPR2026, IBMSecurity2025, Moore2026}. Higher education institutions (HEIs) have faced intense targeting because open networks, distributed governance structures, and larger student populations create several points of vulnerability\~\\citep{Cheng2022}. The technical difficulty and the decentralised authority have increased institutional exposure to cyber events\~\\citep{Fouad2021}. Several studies in the existing literature have concentrated on technical safeguards, offering inadequate guidance for academic leaders responsible for organisational governance and behavioural compliance\~\\citep{Alshaikh2021Model, Cheng2022, ulven2021}. The frameworks often mirror business or government contexts, not the unique structures of universities\~\\citep{Fouad2021}. Academic freedom, distributed authority, and discipline-specific cultures receive insufficient attention in mainstream cybersecurity governance models\~\\citep{alshaikh2020, Bongiovanni2019}.

As cybersecurity gaps widened, scholars called for more integrated approaches to organisational security management, viewing it as a multifaceted challenge linking technology, processes, and culture\~\\citep{Yeoh2022}. Security gaps persisted despite improved firewalls, intrusion detection systems, and security software, mainly because cybersecurity policies ignored human behaviour and organisational cultural norms\~\\citep{alshaikh2020, Georgiadou2022, Hadlington2017}. Institutional leaders, therefore, began to seek frameworks that integrated behavioural reasoning, organisational learning, and institutional governance\~\\citep{Ahmad2019, Patterson2023}. 

Organisational culture emerges as a key to cybersecurity outcomes; robust alignment minimises human threats and reduced the risk of breaches\~\\citep {DaVeiga2020}. Institutions that promoted accountability, shared responsibility, and visible leadership engagement report stronger cybersecurity practices\~\\citep{Lenter2024}. Leadership influence, peer norms, and institutional values consistently influenced daily cybersecurity behaviour more than formal policies alone\~\\citep{Alshaikh2021Model, Lie2021}. Training initiatives also showed variable effectiveness, depending on their design, delivery, and perceived relevance\~\\citep{Prummer2024}. 

Therefore, the higher education sector required a deeper examination of organisational dynamics, behavioural reasoning, and contextual learning processes\~\\citep{Bongiovanni2019, Fouad2021}. This chapter critically reviews existing theories and empirical research to identify key conceptual tensions between individual behaviour, organisational culture, and institutional cybersecurity readiness.

\\paragraph{Chapter Roadmap:\\\\}  
This chapter roadmap is presented in Figure \\ref{fig:2.1} and outlines the structure of the literature review. The chapter progresses from conceptual foundations to applied organisational perspectives, establishing a clear analytical basis for the study. It reviewed key concepts related to privacy, cybersecurity behaviour, mental models, organisational culture, and behavioural intentions in HEIs, then introduced Protection Motivation Theory (PMT) and Schein's model of organisational culture as core theoretical foundations informing the integrated conceptual framework. This was concludes by identifying the literature gaps that justified the research questions and guided the empirical investigation in subsequent chapters.

\\begin{figure}\[H\] %\[\!ht\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[\]{%  
    \\textbf{Figure 2.1}\\\\\[1.2em\]  
    \\textit{Chapter 2 Roadmap}  
    }  
    \\label{fig:2.1}

    \\addcontentsline{lof}{figure}{2.1 \\hspace{0.18cm} Chapter 2 Roadmap}

    \\includegraphics\[width=\\linewidth\]{Figures//c2/2.1roadmap.png}

    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
        \\text{}  
    \\end{minipage}  
\\end{figure}

 

 

\\section{Privacy and Cybersecurity Behaviour}  
\\label{sec:2.2}

Privacy concerns in HEIs extend beyond personal data to include research outputs, intellectual property, and financial records\~\\citep {Cheng2022}. In this study, privacy was defined as control over data access, use, and disclosure, ensuring that information was handled correctly\~\\citep{Lenter2024}. Cybersecurity refers to organised approaches and tools used to protect the confidentiality, integrity, and availability of digital systems and information assets against unauthorised access, theft, or disruption\~\\citep{Yeoh2022}. In reality, cybersecurity readiness in HEIs depends on technical safeguards and everyday user behaviour, with human factors causing many incidents before technical failures\~\\citep{Cheng2022}.

Cybersecurity behaviour is examined in routine actions and regular habits, through which individuals manage digital risk and decrease exposure to harm\~\\citep{Sutton2025}. 

Badreddine et al.\~\\citep{Badreddine2025} conceptualised cybersecurity behaviour as a function of individual potential, motivation, and organisational opportunities. A behavioural study highlights how psychological and situational factors influence cybersecurity decisions. Research indicates that employees consistently underestimate the likelihood of cybersecurity breaches, thereby weakening motivation to adopt protective practices\~\\citep{Hadlington2017, Hina2019}.

\\section{Mental Models and Privacy Decision-Making}  
\\label{sec:2.3}

Mental models serve as internal representations of external reality, allowing individuals to interpret complex systems and phenomena\~\\citep{Tolsdorf2020, Xie2025}. Mental models represent organised knowledge frameworks of specific content and interrelationships, allowing people to describe, explain, and predict digital events\~\\citep{Cassidy2018}. By organising past experiences into familiar patterns, mental models guide attention and supported rapid judgements, yet they could still become inconsistent or unstable in different situations\~\\citep{Schoenherr2022}. In cybersecurity contexts, mental models serve as cognitive tools that allow users to reason about digital environments and anticipate the consequences of their actions, especially when technical knowledge is incomplete\~\\citep {Tolsdorf2020}.

Within higher education institutions, users constitute a diverse population who frequently interact with complex systems without professional knowledge of the underlying cybersecurity infrastructure\~\\citep{Badreddine2025}. Thus, users' privacy decisions are guided through mental models (simplified representations of incomplete information, experience, and private analogies). Rather than seeing official guidelines, employees prioritise familiar peer advice and knowledge-sharing for security behaviour, so collective norms often prevail over written policies\~\\citep{Sutton2025}. These assumptions shape security beliefs, leading users to delegate data protection to management or technical safeguards, raising a false sense of safety\~\\citep{Lenter2024}.

Mental models direct attention to security cues that support expectations, causing users to overlook inconsistent signals\~\\citep{Xie2017}. \~\\citet{Reeves2025} observed that these cognitive patterns influenced credibility judgements and decision-making. Their study found that cybersecurity groups held others responsible for individual errors, advising them on training, while viewing their own issues as requiring system-wide fixes. Even different role-based mental models lead people to perceive cybersecurity risks differently in their respective roles\~\\citep {Murimi2023}.

The relationship between mental models and privacy decision-making has been a central theme in the privacy paradox literature, which examines the disconnect between individuals' expressed privacy attitudes and their actual behaviours\~\\citep{Curzon2021, Mehdy2021}. Many studies, including  \~\\citet{Acquisti2015} and \~\\citet{Gerber2018}, reported that individuals expressed strong privacy fears but engaged in behaviours that revealed sensitive information despite risks. Actions such as credential reuse, ignoring security updates, or informally sharing authorisation continued despite widespread awareness of potential threats\~\\citep{Lie2021, ulven2021}. Researchers argued that such disagreements arise from individuals' mental models of organisational systems and cyber risks, which are often incomplete or inaccurate\~\\citep{Murimi2023, Xie2017}.

These results indicate that organisational policies hamper privacy-related cybersecurity behaviour more than technical controls alone. Thus, mental models offered a vital lens for analysing how privacy perceptions influenced cybersecurity practices in higher education settings.

\\section{Individual Behaviour and Cyber Risk}  
\\label{sec:2.4}

Individual attitudes, beliefs, and reasoning patterns significantly shape the cybersecurity outcomes in HEIs\~\\citep{Georgiadou2022, Sutton2025}. Although organisational arrangements and technical controls remain essential, they are frequently weakened by user decisions driven by personal mental models, emotional reactions, or behavioural shortcuts\~\\citep{Abiodun2025, Gerber2018}. This section explores the multifaceted effects of individual-level cybersecurity readiness, particularly in distributed and knowledge-intensive HEI environments\~\\citep{Bongiovanni2019}.

Human behaviour in digital settings is influenced by cognitive judgement, work pressure, and perceived weight of security procedures\~\\citep{Hadlington2017}. Individuals often make rapid judgements while managing competing tasks in several systems. Under such conditions, security practice is sometimes considered secondary to immediate work\~\\citep{Gerber2018, Prummer2024}. 

Workplace contexts shape behavioural responses to cyber risk. Universities function as open and collaborative environments where information sharing is common and digital tools supported teaching, research, and administration\~\\citep{ulven2021}. Studies reported that employees frequently misjudged the likelihood of cyber incidents\~\\citep{Hina2019}. Similar patterns were detected in environments where users assumed that institutional systems were already safe\~\\citep{Lenter2024}. These conditions sometimes encourage convenience-driven behaviour. Such practices did not necessarily reflect intentional negligence; they often appear in attempts to maintain efficiency within complex digital workflows\~\\citep{Badreddine2025}.

Awareness programmes are a foundation for the institutional cybersecurity strategy. However, their effectiveness varies widely depending on the distribution style, the content's significance, and user engagement. Several studies observed that traditional training designs, such as emails or mandatory modules, often fail to change behaviour in insightful ways\~\\citep{alshaikh2020, Alshaikh2021Journal}. Although users may recall factual knowledge, they recurrently revert to habitual behaviours under stress or distraction.

Several causes contributed to this gap between knowledge and behaviour. Behavioural change requires not only knowledge but also continued motivation, self-efficacy, and alignment with personal values. Without focusing on these dimensions, awareness movements can appear irrelevant or burdensome. In addition, info overload and message fatigue can reduce interest in important signals, particularly when warnings are frequent but are rarely followed by visible consequences\~\\citep{Mangundu2023, Prummer2024, Schaik2020}. More interactive tactics, including simulated phishing exercises and scenario-based training, are more effective because they connected cybersecurity advice with realistic assessment situations\~\\citep{Badreddine2025, Tobarra2021}. Therefore, examining how people reacted to these situations remains necessary to understand cybersecurity readiness within HEIs.

\\section{Organisational Culture and Cybersecurity}  
\\label{sec:2.5}

Organisational culture is widely recognised as a fundamental element of employee behaviour, decision-making, and overall institutional efficacy\~\\citep{Pavlova2020, Sutton2025}. This comprises shared assumptions, beliefs, values, and artefacts that guide members' views and responses to their surroundings\~\\citep{Georgiadou2022}. From a cybersecurity perspective, these cultural patterns guide how individuals explain policies, prioritise security responsibilities, and respond to emerging digital threats. 

In cybersecurity research, organisational cybersecurity culture encompassess individual behaviours that defend organisational information by complying with policies and secure practices, as well as through communication, awareness, training, and education\~\\citep{alshaikh2020, Lie2021}. A deep cybersecurity culture fosters protective actions by integrating security into habits and practices, elevating information safety from a mere technical obligation to a shared institutional value\~\\citep{Alshaikh2021Model}. In contrast, inadequate cultural emphasis on cybersecurity or misalignment between policies and practice often triggers frustration, inconsistent compliance, and avoidance of protocols to prioritise productivity\~\\citep{Badreddine2025}. These cultural elements and subcultures play an important role in how security duties are shared and carried out between different departments\~\\citep{DaVeiga2010}. 

Leadership broadly shapes the cultural conditions essential to organisational cybersecurity, serving as a critical enabler of practical, effective outcomes\~\\citep{DaVeiga2020}. Executive priorities, visible leadership commitment, and strategic resource allocation, such as reserved funding and personnel, signal organisational significance for cybersecurity\~\\citep{alshaikh2020, Cheng2022, alghafri2024}. Institutions where leaders actively model cybersecurity and participate in participatory governance demonstrate stronger security involvement and marked advances in employee compliance\~\\citep{Hassandoust2023}. In contrast, delegating cybersecurity primarily to the organisation or IT departments restricts broader individual accountability and organisational participation\~\\citep{Ashenden2013, Badreddine2025, Reeves2025}.

Cultural misalignment occurs when formal cybersecurity policies clash with operational systems, prompting employees to bypass policies deemed impractical or overly inflexible\~\\citep{Badreddine2025}. Repeated irrelevant security messaging also leads to policy fatigue, reduced participation, and undermined adherence to institutional guidelines\~\\citep{Mangundu2023}. In such conditions, the absence of incentives or feedback undermines the credibility of the policy and concealed behavioural vulnerabilities from detection\~\\citep{Ashenden2013}.

\\section{Behavioural Intentions in Cybersecurity}  
\\label{sec:2.6}

Behavioural intention has been widely examined as a key predictor of cybersecurity behaviour in organisational environments\~\\citep{Mangundu2023}. In this context, the intention of behaviour refers to an individual's willingness to follow institutional security policies, adopt protective practices, and avoid risky actions. Research has shown that these intentions are shaped by how individuals interpreted cyber risks and their potential consequences\~\\citep{Hina2019}. Employees who perceived cyber threats as serious and personally relevant demonstrated stronger intentions to comply with security policies\~\\citep{Skalkos2021}. Conversely, when threats appeared distant or unlikely, convenience frequently outweighed security considerations\~\\citep{Balozian2017}.

Behavioural intention is significantly shaped by organisational expectations and subjective norms, reflecting perceived social pressures to engage in specific security actions \~\\citep{Mehdy2021}. Research indicates that workplace practices, peer behaviour, and managerial communication firmly shape individuals' readings of cybersecurity responsibility\~\\citep{alshaikh2020}. When secure behaviour becames visible and socially reinforced within organisational routines, employees showed greater commitment to institutional security practices\~\\citep{Parsons2015}.

\\section{Cybersecurity Readiness in Higher Education Institutes}  
\\label{sec:2.7}

HEIs have become increasingly attractive targets for cyberattacks due to their exposed academic culture, decentralised governance, and various stakeholder groups\~\\citep{Fouad2021, Kont2024}. Universities prioritise knowledge sharing, but these behaviours often clashed with rigid security frameworks and hesitate to implement consistent cybersecurity practices. Thus, organisational cybersecurity readiness within HEIs depends not only on security infrastructure but also on governance structures, institutional direction, and user commitment\~\\citep{Hakiem2023}.

HEIs, in general, operate in environments defined by academic freedom, openness, decentralisation, and a bring-your-own-device (BYOD) culture. These factors are crucial in increasing innovation and encouraging intellectual engagement, yet they also introduc notable weaknesses\~\\citep{Alshaikh2021Model}. HEIs facilitate diverse user populations with varying levels of digital literacy and security awareness\~\\citep{Fouad2021, Kont2024}.

\\subsection{Cybersecurity Challenges and Recent Case Examples}  
The academic space is especially vulnerable due to sensitive data holdings that include unpublished research, student files, financial data, and proprietary technology\~\\citep{Pinheiro2020}. Recent high-profile incidents highlighted these risks. For example, the 2023 ransomware attack on the University of Duisburg-Essen caused an entire IT shutdown, interrupting teaching and administrative processes for weeks\~\\citep{Antal2023}. Similarly, the 2024 breach at Western Sydney University exposed delicate data of more than 10,000 individuals, highlighting damage to organisational trust and service delivery\~\\citep{WSU2024}. 

AI-driven fear has become a major concern, increasing the occurrence, success rates, and complexity of cyberattacks on HEIs\~\\citep{Kaloudi2020, Lenter2024}. Kaloudi and Li\~\\citep{Kaloudi2020} highlighted how artificial intelligence is used to automate attack activities, enabling threat actors to overcome human weaknesses and devise highly targeted indirect strategies. Ransomware-as-a-Service (RaaS) models comprise a franchise-like economy on the dark web, allowing individuals lacking technical or programming skills to execute effective targeted cyberattacks\~\\citep{Kettani2019, Meland2020}. HEIs remain particularly vulnerable to these attacks due to inadequate incident response systems and a lack of ongoing threat intelligence monitoring\~\\citep{Pinheiro2020}. 

\\subsection{Awareness and Training Interventions}  
Awareness initiatives in HEIs ranged from passive methods (email alerts, posters, infographics) to active models (interactive workshops, simulated phishing campaigns, scenario-based training)\~\\citep{Bada2019, Chaudhary2022, Prummer2024}. Active methods were shown to be more effective in helping people remember and change their behaviour, although they required more resources and ongoing leadership support. The training engagement encounters several persistent obstacles. Issues such as information overload, poorly timed sessions, perceived irrelevance, and training fatigue all contributed\~\\citep{Bada2019, Mangundu2023, Prummer2024}. 

Many participants overlooked cybersecurity updates or invitations, often claiming that they already knew enough or simply lacked time\~\\citep{Alshaikh2021Journal}. This reflected the illusion of knowledge, or overconfidence, in which individuals mistakenly believed that their current awareness levels sufficed despite engaging in risky or outdated behaviours\~\\citep{Chaudhary2022, Kokolakis2017}. Research showed that even extensive training processes did not ensure higher compliance values. Basic awareness initiatives often failed to convert knowledge gains into sustained, secure behaviours\~\\citep{Mangundu2023}.

Awareness strategies focus on these challenges by customising to role-specific risks and processes\~\\citep{Jeong2022}. Training occurrs at optimal times, such as during onboarding or regular updates, and incorporated reflection alongside feedback opportunities \~\\citep{Abiodun2025, Tobarra2021}. Gamified elements, including competitions and behavioural nudges, further boosted engagement and internalisation of security value. Despite these efforts, many HEIs continued to experience substantial gaps in cybersecurity readiness.

\\section{Theoretical and Conceptual Foundations}  
\\label{sec:2.8}

This section assesses the principal theoretical frameworks used in previous research to explain cybersecurity behaviour and organisational culture within HEIs. The literature shows that challenges in academic settings rarely stem from purely technical weaknesses. Instead, security consequences are repeatedly shaped by the relationships between individual behaviour, organisational norms, and institutional arrangements.

Cybersecurity practices are increasingly understood as socio-technical phenomena \~\\citep{Hakiem2023, khadka2025}. Among these angles, Protection Motivation Theory (PMT) and Schein's Model of organisational culture have been broadly applied in cybersecurity research. PMT illuminated the individual evaluations of protection risks and their decisions to adopt defence behaviours\~\\citep{Kiran2025, Menard2017}. By contrast, Schein's framework examined organisational values, artefacts, and underlying assumptions that shaped security practices\~\\citep{DaVeiga2016, Uchendu2021}. Together, the theories offered a comprehensive lens for understanding cybersecurity readiness in HEIs. 

In addition to these two primary frameworks, several supporting theoretical perspectives appear in the cybersecurity literature. These included the Theory of Planned Behaviour (TPB), the Technology Acceptance Model (TAM), socio-technical systems theory, and cultural dimensions theory. These perspectives provided insights into behavioural intentions, technology adoption, and institutional complexity. Chapter \\ref{chapter:c3} (Section\~\\ref{sec:3.2.2}) justifies the selection of protection motivation theory and Schein's organisational culture model. It details how these frameworks shape the research design, interviews, and analytical template.

\\subsection{Protection Motivation Theory}  
\\label{sec:2.8.1}

Protection Motivation Theory (PMT) was originally introduced by Rogers \~\\citeyearpar{Rogers1975} and later expanded by Maddux and Rogers \~\\citeyearpar{Rogers1983}, including self-efficacy and response costs. The theory was initially developed within health psychology to understand behavioural responses to fear appeals and risk communication\~\\citep{Maddux1983, Rogers1983}. Over time, PMT has been increasingly applied in information security research to investigate why individuals choose to follow or disregard recommended cybersecurity practices. 

Within cybersecurity studies, PMT has frequently been used to explain behaviours such as password management, phishing avoidance, and compliance with organisational security policies. Researchers have applied the theory in organisational and educational contexts to examine how individuals interpret digital risks and decide whether protective actions are necessary\~\\citep{Kiran2025, Latif2025, Sharma2022, Shillair2020, Xiao2014}. In cybersecurity research, PMT effectively captures the reasoning behind intentional behaviour change, which is suitable for user-centred and organisational studies. This research adopts the PMT model from \~\\citet{Xiao2014}, as presented in Figure\~\\ref{fig:2.2}.\\\\

\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Protection Motivation Theory\]{%  
    \\textbf{Figure 2.2}\\\\\[1.2em\]  
    \\textit{Protection Motivation Theory}  
    }  
    \\label{fig:2.2}  
    
    % \\addcontentsline{lof}{figure}{2.2 \\hspace{0.18cm} Protection Motivation Theory}  
      
    \\includegraphics\[width=0.7\\linewidth\]{Figures//c2/2.2PMT.png}  
      
    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
        \\textit{\\\\Note.} Adapted From "Protection motivation theory in predicting intention to engage in protective behaviors against schistosomiasis among middle school students in rural China" , by, \\citep{Xiao2014}, PLoS Neglected Tropical Diseases, Volume(8), p. 03\. (https://doi.org/10.1371/journal.pntd.0003246).  
    \\end{minipage}  
\\end{figure}

   
 

\\textit{Knowledge and Experience} studied examines individuals' prior cybersecurity exposure, privacy knowledge, and formal training or experiences\~\\citep{Hanus2016, Xiao2014}. These perceptions reveal how personal and professional backgrounds shaped cybersecurity risk awareness and secure practices. 

\\textit{Threat assessment }captured how individuals assessed the severity and individual likelihood of a threat. This evaluation generally involved three key constructs: severity, vulnerability, and rewards associated with risky behaviour\~\\citep{Latif2025, Menard2017, Skalkos2021, Yusif2023}. Perceived severity assessed the anticipated consequences of cybersecurity incidents, vulnerability judged personal or institutional exposure risk, and rewards captured the benefits of insecure actions, such as convenience or less effort. In higher education environments, these perceptions have often influenced whether employees or students prioritise cybersecurity practices when interacting with digital cybersecurity systems.

\\textit{The Coping Assessment} focused on an individual's assessment of their ability to perform protective actions and the effectiveness of those activities. Three constructs have commonly been associated with this appraisal: self-efficacy, response efficacy, and response cost\~\\citep{Kiran2025, Safa2015, Tsai2016}. Self-efficacy described an individual's confidence in their ability to carry out protective behaviour. The efficacy of the response referred to the perceived effectiveness of the recommended security measure. The response cost represented the perceived effort, inconvenience or time required to implement the protective action. Together, these constructs have been used to explain how individuals balance perceived risks with their perceived capacity to respond. Therefore, the interaction between threat assessment and coping assessment has been central in understanding security behaviour in many cybersecurity studies\~\\citep{Hanus2016, Kiran2025, Latif2025}.

\\textit{Behavioural Intentions} synthesise how cognitive appraisals shaped secure actions, termed protection motivation\~\\citep{Menard2017}. This construct encompassed policy adherence, routine safe practices, and risk awareness, normalising compliance\~\\citep{Kiran2025, Safa2015, Xu2024}. Analysing them bridges the knowledge-doing gap between knowledge and enactment, linking individual psychology to institutional readiness for a holistic view of cybersecurity preparedness\~\\citep{Aliyu2020}.

Applications of PMT within cybersecurity research have expanded considerably over the past decade as organisations have increasingly recognised the importance of human behaviour in security outcomes\~\\citep{Kiran2025}. The theory has been applied in studies that examine employee compliance with organisational policies, responses to phishing threats, and the effectiveness of cybersecurity awareness programs\~\\citep{DelsoVicente2025, khadka2025}. In higher education institutions, PMT has been used to explore how staff and students perceive cybersecurity risks and how these perceptions influence daily security practices.

Despite its utility, recent literature highlights key limitations, notably the emphasis of PMT on rational cognitive evaluation\~\\citep{mou2022}. Therefore, critics have suggested that PMT may not fully capture emotional responses, habitual behaviours, or broader organisational influences that shape cybersecurity practices. In complex institutional environments such as universities, behaviour often emerges from cultural norms, organisational expectations, and social interactions\~\\citep{Hu2012, khadka2025, Lenter2024}. Therefore, integrating PMT with complementary models enables a holistic analysis of individual mindsets and privacy behaviours. This perspective is vital for evaluating cybersecurity readiness in multidisciplinary organisational contexts.

\\subsection{Schein's Model of Organisational Culture}  
\\label{sec:2.8.2}

Edgar Schein's model of organisational culture is widely used to explain how institutional norms, values, and shared assumptions influence behaviour within organisations\~\\citep{Lenter2024, Schein2010, Schein2017, Uchendu2021}. The framework conceptualises culture as three interconnected levels: artefacts, espoused values, and basic underlying assumptions. Collectively, these layers shape how  how organisational units understand policies, responded to expectations, and connected with technological systems. In the context of cybersecurity, these three levels shaped the way security policies were developed, communicated, and implemented\~\\citep{DaVeiga2010}, as presented in Figure\~\\ref{fig:2.3}.\\\\

\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[\]{%  
    \\textbf{Figure 2.3}\\\\\[1.2em\]  
    \\textit{Edgar Schein's model of organisational culture}  
    }  
    \\label{fig:2.3}  
    
    \\addcontentsline{lof}{figure}{2.3 \\hspace{0.18cm} Edgar Schein's model of organisational culture}  
      
    \\includegraphics\[width=0.3\\linewidth\]{Figures//c2/2.3Schein.png}  
      
    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
               \\textit{\\\\Note.} Adapted From "Organisational Culture and Leadership, 3th Edition" (p.26), by\~\\citet{Schein2004}, (https://www.google.com.au/books/edition/Organizational\\\_Culture\\\_and\\\_Leadership/K96qDQAAQBAJ).   
    \\end{minipage}  
\\end{figure}

 

   
 

\\textit{The organisational culture} reflects the shared beliefs and practices that shape the security behaviour of employees\~\\citep{Lenter2024, Schein2010, Yusif2023}. This influences threat perception, task prioritisation, and incident responses. Strong cultures promoted proactive security, weak ones prioritised convenience over vigilance. Training succeedes when aligned with norms, according to Schein's three tiers: artefacts, espoused values, and underlying assumptions, with leadership reinforcing accountability\~\\citep{McCants2022, Schein2017, Uchendu2021}. Awareness of risks motivates preventive action, shaping both personal and collective responses\~\\citep{Alzahrani2021, Kiran2025}. Studies show that high security awareness among employees improves institutional resilience\~\\citep{Liu2020, Riggins2024}. 

\\textit{The} artefacts express visible signs of the commitment to cybersecurity, including policies, posters, protocols, and reporting systems\~\\citep{alshaikh2020, Dimitrov2013, Kaptein2011}. They communicated expectations and regulated routine, safe behaviour through campaigns, and secure designs. Although artefacts signalled culture, they often masked deeper guiding beliefs.

\\textit{The values} comprise principles empphasised in mission statements, strategies, and policies that prioritise cybersecurity and data responsibility\~\\citep{Niekerk2010, Schein2017, Yusif2023}. They guided decision-making by defining behaviour, promoting transparency, accountability, and shared responsibility to achieve stronger security outcomes\~\\citep{Uchendu2021}. Leadership reinforced them through modelling, training, and communication, although gaps persisted between ideals and daily practices.

\\textit{The underpinning assumptions} represent unspoken beliefs, filtering policy interpretation, and risk responses\~\\citep{Schein2017}. They encourage noncompliance, such as over-relying on technology over vigilance, encouraging false safety\~\\citep{Alshaikh2021Model, Lenter2024}. Addressing hidden gaps between assumptions and values aligned behaviour with policy for sustained cultural change.

Nevertheless, several identifies limitations Schein's model, notably its oversimplification of culture as unified and stable\~\\citep{Parsons2015, Uchendu2021}. Large, decentralised institutions harbour multiple subcultures, including generational divides between digital natives and residents that shaped security behaviours in various groups\~\\citep{DaVeiga2020, Yusif2023}. Rapid technological changes and digital risks challenged the stability of organisational assumptions over time\~\\citep{Chaudhary2022}. The researchers recommended complementing cultural analysis with behavioural and socio-technical perspectives for a comprehensive assessment of cybersecurity readiness\~\\citep{DelsoVicente2025}.

\\subsection{Additional Theoretical Perspectives }  
\\label{sec:Additional}

The integration of multiple theories, including TPB, can inspire researchers and cybersecurity professionals to explore innovative approaches, making them feel motivated to advance the field through comprehensive analysis.

\\textbf{Theory of Planned Behaviour:}  
The Theory of Planned Behaviour (TPB), introduced by Ajzen (1991), proposes that behavioural intentions develop from attitudes towards the behaviour, subjective norms, and perceived behavioural control. Meta-analyses, which statistically combine results from multiple empirical studies to identify overall patterns, enhance TPB's predictive power for behaviour, including security policy compliance\~\\citep{Sommestad2017}. TPB excels at identifying interventions such as changing attitudes through communication, norms through leadership, and control through tools. However, this rational focus neglects habits, emotions, and fears in security decisions, necessitating complementary models. Recent higher education studies employ TPB to explain the knowledge-action gap in cybersecurity, where awareness declines to yield consistent practice\~\\citep{Kont2024, Ong2022, Prummer2024, Yusif2023}. This underscores the need for complementary models that address emotional and contextual factors.\\\\

\\textbf{Technology Acceptance Model (TAM):}  
The Technology Acceptance Model (TAM) is a widely adopted framework to predict user acceptance of new technologies, based on perceived usefulness and perceived ease of use\~\\citep{AlAdwan2023, Boss2015}. In cybersecurity, TAM has been used to examine the adoption of security technologies such as authentication systems, incident reporting platforms, and training tools. However, the model primarily addresses user-technology interactions and provides limited insight into organisational culture or behavioural motivation.\\\\

\\textbf{Socio-Technical Systems Theory:}  
Socio-Technical Systems (STS) theory highlight interactions between social actors, processes, and technology, which require joint optimisation for effective performance\~\\citep {Pasmore2019}. From this, cybersecurity incidents rarely result from isolated technical weaknesses. Instead, vulnerabilities often arise from misalignment between institutional policies, user behaviour, and technological systems. Thus, STS provides a useful perspective for examining institutional complexity in cybersecurity situations\~\\citep{Charitoudi2013, Thinyane2024}. Nevertheless, the framework focuses primarily on systemic interactions and provides less detail on individual behavioural judgement processes.\\\\

\\textbf{Cultural Dimensions Theory:}  
Cultural dimensions theory examines how broader cultural characteristics influence behaviour within organisations\~\\citep{Hofstede2010, Willie2023}. In international higher education, cultural orientations shape interpretations of authority, risk, and institutional expectations. These differences affect the interpretation and implementation of cybersecurity policies in diverse academic communities. However, the theory operates at macro-cultural levels and overlookes individual responses to cybersecurity threats.\\\\

These theories provide valuable insights into behavioural intentions, technology adoption, systemic interactions, and cultural influences. The study examined them as discrete facets of cybersecurity behaviour.\\\\

 

\\section{Integrated Conceptual Framework}  
\\label{sec:2.9}

This section presents the integrated conceptual framework developed to examine how individual privacy mental models and organisational cybersecurity culture interact to influence cybersecurity readiness in HEIs. The framework integrates Protection Motivation Theory (PMT) and Edgar Schein's Model of Organisational Culture to capture both behavioural and organisational inspirations on cybersecurity practices. While Section 2.8 discussed these theories conceptually, the present section explains how they are combined to structure the analytical depth of this study.

Cybersecurity behaviour in HEIs is shaped by both individual decision activities and organisational perspectives\~\\citep{Aliyu2020, Hakiem2023}. Although PMT explains how people evaluate cybersecurity threats and establish whether protective action is required\~\\citep{Kiran2025}. The theory observes the relationship between threat and coping, incorporating constructs such as severity, vulnerability, rewards, self-efficacy, response efficacy, and response cost\~\\citep{Latif2025, Menard2017, Skalkos2021}. Empirical research has widely applied PMT to examine security behaviour in organisational and educational environments\~\\citep{Gao2018, Ong2022, Wu2020}.

However, individual behaviour occurs within organisational environments that shape expectations, norms, and everyday practices. Schein's Model of Organisational Culture provides a framework for studying these organised influences. The model conceptualises organisational culture through three interconnected levels: artefacts, values, and basic underlying assumptions\~\\citep{DaVeiga2016, Schein2017, Uchendu2021, Yusif2023}. Artefacts include visible organisational practices, such as security posters, policies, procedures, and technological safeguards. Embraced values reflect organisational priorities expressed through strategies and governance structures. Underlying assumptions represent implicit individual beliefs that shape behaviour within organisations.

The integration of PMT and Schein's model proved both logical and necessary. The study analysed both domains together. This enabled a comprehensive understanding of cybersecurity readiness in HEIs. PMT captured mental factors driving privacy decision-making. Schein's model explained the organisational cultural aspects. Without cultural alignment, people with high awareness of the threat and coping effectiveness often feel discouraged. The combined framework thus offered accurate, actionable insights into cybersecurity readiness.

Figure\~\\ref{fig:2.4} presents the conceptual framework developed for this study. The left side of the framework represents the individual behavioural domain derived from PMT, which examines privacy mental models through knowledge and experience, coping variables, and threat perception. The right side represents the organisational cultural domain derived from Schein's model, analysing influential artefacts, values, and underlying assumptions. A dotted line from left to right illustrated how understanding behavioural intentions strengthened organisational culture. The collaboration between these domains illustrated how individual perceptions and organisational culture collectively influenced cybersecurity readiness in higher education institutions.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[\]{%  
    \\textbf{Figure 2.4}\\\\\[1.2em\]  
    \\textit{Research Conceptual Framework}  
    }  
    \\label{fig:2.4}  
    
    \\addcontentsline{lof}{figure}{2.4 \\hspace{0.18cm} Research Conceptual Framework}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c2/2.4 Propose Framework.png}  
      
    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
        \\text{}  
    \\end{minipage}  
\\end{figure}

 

Figure \\ref{fig:2.4} shows the conceptual framework that guides this study. The framework examined cybersecurity behaviour through PMT Theory. It addressed cultural impact through Schein's model. These perspectives enabled the study to evaluate how individual privacy mental models and organisational cybersecurity culture jointly shaped organisational cybersecurity readiness.

\\section{Research Gaps}  
\\label{sec:2.10}

The previous sections presented the relationships between privacy decision-making, cybersecurity behaviour, organisational culture, and cybersecurity practices within higher education institutions (HEIs). Recent research has expanded substantially. However, the literature remaines fragmented in behavioural, organisational, and methodological perspectives. The synthesis of these studies highlighted key gaps. 

First, a theoretical gap persisted in the integration of behavioural and organisational explanations of cybersecurity behaviour in HEIs. The protection motivation theory studies concentrate on the perception and coping of individual threats\~\\citep{Menard2017, Skalkos2021, Wu2020}. These hardly addresse organisational decision perspectives\~\\citep{Alshaikh2021Model}. Schein's culture research highlighted institutional values, artefacts, and assumptions that influenced security behaviour\~\\citep{DaVeiga2016, Schein2017, Uchendu2021}. These views rarely integrate behavioural theories\~\\citep{Georgiadou2022, Hu2012}. Existing studies therefore analysed the behavioural or cultural dimensions independently. This leaves left a limited theoretical integration between individual cybersecurity reasoning and organisational cultural dynamics\~\\citep{Yusif2023}. Their isolation limits understanding of the interplay in higher education.

Second, a conceptual gap remained in understanding how privacy-related mental models interacted with institutional expectations and cybersecurity culture within HEIs. Previous studies reported fragmented patterns of security compliance, even including technically qualified individuals\~\\citep{Bongiovanni2019, Georgiadou2022}. Research also revealed that cognitive biases, digital nativity, and individual risk perceptions often influenced cybersecurity behaviour more strongly than technical knowledge\~\\citep{Fouad2021, ulven2021, Yusif2023}. Although these findings emphasised the importance of individual reasoning practices, they rarely examine how these mental models were shaped by organisational circumstances, informal practices, or institutional culture\~\\citep{Niekerk2010, Tolsdorf2020}. Consequently, the connection between privacy mental models and cybersecurity culture remained insufficiently studied in higher education contexts\~\\citep{Aliyu2020, ulven2021}. 

Third, a methodological gap existed in cybersecurity culture studies within HEIs. Most of the research on cybersecurity culture in HEIs is based on quantitative surveys\~\\citep{Prummer2024}. These effectively capture large-scale perceptions\~\\citep{Alzahrani2021, Latif2025}. These surveys often overlooked deeper insights and subtleties that reveal the underlying cultural dynamics and behavioural motivations\~\\citep{Kiran2025, Liu2020}. Qualitative investigations of cybersecurity culture remained relatively limited\~\\citep{alshaikh2020, Schaik2020}, and multi-phase qualitative studies examining both individual behaviour reasoning and organisational cultural conditions were particularly few. This limitation restricted the ability to capture the deeper processes through which cybersecurity readiness developed within complex institutional settings such as universities\~\\citep{Hakiem2023, Neri2024}.

These gaps jointly highlighted the need for an integrated analysis of cybersecurity readiness in HEIs. The study addresses these limitations by investigating individual behaviour interpretation and organisational cultural dynamics with methodological depth to capture institutional complexity.

\\section{Chapter Summary}  
\\label{sec:2.11}

This chapter summarised and assessed the literature on privacy decision-making, cybersecurity behaviour, organisational culture, and cybersecurity practices within higher education institutions. The review examined how individual reasoning processes and institutional environments influence cybersecurity behaviour in academic settings.

Protection Motivation Theory and Edgar Schein's Model of Organisational Culture provided the primary theoretical perspectives for analysing behavioural and organisational influences on cybersecurity cultural practices. The literature revealed that behavioural studies focued primarily on perceptions of individual privacy behaviour, while organisational research emphasised institutional norms, leadership, and governance structures. However, these perspectives are rarely examined together in higher education cybersecurity research.

To address these research gaps, this chapter developed an integrated conceptual framework that combined PMT with Schein's culture model. The framework explains how multiple factors influence the overall readiness of the organisation for cybersecurity in HEIs. The next chapter\~\\ref{chapter:c3}  presents the research design and methodological approach adopted to systematically investigate these relationships and operationalise the proposed framework.  
 

%=============================  
 

\\chapter{Research Design}  
\\label{chapter:c3}

%need to fix review comments%

\\section{Introduction}  
\\label{sec:into3}

Chapter \\ref{chapter:c2} reviewed the theoretical foundations of the literature that informs this study. This chapter outlines the research design, epistemological and methodological approaches adopted to investigate cybersecurity readiness in higher education institutions. It explains the rationale for selecting a qualitative, explanatory single-case study and justifies the use of theory-informed template analysis as the analytical framework. Considerations of research trustworthiness, ethical positioning, and potential bias are also addressed. Together, these sections establish the conceptual and methodological rationale for the implementation described in Chapter\~\\ref{chapter:c4}.

To support the orientation of the chapter Figure\~\\ref{fig:3.1} provides a roadmap of Chapter \\ref{chapter:c3} that summarises the structure and sequence of the methodological components discussed.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 3 Roadmap\]{%  
    \\textbf{Figure 3.1}\\\\\[1.2em\]  
    \\textit{Chapter 3 Roadmap}  
    }  
    \\label{fig:3.1}  
    
    % \\addcontentsline{lof}{figure}{3.1 \\hspace{0.18cm} Chapter 3 Roadmap}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c3/3.1roadmap.png}  
      
    \\begin{minipage}{1\\linewidth}  
        \\raggedright  
        \\text{}  
    \\end{minipage}  
\\end{figure}

  

\\section{Research Design Framework}  
\\label{sec:3.2}

A research design is a coherent plan that outlines data collection, analysis and storage to answer research questions and achieve study objectives, integrating epistemology, theory, methodology and methods \\citep{Bryman2016, Creswell2018research}.

For this study, a qualitative positivist approach was applied along with a single explanatory case study (see Section\~\\ref{sec:3.2.3}). The Protection Motivation Theory (PMT) and Schein's organisational culture theories provide a philosophical lens for understanding the data. Data were collected through semi-structured and expert interviews  \\citep{yin2018}. Figure\~\\ref{fig:3.2} summarises how these components are aligned across phases.\\\\

   
\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Summary: Structure of the Research Design Framework\]{%  
    \\textbf{Figure 3.2}\\\\\[1.2em\]  
    \\textit{Summary: Structure of the Research Design Framework}  
    }  
    \\label{fig:3.2}  
    
    % \\addcontentsline{lof}{figure}{3.2 \\hspace{0.18cm} Summary: Structure of the Research Design Framework}  
      
    \\includegraphics\[width=1.2\\linewidth\]{Figures//c3/3.2\_Design.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{\\\\Note.} Source \- Qualitative Positivism \\citep{Park2020}; Protection Motivation Theory behaviour \\citep{Maddux1983}; Edgar Schein Organisational Culture Theory \\citep{Schein2017}; Single Explanatory Case Study \\citep{yin2018}; Semi-Structured Interviews \\citep{Dejonckheere2019}; Template analysis \\citep{King2017}.  
    \\end{minipage}  
\\end{figure}

 

\\subsection{Epistemology}   
\\label{sec:3.2.1}

\\textit{Epistemology} is the study of knowledge formation, evaluation and sharing \\citep{Priya2021, Whittle2025}. Epistemology shapes how researchers generate and interpret knowledge. In this study, a qualitative positivist approach was adopted. In this paradigm, knowledge is generated through a systematic, structured approach. It asks how the world can be known and how this understanding, which involves analysing people's subjective experiences and interpreting the world, is communicated between people \\citep{Su2018}. Within this debate, positivism embraces an objectivist epistemology that seeks to describe and predict phenomena through visible evidence, measurement, and causal relationships \\citep{Sridharan2025}.

A research paradigm maintains reliability by aligning ontological, epistemological, and axiological assumptions with methodological choices \\citep{Creswell2018research}. Ontology exposes the nature of the reality being studied, epistemology addressed how reliable knowledge about that reality is determined, and axiology addresses how values and potential bias are managed throughout the research process\~\\citep{Berkovich2018, Lincoln2011}. 

This epistemological position supported the use of theory-informed qualitative methods that enabled thoughtful explanatory implications, a systematic comparison, and explicit justification of analytic decisions \\citep{Fletcher2017, Priya2021}. It provides a foundation for linking empirical reflections to an explanatory approach while maintaining methodological discipline and transparency.

Positivism is usually associated with quantitative methods, but it also influences qualitative research by adopting a systematic, objective, pattern-seeking approach within rich textual accounts \\citep{Goldkuhl2017, Park2020}. This study recognised that real-world social patterns existed, even when they could not be quantified.

\\subsubsection{Justification for Qualitative Positivism}

Qualitative positivism shaped the examination of organisational structures using qualitative data to mirror reality through an epistemological objectivist lens \\citep{Park2020}. Positivist accuracy seeks methodological trustworthiness by demonstrating that research procedures can be audited and that the data closely match the intended reality \\citep{Berkovich2018}. Recognising positivist qualitative work as a legitimate qualitative approach can enhance research quality and strengthen the case for fully positivist qualitative inquiry.

A qualitative approach was required because the phenomena under investigation, including individual privacy mindset, culture, leadership traditions, and governance arrangements, were context-dependent and not falsifiable to predefined variables \\citep{Creswell2018research}. Semi-structured interviews allowed participants to articulate decision-making processes, constraints, and assumptions in their own terms, while still allowing systematic comparison across cases and phases \\citep{Dejonckheere2019}.

The epistemological stance also justified the use of theory-informed template analysis. Established theories, including PMT theory and Schein's organisational culture model, were used as frameworks to guide initial analytic orientation, rather than as fixed structures for hypothesis testing. The coding template was processed iteratively as empirical evidence was gathered, allowing the analysis to remain receptive to data while maintaining a clear and auditable analytic approach \\citep{Brooks2015, King2017}. Collectively, these procedures aligned epistemology, design, and analysis, assisting cautious yet sound explanatory claims grounded in empirical evidence.

This epistemological position shaped how interview data were interpreted, encouraging attention to recurring organisational patterns \\citep{Whittle2025}. The analytical focus centred on explaining consistent behaviours, decision logistics, and structural influences observed across participants. Coding and theme decisions prioritised traceable, defensible links to data. This approach ensured rigorous, coherent interpretations throughout the study.

 

\\subsection{Underpinning Theory}   
\\label{sec:3.2.2}

This study was theoretically informed by Protection Motivation Theory (PMT) and Schein's model of organisational culture. Chapter \\ref{chapter:c2} discussed these theories conceptually within the literature review. This section explains their methodological relevance and justifies their selection as analytical lenses that guided the research design, interview development, and analytical strategy. Chapter \\ref{chapter:c4} then presents how these lenses were implemented within each empirical phase. 

These theories were applied as theory-informed lenses that structured the research design, guided the development of interview questions, shaped the initial analytic template, and supported cross-phase interpretation \\citep{Berkovich2018, Brooks2015, Golding2024, yin2018}. This research examined cybersecurity readiness in HEIs as both a behavioural and an organisational phenomenon. Individual employees interpreted cybersecurity risks and decided whether protective actions were necessary. At the same time, how organisational culture, leadership, and governance arrangements were played out in practice. Examining cybersecurity readiness is therefore essential to complement theoretical perspectives proficient in supporting both domains.

Methodologically, the theories guided several aspects of the study design. They informed the development of interview protocols by identifying the behavioural and cultural dimensions relevant to each phase of the research. They also provided an initial analytical orientation for template analysis (see Section \\ref{sec:4.7}) by identifying areas of inquiry linked to behavioural judgement and organisational culture. However, the theories were not applied as rigid coding structures. Instead, they provided interpretive guidance while allowing patterns to emerge from the empirical data.

The use of corresponding theoretical lenses also supported the explanatory case study design adopted in this research. PMT enabled analysis of individual cybersecurity reasoning during Phase 1 (Chapter\~\\ref{chapter:c5}), while Schein's framework supported examination of organisational culture during Phase 2 (Chapter\~\\ref{chapter:c6}). Their integration allowed cross-phase analysis of behavioural and cultural findings during Phase 3 (Chapter\~\\ref{chapter:c7}). In this way, the theories functioned as methodological foundations that linked the research questions, data collection procedures, and analytical framework.

\\subsubsection{Justification of Protection Motivation Theory:}

The theory was chosen because its constructs correspond closely with decision processes observed in cybersecurity behaviour research \\citep{Balla2024}. Employees routinely assessed the likelihood of security incidents, the potential consequences of those incidents, and their own capacity to respond effectively. These judgement processes align with PMT's threat appraisal and coping appraisal mechanisms \\citep{Latif2025, Tsai2016, Xiao2014}.

PMT was particularly suitable for the higher education context examined in this study \\citep{Hina2019}. Universities operate as decentralised environments in which cybersecurity behaviour often depends on individual judgement rather than direct supervision or mandatory enforcement \\citep{Brentzel2025}. Understanding how individuals interpret privacy risks, effort requirements, and protective actions therefore becomes essential for explaining security behaviour.

Observed vulnerability reveales the possibility of a cyber incident, while recognised severity concerns the potential consequences if an attack succeeds \\citep{Ifinedo2012}. When both experiences are strong, individuals are more likely to adopt protective measures. Coping appraisal then shapes response choices through perceived skill, belief in the effectiveness of safeguards, and the practical costs of acting \\citep{Balla2024}. Protective behaviour is habitually withdrawn when required effort, time, or distraction is judged to outweigh perceived risk \\citep{Latif2025}. This aligns with the research in understanding individual mindsets and the actions individuals may take.

Within the methodological design, PMT served as an interpretive framework for analysing participants' descriptions of cybersecurity reasoning \\citep{Kiran2025}. It helped identify how participants assessed risk, evaluated their capability to respond, and balanced security practices against common work demands. The theory therefore provided a structured approach for interpreting behavioural accounts without imposing predetermined outcomes on the analysis.

\\subsubsection{Justification of Schein's Organisational Culture Theory:}  
 

Edgar Schein's theories are known to have profoundly influenced studies on organisational leadership and culture, particularly in cybersecurity contexts where cultural alignment drives readiness \\citep{Adamu2025}. Schein's framework examined institutional influences on cybersecurity behaviour as an organisational lens. Culture manifested in artefacts, espoused values, and underlying assumptions \\citep{Schein2017, Venkat2020}.

Schein's theory is appropriate for this study because it uniquely probes underlying assumptions and values shaping behaviour, beyond surface artefacts \\citep{Adamu2025}. It offers deeper insight into organisational ‘cultural DNA' than frameworks emphasising visible elements alone \\citep{Schein2017}. 

Methodologically, Schein's framework provided a structure for analysing organisational conditions that shaped cybersecurity readiness. Schein's framework explains organisational control through policies, procedures, and norms. Researchers applied it to analyse how multi-level initiatives shaped employee beliefs, adopting desired cybersecurity cultural states \\citep{Adamu2025}. Individuals often ignore security when everyday reminders such as email and posters fade away, demonstrating the model's real-world fit \\citep{alshaikh2020, Dimitrov2013}. Its multiple layers help explain why organisational security discourse does not align with practice, showing how visible cues, stated values, and underlying beliefs shape cybersecurity actions day to day \\citep{Schein2017, Sutton2025}. This mindset can lead to a pretty careless approach to handling sensitive information \\citep{DaVeiga2020}. Schein's framework is a great tool for pinpointing these blind spots by highlighting where what we do visibly does not match up with our underlying beliefs \\citep{Adamu2025}. It's especially useful for uncovering the cybersecurity norms of higher education organisations, which tend to develop informally within faculties, departments, or even individual workgroups \\citep{Schein2019}.

\\subsection{Research Methodology}  
\\label{sec:3.2.3}

This study utilised a qualitative research approach, specifically adopting a single explanatory case study method \\citep{Crandall2019, yin2018}, to explore the complex, multi-dimensional nature of cybersecurity readiness within individual and organisational cultural depth.

\\subsubsection{Single Explanatory Case Study:}

The case study examined cybersecurity in a real-world institutional setting, drawing on an established social science method for researching complex organisational phenomena \\citep{Bada2019, Bhana2023, yin2018}. Case study research has a long, established history across disciplines and can support both quantitative and qualitative inquiry \\citep{Priya2021, Su2018}. A single explanatory case study involves rigorous investigation of a single specific case, examining a phenomenon's pattern to explain its causal relationships rather than simply describing them \\citep{Ishak2014}. This research reveals how individual reasoning and organisational culture interact to determine readiness \\citep{Adamu2025, Georgiadou2022}.

\\paragraph{Justification for a Single Explanatory Case Study:\\\\}

An explanatory case study was selected for its analytical value, as it reflected key characteristics of higher education environments, including decentralised governance, professional autonomy, and reliance on trust-based practices, rather than for statistical representativeness \\citep{Priya2021, yin2018}. 

An explanatory case study research address ‘how' and ‘why' questions and examines causal mechanisms within real-world contexts \\citep{Priya2021, Yazan2015, yin2018}. Where a single case study engages intensive analysis of a single unit \\citep{Ishak2014}, such as an organisation, and is perfect when the phenomenon's environmental boundaries are doubtful \\citep{Crandall2019, Jones2021}. Unlike multiple-case designs that highlight replication and cross-case associations, a single-case study facilitated deeper questioning of established relationships and exploration of emerging ones within the specific case \\citep{Ahmad2021, Creswell2018research}.

Single explanatory case studies have been widely used in cybersecurity and information systems research to explore socio-organisational dynamics, behavioural decision-making, and governance challenges in complex institutional settings \\citep{Crandall2019, Cruzes2014}. A case study is not merely a data-collection technique; it is a comprehensive research strategy for examining a unit \\citep{Priya2021}.

The case study approach is suitable for examining how technical factor, behavioural choices, and cultural factors interact to influence cybersecurity impact within organisations \\citep{Crandall2019, Priya2021}. Researchers often select a single-case strategy when the unit is critical to testing or extending a theory, signifiy an extreme or unusual instance, captures a regular, everyday condition, assists a revelatory purpose for previously unreachable phenomena, or provides longitudinal understanding \\citep{Su2018, yin2018}.

Cybersecurity and information systems have long used qualitative explanatory case studies to expose organisational security dynamics \\citep{Crandall2019, Garba2020}. In this study, the explanatory case design enabled integration of individual-level reasoning, organisational practices, and expert perceptions across multiple phases.

Alternative qualitative approaches were considered but rejected based on methodological fit. Grounded theory was unsuitable because the study was guided by established theoretical frameworks rather than aiming to generate theory inductively \\citep{Fletcher2017}. Phenomenology prioritises individual lived experience and does not align with the study's organisational and explanatory focus \\citep{Brooks2015}. Ethnography requires prolonged immersion and observation, which exceeded the scope of the study and was unnecessary for explanation-oriented aims \\citep{Miles2014}. Mixed methods would have introduced additional complexity without offering a clear analytical advantage over an in-depth qualitative explanation of mechanisms \\citep{Creswell2018research}.

Overall, the single explanatory case study design supported pattern matching, explanation building, and cross-phase comparison. This enabled the study to integrate individual, organisational, and expert evidence into a coherent account of cybersecurity readiness that is both theoretically grounded and practically relevant to higher education institutions \\citep{Crandall2019, Miles2014, Priya2021, yin2018}. This approach allowed the study to produce contextually based yet theoretically informed explanations that are both academically rigorous and practically relevant to higher education institutions.

Adopting a single explanatory case study approach, therefore, strenthened this research by facilitating a detailed analysis of complex, real connections that influence cybersecurity readiness within an organisational setting \\citep{Crandall2019, Priya2021}. This methodological choice encouraged both the depth and clarity of findings by allowing directed assessment of the factors.

 

\\subsection{Data Collection Method}   
\\label{sec:3.2.4}  
Data collection took place in three distinct phases (see Table\\ref{tab:3.1}). This phased approach allowed for the gradual improvement of explanations, where insights gained from earlier stages guided subsequent stages of the inquiry, supporting cumulative explanation building instead of descriptive findings \\citep{Creswell2018research, Miles2014}.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{5cm} p{2cm} p{2.8cm}}

\\caption\[Summary Structure and Purpose of the Three-Phase Data Collection\]{%  
\\\\\[1.2em\]  
\\textit{Summary Structure and Purpose of the Three-Phase Data Collection}  
\\label{tab:3.1}  
}  
\\\\

\\hline  
\\textbf{Phase (P)} & \\textbf{Purpose} & \\textbf{Link to RQs} & \\textbf{Proposed Output} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Phase (P)} & \\textbf{Purpose} & \\textbf{Link to RQs} & \\textbf{Proposed Output} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

P1 & To understand the potential impact of individual mental models of privacy. & RQ1 & Cybersecurity behaviour intention. \\\\ \\hline  
P2 & To understand the potential impact of organisational cybersecurity culture. & RQ2 & Organisational cybersecurity cultural mindset. \\\\ \\hline  
P3 & To validate the Phase 1 and Phase 2 findings through expert input. & RQ3 & Expert validation. \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
   
 

\\subsection{Data Analysis Method}   
 \\label{sec:3.2.5}

\\subsubsection{Template Analysis} 

Template analysis systematically organises qualitative data using a hierarchical coding template \\citep{Brooks2015, King2017}. Template analysis represents a distinctive thematic approach within qualitative data analysis \\citep{Burton2019}. Unlike fixed methods like grounded theory, it balances structure and flexibility through an evolving hierarchy of higher-order themes and sub-themes. 

\\paragraph{Template Analysis Workflow—Six Analytical Steps:\\\\}  
Template analysis is a six-step process \\citep{Brooks2015, Maguire2017}. The core procedural six steps (Figure\~\\ref{fig:3.3}) for conducting template analysis are detailed and outlined below. Each step represents a distinct stage in organising, refining, and stabilising themes across qualitative data.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 3 \- Six Steps of Template Analysis\]{%  
    \\textbf{Figure 3.3}\\\\\[1.2em\]  
    \\textit{Phase 3 \- Six Steps of Template Analysis}  
    }  
    \\label{fig:3.3}  
    
    % \\addcontentsline{lof}{figure}{3.3 \\hspace{0.18cm} Phase 3 \- Six Steps of Template Analysis}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c3/3.3Template6steps.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

   
 

\\begin{itemize}  
    \\item \\textbf{Step 1 (Familiarising with the Data):} The initial step in qualitative analysis is to read and re-read the interview transcripts to becomme familiarity with the actual data \\citep{Maguire2017}. Early notes captured recurring expressions and role-specific interpretive. They aimed to support understanding of the data instead of determining specific themes \\citep{Brooks2015, King2018}.  
      
    \\item \\textbf{Step 2 (Preliminary Coding):} Preliminary coding assigned initial labels to meaningful data segments. Codes remained provisional, allowing multiple interpretations. This supported early pattern recognition while preserving openness \\citep{Long2025}.  
      
    \\item \\textbf{Step 3 (Theme Organisation and Relationships):} Codes are grouped into broader categories to form an initial thematic structure. Relationships between themes and sub-themes are explored, resulting in a hierarchical organisation. This step is central to template analysis, as it transforms fragmented codes into a structured analytical framework \\citep{King2017}.  
      
    \\item \\textbf{Step 4 (Review of Themes):} Themes received systematic review for coherence and distinctiveness. Iterative refinement resolved overlaps and ambiguities. This strengthened analytical validity and conceptual clarity \\citep{Casey2023}.  
      
    \\item \\textbf{Step 5 (Defining and Naming Themes):} This step defined each theme's scope, meaning, and boundaries clearly. Concise, accurate names captured their essence. This enhanced interpretive precision and analytical consistency \\citep{Naeem2023}.  
      
    \\item \\textbf{Step 6 (Finalising the Template):} Final steps stabilise the coding template after theme refinement. The final template provided systematic analytical structure. It ensured transparent, auditable data-derived conclusions \\citep{Emerson2026, Long2025}.  
\\end{itemize}

\\subsubsection{Justification of Template Analysis:}  
Template analysis was utilised to organise and interpret the multi-phase interview data. Interview transcripts were analysed using template analysis, a structured yet adaptable form of thematic analysis centred on the iterative development and refinement of a coding template \\citep{Brooks2015, King2017}. 

Template analysis belongs to the wider family of thematic approaches but is distinguished by its explicit use of a hierarchically organised template that is repeatedly applied, revised, and stabilised across the dataset. This process facilitates the researcher to represent both conceptual relationships and patterned variation while supporting clear traceability between raw data, transitional coding decisions, and final themes \\citep{Burton2019, King2012}.

Template analysis was well-suited to this research for three main reasons. First, it aligned with the explicitly theory-informed design, allowing PMT Theory and Schein's organisational culture model to guide preliminary coding \\citep{Burton2019, King2017}. Second, it supported analytic stability across the three empirical phases, as the initial template (Section\~\\ref{sec:4.7.2}) was applied and adapted when moving from individual interviews to organisational and expert data \\citep{Brooks2015, Long2025}. Third, it aligned with the study's qualitative positivist stance by emphasising transparent procedures, versioned templates, and explicit decision trails, which enhanced credibility and dependability \\citep{Burton2019, King2017, Long2025}. 

This methodological structure reflects the study's qualitative positivist epistemology by treating patterned meanings as analysable features of organisational reality, while maintaining systematic and auditable analytic procedures.

\\subsubsection{Initial Template} 

In Template Analysis, researchers often begin by identifying a set of a priori themes to structure the initial template (see Section\~\\ref{sec:4.7.2}). The study adopted a top-down approach, obtaining directly from theory and literature to identify key a priori themes \\citep{King2018, Long2025}. An initial template is constructed from a priori themes developed before or during the early stages of analysis, which guide the organisation of qualitative data \\citep{Brooks2015, King2017}. Theory-derived themes guided early coding and aligned with objectives while allowing emergent patterns. The template evolved iteratively as codes were added, merged, or restructured \\citep{Brooks2015, Emerson2026, Long2025}.

\\section{Trustworthiness, Ethics, and Bias}  
\\label{sec:3.3}

Trustworthiness refers to the quality, credibility, and analytical integrity of qualitative research. It was addressed using four established criteria: credibility, transferability, dependability, and confirmability \\citep{Adler2022, Dejonckheere2019, Forero2018}. 

Credibility concerns the accuracy and plausibility of interpretations and was supported through the use of multiple data sources and iterative analysis \\citep{Dejonckheere2019}. Transferability relates to the extent to which findings may be applicable to similar contexts and was addressed through contextual clarity and detailed description \\citep{Brentzel2025}. Dependability refers to the consistency of the research process and was ensured through a structured and transparent analytical approach \\citep{Forero2018}. Confirmability concerns the neutrality of findings and was supported through reflexive awareness and systematic documentation of analytical decisions \\citep{Brentzel2025}.

   
Ethical considerations concerned the protection of participants, the responsible handling of data, and the integrity of the research process. These principles were particularly important in qualitative research, where data were derived from personal experiences and interpretations, requiring careful attention to consent, confidentiality, and respectful representation \\citep{Creswell2018research, Dejonckheere2019, Taherdoost2022}.

   
Qualitative research is inherently interpretive. Findings reflected researcher perspectives, participant narratives, and sampling choices \\citep{Adler2022, Dejonckheere2019}. Reflexive awareness, transparent procedures, and diverse participant selection managed these influences.

\\section{Chapter Summary}  
Chapter Three outlined the methodological foundations of the study and justified the research design in relation to the research aims. A single explanatory case study approach was adopted to examine how individual privacy beliefs and organisational culture shaped cybersecurity readiness in a higher education setting. Study data were collected through multiple phases with semi-structured interviews and analysed using template analysis. Ethical approval was obtained for all phases, and participants' consent, confidentiality, and data security were preserved throughout. Strategies to support trustworthiness and manage bias were rooted across data collection and analysis. With the methodological approach established, the next chapter presented the Phase 1 findings and discussion.

\\chapter{Implementation of the Research Design}  
\\label{chapter:c4}

\\setcounter{figure}{0}  
\\renewcommand{\\thefigure}{4.\\arabic{figure}}

 

\\section{Introduction}  
\\label{sec:4.1}

Chapter\~\\ref{chapter:c3} established the research design, epistemological position, and methodological justification. This chapter moves from design to execution. It explains how the study was implemented in practice and how theoretical, epistemological, and case study decisions were operationalised across three phases.

This chapter first outlines the research steps (Figure\~\\ref{fig:4.2}) and their sequencing. It then shows how epistemological assumptions informed analytical judgement. Next, it demonstrates how the underpinning theories were applied in data collection and analysis. Finally, it describes the single explanatory case study implementation and the three-phase data collection process, including semi-structured interviews, protocol design, sampling, and phase-specific participant engagement.

Subsequently, the chapter presents the data analysis approach, describing the tools used, the development of phase-specific initial templates, and the execution of template analysis across Phases 1, 2, and 3\. It concludes with a consolidated discussion of data saturation across phases and a summary of implementation outcomes. Figure\~\\ref{fig:4.1} provides a visual roadmap of the chapter structure to guide the reader through the sequence of implementation steps.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 4 Roadmap\]{%  
    \\textbf{Figure 4.1}\\\\\[1.2em\]  
    \\textit{Chapter 4 Roadmap}  
    }  
    \\label{fig:4.1}  
    
    % \\addcontentsline{lof}{figure}{4.1 \\hspace{0.18cm} Chapter 4 Roadmap}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c4/4.1roadmap.png}      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

\\section{Research Steps and Implementation Overview}  
\\label{sec:4.2}

The research followed a structured, multi-phase design aligned with the research questions and analytical objectives. The research implementation design (see Figure\~\\ref{fig:4.2}) enabled gradual improvement in understanding across phases while keeping the methods clear and transparent.\\\\

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Research steps (1-3) with Research Implementation Process.\]{%  
    \\textbf{Figure 4.2}\\\\\[1.2em\]  
    \\textit{Research steps (1-3) with Research Implementation Process.}  
    }  
    \\label{fig:4.2}  
    
    % \\addcontentsline{lof}{figure}{4.2 \\hspace{0.18cm} Research steps (1-3) with Research Implementation Process.}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c4/4.2\_Research\_steps.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

Figure\~\\ref{fig:4.2} focuses on the research implementation approach developed through three steps, linking individual privacy perceptions, organisational culture and expert validation. This design focuses more on guiding the methodological approach. 

\\paragraph{Research Step 1 and 2}

Step 1 semi-structured interviews explored privacy mental models and cybersecurity behavioural strategies among higher education participants. And step 2 involved semi-structured interviews with management, leaders, and operational employees examining organisational cultural practices, governance arrangements, and informal routines shaping cybersecurity in the HEI. This study developed Phase 1 and 2 initial templates (see Section\~\\ref{sec:4.7}) based on PMT theory and Schein's model, respectively. These initial templates guided interview protocols and preliminary coding for template analysis. Findings from both phases addressed Research Questions 1 and 2 (RQ1 and RQ2).

\\paragraph{Research Step 3: Phase 3 \- Expert Validation}

Experts reviewed and challenged findings from earlier phases (1 and 2). Step 3 analysed multi-source data and enabled cross-phase analysis (see Section\~\\ref{sec:4.7}) across phases. This stage strengthened explanatory coherence, boundary clarity, and practical significance. Expert input also sharpened theme boundaries, strengthened reliability, and improved the framework's transferability to the institutional contexts.

 

\\section{Epistemological Influence}  
\\label{sec:4.3}

Recall from Chapter \~\\ref{sec:3.2} that epistemology, the qualitative positivist stance, shaped how data were approached and interpreted during the implementation of the research design. In this study, interviews were conducted with attention to identifying patterned reasoning while still drawing on detailed, text-based evidence. Participant replies were examined for persistent behavioural logics, shared interpretations of privacy behaviour action and steady organisational influences. 

During coding and template modification, the analysis prioritised systematic comparison through cases and phases. Themes were preserved only where consistent patterns were observable and traceable to the data. Interpretations were required to demonstrate clear links between raw transcripts, coded segments, and higher-order explanations. This disciplined approach ensured that conclusions reflected patterned organisational realities rather than impressionistic interpretation, maintaining coherence with the study's explanatory case design.

 

\\section{Applying Underpinning Theories}  
\\label{sec:4.4}

\\subsection{Applying Protection Motivation Theory (PMT)}

PMT is a psychological framework that examines how individuals assess and respond to threats through individual judgment processes (see Section\~\\ref{sec:3.2.2}). In this study, PMT was applied primarily in Phase 1 to examine individual mental models, cybersecurity reasoning, and protective behaviour within the higher education institute (HEI) setting \\citep{Kiran2025, Tolsdorf2020}.

PMT informed the conceptual framework (Figure\~\\ref{fig:2.4}) by targeting analytical attention to individual privacy actions, underlying reasoning procedures, and intentions to engage in cybersecurity behaviours \\citep{Balla2024, Hina2019}. These structures are recognised as central to understanding security compliance behaviours, particularly within decentralised Higher Education Institutions, where security practices often rely on individual judgement \\citep{Hina2019}.  

In implementation, PMT created the Phase 1 interview protocol (Appendix\~\\ref{appendix:A}) by structuring questions about how participants appraised cybersecurity risks and decided whether to implement protective measures \\citep{Balla2024, Shillair2020}. Questions were established to explore perceived severity, vulnerability, response efficacy, self-efficacy, and response cost without explicitly naming these constructs, thereby preventing theoretical priming while allowing systematic comparison across phases \\citep{Latif2025, Shillair2020}. 

PMT also guided the construction of the Phase 1 initial template (Section\~\\ref{sec:4.7.2}) by providing a priori themes aligned with threat and coping appraisal components \\citep{Brooks2015, Long2025}. These structured the preliminary coding process and supported the identification of patterns in how participants understood privacy threats, evaluated their own protective capabilities, and formed behavioural intentions.

\\subsection{Applying Schein's Organisational Culture Theory}

Schein's organisational culture theory conceptualises culture as operating at three interconnected levels: artefacts, values, and underlying assumptions (see Section\~\\ref{sec:3.2.2}). In this study, the framework was applied in Phase 2 as an organisational lens to interpret how organisational cybersecurity culture became enabled, constrained, or normalised within routine institutional processes \\citep{Adamu2025, Schein2010, Sutton2025}. It directed analytical attention to visible structures, communication of leadership values and deeper assumptions shaping cybersecurity readiness beyond formal procedures or written policies \\citep{Dimitrov2013, Schein2019, Schein2017, Venkat2020}.

In implementation, Schein's framework guided the design of the Phase 2 interview protocol and the construction of the Phase 2 Initial Template \\citep{Brooks2015, King2017, yin2018}. Interview questions were structured to explore leadership interaction, onboarding practices, incident reporting routines, and governance processes as artefacts, alongside participants' views of institutional priorities and expectations as values. Probing encouraged reflection on taken for granted assumptions regarding responsibility, autonomy, trust, and tolerance for workarounds that influenced everyday cybersecurity behaviour. Recurring explanations were interpreted as indicators of cultural assumptions rather than isolated individual opinions \\citep{Adamu2025, Balozian2017, Schein2017}. These insights informed the Phase 2 Initial Template, which organised codes hierarchically according to Schein's three-level structure, supporting consistent analysis across organisational roles and responsibilities \\citep{Long2025, Nowell2017}.   

Together, PMT and Schein's framework enabled examination of cybersecurity readiness at both behavioural and organisational levels. This dual-lens approach allowed analysis of how individual privacy reasoning interacted with institutional culture to shape preparedness within HEIs.

\\section{Applying the Case Study Approach}

The single explanatory case was implemented by selecting one Australian public higher education institution as a bounded system through which the interaction between individual privacy mental models and organisational cybersecurity culture could be examined in depth. The case was chosen for three analytical reasons.

First, the institution exhibited structural characteristics central to the research problem, involving decentralised governance with multiple campuses, professional autonomy, distributed decision-making, and reliance on trust-based academic practices. These features created natural variation in how cybersecurity expectations were interpreted and enacted across roles, allowing examination of causal mechanisms linking individual reasoning to institutional culture.

Second, the organisation operated under national regulatory and compliance frameworks common to Australian higher education (TEQSA-registered provider), making it analytically typical rather than idiosyncratic. This strengthened theoretical transferability by situating findings within a recognised sectoral context.

Third, the researcher had official institutional access across multiple organisational levels (see Appendix\~\\ref{appendix:A} \-\~\\ref{appendix:C} for the data collection approval letter), enabling the collection of data from individual employees, senior leaders, and subject matter experts within a realistic organisational setting. This access supported cross-phase comparison within the same bounded environment, enhancing explanation building and pattern matching across individual, organisational, and expert levels.

    
\\section{Data Collection Implementation}  
\\label{sec:4.6}

As detailed in Chapter \\ref{chapter:c3} (see Section\~\\ref{sec:3.2}), the research stretched across three connected sequential phases. In practice, data collection occurred in a multi-layered interview, as showed process that moved from individual reasoning (Phase 1\) to organisational culture dynamics (Phase 2\) and finally to expert review and validation (Phase 3). Each phase maintained the same qualitative approach, yet the way participants were contacted, questioned and selected changed in line with the specific research objectives.

Semi-structured interviews formed the core data source throughout all phases. They were conducted with deliberate attention to role, context, and institutional position, so that responses were interpreted in relation to where they were situated within the case. Documentary materials and field notes were not treated as separate datasets but as contextual anchors that helped interpret the interviews. Sampling strategies were also implemented differently across phases. 

The following subsections explain how semi-structured interviews were enacted in practice, how interview protocols were operationalised, how snowball and purposive sampling were applied, and how data were gathered within each of the three phases. Together, these sections clarify how the research design moved from methodological intention to practical implementation.

\\subsection{Implement Semi-structured Interviews}  
Data collection interviews were conducted online and face-to-face, depending on participant availability \\citep{Lobe2022, Taherdoost2022}. Across the three phases, interviews typically lasted approximately one hour (60 minutes). Informed consent was obtained before the interview and recording. Contextual observations and immediate analytic reflections were documented in field notes and memos, forming part of the study's audit trail \\citep{Young2018}. The total number of participants (22) and their distribution across phases are detailed in this section. All interviews were conducted using secure face-to-face or secure online platforms (MS Teams) \\citep{Lobe2022, Long2025, Ahmad2025}. Audio recordings were transcribed accurately and managed using NVivo 15 to support systematic organisation, traceability, and transparent linkage between data, codes, and themes \\citep{McIntosh2015, Nowell2017, Woods2016, yin2018, Zamawe2015}.

Overall, the data collection strategy confirmed methodological coherence, transparency, and alignment with the study's qualitative explanatory research goals.

\\subsection{Apply Interview Protocol and Design}  
    Interview protocols were developed separately for each research phase (see Appendix\~\\ref{appendix:A}-\\ref{appendix:C}, respectively) and were informed by the study's theoretical positioning and research questions. The protocols ensured systematic mapping of core topics across interviews while allowing flexibility to reflect participants' roles, responsibilities, and organisational environments \\citep{Taherdoost2022}. This mapping ensured that the interview protocols translated abstract framework elements into observable discussion topics without constraining participant expression \\citep{Kallio2016, Taherdoost2022}. 

Questions began with general details about everyday routines before moving towards more focused discussion of security decisions, organisational culture practises, and institutional influences. This sequencing helped establish rapport and encouraged reflective responses \\citep{Kallio2016, Patton2015}. Consistency was maintained across phases through a shared core structure. Phase-specific factors were added to address distinct research questions. Openings and closures followed a common format to support continuity and comparability across interviews \\citep{Young2018}.

\\subsection{Participant Sampling}  
This study's target population consisted of individuals included students, academics, administrative staff, institutional leaders, and cybersecurity experts in HEIs. 

\\paragraph{Snowball Sampling for Phase 1:\\\\}   
Snowball sampling (see Section\~\\ref{sec:3.2.4}) was utilised in Phase 1 to recruit individuals whose privacy and cybersecurity behaviours were rooted in everyday institutional practice. Initial participants were recruited via organisational social emails, noticeboard posters, and informal references among higher degree research (HDR) students, academic staff, and administrative employees. Participants were invited to suggest others who could contribute relevant experiences related to privacy and cybersecurity behaviour. 

\\paragraph{Purposive Sampling for Phases 2 and 3:\\\\}   
Purposive sampling (see Section\~\\ref{sec:3.2.4}) was exercised in Phases 2 and 3 to recruit participants with organisational leadership roles and expert knowledge related to cybersecurity HEIs' governance.

Phase 2 purposive sampling selected senior administrators, managers, department heads, and academic leaders responsible for policy, governance, or operational oversight. These participants provided understanding of organisational culture, leadership behaviour, and institutional cybersecurity readiness.

In Phase 3, purposive sampling was exercised to recruit subject matter experts with recognised credentials and substantial professional experience in cybersecurity and higher education experience. Experts were required to have at least 10 years or more of relevant experience to support significant analysis and expose expert knowledge \\citep{Cronje2024}.

Potential participants were communicated directly by email and provided with an approved interview protocol outlining study aims, confidentiality, and consent. This selective recruitment assisted theoretical refinement and strengthened explanatory validity within the case study design \\citep{Creswell2018research}.

Figure\~\\ref{fig:4.3} shows how data collection progressed across Phases 1-3, showing progression from theory to evidence and explanation using colour groups. Phase 1 (yellow), 2 (blue), and 3 (green) align to accomplish RQ1, RQ2, and RQ3, in that order, following the top-to-bottom flow. The coloured sequence shows how understanding evolved across phases from behavioural intentions to organisational culture, to expert analysis, while keeping a cohesive narrative.

 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Data Collection Process Across Phases (1,2,3)\]{%  
    \\textbf{Figure 4.3}\\\\\[1.2em\]  
    \\textit{Data Collection Process Across Phases (1,2,3)}  
    }  
    \\label{fig:4.3}  
    
    % \\addcontentsline{lof}{figure}{4.3 \\hspace{0.18cm} Data Collection Process Across Phases (1,2,3)}  
      
    \\includegraphics\[width=0.9\\linewidth\]{Figures//c4/4.3datacollection.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

\\paragraph{Recruitment Process:}   
Recruitment was initiated following institutional ethics approval (see Appendix\~\\ref{appendix:A}-\~\\ref{appendix:C}) and was tailored to each phase's analytical purpose. Phase 1 used campus notices, mailing lists, direct invitations, and referrals to reach individuals, while Phases 2 and 3 relied on targeted invitations through institutional directories and professional networks to recruit leaders and domain experts. To minimise power imbalance, no participant had a supervisory relationship with the researcher. Interviews were conducted at participants' convenience, either on campus or securely online, with written consent and withdrawal rights upheld in line with institutional ethics requirements and the \\textit{Australian Code for the Responsible Conduct of Research} \\citeyearpar{NHMRC2018}.

\\paragraph{Sampling Criteria:}  
Sampling criteria were applied to ensure that all participants could provide relevant and credible insight into cybersecurity and privacy within higher education backgrounds. Participants were required to have direct or recent involvement within a HEI's environment. They also needed experience or awareness of privacy practices, data management, or cybersecurity-related behaviour. All participants were adults who provided informed consent prior to participation. Individuals without an institutional connection or practical engagement with cybersecurity were excluded to prevent speculative or abstract responses \\cite{Patton2015}. 

\\paragraph{Participant Groups and Cohorts:}   
Participants were grouped into three cohorts aligned with the study's phases. Phase 1 involved higher degree research (HDR) students, academic staff, and administrative employees to capture everyday privacy reasoning and security behaviour in different roles and duties. Phase 2 involved senior leaders, managers, and departmental heads to examine how organisational culture, governance, and leadership signals shaped those behaviours, given their reliability for policy interpretation and institutional direction. Phase 3 engaged cybersecurity and policy experts to critically assess and refine interpretations, ensuring explanatory validity ahead of a single organisational context. Collectively, these cohorts enabled analysis across individual, organisational, and expert levels of influence on cybersecurity readiness.  
 

\\subsection{Interviews with Participants in Each Phase}  
\\label{sec:4.6.4}

\\subsubsection{Phase 1 (P1): Individual Participant Interviews}

\\paragraph{P1-Participant Recruitment Process:}  
Phase 1 recruitment utilised snowball sampling to gather participants for interviews. Organisational social media yielded one respondent; campus notices attracted six expressions of interest; and emails reached eight potential participants (number of participants \=n). Formal follow-up confirmed seven interviewees from diverse roles and institutional settings\~\\citep{Creswell2018research, yin2018} (Figure\~\\ref{fig:4.4}). 

\\paragraph{P1-Participant Profile and Interview Environment:}  
Phase 1 included seven participants (one female, six males participants) from the case institution, comprising experienced professionals and young researchers. All protocols, consent, and ethics were approved as outlined in Appendix\~\\ref{appendix:A}.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 1 \- Participant Recruitment Process\]{%  
    \\textbf{Figure 4.4}\\\\\[1.2em\]  
    \\textit{Phase 1 \- Participant Recruitment Process.}  
    }  
    \\label{fig:4.4}  
    
    % \\addcontentsline{lof}{figure}{4.4 \\hspace{0.18cm} Phase 1 \- Participant Recruitment Process}  
      
    \\includegraphics\[width=0.9\\linewidth\]{Figures//c4/4.4\_P1-Recruitment.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

 

\\paragraph{P1- Participant Profile and Interview Setting:}  
Phase 1 included seven participants (one female, six males participants) from the case institution, comprising experienced professionals and young researchers. All protocols, consent, and ethics were approved as outlined in Appendix\~\\ref{appendix:D}. 

Tables\~\\ref{tab:4.1} and Appendix\~\\ref{appendix:D} are provided to improve transparency and analytic traceability. Table\~\\ref{tab:4.1} situates participants within their organisational and professional contexts, supporting the interpretation of individual cybersecurity reasoning. Appendix\~\\ref{appendix:D} details interview conditions and consent to demonstrate procedural consistency and ethical compliance across data collection. The table includes interview modality, duration, location, and consent status.

Table\~\\ref{tab:4.1} summarises participant profiles, including role, department, qualifications, and prior experience.

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.2cm} p{1.5cm} p{1.0cm} p{2.0cm} p{1.5cm} p{2.0cm} p{2.0cm}}

\\caption\[Phase 1 \- Interviewee Profiles\]{%  
\\\\\[1.2em\]  
\\textit{Phase 1 \- Interviewee Profiles}  
\\label{tab:4.1}  
}  
\\\\

\\hline  
\\textbf{Pseudonym} & \\textbf{Gender} & \\textbf{Age} & \\textbf{Profession/ Title} & \\textbf{Department of Work} & \\textbf{Qualifications} & \\textbf{Previous experience} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Pseudonym} & \\textbf{Gender} & \\textbf{Age} & \\textbf{Profession/ Title} & \\textbf{Department of Work} & \\textbf{Qualifications} & \\textbf{Previous experience} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Interviewee 1 (P1-001) & M & 27 & HDR (PhD) Student & IISS & Information Technology & No \\\\ \\hline  
Interviewee 2 (P1-002) & M & 34 & HDR (PhD) Student & IISS & Information Technology & 3+ years in Academic Teaching \\\\ \\hline  
Interviewee 3 (P1-003) & F & 33 & Academic Teaching Staff & IISS, GPS & Information Technology & 1 year in an IT company \\\\ \\hline  
Interviewee 4 (P1-004) & M & 32 & Academic Teaching Staff & IISS, GPS & Information Technology & No \\\\ \\hline  
Interviewee 5 (P1-005) & M & 45 & International Reporting Officer & Administration / Compliance & Administration & 13+ years of experience in Administration \\\\ \\hline  
Interviewee 6 (P1-006) & M & 42 & Academic Teaching Staff & GPS Employee & Researcher, Administration & 10+ years of Research experience \\\\ \\hline  
Interviewee 7 (P1-007) & M & 31 & HDR (PhD) Student & IISS & Information Technology & 2.2 years of experience in an IT company \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Phase 2 (P2): Organisational Participant Interviews}

\\paragraph{P2 \- Participant Recruitment Process:}  
Recruitment focused on senior academics, managers, and department leaders within the case institution. Recruitment began with a review of the organisation's internal directory and communication tools (organisational employee portal, Microsoft Teams, and Outlook email). Personalised invitation emails were sent to 26 potential participants, explaining the study's purpose, confidentiality protocols, and voluntary participation. Figure \\ref{fig:4.5} summarises the recruitment flow and participation outcomes for Phase 2.\\\\

\\begin{figure} \[H\]  %\[\!ht\]   
    \\centering  
        \\captionsetup{labelformat=empty,justification=raggedright,singlelinecheck=false}  
    \\caption\[Phase 2 \- Participant Recruitment Process\]{\\textbf{Figure 4.5}\\\\\[0.5ex\]  
    \\textit{Phase 2 \- Participant Recruitment Process.}}  
    
    % \\addcontentsline{lof}{figure}{4.5 \\hspace{0.18cm} Phase 2 \- Participant Recruitment Process}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c4/4.5\_P2-Recruitment.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
      
    \\label{fig:4.5}  
\\end{figure}

 

\\paragraph{P2 \- Participant Profile and Interview Environment:}  
Eight (n=8) agreed to participate in Phase 2, representing senior leadership, academic management, and administrative governance roles across multiple functional areas. This cohort provided insight into how cybersecurity priorities were interpreted and enacted at the organisational level.

Table \\ref{tab:4.2} support organisational-level explanation by clarifying participants' positional authority, governance reach, and operational scope. Table \\ref{tab:4.2} establishes the leadership perspective in which cybersecurity decisions were influenced, including institutional span and team size, which are central to interpreting cultural influence. Appendix\~\\ref{appendix:E} records interview conditions to demonstrate consistency, access constraints, and ethical compliance across senior-level engagement.It showes interview format, duration, location, and consent status. Before taking part, all participants gave their written informed consent.

Table\~\\ref{tab:4.2} summarises participant profiles, including role, department, institutional tenure, and team size.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.2cm} p{1.5cm} p{1.0cm} p{2.5cm} p{1.5cm} p{2.0cm} p{1.5cm}}

\\caption\[Phase 2 \- Interviewee Profiles\]{%  
\\\\\[1.2em\]  
\\textit{Phase 2 \- Interviewee Profiles}  
\\label{tab:4.2}  
}  
\\\\

\\hline  
\\textbf{Pseudonym} & \\textbf{Gender} & \\textbf{Age} & \\textbf{Profession/ Title} & \\textbf{Department of Work} & \\textbf{Connected with the University} & \\textbf{Team Size} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Pseudonym} & \\textbf{Gender} & \\textbf{Age} & \\textbf{Profession/ Title} & \\textbf{Department of Work} & \\textbf{Connected with the University} & \\textbf{Team Size} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Interviewee 1 (P2-001) & Male & 54 & Senior / Professor & IISS & 28 years & 8-10+ \\\\ \\hline  
Interviewee 2 (P2-002) & Male & 53 & Partner Academic Lead & IISS & 20 years & 20+ \\\\ \\hline  
Interviewee 3 (P2-003) & Female & 47 & Senior Manager & Administration & 28 years & 25+ \\\\ \\hline  
Interviewee 4 (P2-004) & Female & 42 & Senior / Professor & IISS & 2 years & 9-12+ \\\\ \\hline  
Interviewee 5 (P2-005) & Male & 64 & Senior / Professor / Head & Engineering & 27 years & 25+ \\\\ \\hline  
Interviewee 6 (P2-006) & Male & 44 & Professor & IISS & 3 years & 5-10+ \\\\ \\hline  
Interviewee 7 (P2-007) & Male & 55 & Senior / Professor & IISS & 22 years & 8-13+ \\\\ \\hline  
Interviewee 8 (P2-008) & Male & 56 & Management \\& Academic Leader & IISS & 2 years & 45+ \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Phase 3 (P3): Expert Interviews}

\\paragraph{P3 \- Participant Recruitment Process:}  
Experts were identified through professional networks, organisational website profiles, and prior research engagement. Initial email invitations were sent to 11 potential participants outlining the study purpose, ethical safeguards, and interview expectations, along with the attached interview protocol and participant consent form. Non-respondents were followed up with after two to three weeks, resulting in further communication with several candidates, although some declined due to time constraints or did not respond after follow-up. Through this staged process, seven participants ultimately provided written consent and completed the interviews, demonstrating a transparent, iterative recruitment pathway. Figure \\ref{fig:4.6} summarises the recruitment flow and participation outcomes for Phase 3\.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 3 \- Participant Recruitment Process\]{%  
    \\textbf{Figure 4.6}\\\\\[1.2em\]  
    \\textit{Phase 3 \- Participant Recruitment Process.}  
    }  
    \\label{fig:4.6}  
    
    % \\addcontentsline{lof}{figure}{4.6 \\hspace{0.18cm} Phase 3 \- Participant Recruitment Process}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c4/4.6\_P3-Recruitment.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
 

\\paragraph{P3 \- Participant Profile and Interview Environment:}  
Seven (n=7) experts participated in Phase 3, representing cybersecurity experts, leadership, policy, and organisational authority roles across higher education and related sectors. This cohort provided professional perspectives for assessing the robustness and applicability of the study's findings. Detailed Phase 3 data validation outcomes are reported in Chapter\~\\ref{chapter:c6}, where expert insights are integrated into the cross-phase synthesis. The diversity of roles strengthened the credibility and transferability of the validation exercise by aligning academic interpretation with institutional practice.

Table\~\\ref{tab:4.3} summarises the professional profiles of the expert participants, while Appendix\~\\ref{appendix:F} details interview conditions and consent to demonstrate procedural consistency and ethical compliance across data collection. It presentes interview modality, duration, location, and consent status.

Appendix\~\\ref{appendix:F} documents the Phase 3 interview environment and consent details. All interviews were conducted online via Microsoft Teams under an approved ethical guidances, audio recorded with consent, and transcribed verbatim.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.2cm} p{1.5cm} p{1.0cm} p{2.8cm} p{3.5cm} p{1.8cm}}

\\caption\[Phase 3 \- Interviewee Profiles\]{%  
\\\\\[1.2em\]  
\\textit{Phase 3 \- Interviewee Profiles}  
\\label{tab:4.3}  
}  
\\\\

\\hline  
\\textbf{Pseudonym} & \\textbf{Gender} & \\textbf{Age} & \\textbf{Profession/ Role} & \\textbf{Key Expertise} & \\textbf{Year of experience} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Pseudonym} & \\textbf{Gender} & \\textbf{Age} & \\textbf{Profession/ Role} & \\textbf{Key Expertise} & \\textbf{Year of experience} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Interviewee 1 (P3-001) & Male & 54 & Senior IT/ Development/ Researcher & IT strategy, research, consultancy & 20 years+ \\\\ \\hline  
Interviewee 2 (P3-002) & Male & 53 & IT/ Development / Lecturer & Software development, teaching & 10 years+ \\\\ \\hline  
Interviewee 3 (P3-003) & Male & 47 & IT / Researcher/ Development & Cybersecurity, systems design, research leadership & 40 years+ \\\\ \\hline  
Interviewee 4 (P3-004) & Male & 42 & Professor / Researcher of IT \\& Cyber-security / Consultant & Cyber-risk analysis, research supervision, advisory & 28 years+ \\\\ \\hline  
Interviewee 5 (P3-005) & Male & 64 & Professor / Researcher of IT \\& Cyber-security / Consultant/ Trainer & Cybersecurity, systems design, research leadership, consultant, training & 14 years+ \\\\ \\hline  
Interviewee 6 (P3-006) & Female & 44 & Senior / Professor / Head & Research, leadership, consultancy, training & 20 years+ \\\\ \\hline  
Interviewee 7 (P3-007) & Male & 55 & Professor / Researcher of IT \\& Cyber-security / Consultant/ Trainer & Cybersecurity, systems design, research leadership, consultancy, training & 22 years+ \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

\\section{Data Analysis Approach}  
\\label{sec:4.7}

Data analysis was conducted using template analysis, implemented in a structured yet iterative manner across all three phases. Although the same six-step analytical logic was followed throughout, each phase began with a distinct initial template (see Section\~\\ref{sec:4.7.2}) aligned to its theoretical lens and research objective. Phase 1 was guided by Protection Motivation Theory, Phase 2 by Schein's organisational culture theory, and Phase 3 by cross-phase analysis and expert validation.

Templates were developed, applied, challenged, revised, and stabilised within each phase before moving to the next. This ensured continuity in analytical procedure while allowing theoretical orientation and coding emphasis to shift appropriately between individual, organisational, and expert data. The subsections that follow outline the tools used, the development of phase-specific initial templates, and the implementation of the six-step template analysis process in each phase.

The following section first outlines the analytical tools that supported this process before detailing the development and application of the phase-specific templates.

\\subsection{Data Analysis Tools}  
\\label{sec:4.7.1}

NVivo 15 (QSR International) was used to handle and analyse qualitative interview data across all phases. Qualitative research using qualitative data analysis software (QDAS) software supports systematic organisation of large text datasets and assisted transparent connection between coded excerpts, analytic memos, and evolving templates \\citep{Woods2016, Zamawe2015}. The use of NVivo ensured structured data management and traceable analytic decision-making appropriate for a multi-phase qualitative case study \\citep{Bonello2019, Maher2018}.

Transcribed interviews were imported into NVivo 15, where the data were coded and revisited through several analytic cycles. The use of codes supported systematic organisation and retrieval of participant responses, enabling comparison across roles and cases \\citep{Bingham2021, Choejey2018, Woods2016}. This structured data management approach supported transparency and auditability during iterative analysis \\citep{Miles2014}.

To enhance structural clarity and communicate the analytical process visually, chapter roadmaps, analytical figures, and coding diagrams were developed using the Draw.io online diagramming platform.

Data analysis followed a six-step template analysis workflow (see Section\~\\ref{sec:3.2}), adapted from established guidance \\citep{Brooks2015, Brooks2014, Maguire2017}. These steps incorporated an iterative coding progression from open exploration to stable thematic interpretation.

\\subsection{Initial Template in Phases}  
\\label{sec:4.7.2}

Following the development of the conceptual framework (Figure\~\\ref{fig:2.4}) and the selection of analysis, phase-specific initial templates were developed to operationalise the theoretical constructs during data collection and analysis (see Section\~\\ref{sec:3.2.4} and \~\\ref{sec:3.2.5}). An initial template is a preliminary coding structure derived from theory to guide early engagement with qualitative data while remaining open to refinement \\citep{King2017, Miles2014}.

In this study, the initial templates translated abstract framework components into analytic domains that shaped both interview design and preliminary coding. They align between research questions and empirical without limiting how participants articulated their experiences. As analysis evolved, codes were revised, merged, or expanded where participant conversation diverged from initial expectations, reinforcing the iterative nature of template analysis.

\\subsubsection\*{Phase 1 Initial Template:}  
The Phase 1 initial template was structured from prior theory-informed themes resulting from PMT Theory. This Initial Template provided an early conceptual map of the multiple factors influencing individual cybersecurity behaviour across the four main domains, as shown in Figure\~\\ref{fig:4.7} : Knowledge and Experience, Threat, Coping, and Behaviour Intention. These prior themes and sub-themes were developed before analysis and served as the initial analytic structure for Phase 1.\\\\

\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 1 Initial Template\]{%  
    \\textbf{Figure 4.7}\\\\\[1.2em\]  
    \\textit{Phase 1 Initial Template.}  
    }  
    \\label{fig:4.7}  
    
    % \\addcontentsline{lof}{figure}{4.7 \\hspace{0.18cm} Phase 1 Initial Template}  
      
    \\includegraphics\[width=0.5\\linewidth\]{Figures//c4/4.7\_P1-InitialTemplate.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{\\\\Note.} Format Adopted From "Optimising data sharing whilst protecting participant privacy: a data note describing processed data from a qualitative study of healthcare professionals’ experiences of caring for women with false positive screening test results" (p.11), by\~\\citep{Long2025}, (https://doi.org/10.1080/21642850.2024.2449400).Open Access article  
    \\end{minipage}  
\\end{figure}

 

 

\\subsubsection\*{Phase 2 Initial Template:}  
The Phase 2 initial template was constructed from prior themes derived from Schein's organisational culture model and informed by the individual behaviour patterns identified in Phase 1\. As shown in Figure\~\\ref{fig:4.8}, the Initial Template was organised into two primary domains (prior theme and sub-themes): Organisational Culture (artefacts, values, assumptions) and Individual Behaviour. The inclusion of Individual Behaviour ensured continuity with Phase 1 findings and allowed examination of how organisational conditions shaped behavioural responses.

\\begin{figure} \[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 2 Initial Template\]{%  
    \\textbf{Figure 4.8}\\\\\[1.2em\]  
    \\textit{Phase 2 Initial Template.}  
    }  
    \\label{fig:4.8}  
    
   
      
    \\includegraphics\[width=0.5\\linewidth\]{Figures//c4/4.8\_P2-InitialTemplate.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
                \\textit{\\\\Note.} Format Adopted From "Optimising data sharing whilst protecting participant privacy: a data note describing processed data from a qualitative study of healthcare professionals’ experiences of caring for women with false positive screening test results" (p.11), by\~\\citep{Long2025}, (https://doi.org/10.1080/21642850.2024.2449400).Open Access article  
    \\end{minipage}  
\\end{figure}

 

 \\subsection{Cross-Phase Analysis}  
 \\label{sec:4.7.3}

 

Phases 1 and 2 were analysed using template analysis, while Phase 3 involved cross-phase integration of findings. Cross-phase analysis refers to bringing together insights from different stages of a study to examine how they relate, reinforce, or challenge one another, rather than treating each phase separately \\citep{Golding2024, Sadri2025}. In this study, individual-level findings from Phase 1, guided by Protection Motivation Theory, were examined alongside organisational patterns identified in Phase 2 through Schein's model. This allowed assessment by experts in Phase 3 to strengthen coherence and practical relevance.

\\subsection{Data Analysis in Phases}   
\\label{sec:4.7.4}

Following data collection, analysis was undertaken separately within each phase. Phases 1 and 2 applied the six-step template analysis process outlined in Chapter\~\\ref{chapter:c3}, whereas Phase 3 employed cross-phase analysis for expert validation. Although the overall procedural logic remained consistent, each phase used a distinct initial template aligned with its theoretical lens and research objective.

   
The subsections that follow explain how template analysis and cross-phase analysis were operationalised in each phase, showing how interview data progressed from preliminary coding to stable thematic interpretations.

\\subsubsection{Phase 1 \- Data Analysis} 

This section presents the data analysis from Phase 1 of the study. The analysis focuses on how individual participants understood privacy and how these understandings shaped their cybersecurity-related intentions and behaviours. Data were analysed using the six-step template analysis method described in Chapter 3 (see Section\~\\ref{sec:3.2.5}). Thorough coding workflows and the Phase 1 codebook are provided in Appendix\~\\ref{appendix:D}. 

\\paragraph{Step 1 (Familiarising with the Data):}   
All Phase 1 transcripts were read repeatedly to build familiarity with participants' language, reasoning patterns, and decision cues. Attention was given to how participants described privacy, cybersecurity actions, and uncertainty in their own words, before fitting responses into predefined categories at this stage. This early engagement supported sensitivity to nuance and prepared the ground for later coding. These early observations informed the organisation of initial labels in the next analytic step. These labels captured how participants understood privacy risk, justified individual actions, and steered hesitation.

\\paragraph{Step 2 (Preliminary Coding):}   
Following familiarisation, preliminary (Initial) coding focused on organising participants' responses into an initial analytic code structure. At this stage, transcripts were coded by the researcher line by line to capture how participants described privacy, protection risks, and everyday decision-making in their own terms. The Initial Template supported this early stage by guiding the development of initial codes aligned with the study's analytic focus. The aim was not to fix meaning, but to surface patterns that reflected participants' immediate understandings and concerns.

The first NVivo coding cycle generated 36 distinct codes, supported by 556 coded references (Version 1 as V1). Figure\~\\ref{fig:4.9} presents a sample of NVivo coding (see Appendix\~\\ref{appendix:D} for detailed codebook information). Most of the codes aligned with the Phase 1 Initial Template domains, particularly knowledge and experience, perceived threat, coping judgements, and behavioural intentions. These included expressions of uncertainty about escalation, informal advice-seeking, and situational decision-making shaped by convenience. This approach allowed the analysis to remain open at an early stage, supporting later refinement as patterns became clearer across interviews.\\\\

 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 1 \- Version 1 NVIVO Coding sample\]{%  
    \\textbf{Figure 4.9}\\\\\[1.2em\]  
    \\textit{Phase 1 \- Version 1 NVIVO Coding sample.}  
    }  
    \\label{fig:4.9}  
    
    % \\addcontentsline{lof}{figure}{4.9 \\hspace{0.18cm} Phase 1 \- Primary (V1) NVIVO Coding sample}  
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures//c4/4.9\_P1-nvivo1.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}    
    \\end{minipage}  
\\end{figure}

\\paragraph{Step 3 (Theme Organisation and Relationships):}   
The second analytic cycle focused on organising preliminary codes into more coherent combinations and examining relationships across the Phase 1 dataset to search for themes. Building on the coding structure in Version 1 (V1), the analysis re-examined coded segments to discover overlap, convergence, and recurring patterns across participants.

During this stage, codes that reflected similar meanings or related decision perspectives were reviewed together. Redundant labels were merged, loosely defined codes were clarified, and several items were repositioned to better reflect their analytic role within the Phase 1 Initial Template. 

As the next analytical step, the coding structure was consolidated to 17 core codes and 38 subcodes, supported by 369 quotations in NVivo (Version 2 as V2). These codes were organised more clearly around participants' reported intentions, decision triggers, and responses to cybersecurity-related situations. The refined structure enabled clearer comparison across interviews and highlighted consistent relationships between perceived risk, confidence in action, and everyday behavioural choices.

The accompanying NVivo visualisations Figure\~\\ref{fig:4.10} (see more in Appendix\~\\ref{appendix:D}, Phase 1 codebook) support transparency by showing how findings were grouped under each code. These visual outputs were used to check internal coherence and consistency of patterns across the dataset. This step marked the transition from broad exploratory coding to a more stable analytic structure, providing the foundation for reviewing pre-themes and generating final themes in the next step.\\\\

   
   
\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 1- Version 2 NVivo coding sample\]{%  
    \\textbf{Figure 4.10}\\\\\[1.2em\]  
    \\textit{Phase 1- Version 2 NVivo coding sample.}  
    }  
    \\label{fig:4.10}  
    
    % \\addcontentsline{lof}{figure}{4.10 \\hspace{0.18cm} Phase 1- Version 2 NVivo coding sample}  
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures//c4/4.10\_P1-nvivo2.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}    
    \\end{minipage}  
\\end{figure}

% \[Insert V2 NVivo Example Figure here\]

\\paragraph{Step 4 (Review of Theme):}   
Building on the refined coding structure (V2) established in the previous step, the analysis focused on reviewing pre-themes (initial template), assessing their internal coherence and distinctiveness, and determining whether they warranted consolidation into higher-level themes.

The final analytic cycle (Version 3 as V3) resulted in an established coding structure consisting of 16 codes and 36 subcodes, confirmed by 380 referenced quotations throughout the Phase 1 dataset (Figure\~\\ref{fig:4.11}). At this point, no additional restructuring was required, and the analytic focus shifted from code refinement to interpretive combination. This stage summarises the multiple coding iterations in Phase 1, revealing how initial codes were refined into a stable thematic structure (Appendix\~\\ref{appendix:D}). 

From this process, five final themes were generated. The themes were derived by aligning stabilised codes with the original Phase 1 Initial Template, ensuring continuity between the conceptual framework and the empirical data.\\\\

 

 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 1- Version 3 NVivo coding sample\]{%  
    \\textbf{Figure 4.11}\\\\\[1.2em\]  
    \\textit{Phase 1- Version 3 NVivo coding sample.}  
    }  
    \\label{fig:4.11}  
    
   
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures//c4/4.11\_P1-nvivo3.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}    
    \\end{minipage}  
\\end{figure}

% \[Insert V3 NVivo Example Figure here\]

\\paragraph{Step 5 (Review the Theme):}   
This fifth step of template analysis presents the five themes generated in Phase 1 (P1-T1 to P1-T5) (see details in Phase 1 Research Findings, Section\~\\ref{sec:5.2.2}). Each theme is introduced through a brief analytic explanation and supported by delicately selected participant quotations. Collectively, the themes explain how participants made sense of privacy-related risks and acted on those interpretations in practice. Detailed codes and supporting NVivo outputs are provided in Appendix\~\\ref{appendix:D}. 

\\paragraph{Step 6 (Finalising the Template and Update):}   
Phase-1 analysis ressulted in a refined five refined analytical themes capturing how individual experiences, perceptions, and organisational signals interact to shape cybersecurity readiness.   

Chapter \\ref{chapter:c5} presented the Phase 1 findings and discussion, with Figure\~\\ref{fig:5.2} illustrating the final analytical template emerging from the thematic analysis. In this template analysis, the sixth step finalised the template, prioritising analytical depth over breadth. Its hierarchical structure preserved complexity, with multiple codes nested under each theme.

\\subsubsection{Phase 2 \- Data Analysis} 

The analysis in Phase 2 began with purposive sampling to ensure that participants reflected the organisational roles relevant to the study (see details in Section\~\\ref{sec:3.2.4}). Template analysis was then applied since it offered a structured framework that allowed adaptability across interview conversations \\citep{Brooks2015, Kiger2020, King2017}. Ideas from \\citeauthor{Braun2021} \\citeyearpar{Braun2021} supported the wider qualitative logic applied throughout the study. The method enabled detailed theme construction while maintaining transparency at each stage. The analytic procedure followed the template analysis steps (1 \- 6\) outlined in this section.

\\paragraph{Step 1 (Familiarising with the Data):}   
Instead of treating transcription as an automatic process, the researcher followed a process of thoughtful review and fine-tuning of each transcript \\citep{McMullin2023, Oliver2005}, were common speech fillers (for example, 'um', 'uh-huh', 'hmmm', 'you know', 'like') were removed where they did not contribute to logical meaning, a practice consistent with qualitative transcript conventions \\citep{Oliver2005, Stuckey2014}. The fact should be noted that the transcripts produced were a filtered version of the initial dialogue; whilst retaining the essential meaning, some of the emotional richness and freshness of the actual interviews are lost \\citep{McMullin2023}. The research used thematic content analysis because it offered a qualitative approach to discover meaningful patterns within the gathered data \\citep{Bingham2021}.

\\paragraph{Step 2 (Preliminary Coding):}  
In Phase 2 of the research, the same intense data familiarisation process was utilised, adopting the designated template analysis process set out by \\citet{Brooks2015}, as well as \\citet{King2017}. During the preliminary coding stage, transcripts were examined line by line to generate a set of codes, using the Initial Template (Section\~\\ref{sec:4.7.2}) as a guideline \\citep{Azungah2018, Linneberg2019, Long2025}. 

This preliminary coding produced 66 codes in NVivo with the help of 381 precise quote references (Figure\~\\ref{fig:4.12}). These codes were the first version of the coding, Version 1 (V1), classified according to the study's Initial Template. Following preliminary coding, the Phase 2 dataset was consolidated into a coherent coding structure through iterative refinement. Details of the full Phase 2 codebook and coding structure are provided in Appendix\~\\ref{appendix:E}.

   
\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 2 \- Version 1 (V1) NVivo coding sample\]{%  
    \\textbf{Figure 4.12}\\\\\[1.2em\]  
    \\textit{Phase 2 \- Version 1 (V1) NVivo coding sample.}  
    }  
    \\label{fig:4.12}  
    
    % \\addcontentsline{lof}{figure}{4.12 \\hspace{0.18cm} Phase 2 Version 1 (V1) NVivo coding sample}  
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures//c4/4.12\_P2-nvivo1.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}    
    \\end{minipage}  
\\end{figure}

% \[Note: Aligned with Table 6.1 \- Codes and Subcodes\]  
 

\\paragraph{Step 3 (Theme Organisation and Relationships):}   
This iterative coding process facilitated the consolidation of related concepts into higher-order categories, allowing patterns to emerge across organisational roles and experiences \\citep{Azungah2018, Nowell2017}. Prior themes under the Initial Template (Section\~4.7.2) were sorted around organisational concerns, including leadership actions, institutional processes, and interactional dynamics, supporting systematic theme development \\citep{Miles2014}. As refinement progressed, redundant or weakly supported codes were merged or removed, resulting in a more focused and analytically stable coding structure. After eliminating redundancies and similar concepts, and following eight interviews, 9 codes and 57 subcodes were produced in Version 2 (V2) (sample Figure\~\\ref{fig:4.13}). Details of the refined Phase 2 (V2) coding structure and visual NVivo representations are provided in Appendix\~\\ref{appendix:E}.

   
   
\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 2 \- Version 2 (V2) NVivo coding sample\]{%  
    \\textbf{Figure 4.13}\\\\\[1.2em\]  
    \\textit{Phase 2 \- Version 2 (V2) NVivo coding sample.}  
    }  
    \\label{fig:4.13}  
    
   
    \\includegraphics\[width=0.8\\linewidth\]{Figures//c4/4.13\_P2-nvivo2.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}    
    \\end{minipage}  
\\end{figure}

\\paragraph{Step 4 (Review the Theme):}   
Following involvement through coding, attention turned to bridging specific behaviours around data privacy to organisational cultural determinants of cybersecurity readiness \\citep{King2017}. At this point, the focus was on the management and organisational perspectives to explore how the developing pre-themes map onto the earlier established codes (V1 and V2). 

In this process of analysis, the researcher observed tensions between individual cybersecurity behaviours and organisational cultural conditions, as reflected in Schein's artefacts, values, and assumptions, showing that culture could enable or constrain readiness \\citep{Adamu2025, Schein2010, Sutton2025}. The research moved from V1 to V2, culminating in a final and clear V3, where the codes stabilisd and become more specific. This final stage generated a total of 11 codes and 50 sub-codes, supported by 315 referenced quotations (sample Figure\~\\ref{fig:4.14}), reflecting both analytic depth and internal consistency across interviews. Also, see NVivo V3 analysis code details in Appendix\~\\ref{appendix:E}.\\\\  
 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Phase 2 \- Version 3 (V3) NVivo coding sample\]{%  
    \\textbf{Figure 4.14}\\\\\[1.2em\]  
    \\textit{Phase 2 \- Version 3 (V3) NVivo coding sample.}  
    }  
    \\label{fig:4.14}  
    
   
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures//c4/4.14\_P2-nvivo3.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}    
    \\end{minipage}  
\\end{figure}

\\paragraph{Step 5 (Defining and Naming Themes):}   
The following sections present the eleven final themes (P2-T1 – P2-T11) (see details in Research Findings and discussion in Chapter \\ref{chapter:c6}), each drawn from the refined coding structure and supported by illustrative participant quotations \\citep{Nowell2017}. This stage focused on naming clear, critically meaningful labels to each theme to ensure conceptual consistency and reliability across the findings. 

\\paragraph{Step 6 (Finalising the Template and Update):}   
Phase 2 analysis was conducted with a refined set of eleven analytical themes capturing how organisational culture, leadership practices, and governance arrangements shaped cybersecurity readiness within the institution. The Phase 2 final template reflected progressive refinement from the Initial Template, incorporating organisational-level patterns that emerged through participants' experiences and interaction with the interview data.. The final template prioritised analytical clarity while preserving organisational complexity through clear codes and quotations under each theme. Chapter \\ref{chapter:c5} presented the Phase 2 findings and discussion, with Figure\~\\ref{fig:6.2} illustrating the final analytical template emerging from the thematic analysis \\citep{Brooks2015, Long2025}.

\\subsubsection{Phase 3 \- Data Analysis}   
Phase 3 utilised cross-phase analysis by presenting the consolidated themes from Phases 1 and 2 to seven domain experts for structured review. An expert panel protected identities and elicited unbiased responses, thereby improving result dependability \\citep{Latif2025, McCants2022}. The integrated thematic structure was presented sequentially, with supporting quotations and interpretive summaries, enabling experts to assess the coherence, practical relevance, and completeness of each theme within the higher education cybersecurity context. Prior study guidance indicates that expert validation panels commonly range from two to twenty participants, with six to ten often cited as appropriate for achieving analytical rigour \\citep{Yusoff2019}. 

This process strengthened the internal validity of the structure in two ways. First, it examined whether Phase 1 mental interpretations remained credible when viewed through organisational practice. Second, it assessed whether Phase 2 cultural explanations adequately accounted for the behavioural patterns identified earlier. The resulting framework represented a cross-verified structure grounded in participant accounts and tested against sector expertise. It provided the final analytical platform for the findings presented in the next chapter.

Importantly, Phase 3 did not function as a new round of open coding. No new thematic domains emerged. Experts recommended that the pressure of work and security fatigue affected cybersecurity behaviour and were critical factors \\citep{Furnell2025, Kannelonning2023}. Feedback yielded deeper organisational insights, backed by several experts and prior phase participants.

\\section{Data Saturation Across All Phases}  

\\paragraph{Phase 1 \- Saturation:\\\\}  
Phase 1 comprised seven interviews. Data saturation was reached before the seventh interview. After Interview 6, no new first-order codes emerged; Interview 7 reinforced existing categories across all five template themes (see Appendix\~\\ref{appendix:D}; Phase 1- codebook for NVivo data analysis). Later interviews confirmed previously identified patterns rather than introducing new concepts, indicating a stable analytic structure. This high cumulative coverage satisfied both code saturation (no additional labels) and meaning saturation (no change in conceptual properties) as defined by Saunders et al. \\citep{Saunders2018}.

\\paragraph{Phase 2 \- Saturation:\\\\}  
Phase 2 included eight interviews with organisational stakeholders. Data saturation occurred by Interview 6; Interviews 7 and 8 yielded no new codes or meaning shifts (see Appendix\~\\ref{appendix:E}; Phase 2- codebook for NVivo data analysis). This confirmed code and meaning saturation, achieving analytic sufficiency \\citep{Hennink2017, Jennings2025, Saunders2018}. Eight interviews sufficed for a theoretically saturated view of organisational cultural factors in cybersecurity readiness.

\\paragraph{Phase 3 \- Saturation:\\\\}  
Phase 3 involved seven expert validation interviews. Saturation emerged by Interview 4, as experts consistently validated Phases 1 and 2 findings without new insights \\citep{Jennings2025}. Partial agreements occurred, but no outright rejections, which strengthened credibility. Data collection continued to Interview 7 for comprehensiveness, confirming no further perspectives \\citep{Saunders2018} (see Appendix\~\\ref{appendix:F}; Phase 3- codebook for NVivo data analysis).

\\section{Implement Trustworthiness, Ethics, and Bias}  
\\label{sec:trustworthiness\_ethics}

Trustworthiness was operationalised through credibility, transferability, dependability, and confirmability \\cite{Adler2022, Forero2018}. As detailed in Chapter \\ref{chapter:c3}, these criteria ensure the qualitative rigour of the study.

Credibility was achieved through the multi-phase design. Phase 1 findings were examined alongside Phase 2 organisational data and subsequently refined through Phase 3 expert validation, enabling comparison across perspectives and strengthening interpretive accuracy. The relationship between these phases is illustrated in Figure \\ref{fig:4.3}.

Transferability was addressed by clearly outlining the institutional setting, participant roles, and analytical scope, as summarised in the Chapter\~\\ref{chapter:c4} (see Section \\ref{sec:4.6.4}). This provides sufficient contextual detail for readers to assess the applicability of findings to similar higher education environments.

Dependability was maintained through a consistent analytical procedure across all phases. Multi-versioned coding structures (see Section \\ref{sec:4.7.4}) and template revisions were applied systematically, ensuring that interpretation followed a stable and traceable process.

Confirmability was supported through explicit documentation (in NVivo) of coding decisions, theme development, and analytical reasoning, with a clear audit trail demonstrating how interpretations were grounded in the data.

Ethical approval was obtained separately for each phase before data collection (see Appendix\~\\ref{appendix:A} \-\~\\ref{appendix:C}). Participants received study information, provided informed consent, and participated voluntarily with the right to withdraw at any time. Confidentiality and anonymity were protected through de-identification, and all data were stored securely.

Bias was actively managed through reflexive practice and structured analytical control. Coding decisions and theme development were systematically documented during template construction, as discussed in Section \\ref{sec:4.7.4}, ensuring transparency in how interpretations evolved. Cross-phase comparison between individual, organisational, and expert data was used to challenge emerging patterns and identify inconsistencies, reducing reliance on single-source accounts and strengthening the robustness of interpretations.

\\section{Conclusion}  
This chapter detailed the research design's practical implementation. The epistemological stance informed theoretical frameworks and initial template application across phases and operationalised the bounded single explanatory case study. It also outlined how participants were recruited, how interviews were conducted, and how template analysis was implemented in a structured and traceable manner.

Together, these procedures demonstrate methodological coherence. Design decisions were not only justified in Chapter\~\\ref{chapter:c3} but enacted here through organised data and phased analysis. The documentation of coding iterations, template refinement, and cross-phase validation establishes the transparency required for evaluative rigour.

The next chapter moves from implementation to findings. Chapter\~\\ref{chapter:c5} presents the Phase 1 findings and discussion, examining how individual mental models of privacy influenced cybersecurity behaviour.

\\chapter{Phase 1 Findings and Discussion}  
\\label{chapter:c5}

\\setcounter{figure}{0}  
\\renewcommand{\\thefigure}{5.\\arabic{figure}}

\\section{Introduction}  
\\label{sec:5.1}

The previous chapter explained how the research design was implemented, including the epistemological positioning, theoretical grounding, case study execution, data collection procedures, and analytical process.

This chapter turns to the empirical findings from Phase 1\. It examined how individuals within a higher education context understood privacy and how their mental models influenced cybersecurity-related behaviour. Applying Protection Motivation Theory (see Section\~\\ref{sec:3.2.2}) as an interpretive lens, the analysis studied how participants assessed threats and evaluated coping options in security behaviour decisions.

The chapter begins with a summary of the Phase 1 analytical structure, followed by a presentation and discussion of the findings. Figure\~\\ref{fig:5.1} provides a roadmap of the chapter's structure and sequence.  
 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 5 Roadmap\]{%  
    \\textbf{Figure 5.1}\\\\\[1.2em\]  
    \\textit{Chapter 5 Roadmap.}  
    }  
    \\label{fig:5.1}  
    
    % \\addcontentsline{lof}{figure}{5.1 \\hspace{0.18cm} Chapter 5 Roadmap}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c5/5.1roadmap.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

 

\\section{Phase 1 \- Research Findings and Discussion}  
\\label{sec:5.2}

This section presents the findings emerging from Phase 1 of the study. Building on the template analysis process towards the findings, five new themes were finalised, reflecting how participants perceived privacy, evaluated cybersecurity risks, and expressed these understandings through their everyday behaviours.

Each theme was discussed in sequence, with selected quotations showing how privacy-related mental models shaped cybersecurity behaviours in practice. Together, the themes presented a coherent response of individual reasoning and cybersecurity action

\\subsection{Phase 1 \- Themes Overview}  
\\label{sec:5.2.1}

Five themes emerged through phase 1, and a brief description of each of these themes follows.

\\begin{itemize}  
    \\item \\textbf{Theme 1: Cybersecurity Awareness and Training Effectiveness} \\\\  
    This theme captured how participants judged the value of training in terms of personal relevance, past incidents, and reliable organisational communication. Effective sessions connected to daily tasks; generic formats proved unproductive, as privacy concerns limited engagement despite growing awareness of cyber threats.

    \\item \\textbf{Theme 2: Assessing and Mitigating Threats Through Awareness and Consequence Management} \\\\  
    This theme shaped how participants considered threats by highlighting perceived vulnerability, anticipated consequences of harmful events, and the expected benefits of secure actions. Judgements proved dynamic and context-driven; careless mistakes, hesitation, and doubt arose amid unrecognised efforts when consequences felt remote. 

    \\item \\textbf{Theme 3: Balancing Confidence, Capability, and Costs in Coping Strategies:} \\\\  
    This theme described participants weighing self-confidence, trust in action effectiveness, and impact against neglect costs and barriers like effort or disruption. Security behaviours weakened when capabilities felt uncertain or routine demands prevailed.

    \\item \\textbf{Theme 4: Proactive and Compliant Cybersecurity Behaviours:} \\\\  
    This theme focused on routine practices that reduced exposure, such as verifying privacy habits and cautious engagement. Proactive actions strengthened with clear policy expectations, feasible workloads, organisational trust, vulnerability awareness, and signals boosting willingness to participate.

    \\item \\textbf{Theme 5: Addressing Gaps in Leadership and Authority:} \\\\  
    This theme highlighted how limited supervisory guidance and unclear authority pathways constrained secure decision-making and delayed escalation. Participants often relied on personal judgment, which increased inconsistency and weakened sustained individual daily practice.  
\\end{itemize}

Each theme comprised multiple codes, and the study focuses on codes for deeper insight into improving analytical depth. Themes 1-5 contained multiple codes.\\\\

\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[ Illustration of Phase 1 Final Template\]{%  
    \\textbf{Figure 5.2}\\\\\[1.2em\]  
    \\textit{Illustration of Phase 1 Final Template}  
    }  
    \\label{fig:5.2}

    % \\addcontentsline{lof}{figure}{5.2 \\hspace{0.18cm} Illustration of Phase 1 Final Template.}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c5/5.2finaltemplate.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{\\\\Note.} Format Adopted From "Optimising data sharing whilst protecting participant privacy: a data note describing processed data from a qualitative study of healthcare professionals’ experiences of caring for women with false positive screening test results" (p.11), by\~\\citet{Long2025}, (https://doi.org/10.1080/21642850.2024.2449400).Open Access article  
    \\end{minipage}  
\\end{figure}

\\subsection{Phase 1 \- Final Coding Template}  
\\label{sec:5.2.2}

The final template was presented as a visual overview of the hierarchical structure, tracing development from the phase 1 initial template (Section\~\\ref{sec:4.7.2}) to the final template. It represented the outcome of the six-step analytical process outlined in Chapter\~\\ref{chapter:c4} (see Section\~\\ref{sec:4.7.4}), ensuring continuity between analysis and findings. This integration ensured conceptual alignment and empirical sensitivity in the final template structure \\citep{Long2025}. Figure\~\\ref{fig:5.2} illustrates the final template, while Table\~\\ref{tab:5.1} details how theory-informed elements extended into data-driven codes, subcode properties, and themes; the five themes were examined in Sections\~\\ref{sec:5.3}.

 

\\subsection{Phase 1 \- Research Findings Code Structure}  
\\label{sec:5.2.3}

Table\~\\ref{tab:5.1} presents the detailed analytical structure underpinning the Phase 1 findings and the final template. It provides a transparent audit trail demonstrating how theory-informed elements from the initial template were systematically extended, refined, and, in some cases, reconfigured through data-driven coding to generate the final themes. Blue-shaded elements in the table represent theory-informed constructs derived from the initial template (see Section\~\\ref{sec:4.7.2}), whereas peach-shaded elements denote emergent codes, sub-code properties, and themes developed inductively from participant data. This distinction was made explicit where the analysis confirmed prior theoretical expectations and where it contributed novel insights.

The table shows where initial theoretical structures were absent and how these were developed or refined through the analysis. Blank cells indicate the absence of predefined structures at particular levels. For instance, Behavioural Intentions (row 4\) do not include predefined sub-themes and are therefore developed directly through empirical coding. And row 5 represents a fully emergent theme, derived solely from the dataset without prior theoretical guidance. The ordered numbering (e.g., 1.1.1) shows the coding structure, progressing from prior themes to codes and sub-code properties. This numbering is used for traceability and does not imply replication, but rather embraces relationships within the analytical framework.\\\\

\\begingroup

% \--- Thikness \---  
\\setlength{\\arrayrulewidth}{1.2pt}  
% \\setlength{\\arrayrulewidth}{1pt}  
% \\renewcommand{\\arraystretch}{1.2}

% \--- COLOR OPTIONS \---  
\\definecolor{frameworkblue}{HTML}{D0E1F9}   
\\definecolor{findingspeach}{HTML}{FAD7C4}  
\\definecolor{white}{HTML}{FFFFFF}

% \\small  
\\begin{spacing}{1.0}

\\begin{longtable}{p{1.2cm} p{1.2cm} p{3.2cm} p{4.8cm} p{3.0cm}}

% \--- APA Style Caption \---  
\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    font={stretch=1.3}  
}  
\\caption\[Phase 1 \- Research Findings Summary Code Structure\]{%  
\\\\\[1.2em\]  
\\textit{Phase 1 \- Research Findings Summary Code Structure}  
\\label{tab:5.1}  
}  
\\\\

\\hline % Top boundary  
\\rowcolor{white} \\multicolumn{2}{c}{\\textbf{Initial Template}} & \\multicolumn{3}{c}{\\textbf{Research Findings}}  \\\\ \\hline  
\\rowcolor{white} \\textbf{Prior Themes} & \\textbf{Sub-Theme} & \\textbf{Code} & \\textbf{Sub-Code Properties} & \\textbf{Emerged Theme (T)} \\\\ \\hline  
\\endfirsthead  
 

\\hline  
\\rowcolor{white} \\centering \\textbf{Prior Themes} & \\centering \\textbf{Sub-Theme} & \\centering \\textbf{Code} & \\centering \\textbf{Sub-Code Properties} & \\centering \\textbf{Emerged Theme (T)} \\tabularnewline \\hline  
\\endhead

\\multicolumn{5}{r}{\\textit{ }} \\\\  
\\endfoot

\\hline % Bottom boundary  
\\endlastfoot

% \--- THEME 1 \---  
\\cellcolor{frameworkblue} 1\. Knowledge and Experience & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 1.1.1: Cybersecurity Incident & \\cellcolor{findingspeach} \- Incident; \- Cybersecurity Advice & \\cellcolor{findingspeach} Cybersecurity Awareness and Training Effectiveness (P1-T1) \\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 1.1.2: Privacy Focus & \\cellcolor{findingspeach} \- Attitudes; \- Behaviours; \- Concerns; \- Limited Awareness & \\cellcolor{findingspeach} \\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 1.1.3: Training Perspective & \\cellcolor{findingspeach} \- Compulsory Training; \- Monitoring; \- Prior Training; \- Unproductive Training Methods & \\cellcolor{findingspeach} \\\\ \\hline

% \--- THEME 2 \---  
\\cellcolor{frameworkblue} 2\. Threat & \\cellcolor{frameworkblue} 2.1: Vulnerability & \\cellcolor{findingspeach} 2.1.1: Exploitability & \\cellcolor{findingspeach} \- Harmful Event & \\cellcolor{findingspeach} Assessing and Mitigating Threats Through Awareness and Consequence Management (P1-T2) \\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 2.1.2: Negligent Reliance & \\cellcolor{findingspeach} \- Careless Mistakes; \- Doubting Organisation; \- Hesitation; \- Ignorance & \\cellcolor{findingspeach} \\\\ \\cline{2-4}  
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} 2.2: Severity & \\cellcolor{findingspeach} 2.2.1: Consequence & \-Perceive Consequence\\cellcolor{findingspeach} & \\cellcolor{findingspeach} \\\\ \\cline{2-4}  
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} 2.3: Rewards & \\cellcolor{findingspeach} 2.3.1: Benefits & \\cellcolor{findingspeach} \- Unrecognised Effort; \- Weighing Benefit & \\cellcolor{findingspeach} \\\\ \\hline

% \--- THEME 3 \---  
\\cellcolor{frameworkblue} 3\. Coping & \\cellcolor{frameworkblue} 3.1: Self-Efficacy & \\cellcolor{findingspeach} 3.1.1: Ability & \\cellcolor{findingspeach} \- Belief; \- Capability & \\cellcolor{findingspeach} Balancing Confidence, Capability, and Costs in Coping Strategies (P1-T3) \\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} 3.2: Response Efficacy & \\cellcolor{findingspeach} 3.2.1: Effectiveness & \\cellcolor{findingspeach} \- Efficacy & \\cellcolor{findingspeach} \\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 3.2.2: Trust & \\cellcolor{findingspeach} \- Confidence; \- Impact & \\cellcolor{findingspeach} \\\\ \\cline{2-4}  
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} 3.3: Response Cost & \\cellcolor{findingspeach} 3.3.1: Barrier & \\cellcolor{findingspeach} \- Neglect Cost; \- Penalty & \\cellcolor{findingspeach} \\\\ \\hline

% \--- THEME 4 \---  
\\cellcolor{frameworkblue} 4\. Behavioural Intentions & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 4.1.1: Cybersecurity Intentions & \\cellcolor{findingspeach} \- Security Intentions; \- Organisation and Trust; \- Organisation Responsibility & \\cellcolor{findingspeach} Proactive and Compliant Cybersecurity Behaviours (P1-T4) \\\\    
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 4.1.2: Policy Compliance & \\cellcolor{findingspeach} \- Policy; \- Willingness & \\cellcolor{findingspeach} \\\\    
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 4.1.3: Risk Awareness & \\cellcolor{findingspeach} \- Risk Indicators; \- Vulnerability Awareness & \\cellcolor{findingspeach} \\\\    
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 4.1.4: Safe Practices & \\cellcolor{findingspeach} \- Action Likelihood; \- Active Participation; \- Security Awareness & \\cellcolor{findingspeach} \\\\ \\hline

% \--- THEME 5 \---  
\\cellcolor{findingspeach} 5\.  & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 5.1.1: Insufficient Support & \\cellcolor{findingspeach} \- Supervisor \\& Managers; \- Authority & \\cellcolor{findingspeach} Addressing Gaps in Leadership and Authority Support (P1-T5) \\\\   
%\\hline 

\\end{longtable}

\\end{spacing}  
\\endgroup

 

\\section{Phase 1 \- Thematic Findings and Discussion}  
\\label{sec:5.3}

This selection presents Phase 1 thematic findings and discussion. It draws on the final template (Figure\~\\ref{fig:5.2}) and coding framework (Table\~\\ref{tab:5.1} to interpret five themes explaining participants' privacy mental models and cybersecurity behaviours. Each theme uses supporting quotations and is linked to prior research.

\\subsection{Theme 1 \- Physical Symbolism and Security Culture Blind Spots:}  
\\label{sec:P1T1}

 Theme 1 showed how visible workplace conditions affected everyday assumptions about privacy and security. Participants described organisational physical surroundings that offered few cues of cybersecurity priority, encouraging casual data handling. Insufficient artefact-level signals thus undermined awareness despite formal controls and online reminders.  
   
Figure\~\\ref{fig:5.3} visualises Theme 1 (P2-T1) code structure emerging from Table\~\\ref{tab:5.1}  data. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:D}.\\\\  
 

\\begin{figure}\[H\] %\[\!ht\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 1 (P1-T1) Code Structure\]{%  
    \\textbf{Figure 5.3}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 1 (P1-T1) Code Structure}  
    }  
    \\label{fig:5.3}  
   
   
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c5/5.2\_P1T1.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{ }  
    \\end{minipage}  
\\end{figure}  
   
 

This theme (P1-T1) consists of three codes that aid understanding of cybersecurity awareness and training effectiveness in real-world environments. 

\\paragraph {\\textbf{Code: Cybersecurity Incident\\\\}}  
This code refers to moments where participants directly encountered cybersecurity incidents, such as phishing emails or malware alerts, which shaped their understanding of risk. These experiences moved security from abstract policy to practical awareness, clarifying personal responsibility and appropriate responses. Incident exposure, therefore, grounded cybersecurity understanding lived in experience, not theoretical instruction. These incidents showed how privacy assumptions shaped passive or protective responses.

This code contains two supporting subcode properties, which enhance the clarity and alignment of the code:   
\\begin{itemize}  
    \\item The\\textbf{ Incident} highlighted real triggers and lessons from others' errors that shift users to alert mode. This clarified why protocols mattered, turning abstract threats into real dangers.  
    \\item The\\textbf{ Cybersecurity Advice} reflected turning events or policies into clear ‘what to do' steps. Participants showed their need for practical guidance that adapted to emerging threats.  
\\end{itemize}

See Table\~\\ref{tab:5.2} for a sample of interview quotes that represent the cybersecurity incident code and visible patterns.\\\\  
 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\centering  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Cybersecurity Incident\` Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Cybersecurity Incident\` Code}  
\\label{tab:5.2}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Cybersecurity Incident & Incident & \`\`They should focus more on what are spams... my supervisors themselves thought this was a general email, but it was a spam.'' (P1-004) \\newline \`\`In his \[study\] also has some of the malware content... the network has not allowed me to install on my OneDrive.'' (P1-003) \\\\ \\cline{2-3}

 & Cybersecurity Advice & \`\`First, I will inform my supervisor... then I will inform IT.'' (P1-003) \\newline \`\`Every student is not like me… students from humanities or liberal arts backgrounds might be \[more\] vulnerable.'' (P1-004) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\paragraph {\\textbf{Code: Privacy Focus\\\\}}  
This code reflects how participants filtered cybersecurity expectations through their own understanding of what counts as sensitive information. Protection practices were applied selectively, depending on perceived risk and social context. Decisions were therefore shaped more by personal judgement than by consistent reference to actual policy. This selective interpretation of privacy beliefs revealed how individual mental models influenced cybersecurity behaviour.

This code contains four supporting subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Attitudes} flagged a shift in responsibility where participants prioritise personal safety over organisational policy.  
    \\item The\\textbf{ Behaviours} presented the practical ‘efficiency-driven' habits of participants, such as selective engagement with training materials and the use of interpersonal trust to bypass formal security rules.  
    \\item The\\textbf{ Concerns} property signalled participant anxieties regarding ‘vulnerable' peers from non-technical backgrounds and the perceived lack of impact in non-interactive, text-heavy training methods.  
    \\item The\\textbf{ Limited Awareness} reflects a self-acknowledged ‘fragmented' understanding of privacy, which reduced the consistent application of institutional cybersecurity practices.  
\\end{itemize}

See Table\~\\ref{tab:5.3} for a sample of interview quotes that represent the Privacy Focus code.

 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\centering  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Privacy Focus' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Privacy Focus' Code}  
\\label{tab:5.3}  
}  
\\\\ \\hline

\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Privacy Focus & Attitudes & \`\`Have I read the data policy? No. Have I done some training on it? I probably would have, yeah.'' (P1-002) \\newline \`\`I don't think that I am sending anything so valuable that I should protect it with the password. It is not a life-or-death issue.'' (P1-006)) \\\\ \\cline{2-3}

 & Behaviours & \`\`You're not meant to... you shouldn't... It's interesting what you would do, particularly if you trust the person... maybe, yeah.'' (P1-005)\\\\ \\cline{2-3}

 & Concerns & \`\`It will be more efficient if we can just get the directions directly from our supervisor... sometimes we miss to open that video.'' (P1-001) \\newline\\newline \`\`Your files can always be viewed by the administrator... you need to be very careful what you're uploading in your OneDrive.'' (P1-002) \\\\ \\cline{2-3}

  & Limited Awareness & \`\`I am not using reading all these policies, but I know the basics.'' (P1-006) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\paragraph{\\textbf{Code: Training Perspective\\\\}}  
Training Perspective portrayed how participants measured cybersecurity training based on practicality, involving workload, relevance, and visible leadership support. Individual commitment was enhanced when training was brief, role-specific, and reinforced by supervisors. Participants' engagement with training was filtered through their existing privacy beliefs and prior experience, influencing whether awareness translated into behavioural change. 

It is refined by four supporting subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Compulsory Training} flagged a reliance on ‘mandatory' status as the primary motivator for engagement, where participants often prioritise training only when it is strictly required for compliance.  
    \\item The\\textbf{ Monitoring} identified the participant's desire for active oversight and updates instead of training, suggesting that awareness is sustained through continuous instead of phishing simulations.  
    \\item The\\textbf{ Prior Training} highlighted how previous work experience and academic backgrounds act as a foundation that participants use to ‘filter' or supplement new institutional training.  
    \\item The\\textbf{ Unproductive Training Methods} captured the friction caused by non-interactive delivery methods, such as long videos or ‘standardised' emails, which participants often view as time-consuming or irrelevant to their specific roles.  
\\end{itemize}

See Table\~\\ref{tab:5.4} for a sample of interview quotes that represent the training perspective code.\\\\

 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\centering  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Training Perspective' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Training Perspective' Code}  
\\label{tab:5.4}  
}  
\\\\ \\hline

\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Training Perspective & Compulsory Training & \`\`When it is not compulsory, then it's like you will. OK, I will say it later. So, I mean like they should be like compulsory training sessions for the student and staff. One day, one hour. That's fine'' (P1-003) \\\\ \\cline{2-3}

& Monitoring & \`\`We should have some kind of monitoring as well in monthly basis. They can, just give us any update regarding a new kind of attack or new kind of security problems.'' (P1-001) \\\\ \\cline{2-3}

 & Prior Training & \`\`Of course, my previous experience has actually helped me a lot, but the training from \[Organisation\] was, of course, additional, but that helped a little bit.'' (P1-006) \\\\ \\cline{2-3}

 & Unproductive Training Methods & \`\`I'm watching the videos \[training\], doing the training, or I've enrolled into... fishing training thing, sort of feel that it was like, oh, God..., it is a waste of time.'' (P1-005) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\subsubsection{Theme 1 \- Discussion:}  
\\label{sec:DP1T1}

Theme (P1-T1) revealed that cybersecurity awareness in Phase 1 depended less on training volume and more on how privacy mental models shaped its interpretation. Awareness translated to behaviour only when participants linked training to lived experience, perceived responsibility, and personal privacy risk judgements. Abstract, generic training detached from daily work was filtered, postponed, or ignored. Consistent with prior research, awareness initiatives are most effective when they are perceived as relevant to participants' roles and daily practices \\citep{Alshaikh2021Journal, Georgiadou2022, ulven2021}. This theme confirms prior knowledge regarding the role of personal relevance and experiential learning in cybersecurity awareness effectiveness \\citep{Kiran2025, Xiao2014}.

Participants repeatedly indicated that they did not reject cybersecurity training in principle. Rather, they evaluated it against workload, prior knowledge, and perceived immediacy \\citep{Prummer2024}. Several participants explicitly described selective engagement and linking to reinforcement:

% \\begin{quote}  
%    \\small {I typically filter the emails ... I selectively go through the ones that are specifically relevant to me. (P1-002)}  
% \\end{quote}

% \\begin{quote}  
%     \\small {When it is not compulsory, then it's like you will. OK, I will say it later ... they should be compulsory training sessions ... one day, one hour. That's fine. (P1-003)}  
% \\end{quote}

\\begin{quote}  
    \\small \\textit{I typically filter the emails ... I selectively go through the ones that are specifically relevant to me. (P1-002)}\\\\  
    \\small \\textit{When it is not compulsory, then it's like you will. OK, I will say it later ... they should be compulsory training sessions ... one day, one hour. That's fine. (P1-003)}  
\\end{quote}

 

This showed that compliance cues, beyond inner drive alone, were needed for real engagement. Without them, awareness lost priority.

\\paragraph{\\textbf{Cybersecurity Incident:\\\\}}

Incidents functioned as activation points. Participants frequently illustrated how breaches, near misses, or visible systems made abstract policy concrete. Prior research has recognised that individual understandings of risk are central to cybersecurity behaviour \\citep{Georgiadou2022, ulven2021}.

When participants described irregular emails or impersonations, they highlighted recurring phishing incidents, the need for daily vigilance, and the value of peer discussions beyond training. Participants reflected on the phishing attempt and malware:

\\begin{quote}  
    \\small \\textit{They should focus more on what are spams ... my supervisors themselves thought this was a general email, but it was a spam. (P1-004)}  
\\end{quote}

Incident exposure clarified escalation and reporting duties; when discussing hypothetical responses to security breaches, participants articulated clearer and more confident response sequences. One stated:

\\begin{quote}  
    \\small \\textit{First, I will inform my supervisor ... then I will inform IT. (P1-003)}  
\\end{quote}

Participants also reflected on uneven awareness across disciplines and roles. P1-004 suggested that non-technical staff were less able to recognise cyber threats, underscoring the limits of generic awareness messages.

\\begin{quote}  
    \\small \\textit{Every student is not like me ... students from humanities or liberal arts backgrounds might be \[more\] vulnerable. (P1-004)}  
\\end{quote}

These explanations suggest cybersecurity incidents served as practical learning triggers. Incident exposure heightened risk projection, clarified responsibilities, and activated privacy judgements, aligning with \\citet{ulven2021} and \\citet{Georgiadou2022}. Without such triggers, awareness lingered mentally but lay dormant behaviourally.

\\paragraph{\\textbf{Privacy Focus:\\\\}}  
Privacy operated as a decision lens through which training was accepted, reshaped, or dismissed. Participants did not uniformly internalise institutional privacy rules. Instead, they applied threshold logic based on perceived sensitivity, trust, and social context. Prior research has shown that individual privacy perceptions strongly influence security behaviour, particularly in complex organisational settings such as higher education \\citep{Aliyu2020, ulven2021}.

Privacy beliefs acted as an internal decision threshold that ignored formal guidance. Participants did not regularly apply security controls; instead, they initiated them selectively:

\\begin{quote}  
    \\small \\textit{If it is sensitive (data) ... then I shall use a password protection. (P1-002)}\\\\  
    \\small \\textit{I don't think that I am sending anything so valuable that I should protect it with the password. It is not a life-or-death issue. (P1-006)}  
\\end{quote}

Participants' protection was triggered by perceived data sensitivity, not by rule-following. When asked about engagement with formal policy, one participant acknowledged:

\\begin{quote}  
    \\small \\textit{Have I read the data policy? No. Have I done some training on it? I probably would have, yeah. (P1-002)}  
\\end{quote}

A gap between institutional privacy guidance planning and its daily uptake was highlighted, reinforcing that policy visibility alone failed to shape behavioural actions.

Trust strongly shaped how participants negotiated privacy risks, especially under pressure \\citep{Mehdy2021}. When asked about sharing credentials in urgent situations, they described conditional exceptions that overrode formal rules.

\\begin{quote}  
    \\small \\textit{You're not meant to ... you shouldn't ... It's interesting what you would do, particularly if you trust the person ... maybe, yeah. (P1-005)}  
\\end{quote}

Trust in colleagues replaced procedural safeguards. Privacy mental models relied on social judgment rather than solely on policy compliance.

Personalised risk thresholds activated privacy protection beyond internal boundaries. Institutional access awareness motivated caution in organisational systems. One participant described being mindful of cloud storage because of administrative visibility:

\\begin{quote}  
    \\small \\textit{Your files can always be viewed by the administrator ... you need to be very careful what you're uploading in your OneDrive. (P1-002)}  
\\end{quote}

Together, these showed privacy served as a behavioural lens rather than a mere compliance checklist. This stretched prior work by demonstrating how mental models influence engagement with privacy in higher education contexts \\citep{Aliyu2020, Georgiadou2022}. Privacy mental models were socially negotiated rather than routinely applied. Such conditional exceptions illustrate how awareness interacts with the individual mindset, reinforcing that behaviour cannot be predicted from training exposure alone.

\\paragraph{\\textbf{Training Perspective:\\\\}}  
Participants consistently described email-based or optional training as easy to overlook in busy academic environments. Engagement increased when training was concise, role-specific, and highlighted by supervisors. Without managerial endorsement, awareness content became background noise. When asked about video training, multiple participants explained:

\\begin{quote}  
    \\small \\textit{I'm watching the videos \[training\], doing the training, or I've enrolled into ... fishing training thing, sort of feel that it was like, oh, God ..., it is a waste of time. (P1-005)}\\\\  
    \\small \\textit{It will be more efficient if we can just get the directions directly from our supervisor ... sometimes we miss to open that video. (P1-001)}\\\\  
    \\small \\textit{If it's not mandatory, I keep it out ... if I get time, then I do it. (P1-006)}  
\\end{quote}

This portrayed awareness materials alone as insufficient. Effectiveness depended on social validation. Priority was signalled by supervisory endorsement, elevating training to expected practice.

Monitoring and light accountability shaped engagement further. Participants favoured short, clearly bounded sessions that respected workload constraints:

\\begin{quote}  
    \\small \\textit{We should have some kind of monitoring as well in monthly basis. They can just give us any update regarding a new kind of attack or new kind of security problems. (P1-001)}  
\\end{quote}

Monitoring here was framed as continuity rather than surveillance. In contrast, broad or optional materials were skipped under workload pressure; non-mandatory training was deferred based on relevance. Participants stated:

\\begin{quote}  
    \\small \\textit{I typically filter the emails ... I selectively go through the ones that are specifically relevant to me. (P1-002)} \\\\  
    \\small \\textit{If it's not mandatory, I keep it out ... if I get time, then I do it. (P1-006)}  
\\end{quote}

Prior work showed that training effectiveness depends not only on content but on how learning was situated within everyday roles and supported by management practices \\citep{Alshaikh2021Journal, ulven2021}.

Theme 1 extended earlier studies by evidencing how user perceptions, institutional context, and prior exposure influence training effectiveness \\citep{Alshaikh2021Journal, Alshaikh2021Model, Jennings2025}. Awareness faded without reinforcement or incident knowledge. Academic demands drove engagement through institutional push and urgency.

 

\\subsection \[Theme 2 \- Assessing and Mitigating Threats Through Awareness\]{Theme 2: Assessing and Mitigating Threats Through Awareness and Consequence Management}  
\\label{sec:P1T2}

Theme 2 captured how participants spotted cybersecurity risks and adjusted actions during daily work. They weighed cues like warnings, past events, and clear harms from their environment. Participants judged vulnerability from daily system use, harm from consequences, and effort against benefits. This dynamic process explained real-world choices over fixed rules. Threat assessments depended on participants' privacy beliefs. These beliefs decided if vulnerability seemed real and they took action.

Figure \\ref{fig:5.4} visualises Theme 2 (P1-T2) code structure emerging from Table\~\\ref{tab:5.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:D}.\\\\

   
\\begin{figure}\[H\] %\[\!ht\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 2 (P1-T2) Code Structure\]{%  
    \\textbf{Figure 5.4}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 2(P1-T2) Code Structure}  
    }  
    \\label{fig:5.4}  
   
   
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c5/5.3\_P1T2.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{ }  
    \\end{minipage}  
\\end{figure}  
 

 

This theme (P1-T2) consists of four codes that accelerate understanding of how participants assessed vulnerability, consequences, and behavioural compromises in cybersecurity situations.  

\\paragraph{\\textbf{Code: Exploitability\\\\} \\small{(Linked to Prior Theme: Threat, Sub-theme: Vulnerability):}}

The Exploitability code captured how routine work practices created cybersecurity openings, which unintentionally increased exposure despite institutional controls. Participants viewed vulnerabilities as restricting regular choices, like skipping protections for convenience or assuming system safeguards, not just technical flaws alone. Observations of exploitability risks decided if participants added protections or accepted the risk. See Table\~\\ref{tab:5.5} for a sample of interview quotes that represent the Exploitability code and visible patterns.

This code is refined by one primary subcode property:   
\\begin{itemize}  
    \\item The\\textbf{ Harmful Event} signalled the necessity of ‘concrete evidence' or past negative experiences. Examples include spam, system compromises, or personal data leaks, which shifted participants' privacy judgements and increased motivation for protective behaviour.\\\\  
\\end{itemize}  
 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\centering  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Exploitability' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Exploitability' Code}  
\\label{tab:5.5}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Exploitability & Harmful Event & \`\`Sadly, I do it. I did it \[wrongly clicking some links\] and then regret it. Yeah, but you know, it's for the greater good.'' (P1-005) \\newline \`\`I just downloaded \[it\], even \[though\] it's not listed in the \[organisation name\] software store. Because I already know whether it is safe or not... many people use that one, and then... I trust the owner of the software.'' (P1-001) \\newline \`\`It would be a hassle to encrypt... it never comes to my mind to protect.'' (P1-007) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\paragraph{\\textbf{Code: Negligent Reliance \\\\} \\small{(Linked to Prior Theme: Threat, Sub-theme: Vulnerability):}}  
The Negligent Reliance described a pattern in which participants altered responsibility for cybersecurity to institutional systems or trusted colleagues, reducing their own protective engagement. Security was often assumed to be embedded within organisational infrastructure, which weakened personal threat appraisal and encouraged vulnerable shortcuts. This code reflects a gap between awareness of risk and active individual accountability. 

This code is refined by four subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Careless Mistakes} flags errors made due to environmental pressures or rational shortcuts, such as clicking suspicious links while in a hurry.  
    \\item The\\textbf{ Doubting Organisation} reflects an underlying scepticism where participants question the absolute safety of organisation systems despite relying on them.  
    \\item The\\textbf{ Hesitation} captures the moment of uncertainty where participants require external guidance or concrete evidence before acting on a potential threat.  
    \\item The\\textbf{ Ignorance} reflects a lack of engagement with security protocols, such as encryption, often justified by a perceived lack of ‘valuable' or sensitive data.  
\\end{itemize}

See Table\~\\ref{tab:5.6} for a sample of interview quotes that represent the Negligent Reliance code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\centering  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Negligent Reliance' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Negligent Reliance' Code}  
\\label{tab:5.6}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Negligent Reliance & Careless Mistakes & \`\`Yes, I normally check, but maybe sometimes I am in a hurry. I miss taken the open anything. Yeah, it could happen.'' (P1-006) \\newline \`\`As the university is providing the VPN, so I feel safe.'' (P1-003) \\\\ \\cline{2-3}

 & Doubting Organisation & \`\`So do you feel like \[organisation\] system also not exactly safe, but they're trying, like, keeping so many privacy factors on it.'' (P1-003) \\\\ \\cline{2-3}

 & Hesitation & \`\`If I am not clear who is collecting those information... I hesitate to provide those. But you know, nowadays like big, big companies like Google... we trust those.'' (P1-006) \\\\ \\cline{2-3}

 & Ignorance & \`\`However, the question is about the one who are responsible to secure data, it is \[organisation\]. If we already put it in the storage'' (P1-001) \\newline \`\`I trust that the \[organisation\] tools and software I use have built-in privacy or encryption technologies.'' (P1-002) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Consequence\\\\} \\small{(Linked to Prior Theme: Threat, Sub-theme: Severity):}}  
The Consequence code appeared within the Phase 1 prior theme Threat, under the sub-theme Severity. Where consequences were detected as minor, reversible, or unlikely to attract individual accountability, vigilance remained low. In comparison, when participants viewed data loss as permanent, reputationally damaging, or emotionally regrettable, they reported increased fears and stronger motivation for protective cybersecurity actions.

This code is refined by one primary subcode property:  
\\begin{itemize}  
    \\item The\\textbf{ Perceive Consequence} captures the participant's behaviour where participants only increase their security vigilance after experiencing a loss or near miss.  
\\end{itemize}

See Table\~\\ref{tab:5.7} for a sample of interview quotes that represent the Consequence code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\centering  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Consequence' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Consequence' Code}  
\\label{tab:5.7}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Consequence & Perceive Consequence & \`\`If the website is not very, I mean very fishy, then I will trust to download this file.'' (P1-006) \\newline \`\`I would think there is no consequence...'' (P1-005) \\newline \`\`I inform ITS and block the email.'' (P1-003) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Benefits \\small{((Linked to Prior Theme: Threat, Sub-theme: Rewards))}:}}  
The Benefits code explored the drivers and the perceived value of adhering to cybersecurity procedures. It captured tension between the desire for institutional recognition and the personal satisfaction of maintaining security. Individuals regularly displayed positive behaviour, even when rewards were absent. This showed how perceived reward influenced behavioural intention. Participants balanced the benefits of security compliance against the effort required, especially when the benefits were unclear.

This code is refined by two subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Unrecognised Effort} captures the participant's frustration when proactive security actions go unnoticed by the organisation or supervisors, creating a sense of "unfairness" in the workload.   
    \\item The\\textbf{ Weighing Benefit} reflects the internal calculation where participants only perform security tasks that provide immediate personal value or when the external encouragement makes the effort seem worthwhile.  
\\end{itemize}

See Table \\ref{tab:5.8} for a sample of interview quotes that represent the Benefits code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Benefits' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Benefits' Code}  
\\label{tab:5.8}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Benefits & Unrecognised Effort & \`\`Maybe they don't recognise where, and there is no such of platform in order to monitor whether we already performed at such a thing or not.'' (P1-001) \\newline  
\`\`Any reward should be regularly to encourage. Yes, it is very good thing.'' (P1-006) \\\\ \\cline{2-3}

& Weighing Benefit & \`\`But nobody really knows because everyone \[is\] doing the same... If it's not, you can quantify it.'' (P1-004) \\newline  
\`\`I think that could be considered, sometimes it's a bit unfair... I'm not looking for recognition, but it I'm doing it for me.'' (P1-005) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup   
 

 

\\subsubsection{Theme 2 \- Discussion:}  
\\label{sec:DP1T2}

Theme 2 (P1-T2) explained how participants actively interpreted vulnerability, severity, and observed reward in routine academic practice. Unlike Theme 1 on awareness, this theme showed threat appraisal via routine workflow, institutional trust, and anticipated consequences before deciding whether the risk warranted behavioural change. Participants acknowledged threat cues, yet their behavioural action depended on how vulnerability, consequence, and benefit were personally drawn. In harmony with PMT, participants judged threat likelihood, severity, and response efficacy in context \\citep{Herath2009, Ifinedo2012}. This pattern suggested mental threat appraisal weakened in practice. This is supported with prior research showing that perceived vulnerability and assumptions about organisational security affect cybersecurity behaviour \\citep{DelsoVicente2025}.

\\paragraph{\\textbf{Exploitability:\\\\}}  
Phase 1 exploitability stemmed not from technical ignorance but confident routines. Participants described security gaps arising from convenience-driven choices, habitual non-encryption, and assumptions that institutional systems would detect anomalies.

Participants commonly acknowledged risk, while continuing practices that increased exposure \\citep{Kennison2020}. For example, when asked about file protection and encryption, one participant admitted:

\\begin{quote}  
    \\small \\textit{It would be a hassle to encrypt ... it never comes to my mind to protect. (P1-007)}  
\\end{quote}

To participants, vulnerability became ordinary but alarming. Safeguards were bypassed not because risks were unfamiliar, but because protective measures were seen as troublesome to workflow. 

Another participant described downloading unapproved software based on perceived social validation:

\\begin{quote}  
    \\small \\textit{I just downloaded \[it\], even \[though\] it's not listed in the \[organisation name\] software store. Because I already know whether it is safe or not ... many people use that one, and then ... I trust the owner of the software. (P1-001)}  
\\end{quote}

Participants relied excessively on organisational security, recognising exposure but seeking reassurance rather than protection.

Thus, exploitability in higher education operated through effort-based rationalisation and routine normalisation, not ignorance. Exploitability, therefore, functioned through overconfidence in personal judgment and reliance on perceived familiarity. \\\\

\\paragraph{\\textbf{Negligent Reliance:\\\\}}  
Negligent reliance described the transfer of protective responsibility away from the individual. Participants frequently positioned institutional safeguards as comprehensive risk managers. In higher education, it appeared as an assumption that VPNs, email filters, and platforms sufficed, amid unclear personal duties during incidents. 

When asked about their attention to security within institutional systems, participants described: 

\\begin{quote}  
    \\small \\textit{For me, it doesn't really bother me ... somehow in the back of the head, I feel that maybe I'm safe inside the \[organisation\]. (P1-002)}\\\\  
    \\small \\textit{As the university is providing the VPN, so I feel safe. (P1-003)}\\\\  
    \\small \\textit{I trust that the \[organisation\] tools and software I use have built-in privacy or encryption technologies. (P1-002)}  
\\end{quote}

Participants' assumptions and blind reliance on organisational safety supplanted personal vigilance. When questioned about responses under stress and time pressure, participants acknowledged negligence.

\\begin{quote}  
    \\small \\textit{Yes, I normally check, but maybe sometimes I am in a hurry. I miss taken the open anything. Yeah, it could happen. (P1-006)}\\\\  
    \\small \\textit{If I trust him ... I would actually change the password to a temporary one, then after getting the help ... change the password immediately. (P1-004)}  
\\end{quote}

This demonstrated participants' negligent reliance through risk externalisation, trust-based bending, and unclear responsibility. Vulnerability was acknowledged yet weakened by structural and individual beliefs.

\\paragraph{\\textbf{Consequence:\\\\}}  
Participants shifted behaviour when consequences were concrete, irreversible, or personally relevant. Across interviews, participants described stronger protective responses when consequences were clearly understood. In these cases, severity appraisal turned directly into action, including reporting incidents, blocking shady communications, and avoiding risky behaviour. Several participants reflected on breach reality:

\\begin{quote}  
    \\small \\textit{I always play it safe ... I do not click on malicious links. (P1-004)}\\\\  
    \\small \\textit{The thing is that already happened, probably we cannot just try to resolve it ... It's already leaked, and then we don't have any choice in order unless we secure for future. (P1-001)}  
\\end{quote}

This response indicates reactive severity recognition. Participants only grasped the importance of consequences after harm occurred, linking threat awareness to protective action. In contrast, when consequences were perceived as limited or selective, urgency declined:

\\begin{quote}  
    \\small \\textit{I do not know what the consequence will be. (P1-006)}\\\\  
    \\small \\textit{I would think there is no consequence ... (P1-005)}  
\\end{quote}

This showed that uncertainty reduced proactive security behaviour. Participants compartmentalised risk and focused on whether harm affected them personally, not considering broader organisational consequences. 

\\paragraph{\\textbf{Benefits:\\\\}}  
The Benefits component added motivation to threat appraisal. Vulnerability and severity recognition alone were insufficient to ensure sustained secure behaviour. Participants consistently described a lack of visible or consistent recognition for secure behaviour. Although they recognised the long-term value of observation, protected practices were felt as isolated actions with little organisational feedback or focus. Participants repeatedly highlighted the invisibility of reward:

\\begin{quote}  
    \\small \\textit{Sometimes my supervisor ... but not very often. (P1-004)}  
\\end{quote}

\\begin{quote}  
    \\small \\textit{Maybe they don't recognise where, and there is no such of platform in order to monitor whether we already performed at such a thing or not. (P1-001)}  
\\end{quote}

This statement indicated motivational invisibility. As a result, secure behaviour lacked reinforcement. Another participant emphasised regularity:

\\begin{quote}  
    \\small \\textit{Any reward should be regularly to encourage. Yes, it is very good thing. (P1-006)}\\\\  
    \\small \\textit{I think that could be considered, sometimes it's a bit unfair ... I'm not looking for recognition, but it I'm doing it for me. (P1-005)}  
\\end{quote}

This participant did not imply a demand for financial incentive. Rather, it reflected the need for behavioural and social encouragement. Where protective benefits seemed unclear, convenience was prioritised \\citep{Furnell2025}.

\\begin{quote}  
    \\small \\textit{They \[management\] are not recognising that person ... they are just \[contributing\]. (P1-003)}\\\\  
    \\small \\textit{But nobody really knows because everyone \[is\] doing the same ... If it's not, you can quantify it. (P1-004)}  
\\end{quote}

Participants' comments indicated that behavioural investment was linked to visible acknowledgement of effort. This illustrated motivation declined in the absence of visible payoffs, institutional recognition, or rewards in cybersecurity compliance.

This theme 2 confirmed prior findings that threat perception, consequence framing, and benefit evaluation impact cybersecurity behaviour \\citep{Hina2019, Kiran2025}. Participants assessed these factors based on experience, training, and institutional context, aligning with PMT and behavioural security research. The analysis emphasised human judgement in preparedness, highlighting the need to address vulnerabilities, response appraisals, and adaptive learning opportunities.

\\subsection \[Theme 3 \- Balancing Confidence, Capability, and Costs\]{Theme 3 \- Balancing Confidence, Capability, and Costs in Coping Strategies:}  
\\label{sec:P1T3}  
This theme 3 explains how participants decided whether to act securely after recognising a risk. Participants' behaviour differed on whether they felt capable of performing the action, believed the action would work, and judged the effort or disruption as manageable. It shaped cybersecurity behaviour not only through risk awareness, but through ongoing evaluations of confidence, effectiveness, and cost.

Figure \\ref{fig:5.5} visualises Theme 3 (P1-T3) code structure emerging from Table\~\\ref{tab:5.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:D}.\\\\

   
 \\begin{figure}\[H\] %\[\!ht\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 3 (P1-T3) Code Structure\]{%  
    \\textbf{Figure 5.5}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 3 (P1-T3) Code Structure.}  
    }  
    \\label{fig:5.5}  
   
    % \\addcontentsline{lof}{figure}{5.5 \\hspace{0.18cm} Visual Summary of Theme 3 (P1-T3) Code Structure}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c5/5.4\_P1T3.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{ }  
    \\end{minipage}  
\\end{figure}

 

This theme (P1-T3) consists of four codes that aid understanding of how participants valued Ability, Effectiveness, Trust and Barrier compromises in the mental model of privacy affecting cybersecurity individual behaviour.

\\paragraph{\\textbf{Code: Ability\\\\} \\small{(Linked to Prior Theme: Coping, Sub-theme: Self-Efficacy):}}  
The Ability code, located within the Self-Efficacy branch of Coping, captures the internal conviction participants have regarding their power to prevent security breaches. It reflected a self-first protection model under the Coping theme and Self-Efficacy sub-theme, where participants relied on personal judgement and technical skills to navigate threats independently of institutional support. This demonstrates how privacy mental models influenced behaviour through perceived personal competence.

This code is refined by two subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Belief} properties capture the participant's psychological confidence in their own vigilance and the defensive mindset.  
    \\item The\\textbf{ Capability} identifies the specific tactical skills, where participants attempt to fix security issues or verify links themselves before seeking IT support, potentially delaying professional intervention.  
\\end{itemize}

See Table\~\\ref{tab:5.9} for a sample of interview quotes that represent the Ability code and visible patterns.\\\\

 \\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Ability' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Ability' Code}  
\\label{tab:5.9}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Ability & Belief & \`\`Personally, I've never made such a mistake, which is good... no I don't have any idea. But I actually prevent myself from happening.'' (P1-002) \\\\ \\cline{2-3}

 & Capability & \`\`If something happened with my laptop, usually first thing that I need to do is I'll do it by myself. Try to search on the online. Yeah. Like how I can solve it.'' (P1-001) \\newline \`\`I can. I know how to report things, and you know, just keep my nose clean.'' (P1-005) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Effectiveness\\\\} \\small{(Linked to Prior Theme: Coping, Sub-theme: Response Efficacy):}}  
   
The Effectiveness code reflected participants' beliefs about whether recommended security actions genuinely reduce risk. It captured how individuals evaluated actions such as reporting incidents, following policy, or filtering emails in terms of practical impact on protecting personal and institutional data. This showed how privacy mental models shaped behaviour through judgements about whether protective responses would be effective.

This code is refined by one subcode property:   
\\begin{itemize}  
    \\item \\textbf{The Efficacy} connects the participant's belief that following in selective compliance, where participants only execute security responses they perceive as high-value or effective, often bypassing institutional rules they deem redundant or technically unnecessary.  
\\end{itemize}

See Table\~\\ref{tab:5.10} for a sample of interview quotes that represent the Effectiveness code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Effectiveness' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Effectiveness' Code}  
\\label{tab:5.10}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Effectiveness & Efficacy & \`\`I shall assist \[assess\] that first if I am not affected, then I will not bother about this.'' (P1-006) \\newline \`\`I do inform the \[Organisation IT\], and straight away I just delete the email... I blocked the email.'' (P1-003) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Trust\\\\} \\small{(Linked to Prior Theme: Coping, Sub-theme: Response Efficacy):}}

The Trust code, situated under Response Efficacy, reflected that participants rely on institutional security infrastructure and trusted platforms as effective protections, shaping response efficacy rather than vulnerability perception. It highlighted how confidence in organisational systems or established providers reduced the perceived need for personal vigilance. In this way, privacy mental models influenced assumptions about who ultimately carried responsibility for protection.

This code is refined by two subcode properties:   
\\begin{itemize}  
    \\item The\~\\textbf{Confidence} relates that the participant's high level of faith often results in security complacency, where participants relax their own protective measures because they believe the system will automatically catch any errors or threats.  
    \\item The\~\\textbf{Impact} captures the participant's recognition of how organisational security measures (like VPNs or mandatory policies) affect their personal safety, because they believe those specific rules provide a personal shield against high-impact digital harm.  
\\end{itemize}

See Table\~\\ref{tab:5.11} for a sample of interview quotes that represent the Trust code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Trust' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Trust' Code}  
\\label{tab:5.11}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Trust & Confidence & \`\`I didn't…I always think this is a safe place for me to deal with, so I should not be on my toes every time I am dealing with \[organisation\].'' (P1-004) \\newline \`\`I would hope so that you know, the IT security team have taken... reasonable measures... for virus protection and firewalls.'' (P1-005) \\\\ \\cline{2-3}

 & Impact & \`\`I feel safe because in \[my\] personal life. I don't use any VPN, so \[organisation name\] is giving me an extra layer of VPN, so I feel more secure when I use.'' (P1-006) \\newline \`\`The only reason to feel safe is that big organisation working behind OneDrive \[storage\]... it feels like it's a good addition to your security.'' (P1-007) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Barrier\\\\} \\small{(Linked to Prior Theme: Coping, Sub-theme: Response Cost):}}  
   
The Barrier code, situated under Response Cost within the Coping framework, identifies the perceived costs or negative outcomes that discourage participants from engaging in security protocols. It reflected situations where time pressure, workload, procedural complexity, or perceived inconvenience reduced motivation to comply proactively. In this sense, coping decisions were shaped not only by awareness but also by outcome understanding, and actions appeared in work.

This code is refined by two subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Neglect Cost} showed where participants prioritised immediate task efficiency over investing additional effort in protective procedures.  
    \\item The\\textbf{ Penalty} property reflected low perceived personal accountability, which reduced the urgency to invest effort in security actions. Participants viewed training neglect or security bypassing as inconsequential.  
\\end{itemize}

See Table\~\\ref{tab:5.12} for a sample of interview quotes that represent the Barrier code and visible patterns.\\\\

 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Barrier' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Barrier' Code}  
\\label{tab:5.12}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Barrier & Neglect Cost & \`\`While my immediate thought is about protecting myself, I haven't previously considered the potential harm to the organisation'' (P1-002) \\newline \`\`I don't believe there be any consequence for them. \[if they click\]... I would \[have\] thought. And you know, it's just one of those things that happens.'' (P1-005) \\\\ \\cline{2-3}

& Penalty & \`\`Yes, I know, like it can affect me also, like they can fire me or something... and it can also affect they said you need reputations.'' (P1-003) \\newline \`\`Probably they will just like close the access of my resource... if I'm doing something wrong... maybe they just take \[it\] back.'' (P1-004) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\subsubsection{Theme 3 \- Discussion:}  
\\label{sec:DP1T3}

Theme 3 studied how participants realised perception into action through coping judgments \\citep{Menard2017, Tsai2016, Xiao2014}, where behaviour depended on complementary confidence, perceived effectiveness, and effort. Cybersecurity behaviour was not uncovered just by awareness but also depended on whether participants believed they could act, whether action would work, and whether effort was justified. These themes emerged from four codes that explained how participants balanced confidence, capability, and cost in cybersecurity responses. Many participants felt confident spotting suspicious content or handling issues alone. Yet this confidence was often self-directed.

This theme revealed how participants balanced confidence, effort, and perceived effectiveness in their security decision systems \\citep{Wu2020, Xiao2014}. It extended behavioural patterns by demonstrating that cybersecurity readiness requires effective coping beliefs beyond threat recognition or policy knowledge.  

\\paragraph{\\textbf{Ability:\\\\}}  
Confidence in handling incidents independently was often described by participants, though unevenly aligned with institutional procedures. Ability was not simply reflected by skill. It revealed participants' views on cybersecurity responsibility. Some expressed high vigilance:

\\begin{quote}  
    \\small \\textit{If something happened with my laptop, usually first thing that I need to do is I'll do it by myself. Try to search on the online, like how I can solve it. (P1-001)} \\\\  
    \\small \\textit{I can, I know how to report things, and you know, just keep my nose clean. (P1-005)}  
\\end{quote}

Participants preferred independent correction over escalation, signalling self-efficacy but exposing procedural gaps. Furthermore, ability was often filtered through perceived protection bias. Careful participants often stopped seeking training or help, considering their own vigilance is sufficient. However, confidence sometimes shifted into perceived invulnerability:

\\begin{quote}  
    \\small \\textit{I feel like I'm already being careful and everything ... I'm always on my toes. (P1-004)} \\\\  
    \\small \\textit{Personally, I've never made such a mistake … I actually prevent myself from happening. (P1-002)} \\\\  
    \\small \\textit{Yes, I have some basic idea, so I can identify which call, or mail, or SMS is response. So, I don't do any action, \[which\] means I don't click the links provided. (P1-006)}  
\\end{quote}

Supportingly, another participant acted only above a personal harm threshold, prioritising it over organisational effects:

\\begin{quote}  
    \\small \\textit{If I am not affected, then I will not really bother with it. (P1-006)}  
\\end{quote}

The analysis revealed that privacy mental models shaped the scope of perceived responsibility. Protective actions arose from personal relevance, not just collective risk. The findings showed that ability proved irregular across participants.

\\paragraph{\\textbf{Effectiveness:\\\\}}  
The Effectiveness captured how participants judged whether cybersecurity actions actually worked. It reflected the response efficacy that a recommended action would reduce harm. Clear response efficacy prompted immediate containment. Multiple participants described it:

\\begin{quote}  
    \\small \\textit{I know how to deal with that system, so I will contact the system administration and tell them this might have happened, and can you take these necessary steps. (P1-004)} \\\\  
    \\small \\textit{I do inform the \[Organisation IT\], and straight away I just delete the email … I blocked the email. (P1-003)}  
\\end{quote}

This illustrated structured coping. The participant believed the action would work and therefore executed it immediately. In contrast, participants' actions were sometimes transferred to their personal sense. Participants who did not feel personally affected by a potential breach perceived low efficacy in protective actions. They adopted a wait-and-see approach, thereby heightening organisational vulnerability.

\\begin{quote}  
    \\small \\textit{I shall \[assess\] that first if I am not affected, then I will not bother about this. (P1-006)}  
\\end{quote}

The findings indicated that participants acted with certainty when they observed a direct underlying association between their behaviour and risk reduction. When participants trusted their actions, they applied immediate restraint and escalation. Reliance on institutional safeguards narrowed vigilance to environmental trust.

\\paragraph{\\textbf{Trust:\\\\}}   
Trust shaped coping by redefining who carried responsibility. Trust shaped coping by influencing perceived response efficacy. Institutional and vendor credibility were frequently substituted for active verification. Several participants expressed strong confidence in institutional controls, assuming that errors would be detected and managed without further individual action. When asked about accidental clicks or mistakes, participants stated:

\\begin{quote}  
    \\small \\textit{I don't really think that because of \[organisation\] already has a system in place security check, which means other persons, means even if they mistakenly click something or some other means went inside, it can be handled by the \[organisation\] system. (P1-004)} \\\\  
    \\small \\textit{I would hope the IT security team has taken reasonable measures. (P1-005)}  
\\end{quote}

Here, participants illustrated the delegation of vigilance, where institutional systems absorbed and undertook risk and where individuals relaxed about personal carefulness. Prior findings illustrated that institutional trust can narrow individual risk appraisal \\citep{DelsoVicente2025, Schaik2020, Tolsdorf2020, ulven2021}. Similarly, organisational tools and big-brand reputation generated perceptions of trust.

\\begin{quote}  
    \\small \\textit{The only reason to feel safe is that big organisation working behind OneDrive \[data storage\] ... it feels like it's a good addition to your security. (P1-007)}  
\\end{quote}

This described, big-brand reputation provided reassurance against risk; trust thereby replaced active checking. Participants' privacy mental models influenced response efficacy. Calibrated trust, or balanced reliance on systems, sustained active engagement. This illustrated trust served as a coping shortcut; when organisational protections seemed comprehensive, participants reduced personal effort.

   
\\paragraph{\\textbf{Barrier:\\\\}}   
The Barrier code reflected perceived response cost and clarified why confidence and capability alone did not consistently influence behaviour. Participants acknowledged the organisational risk. Multiple participants stated:

\\begin{quote}  
    \\small \\textit{If I am sharing some personal information of \[organisation\] with others, then it can affect the whole organisation. (P1-003)} \\\\  
    \\small \\textit{Based on individual action, it might cost the organisation, if we are not very careful. (P1-004)}  
\\end{quote}

Barriers were also evident in response processes. When asked about incident escalation, several participants described uncertainty and delay:

\\begin{quote}  
    \\small \\textit{If something happened with my laptop, I try to fix it myself ... I do not know \[who to contract\]. (P1-001)} \\\\  
    \\small \\textit{While my immediate thought is about protecting myself, I haven't previously considered the potential harm to the organisation. (P1-002)} \\\\  
    \\small \\textit{I do not know what the consequence will be. (P1-006)}  
\\end{quote}

This showed participants were unsure and had a limited motivational scope, with effort investment remaining personal; uncertainty increased perceived cost. Also observed absence of consequences further reduced protective motivation. Participants clearly demonstrated the awareness and action gap \\citep{Alshaikh2021Model, alshaikh2020, jeong2021}; they recognised vulnerability and potential consequences but failed to act. High realised effort (response costs) dominated protective behaviour by reducing coping motivation, consistent with PMT research showing that elevated response costs weaken behavioural interpretation \\citep{Kiran2025, Latif2025}.

This theme 3 extended PMT theory by showing that coping appraisal components self-efficacy, response efficacy, and response cost; were weighed together in daily work contexts \\citep{Kiran2025, Menard2017, Tsai2016}. The findings showed participants weighed confidence, effectiveness, and effort together when deciding on cybersecurity actions. This offered context-specific insights into coping strategies shaped by organisational conditions, workload, and responsibility in higher education.

\\subsection\[Theme 4 \- Proactive and Compliant Cybersecurity Behaviours\]{Theme 4 \- Proactive and Compliant Cybersecurity Behaviours:}  
\\label{sec:P1T4}  
This theme 4 captures how participants represented cybersecurity behaviour in routine work contexts. It reflects situations where individuals recognised risks, expressed intention to act, and demonstrated compliance with organisational expectations through safe practices. Together, the codes showed how privacy-related reasoning became enacted behaviour within routine work contexts.

Figure \\ref{fig:5.6} visualises Theme 4 (P1-T4) code structure emerging from Table\~\\ref{tab:5.1} data. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:D}.\\\\

 

\\begin{figure}\[H\] %\[\!ht\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 4 (P1-T4) Code Structure\]{%  
    \\textbf{Figure 5.6}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 4 (P1-T4) Code Structure.}  
    }  
    \\label{fig:5.6}  
   
    % \\addcontentsline{lof}{figure}{5.6 \\hspace{0.18cm} Visual Summary of Theme 4 (P1-T4) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c5/5.5\_P1T4.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{ }  
    \\end{minipage}  
\\end{figure}  
   
 

This theme (P1-T4) consists of four codes that showed how participants considered Cybersecurity Intentions, Policy Compliance, Risk Awareness, and Safe Practices. 

\\paragraph {\\textbf{Code: Cybersecurity Intentions\\\\}}  
The Cybersecurity Intentions code captured expressed commitments to act securely when facing potential threats. These intentions were often conditional and depended on the context. It showed readiness to adopt protective measures. This depended on perceived ties to the organisation and views of personal versus institutional risk.

This code is refined by three subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Cybersecurity Intentions} property described participants' willingness to engage in protective habits, and individuals actively seek out security options, such as researching before data sharing and using security features like multi-factor authentication for personal safety.  
    \\item The\\textbf{ Organisation and Trust} reflected participants' intent to rely on institutional infrastructure for felt inherent safety, feeling comfortable with sensitive tasks on organisational Wi-Fi.  
    \\item The\\textbf{ Organisation Responsibility} property played a reliance on institutional systems, where participants usually allocated tasks such as malware scanning or breach mitigation to automated tools rather than manual checks.  
\\end{itemize}

Table\~\\ref{tab:5.13} for a sample of interview quotes that represent Cybersecurity Intentions code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Cybersecurity Intentions' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Cybersecurity Intentions' Code}  
\\label{tab:5.13}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Cybersecurity Intentions & Cybersecurity Intentions & \`\`I have thought honestly, but as I have mentioned that there is no such sensitive information in my mobile device or in my laptop. So, I am using that public Wi-Fi, I am safe because I'm not doing any transaction using public Wi-Fi. ... But maybe I am browsing my email, I can do that.'' (P1-006) \\newline \`\`I'm not keeping anything in my personal laptop... my laptop will be a little bit slower If I use VPN... so I'm not using that in my personal laptop.'' (P1-006) \\\\ \\cline{2-3}

 & Organisation and Trust & \`\`According to my personal perception, I think what are the whatever the trainings of \[organisation name\] providing us, that's enough.'' (P1-002) \\newline \`\`It become my habit now... anytime I'm inside the \[organisation\], yeah, would be connected to Wi-Fi and I don't think before I open anything.'' (P1-007) \\\\ \\cline{2-3}

 & Organisation Responsibility & \`\`They \[organisation\] are the iron-built. They don't have to have an issue... every time a file is uploaded, it's always checked.'' (P1-004) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Policy Compliance\\\\}}  
The Policy Compliance code captures how participants described their adherence to institutional cybersecurity rules and the motivation behind expectations. Formal policy documents were frequently overlooked, while rules embedded in systems, mandatory processes, or reinforced by supervisors were more consistently followed.

This code is refined by two subcode properties:    
\\begin{itemize}  
    \\item The\\textbf{ Policy} property identified the participants' awareness of formal written guidelines, such as password change or data sharing rules, but low engagement led to reliance on automated prompts over self-guided compliance.   
    \\item The\\textbf{ Willingness} property captured participants' mindset, readiness to follow security protocols only when non-compliance risked professional job status via direct authority or supervisor enforcement.    
\\end{itemize}

Table\~\\ref{tab:5.14} for a sample of interview quotes that represent the Policy Compliance code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Policy Compliance' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Policy Compliance' Code}  
\\label{tab:5.14}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Policy Compliance & Policy & \`\`I don't know what current password policy means, but \[organisation\] sends us emails sometimes that you have to change your email periodically. So, when I received this email \[Password change notification\], I changed my email password.'' (P1-006) \\newline \`\`Policies and policies, aren't they? They're just. You know, not great fun reading... there's nothing for you to read it.'' (P1-005) \\\\ \\cline{2-3}

 & Willingness & \`\`I will only share if my supervisor suggests me... if it is a job-related or work-related thing, I shall not share it. Rather, I shall ask my job supervisor.'' (P1-006) \\newline \`\`If it is come to my personal... I would give it... but if it is work... I will not share it because even my job is at stake... Still, my job would be at stake breaching policy.'' (P1-007) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Risk Awareness\\\\}}  
   
The Risk Awareness code captures how recognised risks triggered or failed to trigger behavioural compliance. It reflects how individuals distinguished between ‘safe' and ‘unsafe' digital conditions, and how this judgement shaped their willingness to comply with or bypass institutional security measures.

This code is refined by two subcode properties:    
\\begin{itemize}  
    \\item The\\textbf{ Vulnerability Awareness} captured the participant's recognition of their personal or departmental exposure to harm, specifically regarding financial data, identity theft, or professional standing.   
    \\item The\\textbf{ Risk Indicators} property referred to cues like system blocks, suspicious websites, or access issues signalling threats; participants often took workarounds when security filters impeded productivity instead of supporting protection.  
\\end{itemize}

See Table\~\\ref{tab:5.15} for a sample of interview quotes that represent the Code ‘Risk Awareness' and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Risk Awareness' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Risk Awareness' Code}  
\\label{tab:5.15}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Risk Awareness & Vulnerability Awareness & \`\`Nothing they \[Hacker\] can \[do\], at most like, contact me, send me spam... Even if it is compromised, they can't do identity theft because my identity is already established.'' (P1-004) \\newline \`\`We never use data that could breach privacy.'' (P1-007) \\\\ \\cline{2-3}

 & Risk Indicators & \`\`Because I first look where I am giving \[data\], what are the suits who are collecting and who are collecting? If I am not clear... then I hesitate to provide those.'' (P1-006) \\newline \`\`Since the servers are in my organisational scope, I did not use encryption \[data sharing\].'' (P1-002) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Safe Practices\\\\}}  
The Safe Practices code, categorised under Behavioural Intentions, describes the specific habits and routine security measures participants intend to adopt in their daily digital interactions. This code reflected the shift from awareness to performed behaviour, showing how individuals balanced protection against technical performance and personal convenience.

This code is refined by three subcode properties:    
\\begin{itemize}  
    \\item The\\textbf{ Action Likelihood} measured participants' probability of performing security tasks only when high perceived threats justified the technical hassle or bandwidth impact.  
    \\item The\\textbf{ Active Participation} captured participants' willingness to use institutional security tools or seek help only when aligned with immediate work needs.  
    \\item The\\textbf{ Security Awareness} reflected participants' grasp of private data and knowledge of digital threats. This built a preventative mindset. Users instinctively avoided risks like sharing passwords or clicking malicious links, even without supervision.  
\\end{itemize}

Table\~\\ref{tab:5.16} for a sample of interview quotes that represent the code ‘Safe Practices' and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Safe Practices' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Safe Practices' Code}  
\\label{tab:5.16}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Safe Practices & Action Likelihood & \`\`And even if I click and see there is it, there's a probability of something is going on or wrong, so I don't proceed further.'' (P1-004) \\newline \`\`I normally \[without encryption\] send because the person sometimes I'm sharing they think it's inconvenient to have a password... it defeats the purpose.'' (P1-004)\\\\ \\cline{2-3}

 & Active Participation & \`\`I know that \[IT Department name\]. And I have also taken some support for whenever I need it. But for installing any software which requires that IT support, I don't install it.'' (P1-006) \\\\ \\cline{2-3}

  & Security Awareness & \`\`I had some knowledge beforehand from my previous experience... it was further enhanced when I started working at \[organisation name\]. I received some training on privacy.'' (P1-002) \\newline \`\`I'm kind of person who do bite of research before I share my information.'' (P1-007) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 4 \- Discussion:}  
\\label{sec:DP1T4}  
Theme 4 demonstrated how privacy mental models moved from interpretation to performance. While earlier themes showed how participants assessed threat and coping, this theme reveals when and why behaviour became observable. Compliance was not automatic. Behavioural intention appeared when personal relevance, faced consequences, and organisational signalling supported it. Research supported that clear expectations and situational relevance are critical determinants of security compliance behaviour \\citep{Alshaikh2021Model, Anderson2010}.

\\paragraph{\\textbf{Cybersecurity Intentions:\\\\}}  
Cybersecurity intentions were often conditional and performance-biased. Participants did not decline the secure behaviour necessity; they calibrated it against convenience and perceived sensitivity. One participant stated:

\\begin{quote}  
    \\small \\textit{I have thought honestly, but as I have mentioned that there is no such sensitive information in my mobile device or in my laptop. So, I am using that public Wi-Fi, I am safe because I'm not doing any transaction using public Wi-Fi. ... But maybe I am browsing my email, I can do that. (P1-006)} \\\\  
    \\small \\textit{I'm not keeping anything in my personal laptop ... my laptop will be a little bit slower if I use VPN \[secure software\] ... so I'm not using \[security\] that in my personal laptop. (P1-006)}  
\\end{quote}

Participants overlooking risks revealed a gap between awareness and cybersecurity incident possibility. Intention impacted action as it was calibrated to personal importance rather than systemic vulnerability. Similarly, other participants relied wholly on organisational protection measures, believing everything would be fine on the network; this mindset left them more open to attacks and risked larger incidents. Several participants shared:

\\begin{quote}  
    \\small \\textit{It become my habit now ... anytime I'm inside the \[organisation\], yeah, would be connected to Wi-Fi and I don't think before I open anything. (P1-007)} \\\\  
    \\small \\textit{They are the iron-built … every time a file is uploaded, it's always checked \[by security\]. (P1-004)}  
\\end{quote}

This presented the routine habits, limited behavioural intention change as threats evolved. Security was recognised in principle by participants. Consistent intention to act depended on the personal relevance and actionability of the risk.

   
\\paragraph{\\textbf{Policy Compliance:\\\\}}  
Policy compliance was conditional, not internalised. Policies were acknowledged by participants but rarely served as active decision-making references. Consistent with behavioural security research, intention to comply emerged as a critical factor of actual compliance behaviour \\citep{Ifinedo2012, Moody2018}, yet this individual behaviour intention was itself weakened by the conditional nature of participants' policy engagement. Several participants expressed policies as officially available but practically distant:

\\begin{quote}  
    \\small \\textit{Even if you put the policy on there ... before clicking, no one will ever read it. (P1-004)} \\\\  
    \\small \\textit{Policies and policies, aren't they? They're just. You know, not great fun reading ... there's nothing for you to read it. (P1-005)}  
\\end{quote}

This demonstrated that policies' presence was acknowledged by participants, yet they perceived no inherent value. Compliance increased when policy expectations were translated into operational signals, particularly through supervisors. As one participant noted:

\\begin{quote}  
    \\small \\textit{I don't know what current password policy means, but \[organisation\] sends us \[system notification\] emails sometimes that you have to change your email periodically. So, when I received this email \[Password change notification\], I changed my email password. (P1-006)}   
\\end{quote}

This showed that managerial and organisational reinforcement acted as a behavioural trigger. Policy became actionable when socially embedded; without reinforcement, compliance relied on automated system cues or fear of professional repercussions. Prior studies also showed that reminder-based compliance could hide underlying knowledge gaps and reduce resilience when cues were absent \\citep{Moody2018}. System reminder notification-driven compliance suggested procedural obedience over conceptual understanding.

\\paragraph{\\textbf{Risk Awareness:\\\\}}  
Risk awareness acted as a situational filter through minimisation and selective vigilance. Participants identified security concerns clearly but bypassed them to maintain workflow convenience. Participants assumed that internal approaches provided sufficient protection, reducing perceived need for extra safeguards. Some participants downplayed vulnerability:

\\begin{quote}  
    \\small \\textit{Nothing they \[Hacker\] can \[do\], at most like, contact me, send me spam ... Even if it is compromised, they can't do identity theft because my identity is already established. (P1-004)} \\\\  
    \\small \\textit{Since the servers are in my organisational scope, I did not use encryption \[data sharing\]. (P1-002)}  
\\end{quote}

This illustrated that institutional trust enlarged individual risk appraisal. Individual vulnerability awareness remained secondary. However, convenience frequently overrode safer options and security signalling. One participant noted:

\\begin{quote}  
    \\small \\textit{Sometimes, I use a Google Drive link I sent them using link because I've experienced problems in this in the past, like people who go outside of our \[organisation\], they can't access the teams \[shared files\] … it's a security concern. I have to switch to something which is more convenient. (P1-004)}  
\\end{quote}

Participants prioritised workflow over organisational security in routine work. Prior research exposed that awareness alone is insufficient unless individuals understand real consequences and appropriate responses \\citep{Alshaikh2021Model, Singh2024}.

\\paragraph{\\textbf{Safe Practices:\\\\}}  
Safe practices were embedded in everyday practice. Some participants adopted preventative and limiting habits:

\\begin{quote}  
    \\small \\textit{And even if I click and see there is it, there's a probability of something is going on or wrong, so I don't proceed further. (P1-004)} \\\\  
    \\small \\textit{I'm kind of person who do bite of research before I share my information. (P1-007)}  
\\end{quote}

Interview data showed adoption of secure practices. Participants similarly described cautious information handling. In contrast to that, some participants stated:

\\begin{quote}  
    \\small \\textit{I feel it sometimes might slow my Internet ... I usually don't use it unless \[protection\] it's required. (P1-004)} \\\\  
    \\small \\textit{I normally \[without encryption\] send because the person sometimes I'm sharing they think it's inconvenient to have a password ... it defeats the purpose. (P1-007)}  
\\end{quote}

This deepened that safe practices were performed when effort was manageable and threat recognition was immediate. Behaviour defaulted to convenience when friction increased. Prior research linked responsible individual practices and rooted safeguards to stronger organisational resilience, particularly when integrated into daily work \\citep{Safa2015, Uchendu2021}.

This theme 4 confirmed prior research that behavioural intention and policy compliance determined cybersecurity behaviour \\citep{Anderson2010, Hina2019, Ifinedo2012}. However, it extended findings by showing intention did not always result in secure action; instead, ease of use, trust, and workflow disruption influenced it. This aligned with studies noting awareness and intention needed contextual reinforcement \\citep{Kiran2025, Sharma2022}, offering higher education-specific insights into role-shaped compliance. 

 

\\subsection{Theme 5 \- Addressing Gaps in Leadership and Authority Support }  
\\label{sec:P1T5}  
This theme 5 captured how gaps in supervisory and institutional authority support shaped participants' cybersecurity behaviour. These gaps influenced how participants understood responsibility and risk within their privacy mental model. Participants described situations where unclear guidance, limited managerial reinforcement, or distant IT authority reduced their confidence to act and delayed escalation during security incidents. This theme showed that individual awareness and intention were often constrained when organisational leadership signals and practical support were inconsistent or weak. Unlike Theme 3, which focused on individual coping costs, this theme highlights external structural influences on behaviour. Participants often hesitated not because they lacked awareness, but because authority signals were unclear.

Figure \\ref{fig:5.7} visualises Theme 5 (P1-T5) code structure emerging from Table\~\\ref{tab:5.1} data. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:D}.\\\\

\\begin{figure}\[H\] %\[\!ht\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 5 (P1-T5) Code Structur\]{%  
    \\textbf{Figure 5.7}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 5 (P1-T5) Code Structure.}  
    }  
    \\label{fig:5.7}  
   
   
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c5/5.6\_P1T5.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{ }  
    \\end{minipage}  
\\end{figure}   
   
 

This theme (P1-T5) consist of one code that illustrates how organisational hierarchy influenced participants' interpretation of responsibility and proper action.\\\\

\\paragraph{\\textbf{Insufficient Support:\\\\}}  
The Insufficient Support code captured participants' perceptions of limited practical guidance from supervisors, managers, and central IT authorities in relation to cybersecurity expectations. Participants noted that technical approaches existed. Yet a lack of proactive clarification, feedback, or role-specific direction led them to use personal intuition for cybersecurity situations.

This code is refined by two subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Supervisor \\& Managers} property described the lack of direct cybersecurity discussion or guidance from immediate leadership, where managers assume employees already possess the necessary knowledge.   
    \\item The\\textbf{ Authority} property captured the perceived inadequacy of centralised support. It involved unclear escalation pathways, limited role-relevant guidance, and limited face-to-face or after-hours access.  
\\end{itemize}

See Table\~\\ref{tab:5.17} for a sample of interview quotes that represent ‘Insufficient Support' code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Insufficient Support' Code\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Insufficient Support' Code}  
\\label{tab:5.17}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Insufficient Support & Supervisor \\& Managers & \`\`No, they \[organisation\] just told me that. There are some privacy regulations and guidelines. Just follow them. But they didn't actually tell me about the consequences directly... \[also\] not from the supervisors.'' (P1-002) \\newline \`\`They believe I should know those things. That's why they did not disclose those things.'' (P1-006) \\newline \`\`No, it's like there's not a topic of that's ever discussed, I think.'' (P1-005) \\\\ \\cline{2-3}

 & Authority & \`\`No, no one gave me, absolutely no one \[regarding cybersecurity guidance\]... I think they should impart the knowledge.'' (P1-004) \\newline \`\`If it is after hours, then I have mentioned whether I shall look that which is there any number or anything that I can call. If not, then in the next day I shall call.'' (P1-006) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 5 \- Discussion:}  
\\label{sec:DP1T5}  
Theme 5 examined how gaps in leadership and organisational authority acted as obstacles. Participants described uncertainty in guidance, reinforcement, and authority accessibility. These impacted privacy decisions or delayed responses. While prior research has established that leadership tone and modelling influence security culture \\citep{alshaikh2020, DaVeiga2020, Georgiadou2022}, present findings extend this study by showing that the absence of supervisor, managerial, and authority support actively exhausted individual cybersecurity behaviour.

\\paragraph{\\textbf{Insufficient Support:\\\\}}  
Participants frequently reported that supervisors referenced policy but rarely linked it to role-specific expectations. Several participants noted: 

\\begin{quote}  
    \\small \\textit{No, they \[organisation\] just told me that. There are some privacy regulations and guidelines. Just follow them. But they didn't actually tell me about the consequences directly ... \[also\] not from the supervisors. (P1-002)} \\\\  
    \\small \\textit{No, no one gave me, absolutely no one \[regarding cybersecurity guidance\] ... I think they should impart the knowledge. (P1-004)} \\\\  
    \\small \\textit{They did not disclose those things ... there are some trainings mandatories for any staff. So, they advised me to take those trainings, that's it. (P1-006)}  
\\end{quote}

Participants illustrated that management informed without explanation of their meaning. It showed how unclear supervisory or manager guidance and unclear authority support interrupted individual decision-making and delayed escalation \\citep{Patterson2024}. 

The communication gap created dependency; employees wished to escalate but felt unprepared. Several participants suggested the practical situation:

\\begin{quote}  
    \\small \\textit{The basic training ... should be face-to-face ... this information should be clearly disseminated so that there is no gap. (P1-006)} \\\\  
    \\small \\textit{If supervisor shares something about the cybersecurity or protection issue from their experience, that will alert the staff. (P1-006)}  
\\end{quote}

One participant emphasised that face-to-face training or guidance proved more effective than email or online modules. Also shared that supervisor guidance set the tone for employees to take cybersecurity seriously. Similarly, participants perceived support latency undermined confidence in responding; lack of immediate contacts caused delays in reporting incidents until the next day.

\\begin{quote}  
    \\small \\textit{If it is after hours, then I have mentioned whether I shall look that which is there any number or anything that I can call. If not, then in the next day I shall call. (P1-006)}  
\\end{quote}

Participants demonstrated that where authority seemed abstract or reactive, intuition, workarounds, or delayed reporting occurred. Theme 5 identified supervisory and authority support as key necessities. These transformed awareness and intention into consistent cybersecurity behaviour in higher education.

This theme 5 confirmed prior research that leadership, culture, and governance influenced cybersecurity behaviour \\citep{alshaikh2020, DaVeiga2020, Sharma2022}. However, it extended findings by revealing absent or unclear guidance disrupted decisions and delayed protective action. Participants used personal judgement without clear organisational signals, showing behaviour relied on visible authority in higher education \\citep{Hina2019, Pollini2022}.

 

\\section{Summary and Conclusion}  
\\label{sec:5.4}  
Phase 1 showed that individual cybersecurity behaviour in higher education was shaped by privacy-based mental models, not by policy availability or awareness exposure alone. Adopting Protection Motivation Theory, analysis demonstrated that participants understood threats and coping options through personal relevance, convenience, and perceived responsibility, which formed selective protection habits even when risks were recognised.

The findings indicated that awareness and training operated as weak controls when they were disconnected from real experience. Participants did not reject cybersecurity training as irrelevant. Instead, they assessed it against workload pressure, perceived immediacy, and trust in institutional protection, which meant engagement became conditional and often delayed. Poor training outcomes were not from knowledge gaps but from issues of relevance and reinforcement, as institutional communication competed with habits and selective privacy views.

Across Themes 1 and 2, awareness and threat assessment failed because they were filtered through experience and perceived consequences. Training was adopted when it felt directly relevant, reinforced, or incident-linked, yet it was discounted when it appeared basic or disconnected from practice. Vulnerability and severity were measured through personal harm thresholds, and organisational impact was repeatedly taken as irrelevant, which explains why exploitability stayed despite minimal awareness.

Themes 3 and 4 clarified why intention did not reliably become action. Coping decisions depended on confidence, perceived effectiveness, adjusted trust, and response cost; where protective behaviour was perceived as disruptive, slow, or procedurally unclear, convenience became the influential choice. Compliance was most consistent with supervisor encouragement, monitoring, and easy secure options, not just email policy reminders.

Theme 5 identified leadership and authority support as the behavioural infrastructure that determined whether secure practice could be sustained. When supervisors and IT authorities provided instruction without explanation, or when escalation pathways felt challenging or delayed, participants relied on personal judgment and unauthorised workarounds. 

Phase 1 answered RQ1 (see Section\~\\ref{sec:1.5}) by showing that privacy mental models shaped cybersecurity behaviour through perceived sensitivity, responsibility allocation, and judgements of worthwhile action. This provides the basis for Phase 2's focus on organisational culture, individual intention and governance conditions.

\\chapter{Phase 2 Findings and Discussion}  
\\label{chapter:c6}

\\setcounter{figure}{0}  
\\renewcommand{\\thefigure}{6.\\arabic{figure}}

\\section{Introduction}  
\\label{sec:6.1}

The previous chapter presented Phase 1 findings and discussion, addressing Research Question 1 (RQ1) at the individual level. This Chapter\~\\ref{chapter:c6} forwards the focus to RQ2 by studying how organisational culture and individual behaviour structural conditions influence cybersecurity readiness. The analysis is drawn from Phase 2 semi-structured interviews and lensing findings through Schein's cultural framework, including artefacts, values, and underlying assumptions \\citep{Adamu2025, Schein2010, Schein2019, Venkat2020}, which is discussed in Chapter\~\\ref{chapter:c2} (see Section \\ref{sec:2.8}).

This chapter explored how leadership signals, governance arrangements, communication patterns, and institutional cultures either highlighted or restricted secure behaviour. This extended Phase 1 individual insights to the organisational level. It offered a cultural explanation for the behaviour patterns identified in Chapter\~\\ref{chapter:c5}. This aligned with research, which implied that human behaviour and cultural factors shaped cybersecurity readiness in higher education \\citep{Georgiadou2022}.

Figure \~\\ref{fig:6.1} presents the roadmap for Chapter 6, outlining the structure of the Phase 2 findings and discussion.\\\\  
 

 \\begin{figure}\[H\]  
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 6 Roadmap\]{%  
    \\textbf{Figure 6.1}\\\\\[1.2em\]  
    \\textit{Chapter 6 Roadmap.}  
    }  
    \\label{fig:6.1}  
      
   
      
    \\includegraphics\[width=0.9\\linewidth\]{Figures/c6/6.1roadmap.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

\\section{Phase 2 \- Research Findings and Discussion}  
\\label{sec:6.2}

This section presents the findings emerging from Phase 1 of the study. Building on the template analysis process towards the findings, five new themes were finalised, reflecting how participants perceived privacy, evaluated cybersecurity risks, and expressed these understandings through their everyday behaviours.

Each theme was discussed in sequence, with selected quotations showing how privacy-related mental models shaped cybersecurity behaviours in practice. Together, the themes presented a coherent response of individual reasoning and cybersecurity action

\\subsection{Phase 2 \- Themes Overview}  
\\label{sec:6.2.1}

Eleven themes emerged in this Phase 2, each capturing a distinct organisational condition. Below follows a brief description of each theme.

\\begin{itemize}  
    \\item \\textbf{Theme 1: Physical Symbolism and Security Culture Blind Spots} \\\\  
    This theme defined how visible artefacts impacted perceptions of cybersecurity priority within higher education environments. Absent or fading physical indications created low urgency, weakening daily awareness.

    \\item \\textbf{Theme 2: Organisational Values Are Not Reflected in Daily Leadership Decisions} \\\\  
    This theme showed that leadership actions often challenged clear portrayal in cybersecurity values. Selective enforcement failed cultural consistency and harmed employees’ interpretation of security importance. 

    \\item \\textbf{Theme 3: Assumptive Resistance Loops Undermining Cybersecurity Readiness} \\\\  
    This theme captured persistent assumptions that continued detachment from cybersecurity duties. Perceived irrelevance and a delegated responsibility mindset created self-reinforcing patterns of bypassing security rules.

    \\item \\textbf{Theme 4: Experiential Trust Threshold in Incident Reporting} \\\\  
    This theme identified that reporting decisions depended on prior experience and perceived mental safety. Formal procedures existed, but staff required help or reported concerns only when trust exceeded fear of negative consequences.

    \\item \\textbf{Theme 5: End-User Behavioural Drift and Compliance Fatigue} \\\\  
    This theme revealed gradual disengagement caused by the suffered procedural burden and workload. Repeated demands reduced attention to security tasks, leading to minimal compliance.  
      
    \\item \\textbf{Theme 6: Cultural Miscalibration in Cyber Risk Perception} \\\\  
    This theme demonstrated misalignment between formal threat beliefs and daily cultural assumptions. Cyber risks were often underestimated, dismissed, or deprioritised within organisational practice.  
      
    \\item \\textbf{Theme 7: Security Culture Embarrassment Barrier } \\\\  
    This theme showed that social discomfort limited open discussion of security mistakes. Fear of reputational harm or appearing professionally incompetent suppressed reporting and collective learning.  
      
    \\item \\textbf{Theme 8: Leadership Lag in Onboarding Cybersecurity Policy } \\\\  
    This theme identified weak translation of cybersecurity expectations during organisational entry processes. Unclear or overly general onboarding modules reduced early norm formation; leaders also were uncertain about new employees’ understanding.  
      
    \\item \\textbf{Theme 9: Strategic Weakness in Security Governance in Academia } \\\\  
    This theme captured strategic downfall in cybersecurity action and oversight. Governance structures existed but lacked coordination, accountability, clarity, and consistent follow-up.  
      
    \\item \\textbf{Theme 10: Leadership and Behavioural Dynamics Influencing Cybersecurity Culture} \\\\  
    This theme examined how leadership behaviour with the individual, relationship dynamics shaped cybersecurity practices after a new policy implementation. Silence, avoidance, or inconsistent reinforcement permitted behavioural drift despite formal controls.  
      
    \\item \\textbf{Theme 11: Ignorance Towards Policy } \\\\  
    This theme examined how leadership behaviour and relationship comfort shaped cybersecurity practices. Silence, avoidance, use common sense, or an inconsistent reinforcement policy ignorance.  
      
\\end{itemize}

Each theme comprised multiple codes, and the study focused on codes for deeper insight into improving analytical depth. Themes 1-11 contained multiple codes.\\\\

\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Illustration of Phase 2 Final Template\]{%  
    \\textbf{Figure 6.2}\\\\\[1.2em\]  
    \\textit{Illustration of Phase 2 Final Template.}  
    }  
    \\label{fig:6.2}

    % \\addcontentsline{lof}{figure}{6.2 \\hspace{0.18cm} Illustration of Phase 2 Final Template.}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.2finaltemplate.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
                \\textit{\\\\Note.} Format Adopted From "Optimising data sharing whilst protecting participant privacy: a data note describing processed data from a qualitative study of healthcare professionals’ experiences of caring for women with false positive screening test results" (p.11), by\~\\citet{Long2025}, (https://doi.org/10.1080/21642850.2024.2449400).Open Access article  
    \\end{minipage}  
\\end{figure}

\\subsection{Phase 2 \- Final Coding Template}  
\\label{sec:6.2.2}

The Phase 2 final template summarised the coding structure developed through the analysis (see Sections \\ref{sec:4.7.2} and \\ref{sec:4.7.4}), presenting a consolidated view of how organisational-level data were interpreted. It showed how the initial template informed by the organisational lens evolved through iterative refinement into a stable hierarchical structure. This process followed the six-step template analysis procedure outlined in Chapter \\ref{chapter:c4} (Section \\ref{sec:4.7.4}), ensuring that analytical decisions remained consistent and transparent across phases.

The resulting final template captured how organisational culture, leadership practices, and governance processes shaped cybersecurity readiness, combining predefined theoretical categories with patterns emerging directly from participant accounts. Figure \\ref{fig:6.2} presents this structure visually, while Table \\ref{tab:6.1} details the progression from initial template (see Section \\ref{sec:4.7.2}) elements to final codes, sub-code properties, and themes. The themes were examined in depth in the subsequent sections.\\\\

   
 

\\subsection{Phase 2 \- Research Findings Code Structure}  
\\label{sec:6.2.3}

Table \\ref{tab:6.1} presents the analytical structure underlying the Phase 2 findings and the final template. It shows how the organisation-informed initial template was refined through data-driven coding to produce the final themes. This structure demonstrated how cultural, leadership, and governance elements were interpreted and reorganised during analysis.  
   
Blue-shaded portions represented theory-informed constructs from the Phase 2 initial template (see Section \\ref{sec:4.7.2}). Peach-shaded portions indicated codes, sub-code properties, and themes emerging directly from participant data. This visual difference clarified where findings aligned with existing theoretical expectations and where new patterns were identified through empirical analysis.  
   
Table \\ref{tab:6.1} also highlights how the analytical structure evolved during coding. Blank cells indicated that no predefined Initial pre-themes existed at that level and that these elements emerged through the data analysis. The hierarchical numbering (e.g., 1.1.1) traced the progression from initial categories to refined codes and sub-code properties, supporting transparency and analytical traceability throughout the framework.\\\\

 %myone  
\\begingroup  
\\setlength{\\arrayrulewidth}{1.2pt}  
% \--- COLOR OPTIONS \---  
\\definecolor{frameworkblue}{HTML}{D0E1F9}   
\\definecolor{findingspeach}{HTML}{FAD7C4}  
\\definecolor{white}{HTML}{FFFFFF}

\\small  
\\begin{spacing}{1.0}

\\begin{longtable}{p{1.2cm} p{1.2cm} p{3.2cm} p{5.0cm} p{3.0cm}}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\caption\[Phase 2 \- Research Findings Summary Code Structure\]{%  
\\\\\[1.2em\]  
\\textit{Phase 2 \- Research Findings Summary Code Structure}  
\\label{tab:6.1}  
}  
\\\\

\\hline  
\\rowcolor{white} \\multicolumn{2}{c}{\\textbf{Initial Template}} & \\multicolumn{3}{c}{\\textbf{Research Findings}}  \\\\ \\hline  
\\rowcolor{white} \\textbf{Prior Themes} & \\textbf{Sub-Theme} & \\textbf{Code} & \\textbf{Sub-Code Properties} & \\textbf{Emerged Theme (T)} \\\\ \\hline  
\\endfirsthead

\\hline  
\\rowcolor{white} \\textbf{Prior Themes} & \\textbf{Sub-Theme} & \\textbf{Code} & \\textbf{Sub-Code Properties} & \\textbf{Emerged Theme (T)} \\\\ \\hline  
\\endhead

\\multicolumn{5}{r}{\\textit{}} \\\\  
\\endfoot

\\hline  
\\endlastfoot

% \--- THEME 1 \---  
\\cellcolor{frameworkblue} 1\. Organisational Culture & \\cellcolor{frameworkblue} 1.1 Artefacts & \\cellcolor{findingspeach} 1.1.1 Lack of Awareness on Physical Security. & \\cellcolor{findingspeach} \- Office Layout ; \- Weak Enforcement of Security Policies; \- Visual Indication; \- Physical Security & \\cellcolor{findingspeach} Physical Symbolism and Security Culture Blind Spots (P2-T1)\\\\ \\hline

% \--- THEME 2 \---  
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} 1.2 Values & \\cellcolor{findingspeach} 1.2.1 Impact of Disagreement Between Organisational and Personal Values. & \\cellcolor{findingspeach} \- Disagreement Values & \\cellcolor{findingspeach} Organisational Values Are Not Reflected in Daily Leadership Decisions (P2-T2) \\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 1.2.2 Leader Handled Employee Conflicts or Decision-Making Based on Experience, Not Values or Policy. & \\cellcolor{findingspeach} \- Not Promoting Values; \- Values Not Top-of-Mind (Leaders); \- Culture Navigating Ethical Dilemmas (Leadership and Employee) & \\cellcolor{findingspeach} \\\\ \\hline

% \--- THEME 3 \---  
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} 1.3 Underlying Assumptions & \\cellcolor{findingspeach} 1.3.1 Individual Assumptions May Risk or Undermine Organisational Cybersecurity Readiness. & \\cellcolor{findingspeach} \- Individual Assumption and Resistant Avoidance Risk & \\cellcolor{findingspeach} Assumptive Resistance Loops Undermining Cybersecurity Readiness (P2-T3)\\\\   
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 1.3.2 Individuals Feel There Is Always a Gap Between Organisational Policy Implementation and Communication. & \\cellcolor{findingspeach} \- Lack of Communication and Feedback ; \- Unsatisfied Leader & \\cellcolor{findingspeach} \\\\ \\hline

% \--- THEME 4 \---  
\\cellcolor{frameworkblue} 2\. Individual Behaviour & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 2.1.1 Individual Incident Reporting Depends on Trust & \\cellcolor{findingspeach} \- Impact of Knowledge and Experience; \- Experiential Learner & \\cellcolor{findingspeach} Experiential Trust Threshold and Disengagement in Incident Reporting (P2-T4) \\\\ \\hline

% \--- THEME 5 \---  
\\cellcolor{frameworkblue} & \\cellcolor{frameworkblue} & \\cellcolor{findingspeach} 2.1.2 Behavioural Fatigue and Disengagement & \\cellcolor{findingspeach} \- End-user Ignorance; \- Individual vs Teamwork; \- Frustration with Security & \\cellcolor{findingspeach} End-User Behavioural Drift and Compliance Fatigue (P2-T5) \\\\ \\hline

% \--- THEME 6 \---  
\\cellcolor{findingspeach} 3\.  & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 3.1.1 Cyber risks due to deep-rooted cultural misperceptions & \\cellcolor{findingspeach} \- Organisational Cybersecurity Insufficient Practices; \- Lack of Seriousness Toward Cybersecurity & \\cellcolor{findingspeach} Cultural Miscalibration in Cyber Risk Perception (P2-T6) \\\\ \\hline

% \--- THEME 7 \---  
\\cellcolor{findingspeach} 4\.  & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 4.1.1 Cultural Hesitation to Report Incidents Due to Fear or Embarrassment & \\cellcolor{findingspeach} \- Leaders Believe; \- Lack of Leadership Initiative    & \\cellcolor{findingspeach} Security Culture Embarrassment Barrier (P2-T7) \\\\ \\hline

% \--- THEME 8 \---  
\\cellcolor{findingspeach} 5\.  & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 5.1.1 Leadership Lag in Onboarding Cybersecurity Policy Awareness & \\cellcolor{findingspeach} \- Gap Between Leaders and New Joiners  & \\cellcolor{findingspeach} Leadership Lag in Onboarding Cybersecurity Policy (P2-T8) \\\\ \\hline

% \--- THEME 9 \---  
\\cellcolor{findingspeach} 6\.  & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 6.1.1 Organisational Actions Are Not Effective Enough & \\cellcolor{findingspeach} \- Doubt Over Organisations' Ability; \- Poor Leadership in Handling of Incidents; \- Frustration over Reactions to cybersecurity drills and exercises & \\cellcolor{findingspeach} Strategic Weakness in Security Governance in Academia (P2-T9)  \\\\ \\hline

% \--- THEME 10 \---  
\\cellcolor{findingspeach} 7\.  & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 7.1.1 Leadership and Behavioural Dynamics Influencing Cybersecurity Culture & \\cellcolor{findingspeach} \-  Employer and Employee Relationship Affects Cybersecurity and Culture; \- Lack of Promoting from Leaders for Cybersecurity Culture and Policy;  \- Lack of Cultural Motivation for Cybersecurity Best Practices & \\cellcolor{findingspeach} Leadership and Behavioural Dynamics Influencing Cybersecurity Culture (P2-T10) \\\\ \\hline

% \--- THEME 11 \---  
\\cellcolor{findingspeach} 8\.   & \\cellcolor{findingspeach} & \\cellcolor{findingspeach} 8.1.1 Ignorance Towards Policy & \\cellcolor{findingspeach} \- Policy Awareness Negligence (Individual Level) ; \- Relying on Common Sense Rather Than Policy; \- Confusion About the Data Protection Policy & \\cellcolor{findingspeach} Ignorance Towards Policy (P2-T11) \\\\ 

\\end{longtable}

\\end{spacing}  
\\endgroup  
 

 

 

\\section{Phase 2 \- Thematic Findings and Discussion}  
\\label{sec:6.3}

This section presents the Phase 2 thematic findings and discussion. It drew on the final template (Figure \\ref{fig:6.2}) and coding structure (Table \\ref{tab:6.1}) to interpret how organisational culture, leadership, and governance shaped cybersecurity readiness. Each theme was supported by participant evidence and critically linked to prior research.

\\subsection{Theme 1 \- Physical Symbolism and Security Culture Blind Spots}  
Theme 1 (P2-T1) showed how visible workplace conditions affected everyday assumptions about privacy and security. Participants described organisational physical surroundings that offered few cues of cybersecurity priority, encouraging casual data handling. Insufficient artefact-level signalled thus undermined awareness despite formal controls and online reminders.  
   
Figure\~\\ref{fig:6.3} visualises Theme 1 (P2-T1) code structure emerging from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix \\ref{appendix:E}.\\\\

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 1 (P2-T1) Code Structure\]{%  
    \\textbf{Figure 6.3}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 1 (P2-T1) Code Structure.}  
    }  
    \\label{fig:6.3}  
    
    % \\addcontentsline{lof}{figure}{6.3 \\hspace{0.18cm} Visual Summary of Theme 1 (P2-T1) Code Structure}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures/c6/6.2\_P2T1.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

This theme (P2-T1) comprises one code that clarified how physical security awareness is formed through everyday artefacts in higher education workplaces. 

\\paragraph{\\textbf{Code: Lack of Awareness on Physical Security\\\\}}  
Participants described limited visibility of reminders, weak access-control signalling, and uncertainty about organisational physical device-handling practices. These reduced security projections in the work routine created cultural blind spots. The code captured the disconnect between employees and physical safeguards for organisational assets.

This code contained four supporting subcode properties, which enhanced the clarity and alignment of the code:

\\begin{itemize}  
    \\item The\\textbf{ Office Layout} property reflected how open-plan designs and shared workspaces normalised visibility of sensitive screens. Participants indicated that spatial design created impressions of exposure.  
      
    \\item The\\textbf{ Weak Enforcement of Security Policies} reflected inconsistent ID badge use, identity checks, and controlled-entry enforcement. Participants viewed poor enforcement as the organisation accepting physical security risks. 

    \\item The\\textbf{ Physical Security} property described limited awareness of device safeguards and uncertainty about device or data disposal processes. 

    \\item The\\textbf{ Visual Indication} property captured absent or faded awareness posters and banners of ‘To do' in offices.   
\\end{itemize}

See Table\~\\ref{tab:6.2} for a sample of interview quotes that represent the Lack of Awareness on Physical Security code and visible patterns.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing ‘Lack of Awareness on Physical \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing ‘Lack of Awareness on Physical Security'}  
\\label{tab:6.2}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Lack of Awareness on Physical Security & Visual Indication & \`\`I remember seeing posters a few years back, but I don't think there are any up these days. Seen it's mostly done through, you know, e-mail.'' (P2-001) \\\\ \\cline{2-3}

& Office Layout & \`\`I think open plan kind of offices don't lend themselves to security. That's always a huge issue... the space is shared by students and staff.'' (P2-004) \\\\ \\cline{2-3}

& Weak Enforcement of Security Policies & \`\`From recollection, last time I had to go and visit \[IT\]... I don't think there was anyone checking anything... there is nothing like that.'' (P2-001) \\\\ \\cline{2-3}

& Physical Security & \`\`What IT services do with the machine \[device\], I have no idea. I'm not really up to speed on how they do it.'' (P2-006) \\newline \`\`I take away/deleted all the data... before I hand back \[the device\]. But actually, what IT services do with the machine, I have no idea.'' (P2-005) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 1 \- Discussion:}  
\\label{sec:DP2T1}

Theme 1(P2-T1) is important because it demonstrated that cybersecurity culture emerged from visible physical signals, not just formal policy. Artefacts such as layout, signs, and access practices communicated daily priorities in HEIs. Absent or unclear artefacts reduced staff awareness and engagement.

Artefacts have been shown to influence security behaviour by shaping attention, responsibility, and behavioural cues \\citep{Schein2010, Schein2019}. Prior studies identified physical security culture as a neglected but foundational component of cybersecurity readiness \\citep{Ciagala2024, DaVeiga2010}.

\\paragraph{\\textbf{Lack of Awareness on Physical Security\\\\}}  
A critical shift from physical visibility to digital perception was revealed, where absent material reminders created mental disconnects from organisational asset protection. One participant noticed:

\\begin{quote}  
    \\small \\textit{I think open plan kind of offices don’t lend themselves to security. That’s always a huge issue... the space is shared by students and staff. (P2-004)}  
\\end{quote}

Open settings highlighted risks like unauthorised access:

\\begin{quote}  
    \\small \\textit{Given that everybody is open cubicles or open space, it’s not that secure. Tailgating is still possible. (P2-008)}  
\\end{quote}

Weak Enforcement masked this perception; participants viewed ID badge use and access controls as procedural formalities without active monitoring \\citep{Adamu2025, Ciagala2024}. One participant shared:

\\begin{quote}  
    \\small \\textit{I don’t think there was anyone checking anything. (P2-001)}  
\\end{quote}

Across interviews, participants noted cybersecurity relied mainly on emails and online modules, lacking workplace physical presence:

\\begin{quote}  
    \\small \\textit{Definitely not in my office, and I can’t recall really seeing much around campus in terms of cybersecurity. (P2-002)} \\\\  
    \\small \\textit{I have never seen any posters or any visual signs about cybersecurity. (P2-006)}  
\\end{quote}

Participants showed a lack of visible cybersecurity awareness materials, such as posters, banners, or signage, which shaped employees’ privacy and security expectations in the workplace \\citep{Chaudhary2022, DaVeiga2010, Dimitrov2013}.

Participants also highlighted uncertainty about device security and disposal processes:

\\begin{quote}  
    \\small \\textit{What IT services do with the machine \[device\]; I have no idea. (P2-005)} \\\\  
    \\small \\textit{I don’t know about their data disposal policy. Probably I might have received it, but it’s not, at least currently in my mind. (P2-006)}  
\\end{quote}

This captured employees’ unawareness of device and data disposal procedures, exposing organisational cybersecurity gaps \\citep{Adamu2025, Sidor2022, Yeng2022}. Invisible artefacts like these created cultural blind spots, undermining HEI readiness.

Collectively, the code exhibited that physical security was culturally deprioritised through artefact-level inconsistencies. Layout, enforcement, and reminders shaped assumptions about acceptable practice, supporting Theme P2-T1 by evidencing physical symbolism’s influence on cybersecurity readiness. 

Collectively, Theme P2-T1 enhances prior research by providing empirically grounded, higher education-specific evidence of how physical artefacts influence cybersecurity culture. While \\citet{Ciagala2024} identified physical security as a neglected foundation, \\citet{DaVeiga2010} proposed artefact-level indicators within security culture frameworks. This theme was extended both by showing how specific artefacts, such as office layout, absent posters, weak enforcement, and unclear device disposal, created measurable cultural blind spots. Similarly, this theme advances \\citet{Georgiadou2022} by supplying qualitative evidence of how visible organisational signals directly influence employee readiness in HEIs.

 

\\subsection \[Theme 2 \- Organisational Values Are Not Reflected in Daily \]{Theme 2 \- Organisational Values Are Not Reflected in Daily Leadership Decisions:}  
\\label{sec:P2T2}

This theme showed organisational values formally acknowledged but inconsistently applied through leadership decisions. Participants noted gaps between values stated priorities and daily practice among conflicts or pressures. Findings revealed cybersecurity values were bypassed for experience or operational needs, rendering policies negotiable.  

Figure\~\\ref{fig:6.4} visualises Theme 2 (P2-T2) code structure and emergence from Table\~\\ref{tab:6.1} data. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.\\\\  
 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 2 (P2-T2) Code Structure\]{%  
    \\textbf{Figure 6.4}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 2 (P2-T2) Code Structure.}  
    }  
    \\label{fig:6.4}  
    
    % \\addcontentsline{lof}{figure}{6.4\\hspace{0.18cm} Visual Summary of Theme 2 (P2-T2) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures/c6/6.3\_P2T2.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

This theme (P2-T2) comprises one code that clarified how organisational value disagreement is reflected in workplaces.  

\\paragraph{\\textbf{Code: Impact of Disagreement Between Organisational and Personal Values\\\\}}  
This code captured situations where leaders' personal beliefs or professional judgments diverged from formal organisational values or policy expectations. Such disagreement shaped selective compliance, informal negotiation, and reduced normative clarity around cybersecurity priorities.

This code contains one supporting subcode property:   
\\begin{itemize}  
    \\item The\\textbf{ Disagreement Values} property reflected ideological or practical tension between institutional vision and individual viewpoints. Perceived counterproductive policies led to superficial compliance not genuine value embrace, creating a weak security culture.  
\\end{itemize}

See Table\~\\ref{tab:6.3} for sample quotes on the \`Impact of Disagreement Between Organisational and Personal Values' code.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing ‘Impact of Disagreement Between \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing ‘Impact of Disagreement Between Organisational and Personal Values’}  
\\label{tab:6.3}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Impact of Disagreement Between Organisational and Personal Values & Disagreement Values & \`\`Different views would be always there... but since we are working in an umbrella, we have to protect this umbrella. Try to minimise the gap.'' (P2-007) \\newline \`\`We try our best to keep in mind all those values… but ultimately, we have to make a decision based on ground reality.'' (P2-006) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\paragraph{\\textbf{Code: Leader Handled Employee Conflicts or Decision-Making Based on Experience, Not Values or Policy\\\\}}  
   
This code captured how leaders resolved conflicts or guided decisions relying on personal experience, majority reasoning, or ground reality judgment over formal value or policy. Leadership behaviour functioned as a practical signal of what truly mattered within the institution. Table \\ref{tab:6.4} presents sample interview quotes to support the code.

This code included three subcode properties that deepened alignment and theme development:  
\\begin{itemize}  
    \\item \\textbf{The Not Promoting Values} flagged passive leadership assumptions that the employee already understood organisational values. Cybersecurity appeared only via external triggers like emails, signalling passive value support.  
    \\item \\textbf{The Values Not Top-of-Mind} indicated that organisational values were not consistently recalled during decision-making.   
    \\item \\textbf{The Culture Navigating Ethical Dilemmas} captured how leaders framed ethical dilemmas pragmatically. Decisions were justified through fairness, realism, or majority consensus rather than explicit policy interpretation. \\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Leader Handled Employee \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Leader Handled Employee Conflicts or Decision-Making Based on Experience, Not Values or Policy'}  
\\label{tab:6.4}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Leader Handled Employee Conflicts or Decision-Making Based on Experience, Not Values or Policy & Not Promoting Values & \`\`I don't see it really as something that I have to constantly remind them about... I have never felt the need to repeat it.'' (P2-004) \\newline \`\`I get reminders when staff haven't done the mandatory cybersecurity training... Look, you have to do this or we're both keep getting emails.'' (P2-001) \\\\ \\cline{2-3}

& Values Not Top-of-Mind & \`\`I honestly would say most academics would not know what the values were off their head now... I don't have them in my mind all the time.'' (P2-002) \\newline \`\`Leadership… they are making decisions from their mind… You have to make a decision that is fair.'' (P2-007) \\\\ \\cline{2-3}

& Culture Navigating Ethical Dilemmas & \`\`Depending on the nature of it, it depends on how we would address it.'' (P2-003) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

 

\\subsubsection{Theme 2 \- Discussion:}  
\\label{sec:DP2T2}

This theme showed that inconsistent leadership decisions undermined stated values, shaping employees’ views of cybersecurity importance under pressure. Participant responses showed leadership often undermined values by overlooking minor violations, delaying responses, or resolving issues informally. The findings showed that gaps between formal controls and lived practice were maintained in higher education, where decentralised structures and local discretion strongly shaped decision-making \\citep{Sabillon2024, ulven2021}. Within organisational culture theory, values functioned as the resolving tier between visible artefacts and deeper assumptions \\citep{Adamu2025, Schein2010, Schein2019}. Prior findings showed that leadership demonstrating is critical for embedding cybersecurity values in organisational practice \\citep{alshaikh2020, Sutton2025}.

\\paragraph{\\textbf{Impact of Disagreement Between Organisational and Personal Values:\\\\}}  
Leaders selectively complied with conflicting policies, reducing formal values’ authority. Several participants summarised this tension by stating:

\\begin{quote}  
    \\small \\textit{Different people may have different views... but we have to protect this umbrella. (P2-007)} \\\\  
    \\small \\textit{There is always this conflict between someone like myself and the IT service. I want to be the admin... It’s very, very stressful. (P2-005)}  
\\end{quote}

When policy is perceived as imposed not co-created, values appear external rather than shared. Responses acknowledged opinion diversity but implied informal management of value disagreements, lacking explicit leadership guidance. 

One participant acknowledged this ideological difference and tension clearly when reflecting on mandated changes in the system and use policy:

\\begin{quote}  
    \\small \\textit{It has been shown that getting people to update \[password\] them too frequently is not a good idea. It has been shown that insisting on special characters etc., is not necessarily promoting good practice, but that is the central \[IT\] policy, and there is no way of changing it. (P2-001)} \\\\  
    \\small \\textit{We try our best to keep in mind all those values… but ultimately, we have to make a decision based on ground reality. (P2-006)}  
\\end{quote}

Ground reality overrode formal value consistency. Together, these showed that leaders’ or management’s ignorance, weak follow-up, and limited consequences normalised underestimation of cyber risk \\citep{Sutton2025}. 

\\paragraph{\\textbf{Leader Handled Employee Conflicts or Decision-Making Based on Experience, Not Values or Policy:\\\\}}  
Leaders resolved conflicts through experience, fairness, or consensus rather than organisational values, weakening policy authority. This mattered as leaders operationalised values through everyday actions. Participants described decision-making that prioritised situational understanding over procedural guidance. Multiple leaders acknowledged:

\\begin{quote}  
    \\small \\textit{My action \[was\] based on my experience... within the constraints I know... not necessarily what is written, but what works in that situation. (P2-001)} \\\\  
    \\small \\textit{Leadership… they are making decisions from their mind… You have to make a decision that is fair. (P2-007)}  
\\end{quote}

Not promoting values captured passive assumptions that employees understood institutional principles. Several participants (P2-002, P2-003, P2-004) shared this mindset. P2-004 stated:

\\begin{quote}  
    \\small \\textit{I don’t see it really as something that I have to constantly remind them about... I have never felt the need to repeat it. (P2-004)}   
\\end{quote}

Values were assumed to be internalised. Prior research indicated that values shape organisational culture only when they are actively recalled, communicated and applied at decision points \\citep{alshaikh2020, Georgiadou2022, Sutton2025}. Others invoked values only under external pressure, such as notification emails, reactively rather than routinely. 

\\begin{quote}  
    \\small \\textit{I get reminders when staff haven’t done the mandatory cybersecurity training... I tell them, ‘You have to do this, or we both keep getting emails.’ (P2-001)}  
\\end{quote}

Compliance appeared from administrative irritation, not value endorsement. This reactivity reduced natural motivation for cybersecurity adherence. 

Collectively, this showed how policy disagreements, experiential decisions, and passive reinforcement diluted cybersecurity priorities. Leadership behaviour translates values into culture. When hesitant, readiness relied on personal judgement rather than institutional commitment.

Theme 2 (P2-T2) both confirmed and enhanced prior research on leadership and cybersecurity culture. It confirmed that leadership modelling was significant for embedding cybersecurity values in organisational practice \\citep{alshaikh2020, Georgiadou2022, ulven2021}. It enhanced \\citet{Sabillon2024} by exposing that gaps between formal controls and practice in HEIs extended beyond technical compliance into daily leadership decision-making. While \\citet{Fenech2024} showed that individual values shaped cybersecurity decisions, this theme extended that insight organisationally, showing how leadership judgements and value contradictions affected higher-education cybersecurity culture.

\\subsection\[Theme 3 \- Assumptive Resistance Loops Undermining\]{Theme 3 \- Assumptive Resistance Loops Undermining Cybersecurity Readiness}  
\\label{sec:P2T3}  
Theme 3 (P2-T3) showed that resistance emerged from repeating assumptions about relevance, responsibility, and feasibility. Participants interpreted controls through personal judgement and adjusted their behaviour to match those views. They framed security as an external IT problem or a burden on productivity, which justified limited engagement and selective compliance. These assumptions formed cycles: low participation yielded weak feedback, reinforcing views of policies as unrealistic or optional for academic work. This gradually weakened organisational readiness.  
   
Figure\~\\ref{fig:6.5} visualises Theme 3 (P2-T3) code structure and emergence from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.\\\\

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 3 (P2-T3) Code Structure\]{%  
    \\textbf{Figure 6.5}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 3 (P2-T3) Code Structure}  
    }  
    \\label{fig:6.5}  
    
    % \\addcontentsline{lof}{figure}{6.5 \\hspace{0.18cm} Visual Summary of Theme 3 (P2-T3) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures/c6/6.4\_P2T3.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

This theme (P2-T3) consists of two codes that clarified how assumptions and communication gaps sustained resistance loops within HEI. 

\\paragraph{\\textbf{Code: Individual Assumptions May Risk or Undermine Organisational Cybersecurity Readiness\\\\}}  
This code referred to how individual assumptions may risk or undermine organisational cybersecurity readiness, which captured how employees interpreted cybersecurity through personal filters of relevance and responsibility. Security was perceived as a technical restriction that clashed with professional autonomy, rather than a shared cultural value, leading participants to frame controls as excessive, irrelevant, or outside their role and reducing shared accountability. Table\~\\ref{tab:6.5} showed sample quotes for this code.

This code included one supporting subcode property:  
\\begin{itemize}  
    \\item \\textbf{The Individual Assumption and Resistant Avoidance Risk} identified how employees treated themselves as unlikely targets or assumed others would manage security, which reduced vigilance and non-engagement. Participants saw strict controls as unnecessary, accepting low compliance and silent avoidance as resistance behaviour.  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Individual Assumptions May Risk \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Individual Assumptions May Risk or Undermine Organisational Cybersecurity Readiness'}  
\\label{tab:6.5}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Individual Assumptions May Risk or Undermine Organisational Cybersecurity Readiness & Individual Assumption and Resistant Avoidance Risk & \`\`So, I know it's a little, like for me some days it feels 'overkill'...'' (P2-003) \\newline \`\`I assume most of the organisational people they are mature enough... so definitely assumptions, they impact a lot.'' (P2-006) \\newline \`\`Everybody has their own internal beliefs. If somebody is reluctant in change, so definitely they will try to resist as much as they can.'' (P2-006) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

 

\\paragraph{\\textbf{Code: Individuals Feel There Is Always a Gap Between Organisational Policy Implementation and Communication\\\\}}  
   
This code captured perceived disconnects between policy changes and practical communication, raising doubt and low commitment. Participants highlighted weak feedback, limited consultation, and unclear reporting. Leaders were dissatisfied that policies were imposed unilaterally by authority (IT department) without input on organisational realities, perpetuating a communication loop failure. Table\~\\ref{tab:6.6} presented sample quotes showing the code and patterns.

This code included two subcode properties that enhanced interpretive alignment:

\\begin{itemize}  
    \\item The\\textbf{ Lack of Communication and Feedback} captured sudden, unannounced policy changes that left employees uncertain about the rationale and reporting. Participants felt absent feedback channels and neglected end-user input during design or before implementation.  
    \\item The\\textbf{ Unsatisfied Leader} property described leaders' frustration with the policy, which exhausted motivation and security practices for team development. Dissatisfaction was often unspoken but shaped communication and reduced influence.\\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Individuals Feel There Is Always \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Individuals Feel There Is Always a Gap Between Organisational Policy Implementation and Communication'}  
\\label{tab:6.6}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Individuals Feel There Is Always a Gap Between Organisational Policy Implementation and Communication & Lack of Communication and Feedback & \`\`There is no communication... I was not familiar with it... I also discovered this just accidentally by clicking on something.'' (P2-005) \\newline \`\`These things are unilaterally done because they feel they have to do something. But then they forget to talk to the users at large.'' (P2-008) \\\\ \\cline{2-3}

& Unsatisfied Leader & \`\`I don't like it... I like admin privileges... I think we need to talk to IT... But I have not found a solution.'' (P2-007) \\newline \`\`And so, they gave me a computer, which has just turned into a paperweight on my desk. I don't use it because I can't. Like I get one tiny, update... I have to call IT \[system authority\] and say can you install an update for me? It's ridiculous.'' (P2-004) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

\\subsubsection{Theme 3 \- Discussion:}  
\\label{sec:DP2T3}

Theme 3 (P2-T3) is significant because it revealed how cybersecurity resistance was not always manifest or confrontational but rooted in everyday assumptions. Participants reframed it as unnecessary, technical, inconvenient, or someone else's responsibility. These underlying assumptions formed self-reinforcing loops that quietly weakened readiness. This is crucial because organisational security culture depends on shared interpretations of relevance and responsibility. 

Schein’s concept of underlying assumptions provided the primary interpretive lens, as these beliefs silently guided behaviour and defined what participants viewed as usual practice \\citep{Schein2017, Venkat2020}. Participants reported that some managers questioned policy relevance, avoided enforcement, or expressed dissatisfaction with cybersecurity procedures. This finding supported \\citet{alshaikh2020} argument that leadership modelling directly shaped security culture, but extended it by showing how behavioural intention actively sustained resistance.

\\paragraph{\\textbf{Individual Assumptions May Risk or Undermine Organisational Cybersecurity Readiness:\\\\}}  
Participants usually interpreted cybersecurity requirements through individual judgments about relevance, necessity, and responsibility \\citep{Sutton2025}. These assumptions guided behaviour quietly, influencing compliance decisions without deliberate intent. 

Several participants illustrate how such assumptions reduced vigilance. One described security requirement as excessive:

\\begin{quote}  
    \\small \\textit{So, I know it’s a little, like for me some days it feels overkill. (P2-003)}   
\\end{quote}

This perception reduced vigilance necessity and safety behaviour. Assumptions about others’ competence further reduced engagement. One participant explained:

\\begin{quote}  
    \\small \\textit{I assume most of the organisational people… they are reading it \[Policy\]… probably… some people they are not aware. (P2-006)}  
\\end{quote}

Time pressure reinforced avoidance; participants deprioritised cybersecurity, viewing risks as distant. Several participants (P2-002, P2-006, P2-007) reflected on this. P2-006 stated:

\\begin{quote}  
    \\small \\textit{Everybody has their own internal beliefs. If someone is reluctant to change, then they will try to resist as much as they can. (P2-006)}  
\\end{quote}

As \\citet{Balozian2017} argued that when inaccurate assumptions remained unchallenged, they gradually shaped the shared interpretations and weakened compliance norms. The findings here confirmed that assumption-driven reasoning encountered a sudden level of resistance without explicit opposition.

\\paragraph{\\textbf{Individuals Feel There Is Always a Gap Between Organisational Policy Implementation and Communication:\\\\}}  
This showed how policy-communication disconnected reinforced hesitation. The Lack of a clear message and Feedback code captured frustration with new implementations. Participants described discovering policy changes accidentally. One stated:

\\begin{quote}  
    \\small \\textit{There is no communication... I was not familiar with it... I also discovered this just accidentally by clicking on something. (P2-005)}  
\\end{quote}

This reflects reactive awareness rather than proactive engagement. Another participant noted the absence of interaction and consultation:

\\begin{quote}  
    \\small \\textit{The IT don’t ask us to provide feedback on that... They never asked us about this \[impact on our work\]. (P2-005)} \\\\  
    \\small \\textit{These things are unilaterally done because they feel they have to do something. But then they forget to talk to the users at large. (P2-008)}  
\\end{quote}

Participants showed that imposed policies lost collaborative legitimacy. 

Multiple participants (P2-003, P2-004, P2-007) also mentioned how leaders’ quiet dissatisfaction with organisational security policy faded their capacity to motivate others. Leaders admitted:

\\begin{quote}  
    \\small \\textit{Yeah. So, as much as I say, those things are annoying. I wouldn’t say that to my team. (P2-003)} \\\\  
    \\small \\textit{I don’t like it... I like admin privileges... I think we need to talk to IT... But I have not found a solution. (P2-007)} \\\\  
    \\small \\textit{And so, they gave me a computer, which has just turned into a paperweight on my desk. I don’t use it because I can’t. Like I get one tiny, update... I have to call IT \[system authority\] and say can you install an update for me? It’s ridiculous. (P2-004)}  
\\end{quote}

This showed recursive resistance loops from assumptions, communication gaps, and leadership hesitation. This gap quietly undermined readiness. HEIs must break them to embed security culturally beyond compliance.

Finally, Theme P2-T3 both confirmed and enhanced prior research on cybersecurity resistance and compliance. It confirmed that individual assumptions, rationalisations, and communication gaps were established barriers to security compliance \\citep{alshaikh2020, Herath2009, Ifinedo2012, Siponen2014}. It enhanced \\citet{Balozian2017} by showing that assumption-driven security profiles were not static. Those assumptions cyclically interacted with leadership hesitation and policy-communication failures, sustaining resistance loops. This theme extended \\citet{Georgiadou2022} by revealing a dynamic recursive process undermining organisational readiness, absent from their assessment model; it provided HEI-specific qualitative evidence.

\\subsection\[Theme 4 \- Experiential Trust Threshold and Disengagement\]{Theme 4 \- Experiential Trust Threshold and Disengagement in Incident Reporting}  
\\label{sec:P2T4}  
Theme 4 (P2-T4) showed that incident reporting depended on an experiential trust threshold, not only on formal procedures. Participants did not escalate security concerns based on policy instructions. Instead, they considered perceived consequences for job security, reputation, and possible authority frustration against their trust in the reporting contact. Participants reported uncertainty about reporting pathways and anticipated outcomes, which reduced timely escalation. 

Figure \\ref{fig:6.6} shows the structure of Theme 4 (P2-T4) codes. It summarised code emergence from Table \\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix \\ref{appendix:E}.\\\\

 

 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 4 (P2-T4) Code Structure\]{%  
    \\textbf{Figure 6.6}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 4 (P2-T4) Code Structure.}  
    }  
    \\label{fig:6.6}  
    
    % \\addcontentsline{lof}{figure}{6.6 \\hspace{0.18cm} Visual Summary of Theme 4 (P2-T4) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures/c6/6.5\_P2T4.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

This theme (P2-T4) consists of one code that clarified how trust, knowledge, and experience shaped incident reporting behaviour in practice. 

\\paragraph{\\textbf{Code: Individual Incident Reporting Depends on Trust\\\\}}  
This code referred to reporting occurring only when the employee believed the process paths and expected visible support. Underuse stemmed from unclear channels and absent trust, leading to silence or informal workarounds. Uncertainty was masked by assumption-based confidence among participants. Issues were hesitant to be raised, and leaders were distrusted by team members. Table\~\\ref{tab:6.7} presents sample quotes representing the code and patterns.

This code contained two subcodes, which strengthened the code’s interpretive alignment:

\\begin{itemize}  
    \\item The\\textbf{ Impact of Knowledge and Experience} property showed limited awareness of reporting channels. Rare leader discussions or uncertainty left employees unwilling to raise concerns. This created a reporting vacuum, hiding issues.  
    \\item The\\textbf{ Experiential Learner} revealed how participants learned through trial and error. Participant response patterns showed repeated exposure to organisational simulated phishing emails or policy changes shaped reporting confidence and vigilance.\\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Individual Incident Reporting \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Individual Incident Reporting Depends on Trust'}  
\\label{tab:6.7}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Individual Incident Reporting Depends on Trust & Impact of Knowledge and Experience & \`\`There must be a formal process or a procedure... otherwise it will depend on somebody's personal knowledge. It is not reinforced. It is not consistently conveyed to the employees.'' (P2-006) \\\\ \\cline{2-3}

& Experiential Learner & \`\`Some people just click on it intentionally just for fun because we can tell it's wrong... People still click on it just for the fun of it... they need to trust that you \[employees\] are responsible.'' (P2-005) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 4 \- Discussion:}  
\\label{sec:DP2T4}

Theme 4 (P2-T4) is significant because it demonstrates that incident reporting was not activated by policy awareness alone, but by an experiential trust threshold.   
Participants judged escalation by experience, trust, and expected response; some waited for self-resolution, others consulted colleagues first \\citep{ulven2021}. This is crucial because cybersecurity governance depends on the timely disclosure of incidents. These behaviours reflected uncertainty about consequences (for example, fear of job loss, frustration) rather than negligence \\citep{Tryfonas2015}. Similar dynamics were noted by \\citet{Cains2022}, who showed that uncertainty influenced risk judgment outcomes. 

Participants relied on personal interpretations of incidents, delaying or avoiding reports \\citep{Balozian2017}. Hesitation grew with unclear outcomes, fearing scrutiny over support \\citep{Patterson2023}. The findings extended this literature by evidencing how knowledge gaps and lived experience jointly shaped escalation decisions within higher education.

\\paragraph{\\textbf{Individual Incident Reporting Depends on Trust:\\\\}}  
Participants indicated that incident reporting relied more on trust, visibility, and lived experience. Leaders often assumed reporting would occur, but were not informed:

\\begin{quote}  
    \\small \\textit{I assume so, but I don’t know. It hasn’t come up. Maybe there have been incidents, but they haven’t told me. (P2-001)}  
\\end{quote}

Assumed confidence creates uncertainty. Team members distrusted managers or hesitated to discuss issues. Others (P2-007, P2-008) noted reporting system visibility gaps. P2-007 stated:

\\begin{quote}  
    \\small \\textit{No, not that I know. For security and emergencies, yes, they’re listed, but for cybersecurity, no, I don’t think so. We have an email to report to... but I don’t think there’s any display as such that indicates that. It may exist, but I’ve never really paid attention to it. (P2-007)}  
\\end{quote}

This quotation illustrated procedural fragility. Unclear pathways increased hesitation. Participants acknowledged responsibility but lacked pathway knowledge; P2-006 reflected:

\\begin{quote}  
    \\small \\textit{If there is an incident, everybody should be able to know where they have to report it. But I think this needs to be communicated. Again, I don’t see, even frankly speaking, if you ask me, where I will report it, I’m not sure. I would try to find out. This information needs to be communicated effectively. (P2-006)}  
\\end{quote}

When leaders could not articulate escalation pathways, employees inferred low priority. Reporting became conditional on personal comfort, not institutional expectation. 

Participants (P2-002, P2-004, P2-005) described mindsets where confidence grew through lived encounters and simulations. They valued prior experience and tests; one explained:

\\begin{quote}  
    \\small \\textit{As humans, we learn from past experience... occasionally you’ll be sent an e-mail which looks too fake... they are wanting you to report it. They’re not wanting you to click that link, so they are testing us \[phishing simulation\]. (P2-002)}   
\\end{quote}

These participants showed experiential reinforcement boosted awareness despite knowledge gaps that reduced confidence. Reporting ultimately depended on experiential trust and clarity.

Finally, Theme 4 (P2-T4) both confirmed and enhanced prior research on incident reporting behaviour. It confirmed that under-reporting stemmed from unclear pathways, trust deficits, and hesitation about consequences \\citep{Patterson2023, ulven2021}. It confirmed that assumption-driven reasoning shaped employees' escalation decisions without deliberate intent \\citep{Balozian2017}. However, this theme enhanced existing literature by introducing experiential trust as a sequential precondition for reporting activation. Prior studies identified trust as a cultural factor, but did not specify how lived experience and simulation exposure built reporting confidence over time. This theme provided HEI-specific qualitative evidence of how knowledge gaps and experiential learning jointly shaped escalation decisions.

 

\\subsection{Theme 5 \- End-User Behavioural Drift and Compliance Fatigue}  
\\label{sec:P2T5}  
Theme 5 (P2-T5) described how repeated limitations, unclear policy justifications, and work pressure caused gradual behavioural drift and compliance fatigue. Participants shifted from engagement to minimal compliance with frustration. Behavioural drift increased the gap between policy and practice due to mental overload, leading to quiet disengagement.

Figure \\ref{fig:6.7} shows the structure of Theme 5 (P2-T5) codes. It summarised code emergence from Table \\ref{tab:6.1}.  Supporting code-subcode extra quotations appear in Appendix \\ref{appendix:E}.\\\\

 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 5 (P2-T5) Code Structure\]{%  
    \\textbf{Figure 6.7}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 5 (P2-T5) Code Structure}  
    }  
    \\label{fig:6.7}  
    
    % \\addcontentsline{lof}{figure}{6.7 \\hspace{0.18cm} Visual Summary of Theme 5 (P2-T5) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.6\_P2T5.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

This Theme (P2-T5) consists of one code that clarified how accumulated fatigue translated into disengagement across daily cybersecurity practices.  

\\paragraph{\\textbf{Code: Behavioural Fatigue and Disengagement\\\\}}  
This code stated to collective mental and emotional strain that reduced individual attention, motivation, and willingness to engage with cybersecurity behaviour actions. Participants reported confusion, irritation, overload, and accepted shortcuts, which together reduced cybersecurity readiness. Table \\ref{tab:6.8} presents sample interview quotations representing the code and visible patterns.

This code contained four subcodes, which strengthened clarity and alignment with the theme:  
\\begin{itemize}  
    \\item The \\textbf{End-user Ignorance} property captured knowledge gaps and limited conceptual understanding of security and data protection. Participants associated it with risk-taking and error tolerance under pressure, especially with fragmented guidance.  
    \\item The\\textbf{ Individual vs Teamwork Dynamics} presented behavioural differences between solo and group work. Participants indicated that collaboration increased checking, permissions discipline, and shared responsibility, while solo work increased reliance on personal judgment and occasional shortcuts.  
    \\item The\\textbf{ Frustration with Security} property showed dissatisfaction and demotivation caused by authoritative limitations, restricted user access, and unclear new data classification policy implementation in routine work. \\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Behavioural Fatigue \]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Behavioural Fatigue and Disengagement'}  
\\label{tab:6.8}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Behavioural Fatigue and Disengagement & End-user Ignorance & \`\`I think the organisation is pretty averse to adopting technology… increasingly, I am as well because I'm too busy to change anything.'' (P2-001) \\newline \`\`People do not leave their comfort zone... As long as they are not feeling comfortable, they will resist this \[new implementation\].'' (P2-007) \\\\ \\cline{2-3}

& Individual vs Teamwork Dynamics & \`\`Individualistic versus teamwork… when you are individual… you might ignore it \[privacy/security\]… but when you're working in a team… collective wisdom… helps a lot.'' (P2-006) \\\\ \\cline{2-3}

& Frustration with Security & \`\`It is annoying. You know it is wasting our time... every e-mail, every document, everything the \[organisation\] introduced. Time... this is wasting our time.'' (P2-007) \\newline \`\`Engineering staff who do research will struggle... we spent plenty of money on this machine... restricted our access... not helping them, the staff to do research.'' (P2-005) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

\\subsubsection{Theme 5 \- Discussion:}  
\\label{sec:DP2T5}

Cybersecurity demands in HEIs have grown, raising individuals’ mental and procedural load. Participants juggled digital systems with teaching, research, and administration. Sustained organisational readiness depends on consistent attention which is significant. Theme P2-T5 captured this fatigue-driven disengagement, aligning with prior research on security fatigue while revealing higher education-specific dynamics \\citep{Ifinedo2012, Kannelonning2023}.

Behavioural drift progressed gradually as overload, poor response, and invisible consequence dominated motivation, standardising shortcuts and restraint. This gradual disengagement echoed technostress research in academic environments, where sustained mental strain undermined consistent security behaviour \\citep{Mangundu2023}. Participants described repeated authentication, classification, policy changes, and time-consuming procedures that reduced attention and encouraged minimal compliance, reflecting compliance fatigue \\citep{Bhana2023}.

\\paragraph{\\textbf{Behavioural Fatigue and Disengagement:\\\\}}  
Participants often relied on surface-level interpretations of protection. Multiple participants (P2-002, P2-006) directly admitted this. One participant stated:

\\begin{quote}  
    \\small \\textit{A common end user doesn’t understand what is a cybersecurity policy, what is confidentiality, integrity, availability, DDoS and so many things. (P2-006)}  
\\end{quote}

Limited conceptual literacy increased dependence on habit and guesswork. Some participants (P2-004, P2-006) described behavioural variation between solo and collaborative environments. P2-006 observed:

\\begin{quote}  
    \\small \\textit{Individualistic versus teamwork… when you are individual… you might ignore it \[Privacy/Security\] … but when you’re working in a team… collective wisdom… helps a lot. (P2-006)}  
\\end{quote}

Collective visibility strengthened accountability, whereas solitary work reduced peer monitoring and increased shortcuts. 

The participant explained emotional strain and irritation caused by frequent email notifications and unclear implementation. P2-007 expressed:

\\begin{quote}  
    \\small \\textit{It is annoying. You know it is wasting our time... every e-mail, every document, everything the \[organisation\] introduced. Time... this is wasting our time \[notification email\]. (P2-007)}  
\\end{quote}

Frustration also intersected with resistance to constant change. Multiple participant (P2-001, P2-004, P2-007) reflected on this. One Shared :

\\begin{quote}  
    \\small \\textit{People do not leave their comfort zone... As long as they are not feeling comfortable, they will resist this \[new implementation\]. (P2-007)}  
\\end{quote}

These quotations showed behavioural fatigue emerging through confusion, overload, irritation, and weak reinforcement, not disobedience. Disengagement grew quietly as security tasks became mentally burdensome and disconnected from work. This supported Theme P2-T5, showing cybersecurity readiness declined through gradual behavioural drift.

Finally, Theme 5 (P2-T5) both confirmed and enhanced prior research on cybersecurity fatigue and behavioural disengagement. It confirmed that cybersecurity fatigue impacted to burnout, diminished productivity, and disengagement across organisational settings \\citep{alshaikh2020, Mizrak2025}. It confirmed that repeated warnings and unclear policies drove compliance fatigue among end users \\citep{Bada2019, Ifinedo2012}. However, this theme enhanced \\citet{Mizrak2025} by providing qualitative HEI-specific evidence of fatigue mechanisms unavailable through their quantitative approach. It further introduced a sequential drift progression, from end-user ignorance through frustration to disengagement, not previously documented as a structured pattern. Additionally, solo versus teamwork dynamics as a fatigue moderator represented a new empirical contribution absent from prior behaviour assessments \\citep{Kannelonning2023}.

 

\\subsection{Theme 6 \- Cultural Miscalibration in Cyber Risk Perception}  
\\label{sec:P2T6}

Theme 6 (P2-T6) revealed cyber risk perception filtered through academic cultural assumptions. Participants judged risks low due to absent knowledge about incidents, lowering urgency and accountability. Cybersecurity appeared secondary to academic identity, misaligning formal expectations with cultural behaviour reality. Deep assumptions like silence equals security distorted individual threat responses. Figure \\ref{fig:6.8} provides a visual representation of Theme 6 code structure and summarises the code emergence presented in Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.\\\\  
   
 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 6 (P2-T6) Code Structure\]{%  
    \\textbf{Figure 6.8}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 6 (P2-T6) Code Structure.}  
    }  
    \\label{fig:6.8}  
    
    % \\addcontentsline{lof}{figure}{6.8 \\hspace{0.18cm} Visual Summary of Theme 6 (P2-T6) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.7\_P2T6.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
   
 

This theme (P2-T6) consisted of one code that explained how deep-rooted misperceptions shaped staff cyber risk judgement. 

\\paragraph{\\textbf{Code: Cyber Risks Due to Deep-Rooted Cultural Misperceptions\\\\}}  
   
This code captured employees interpreting cyber risk through entrenched cultural beliefs and routines, skipping formal appraisal. Participants viewed an absent breach incident as safety proof; unreported issues implied correct practice reduced learning necessity. Routine training created false coverage confidence, while organisational focus stayed narrow on phishing despite doubtful policy information. Table\~\\ref{tab:6.9} presented sample interview quotes representing the code.

It is refined by two supporting subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Organisational Cybersecurity Insufficient Practices} property captured perceptions of inadequate, inconsistently enforced, or poorly explained practices. A culture of absent incidents reinforced false success assumptions.   
    \\item The\\textbf{ Lack of Seriousness Toward Cybersecurity} identified reduced urgency and weak perceived consequences, where employees framed breaches as unlikely, manageable, or educational. Some clicked phishing tests for fun, ignoring real duties.\\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Cyber risks due to deep-rooted\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Cyber risks due to deep-rooted cultural misperceptions'}  
\\label{tab:6.9}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Cyber risks due to deep-rooted cultural misperceptions & Organisational Cybersecurity Insufficient Practices & \`\`Assessment process for academics... I suppose if something went horribly wrong... the assumption is if I haven't heard anything, you must be doing it correctly... then I guess it would come \[to light\].'' (P2-001) \\newline \`\`Honestly, I'm struggling to understand what the point of the \[document classification\] labelling \[new policy\] is... people are just going to pick public all the time or official... they're not going to think about it \[privacy\].'' (P2-004) \\\\ \\cline{2-3}

& Lack of Seriousness Toward Cybersecurity & \`\`I think most of us are pretty slack actually... we never hear of any breaches. So, I think most of us probably think that'll happen to somebody else or some other organisation.'' (P2-002) \\newline \`\`I don't think that people understand that even with sensitive information there is Freedom of Information Act... if you're not careful and you don't know what those terms mean, it's a lot more harder.'' (P2-008) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 6 \- Discussion:}  
\\label{sec:DP2T6}

Theme 6 (P2-T6) showed cyber risk was underestimated through culturally embedded assumptions. Participants viewed silence, routine, and past stability as safety evidence, weakening vigilance amid formal policies. These assumptions distorted risk perception, producing a misalignment between formal cybersecurity expectations and lived behaviour \\citep{Balozian2017}. A mismatch existed between perceived and actual threat pathways. 

This theme showed how common cultural assumptions diminished everyday cybersecurity maturity in the organisation \\citep{Adamu2025, Jeong2022}. Deep-rooted misperceptions created a false sense of security, producing complacency where threats emerged only after tragic failure.

\\paragraph{\\textbf{Cyber Risks Due to Deep-Rooted Cultural Misperceptions:\\\\}}  
When reflecting on everyday cybersecurity exposure, participants consistently relied on what they had not seen or heard to judge whether risk existed. While discussing how employees assessed whether security practices were effective, Participants (P2-001, P2-002) explained that silence itself became reassurance. One Stated:

\\begin{quote}  
    \\small \\textit{I think most of us are pretty slack actually... we never hear of any breaches. So, I think most of us probably think that’ll happen to somebody else. (P2-002)}  
\\end{quote}

Participants reflected on how silence and limited visibility justify the absence of improvement. Other participants perceived organisational practices as restricted and poorly explained, with others fixating solely on phishing while unaware of broader policy obligations:

\\begin{quote}  
    \\small \\textit{If we get an attack from outside... an e-mail with a sort of risky link... This is what they focus on. We're not aware of policies or anything beyond this. Just don’t click the wrong link. (P2-005)}  
\\end{quote}

When asked about new security and privacy system implementation (data classification):

\\begin{quote}  
    \\small \\textit{Honestly, I’m struggling to understand what the point of the \[document classification\] labelling \[new policy\] is... people are just going to pick public all the time or official... they’re not going to think about it \[privacy\]. (P2-004)}  
\\end{quote}

Employees took the path of least resistance, making safeguards ineffective. One participant noted that limited legal awareness created vulnerabilities:

\\begin{quote}  
    \\small \\textit{I don't think that people understand that even with sensitive information, there is Freedom of Information Act... if you're not careful and you don't know what those terms mean, it's a lot more harder. (P2-008)}  
\\end{quote}

Another participant argued that cultural disengagement made enforcement necessary, as information alone failed to shift risk perception \\citep{Cronje2024}:

\\begin{quote}  
    \\small \\textit{To be honest, I feel like cybersecurity is something best enforced. You have to make really tough rules... people are not interested in looking for cybersecurity information, and those who are not interested won’t pay attention no matter how much you train them. (P2-004)}  
\\end{quote}

Participants advocated enforcement to bridge perceived and actual risk gaps. This indicated cyber risk downplayed through silence, routine, workload, and assumed competence. Risk seemed distant or managed by others unless disruptive. This supported Theme (P2-T6), collective assumptions distorted perception, weakening readiness.

Finally, Theme 6 (P2-T6) both confirmed and enhanced prior research on cultural assumptions and cyber risk perception. It confirmed that cultural assumptions silently shaped employee behaviour and distorted formal cybersecurity expectations \\citep{Adamu2025, Balozian2017}. It confirmed that HEI openness culture created specific compliance challenges distinct from other organisational settings \\citep{Cronje2024}. However, this theme enhanced existing literature by identifying specific cultural logic not previously documented. The 'silence equals safety' assumption, where absent incidents were interpreted as proof of security, was a new empirical finding. Academic professional identity overriding cybersecurity obligations, and phishing simulations treated as entertainment, were culturally embedded processes unique to the higher education environment.

 

\\subsection{Theme 7 \- Security Culture Embarrassment Barrier}  
\\label{sec:P2T7}

Theme 7 (P2-T7) revealed social discomfort preventing cybersecurity readiness beyond technical issues. Employees hesitated to report incidents because they feared it would signal weakness, training as a social penalty, or incompetence to teams or management. This suppressed knowledge, reduced learning, and weakened awareness. Fear of judgment over reportable errors amplified the barrier.

Figure \\ref{fig:6.9} shows the structure of Theme (P2-T7) codes. It summarised code emergence from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.\\\\

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 7 (P2-T7) Code Structure\]{%  
    \\textbf{Figure 6.9}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 7 (P2-T7) Code Structure.}  
    }  
    \\label{fig:6.9}  
    
    % \\addcontentsline{lof}{figure}{6.9 \\hspace{0.18cm} Visual Summary of Theme 7 (P2-T7) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.8\_P2T7.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

   
 

Theme 7 (P2-T7) consisted of one code. It explained how embarrassment and fear shaped incident silence and redirected reporting away from leaders.

\\paragraph{\\textbf{Code: Cultural Hesitation to Report Incidents Due to Fear or Embarrassment\\\\}}  
This code captured how individuals avoided reporting cybersecurity issues, as disclosure felt socially risky. Participants preferred informal peer queries, quiet self-management, or impersonal channels; these reduced embarrassment risk. Reporting depended on mental safety, social penalty (extra training), and leader approachability to ease fear, not just policy availability. Table\~\\ref{tab:6.10} presents sample interview quotations representing the code and visible patterns.

This code contained two supporting subcode properties, which enhanced the clarity and alignment of the code:  
\\begin{itemize}  
    \\item The\\textbf{ Leaders Believe} properties indicated a recurring pattern was the academic pedigree bias. Leaders believed well-informed, educated academics handled cybersecurity independently.   
    \\item The\\textbf{ Lack of Leadership Initiative} property presented that leaders took little action to build an incident reporting culture.\\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Cultural Hesitation to Report\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Cultural Hesitation to Report Incidents Due to Fear or Embarrassment'}  
\\label{tab:6.10}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Cultural Hesitation to Report Incidents Due to Fear or Embarrassment & Leaders Believe & \`\`I've never experienced any such thing where people have reported it to me... I believe they have to create a ticket for IT... they never shared for example...'' (P2-006) \\newline \`\`I don't really speak to the staff who report to me because I expect that they already know this stuff.'' (P2-004) \\\\ \\cline{2-3}

& Lack of Leadership Initiative & \`\`I honestly don't think it really comes on most people's radar. I don't think I've never I can't recall ever being in a meeting where anyone has really mentioned it strongly.'' (P2-002) \\newline \`\`I think I would just direct them to IT services. Yeah, there's not much I can do about it... I just refer them to IT.'' (P2-001) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

\\subsubsection{Theme 7 \- Discussion:}  
\\label{sec:DP2T7}

Cybersecurity readiness was constrained by social discomfort instead of technical limitations \\citep{Georgiadou2022}. Participants described hesitation driven by embarrassment, fear of appearing incompetent, or uncertainty about social boundaries \\citep{Patterson2024}. Cybersecurity readiness depends on timely reporting and collective learning. Leaders trusted educated teams ‘already knew’ practices, discouraging corrective conversations and peer intervention \\citep{Schein2017}. Reporting felt risky, exposing mistakes threatened professional identity, and creating incident silence through shame and uncertainty \\citep{Patterson2023}. 

\\paragraph{\\textbf{Cultural Hesitation to Report Incidents Due to Fear or Embarrassment:\\\\}}  
Silence functioned as a protective strategy for participants. Leaders acknowledged employee avoided formal channels, preferring informal reassurance; one reflected:

\\begin{quote}  
    \\small \\textit{If they had someone a quick question, they’re \[employee\] probably going to ask someone they can talk to in person rather than me \[leader\]... I’m not just going to jump down their throat if they tell me something’s gone wrong. (P2-001)}  
\\end{quote}

Participants prioritised emotional safety over procedural clarity. Reporting depends on comfort; embarrassment grew from visible consequences. When asked about uncertain decisions, P2-007 framed action as an internal ethical judgement:

\\begin{quote}  
    \\small \\textit{You have to make a decision from your mind... not necessarily following social norms or rules, but what you think is fair. (P2-007)}  
\\end{quote}

Reporting errors or failing phishing simulations triggered mandatory retraining, seen as a social penalty. Others described enforced enrolment evoking embarrassment and a fearful mindset. 

\\begin{quote}  
    \\small \\textit{We’re not giving advice on how to do cybersecurity. We just throw it in with all the training. (P2-001)} \\\\  
    \\small \\textit{If someone accidentally clicks on a phishing e-mail... they do have to go back and do some mandatory training. (P2-001)}  
\\end{quote}

Some leaders presumed educated staff understood cybersecurity expectations, avoiding open discussion. P2-004 stated:

\\begin{quote}  
    \\small \\textit{I don’t really speak to the staff who report to me because I expect that they already know this stuff. (P2-004)}  
\\end{quote}

Another participant (P2-001, P2-006) described the leader’s response to incidents as purely transferred to others. P2-001 Shared: 

\\begin{quote}  
    \\small \\textit{I think I would just direct them to IT services. Yeah, there’s not much I can do about it... I just refer them to IT. (P2-001)}  
\\end{quote}

This revealed a lack of leadership initiative that intensified hesitation. Cultural discomfort, leadership gaps, and social risks caused hesitation, not ignorance. Theme 7 (P2-T7) hid incidents through cultural discomfort, weakening readiness.

Finally, Theme 7 (P2-T7) confirmed and significantly extended prior research on cybersecurity incident reporting barriers. It confirmed that organisations widely missed opportunities to learn from incidents due to social and cultural barriers \\citep{Patterson2023}. It confirmed that creating openness to hear about incidents was critical, but remained largely absent in practice \\citep{Patterson2024}. However, this theme introduced three genuinely new findings absent from both foundational works. Embarrassment functioned as an institutionalised cultural barrier, not merely individual discomfort, creating a recursive silence cycle. Academic pedigree bias, where leaders assumed educated staff independently understood cybersecurity, was a leadership-reinforced mechanism amplifying that silence. Mandatory retraining perceived as social penalty actively discouraged future reporting, which was not previously identified in cybersecurity literature.

\\subsection{Theme 8 \- Leadership Lag in Onboarding Cybersecurity Policy}  
\\label{sec:P2T8}

Theme 8 (P2-T8) showed that leadership failed to embed cybersecurity norms during onboarding. Leaders delegated onboarding to modules, remaining detached and unaware of new joiners' knowledge gaps. New staff learned policies via generic modules without leader input. This detachment made cybersecurity seem like a mere compliance task, not establishing a core value. 

Figure \\ref{fig:6.10} shows Theme 8 (P2-T8) code structure and summarised emergence from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.\\\\

   
 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 8 (P2-T8) Code Structure\]{%  
    \\textbf{Figure 6.10}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 8 (P2-T8) Code Structure.}  
    }  
    \\label{fig:6.10}  
    
    % \\addcontentsline{lof}{figure}{6.10 \\hspace{0.18cm} Visual Summary of Theme 8 (P2-T8) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.9\_P2T8.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
   
 

This theme 8 consisted of one code. It explained leaders' distance from onboarding, relying on unverified assumptions about induction coverage, emphasis and impact. 

\\paragraph{\\textbf{Code: Leadership Lag in Onboarding Cybersecurity Policy Awareness\\\\}}  
This code captured leadership disengagement from communicating cybersecurity policy to new joiners. Leaders failed to ensure understanding of organisational practices and cultural sharing to build team strength. Leaders expressed uncertainty about new staff onboarding content. They expected instant knowledge, delegating to HR or IT without sharing. This created major gaps. Table\~\\ref{tab:6.11} presents sample interview quotes representing the code.

This code was refined by one supporting subcodes property:   
\\begin{itemize}  
    \\item The\\textbf{ Gap Between Leaders and New Joiners} property captured the structural and communicative distance between leaders and new staff during onboarding. Leaders lacked training content knowledge, assumed modules sufficed, and offered no reinforcement.  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Leadership Lag in Onboarding\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Leadership Lag in Onboarding Cybersecurity Policy Awareness'}  
\\label{tab:6.11}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Leadership Lag in Onboarding Cybersecurity Policy Awareness & Gap Between Leaders and New Joiners & \`\`I know that there are some orientation sessions... when I put a research assistant on earlier last year. But I don't know the specifics of what was involved.'' (P2-001) \\newline \`\`New stuff how they are approaching I don't \[know\]. It depends on you know it. Strategic decision... probably they are doing this.'' (P2-007)) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 8 \- Discussion:}  
\\label{sec:DP2T8}

Theme 8 (P2-T8) is crucial because onboarding represents the first moment where organisational values become operationalised. When cybersecurity expectations are weakly embedded at entry, misalignment endures throughout employment. The findings showed that leaders assumed onboarding covered security adequately, yet they lacked clarity regarding policy, cultural practice, emphasis, or reinforcement. This gap mattered because early leadership examples shaped lasting behavioural norms. 

Organisational security readiness relies on guiding new employees through clear cybersecurity expectations. Prior research identified onboarding as a critical phase for embedding security behaviour and organised norms \\citep{Cheng2022, DaVeiga2010}. Participants assumed cybersecurity onboarding occurred via standard induction, but leaders couldn’t describe content or impact. 

\\paragraph{\\textbf{Leadership Lag in Onboarding Cybersecurity Policy Awareness:\\\\}}  
   
Leaders depended on administrative systems yet remained uncertain about communicated content:

\\begin{quote}  
    \\small \\textit{I know there are some orientation sessions... but I don’t know the specifics of what was involved. (P2-001)}  
\\end{quote}

Without knowing what a new team member learned, leaders could not target support, creating gaps from assumptions and later embarrassment fears. Several participants (P2-002, P2-006, P2-007) shared a similar pattern. P2-007 stated: 

\\begin{quote}  
    \\small \\textit{Now I don’t know that one... probably they are doing this, but how they are approaching it, I don’t know. It depends on strategic decisions. (P2-007)}  
\\end{quote}

Another participant echoed this assumption-driven culture directly:

\\begin{quote}  
    \\small \\textit{I’m not sure because ... orientation for new staff... they must be talking about this \[cybersecurity\], I hope. (P2-005)}  
\\end{quote}

This appeared from the code, identified onboarding as a missed opportunity for cultural embedding, where leadership action signalled that cybersecurity was secondary. 

Finally, Theme 8 (P2-T8) confirmed and considerably extended prior research on cybersecurity culture embedding and HEI governance. It confirmed that onboarding represented a critical phase for embedding cybersecurity behaviour and institutional norms \\citep{alshaikh2020, Cheng2022}. It confirmed that security culture components required active leadership reinforcement to be effective in practice \\citep{DaVeiga2020}. However, this theme introduced new findings not previously documented. Leadership detachment from onboarding was identified as a specific structural vulnerability; leaders were unaware of what new joiners had actually learned. Assumption-driven delegation, where leaders expected HR or IT to embed cybersecurity valued without personal involvement, created persistent knowledge gaps. Onboarding as the first missed opportunity for cultural embedding in HEIs represented a new contribution absent from all prior institutional cybersecurity frameworks.

 

\\subsection\[Theme 9 \- Strategic Weakness in Security Governance\]{Theme 9 \- Strategic Weakness in Security Governance in Academia}  
\\label{sec:P2T9}

Theme 9 (P2-T9) revealed structural governance weaknesses that undermined cybersecurity readiness in HEI. Participants described fragmented implementation, inconsistent follow-up, and unclear accountability across institutional layers. Although policies, modules, and drills existed, their execution did not consistently translate into confidence, trust, or behavioural integration. This systemic gap shifted to ineffective strategic coordination and weak governance coherence.  
   
Figure \\ref{fig:6.11} illustrates the code structure for Theme (P2-T9) and summarises code emergence from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.\\\\

 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 9 (P2-T9) Code Structure\]{%  
    \\textbf{Figure 6.11}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 9 (P2-T9) Code Structure.}  
    }  
    \\label{fig:6.11}  
    
    % \\addcontentsline{lof}{figure}{6.11 \\hspace{0.18cm} Visual Summary of Theme 9 (P2-T9) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.10\_P2T9.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
   
 

This theme consisted of one overarching code that captured perceptions of institutional cybersecurity efforts as lacking credibility, clarity, and sustained impact. 

\\paragraph{\\textbf{Code: Organisational Actions Are Not Effective Enough\\\\}}  
This code captured perceptions that formal cybersecurity governance, including modules, drills, policies, and channels, existed but failed operationally through inconsistent execution, weak reinforcement, poor control (such as phishing-like training links), old content, and poor workflow integration. Participants completed compulsory training without internalising it; reporting pathways stayed unclear, and leadership accountability remained thin. Table\~\\ref{tab:6.12} shows sample interview quotes representing the code.

This code contains three supporting subcode properties:   
\\begin{itemize}  
    \\item The Doubt Over Organisations' Ability\\textbf{} captured participants' uncertainty about institutional competence and credibility in cybersecurity. This arose from poor practices, training perceived as a hassle completed by clicking next, and weak enforcement that eroded trust.  
    \\item The\\textbf{ Poor Leadership in handling incidents} reflected uncertainty about leadership oversight, incident ownership, and escalation clarity.   
    \\item The\\textbf{ Frustration Over Reactions to Cybersecurity Drills and Exercises} property captured dissatisfaction with phishing simulations, repetitive training, and perceived time burdens. Failed drills triggered mandatory retraining, already viewed as boring and wasteful, creating a negative cycle where exercises appeared punitive rather than educational.\\\\  
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Organisational Actions Are Not\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Organisational Actions Are Not Effective Enough'}  
\\label{tab:6.12}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Organisational Actions Are Not Effective Enough & Doubt Over Organisations' Ability & \`\`I treat it as more of a five-minute hassle that you just got to go next, next, next... just wasting my time doing this bloody module for the fifth time and the content hasn't changed.'' (P2-002) \\newline \`\`The IT don't ask us to provide feedback on that... They never asked us about this \[impact on our work\].'' (P2-005) \\\\ \\cline{2-3}

& Poor Leadership in handling incidents & \`\`Even if you ask me, OK, where I will report it, I'm not sure. I have to try to find out... I don't see there is anything \[new\] similarly phishing attacks... they should be reinforced more.'' (P2-006) \\newline \`\`Not really, it's not something from a manager who roles in general, we're not giving (advice on cybersecurity or privacy)...'' (P2-001) \\\\ \\cline{2-3}

& Frustration Over Reactions to Cybersecurity Drills and Exercises & \`\`Video \[Training\] for half an hour… so boring… nobody checks…'' (P2-008) \\newline \`\`They sent emails saying, \`Here's the training, click the link.' I thought, I'm not clicking that... two weeks later, they said those were genuine. I thought it was interesting that their practice was so bad.'' (P2-001) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 9 \- Discussion:}  
\\label{sec:DP2T9}

 Theme 9 (P2-T9) is important because it shifts the analytical focus from individual behaviour to institutional design. Cybersecurity governance in higher education was experienced as structurally weak and unevenly enforced \\citep{lallie2025}. Participants described fragmented governance lacking strategic coordination. Other reported unclear ownership, inconsistent protocols, and limited follow-up. This theme matters because organisational readiness depends on credible coordination between policy, leadership, and daily practice \\citep{Cheng2022}. P2-T9 shifted focus from individual behaviour to institutional design and system execution. 

\\paragraph{\\textbf{Organisational Actions Are Not Effective Enough:\\\\}}  
   
Participants questioned institutional competence, described leadership detachment in incident handling, and expressed frustration with drills and repetitive exercises.

The doubt over organisations’ ability emerged through participants’ reflections on training quality and communication design. Participants explained:

\\begin{quote}  
    \\small \\textit{I treat it as more of a five-minute hassle that you just got to go next, next, next... just wasting my time doing this bloody module for the fifth time and the content hasn’t changed. (P2-002)} \\\\  
    \\small \\textit{There are a couple of small mandatory modules \[training\] related to cybersecurity awareness, but they are just once in a year or in induction. It’s not consistent, so people probably try to do it quickly and get rid of it, and then it’s not integrated into daily work life. (P2-006)}  
\\end{quote}

Flawed organisational security practices undermined staff confidence in governance structures. Training was completed, but not adopted, which weakened governance \\citep{Haney2020}. 

Participants described confusion from poorly coordinated training and simulation practices. Multiple participants acknowledged a similar pattern:

\\begin{quote}  
    \\small \\textit{They sent emails saying, ‘Here’s the cybersecurity training, click the link.’ I thought, I’m not clicking that. Two weeks later, they said those were genuine. I thought it was interesting that their practice was so bad. (P2-001)} \\\\  
    \\small \\textit{video \[Training\] for half an hour… so boring… nobody checks… (P2-008)}  
\\end{quote}

This experience reduced trust in institutional messaging and blurred distinctions between real threats and training exercises. Participants also described unclear incident responsibility and limited leadership ownership.

Several participants (P2-001, P2-003, P2-006) described the managerial distance from incident handling.

\\begin{quote}  
    \\small \\textit{Even if there is an incident, they’re not going to report it to me. They go straight to IT. (P2-006)} \\\\  
    \\small \\textit{I have never been told this is part of my responsibility, to promote the culture of cybersecurity. (P2-003)}  
\\end{quote}

Another participant noted that absent feedback on this or other issues, limited organisational strategy improvements.

\\begin{quote}  
    \\small \\textit{I don’t think… employees… will be aware of where they can provide feedback related to cybersecurity. (P2-006)}  
\\end{quote}

P2-006 also acknowledged the broader strategic lag:

\\begin{quote}  
    \\small \\textit{Cybersecurity is always emerging and evolving, so no organisation can really catch up with the pace of increasing cybersecurity threats. There is a need for continuous improvement. (P2-006)}  
\\end{quote}

This statement highlighted institutional limits in keeping pace with evolving threats. This showed governance strategic weaknesses appeared from poor execution, unclear leadership, absent feedback, and low training credibility. 

Finally, Theme 9 (P2-T9) confirmed and significantly extended prior research on cybersecurity governance in higher education. It confirmed that realistic research on HEI cybersecurity governance stayed scarce and underexplored \\citep{ulven2021}. Also, confirmed that tactical coordination between policy, leadership, and practice was critical for organisational cybersecurity readiness \\citep{Cheng2022}. Theme 9 similarly confirmed that formal organisational structures indirectly shaped security culture through InfoSec practices \\citep{Hassandoust2023}. However, this theme introduced several new governance failure approaches not previously documented. These patterns revealed systemic weaknesses beyond individual behaviour or policy design. Training dismissal, described as mindless clicking through unchanged modules, represented a new empirical pattern of governance credibility erosion. Drill confusion, where simulated phishing was mistaken for genuine threats, actively undermined institutional trust in governance messaging. Absent feedback channels and leader uncertainty about incident ownership revealed structural voids not captured in prior HEI governance frameworks.

 

\\subsection\[Theme 10 \- Leadership and Behavioural Dynamics Influencing\]{Theme 10 \- Leadership and Behavioural Dynamics Influencing Cybersecurity Culture}  
\\label{sec:P2T10}  
Theme 10 (P2-T10) demonstrated how leadership behaviours sustained cybersecurity culture after policy rollout. While previous themes identified structural and strategic gaps. Participants observed formal expectations through organisational training and controls, yet leaders reinforced them through relational motivation. Cybersecurity thus remained administratively secondary rather than culturally integrated.

Figure \\ref{fig:6.12} illustrates Theme (P2-T10) code structure and summarises emergence from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.

 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 10 (P2-T10) Code Structure\]{%  
    \\textbf{Figure 6.12}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 10 (P2-T10) Code Structure.}  
    }  
    \\label{fig:6.12}  
    
    % \\addcontentsline{lof}{figure}{6.12 \\hspace{0.18cm} Visual Summary of Theme 10 (P2-T10) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.11\_P2T10.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
   
  

This theme consisted of one overarching code that captured leaders' influence on cybersecurity culture through relationships, trust, behavioural modelling, and active promotion of norms.

\\paragraph{\\textbf{Code: Leadership and Behavioural Dynamics Influencing Cybersecurity Culture\\\\}}  
This code revealed leadership's central role in shaping cybersecurity culture through employer-employee relationship quality, limited visible policy enforcement, and weak motivation for best practices. Leaders determined psychological protection for communication and learning. Behavioural signals thus expanded or undermined organisational security posture. Table\~\\ref{tab:6.13} showed sample interview quotes representing the code.

This code comprised three interrelated subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Employer and Employee Relationship Affects Cybersecurity Culture} property explained how interpersonal trust deficits, absent psychological safety, and poor relational quality reduced staff willingness to disclose incidents or share cybersecurity responsibility.   
    \\item The\\textbf{ Lack of Promoting from Leaders for Cybersecurity Culture and Policy} highlighted leaders' minimal active promotion of cybersecurity norms beyond central training modules.   
    \\item The\\textbf{ Lack of Cultural Motivation for Cybersecurity Best Practices} highlighted weak cultural reinforcement that reduced motivation for sustained best practices despite general awareness. Cybersecurity is rarely linked to organisational values or discussion, delaying the transition from knowing to doing.  
\\end{itemize}

See Table\~\\ref{tab:6.13} for a sample of interview quotes that represent the training perspective code.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Leadership and Behavioural\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Leadership and Behavioural Dynamics Influencing Cybersecurity Culture'}  
\\label{tab:6.13}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Leadership and Behavioural Dynamics Influencing Cybersecurity Culture & Employer and Employee Relationship Affects & \`\`If there was not a feeling of trust between individuals... those who manage and those who are managed, then that would definitely impact that relationship... they wouldn't want to report.'' (P2-002) \\newline \`\`I think the relationship that you have with your team is so important... there have been times where people have felt really insecure in being able to voice their concerns.'' (P2-003) \\\\ \\cline{2-3}

& Lack of Promoting from Leaders for Cybersecurity Culture and Policy & \`\`Manager, of course should be a role model... I did use that as a learning experience \[sharing a personal incident\]... to say, well, how it's the first time ever I shouldn't have.'' (P2-002) \\\\ \\cline{2-3}

& Lack of Cultural Motivation for Cybersecurity Best Practices & \`\`Convince them based on your ideology that will not work. You need to understand the issue 1st... How can we provide a comfortable environment for that person.'' (P2-007) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

\\subsubsection{Theme 10 \- Discussion:}  
\\label{sec:DP2T10}

Theme 10 (P2-T10) is essential because it demonstrates that leaders influenced cybersecurity after policies were introduced and systems were operational. While Theme 8 (P2-T8) addressed leadership gaps during onboarding and Theme 9 (P2-T9) examined institutional governance weaknesses, Theme 10 (P2-T10) focused on how leadership behaviour shaped cybersecurity culture in practice. Leadership signals played a decisive role in shaping responsibility \\citep{DextrasGauthier2023, Kaptein2011}.

\\paragraph{\\textbf{Leadership and Behavioural Dynamics Influencing Cybersecurity Culture:\\\\}}  
Employer-employee relationships shaped cybersecurity culture across participant responses. Several participants agreed:

\\begin{quote}  
    \\small \\textit{If there was not a feeling of trust between individuals... those who manage and those who are managed, then that would definitely impact that relationship... they wouldn’t want to report. (P2-002)} \\\\  
    \\small \\textit{Yes, of course. Your relationship and stuff. This 100\\% impacts... if you have a good relation with people, then if they have an issue they can talk with you about it... but if there is bad listenership, this means avoid each other... everyone left their own problem without sharing. (P2-005)}  
\\end{quote}

Another participant stressed that team members must feel safe to raise concerns.

\\begin{quote}  
    \\small \\textit{I think the relationship that you have with your team is so important... there have been times where people have felt really insecure in being able to voice their concerns. (P2-003)}  
\\end{quote}

These showed that the reporting depended on psychological safety. Organisational culture, shaped by ethical climate and leader behaviour, influenced compliance attitudes.

\\begin{quote}  
    \\small \\textit{Convince them based on your ideology that will not work. You need to understand the issue 1st... How can we provide a comfortable environment for that person? (P2-007)}  
\\end{quote}

Participants framed cybersecurity as a personal obligation rather than a shared responsibility. P2-006 observed:

\\begin{quote}  
    \\small \\textit{We don’t really have any discussion related to this... because we are in academia, everybody is well informed... we just trust them. (P2-006)}  
\\end{quote}

Employee silence on cybersecurity issues increased when leaders neglected them in discussions and meetings. This showed clearly that cybersecurity culture relied on relational reinforcement, visible modelling, and consistent discussion. Cybersecurity readiness depended not only on structures or training, but on how leaders acted, exhibited, and prioritised cybersecurity in everyday interactions.

Finally, Theme 10 (P2-T10) confirmed and enhanced prior research on leadership behaviour and cybersecurity culture. It confirmed that emotionally rational leadership shaped team cybersecurity behaviour more effectively than technical proficiency alone \\citep{Burton2023}. Also, confirmed that leadership behaviours and culture jointly shaped employees' sense of psychological protection and shared responsibility \\citep{DextrasGauthier2023}. However, this theme introduced genuinely new HEI-specific findings not previously documented. Relational trust between leader and employee was identified as the primary enabler of incident reporting in academic settings. The passive promotion pattern, where leaders assumed academics already understood cybersecurity independently, represented a new cultural vulnerability specific to higher education. Cybersecurity was framed as a personal rather than a shared organisational obligation, a finding absent from prior leadership and culture frameworks.

\\subsection{Theme 11 \- Ignorance Towards Policy}  
\\label{sec:P2T11}

Theme 11 (P2-T11) demonstrated how abundant, generic policies failed to influence daily behaviour due to assumptions and a lack of interest in reading them. Participants treated them as routine compliance without comprehension or alignment. Ignorance reflected functional detachment; policies appeared irrelevant to academic workflows, exposing human vulnerabilities.

Figure \\ref{fig:6.13} illustrates Theme (P2-T11) code structure and summarises emergence from Table\~\\ref{tab:6.1}. Supporting code-subcode extra quotations appear in Appendix\~\\ref{appendix:E}.

 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Visual Summary of Theme 11 (P2-T11) Code Structure\]{%  
    \\textbf{Figure 6.13}\\\\\[1.2em\]  
    \\textit{Visual Summary of Theme 11 (P2-T11) Code Structure.}  
    }  
    \\label{fig:6.13}  
    
    % \\addcontentsline{lof}{figure}{6.13 \\hspace{0.18cm} Visual Summary of Theme 11 (P2-T11) Code Structure}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c6/6.12\_P2T11.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
   
 

This theme consists of one code that captured neglected policy awareness, common-sense reliance over policy judgement, and persistent confusion about data protection processes.

\\paragraph{\\textbf{Code: Ignorance Towards Policy\\\\}}  
This code identified policy ignorance developing from individual negligence, common-sense reliance over policy guidance, and confusion about data protection processes. Participants exhibited habitual detachment, mechanical training completion, and uncertainty on policy relevance to tasks. Table\~\\ref{fig:6.1} presents sample quotes representing the code and patterns.

It is refined by three supporting subcode properties:   
\\begin{itemize}  
    \\item The\\textbf{ Policy Awareness Negligence- Individual Level} captured routine neglect of policy engagement. Participants exhibited compliance bypass behaviour, viewing training as predictable, easy, and repetitive, which normalised disengagement from policy details.  
    \\item The\\textbf{ Relying on Common Sense Rather Than Policy} identified that employees treated security guidance as self-evident and favoured personal judgement, where participants relied on common sense for privacy decisions, often creating risks.  
    \\item The\\textbf{ Confusion About the Data Protection Policy} captured uncertainty about how the data protection policy operated, who managed it, and how data was stored, erase and shared.\\\\   
\\end{itemize}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{3.3cm} p{8cm}}

\\caption\[Sample Quotations Representing \`Ignorance Towards Policy'\]{%  
\\\\\[1.2em\]  
\\textit{Sample Quotations Representing \`Ignorance Towards Policy'}  
\\label{tab:6.14}  
}  
\\\\

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code} & \\textbf{Subcode Properties} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Ignorance Towards Policy & Policy Awareness Negligence- Individual Level & \`\`There would be policies; whether or not people read the policy is a different matter... there's probably thousands of policies... I treat it as more of a five-minute hassle.'' (P2-002) \\\\ \\cline{2-3}

& Relying on Common Sense Rather Than Policy & \`\`I would say a lot of people would think the basic training is common sense... because it's common sense, that's probably where people tend to ignore it... we're actually pretty slack.'' (P2-002) \\\\ \\cline{2-3}

& Confusion About the Data Protection Policy & \`\`Data protection policy is, I think, organised by the library... but I don't know how they are sharing the data... The \[Organisation\] is trying to protect data, but I do not really know how.'' (P2-007) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\subsubsection{Theme 11 \- Discussion:}  
\\label{sec:DP2T11}

   
Theme 11 (P2-T11) is crucial because it demonstrates that policy presence did not equate to policy influence. Prior research has consistently shown that limited policy understanding remains a persistent human vulnerability in cybersecurity compliance \\citep{Kannelonning2023, Siponen2014}. This gap is important because such behaviour matched findings where policy compliance declined amid routine, repetitive, work-disconnected training. Security awareness training must therefore connect security to all organisational role duties \\citep{Haney2020}. 

\\paragraph{\\textbf{Ignorance Towards Policy:\\\\}}  
One participant captured how repetitive training and unchanged questions led to individual policy negligence. Participants ignored and rushed the completion.

\\begin{quote}  
    \\small \\textit{They send us \[training\] every couple of months... And it is so straightforward that you can just skip to the assessment section at the end and click the really obvious answer to each question and your past... you’ve got to watch the video or whatever...others do the same thing as me. You set the video going, you mute it, you go and do something else for five minutes, and you come back. It really feels it's pushed so heavily that we don’t take it seriously anymore because. I've done this 100 times before. (P2-001)}  
\\end{quote}

Another participant described a similar pattern:

\\begin{quote}  
    \\small \\textit{There would be policies; whether or not people read the policy is a different matter... there’s probably thousands of policies... I treat it as more of a five-minute hassle. (P2-002)}  
\\end{quote}

This behaviour showed passive compliance with the checkbox without changing behaviours, hiding risks and undermining institutional readiness.

Reliance on common sense traps over formal policy further explained patterns in participant responses. P2-002 observed:

\\begin{quote}  
    \\small \\textit{I would say a lot of people would think the basic training is common sense... because it’s common sense, that's probably where people tend to ignore it. (P2-002)}  
\\end{quote}

Others are confused about the data protection, policy, responsibilities and practical application. Participant (P2-007) explained data protection:

\\begin{quote}  
    \\small \\textit{Data protection policy is, I think, organised by the library... but I don’t know how they are sharing the data... The \[Organisation\] is trying to protect data, but I do not really know how. (P2-007)}  
\\end{quote}

Another admitted direct uncertainty:

\\begin{quote}  
    \\small \\textit{No, I don't know about the policy... I am really struggling with the result of this policy. (P2-005)}  
\\end{quote}

This confusion from the participant reflected a breakdown between policy design and individual comprehension. This code reflected habituation, perceived irrelevance, and responsibility misinterpretation. This is significant because cybersecurity readiness requires more than documented rules. Clear understanding, practical clarity, and strong links between policy and daily work were essential.

Theme 11 (P2-T11) confirmed and extended prior research on policy ignorance and cybersecurity compliance behaviour. It demonstrated that individual decision styles and avoidance patterns drove non-compliance with security policies \\citep{Donalds2020}. It further showed that impulsivity and habitual overrides led individuals to bypass formal policy in favour of personal judgement \\citep{Hadlington2017}. Similarly, the findings indicated that security culture failed when policies were not reflected in daily organisational practice \\citep{DaVeiga2020}. However, this theme introduced new empirical findings not previously documented. The commonsense trap, dismissing training as self-evident to avoid formal policy, represented a new HEI-specific avoidance mechanism. Checkbox compliance behaviours, empirically documented through participant accounts of muting videos and skipping to assessments, extended \\citet{Haney2020} foundational work on moving beyond tick-box compliance. Data protection ownership confusion, where participants were uncertain whether the library or IT managed protection, revealed a structural comprehension gap absent from prior compliance frameworks.

\\section{Summary and Conclusion}  
\\label{sec:6.4}

This Chapter \\ref{chapter:c6} examined how organisational culture shaped cybersecurity readiness in the higher education institute context. Phase 2 findings and discussion addressed Research Question 2 (RQ2). Eleven themes emerged using template analysis, and each exposed several weaknesses in how cybersecurity was understood, communicated, or reinforced.

Consistent engagement was not always achieved, even though policies and training were in place. In many cases, cybersecurity was preserved as a managerial task instead of a shared duty. Onboarding gaps, doubtful reporting pathways, dull training, and fragmented governance reduced confidence and clarity. Leadership behaviour also influenced how seriously security was taken. When expectations were not reinforced in regular discussions or meetings, cybersecurity slipped behind other priorities.

Cultural assumptions influenced behaviour more than formal rules. Silence was often taken as safety, and trust replaced verification. Some risks were minimised because no visible incident had occurred. Over time, this created distance between policy engagement and practice. Individual judgment frequently switched to structured guidance, especially when policies were unclear or miscommunicated.

The explanatory case study design allowed these patterns to be examined in depth. Through interviews, it was shown that weaknesses were social, relational, and organisational. Phase 2 provided an organisational response that enhanced the individual findings from Phase 1\. Together, they revealed a cybersecurity culture shaped by leadership actions, policy communication, and daily priority balance. These insights are strengthened by expert validation in the next Chapter \\ref{chapter:c7}.

\\chapter{Phase 3 Findings and Discussion}  
\\label{chapter:c7}

\\setcounter{figure}{0}  
\\renewcommand{\\thefigure}{7.\\arabic{figure}}

\\section{Introduction}  
\\label{sec:7.1}

The previous Chapter \\ref{chapter:c6} presented Phase 2 findings and discussion on organisational cybersecurity’s cultural impact on readiness. This chapter covers Phase 3 expert validation of Phases 1 and 2, including recommendations, arguments, variations, and limitations.

A purposive sampling (see Section \\ref{sec:3.2.4}) technique was used to select higher education institutes (HEIs) experts for semi-structured interviews in phase three. These were experts in cybersecurity and professional practice \\citep{Ramos2022}. Phase three themes are presented sequentially, supported by relevant quotes \\citep{Barruga2025, Terrell2023}. Experts confirmed patterns, identified refinements, and assessed accuracy, relevance, completeness, and organisational alignment using experience and examples \\citep{Latif2025, McCants2022}. This clarified boundaries and followed qualitative validation methods \\citep{King2017, Miles2014}.

Experts highlighted workload pressure and operational fatigue as key influences on cybersecurity behaviour. These shaped task prioritisation, training engagement, and policy interpretation. Feedback refined factors revealed constraint-behaviour interactions and enhanced cybersecurity perception. 

Figure \\ref{fig:7.1} maps Chapter \\ref{chapter:c7}’s structure. It outlines Phase 3 findings and discussion, including validation outcomes, suggestions, and limitations.  
 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 7 Roadmap\]{%  
    \\textbf{Figure 7.1}\\\\\[1.2em\]  
    \\textit{Chapter 7 Roadmap.}  
    }  
    \\label{fig:7.1}  
    
    % \\addcontentsline{lof}{figure}{7.1 \\hspace{0.18cm} Chapter 7 Roadmap}  
      
    \\includegraphics\[width=0.9\\linewidth\]{Figures/c7/7.1roadmap.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
   
 

\\section{Phase 3 \- Research Expert Validation}  
\\label{sec:7.2}

\\subsection{Research Findings}  
\\label{sec:7.2.1}

In Phase 3, seven domain experts assessed the 16 themes resulting from Phases 1 and 2, which contained five individual-level and eleven organisational-level themes. Their assessment focused on relevance, clarity, and alignment with cybersecurity practices within HEIs.

Collectively, the expert feedback showed strong alignment with the study findings. Most themes were retained, indicating that the results reflected credible patterns of cybersecurity behaviour and organisational dynamics. However, this agreement was not uniform across all themes and required careful interpretation beyond simple consensus.

For Phase 1, Themes 1 (P1-T1), 2 (P1-T2), and 4 (P1-T4) were steadily agreed (A), revealing stable and recognisable individual-level behavioural patterns. Theme 3 (P1-T3) was also essentially accepted, although Expert 3 (P3-003) raised concerns about the simplicity of its title. This feedback led to a minor revision to better represent the decision-making processes associated with coping behaviour. Theme 5 (P1-T5) received comprehensive support, yet Expert 3 (P3-002) disagreed (D), stating that IT authority support in their institution was consistently clear and accessible. This perspective contrasted with other experts, who reported gaps in organisational guidance and authority visibility, thereby strengthening the original interpretation of theme 5 (P1-T5).

In Phase 2, partial agreement (PA) was clearly observed in themes related to organisational cultural influence and behavioural conditions, particularly Themes 1 (P2-T1), 2 (P2-T2), 4 (P2-T4), and 5 (P2-T5). Experts P3-002, P3-006, and P3-007 noted that physical security signals, such as posters and office layouts, affected awareness, while their impression varied depending on visibility, role significance, and employee experience. Similarly, Experts P2-004 and P2-007 acknowledged leadership inconsistency in Theme 2 (P2-T2), but anticipated that organisational values were not always enthusiastically considered during decision-making. In Theme 4 (P2-T4), Expert (P2-001) showed ambiguity in the interpretation of trust, indicating a need for transparent conceptual framing. For Theme 5 (P2-T5), responses reflected variation across departments, where one expert (P3-003) observed strong leadership engagement, while others described noticeable gaps. Despite these differences, all experts recognised consistent behavioural patterns across organisational cultural contexts, supporting the retention of these themes.

Various forms of disagreement appeared in themes shaped by institutional settings and operational exposure, particularly Themes 6 (P2-T6), 8 (P2-T8), 9 (P2-T9), and 11 (P2-T11). Expert (P3-003) disagreed with Theme 6 (P2-T6), advising that risk sensitivity was accurate within their organisation, whereas other experts described clear biases towards risk underestimation. In Theme 8 (P2-T8), Expert (P2-006) questioned whether onboarding gaps should be attributed to leadership, instead pointing to the HR department as the responsible party. Similarly, Theme 9 (P2-T9) drew disagreement from Expert (P3-003), who informed effective governance practices locally, while others emphasised weaknesses in organisational enforcement and individual accountability. For Theme 11 (P2-T11), Expert (P3-003) challenged whether policy ignorance stemmed from behavioural disengagement or insufficient training. These contrasting views reflected differences in institutional maturity and organisational structure, rather than dismissal of the themes themselves.

A smaller set of concerns, particularly in Theme 3 (P2-T3), related to how the theme was expressed. Expert (P3-003) indicated uncertainty due to the way the belief was presented, advocating that clearer delivery was required. Importantly, this did not challenge the presence of the behaviour, but stressed the need for adjusted conceptual clarity.

No theme was rejected. Expert judgement variations identified contextual limits and refinement areas. They strengthened findings' depth, showing broad applicability sensitive to institutional context. This strengthened the explanatory depth of the findings by demonstrating that while the thematic framework was broadly applicable, its expression remained sensitive to HEIs' context. A detailed summary table of expert judgements is provided in Appendix\~\\ref{appendix:F}.     
 

\\subsection{Research Discussion}  
\\label{sec:7.2.2}  
This section presents expert discussions on Phases 1 and 2 findings. It clarifies how the 16 themes influenced organisational cybersecurity readiness.

\\subsubsection{Expert Validation on Phase 1}  
\\label{sec:7.2.2.1}

Phase 1 yielded five themes, which experts reviewed individually, validating findings with supporting quotations to ensure transparency. 

\\paragraph{\\textbf{Validation of Theme 1- Cybersecurity Awareness and Training Effectiveness (P1-T1):\\\\}}   
Expert validation confirmed that cybersecurity awareness and training influenced behaviour only when learning was grounded in lived experience and operational relevance. Experts (P3-001, P3-003) supported that formal training alone was insufficient to produce sustained behavioural change, particularly in academic environments.

When asked whether existing awareness programs changed behaviour, experts shared:

\\begin{quote}  
    \\small \\textit{It’s just people being lazy. IT training happens across all levels. Saying, ‘I didn’t know,’ is an excuse. (P3-003)}  
\\end{quote}

Experts confirmed that generic or inconsistent training failed to drive behaviour change, while employees provided excuses to avoid accountability \\citep{Reeves2025}.

\\begin{quote}  
    \\small \\textit{If someone has been impacted by a cybersecurity event, it has a stronger effect. They are more likely to retain the lessons on how to avoid it in the future. Without that real-world experience, education \[training/workshop\] alone might not stick as effectively. (P3-001)}  
\\end{quote}

Experts also linked training effectiveness to leadership reinforcement, frustration with passive delivery, and policy visibility in the everyday work context. P1-006 shared:

\\begin{quote}  
    \\small \\textit{Yes, I think it would help. But often managers are so busy that they don’t reinforce the message. They have many other things to handle, so it’s unlikely to be a priority. And when it comes to policies, many people don’t even realise such policies exist. (P3-006)}  
\\end{quote}

Experts further explained that training effectiveness was constrained by the difficulty of tailoring content beyond broad role categories. One expert described the practical limits of customisation in organisational training delivery:

\\begin{quote}  
    \\small \\textit{It’s very, very difficult to tailor training and awareness programs down to the individual…So it has to be a little bit generic, even when it’s targeted. The same applies to HR or the IT school. We tailor it to the type of work they do, but going deeper than that would be extremely difficult. We usually tailor training based on role types, not individual profiles, because going further is too much work. (P3-007)}  
\\end{quote}

Accountability and consequences were also emphasised during validation. Experts argued that awareness without responsibility weakened behavioural outcomes. P3-003 stated:

\\begin{quote}  
    \\small \\textit{Training must be consistent, followed up, and measured for effectiveness. Employees should be held accountable; they can’t just say, I didn’t know. (P3-003)}  
\\end{quote}

The expert panel fully supported Theme 1 (P1-T1), with no structural alterations required. Proper training transforms employees from the weakest link into the organisation’s strongest cybersecurity defence \\citep{Kamarulzaman2024}. Validation refined its emphasis on experience-based learning, role relevance, reinforcement, and accountability. Training effectiveness depends on behavioural change rather than completion \\citep{alshaikh2020, Haney2020}.

\\paragraph{\\textbf{Validation of Theme 2 \- Assessing and Mitigating Threats Through Awareness and Consequence Management (P1-T2):\\\\}} 

 Expert review collectively supported the theme, confirming that cybersecurity behaviour was influenced by how clearly individuals understood both the ease of attack and the consequences of failure. Experts emphasised that an inadequate understanding of consequences clearly undermined secure decision-making \\citep{Parsons2015}.

\\begin{quote}  
    \\small \\textit{If people don’t understand the risks or the potential consequences, they’re not going to take the right actions. It leads to uninformed decision-making. (P3-006)}  
\\end{quote}

An expert noted that technical controls created a false sense of security. Employees assumed safeguards prevent harm, even as they ignored vulnerabilities. Impacts include:

\\begin{quote}  
    \\small \\textit{Some people see security as a black box, something they're not directly involved in. They might mistakenly feel fully protected by the university’s systems and processes. This creates a false sense of security, where they assume everything is being taken care of for them and feel no need to think about it in their daily work. (P3-001)} \\\\  
    \\small \\textit{Over-relying on IT is risky. Technical controls help, but they aren’t enough. For example, phishing emails bypass filters because attackers adapt. Individuals must also take responsibility and understand that technology alone cannot prevent threats. (P3-003)}  
\\end{quote}

This illustrated how misplaced trust in safeguards lowered personal threat appraisal, proactive assessment, and mitigation.

Experts consistently linked threat awareness to an understanding of organisational consequences, emphasising that individual actions could have institution-wide implications.

\\begin{quote}  
    \\small \\textit{If someone does the wrong thing, the impact to the \[organisation\] could be enormous. And we’ve seen this happen at other institutions with breaches and security incidents. (P3-007)} \\\\  
    \\small \\textit{Education helps people understand cybersecurity issues, the types of attacks, and how they happen...experienced people know how others suffer and how they themselves are affected. They understand the consequences. (P3-004)}  
\\end{quote}

This perspective reinforced the view that recognising consequences of security failures as concrete and organisationally significant developed secure behaviours, reputation and accountability in cybersecurity action \\citep{Cram2023, mou2022}.

This theme demonstrates exploitability, communicating real consequences, and reinforcing individual responsibility. All seven experts endorsed Theme P1-T2 without structural change.

\\paragraph{\\textbf{Validation of Theme 3 \- Balancing Confidence, Capability, and Costs in Coping Strategies (P1-T3):\\\\}}  
Cybersecurity behaviour reflected employee balancing ability, control effectiveness, and effort costs \\citep{Kiran2025, Latif2025}. Expert validation supported this interpretation, with one expert recommending a clearer emphasis on the decision process involved. As P3-003 observed, the issue was not the absence of controls but rather how people decided whether and how to act, leading to the revised title, Deciding to Cope. This aligned with coping in PMT Theory, where self-efficacy, response efficacy, and response cost together influenced protective activity.

When discussing delayed responses after detecting suspicious activity, experts emphasised hesitation and misplaced urgency. One expert explained:

\\begin{quote}  
    \\small \\textit{We’ve had actual examples where someone clicked a suspicious link, then noticed something strange happening on their computer, so they just went to lunch… If someone goes to lunch and comes back an hour later, in that time, we could lose half the network if something goes horribly wrong... We always say: If you think something’s not right, tell us. (P3-007)}\\\\  
    \\small \\textit{We must balance protection with practicality; otherwise, users resist security. (P3-004)}  
\\end{quote}

Experts noted that low personal responsibility reduced motivation to act. Participants observed why users deprioritised security:

\\begin{quote}  
    \\small \\textit{Cybersecurity is not the end product for any business. It’s an additional task for employees. And they think, “Even if something happens, I won't be responsible. The organisation will be.” They just care about their job. For common users, this is just a nuisance. (P3-005)}  
\\end{quote}

The expert added that coping improved with concrete, personal consequences:

\\begin{quote}  
    \\small \\textit{Unless we show them its real value, for example, if an organisation is penalised for over \\$1 million. This is what we need to tell people: your single click can cost your organisation or society millions of dollars, not just money, but reputational damage that can be worse than financial loss. (P3-005)}  
\\end{quote}

Together, these experts confirmed that cybersecurity coping was shaped by a deliberate assessing process involving effort, perceived responsibility, and practical value. Validation confirmed that Theme 3 (P1-T3) decisions balanced usability and consequences. Six experts agreed, while one refined the title. 

\\paragraph{\\textbf{Validation of Theme 4 \-  Proactive and Compliant Cybersecurity Behaviours (P1-T4):\\\\}}  
Experts confirmed that compliance depended not just on policies, but also on individual understanding of expectations, recognition of consequences, and a sense of accountability. Experts noted that policy engagement was low when relevance was unclear. Awareness stayed passive unless tied to tasks or consequences:

\\begin{quote}  
    \\small \\textit{I think it’s difficult to get many people interested in policies. Definitely not, I don’t \[read policy\], unless there’s a direct reason or it impacts me personally. (P3-002)}  
\\end{quote}

Experts further explained that compliance involved a trade-off between good intentions and practical constraints. P3-001 reflected:

\\begin{quote}  
    \\small \\textit{I could see this as a kind of trade-off. People want to behave properly and develop good habits, but if it interferes with their work or takes too much time, they might cut corners. (P3-001)}  
\\end{quote}

Risk understanding and habitual practice were also identified as reinforcing compliance. As one expert noted:

\\begin{quote}  
    \\small \\textit{People who understand the risks and have good habits are more likely to follow policies. I agree with that. (P3-003)}  
\\end{quote}

Experts noted that understanding alone failed without clear governance. One expert highlighted missing context:

\\begin{quote}  
    \\small \\textit{Unless you provide clear context. For example, when we ask staff to complete cybersecurity training, are they told it’s a regulatory requirement? If they understood it’s needed for compliance with cybersecurity laws, they’d see it as a responsibility. Unfortunately, this is rarely conveyed. … So, people think, “Whether I do it or not, it doesn’t matter.” We need smart governance linking everything clearly, with checklists to ensure compliance with policies and procedures. (P3-005)}  
\\end{quote}

Collectively, expert feedback validated Theme ‘Proactive and Compliant Cybersecurity Behaviours’ without modification. Experts agreed that proactive compliance needed clear, practical policies framed as shared responsibility. The validation showed compliance depended on relevance, clarity, and reinforcement \\citep{Ifinedo2012}.

\\paragraph{\\textbf{Validation of Theme 5 \- Addressing Gaps in Leadership and Authority Support (P1-T5):\\\\}}

Phase 3 expert validation reaffirmed leadership and authority support as a foundational situation impacting cybersecurity behaviour \\citep{alshaikh2020, DaVeiga2020, Georgiadou2022}. Experts (P1-T1, P1-T2, P1-T4) emphasised that leadership actions, priorities, and visible engagement directly influenced how individuals interpreted the importance of cybersecurity in work.

Experts linked leadership behaviour to motivation and norms. P3-004 and P3-005 supported the leadership tone:

\\begin{quote}  
    \\small \\textit{Absolutely. Leaders shape the tone and set examples for their teams. Leaders shape employee behaviour by understanding and motivating them. It’s the leader’s main task to know their employees, inspire them, and guide them towards following proper practices. Leaders model organisational culture and motivate people; it’s very important. If leaders don’t do this, it’s a serious problem. (P3-004)}  
\\end{quote}

Experts also noted that leadership gaps were often unintentional, reflecting limited awareness or competing priorities. P3-006 observed:

\\begin{quote}  
    \\small \\textit{Yes, I do think it’s an issue. But I also wonder if some leaders themselves aren't fully aware of what’s required. (P3-006)}  
\\end{quote}

Another expert underscored the consequences of leadership silence for staff decision-making:

\\begin{quote}  
    \\small \\textit{When leaders don't talk about cybersecurity, staff are unsure what to do. (P3-003)}  
\\end{quote}

One expert contrasted, citing strong leadership support locally:

\\begin{quote}  
    \\small \\textit{No. I’d say cybersecurity support is very good in my department... (P3-002)}  
\\end{quote}

This contrast showed support varied by unit. Most experts saw signalling gaps as systemic.

One expert summarised the broader challenge succinctly:

\\begin{quote}  
    \\small \\textit{I think it definitely does \[matter\]… because it’s absolutely an issue. It’s something we face daily. It goes back to building a cybersecurity culture across the organisation. (P3-007)}  
\\end{quote}

Expert validation confirmed inconsistent institutional leadership engagement, despite unit-level support. Theme 5 (P1-T5) remained unchanged. The majority agreement and Phase 1 findings supported retention. Uneven leadership proved key for cybersecurity readiness.

\\subsubsection{Expert Validation on Phase 2}  
\\label{sec:7.2.2.2}

Phase 2 examined organisational cultural influences on cybersecurity behaviour. Phase 3 experts assessed the accuracy of the theme in higher education practice.

\\paragraph{\\textbf{Validation of Theme 1-  Physical Symbolism and Security Culture Blind Spots (P2-T1):\\\\}}   
Theme P2-T1 examined how visible cues, environmental artefacts, and everyday physical practices shaped cybersecurity behaviour beyond formal policy \\citep{Chaudhary2022, DaVeiga2010, Dimitrov2013}. Expert validation confirmed that physical symbolism influenced awareness and behaviour, although its effectiveness varied by context, visibility, and renewal.

Experts agreed that repeated visual cues reinforce awareness. P3-005 emphasised the effect of visibility:

\\begin{quote}  
    \\small \\textit{Of course, people, what they see, they remember. Information overloading has caused a lot of issues, so we forget what is not present at the moment. These physical symbolisms, if you see them one, two, three times, they stick in your mind. If you don’t see them, you forget them. (P3-005)}  
\\end{quote}

Another expert emphasised:

\\begin{quote}  
    \\small \\textit{Things like posters or notices with security information are important, but they must be concise and focused on key points so people can read them quickly and retain the message. Placement also matters; where you put them makes a difference. (P3-004)}  
\\end{quote}

P3-006 noted cues lose salience over time unless refreshed:

\\begin{quote}  
    \\small \\textit{Physical reminders can have an impact, but they eventually lose effectiveness. People see them so often that they stop noticing them. Then you need to refresh or update them. Office layout also matters, whether staff even see these things. (P3-006)} \\\\  
    \\small \\textit{It can’t hurt to have visual indicators; it becomes almost a kind of subliminal messaging... (P3-007)}  
\\end{quote}

Two experts noted relevance varies by audience. Cues suited non-technical staff more than IT groups:

\\begin{quote}  
    \\small \\textit{That might depend on the group. The people I deal with are in IT, so they already know these things. But for less tech-savvy staff or students, clear physical signs or instructions could be useful. (P3-001)} \\\\  
    \\small \\textit{You’d think more posters and visible reminders would help promote a security culture... (P3-002)}  
\\end{quote}

Experts confirmed physical symbolism (P2-T1) influences behaviour, though unevenly. All experts clearly supported the theme without rejecting its relevance.  
 

\\paragraph{\\textbf{Validation of Theme 2- Organisational Values Are Not Reflected in Daily Leadership Decisions (P2-T2):\\\\}}   
Experts supported the view. Inconsistent leadership decisions undermined values, weakened cybersecurity priority under pressure; Values resolved artefacts and assumptions in culture theory \\citep{Adamu2025, Schein2010, Schein2019}. An expert noted that personnel rarely hold abstract values in mind when working, stating:

\\begin{quote}  
    \\small \\textit{I’m not sure people actively carry organisational values in their minds when working. Most are just focused on their tasks. (P3-002)}  
\\end{quote}

Other experts highlighted inconsistency at the leadership level. Experts explained that misalignment between supported values and leadership behaviour weakened rule legitimacy:

\\begin{quote}  
    \\small \\textit{Leaders often don’t act on the values the organisation claims to support. This confuses staff and weakens the impact of cybersecurity rules. (P3-003)}  
\\end{quote}

Experts highlighted absent governance and reinforcement. One argued values weaken without recognition or evaluation links:

\\begin{quote}  
    \\small \\textit{If your values are just a chart that people don’t even remember, and they’re not reflected in practice, ultimately, everyone will ignore them. (P3-005)}  
\\end{quote}

One expert (P3-001) clarified that values stay abstract unless operationalised for cybersecurity. Their link remained rarely explicit:

\\begin{quote}  
    \\small \\textit{Yes, I see how values might guide decision-making, but unless they’re explicitly tied to cybersecurity, the link feels weak. Unless each value is detailed with guidance on how it applies to cybersecurity, people won’t see the connection... If they included guidelines, for example, “this value relates to cybersecurity in this way”, it would make more sense... (P3-001)}  
\\end{quote}

Overall, experts agreed that organisational values existed but were inconsistently translated into daily cybersecurity decisions. While some questioned the strength of this influence, none rejected the theme outright. Consequently, the theme was confirmed without modification, with broad agreement.

\\paragraph{\\textbf{Validation of Theme 3 \- Assumptive Resistance Loops Undermining Cybersecurity Readiness (P2-T3):\\\\}}   
Experts consistently described how employees defaulted to familiar or easier practices when security measures were perceived as disruptive to primary work tasks. One participant explained:

\\begin{quote}  
    \\small \\textit{As cybersecurity threats grow more complex, people can get burnt out trying to keep up with everything. One example is constant password changes. It creates a high mental load... If security measures are simpler and less disruptive, they’re more likely to be followed. (P3-001)}  
\\end{quote}

Resistance occurred from efficiency assumptions, not only a lack of awareness. Cybersecurity seemed secondary to tasks. One expert linked this directly to how work is evaluated:

\\begin{quote}  
    \\small \\textit{It’s not considered part of your job... You will be evaluated based on your KPIs, and cybersecurity is not there. So why should I focus on reading those emails or policies which are not counted in my job? (P3-005)}  
\\end{quote}

Others emphasised that resistance increased when controls were experienced as obtrusive or poorly aligned with normal workflows. P3-003 noted:

\\begin{quote}  
    \\small \\textit{If the security policies are very obtrusive, the staff might get annoyed. (P3-003)}  
\\end{quote}

Although the expert disagreed with the theme’s framing, their view supported that ease-of-use shapes behaviour. 

Communication overload further reinforced assumptive resistance. One expert noted repeated messaging failed to change behaviour despite communicating with official channels:

\\begin{quote}  
    \\small \\textit{People chose not to read it... even if we communicated with every person daily, we’d still get people saying: “Why do we have to do this?” (P3-007)}  
\\end{quote}

Experts consistently found that individuals viewed security as optional or secondary to productivity and habits. P3-003 questioned framing, but most agreed that assumptive loops weakened readiness. Accordingly, the theme was confirmed without modification. Experts clarified that resistance stemmed from assumptions about effort and priority, not ignorance.

\\paragraph{\\textbf{Validation of Theme4 \- Experiential Trust Threshold and Disengagement in Incident Reporting (P2-T4):\\\\}} 

Expert validation supported this theme by confirming that trust in how incidents were handled strongly shaped indecision or reporting behaviour \\citep{khadka2025, ulven2021}. While not all experts experienced this issue personally, most recognised its relevance for others, particularly where fear of blame, poor follow-up, or unclear consequences existed.

One expert explicitly positioned themselves outside the problem but acknowledged its broader impact:

\\begin{quote}  
    \\small \\textit{Yeah. I don’t feel that way personally, but I can see how others might. It could definitely affect their willingness to report if they fear it’ll reflect badly on them. (P3-001)}  
\\end{quote}

The expert also observed that organisational responses and managerial actions shaped whether employees felt safe to report incidents. One expert stated:

\\begin{quote}  
    \\small \\textit{If managers or higher authorities fail to respond properly, it discourages reporting and creates bigger problems. (P3-004)}  
\\end{quote}

Another linked reporting behaviour directly to organisational cultural direct impacting:

\\begin{quote}  
    \\small \\textit{If the organisational culture is, you will be penalised or punished for being honest... of course, people will just put it under the carpet. It all depends on organisational culture. (P3-005)}  
\\end{quote}

Even in environments where reporting was automated, trust remained a decisive factor. P3-006 explained:

\\begin{quote}  
    \\small \\textit{\[IT Department\] automatically reports incidents back to managers... but trust is still important. People need to feel safe about how those conversations happen afterwards. (P3-006)}  
\\end{quote}

This expert further noted that formal policy alone was insufficient if individuals did not engage with it:

\\begin{quote}  
    \\small \\textit{If people actually read the policy documents, they’d know how to report; it’s all there. (P3-007)}  
\\end{quote}

Expert feedback showed incident reporting depended not only on processes but also on experiential trust built through prior interactions and leadership responses. One expert (P3-001) did not personally experience this barrier but recognised its relevance for others. The remaining panel supported the theme, leading to confirmation without modification.

\\paragraph{\\textbf{Validation of Theme 5 \- End-User Behavioural Drift and Compliance Fatigue (P2-T5):\\\\}} 

Experts supported that behavioural drift and compliance fatigue were persistent influences on cybersecurity practice, specifically where security obligations were perceived as troublesome, mentally demanding, or misaligned with work priorities \\citep{bada2019cyber, khadka2025, Schein2017}. Some described compliance fatigue as a practical reality that drove workarounds:

\\begin{quote}  
    \\small \\textit{Compliance fatigue is real. If people see security measures as obstacles, they will look for workarounds whenever possible. (P3-002)} \\\\  
    \\small \\textit{Logging an IT request can mean delays... instead, people take the fastest route to get their job done, even if it’s not the correct or secure method. (P3-002)}  
\\end{quote}

Other experts emphasised that usability outweighed rule clarity, arguing:

\\begin{quote}  
    \\small \\textit{If something is easy, people will do it. If it’s hard or slow, they won’t. (P3-006)} \\\\  
    \\small \\textit{If security measures are simpler and less disruptive, they’re more likely to be followed. (P3-001)}  
\\end{quote}

Information burden was also identified as counterproductive. One expert observed:

\\begin{quote}  
    \\small \\textit{Fatigue is real. To reduce it, organisations need to simplify processes... overloading them with information is counterproductive. (P3-004)}  
\\end{quote}

Experts confirmed that behavioural drift arose from control friction, attention demands, and productivity conflicts. One (P3-003) stressed accountability, but the panel agreed fatigue and convenience drove regular behaviour.

\\paragraph{\\textbf{Validation of Theme 6 \- Cultural Miscalibration in Cyber Risk Perception (P2-T6):\\\\}}   
 This theme reflects a cultural miscalibration in cyber risk perception, where experts observed that individuals interpret organisational security risks through personal experience and everyday norms, leading to systematic underestimation of how individual actions translate into broader institutional impact \\citep{Cains2022, Sutton2025}.

\\begin{quote}  
    \\small \\textit{Culture influences behaviour. Phishing simulations help reinforce consequences. If people repeatedly fail, they’re retrained. That feedback loop likely deters risky behaviour over time. (P3-002)}  
\\end{quote}

This disconnect was most visible in how employees valued their own accounts. P3-005 explanation:

\\begin{quote}  
    \\small \\textit{Attackers compromise normal accounts from users who set passwords like ABC123 because they don’t consider their account valuable... They think, “It’s just student emails, it doesn’t matter if compromised.” But one user account can expose so much organisational information…Through that account, they escalate privileges and penetrate the organisation... one account can lead to larger-scale risks and incidents. (P3-005)}  
\\end{quote}

Other experts recognised that experience influenced behaviour, even when formal guidance was available. 

\\begin{quote}  
    \\small \\textit{If people don't understand cybersecurity themselves, they won’t see the need. They’ll ask, “Why should I bother?” (P3-006)}  
\\end{quote}

P3-003 disagreed, citing personal non-risky behaviour from training. Yet they framed it as an individual matter, not rejecting the pattern. 

\\begin{quote}  
    \\small \\textit{I can see how that happens, but I can’t relate personally... That probably reflects my training and mindset. (P3-003)}  
\\end{quote}

This contrast highlighted perceptual variation, reinforcing the theme. Experts noted organisational reality contradicted assumptions:

\\begin{quote}  
    \\small \\textit{We’re under attack right this minute, all day, every day... Everyone has a role to play. (P3-007)}  
\\end{quote}

Experts confirmed misaligned risk perception persisted, with people underestimating organisational impacts.

\\paragraph{\\textbf{Validation of Theme 7 \- Security Culture Embarrassment Barrier (P2-T7):\\\\}}   
Embarrassment and fear culture inhibit timely reporting despite pathways. Experts consistently framed this barrier as a cultural issue, not a technical one, and confirmed that emotional hesitation delayed escalation of potentially serious incidents \\citep{Patterson2024}.

An expert described embarrassment as an immediate human response following a mistake:

\\begin{quote}  
    \\small \\textit{Someone does something, and the first thing they say is, “Oh, I’m so embarrassed. I shouldn’t have done this.”... People won’t want to put their hand up and say, “Oops, I’ve messed up.” The problem is what they’ve done might be about to cause a significant issue…They should also know that it won’t be held against them. But we still need to know what’s happened from a security and incident response perspective. (P3-007)}  
\\end{quote}

Other experts linked embarrassment directly to organisational culture. One stated:

\\begin{quote}  
    \\small \\textit{If staff feel embarrassed or fear consequences, they will stay silent instead of reporting issues, which increases risks. Normally, this is an organisational culture issue. (P3-004)}  
\\end{quote}

Another expert emphasised the role of blame:

\\begin{quote}  
    \\small \\textit{If you have a culture of blaming and shaming, why would people report?... We should appreciate honesty. Whatever happened, happened; let’s focus on preventing it from happening again. (P3-005)}  
\\end{quote}

Even in surroundings where incidents were automatically escalated, embarrassment was still recognised as influential:

\\begin{quote}  
    \\small \\textit{Here, incidents are automatically reported anyway, so staff don’t have a chance to hide it. But yes, in general, embarrassment is a factor. Workplace culture affects this. (P3-006)}  
\\end{quote}

Another expert linked this hesitation to perceived self-image:

\\begin{quote}  
    \\small \\textit{If someone clicks on a malicious link, they might feel embarrassed and stay silent. (P3-001)}  
\\end{quote}

Experiences varied, but no expert rejected the theme. The panel endorsed non-disciplinary messaging, reassurance, and cultural normalisation to boost incident reporting. Theme confirmed unchanged; individual sensitivity and cultural barriers affect readiness.   
 

\\paragraph{\\textbf{Validation of Theme 8 \- Leadership Lag in Onboarding Cybersecurity Policy (P2-T8): \\\\}}  
Expert validation mostly confirmed that gaps in early cybersecurity onboarding weaken readiness, particularly when responsibility is diffused between leaders and central processes \\citep{Cheng2022, DaVeiga2010}. Managers assume induction covers security policies. They skip verification, signalling low priority. Newcomers make mistakes; vigilance erodes.

Experts highlighted the consequences of insufficient cybersecurity grounding at entry:

\\begin{quote}  
    \\small \\textit{If new staff don’t get that foundation, or if managers don’t know what’s covered, then both sides can be left uncertain. In the event of a security issue, staff could be lost on what to do. (P3-001)} \\\\  
    \\small \\textit{I’d say, I’m not familiar with the current onboarding process, but I agree, it would help if there were a clear element of cybersecurity training at the start. (P3-001)}  
\\end{quote}

Another expert noted uncertainty about whether cybersecurity was meaningfully embedded in induction at all:

\\begin{quote}  
    \\small \\textit{If there isn’t sufficient cybersecurity training as part of onboarding, that would absolutely impact readiness. I honestly don’t know what the onboarding cybersecurity training looks like for new staff. (P3-002)}  
\\end{quote}

Leadership duty was highlighted by experts who viewed onboarding gaps as a failure of managerial awareness and positioning decisions:

\\begin{quote}  
    \\small \\textit{Leaders must clearly know their employees’ knowledge and skills. If they don’t understand their team, it creates big problems. If someone lacks awareness, they shouldn’t be placed in roles without proper onboarding. (P3-004)}  
\\end{quote}

Others observed that cybersecurity was often overshadowed by traditional induction priorities:

\\begin{quote}  
    \\small \\textit{Most organisations do health and safety onboarding, but cybersecurity policies are rarely explained to new hires. That’s what people take advantage of to avoid responsibilities. (P3-005)}  
\\end{quote}

A minority view reframed the issue as an HR responsibility. One expert argued:

\\begin{quote}  
    \\small \\textit{I think this falls back on HR. They manage onboarding, and this should be part of it. As a leader, you’d assume HR covers essential training during induction. (P3-006)}  
\\end{quote}

Another expert acknowledged the existence of formal onboarding checklists but identified weak enforcement:

\\begin{quote}  
    \\small \\textit{There’s a clearly defined onboarding checklist... But if there’s no follow-up to confirm that they’ve actually done it, then there could absolutely be a gap. (P3-007)}  
\\end{quote}

Experts agreed that onboarding was inconsistent, despite HR assignment. Leadership assumptions and poor confirmation left the new employee exposed. One expert differed, but panel consensus confirmed the theme unchanged.

\\paragraph{\\textbf{Validation of Theme 9 \- Strategic Weakness in Security Governance in Academia (P2-T9):\\\\}}  
Governance, enforcement, and resourcing gaps undermine academic readiness. Expert 003 disagreed locally, but the majority noted issues with training, accountability, and oversight. Theme confirmed unchanged.

Experts emphasised that governance failures were most visible through ineffective or weakly enforced training systems \\citep{alshaikh2020}. One expert explained how mandatory training often lacked engagement:

\\begin{quote}  
    \\small \\textit{If training is boring or irrelevant, people will click through quickly. This applies across all mandatory training. Training needs interactive elements, relevant examples, and assessments so participants engage meaningfully. (P3-006)}  
\\end{quote}

Others reinforced that weak enforcement diluted governance intent:

\\begin{quote}  
    \\small \\textit{Roles and responsibilities must be clearly defined. Even then, if they’re not enforced or evaluated, they’ll be ignored. And if it’s not someone’s primary responsibility, it will be neglected. (P3-005)}  
\\end{quote}

Resource constraints were also identified as a structural governance issue:

\\begin{quote}  
    \\small \\textit{Weakness in governance affects everything. Training needs to be effective and practical. Leaders are responsible for this. But cybersecurity is resource intensive and costly. If organisations don’t allocate enough resources or budget, leaders are limited in what they can do. (P3-004)}  
\\end{quote}

Experts noted operational compliance limits in academic operations. One highlighted the consequences:

\\begin{quote}  
    \\small \\textit{We can't force somebody to read every screen. People just want to get through it. I don't think there’s any consequence if you don't actually complete it properly. (P3-007)}  
\\end{quote}

One expert (P3-003) disagreed, arguing that governance capacity already existed.

\\begin{quote}  
    \\small \\textit{I think the academic institutions I’ve seen do have the resources to properly support cybersecurity, so I would disagree with this. (P3-003)}  
\\end{quote}

However, P3-001 noted:

\\begin{quote}  
    \\small \\textit{I complete the training and pay attention to it, but I know some staff just click through it. (P3-001)}  
\\end{quote}

Overall, experts agreed that formal governance needed enforcement, resourcing, and evaluation. Weaknesses appeared in training, accountability, and leadership. Theme confirmed unchanged. 

\\paragraph{\\textbf{Validation of Theme 10 \- Leadership and Behavioural Dynamics Influencing Cybersecurity Culture (P2-T10): \\\\}}  
 All experts strongly supported that leadership behaviour directly shapes cybersecurity culture through modelling, attitudes, and everyday decision-making \\citep{DextrasGauthier2023, Kaptein2011}.

Across interviews, experts consistently emphasised that leaders set the behavioural tone that employees follow. Several experts (P3-003, P3-005, P3-006) stated:

\\begin{quote}  
    \\small \\textit{They \[leader\] just set the tone. That’s it. (P3-003)} \\\\  
    \\small \\textit{If leadership does not demonstrate what is important for the organisation, including cybersecurity, staff will behave the same way. (P3-005)}  
\\end{quote}

P3-001 explained how negative leadership signals weakened practice:

\\begin{quote}  
    \\small \\textit{If leaders express frustration, their teams are likely to feel the same way, which could weaken adherence to security protocols. If both leaders and their teams resist security measures, it devalues the process and creates a shared culture of non-compliance. (P3-001)}  
\\end{quote}

Concrete examples further demonstrated how leadership actions legitimised insecure practices. One expert described a case where managerial decisions directly undermined controls:

\\begin{quote}  
    \\small \\textit{I know of a manager who bought multiple Wi-Fi routers and installed them around their building because they weren’t satisfied with the existing network. That shouldn’t happen. In this case, it was the manager leading the way. Staff will inevitably follow that example. (P3-002)}  
\\end{quote}

Relational leadership and trust were also identified as key processes influencing behaviour. One expert stressed:

\\begin{quote}  
    \\small \\textit{Connecting with people is a leader’s main responsibility. If they can’t build relationships, they’re unfit for leadership. Leaders should discuss, understand problems, and help solve them. That’s how they create trust and alignment. (P3-004)}  
\\end{quote}

Experts confirmed that leadership behaviour shapes staff cybersecurity norms and responses. The theme was therefore confirmed without modification.

\\paragraph{\\textbf{Validation of Theme 11 \- Ignorance Towards Policy (P2-T11): \\\\}}  
Expert validation largely confirmed the finding that formal cybersecurity policies were frequently ignored or misunderstood \\citep{Kannelonning2023, Siponen2014}. Across interviews, experts repeatedly observed that policy documents existed but were not read or recalled. 

One expert described this pattern directly from operational experience:

\\begin{quote}  
    \\small \\textit{We see it every day. The policy documents are actually sitting here beside me, being updated as we speak. We know people don’t read them. There are things in those documents that, if they had read them, they wouldn’t be doing. When we say, “This is a breach of university policy,” they respond, “Oh, I didn’t know.” (P3-007)}  
\\end{quote}

Others linked policy ignorance to overload and poor accessibility. One expert explained:

\\begin{quote}  
    \\small \\textit{Being practical, life is already overwhelming. Even organisationally, if you ask any leader how many policies exist, nobody might remember the number. Sometimes, even finding policies is difficult; they’re just on paper. (P3-005)}  
\\end{quote}

An expert acknowledged their own limited engagement with written policy, reinforcing the regularisation of this behaviour:

\\begin{quote}  
    \\small \\textit{I’ll be honest: I haven’t read the policies myself. I focus on practical measures, protecting confidentiality, integrity, and availability, but I couldn’t tell you what the policies actually say. (P3-002)}  
\\end{quote}

The consequences of this gap were clearly articulated. P3-004 noted that failure to engage with policy directly increased exposure:

\\begin{quote}  
    \\small \\textit{Ignoring or not understanding policies is a big problem. Every organisation has strong security policies, but if people don’t follow them, risks increase significantly. (P3-004)}  
\\end{quote}

Others emphasised the structural causes of ignorance, particularly weak reinforcement after induction:

\\begin{quote}  
    \\small \\textit{Policy awareness should be reinforced during induction and performance reviews. Without follow-up, some people will claim ignorance. (P3-006)}  
\\end{quote}

From a compliance perspective, experts highlighted that reliance on personal judgment in place of policy undermined consistency:

\\begin{quote}  
    \\small \\textit{If staff ignore policies or act solely on their own judgment, it undermines compliance. Policies need to be better understood and enforced. (P3-001)}  
\\end{quote}

A minority view challenged the theme based on strong institutional training practices. P3-003 disagreed:

\\begin{quote}  
    \\small \\textit{They don’t just send an email. They have training with quizzes to ensure understanding. So, I’d say no to this question. (P3-003)}  
\\end{quote}

However, this disagreement was context-specific and did not negate the broader pattern identified across expert accounts. The theme was confirmed unchanged. Findings showed that formal policy alone is insufficient for consistent cybersecurity behaviour \\citep{Neri2024}.

\\subsection{Expert Recommendation}  
\\label{sec:7.2.3}

Expert validation interviews identified distraction and workload as a previously under-articulated but influential factor shaping cybersecurity behaviour. Experts indicated that competing demands, time pressure, and task overload frequently determined whether an individual noticed security cues, prioritised reporting, or delayed action \\citep{Posey2014}. This recommendation factor was suggested directly from Phase 3 expert reflection, was supported by other experts and was independently reinforced by earlier Phase 2 participant accounts, demanding its recognition as an influential factor.

When experts were asked whether any additional factors from their experience influenced individuals' attitudes towards cybersecurity practices, one expert explicitly stated: 

\\begin{quote}  
    \\small \\textit{Yes, distraction and workload. (P3-002)}  
\\end{quote}

This concern was echoed by several participants during interviews. They emphasised that cybersecurity behaviour could not be fully understood without everyday workload pressures. Experts (P3-004, P3-007) supported this view, while others raised concerns about time pressure and workload \\citep{Kannelonning2023}. Some of the Phase 2 participants (P2-005, P2-007) similarly noted pressures and stresses affected cybersecurity decisions.

\\paragraph{\\textbf{Distraction and Workload as Residual Cybersecurity Risk:\\\\}}  
Experts described distraction and workload as factors quietly increasing residual risk through delayed reporting, reduced vigilance, and discouraged escalation. Several experts noted avoidance often stemmed from workload pressure, not lack of awareness:

\\begin{quote}  
    \\small \\textit{I know there are issues I don’t report \[incident\] upwards, not out of embarrassment, but because I don’t want additional hassle or workload... (P3-002)}  
\\end{quote}

Workload was also associated with reduced attention, even among employees familiar with cybersecurity. Experts reflected:

\\begin{quote}  
    \\small \\textit{If they don’t have much time to spare, even I’m doing cybersecurity research, but with too many tasks and high pressure, you sometimes don’t check carefully. So, people may fall into phishing traps or other issues. (P3-004)} \\\\  
    \\small \\textit{When you’re busy, you rely on common sense, and things can slip through, especially during high workloads or peak periods. The sheer volume of emails can make it harder to stay vigilant. (P3-006)}  
\\end{quote}

Experts also noted that acceptance improved when security controls reduced effort and interruption. One explained:

\\begin{quote}  
    \\small \\textit{Too much \[awareness notification\] information will overload employees. (P3-004)} \\\\  
    \\small \\textit{If security measures increase mental workload, users see them negatively. Reducing mental load is key. For example, multi-factor authentication works well because it’s secure but doesn’t require frequent password changes. (P3-001)}  
\\end{quote}

Other Phase 2 participants confirmed workload and stress reduced secure behaviour; some shared (P2-005 and P2-007):

\\begin{quote}  
    \\small \\textit{If something slows me down, I’m more likely to put it aside and deal with it later, especially when I’m under pressure. (P2-005)} \\\\  
    \\small \\textit{People are juggling a lot already. Training, teaching, admin. Adding more security steps just feels like more work. (P2-007)}  
\\end{quote}

Together, distraction and workload persistently influenced cybersecurity readiness as background conditions. Despite awareness and training, a high workload shaped threat notice, incident reporting, and action timing. Expert recommendations and participant evidence confirmed that workload stress and distraction affected individual cybersecurity decision-making, enhancing the research explanatory depth.

 

% \\subsection{Expert Areas of Agreement and Variation}  
% \\label{sec:7.2.4}

\\subsection{Expert-Derived Implications }  
\\label{sec:7.2.4}

Expert feedback increased the analytical value of the thematic framework beyond confirmation. Across Phase 3 interviews, experts fundamentally validated the Phase 1 and Phase 2 themes while clarifying how contextual conditions shaped their expression. Where disagreement arose, it concerned the applicability of specific themes within enclosed settings rather than rejection of the underlying behavioural patterns. Four key implications emerged directly from expert experience.

\\paragraph{\\textbf{Cybersecurity readiness is a multi-factor condition:}} Experts consistently indicated that no single factor explained behavioural variation. While Phase 2 Theme 6 (P2-T6) emphasised cultural misperception, Expert (P3-003) recognised behavioural patterns in relation to resourcing constraints and system limitations rather than cultural factors alone. This exhibited that cultural explanations remained inadequate without considering operational capacity and infrastructure. This finding extended existing knowledge by empirically demonstrating that culture, resourcing, and systems must be addressed together rather than sequentially.

\\paragraph{\\textbf{Unclear responsibility ownership directly undermines implementation:}} In Phase 2, Theme 8 (P2-T8), Expert P3-006 positioned onboarding as an HR department responsibility while still acknowledging that onboarding gaps weakened cybersecurity readiness. Other experts associated this responsibility with line leadership. This variance illustrated how uncertain ownership created implementation gaps, especially during early employee integration. Cybersecurity policy embedding thus requires explicit responsibility across leadership, HR, and the IT department, beyond assumed hierarchy.

\\paragraph{\\textbf{Absence of visible behaviour does not indicate absence of risk:}} In Phase 2, Theme 4 (P2-T4), Expert P3-001 reported no personal hesitation in incident reporting. They accepted that unwillingness could arise for others, depending on leadership responses and workplace norms. This distinction is rationally significant; behaviours may persist invisibly within specific roles or units due to contextual shielding, while remaining structurally present across the institution. This finding challenges the assumption that unreported behaviour reflects resolved risk.

\\paragraph{\\textbf{Variation in expert judgement is itself a contribution, not a limitation:}} Expert disagreement highlighted organisational variation and role-specific conditions influencing cybersecurity behaviour rather than undermining the findings. This bounded divergence identified the conditions under which themes intensified, diminished, or shifted across institutions. 

Collectively, these implications advance the body of knowledge by moving beyond constant, policy-centred models of cybersecurity behaviour. They demonstrate that in higher education, behaviour is shaped through interacting conditions, distributed responsibilities, contextual practices, and leadership dynamics that operate simultaneously. An effective cybersecurity strategy must shift from general policies to context-aware implementation. Leadership, systems, and structures require deliberate coordination, not assumed alignment.

\\subsection{Scope and Limits of Expert Validation}  
\\label{sec:7.2.5}  
Phase 3 validation judged whether the Phase 1 and Phase 2 findings were convincing, coherent, and meaningful within HEI practice, not just establishing consensus or generalisability \\citep{Lincoln1985, Miles2014}. Experts were purposively selected from relevant institutional contexts, confirming that informed judgment was grounded in operational experience.

Experts’ doubts or partial agreement and disagreement did not reflect rejection of the findings. Instead, they arose from differences in institutional maturity, role responsibility, and operational constraints. These variations clarified the conditions under which specific themes were more or less applicable. Expert validation defines the scope and boundaries. It strengthens precision without overextending claims.

Accordingly, expert validation functioned to define the scope of the findings. It identified contextual boundaries and strengthened interpretive precision, without extending claims beyond the studied setting. Broader interpretation and theoretical integration of these validated patterns are taken forward in Chapter \\ref{chapter:c8}.

\\section{Summary and Conclusion}  
\\label{sec:7.3}

This chapter presented findings across all three phases, tracing how the understanding of cybersecurity readiness in HEIs developed, deepened and was critically tested at each stage.

Phase 1 established the foundation by identifying five individual-level behavioural themes. These captured how employees formed awareness via incidents, judged threats personally, coped with confidence and effort, enacted policy routines, and relied on leadership for escalation. At this stage, the analysis focused on how individuals interpreted and responded to cybersecurity expectations within their immediate work practices.

Phase 2 extended these findings by moving the analytical lens from the individual to the organisational culture. Eleven themes uncovered how physical environment, leadership decisions, cultural assumptions, governance, and institutional practices shaped and frequently constrained the individual behaviours identified in Phase 1\. Phase 2 showed individual patterns were not purely dispositional. Organisational cultural conditions actively produced or suppressed them. For example, the incident reporting hesitation identified in Phase 1 was clarified in Phase 2 through leadership gaps, embarrassment barriers, and an absent reporting culture. Policy ignorance, similarly, was shown to occur due to governance failures and training disconnection rather than individual negligence alone.

Phase 3 subjected these 16 themes to expert assessment, providing the critical evaluative layer absent from the earlier phases. Seven domain experts assessed importance, clarity, and cross-institutional applicability. This phase did not merely confirm earlier findings; it investigated their boundaries. Expert feedback revealed that while all themes were recognisable across institutions, their intensity and visibility depended on organisational maturity, resource availability, role clarity, and leadership engagement. Cultural misperception interacted with system constraints; onboarding gaps blurred HR-leadership responsibilities; behaviours persisted invisibly in some contexts.

The phases progressed deliberately from individual behaviour to organisational conditions, then to validation and boundary definition. Cybersecurity readiness emerged not as a fixed state but as a context-dependent outcome produced through the interaction of individual, organisational culture, and leadership factors. This refined understanding provides the clear empirical foundation for the integrated framework presented in the subsequent Chapter \\ref{chapter:c8}. 

   
\\chapter{Overall Discussion and Research Contribution}  
\\label{chapter:c8}

\\setcounter{figure}{0}  
\\renewcommand{\\thefigure}{8.\\arabic{figure}}  
% \\setcounter{table}{0}  
% \\renewcommand{\\thetable}{8.\\arabic{table}}

\\section{Introduction}  
\\label{sec:8.1}

The preceding chapters presented empirical findings across three interconnected phases. Phase 1 (Chapter \\ref{chapter:c5}) examined how individual participants interpreted privacy mental models and evaluated cybersecurity threats. Phase 2 (Chapter \\ref{chapter:c6}) explored how organisational culture, governance arrangements, and leadership signals shaped cybersecurity behavioural practices. Phase 3 (Chapter \\ref{chapter:c7}) subjected these findings to expert validation, clarifying their relevance, boundaries, and practical applicability within higher education institutions (HEIs) settings. Together, these phases constructed a layered understanding of cybersecurity readiness that integrates individual, cultural, and governance dimensions beyond isolated structural explanations.

This chapter synthesises findings across the individual and organisational levels and consolidates the study’s theoretical, practical, and methodological contributions. Drawing on the explanatory single case study design, the study explored why specific behaviours and situations appeared, and how individual judgement, leadership, and culture influenced security outcomes.

Building on this overview, first is an integrated interpretation of the phases. This formalises the interactional process underlying cybersecurity readiness and articulates the study's contributions, including theoretical refinements and the final integrated conceptual framework. Practical implications for HEIs follow, along with the methodological contributions and scope of knowledge claims. Figure \\ref{fig:8.1} visually maps the Chapter \\ref{chapter:c8} roadmap. Figure \\ref{fig:8.2} provides an overview sight of the multi-phase research process and contributions.

 

 \\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 8 Roadmap\]{%  
    \\textbf{Figure 8.1}\\\\\[1.2em\]  
    \\textit{Chapter 8 Roadmap.}  
    }  
    \\label{fig:8.1}  
    
    % \\addcontentsline{lof}{figure}{8.1 \\hspace{0.18cm} Chapter 8 Roadmap}  
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures/c8/8.1roadmap.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

   
Figure\~\\ref{fig:8.2} portrayed an integrated overview of the multi-phase research design, demonstrating how empirical findings were gradually developed, connected, and produced into the final conceptual contributions. The figure should be read from left to right, indicating the sequential logic of the study and the sequence of analysis across phases.  
 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Overview of the Multi-Phase Research, Findings and Contribution\]{%  
    \\textbf{Figure 8.2}\\\\\[1.2em\]  
    \\textit{Overview of the Multi-Phase Research, Findings and Contribution.}  
    }  
    \\label{fig:8.2}  
    
    % \\addcontentsline{lof}{figure}{8.2 \\hspace{0.18cm} Overview of the Multi-Phase Research, Findings and Contribution.}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures/c8/8.2 Research Overall.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}

 

The upper left section signifies Phase 1, which was grounded in Protection Motivation Theory (PMT) (see Section \\ref{sec:3.2.2}). This phase began with an initial template (Section \\ref{sec:4.7.2}), which guided data collection and analysis through the six-step template analysis process. The outcome of this phase was the identification of five themes (see Section \\ref{sec:5.2}), capturing how individual privacy mental models shaped cybersecurity behavioural intentions. This phase established the behavioural foundation of cybersecurity readiness.

The lower left section followed Phase 1, illustrating Phase 2\. It extended analysis using Schein's organisational culture framework. Utilising behaviour insights from Phase 1, a second initial template (Section \\ref{sec:4.7.2}) led organisational-level data collection and template analysis. Through iterative coding, eleven themes emerged, describing how organisational culture, leadership practices, governance structures, and learning settings shaped and restrained individual behaviour and action. Analysis shifted from individual intention to organisational cultural influence, showing behaviour embedded in institutional conditions.

The central (right) section signifies Phase 3 expert validation, which judgmentally evaluated the joined findings from Phases 1 and 2\. Rather than functioning as confirmation alone, this refined interpretation identifies relative variation, border conditions, and areas needing conceptual clarification. It ensured that the findings were credible, transferable, and supported in real-world higher education environments.

The top right-hand side offers the final integrated outputs of the study. These include the integrated conceptual framework, mental model characteristics, organisational readiness checklist, and actionable recommendations. Jointly, Individual intentions and organisational culture dynamically interacted to shape cybersecurity readiness.

Figure \\ref{fig:8.2} links Phase 1 (behavioural), Phase 2 (organisational), and Phase 3 (validation) into one explanatory pathway. Each phase builds sequentially, synthesising processes and findings from individual to validated insights.

\\section{Cross-Phase Synthesis}  
\\label{sec:8.2}

\\paragraph{\\textbf{Individual behaviour judgment and privacy reasoning:\\\\} }  
The findings indicate that individual cybersecurity behaviour was influenced primarily by individual participants’ personal judgement in everyday work. Individuals measured effort, relevance, and potential consequences in relation to their immediate responsibilities. 

Individuals judged threats as avoidable or remained silent when consequences felt unimportant and personally unrelatable. This perception reduced motivation for protective behaviours, such as reporting risks or following policies. Risks were acknowledged but rational interpreted as manageable through prior experience, assumed organisational protections, implicitly delegating responsibility and sustaining vulnerability. Threat evaluation was filtered through personal workload and task priorities, with organisational-level consequences often treated as secondary. 

Coping appraisal determined behavioural variation, as protective action depended on perceived capability, confidence in escalation pathways, and the effort required within existing workflows. Participants described ongoing trade-offs between task completion, time pressure, and security compliance. Controls that aligned with routines and felt manageable were more likely to be followed; when response costs grew too high, secure intentions weakened and behavioural drift emerged. 

Leadership visibility further conditioned this process. Participants described leadership and authority support as shaping interpretations of cybersecurity expectations, reinforcing or undermining commitment to secure practices. Expert validation reinforced this interpretation, confirming that awareness alone rarely produces sustained protective behaviour without clear reinforcement.

This indicates that organisations must move beyond awareness-based interventions and instead design support mechanisms that reduce effort, clarify responsibility, and embed security into everyday workflows.

\\paragraph{\\textbf{Organisational Culture and Leadership Influence:\\\\} }  
Individual reasoning was influenced by organisational signals on seriousness, urgency, and legitimacy. Cultural artefacts, values, underlying assumptions, leadership action, and governance arrangements collectively shaped whether cybersecurity was treated as core or marginal to institutional work. Where policies lacked reinforcement, values remained uncertain, and leadership showed hesitation or inconsistency, a disconnect emerged between awareness and behavioural action.

Organisational structures further influenced how individuals interpreted their responsibilities. Fragmented onboarding, uneven training enforcement, compliance fatigue, and emotional barriers to reporting created conditions in which secure behaviour required additional effort and confidence. Under such conditions, staff justified minor bypasses as practical adjustments to maintain productivity, which gradually led to major organisational risks. Moreover, repetitive security notifications or warnings and common training created compliance fatigue. Participants found the content irrelevant to their actual work, viewing it as a waste of time rather than meaningful learning. 

Also, social embarrassment emerged as a major obstacle to incident reporting. Participants avoided admitting incidents to evade perceptions of carelessness or incompetence among peers. Unspoken social norms restrained openness, thereby amplifying vulnerabilities. Likewise, Individuals relied on personal morals as ethical grounds to resolve conflicts between their actions and organisational decisions. Some shared religious beliefs over organisational policy practices.

Additionally, leaders dissatisfied with the authoritative protective systems unintentionally conveyed low priority through inconsistent support, allowing behavioural drift. Similarly, policies appeared difficult, unappealing, or unnecessary, low visibility and poor usability provoked ignorance over formal compliance. 

This demonstrated that organisational culture must be actively enacted through leadership behaviour, clear communication, and usable policies, as passive policy presence alone does not produce secure practice.

\\paragraph{\\textbf{Cybersecurity Readiness as Cross-Level Dynamic:\\\\}}  
Synthesised across three phases, cybersecurity readiness in HEI emerged as a relational outcome. Individual judgment deliberately influenced privacy behaviour intentions based on personal risk understanding, coping or reporting effort, and responsibility. Organisational culture conditioned whether those objectives were reinforced, delayed, or overridden. Leadership cues, governance clarity, and accountability practices aligned individual reasoning with institutional policy expectations. Conversely, workload pressures, confusing authority contacts or feedback pathways, and weak reinforcement raised response costs and encouraged selective compliance.

Expert validation reinforced this interpretation by confirming that readiness was rarely a matter of individual failure or technical deficiency alone. It reflected alignment or misalignment between employee judgment and organisational cultural conditioning. Readiness thus depended on cross-level coherence: aligned mental judgements and cultural signals routinised secure behaviour; misalignment created vulnerability even among motivated employees.

This implies that effective cybersecurity readiness strategies must address behavioural, cultural, and structural factors simultaneously, ensuring alignment across individual actions, leadership practices, and organisational systems.

\\section{Theoretical Contributions}  
\\label{sec:8.3}  
This study advances theoretical understanding of cybersecurity readiness by explaining how individual security reasoning and organisational culture jointly shape behaviour in higher education institutions. Building on the integrated interpretation presented earlier, this section formalises the study’s conceptual contributions. Specifically, as a novel contribution, the research identified 13 mental model characteristics that describe recurring cognitive orientations and action tendencies shaping cybersecurity decision-making. Cross-phase analysis demonstrated that these characteristics operated consistently across roles and organisational levels, while interacting with cultural beliefs and governance structures.

The section then demonstrates how these characteristics extend Protection Motivation Theory by clarifying how threat and coping appraisal are interpreted through situated cognitive orientations. It further refines Schein's organisational culture model by specifying how cultural assumptions, leadership signalling, and governance activation condition cybersecurity behaviour in practice. Drawing on cross-phase synthesis and expert validation, the section presents the integrated conceptual framework as the central theoretical advancement of the thesis, clarifying its novelty, scope, and explanatory significance.

\\subsection{Mental Model Characteristics Contribution}  
\\label{sec:8.3.1}

This research contributes theoretically through an integrated frame of 13 mental model characteristics (Figure\~\\ref{fig:8.3}). It defines how individuals perceive, evaluate, and respond to cybersecurity threats in higher education, synthesising through multi-phase analysis. These characteristics were not treated as purely individual phenomena. Instead, they were derived from the full three phase interview dataset, showing how personal reasoning (Phase 1\) interacted with organisational culture and norms (Phase 2), and how the boundaries and practical significance of these mindsets were confirmed through expert validation (Phase 3).

Mental models are illustrations of reality that help individuals reason, predict, and explain approaches \\citep{Park1995, Saucier2025}. They create stable patterns that outline what individuals notice, trust, find feasible, or avoid \\citep{Reeves2025}. The empirical value of these thirteen characteristics explains why the general policies, common training, and strict controls produced uneven readiness outcomes across organisational units and roles. Readiness varied because individuals carried different mindsets into identical conditions, and those attitudes were amplified or weakened by cultural signals, leadership responses, and workload settings \\citep{Balozian2017}.

A security mindset advances uniformly positive cybersecurity attitudes that shape broader values, choices, and safer behaviours, reducing negative security experiences \\citep{Dutton2017}. They are consolidated in Table \\ref{tab:8.1} and Table \\ref{tab:8.2} as the main empirical output of the study. Each characteristic is framed as a cross-phase mindset; these are linked to research findings and behavioural effects. 

This set of mindset (Figure \\ref{fig:8.3}) shows how participants viewed cybersecurity risk, responsibility, effort, and security action. Attributes illustrate how people grasped privacy as individual responsibility. Culture influences views on controls for access and data handling \\citep{Schoenmakers2023}. They occur across individual interviews, organisational accounts, and expert views, shaped by experience, workload, leadership, trust, and support. The following parts briefly elaborate on each characteristic using direct empirical evidence to demonstrate its support in the data.

This character orientation aligns explicitly with the research themes (Table \\ref{tab:8.1}) and is indicated by multiple-phase participants (see Table \\ref{tab:8.2}). The thirteen mental model characteristics are defined as follows:

\\begin{itemize}  
    \\item \\textbf{{The Experiential Learner:}} interprets cybersecurity risk primarily through personal exposure to incidents, resulting in reactive behaviour and uneven readiness where learning depends on prior harm rather than preventive engagement. Research participants interpreted cybersecurity risk understanding primarily through prior experience and personal exposure to incidents. This resulted in reactive behaviour and uneven readiness.

 % \\item \\textbf{Delegated Responsibility/ Responsibility Delegator:}

      
    \\item \\textbf{The Responsibility Delegator:} assigns primary accountability for cybersecurity to institutional systems or IT units, reducing individual initiative and weakening distributed responsibility across the organisation. A recurring mindset involves the assumption that cybersecurity is primarily the organisation’s responsibility. Managers and regular employees avoid cybersecurity responsibility by externalising issues, reflecting limited attribution differences across roles.  
      
    \\item \\textbf{The Vigilant Verifier:} relies on personal judgement to independently assess threat legitimacy, strengthening individual detection capacity but risking inconsistency where institutional guidance is overlooked. Individuals prioritise personal cues over institutional protocols, enhancing threat detection yet risking inconsistencies.  
      
    \\item \\textbf{The Overwhelmed Avoider:} interprets cybersecurity tasks as too complex or time-consuming; when feeling incapable, disengaged, and leaving risks unaddressed. Participants frequently avoided encryption and secure data sharing or transfer. These exemplify avoidant underscoring the need for leadership training on systemic factors rather than their unbalanced attribution styles due to exhaustion, highlighting the need for leadership training on systemic factors over individual blame.  
      
    \\item \\textbf{The Pragmatic Trade-off Maker:} balances security demands against workload and productivity pressures, leading to conditional compliance when response costs are perceived as excessive. Heightened cost-benefit coping tipped balances toward shortcuts, thereby undermining institutional safeguards. Under workload pressure, task completion is over strict time, adapting behaviour through self-awareness skills to assess performance and cope collaboratively.  
      
    \\item \\textbf{The Ethical Complier:} moral convictions drive consistent compliance, independent of monitoring or rewards. Ethical compliers integrate ethical, moral, human, and social values into cybersecurity decisions, applying care ethics to recognise emotions in problem-solving, tailor empathetic responses, and promote fairness and societal well-being from the outset.  
      
    \\item \\textbf{The Embarrassment-Averse Reporter:} avoids incident disclosure due to fear of reputational judgment, delaying organisational response and limiting collective learning. Fear of embarrassment develops as a significant obstacle to incident reporting. Concern about reputational damage and peer judgment often leads to silence, including fear links to privacy disclosure or mishandling, rather than early escalation. Where psychological safety is weak, this sensitivity to social evaluation suppresses learning from incidents and delays organisational response.  
      
    \\item \\textbf{The Leadership-Dependent Follower:} adjusts security behaviour according to visible leadership demonstration and reinforcement, creating variability in readiness depending on leader engagement. Leadership tone influences observational learning and sets organisational cultural norms. Clear leadership provides essential guidance, cues, policy clarity, and communication that help adjust behaviours and align organisational cybersecurity postures effectively. Absence of clear role-modelling induces hesitation and weakens self-efficacy; consistent cultural signals are embedded in a protective culture institution-wide.  
      
    \\item \\textbf{The Training-Detached Completer:} treats mandatory cybersecurity training as procedural compliance rather than behavioural development, weakening the long-term impact of awareness initiatives. Training fatigue and disengagement have been widely reported. Mandatory modules generate superficial engagement, prioritising box-ticking over behavioural change. Infrequent reinforcement and irrelevant content further diminished perceived training value, perpetuating minimal compliance.  
      
    \\item \\textbf{The Policy-Detached Operator:} recognises the existence of policies but disengages from formal practice, reducing policy activation in daily work. Policies appeared difficult, unappealing, or unnecessary. Low visibility and poor usability reinforce this disinterest, favouring intuitive practices over formal adherence. This detachment notably harms privacy efforts by curbing engagement with rules on data collection, storage, and sharing. Organisational notifications overload intensified detachment, giving policies secondary to practice. Accessible, integrated policy design opposes avoidance by aligning with workflow realities.  
      
    \\item \\textbf{The Relationship-Sensitive Actor:} bases disclosure and compliance decisions on relational trust and psychological safety. Security behaviour has frequently been shaped by trust and interpersonal relationships. Individuals describe disclosure and discussion as dependent on relational safety. A positive employment relationship, reflected in high job satisfaction and perceived organisational support, motivates employees to reciprocate through stronger cybersecurity compliance and more secure everyday computing behaviour. Weak trust interrupts open communication, delaying incident responses. Strong psychological safety enables proactive sharing, enhancing collective vigilance.  
      
    \\item \\textbf{The Restriction-Frustrated Resister:} responds to restrictive or usability-limiting controls with resistance or workaround behaviour, undermining cybersecurity safeguards. Strong frustration emerges around authoritative protection restraints. Usable security tensions lower self-efficacy, amplifying resistance to controls.  
      
    \\item \\textbf{The Compliance-Fatigued Adapter:}  reflects cumulative exhaustion with restriction, poor system practice, and mandatory requirements. Individuals struggle with unclear data privacy policies and controls under daily work expectations. Organisations fixate on compliance checkboxes over genuine security, creating fatigue as regulation lags technology and blinds ethical responsibility. Habituation normalises minimal effort and gradually reduces vigilance. Exhibits reduce vigilance due to repeated exposure to mandatory controls and procedural requirements, normalising minimal compliance over time. Sustained pushback adopts policy ignorance, weakening overall readiness.  
\\end{itemize}

Figure \\ref{fig:8.3} presents the structure of thirteen mental model characteristics identified in this study, which influenced individuals’ understanding of cybersecurity and practice.\\\\

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Cybersecurity Mental Model Characteristics\]{%  
    \\textbf{Figure 8.3}\\\\\[1.2em\]  
    \\textit{Cybersecurity Mental Model Characteristics}  
    }  
    \\label{fig:8.3}  
    
    % \\addcontentsline{lof}{figure}{8.3 \\hspace{0.18cm} Cybersecurity Mental Model Characteristics}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures/c8/8.3 Character.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
 

   
 

Table \\ref{tab:8.1} presents connections between mental model characteristics and links to multiple themes where these characteristics are observed; this provides supporting evidence for the research findings and characteristics' contributions.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{3cm} p{5cm} p{5.5cm}}

\\caption\[Mental Model Characteristics and Supporting Evidence\]{%  
\\\\\[1.2em\]  
\\textit{Mental Model Characteristics and Supporting Evidence}  
\\label{tab:8.1}  
}  
\\\\

\\hline  
\\textbf{Characteristic} & \\textbf{Explanation} & \\textbf{Linked Themes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Characteristic} & \\textbf{Explanation} & \\textbf{Linked Themes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Experiential Learner & Learns cybersecurity importance only after personal incident exposure. & Physical Symbolism and Security Culture Blind Spots (P1-T1) \\\\ \\hline

Responsibility Delegator & Assumes cybersecurity is IT’s or the organisation’s job, not individuals. & Balancing Confidence, Capability, and Costs in Coping Strategies (P1-T3); Leadership Lag in Onboarding Cybersecurity Policy (P2-T8) \\\\ \\hline

Vigilant Verifier & Checks indicators and verifies legitimacy independently, ignoring organisational instructions. & Balancing Confidence, Capability, and Costs in Coping Strategies (P1-T3) \\\\ \\hline

Overwhelmed Avoider & Feels under-skilled or overwhelmed and avoids complex security tasks & Assessing and Mitigating Threats Through Awareness and Consequence Management (P1-T2); Assumptive Resistance Loops Undermining Cybersecurity Readiness (P2-T3) \\\\ \\hline

Pragmatic Trade-off Maker & Prioritises efficiency over security due to time stress and workload, passing security tasks to others if needed. & Balancing Confidence, Capability, and Costs in Coping Strategies (P1-T3) \\\\ \\hline

Ethical Complier & Acts securely based on professional or moral responsibility, independent of enforcement. & Organisational Values Are Not Reflected in Daily Leadership Decisions (P2-T2) \\\\ \\hline

Embarrassment-Averse Reporter & Avoids reporting incidents due to fear of judgment or reputational harm. & Experiential Trust Threshold in Incident Reporting (P2-T4); Security Culture Embarrassment Barrier (P2-T7) \\\\ \\hline

Leadership-Dependent Follower & Security behaviour depends on visible leadership modelling, communication and follow-through. & Addressing Gaps in Leadership and Authority (P1-T5); Leadership and Behavioural Dynamics Influencing Cybersecurity Culture (P2-T10) \\\\ \\hline

Training-Detached Completer & Views cybersecurity training as repetitive, generic, and irrelevant to work; does it just to comply. & Cybersecurity Awareness and Training Effectiveness (P1-T1) \\\\ \\hline

Policy-Detached Operator & Sees policies as available but ignores them, finds them unengaging or disconnected from regular work. & Ignorance Towards Policy (P2-T11) \\\\ \\hline

Relationship-Sensitive Actor & Security action depends on trust and feeling safe with leaders or peers. & Leadership and Behavioural Dynamics Influencing Cybersecurity Culture (P2-T10) \\\\ \\hline

Restriction-Frustrated Resister & Experiences security controls as obstructive, which triggers resistance and workarounds. & Strategic Weakness in Security Governance in Academia (P2-T9) \\\\ \\hline

Compliance-Fatigue Adapter & New system implementation, mandatory modules, and extra steps drain attention and slowly normalise ignorance and resistance. & End-User Behavioural Drift and Compliance Fatigue (P2-T5); Strategic Weakness in Security Governance in Academia (P2-T9) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

Table \\ref{tab:8.2} presents the characteristics of the mental model alongside supporting sample quotations drawn directly from participant interviews across both phases (See details quotations in Appendix\~\\ref{appendix:G}). These quotations illustrated how each characteristic manifested in real organisational settings, independent of participant role or seniority level. The inclusion of participant voices served to ground the mental model in lived experience, strengthening its empirical credibility and demonstrating its applicability across diverse institutional contexts.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.5cm} p{8.2cm} p{3.3cm}}

\\caption\[Characteristics: Supported Participants and Sample Quotations\]{%  
\\\\\[1.2em\]  
\\textit{Characteristics: Supported Participants and Sample Quotations}  
\\label{tab:8.2}  
}  
\\\\

\\hline  
\\textbf{Characteristic} & \\textbf{Characteristic Supporting Sample Quotations} & \\textbf{Supported Participants} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Characteristic} & \\textbf{Characteristic Supporting Sample Quotations} & \\textbf{Supported Participants} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
Experiential Learner & \`\`My previous working experience helped me to shape my behaviour definitely, so that’s why I am not using reading all these policies.'' (P1-006) & P1-002, 006; \\newline P2-001; \\newline P3-001, 003 \\\\ \\hline

Responsibility Delegator & \`\`I trust that the \[organisation\] tools and software I use have built-in privacy and encryption technologies'' (P1-002) & P1-001, 002, 004; \\newline P3-002 \\\\ \\hline

Vigilant Verifier & \`\`First thing will be as I have mentioned, how badly affected I am. I shall assist that first. If I am not affected then I will not bother about this.'' (P1-006) & P1-001, 004, 006; \\newline P3-001 \\\\ \\hline

Overwhelmed Avoider & \`\`I have to switch to something which is more convenient'' (P1-004). \\newline \`\`There’s so much training... and yet it’s mandatory.'' (P2-001) & P1-004; \\newline P2-001; \\newline P3-002, 004 \\\\ \\hline

Pragmatic Trade-off Maker & \`\`We are busy, very busy... it is also required, but also wasting time, when describing training and phishing controls.'' (P2-007). & P1-007; \\newline P2-002, 005; \\newline P3-001, 002, 004, 006 \\\\ \\hline

Ethical Complier & \`\`I think it almost comes out of common sense'' (P1-005) \\newline \`\`I usually go for ethical things'' (P1-007). & P1-005, 007; \\newline P2-007 \\\\ \\hline

Embarrassment-Averse Reporter & \`\`If they are the source of a security breach, \[they\] would be very embarrassed'' (P2-002) & P2-002; \\newline P3-001, 002, 004, 006, 007 \\\\ \\hline

Leadership-Dependent Follower & \`\`It will be more efficient if we can just get the directions directly from our supervisor'' (P1-001). & P1-001, 004, 006; \\newline P2-005, 006; \\newline P3-001, 002, 003, 004, 005 \\\\ \\hline

Training-Detached Completer & \`\`It’s really for us. It’s a box-ticking exercise at that time, and it’s boring'' (P2-002) & P1-002, 003, 004, 005, 006; \\newline P2-001, 002; \\newline P3-001, 002, 003, 006, 007 \\\\ \\hline

Policy-Detached Operator & \`\`They’re just... not great fun reading'' (P1-005). & P1-001, 002, 004, 005, 006, 007; \\newline P2-002, 005, 008; \\newline P3-001, 002, 004, 005, 006, 007 \\\\ \\hline

Relationship-Sensitive Actor & \`\`It depends on the trust'' (P1-001) \\newline \`\`The relationship that you have with your team \[management\]... does impact our cybersecurity'' (P2-003). & P1-001, 005; \\newline P2-002, 003, 004, 005; \\newline P3-001, 004 \\\\ \\hline

Restriction-Frustrated Resister & \`\`They gave me a computer, which has just turned into a paperweight on my desk. I don’t use it because I can’t…. This policy that essentially, no one has given administrative rights on their computer… I don’t understand it. It doesn’t make any sense to me… I think it’s an unnecessary restriction'' (P2-004) & P2-003, 004, 005, 007; \\newline P3-001, 003 \\\\ \\hline

Compliance Fatigue & \`\`Rather than making it mandatory, this could be optional, and the user will select if it is required.'' (P2-007) & P1-001, 006; \\newline P2-001, 005, 007; \\newline P3-001, 002, 005, 007 \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

   
   
Taken together, these thirteen mental model characteristics clarify how cybersecurity readiness is cognitively filtered before it becomes organisational practice. They explain why system controls, policies, and training involvement produced conflicting behavioural outcomes across roles and units. Readiness was not determined solely by knowledge or governance design, but by how responsibility, effort, trust, authority, and risk were interpreted through these recurring orientations. Some characteristics stabilise protective behaviour, others weaken or delay it, and several operate conditionally depending on leadership signals and workload context. Collectively, these characteristics form a cross-level interpretive layer linking individual reasoning to cultural reinforcement. These explain irregular cybersecurity understanding into sustained readiness. Leaders, managers, and supervisors can diagnose team patterns, identify gaps, and design targeted interventions aligning training, policy, and support with user behaviour.  
 

\\subsection{Extending Protection Motivation Theory}  
\\label{sec:8.3.2}

This study extends Protection Motivation Theory (PMT) by demonstrating that knowledge and experience, threat and coping appraisal operated within organisational conditions. This assessment is shaped by lived experience, leadership signals, workload difficulty, and perceived institutional support. Severity and vulnerability became behaviourally meaningful when risks felt immediate and role-relevant. Self-efficacy and response efficacy depended on visible guidance and credible escalation pathways. Response cost emerged as a structurally conditioned judgement influenced by process complexity and competing priorities.

To support this extension, Figure \\ref{fig:8.4} presents the original PMT structure used in this study, while Figure \\ref{fig:8.5} illustrates the extended model developed in this research.\\\\

\\begin{figure}\[\!ht\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Adapted Protection Motivation Theory (PMT)\]{%  
    \\textbf{Figure 8.4}\\\\\[1.2em\]  
    \\textit{Adapted Protection Motivation Theory (PMT)}  
    }  
    \\label{fig:8.4}  
    
    % \\addcontentsline{lof}{figure}{8.4 \\hspace{0.18cm} Adapted Protection Motivation Theory (PMT)}  
      
    \\includegraphics\[width=0.5\\linewidth\]{Figures//c2/2.2PMT.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{Note.} PAM Adapted From "Protection motivation theory in predicting intention to engage in protective behaviors against schistosomiasis among middle school students in rural China" , by, \\citet{Xiao2014}, PLoS Neglected Tropical Diseases, Volume(8), p. 03\. (https://doi.org/10.1371/journal.pntd.0003246).  
    \\end{minipage}  
\\end{figure}

Figure \\ref{fig:8.4}  represents the baseline PMT structure, where behavioural intention is explained primarily through individual threat and coping appraisal. However, the findings of this study indicate that this structure does not sufficiently account for organisational conditions influencing decision-making. In particular, the absence of clear guidance, leadership reinforcement, and accessible support creates gaps between intention and action. This limitation informs the development of the extended model presented in Figure \\ref{fig:8.5}, where 'Insufficient Support' is introduced as a critical contextual factor shaping behavioural intention.

 

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Extended Protection Motivation Theory (PMT)\]{%  
    \\textbf{Figure 8.5}\\\\\[1.2em\]  
    \\textit{Extended Protection Motivation Theory (PMT)}  
    }  
    \\label{fig:8.5}  
    
    % \\addcontentsline{lof}{figure}{8.5 \\hspace{0.18cm} Extended Protection Motivation Theory (PMT)}  
      
    \\includegraphics\[width=\\linewidth\]{Figures//c8/8.4\_improvedPMT.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}   
    \\end{minipage}  
\\end{figure}

This study extends Protection Motivation Theory (PMT) by demonstrating that knowledge and experience, threat and coping appraisal operate within organisational conditions. This assessment is shaped by lived experience, leadership signals, workload difficulty, and perceived institutional support. Severity and vulnerability have become behaviourally meaningful when risks are felt immediate and role-relevant. Self-efficacy and response efficacy depend on visible guidance and credible escalation pathways. Response cost has emerged as a structurally conditioned judgement influenced by process complexity and competing priorities.

Leadership functioned as a key moderator in these evaluations. Clear messages, visible role-modelling, and supportive responses induced self-efficacy and response efficacy, whereas silence or mixed signals reduced intention and slowed action \\cite{DextrasGauthier2023, Kaptein2011}. Leadership is framed here as part of the motivational setting for PMT, outside influence on behaviour \\cite{DextrasGauthier2023}. This refines PMT by showing that its core constructs work through organisational relationships and everyday practices.

A further theoretical contribution is the identification of \\textit{insufficient support} as a critical moderating factor influencing behavioural intention. Phase 1 (Theme P1-T5) revealed that unclear authority pathways, limited supervisory engagement, and delayed guidance elevated perceived effort and uncertainty (see Section\~\\ref{sec:5.3}). When individuals lacked timely reinforcement or accessible assistance, coping appraisal weakened even where awareness and motivation were present. Insufficient support therefore functioned as a destabilising influence on intention formation within PMT's behavioural motivational process.

The study reframes PMT as an organisationally embedded model; individual perceptions and organisational reinforcement activate or constrain its motivational constructs. Behavioural intention is strongest when efficacy beliefs are aligned with structural support and leadership clarity. Where support was fragmented, threat recognition did not consistently translate into protective action. This clarification strengthens PMT’s explanatory power in higher education cybersecurity settings.

\\subsection{Refining Schein’s Organisational Culture Model}  
\\label{sec:8.3.3}

The study utilises Schein's organisational culture model to explain how visible and functional artefacts, including notifications, posters, policy documents, onboarding processes, and guidance, shape cybersecurity behaviour \\citep{Adamu2025, alshaikh2020}. Values such as sincerity and efficiency frequently conflict with security constraints, particularly where leadership prioritises quickness over control \\citep{Cheng2022, ulven2021}. At a deeper level, underlying assumptions, involving reliance on workarounds, embarrassment in reporting incidents, and identified institutional protection, influence how individuals assess and react to risk. These assumptions often influence behaviour more strongly than policy or rules \\citep{Balozian2017, Dimitrov2013}.

The study operationalises Schein's cultural layers through measurable conditions: leadership visibility, engagement, onboarding reliability, and incident response tone \\citep{alshaikh2020, DaVeiga2020, Sutton2025}. These explain cultural presentation in practice and varying policy outcomes across units. 

To clarify this refinement, Figure \\ref{fig:8.6} presents the original Schein model, illustrating the three-layer cultural structure. Figure \\ref{fig:8.7} presents the extended model developed in this study. The figures should be read comparatively. While Figure \\ref{fig:8.6} represents the original culture theory structure, Figure \\ref{fig:8.7} demonstrates how leadership, governance, behavioural conditions, and social factors actively shape and influence these layers in practice.

\\begin{figure}\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Adopted Edgar Schein's Model of Organisational Culture\]{%  
    \\textbf{Figure 8.6}\\\\\[1.2em\]  
    \\textit{Adopted Edgar Schein's Model of Organisational Culture Theory.}  
    }  
    \\label{fig:8.6}  
    
    % \\addcontentsline{lof}{figure}{8.6 \\hspace{0.18cm} Adopted Edgar Schein's Model of Organisational Culture Theory}  
      
    \\includegraphics\[width=0.3\\linewidth\]{Figures//c2/2.3Schein.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{Note.} Schein Model Adopted From "Organizational Culture and Leadership, 3th Edition" (p.26), by\~\\citet{Schein2004}, (https://www.google.com.au/books/edition/Organizational\\\_Culture\\\_and\\\_Leadership/K96qDQAAQBAJ).   
    \\end{minipage}  
\\end{figure}

Figure \\ref{fig:8.7}, the extended model introduces four key factor groups: leadership and authority influence, governance and structural conditions, behavioural and operational constraints, and social and psychological factors. These factors do not replace Schein's layers but interact with them, explaining how cultural meaning is translated into behaviour. Leadership shapes how values are interpreted, governance structures influence how artefacts are implemented, behavioural conditions affect the feasibility of compliance, and social factors shape underlying assumptions

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Extended Schein's Model of Organisational Culture Theory\]{%  
    \\textbf{Figure 8.7}\\\\\[1.2em\]  
    \\textit{Extended Schein's Model of Organisational Culture Theory.}  
    }  
    \\label{fig:8.7}  
    
    % \\addcontentsline{lof}{figure}{8.7 \\hspace{0.18cm} Extended Schein's Model of Organisational Culture Theory}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c8/8.7\_improvedSchein.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}     
    \\end{minipage}  
\\end{figure}

A further refinement is the inclusion of behavioural outcomes, showing how artefacts, values, and assumptions collectively influence cybersecurity behaviour and organisational readiness. This addresses a limitation in Schein's model, which explains cultural structure but does not explicitly present how behaviour emerges from that structure (see Chapter \\ref{chapter:c6}).  
   
The study extends Schein's framework within a digital governance context, referring to the structures, policies, decision-making processes, and clear responsibility structures through which cybersecurity responsibilities are managed within the organisation. It demonstrates that cultural assumptions alone do not determine behaviour. Cybersecurity intention becomes a sustained organisational practice only when cultural layers align with leadership signals, structural support, governance clarity, and everyday working conditions.

Researchers can apply this refined model to study organisational culture as a multi-level system shaping cybersecurity behaviour. It structures the integration of cultural theory with leadership, governance, and behavioural factors. Future work may test interactions across maturity, resources, and complexity levels.

 

\\subsection{Integrated Conceptual Framework}  
\\label{sec:8.3.4}

This study spreads theoretical understanding of cybersecurity readiness by integrating a framework for how individual security rationality and organisational culture jointly shape behaviour in higher education institutions. By integrating PMT with Schein’s model of organisational culture, the research moves beyond explanations that treat cybersecurity behaviour as either an individual mental problem or a compliance issue driven by policy alone. Instead, it displays how individual assessment processes are continuously influenced, reinforced, or weakened by cultural settings, leadership behaviour, and institutional practice \\citep{Georgiadou2022, Herath2009, Schein2017}.

At the individual level, mental model characteristics shape how threat and coping appraisal are interpreted. These orientations influence intention formation under varying workload and support conditions \\citep{Barruga2025}. And at the organisational level, artefacts, values, and assumptions conditioned whether intentions were reinforced or undermined. Leadership signals operated as the connector across all organisational levels. Finally, in Phase 3, expert validation confirmed the model’s boundary conditions. Workload intensity and distributed authority conditioned response cost and behavioural consistency.

The framework demonstrates that usual policies produced different outcomes because readiness depended on alignment, not just organisational instruction. It offers a structured explanation of why behaviour varied across units within the same institution. This integration represents the thesis's central theoretical advancement. It links mental behaviour and culture through a cross-level link grounded in empirical evidence.

Figure \\ref{fig:8.8} visualises the integrated final conceptual framework developed in this study. It presents the interaction between individual mental judgment processes and organisational cultural conditioning as a connected system. Mental model characteristics influence how threat and coping constructs were interpreted, while artefacts, values, leadership engagement, and underlying assumptions determine whether behavioural intention persisted or faded. The framework also highlights insufficient support and workload intensity as cross-level moderating influences. It illustrates that cybersecurity readiness emerged from alignment across cognitive judgment and cultural reinforcement within HEIs.

The framework is organised as a step-by-step process linking individual behaviour, organisational context, and validated outcomes. \\textit{Step 1} evaluates individual mindsets, identifying how mental model characteristics structure cybersecurity behavioural intentions (see Chapter \\ref{chapter:c5}). \\textit{Step 2} translates behaviours into organisational context, showing how culture, leadership, governance, and social conditions influence action(see Chapter \\ref{chapter:c6}). In\~\\textit{Step 3} uses expert validation to confirm findings' relevance and clarify boundary conditions across HEI contexts (see Chapter \\ref{chapter:c7}). Finally,\~\\textit{Step 4} operationalises the framework through two practice-oriented assessment tools proposed by this study (Chapter \\ref{chapter:c8}). Mental Model Characteristics identifies cognitive patterns, privacy views, and gaps for understanding individual mindset as well as gaps. Readiness Checklist assesses leadership, governance, social behavioural, and cultural alignment between policies, practice and assumptions. These steps create a pathway from theory to practice. Organisations assess readiness, identify gaps, and prioritise improvements, making the framework robust and usable in higher education.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Final Integrated Conceptual Framework for Cybersecurity Readiness\]{%  
    \\textbf{Figure 8.8}\\\\\[1.2em\]  
    \\textit{Final Integrated Conceptual Framework for Cybersecurity Readiness in Higher Education}  
    }  
    \\label{fig:8.8}  
    
    % \\addcontentsline{lof}{figure}{8.8 \\hspace{0.18cm} Final Integrated Conceptual Framework for Cybersecurity Readiness in Higher Education}  
      
    \\includegraphics\[width=1.1\\linewidth\]{Figures//c8/8.8FinalFramework.png}  
          
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
 

 

\\section{Practical Contributions}  
\\label{sec:8.4}

The preceding sections demonstrate that cybersecurity readiness in higher education is shaped by empirically validated mental model characteristics and organisational cultural conditions. These findings explain why formal policies, training programmes, and technical safeguards did not produce secure behavioural outcomes across units and roles. This section translates those insights into practical institutional application.

The practical contribution of this study consists of three interconnected outputs. First, it operationalises the mental model characteristics as an evaluative lens for organisational use. Second, it develops a structured cybersecurity readiness checklist grounded in cross-phase evidence. Third, it proposes targeted organisational recommendations derived directly from the observed behavioural and cultural mechanisms. Together, these outputs are designed to assist organisations in assessing current conditions, identifying support gaps, and aligning interventions with actual reasoning patterns present within teams and overall cybersecurity readiness. 

\\subsection\[Operationalising Mental Model Characteristics\]{Operationalising Mental Model Characteristics for Organisational Assessment}  
\\label{sec:8.4.1}

Although the thirteen mental model characteristics are analytically derived, their significance extends beyond theoretical explanation. They provide a clear means for organisations to understand how employees interpret responsibility, effort, authority, and risk in everyday work. The findings imply that behavioural weaknesses often reflect misalignment between mindset and structural conditions, not individual negligence.

Each characteristic is reformulated into scenario-based diagnostic prompts that could be used during induction discussions, team reflections, or supervisory review conversations (see Appendix\~\\ref{appendix:G}). These cues support structured dialogue about responsibility ownership, perceived effort, leadership visibility, usability friction, and confidence in reporting pathways. The approach shifts attention from enforcement to understanding, allowing leaders to provide support suited to prevalent reasoning patterns within a team.

This operationalisation reflects the cross-phase findings. Individual intention formation is influenced by perceived feasibility and support. Organisational signals amplified or weakened individual behavioural intention. The evaluative tool enables proactive structural interventions reducing reliance on repeated compliance reminders. Full evaluatiosn tools guidance appears in Appendix\~\\ref{appendix:G}.

 

\\subsection{Cybersecurity Readiness Checklist}  
\\label{sec:8.4.2}

 Building on this operational lens, the study develops an organisational cybersecurity readiness checklist \\citep{Mortazavi2019, Rajamaki2024, Sabillon2024}. The checklist is derived from the thematic findings and mental model analysis. It is designed to enable institutions to assess their current cybersecurity readiness status using observable organisational indicators.

The checklist translates qualitative evidence into reviewable conditions. It captures structural vulnerabilities such as responsibility delegator , policy detachment, training disengagement, elevated response cost, and compliance fatigue. It also identifies enabling factors, including leadership visibility, clarity of authority pathways, psychological safety for reporting, and workflow-integrated security guidance.

Evidence across the dataset demonstrates that readiness gaps rarely reflected a single technical deficiency. They emerged from unclear data privacy, device security and ownership, inaccessible policies at decision points, excessive procedural burden, and weak reporting confidence. 

To improve usability, the checklist is refined into a concise set of 18 diagnostic questions (see Appendix \\ref{appendix:G}, each mapped to the study's thematic outcomes. The questions are written in simple, non-technical language so they could be understood by both technical and non-technical staff. In practice, organisations respond to each item using a three-point scale (Yes, Partly, No), allowing rapid judgment without requiring a full audit. A sample of the checklist is presented in this section (Table \\ref{tab:8.3}), while the complete version is provided in Appendix \\ref{appendix:G}. \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{4cm} p{8.5cm}}

\\caption\[A sample of the Cybersecurity Readiness Checklist.\]{%  
\\\\\[1.2em\]  
\\textit{A sample of the Cybersecurity Readiness Checklist.}  
\\label{tab:8.3}  
}  
\\\\

\\hline  
\\multicolumn{2}{p{12.5cm}}{\\textbf{Organisation Cybersecurity Readiness Checklist}} \\\\ \\hline  
\\multicolumn{2}{p{12.5cm}}{\\textbf{1. Awareness / Policy clarity}} \\\\ \\hline  
$\\square$ Yes \\hspace{2pt} $\\square$ Partly \\hspace{2pt} $\\square$ No & Are cybersecurity expectations clearly explained for different roles so staff understand what is required in their daily work? \\\\ \\hline

\\multicolumn{2}{p{12.5cm}}{\\textbf{2. Training / Learning}} \\\\ \\hline  
$\\square$ Yes \\hspace{2pt} $\\square$ Partly \\hspace{2pt} $\\square$ No & Is training based on real work situations and recent incidents so staff can apply what they learn? \\\\ \\hline

\\multicolumn{2}{p{12.5cm}}{\\textbf{3. Risk Awareness}} \\\\ \\hline  
$\\square$ Yes \\hspace{2pt} $\\square$ Partly \\hspace{2pt} $\\square$ No & Do staff understand how cybersecurity risks can affect their work, students, or the organisation? \\\\ \\hline

\\multicolumn{2}{p{12.5cm}}{\\textbf{4. Reporting / Access}} \\\\ \\hline  
$\\square$ Yes \\hspace{2pt} $\\square$ Partly \\hspace{2pt} $\\square$ No & Is it easy for staff to report a cybersecurity issue at the time it happens, without confusion? \\\\ \\hline

\\multicolumn{2}{p{12.5cm}}{\\textbf{5. Confidence / Support}} \\\\ \\hline  
$\\square$ Yes \\hspace{2pt} $\\square$ Partly \\hspace{2pt} $\\square$ No & Do staff feel supported and confident when they need to take action during a cybersecurity issue? \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

%Appndix link (update late)%

\\subsection{Research  Recommendations}  
\\label{sec:8.4.3}

This study offers a set of targeted recommendations to strengthen cybersecurity readiness in HEIs \\cite{Mizrak2025, Petric2025}. These recommendations are not generic best-practice statements. They address the specific reasoning patterns and cultural dynamics observed in the research setting.

First, institutions should shift from uniform cybersecurity interventions to targeted readiness strategies, acknowledging distinct mental model characteristics. The findings demonstrate that individuals interpreted responsibility, effort, and privacy risk through stable mindsets such as \\textit{Responsibility Delegator}, \\textit{Pragmatic Trade-off Maker}, or \\textit{Training-Detached Completer}. Applying the same training or policy process across these groups produced uneven outcomes. Effective improvement requires differentiated strategies that clarify ownership, reduce structural friction, and align expectations with real workload conditions.

Second, leadership behaviour must be treated as a primary readiness lever, not a supporting factor. Behavioural intention strengthened when leaders modelled secure practice, reinforced expectations during peak operational periods, and responded constructively to disclosure. Inconsistent reinforcement weakens coping appraisal even when awareness was present. Cybersecurity, therefore, requires visible integration into everyday leadership practice.

Third, process design and usability also influence readiness stability. \\textit{Overwhelmed Avoider}, \\textit{Restriction-Frustrated Resister}, and \\textit{Compliance Fatigue} characteristics show that excessive complexity, fixed controls, and poorly timed conditions encouraged workarounds and disengagement. Readiness improves when secure action is embedded within the routine workflow rather than merely added on top.

Fourth, institutions must actively cultivate mental safety for incident reporting. \\textit{Embarrassment \-Averse Reporter} and \\textit{Relationship- Sensitive} characteristics exhibit that fear of judgment, reputational harm, or relational damage underlying early reporting. This diminishes organisational learning and delayed response. Organisations should create clear awareness of formalised blameless reporting practices and ensure timely response loops that reinforce trust and good relationships with teams and leaders. 

Finally, readiness monitoring requires behavioural indicators beyond policy existence or training completion. The research evidence indicates that awareness measures alone did not reliably predict secure practice. Organisations should associate review and assurance developments with these behavioural indicators, using the checklist to guide prioritisation and track progress over time.

Collectively, these recommendations reframe cybersecurity readiness as an organisational alignment issue grounded in mindset, leadership reinforcement, and practical viability. The study provides institutions with an empirically informed pathway to move beyond compliance visibility toward sustained behavioural consistency.

\\section{Methodological Contribution}  
\\label{sec:8.5}

The research integrates phases sequentially, connecting individual, organisational, and expert perspectives within one bounded case to build, test, and refine an integrated explanation of cybersecurity readiness. This study demonstrates how a sequential qualitative explanatory design can be used to build a collective explanation within a single institutional case \\citep{Miles2014, Neri2024}.

The study's primary methodological contribution lay in using template analysis as a cross-phase analytical framework rather than a single-stage coding technique. Initial coding structures developed in Phase 1 (Chapter \\ref{chapter:c5}) were carried forward into later phases and revised only when supported by consistent evidence. This creates a controlled process for refining interpretation, reducing analytic drift while preserving conceptual continuity across the study.

This approach is methodologically significant because it enabled the analysis to progress systematically from individual reasoning to organisational conditions, and then to expert-validated boundary testing. Template analysis, therefore, supports explanation building across phases, not simply thematic description within separate datasets. This demonstrates how a sequential qualitative analysis can generate a stable yet adaptable interpretive pathway for theory refinement within a single-case cybersecurity study.

A further methodological contribution derived from the systematic integration of cross-phase evidence. Pattern matching, synthesis tables, and alignment tables have been used to link quotations to codes, codes to themes, and themes to explanatory constructs. This strengthens traceability and provides a clear audit trail from claims to participant data across phases. Expert validation in Phase 3 (Chapter \\ref{chapter:c7}) was incorporated only where it converged with earlier evidence, reinforcing methodological restraint and protecting against over-interpretation \\citep{Hibshi2016, Miles2014, Stenfors2020}.

The study also demonstrates how qualitative findings can be translated into practical evaluation tools. The development of mental model characteristics and the organisational cybersecurity readiness checklist illustrates how empirically grounded insights can be operationalised into structured assessment instruments. This represents a methodological extension by bridging qualitative explanation with applied organisational diagnostics, enabling direct use of research outcomes in practice.

Collectively, these methodological contributions provide a structured approach for conducting explanatory qualitative research in complex organisational environments. The study shows that a single-case design can achieve analytical depth, theoretical refinement, and practical applicability when sequential design, coding discipline, and validation processes are carefully aligned.

\\section{Nature of the Knowledge Claim}  
\\label{sec:8.6}

This study generates an explanatory and contextually grounded knowledge claim concerning cybersecurity readiness within higher education institutions. The claim does not propose universal behavioural laws. It advances a structured interpretation of how individual judgment and organisational culture interact within a bounded institutional case.

The integrated framework and mental model characteristics are derived from systematic cross-phase analysis and are supported by convergent participant and expert evidence. This claim is further strengthened through the operationalisation of findings into assessment tools, linking conceptual explanation with practical evaluation. Within a qualitative explanatory case study paradigm, the findings identify persistent cognitive orientations and structural processes that explain inconsistent readiness across organisational units.

Transferability depends on contextual similarity rather than population equivalence. Similar institutions with shared authority, autonomy, and high workloads may recognise these patterns, but local adaptation to policy, regulations and culture remains essential.

The knowledge claim is bounded by the single-institution case, participants' scope, and data collection.  Although not comprehensive across industries, the thirteen mental model characteristics remain stable and strongly supported across all three phases.  

Importantly, the study repositions cybersecurity readiness as requiring alignment between individual mindsets and organisational culture. This claim is further strengthened through the operationalisation of findings into assessment tools, linking conceptual explanation with practical evaluation. Mutual reinforcement creates success; misalignment causes formal policies to fail.

Thus, the thesis advances an empirically grounded, theoretically integrated explanation of cybersecurity readiness in higher education. The contribution extends existing theories by exhibiting how behavioural intention and cultural conditioning interact as an integrated approach. This clarifies processes, conditions, and alignment dynamics rather than deterministic outcomes.

\\section{Chapter Summary}  
\\label{sec:8.7}  
This chapter consolidates the study's integrated explanation of cybersecurity readiness within a HEI. The study presents that readiness does not depend solely on awareness, policy presence, or technical controls. It depends on whether individual judgement is reinforced or weakened by organisational culture and leadership practice.

Thirteen mental model characteristics are identified and validated across phases, clarifying how responsibility, effort, authority, and risk were interpreted in daily work. The integrated conceptual framework formalises this process and refines existing theoretical models by situating motivational appraisal within cultural conditioning.

The chapter translates these insights into applied outputs, including an evaluative lens, a readiness checklist, and evidence-based organisational recommendations. Methodologically, it illustrates how sequential qualitative design and disciplined template analysis support explanatory coherence.

Overall, the chapter illuminates that cybersecurity readiness depends on the consistency between individual decision-making and organisational reinforcement. This consistency is shown to be shaped by leadership, governance structures, behavioural conditions, and social influences operating across levels. The next chapter reflects on the overall implications, limitations, and future research directions.

 

 

 

   
\\chapter{Conclusion and Future Works}  
\\label{chapter:c9}

\\setcounter{figure}{0}  
\\renewcommand{\\thefigure}{9.\\arabic{figure}}

\\section{Introduction}  
\\label{sec:9.1}

The previous chapter presented the integrated interpretation of findings and communicated the study's theoretical, practical, and methodological contributions. It developed the integrated conceptual framework and supported how individual mental models and organisational cultural conditions interact to shape cybersecurity readiness.

This chapter provides a conclusion to the thesis. It synthesised findings on cybersecurity readiness in higher education institutions (HEIs). The synthesis explained their significance for theory, policy, and practice.

Across the three experimental phases (1-3), it was established that cybersecurity readiness could not be grasped through purely technical conditions or awareness consequences alone. Instead, readiness emerged from collaborations between individual privacy reasoning, culture, and organisational governance procedures.

The outcomes clearly illustrated that cybersecurity behaviour was influenced by how individuals understood responsibility, risk, effort, and authority within the workplace. These interpretations affected whether policies were followed, delayed, or bypassed through routine work.

The research further demonstrated that organisational culture and leadership signals greatly guided whether individual intentions changed into consistent cybersecurity behaviour. Where policies required reinforcement, guidance, or operational clarity, employees trusted on personal judgement and unofficial practices.

Consequently, identical policies, systems, and training produced uneven behavioural outcomes across different organisational contexts. Cybersecurity readiness thus reflected organisational alignment of behavioural reasoning, cultural reinforcement, and governance clarity.

This chapter revisited the research aim. It integrated findings from all phases to address the research questions comprehensively. The study then positioned its theoretical, practical, and methodological contributions within existing cybersecurity research. Implications for policy and practice followed. Limitations appeared next, alongside future research directions.

Figure \\ref{fig:9.1} represents this chapter’s structure. It illustrates progression from research evaluation to integrated research question responses, contributions, implications, limitations, and conclusions.

\\begin{figure}\[H\] %\[\!ht\]   
    \\centering  
    \\captionsetup{  
        labelformat=empty,  
        justification=raggedright,  
        singlelinecheck=false,  
        font={stretch=1.3}  
    }  
    \\caption\[Chapter 9 Roadmap\]{%  
    \\textbf{Figure 9.1}\\\\\[1.2em\]  
    \\textit{Chapter 9 Roadmap.}  
    }  
    \\label{fig:9.1}  
    
    % \\addcontentsline{lof}{figure}{9.1 \\hspace{0.18cm} Chapter 9 Roadmap}  
      
    \\includegraphics\[width=0.8\\linewidth\]{Figures/c9/9.1roadmap.png}  
      
    \\begin{minipage}{\\linewidth}  
        \\raggedright  
        \\textit{}  
    \\end{minipage}  
\\end{figure}  
 

   
\\section{Synthesis of Findings Across Research Phases}   
\\label{sec:9.2}  
In this thesis, an analysis was conducted to explore how organisational culture interacted with individuals' mental models of privacy to influence cybersecurity readiness in HEIs. This work addressed the main aim outlined in Chapter \\ref{chapter:c1} (see Section \\ref{sec:1.5}) by \\textit{'examining how organisational culture and individual privacy perceptions influence cybersecurity readiness in higher education institutions'}.

This study evaluated cybersecurity readiness in HEIs. Behavioural reasoning and institutional conditions shaped it as a socio-organisational experience. A three-phase qualitative case study addressed this objective. Each phase examined cybersecurity readiness dimensions and refined the analysis progressively.

\\begin{itemize}  
    \\item \\textbf{Phase 1} examined personal interpretations of privacy, threat, accountability, and effort in cybersecurity choices. Findings indicated behaviour stemmed from subjective assessments rather than policy knowledge alone.   
    \\item \\textbf{Phase 2} analysed how organisational culture, leadership practices, and governance structures influenced behavioural interpretations. Findings indicated institutional norms and governance strongly determined experienced secure practices.   
    \\item \\textbf{Phase 3} evaluated the credibility and transferability of these findings through expert validation interviews. Expert feedback largely confirmed the identified behavioural and cultural patterns and refined several contextual explanations.  
\\end{itemize}

Together, the three phases provided a rational explanation of cybersecurity readiness in HEIs. The design enabled analysis beyond surface behaviour descriptions. It pinpointed organisational conditions influencing safety practices.

Cybersecurity readiness emerged beyond individual behaviour or policy alone. Individual autonomy, cultural reinforcement, and governance interactions shaped it. This reflected higher education's decentralised governance, academic freedom, and trust-based settings.

By maintaining a consistent focus on privacy reasoning and organisational context, the study produced a grounded interpretation of how cybersecurity readiness developed and weakened in practice.

Building on this evaluation, the following section presents integrated responses to the research questions. Each response draws on evidence across all three phases, combining individual behavioural insights, organisational cultural analysis, and expert validation to provide a comprehensive answer.

\\section{Integrated Answer to the Research Questions}  
\\label{sec:9.3}

This section presents integrated responses to the research questions (RQ) addressed in this study:

\\begin{itemize}  
    \\item \\textbf{RQ1:} How do individual mental models of privacy impact individuals' cybersecurity behaviour?  
    \\item \\textbf{RQ2:} How do organisational culture and individual behavioural intentions impact the cybersecurity practice of higher education institutes?  
    \\item \\textbf{RQ3:} How do organisational culture and individual privacy behaviours influence organisational cybersecurity readiness.  
\\end{itemize}

\\subsection\[Individual Mental Models and RQ1\]{Individual Mental Models and RQ1 :}

Phase 1 addressed RQ1 by examining how individual mental models of privacy influenced cybersecurity behavioural intention (Chapter \\ref{chapter:c5}). Five themes were identified and they contributing to answer RQ1 (Table \\ref{tab:9.1}).\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{10cm}}

\\caption\[Phase 1 Themes Addressing RQ1\]{%  
\\\\\[1.2em\]  
\\textit{Phase 1 Themes Addressing RQ1}  
\\label{tab:9.1}  
}  
\\\\

\\hline  
\\textbf{Theme} & \\textbf{Phase 1- Themes Title} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Theme} & \\textbf{Phase 1- Themes Title} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
P1-T1 & Cybersecurity Awareness and Training Effectiveness \\\\ \\hline  
P1-T2 & Assessing and Mitigating Threats Through Awareness and Consequence Management \\\\ \\hline  
P1-T3 & Balancing Confidence, Capability, and Costs in Coping Strategies \\\\ \\hline  
P1-T4 & Proactive and Compliant Cybersecurity Behaviours \\\\ \\hline  
P1-T5 & Addressing Gaps in Leadership and Authority Support \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

The five Phase 1 themes (P1-T1 \- P1-T5) revealed behaviour guidance through daily interpretations. Privacy beliefs framed practical decisions, determining procedure adherence, delay, or bypass under pressure. Participants assessed action practicality, necessity, and environmental support rather than automatic compliance.

Phase 1 themes on awareness and threats (P1-T1 \- P1-T2) showed inconsistent secure behaviour when people lacked coping confidence or saw high effort (P1-T3 \- P1-T4). Coping appraisal also influenced behaviour. Participants adopted secure practices when they felt confident in their ability to respond and when procedures appeared manageable within existing workloads. High effort, uncertainty, or unclear instructions reduced the likelihood of protective behaviour. Behavioural intentions faded when response costs impacted perceived personal benefits. 

Phase 1 also revealed leadership support (P1-T5) as a key mindset. Leadership support further influenced behavioural intention. Where guidance, escalation pathways, and supervisory encouragement were visible, participants reported greater confidence in responding to risks. Unclear or no guidance and support affect activity, confidence, even for risk-aware people. 

Overall, Phase 1 answered RQ1 by establishing that cybersecurity behaviour was driven by feasibility, confidence, and perceived authority. This offered insight into individual intentions, enabling deeper Phase 2 (Chapter \\ref{chapter:c6}) analysis of how organisational culture shapes cybersecurity readiness in HEI.

\\subsection\[Organisational Culture and RQ2\]{Organisational Culture and RQ2 :}  
Phase 2 addressed RQ2 by examining how organisational culture influenced whether individual intentions translated into consistent cybersecurity practice (Chapter \\ref{chapter:c6}). Eleven themes were identified (Table \\ref{tab:9.2}):

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{10cm}}

\\caption\[Phase 2 Themes Addressing RQ2\]{%  
\\\\\[1.2em\]  
\\textit{Phase 2 Themes Addressing RQ2}  
\\label{tab:9.2}  
}  
\\\\

\\hline  
\\textbf{Theme} & \\textbf{Phase 2- Themes Title} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Theme} & \\textbf{Phase 2- Themes Title} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
P2-T1 & Physical Symbolism and Security Culture Blind Spots \\\\ \\hline  
P2-T2 & Organisational Values Are Not Reflected in Daily Leadership Decisions \\\\ \\hline  
P2-T3 & Assumptive Resistance Loops Undermining Cybersecurity Readiness \\\\ \\hline  
P2-T4 & Experiential Trust Threshold and Disengagement in Incident Reporting \\\\ \\hline  
P2-T5 & End-User Behavioural Drift and Compliance Fatigue \\\\ \\hline  
P2-T6 & Cultural Miscalibration in Cyber Risk Perception \\\\ \\hline  
P2-T7 & Security Culture Embarrassment Barrier \\\\ \\hline  
P2-T8 & Leadership Lag in Onboarding Cybersecurity Policy \\\\ \\hline  
P2-T9 & Strategic Weakness in Security Governance in Academia \\\\ \\hline  
P2-T10 & Leadership and Behavioural Dynamics Influencing Cybersecurity Culture \\\\ \\hline  
P2-T11 & Ignorance Towards Policy \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

Phase 2 addressed RQ2 (Chapter \\ref{chapter:c6}) by examining how organisational culture influenced whether individual intentions translated into consistent cybersecurity behaviour. Phase 2 themes (P2-T1 \- P2-T11) showed that Phase 1 intentions became steady only with supportive culture, leadership, and governance. Artefacts and values themes (P2-T1 \- P2-T4) revealed policies, leadership cues, onboarding, and reporting existed but lacked clarity and visibility. When unclear or outdated, individuals relied on subjective assessments and unofficial practices. This undermined institution-wide alignment.

Leadership themes (P2-T2, P2-T8, P2-T10) showed that leaders’ behaviour and follow-through shaped norms. When they reinforced security, clarified roles, and handled exceptions, individual intentions built shared habits. Silence or inconsistency, however, encouraged workarounds and reinforced the behavioural weakness observed in Phase 1 (Chapter \\ref{chapter:c5}).

Fatigue, embarrassment, and governance themes (P2-T5, P2-T7, P2-T9, P2-T11) showed culture reducing motivation over time. Exhaustion dulled focus; humiliation fears blocked reporting; weekly governance structures scattered accountability and constrained individual initiative.

These findings showed that cybersecurity culture turned individual intentions into secure habits only through aligned artefacts, values, leadership cues, and effective governance. Misalignment or assumption pushed efforts back to individual effort, controlling institutional readiness.

\\subsection\[Expert Validation and RQ3\]{Expert Validation and RQ3 :}

Phase 3 addressed RQ3 by examining whether the behavioural and cultural patterns identified in Phases 1 and 2 reflected larger professional experience. Phase 3 drew on expert validation (Chapter \\ref{chapter:c7}) to confirm and refine how behaviours, intentions, and culture drove readiness. It confirmed whether Phase 1-2 patterns exhibited sector-wide relevance in HEIs. Experts largely endorsed Phase 1-2 findings, with minor disagreements or partial agreements (see Sections \\ref{sec:7.2} and \\ref{sec:7.3}). 

Experts highlighted that workload pressure and challenging priorities strongly influenced cybersecurity engagement. High cognitive demand reduced attention to secure action, delayed reporting, and weakened compliance. They also stressed that policy disengagement often resulted from timing, complexity, or poor integration with work routines rather than intentional conflict. These findings confirmed that cybersecurity readiness varied based on the alignment among individual behaviour, organisational culture, and operational conditions.

Importantly, expert validation not only confirmed the findings but also refined their practical application. This process informed the final integrated framework and supported the improvement of the organisational readiness checklist and recommendations, ensuring they are reflective of real-world organisational conditions.

Overall, Phase 3 confirmed that cybersecurity readiness required alignment between individual behaviour, cultural reinforcement, and practical workload conditions. This validation strengthened the credibility of the study’s conclusions and demonstrate relevance beyond the case institution.

 

\\section{Positioning of the Study’s Contributions}  
This study produces theoretical, empirical, and practical contributions that advance the understanding of cybersecurity readiness within HEIs. Chapter \\ref{chapter:c8} presents these contributions in detail. This section positions them within the broader research context.

At a theoretical level, the study includes Protection Motivation Theory (PMT) with Schein's organisational culture model to rationalise cybersecurity readiness in institutional environments. The outcomes demonstrate that behavioural intentions integrated individual threat and coping appraisals with organisational culture, leadership signals, and governance structures. 

The study also extends PMT theory by identifying organisational support as a moderating influence factor on cybersecurity behavioural intention. Where leadership guidance, escalation pathways, and practical support are visible, individuals show stronger confidence in responding to cybersecurity risks. This finding illustrates how motivational processes operated within organisational environments.

Empirically, the study identifies thirteen recurring mental model characteristics shaping how individuals interpret privacy, responsibility, risk, effort, and authority in cybersecurity decisions. These characteristics are observed across phase interviews, organisational analysis, and expert validation. The results provide a structured explanation of how individual reasoning filters institutional policies and influences everyday cybersecurity behaviour.

The research further demonstrates how organisational culture reinforced or weakened these behavioural patterns. Leadership visibility, policy clarity, governance coordination, and operational workload influenced whether secure behaviour became a consistent practice. This evidence clarifies how cybersecurity readiness developed within decentralised higher education environments.

Practically, the study produces an operational lens for evaluating cybersecurity readiness in HEIs. The research introduces a cybersecurity readiness checklist derived from cross-phase evidence and behavioural indicators. The study also provides a practical mental model assessment that organisations can use to evaluate individual cybersecurity thinking, identify mindset gaps, and determine who may need further training or support (Appendix \\ref{appendix:G}). These tools empower institutions to identify organisational misalignment, classify structural barriers, and prioritise targeted improvements.

Collectively, these contributions position the study as an explanatory framework for understanding cybersecurity readiness within HEIs. Rather than universal solutions, this research provides a diagnostic framework. Institutions could integrate behavioural, cultural, and governance factors to strengthen cybersecurity practices.

\\section{Implications for Policy and Practice}  
The findings indicate that cybersecurity governance in HEIs requires stronger alignment between institutional policy expectations and everyday work practices.

Security procedures were most effective when protective actions could be completed quickly within existing workflows. Complex reporting processes or added administrative steps reduced consistent engagement. Institutions should therefore prioritise operational clarity when planning cybersecurity measures. Employee requires clear escalation pathways, simple reporting mechanisms, and visible responsibility structures. Leadership also played a stabilising role in reinforcing security expectations. Visible managerial support clarifies decision authority and encourages employees to address security concerns without hesitation.

The study further suggests that cybersecurity initiatives should consider workload and attention limits. Competing administrative demands frequently displace security tasks, even when individuals recognise potential risks. Universities should therefore treat workload pressure as a governance consideration when designing security programmes, training schedules, and communication cycles. Embedding cybersecurity responsibilities into routine organisational processes strengthened institutional readiness more effectively than relying on periodic awareness campaigns.

\\section{Study Limitations and Future Direction}  
This study adopted a qualitative, multi-phase explanatory case study design to examine cybersecurity readiness as a layered socio-organisational circumstance. The phased structure enabled insight at individual, organisational, and expert levels, while the analytic structure ensured consistency across datasets. Although this approach was effective for developing an in-depth explanation of readiness understanding, several limitations should be acknowledged.

First, the study was conducted within a qualitative single case study. The findings are therefore not meant to support statistical generalisation but theoretical transferability. Future research could extend this work through comparative multi-case studies across institutions, jurisdictions, or governance models to test the stability and boundaries of the conceptual framework.

Second, 22 semi-structured interviews across three phases provided the main empirical data. The sample size suited qualitative depth and saturation, but limits behaviour frequency claims. Future studies could accompany these findings with larger samples, survey-based instruments, or mixed-method designs to examine how widely the identified mental model characteristics operate across the higher education sector or apply alternative qualitative approaches, such as grounded theory or narrative analysis, to explore different analytic perspectives.

Third, the study relied on participants’ self-reports to drive findings. Phase 3 experts’ validation boosted the credibility; the study did not include direct observation of organisational system activity logs. Future work could use logs or long-term tracking for deeper behavioural shifts.

Fourth, the theory focused on PMT and Schein's model for analytical clarity; however, this limited the theoretical scope. Future studies could add institutional theory, other behaviour theories' perspective, or socio-technical views.

Taken together, these limitations do not undermine the study’s contributions. Despite these limitations, the study provided a grounded reasoning of how behavioural perception and organisational culture interact to shape cybersecurity readiness in HEIs. These limitations, therefore, highlight clear opportunities for extending and enriching the present findings in future research. 

\\section{Final Concluding}   
This thesis examined how cybersecurity readiness was shaped within a regional Australian higher education institution, despite the presence of formal governance, policies and established technical controls. The findings showed that employees were generally aware of cybersecurity risks; however, secure behaviour depended on how individuals interpreted privacy, responsibility, effort and perceived threats within everyday work practices.

Across the three phases of the study, cybersecurity behaviour was shaped by practical judgement rather than formal procedures alone. Individuals acted securely when actions felt achievable, meaningful, and supported. Where effort was high, authority unclear, or attention stretched, even a privacy-aware employee deprioritised secure action. These patterns were not isolated individual shortcomings. They reflected how organisational culture, leadership signals, governance practices, and workload conditions interacted with individual decision-making.

The study demonstrated that cybersecurity readiness is a collective condition. It emerged when individual privacy reasoning was reinforced by visible leadership, clear accountability, usable processes, and realistic expectations of work. Where these conditions were misaligned, readiness weakened, regardless of policy coverage or awareness levels.

By integrating individual mental models with organisational culture and expert validation, this research provided a grounded explanation of how readiness is formed and sustained in HEIs. The contribution lies not in identifying new risks, but in explaining why existing controls succeed or fail in practice.

At a time of increasing cyber exposure in decentralised academic environments, this thesis shows that improving readiness requires alignment between behaviour and institutional design. Secure behaviour becomes reliable only when it is supported as normal work, not treated as an additional demand.

 

   
\\clearpage  
\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{figure}{0}  
\\setcounter{table}{0}

\\renewcommand{\\thesection}{A.\\arabic{section}}  
\\renewcommand{\\thesubsection}{A.\\arabic{section}.\\arabic{subsection}}  
\\renewcommand{\\thefigure}{A.\\arabic{figure}}  
\\renewcommand{\\thetable}{A.\\arabic{table}}

\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{A}  
\\label{appendix:A}  
\\makeatother  
\\addcontentsline{toc}{chapter}{A: Research Phase 1 \- Supporting Documents}  
\\markboth{APPENDIX A}{APPENDIX A}

\\begin{center}  
    {\\Large \\textbf{Appendix A}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}

\\section\*{A.1 Research Phase 1 \- Documents}  
TThis study was conducted across three sequential phases of data collection, each employing semi-structured interviews to generate in-depth qualitative insights. Ethical approval for Phase 1 was obtained from the institutional Human Research Ethics Committee under approval number 2023/189. Prior to participant recruitment, formal permission was secured from the host institution, ensuring appropriate access, participant anonymity, and compliance with approved protocols.

This appendix provides the supporting documents used in Phase 1, including the recruitment poster, organisational social media announcement, participant invitation email, consent form, and interview protocol.

   
\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1- Ethics Approval}\\\\   
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/P1-ethics.pdf}  
\\end{center}

\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1- Recruitment Poster}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_rec\_Poster.jpg}  
\\end{center}

\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1 \- Recruitment: Organisational Social News Post}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_rec\_news1.jpg}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1- Recruitment Email}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_rec\_email.jpg}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1 \- Participant Consent Form}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_rec\_cons.jpg}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1 \- Interview Protocol (Part A)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_interview1.jpg}  
\\end{center}

\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 1 \- Interview Protocol (Part B)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_interview2.jpg}  
\\end{center}  
   
 

\\clearpage

\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{table}{0}  
\\setcounter{figure}{0}

\\renewcommand{\\thesection}{B.\\arabic{section}}  
\\renewcommand{\\thesubsection}{B.\\arabic{section}.\\arabic{subsection}}

   
\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{B}  
\\label{appendix:B}  
\\makeatother  
\\addcontentsline{toc}{chapter}{B: Research Phase 2 \- Supporting Documents}  
\\markboth{APPENDIX B}{APPENDIX B}

\\begin{center}  
    {\\Large \\textbf{Appendix B}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}

   
% \\section{Phase: Ethics Approval}

 \\section\*{B.1 Phase 2 \- Documents}  
Phase 2 examined organisational culture and leadership influences on cybersecurity readiness through semi-structured interviews. Ethical approval for this phase was obtained from the institutional Human Research Ethics Committee under approval number 2024/074. Prior to participant recruitment, formal permission was secured from the host institution, ensuring appropriate access, participant anonymity, and compliance with approved protocols.

This appendix presents the supporting documents used in Phase 2, including the recruitment poster, participant invitation email, and interview protocol tailored to organisational and leadership perspectives.

 

   
\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2 \- Ethics Approval}\\\\   
    \\includegraphics\[width=1.5\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/P2-ethics.pdf}  
\\end{center}

\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2- Recruitment Poster}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p2\_rec\_Poster.jpg}  
\\end{center}

 

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2- Recruitment Email}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p2\_rec\_email.jpg}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2 \- Participant Consent Form}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p2\_rec\_cons.pdf}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2 \- Interview Protocol (Part A)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p2\_interview1.jpg}  
\\end{center}

\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase  2- Interview Protocol (Part B)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p2\_interview2.jpg}  
\\end{center}  
   
\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2- Interview Protocol (Part C)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p2\_interview3.jpg}  
\\end{center}  
 

 

\\clearpage  
\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{table}{0}  
\\setcounter{figure}{0}

\\renewcommand{\\thesection}{C.\\arabic{section}}  
\\renewcommand{\\thesubsection}{C.\\arabic{section}.\\arabic{subsection}}

\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{C}  
\\label{appendix:C}  
\\makeatother

\\addcontentsline{toc}{chapter}{C: Research Phase 3 \- Supporting Documents}  
\\markboth{APPENDIX C}{APPENDIX C}

\\begin{center}  
    {\\Large \\textbf{Appendix C}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}

   
 

 \\section\*{C.1 Phase 3 \- Documents}  
Phase 3 focused on expert validation and refinement of the findings and the integrated conceptual framework developed in earlier phases. Semi-structured interviews were conducted with domain experts to evaluate the relevance, clarity, and applicability of the identified themes and proposed relationships. Ethical approval for this phase was obtained from the institutional Human Research Ethics Committee under approval number 2024/119. Prior to participant recruitment, formal permission was secured from the host institution, ensuring appropriate access, participant anonymity, and compliance with approved protocols.

This appendix presents the supporting documents used in Phase 3, including the recruitment materials, participant invitation email, and interview protocol designed for expert validation and framework assessment.

 

   
\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 3 \- Ethics Approval}\\\\   
    \\includegraphics\[width=1.5\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/P3-ethics.pdf}  
\\end{center}

% \\clearpage  
% \\begin{center}  
%     % \\textbf{Figure A.1}\\\\\[1em\]  
%     \\textbf{Phase 3- Recruitment Poster}\\\\\[1.5em\]  
%     \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p3\_rec\_Poster.jpg}  
% \\end{center}

% \\clearpage  
% \\begin{center}  
%     % \\textbf{Figure A.1}\\\\\[1em\]  
%     \\textbf{Phase 2- Recruitment \- Organisational Social News Advertiser}\\\\\[1.5em\]  
%     \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p1\_rec\_news1.jpg}  
% \\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 3- Recruitment Email}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p3\_rec\_email.jpg}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 3 \- Participant Consent Form}\\\\\[1.5em\]  
    \\includegraphics\[width=1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p3\_rec\_cons.jpg}  
\\end{center}

 \\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 3 \- Interview Protocol (Part A)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p3\_interview1.jpg}  
\\end{center}

\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 3- Interview Protocol (Part B)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p3\_interview2.jpg}  
\\end{center}  
   
\\clearpage  
\\begin{center}  
    % \\textbf{Figure A.1}\\\\\[1em\]  
    \\textbf{Phase 2 \- Interview Protocol (Part C)}\\\\\[1.5em\]  
    \\includegraphics\[width=1.1\\linewidth,height=0.85\\textheight,keepaspectratio\]{Figures//appendix/p3\_interview3.jpg}  
\\end{center}  
 

% \\begin{figure}\[htbp\]  
% \\centering  
% \\includegraphics\[width=\\textwidth\]{figure.pdf}  
% \\caption{Descriptive caption of the figure}  
% \\label{fig:pdf\_figure}  
% \\end{figure}

   
\\clearpage

\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{table}{0}  
\\setcounter{figure}{0}

\\renewcommand{\\thesection}{D.\\arabic{section}}  
\\renewcommand{\\thesubsection}{D.\\arabic{section}.\\arabic{subsection}}  
\\renewcommand{\\thefigure}{D.\\arabic{figure}}  
\\renewcommand{\\thetable}{D.\\arabic{table}}

   
\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{D}  
\\label{appendix:D}  
\\makeatother  
\\addcontentsline{toc}{chapter}{D: Research Phase 1 \- Data and Codebook}  
\\markboth{APPENDIX D}{APPENDIX D}

\\begin{center}  
    {\\Large \\textbf{Appendix D}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}

   
% \\section{Phase: Ethics Approval}

 % \\section\*{D.1 Phase 1- Analysis Data,  Quotations}  
   
\\noindent Appendix D presents selected Phase 1 data, code analysis, and the complete Phase 1 codebook developed through the NVivo-based analysis process. It includes all codes and subcodes, their definitions, associated properties, and supporting participant quotations. The appendix also outlines the stages of data analysis undertaken during Phase 1, and presents how initial coding evolved into a structured thematic framework.

To maintain clarity and readability in Chapter \\ref{chapter:c5}, only representative sample quotations were presented in the main text. The full set of supporting quotations is therefore provided in this appendix to ensure analytical transparency and enable verification of coding decisions.

\\section\*{\\textbf{D.1 Phase 1- Participant Interview Environment and Consent:}}

Table D.1 documents interview modality, duration, location, and consent status \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{3cm} p{2.5cm} p{3cm} p{2cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Phase 1 Interview Environment and Consent}  
\\label{tab:D.1}  
}  
\\\\

\\hline  
\\textbf{Interview ID} & \\textbf{Type of Interview} & \\textbf{Interview Duration (minutes)} & \\textbf{Location} & \\textbf{Consent Signed} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Interview ID} & \\textbf{Type of Interview} & \\textbf{Interview Duration (minutes)} & \\textbf{Location} & \\textbf{Consent Signed} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
P1-001 & Face-to-Face & 45 & On-site meeting room & YES \\\\ \\hline  
P1-002 & Face-to-Face & 37 & On-site meeting room & YES \\\\ \\hline  
P1-003 & Face-to-Face & 42 & On-site meeting room & YES \\\\ \\hline  
P1-004 & Face-to-Face & 38 & On-site meeting room & YES \\\\ \\hline  
P1-005 & Face-to-Face & 46 & On-site meeting room & YES \\\\ \\hline  
P1-006 & Face-to-Face & 51 & On-site meeting room & YES \\\\ \\hline  
P1-007 & Online (Microsoft Teams) & 55 & Teams (online) & YES \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\section\*{\\textbf{D.2 Phase 1 data and the NVivo Coding Version:}}

This section presents multiple coding iterations in Phase 1 (Figure  D.1), illustrating how initial codes were refined into a stable thematic structure. \\\\

\\noindent  
\\textbf{Figure D.1}\\\\\[1em\]  
\\textit{Phase 1 Coding Iterations and Theme Development}\\\\   
% \\noindent  
\\begin{minipage}\[t\]{0.6\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1-multicod1.png}  
\\end{minipage}

% \\begin{figure} \[H\]  
%     \\centering  
%     \\includegraphics\[width=0.5\\linewidth\]{Figures//appendix/p1-multicod1.png}  
%     \\caption{Phase 1 Coding Iterations and Theme Development\[}  
%     \\label{fig:D1}  
% \\end{figure}

\\clearpage  
\\noindent  
\\textbf{Figure D.2}\\\\\[1em\]  
\\textit{Phase 1 Code Version 1}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.5\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1c1v1.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1c1v2.png}  
\\end{minipage}

\\clearpage  
\\noindent  
\\textbf{Figure D.2}\\\\\[1em\]  
\\textit{Phase 1 Code Version 2}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.48\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1c2v1.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1c2v2.png}  
\\end{minipage}

   
\\clearpage  
\\noindent  
\\textbf{Figure D.3}\\\\\[1em\]  
\\textit{Phase 1 Code Version 3}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.6\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1c3v1.png}  
\\end{minipage}  
\\hfill  
% \\begin{minipage}\[t\]{0.48\\linewidth}  
%     \\centering  
%     \\includegraphics\[width=\\linewidth\]{Figures/appendix/p1c3v2.png}  
% \\end{minipage}  
   
\\section\*{\\textbf{D.3 Phase 1 Code book:}}

This section presents Table D.2, which contains the complete Phase 1 codebook, including code definitions and supporting quotations. Table D.3 presents the supplementary quotations and qualitative evidence for Phase 1\. \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.8cm} p{4.2cm} p{7cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Phase 1 Code Book with Aligned Hierarchical Coding and Evidence}  
\\label{tab:D.2}  
}  
\\\\

\\hline  
\\textbf{Code \\& ID} & \\textbf{Code Definition} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code \\& ID} & \\textbf{Code Definition} & \\textbf{Sample Interview Quotes} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

\\textbf{1.1.1 Cybersecurity Incident} & Occurrences where security is breached or compromised by threats. & \`\`They should focus more on what are spams... my supervisors themselves thought this was a general email, but it was a spam.'' (P1-004) \\newline \`\`In his \[study\] also has some of the malware content... the network has not allowed me to install on my OneDrive.'' (P1-003) \\\\ \\hline

\\textbf{1.1.2 Privacy Focus} & The extent to which users prioritise and act upon data protection. & \`\`Have I read the data policy? No. Have I done some training on it? I probably would have, yeah.'' (P1-002) \\newline \`\`I don't think that I am sending anything so valuable that I should protect it with the password.'' (P1-006) \\\\ \\hline

\\textbf{1.1.3 Training Perspective} & Participant attitudes toward the necessity and quality of security education. & \`\`When it is not compulsory, then it's like you will. OK, I will say it later... they should be like compulsory training.'' (P1-003) \\newline \`\`If it's not mandatory, I keep it out... if I get time, then I do it.'' (P1-006) \\\\ \\hline

\\textbf{2.1.1 Exploitability} & Technical or behavioural gaps that allow for successful cyber attacks. & \`\`Sadly, I do it. I did it \[wrongly clicking\] and then regret it.'' (P1-005) \\newline \`\`I just downloaded \[it\]... many people use that one, and then... I trust the owner.'' (P1-001) \\\\ \\hline

\\textbf{2.1.2 Negligent Reliance} & Over-trusting existing systems or habits leading to reduced vigilance. & \`\`For me, it doesn't really bother me... somehow in the back of the head, I feel that maybe I'm safe inside the \[organisation\].'' (P1-006) \\newline \`\`As the university is providing the VPN, so I feel safe.'' (P1-003) \\\\ \\hline

\\textbf{2.2.1 Consequence} & Perceived impact or results of a security breach or policy violation. & \`\`I am not giving any information that can personally help me... I am thinking that I am apparently safe.'' (P1-006) \\newline \`\`I would think there is no consequence...'' (P1-005) \\\\ \\hline

\\textbf{2.3.1 Benefits} & Perceived rewards or positive recognition for adhering to security protocols. & \`\`Any reward should be regularly to encourage. Yes, it is very good thing.'' (P1-006) \\newline \`\`I'm not looking for recognition, but it I'm doing it for me.'' (P1-005) \\\\ \\hline

\\textbf{3.1.1 Ability} & Self-reported competence and skill in managing security tasks. & \`\`I feel like I'm already being careful... I'm always on my toes.'' (P1-004) \\newline \`\`If something happened... usually first thing that I need to do is I'll do it by myself.'' (P1-001) \\\\ \\hline

\\textbf{3.2.1 Effectiveness} & The perceived success of specific security actions or tools. & \`\`I do inform the \[IT Department\], and straight away I just delete the email... I blocked the email.'' (P1-003) \\newline \`\`I normally avoid the type of things and then only download the files from the real source.'' (P1-001) \\\\ \\hline

\\textbf{3.2.2 Trust} & Confidence in the organization's infrastructure and management to protect data. & \`\`I always think this is a safe place for me to deal with, so I should not be on my toes every time.'' (P1-004) \\newline \`\`The only reason to feel safe is that big organisation working behind OneDrive.'' (P1-005) \\\\ \\hline

\\textbf{3.3.1 Barrier} & Obstacles that prevent or discourage secure behavior and awareness. & \`\`While my immediate thought is about protecting myself, I haven't previously considered the potential harm to the organisation.'' (P1-002) \\newline \`\`Yes, I know, like it can affect me also, like they can fire me... and it can also affect reputations.'' (P1-003) \\\\ \\hline

\\textbf{4.1.1 Cybersecurity Intentions} & The planned or likely future behaviours regarding security practices. & \`\`I am safe because I'm not doing any transaction using public Wi-Fi... But maybe I am browsing my email.'' (P1-006) \\newline \`\`It become my habit now... I don't think before I open anything.'' (P1-007) \\\\ \\hline

\\textbf{4.1.2 Policy Compliance} & Adherence to official organisational security rules and guidelines. & \`\`I don't know what current password policy means, but \[organisation\] sends us emails... so I changed my email password.'' (P1-006) \\newline \`\`Policies and policies, aren't they? They're just... not great fun reading.'' (P1-005) \\\\ \\hline

\\textbf{4.1.3 Risk Awareness} & Recognition of potential threats and the sensitivity of handled data. & \`\`Nothing they \[Hacker\] can \[do\], at most like, contact me, send me spam... they can't do identity theft.'' (P1-004) \\newline \`\`To my understanding, it means the data which has some personal information... which can cause harm.'' (P1-006) \\\\ \\hline

\\textbf{4.1.4 Safe Practices} & Routine behaviours used to mitigate security risks in daily tasks. & \`\`Even if I click and see... there's a probability of something is going on or wrong, so I don't proceed further.'' (P1-004) \\newline \`\`I'm kind of person who do bite of research before I share my information.'' (P1-007) \\\\ \\hline

\\textbf{5.1.1 Insufficient Support} & Perceived lack of guidance or resources from management and IT. & \`\`No, they \[organisation\] just told me that there are some privacy regulations... But they didn't actually tell me about the consequences.'' (P1-002) \\newline \`\`No, no one gave me, absolutely no one \[regarding guidance\]... I think they should impart the knowledge.'' (P1-004) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{3.2cm} p{1.5cm} p{9cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Complete Phase 1 Supplementary Quotations by Theme}  
\\label{tab:D.3}  
}  
\\\\

\\hline  
\\textbf{Theme} & \\textbf{ID} & \\textbf{Sample Quotation} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Theme} & \\textbf{ID} & \\textbf{Sample Quotation} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
\\textbf{Cybersecurity Awareness and Training Effectiveness  
(P1-T1)} & P1-001 & \`\`I know there are some policies, but I did not really go through them.'' \\\\ \\cline{2-3}   
 & P1-002 & \`\`They give us training once a year, but after that no one checks whether we actually remember or apply it.'' \\\\ \\cline{2-3}   
 & P1-003 & \`\`Training is mostly generic. It does not really explain how my role could cause a problem.'' \\\\ \\cline{2-3}   
 & P1-004 & \`\`Most of the security training feels the same every year, so people already know what to click.'' \\\\ \\cline{2-3}   
 & P1-005 & \`\`You just click, click, click and finish it.'' \\\\ \\cline{2-3}   
 & P1-006 & \`\`We receive emails about security, but they are easy to ignore once work starts.'' \\\\ \\cline{2-3}   
 & P1-007 & \`\`I know there are guidelines, but I do not actively think about them day to day.'' \\\\ \\hline

\\textbf{Assessing and Mitigating Threats Through Awareness and Consequence Management  
(P1-T2)  
} & P1-001 & \`\`Once the hacker gain access, they can do anything.'' \\\\ \\cline{2-3}   
 & P1-002 & \`\`If something happened to student data, it would be embarrassing for the university...'' \\\\ \\cline{2-3}   
 & P1-003 & \`\`I think attacks are more likely to happen because someone makes a small mistake.'' \\\\ \\cline{2-3}   
 & P1-004 & \`\`Once data is out, you cannot undo the damage to reputation.'' \\\\ \\cline{2-3}   
 & P1-005 & \`\`You assume nothing bad will happen because it has not happened before.'' \\\\ \\cline{2-3}   
 & P1-006 & \`\`If something happened, IT would probably fix it.'' \\\\ \\cline{2-3}   
 & P1-007 & \`\`If there was a breach, it would be more of an organisational issue.'' \\\\ \\hline

\\textbf{Balancing Confidence, Capability, and Costs in Coping Strategies  
(P1-T3)  
} & P1-001 & \`\`First I will try to fix it by myself.'' \\\\ \\cline{2-3}   
 & P1-002 & \`\`I know what I should do in theory, but when things get busy, security becomes secondary.'' \\\\ \\cline{2-3}   
 & P1-003 & \`\`Following all the steps properly takes time, especially when deadlines are close.'' \\\\ \\cline{2-3}   
 & P1-004 & \`\`Security tools slow things down, especially when you just need to finish something.'' \\\\ \\cline{2-3}   
 & P1-005 & \`\`Security steps always feel like extra work added on top of what we have to do.'' \\\\ \\cline{2-3}   
 & P1-006 & \`\`Sometimes I feel I lack the technical knowledge to decide.'' \\\\ \\cline{2-3}   
 & P1-007 & \`\`Extra security slows down my work.'' \\\\ \\hline

\\textbf{Proactive and Compliant Cybersecurity Behaviours  
(P1-T4)  
} & P1-002 & \`\`I follow the rules when they are very clear, but otherwise I just do what seems practical.'' \\\\ \\cline{2-3}   
 & P1-003 & \`\`If I trust him only in that case… I would change the password after.'' \\\\ \\cline{2-3}   
 & P1-004 & \`\`I try to avoid risky things instead of dealing with security processes.'' \\\\ \\cline{2-3}   
 & P1-005 & \`\`People react only when they are warned or reminded.'' \\\\ \\cline{2-3}   
 & P1-006 & \`\`I change my password only when I get the email.'' \\\\ \\cline{2-3}   
 & P1-007 & \`\`I usually follow security steps when they are clearly required.'' \\\\ \\hline

\\textbf{Addressing Gaps in Leadership and Authority Support  
(P1-T5)} & P1-001 & \`\`If any issue comes unexpected, I shall contact my immediate supervisor.'' \\\\ \\cline{2-3}   
 & P1-003 & \`\`Cybersecurity feels like an IT responsibility, not a management topic.'' \\\\ \\cline{2-3}   
 & P1-004 & \`\`Supervisors do not really talk about cybersecurity unless there is a problem.'' \\\\ \\cline{2-3}   
 & P1-005 & \`\`No, no one gave me, absolutely no one.'' \\\\ \\cline{2-3}   
 & P1-006 & \`\`It needs to be part of that, perhaps induction.'' \\\\ \\cline{2-3}   
 & P1-007 & \`\`I assume IT handles most of the serious issues.'' \\\\ \\hline

\\textbf{Other: } & P1-001 & \`\`That is more the university’s responsibility.'' \\\\ \\cline{2-3}   
 & P1-002 & \`\`As the university is providing the VPN, I feel safe.'' \\\\ \\cline{2-3}   
 & P1-003 & \`\`People find shortcuts when systems feel complicated.'' \\\\ \\cline{2-3}   
 & P1-004 & \`\`Because systems are managed centrally, people trust them more than themselves.'' \\\\ \\cline{2-3}   
 & P1-005 & \`\`I care about my privacy, but cybersecurity is handled by IT.'' \\\\ \\cline{2-3}   
 & P1-006 & \`\`I'm probably one of the few people who take this part seriously.'' \\\\ \\cline{2-3}   
 & P1-007 & \`\`I trust large organisations more with my data.'' \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

 

 

\\clearpage  
\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{table}{0}  
\\setcounter{figure}{0}

\\renewcommand{\\thesection}{E.\\arabic{section}}  
\\renewcommand{\\thesubsection}{E.\\arabic{section}.\\arabic{subsection}}  
\\renewcommand{\\thefigure}{E.\\arabic{figure}}  
\\renewcommand{\\thetable}{E.\\arabic{table}}

\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{E}  
\\label{appendix:E}  
\\makeatother

\\addcontentsline{toc}{chapter}{E: Research Phase 2 \- Data and Codebook}  
\\markboth{APPENDIX E}{APPENDIX E}

\\begin{center}  
    {\\Large \\textbf{Appendix E}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}

   
% \\section{Phase: Ethics Approval}  
%a

 % \\section\*{E.1 Phase 2- Analysis Data,  Quotations}  
   
\\noindent Appendix E details Phase 2 data analysis alongside the full Phase 2 NVivo codebook, including codes, subcodes, definitions, properties, and participant quotations. It also traces the data analysis stages, showing how initial codes were refined into structured themes.

For Chapter\~\\ref{chapter:c6} readability, the main chapter presents selected sample quotations; full supporting extracts are provided here for transparency.

\\section\*{\\textbf{E.1 Phase 2 \- Participant Interview Environment and Consent:}}

Table E.1 documents interview modality, duration, location, and consent status \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{3cm} p{2.5cm} p{3cm} p{2cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Phase 2 Interview Environment and Consent}  
\\label{tab:E.1}  
}  
\\\\

\\hline  
\\textbf{Interview ID} & \\textbf{Type of Interview} & \\textbf{Interview Duration (minutes)} & \\textbf{Location} & \\textbf{Consent Signed} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Interview ID} & \\textbf{Type of Interview} & \\textbf{Interview Duration (minutes)} & \\textbf{Location} & \\textbf{Consent Signed} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

% \--- Table Data \---  
P1-001 & Face-to-Face & 38 & On-site meeting room & YES \\\\ \\hline  
P1-002 & Online & 53 & MS Teams (online) & YES \\\\ \\hline  
P1-003 & Online & 55 & MS Teams (online) & YES \\\\ \\hline  
P1-004 & Online & 36 & MS Teams (online) & YES \\\\ \\hline  
P1-005 & Online & 55 & MS Teams (online) & YES \\\\ \\hline  
P1-006 & Online & 38 & MS Teams (online) & YES \\\\ \\hline  
P1-007 & Online & 59 & MS Teams (online) & YES \\\\ \\hline  
P1-008 & Online & 40 & MS Teams (online) & YES \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\section\*{\\textbf{E.2 Phase 2 data and the NVivo Coding Version:}}

The multiple coding iterations in Phase 2 are presented, showing how initial codes were refined into a stable thematic structure. \\\\

\\noindent  
\\textbf{Figure E.1}\\\\\[1em\]  
\\textit{Phase 2 Coding Iterations and Theme Development}\\\\   
% \\noindent  
\\begin{minipage}\[t\]{0.6\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2-multicod1.png}  
\\end{minipage}

 

% \\begin{figure} \[H\]  
%     \\centering  
%     \\includegraphics\[width=0.5\\linewidth\]{Figures//appendix/p1-multicod1.png}  
%     \\caption{Phase 1 Coding Iterations and Theme Development\[}  
%     \\label{fig:D1}  
% \\end{figure}

\\clearpage  
\\noindent  
\\textbf{Figure E.2}\\\\\[1em\]  
\\textit{Phase 2 Code Version 1}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.55\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c1v1.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.55\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c1v3.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.55\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c1v2.png}  
\\end{minipage}  
 \\hfill

   
\\clearpage  
\\noindent  
\\textbf{Figure E.2}\\\\\[1em\]  
\\textit{Phase 2 Code Version 2}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.5\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c2v1.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.5\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c2v3.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.5\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c2v3.png}  
\\end{minipage}  
   
   
   
\\clearpage  
\\noindent  
\\textbf{Figure E.3}\\\\\[1em\]  
\\textit{Phase 2 Code Version 3}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.55\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c3v1.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p2c3v2.png}  
\\end{minipage}  
   
   
\\section\*{\\textbf{E.3 Phase 1 Codebook:}}

Table E.2 presents the complete Phase 2 codebook, including code definitions and supporting quotations. Table E.3 presents supplementary quotations and qualitative evidence for Phase 2\. \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2.8cm} p{4.2cm} p{7cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Phase 2 Code Book with Aligned Hierarchical Coding and Evidence}  
\\label{tab:E.2}  
}  
\\\\

\\hline  
\\textbf{Code \\& ID} & \\textbf{Definition} & \\textbf{Sample Interview Quotations} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Code \\& ID} & \\textbf{Definition} & \\textbf{Sample Interview Quotations} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

\\textbf{1.1.1 Lack of Awareness on Physical Security} & Refers to the oversight of tangible security measures like signage, office layout, and ID protocols. & \`\`Mostly now it's just emails... I haven't noticed any wall banners or posters. The fact I haven't noticed them means they aren't effective.'' (P2-005) \\newline \`\`I think open plan kind of offices don't lend themselves to security... the space is shared by students and staff.'' (P2-004) \\\\ \\hline

\\textbf{1.2.1 Impact of Disagreement Between Organisational and Personal Values} & Occurs when institutional security policies conflict with personal professional values, ethics, or efficiency. & \`\`It has been shown that getting people to update \[password\] too frequently is not a good idea... but that is the central \[IT\] policy.'' (P2-001) \\newline \`\`There is always this conflict... I want to be the admin... It's very, very stressful.'' (P2-005) \\\\ \\hline

\\textbf{1.2.2 Leader Handled Employee Conflicts or Decision-Making Based on Experience} & Describes leaders relying on personal history and situational judgment rather than formal policy or values. & \`\`End of the day, my action \[is\] based on my experience... within the constraints I know I have available to me.'' (P2-001) \\newline \`\`Leadership... they are making decisions from their mind... You have to make a decision that is fair.'' (P2-007) \\\\ \\hline

\\textbf{1.3.1 Individual Assumptions May Risk or Undermine Organisational Readiness} & Identifies how personal beliefs about others' maturity or system safety can weaken institutional vigilance. & \`\`I assume most of the organisational people they are mature enough... so definitely assumptions, they impact a lot.'' (P2-006) \\newline \`\`I don't see the relationship between cyber security and the day-to-day culture.'' (P2-005) \\\\ \\hline

\\textbf{1.3.2 Gap Between Organisational Policy Implementation and Communication} & Represents the perceived disconnect between top-down security decisions and the explanation of their necessity. & \`\`There is no communication... I also discovered this just accidentally by clicking on something.'' (P2-005) \\newline \`\`And so, they gave me a computer, which has just turned into a paperweight... I have to call IT for one tiny update.'' (P2-004) \\\\ \\hline

\\textbf{2.1.1 Individual Incident Reporting Depends on Trust} & Indicates that the willingness to report breaches is influenced by procedural clarity and the social trust within the hierarchy. & \`\`If there was not a feeling of trust... then that would definitely impact... they wouldn't want to report.'' (P2-002) \\newline \`\`Some people just click on it intentionally just for fun because we can tell it's wrong... they need to trust that you are responsible.'' (P2-005) \\\\ \\hline

\\textbf{2.1.2 Behavioural Fatigue and Disengagement} & Captures the psychological burnout and resistance resulting from repetitive, boring, or restrictive security protocols. & \`\`It is annoying. You know it is wasting our time... every e-mail, every document, everything the \[organisation\] introduced.'' (P2-007) \\newline \`\`Normal users... they are not responsible for cybersecurity... end users have always been a pain area.'' (P2-006) \\\\ \\hline

\\textbf{3.1.1 Cyber Risks Due to Deep-Rooted Cultural Misperceptions} & Identifies systemic vulnerabilities caused by the belief that security is someone else's responsibility or simply \`\`common sense.'' & \`\`I think most of us are pretty slack actually... we never hear of any breaches. So we think it'll happen to someone else.'' (P2-002) \\newline \`\`I don't think that people understand that even with sensitive information there is Freedom of Information Act.'' (P2-008) \\\\ \\hline

\\textbf{4.1.1 Cultural Hesitation to Report Incidents Due to Fear or Embarrassment} & Reflects the tendency to avoid reporting security lapses due to perceived social stigma or punitive training consequences. & \`\`If someone accidentally clicks on a phishing e-mail... they do have to go back and do some mandatory training.'' (P2-003) \\newline \`\`I've never experienced any such thing where people have reported it to me... they never shared for example...'' (P2-006) \\\\ \\hline

\\textbf{5.1.1 Leadership Lag in Onboarding Cybersecurity Policy Awareness} & Reflects the lack of specific cybersecurity guidance provided to new staff during the initial induction phase. & \`\`I know that there are some orientation sessions... But I don't know the specifics of what was involved.'' (P2-001) \\newline \`\`I'm not sure because orientation for new staff... they must be talking about this, I hope.'' (P2-005) \\\\ \\hline

\\textbf{6.1.1 Organisational Actions Are Not Effective Enough} & Highlights the failure of top-down measures to engage users due to poor content quality and lack of feedback. & \`\`Video \[Training\] for half an hour... so boring... nobody checks... they're not that clever.'' (P2-008) \\newline \`\`The IT don't ask us to provide feedback on that... They never asked us about this.'' (P2-005) \\\\ \\hline

\\textbf{7.1.1 Leadership and Behavioural Dynamics Influencing Cybersecurity Culture} & Examines how interpersonal relationships and role modeling within management dictate the overall security climate. & \`\`Manager, of course should be a role model... I did use that as a learning experience \[sharing a personal incident\].'' (P2-002) \\newline \`\`If you have a good relation with people, then if they have an issue they can talk with you about it.'' (P2-005) \\\\ \\hline

\\textbf{8.1.1 Ignorance Towards Policy} & Focuses on the active or passive avoidance of reading and understanding formal policy documents due to volume. & \`\`There would be policies; whether or not people read the policy is a different matter... there's probably thousands.'' (P2-002) \\newline \`\`It is so straightforward that you can just skip to the assessment... I've done this 100 times before.'' (P2-001) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{3.2cm} p{1.5cm} p{9cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Complete Phase 2 Supplementary Quotations by Theme}  
\\label{tab:E.3}  
}  
\\\\

\\hline  
\\textbf{Theme} & \\textbf{ID} & \\textbf{Sample Quotation} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Theme} & \\textbf{ID} & \\textbf{Sample Quotation} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

\\textbf{Physical Symbolism and Security Culture Blind Spots  
(P2-T1)} & P2-005 & \`\`Mostly now it's just emails... I haven't noticed any wall banners or posters. The fact I haven't noticed them means they aren't effective.''   \\\\ \\cline{2-3}  
 & P2-001 & \`\`I remember seeing posters a few years back, but I don't think there are any up these days.''   \\\\ \\cline{2-3}  
 & P2-004 & \`\`I think open plan kind of offices don't lend themselves to security. That's always a huge issue... the space is shared by students and staff.''   \\\\ \\cline{2-3}  
 & P2-008 & \`\`Given that everybody is open cubicles or open space, it's not that secure. Tailgating is still possible.''   \\\\ \\hline

\\textbf{Organisational Values Are Not Reflected in Daily Leadership Decisions  
(P2-T2)} & P2-001 & \`\`...insisting on special characters etc. is not necessarily promoting good practice, but that is the central \[IT\] policy, and there is no way of changing it.''   \\\\ \\cline{2-3}  
 & P2-007 & \`\`Different views would be always there... but since we are working in an umbrella, we have to protect this umbrella.''   \\\\ \\cline{2-3}  
 & P2-005 & \`\`There is always this conflict between someone like myself and the IT service. I want to be the admin... It's very, very stressful.''   \\\\ \\hline

\\textbf{Assumptive Resistance Loops Undermining Cybersecurity Readiness  
(P2-T3)} & P2-005 & \`\`I don't see the relationship between cyber security and the day-to-day culture... cybersecurity is the relationship between you and the computer.''   \\\\ \\cline{2-3}  
 & P2-006 & \`\`I assume most of the organisational people they are mature enough... so definitely assumptions, they impact a lot.''   \\\\ \\cline{2-3}  
 & P2-006 & \`\`If somebody is reluctant in change, so definitely they will try to resist as much as they can.''   \\\\ \\hline

\\textbf{Experiential Trust Threshold and Disengagement in Incident Reporting  
(P2-T4)} & P2-006 & \`\`If there is an incident, everybody should be able to know where they have to report it... if you ask me, where I will report it, I'm not sure.''   \\\\ \\cline{2-3}  
 & P2-003 & \`\`...if one of my members of my team had done that \[breach\] I wouldn't know \[the protocol\] off the top of my head at all.''   \\\\ \\cline{2-3}  
 & P2-005 & \`\`Some people just click on it \[phishing test\] intentionally just for fun because we can tell it's wrong... they need to trust that you are responsible.''   \\\\ \\hline

\\textbf{End-User Behavioural Drift and Compliance Fatigue  
(P2-T5)} & P2-001 & \`\`...you can just skip to the assessment section... you set the video going, you mute it, you go and do something else... it really feels it's pushed so heavily that we don't take it seriously.''   \\\\ \\cline{2-3}  
 & P2-001 & \`\`...increasingly, I am \[averse to technology\] as well because I'm too busy to change anything.''   \\\\ \\cline{2-3}  
 & P2-004 & \`\`You get used to clicking through things because it's always the same.''   \\\\ \\hline

\\textbf{Cultural Miscalibration in Cyber Risk Perception  
(P2-T6)} & P2-002 & \`\`We never hear of any breaches… most of us probably believe it won't happen here. We're pretty slack actually.''   \\\\ \\cline{2-3}  
 & P2-003 & \`\`Cybersecurity is something best enforced… you need really tough rules; otherwise people won't pay attention.''   \\\\ \\cline{2-3}  
 & P2-008 & \`\`People assume that if something is serious, someone else will handle it.''   \\\\ \\hline

\\textbf{Security Culture Embarrassment Barrier  
(P2-T7)} & P2-003 & \`\`People have felt really insecure in being able to voice their concerns… that would definitely flow on to that cybersecurity space.''   \\\\ \\cline{2-3}  
 & P2-005 & \`\`People would feel like they were being judged... if they made a mistake with a link.''   \\\\ \\hline

\\textbf{Leadership Lag in Onboarding Cybersecurity Policy  
(P2-T8)} & P2-001 & \`\`I know there are some orientation sessions… but I don't know the specifics of what was involved.''   \\\\ \\cline{2-3}  
 & P2-007 & \`\`I think the onboarding for security is very quiet. It is not mentioned as a priority.''   \\\\ \\hline

\\textbf{Strategic Weakness in Security Governance in Academia  
(P2-T9)} & P2-004 & \`\`Cybersecurity is always emerging and evolving… there is a need for continuous improvement \[but the institution is lagging\].''   \\\\ \\cline{2-3}  
 & P2-002 & \`\`Doing this module again… the content hasn't changed. It's just wasting my time.''   \\\\ \\cline{2-3}  
 & P2-008 & \`\`I think the system exists, but I don't know who actually owns it.''   \\\\ \\hline

\\textbf{Leadership and Behavioural Dynamics Influencing Cybersecurity Culture  
(P2-T10)} & P2-004 & \`\`If leaders don't reinforce it, people won't treat it as important.''   \\\\ \\cline{2-3}  
 & P2-003 & \`\`I don't really speak to the staff who report to me because I expect they already know this stuff.''   \\\\ \\cline{2-3}  
 & P2-002 & \`\`When I got a virus on my laptop… I did use that as a learning experience \[to show others\].''   \\\\ \\hline

\\textbf{Ignorance Towards Policy  
(P2-T11)} & P2-002 & \`\`I don't know what's in induction… I'm assuming they had to do a series of online modules.''   \\\\ \\cline{2-3}  
 & P2-003 & \`\`I've never actually had one \[policy\]. I wouldn't know them off the top of my head… I would have to go and find that information.''   \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup  
   
 

\\clearpage  
\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{table}{0}  
\\setcounter{figure}{0}

\\renewcommand{\\thesection}{F.\\arabic{section}}  
\\renewcommand{\\thesubsection}{F.\\arabic{section}.\\arabic{subsection}}  
\\renewcommand{\\thefigure}{F.\\arabic{figure}}  
\\renewcommand{\\thetable}{F.\\arabic{table}}

   
\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{F}  
\\label{appendix:F}  
\\makeatother

\\addcontentsline{toc}{chapter}{F: Research Phase 3 \- Data and Codebook}  
\\markboth{APPENDIX F}{APPENDIX F}

\\begin{center}  
    {\\Large \\textbf{Appendix F}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}  
   
\\noindent Appendix F details Phase 3 data analysis, including NVivo-coded expert data alongside supporting evidence for the findings.

For Chapter\~\\ref{chapter:c7} presents selected sample quotations; full supporting extracts are provided here for transparency.

\\section\*{\\textbf{F.1 Phase 3 \- Participant Interview Environment and Consent:}}

Table F.1 documents expert interview modality, duration, location, and consent status. \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{3cm} p{2.5cm} p{3cm} p{2cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Phase 3 Interview Environment and Consent}  
\\label{tab:F.1}  
}  
\\\\

\\hline  
\\textbf{Interview ID} & \\textbf{Type of Interview} & \\textbf{Duration (min)} & \\textbf{Location} & \\textbf{Consent Signed} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Interview ID} & \\textbf{Type of Interview} & \\textbf{Duration (min)} & \\textbf{Location} & \\textbf{Consent Signed} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

P3-001 & MS Teams (Online) & 49 & Remote (Campus) & YES \\\\ \\hline  
P3-002 & MS Teams (Online) & 58 & Remote & YES \\\\ \\hline  
P3-003 & MS Teams (Online) & 47 & Remote & YES \\\\ \\hline  
P3-004 & MS Teams (Online) & 57 & Remote & YES \\\\ \\hline  
P3-005 & MS Teams (Online) & 52 & Remote & YES \\\\ \\hline  
P3-006 & MS Teams (Online) & 47 & Remote (Campus) & YES \\\\ \\hline  
P3-007 & MS Teams (Online) & 49 & Remote (Campus) & YES \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

\\section\*{\\textbf{F.2 Phase 3 data and the NVivo Coding Version:}}

The multiple coding iterations in Phase 3, exposing how initial codes were refined into a stable thematic structure. \\\\  
   
 %  
 

\\clearpage  
\\noindent  
\\textbf{Figure F.2}\\\\\[1em\]  
\\textit{Phase 3 NVivo Code Analysis}\\\\ 

\\noindent  
\\begin{minipage}\[t\]{0.5\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p3c1v1.png}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.5\\linewidth}  
    \\centering  
    \\includegraphics\[width=\\linewidth\]{Figures/appendix/p3c1v2.png}  
\\end{minipage}  
   
   
\\section\*{\\textbf{F.3 Phase 3 Codebook:}}

Table F.2 presents supplementary expert quotations and qualitative evidence for Phase 3\. \\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{3.5cm} p{1.8cm} p{9cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Phase 3 Expert Validation: Consolidated Supplementary Quotations Table}  
\\label{tab:F.2}  
}  
\\\\

\\hline  
\\textbf{Phase} & \\textbf{ID} & \\textbf{Sample Expert Quotation (Verbatim)} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Phase} & \\textbf{ID} & \\textbf{Sample Expert Quotation (Verbatim)} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

\\multirow{14}{3.5cm}{\\textbf{Phase 1: Individual Behaviour Support}}   
& P3-003 & \`\`It's just people being lazy. IT training happens across all levels. Saying, \`I didn't know,' is an excuse.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`If someone has been impacted by a cybersecurity event, it has a stronger effect... education alone might not stick.'' \\\\ \\cline{2-3}  
& P3-007 & \`\`It's very difficult to tailor training... we usually tailor based on role types, but not necessarily on an individual's profile.'' \\\\ \\cline{2-3}  
& P3-003 & \`\`Training must be consistent, followed up, and measured for effectiveness. Employees should be held accountable.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`Without that real-world experience, education alone might not stick as effectively... it has a stronger effect if someone has been impacted.'' \\\\ \\cline{2-3}  
& P3-006 & \`\`If people don't understand risks or consequences, they won't take the right actions.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`Some people see security as a black box... they assume everything is handled for them and feel no need to think about it.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`They might mistakenly feel fully protected by the university's systems... This creates a false sense of security.'' \\\\ \\cline{2-3}  
& P3-003 & \`\`Over-relying on IT is risky... individuals must also take responsibility and understand that technology alone cannot prevent all threats.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`People want to behave properly... but if it interferes with their work or takes too much time, they might cut corners. It's a trade-off.'' \\\\ \\cline{2-3}  
& P3-002 & \`\`I've been involved in many research projects where security is seen as a secondary concern... the focus is always on the research output.'' \\\\ \\cline{2-3}  
& P3-004 & \`\`Leaders shape the tone... If they don't act, it's a serious problem. It must be seen as part of the organisation's core values.'' \\\\ \\cline{2-3}  
& P3-006 & \`\`Some leaders themselves aren't fully aware of what's required of them.'' \\\\ \\cline{2-3}  
& P3-003 & \`\`Leadership tone is vital. People watch everything leaders do, so leaders must model good security behavior.'' \\\\ \\hline

\\multirow{14}{3.5cm}{\\textbf{Phase 2: Organisational Culture Support}}   
& P3-005 & \`\`These physical symbolisms... if you don't see them, you forget them. If you see them one, two, three times, they stick in your mind.'' \\\\ \\cline{2-3}  
& P3-004 & \`\`Posters are important but must be concise... placement matters.'' \\\\ \\cline{2-3}  
& P3-006 & \`\`Physical reminders lose effectiveness... they must be refreshed or updated to maintain awareness.'' \\\\ \\cline{2-3}  
& P3-003 & \`\`Leaders often don't act on organisational values... this confuses staff and weakens the impact of rules.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`Unless values are explicitly tied to cybersecurity, the link feels weak.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`If security is simpler, people are more likely to follow it. As threats grow complex, people can get burnt out.'' \\\\ \\cline{2-3}  
& P3-005 & \`\`You will be evaluated based on your KPIs, and cybersecurity is not there. So why should I focus on reading those emails?'' \\\\ \\cline{2-3}  
& P3-005 & \`\`If culture punishes honesty... people will just put it under the carpet. We should appreciate honesty over perfection.'' \\\\ \\cline{2-3}  
& P3-006 & \`\`Trust is critical in how incidents are reported. If they don't trust IT to handle it fairly, they won't report it.'' \\\\ \\cline{2-3}  
& P3-001 & \`\`If you want people to report things, they need to know that they won't be in trouble for making an honest mistake.'' \\\\ \\cline{2-3}  
& P3-002 & \`\`Compliance fatigue is real... people look for workarounds whenever possible. We see it in many areas, not just cybersecurity.'' \\\\ \\cline{2-3}  
& P3-006 & \`\`If something is easy, people do it. If hard, they avoid it. It's all about the \`path of least resistance.' '' \\\\ \\cline{2-3}  
& P3-007 & \`\`People feel embarrassed after mistakes... that hesitation is where the danger lies because the issue might be significant.'' \\\\ \\cline{2-3}  
& P3-005 & \`\`Blaming culture prevents reporting... honest reporting should be valued to prevent larger-scale risks.'' \\\\ \\cline{2-3}  
& P3-003 & \`\`Embarrassment is a huge factor in why people stay silent after a breach... we need to normalise reporting mistakes.'' \\\\ \\cline{2-3}  
& P3-002 & \`\`People are not interested in policies unless there is a direct reason. They are often long and written in technical or legal language.'' \\\\ \\cline{2-3}  
& P3-005 & \`\`Without context, people think it does not matter. It's about making it relevant to people's daily work.'' \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

   
\\clearpage

\\setcounter{section}{0}  
\\setcounter{subsection}{0}  
\\setcounter{table}{0}  
\\setcounter{figure}{0}

\\renewcommand{\\thesection}{G.\\arabic{section}}  
\\renewcommand{\\thesubsection}{G.\\arabic{section}.\\arabic{subsection}}  
\\renewcommand{\\thefigure}{G.\\arabic{figure}}  
\\renewcommand{\\thetable}{G.\\arabic{table}}

   
\\makeatletter  
\\phantomsection  
\\def\\@currentlabel{G}  
\\label{appendix:G}  
\\makeatother

\\addcontentsline{toc}{chapter}{G: Chapter 8 \- Research Contribution Supporting Data}  
\\markboth{APPENDIX G}{APPENDIX G}

\\begin{center}  
    {\\Large \\textbf{Appendix G}\\par}  
    % \\vspace{1.5em}  
    % {\\Large \\textbf{Phase 1 Documents}\\par}  
\\end{center}  
   
\\noindent Appendix G provides supplementary data supporting Chapter 8, including full participant quotations for mental model characteristics, the Cybersecurity Mental Model Evaluation Checklist, and the Organisational Cybersecurity Readiness Checklist.

\\section\*{\\textbf{G.1 Mental Model Characteristics: Supporting Quotations:}}

Supporting Chapter\~\\ref{chapter:c8}, Table G.1 illustrates mental model characteristics derived from research participants, with sample quotations and supporting participant identifiers for each mindset.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{3cm} p{6cm} p{4cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Mental Model Characteristics: Supported Participants and Full Quotations}  
\\label{tab:G.1}  
}  
\\\\

\\hline  
\\textbf{Characteristic} & \\textbf{Characteristic Supporting Sample Quotations} & \\textbf{Supported Participants} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Characteristic} & \\textbf{Characteristic Supporting Sample Quotations} & \\textbf{Supported Participants} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

\\multirow{3}{3cm}{Experiential Learner} & P1-002: \`\`Around a quarter of the information from these trainings proves to be useful for me based on my past experiences'' & \\multirow{3}{3cm}{P1-002, 006; P2-001; P3-001, 003} \\\\ \\cline{2-2}  
& P1-006: \`\`My previous working experience helped me to shape my behaviour definitely, so that's why I am not using reading all these policies.'' & \\\\ \\cline{2-2}  
& P2-001: \`\`My action is based on my experience'' & \\\\ \\hline

\\multirow{2}{3cm}{Responsibility Delegator} & \`\`I trust that the \[organisation\] tools and software I use have built-in privacy and encryption technologies'' (P1-002) & \\multirow{2}{3cm}{P1-001, 002, 004; P3-002} \\\\ \\cline{2-2}  
& \`\`If we already put it in the storage... it is \[the organisation\] who is responsible'' (P1-001). & \\\\ \\hline

\\multirow{3}{3cm}{Vigilant Verifier} & \`\`If I click and see it, there's a probability something is going on or wrong, so I don't proceed further'' (P1-004). & \\multirow{3}{3cm}{P1-001, 004, 006; P3-001} \\\\ \\cline{2-2}  
& \`\`First thing will be as I have mentioned, how badly affected I am. I shall assess that first. If I am not affected then I will not bother about this.'' (P1-006) & \\\\ \\cline{2-2}  
& \`\`That's not like really big deals cause, I feel like I know how to prevent some something that...'' (P1-001). & \\\\ \\hline

\\multirow{4}{3cm}{Overwhelmed Avoider} & \`\`I never encrypted any file... it defeats the purpose'' (P1-004). & \\multirow{4}{3cm}{P1-004; P2-001; P3-002, 004} \\\\ \\cline{2-2}  
& \`\`I have to switch to something which is more convenient'' (P1-004). & \\\\ \\cline{2-2}  
& \`\`There's so much training... and yet it's mandatory'' (P2-001). & \\\\ \\cline{2-2}  
& \`\`Okay, it has been shown that getting people to update them too frequently is not a good idea.'' (P2-001) & \\\\ \\hline

\\multirow{1}{3cm}{Pragmatic Trade-off Maker} & \`\`We are busy, very busy... it is also required, but also wasting time'' when describing training and phishing controls (P2-007). & \\multirow{1}{3cm}{P1-007; P2-002, 005; P3-001, 002, 004, 006} \\\\ \\hline

\\multirow{3}{3cm}{Ethical Complier} & \`\`You have to make a decision from your mind... not necessarily following social norms or rules, but what you think is fair.'' (P2-007) & \\multirow{3}{3cm}{P1-005, 007; P2-007} \\\\ \\cline{2-2}  
& \`\`I think it almost comes out of common sense'' (P1-005) & \\\\ \\cline{2-2}  
& \`\`I usually go for ethical things'' (P1-007). & \\\\ \\hline

\\multirow{2}{3cm}{Embarrassment-Averse Reporter} & \`\`If they are the source of a security breach, \[they\] would be very embarrassed'' (P2-002) & \\multirow{2}{3cm}{P2-002; P3-001, 002, 004, 006, 007} \\\\ \\cline{2-2}  
& \`\`Definitely, I think... especially maybe because we were very multicultural... so, I think culture would come into play, but also the personality.'' (P2-002) & \\\\ \\hline

\\multirow{2}{3cm}{Leadership-Dependent Follower} & \`\`It will be more efficient if we can just get the directions directly from our supervisor'' (P1-001). & \\multirow{2}{3cm}{P1-001, 004, 006; P2-005, 006; P3-001, 002, 003, 004, 005} \\\\ \\cline{2-2}  
& \`\`No, no one gave me, absolutely no one'' (P1-004) & \\\\ \\hline

\\multirow{3}{3cm}{Training-Detached Completer} & \`\`It really feels, it's pushed so heavily that we don't take it seriously anymore because I've done this 100 times before.'' (P2-001) & \\multirow{3}{3cm}{P1-002, 003, 004, 005, 006; P2-001, 002; P3-001, 002, 003, 006, 007} \\\\ \\cline{2-2}  
& \`\`It's really for us. It's a box-ticking exercise at that time, and it's boring'' (P2-002). & \\\\ \\cline{2-2}  
& \`\`...more of a five-minute hassle that you just got to go next next next next and then sit a small test.'' (P2-002) & \\\\ \\hline

\\multirow{2}{3cm}{Policy-Detached Operator} & \`\`I did not search... I did not read all those things because I don't feel comfortable reading those kinds of policy things'' (P1-006). & \\multirow{2}{3cm}{P1-001, 002, 004, 005, 006, 007; P2-002, 005, 008; P3-001, 002, 004, 005, 006, 007} \\\\ \\cline{2-2}  
& \`\`They're just... not great fun reading'' (P1-005). & \\\\ \\hline

\\multirow{3}{3cm}{Relationship-Sensitive Actor} & \`\`It depends on the trust'' (P1-001) & \\multirow{3}{3cm}{P1-001, 005; P2-002, 003, 004, 005; P3-001, 004} \\\\ \\cline{2-2}  
& \`\`If there was not a feeling of trust between employees... then that would definitely impact that relationship.'' (P2-002) & \\\\ \\cline{2-2}  
& \`\`The relationship that you have with your team... does impact our cybersecurity'' (P2-003). & \\\\ \\hline

\\multirow{2}{3cm}{Restriction-Frustrated Resister} & \`\`They gave me a computer, which has just turned into a paperweight... I don't use it because I can't... I think it's an unnecessary restriction'' (P2-004) & \\multirow{2}{3cm}{P2-003, 004, 005, 007; P3-001, 003} \\\\ \\cline{2-2}  
& \`\`Will struggle when we get, like a research computer... was spent plenty of money on this machine to be able to install research software on it.'' (P2-005) & \\\\ \\hline

\\multirow{2}{3cm}{Compliance-Fatigued Adapter} & \`\`I am really struggling with the result of this policy \[new system implementation\]'' (P2-005) & \\multirow{2}{3cm}{P1-001, 006; P2-001, 005, 007; P3-001, 002, 005, 007} \\\\ \\cline{2-2}  
& \`\`Rather than making it mandatory, this could be optional, and the user will select if it is required.'' (P2-007) & \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

  

\\section\*{\\textbf{G.2 Cybersecurity Mental Model Evaluation System:}}

\\noindent This appendix provides an operational checklist based on thirteen cybersecurity mental model characteristics validated across Phases 1-3 (see Section\\ref{sec:8.3.1}). It supports organisational reflection, induction, and supervisory analysis, not just individual performance ratings. Leaders and supervisors can use it to identify dominant mindsets and highlight where support, clarity, or structural change is needed, guiding conversations about workload, leadership signals, training, and system usability in line with the study’s focus on organisational responsibility for readiness.

\\paragraph{Evaluation Details:}  
The checklist uses a simple score system so respondents can note how often each statement reflects typical behaviour, supporting consistent use without suggesting precise measurement. Scores were evaluated for each mindset characteristic: A higher score indicates that additional support is required, whereas a lower score reflects stronger alignment with policy expectations (Tables G.2 and G.3).

This study provides three illustrative example samples (Figure G.1, G.2, G.3) evaluation views below, including an example score interpretation and a sample evaluation summary, to demonstrate practical use of the checklist in organisational settings.

\\paragraph{Example score interpretations from the evaluation system are as follows:}

\\begin{itemize}  
    \\item \\textbf{Score (0-13): Low Cultural Friction:} \\\\  
    Security alignment is relatively strong. (Existing supports appear sufficient).  
      
    \\item \\textbf{Score (14-26): Moderate Risk:} \\\\  
    Behavioural gaps identified in daily habits. (Adjustment is required)  
      
    \\item \\textbf{Score (27-39): High Risk:} \\\\  
    Significant disconnect between policy and practice.\\\\  
\\end{itemize}

   
% \\paragraph{Data Format To utilise:\\\\}

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{2cm} p{3cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Scoring Scale and Interpretation}  
\\label{tab:G.2}  
}  
\\\\

\\hline  
\\textbf{Score} & \\textbf{Interpretation} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Score} & \\textbf{Interpretation} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

0 & Rarely \\\\ \\hline  
1 & Occasionally \\\\ \\hline  
2 & Frequently \\\\ \\hline  
3 & Strongly or consistently \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{12cm} p{2cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Mental Model Assessment Sample Questions and Scoring}  
\\label{tab:G.3}  
}  
\\\\

\\hline  
\\textbf{Mind Set (Question)} & \\textbf{Score} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Mind Set (Question)} & \\textbf{Score} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

Do individuals rely more on past experience than formal training or policy when making cybersecurity decisions? & \\\\ \\hline  
Do staff assume cybersecurity is primarily the responsibility of IT or the organisation? & \\\\ \\hline  
Do individuals prioritise personal judgement over organisational procedures when suddenly facing a threat? & \\\\ \\hline  
Are security tasks avoided when they feel too complex, unclear, or time-consuming? & \\\\ \\hline  
Is it difficult to prioritise security when workload pressure increases? & \\\\ \\hline  
Do individuals act based on personal ethics or judgement when supervision is absent? & \\\\ \\hline  
Are incidents avoided or unreported due to fear of judgement or blame? & \\\\ \\hline  
Does secure behaviour improve only when supervisors actively reinforce expectations? & \\\\ \\hline  
Does security training feel like a box-ticking or time-wasting activity? & \\\\ \\hline  
Are policies known to exist but rarely consulted during daily work? & \\\\ \\hline  
Does willingness to report or seek help depend on trust or relationships with colleagues or managers? & \\\\ \\hline  
Do restrictive organisational controls lead to workarounds or conflict with individual behaviour? & \\\\ \\hline  
Do repeated reminders or mandatory steps lead to disengagement over time? & \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

\\clearpage  
\\noindent  
\\textbf{Figure G.1}\\\\\[1em\]  
\\textit{Sample Example Evaluation Scoring view (A)}\\\\   
 \\begin{center}  
\\includegraphics\[width=0.6\\linewidth\]{Figures/appendix/I\_evolu0.1.png}  
\\end{center}

% \\vspace{1em}

\\begin{center}  
\\includegraphics\[width=0.7\\linewidth\]{Figures/appendix/I\_evolu0.2.png}  
\\end{center}

\\clearpage  
\\noindent  
\\textbf{Figure G.2}\\\\\[1em\]  
\\textit{Sample Example Evaluation Scoring view (B)}\\\\   
 \\begin{center}  
\\includegraphics\[width=0.6\\linewidth\]{Figures/appendix/I\_evolu1.1.png}  
\\end{center}

% \\vspace{1em}

\\begin{center}  
\\includegraphics\[width=0.6\\linewidth\]{Figures/appendix/I\_evolu1.2.png}  
\\end{center}

\\clearpage  
\\noindent  
\\textbf{Figure G.3}\\\\\[1em\]  
\\textit{Sample Example Evaluation Scoring view (C)}\\\\   
 \\begin{center}  
\\includegraphics\[width=0.6\\linewidth\]{Figures/appendix/I\_evolu2.1.png}  
\\end{center}

% \\vspace{1em}

\\begin{center}  
\\includegraphics\[width=0.6\\linewidth\]{Figures/appendix/I\_evolu2.2.png}  
\\end{center}

\\section\*{\\textbf{G.3 Organisational Cybersecurity Readiness Checklist:}}

To support Chapter\~\\ref{chapter:c8} (Section\~\\ref{sec:8.4.2}), Table G.4, G.5 and G.6 illustrate the evaluation criteria for the organisational cybersecurity readiness checklist.\\\\

\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{3cm} p{3cm} p{8cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Checklist Evaluation Criteria}  
\\label{tab:G.4}  
}  
\\\\

\\hline  
\\textbf{Score (Number of responses)} & \\textbf{Readiness Level} & \\textbf{Interpretation and Action Required} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Score (Number of responses)} & \\textbf{Readiness Level} & \\textbf{Interpretation and Action Required} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

8.0-10.0 & High & Strong cybersecurity readiness. Maintain current practices and continue regular review and improvement. \\\\ \\hline  
5.0-7.9 & Moderate & Adequate readiness with identifiable gaps. Focus on improving lower-scoring areas through targeted actions. \\\\ \\hline  
3.0-4.9 & Low & Partial readiness. Significant weaknesses exist; prioritise corrective actions in critical areas. \\\\ \\hline  
0.0-2.0 & Very Low & Inadequate readiness. Immediate and comprehensive intervention required, including a full organisational review. \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 \\vspace{1em}  
   
\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{5cm} p{3cm} p{6cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Total Calculation and Points System}  
\\label{tab:G.5}  
}  
\\\\

\\hline  
\\textbf{Total Calculation} & \\textbf{Responses} & \\textbf{Points System} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{Total Calculation} & \\textbf{Responses} & \\textbf{Points System} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

\\multirow{4}{5cm}{Total Score \= (Sum of all responses $\\div$ 18\) $\\times$ 10}   
& Yes & 1 Point \\\\ \\cline{2-3}  
& Partly & 0.1 Point \\\\ \\cline{2-3}  
& No & 0 Point \\\\ \\cline{2-3}  
& Not applicable & Leave blank (do not count in the denominator) \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 \\vspace{1em}  
   
\\captionsetup{  
    labelfont=bf,  
    justification=raggedright,  
    singlelinecheck=false,  
    labelsep=none,  
    font={stretch=1.3}  
}

\\begingroup  
\\small  
\\begin{spacing}{1.0}  
\\begin{longtable}{p{1cm} p{3.2cm} p{3.2cm} p{6.6cm}}

\\caption\[\]{%  
\\\\\[1.2em\]  
\\textit{Organisation Readiness Assessment Checklist}  
\\label{tab:org\_readiness\_checklist}  
}  
\\\\

\\hline  
\\textbf{No.} & \\textbf{Category} & \\textbf{Response} & \\textbf{Assessment Question} \\\\ \\hline  
\\endfirsthead

\\hline  
\\textbf{No.} & \\textbf{Category} & \\textbf{Response} & \\textbf{Assessment Question} \\\\ \\hline  
\\endhead

\\hline  
\\endlastfoot

1 & Awareness / Policy clarity & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Are cybersecurity expectations clearly explained for different roles so staff understand what is required in their daily work? \\\\ \\hline

2 & Training / Learning & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Is training based on real work situations and recent incidents so staff can apply what they learn? \\\\ \\hline

3 & Risk Awareness & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do staff understand how cybersecurity risks can affect their work, students, or the organisation? \\\\ \\hline

4 & Reporting / Access & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Is it easy for staff to report a cybersecurity issue at the time it happens, without confusion? \\\\ \\hline

5 & Confidence / Support & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do staff feel supported and confident when they need to take action during a cybersecurity issue? \\\\ \\hline

6 & Workflow / Usability & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Are security steps built into systems and tools so staff do not need to search for policies separately? \\\\ \\hline

7 & Behaviour under Pressure & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do staff follow secure practices even when they are busy, or do they skip steps under pressure? \\\\ \\hline

8 & Leadership Behaviour & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do leaders show expected cybersecurity behaviour through their actions, not just words? \\\\ \\hline

9 & Accountability & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Is it clear who is responsible for cybersecurity decisions and actions across the organisation? \\\\ \\hline

10 & Policy Clarity & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Are policies easy to find, easy to understand, and useful when staff need them? \\\\ \\hline

11 & Values Alignment & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do organisational values, for example speed and flexibility, support security, or do they sometimes conflict with it? \\\\ \\hline

12 & Culture / Emotion & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do staff avoid reporting issues because of fear, embarrassment, or concern about being judged? \\\\ \\hline

13 & Trust / Leadership & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do staff trust that leaders will handle cybersecurity issues fairly and supportively? \\\\ \\hline

14 & Onboarding & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Do new staff receive clear and practical cybersecurity guidance when they join? \\\\ \\hline

15 & Governance & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Are rules, processes, and decision pathways clear and applied consistently across teams? \\\\ \\hline

16 & Work Conditions & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Are workload and time pressure considered when security processes are designed? \\\\ \\hline

17 & Communication & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Are cybersecurity messages clear, relevant, and not overwhelming for staff? \\\\ \\hline

18 & Improvement / Monitoring & $\\square$ Yes \\quad $\\square$ Partly \\quad $\\square$ No & Does the organisation regularly review behaviour, for example reporting and compliance, and improve based on it? \\\\ \\hline

\\end{longtable}  
\\end{spacing}  
\\endgroup

 

 

 

Reference:

 

%============================= chapters 1====================================

@misc{HFK2025,  
  author \= {{HFK}},  
  title \= {Cyber security: A month in retrospect (Australia) \- February 2025},  
  institution \= {Herbert Smith Freehills Kramer},  
  year \= {2025},  
  month \= {March},  
  url \= {https://www.hsfkramer.com/notes/cybersecurity/2025-posts/cyber-security-a-month-in-retrospect-australia-february-2025},  
  note \= {Accessed March 6, 2025}  
}

@techreport{WEF2025,  
  author \= {{WEF}},  
  title \= {{Global Cybersecurity Outlook 2025}},  
  institution \= {World Economic Forum},  
  year \= {2025},  
  note \= {Emerging themes: culture, compliance fatigue, geopolitical risk}  
}

@article{Aldaajeh2022,  
  author \= {AlDaajeh, Saleh and Saleous, Heba and Alrabaee, Saed and Barka, Ezedin and Breitinger, Frank and Choo, Kim-Kwang Raymond},  
  title \= {The role of national cybersecurity strategies on the improvement of cybersecurity education},  
  journal \= {Computers and Security},  
  volume \= {119},  
  pages \= {102754},  
  year \= {2022},  
  doi \= {10.1016/j.cose.2022.102754}  
}

@article{Sandi2025,  
  author \= {Sandi, S. and Berg, van den., C. L.},  
  title \= {Cybersecurity mindset and upskilling: Resilience via lifelong learning and security education},  
  journal \= {South African Journal of Information Management},  
  year \= {2025},  
  volume \= {27},  
  number \= {1},  
  pages \= {12},  
  doi \= {10.4102/sajim.v27i1.2044}  
}

 

@article{lallie2025,  
  author \= {Lallie, Harjinder Singh and Thompson, A. and Titis, E. and Stephens, P.},  
  title \= {Analysing Cyber Attacks and Cyber Security Vulnerabilities in the University Sector},  
  journal \= {Computers},  
  volume \= {14},  
  number \= {2},  
  pages \= {49},  
  year \= {2025},  
  publisher \= {MDPI},  
  doi \= {10.3390/computers14020049},  
  url \= {https://doi.org/10.3390/computers14020049}  
}

@article{morrow2024,  
  author \= {Morrow, E.},  
  title \= {Scamming higher ed: An analysis of phishing content and trends},  
  journal \= {Computers in Human Behavior},  
  volume \= {158},  
  pages \= {108274},  
  year \= {2024},  
  doi \= {10.1016/j.chb.2024.108274},  
  url \= {https://doi.org/10.1016/j.chb.2024.108274}  
}

@misc{crozier2022,  
  author \= {Crozier, R.},  
  title \= {Deakin University reveals breach of 47,000 students’ details},  
  year \= {2022},  
  howpublished \= {ITNews},  
  note \= {Online Article}  
}

@article{paganini2022,  
  author \= {Paganini, Pierluigi},  
  title \= {Cybersecurity in Education: Why Academics are Targeted},  
  journal \= {Infosec Magazine},  
  year \= {2022},  
  note \= {Trends in cyber-attacks on universities and research institutions},  
  url \= {https://www.infosecinstitute.com/blog/cybersecurity-in-education/}  
}

@article{acsm2021,  
  author \= {{ACSM}},  
  title \= {Education Sector Sees 29\\% Increase in Attacks Against Organisations Globally},  
  journal \= {Australian Cyber Security Magazine},  
  year \= {2021},  
  month \= {August},  
  day \= {23},  
  url \= {https://australiancybersecuritymagazine.com.au/education- sector- sees- 29- increase- in- attacks- against- organisations- globally/}  
}

@misc{CPR2026,  
  author \= {{CPR}},  
  title \= {Global Cyber Attacks Rise in January 2026 Amid Increasing Ransomware Activity and Expanding GenAI Risks},  
  year \= {2026},  
  publisher \= {Check Point Research},  
  note \= {Industry report}  
}

@article{houser2025,  
  author \= {Houser, A. M. and Bolton, M. L.},  
  title \= {Formal Mental Models for Human-Centered Cybersecurity},  
  journal \= {International Journal of Human--Computer Interaction},  
  year \= {2025},  
  url \= {https://www.tandfonline.com/doi/abs/10.1080/10447318.2024.2314353}  
}

@article{saucier2025,  
  author  \= {Saucier, C. J. and Dobmeier, C. M.},  
  title   \= {A mental models approach to communication: Integrating the features, functions, and mechanisms of mental modeling},  
  journal \= {Communication Theory},  
  volume  \= {35},  
  number  \= {4},  
  pages   \= {250--260},  
  year    \= {2025},  
  doi     \= {10.1093/ct/qtaf012}  
}

@article{espinosa2023,  
  author \= {Espinosa, T. T. and Simmers, K. and Batchelor, D. and Nelson, A. D. and Borja, C.},  
  title \= {A Theory of Mental Frameworks},  
  journal \= {Frontiers in Psychology},  
  year \= {2023},  
  volume \= {14},  
  pages \= {1220664},  
  doi \= {10.3389/fpsyg.2023.1220664}  
}

@article{lamere2020,  
  author \= {LaMere, K. and Mäntyniemi, S. and Vanhatalo, J. and Haapasaari, P.},  
  title \= {Making the most of mental models: Advancing the methodology for mental model elicitation and documentation with expert stakeholders},  
  journal \= {Environmental Modelling \\& Software},  
  year \= {2020},  
  volume \= {124},  
  pages \= {104589},  
  doi \= {10.1016/j.envsoft.2019.104589}  
}  
@article{Rouse1986,  
  author \= {Rouse, William B. and Morris, Nancy M.},  
  title \= {On looking into the black box: Prospects and limits in the search for mental models},  
  journal \= {Psychological Bulletin},  
  volume \= {100},  
  number \= {3},  
  pages \= {349--363},  
  year \= {1986},  
  doi \= {10.1037/0033-2909.100.3.349},  
  url \= {https://doi.org/10.1037/0033-2909.100.3.349}  
}

 

@techreport{ASD2025,  
  author \= {{ASD}},  
  title \= {Annual Cyber Threat Report 2024--2025},  
  institution \= {Australian Signals Directorate},  
  year \= {2025},  
  url \= {https://www.cyber.gov.au/about-us/reports-and-statistics},  
  note \= {Cybersecurity insights and incident statistics}  
}  
 

@misc{CPR2025,  
  author \= {{CPR}},  
  title \= {Q1 2025 Global Cyber Attack Report from {Check Point Software}: An Almost 50\\% Surge in Cyber Threats Worldwide, with a Rise of 126\\% in Ransomware Attacks},  
  howpublished \= {Check Point Blog},  
  year \= {2025},  
  month \= {April 16},  
  url \= {https://blog.checkpoint.com/research/q1-2025-global-cyber-attack-report-from-check-point-software-an-almost-50-surge-in-cyber-threats-worldwide-with-a-rise-of-126-in-ransomware-attacks/},  
  note \= {Check Point Research, Accessed March 11, 2026}  
}  
@article{alshaikh2020,  
 author \= {Alshaikh, Moneer},  
 title \= {Developing cybersecurity culture to influence employee behavior},  
 journal \= {Information and Computer Security},  
 year \= {2020},  
 volume \= {28},  
 number \= {3},  
 pages \= {337--358},  
 doi \= {10.1108/ICS-07-2019-0083}  
}  
@article{khadka2025,  
  author       \= {Khadka, Kalam and Ullah, Abu Barkat},  
  title        \= {Human factors in cybersecurity: an interdisciplinary review and framework proposal},  
  journal      \= {International Journal of Information Security},  
  volume       \= {24},  
  number       \= {3},  
  pages        \= {119},  
  year         \= {2025},  
  doi          \= {10.1007/s10207-025-01032-0}  
}

@article{cheng2022,  
  title={Institutional strategies for cybersecurity in higher education institutions},  
  author={Cheng, Eric CK and Wang, Tianchong},  
  journal={Information},  
  volume={13},  
  number={4},  
  pages={192},  
  year={2022},  
  publisher={MDPI}  
}

@article{xie2025,  
  author       \= {Xie, Yuntian and others},  
  title        \= {How do mental models affect cybersecurity awareness? The roles of questioning styles, need for cognition, and graphical representations},  
  journal      \= {Computers and Security},  
  year         \= {2025},  
  doi          \= {10.1016/j.cose.2024.104292}  
}

@article{alge2006impact,  
  author       \= {Alge, Bradley J. and Ballinger, Gary A. and Tangirala, Subrahmaniam and Oakley, John L.},  
  title        \= {Information Privacy in Organizations: Empowering Creative and Extra‑role Performance},  
  journal      \= {Journal of Applied Psychology},  
  volume       \= {91},  
  number       \= {1},  
  pages        \= {221--232},  
  year         \= {2006},  
  doi          \= {10.1037/0021-9010.91.1.221},  
    
}  
   
@article{tolsdorf2020,  
  title={Interviews in qualitative information systems research: A categorization of interview types and guidelines for researchers},  
  author={Tolsdorf, Jan and Dehling, Tobias},  
  journal={AIS Transactions on Human-Computer Interaction},  
  volume={12},  
  number={4},  
  pages={204--229},  
  year={2020},  
  publisher={Association for Information Systems},  
  doi={10.17705/1thci.00133}  
}

 @article{georgiadou2022,  
  author       \= {Georgiadou, Anna and Mouzakitis, Spiros and Bounas, Kanaris and Askounis, Dimitrios},  
  title        \= {A cyber‑security culture framework for assessing organization readiness},  
  journal      \= {Journal of Computer Information Systems},  
  volume       \= {62},  
  number       \= {3},  
  pages        \= {452--462},  
  year         \= {2022},  
  doi          \= {10.1080/08874417.2022.2051567}  
}  
@article{rogers1975,  
  author    \= {Ronald W. Rogers},  
  title     \= {A protection motivation theory of fear appeals and attitude change},  
  journal   \= {The Journal of Psychology},  
  volume    \= {91},  
  number    \= {1},  
  pages     \= {93--114},  
  year      \= {1975},  
  publisher \= {Taylor and Francis}  
}  
@book{rogers1983,  
  title={Cognitive and Physiological Processes in Fear Appeals and Attitude Change: A Revised Theory of Protection Motivation},  
  author={Rogers, Ronald W.},  
  booktitle={Social Psychophysiology: A Sourcebook},  
  editor={Cacioppo, John T. and Petty, Richard E.},  
  pages={153--176},  
  year={1983},  
  publisher={Guilford Press},  
  address={New York}  
}  
@book{Schein2017,  
  author    \= {Schein, Edgar H. and Schein, Peter A.},  
  title     \= {Organizational Culture and Leadership},  
  edition   \= {5},  
  publisher \= {Wiley},  
  year      \= {2017}  
}  
 

@article{mou2022,  
  author       \= {Mou, Xiang and others},  
  title        \= {Cybersecurity culture as a socio‑technical capability: norms, leadership and learning in organisations},  
  journal      \= {Computers and Security},  
  volume       \= {115},  
  pages        \= {102589},  
  year         \= {2022},  
  doi          \= {10.1016/j.cose.2021.102589}  
}  
@article{uchendu2021,  
  title={Developing a cyber security culture: Current practices and future needs},  
  author={Uchendu, Betsy and Nurse, Jason RC and Bada, Maria and Furnell, Steven},  
  journal={Computers and Security},  
  volume={109},  
  pages={102387},  
  year={2021},  
  publisher={Elsevier}  
}  
@article{marshall2024,  
  author \= {Marshall, N. and Sturman, D. and Auton, J. C.},  
  title \= {Exploring the evidence for email phishing training: A scoping review},  
  journal \= {Computers \\& Security},  
  volume \= {139},  
  pages \= {103695},  
  year \= {2024},  
  doi \= {10.1016/j.cose.2023.103695},  
  url \= {https://doi.org/10.1016/j.cose.2023.103695}  
}

@article{prummer2025,  
  author       \= {Pr{\\"u}mmer, J. and van Steen, T. and van den Berg, B.},  
  title        \= {Assessing the effect of cybersecurity training on End-users: A Meta-analysis},  
  journal      \= {Computers and Security},  
  volume       \= {150},  
  pages        \= {104206},  
  year         \= {2025},  
  doi          \= {10.1016/j.cose.2024.104206}  
}

@article{sutton2025,  
  author \= {Sutton, A. and Tompson, L.},  
  title \= {Towards a cybersecurity culture-behaviour framework: A rapid evidence review},  
  journal \= {Computers \\& Security},  
  volume \= {148},  
  pages \= {104110},  
  year \= {2025},  
  doi \= {10.1016/j.cose.2024.104110},  
  url \= {https://doi.org/10.1016/j.cose.2024.104110}  
}

 

@article{datta2024,  
  author={Datta, P. M. and Krancher, O.},  
  title={Cybersecurity end-user compliance: Password management versus update compliance},  
  journal={Information and Management},  
  volume={61},  
  number={8},  
  pages={104060},  
  year={2024},  
  doi={10.1016/j.im.2024.104060}  
}  
@article{patterson2023,  
  author  \= {Patterson, C. M. and Nurse, J. R. C. and Franqueira, V. N. L.},  
  title   \= {Learning from cyber security incidents: {A} systematic review and future research agenda},  
  journal \= {Computers and Security},  
  volume  \= {132},  
  pages   \= {103309},  
  year    \= {2023},  
  doi     \= {10.1016/j.cose.2023.103309}  
}  
@article{Alraja2023,  
  author \= {Alraja, M. N. and Butt, U. J. and Abbod, M.},  
  title \= {Information security policies compliance in a global setting: An employee’s perspective},  
  journal \= {Computers \\& Security},  
  year \= {2023},  
  volume \= {129},  
  pages \= {103208},  
  doi \= {10.1016/j.cose.2023.103208}  
}  
@article{Herath2009,  
  author \= {Herath, T. and Rao, H. R.},  
  title \= {Protection motivation and deterrence: A framework for security policy compliance in organisations},  
  journal \= {European Journal of Information Systems},  
  year \= {2009},  
  volume \= {18},  
  number \= {2},  
  pages \= {106--125},  
  doi \= {10.1057/ejis.2009.6}  
}

@article{Bada2019,  
  author \= {Bada, M. and Nurse, J. R. C.},  
  title \= {Developing cybersecurity education and awareness programmes for small- and medium-sized enterprises (SMEs)},  
  journal \= {Information \\& Computer Security},  
  year \= {2019},  
  volume \= {27},  
  number \= {3},  
  pages \= {393--410},  
  doi \= {10.1108/ics-07-2018-0080}  
}

@misc{bada2019cyber,  
  title={Cyber Security Awareness Campaigns: Why do they fail to change behaviour?},  
  author={Bada, Maria and Sasse, Angela Angela and Nurse, Jason R. C.},  
  year={2019},  
  publisher={arXiv},  
  note={arXiv preprint arXiv:1901.02672},  
  doi={10.48550/arXiv.1901.02672},  
  url={https://doi.org/10.48550/arXiv.1901.02672}  
}

@article{patterson2024,  
  title={"I don't think we're there yet": The practices and challenges of organisational learning from cybersecurity incidents},  
  author={Patterson, Rebecca and Shergold, Peter and McDonald, Hazel},  
  journal={Computers and Security},  
  volume={135},  
  pages={103099},  
  year={2024},  
  publisher={Elsevier}  
}

@article{ulven2021,  
  title={A Systematic Review of Cybersecurity Risks in Higher Education},  
  author={Ulven, Jørn Borchsenius and Wangen, Gaute},  
  journal={Future Internet},  
  volume={13},  
  number={2},  
  pages={39},  
  year={2021},  
  publisher={Multidisciplinary Digital Publishing Institute},  
  doi={10.3390/fi13020039},  
  url={https://doi.org/10.3390/fi13020039}  
}

@article{alsharida2023,  
  author={Alsharida, R. A. and Al-rimy, B. A. S. and Al-Emran, M. and Zainal, A.},  
  title={A systematic review of multi perspectives on human cybersecurity behavior},  
  journal={Technology in Society},  
  volume={73},  
  pages={102258},  
  year={2023},  
  doi={10.1016/j.techsoc.2023.102258}  
}  
   
@article{sharma2022,  
  author \= {Sharma, S. and Aparicio, E.},  
  title \= {Organizational and team culture as antecedents of protection motivation among IT employees},  
  journal \= {Computers \\& Security},  
  volume \= {120},  
  pages \= {102774},  
  year \= {2022},  
  doi \= {10.1016/j.cose.2022.102774},  
  url \= {https://doi.org/10.1016/j.cose.2022.102774}  
}

@article{yusif2023,  
  author  \= {Mohammed Yusif and Abdul Hafeez-Baig},  
  title   \= {An empirical study of cybersecurity awareness in higher education: Using TPB},  
  journal \= {Education and Information Technologies},  
  volume  \= {28},  
  pages   \= {12345--12367},  
  year    \= {2023},  
  doi     \= {10.1007/s10639-023-12345}  
}

@article{sabbagh2012,  
  author \= {Sabbagh, B. A. and Ameen, M. and Watterstam, T. and Kowalski, S.},  
  title \= {A Prototype For {HI2Ping} Information Security Culture and Awareness Training},  
  booktitle \= {2012 International Conference on E-Learning and E-Technologies in Education (ICEEE)},  
  pages \= {32--36},  
  year \= {2012},  
  organization \= {IEEE},  
  doi \= {10.1109/ICeLeTE.2012.6333397},  
  url \= {https://doi.org/10.1109/ICeLeTE.2012.6333397}  
}

@inproceedings{lie2021,  
  author \= {Lie, L. B. and Utomo, P. and Winarno, P. M.},  
  title \= {Investigating the Impact of Cybersecurity Culture on Employees’ Cybersecurity Protection Behaviours: A Conceptual Paper},  
  booktitle \= {Conference Series},  
  volume \= {3},  
  number \= {2},  
  pages \= {295--305},  
  year \= {2021},  
  doi \= {10.34306/conferenceseries.v3i2.598},  
  url \= {https://doi.org/10.34306/conferenceseries.v3i2.598}  
}

@article{kannelonning2023,  
  title={A systematic literature review of how cybersecurity-related behavior has been assessed},  
  author={Kannel{\\o}nning, Kristian and Katsikas, Sokratis K},  
  journal={Information and Computer Security},  
  volume={31},  
  number={4},  
  pages={463--477},  
  year={2023},  
  publisher={Emerald Publishing Limited}  
}

   
   
@article{daveiga2020,  
  title={Defining organisational information security culture—Perspectives from academia and industry},  
  author={Da Veiga, Adele and Astakhova, Liudmila V and Botha, Ad{\\'e}le and Herselman, Marlien},  
  journal={Computers and Security},  
  volume={92},  
  pages={101713},  
  year={2020},  
  publisher={Elsevier}  
}  
@article{deramos2022,  
  author    \= {De Ramos, Noly M. and Esponilla II, Francisco D.},  
  title     \= {Cybersecurity program for Philippine higher education institutions: A multiple‐case study},  
  journal   \= {International Journal of Evaluation and Research in Education},  
  volume    \= {11},  
  number    \= {3},  
  pages     \= {1198--1209},  
  year      \= {2022},  
  doi       \= {10.11591/ijere.v11i3.22863}  
}

@article{bernstein2012,  
  author \= {Bernstein, Ethan S.},  
  title \= {The Transparency Paradox: A Role for Privacy in Organizational Learning and Operational Control},  
  journal \= {Administrative Science Quarterly},  
  volume \= {57},  
  number \= {2},  
  pages \= {181--216},  
  year \= {2012},  
  doi \= {10.1177/0001839212453028},  
  url \= {https://doi.org/10.1177/0001839212453028}  
}  
@article{fenech2024,  
  author \= {Fenech, J. and Richards, D. and Formosa, P.},  
  title \= {Ethical principles shaping values-based cybersecurity decision-making},  
  journal \= {Computers \\& Security},  
  volume \= {140},  
  pages \= {103795},  
  year \= {2024},  
  doi \= {10.1016/j.cose.2024.103795},  
  url \= {https://doi.org/10.1016/j.cose.2024.103795}  
}  
   
   
@article{fatoki2024,  
  author={Fatoki, J. G. and Shen, Z. and Mora-Monge, C. A.},  
  title={Optimism amid risk: How non-IT employees’ beliefs affect cybersecurity behavior},  
  journal={Computers and Security},  
  volume={141},  
  pages={103812},  
  year={2024},  
  doi={10.1016/j.cose.2024.103812}  
}  
   
 

@article{bhana2023,  
  author \= {Bhana, A. and Ophoff, J.},  
  title \= {Risk homeostasis and security fatigue: A case study of data specialists},  
  journal \= {Information and Computer Security},  
  volume \= {31},  
  number \= {3},  
  pages \= {267--280},  
  year \= {2023},  
  doi \= {10.1108/ICS-11-2022-0172},  
  url \= {https://doi.org/10.1108/ICS-11-2022-0172}  
}

 @article{Albinali2025,  
  author \= {Albinali, M. and Niazi, M. and Alshayeb, M. and Mahmood, S. and Khan, A. A.},  
  title \= {Taxonomy-based approach for understanding and enhancing security culture in universities},  
  journal \= {PeerJ Computer Science},  
  volume \= {11},  
  pages \= {e3005},  
  year \= {2025},  
  doi \= {10.7717/peerj-cs.3005},  
  url \= {https://doi.org/10.7717/peerj-cs.3005}  
}

@article{Ramos2022,  
  author \= {Ramos, N. M. and Esponilla II, F. D.},  
  title \= {Cybersecurity program for {Philippine} higher education institutions: A multiple-case study},  
  journal \= {International Journal of Evaluation and Research in Education (IJERE)},  
  year \= {2022},  
  volume \= {11},  
  number \= {3},  
  pages \= {1198--1207},  
  doi \= {10.11591/ijere.v11i3.22863}  
}

@inproceedings{Burris2024,  
  author \= {Burris, J. W. and Regis, P.},  
  title \= {Bridging Theory and Practice: Preparing Future {IT} Service Leaders through Experiential Learning in Cybersecurity Policy and Governance},  
  booktitle \= {Proceedings of the 2024 8th International Conference on Information System and Data Mining (ICISDM '24)},  
  year \= {2024},  
  pages \= {39--43},  
  publisher \= {ACM},  
  doi \= {10.1145/3686397.3686404}  
}  
@article{Alshaikh2021Model,  
  author       \= {Alshaikh, Moneer and Adamson, Blair},  
  title        \= {From awareness to influence: toward a model for improving employees’ security behaviour},  
  journal      \= {Personal and Ubiquitous Computing},  
  volume       \= {25},  
  number       \= {5},  
  pages        \= {829--841},  
  year         \= {2021},  
  doi          \= {10.1007/s00779-021-01551-2},  
  note         \= {}  
}

@article{Alshaikh2021Journal,  
  title \= {Applying social marketing to evaluate current security education training and awareness programs in organisations},  
  author \= {Alshaikh, M. and Maynard, S. B. and Ahmad, A.},  
  journal \= {Computers \\& Security},  
  volume \= {100},  
  pages \= {102090},  
  year \= {2021},  
  doi \= {10.1016/j.cose.2020.102090},  
  url \= {https://doi.org/10.1016/j.cose.2020.102090}  
}

@article{schaik2020,  
  author    \= {Paul van Schaik and Andrea Junger and Kenneth H. D. M. Wong and Linda Turner},  
  title     \= {Cyber security awareness and behaviour: A comparative study},  
  journal   \= {Computers in Human Behavior},  
  volume    \= {111},  
  pages     \= {106421},  
  year      \= {2020},  
  publisher \= {Elsevier},  
  doi       \= {10.1016/j.chb.2020.106421}  
}  
@article{jan2020,  
  author={Jan, V. den B.},  
  title={A Basic Set of Mental Models for Understanding and Dealing with the Cyber-Security Challenges of Today},  
  journal={Journal of Information Warfare},  
  volume={19},  
  number={1},  
  pages={26--47},  
  year={2020}  
}  
 

@incollection{Daveiga2022,  
  author \= {Da Veiga, A.},  
  title \= {A Model for Information Security Culture with Innovation and Creativity as Enablers},  
  booktitle \= {Information Security Education – Education in Depth},  
  editor \= {Clarke, N. and Furnell, S.},  
  series \= {IFIP Advances in Information and Communication Technology},  
  volume \= {658},  
  pages \= {186--196},  
  year \= {2022},  
  publisher \= {Springer International Publishing},  
  address \= {Cham},  
  doi \= {10.1007/978-3-031-12172-2\_14},  
  url \= {https://doi.org/10.1007/978-3-031-12172-2\_14}  
}

@article{ahmad2019,  
  author={Ahmad, A. and Desouza, K. C. and Maynard, S. B. and Naseer, H. and Baskerville, R. L.},  
  title={How integration of cyber security management and incident response enables organizational learning},  
  journal={Journal of the Association for Information Science and Technology},  
  volume={71},  
  number={8},  
  pages={939--953},  
  year={2019},  
  doi={10.1002/asi.24311}  
}  
@article{Singh2024,  
  author \= {Singh, C. M. and Musikavanhu, T. B.},  
  title \= {A Narrative Review on Enhancing Cybersecurity in Higher Education Institutions: The Role of Continuous Training and Awareness},  
  journal \= {Expert Journal of Business and Management},  
  year \= {2024},  
  volume \= {12},  
  number \= {2},  
  pages \= {67--73},  
  url \= {http://businessandmanagement.expertjournals.com/ark:/16759/EJB\_1207singh67-73.pdf}  
}

 @article{fouad2021,  
  author={Fouad, N. S.},  
  title={Securing higher education against cyberthreats: From an institutional risk to a national policy challenge},  
  journal={Journal of Cyber Policy},  
  volume={6},  
  number={2},  
  pages={137--154},  
  year={2021},  
  doi={10.1080/23738871.2021.1973526}  
}

@article{Hillman2023,  
  author={Hillman, D. and Harel, Y. and Toch, E.},  
  title={Evaluating organizational phishing awareness training on an enterprise scale},  
  journal={Computers and Security},  
  volume={132},  
  pages={103364},  
  year={2023},  
  doi={10.1016/j.cose.2023.103364}  
}  
@book{Schein2019,  
  author \= {Schein, Edgar H. and Schein, Peter A.},  
  title \= {The Corporate Culture Survival Guide},  
  edition \= {3rd},  
  year \= {2019},  
  publisher \= {Wiley},  
  url \= {https://www.perlego.com/book/992190/the-corporate-culture-survival-guide-pdf}  
}

@article{Brooks2015,  
  author  \= {Brooks, J. and McCluskey, S. and Turley, E. and King, N.},  
  title   \= {The Utility of Template Analysis in Qualitative Psychology Research},  
  journal \= {Qualitative Research in Psychology},  
  volume  \= {12},  
  number  \= {2},  
  pages   \= {202--222},  
  year    \= {2015},  
  doi     \= {10.1080/14780887.2014.955224}  
}  
@article{Dejonckheere2019,  
  title={Semi-structured interviewing in primary care research: a balance of relationship and rigour},  
  author={DeJonckheere, Melissa and Vaughn, Lisa M.},  
  journal={Family Medicine and Community Health},  
  volume={7},  
  number={2},  
  pages={e000057},  
  year={2019},  
  publisher={BMJ Publishing Group},  
  doi={10.1136/fmch-2018-000057}  
}  
@article{Kallio2016,  
  author       \= {Kallio, Hanna and Pietilä, Anna‑Maija and Johnson, Marja and Kangasniemi, Mari},  
  title        \= {Systematic methodological review: developing a framework for a qualitative semi‑structured interview guide},  
  journal      \= {Journal of Advanced Nursing},  
  volume       \= {72},  
  number       \= {12},  
  pages        \= {2954--2965},  
  year         \= {2016},  
  doi          \= {10.1111/jan.13031}  
}

@incollection{King2017,  
  author    \= {King, N. and Brooks, J. M.},  
  title     \= {Doing Template Analysis: A Guide to the Main Components and Procedures},  
  booktitle \= {Template Analysis for Business and Management Students},  
  publisher \= {SAGE Publications Ltd},  
  pages     \= {25--46},  
  year      \= {2017},  
  doi       \= {10.4135/9781473983304}  
}

@article{Zamawe2015,  
  title={The implication of using NVivo software in qualitative data analysis: Evidence-based reflections},  
  author={Zamawe, Frederick C},  
  journal={Malawi Medical Journal},  
  volume={27},  
  number={1},  
  pages={13--15},  
  year={2015}  
}

@article{Niekerk2010,  
  author  \= {Van Niekerk, J. F. and Von Solms, R.},  
  title   \= {Information security culture: A management perspective},  
  journal \= {Computers and Security},  
  volume  \= {29},  
  number  \= {4},  
  pages   \= {476--486},  
  year    \= {2010},  
  doi     \= {10.1016/j.cose.2009.10.005}  
}  
@article{safa2015,  
  author    \= {Safa, Nader Sohrabi and Von Solms, Rossouw and Furnell, Steven},  
  title     \= {Information security policy compliance model in organizations},  
  journal   \= {Computers and Security},  
  volume    \= {56},  
  pages     \= {70--82},  
  year      \= {2015},  
  publisher \= {Elsevier},  
  doi       \= {10.1016/j.cose.2015.10.006}  
}

@article{tsai2016,  
  author       \= {Tsai, Hsin‑yi Sandy and Jiang, Mengtian and Alhabash, Saleem and LaRose, Robert and Rifon, Nora J. and Cotten, Sheila R.},  
  title        \= {Understanding online safety behaviors: A protection motivation theory perspective},  
  journal      \= {Computers and Security},  
  volume       \= {59},  
  pages        \= {138--150},  
  year         \= {2016},  
  doi          \= {10.1016/j.cose.2016.06.009}  
}  
 

   
@article{alge2006,  
  author       \= {Alge, Bradley J. and Ballinger, Gary A. and Tangirala, Subrahmaniam and Oakley, John L.},  
  title        \= {Information Privacy in Organizations: Empowering Creative and Extra‑role Performance},  
  journal      \= {Journal of Applied Psychology},  
  volume       \= {91},  
  number       \= {1},  
  pages        \= {221--232},  
  year         \= {2006},  
  doi          \= {10.1037/0021-9010.91.1.221},  
   
}  
@article{Aliyu2020,  
  title={A holistic cybersecurity maturity assessment framework for higher education institutions in the United Kingdom},  
  author={Aliyu, Aliyu and Maglaras, Leandros and He, Ying and Yevseyeva, Iryna and Boiten, Eerke and Cook, Allan and Janicke, Helge},  
  journal={Applied Sciences},  
  volume={10},  
  number={10},  
  pages={3660},  
  year={2020},  
  publisher={MDPI}  
}  
@article{Hasan2021,  
  author={Hasan, S. and Ali, M. and Kurnia, S. and Thurasamy, R.},  
  title={Evaluating the cyber security readiness of organizations and its influence on performance},  
  journal={Journal of Information Security and Applications},  
  volume={58},  
  year={2021},  
  doi={10.1016/j.jisa.2020.102726}  
}  
@article{Ozkan2021,  
  author  \= {Ozkan, B. Y. and van Lingen, S. and Spruit, M.},  
  title   \= {The Cybersecurity Focus Area Maturity ({CYSFAM}) Model},  
  journal \= {Journal of Cybersecurity and Privacy},  
  volume  \= {1},  
  number  \= {1},  
  pages   \= {119--139},  
  year    \= {2021},  
  doi     \= {10.3390/jcp1010007}  
}

@article{Dienlin2015,  
  author={Dienlin, T. and Trepte, S.},  
  title={Is the privacy paradox a relic of the past? An in-depth analysis of privacy attitudes and privacy behaviors},  
  journal={European Journal of Social Psychology},  
  volume={45},  
  number={3},  
  pages={285--297},  
  year={2015},  
  doi={10.1002/ejsp.2049}  
}

@techreport{OAIIC2021,  
  author      \= {{OAIC}},  
  title       \= {Annual Report 2020--21},  
  institution \= {Office of the Australian Information Commissioner},  
  year        \= {2021},  
  url         \= {https://www.oaic.gov.au/about-the-OAIC/our-corporate-information/oaic-annual-reports/annual-report-202021}  
}  
@article{Anderson2010,  
  author  \= {Anderson, Catherine L. and Agarwal, Ritu},  
  title   \= {Practicing safe computing: A multimethod empirical examination of home computer user security behavioral intentions},  
  journal \= {MIS Quarterly},  
  year    \= {2010},  
  volume  \= {34},  
  number  \= {3},  
  pages   \= {613--643},  
  doi     \= {10.2307/25750694}  
}  
@techreport{Franks2020,  
  author={Franks, C. and Smith, R. G.},  
  title={Identity crime and misuse in Australia 2019},  
  institution={Australian Institute of Criminology},  
  year={2020}  
}

 

@standard{ISO2023,  
  author \= {{ISO/IEC}},  
  title \= {Information technology — Cybersecurity — Guidelines for Internet Security},  
  number \= {ISO/IEC 27032:2023},  
  edition \= {Second},  
  year \= {2023},  
  url \= {https://www.iso.org/standard/76070.html}  
}

@incollection{Murimi2023,  
  author \= {Murimi, R. and Blanke, S. and Murimi, R.},  
  title \= {A Decade of Development of Mental Models in Cybersecurity and Lessons for the Future},  
  booktitle \= {Proceedings of the International Conference on Cybersecurity, Situational Awareness and Social Media},  
  editor \= {Onwubiko, C. and Rosati, P. and Rege, A. and Erola, A. and Bellekens, X. and Hindy, H. and Jaatun, M. G.},  
  publisher \= {Springer Nature Singapore},  
  year \= {2023},  
  pages \= {105--132},  
  doi \= {10.1007/978-981-19-6414-5\_7}  
}

@article{Reidenberg2018,  
  author \= {Reidenberg, J. R. and Schaub, F.},  
  title \= {Achieving big data privacy in education},  
  journal \= {Theory and Research in Education},  
  year \= {2018},  
  volume \= {16},  
  number \= {3},  
  pages \= {261--279},  
  doi \= {10.1177/1477878518805308}  
}

@article{Schoenherr2022,  
  author \= {Schoenherr, J.},  
  title \= {Whose Privacy, What Surveillance? {D}imensions of the Mental Models for Privacy and Security},  
  journal \= {IEEE Technology and Society Magazine},  
  year \= {2022},  
  volume \= {41},  
  number \= {1},  
  pages \= {54--65},  
  doi \= {10.1109/MTS.2022.3147536}  
}

@techreport{Victoria2014,  
  author \= {{State Government of Victoria}},  
  title \= {Privacy and Data Protection Act 2014},  
  institution \= {Victorian Legislation},  
  year \= {2014},  
  url \= {https://www.legislation.vic.gov.au/in-force/acts/privacy-and-data-protection-act-2014}  
}

@misc{ACSC2020,  
  author \= {{ACSC}},  
  title \= {Identity theft},  
  howpublished \= {Cyber.gov.au},  
  year \= {2020},  
  url \= {https://www.cyber.gov.au/threats/types-threats/identity-theft}  
}

@techreport{OAIC2021,  
  author \= {{OAIC}},  
  title \= {Annual Report 2020--21},  
  institution \= {Office of the Australian Information Commissioner},  
  year \= {2021},  
  url \= {https://www.oaic.gov.au/about-the-OAIC/our-corporate-information/oaic-annual-reports/annual-report-202021},  
  note \= {Government Report}  
}

@book{yin2018,  
  author    \= {Robert K. Yin},  
  title     \= {Case Study Research and Applications: Design and Methods},  
  publisher \= {SAGE Publications},  
  edition   \= {6th},  
  year      \= {2018}  
}  
   
@article{biernacki1981,  
  title={Snowball sampling: Problems and techniques of chain referral sampling},  
  author={Biernacki, Patrick and Waldorf, Dan},  
  journal={Sociological Methods and Research},  
  volume={10},  
  number={2},  
  pages={141--163},  
  year={1981},  
  publisher={Sage}  
}  
@article{noy2008,  
  title={Sampling knowledge: The hermeneutics of snowball sampling in qualitative research},  
  author={Noy, Shlomo},  
  journal={International Journal of Social Research Methodology},  
  volume={11},  
  number={4},  
  pages={327--344},  
  year={2008},  
  publisher={Taylor and Francis}  
}  
@article{parker2019,  
  title={Snowball sampling to saturation: Incorporating reflexivity into the research process},  
  author={Parker, Lisa D. and Scott, Susan and Geddes, Anna},  
  journal={International Journal of Social Research Methodology},  
  volume={22},  
  number={3},  
  pages={219--233},  
  year={2019},  
  publisher={Taylor and Francis}  
}  
@book{Miles2014,  
  author    \= {Miles, Matthew B. and Huberman, A. Michael and Saldaña, Johnny},  
  title     \= {Qualitative Data Analysis: A Methods Sourcebook},  
  edition   \= {3rd},  
  publisher \= {SAGE Publications},  
  year      \= {2014},  
  address   \= {Thousand Oaks, CA},  
  isbn      \= {9781452257877}  
}

@book{Holloway2017,  
  title={Qualitative Research in Nursing and Healthcare},  
  author={Holloway, Immy and Galvin, Kathleen},  
  year={2017},  
  edition={4th},  
  publisher={Wiley-Blackwell},  
  address={Chichester, UK},  
  isbn={9781118874498}  
}  
@book{lincoln1985,  
  title     \= {Naturalistic Inquiry},  
  author    \= {Lincoln, Yvonna S. and Guba, Egon G.},  
  year      \= {1985},  
  publisher \= {SAGE Publications},  
  address   \= {Beverly Hills, CA}  
}

@book{Creswell2018research,  
  author    \= {John W. Creswell and J. David Creswell},  
  title     \= {Research Design: Qualitative, Quantitative, and Mixed Methods Approaches},  
  publisher \= {SAGE Publications},  
  edition   \= {5th},  
  year      \= {2018}  
}

@article{nowell2017,  
  title     \= {Thematic analysis: Striving to meet the trustworthiness criteria},  
  author    \= {Nowell, Lorelli S. and Norris, Jill M. and White, Deborah E. and Moules, Nancy J.},  
  journal   \= {International Journal of Qualitative Methods},  
  volume    \= {16},  
  number    \= {1},  
  pages     \= {1--13},  
  year      \= {2017},  
  publisher \= {SAGE},  
  doi       \= {10.1177/1609406917733847}  
}  
@article{Garba2020,  
  author \= {Garba, A. A. and Siraj, M. M. and Othman, S. H.},  
  title \= {An Explanatory Review on Cybersecurity Capability Maturity Models},  
  journal \= {Advances in Science, Technology and Engineering Systems Journal},  
  year \= {2020},  
  volume \= {5},  
  number \= {4},  
  pages \= {762--769},  
  doi \= {10.25046/aj050490}  
}  
   
@article{etikan2016,  
  title={Comparison of convenience sampling and purposive sampling},  
  author={Etikan, Ilker and Musa, Sulaiman A. and Alkassim, Rukayya S.},  
  journal={American Journal of Theoretical and Applied Statistics},  
  volume={5},  
  number={1},  
  pages={1--4},  
  year={2016},  
  publisher={Science Publishing Group}  
}  
@article{palinkas2015,  
  title     \= {Purposeful sampling for qualitative data collection and analysis in mixed method implementation research},  
  author    \= {Palinkas, Lawrence A. and Horwitz, Sarah M. and Green, Carla A. and Wisdom, Jennifer P. and Duan, Naihua and Hoagwood, Kimberly},  
  journal   \= {Administration and Policy in Mental Health and Mental Health Services Research},  
  volume    \= {42},  
  number    \= {5},  
  pages     \= {533--544},  
  year      \= {2015},  
  publisher \= {Springer},  
  doi       \= {10.1007/s10488-013-0528-y}  
}  
@article{king2012,  
  author       \= {King, Nigel},  
  title        \= {Doing template analysis},  
  journal      \= {Qualitative Organizational Research: Core Methods and Current Challenges},  
  volume       \= {426},  
  pages        \= {426--450},  
  year         \= {2012},  
   
}

   
@article{boss2015,  
  author       \= {Boss, Stephen R. and Galletta, Dennis F. and Lowry, Paul B. and Moody, Gregory D. and Polak, Peter},  
  title        \= {If someone is watching, I'll do what I'm asked: Mandatoriness, control, and information security},  
  journal      \= {European Journal of Information Systems},  
  volume       \= {24},  
  number       \= {3},  
  pages        \= {285--308},  
  year         \= {2015},  
  doi          \= {10.1057/ejis.2014.30}  
}

@article{berger2015,  
  author={Berger, R.},  
  title={Now I see it, now I don’t: Researcher’s position and reflexivity in qualitative research},  
  journal={Qualitative Research},  
  volume={15},  
  number={2},  
  pages={219--234},  
  year={2015},  
  doi={10.1177/1468794112468475}  
}

%=============================For previous chapters 2 \====================================

 @article{bongiovanni2019,  
  author    \= {Ilaria Bongiovanni},  
  title     \= {Organisational Culture and Cybersecurity: The Role of Shared Assumptions and Values},  
  journal   \= {International Journal of Cyber Security and Digital Forensics},  
  year      \= {2019},  
  volume    \= {8},  
  number    \= {2},  
  pages     \= {93--102},  
  doi       \= {10.17781/P002548},  
  url       \= {https://www.scribd.com/document/511813619/Organisational-Culture-and \-Cybersecurity-The-Role-of-Shared \-Assumptions-and-Values}  
}  
Yeoh, W., Wang, S., Popovič, A., & Chowdhury, N. H. (2022). A systematic synthesis of critical success factors for cybersecurity. Computers & Security, 118, 102724\. https://doi.org/10.1016/j.cose.2022.102724

@article{hadlington2017,  
  author={Hadlington, L.},  
  title={Human factors in cybersecurity; examining the link between Internet addiction, impulsivity, attitudes towards cybersecurity, and risky cybersecurity behaviours},  
  journal={Heliyon},  
  volume={3},  
  number={7},  
  year={2017},  
  doi={10.1016/j.heliyon.2017.e00346}  
}

@misc{fridlenter2024,  
  author={Frid Lenter, A. and Weid, E.},  
  title={How Does Organizational Culture Influence Cybersecurity Risks?},  
  year={2024},  
  url={https://urn.kb.se/resolve?urn=urn:nbn:se:su:diva-242735}  
}  
@techreport{IBMSecurity2025,  
  author \= {{IBM Security}},  
  title \= {Cost of a Data Breach Report 2025},  
  institution \= {IBM Corporation},  
  year \= {2025},  
  url \= {https://www.ibm.com/reports/data-breach}  
}

@misc{Moore2026,  
  author \= {Moore, M.},  
  title \= {Top Cybersecurity Threats to Watch in 2026},  
  howpublished \= {University of San Diego Online Degrees},  
  year \= {2026},  
  url \= {https://onlinedegrees.sandiego.edu/top-cyber-security-threats/}  
}

@misc{lenter2024,  
  author={Frid Lenter, A. and Weid, E.},  
  title={How Does Organizational Culture Influence Cybersecurity Risks?},  
  year={2024},  
  url={https://urn.kb.se/resolve?urn=urn:nbn:se:su:diva-242735}  
}

@article{Yeoh2022,  
  author \= {Yeoh, W. and Wang, S. and Popovi\\v{c}, A. and Chowdhury, N. H.},  
  title \= {A systematic synthesis of critical success factors for cybersecurity},  
  journal \= {Computers \\& Security},  
  year \= {2022},  
  volume \= {118},  
  pages \= {102724},  
  doi \= {10.1016/j.cose.2022.102724}  
}

@article{Prummer2024,  
  author \= {Pr{\\"u}mmer, J. and van Steen, T. and van den Berg, B.},  
  title \= {A systematic review of current cybersecurity training methods},  
  journal \= {Computers \\& Security},  
  year \= {2024},  
  volume \= {136},  
  pages \= {103585},  
  doi \= {10.1016/j.cose.2023.103585}  
}  
@article{Badreddine2025,  
  author \= {Badreddine, S. and Alwada'n, T. and Razzaque, M. A. and Kafri, A. A. and Omari, A. and Alazzam, A. and Ammari, H. A.},  
  title \= {Cybersecurity attitudes in higher education institutions: {A} behavioural analysis of faculty and staff in the {United Arab Emirates}},  
  journal \= {ResearchGate},  
  year \= {2025},  
  url \= {https://www.researchgate.net/publication/396820161\_Cybersecurity\_attitudes\_in\_higher\_education\_institutions\_A\_behavioural\_analysis\_of\_faculty\_and\_staff\_in\_the\_United\_Arab\_Emirates},  
  note \= {Preprint/Technical Report}  
}  
@article{Hina2019,  
  author \= {Hina, S. and Panneer Selvam, D. D. D. and Lowry, P. B.},  
  title \= {Institutional governance and protection motivation: {T}heoretical insights into shaping employees’ security compliance behavior in higher education institutions in the developing world},  
  journal \= {Computers \\& Security},  
  year \= {2019},  
  volume \= {87},  
  pages \= {101594},  
  doi \= {10.1016/j.cose.2019.101594}  
}

@article{Cassidy2018,  
  author \= {Cassidy, S. A. and Stanley, D. J.},  
  title \= {Getting From ‘Me’ to ‘We’: {R}ole Clarity, Team Process, and the Transition From Individual Knowledge to Shared Mental Models in Employee Dyads},  
  journal \= {Canadian Journal of Administrative Sciences / Revue Canadienne des Sciences de l'Administration},  
  year \= {2018},  
  volume \= {36},  
  number \= {2},  
  pages \= {208--220},  
  doi \= {10.1002/cjas.1493}  
}

@article{Reeves2025,  
  author \= {Reeves, A. and Calic, D. and Delfabbro, P.},  
  title \= {How to {De-CyFa} the actor-observer bias in cybersecurity fatigue: {B}uilding the {CyFa} measure of attribution styles and mitigation strategies},  
  journal \= {Computers \\& Security},  
  year \= {2025},  
  volume \= {150},  
  pages \= {104179},  
  doi \= {10.1016/j.cose.2024.104179}  
}

 

@article{Curzon2021,  
  author \= {Curzon, J. and Kosa, T. A. and Akalu, R. and El-Khatib, K.},  
  title \= {Privacy and Artificial Intelligence},  
  journal \= {IEEE Transactions on Artificial Intelligence},  
  year \= {2021},  
  volume \= {2},  
  number \= {2},  
  pages \= {96--108},  
  doi \= {10.1109/TAI.2021.3088084}  
}

@article{Acquisti2015,  
  author \= {Acquisti, A. and Brandimarte, L. and Loewenstein, G.},  
  title \= {Privacy and human behavior in the age of information},  
  journal \= {Science},  
  year \= {2015},  
  volume \= {347},  
  number \= {6221},  
  pages \= {509--514},  
  doi \= {10.1126/science.aaa1465}  
}

@article{Gerber2018,  
  author \= {Gerber, N. and Gerber, P. and Volkamer, M.},  
  title \= {Explaining the privacy paradox: {A} systematic review of literature investigating privacy attitude and behavior},  
  journal \= {Computers \\& Security},  
  year \= {2018},  
  volume \= {77},  
  pages \= {226--261},  
  doi \= {10.1016/j.cose.2018.04.002}  
}

@article{Xie2017,  
  author \= {Xie, B. and Zhou, J. and Wang, H.},  
  title \= {How Influential Are Mental Models on Interaction Performance? {E}xploring the Gap between Users’ and Designers’ Mental Models through a New Quantitative Method},  
  journal \= {Advances in Human-Computer Interaction},  
  year \= {2017},  
  volume \= {2017},  
  pages \= {1--14},  
  doi \= {10.1155/2017/3683546}  
}  
@inproceedings{Mehdy2021,  
  author \= {Mehdy, A. K. M. N. and Ekstrand, M. D. and Knijnenburg, B. P. and Mehrpouyan, H.},  
  title \= {Privacy as a {Planned Behavior}: {E}ffects of {Situational Factors} on {Privacy Perceptions} and {Plans}},  
  booktitle \= {Proceedings of the 29th {ACM} Conference on {User Modeling, Adaptation and Personalization}},  
  year \= {2021},  
  pages \= {169--178},  
  doi \= {10.1145/3450613.3456829}  
}

@article{Abiodun2025,  
  author \= {Abiodun, Y. T. and Mahmood, S. and Niazi, M. and Alshayeb, M. and AlGhamdi, A. A.},  
  title \= {Cybersecurity Readiness Model Based on Human Factors},  
  journal \= {Arabian Journal for Science and Engineering},  
  year \= {2025},  
  volume \= {50},  
  number \= {19},  
  pages \= {16199--16219},  
  doi \= {10.1007/s13369-025-10349-w}  
}

 

@article{Mangundu2023,  
  author \= {Mangundu, J. and Mayayise, T.},  
  title \= {The impact of technostress creators on academics’ cybersecurity fatigue in {S}outh {A}frica},  
  journal \= {Issues In Information Systems},  
  year \= {2023},  
  doi \= {10.48009/4\_iis\_2023\_123}  
}

 

@article{Tobarra2021,  
  author \= {Tobarra, L. and Utrilla, A. and Robles-G{\\'o}mez, A. and Pastor-Vargas, R. and Roberto, H.},  
  title \= {A {Cloud Game-Based Educative Platform Architecture}: {T}he {CyberScratch} Project},  
  journal \= {Applied Sciences},  
  year \= {2021},  
  volume \= {11},  
  number \= {2},  
  pages \= {807},  
  doi \= {10.3390/app11020807}  
}

@article{Pavlova2020,  
  author \= {Pavlova, E.},  
  title \= {Enhancing the {O}rganisational {C}ulture related to {C}yber {S}ecurity during the {U}niversity {D}igital {T}ransformation},  
  journal \= {Information \\& Security: An International Journal},  
  year \= {2020},  
  volume \= {46},  
  number \= {3},  
  pages \= {239--249},  
  doi \= {10.11610/isij.4617}  
}

@article{da2010framework,  
  author \= {Da Veiga, A. and Eloff, J. H. P.},  
  title \= {A framework and assessment instrument for information security culture},  
  journal \= {Computers \\& Security},  
  year \= {2010},  
  volume \= {29},  
  number \= {2},  
  pages \= {196--207},  
  doi \= {10.1016/j.cose.2009.09.002}  
}

@article{Hassandoust2023,  
  author \= {Hassandoust, F. and Johnston, A. C.},  
  title \= {Peering through the lens of high‐reliability theory: {A} competencies driven security culture model of high‐reliability organisations},  
  journal \= {Information Systems Journal},  
  year \= {2023},  
  volume \= {33},  
  number \= {5},  
  pages \= {1212--1238},  
  doi \= {10.1111/isj.12441}  
}

@article{Ashenden2013,  
  author \= {Ashenden, D. and Sasse, A.},  
  title \= {{CISO}s and organisational culture: {T}heir own worst enemy?},  
  journal \= {Computers \\& Security},  
  year \= {2020},  
  volume \= {39},  
  pages \= {396--405},  
  doi \= {10.1016/j.cose.2013.09.004}  
}

   
@inproceedings{balozian2017,  
  author    \= {Balozian, P. and Leidner, D.},  
  title     \= {The Assumptions and Profiles Behind {IT} Security Behavior},  
  booktitle \= {Proceedings of the 50th Hawaii International Conference on System Sciences ({HICSS})},  
  year      \= {2017},  
  url       \= {http://hdl.handle.net/10125/41767}  
}  
@article{parsons2015,  
  author  \= {Parsons, K. M. and Young, E. and Butavicius, M. A. and McCormac, A. and Pattinson, M. R. and Jerram, C.},  
  title   \= {The Influence of Organizational Information Security Culture on Information Security Decision Making},  
  journal \= {Journal of Cognitive Engineering and Decision Making},  
  volume  \= {9},  
  number  \= {2},  
  pages   \= {117--129},  
  year    \= {2015},  
  doi     \= {10.1177/1555343415575152}  
}  
@article{skalkos2021,  
  title={Users’ privacy attitudes towards the use of behavioral biometrics continuous authentication (BBCA) technologies: A protection motivation theory approach},  
  author={Skalkos, Andreas and Stylios, Ioannis and Karyda, Maria and Kokolakis, Spyros},  
  journal={Journal of Cybersecurity and Privacy},  
  volume={1},  
  number={4},  
  pages={743--766},  
  year={2021},  
  publisher={MDPI}  
}  
@article{Kont2024,  
  author \= {Kont, K.-R.},  
  title \= {Cybersecurity behaviours of the employees and students at the {Estonian Academy of Security Sciences}},  
  journal \= {Organizational Cybersecurity Journal: Practice, Process \\& People},  
  year \= {2024},  
  volume \= {4},  
  number \= {2},  
  pages \= {85--104},  
  doi \= {10.1108/OCJ-02-2024-0001}  
}

@article{Hakiem2023,  
  author \= {Hakiem, N. and Afrizal, S. and Shofi, I. M. and Wardhani, L. K. and Anggraini, N. and Zulhuda, S. and Setiadi, Y.},  
  title \= {Assessing Cybersecurity Readiness among Higher Education Institutions in {Indonesia} Using Management Perspectives},  
  journal \= {ICIC Express Letters},  
  year \= {2023},  
  volume \= {17},  
  number \= {10},  
  pages \= {1151--1160},  
  doi \= {10.24507/icicel.17.10.1151}  
}

@inproceedings{Pinheiro2020,  
  author \= {Pinheiro, J.},  
  title \= {Review of cyber threats on Educational Institutions},  
  booktitle \= {Proceedings of the Digital Privacy and Security Conference},  
  pages \= {43--52},  
  year \= {2020},  
  url \= {https://www.academia.edu/62002199/Review\_of\_cyber\_threats\_on\_Educational\_Institutions}  
}

@misc{Antal2023,  
  author \= {Antal, G.},  
  title \= {How {Vice Society’s} Ransomware Attack Impacted {University of Duisburg-Essen}},  
  howpublished \= {Heimdal Security Blog},  
  month \= {January},  
  year \= {2023},  
  url \= {https://heimdalsecurity.com/blog/how-vice-societys-ransomware-attack-impacted-university-of-duisburg-essen/}  
}

@misc{WSU2024,  
  author \= {{WSU}},  
  title \= {Cyber Incident},  
  year \= {2024},  
  url \= {https://www.westernsydney.edu.au/news/cyber-incident},  
  note \= {Western Sydney University; Official Institutional Statement}  
}

 

@article{Kaloudi2020,  
  author \= {Kaloudi, N. and Li, J.},  
  title \= {The {AI-Based} Cyber Threat Landscape},  
  journal \= {ACM Computing Surveys},  
  year \= {2020},  
  volume \= {53},  
  number \= {1},  
  pages \= {1--34},  
  doi \= {10.1145/3372823}  
}

@inproceedings{Kettani2019,  
  author \= {Kettani, H. and Wainwright, P.},  
  title \= {On the top threats to cyber systems},  
  booktitle \= {2019 {IEEE} 2nd international conference on information and computer technologies ({ICICT})},  
  year \= {2019},  
  pages \= {175--179},  
  organization \= {IEEE},  
  doi \= {10.1109/ICICT.2019.8710978}  
}

@article{Meland2020,  
  author \= {Meland, P. H. and Bayoumy, Y. F. F. and Sindre, G.},  
  title \= {The {Ransomware-as-a-Service} economy within the darknet},  
  journal \= {Computers \\& Security},  
  year \= {2020},  
  volume \= {92},  
  pages \= {101762},  
  doi \= {10.1016/j.cose.2020.101762}  
}

@inproceedings{chaudhary2022,  
  author \= {Chaudhary, S. and Kompara, M. and Pape, S. and Gkioulos, V.},  
  title \= {Properties for Cybersecurity Awareness Posters' Design and Quality Assessment},  
  booktitle \= {Proceedings of the 17th International Conference on Availability, Reliability and Security},  
  series \= {ARES '22},  
  pages \= {1--8},  
  year \= {2022},  
  publisher \= {Association for Computing Machinery},  
  address \= {New York, NY, USA},  
  doi \= {10.1145/3538969.3543794},  
  url \= {https://doi.org/10.1145/3538969.3543794}  
}

@article{jeong2022,  
  title={Simplifying Cyber Security Maturity Models through National Culture},  
  author={Jeong, Hwa-Kyung and Grobler, Martin and M.A.P., Zaaiman},  
  journal={Information and Computer Security},  
  volume={30},  
  number={3},  
  pages={489--509},  
  year={2022},  
  publisher={Emerald Publishing Limited}  
}

@article{jeong2021,  
  title={The current state of research on people, culture and cybersecurity},  
  author={Jeong, J. J. and Oliver, G. and Kang, E. and Creese, S. and Thomas, P.},  
  journal={Personal and Ubiquitous Computing},  
  volume={25},  
  number={5},  
  pages={809--812},  
  year={2021},  
  publisher={Springer},  
  doi={10.1007/s00779-021-01591-8},  
  url={https://doi.org/10.1007/s00779-021-01591-8}  
}

@article{Kokolakis2017,  
  author \= {Kokolakis, S.},  
  title \= {Privacy attitudes and privacy behaviour: {A} review of current research on the privacy paradox phenomenon},  
  journal \= {Computers \\& Security},  
  year \= {2017},  
  volume \= {64},  
  pages \= {122--134},  
  doi \= {10.1016/j.cose.2015.07.002}  
}

@phdthesis{Alshammari2024,  
  author \= {Alshammari, A. S. A.},  
  title \= {The Influence of Emotions on Employees’ Cybersecurity {P}rotection {M}otivation {B}ehaviour: {E}xamining the {M}ediating {E}ffect of {S}elf-{E}fficacy and {M}oderating {R}ole of {C}ybersecurity {A}wareness},  
  school \= {Aston University},  
  year \= {2024},  
  type \= {{PhD} Thesis}  
}

@article{Kiran2025,  
  author \= {Kiran, U. and Khan, N. F. and Murtaza, H. and Farooq, A. and Pirkkalainen, H.},  
  title \= {Explanatory and predictive modeling of cybersecurity behaviors using protection motivation theory},  
  journal \= {Computers \\& Security},  
  year \= {2025},  
  volume \= {149},  
  pages \= {104204},  
  doi \= {10.1016/j.cose.2024.104204}  
}

@article{Menard2017,  
  author \= {Menard, P. and Bott, G. J. and Crossler, R. E.},  
  title \= {User {M}otivations in {P}rotecting {I}nformation {S}ecurity: {P}rotection {M}otivation {T}heory {V}ersus {S}elf-{D}etermination {T}heory},  
  journal \= {Journal of Management Information Systems},  
  year \= {2017},  
  volume \= {34},  
  number \= {4},  
  pages \= {1203--1230},  
  doi \= {10.1080/07421222.2017.1394083}  
}

@inproceedings{DaVeiga2016,  
  author \= {Da Veiga, A.},  
  title \= {A cybersecurity culture research philosophy and approach to develop a valid and reliable measuring instrument},  
  booktitle \= {2016 {SAI} Computing Conference ({SAI})},  
  year \= {2016},  
  pages \= {1006--1015},  
  doi \= {10.1109/SAI.2016.7556102},  
  organization \= {IEEE}  
}  
@article{Maddux1983,  
  author \= {Maddux, J. E. and Rogers, R. W.},  
  title \= {Protection motivation and self-efficacy: {A} revised theory of fear appeals and attitude change},  
  journal \= {Journal of Experimental Social Psychology},  
  year \= {1983},  
  volume \= {19},  
  number \= {5},  
  pages \= {469--479},  
  doi \= {10.1016/0022-1031(83)90023-9}  
}

@article{Latif2025,  
  author \= {Latif, S. F. A. and Sulaiman, N. S. and Aziz, N. S. A. and Yacob, A. and Nasir, A.},  
  title \= {Development of {Cybersecurity Awareness Model} Based on {Protection Motivation Theory} ({PMT}) for {Digital IR 4.0} in {Malaysia}},  
  journal \= {International Journal of Advanced Computer Science and Applications},  
  year \= {2025},  
  volume \= {16},  
  number \= {3}  
}

@incollection{Shillair2020,  
  author \= {Shillair, R.},  
  title \= {Protection {Motivation Theory}},  
  booktitle \= {The International Encyclopedia of Media Psychology},  
  editor \= {Bulck, J.},  
  publisher \= {Wiley},  
  year \= {2020},  
  edition \= {1st},  
  pages \= {1--3},  
  doi \= {10.1002/9781119011071.iemp0188}  
}

@article{Xiao2014,  
  author \= {Xiao, H. and Li, S. and Chen, X. and Yu, B. and Gao, M. and Yan, H. and Okafor, C. N.},  
  title \= {Protection motivation theory in predicting intention to engage in protective behaviors against schistosomiasis among middle school students in rural {China}},  
  journal \= {PLoS Neglected Tropical Diseases},  
  year \= {2014},  
  volume \= {8},  
  number \= {10},  
  pages \= {e3246},  
  doi \= {10.1371/journal.pntd.0003246}  
}

@article{Hanus2016,  
  author \= {Hanus, B. and Wu, Y. Andy},  
  title \= {Impact of {U}sers’ {S}ecurity {A}wareness on {D}esktop {S}ecurity {B}ehavior: {A} {P}rotection {M}otivation {T}heory {P}erspective},  
  journal \= {Information Systems Management},  
  year \= {2016},  
  volume \= {33},  
  number \= {1},  
  pages \= {2--16},  
  doi \= {10.1080/10580530.2015.1117842}  
}

@article{Xu2024,  
  author \= {Xu, F. and Hsu, C. and Wang, T. David and Lowry, P. B.},  
  title \= {The antecedents of employees’ proactive information security behaviour: {T}he perspective of proactive motivation},  
  journal \= {Information Systems Journal},  
  year \= {2024},  
  volume \= {34},  
  number \= {4},  
  pages \= {1144--1174},  
  doi \= {10.1111/isj.12488}  
}

 

@article{DelsoVicente2025,  
  author \= {Delso-Vicente, A.-T. and Diaz-Marcos, L. and Aguado-Tevar, O. and de Blanes-Sebasti{\\'a}n, M. G.},  
  title \= {Factors influencing employee compliance with information security policies: {A} systematic literature review of behavioral and technological aspects in cybersecurity},  
  journal \= {Future Business Journal},  
  year \= {2025},  
  volume \= {11},  
  number \= {1},  
  pages \= {28},  
  doi \= {10.1186/s43093-025-00452-7}  
}  
@article{Hu2012,  
  author \= {Hu, Q. and Dinev, T. and Hart, P. and Cooke, D.},  
  title \= {Managing {E}mployee {C}ompliance with {I}nformation {S}ecurity {P}olicies: {T}he {C}ritical {R}ole of {T}op {M}anagement and {O}rganizational {C}ulture},  
  journal \= {Decision Sciences},  
  year \= {2012},  
  volume \= {43},  
  number \= {4},  
  pages \= {615--660},  
  doi \= {10.1111/j.1540-5915.2012.00361.x}  
}  
@book{schein2010,  
  title={Organizational Culture and Leadership},  
  author={Schein, Edgar H},  
  edition={4th},  
  year={2010},  
  publisher={Jossey-Bass}  
}

@article{DaVeiga2010,  
  author \= {Da Veiga, A. and Eloff, J. H. P.},  
  title \= {A framework and assessment instrument for information security culture},  
  journal \= {Computers \\& Security},  
  year \= {2010},  
  volume \= {29},  
  number \= {2},  
  pages \= {196--207},  
  doi \= {10.1016/j.cose.2009.09.002}  
}  
@book{schein2004,  
  author    \= {Edgar H. Schein},  
  title     \= {Organizational Culture and Leadership},  
  publisher \= {Jossey-Bass},  
  edition   \= {3rd},  
  year      \= {2004}  
}

@phdthesis{Compton2020,  
  author \= {Compton, Y. R.},  
  title \= {Obstacles With {D}ata {S}ecurity: {S}trategies {F}rom {C}arolina {U}niversities},  
  school \= {Walden University},  
  year \= {2020},  
  type \= {{PhD} Thesis},  
  url \= {https://doi.org/10.1.1.392.9280}  
}

@misc{McCants2022,  
  author \= {McCants, N.},  
  title \= {The resource allocation process and the effects on cybersecurity culture},  
  year \= {2022},  
  howpublished \= {Independent Publication},  
  note \= {Monograph/Self-Published}  
}

@article{Alzahrani2021,  
  author \= {Alzahrani, L.},  
  title \= {Statistical {A}nalysis of {C}ybersecurity {A}wareness},  
  journal \= {International Journal of Advanced Computer Science and Applications},  
  year \= {2021},  
  volume \= {12},  
  number \= {11},  
  pages \= {630--637},  
  doi \= {10.14569/IJACSA.2021.0121172}  
}

@article{Liu2020,  
  author \= {Liu, N. and Nikitas, A. and Parkinson, S.},  
  title \= {Exploring expert perceptions about the cyber security and privacy of {C}onnected and {A}utonomous {V}ehicles: {A} thematic analysis approach},  
  journal \= {Transportation Research Part F: Traffic Psychology and Behaviour},  
  year \= {2020},  
  volume \= {75},  
  pages \= {66--86},  
  doi \= {10.1016/j.trf.2020.09.019}  
}

@phdthesis{Riggins2024,  
  author \= {Riggins, J.},  
  title \= {Chief {I}nformation {S}ecurity {O}fficers {S}trategies for {M}inimizing {C}ybersecurity {A}ttacks},  
  school \= {ProQuest LLC},  
  year \= {2024},  
  type \= {Doctoral Dissertation},  
  url \= {https://www.proquest.com/docview/3066598591}  
}

@article{dimitrov2013,  
  title={The Role of Values in the Theory and Practice of Leadership},  
  author={Dimitrov, Vladimir},  
  journal={Leadership and Organization Development Journal},  
  volume={34},  
  number={7},  
  pages={637--653},  
  year={2013}  
}

@article{kaptein2011,  
  author  \= {Kaptein, Muel},  
  title   \= {Understanding unethical behavior by unraveling ethical culture},  
  journal \= {Human Relations},  
  year    \= {2011},  
  volume  \= {64},  
  number  \= {6},  
  pages   \= {843--869},  
  doi     \= {10.1177/0018726710390536}  
}

@article{Sommestad2017,  
  author \= {Sommestad, T. and Karlzén, H. and Hallberg, J.},  
  title \= {The {T}heory of {P}lanned {B}ehavior and {I}nformation {S}ecurity {P}olicy {C}ompliance},  
  journal \= {Journal of Computer Information Systems},  
  year \= {2017},  
  volume \= {59},  
  number \= {4},  
  pages \= {344--353},  
  doi \= {10.1080/08874417.2017.1368421}  
}

@article{Ong2022,  
  author \= {Ong, A. K. S. and Prasetyo, Y. T. and Salazar, J. M. L. D. and Erfe, J. J. C. and Abella, A. A. and Young, M. N. and Chuenyindee, T. and Nadlifatin, R. and Ngurah Perwira Redi, A. A.},  
  title \= {Investigating the acceptance of the reopening {B}ataan nuclear power plant: {I}ntegrating protection motivation theory and extended theory of planned behavior},  
  journal \= {Nuclear Engineering and Technology},  
  year \= {2022},  
  volume \= {54},  
  number \= {3},  
  pages \= {1115--1125},  
  doi \= {10.1016/j.net.2021.08.032}  
}

@article{AlAdwan2023,  
  author \= {Al-Adwan, A. S. and Li, N. and Al-Adwan, A. and Abbasi, G. A. and Albelbisi, N. A. and Habibi, A.},  
  title \= {Extending the {T}echnology {A}cceptance {M}odel ({TAM}) to {P}redict {U}niversity {S}tudents’ {I}ntentions to {U}se {M}etaverse-{B}ased {L}earning {P}latforms},  
  journal \= {Education and Information Technologies},  
  year \= {2023},  
  volume \= {28},  
  number \= {11},  
  pages \= {15381--15413},  
  doi \= {10.1007/s10639-023-11816-3}  
}

@techreport{Dwyer2011,  
  author \= {Dwyer, C.},  
  title \= {Socio-technical {S}ystems {T}heory and {E}nvironmental {S}ustainability},  
  institution \= {Pace University},  
  year \= {2011},  
  url \= {https://www.researchgate.net/publication/277986161}  
}

@article{Pasmore2019,  
  author \= {Pasmore, W. and Winby, S. and Mohrman, S. A. and Vanasse, R.},  
  title \= {Reflections: Sociotechnical Systems Design and Organization Change},  
  journal \= {Journal of Change Management},  
  volume \= {19},  
  number \= {2},  
  pages \= {67--85},  
  year \= {2019},  
  doi \= {10.1080/14697017.2018.1553761},  
  url \= {https://doi.org/10.1080/14697017.2018.1553761}  
}

@article{Charitoudi2013,  
  author \= {Charitoudi, K. and Blyth, A.},  
  title \= {A {S}ocio-{T}echnical {A}pproach to {C}yber {R}isk {M}anagement and {I}mpact {A}ssessment},  
  journal \= {Journal of Information Security},  
  year \= {2013},  
  volume \= {4},  
  number \= {1},  
  pages \= {Article 1},  
  doi \= {10.4236/jis.2013.41005}  
}

@inproceedings{Thinyane2024,  
  author \= {Thinyane, M.},  
  title \= {Unpacking the {C}omplex {S}ocio-{T}echnical {S}ystems {A}ssemblages in {C}ybersecurity},  
  booktitle \= {European Conference on Cyber Warfare and Security},  
  year \= {2024},  
  volume \= {23},  
  number \= {1},  
  pages \= {Article 1},  
  doi \= {10.34190/eccws.23.1.2155}  
}

@book{Hofstede2010,  
  author \= {Hofstede, G. and Hofstede, G. J. and Minkov, M.},  
  title \= {Cultures and organizations: {S}oftware of the mind: intercultural cooperation and its importance for survival},  
  publisher \= {McGraw-Hill},  
  year \= {2010},  
  edition \= {3rd},  
  url \= {https://archive.org/details/culturesorganiza0000hofs\_k8j8}  
}

@article{Willie2023,  
  author \= {Willie, M. M.},  
  title \= {The {R}ole of {O}rganizational {C}ulture in {C}ybersecurity: {B}uilding a {S}ecurity-{F}irst {C}ulture},  
  journal \= {Journal of Research, Innovation and Technologies},  
  year \= {2023},  
  volume \= {2},  
  number \= {2(4)},  
  pages \= {05},  
  doi \= {10.57017/jorit.v2.2(4).05}  
}

@article{Gao2018,  
  author \= {Gao, W. and Liu, Z. and Guo, Q. and Li, X.},  
  title \= {The dark side of ubiquitous connectivity in smartphone-based {SNS}: {A}n integrated model from information perspective},  
  journal \= {Computers in Human Behavior},  
  year \= {2018},  
  volume \= {84},  
  pages \= {185--193},  
  doi \= {10.1016/j.chb.2018.02.023}  
}

@article{Wu2020,  
  author \= {Wu, D.},  
  title \= {Empirical study of knowledge withholding in cyberspace: {I}ntegrating protection motivation theory and theory of reasoned behavior},  
  journal \= {Computers in Human Behavior},  
  year \= {2020},  
  volume \= {105},  
  pages \= {106229},  
  doi \= {10.1016/j.chb.2019.106229}  
}

@phdthesis{Wall2014,  
  author \= {Wall, M.},  
  title \= {Understanding the {V}alues of {C}hristian {O}rganisations: {A} {C}ase {S}tudy of {A}cross (1972-2005) using the {O}rganisational {C}ulture {T}heory of {E}dgar {S}chein},  
  school \= {Middlesex University},  
  year \= {2014},  
  type \= {{PhD} Thesis},  
  url \= {https://eprints.mdx.ac.uk/13511/}  
}  
@article{Neri2024,  
  author \= {Neri, M. and Niccolini, F. and Martino, L.},  
  title \= {Organizational cybersecurity readiness in the {ICT} sector: {A} quanti-qualitative assessment},  
  journal \= {Information \\& Computer Security},  
  year \= {2024},  
  doi \= {10.1108/ICS-05-2023-0084}  
}

%=============================For chapter 3 \=========================

@book{Bryman2016,  
  author \= {Bryman, A.},  
  title \= {Social Research Methods},  
  publisher \= {Oxford University Press},  
  year \= {2016},  
  edition \= {5th}  
}  
@article{Park2020,  
  author \= {Park, Y. and Konge, L. and Artino, Jr., A. R.},  
  title \= {The Positivism Paradigm of Research},  
  journal \= {Academic Medicine},  
  year \= {2020},  
  volume \= {95},  
  number \= {5},  
  pages \= {690--694},  
  doi \= {10.1097/ACM.0000000000003093},  
  url \= {https://doi.org/10.1097/ACM.0000000000003093}  
}

@incollection{Su2018,  
  author \= {Su, Ning},  
  title \= {Positivist Qualitative Methods},  
  booktitle \= {The SAGE Handbook of Qualitative Business and Management Research Methods: History and Traditions},  
  editor \= {Cassell, C. and Cunliffe, A. L. and Grandy, G.},  
  publisher \= {SAGE Publications},  
  year \= {2018}  
}

@phdthesis{Choejey2018,  
  author \= {Choejey, P.},  
  title \= {Cybersecurity Challenges and Practices: A Case Study of Bhutan},  
  school \= {Queensland University of Technology},  
  year \= {2018}  
}

@article{Sridharan2025,  
  author \= {Sridharan, V.},  
  title \= {Incommensurable but still compatible: Paradigm hybridization trends in qualitative management control systems research},  
  journal \= {Qualitative Research in Accounting \\& Management},  
  year \= {2025},  
  note \= {Forthcoming/Earlycite}  
}

@article{Berkovich2018,  
  author \= {Berkovich, I.},  
  title \= {Beyond qualitative/quantitative structuralism: The positivist qualitative research and the paradigmatic disclaimer},  
  journal \= {Quality \\& Quantity},  
  year \= {2018},  
  volume \= {52},  
  number \= {5},  
  pages \= {2063--2077},  
  doi \= {10.1007/s11135-017-0607-3}  
}

@incollection{Lincoln2011,  
  author \= {Lincoln, Y. S. and Guba, E. G. and Lynham, S. A.},  
  title \= {Paradigmatic controversies, contradictions, and emerging confluences, revisited},  
  booktitle \= {The Sage Handbook of Qualitative Research},  
  publisher \= {SAGE Publications, Inc},  
  year \= {2011},  
  pages \= {97--128},  
  edition \= {4th}  
}  
@article{Fletcher2017,  
  author \= {Fletcher, A. J.},  
  title \= {Applying critical realism in qualitative research: Methodology meets method},  
  journal \= {International Journal of Social Research Methodology},  
  year \= {2017},  
  volume \= {20},  
  number \= {2},  
  pages \= {181--194},  
  doi \= {10.1080/13645579.2016.1144401}  
}

@article{Priya2021,  
  author \= {Priya, A.},  
  title \= {Case Study Methodology of Qualitative Research: Key Attributes and Navigating the Conundrums in Its Application},  
  journal \= {Sociological Bulletin},  
  year \= {2021},  
  volume \= {70},  
  number \= {1},  
  pages \= {94--110},  
  doi \= {10.1177/0038022920970318}  
}

@article{Goldkuhl2017,  
  author \= {Goldkuhl, G.},  
  title \= {Pragmatism vs interpretivism in qualitative information systems research},  
  journal \= {European Journal of Information Systems},  
  year \= {2017},  
  volume \= {21},  
  number \= {2},  
  pages \= {135--146},  
  doi \= {10.1057/ejis.2011.54}  
}  
@article{Wilson2014,  
  author \= {Wilson, J. and Gabriel, L. and James, H.},  
  title \= {Observing a client’s grieving process: Bringing logical positivism into qualitative grief counselling research},  
  journal \= {British Journal of Guidance \\& Counselling},  
  year \= {2014},  
  volume \= {42},  
  number \= {5},  
  pages \= {580--602},  
  doi \= {10.1080/03069885.2014.936823}  
}  
@article{Crandall2019,  
  author \= {Crandall, C. and Noteboom, C. and El-Gayar, O. and Crandall, K.},  
  title \= {High school students' perceptions of cybersecurity: An explanatory case study},  
  journal \= {Issues in Information Systems},  
  year \= {2019},  
  volume \= {20},  
  number \= {3},  
  pages \= {74--82},  
  doi \= {10.48009/3\_iis\_2019\_74-82}  
}

@article{Yazan2015,  
  author \= {Yazan, B.},  
  title \= {Three Approaches to Case Study Methods in Education: Yin, Merriam, and Stake},  
  journal \= {The Qualitative Report},  
  year \= {2015},  
  volume \= {20},  
  number \= {2},  
  pages \= {134--152},  
  doi \= {10.46743/2160-3715/2015.2102}  
}

@article{Jones2021,  
  author \= {Jones, J. and Bennett, S. and Lockyer, L.},  
  title \= {Applying a learning design to the design of a university unit: A single case study},  
  journal \= {Journal of Computing in Higher Education},  
  year \= {2021},  
  volume \= {33},  
  pages \= {21--43},  
  doi \= {10.1007/s12528-020-09255-7}  
}

@article{Ahmad2021,  
  author \= {Ahmad, A. and Maynard, S. B. and Desouza, K. C. and Kotsias, J. and Whitty, M. T. and Baskerville, R. L.},  
  title \= {How can organizations develop situation awareness for incident response: A case study of management practice},  
  journal \= {Computers \\& Security},  
  year \= {2021},  
  volume \= {101},  
  pages \= {102122},  
  doi \= {10.1016/j.cose.2020.102122}  
}

@article{Cruzes2014,  
  author \= {Cruzes, D. S. and Dybå, T. and Runeson, P. and H{\\"o}st, M.},  
  title \= {Case studies synthesis: A thematic, cross-case, and narrative synthesis worked example},  
  journal \= {Empirical Software Engineering},  
  year \= {2014},  
  volume \= {20},  
  number \= {6},  
  pages \= {1634--1665},  
  doi \= {10.1007/s10664-014-9326-8}  
}

@article{Whittle2025,  
  author \= {Whittle, A. and Reissner, S.},  
  title \= {Making Knowledge Claims from Qualitative Interviews: A Typology of Epistemological Modes},  
  journal \= {British Journal of Management},  
  year \= {2025},  
  volume \= {36},  
  number \= {1},  
  pages \= {3--16},  
  doi \= {10.1111/1467-8551.12845}  
}  
@article{Golding2024,  
  author \= {Golding, J.},  
  title \= {Teachers, Learners and Edu-Business Co-Constructing Mathematics Curriculum Implementation: An Insider’s Lens in Cross-Phase Longitudinal Research},  
  journal \= {Education Sciences},  
  year \= {2024},  
  volume \= {14},  
  number \= {12},  
  pages \= {1322},  
  doi \= {10.3390/educsci14121322}  
}  
@phdthesis{Brentzel2025,  
  author \= {Brentzel, E. R.},  
  title \= {Organizational Cyber Resilience in Higher Education: How Administrative Leaders Experience a Disruptive Cyber Attack},  
  school \= {Abilene Christian University},  
  year \= {2025}  
}

@phdthesis{Crossland2022,  
  author \= {Crossland, G.},  
  title \= {Using Psychological Theories and Usable Security to Understand Cyber-Security Perceptions and Behaviours Within an Organisation; a Case Study of a Law Firm},  
  school \= {Royal Holloway, University of London},  
  year \= {2022},  
  url \= {https://pure.royalholloway.ac.uk/ws/portalfiles/portal/46845921/GC\_Crossland\_Doctoral\_Thesis\_FINAL.pdf}  
}

@article{Pollini2022,  
  author \= {Pollini, A. and Callari, T. C. and Tedeschi, A. and Ruscio, D. and Save, L. and Chiarugi, F. and Guerri, D.},  
  title \= {Leveraging human factors in cybersecurity: An integrated methodological approach},  
  journal \= {Cognition, Technology \\& Work},  
  year \= {2022},  
  volume \= {24},  
  number \= {2},  
  pages \= {371--390},  
  doi \= {10.1007/s10111-021-00683-y}  
}

@inproceedings{Fujs2019,  
  author \= {Fujs, D. and Mihelič, A. and Vrhovec, S. L. R.},  
  title \= {The power of interpretation: Qualitative methods in cybersecurity research},  
  booktitle \= {14th International Conference on Availability, Reliability and Security (ARES ’19)},  
  year \= {2019},  
  pages \= {1--10},  
  doi \= {10.1145/3339252.3341479}  
}

@inproceedings{Nagele2023,  
  author \= {Nägele, S. and Korn, L. and Matthes, F.},  
  title \= {Adoption of Information Security Practices in Large-Scale Agile Software Development: A Case Study in the Finance Industry},  
  booktitle \= {The 18th International Conference on Availability, Reliability and Security (ARES ’23)},  
  year \= {2023},  
  pages \= {1--12},  
  doi \= {10.1145/3600160.3600170}  
}

@article{Irvine2012,  
  author \= {Irvine, A. and Drew, P. and Sainsbury, R.},  
  title \= {‘Am I not answering your questions properly?’ Clarification, adequacy and responsiveness in semi-structured telephone and face-to-face interviews},  
  journal \= {Qualitative Research},  
  year \= {2012},  
  volume \= {13},  
  number \= {1},  
  pages \= {87--106},  
  doi \= {10.1177/1468794112439086}  
}  
@article{Burton2019,  
  author \= {Burton, N. and Galvin, P.},  
  title \= {Using template and matrix analysis: A case study of management and organisation history research},  
  journal \= {Qualitative Research in Organizations and Management: An International Journal},  
  year \= {2019},  
  volume \= {14},  
  number \= {4},  
  pages \= {393--409},  
  doi \= {10.1108/QROM-04-2018-1626}  
}  
@article{Burton2023,  
  author \= {Burton, S. L. and Burrell, D. N. and Nobles, C. and Jones, L. A.},  
  title \= {Exploring the Nexus of Cybersecurity Leadership, Human Factors, Emotional Intelligence, Innovative Work Behavior, and Critical Leadership Traits},  
  journal \= {Scientific Bulletin},  
  volume \= {28},  
  number \= {2},  
  pages \= {162--175},  
  year \= {2023},  
  doi \= {10.2478/bsaft-2023-0016},  
  url \= {https://doi.org/10.2478/bsaft-2023-0016}  
}

@article{Braun2006,  
  author \= {Braun, V. and Clarke, V.},  
  title \= {Using thematic analysis in psychology},  
  journal \= {Qualitative Research in Psychology},  
  year \= {2006},  
  volume \= {3},  
  number \= {2},  
  pages \= {77--101},  
  doi \= {10.1191/1478088706qp063oa}  
}

@incollection{King2018,  
  author \= {King, N. and Brooks, J. and Tabari, S.},  
  title \= {Template Analysis in Business and Management Research},  
  booktitle \= {Qualitative Methodologies in Organization Studies: Volume II: Methods and Possibilities},  
  editor \= {Ciesielska, M. and Jemielniak, D.},  
  publisher \= {Springer International Publishing},  
  year \= {2018},  
  pages \= {179--206},  
  address \= {Cham},  
  doi \= {10.1007/978-3-319-65442-3\_8}  
}  
@book{Saldana2013,  
  author \= {Saldaña, J.},  
  title \= {The coding manual for qualitative researchers},  
  edition \= {2nd},  
  publisher \= {SAGE Publications},  
  address \= {London},  
  year \= {2013}  
}

@article{Sadri2025,  
  author \= {Sadri, M. and Aristidou, A. and Ravasi, D.},  
  title \= {Cross-Sector Partnership Research at Theoretical Interstices: Integrating and Advancing Theory across Phases},  
  journal \= {Journal of Management Studies},  
  year \= {2025},  
  volume \= {62},  
  number \= {1},  
  pages \= {484--517},  
  doi \= {10.1111/joms.13046}  
}  
@article{Adler2022,  
  author \= {Adler, R. H.},  
  title \= {Trustworthiness in Qualitative Research},  
  journal \= {Journal of Human Lactation},  
  year \= {2022},  
  volume \= {38},  
  number \= {4},  
  pages \= {598--602},  
  doi \= {10.1177/08903344221116620}  
}

@article{Forero2018,  
  author \= {Forero, R. and Nahidi, S. and De Costa, J. and Mohsin, M. and Fitzgerald, G. and Gibson, N. and McCarthy, S. and Aboagye-Sarfo, P.},  
  title \= {Application of four-dimension criteria to assess rigour of qualitative research in emergency medicine},  
  journal \= {BMC Health Services Research},  
  year \= {2018},  
  volume \= {18},  
  number \= {1},  
  pages \= {120},  
  doi \= {10.1186/s12913-018-2915-2}  
}  
   
@article{Jimenez2021,  
  author \= {Jiménez, Tomás R. and Orozco, Monica},  
  title \= {Prompts, Not Questions: Four Techniques for Crafting Better Interview Protocols},  
  journal \= {Qualitative Sociology},  
  volume \= {44},  
  number \= {4},  
  pages \= {507--528},  
  year \= {2021},  
  doi \= {10.1007/s11133-021-09483-2},  
  url \= {https://doi.org/10.1007/s11133-021-09483-2}  
}

@inproceedings{Kramer2020,  
  author \= {Kramer, Amy and Dringenberg, Emily and Kajfez, Rachel Louis},  
  title \= {Development and Refinement of Interview Protocol to Study Engineering Students’ Beliefs and Identities},  
  booktitle \= {2020 ASEE Virtual Annual Conference Content Access},  
  month \= {June},  
  year \= {2020},  
  url \= {https://peer.asee.org/development-and-refinement-of-interview-protocol-to-study-engineering-students-beliefs-and-identities}  
}

@article{Shoozan2024,  
  author \= {Shoozan, A. and Mohamad, M.},  
  title \= {Application of Interview Protocol Refinement Framework in Systematically Developing and Refining a Semi-structured Interview Protocol},  
  journal \= {SHS Web of Conferences},  
  volume \= {182},  
  pages \= {04006},  
  year \= {2024},  
  doi \= {10.1051/shsconf/202418204006},  
  url \= {https://doi.org/10.1051/shsconf/202418204006}  
}

@article{Marszalek2024,  
  author \= {Marszałek, K. C. and McCabe, S.},  
  title \= {Sampling in qualitative interview research: Criteria, considerations and guidelines for success},  
  journal \= {Annals of Tourism Research},  
  volume \= {104},  
  pages \= {103711},  
  year \= {2024},  
  doi \= {10.1016/j.annals.2023.103711},  
  url \= {https://doi.org/10.1016/j.annals.2023.103711},  
  note \= {Annals of Tourism Research: 50th Anniversary Issue}  
}

@article{Ting2025,  
  author \= {Ting, H. and Memon, M. A. and Thurasamy, R. and Cheah, J.-H.},  
  title \= {Snowball Sampling: A Review and Guidelines for Survey Research},  
  journal \= {Asian Journal of Business Research},  
  volume \= {15},  
  number \= {1},  
  pages \= {1--15},  
  year \= {2025},  
  doi \= {10.14707/ajbr.250186},  
  url \= {https://doi.org/10.14707/ajbr.250186}  
}  
@article{Ahmad2025,  
  author \= {Ahmad, M. and Wilkins, S.},  
  title \= {Purposive sampling in qualitative research: A framework for the entire journey},  
  journal \= {Quality \\& Quantity},  
  volume \= {59},  
  number \= {2},  
  pages \= {1461--1479},  
  year \= {2025},  
  doi \= {10.1007/s11135-024-02022-5},  
  url \= {https://doi.org/10.1007/s11135-024-02022-5}  
}

@article{Hennink2022,  
  author \= {Hennink, Monique and Kaiser, Bonnie N.},  
  title \= {Sample sizes for saturation in qualitative research: A systematic review of empirical tests},  
  journal \= {Social Science \\& Medicine},  
  volume \= {292},  
  pages \= {114523},  
  year \= {2022},  
  doi \= {10.1016/j.socscimed.2021.114523},  
  url \= {https://doi.org/10.1016/j.socscimed.2021.114523}  
}

@techreport{Kindsiko2019,  
  author \= {Kindsiko, Eneli and Poltimäe, Helen},  
  title \= {The Poor and Embarrassing Cousin to the Gentrified Quantitative Academics: What Determines the Sample Size in Qualitative Interview-Based Organization Studies?},  
  institution \= {SSOAR-Social Science Open Access Repository},  
  year \= {2019},  
  url \= {https://www.ssoar.info/ssoar/handle/document/65324}  
}

@article{Vasileiou2018,  
  author \= {Vasileiou, Konstantina and Barnett, Julie and Thorpe, Susan and Young, Terry},  
  title \= {Characterising and justifying sample size sufficiency in interview-based studies: Systematic analysis of qualitative health research over a 15-year period},  
  journal \= {BMC Medical Research Methodology},  
  volume \= {18},  
  pages \= {1--18},  
  year \= {2018},  
  doi \= {10.1186/s12874-018-0594-7},  
  url \= {https://doi.org/10.1186/s12874-018-0594-7}  
}  
@article{Fusch2015,  
  author \= {Fusch, Patricia and Ness, Lawrence},  
  title \= {Are We There Yet? Data Saturation in Qualitative Research},  
  journal \= {The Qualitative Report},  
  volume \= {20},  
  number \= {9},  
  pages \= {1408--1416},  
  year \= {2015},  
  doi \= {10.46743/2160-3715/2015.2281},  
  url \= {https://doi.org/10.46743/2160-3715/2015.2281}  
}  
@article{Casey2023,  
  author \= {Casey, L. J. and Bowman, S. J. and Wootton, B. M. and McAloon, J. and Power, E.},  
  title \= {“A Tremendous Outpouring of Love and Affection”: A Template Analysis of Positive Experiences During a Major LGBTQ Rights Campaign},  
  journal \= {Journal of Homosexuality},  
  volume \= {70},  
  number \= {9},  
  pages \= {1936--1958},  
  year \= {2023},  
  doi \= {10.1080/00918369.2022.2044272},  
  url \= {https://doi.org/10.1080/00918369.2022.2044272}  
}

@article{Naeem2023,  
  author \= {Naeem, M. and Ozuem, W. and Howell, K. and Ranfagni, S.},  
  title \= {A Step-by-Step Process of Thematic Analysis to Develop a Conceptual Model in Qualitative Research},  
  journal \= {International Journal of Qualitative Methods},  
  volume \= {22},  
  pages \= {16094069231205789},  
  year \= {2023},  
  doi \= {10.1177/16094069231205789},  
  url \= {https://doi.org/10.1177/16094069231205789}  
}

@article{Emerson2026,  
  author \= {Emerson, C. and Klas, A. and Gibson, P. R. and Olive, L. and Fuller-Tyszkiewicz, M. and Mikocka-Walus, A.},  
  title \= {A Qualitative Template Analysis to Understand Patient and Practitioner Perspectives on a Psychological Intervention for Fatigue in Inflammatory Bowel Disease},  
  journal \= {JGH Open},  
  volume \= {10},  
  number \= {2},  
  pages \= {e70363},  
  year \= {2026},  
  doi \= {10.1002/jgh3.70363},  
  url \= {https://doi.org/10.1002/jgh3.70363}  
}

%=============================For previous chapters 4 \====================================

@article{Balla2024,  
  author \= {Balla, J. and Hagger, M. S.},  
  title \= {Protection motivation theory and health behaviour: Conceptual review, discussion of limitations, and recommendations for best practice and future research},  
  journal \= {Health Psychology Review},  
  year \= {2024},  
  volume \= {19},  
  number \= {1},  
  pages \= {145--171},  
  doi \= {10.1080/17437199.2024.2413011},  
  url \= {https://doi.org/10.1080/17437199.2024.2413011}  
}

@phdthesis{Yusuf2024,  
  author \= {Yusuf, A. A.},  
  title \= {Employees’ Cybersecurity Awareness and Behaviour in South African Higher Education Institutions},  
  school \= {University of Pretoria},  
  year \= {2024},  
  type \= {PhD Thesis},  
  address \= {South Africa}  
}

@article{Long2025,  
  author \= {Long, H. A. and Branney, P. and French, D. P. and Brooks, J. M.},  
  title \= {Optimising data sharing whilst protecting participant privacy: A data note describing processed data from a qualitative study of healthcare professionals’ experiences of caring for women with false positive screening test results},  
  journal \= {Health Psychology and Behavioral Medicine},  
  year \= {2025},  
  volume \= {13},  
  number \= {1},  
  pages \= {2449400},  
  doi \= {10.1080/21642850.2024.2449400},  
  url \= {https://doi.org/10.1080/21642850.2024.2449400}  
}  
@article{Lobe2022,  
  author \= {Lobe, B. and Morgan, D. L. and Hoffman, K.},  
  title \= {A Systematic Comparison of In-Person and Video-Based Online Interviewing},  
  journal \= {International Journal of Qualitative Methods},  
  year \= {2022},  
  volume \= {21},  
  pages \= {16094069221127068},  
  doi \= {10.1177/16094069221127068},  
  url \= {https://doi.org/10.1177/16094069221127068}  
}

@article{Taherdoost2022,  
  author \= {Taherdoost, H.},  
  title \= {How to Conduct an Effective Interview; A Guide to Interview Design in Research Study},  
  journal \= {International Journal of Academic Research in Management},  
  year \= {2022},  
  volume \= {11},  
  number \= {1},  
  pages \= {1--10}  
}

@article{Young2018,  
  author \= {Young, J. C. and Rose, D. C. and Mumby, H. S. and Benitez-Capistros, F. and Derrick, C. J. and Finch, T. and Garcia, C. and Home, C. and Marwaha, E. and Morgans, C. and Parkinson, S. and Shah, J. and Wilson, K. A. and Mukherjee, N.},  
  title \= {A methodological guide to using and reporting on interviews in conservation science research},  
  journal \= {Methods in Ecology and Evolution},  
  year \= {2018},  
  volume \= {9},  
  number \= {1},  
  pages \= {10--19},  
  doi \= {10.1111/2041-210X.12828},  
  url \= {https://doi.org/10.1111/2041-210X.12828}  
}

@phdthesis{Cohen2022,  
  author \= {Cohen, S.},  
  title \= {The Exploration of Cyber-Security Information for Home Users: A Qualitative Exploratory Case Study},  
  school \= {University of Phoenix},  
  year \= {2022},  
  type \= {PhD Thesis}  
}

@phdthesis{Tran2022,  
  author \= {Tran, N. T.},  
  title \= {Perceptions Of Higher Education Learners And Educators Regarding The Learner-Centered Strategy Implementation: A Qualitative Single Case Study},  
  school \= {The University of Nebraska \- Lincoln},  
  year \= {2022},  
  type \= {PhD Thesis}  
}

@article{McIntosh2015,  
  author \= {McIntosh, M. J. and Morse, J. M.},  
  title \= {Situating and Constructing Diversity in Semi-Structured Interviews},  
  journal \= {Global Qualitative Nursing Research},  
  year \= {2015},  
  volume \= {2},  
  pages \= {2333393615597674},  
  doi \= {10.1177/2333393615597674},  
  url \= {https://doi.org/10.1177/2333393615597674}  
}

@article{Woods2016,  
  author \= {Woods, M. and Paulus, T. and Atkins, D. P. and Macklin, R.},  
  title \= {Advancing Qualitative Research Using Qualitative Data Analysis Software (QDAS)? Reviewing Potential Versus Practice in Published Studies using ATLAS.ti and NVivo, 1994--2013},  
  journal \= {Social Science Computer Review},  
  year \= {2016},  
  volume \= {34},  
  number \= {5},  
  pages \= {597--617},  
  doi \= {10.1177/0894439315596311}  
}  
@book{Patton2015,  
  author \= {Patton, M. Q.},  
  title \= {Qualitative research \\& evaluation methods: Integrating theory and practice},  
  publisher \= {SAGE Publications, Inc.},  
  year \= {2015},  
  edition \= {Fourth},  
  address \= {Thousand Oaks, CA}  
}  
@article{Cronje2024,  
  author \= {Cronje, J. C. and Okigui, H. and Francke, E. R.},  
  title \= {An Analysis of Cybersecurity Policy Compliance in Organisations},  
  journal \= {Applied Cybersecurity \\& Internet Governance},  
  year \= {2024},  
  doi \= {10.60097/ACIG/191942},  
  url \= {https://doi.org/10.60097/ACIG/191942}  
}

 

@article{Bonello2019,  
  author \= {Bonello, M. and Meehan, B.},  
  title \= {Transparency and coherence in a doctoral study case analysis: Reflecting on the use of NVivo within a 'Framework' approach},  
  journal \= {The Qualitative Report},  
  year \= {2019},  
  volume \= {24},  
  number \= {3},  
  pages \= {483--498},  
  issn \= {1052--0147}  
}

@article{Maher2018,  
  author \= {Maher, C. and Hadfield, M. and Hutchings, M. and de Eyto, A.},  
  title \= {Ensuring Rigor in Qualitative Data Analysis: A Design Research Approach to Coding Combining NVivo With Traditional Material Methods},  
  journal \= {International Journal of Qualitative Methods},  
  year \= {2018},  
  volume \= {17},  
  number \= {1},  
  pages \= {1609406918786362},  
  doi \= {10.1177/1609406918786362},  
  url \= {https://doi.org/10.1177/1609406918786362}  
}

@techreport{NHMRC2018,  
  author \= {{National Health and Medical Research Council}},  
  title \= {Australian Code for the Responsible Conduct of Research 2018},  
  institution \= {NHMRC, Australian Research Council and Universities Australia},  
  year \= {2018},  
  address \= {Canberra, Australia},  
  url \= {https://www.nhmrc.gov.au/about-us/publications/australian-code-responsible-conduct-research-2018}  
}

@inbook{Brooks2014,  
  author \= {Brooks, J. and King, N.},  
  title \= {Doing Template Analysis: Evaluating an End-of-Life Care Service},  
  booktitle \= {SAGE Research Methods Cases},  
  year \= {2014},  
  publisher \= {SAGE Publications Ltd},  
  doi \= {10.4135/978144627305013512755},  
  url \= {https://doi.org/10.4135/978144627305013512755}  
}

@article{Maguire2017,  
  author \= {Maguire, M. and Delahunt, B.},  
  title \= {Doing a Thematic Analysis: A Practical, Step-by-Step Guide for Learning and Teaching Scholars},  
  journal \= {All Ireland Journal of Higher Education},  
  year \= {2017},  
  volume \= {9},  
  number \= {3}  
}  
@article{Hadi2005,  
  author \= {Hadi, H. J. and Omar, M. A. and Osman, W. R. S. and Ibrahim, M. F. and Hussaini, M.},  
  title \= {Performing a Content Validity: Establishing a Reliable Instrument to Measure the Intention to Adopt Cloud Computing Software as a Service in Public Organisation},  
  journal \= {Journal of Theoretical and Applied Information Technology},  
  year \= {2005},  
  number \= {22}  
}

@article{Yusoff2019,  
  author \= {Yusoff, M. S. B.},  
  title \= {ABC of Content Validation and Content Validity Index Calculation},  
  journal \= {Education in Medicine Journal},  
  year \= {2019},  
  volume \= {11},  
  number \= {2},  
  pages \= {49--54},  
  doi \= {10.21315/eimj2019.11.2.6}  
}

@incollection{Furnell2025,  
  author \= {Furnell, S.},  
  title \= {Security Fatigue},  
  booktitle \= {Encyclopedia of Cryptography, Security and Privacy},  
  year \= {2025},  
  publisher \= {Springer Nature Link}  
}

@article{Saunders2018,  
  author \= {Saunders, B. and Sim, J. and Kingstone, T. and Baker, S. and Waterfield, J. and Bartlam, B. and Burroughs, H. and Jinks, C.},  
  title \= {Saturation in qualitative research: Exploring its conceptualization and operationalization},  
  journal \= {Quality \\& Quantity},  
  year \= {2018},  
  volume \= {52},  
  number \= {4},  
  pages \= {1893--1907},  
  doi \= {10.1007/s11135-017-0574-8}  
}

@article{Hennink2017,  
  author \= {Hennink, M. M. and Kaiser, B. N. and Marconi, V. C.},  
  title \= {Code Saturation Versus Meaning Saturation: How Many Interviews Are Enough?},  
  journal \= {Qualitative Health Research},  
  year \= {2017},  
  volume \= {27},  
  number \= {4},  
  pages \= {591--608},  
  doi \= {10.1177/1049732316665344}  
}

@article{Jennings2025,  
  author \= {Jennings, B. M. and Yeager, K. A.},  
  title \= {Re-viewing the concept of saturation in qualitative research},  
  journal \= {International Journal of Nursing Studies Advances},  
  year \= {2025},  
  volume \= {8},  
  pages \= {100298},  
  doi \= {10.1016/j.ijnsa.2025.100298}  
}

@article{Ishak2014,  
  author \= {Ishak, N. M. and Bakar, A. Y. A.},  
  title \= {Developing Sampling Frame for Case Study: Challenges and Conditions},  
  journal \= {World Journal of Education},  
  year \= {2014},  
  volume \= {4},  
  number \= {3},  
  pages \= {29--35},  
  doi \= {10.5430/wje.v4n3p29}  
}

@article{Kiger2020,  
  author \= {Kiger, M. E. and Varpio, L.},  
  title \= {Thematic analysis of qualitative data: AMEE Guide No. 131},  
  journal \= {Medical Teacher},  
  year \= {2020},  
  volume \= {42},  
  number \= {8},  
  pages \= {846--854},  
  doi \= {10.1080/0142159X.2020.1755030}  
}

@article{Braun2021,  
  author \= {Braun, V. and Clarke, V.},  
  title \= {To saturate or not to saturate? Questioning data saturation as a useful concept for thematic analysis and sample-size rationales},  
  journal \= {Qualitative Research in Sport, Exercise and Health},  
  year \= {2021},  
  volume \= {13},  
  number \= {2},  
  pages \= {201--216},  
  doi \= {10.1080/2159676X.2019.1704846}  
}

@article{McMullin2023,  
  author \= {McMullin, C.},  
  title \= {Transcription and Qualitative Methods: Implications for Third Sector Research},  
  journal \= {Voluntas},  
  year \= {2023},  
  volume \= {34},  
  number \= {1},  
  pages \= {140--153},  
  doi \= {10.1007/s11266-021-00400-3}  
}

@article{Oliver2005,  
  author \= {Oliver, D. G. and Serovich, J. M. and Mason, T. L.},  
  title \= {Constraints and Opportunities with Interview Transcription: Towards Reflection in Qualitative Research},  
  journal \= {Social Forces},  
  year \= {2005},  
  volume \= {84},  
  number \= {2},  
  pages \= {1273--1289},  
  doi \= {10.1353/sof.2006.0023}  
}

@article{Stuckey2014,  
  author \= {Stuckey, H. L.},  
  title \= {The first step in Data Analysis: Transcribing and managing qualitative research data},  
  journal \= {Journal of Social Health and Diabetes},  
  year \= {2014},  
  volume \= {2},  
  number \= {1},  
  pages \= {6--10}  
}

@article{Bingham2021,  
  author \= {Bingham, A. J.},  
  title \= {How Distributed Leadership Facilitates Technology Integration: A Case Study of \`\`Pilot Teachers''},  
  journal \= {Teachers College Record},  
  year \= {2021},  
  volume \= {123},  
  number \= {3},  
  pages \= {1--38}  
}

@article{Azungah2018,  
  author \= {Azungah, T.},  
  title \= {Qualitative research: Deductive and inductive approaches to data analysis},  
  journal \= {Qualitative Research Journal},  
  year \= {2018},  
  volume \= {18},  
  number \= {4},  
  pages \= {383--400},  
  doi \= {10.1108/QRJ-D-18-00035}  
}

@article{Linneberg2019,  
  author \= {Linneberg, M. S. and Korsgaard, S.},  
  title \= {Coding qualitative data: A synthesis guiding the novice},  
  journal \= {Qualitative Research Journal},  
  year \= {2019},  
  volume \= {19},  
  number \= {3},  
  pages \= {259--270},  
  doi \= {10.1108/QRJ-12-2018-0012}  
}

%=============================For previous chapters 5====================================

 

@article{Kennison2020,  
  author \= {Kennison, S. M. and Chan-Tin, E.},  
  title \= {Taking Risks With Cybersecurity: Using Knowledge and Personal Characteristics to Predict Self-Reported Cybersecurity Behaviors},  
  journal \= {Frontiers in Psychology},  
  year \= {2020},  
  volume \= {11},  
  pages \= {546546},  
  doi \= {10.3389/fpsyg.2020.546546},  
  url \= {https://doi.org/10.3389/fpsyg.2020.546546}  
}  
@article{Moody2018,  
  author \= {Moody, G. D. and Siponen, M. and Pahnila, S.},  
  title \= {Toward a Unified Model of Information Security Policy Compliance},  
  journal \= {MIS Quarterly},  
  year \= {2018},  
  volume \= {42},  
  number \= {1},  
  pages \= {285--311},  
  doi \= {10.25300/MISQ/2018/13853},  
  url \= {https://doi.org/10.25300/MISQ/2018/13853}  
}

%=============================For previous chapters 6====================================  
@article{Ciagala2024,  
  author \= {Ciagala, K. R. and Reichin, S. L. and Parsons, K. and Hunter, S. T.},  
  title \= {Physical security culture: The neglected foundation for effective security},  
  journal \= {Safety Science},  
  year \= {2024},  
  volume \= {175},  
  pages \= {106518},  
  doi \= {10.1016/j.ssci.2024.106518}  
}  
@article{Sidor2022,  
  author \= {Sidor-Rządkowska, M.},  
  title \= {Human—The weakest or the strongest link? {T}he role of organisational culture in ensuring security of remote work},  
  journal \= {Journal of Modern Science},  
  year \= {2022},  
  volume \= {49},  
  number \= {2},  
  pages \= {608--620},  
  doi \= {10.13166/jms/156776}  
}

@article{Yeng2022,  
  author \= {Yeng, K. and Fauzi, M. A. and Sun, L.},  
  title \= {Assessing the Legal Aspects of Information Security Requirements for Health Care in 3 Countries: {S}coping Review and Framework Development},  
  journal \= {JMIR Human Factors},  
  year \= {2022},  
  volume \= {9},  
  number \= {2},  
  doi \= {10.2196/30050}  
}  
@techreport{Gutterman2023,  
  author      \= {Gutterman, A. S.},  
  title       \= {Organizational Culture: State of the Research 2023},  
  institution \= {Social Science Research Network},  
  year        \= {2023},  
  type        \= {SSRN Scholarly Paper},  
  number      \= {4403558},  
  url         \= {https://papers.ssrn.com/abstract=4403558}  
}  
@article{Cains2022,  
  author \= {Cains, M. G. and Flora, L. and Taber, D. and King, Z. and Henshel, D.},  
  title \= {Defining Cyber Security and Cyber Security Risk within a Multidisciplinary Context using Expert Elicitation},  
  journal \= {Risk Analysis},  
  publisher \= {Wiley},  
  year \= {2022},  
  volume \= {42},  
  doi \= {10.1111/risa.13687}  
}

@book{Tryfonas2015,  
  editor \= {Tryfonas, T. and Askoxylakis, I.},  
  title \= {Human Aspects of Information Security, Privacy, and Trust: Third International Conference, HAS 2015, Held as Part of HCI International 2015, Los Angeles, CA, USA, August 2-7, 2015\. Proceedings},  
  series \= {Lecture Notes in Computer Science},  
  volume \= {9190},  
  publisher \= {Springer International Publishing},  
  year \= {2015},  
  doi \= {10.1007/978-3-319-20376-8}  
}

@article{Donalds2020,  
  author \= {Donalds, Charlette and Osei-Bryson, Kweku-Muata},  
  title \= {Cybersecurity compliance behavior: Exploring the influences of individual decision style and other antecedents},  
  journal \= {International Journal of Information Management},  
  volume \= {51},  
  pages \= {102056},  
  year \= {2020},  
  doi \= {10.1016/j.ijinfomgt.2019.102056},  
  url \= {https://doi.org/10.1016/j.ijinfomgt.2019.102056}  
}

%=============================For previous chapters 7====================================

@article{Barruga2025,  
  author \= {Barruga, M. B.},  
  title \= {Cybersecurity Strategy for Higher Education Institutions: {A} Thematic Analysis on Standards and Frameworks},  
  journal \= {Journal of Information Systems Engineering and Management},  
  year \= {2025},  
  volume \= {10},  
  number \= {43s},  
  pages \= {1140--1152},  
  doi \= {10.52783/jisem.v10i43s.8533}  
}

@article{Terrell2023,  
  author \= {Terrell, S. R. and Lingelbach, K.},  
  title \= {Validating Prior Research: {A} Qualitative Study of the Career Perspectives and Experiences of Female Cybersecurity Professionals},  
  journal \= {Issues In Information Systems},  
  year \= {2023},  
  doi \= {10.48009/4\_iis\_2023\_109}  
}

@article{Perera2022,  
  author \= {Perera, S. and Jin, X. and Maurushat, A. and Opoku, D.-G. J.},  
  title \= {Factors Affecting Reputational Damage to Organisations Due to Cyberattacks},  
  journal \= {Informatics},  
  year \= {2022},  
  volume \= {9},  
  number \= {1},  
  pages \= {28},  
  doi \= {10.3390/informatics9010028}  
}  
@article{Kamarulzaman2024,  
  author \= {Kamarulzaman, M. S. and Shuhidan, S. M. and Wahid, K. A. and Wahab, A. A. and Toha, A. J.},  
  title \= {Content Validity of Assessment Instrument for Information Security Culture in Relation to Digital Literacy},  
  journal \= {Journal of Information and Knowledge Management},  
  year \= {2024},  
  volume \= {14},  
  number \= {1},  
  pages \= {95--107},  
  doi \= {10.24191/jikm.v14i1.4688}  
}

@article{Haney2020,  
  author \= {Haney, J. and Lutters, W.},  
  title \= {Security Awareness Training for the Workforce: {M}oving Beyond \`\`Check-the-Box'' Compliance},  
  journal \= {Computer},  
  year \= {2020},  
  volume \= {53},  
  number \= {10},  
  pages \= {91--95},  
  doi \= {10.1109/mc.2020.3001959}  
}

@phdthesis{Ali2025,  
  author \= {Ali, Mohammad Ghulam},  
  title \= {Cybersecurity Governance and Policy Development in Higher Education Institutions: {A} Strategic Framework for Resilience and Compliance},  
  journal \= {IIT Kharagpur},  
  year \= {2025},  
  type \= {{PhD} Thesis}  
}

@article{alghafri2024,  
title={Understanding Big Data Adoption and its Impact on Decision-Making Quality: A Perspective from Public Sector IT Managers in Oman},  
author={AlGhafri, G. and AlBalushi, T. and Rahim, M. M.},  
journal={Journal of System and Management Sciences},  
year={2024},  
doi={10.33168/JSMS.2024.1113},  
url={https://doi.org/10.33168/JSMS.2024.1113}  
}

@article{Cram2023,  
  author \= {Cram, W. A. and D'Arcy, J.},  
  title \= {\`What a waste of time': {A}n examination of cybersecurity legitimacy},  
  journal \= {Information Systems Journal},  
  year \= {2023},  
  volume \= {34},  
  number \= {2},  
  pages \= {483--515},  
  doi \= {10.1111/isj.12460}  
}

@phdthesis{Ngwese2025,  
  author \= {Ngwese, F.},  
  title \= {Strategies to Implement Employee Cybersecurity Awareness Programs},  
  school \= {Walden University},  
  year \= {2025},  
  type \= {{PhD} Thesis}  
}  
@article{Ifinedo2012,  
  author \= {Ifinedo, P.},  
  title \= {Understanding information systems security policy compliance: {A}n integration of the theory of planned behavior and the protection motivation theory},  
  journal \= {Computers \\& Security},  
  year \= {2012},  
  volume \= {31},  
  number \= {1},  
  pages \= {83--95},  
  doi \= {10.1016/j.cose.2011.10.007}  
}  
@phdthesis{brown2024,  
  author={Brown, R.},  
  title={Best Practices In Employee Cybersecurity Training: A Qualitative Delphi Study},  
  school={University of Phoenix},  
  year={2024}  
}  
@article{dextras2023,  
  title={Organisational culture and leadership behaviours: Is manager’s psychological health the missing piece?},  
  author={Dextras-Gauthier, Julie and Marchand, André and Ouellet, Simon and Boudrias, Jean-Sébastien},  
  journal={International Journal of Environmental Research and Public Health},  
  volume={20},  
  number={5},  
  pages={3982},  
  year={2023}  
}  
 

@article{Siponen2014,  
  author \= {Siponen, M. and Adam Mahmood, M. and Pahnila, S.},  
  title \= {Employees' adherence to information security policies: {A}n exploratory field study},  
  journal \= {Information \\& Management},  
  year \= {2014},  
  volume \= {51},  
  number \= {2},  
  pages \= {217--224},  
  doi \= {10.1016/j.im.2013.08.006}  
}  
@article{Posey2014,  
  author \= {Posey, C. and Roberts, T. L. and Lowry, P. B. and Hightower, R. T.},  
  title \= {Bridging the divide: {A} qualitative comparison of information security thought patterns between information security professionals and ordinary organizational insiders},  
  journal \= {Information \\& Management},  
  year \= {2014},  
  volume \= {51},  
  number \= {5},  
  pages \= {551--567},  
  doi \= {10.1016/j.im.2014.03.009}  
}  
@article{Venkat2020,  
  author \= {Venkat, M. S. and Patil, G. M.},  
  title \= {Founder Leaders and Organization Culture: {A} Comparative Study on Indian and American Founder Leaders Based on Schein’s Model of Organizational Culture},  
  journal \= {IIM Kozhikode Society \\& Management Review},  
  year \= {2020},  
  volume \= {9},  
  number \= {1},  
  pages \= {23--33},  
  doi \= {10.1177/2277975219890932}  
}

%=============================For previous chapters 8====================================

@article{Park1995,  
  author \= {Park, O. C. and Gittelman, S. S.},  
  title \= {Dynamic characteristics of mental models and dynamic visual displays},  
  journal \= {Instructional Science},  
  year \= {1995},  
  volume \= {23},  
  number \= {5--6},  
  pages \= {303--320},  
  doi \= {10.1007/BF00896876}  
}

@article{Schoenmakers2023,  
  author \= {Schoenmakers, K. and Greene, D. and Stutterheim, S. and Lin, H. and Palmer, M. J.},  
  title \= {The security mindset: {C}haracteristics, development, and consequences},  
  journal \= {Journal of Cybersecurity},  
  year \= {2023},  
  volume \= {9},  
  number \= {1},  
  pages \= {tyad010},  
  doi \= {10.1093/cybsec/tyad010}  
}

@article{Angafor2023,  
  author \= {Angafor, G. N. and Yevseyeva, I. and Maglaras, L.},  
  title \= {Scenario-based incident response training: {L}essons learnt from conducting an experiential learning virtual incident response tabletop exercise},  
  journal \= {Information \\& Computer Security},  
  year \= {2023},  
  volume \= {31},  
  number \= {4},  
  pages \= {404--426},  
  doi \= {10.1108/ICS-05-2022-0085}  
}

@article{Dreimane2025,  
  author \= {Dreimane, R. P. and Brilingaitė, A. and Roponena, E. and Parish, K. and Grabis, J. and Lugo, R. G. and Bonders, M.},  
  title \= {Try to es{CAPE} from {C}ybersecurity {I}ncidents\! {A} {T}echnology-{E}nhanced {E}ducational {A}pproach},  
  journal \= {Technology, Knowledge and Learning},  
  year \= {2025},  
  volume \= {30},  
  number \= {3},  
  pages \= {1577--1606},  
  doi \= {10.1007/s10758-024-09769-8}  
}

@article{Boeken2024,  
  author \= {Boeken, J.},  
  title \= {From compliance to security, responsibility beyond law},  
  journal \= {Computer Law \\& Security Review},  
  year \= {2024},  
  volume \= {52},  
  pages \= {105926},  
  doi \= {10.1016/j.clsr.2023.105926}  
}

@article{Panteli2025,  
  author \= {Panteli, N. and Nthubu, B. R. and Mersinas, K.},  
  title \= {Being {R}esponsible in {C}ybersecurity: {A} {M}ulti-{L}ayered {P}erspective},  
  journal \= {Information Systems Frontiers},  
  year \= {2025},  
  doi \= {10.1007/s10796-025-10588-0}  
}

@phdthesis{Dennehy2021,  
  author \= {Dennehy, M. and Mostafa, A. and Curtis, R. and Litchmore, K. and Straub, J. A. and Dean, I.},  
  title \= {{PREVENTING INSIDER CYBERTHREATS IN ORGANIZATIONS: A QUALITATIVE DELPHI STUDY}},  
  school \= {Capella University},  
  year \= {2021}  
}

@article{Cram2021,  
  author \= {Cram, W. A. and Proudfoot, J. G. and D'Arcy, J.},  
  title \= {When enough is enough: {I}nvestigating the antecedents and consequences of information security fatigue},  
  journal \= {Information Systems Journal},  
  year \= {2021},  
  volume \= {31},  
  number \= {4},  
  pages \= {521--549},  
  doi \= {10.1111/isj.12319}  
}

@article{Dutton2017,  
  author \= {Dutton, W. H.},  
  title \= {Fostering a cyber security mindset},  
  journal \= {Internet Policy Review},  
  year \= {2017},  
  volume \= {6},  
  number \= {1},  
  doi \= {10.14763/2017.1.443}  
}

@article{Darcy2014,  
  author \= {D'Arcy, J. and Greene, G.},  
  title \= {Security culture and the employment relationship as drivers of employees' security compliance},  
  journal \= {Information Management \\& Computer Security},  
  year \= {2014},  
  volume \= {22},  
  number \= {5},  
  pages \= {474--489},  
  doi \= {10.1108/IMCS-08-2013-0057}  
}  
@article{dextrasgauthier2023,  
  author={Dextras-Gauthier, J. and Gilbert, M.-H. and Dima, J. and Adou, L. B.},  
  title={Organizational culture and leadership behaviors: Is manager’s psychological health the missing piece?},  
  journal={Frontiers in Psychology},  
  volume={14},  
  year={2023},  
  doi={10.3389/fpsyg.2023.1237775}  
}  
@incollection{adamu2025,  
  author    \= {Adamu, M. A. and Niemimaa, M. I. and Spagnoletti, P.},  
  title     \= {Towards a Three-Tiered Framework for Fostering Organizational Cybersecurity Culture},  
  booktitle \= {Information Systems},  
  editor    \= {Themistocleous, M. and Bakas, N. and Kokosalakis, G. and Papadaki, M.},  
  series    \= {Lecture Notes in Business Information Processing},  
  volume    \= {536},  
  pages     \= {313--324},  
  year      \= {2025},  
  publisher \= {Springer Nature Switzerland},  
  address   \= {Cham},  
  doi       \= {10.1007/978-3-031-81325-2\_22}  
}

@article{Mortazavi2019,  
  author \= {Mortazavi, S. A. R. and Esfahani, F. S.},  
  title \= {A checklist based evaluation framework to measure risk of information security management systems},  
  journal \= {International Journal of Information Technology},  
  year \= {2019},  
  volume \= {11},  
  number \= {3},  
  pages \= {517--534},  
  doi \= {10.1007/s41870-019-00302-0}  
}

@inproceedings{Rajamaki2024,  
  author \= {Rajam{\\"a}ki, J. and Wood, K. and Espada, B.},  
  title \= {{LOCKing} Patient Safety: {A} Dynamic Cybersecurity Checklist for Healthcare Workers},  
  booktitle \= {European Conference on Cyber Warfare and Security},  
  year \= {2024},  
  volume \= {23},  
  number \= {1},  
  pages \= {811--815},  
  doi \= {10.34190/eccws.23.1.2072}  
}

@article{Sabillon2024,  
  author \= {Sabillon, R. and Higuera, J. R. B. and Cano, J. and Higuera, J. B. and Montalvo, J. A. S.},  
  title \= {Assessing the Effectiveness of Cyber Domain Controls When Conducting Cybersecurity Audits: {I}nsights from Higher Education Institutions in {C}anada},  
  journal \= {Electronics},  
  year \= {2024},  
  volume \= {13},  
  number \= {16},  
  pages \= {3257},  
  doi \= {10.3390/electronics13163257}  
}  
   
@article{Mizrak2025,  
  author \= {Mizrak, F. and Demirel, H. G. and Ya{\\c{s}}ar, O. and Karakaya, T.},  
  title \= {Digital detox: Exploring the impact of cybersecurity fatigue on employee productivity and mental health},  
  journal \= {Discover Mental Health},  
  volume \= {5},  
  number \= {1},  
  pages \= {25},  
  year \= {2025},  
  doi \= {10.1007/s44192-025-00149-x},  
  url \= {https://doi.org/10.1007/s44192-025-00149-x}  
}

@article{Petric2025,  
  author \= {Petri{\\v{c}}, G. and Just, J. N.},  
  title \= {Information security culture and phishing-reporting model: {S}tructural equivalence across {G}ermany, {UK}, and {USA}},  
  journal \= {Journal of Cybersecurity},  
  year \= {2025},  
  volume \= {11},  
  number \= {1},  
  pages \= {tyaf011},  
  doi \= {10.1093/cybsec/tyaf011}  
}

@article{Hibshi2016,  
  author \= {Hibshi, H. and Breaux, T. D. and Riaz, M. and Williams, L.},  
  title \= {A grounded analysis of experts’ decision-making during security assessments},  
  journal \= {Journal of Cybersecurity},  
  year \= {2016},  
  volume \= {2},  
  number \= {1},  
  pages \= {tyw010},  
  doi \= {10.1093/cybsec/tyw010}  
}

@phdthesis{Schatz2018,  
  author \= {Schatz, D.},  
  title \= {Towards a Comprehensive Evidence-Based Approach For Information Security Value Assessment},  
  school \= {University of East London},  
  year \= {2018},  
  type \= {{PhD} Thesis},  
  doi \= {10.15123/PUB.7950}  
}

@article{Stenfors2020,  
  author \= {Stenfors, T. and Kajamaa, A. and Bennett, D.},  
  title \= {How to … assess the quality of qualitative research},  
  journal \= {The Clinical Teacher},  
  year \= {2020},  
  volume \= {17},  
  number \= {6},  
  pages \= {596--599},  
  doi \= {10.1111/tct.13242}  
}

%=============================For previous chapters 9===================================

 

   
