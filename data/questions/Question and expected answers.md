# Teen Mental Health RAG Evaluation Set

| question_id | question_type | difficulty | question | expected_answer | supporting_docs | key_facts_required | answer_style | evaluation_notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Q01 | factual | easy | Which social media platform is associated with the highest average anxiety scores among teens? | According to the dataset, TikTok-exclusive users demonstrate the highest average anxiety levels at 5.75/10. This exceeds the anxiety levels reported for Instagram-only users (5.67/10) and those using multiple platforms (5.49/10). | DOC_01 | - TikTok avg anxiety is 5.75/10 - Higher than Instagram-only (5.67) - Higher than "Both" (5.49) | extractive | Correct identification of TikTok and the score 5.75 is required. |
| Q02 | factual | easy | What is the specific statistical correlation between sleep hours and the presence of a depression label? | There is a negative correlation coefficient of -0.19 between sleep hours and the presence of a depression label. This represents the strongest correlation among all behavioral variables in the dataset. | DOC_02 | - Correlation coefficient is -0.19 - Relationship is negative - Strongest correlation in dataset | extractive | Correct value (-0.19) and negative direction are mandatory. |
| Q03 | factual | medium | For teens with the highest tier of pre-sleep screen time, what is the reported average addiction level? | Teens in the highest bracket of pre-sleep screen time (2.5 to 3.0 hours) report an average addiction level of 5.78. This group also shows a higher incidence of depression markers compared to lower-usage groups. | DOC_03 | - Range is 2.5-3.0 hours - Avg addiction level is 5.78 - Higher than 0.5-1.0h group (5.40) | extractive | Accurate mapping of the 2.5-3.0h range to the 5.78 value is required. |
| Q04 | factual | easy | What is the average daily physical activity duration for adolescents identified in the "High-Risk" profile? | Adolescents categorized as "High-Risk" report an average of 0.95 hours of physical activity per day. This is lower than the overall dataset mean of 1.01 hours. | DOC_04, DOC_06 | - High-Risk activity is 0.95 hours - Below dataset mean (1.01) | extractive | Must cite the 0.95 hours figure. |
| Q05 | factual | easy | Compare the average anxiety and stress levels of teens with "low" social interaction levels to the dataset means. | Teens with "low" social interaction levels report average anxiety of 5.52 and stress of 5.35. These are the lowest averages among the three interaction categories (High, Medium, Low). | DOC_05 | - Low interaction anxiety is 5.52 - Low interaction stress is 5.35 - Lowest of all categories | extractive | Requires both values (5.52 and 5.35). |
| Q06 | comparison | medium | How do stress levels differ between TikTok-only users and users who engage with both Instagram and TikTok? | TikTok-only users report the lowest mean stress levels at 5.29/10. In contrast, users of "Both" platforms report the highest average stress levels at 5.55/10, suggesting a potential cognitive load from platform switching. | DOC_01 | - TikTok-only stress is 5.29 - "Both" platform stress is 5.55 - "Both" is higher than TikTok-only | abstractive_grounded | Comparison must identify "Both" as higher stress than TikTok. |
| Q07 | comparison | hard | Contrast the daily social media usage and sleep hours between high-risk and low-risk teen profiles. | High-risk teens average 6.72 hours of social media daily and only 4.76 hours of sleep. Low-risk teens spend significantly less time on social media (4.55 hours) and sleep more (6.59 hours). | DOC_06 | - High-risk: 6.72h social media / 4.76h sleep - Low-risk: 4.55h social media / 6.59h sleep - High-risk has ~1.8h less sleep | abstractive_grounded | All four numerical values are needed for a complete comparison. |
| Q08 | comparison | medium | Describe the change in depression label incidence as pre-sleep screen time increases from the 1-2 hour bracket to the 2-3 hour bracket. | The incidence of the depression label increases by approximately 13% when moving from the 1-2 hour pre-sleep screen time group to the 2-3 hour group. The average label shifts from 0.024 to 0.027. | DOC_03 | - 13% increase in incidence - 1-2h label: 0.024 - 2-3h label: 0.027 | abstractive_grounded | The 13% figure is the primary metric for comparison. |
| Q09 | comparison | medium | How do the academic performance and stress levels of the most active teens compare to the least active group? | The most active teens (1.5-2.0h physical activity) have a higher average GPA (3.06) and lower stress (5.44) than the least active group (0.0-0.5h), who average a 2.91 GPA and 5.49 stress level. | DOC_04 | - Most active: 3.06 GPA / 5.44 stress - Least active: 2.91 GPA / 5.49 stress - Most active has higher GPA/lower stress | abstractive_grounded | Must link activity level to both GPA and stress trends. |
| Q10 | comparison | medium | Based on social interaction levels, which group reports the highest anxiety, and how does it compare to the "low" interaction group? | The "high" social interaction group reports the highest average anxiety at 5.70/10. This is significantly higher than the "low" interaction group, which reports the dataset's lowest anxiety average of 5.52/10. | DOC_05 | - High interaction anxiety is 5.70 - Low interaction anxiety is 5.52 - High interaction is the highest anxiety group | abstractive_grounded | Must identify "High" as the most anxious interaction level. |
| Q11 | multi_hop | hard | How does the average sleep of a "High-Risk" teen compare to the specific sleep threshold identified as a major depression risk factor? | The "High-Risk" profile averages 4.76 hours of sleep, which falls below the 5-hour threshold where the probability of reporting a depression label increases significantly. This sleep deficit is a defining characteristic of the high-risk demographic compared to the low-risk mean of 6.59 hours. | DOC_02, DOC_06 | - High-risk sleep avg is 4.76h - Risk threshold identified as < 5h - High-risk is below the identified risk threshold | abstractive_grounded | Requires combining the profile stat (4.76) from DOC_06 with the threshold (5h) from DOC_02. |
| Q12 | multi_hop | hard | Analyze how pre-sleep digital habits and total daily social media volume interact within the "High-Risk" teen profile. | High-risk teens spend 6.72 hours daily on social media, nearly 50% more than low-risk peers. Evidence suggests pre-sleep screen time is a primary driver of this total volume, with high-risk individuals also reporting significant sleep deficits linked to late-night usage. | DOC_03, DOC_06 | - High-risk daily volume: 6.72h - Pre-sleep usage drives overall daily volume - Late-night usage correlates with high addiction/low sleep | abstractive_grounded | Requires linking High-Risk volume (DOC_06) with the behavioral driver (DOC_03). |
| Q13 | multi_hop | hard | Discuss the shared anxiety outcomes between high-volume platform users and high-volume social interactors. | Both TikTok-exclusive users (high-volume platform) and "high" social interaction levels are associated with peak anxiety scores (5.75 and 5.70 respectively). This suggests that high engagement, whether through a specific algorithmic feed or general social volume, correlates with elevated adolescent anxiety. | DOC_01, DOC_05 | - TikTok anxiety peak: 5.75 - High interaction anxiety peak: 5.70 - High volume/engagement across both metrics links to peak anxiety | abstractive_grounded | Must synthesize the peak anxiety values from both platform and interaction documents. |
| Q14 | limitation | medium | Does the dataset establish a causal link between sleeping less than five hours and clinical depression? | No, the dataset identifies a strong inverse correlation (-0.19) but explicitly notes that correlation does not prove causation. It remains unclear if sleep loss causes depression or if depression causes sleep disturbances like insomnia. | DOC_02, DOC_06 | - Correlation coefficient is -0.19 - Correlation vs. causation limitation - Unclear direction of causality | abstractive_grounded | Answer must highlight that causality is not proven. |
| Q15 | limitation | medium | What specific qualitative information is missing regarding "social interaction" that limits the dataset's interpretation of stress? | The dataset uses self-defined qualitative metrics for social interaction but does not distinguish between online and face-to-face interactions. Additionally, it lacks controls for individual personality types, such as introversion vs. extroversion, which could influence how interaction volume impacts stress. | DOC_05 | - No distinction between online vs face-to-face - No control for personality types - Self-defined/subjective metrics | abstractive_grounded | Must list at least two specific missing factors noted in the "Limitations" sections. |

### Section A: Ground-truth checklist

* **Q01:**
    * KF1: Identifies TikTok as the platform with the highest anxiety.
    * KF2: Cites the anxiety score as 5.75/10.
    * KF3: Mentions it is higher than Instagram (5.67) or "Both" (5.49).
* **Q02:**
    * KF1: States the correlation coefficient is -0.19.
    * KF2: Notes the relationship is negative (inverse).
    * KF3: Identifies it as the strongest correlation among behavioral variables.
* **Q03:**
    * KF1: Identifies the 2.5-3.0 hour pre-sleep screen time bracket.
    * KF2: Cites the average addiction level as 5.78.
* **Q04:**
    * KF1: States the High-Risk physical activity average is 0.95 hours.
    * KF2: Compares it to the dataset mean of 1.01 hours.
* **Q05:**
    * KF1: Cites low interaction anxiety as 5.52.
    * KF2: Cites low interaction stress as 5.35.
    * KF3: Identifies these as the lowest in their respective categories.
* **Q06:**
    * KF1: Cites TikTok-only stress as 5.29.
    * KF2: Cites "Both" platform stress as 5.55.
    * KF3: Concludes "Both" is higher stress than TikTok-only.
* **Q07:**
    * KF1: High-risk social media: 6.72h; High-risk sleep: 4.76h.
    * KF2: Low-risk social media: 4.55h; Low-risk sleep: 6.59h.
* **Q08:**
    * KF1: Identifies a 13% increase in depression label incidence.
    * KF2: Notes the shift from 0.024 (1-2h) to 0.027 (2-3h).
* **Q09:**
    * KF1: Most active (1.5-2.0h) avg GPA: 3.06; Stress: 5.44.
    * KF2: Least active (0.0-0.5h) avg GPA: 2.91; Stress: 5.49.
* **Q10:**
    * KF1: Identifies "High" social interaction as the highest anxiety group (5.70).
    * KF2: Identifies "Low" social interaction as the lowest anxiety group (5.52).
* **Q11:**
    * KF1: Cites High-Risk sleep average of 4.76 hours.
    * KF2: Identifies the critical risk threshold as below 5 hours.
    * KF3: Synthesizes that high-risk teens fall into this danger zone.
* **Q12:**
    * KF1: Cites High-Risk daily volume of 6.72 hours.
    * KF2: Explains that pre-sleep screen time is a primary driver of overall volume.
* **Q13:**
    * KF1: Links TikTok anxiety peak (5.75) with High Interaction anxiety peak (5.70).
    * KF2: Suggests high engagement/volume is the common denominator for anxiety.
* **Q14:**
    * KF1: Mentions the correlation of -0.19.
    * KF2: Explicitly states that correlation does not equal causation.
    * KF3: Notes the uncertainty of directionality (e.g., insomnia vs depression).
* **Q15:**
    * KF1: Mentions the lack of distinction between online and face-to-face interaction.
    * KF2: Mentions the lack of controls for personality types (introversion/extroversion).
