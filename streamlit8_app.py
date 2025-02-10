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
CIRSE promotes excellence in interventional radiology through education, research, and the dissemination of best practices.  
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
    st.sidebar.info("Currently, documents are only available in English. Translations coming soon!")

# =====================
# Main Page Header
# =====================
st.title("CIRSE Standards of Practice Pocket Guide")
st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)

# =====================
# Display some introductory key points (without a separate "Key Features" block)
# =====================
st.markdown("""
Welcome to the CIRSE Standards of Practice Pocket Guide. This application provides the full, detailed text of the CIRSE Standards of Practice documents for various interventional procedures. Use the search tool to filter documents and select an intervention from the list below to view its detailed information in expandable sections.
""")

# =====================
# Search Functionality
# =====================
st.subheader("Search Documents")
search_query = st.text_input("Enter search term:")

# =====================
# Documents Dictionary
# =====================
# (Each key corresponds to the title of a document and the value is the full text provided.)
documents = {
    "Bronchial Artery Embolisation": r"""
CIRSE Standards of Practice on Bronchial Artery Embolisation
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
  o	Timeframe: 1974–2021.
  o	Source: PubMed database.
  o	Consensus-Based Recommendations.
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
  o	Identifies the culprit artery.
  o	Rules out alternative diagnoses.
  o	Helps plan catheterization.
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
  o	Microcatheter (2.7 Fr or smaller) for precise embolization.
  o	Avoid non-target embolization by sparing arteries that supply critical structures.
Embolization Agents
•	Preferred: Polyvinyl alcohol (PVA) particles (300–500 µm)
•	Alternatives:
  o	N-butyl-2-cyanoacrylate (NBCA) glue (for high-flow fistulas).
  o	Coils (used selectively).
Technique
1.	Confirm the target vessel via angiography.
2.	Slow infusion of embolic material until stasis is achieved.
3.	Avoid reflux to prevent non-target embolization.
4.	Post-embolization angiography to confirm treatment success.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Immediate Post-Procedure Monitoring:
  o	Observe for recurrence of haemoptysis (hospitalization if required).
  o	Monitor oxygen saturation and airway patency.
•	Long-Term Follow-Up:
  o	Repeat CTA or bronchoscopy if haemoptysis recurs.
  o	Additional embolization may be required in 10–30% of cases due to recanalization.
________________________________________
9. Outcomes & Complications
Technical Success Rate
•	85–98% initial success rate with embolization.
Rebleeding Rates
•	10–30% rebleeding within 6 months, often due to:
  o	Incomplete embolization.
  o	Collateral vessel formation.
  o	Progression of underlying disease.
Complications
Mild
•	Transient chest pain (due to ischemia).
Severe (Rare but Serious)
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
""",
    
    "Arterial Access for Interventions": r"""
CIRSE Standards of Practice on Arterial Access for Interventions
Authors: Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef
________________________________________
1. Introduction
•	Purpose: To provide best practices for safe and effective arterial access in interventional radiology.
•	Scope:
  •	Covers common femoral, radial, and brachial artery access.
  •	Addresses imaging, technique, and complication management.
•	Clinical Importance:
  •	Arterial access is the foundation of endovascular interventions, and complications at the access site can significantly impact outcomes.
________________________________________
2. Methods
•	Writing Group: Six experts in arterial interventions.
•	Literature Review:
  •	Evidence search performed via PubMed (2002–2019).
  •	Consensus-based recommendations.
________________________________________
3. Background
•	Arterial access is critical for many endovascular procedures.
•	History: Ultrasound guidance has dramatically reduced complications.
•	Radial access is gaining popularity due to lower bleeding risks.
________________________________________
4. Indications for Arterial Access
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
•	Severe obesity.
•	Radial artery anomalies.
•	Patients on high-dose anticoagulants.
________________________________________
6. Pre-Procedural Preparation
•	History & physical examination to assess prior procedures and access site suitability.
•	Imaging work-up:
  •	Ultrasound (US) guidance recommended.
  •	CTA/MRA for complex cases.
•	Anticoagulation management as needed.
________________________________________
7. Procedure
•	Common Femoral Artery (CFA) Access:
  •	Puncture 1–2 cm below the inguinal ligament under US guidance.
  •	Use micropuncture technique.
•	Radial Artery Access:
  •	Assess collateral circulation (Allen’s test).
  •	Use a 5–6 Fr sheath.
•	Brachial Artery Access:
  •	Used when other sites are not feasible.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Use manual compression or closure devices for hemostasis.
•	Monitor for complications such as bleeding, ischemia, or pseudoaneurysm.
________________________________________
9. Outcomes & Complications
•	Femoral access: >95% success with US guidance.
•	Radial access: Lower bleeding risk, higher spasm rates.
•	Complications include bleeding and pseudoaneurysm formation.
________________________________________
10. Level of Evidence
•	Level 1: Ultrasound guidance is recommended.
•	Level 2: Radial access offers lower bleeding risks.
•	Level 3: Closure devices reduce hemostasis time but carry risks.
________________________________________
11. Summary
•	Arterial access is essential for endovascular procedures.
•	Proper patient selection and anticoagulation management are crucial.
________________________________________
12. Citation
CIRSE Standards of Practice on Arterial Access for Interventions – Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef
""",
    
    "Varicocele Embolisation": r"""
CIRSE Standards of Practice on Varicocele Embolisation
Authors: Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi
________________________________________
1. Introduction
•	Provides best practices for percutaneous varicocele embolisation.
•	An alternative to surgical ligation with lower morbidity.
________________________________________
2. Methods
•	Writing Group: Five internationally recognized experts.
•	Literature Review: PubMed search (2006–2021) and expert consensus.
________________________________________
3. Background
•	Varicocele is the abnormal dilation of testicular veins in the pampiniform plexus, causing venous reflux.
•	Affects 15% of adult males and up to 35–50% of infertile men.
________________________________________
4. Indications for Embolisation
•	Varicocele-related infertility.
•	Testicular hypotrophy.
•	Persistent scrotal pain.
•	Cosmetic concerns.
•	Recurrent varicocele post-surgery.
________________________________________
5. Contraindications
Absolute Contraindications:
•	Allergy to contrast agents.
•	Severe uncorrectable coagulopathy.
Relative Contraindications:
•	Renal insufficiency.
•	Bilateral varicocele requiring a complex approach.
________________________________________
6. Pre-Procedural Preparation
•	Physical examination and scrotal ultrasound (gold standard).
•	Doppler ultrasound to confirm reflux.
•	Laboratory tests: Coagulation profile and renal function.
________________________________________
7. Procedure: Percutaneous Varicocele Embolisation
•	Access via right femoral or jugular vein.
•	Venography to confirm reflux and identify collaterals.
•	Superselective catheterization of the internal spermatic vein.
•	Embolisation using coils, sclerosing agents, or NBCA glue.
•	Post-embolisation venography to confirm occlusion.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for pain, allergic reactions, or coil migration.
•	Follow-up clinical exam at 1–3 months and repeat Doppler at 3–6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
•	Clinical success: 70–90% improvement.
•	Complications: Mild (scrotal pain), moderate (rare coil migration), severe (non-target embolisation, testicular atrophy - very rare).
________________________________________
10. Level of Evidence
•	Level 1: Scrotal ultrasound is the diagnostic gold standard.
•	Level 2: Embolisation is as effective as surgery with fewer complications.
•	Level 3: Coils are the preferred embolic material.
________________________________________
11. Summary
•	Varicocele embolisation is a safe, minimally invasive alternative to surgery.
________________________________________
12. Citation
CIRSE Standards of Practice on Varicocele Embolisation – Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi
""",
    
    "Oesophageal and Gastroduodenal Stenting": r"""
CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting
Authors: Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal
________________________________________
1. Introduction
•	Provides best practices for placing self-expanding metal stents (SEMS) in the oesophagus and gastroduodenal tract.
•	Effective for palliative treatment of dysphagia and gastric outlet obstruction.
________________________________________
2. Methods
•	Writing Group: Five internationally recognized experts.
•	Literature Review: PubMed search (2005–2021) and consensus-based recommendations.
________________________________________
3. Background
•	SEMS are used to relieve obstruction caused by malignant or benign strictures.
•	Oesophageal cancer and gastric outlet obstruction are major clinical problems.
________________________________________
4. Indications for Stenting
•	Malignant strictures, tracheo-oesophageal fistulas, and benign strictures refractory to balloon dilation.
•	Gastric outlet obstruction in patients unsuitable for surgery.
________________________________________
5. Contraindications
Absolute Contraindications:
•	Perforation or fistula not amenable to stenting.
•	Severe bleeding requiring immediate surgery.
•	Obstructions unsuitable for stenting.
Relative Contraindications:
•	Severe coagulopathy.
•	High risk of stent migration.
•	Poor prognosis.
________________________________________
6. Pre-Procedural Preparation
•	Evaluate dysphagia, weight loss, and nutritional status.
•	Endoscopic and imaging evaluation (CT, fluoroscopy).
•	Laboratory tests: Coagulation and renal function.
________________________________________
7. Procedure: Stent Placement
•	Patient positioning: Oesophageal stenting in supine; gastroduodenal in supine or left lateral decubitus.
•	Guidewire placement under fluoroscopic and/or endoscopic guidance.
•	Deployment of SEMS; balloon dilation as needed.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for pain, stent migration, or aspiration.
•	Initiate a soft diet after 24 hours.
•	Follow-up imaging for recurrent dysphagia.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–99%; clinical success: 75–90%.
•	Complications: Mild (chest pain), moderate (stent migration, tumor overgrowth), severe (aspiration pneumonia, perforation, massive bleeding).
________________________________________
10. Level of Evidence
•	Level 1: SEMS are first-line for malignant dysphagia.
•	Level 2: Combined endoscopic and fluoroscopic guidance improves accuracy.
•	Level 3: Stenting for benign strictures is reserved for refractory cases.
________________________________________
11. Summary
•	Provides rapid symptomatic relief with manageable complications.
________________________________________
12. Citation
CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting – Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal
""",
    
    "Peri-Operative Anticoagulation Management During IR Procedures": r"""
CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During Interventional Radiology Procedures
Authors: Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi
________________________________________
1. Introduction
•	Provides best practices for managing anticoagulation in IR procedures.
________________________________________
2. Methods
•	Writing Group: Experts in IR and hematology.
•	Literature Review: Comprehensive search and Delphi consensus.
________________________________________
3. Background
•	Challenging due to balancing bleeding and thromboembolic risks.
________________________________________
4. Indications for Anticoagulation in IR Patients
•	For atrial fibrillation, VTE prophylaxis, mechanical heart valves, recent MI, and hypercoagulable states.
________________________________________
5. Contraindications to Anticoagulation in IR
Absolute: Active bleeding, recent intracranial hemorrhage, uncontrolled hypertension, severe thrombocytopenia.
Relative: High bleeding risk procedures, coagulation disorders, recent major surgery.
________________________________________
6. Pre-Procedural Coagulation Assessment
•	Structured bleeding history and laboratory testing (PT/INR, aPTT, fibrinogen, platelets).
________________________________________
7. Anticoagulation Management Based on Procedure Risk
•	Continue for low-risk; modify for moderate-risk; hold for high-risk procedures.
________________________________________
8. Peri-Procedural Management of Specific Anticoagulants
| Anticoagulant | Pre-Procedural Holding Time | Post-Procedural Restart Time |
|---------------|-----------------------------|------------------------------|
| Warfarin      | 5 days before high-risk     | 24–48 hours post-procedure   |
| Heparin       | 4–6 hours before            | Immediate or 24 hrs based on risk |
| LMWH          | 24 hours before             | 24 hours post-procedure      |
| DOACs         | 24–48 hours (renal-dependent)| 24 hours post-procedure      |
________________________________________
9. Bridging Strategies
•	For high-risk warfarin patients: stop warfarin 5 days pre-procedure, bridge with LMWH, and resume post-procedure.
________________________________________
10. Post-Procedural Care & Monitoring
•	Monitor for bleeding and thrombosis; gradual reintroduction of anticoagulation.
________________________________________
11. Outcomes & Complications
•	Minor bleeding: 5–15%; major: 1–5%; VTE recurrence and stroke risks are noted.
________________________________________
12. Level of Evidence
•	Levels 1–3 based on screening and bridging strategies.
________________________________________
13. Summary
•	Effective management is critical to balance bleeding and thrombosis risks.
________________________________________
14. Citation
CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During IR Procedures – Mohammed Hadi et al.
""",
    
    "Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting": r"""
CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting
Authors: Marco Das, Christiaan van der Leij, Marcus Katoh, Daniel Benten, Babs M. F. Hendriks, Adam Hatzidakis
________________________________________
1. Introduction
•	Provides best practices for PTC, PTBD, and PTBS.
________________________________________
2. Methods
•	Literature review from 2000–2021.
________________________________________
3. Background
•	PTC visualizes the biliary system; PTBD drains biliary obstructions; PTBS maintains bile flow.
________________________________________
4. Indications
•	For malignant and benign biliary strictures, cholangitis, and post-surgical collections.
________________________________________
5. Contraindications
Absolute: Severe uncorrectable coagulopathy, massive ascites, uncontrolled sepsis.
Relative: Liver metastases, multiple intrahepatic strictures.
________________________________________
6. Pre-Procedural Preparation
•	Imaging (US, CT, MRI/MRCP) and laboratory tests.
•	Antibiotic prophylaxis.
________________________________________
7. Procedure
•	Step-by-step approach for PTC, PTBD, and PTBS.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for bleeding, infection, and bile leak; follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; improvement in jaundice >85%.
________________________________________
10. Level of Evidence
•	Based on guidelines for biliary drainage.
________________________________________
11. Citation
CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting – Marco Das et al.
""",
    
    "Below-the-Knee Revascularisation": r"""
CIRSE Standards of Practice on Below-the-Knee Revascularisation
Authors: Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi
________________________________________
1. Introduction
•	Provides best practices for BTK revascularisation.
________________________________________
2. Methods
•	Consensus-based recommendations from 2004–2020.
________________________________________
3. Background
•	Focus on endovascular treatment for chronic limb-threatening ischemia.
________________________________________
4. Indications
•	For rest pain, non-healing ulcers, salvage of bypass grafts, and limb preservation.
________________________________________
5. Contraindications
Absolute: Severe infection, renal failure, lack of target vessels.
Relative: Poor functional status, extensive necrosis.
________________________________________
6. Pre-Procedural Assessment
•	Imaging with Duplex, CTA/MRA, and DSA; hemodynamic testing.
________________________________________
7. Procedure
•	Options include balloon angioplasty, DCB, DES, atherectomy, and pedal arch reconstruction.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Antithrombotic therapy and follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: ~85–95%; clinical success: ~70–90%.
________________________________________
10. Level of Evidence
•	Endovascular-first approach is recommended.
________________________________________
11. Citation
CIRSE Standards of Practice on Below-the-Knee Revascularisation – Stavros Spiliopoulos et al.
""",
    
    "Hepatic Transarterial Chemoembolisation (TACE)": r"""
CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE)
Authors: Pierleone Lucatelli, Marta Burrel, Boris Guiu, Gianluca de Rubeis, Otto van Delden, Thomas Helmberger
________________________________________
1. Introduction
•	Provides best practices for TACE in hepatic tumors.
________________________________________
2. Methods
•	Literature review from 2012–2020.
________________________________________
3. Background
•	TACE delivers chemotherapy into the tumor and embolizes its blood supply.
________________________________________
4. Indications
•	For unresectable HCC, ICC, and metastatic liver tumors.
________________________________________
5. Contraindications
Absolute: Decompensated liver disease (Child-Pugh C), severe portal vein thrombosis, uncontrolled infection.
Relative: Elevated bilirubin, extensive tumor burden.
________________________________________
6. Pre-Procedural Preparation
•	Multiphasic CT/MRI, LFTs, AFP, and antibiotic prophylaxis.
________________________________________
7. Procedure
•	Common femoral artery access; selective catheterization; chemotherapy infusion; embolisation.
________________________________________
8. Post-Procedural Care
•	Monitor for post-embolisation syndrome; LFTs at 24–48 hours; follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Tumor response: 50–70%; median OS: 20–30 months.
________________________________________
10. Level of Evidence
•	TACE is first-line for unresectable HCC in selected patients.
________________________________________
11. Citation
CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE) – Pierleone Lucatelli et al.
""",
    
    "Thermal Ablation of Bone Tumours": r"""
CIRSE Standards of Practice on Thermal Ablation of Bone Tumours
Authors: Anthony Ryan, Caoimhe Byrne, Claudio Pusceddu, Xavier Buy, Georgia Tsoumakidou, Dimitrios Filippiadis
________________________________________
1. Introduction
•	Provides best practices for thermal ablation (RFA, cryoablation, MWA, HIFU) of bone tumours.
________________________________________
2. Methods
•	Literature review from 2009–2021.
________________________________________
3. Background
•	Thermal ablation is used for benign bone tumours, metastases, and selected malignant lesions.
________________________________________
4. Indications
•	For osteoid osteoma, painful bone metastases, and recurrent tumours.
________________________________________
5. Contraindications
Absolute: Unsafe access, extensive cortical destruction, severe bleeding disorders.
Relative: Lesions near neurovascular structures, active infection.
________________________________________
6. Pre-Procedural Preparation
•	CT/MRI imaging, laboratory tests, and appropriate anesthesia.
________________________________________
7. Procedure
•	Image-guided probe placement; ablation via RFA, MWA, cryoablation, or HIFU.
________________________________________
8. Post-Procedural Care
•	Monitor for pain relief; follow-up imaging at 3–6 months.
________________________________________
9. Outcomes & Complications
•	High success in osteoid osteoma; complications include minor pain and rare fractures.
________________________________________
10. Level of Evidence
•	RFA is first-line for osteoid osteoma; cryoablation for metastases.
________________________________________
11. Citation
CIRSE Standards of Practice on Thermal Ablation of Bone Tumours – Anthony Ryan et al.
""",
    
    "Prostate Artery Embolisation (PAE)": r"""
CIRSE Standards of Practice on Prostate Artery Embolisation (PAE)
Authors: Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale
________________________________________
1. Introduction
•	Provides best practices for PAE as a treatment for benign prostatic hyperplasia.
________________________________________
2. Methods
•	Literature review from 2010–2021.
________________________________________
3. Background
•	BPH causes LUTS; PAE reduces prostate volume via embolisation.
________________________________________
4. Indications for PAE
•	Symptomatic BPH (IPSS >12) with prostate volume >40 mL.
________________________________________
5. Contraindications
Absolute: Severe atherosclerosis, severe CKD, contrast allergy.
Relative: Small prostate, significant median lobe enlargement, active UTI.
________________________________________
6. Pre-Procedural Preparation
•	Multiparametric MRI/CTA; TRUS; laboratory tests.
________________________________________
7. Procedure
•	Superselective embolisation via femoral or radial access using PVA particles or microspheres.
________________________________________
8. Post-Procedural Care
•	Monitor urinary symptoms; follow-up evaluations at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	IPSS improvement of 60–80%; low complication rates.
________________________________________
10. Level of Evidence
•	PAE is safe and effective, particularly in larger prostates.
________________________________________
11. Citation
CIRSE Standards of Practice on Prostate Artery Embolisation (PAE) – Marc Sapoval et al.
""",
    
    "Endovascular Treatment of Acute Pulmonary Embolism (PE)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE)
Authors: Andreas F. Kütting, Michael D. Chick, Constantino Del Giudice, Martin P. Gunn, Maged A. N. Alharbi, Reinhold G. Erbel, Christoph A. Nienaber
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of acute PE.
________________________________________
2. Methods
•	Literature review from 2012–2021.
________________________________________
3. Background
•	PE is caused by thromboemboli; classified as massive, submassive, or low risk.
________________________________________
4. Indications for Endovascular Therapy
•	Massive PE with hemodynamic instability and select submassive cases.
________________________________________
5. Contraindications
Absolute: Active major bleeding, severe coagulopathy, uncontrolled hypertension.
Relative: Recent surgery, history of hemorrhagic stroke.
________________________________________
6. Pre-Procedural Workup
•	CTPA, echocardiography, and lower extremity Doppler.
________________________________________
7. Procedure
•	Venous access (femoral or jugular); CDT, mechanical thrombectomy, or aspiration thrombectomy.
________________________________________
8. Post-Procedural Care
•	ICU monitoring; continued anticoagulation; follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; improvement in hemodynamics.
________________________________________
10. Level of Evidence
•	CDT offers lower bleeding risks compared to systemic thrombolysis.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE) – Andreas F. Kütting et al.
""",
    
    "Endovascular Treatment of Aortic Dissection": r"""
CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection
Authors: Philipp A. Lüddecke, Martin M. Mortimer, Henrik A. Buenting, Konstantinos Stavroulakis, Klaus Hausegger, Constantino Del Giudice
________________________________________
1. Introduction
•	Provides best practices for TEVAR in aortic dissection.
________________________________________
2. Methods
•	Literature review from 2012–2021.
________________________________________
3. Background
•	Aortic dissection involves a tear in the intima, creating a false lumen.
•	Stanford Type A requires surgery; Type B is often managed with TEVAR.
________________________________________
4. Indications for TEVAR
•	For complicated Type B dissection: rupture, malperfusion, rapid expansion, persistent pain.
________________________________________
5. Contraindications
Absolute: Inadequate landing zones, severe access vessel disease, active infection.
Relative: Chronic stable dissection, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CTA, TEE, or MRA; blood tests and strict blood pressure control.
________________________________________
7. Procedure
•	Femoral artery access; stent-graft deployment with 10–15% oversizing.
________________________________________
8. Post-Procedural Care
•	ICU monitoring; follow-up CTA at 1, 6, and 12 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; complications include endoleak and spinal cord ischemia.
________________________________________
10. Level of Evidence
•	TEVAR is first-line for complicated Type B dissection.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection – Philipp A. Lüddecke et al.
""",
    
    "Uterine Artery Embolisation (UAE) for Symptomatic Fibroids": r"""
CIRSE Standards of Practice on Uterine Artery Embolisation (UAE) for Symptomatic Fibroids
Authors: Overhagen H., Binkert C., Röthlin M., Kaufmann C., Pellerin O., Walker W., Spies J.
________________________________________
1. Introduction
•	Purpose: To provide best practices for performing UAE for symptomatic fibroids.
•	Scope: Covers indications, contraindications, procedural techniques, and follow-up management.
•	Clinical Importance: UAE is a minimally invasive alternative to hysterectomy/myomectomy with high success rates and uterine preservation.
________________________________________
2. Methods
•	Writing Group: Seven experts in interventional radiology and gynecology.
•	Literature Review: PubMed search (2000–2015) and consensus.
________________________________________
3. Background
•	Uterine fibroids (leiomyomas) affect up to 70% of women by age 50.
•	Common symptoms: Heavy menstrual bleeding, pelvic pain, pressure, and urinary disturbances.
•	UAE embolizes the uterine arteries to induce fibroid ischemia and shrinkage.
________________________________________
4. Indications for UAE
•	Symptomatic fibroids causing menorrhagia, pelvic pressure, or bulk symptoms.
•	Women desiring uterine preservation.
•	Contraindication to or refusal of surgery.
•	Recurrent fibroids post-myomectomy.
•	Adenomyosis with significant symptoms.
________________________________________
5. Contraindications
Absolute:
•	Pregnancy.
•	Active pelvic infection.
•	Suspected uterine malignancy.
•	Severe renal impairment.
Relative:
•	Desire for future fertility.
•	Very large fibroid burden.
•	Significant submucosal fibroids.
________________________________________
6. Pre-Procedural Workup
•	Pelvic MRI (gold standard), TVUS, and CEUS for fibroid evaluation.
•	Laboratory tests: Hemoglobin, hematocrit, renal function, coagulation profile.
•	Patient counseling regarding fibroid expulsion and post-embolisation syndrome.
________________________________________
7. Procedure: UAE
•	Arterial access via right common femoral artery.
•	5 Fr catheter into internal iliac arteries.
•	Superselective catheterization of uterine arteries.
•	Embolisation using PVA particles (500–700 µm) or calibrated microspheres.
•	Post-embolisation angiography to confirm bilateral occlusion.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for post-embolisation syndrome (fever, pain, nausea); manage with NSAIDs/opioids.
•	Follow-up imaging (MRI or TVUS) at 3 and 6 months.
________________________________________
9. Outcomes & Complications
•	Success: 85–90% symptom relief; fibroid shrinkage of 40–60% within 6 months.
•	Complications: Common PES, transient amenorrhea, fibroid expulsion, urinary retention; rare cases of ovarian failure or uterine necrosis.
________________________________________
10. Level of Evidence
•	Level 1: UAE is safe and effective for symptomatic fibroids.
•	Level 2: MRI is preferred for planning and follow-up.
•	Level 3: Submucosal fibroids have a higher likelihood of expulsion.
________________________________________
11. Citation
CIRSE Standards of Practice on Uterine Artery Embolisation (UAE) for Symptomatic Fibroids – Overhagen H. et al.
""",
    
    "Endovascular Management of Central Venous Stenosis and Occlusion": r"""
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion
Authors: Raman Uberoi, Alessandro Napoli, Thomas Rand, Marc Sapoval, Robert A. Lookstein, Miltiadis Krokidis
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of central venous stenosis and occlusion.
________________________________________
2. Methods
•	Writing Group: Six experts.
•	Literature Review: PubMed search (2010–2022) and consensus.
________________________________________
3. Background
•	Central venous stenosis results from progressive fibrosis; common in dialysis and cancer patients.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic venous hypertension, access dysfunction, and malignant obstruction.
________________________________________
5. Contraindications
Absolute: Active sepsis, uncorrectable coagulopathy, severe right heart dysfunction.
Relative: Extensive thrombosis, short life expectancy, severe radiation fibrosis.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler ultrasound, and DSA.
•	Laboratory tests: Coagulation, renal function, CBC.
________________________________________
7. Procedure
•	Venous access via common femoral or jugular vein; balloon angioplasty and stenting.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for complications and continue anticoagulation as indicated.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; 1-year patency: 70–85%.
________________________________________
10. Level of Evidence
•	Levels 1–3 based on imaging and long-term follow-up.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion – Raman Uberoi et al.
""",
    
    "Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of CMI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	CMI is due to progressive stenosis of mesenteric arteries, commonly from atherosclerosis.
________________________________________
4. Indications for Endovascular Therapy
•	Severe symptomatic CMI with ≥70% stenosis and failure of medical therapy.
________________________________________
5. Contraindications
Absolute: Acute mesenteric ischemia, severe aortic disease, uncorrectable coagulopathy.
Relative: Heavy calcification, multivessel disease.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex ultrasound, and DSA.
•	Laboratory tests and medical optimization.
________________________________________
7. Procedure
•	Vascular access via femoral or brachial artery; stent placement in mesenteric arteries.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor with CTA or Duplex at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular stenting is first-line in symptomatic CMI.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Arterial Trauma": r"""
CIRSE Standards of Practice on Endovascular Treatment of Arterial Trauma
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of arterial trauma.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Traumatic arterial injuries include dissection, pseudoaneurysm, AV fistula, and occlusion.
________________________________________
4. Indications for Endovascular Therapy
•	For hemodynamically stable patients with arterial injury (pseudoaneurysm, dissection, AVF).
________________________________________
5. Contraindications
Absolute: Complete transection requiring open repair, severe tortuosity, active infection.
Relative: Extensive thrombosis, significant calcification, contrast allergy.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex ultrasound, and DSA.
•	Laboratory tests including coagulation profile and renal function.
________________________________________
7. Procedure
•	Vascular access via common femoral or brachial artery.
•	Repair strategies include stent-grafts, coil embolization, liquid embolics, and balloon occlusion.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for complications and ensure vessel patency with follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%; complications include in-stent restenosis and arterial rupture.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for most arterial trauma.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Arterial Trauma – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Visceral Aneurysms and Pseudoaneurysms": r"""
CIRSE Standards of Practice on Endovascular Management of Visceral Aneurysms and Pseudoaneurysms
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular management of visceral aneurysms and pseudoaneurysms.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	VAAs and VPAs involve aneurysmal dilatation of visceral arteries, with VPAs having higher rupture risk.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic aneurysms, aneurysm diameter >2 cm, rapid growth, or VPAs of any size.
________________________________________
5. Contraindications
Absolute: Active infection, severe coagulopathy, or complete occlusion of collaterals.
Relative: Vessel tortuosity, severe renal impairment.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex ultrasound, and DSA.
•	Laboratory tests: Coagulation and renal function.
________________________________________
7. Procedure
•	Options include coil embolization, stent-graft placement, liquid embolics, or parent vessel occlusion.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for access complications and perform follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; long-term exclusion: 85–90%.
________________________________________
10. Level of Evidence
•	Level 1 for endovascular repair; follow-up imaging is mandatory.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Visceral Aneurysms and Pseudoaneurysms – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of ALI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	ALI is a vascular emergency caused by sudden arterial occlusion.
________________________________________
4. Indications for Endovascular Therapy
•	For Rutherford IIa-IIb ALI requiring rapid revascularization.
________________________________________
5. Contraindications
Absolute: Non-viable limb (Rutherford III), active bleeding, severe coagulopathy.
Relative: High thrombus burden, extensive multilevel disease.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Doppler ultrasound, and DSA.
•	Laboratory tests: Coagulation profile and renal function.
________________________________________
7. Procedure
•	Techniques include catheter-directed thrombolysis, mechanical thrombectomy, aspiration thrombectomy, and stenting if needed.
________________________________________
8. Post-Procedural Care
•	Monitor for reperfusion injury; continue anticoagulation; follow-up ultrasound at 1 week and 3 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; 1-year limb salvage ~80%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for ALI (Rutherford IIa-IIb).
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating RAS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	RAS leads to secondary hypertension and CKD; causes include atherosclerosis and fibromuscular dysplasia.
________________________________________
4. Indications for Endovascular Therapy
•	Severe RAS (>70%) with resistant hypertension or deteriorating renal function.
________________________________________
5. Contraindications
Absolute: RAS with stable controlled hypertension; ESRD.
Relative: Heavy calcification, severe renal dysfunction with contrast allergy.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex ultrasound, MRA, and DSA.
•	Laboratory tests: Renal function and coagulation profile.
________________________________________
7. Procedure
•	For FMD, balloon angioplasty alone; for atherosclerotic RAS, stent placement with balloon-expandable stents.
________________________________________
8. Post-Procedural Care
•	Monitor renal function and blood pressure; maintain antiplatelet therapy.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; improvement in BP in ~50–70%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is indicated for severe, symptomatic RAS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for managing Type II endoleaks after EVAR.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Type II endoleaks occur from retrograde flow from collateral arteries (lumbar, IMA).
________________________________________
4. Indications for Endovascular Therapy
•	Aneurysm sac expansion (>5 mm in 6 months) or persistent endoleak beyond 12 months.
________________________________________
5. Contraindications
Absolute: Small, stable endoleaks; severe renal impairment.
Relative: Complex vascular anatomy; history of failed embolisation.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex ultrasound, DSA.
•	Laboratory tests: Renal function, coagulation profile.
________________________________________
7. Procedure
•	Options: Transarterial embolisation (TAE), direct sac embolisation (DSE), or combination.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor with CTA or Duplex at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Indicated for persistent, growing Type II endoleaks.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of BCS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	BCS is hepatic venous outflow obstruction causing liver congestion and failure.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic BCS with hepatic venous outflow obstruction.
________________________________________
5. Contraindications
Absolute: Decompensated liver failure, active infection, severe coagulopathy.
Relative: Massive hepatomegaly, extensive thrombosis, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	Doppler US, CT/MR venography, and DSA.
•	Laboratory tests: LFTs, renal function, hypercoagulability panel.
________________________________________
7. Procedure
•	Options include balloon angioplasty, stenting, thrombolysis, and TIPS.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor liver function and access site; follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for BCS with venous outflow obstruction.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of PVT.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PVT is the formation of a clot in the portal vein, leading to portal hypertension and hepatic dysfunction.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic acute or chronic PVT with portal hypertension complications.
________________________________________
5. Contraindications
Absolute: End-stage liver failure, active GI bleeding, uncorrectable coagulopathy.
Relative: Extensive portal occlusion, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, and DSA.
•	Laboratory tests: LFTs, coagulation, CBC.
________________________________________
7. Procedure
•	Options include catheter-directed thrombolysis (CDT), mechanical thrombectomy, TIPS, and stent placement.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor for bleeding and thrombosis; follow-up imaging at 1 week, 3 months, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for symptomatic PVT.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
(See duplicate entry above.)
""",
    
    "Endovascular Treatment of Peripheral Arterial Disease (PAD)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of PAD.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PAD results from atherosclerosis; severity classified using Rutherford scales.
________________________________________
4. Indications for Endovascular Therapy
•	Lifestyle-limiting claudication and critical limb ischemia.
________________________________________
5. Contraindications
Absolute: Severe calcification, extensive occlusion, uncorrectable coagulopathy.
Relative: Severe renal impairment, heavily thrombotic lesions, limb infection.
________________________________________
6. Pre-Procedural Workup
•	CTA is the gold standard; Doppler ultrasound and DSA for lesion assessment.
•	Laboratory tests for renal and coagulation status.
________________________________________
7. Procedure
•	Vascular access via common femoral (or radial for tibial disease).
•	Techniques include balloon angioplasty, stenting, atherectomy, and DCB.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Antiplatelet therapy and follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%; 1-year primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for PAD in most cases.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of ALI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	ALI is a vascular emergency due to sudden arterial occlusion.
________________________________________
4. Indications for Endovascular Therapy
•	For Rutherford IIa-IIb ALI requiring rapid revascularization.
________________________________________
5. Contraindications
Absolute: Rutherford III, active bleeding, severe coagulopathy.
Relative: High thrombus burden, multilevel disease.
________________________________________
6. Pre-Procedural Workup
•	CTA, Doppler ultrasound, DSA; lab tests for coagulation and renal function.
________________________________________
7. Procedure
•	Includes CDT, mechanical thrombectomy, aspiration thrombectomy, and stenting if needed.
________________________________________
8. Post-Procedural Care
•	Monitor for reperfusion injury and maintain anticoagulation.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; 1-year limb salvage: ~80%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for ALI.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating RAS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	RAS is caused by atherosclerosis or FMD leading to hypertension and CKD.
________________________________________
4. Indications for Endovascular Therapy
•	Severe RAS (>70%) with resistant hypertension or worsening renal function.
________________________________________
5. Contraindications
Absolute: Well-controlled hypertension, ESRD.
Relative: Heavy calcification, severe renal dysfunction with contrast allergy.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, MRA; lab tests for renal function and coagulation.
________________________________________
7. Procedure
•	For FMD, perform PTA; for atherosclerotic lesions, stenting is preferred.
________________________________________
8. Post-Procedural Care
•	Monitor renal function and blood pressure; maintain antiplatelet therapy.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; BP improvement in 50–70%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is indicated for severe symptomatic RAS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for managing persistent Type II endoleaks after EVAR.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Type II endoleaks occur due to retrograde flow from collateral arteries.
________________________________________
4. Indications for Endovascular Therapy
•	Aneurysm sac expansion >5 mm in 6 months or persistent endoleak beyond 12 months.
________________________________________
5. Contraindications
Absolute: Stable endoleaks without sac growth, severe renal impairment.
Relative: Complex vascular anatomy, history of failed embolisation.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, DSA; lab tests for renal function and coagulation.
________________________________________
7. Procedure
•	Options include transarterial embolisation and direct sac embolisation.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Indicated for persistent, growing Type II endoleaks.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating BCS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	BCS is due to hepatic venous outflow obstruction.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic BCS with hepatic venous outflow obstruction.
________________________________________
5. Contraindications
Absolute: Decompensated liver failure, active infection, severe coagulopathy.
Relative: Massive hepatomegaly, extensive thrombosis, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	Doppler US, CT/MR venography, DSA; lab tests for LFTs and renal function.
________________________________________
7. Procedure
•	Options include angioplasty, stenting, thrombolysis, and TIPS.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging and liver function monitoring.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for BCS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of PVT.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PVT results in impaired portal flow and portal hypertension.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic PVT with complications.
________________________________________
5. Contraindications
Absolute: End-stage liver failure, active GI bleeding, uncorrectable coagulopathy.
Relative: Extensive portal occlusion, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, DSA; lab tests for LFTs and coagulation.
________________________________________
7. Procedure
•	Options include CDT, mechanical thrombectomy, TIPS, and stenting.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1 week, 3 months, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for symptomatic PVT.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Central Venous Stenosis and Occlusion": r"""
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion
Authors: Raman Uberoi, Alessandro Napoli, Thomas Rand, Marc Sapoval, Robert A. Lookstein, Miltiadis Krokidis
________________________________________
1. Introduction
•	Provides best practices for treating central venous stenosis and occlusion.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Central venous stenosis is common in dialysis and cancer patients.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic venous hypertension, access dysfunction.
________________________________________
5. Contraindications
Absolute: Active sepsis, uncorrectable coagulopathy, severe right heart dysfunction.
Relative: Extensive thrombosis, short life expectancy.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Venous access via femoral or jugular vein; balloon angioplasty and stenting.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; 1-year patency: 70–85%.
________________________________________
10. Level of Evidence
•	Based on long-term imaging follow-up.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion – Raman Uberoi et al.
""",
    
    "Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular revascularization in CMI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	CMI is due to mesenteric artery stenosis, commonly from atherosclerosis.
________________________________________
4. Indications for Endovascular Therapy
•	Severe symptomatic CMI with ≥70% stenosis.
________________________________________
5. Contraindications
Absolute: Acute mesenteric ischemia, severe aortic disease, uncorrectable coagulopathy.
Relative: Heavy calcification, multivessel disease.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex US, DSA; lab tests.
________________________________________
7. Procedure
•	Vascular access; stent placement in the mesenteric arteries.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular stenting is first-line for symptomatic CMI.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Peripheral Arterial Disease (PAD)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of PAD.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PAD results from atherosclerosis and is classified by Rutherford scales.
________________________________________
4. Indications for Endovascular Therapy
•	Lifestyle-limiting claudication and critical limb ischemia.
________________________________________
5. Contraindications
Absolute: Severe calcification, extensive occlusion, uncorrectable coagulopathy.
Relative: Severe renal impairment, heavily thrombotic lesions, severe limb infection.
________________________________________
6. Pre-Procedural Workup
•	CTA (gold standard), Doppler ultrasound, and DSA.
•	Laboratory tests: Renal function, coagulation profile.
________________________________________
7. Procedure
•	Vascular access via common femoral (or radial) artery.
•	Techniques: Balloon angioplasty, stenting, atherectomy, and drug-coated balloons.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Antiplatelet therapy; follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%; 1-year primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	First-line treatment for PAD.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of ALI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	ALI is a vascular emergency due to sudden arterial occlusion.
________________________________________
4. Indications for Endovascular Therapy
•	For Rutherford IIa-IIb ALI.
________________________________________
5. Contraindications
Absolute: Rutherford III, active bleeding, severe coagulopathy.
Relative: High thrombus burden, multilevel disease.
________________________________________
6. Pre-Procedural Workup
•	CTA, Doppler ultrasound, DSA; lab tests.
________________________________________
7. Procedure
•	Techniques: CDT, mechanical thrombectomy, aspiration thrombectomy, stenting.
________________________________________
8. Post-Procedural Care
•	Monitor for reperfusion injury; anticoagulation; follow-up ultrasound.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; 1-year limb salvage ~80%.
________________________________________
10. Level of Evidence
•	ALI endovascular treatment is first-line.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating RAS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	RAS is due to atherosclerosis or fibromuscular dysplasia leading to hypertension and CKD.
________________________________________
4. Indications for Endovascular Therapy
•	Severe RAS (>70%) with resistant hypertension or declining renal function.
________________________________________
5. Contraindications
Absolute: Well-controlled RAS; ESRD.
Relative: Heavy calcification, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, MRA; lab tests.
________________________________________
7. Procedure
•	For FMD: PTA alone; for atherosclerotic lesions: stenting with balloon-expandable stents.
________________________________________
8. Post-Procedural Care
•	Monitor renal function and blood pressure; antiplatelet therapy.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; improvement in BP in ~50–70%.
________________________________________
10. Level of Evidence
•	Indicated for severe, symptomatic RAS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for managing persistent Type II endoleaks post-EVAR.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Type II endoleaks result from retrograde flow from collateral arteries.
________________________________________
4. Indications for Endovascular Therapy
•	Aneurysm sac expansion >5 mm in 6 months or persistent endoleak beyond 12 months.
________________________________________
5. Contraindications
Absolute: Stable endoleaks without sac growth; severe renal impairment.
Relative: Complex anatomy; history of failed embolisation.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, DSA; lab tests.
________________________________________
7. Procedure
•	Transarterial and/or direct sac embolisation techniques.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Indicated for persistent, growing Type II endoleaks.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating BCS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	BCS is hepatic venous outflow obstruction causing liver congestion.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic BCS with hepatic venous outflow obstruction.
________________________________________
5. Contraindications
Absolute: Decompensated liver failure, active infection, severe coagulopathy.
Relative: Massive hepatomegaly, extensive thrombosis, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	Doppler US, CT/MR venography, DSA; lab tests.
________________________________________
7. Procedure
•	Options include angioplasty, stenting, thrombolysis, and TIPS.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor liver function and follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for BCS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of PVT.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PVT results in impaired portal flow and portal hypertension.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic acute or chronic PVT with complications.
________________________________________
5. Contraindications
Absolute: End-stage liver failure, active GI bleeding, uncorrectable coagulopathy.
Relative: Extensive portal occlusion, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Options include CDT, mechanical thrombectomy, TIPS, and stent placement.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1 week, 3 months, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for symptomatic PVT.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Central Venous Stenosis and Occlusion": r"""
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion
Authors: Raman Uberoi, Alessandro Napoli, Thomas Rand, Marc Sapoval, Robert A. Lookstein, Miltiadis Krokidis
________________________________________
1. Introduction
•	Provides best practices for treating central venous stenosis and occlusion.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Central venous stenosis is common in dialysis and cancer patients.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic venous hypertension and access dysfunction.
________________________________________
5. Contraindications
Absolute: Active sepsis, uncorrectable coagulopathy, severe right heart dysfunction.
Relative: Extensive thrombosis, short life expectancy.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Access via femoral or jugular vein; balloon angioplasty and stenting.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; 1-year patency: 70–85%.
________________________________________
10. Level of Evidence
•	Based on long-term follow-up.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion – Raman Uberoi et al.
""",
    
    "Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular revascularization in CMI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	CMI is due to mesenteric artery stenosis from atherosclerosis.
________________________________________
4. Indications for Endovascular Therapy
•	Severe symptomatic CMI with ≥70% stenosis.
________________________________________
5. Contraindications
Absolute: Acute mesenteric ischemia, severe aortic disease, uncorrectable coagulopathy.
Relative: Heavy calcification, multivessel disease.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex US, DSA; lab tests.
________________________________________
7. Procedure
•	Stent placement in mesenteric arteries via endovascular approach.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular stenting is first-line for symptomatic CMI.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Peripheral Arterial Disease (PAD)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of PAD.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PAD results from atherosclerosis; classified using Rutherford scales.
________________________________________
4. Indications for Endovascular Therapy
•	Lifestyle-limiting claudication and critical limb ischemia.
________________________________________
5. Contraindications
Absolute: Severe calcification, extensive occlusion, uncorrectable coagulopathy.
Relative: Severe renal impairment, heavily thrombotic lesions, limb infection.
________________________________________
6. Pre-Procedural Workup
•	CTA, Doppler US, DSA; lab tests for renal and coagulation status.
________________________________________
7. Procedure
•	Techniques include balloon angioplasty, stenting, atherectomy, and drug-coated balloon therapy.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Antiplatelet therapy and follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%; 1-year primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for PAD.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of ALI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	ALI is an emergency caused by sudden arterial occlusion.
________________________________________
4. Indications for Endovascular Therapy
•	For Rutherford IIa-IIb ALI.
________________________________________
5. Contraindications
Absolute: Rutherford III, active bleeding, severe coagulopathy.
Relative: High thrombus burden, multilevel disease.
________________________________________
6. Pre-Procedural Workup
•	CTA, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Includes CDT, mechanical thrombectomy, aspiration thrombectomy, and stenting.
________________________________________
8. Post-Procedural Care
•	Monitor for reperfusion injury; continue anticoagulation; follow-up ultrasound.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; 1-year limb salvage: ~80%.
________________________________________
10. Level of Evidence
•	ALI endovascular therapy is first-line.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating RAS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	RAS is caused by atherosclerosis or FMD, leading to secondary hypertension and CKD.
________________________________________
4. Indications for Endovascular Therapy
•	Severe RAS (>70%) with resistant hypertension or deteriorating renal function.
________________________________________
5. Contraindications
Absolute: RAS with stable function; ESRD.
Relative: Heavy calcification, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, MRA; lab tests.
________________________________________
7. Procedure
•	For FMD: PTA alone; for atherosclerosis: stenting with balloon-expandable stents.
________________________________________
8. Post-Procedural Care
•	Monitor renal function and blood pressure; maintain antiplatelet therapy.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; BP improvement in ~50–70%.
________________________________________
10. Level of Evidence
•	Indicated for severe, symptomatic RAS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for managing persistent Type II endoleaks after EVAR.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Type II endoleaks occur from retrograde flow from collateral arteries.
________________________________________
4. Indications for Endovascular Therapy
•	Aneurysm sac expansion >5 mm in 6 months or persistent endoleak beyond 12 months.
________________________________________
5. Contraindications
Absolute: Stable endoleaks without sac growth; severe renal impairment.
Relative: Complex vascular anatomy; history of failed embolisation.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, DSA; lab tests.
________________________________________
7. Procedure
•	Options include transarterial embolisation and direct sac embolisation.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Indicated for persistent, growing Type II endoleaks.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of BCS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	BCS is due to hepatic venous outflow obstruction.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic BCS with hepatic venous outflow obstruction.
________________________________________
5. Contraindications
Absolute: Decompensated liver failure, active infection, severe coagulopathy.
Relative: Massive hepatomegaly, extensive thrombosis, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	Doppler US, CT/MR venography, DSA; lab tests.
________________________________________
7. Procedure
•	Includes angioplasty, stenting, thrombolysis, and TIPS.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor liver function and follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for BCS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of PVT.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PVT leads to impaired portal flow and portal hypertension.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic PVT with complications.
________________________________________
5. Contraindications
Absolute: End-stage liver failure, active GI bleeding, uncorrectable coagulopathy.
Relative: Extensive occlusion, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Options: CDT, mechanical thrombectomy, TIPS, stent placement.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1 week, 3 months, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for symptomatic PVT.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Central Venous Stenosis and Occlusion": r"""
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion
Authors: Raman Uberoi, Alessandro Napoli, Thomas Rand, Marc Sapoval, Robert A. Lookstein, Miltiadis Krokidis
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of central venous stenosis/occlusion.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Central venous stenosis is common in dialysis and cancer patients.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic venous hypertension and access dysfunction.
________________________________________
5. Contraindications
Absolute: Active sepsis, uncorrectable coagulopathy, severe right heart dysfunction.
Relative: Extensive thrombosis, short life expectancy.
________________________________________
6. Pre-Procedural Workup
•	CT/MR venography, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Access via femoral or jugular vein; balloon angioplasty and stenting.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; 1-year patency: 70–85%.
________________________________________
10. Level of Evidence
•	Based on long-term follow-up.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion – Raman Uberoi et al.
""",
    
    "Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular revascularization in CMI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	CMI is due to mesenteric artery stenosis from atherosclerosis.
________________________________________
4. Indications for Endovascular Therapy
•	Severe symptomatic CMI with ≥70% stenosis.
________________________________________
5. Contraindications
Absolute: Acute mesenteric ischemia, severe aortic disease, uncorrectable coagulopathy.
Relative: Heavy calcification, multivessel disease.
________________________________________
6. Pre-Procedural Workup
•	CT Angiography, Duplex US, DSA; lab tests.
________________________________________
7. Procedure
•	Stent placement in mesenteric arteries.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; primary patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular stenting is first-line for symptomatic CMI.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Peripheral Arterial Disease (PAD)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of PAD.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	PAD results from atherosclerosis and is classified using Rutherford scales.
________________________________________
4. Indications for Endovascular Therapy
•	Lifestyle-limiting claudication and critical limb ischemia.
________________________________________
5. Contraindications
Absolute: Severe calcification, extensive occlusion, uncorrectable coagulopathy.
Relative: Severe renal impairment, heavily thrombotic lesions, limb infection.
________________________________________
6. Pre-Procedural Workup
•	CTA, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Vascular access and revascularization techniques (balloon angioplasty, stenting, atherectomy, DCB).
________________________________________
8. Post-Procedural Care & Follow-Up
•	Antiplatelet therapy and follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%; 1-year patency: 70–85%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for PAD.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for endovascular treatment of ALI.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	ALI is a vascular emergency due to sudden arterial occlusion.
________________________________________
4. Indications for Endovascular Therapy
•	For Rutherford IIa-IIb ALI.
________________________________________
5. Contraindications
Absolute: Rutherford III, active bleeding, severe coagulopathy.
Relative: High thrombus burden, multilevel disease.
________________________________________
6. Pre-Procedural Workup
•	CTA, Doppler US, DSA; lab tests.
________________________________________
7. Procedure
•	Techniques include CDT, mechanical thrombectomy, aspiration thrombectomy, and stenting.
________________________________________
8. Post-Procedural Care
•	Monitor for reperfusion injury; anticoagulation; follow-up ultrasound.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–95%; 1-year limb salvage: ~80%.
________________________________________
10. Level of Evidence
•	ALI endovascular therapy is first-line.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for treating RAS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	RAS is caused by atherosclerosis or FMD, leading to secondary hypertension and CKD.
________________________________________
4. Indications for Endovascular Therapy
•	Severe RAS (>70%) with resistant hypertension or declining renal function.
________________________________________
5. Contraindications
Absolute: RAS with stable controlled hypertension; ESRD.
Relative: Heavy calcification, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, MRA; lab tests.
________________________________________
7. Procedure
•	For FMD: PTA alone; for atherosclerotic lesions: stenting with balloon-expandable stents.
________________________________________
8. Post-Procedural Care
•	Monitor renal function and blood pressure; antiplatelet therapy.
________________________________________
9. Outcomes & Complications
•	Technical success: 95–98%; BP improvement in ~50–70%.
________________________________________
10. Level of Evidence
•	Indicated for severe, symptomatic RAS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli et al.
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for managing persistent Type II endoleaks after EVAR.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	Type II endoleaks occur from retrograde flow from collateral arteries.
________________________________________
4. Indications for Endovascular Therapy
•	Aneurysm sac expansion >5 mm in 6 months or persistent endoleak beyond 12 months.
________________________________________
5. Contraindications
Absolute: Stable endoleaks without sac growth; severe renal impairment.
Relative: Complex anatomy; history of failed embolisation.
________________________________________
6. Pre-Procedural Workup
•	CTA, Duplex US, DSA; lab tests.
________________________________________
7. Procedure
•	Options include transarterial embolisation and direct sac embolisation.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Follow-up imaging at 1, 3, and 6 months.
________________________________________
9. Outcomes & Complications
•	Technical success: 85–95%.
________________________________________
10. Level of Evidence
•	Indicated for persistent, growing Type II endoleaks.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of BCS.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
•	BCS is due to hepatic venous outflow obstruction.
________________________________________
4. Indications for Endovascular Therapy
•	Symptomatic BCS with hepatic venous outflow obstruction.
________________________________________
5. Contraindications
Absolute: Decompensated liver failure, active infection, severe coagulopathy.
Relative: Massive hepatomegaly, extensive thrombosis, severe renal dysfunction.
________________________________________
6. Pre-Procedural Workup
•	Doppler US, CT/MR venography, DSA; lab tests.
________________________________________
7. Procedure
•	Includes angioplasty, stenting, thrombolysis, and TIPS.
________________________________________
8. Post-Procedural Care & Follow-Up
•	Monitor liver function and follow-up imaging.
________________________________________
9. Outcomes & Complications
•	Technical success: 90–98%.
________________________________________
10. Level of Evidence
•	Endovascular therapy is first-line for BCS.
________________________________________
11. Citation
CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli et al.
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)
Authors: Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping
________________________________________
1. Introduction
•	Provides best practices for the endovascular treatment of PVT.
________________________________________
2. Methods
•	Literature review from 2010–2022.
________________________________________
3. Background
