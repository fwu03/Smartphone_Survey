# Milestone 1: Proposal

### Research Question
The survey is designed to investigate a research question: Does an individuals choice of phone (and thus phone operating system) influence their current choice of laptop operating system?

### Background

The idea is that since the smartphone operating system industry is dominated by iOS and Android and the laptop operating system industry is dominated by Mac OS and Windows (also Linux, but for the purposes of this investigation it falls under 'Other'), we want to see if having there is any relation between the phones that people own and their PC operating system choices. 

The hypothesis is that the choice of phone will influence the choice of laptop in the individuals. For example, people with an iPhone will have a non-negligible preference for purchasing/owning a Mac, and people with an Android will edge towards a Windows or Linux OS.

### Survey Questions
Q1: Do you own a smartphone?
- Yes
- No

> This question identifies a confounding variable: Whether someone has a smartphone or not (Categorical)

Q2: What smartphone operating system/platform do you have?
- Android
- iOS
- Other

> This question identifies the independent variable in our analysis: Smartphone operating system

Q3: What is your level of satisfaction using your current phone/phone OS?
1 - 2 - 3 - 4 - 5

> This question identifies a confounding variable: Someone's satisfaction level toward their phone operating system (Numerical/Ordinal)
> Someone satisfaction level toward their phone operating system can influence their choice of both smartphone and laptop operating systems.

Q4: How long ago did you purchase your current phone (years ago)?

less than 1 - 2 - 3 - 4 - more than 5

> This question will allow us to compare this to the purchase date of their laptop and understand the chronology of the purchases (i.e. what came before what).

Q5: What was your previous smartphone platform?
- Android
- iOS
- Didn’t have a phone before

> This question identifies a confounding variable: Someone's previous smartphone operating system(Categorical)
> Someone keep using the same operating system on their phone indicates that they are used to the system, and they are less likely to change the systems on their smartphone and laptop.

Q6: If you were to purchase a phone today, would you stick to your operating system or switch?

Q7: What is the most common phone within your family?
- Android
- iOS
- Other

Q8: Whats the most common phone within your friend group?
- Android
- iOS
- Other

> These questions identify two confounding variables: Someone's family smartphone operating system (Categorical), their friends' smartphone operating systems (Categorical)
> The common choice of phone operating systems within the family and friends may also influence someone's choice toward both smartphone and laptop.

Q9: Do you own a laptop?

- Yes
- No

> This question is similar to Q1 and is simply to 

Q10: What operating system is running on your PC
- Mac OS
- Windows
- Other

> This question identify the dependent variable in our analysis: Laptop operating system

Q11: What is your level of satisfaction using your current laptop?
(Least Satisfied) 1 - 2 - 3 - 4 - 5 (Most Satisfied)

> This question identifies a confounding variable: Someone's satisfaction of the laptop operating system (Numerical)
> Someone satisfaction level toward their laptop operating system can influence their choice of both smartphone and laptop operating systems.

Q12: How long ago did you purchase your current PC (years ago)?

less than 1 - 2 - 3 - 4 - more than 5

> This question will allow us to compare this to the purchase date of their phone and understand the chronology of the purchases (i.e. what came before what).

Q13: If you were to purchase a laptop today, what operating system do you envision will be running on your next PC?
- Mac OS
- Windows
- Other

> This question identifies a confounding variable: Someone's future choice for the laptop operating system (Categorical)
> The future choice of the laptop operating system indicates whether or not someone get used to the system and their satisfaction of it, this variable may influence the choice of both smartphone and laptop operating systems.

Q14: What laptop operating system is used/required at your place of employment/study?

- Mac OS
- Windows
- Other
- Either/Doesn't Matter
- Don't use PC at work/study

> This question will identify the confounding variable of an individuals workplace requirements that may influence their current choice of PC.

Optional Questions:
What type of phone do you have?
- Apple
- Samsung
- Windows
- Blackberry
- Huawei
- Other: Please Enter

> This question identify more details about the independent variable

### Statistics Analysis
Describe the plan to analyze the survey results

A chi-square test of independence will be used to test for association between the independent variable, choice of smartphone platform, and the dependent variable, choice of laptop platform. The null hypothesis is that the choices of laptop platform is independent of phone platform. The alternative hypothesis is that choices laptop platform is not independent of phone platform. The test statistic for the Chi-square test is denote by:

![alt text](chisq.PNG)

r: number of rows <br/>
c: number of columns <br/>
O_ik: observed count of the cell in the i row and the k column <br/>
E_ik: the expected count of the cell in the i row and the k column <br/>

Data collected from the survey will be analyzed using R. A contingency table will be created, then follow by a chi-square test of independence.


### Online Surveys Ethics
Discuss the aspects of the UBC Office of Research Ethics document on Using Online Surveys that are relevant to the proposed survey.

Based on the UBC Office of Research Ethics document, all online survey data will be stored and accessed in Canada only. In addition, no private information, such as names, IP address, or any information that can indirectly identify someone, will be collected in the survey. Thus, a cover letter will be used instead of a full signed consent form.
