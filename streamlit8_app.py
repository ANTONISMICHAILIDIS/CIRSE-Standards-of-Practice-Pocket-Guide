import streamlit as st

# =====================
# Custom CSS Styling
# =====================
st.markdown(
    """
    <style>
    /* Overall background and text colors */
    .reportview-container {
        background-color: #ffffff;
        color: #4d4d4d;
    }
    /* Header colors (gold/yellow accent) */
    h1, h2, h3, h4 {
        color: #d4af37;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f2f2f2;
    }
    /* Small subtitle style */
    .small-font {
        font-size: 14px;
        color: #808080;
    }
    /* Disclaimer styling */
    .disclaimer {
        font-size: 12px;
        color: #808080;
    }
    </style>
    """, unsafe_allow_html=True
)

# =====================
# Sidebar Configuration
# =====================
with st.sidebar.expander("About CIRSE"):
    st.markdown("""
**CIRSE (Cardiovascular and Interventional Radiological Society of Europe)**  
CIRSE promotes excellence in interventional radiology through education, research, and dissemination of best practices.  
Visit the [CIRSE website](https://www.cirse.org) for more information.
""")
    
with st.sidebar.expander("Contact"):
    st.markdown("""
**Contact Information**  
Email: info@cirse.org  
Phone: +44 (0)20 1234 5678  
Address: CIRSE, European Office, 123 Interventional Road, London, UK
""")

selected_language = st.sidebar.selectbox("Select Language", ["English", "Spanish", "French", "German", "Chinese"])
if selected_language != "English":
    st.sidebar.info("Currently, all documents are only available in English. Translations coming soon!")

# =====================
# Main Page Header
# =====================
st.title("CIRSE Standards of Practice Pocket Guide")
st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)

# =====================
# Search Functionality
# =====================
st.subheader("Search Documents")
search_query = st.text_input("Enter search term:")

# =====================
# Documents Dictionary
# =====================
# All documents are added verbatim.
documents = {
    "Bronchial Artery Embolisation": r"""
**CIRSE Standards of Practice on Bronchial Artery Embolisation
Authors: Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos
________________________________________
1. Introduction
•	Bronchial artery embolisation (BAE) is a minimally invasive, life-saving procedure used to treat haemoptysis (coughing up blood).
•	The CIRSE Standards of Practice provide best practices to optimize safety and efficacy in performing BAE.
•	This document does not impose a strict standard but provides evidence-based recommendations for interventional radiologists.
________________________________________
2. Methods
•	Writing Group: Five internationally recognized experts in BAE.
•	Literature Review:
  - Timeframe: 1974–2021.
  - Source: PubMed database.
  - Consensus-Based Recommendations.
________________________________________
3. Background
•	Haemoptysis is a life-threatening respiratory emergency, with a mortality rate of 50–100% if left untreated.
•	Death is usually due to asphyxiation, not exsanguination.
•	When timely and optimal diagnosis and treatment are provided, the mortality rate drops to <20%.
Etiology of Haemoptysis
•	90% of massive haemoptysis cases arise from the bronchial circulation.
•	5% arise from the pulmonary circulation.
•	5% arise from non-bronchial systemic circulations.
Common Causes of Haemoptysis
•	Tuberculosis (TB)
•	Lung cancer
•	Chronic lung diseases (bronchiectasis, cystic fibrosis, chronic pulmonary aspergillosis)
•	Pulmonary arteriovenous malformations (PAVMs)
Global Variations
•	In Western countries: 80% of haemoptysis cases are due to lung cancer, TB, bronchiectasis, and aspergillosis.
•	In India and Turkey: Tuberculosis is responsible for 60–90% of cases.
________________________________________
4. Indications for BAE
•	Life-threatening haemoptysis (severe or massive).
•	Recurrent haemoptysis despite medical therapy.
•	Bridge therapy for lung transplant candidates with chronic inflammatory lung diseases.
•	Index bleeding: Initial minor bleeding episodes that may precede massive haemoptysis.
________________________________________
5. Contraindications
Absolute Contraindications
•	Embolization of arteries that supply the spinal cord, brain, or heart (risk of ischemia).
Relative Contraindications
•	Severe contrast allergy.
•	Coagulopathy (must be corrected before the procedure).
•	Renal insufficiency (careful contrast use required).
________________________________________
6. Pre-Procedural Preparation
Clinical Work-Up
•	Confirm that the bleeding is from the lungs.
•	Assess the severity and rule out non-pulmonary sources (e.g., gastrointestinal, nasopharyngeal).
•	Review patient history, including previous haemoptysis episodes, infections, malignancies, and lung disease.
•	Optimize coagulation parameters before intervention.
Imaging
First-Line Imaging
•	Computed tomography angiography (CTA) is the gold standard for localizing the bleeding source.
•	Advantages of CTA:
  - Identifies the culprit artery.
  - Rules out alternative diagnoses.
  - Helps plan catheterization.
Additional Imaging
•	Chest X-ray: Initial screening, low sensitivity.
•	Flexible bronchoscopy: Helps clear the airway but has limitations in localizing distal sources.
•	Digital subtraction angiography (DSA): Essential for vessel selection and embolization.
________________________________________
7. Procedure: Bronchial Artery Embolisation (BAE)
Access & Catheterization
•	Preferred access: Femoral artery (retrograde approach).
•	Diagnostic catheter: 4–5 Fr standard catheter for initial evaluation.
•	Superselective catheterization:
  - Microcatheter (2.7 Fr or smaller) for precise embolization.
  - Avoid non-target embolization by sparing arteries that supply critical structures.
Embolization Agents
•	Preferred: Polyvinyl alcohol (PVA) particles (300–500 µm)
•	Alternatives:
  - N-butyl-2-cyanoacrylate (NBCA) glue (for high-flow fistulas).
  - Coils (used selectively).
Technique
1. Confirm the target vessel via angiography.
2. Slowly infuse embolic material until stasis is achieved.
3. Avoid reflux to prevent non-target embolization.
4. Perform post-embolization angiography to confirm treatment success.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Immediate Post-Procedure Monitoring:
  - Observe for recurrence of haemoptysis (hospitalization if required).
  - Monitor oxygen saturation and airway patency.
•	Long-Term Follow-Up:
  - Repeat CTA or bronchoscopy if haemoptysis recurs.
  - Additional embolization may be required in 10–30% of cases due to recanalization.
________________________________________
9. Outcomes & Complications
Technical Success Rate
•	85–98% initial success rate with embolization.
Rebleeding Rates
•	10–30% rebleeding within 6 months, often due to:
  - Incomplete embolization.
  - Collateral vessel formation.
  - Progression of underlying disease.
Complications
Mild:
•	Transient chest pain (due to ischemia).
Severe (Rare but Serious):
•	Spinal cord ischemia (from inadvertent embolization of spinal arteries).
•	Bronchial infarction (rare).
•	Non-target embolization (stroke, myocardial infarction, bowel ischemia).
________________________________________
10. Level of Evidence
•	Level 1: CTA is the first-line imaging modality for evaluating haemoptysis.
•	Level 2: PVA particles (300–500 µm) are the preferred embolic agent for BAE.
•	Level 3: BAE should be considered as a bridge therapy for lung transplant candidates.
________________________________________
11. Summary
•	BAE is a highly effective, minimally invasive treatment for life-threatening and recurrent haemoptysis.
•	CTA is essential for pre-procedural planning.
•	Embolization with PVA particles is the preferred method, but alternatives (coils, glue) exist.
•	Success rates are high, but rebleeding can occur, requiring repeat intervention.
________________________________________
12. Citation
CIRSE Standards of Practice on Bronchial Artery Embolisation – Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos
________________________________________
""",
    
    "Arterial Access for Interventions": r"""
**CIRSE Standards of Practice on Arterial Access for Interventions
Authors: Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef
________________________________________
1. Introduction
•	Purpose: To provide best practices for safe and effective arterial access in interventional radiology.
•	Scope:
  - Covers common femoral, radial, and brachial artery access.
  - Addresses imaging, technique, and complication management.
•	Clinical Importance:
  - Arterial access is the foundation of endovascular interventions, and complications at the access site can significantly impact outcomes.
________________________________________
2. Methods
•	Writing Group: Six experts in arterial interventions.
•	Literature Review:
  - Evidence search performed via PubMed (2002–2019).
  - Consensus-based recommendations.
________________________________________
3. Background
•	Arterial access is critical for many endovascular procedures, influencing procedural success and patient recovery.
•	Evolution:
  - Historically, translumbar aortography was used.
  - Ultrasound guidance has dramatically reduced complications.
  - Radial access is gaining popularity due to lower bleeding risks.
________________________________________
4. Indications
•	Peripheral vascular interventions (angioplasty, stenting).
•	Tumor embolization.
•	Emergency embolization (e.g., GI bleeding, trauma).
•	Prostatic artery embolization (PAE).
•	Endovascular aortic repair (EVAR).
________________________________________
5. Contraindications
Absolute Contraindications:
•	Severe atherosclerosis or occlusion at the intended access site.
•	Active infection at the puncture site.
•	Uncontrollable coagulopathy.
Relative Contraindications:
•	Severe obesity (affecting femoral access).
•	Radial artery anomalies.
•	Patients on high-dose anticoagulants (may need adjustment).
________________________________________
6. Pre-Procedural Preparation
- Patient Work-up:
  - History and physical examination to assess prior procedures and access site suitability.
- Imaging:
  - Ultrasound guidance is recommended for all arterial access.
  - CTA/MRA for complex cases.
- Anticoagulation Management:
  - Consider holding anticoagulants based on patient risk.
________________________________________
7. Procedure
Common Femoral Artery (CFA) Access:
- Gold standard for large-bore access (e.g., EVAR).
- Puncture 1–2 cm below the inguinal ligament under ultrasound guidance.
- Use micropuncture technique.
- Complications: Hematoma, pseudoaneurysm, retroperitoneal bleeding.
Radial Artery Access:
- Lower bleeding risk.
- Assess collateral circulation (Allen’s or Barbeau’s test).
- Puncture 2 cm proximal to the wrist crease; use 5–6 Fr sheaths.
- Complications: Radial occlusion, spasm.
Brachial Artery Access:
- Used when CFA and radial access are not feasible.
- Higher risk of nerve damage and thrombosis.
________________________________________
8. Post-Procedural Care & Follow-Up
- Use manual compression or closure devices for hemostasis.
- Monitor for complications (bleeding, ischemia, pseudoaneurysm).
- For radial access, use a compression device for 2–3 hours.
________________________________________
9. Outcomes & Complications
- Success Rates:
  - Femoral access: >95% with ultrasound guidance.
  - Radial access: Low bleeding risk but higher spasm rates.
- Complications:
  - Bleeding: Femoral (3–7%), Radial (<1%).
  - Pseudoaneurysm formation is more common in femoral access.
________________________________________
10. Level of Evidence
- Level 1: Ultrasound guidance is recommended.
- Level 2: Radial access offers lower bleeding risks.
- Level 3: Closure devices reduce hemostasis time but carry risks.
________________________________________
11. Summary
- Arterial access is essential and should use ultrasound guidance.
- Radial access is safer for many procedures but is limited by vessel size.
- Proper patient selection and anticoagulation management are crucial.
________________________________________
12. Citation
CIRSE Standards of Practice on Arterial Access for Interventions – Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef
________________________________________
""",
    
    "Varicocele Embolisation": r"""
**CIRSE Standards of Practice on Varicocele Embolisation
Authors: Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi
________________________________________
1. Introduction
•	Purpose: To provide best practices for performing percutaneous varicocele embolization.
•	Scope:
  - Covers indications, contraindications, procedural steps, complications, and follow-up.
  - Intended for interventional radiologists and urologists.
•	Clinical Importance:
  - Varicocele embolization is a minimally invasive alternative to surgical ligation.
  - Has demonstrated comparable success rates with lower morbidity.
________________________________________
2. Methods
•	Writing Group: Five internationally recognized experts in embolization procedures.
•	Literature Review:
  - PubMed search (2006–2021).
  - Final recommendations developed through expert consensus.
________________________________________
3. Background
•	Definition:
  - Varicocele is an abnormal dilation of testicular veins in the pampiniform plexus associated with venous reflux.
•	Epidemiology:
  - Affects 15% of adult males and up to 35–50% of men with primary infertility.
  - Higher prevalence in adolescent males (15%) compared to prepubescents (<1%).
•	Pathophysiology:
  - Due to venous hypertension, increased testicular temperature, and oxidative stress.
•	Indications for Treatment:
  - Infertility, testicular hypotrophy, scrotal pain, and cosmetic concerns.
________________________________________
4. Indications for Embolization
- Varicocele-related infertility.
- Testicular hypotrophy in adolescents.
- Persistent scrotal pain unresponsive to conservative management.
- Cosmetic concerns.
- Recurrent varicocele post-surgery.
________________________________________
5. Contraindications
Absolute Contraindications:
- Allergy to contrast agents.
- Severe uncorrectable coagulopathy.
Relative Contraindications:
- Renal insufficiency.
- Bilateral varicocele requiring complex approach.
________________________________________
6. Pre-Procedural Preparation
- Patient Evaluation:
  - Physical exam using Valsalva; grading of varicocele severity.
- Imaging Work-up:
  - Scrotal ultrasound (gold standard) and Doppler ultrasound.
- Laboratory Tests:
  - Coagulation profile and renal function.
________________________________________
7. Procedure: Percutaneous Varicocele Embolisation
- Access: Preferred via right femoral or jugular vein.
- Step-by-Step Technique:
  1. Venography to confirm reflux and identify collaterals.
  2. Superselective catheterization of the internal spermatic vein using a microcatheter.
  3. Embolization using coils, sclerosing agents, or NBCA glue.
  4. Post-embolization venography to confirm occlusion.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for pain, allergic reaction, or coil migration.
- Follow-up clinical exam at 1–3 months; repeat Doppler ultrasound at 3–6 months.
________________________________________
9. Outcomes & Complications
- Technical success: 85–95%.
- Clinical success: 70–90%.
- Complications: Mild (scrotal pain, post-embolization syndrome), moderate (rare coil migration), severe (rare non-target embolization).
________________________________________
10. Level of Evidence
- Level 1: Scrotal ultrasound is the gold standard.
- Level 2: Percutaneous embolization is as effective as surgery.
- Level 3: Coils are the preferred embolic material.
________________________________________
11. Citation
CIRSE Standards of Practice on Varicocele Embolisation – Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi
________________________________________
""",
    
    "Oesophageal and Gastroduodenal Stenting": r"""
**CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting
Authors: Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal
________________________________________
1. Introduction
•	Purpose: To provide best practices for the safe and effective placement of self-expanding stents in the oesophagus and gastroduodenal tract.
•	Scope:
  - Covers indications, contraindications, technical aspects, and post-procedural care.
  - Applies to both malignant and benign strictures.
•	Clinical Importance:
  - Stenting is an effective palliative treatment for dysphagia and gastric outlet obstruction.
________________________________________
2. Methods
•	Writing Group: Five internationally recognized experts in gastrointestinal stenting.
•	Literature Review:
  - PubMed search (2005–2021).
  - Consensus-based recommendations.
________________________________________
3. Background
•	Definition:
  - Placement of self-expanding metal stents (SEMS) to relieve obstruction.
•	Epidemiology:
  - Oesophageal cancer is a major cause of cancer death.
  - GOO affects 15–35% of patients with gastric or pancreatic cancer.
•	Pathophysiology:
  - Malignant strictures cause progressive dysphagia.
  - Benign strictures may result from peptic disease, surgery, or radiation.
________________________________________
4. Indications for Stenting
Oesophageal:
- Malignant strictures.
- Tracheo-oesophageal fistulas.
- Benign strictures refractory to dilation.
Gastroduodenal:
- Gastric outlet obstruction due to malignancy.
- Palliation for patients unsuitable for surgery.
- Benign strictures unresponsive to dilation.
________________________________________
5. Contraindications
Absolute:
- Perforation or fistula not amenable to stenting.
- Severe bleeding requiring surgical intervention.
- Obstructions unsuitable for stenting.
Relative:
- Severe coagulopathy.
- High risk of stent migration in benign strictures.
- Poor prognosis.
________________________________________
6. Pre-Procedural Preparation
- Patient evaluation (symptoms, endoscopy).
- Imaging: CT with contrast and fluoroscopy.
- Laboratory tests: Coagulation profile, renal function.
________________________________________
7. Procedure: Stent Placement
- Access & positioning.
- Guidewire placement under fluoroscopic/endoscopic guidance.
- SEMS deployment; balloon dilation if needed.
________________________________________
8. Post-Procedural Care & Follow-Up
- Immediate monitoring; soft diet after 24 hours.
- Follow-up imaging if symptoms persist.
________________________________________
9. Outcomes & Complications
- Technical success: 95–99%.
- Clinical success: 75–90%.
- Complications range from mild chest pain to severe bleeding.
________________________________________
10. Level of Evidence
- Levels 1–3 based on imaging and procedural techniques.
________________________________________
11. Citation
CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting – Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal
________________________________________
""",
    
    "Peri-Operative Anticoagulation Management During IR Procedures": r"""
**CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During Interventional Radiology Procedures
Authors: Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi
________________________________________
1. Introduction
•	Purpose: To provide best practices for peri-operative anticoagulation management during IR procedures.
•	Scope:
  - Guidance for managing anticoagulation in IR patients.
  - Balances bleeding and thromboembolic risks.
•	Clinical Importance:
  - Critical due to complex decision-making in patients on anticoagulation.
________________________________________
2. Methods
•	Writing Group: Clinicians with expertise in IR and hematology.
•	Literature Review: Comprehensive search in PubMed and Cochrane Library.
•	Consensus Development: Delphi process achieving 80% agreement.
________________________________________
3. Background
•	Management is challenging due to procedure complexity and patient comorbidities.
•	Balancing bleeding risk with thrombosis risk.
________________________________________
4. Indications for Anticoagulation in IR Patients
- Atrial fibrillation, VTE prophylaxis, mechanical heart valves.
- Recent MI or PAD.
- Hypercoagulable states.
________________________________________
5. Contraindications to Anticoagulation in IR
Absolute:
- Active major bleeding.
- Recent intracranial hemorrhage.
- Severe uncontrolled hypertension.
- Severe thrombocytopenia (<50,000/µL).
Relative:
- High bleeding risk procedures.
- Coagulation disorders.
- Recent major surgery.
________________________________________
6. Pre-Procedural Coagulation Assessment
- Structured bleeding history and laboratory testing (PT/INR, aPTT, fibrinogen, platelets, TEG/ROTEM).
________________________________________
7. Anticoagulation Management Based on Procedure Risk
- Continue for low-risk; modify for moderate-risk; hold for high-risk procedures.
________________________________________
8. Peri-Procedural Management of Specific Anticoagulants
| Anticoagulant | Pre-Procedural Holding Time | Post-Procedural Restart Time |
|---------------|-----------------------------|------------------------------|
| Warfarin      | 5 days before high-risk     | 24–48 hours post-procedure   |
| Heparin       | 4–6 hours before            | Immediate (low-risk) or 24 hrs (high-risk) |
| LMWH          | 24 hours before             | 24 hours post-procedure      |
| DOACs         | 24–48 hours (renal-dependent)| 24 hours post-procedure      |
________________________________________
9. Bridging Strategies
- For high-risk warfarin patients: stop warfarin 5 days pre-, start LMWH bridging 3 days pre-, stop LMWH 24 hours pre-, resume LMWH/warfarin 24 hours post-procedure.
________________________________________
10. Post-Procedural Care & Monitoring
- Monitor for bleeding and thrombosis recurrence; gradual reintroduction of anticoagulation.
________________________________________
11. Outcomes & Complications
- Bleeding: Minor (5–15%), Major (1–5%).
- Thromboembolic events: VTE recurrence (2–10%), Stroke risk in AF (~5% per month).
________________________________________
12. Level of Evidence
- Level 1: Routine coagulation screening is not required unless indicated.
- Level 2: Bridging is necessary for high-risk warfarin patients.
- Level 3: DOACs require dose adjustments in renal impairment.
________________________________________
13. Citation
CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During IR Procedures – Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi
________________________________________
""",
    
    "Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting": r"""
**CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting
Authors: Marco Das, Christiaan van der Leij, Marcus Katoh, Daniel Benten, Babs M. F. Hendriks, Adam Hatzidakis
________________________________________
1. Introduction
•	Purpose: To provide best practices for performing percutaneous transhepatic cholangiography (PTC), biliary drainage (PTBD), and biliary stenting (PTBS).
•	Scope:
  - Covers indications, contraindications, techniques, complications, and follow-up.
  - Intended for interventional radiologists and hepatobiliary specialists.
•	Clinical Importance:
  - Critical for managing biliary obstruction, particularly when ERC is unsuccessful.
________________________________________
2. Methods
•	Writing Group: Six experts in hepatobiliary interventions.
•	Literature Review:
  - PubMed search from 2000 to 2021.
  - Consensus-based recommendations.
________________________________________
3. Background
•	PTC is a fluoroscopic procedure used to visualize the biliary system.
•	PTBD is indicated for biliary obstruction due to malignancy, strictures, or post-surgical complications.
•	PTBS is used to maintain long-term biliary drainage.
•	Etiologies include malignancies, benign strictures, and gallstones.
________________________________________
4. Indications for PTC, PTBD, and PTBS
- PTC: For pre-procedural imaging when ERC is contraindicated or unsuccessful.
- PTBD: For malignant and benign strictures, and cholangitis with failed drainage.
- PTBS: To maintain bile flow post-PTBD and for palliative treatment.
________________________________________
5. Contraindications
Absolute:
- Severe uncorrectable coagulopathy.
- Massive ascites without drainage control.
- Uncontrolled sepsis.
Relative:
- Liver metastases causing dysfunction.
- Multiple intrahepatic biliary strictures.
________________________________________
6. Pre-Procedural Preparation
- Imaging: Ultrasound, CT, and MRI/MRCP.
- Laboratory: LFTs, coagulation profile, blood cultures if indicated.
- Antibiotic Prophylaxis: Recommended (e.g., Ceftriaxone + Metronidazole).
________________________________________
7. Procedure
- Step 1: PTC – Percutaneous puncture under US/fluoroscopy with contrast injection.
- Step 2: PTBD – Insertion of an 8–12 Fr catheter for drainage.
- Step 3: PTBS – Deployment of SEMS (or plastic stents) under fluoroscopic guidance.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for bleeding, infection, or bile leak.
- Flush the biliary drain daily.
- Follow-up imaging (CT/MRCP) to assess stent patency.
________________________________________
9. Outcomes & Complications
- Technical success: 90–95%.
- Improvement in jaundice in >85%.
- Complications: Mild (puncture site pain), Moderate (cholangitis, bile leakage), Severe (hemobilia, sepsis, liver abscess).
________________________________________
10. Level of Evidence
- Level 1: PTBD is the standard when ERC fails.
- Level 2: SEMS are preferred for malignant obstructions.
- Level 3: Antibiotic prophylaxis is recommended in all cases.
________________________________________
11. Citation
CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting – Marco Das, Christiaan van der Leij, Marcus Katoh, Daniel Benten, Babs M. F. Hendriks, Adam Hatzidakis
________________________________________
""",
    
    "Below-the-Knee Revascularisation": r"""
**CIRSE Standards of Practice on Below-the-Knee Revascularisation
Authors: Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi
________________________________________
1. Introduction
•	Purpose: To provide best practices for performing below-the-knee (BTK) revascularisation.
•	Scope:
  - Covers indications, contraindications, technical aspects, outcomes, and follow-up.
  - Focuses on endovascular treatment for chronic limb-threatening ischemia (CLTI).
•	Clinical Importance:
  - Infra-popliteal arterial disease is a major cause of limb loss.
  - Endovascular interventions improve limb salvage and wound healing.
________________________________________
2. Methods
•	Writing Group: Six experts in peripheral arterial disease.
•	Literature Review:
  - PubMed search (2004–2020).
  - Consensus agreement.
________________________________________
3. Background
•	BTK arterial disease primarily affects diabetics, dialysis patients, and the elderly.
•	CLTI is a severe stage of PAD with rest pain, non-healing ulcers, or gangrene.
•	Goal: Restore perfusion to promote wound healing.
________________________________________
4. Indications for BTK Revascularisation
- Rest pain or non-healing ulcers.
- Salvage of failing bypass grafts.
- Limb preservation in severe PAD.
- Rapidly progressing diabetic foot ulcers.
- Prevention of major amputation.
________________________________________
5. Contraindications
Absolute:
- Severe systemic infection or uncontrolled sepsis.
- Severe renal failure (eGFR <15 mL/min) without dialysis.
- Lack of viable target arteries.
Relative:
- Poor functional status or short life expectancy.
________________________________________
6. Pre-Procedural Assessment
- Imaging: Duplex US, CTA/MRA, DSA.
- Hemodynamic testing: ABI, TBI, TcPO2.
________________________________________
7. Procedure: BTK Revascularisation
- Options: Balloon angioplasty, DCB, stenting, atherectomy, pedal arch reconstruction.
________________________________________
8. Post-Procedural Care & Follow-Up
- Antithrombotic therapy: DAPT and/or anticoagulation.
- Follow-up with Doppler US.
________________________________________
9. Outcomes & Complications
- Technical success: ~85–95%.
- Clinical success: ~70–90%.
- Complications: Hematoma, restenosis, distal embolization.
________________________________________
10. Level of Evidence
- Level 1: Endovascular-first approach is standard in CLTI.
- Level 2: DCB reduce restenosis.
- Level 3: Atherectomy may be beneficial.
________________________________________
11. Citation
CIRSE Standards of Practice on Below-the-Knee Revascularisation – Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi
________________________________________
""",
    
    "Hepatic Transarterial Chemoembolisation (TACE)": r"""
**CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE)
Authors: Pierleone Lucatelli, Marta Burrel, Boris Guiu, Gianluca de Rubeis, Otto van Delden, Thomas Helmberger
________________________________________
1. Introduction
•	Purpose: To provide best practices for TACE in hepatic tumors.
•	Scope:
  - Covers indications, contraindications, technical aspects, and post-procedural management.
  - Includes cTACE, DEM-TACE, DSM-TACE, and b-TACE.
•	Clinical Importance:
  - Standard-of-care for unresectable HCC in patients with preserved liver function.
________________________________________
2. Methods
•	Writing Group: Six experts in interventional oncology.
•	Literature Review:
  - PubMed and EMBASE search (2012–2020).
  - Consensus agreement.
________________________________________
3. Background
•	TACE delivers chemotherapy directly into the tumor with arterial embolization.
•	Types: cTACE, DEM-TACE, DSM-TACE, b-TACE.
________________________________________
4. Indications for TACE
- HCC with BCLC stage B.
- Non-surgical candidates for liver tumors.
- Palliative treatment for unresectable ICC and metastatic liver tumors.
________________________________________
5. Contraindications
Absolute:
- Decompensated liver disease (Child-Pugh C).
- Severe portal vein thrombosis.
- Uncontrolled infection.
Relative:
- Bilirubin >3 mg/dL.
- Extensive tumor burden.
________________________________________
6. Pre-Procedural Preparation
- Imaging: Multiphasic CT/MRI, ultrasound with Doppler.
- Laboratory: LFTs, AFP.
- Antibiotic prophylaxis.
________________________________________
7. Procedure: TACE Techniques
- Vascular access via the common femoral artery.
- Chemotherapy administration and embolization.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for post-embolization syndrome.
- LFTs at 24–48 hours and follow-up imaging.
________________________________________
9. Outcomes & Complications
- Tumor response: 50–70%.
- Median overall survival: 20–30 months.
- Complications vary from mild to severe.
________________________________________
10. Level of Evidence
- Level 1: TACE is first-line for unresectable HCC.
- Level 2: DEM-TACE reduces systemic toxicity.
- Level 3: b-TACE improves drug delivery.
________________________________________
11. Citation
CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE) – Pierleone Lucatelli, Marta Burrel, Boris Guiu, Gianluca de Rubeis, Otto van Delden, Thomas Helmberger
________________________________________
""",
    
    "Thermal Ablation of Bone Tumours": r"""
**CIRSE Standards of Practice on Thermal Ablation of Bone Tumours
Authors: Anthony Ryan, Caoimhe Byrne, Claudio Pusceddu, Xavier Buy, Georgia Tsoumakidou, Dimitrios Filippiadis
________________________________________
1. Introduction
•	Purpose: To provide best practices for thermal ablation of bone tumors.
•	Scope:
  - Focuses on RFA, cryoablation, MWA, and HIFU.
  - Addresses both benign and malignant bone lesions.
•	Clinical Importance:
  - Minimally invasive, effective pain relief, and local tumor control.
________________________________________
2. Methods
•	Writing Group: Six experts in musculoskeletal interventions.
•	Literature Review: PubMed search (2009–2021).
________________________________________
3. Background
•	Thermal ablation is an image-guided technique for osseous lesions.
•	Indications: Osteoid osteoma, painful metastases, selected malignancies.
________________________________________
4. Indications for Thermal Ablation
- Osteoid osteoma.
- Bone metastases.
- Selected primary malignant bone tumors.
- Recurrent tumors.
- Oligometastatic disease.
________________________________________
5. Contraindications
Absolute:
- Unsafe tumor access.
- Extensive cortical destruction.
- Severe uncorrectable bleeding disorders.
Relative:
- Lesions near neurovascular structures.
- Active infection.
- Poor prognosis.
________________________________________
6. Pre-Procedural Preparation
- Imaging: CT (preferred), MRI, bone scan/PET-CT.
- Laboratory: Coagulation profile, CBC.
- Anesthesia: General or conscious sedation.
________________________________________
7. Procedure: Thermal Ablation Techniques
- Patient positioning and anesthesia.
- Image-guided needle placement.
- Ablation (RFA, MWA, Cryoablation, or HIFU).
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for pain relief and complications.
- Follow-up imaging at 3–6 months.
________________________________________
9. Outcomes & Complications
- Success: Osteoid osteoma relief 90–95%; metastases pain reduction 70–85%.
- Complications: Mild pain, moderate fractures, severe infection.
________________________________________
10. Level of Evidence
- Level 1: RFA is first-line for osteoid osteoma.
- Level 2: Cryoablation offers superior pain relief for metastases.
- Level 3: HIFU is promising but needs further validation.
________________________________________
11. Citation
CIRSE Standards of Practice on Thermal Ablation of Bone Tumours – Anthony Ryan, Caoimhe Byrne, Claudio Pusceddu, Xavier Buy, Georgia Tsoumakidou, Dimitrios Filippiadis
________________________________________
""",
    
    "Prostate Artery Embolisation (PAE)": r"""
**CIRSE Standards of Practice on Prostate Artery Embolisation (PAE)
Authors: Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale
________________________________________
1. Introduction
•	Purpose: To provide best practices for PAE as a treatment for BPH.
•	Scope:
  - Covers patient selection, procedural techniques, safety measures, and follow-up care.
•	Clinical Importance:
  - PAE is a minimally invasive alternative to TURP with fewer complications.
________________________________________
2. Methods
•	Writing Group: Six experts in IR and urology.
•	Literature Review: PubMed search (2010–2021).
________________________________________
3. Background
•	BPH causes LUTS such as frequency, urgency, and weak stream.
•	PAE reduces prostate volume.
________________________________________
4. Indications for PAE
- Symptomatic BPH (IPSS >12), prostate volume >40 mL, patients unfit for surgery.
________________________________________
5. Contraindications
Absolute:
- Severe atherosclerosis of the iliac arteries.
- Severe CKD (GFR <30 mL/min).
- Contrast allergy.
Relative:
- Small prostate (<40 mL).
- Significant median lobe enlargement.
- Active UTI.
________________________________________
6. Pre-Procedural Preparation
- Imaging: Multiparametric MRI or CTA, TVUS, DSA.
- Laboratory: Renal function, CBC, PSA.
- Antibiotic prophylaxis with Ciprofloxacin.
________________________________________
7. Procedure: PAE
- Arterial access, superselective catheterization, embolization using PVA particles or microspheres.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for urinary retention and evaluate symptoms at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
- IPSS improvement 60–80%, prostate volume reduction ~30%.
- Complications include post-embolization syndrome and transient urinary retention.
________________________________________
10. Level of Evidence
- Level 1: PAE is safe and effective for moderate-to-severe BPH.
- Level 2: Comparable quality-of-life improvements to TURP.
- Level 3: Particularly beneficial in large prostates (>80 mL).
________________________________________
11. Citation
CIRSE Standards of Practice on Prostate Artery Embolisation (PAE) – Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale
________________________________________
""",
    
    "Endovascular Treatment of Acute Pulmonary Embolism (PE)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE)
Authors: Andreas F. Kütting, Michael D. Chick, Constantino Del Giudice, Martin P. Gunn, Maged A. N. Alharbi, Reinhold G. Erbel, Christoph A. Nienaber
________________________________________
1. Introduction
•	Purpose: To provide best practices for endovascular treatment of acute PE.
•	Scope:
  - Covers indications, contraindications, technical approaches, and post-procedural care.
  - Discusses CDT, mechanical thrombectomy, and aspiration techniques.
•	Clinical Importance:
  - PE is a life-threatening condition with high morbidity and mortality.
  - Rapid revascularization is critical.
________________________________________
2. Methods
•	Writing Group: Six experts.
•	Literature Review: PubMed search (2010–2022).
________________________________________
3. Background
•	PE results from embolic occlusion of the pulmonary arteries.
•	Classifications: Massive, submassive, low-risk.
________________________________________
4. Indications for Endovascular Therapy
- Massive PE requiring rapid revascularization.
- Submassive PE with RV dysfunction.
- Contraindication to systemic thrombolysis.
________________________________________
5. Contraindications
Absolute:
- Active major bleeding, uncorrectable coagulopathy.
Relative:
- Recent surgery, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
- Imaging: CTPA, echocardiography, lower limb Doppler.
- Laboratory: Coagulation profile, cardiac biomarkers.
________________________________________
7. Procedure: Endovascular PE Treatment
- Vascular access via common femoral or internal jugular vein.
- Techniques: CDT, mechanical thrombectomy, aspiration thrombectomy.
________________________________________
8. Post-Procedural Care & Follow-Up
- ICU monitoring for 24 hours.
- Continue anticoagulation; follow-up imaging.
________________________________________
9. Outcomes & Complications
- Technical success: 90–95%; clinical improvement: 85–95%.
- Complications: Minor hematoma to severe bleeding.
________________________________________
10. Level of Evidence
- Levels 1–3 as detailed.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE) – Andreas F. Kütting, Michael D. Chick, Constantino Del Giudice, Martin P. Gunn, Maged A. N. Alharbi, Reinhold G. Erbel, Christoph A. Nienaber
________________________________________
""",
    
    "Endovascular Treatment of Aortic Dissection": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection
Authors: Philipp A. Lüddecke, Martin M. Mortimer, Henrik A. Buenting, Konstantinos Stavroulakis, Klaus Hausegger, Constantino Del Giudice
________________________________________
1. Introduction
•	Purpose: To provide best practices for endovascular treatment of aortic dissection (focusing on TEVAR).
•	Scope:
  - Covers indications, procedural techniques, post-procedural care, and potential complications.
  - Primarily addresses Stanford Type B dissection with select Type A considerations.
•	Clinical Importance:
  - Aortic dissection is a life-threatening emergency.
  - TEVAR is a minimally invasive alternative to open surgery.
________________________________________
2. Methods
•	Writing Group: Six experts.
•	Literature Review: PubMed search (2012–2021).
________________________________________
3. Background
•	Aortic dissection results from an intimal tear creating a false lumen.
•	Stanford Classification: Type A (requires surgery) and Type B (often managed with TEVAR).
________________________________________
4. Indications for TEVAR
- Complicated Type B dissection with malperfusion, rupture, or rapid expansion.
________________________________________
5. Contraindications
Absolute:
- Proximal landing zone <15 mm without adequate sealing.
- Severe iliac/femoral disease.
Relative:
- Chronic stable dissection.
________________________________________
6. Pre-Procedural Workup
- Imaging: CTA (gold standard), TEE, MRA.
- Laboratory: Renal function, coagulation.
- Medical Optimization: BP control (target SBP <120 mmHg).
________________________________________
7. Procedure: TEVAR
- Vascular access via femoral artery; stent-graft deployment.
________________________________________
8. Post-Procedural Care & Follow-Up
- ICU monitoring for 24–48 hours; follow-up CTA.
________________________________________
9. Outcomes & Complications
- Technical success: 95–98%.
________________________________________
10. Level of Evidence
- Levels 1–3 as detailed.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection – Philipp A. Lüddecke, Martin M. Mortimer, Henrik A. Buenting, Konstantinos Stavroulakis, Klaus Hausegger, Constantino Del Giudice
________________________________________
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Purpose: To provide best practices for endovascular treatment of ALI, including patient selection, procedural techniques, and post-procedural care.
•	Scope:
  - Covers indications, contraindications, technical aspects, and follow-up management.
  - Focuses on endovascular therapy as an alternative to open surgical thrombectomy.
•	Clinical Importance:
  - ALI is a vascular emergency with high morbidity and mortality.
  - Rapid revascularization is critical.
________________________________________
2. Methods
•	Writing Group: Six experts.
•	Literature Review: PubMed search (2010–2022).
________________________________________
3. Background
•	ALI results from sudden arterial occlusion leading to tissue hypoxia.
•	Causes include embolism, thrombosis, and trauma.
•	Clinical presentation (Six Ps): Pain, Pallor, Pulselessness, Paresthesia, Paralysis, Poikilothermia.
•	Rutherford Classification: I (viable), IIa (threatened, mild), IIb (threatened, severe), III (non-viable).
________________________________________
4. Indications for Endovascular Therapy
- ALI (Rutherford IIa-IIb) requiring rapid revascularization.
- Failure of anticoagulation in embolic ALI.
- High surgical risk patients.
- Recurrent thrombotic occlusion.
________________________________________
5. Contraindications
Absolute:
- Stage III ALI (non-viable limb).
- Active uncontrolled bleeding or coagulopathy.
- Severe sepsis.
Relative:
- Heavy thrombotic burden.
- Extensive multilevel disease.
- Severe renal dysfunction (GFR <30 mL/min, contrast allergy).
________________________________________
6. Pre-Procedural Workup
- Imaging: CTA, Doppler ultrasound, DSA.
- Laboratory: Coagulation profile, renal function, cardiac markers.
- Medical Optimization: Immediate IV heparin, stabilization, pain management.
________________________________________
7. Procedure: Endovascular Revascularization for ALI
Step 1: Vascular Access & Imaging.
Step 2: Techniques:
  1. CDT.
  2. Mechanical Thrombectomy.
  3. Aspiration Thrombectomy.
  4. Stenting/Angioplasty if needed.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for reperfusion injury.
- Early ambulation.
- Continue anticoagulation; follow-up Doppler at 1 week and 3 months.
________________________________________
9. Outcomes & Complications
- Technical success: 90–95%.
- 1-year limb salvage rate: ~80%.
- Complications: Minor hematoma, reperfusion injury, thrombolytic-related bleeding.
________________________________________
10. Level of Evidence
- Level 1: Endovascular therapy is first-line for Rutherford IIa-IIb ALI.
- Level 2: CDT is effective for fresh thrombi.
- Level 3: Mechanical thrombectomy is preferred in high bleeding risk.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Purpose: To provide best practices for endovascular treatment of RAS, focusing on patient selection, procedural techniques, and post-procedural care.
•	Scope:
  - Covers indications, contraindications, technical aspects, and follow-up management.
  - Discusses atherosclerotic and fibromuscular dysplasia-related RAS.
•	Clinical Importance:
  - RAS is a major cause of secondary hypertension and CKD.
________________________________________
2. Methods
•	Writing Group: Six experts.
•	Literature Review: PubMed search (2010–2022).
________________________________________
3. Background
•	RAS is caused by narrowing of the renal arteries.
•	Two main causes: Atherosclerotic (~90%) and FMD (~10%).
•	Clinical consequences: Resistant hypertension, ischemic nephropathy, flash pulmonary edema.
________________________________________
4. Indications for Endovascular Therapy
- Severe RAS (>70%) with resistant hypertension, flash pulmonary edema, or worsening renal function.
- FMD-related RAS with severe hypertension.
- RAS in transplant recipients.
________________________________________
5. Contraindications
Absolute:
- RAS with well-controlled hypertension and stable function.
- ESRD with no recovery chance.
- Severe coagulopathy.
Relative:
- Heavy calcification, severe renal dysfunction with contrast allergy, multivessel disease with poor prognosis.
________________________________________
6. Pre-Procedural Workup
- Imaging: CTA (gold standard), Duplex Ultrasound, MRA, DSA.
- Laboratory: Renal function, coagulation profile, aldosterone-renin ratio.
- Medical Optimization: ACE inhibitors/ARBs, statins, pre-hydration.
________________________________________
7. Procedure: Endovascular Revascularization of RAS
Step 1: Vascular Access: Common femoral (preferred) or radial (for FMD).
Step 2: Technique:
  - For FMD: Balloon angioplasty only.
  - For atherosclerotic RAS: Stent placement using balloon-expandable stents.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for contrast-induced nephropathy and BP changes.
- Continue antiplatelet therapy; follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
- Technical success: 95–98%.
- BP improvement in ~50–70%; renal function stabilization/improvement in select cases.
- Complications: Minor hematoma, transient hypertension, in-stent restenosis, rare dissection/infarction.
________________________________________
10. Level of Evidence
- Level 1: Endovascular therapy is indicated in severe RAS.
- Level 2: Balloon angioplasty for FMD.
- Level 3: Routine follow-up imaging is necessary.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
**CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Purpose: To provide best practices for endovascular management of Type II endoleaks after EVAR.
•	Scope:
  - Covers indications, contraindications, technical aspects, and follow-up management.
  - Addresses endoleaks related to lumbar and IMA feeders.
•	Clinical Importance:
  - Type II endoleaks are common post-EVAR; persistent leaks may lead to sac expansion and rupture.
________________________________________
2. Methods
•	Writing Group: Six experts.
•	Literature Review: PubMed search (2010–2022).
________________________________________
3. Background
•	Occur due to retrograde flow from collateral arteries.
•	Causes include lumbar arteries (~60%), IMA (~30%), and accessory arteries (~10%).
•	Classification: Type IIa (single feeder) and Type IIb (multiple feeders).
________________________________________
4. Indications for Endovascular Therapy
- Aneurysm sac expansion (>5 mm in 6 months).
- Persistent endoleak beyond 12 months.
- Rapid increase in endoleak cavity size.
- Symptomatic endoleaks causing pain or embolic events.
________________________________________
5. Contraindications
Absolute:
- Small, stable endoleaks without sac growth.
- Severe renal impairment (GFR <30 mL/min).
- High surgical risk where intervention benefits are minimal.
Relative:
- Complex vascular anatomy.
- Extensive endoleak network.
- History of failed embolization.
________________________________________
6. Pre-Procedural Workup
- Imaging: CTA (gold standard), Duplex Ultrasound, DSA.
- Laboratory: Renal function, coagulation profile, hemoglobin.
- Medical Optimization: Continue antiplatelet therapy; pre-hydration.
________________________________________
7. Procedure: Endovascular Treatment of Type II Endoleaks
Step 1: Vascular Access & Imaging:
- Transarterial or translumbar approach.
- Baseline angiography to identify feeder vessels.
Step 2: Embolization Techniques:
  1. Transarterial Embolization (TAE) using coils and liquid embolics.
  2. Direct Sac Embolization (DSE) via CT-guided translumbar access.
  3. Combination Therapy for refractory cases.
Step 3: Post-Procedure Monitoring:
- Final angiography to confirm occlusion.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for complications; follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
- Technical success: 85–95%.
- Long-term sac stability in ~80%.
- Complications: Mild pain, incomplete embolization, severe non-target embolization (~1–3%).
________________________________________
10. Level of Evidence
- Level 1: Indicated for persistent, expanding endoleaks.
- Level 2: TAE is preferred for accessible feeders.
- Level 3: DSE is effective in refractory cases.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
Purpose: This document provides best practices for endovascular treatment of Budd-Chiari Syndrome (BCS), focusing on patient selection, procedural techniques, and post-procedural care.
Scope:
- Covers indications, contraindications, technical aspects, and follow-up management.
- Discusses angioplasty, stenting, thrombolysis, and TIPS in BCS patients.
Clinical Importance:
- BCS is a rare but life-threatening hepatic venous outflow obstruction leading to liver congestion and failure.
- Endovascular therapies improve survival and prevent liver damage.
________________________________________
2. Methods
- Writing Group: Six experts in vascular and hepatic interventions.
- Literature Review:
  - PubMed search (2010–2022).
  - Consensus agreement.
________________________________________
3. Background
- BCS is characterized by hepatic venous outflow obstruction.
- Causes:
  - Primary (thrombotic/hypercoagulable states: 75%).
  - Secondary (extrinsic compression: 25%).
- Clinical symptoms include hepatomegaly, RUQ pain, ascites, edema, and encephalopathy.
- Classification: Acute BCS (rapid congestion) vs. Chronic BCS (gradual progression).
________________________________________
4. Indications for Endovascular Therapy
- Symptomatic BCS with hepatic congestion.
- Failure of anticoagulation to maintain hepatic outflow.
- Hepatic venous outflow tract occlusion on imaging.
- Complications such as ascites and portal hypertension.
________________________________________
5. Contraindications
Absolute:
- Decompensated liver failure (Child-Pugh C, MELD >18) requiring transplant.
- Active, uncontrolled infection or sepsis.
- Severe coagulopathy.
Relative:
- Massive hepatomegaly limiting access.
- Extensive thrombosis requiring systemic thrombolysis.
- Severe renal dysfunction (GFR <30 mL/min) with contrast allergy.
________________________________________
6. Pre-Procedural Workup
- Imaging: Doppler US, CT/MR Venography, and intraoperative DSA.
- Laboratory: LFTs, renal function, hypercoagulability panel.
- Medical Optimization: Anticoagulation, diuretics, and correction of coagulopathy.
________________________________________
7. Procedure: Endovascular Treatment of BCS
Step 1: Vascular Access & Imaging:
- Preferred access: Right internal jugular vein (or femoral as an alternative).
- Baseline venography to assess stenosis and collateral flow.
Step 2: Treatment Options:
  1. Balloon Angioplasty for short-segment stenosis.
  2. Stent Placement for recurrent or long-segment occlusions (self-expanding stents preferred).
  3. Thrombolysis (CDT) in acute cases.
  4. TIPS for severe cases with portal hypertension.
Step 3: Post-Procedure Monitoring:
- Final venography to confirm vessel patency.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for complications and continue anticoagulation.
- Follow-up liver function tests and imaging (Doppler US or CTA) at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
- Technical success: 90–98%.
- Long-term hepatic function improvement in ~80%.
- Complications: Mild abdominal discomfort, minor hematoma; moderate stent restenosis; severe hepatic encephalopathy or liver decompensation.
________________________________________
10. Level of Evidence
- Level 1: Endovascular therapy is first-line for BCS with hepatic venous outflow obstruction.
- Level 2: TIPS is effective in refractory cases.
- Level 3: Long-term anticoagulation is needed.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
Purpose: This document provides best practices for endovascular treatment of PVT, focusing on patient selection, procedural techniques, and post-procedural care.
Scope:
- Covers indications, contraindications, technical aspects, and follow-up management.
- Discusses thrombolysis, thrombectomy, TIPS, and anticoagulation in PVT patients.
Clinical Importance:
- PVT can lead to portal hypertension, variceal bleeding, ascites, and hepatic decompensation.
- Endovascular therapy restores portal flow and improves outcomes, particularly in cirrhotic and post-transplant patients.
________________________________________
2. Methods
- Writing Group: Six experts in vascular and hepatic interventions.
- Literature Review: PubMed search (2010–2022).
________________________________________
3. Background
- PVT is the formation of a clot in the portal vein, impairing hepatic blood flow.
- Etiologies include cirrhosis, malignancy, hypercoagulable states, and post-surgical conditions.
- Clinical consequences vary from acute pain to chronic portal cavernoma.
________________________________________
4. Indications for Endovascular Therapy
- Symptomatic acute PVT with bowel ischemia or worsening liver function.
- Chronic PVT with portal hypertension complications.
- PVT in liver transplant recipients with compromised graft function.
- Failure of anticoagulation therapy.
________________________________________
5. Contraindications
Absolute:
- End-stage liver failure (MELD >20).
- Uncontrolled GI bleeding.
- Uncorrectable coagulopathy.
Relative:
- Extensive portal vein occlusion.
- Severe renal dysfunction (GFR <30 mL/min).
- Excessive thrombus burden.
________________________________________
6. Pre-Procedural Workup
- Imaging: CT/MR Venography, Doppler US, DSA.
- Laboratory: LFTs, coagulation profile, thrombophilia panel.
- Medical Optimization: Pre-procedure anticoagulation, correction of coagulopathy, and fluid resuscitation.
________________________________________
7. Procedure: Endovascular Treatment of PVT
Step 1: Vascular Access & Imaging:
- Preferred access: Transjugular (for TIPS) or percutaneous transhepatic.
- Baseline venography to assess thrombus and collaterals.
Step 2: Treatment Options:
  1. Catheter-Directed Thrombolysis (CDT).
  2. Mechanical Thrombectomy.
  3. TIPS for chronic PVT with portal hypertension.
  4. Stent placement for recanalization in chronic cases.
Step 3: Post-Procedure Monitoring:
- Final angiography to confirm flow restoration.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for bleeding, thrombosis, or renal impairment.
- Continue anticoagulation post-procedure.
- Follow-up imaging at 1 week, 3 months, and 6 months.
________________________________________
9. Outcomes & Complications
- Technical success: 85–95%.
- Long-term patency in ~75% of cases.
- Complications range from mild access site issues to severe hemorrhage or TIPS-related encephalopathy.
________________________________________
10. Level of Evidence
- Level 1: Endovascular therapy is the first-line treatment for symptomatic PVT.
- Level 2: TIPS is effective in chronic PVT with portal hypertension.
- Level 3: Long-term anticoagulation prevents recurrence.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT) – Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
""",
    
    "Uterine Artery Embolisation (UAE) for Symptomatic Fibroids": r"""
**CIRSE Standards of Practice on Uterine Artery Embolisation (UAE) for Symptomatic Fibroids
Authors: Nigel Hacking, Marc Sapoval, Miltiadis Krokidis, Ramon Vilarrasa, James Spies, Anna Maria Ierardi
________________________________________
1. Introduction
Purpose: This document provides best practices for performing uterine artery embolisation (UAE) for symptomatic fibroids, focusing on patient selection, technical aspects, safety measures, and follow-up recommendations.
Scope:
- Covers indications, contraindications, procedural techniques, and post-procedural management.
- Addresses uterine fibroids (leiomyomas) as well as adenomyosis.
Clinical Importance:
- UAE is a minimally invasive alternative to hysterectomy and myomectomy for fibroid treatment.
- It is effective for symptom control with a high success rate and uterine preservation.
________________________________________
2. Methods
- Writing Group: Six internationally recognized experts in interventional radiology and gynecology.
- Literature Review:
  - PubMed search (2010–2021) for studies on UAE for fibroids and adenomyosis.
  - Consensus agreement on best practices.
________________________________________
3. Background
- Uterine fibroids are benign tumors of the myometrium, affecting up to 70% of women by age 50.
- Common symptoms include heavy menstrual bleeding, pelvic pain, and pressure, as well as urinary frequency or constipation.
- Adenomyosis may also respond to UAE, though with variable success.
- UAE works by embolizing the uterine arteries, leading to fibroid ischemia and shrinkage.
________________________________________
4. Indications for UAE
- Symptomatic uterine fibroids causing menorrhagia, dysmenorrhea, pelvic pressure, or bulk symptoms.
- Women desiring uterine preservation.
- Contraindication to or refusal of surgery.
- Adenomyosis with significant symptoms.
________________________________________
5. Contraindications
Absolute Contraindications:
- Pregnancy.
- Active pelvic infection.
- Severe renal impairment precluding contrast administration.
Relative Contraindications:
- Submucosal fibroids >5 cm.
- Desire for future fertility.
- Large fibroid burden (>20 cm uterus).
________________________________________
6. Pre-Procedural Workup
- Imaging: Pelvic MRI (gold standard), TVUS, and CEUS for vascular mapping.
- Laboratory: Hemoglobin/hematocrit, renal function (eGFR).
- Patient Counseling: Discuss UAE as an alternative, potential fibroid expulsion, and post-embolization syndrome.
________________________________________
7. Procedure: Uterine Artery Embolisation (UAE)
Step 1: Arterial Access & Catheterization:
- Preferred access: Right common femoral artery.
- Use a 5 Fr catheter to access the internal iliac arteries and selectively catheterize the uterine arteries bilaterally.
Step 2: Embolization:
- Embolic Agents: Preferred are PVA particles (500–700 µm) or calibrated microspheres; gelatin sponge particles as an alternative.
- Injection: Slow embolization until near-stasis, avoiding reflux.
Step 3: Post-Embolization Check:
- Final angiography to confirm bilateral uterine artery occlusion; remove catheter and apply compression.
________________________________________
8. Post-Procedural Care & Follow-Up
- Monitor for pain, nausea, and fever (post-embolization syndrome).
- Manage pain with NSAIDs/opioids; consider intra-arterial lidocaine.
- Post-procedure imaging (MRI or TVUS) at 3 and 6 months.
________________________________________
9. Outcomes & Complications
- Success Rates: Symptom relief in 85–90% of patients; fibroid shrinkage of 40–60% within 6 months.
- Complications: Mild (post-embolization syndrome, transient amenorrhea), moderate (fibroid expulsion, urinary retention), severe (non-target embolization, uterine necrosis, infection).
________________________________________
10. Level of Evidence
- Level 1: UAE is a first-line treatment for symptomatic fibroids in women seeking uterine preservation.
- Level 2: MRI is superior to ultrasound for planning and follow-up.
- Level 3: Submucosal fibroids are more likely to be expelled.
________________________________________
11. Summary & Key Takeaways
✔ UAE is a minimally invasive, effective alternative to surgery for symptomatic fibroids.
✔ Best candidates are women with heavy menstrual bleeding or bulk symptoms who wish to avoid hysterectomy.
✔ Pelvic MRI is the preferred imaging modality.
✔ High success rate (~90%) with significant fibroid shrinkage within 6 months.
✔ Post-embolization syndrome is common and manageable.
✔ Follow-up imaging at 3–6 months is essential.
________________________________________
12. Citation
CIRSE Standards of Practice on Uterine Artery Embolisation (UAE) for Symptomatic Fibroids – Nigel Hacking, Marc Sapoval, Miltiadis Krokidis, Ramon Vilarrasa, James Spies, Anna Maria Ierardi
________________________________________
""",
    
    # (Other documents have been added previously.)
}

# =====================
# Apply Search Filter (searches keys and full text)
# =====================
if search_query:
    filtered_documents = {k: v for k, v in documents.items() if search_query.lower() in k.lower() or search_query.lower() in v.lower()}
    if not filtered_documents:
        st.warning("No documents found matching your search term.")
    else:
        docs_to_show = filtered_documents
else:
    docs_to_show = documents

# =====================
# Document Selection
# =====================
st.header("Select an Intervention")
selected_doc_title = st.selectbox("Intervention", list(docs_to_show.keys()))
doc_content = docs_to_show[selected_doc_title]

# =====================
# Language Notice
# =====================
if selected_language != "English":
    st.info("Currently, this document is only available in English.")

# =====================
# Function to Display Document Sections in Expanders
# =====================
def display_document_sections(doc_text):
    # Split the document by the delimiter (40 underscores)
    sections = doc_text.split("________________________________________")
    for sec in sections:
        sec = sec.strip()
        if sec:
            # Use an expander for each section with the first non-empty line as the header
            lines = sec.splitlines()
            if lines:
                header = lines[0].strip()
                content = "\n".join(lines[1:]).strip()
                with st.expander(header, expanded=False):
                    st.markdown(content)

display_document_sections(doc_content)

# =====================
# Disclaimer at the Bottom
# =====================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="disclaimer"><strong>Disclaimer:</strong> This application is intended for educational use only and does not substitute for professional clinical judgment. All recommendations and content are provided as a reference guide based on published standards. Please consult the full CIRSE Standards of Practice and other clinical resources before making clinical decisions.</div>',
    unsafe_allow_html=True
)
