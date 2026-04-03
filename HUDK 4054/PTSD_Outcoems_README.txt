This PTSD_Outcomes.readme file was generated on 2022-03-20 by Simon Chen


GENERAL INFORMATION

1. Title of Dataset: PTSD Outcomes Within Each Treatment Arm

2. Author Information
	A. Principal Investigator Contact Information
		Name: National Center for PTSD
		Institution: National Center for PTSD
		Address: 1234 VA Cutoff Rd, White River Junction, VT 05009
		Email: ncptsd@va.gov

3. Date of data collection (single date, range, approximate date): 2021-08-12 

4. Geographic location of data collection: the United States

5. Information about funding sources that supported the collection of the data: National Center for PTSD


SHARING/ACCESS INFORMATION

1. Licenses/restrictions placed on the data:  No license information was provided. If this work was prepared by an officer or employee of the United States government as part of that person's official duties it is considered a U.S. Government Work.

2. Links to publications that cite or use the data: https://www.data.va.gov/d/tkqa-ivyb

3. Links to other publicly accessible locations of the data: https://catalog.data.gov/dataset/ptsd-outcomes-within-each-treatment-arm


4. Was data derived from another source? no 
	A. If yes, list source(s): 

5. Recommended citation for this dataset: 
National Center for PTSD. (2021). PTSD Outcomes Within Each Treatment Arm [Data set].
	https://catalog.data.gov/dataset/ptsd-outcomes-within-each-treatment-arm

DATA & FILE OVERVIEW

1. File List: 
	1. Comma Separated Values File - dataset in txt/csv format.
	2. RDF File - dataset in RDF format
	3. JSON File - dataset in JSON format
	4. XML File - dataset in XML format

2. Relationship between files, if important: same dataset in different format

3. Additional related data collected that was not included in the current data package: N/A

4. Are there multiple versions of the dataset? no but update once a year.


METHODOLOGICAL INFORMATION

1. Description of methods used for collection/generation of data: 
Record input.


2. Methods for processing the data: 
The PTSD Outcomes Within Each Treatment Arm dataset includes information on how PTSD was measured and at which timepoint. Descriptive information is provided on which measure was used, the statistical approach to measuring change in PTSD, how PTSD was defined and the definitions of loss of diagnosis and clinically meaningful change, if these variables were included in the study.

3. Instrument- or software-specific information needed to interpret the data: 
Any software could access .csv file.

4. Standards and calibration information, if appropriate: N/A

5. Environmental/experimental conditions: N/A

6. Describe any quality-assurance procedures performed on the data:  Yes

7. People involved with sample collection, processing, analysis and/or submission: Yes


DATA-SPECIFIC INFORMATION FOR: [FILENAME]
<repeat this section for each dataset, folder or file, as appropriate>

1. Number of variables: 77

2. Number of cases/rows: 3741

3. Variable List: 

	1. study_id: an identifier for each row constructed from Author, Year, Intervention Arm, a number indicating an assessment point, and the analysis type. Text 
	2. Study Class: Describes top-level classification of the study as: Psychotherapy, Pharmacotherapy, CIH, Nonpharm biologic, Nonpharm cognitive, Collaborative Care, Psychotherapy & Pharmacotherapy, Psychotherapy & CIH, Other Mixed. Text.
	3. Treatment Focus (Study level):Primary treatment focus of the study. One of: PTSD or PTSD+SUD. SUD is Substance Use Disorder. Text.
	4. Total N Randomized: Total participants randomized in the study (total of all arms). Number
	5. Intervention Group: Label for each intervention group or arm in the study. One of A, B, C, or D. A study may have only two arms (A, B). Text.
	6. Treatment Focus (Arm level): Describes the treatment focus of the individual treatment arm referenced in the Intervention Group column. Text
	7. Treatment Focus Subclass (Arm level): For treatment arms with a Treatment Focus of PTSD+SUD, indicates if treatments are Integrated or Not integrated. Integrated treatments for PTSD-SUD include interventions that integrate interventions for PTSD and SUD within one protocol delivered by one provider or are interventions for PTSD and SUD that are delivered simultaneously (within one therapy session) by one provider, to be distinguished from, for example, one treatment intended to address both conditions (e.g., pharmacotherapy), two treatments delivered simultaneously without clear integration or alignment by different providers (e.g., Relapse Prevention and TF-CBT with different therapists), or phased treatment (e.g., Relapse Prevention then TF-CBT). Text
	8. N Completed Outcome Measurement: Number of participants that completed assessment. Number
	9. N Completed Outcome Measurement Detail: Qualitative elements included in number of participants that completed assessment. Text
	10. Publication Treatment Name: Name of intervention as stated by study. Text
	11. NCPTSD Treatment Name	:NCPTSD-provided Treatment Name. Text
	12. Psychotherapy: Categorization of the arm/intervention: Yes, No, or null for Psychotherapy.Text
	13. Psychotherapy Subclass: Categorization of the arm/intervention: coded as Trauma-focused or Non-Trauma-focused. Text
	14. Pharmacotherapy: Categorization of the arm/intervention: Yes, No, or null for Psychotherapy. Text
	15. Pharmacotherapy Subclass: Categorization of the arm/intervention: options are Antidepressant: SSRI; Antidepressant: SNRI; Antidepressant: TCA; Antidepressant: MAOI; Antiadrenergic; Anitanxiety: Benzo; Antianxiety: nonbenzo; Phytocannabinoid; Synthetic cannabinoid; mood stabilizer; psychostimulants; steroids; other. Text
	16. CIH: Categorization of the arm/intervention: Complementary and Integrative Health. Text
	17. CIH Subclass: Type of Complementary and Integrative Health intervention: Acupuncture, Biofeedback, Clinical hypnosis, Massage therapy, Meditation, Guided imagery, Tai chi/qi gong, Yoga, Animal-assisted, Exercise and recreational therapies, Relaxation, Natural products, Creative therapy, Progressive muscle relaxation, Spirituality, Other. Text
	18. Nonpharm Biologic: Categorization of the arm/intervention: Nonpharm Biologic. Text
	19. Nonpharm Cognitive Therapy: Categorization of the arm/intervention: Nonpharm Cognitive Therapy.Text
	20. Control: Categorization of the arm/intervention: Is the arm a Control group?. Text
	21. Other: Categorization of the arm/intervention: Treatments that don’t better fit into another category, like digital interventions not delivered by a licensed provider (e.g., internet-based CBT, PTSD Coach). Text
	22. Collaborative Care: Categorization of the arm/intervention: Collaborative Care. Text
	23. Format: Categorization of the arm/intervention: coded as group, individual, couples, or mixed. Text
	24. Delivery Method: Categorization of the arm/intervention: coded as in person, phone, video, technology alone, technology assisted, written, or mixed. Text
	25. Arm N Randomized: Number of participants randomized to intervention arm. Number
	26. Outcome Assessment Type: One of: Clinical diagnosis, Self report, Structured Clinical Interview, or NR. Text
	27. PTSD Outcome Measure: Simplified and standardized abstraction of PTSD Outcome measure. Text. 
	28. PTSD Outcome Measure Detail: PTSD outcome (listed here in order of priority): CAPS: total (sometimes called severity), Structured Clinical Interview for DSM (SCID), PTSD Symptom Scale – Interview (PSS-I), Standardized Assault Interview (SAI, sometimes called STI), Structured Interview for PTSD (SI-PTSD), Mini-International Neuropsychiatric Interview (MINI), Other structured clinical interview, PTSD Checklist (PCL), PTSD Symptom Scale – Self-Report (PSS-SR), Posttraumatic Diagnostic Scale (PDS), Impact of Event Scale (IES), Other self-reported measure of PTSD.Text
	29. Analysis Type: ITT and/or completer; other approaches if indicated.Text
	30. Method for Handling Missing Data: Name of method or statistical modeling approach for PTSD measure data (e.g. LOCF, imputation, mixed effects models). If multiple types of analyses conducted, method listed for each (e.g. methods for ITT and Completer samples) in the row corresponding to that analysis type. Text
	31. Statistical Analysis Method: Description of statistical method(s) used to analyze primary PTSD measure, PTSD diagnostic change, and clinically meaningful response. Text
	32. Assessment Point Category. Text
	33. Follow-up Assessment in Weeks: Point in time of assessment.Text
	34. Measure Score Detail: Detail for reported value(s) of Measure Score Mean and Standard Deviation. Text
	35. Measure Score Mean:Mean measure score for PTSD outcome.Text
	36. Measure Score Standard Deviation: Standard deviation of measure score for PTSD outcome. Number
	37. Measure Score Type of Variance Measure	: Describes the type of the measure of variance reported, typically one of 95% CI, 90% CI, SEM, IQR, Range. Text
	38. Measure Score Variance Value or Lower Bound： Measure of variance value as described in Type of Variance Measure column or lower bound of the variance measure for measure score for the given PTSD outcome. Number
	39. Measure Score Variance Upper Bound: Upper bound of the variance measure described in Type of Variance Measure, if applicable, for measure score for the given PTSD outcome. Number
	40. Score Difference from Baseline Detail: Details for Score Difference, including additional text or non-standard values. Plain Text
	41. Score Difference from Baseline: Calculated as score at time of assessment minus baseline score. Number
	42. Score Difference from Baseline Standard Deviation: Standard deviation of score difference from baseline. Plain Text
	43. Score Difference from Baseline 95% CI Lower Bound. Number
	44. Score Difference from Baseline 95% CI Upper Bound. Number
	45. Effect Size 1 Detail: Details associated with Effect Size 1. Plain Text
	46. Effect Size 1 Type: Type of effect size, e.g. Cohen's d, Hedges' g, etc. Plain Text
	47. Effect Size 1 Value: Effect size value, as a number. Number
	48. Effect Size 1 Type of Variance Measure	: Describes the type of the measure of variance reported, typically one of 95% CI, 90% CI, SEM, IQR, Range. Plain Text
	49. Effect Size 1 Variance Value or Lower Bound: Measure of variance value or lower bound of the variance measure described in Type of Variance Measure column. Number
	50. Effect Size 1 Variance Upper Bound: Upper bound of the variance measure described in Type of Variance Measure, if applicable. Number
	51. Effect Size 1 p value	: p value reported with Effect Size 1. Plain Text
	52. Effect Size 2 Detail: Details associated with Effect Size 2. Plain Text
	53. Effect Size 2 Type: Type of effect size, e.g. Cohen's d, Hedges' g, etc. Plain Text
	54. Effect Size 2 Value: Effect size value, as a number. Number
	55. Effect Size 2 Type of Variance Measure	: Describes the type of the measure of variance reported, typically one of 95% CI, 90% CI, SEM, IQR, Range. Plain Text
	56. Effect Size 2 Variance Value or Lower Bound: Measure of variance value or lower bound of the variance measure described in Type of Variance Measure column. Number
	57. Effect Size 2 Variance Upper Bound: Upper bound of the variance measure described in Type of Variance Measure, if applicable. Number
	58. Effect Size 2 p value	: p value reported with Effect Size 2. Plain Text
	59. Diagnostic Change Definition 1: First definition for loss of PTSD diagnosis, as stated by study. Instrument name and threshold, if applicable. If study did not define PTSD diagnostic change but reported % of participants achieving PTSD diagnostic change, no definition was abstracted but % of participants was abstracted. Plain Text
	60. Percent Achieved Diagnostic Change Definition 1: Percent of participants with loss of PTSD diagnosis, as previously defined by first definition. Number
	61. Additional Defs of Diagnostic Change: Indicates if additional definitions of diagnostic change are reported in the study but not abstracted here. Plain Text
	62. Clinically Meaningful Response Definition 1: First definition for clinically meaningful response, as stated by study. Instrument name(s) and threshold(s), if applicable. Clinically meaningful response indicators include response, remission, clinically meaningful change, etc; global change index and reliable change index are included. Plain Text
	63. Percent Achieved Clinically Meaningful Response Definition 1: Percent of participants with clinically meaningful response, as previously defined by first definition: Number
	64: Additional Defs of Clinically Meaningful Response: Indicates if additional definitions of clinically meaningful response are reported in the study but not abstracted here. Plain Text
	65. Military Status (Study level): At the study level, a category describing the composition of active duty military, veterans, and community members participating in the study. One of Military, Veteran, Community, Mixed, or no value. Plain Text
	66. Active Duty Military Percent (Study level): At the study level, percent of participants actively serving in the armed forces (U.S. or foreign). Abstracted as "NR" (null cell value) if study did not specify proportion of participants as military or non-military. Number
	67. Veteran Percent (Study level): At the study level, percent of participants who are veterans of armed forces (U.S. or foreign). Abstracted as "NR" (null cell value) if study did not specify proportion of participants as military or non-military. Number
	68. Community Percent (Study level): At the study level, percent of participants who are not active duty military or veterans. Assumed 100% if study did not specify proportion of participants as military or non-military. Civilian fighters were classified as community/non-military. Number
	69. Female Percent (Study level): At the study level, percent female. Number
	70, Female Percent Detail (Study level): At the study level, qualitative values reported in "Female, percent". Includes sexual orientation if reported. Plain Text
	71. Male Percent (Study level): At the study level, percent male. Number
	72. Trauma Type (Study level): At the study level: Military Sexual Trauma (MST); Combat-related; Child physical abuse; Child sexual abuse; Child other abuse; Rape/sexual assault; Intimate partner violence; Accidents; Illness/medical procedure; Community/school violence; Natural or manmade disasters; Terrorism/political violence/forced displacement; Other; Mixed (If Mixed, list included types; if Other, list short description). Active duty member reporting sexual assault outside of military was categorized as "rape/sexual assault." "Child other abuse" included neglect and psychological maltreatment. "Intimate partner violence" included domestic violence. "Accidents" included motor vehicle accidents, transportation-related accidents, and accidents due to construction. "Community/school violence" included bullying, physical abuse/assault, gang-related violence, interracial violence, police and citizen altercations, mass shootings, homicide, etc. "Natural or manmade disasters" included tornadoes, hurricanes, wildfires, earthquake, drought, chemical spills, etc. Plain Text
	73. Trauma Detail (Study level): At the study level, expands on trauma types for studies with the value "Mixed" under Trauma Type. Plain Text
	74. Risk of Bias Rating (Study level): At the study level, Risk of Bias rating. See Risk of Bias dataset for more detail on Risk of Bias assessment. Plain Text
	75. Citation: AHRQ-style citation. Plain Text
	76. PTSDPubs ID: PTSDpubs Identifier. Plain Text
	77. Year Added to PTSD-Repository: Year that the study was added to the PTSD-Repository. Year listed, as text, corresponds to a publication year of an AHRQ Technical Brief for the PTSD-Repository. Plain Text


4. Missing data codes: Values abstracted as not applicable ("NA") or not reported ("NR") by the study are null values (empty cells).
	

5. Specialized formats or other abbreviations used: 
	1. Psychotherapy Subclass: Categorization of the arm/intervention: coded as Trauma-focused or Non-Trauma-focused
	2. Treatment Focus (Study level): Primary treatment focus of the study. One of: PTSD or PTSD+SUD. SUD is Substance Use Disorder.
	3. PTSD Outcome Measure Detail: PTSD outcome (listed here in order of priority): CAPS: total (sometimes called severity), Structured Clinical Interview for DSM (SCID), PTSD Symptom Scale – Interview (PSS-I), Standardized Assault Interview (SAI, sometimes called STI), Structured Interview for PTSD (SI-PTSD), Mini-International Neuropsychiatric Interview (MINI), Other structured clinical interview, PTSD Checklist (PCL), PTSD Symptom Scale – Self-Report (PSS-SR), Posttraumatic Diagnostic Scale (PDS), Impact of Event Scale (IES), Other self-reported measure of PTSD
