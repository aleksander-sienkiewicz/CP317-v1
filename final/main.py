from PDFCreator import createPowerPoint
from TextExtractor import articleDissasembler
from pathlib import Path
import os
import time


# Usage example
def article_to_ppt(input_file, output_file):
  path = Path(input_file)
  if (not path.is_file()):
    print("File Does not Exist")
  else:
    a = articleDissasembler(input_file)
    a.extractTextAndImages()
    a.extractTables()
        
    b = a.summarize_pdf(a.text)

    # d = ['ARTHUR J. MAYORGA, ASHUTOSH DALVI, MICHELLE E. PAGE, SARAH ZIMOV-LEVINSON, RENE  HEN, and IRWIN LUCKI Departments of psychi', 'ine (5-HT)1A and 5-HT1B receptor mutant mice decreased baseline immobility . fluoxetine (10.0–20.0 mg/kg i.p.) and desipra- mine (5.0– 20.0 mg /kg) .', 'administration of selective 5-HT receptor antagonists in wild-type mice partially reproduced the phenotypes of the mutant mice . 5-HT1A receptors have different roles in the modulation of the response to antidepressant drugs in the TST .', '5-HT receptor ago- nists produce behavioral re- sponses characteristic of conventional antidepressants using selective agonists . selective 5-HT1A receptor agons produce responses in rodent behaviors, such as the forced swimming test (FST) and', 'the recent development of 5-HT receptor knockout mice has allowed the study of behavioral effects and drug re- sponses in animals that have genetic deletion of targeted . this research was supported by U.S. Public Health Service Grant P01-MH 48125 .', 'the 5-HT1A receptor knockout mice showed behaviors consistent with an increase in anxiety . these receptor subtypes may play a role in affective disorders .', 'studies of antidepressant-like behaviors using mice with genetic deletions targeted at 5-HT1A receptors may provide complementary information . genetic techniques produce more selective and total deletion of targeted receptors than acute pharmacological tools .', 'psy-chiatric medications may be related to human homologs of the murine-disrupted gene . current studies examined the effects of antide- pressant drugs on the immobility of mice in the TST .', 'wild-type, and homozygote 5-HT1A mice were bred and housed in a colony at the university of Pennsylvania (Philadelphia, PA) . es- tablished colonies derived from the 129/Sv strain', 'subjects were randomly allocated to treatment conditions and tested in coun- terbalanced order . mice were individ- ually suspended by tail to a horizontal ring-stand bar . a 6-min test session was videotaped .', 'all drugs were dissolved in distilled water and administered via intraperitoneal route . the selective 5-HT1A receptor antagonist WAY 100635 (0.1 mg/kg; Fletcher et al., 1996) were administered immediately prior to fluoxetine .', 'brain tissue samples were taken for determination of brain monoamine levels in mice treated with either PCPA or AMPT . mice were sacrificed by decapitation 1 h after behavioral testing . whole brain was removed and separated from cerebellum .', 'the mobile phase consisted of 60 mM sodium phosphate buffer (pH 4.2) with 100 M EDTA . the flow rate through the system was 700 l/min .', 'the mobile phase con-sisted of 90 mM NaAc, 35 mm citric acid, 0.34mM EDTA, 1.2mm octyl sulfate and 9% (v/v) methanol adjusted to', 'PCPA reduced 5-HT levels by 70% in wild-type mice and 67% in 5-HT1A receptor knockout mice without signifi- cant effects on DA or NE . AMPT did not significantly affect levels of 5-HT .', 'n 7 8 8 8 5-HTa,b 1009.0 27.7 300.6 36.2* 1187.5 57.7 394.7 57,7* 5-HIAAa,c 880.3 29.9 403.6 19.2* 1109.8 103.4 37', 'n 7–9 mice/group. *p 0.05 versus same genotype saline control . the depletion of catecholamines with AMPT reversed the reduced baseline immobility of 5-HT1A receptor knockout mice .', 'test doses of SSRIs fluoxetine and paroxetine failed to reduce immobility values in 5-HT1A receptor mu- tants . the highest dose of desipramine that was effective in the 55%, p 0.05 .', 'two-way ANOVA revealed a significant genotype treat-ment interaction on immobility . 5-HT1B / mice showed an increase in sensitivity to the behavioral effects of fluoxetine .', 'pretreatment with 5-HT receptor antagonist WAY 100635 (p 0.05) blocked anti-immobility effect of 20.0 mg/kg fluox- etine . effects of desipramine, fluoxetine and paroxetine on wild-type mice', 'effects of desipramine (2.5–20.0 mg/kg) on the behavior of wild-type 5-HT1B receptor knockout mice in the tail suspension test . for both genotypes, n 9 to 22 mice for each dose .', '5-HT1A receptors have different roles in the modulation of the response to antidepressant drugs in the TST . the ab- sence of 5-HT1,5 and 5HT1B receptors was associated with a decrease in immobility under baseline conditions', '5-HT1A receptor mutants showed a decrease of baseline im-mobility values . ant mice have also been reported to show reduction of immobility in the FST .', 'the lack of a behavioral response to PCPA pretreatment is quite significant because it suggests that the TST behavior is not caused by the absence of pre- synaptic 5-HT1A receptors .', 'antidepressant-like responses of 5-HT1A receptor mu- tants could involve altered regulation of NE or DA transmission . this hypothesis was tested using the tyrosine hydroxylase inhibitor AMPT .', 'pretreatment on the effect of fluoxetine (2.5 and 20.0 mg/kg) on the behavior of wild-type mice . n 10 to 11 mice/group. *p 0.05 versus saline control with same pretreatment .', '5-HT1A receptor deletion did not alter the antidepressant behavioral response to desipramine, a selective NE reuptake inhibitor . a low 2.5-mg/kg dose of fluoxetine produced an augmented increasing response .', '5-HT1B receptor mutant mice may potentiate antidepressant-like behaviors to SSRIs because they are important in regulating extracellular 5-HT in regions, like the hippocampus, that are critical for their expression . 5-HT', 'the decreased baseline immobility in 5-HT1A receptor mutant mice was not mimicked by administration of WAY 100635 alone . the duration of treatment with the antago- nist was brief, but developmental compensation may account for the dramatic differences .', 'ited response to GR 127935 may be due to its poor selectivity, partial efficacy at 5-HT1B receptors, or the need to block receptors for longer periods of time . new compounds may be available that can discriminate the effects of 5-HT', '129 mice were among the mouse strains that failed to show antidepressant-like responses to SSRIs in the FST . a recent strain survey study found that 129 showed immobility for nearly the entire 4-min testing period .', 'the functional consequences of 5-HT receptor mutations may depend on the pharmacological selectivity of the antide- pressants because they were unnecessary for the behavioral activity of the selective NE reuptake inhibitor desipramine . future studies with genetic mu- tant mice will', 'serotonin inhibits acetylcholine release in rat frontal cortex through 5-HT1B receptors . fluoxetine anti-immobility effect in forced swimming test in mice .', 'tryptophan-depletion challenge in depressed patients treated with desipramine or fluoxetine: implications for the role of serotonin in the mechanism of antidepressant action .', 'Knobelman DA, Kung HF and Lucki I (2000) Regulation of extracellular sero- tonin by 5-hydroxytryptamine1A and 5-HT1B autoreceptors in dif- ferent brain regions .', 'tchins LJ, Gosden J and Heal DJ (1993) Mediation of the antidepressant-like effect of 8-OH-DPAT in mice by postsynaptic 5-HT1A receptors .', '5-HT1A receptor mutant mice exhibit enhanced tonic, stress-induced and fluoxetine-induced serotonergic transmission . perrault GH, Morel E, Zivkovic B and Sanger DJ .', 'h5-HT1B receptors are discriminated against in mice . the role of 5-HT1A receptors in antidepressant drug actions in the mouse forced swimming test .', 'ne-evoked dopamine levels following constitutive deletion of the serotonin(1B) receptor . a new method for screening antidepressant drugs .', 'Eur J Pharmacol 410:165–181 . altered emotional states in knockout mice lacking 5HT1A or 5-HT1B receptors .']

    c = createPowerPoint(output_file)
    c.add_slides(b, a.images, a.tables, a.endOfPage)



# ------ UNIT TESTING

# ------ TextExtractor Class

# ------ extract images and tables

# a =  ["KHALIMBOYEVA.pdf", "DesignDocument.pdf", "scholar.pdf", "scholar2.pdf", "scholar3.pdf", "scholar4.pdf", "helpforproject.pdf", "tables.pdf", "Longarticle.pdf"]

# i = "b.pdf"

# t0 = time.time()
# a = articleDissasembler(i)
# a.extractTextAndImages()
# b = a.summarize_pdf(a.text)

# t1 = time.time()
# total = t1-t0

# print(f"\n\n\n{i} time: {total}\n\n\n")

# for x in (range(0, len(b))):
#   print()
#   print(b[x])
# print(f"\n\n\n")








# ------ SYSTEM TESTING
# t0 = time.time()
# article_to_ppt("KHALIMBOYEVA.pdf", "KHALIMBOYEVA.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"KHALI time: {total}")


# t0 = time.time()
# article_to_ppt("DesignDocument.pdf", "DesignDocument.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"\n\n\nDesign Document time: {total}\n\n\n")

# t0 = time.time()
# article_to_ppt("scholar.pdf", "scholar.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"\n\n\nscholar time: {total}\n\n\n")

# t0 = time.time()
# article_to_ppt("scholar2.pdf", "scholar2.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"\n\n\nscholar2 time: {total}\n\n\n")

# t0 = time.time()
# article_to_ppt("scholar3.pdf", "scholar3.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"\n\n\nscholar3 time: {total}\n\n\n")

# t0 = time.time()
# article_to_ppt("helpforproject.pdf", "helpforproject.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"\n\n\nhelpforproject time: {total}\n\n\n")


# t0 = time.time()
# article_to_ppt("Longarticle.pdf", "Longarticle.pptx")
# t1 = time.time()
# total = t1-t0
# print(f"\n\n\ntables time: {total}\n\n\n")



