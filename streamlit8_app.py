import streamlit as st

# Custom CSS for colors and styling
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

# Title and subtitle
st.title("CIRSE Standards of Practice Pocket Guide")
st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)

st.markdown("""
Welcome to the CIRSE Standards of Practice Pocket Guide.  
This guide provides structured summaries of various CIRSE Standards of Practice documents for interventional procedures.  
Select an intervention from the sidebar to view its detailed information.
""")

# Define documents as a dictionary with embedded multi-line strings
documents = {
    "Bronchial Artery Embolisation": r"""
**CIRSE Standards of Practice on Bronchial Artery Embolisation**  
**Authors:** Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos  
________________________________________
### 1. Introduction
- Bronchial artery embolisation (BAE) is a minimally invasive, life-saving procedure used to treat haemoptysis (coughing up blood).
- The CIRSE Standards of Practice provide best practices to optimize safety and efficacy in performing BAE.
- This document does not impose a strict standard but provides evidence-based recommendations for interventional radiologists.

________________________________________
### 2. Methods
- **Writing Group:** Five internationally recognized experts in BAE.
- **Literature Review:**
  - Timeframe: 1974–2021.
  - Source: PubMed database.
  - Consensus-Based Recommendations.

________________________________________
### 3. Background
- Haemoptysis is a life-threatening respiratory emergency, with a mortality rate of 50–100% if left untreated.
- Death is usually due to asphyxiation, not exsanguination.
- When timely and optimal diagnosis and treatment are provided, the mortality rate drops to <20%.
  
**Etiology of Haemoptysis**
- 90% of massive haemoptysis cases arise from the bronchial circulation.
- 5% arise from the pulmonary circulation.
- 5% arise from non-bronchial systemic circulations.

**Common Causes of Haemoptysis**
- Tuberculosis (TB)
- Lung cancer
- Chronic lung diseases (bronchiectasis, cystic fibrosis, chronic pulmonary aspergillosis)
- Pulmonary arteriovenous malformations (PAVMs)

**Global Variations**
- In Western countries: 80% of haemoptysis cases are due to lung cancer, TB, bronchiectasis, and aspergillosis.
- In India and Turkey: Tuberculosis is responsible for 60–90% of cases.

________________________________________
### 4. Indications for BAE
- Life-threatening haemoptysis (severe or massive).
- Recurrent haemoptysis despite medical therapy.
- Bridge therapy for lung transplant candidates with chronic inflammatory lung diseases.
- Index bleeding: Initial minor bleeding episodes that may precede massive haemoptysis.

________________________________________
### 5. Contraindications
**Absolute Contraindications**
- Embolization of arteries that supply the spinal cord, brain, or heart (risk of ischemia).

**Relative Contraindications**
- Severe contrast allergy.
- Coagulopathy (must be corrected before the procedure).
- Renal insufficiency (careful contrast use required).

________________________________________
### 6. Pre-Procedural Preparation
**Clinical Work-Up**
- Confirm that the bleeding is from the lungs.
- Assess the severity and rule out non-pulmonary sources (e.g., gastrointestinal, nasopharyngeal).
- Review patient history, including previous haemoptysis episodes, infections, malignancies, and lung disease.
- Optimize coagulation parameters before intervention.

**Imaging**
- **First-Line Imaging:**  
  Computed tomography angiography (CTA) is the gold standard for localizing the bleeding source. It identifies the culprit artery, rules out alternative diagnoses, and helps plan catheterization.
- **Additional Imaging:**  
  Chest X-ray (initial screening, low sensitivity), flexible bronchoscopy (helps clear the airway but has limitations in localizing distal sources), and digital subtraction angiography (DSA; essential for vessel selection and embolization).

________________________________________
### 7. Procedure: Bronchial Artery Embolisation (BAE)
**Access & Catheterization**
- Preferred access: Femoral artery (retrograde approach).
- Diagnostic catheter: 4–5 Fr standard catheter for initial evaluation.
- Superselective catheterization:
  - Microcatheter (2.7 Fr or smaller) for precise embolization.
  - Avoid non-target embolization by sparing arteries that supply critical structures.
  
**Embolization Agents**
- **Preferred:** Polyvinyl alcohol (PVA) particles (300–500 µm)
- **Alternatives:**  
  - N-butyl-2-cyanoacrylate (NBCA) glue (for high-flow fistulas).  
  - Coils (used selectively).

**Technique**
1. Confirm the target vessel via angiography.
2. Slowly infuse embolic material until stasis is achieved.
3. Avoid reflux to prevent non-target embolization.
4. Perform post-embolization angiography to confirm treatment success.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- **Immediate Post-Procedure Monitoring:**  
  - Observe for recurrence of haemoptysis (hospitalization if required).
  - Monitor oxygen saturation and airway patency.
- **Long-Term Follow-Up:**  
  - Repeat CTA or bronchoscopy if haemoptysis recurs.
  - Additional embolization may be required in 10–30% of cases due to recanalization.

________________________________________
### 9. Outcomes & Complications
**Technical Success Rate**
- 85–98% initial success rate with embolization.

**Rebleeding Rates**
- 10–30% rebleeding within 6 months, often due to incomplete embolization, collateral vessel formation, or progression of underlying disease.

**Complications**
- *Mild:* Transient chest pain (due to ischemia).
- *Severe (Rare but Serious):*  
  - Spinal cord ischemia (from inadvertent embolization of spinal arteries).  
  - Bronchial infarction (rare).  
  - Non-target embolization (stroke, myocardial infarction, bowel ischemia).

________________________________________
### 10. Level of Evidence
- Level 1: CTA is the first-line imaging modality for evaluating haemoptysis.
- Level 2: PVA particles (300–500 µm) are the preferred embolic agent for BAE.
- Level 3: BAE should be considered as a bridge therapy for lung transplant candidates.

________________________________________
### 11. Summary
- BAE is a highly effective, minimally invasive treatment for life-threatening and recurrent haemoptysis.
- CTA is essential for pre-procedural planning.
- Embolization with PVA particles is the preferred method, although alternatives (coils, glue) exist.
- Success rates are high, but rebleeding can occur, requiring repeat intervention.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Bronchial Artery Embolisation**  
*Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos*
________________________________________
""",
    
    "Arterial Access for Interventions": r"""
**CIRSE Standards of Practice on Arterial Access for Interventions**  
**Authors:** Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for safe and effective arterial access in interventional radiology.
- Scope:  
  - Covers common femoral, radial, and brachial artery access.
  - Addresses imaging, technique, and complication management.
- Clinical Importance:  
  - Arterial access is the foundation of endovascular interventions, and complications at the access site can significantly impact outcomes.

________________________________________
### 2. Methods
- Writing Group: Six experts in arterial interventions.
- Literature Review:  
  - Evidence search performed via PubMed (2002–2019).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- Arterial access is critical for many endovascular procedures, influencing procedural success and patient recovery.
- Evolution:  
  - Historically, translumbar aortography was used.
  - Ultrasound guidance has dramatically reduced complications.
  - Radial access is gaining popularity due to lower bleeding risks.

________________________________________
### 4. Indications
- Peripheral vascular interventions (angioplasty, stenting).
- Tumor embolization.
- Emergency embolization (e.g., GI bleeding, trauma).
- Prostatic artery embolization (PAE).
- Endovascular aortic repair (EVAR).

________________________________________
### 5. Contraindications
**Absolute Contraindications:**  
- Severe atherosclerosis or occlusion at the intended access site.
- Active infection at the puncture site.
- Uncontrollable coagulopathy.

**Relative Contraindications:**  
- Severe obesity (affecting femoral access).
- Radial artery anomalies.
- Patients on high-dose anticoagulants (may need adjustment).

________________________________________
### 6. Pre-Procedural Preparation
- **Patient Work-up:**  
  - History and physical examination to assess prior procedures and access site suitability.
- **Imaging:**  
  - Ultrasound guidance is recommended for all arterial access.
  - CTA/MRA for complex cases.
- **Anticoagulation Management:**  
  - Consider holding anticoagulants based on patient risk.

________________________________________
### 7. Procedure
**Common Femoral Artery (CFA) Access:**  
- Gold standard for large-bore access (e.g., EVAR).
- Puncture 1–2 cm below the inguinal ligament under ultrasound guidance.
- Use micropuncture technique.
- Complications: Hematoma, pseudoaneurysm, retroperitoneal bleeding.

**Radial Artery Access:**  
- Lower bleeding risk.
- Assess collateral circulation (Allen’s or Barbeau’s test).
- Puncture 2 cm proximal to the wrist crease; use 5–6 Fr sheaths.
- Complications: Radial occlusion, spasm.

**Brachial Artery Access:**  
- Used when CFA and radial are not feasible.
- Higher risk of nerve damage and thrombosis.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Use manual compression or closure devices for hemostasis.
- Monitor for complications (bleeding, ischemia, pseudoaneurysm).
- For radial access, use a compression device for 2–3 hours.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Femoral access: >95% with ultrasound guidance.  
  - Radial access: Low bleeding risk but higher spasm rates.
- **Complications:**  
  - Bleeding: Femoral (3–7%), Radial (<1%).  
  - Pseudoaneurysm formation is more common in femoral access.

________________________________________
### 10. Level of Evidence
- Level 1: Ultrasound guidance is recommended.
- Level 2: Radial access offers lower bleeding risks.
- Level 3: Closure devices reduce hemostasis time but have associated risks.

________________________________________
### 11. Summary
- Arterial access is essential for endovascular procedures.
- Ultrasound guidance improves success and reduces complications.
- Radial access is safer for many procedures but is limited by vessel size.
- Proper patient selection and anticoagulation management are crucial.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Arterial Access for Interventions**  
*Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef*
________________________________________
""",
    
    "Varicocele Embolisation": r"""
**CIRSE Standards of Practice on Varicocele Embolisation**  
**Authors:** Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for percutaneous varicocele embolization.
- Scope:  
  - Covers indications, contraindications, procedural steps, complications, and follow-up.
  - Intended for interventional radiologists and urologists.
- Clinical Importance:  
  - A minimally invasive alternative to surgical ligation with comparable success and lower morbidity.

________________________________________
### 2. Methods
- Writing Group: Five internationally recognized experts.
- Literature Review:  
  - PubMed search (2006–2021).
  - Expert consensus-based recommendations.

________________________________________
### 3. Background
- Definition: Varicocele is the abnormal dilation of testicular veins in the pampiniform plexus with venous reflux.
- Epidemiology:  
  - Affects 15% of adult males; up to 35–50% in cases of primary infertility.
  - Higher prevalence in adolescents (15%) than in prepubescents (<1%).
- Pathophysiology: Due to venous hypertension, increased testicular temperature, and oxidative stress.
- Indications: Infertility, testicular hypotrophy, scrotal pain, and cosmetic concerns.

________________________________________
### 4. Indications for Embolization
- Varicocele-related infertility.
- Testicular hypotrophy in adolescents.
- Persistent scrotal pain unresponsive to conservative management.
- Cosmetic concerns.
- Recurrent varicocele after surgery.

________________________________________
### 5. Contraindications
**Absolute Contraindications:**  
- Allergy to contrast agents.
- Severe uncorrectable coagulopathy.

**Relative Contraindications:**  
- Renal insufficiency.
- Bilateral varicocele requiring a complex approach.

________________________________________
### 6. Pre-Procedural Preparation
- **Patient Evaluation:**  
  - Physical exam using the Valsalva maneuver; grading of varicocele severity.
- **Imaging Work-up:**  
  - Scrotal ultrasound (gold standard) and Doppler ultrasound for reflux confirmation and testicular volume.
- **Laboratory Tests:**  
  - Coagulation profile and renal function.

________________________________________
### 7. Procedure: Percutaneous Varicocele Embolisation
- **Access:** Preferred via right femoral or jugular vein.
- **Technique:**  
  1. Venography to confirm reflux and identify collaterals.
  2. Superselective catheterization of the internal spermatic vein (ISV) with a microcatheter.
  3. Embolization using coils, sclerosing agents, or NBCA glue.
  4. Post-embolization venography to confirm occlusion.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Immediate monitoring for pain, allergic reactions, or coil migration.
- Follow-up: Clinical exam at 1–3 months; repeat Doppler ultrasound at 3–6 months.
- Patient counseling regarding mild post-procedural pain and recurrence risk (5–10%).

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Technical success: 85–95%.  
  - Clinical success: 70–90% improvement.
- **Complications:**  
  - Mild: Scrotal pain, post-embolization syndrome.
  - Moderate: Rare coil migration, persistent reflux.
  - Severe: Non-target embolization and testicular atrophy (very rare).

________________________________________
### 10. Level of Evidence
- Level 1: Scrotal ultrasound is the gold standard.
- Level 2: Embolization is as effective as surgery with fewer complications.
- Level 3: Coils are the preferred embolic material.

________________________________________
### 11. Summary & Key Takeaways
- Varicocele embolization is a safe, minimally invasive alternative to surgery.
- Essential imaging and follow-up ensure long-term success.
- Recurrence is low with proper technique.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Varicocele Embolisation**  
*Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi*
________________________________________
""",
    
    "Oesophageal and Gastroduodenal Stenting": r"""
**CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting**  
**Authors:** Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for placing self-expanding stents in the oesophagus and gastroduodenal tract.
- Scope:  
  - Covers indications, contraindications, technical aspects, and post-procedural care.
  - Applies to both malignant and benign strictures.
- Clinical Importance:  
  - Effective palliative treatment for dysphagia and gastric outlet obstruction.
  - Provides immediate symptom relief and improves quality of life.

________________________________________
### 2. Methods
- Writing Group: Five experts in gastrointestinal stenting.
- Literature Review:  
  - PubMed search (2005–2021).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- Definition: Placement of self-expanding metal stents (SEMS) to relieve obstruction.
- Epidemiology:  
  - Oesophageal cancer is a major cause of cancer death.
  - Gastric outlet obstruction (GOO) affects 15–35% of patients with gastric or pancreatic cancer.
- Pathophysiology:  
  - Malignant strictures cause progressive dysphagia.
  - Benign strictures may result from peptic disease, surgery, or radiation.

________________________________________
### 4. Indications for Stenting
**Oesophageal Stenting:**
- Malignant strictures.
- Tracheo-oesophageal fistulas.
- Benign strictures refractory to balloon dilation.

**Gastroduodenal Stenting:**
- Gastric outlet obstruction due to malignancy.
- Palliation in patients unsuitable for surgery.
- Benign strictures unresponsive to dilation.

________________________________________
### 5. Contraindications
**Absolute Contraindications:**  
- Perforation or fistula not amenable to stenting.
- Severe bleeding requiring surgical intervention.
- Obstructions unsuitable for stenting (e.g., multiple stenoses).

**Relative Contraindications:**  
- Severe coagulopathy.
- High risk of stent migration in benign strictures.
- Poor prognosis.

________________________________________
### 6. Pre-Procedural Preparation
- **Patient Evaluation:**  
  - Assess dysphagia, weight loss, and nutritional status.
  - Endoscopic evaluation to confirm stenosis details.
- **Imaging:**  
  - CT scan with contrast; fluoroscopy for guidance.
- **Laboratory Tests:**  
  - Coagulation profile and renal function.

________________________________________
### 7. Procedure: Stent Placement
- **Access & Positioning:**  
  - Oesophageal: Supine; Gastroduodenal: Supine or left lateral decubitus.
- **Guidewire Placement:**  
  - Under fluoroscopic/endoscopic guidance.
- **Stent Deployment:**  
  - Deploy SEMS across the stricture; balloon dilation may be used.
- **Special Considerations:**  
  - Covered stents for TEFs.
  - Precise placement in pyloric obstruction.
  - Caution in benign strictures due to granulation tissue risk.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- **Immediate Monitoring:**  
  - Assess for pain, stent migration, and aspiration risk.
  - Initiate soft diet after 24 hours.
- **Follow-Up Imaging:**  
  - Fluoroscopy/endoscopy at 1–2 weeks if symptoms persist.
- **Long-Term:**  
  - Stent removal for benign strictures; palliative follow-up for malignancies.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Technical: 95–99%.  
  - Clinical: 75–90% symptom relief.
- **Complications:**  
  - Mild: Chest pain, transient dysphagia.
  - Moderate: Stent migration, tumor overgrowth.
  - Severe: Aspiration pneumonia, perforation, massive bleeding.

________________________________________
### 10. Level of Evidence
- Level 1: SEMS are the first-line treatment for malignant dysphagia.
- Level 2: Combined endoscopic and fluoroscopic guidance improves accuracy.
- Level 3: Stenting for benign strictures should be reserved for refractory cases.

________________________________________
### 11. Summary & Key Takeaways
- Oesophageal and gastroduodenal stenting is an effective palliative intervention.
- SEMS provide immediate relief.
- CT and endoscopy are essential for planning and follow-up.
- Complications are manageable.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting**  
*Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal*
________________________________________
""",
    
    "Peri-Operative Anticoagulation Management During IR Procedures": r"""
**CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During Interventional Radiology Procedures**  
**Authors:** Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for peri-operative anticoagulation management during IR procedures.
- Scope:  
  - Guidance for managing anticoagulation in IR patients.
  - Balances bleeding and thromboembolic risks.
- Clinical Importance:  
  - Critical due to complex decision-making in patients on anticoagulation.

________________________________________
### 2. Methods
- Writing Group: Clinicians with expertise in IR and hematology.
- Literature Review:  
  - Comprehensive search in PubMed and Cochrane Library.
- Consensus Development:  
  - Delphi process achieving 80% agreement among experts.

________________________________________
### 3. Background
- Management is challenging due to procedure complexity and patient comorbidities.
- Balances bleeding risk (procedure and patient factors) with thrombosis risk.

________________________________________
### 4. Indications for Anticoagulation in IR Patients
- Atrial fibrillation, VTE prophylaxis, mechanical heart valves.
- Recent MI or PAD.
- Hypercoagulable states.

________________________________________
### 5. Contraindications to Anticoagulation in IR
**Absolute Contraindications:**  
- Active major bleeding.
- Recent intracranial hemorrhage.
- Severe uncontrolled hypertension.
- Severe thrombocytopenia (<50,000/µL).

**Relative Contraindications:**  
- High bleeding risk procedures.
- Coagulation disorders.
- Recent major surgery.

________________________________________
### 6. Pre-Procedural Coagulation Assessment
- **Structured Bleeding History:**  
  - Evaluate previous bleeding episodes, surgeries, and conditions.
- **Laboratory Testing:**  
  - Coagulation profile (PT/INR, aPTT, fibrinogen, platelets) and point-of-care tests (TEG/ROTEM).

________________________________________
### 7. Anticoagulation Management Based on Procedure Risk
- **Low-Bleeding-Risk:** Continue anticoagulation.
- **Moderate-Bleeding-Risk:** Consider modifying anticoagulation.
- **High-Bleeding-Risk:** Hold anticoagulation temporarily.

________________________________________
### 8. Peri-Procedural Management of Specific Anticoagulants
| Anticoagulant               | Pre-Procedural Holding Time        | Post-Procedural Restart Time        |
|-----------------------------|------------------------------------|-------------------------------------|
| Warfarin (Coumadin)         | 5 days before high-risk procedures | 24–48 hours post-procedure          |
| Heparin (IV infusion)       | 4–6 hours before procedure         | Immediate if low-risk; 24 hours if high-risk |
| LMWH                        | 24 hours before procedure          | 24 hours post-procedure             |
| DOACs                       | 24–48 hours (depends on renal function) | 24 hours post-procedure          |

________________________________________
### 9. Bridging Strategies for High-Thrombotic-Risk Patients
- For high-risk warfarin patients:
  - Stop warfarin 5 days pre-procedure.
  - Start LMWH bridging 3 days pre-procedure.
  - Stop LMWH 24 hours pre-procedure.
  - Resume LMWH/warfarin 24 hours post-procedure.

________________________________________
### 10. Post-Procedural Care & Monitoring
- Monitor for bleeding (serial hemoglobin, INR, platelets).
- Assess for thrombosis recurrence (DVT screening, Doppler ultrasound).
- Gradual reintroduction of anticoagulation for high-risk patients.

________________________________________
### 11. Outcomes & Complications
- **Bleeding Complications:**  
  - Minor: 5–15%  
  - Major (requiring intervention): 1–5%
- **Thromboembolic Events:**  
  - VTE recurrence: 2–10% in high-risk patients  
  - Stroke risk in AF patients off anticoagulation: ~5% per month

________________________________________
### 12. Level of Evidence
- Level 1: Routine coagulation screening is not recommended unless indicated.
- Level 2: Bridging therapy is necessary for high-risk patients on warfarin.
- Level 3: DOACs require dose adjustments in renal impairment.

________________________________________
### 13. Summary & Key Takeaways
- Balancing bleeding vs. thromboembolic risk is critical.
- Routine coagulation testing is not necessary unless clinically indicated.
- Bridging therapy should be reserved for high-risk patients.
- Post-procedural monitoring is essential.

________________________________________
### 14. Citation
**CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During IR Procedures**  
*Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi*
________________________________________
""",
    
    "Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting": r"""
**CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting**  
**Authors:** Marco Das, Christiaan van der Leij, Marcus Katoh, Daniel Benten, Babs M. F. Hendriks, Adam Hatzidakis  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for PTC, PTBD, and PTBS.
- Scope:  
  - Covers indications, contraindications, techniques, complications, and follow-up.
  - Intended for interventional radiologists and hepatobiliary specialists.
- Clinical Importance:  
  - Critical for managing biliary obstruction, especially when ERC is unsuccessful.

________________________________________
### 2. Methods
- Writing Group: Six experts in hepatobiliary interventions.
- Literature Review:  
  - PubMed search (2000–2021).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- **PTC:** Fluoroscopic visualization of the biliary system.
- **PTBD:** For biliary obstruction due to malignancy, strictures, or post-surgical complications.
- **PTBS:** Maintains long-term biliary drainage.
- Etiologies include malignancies, benign strictures, and gallstones.

________________________________________
### 4. Indications for PTC, PTBD, and PTBS
- **PTC:** For pre-procedural imaging when ERC is contraindicated or unsuccessful.
- **PTBD:** For malignant or benign strictures and cholangitis with failed drainage.
- **PTBS:** To maintain bile flow post-PTBD and for palliative treatment.

________________________________________
### 5. Contraindications
**Absolute:**  
- Severe uncorrectable coagulopathy.
- Massive ascites without drainage control.
- Uncontrolled sepsis.

**Relative:**  
- Liver metastases causing dysfunction.
- Multiple intrahepatic strictures.

________________________________________
### 6. Pre-Procedural Preparation
- **Imaging:** Ultrasound, CT, and MRI/MRCP.
- **Laboratory Tests:** LFTs, coagulation profile.
- **Antibiotic Prophylaxis:** Ceftriaxone + Metronidazole (or equivalent).

________________________________________
### 7. Procedure
**Step 1: PTC**  
- Percutaneous puncture under US/fluoroscopy and contrast injection.
**Step 2: PTBD**  
- Insertion of an 8–12 Fr catheter for external or internal-external drainage.
**Step 3: PTBS**  
- Deployment of SEMS (or plastic stents) under fluoroscopic guidance.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for bleeding, infection, or bile leak.
- Flush the biliary drain daily.
- Follow-up imaging (CT/MRCP) to assess stent patency.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Technical success: 90–95%.
  - >85% improvement in jaundice.
- **Complications:**  
  - Mild: Puncture site pain, transient fever.
  - Moderate: Cholangitis (~5–10%), bile leakage (~5%).
  - Severe: Hemobilia, sepsis, liver abscess.

________________________________________
### 10. Level of Evidence
- Level 1: PTBD is the standard when ERC fails.
- Level 2: SEMS are preferred for malignant cases.
- Level 3: Antibiotic prophylaxis is recommended in all cases.

________________________________________
### 11. Summary & Key Takeaways
- PTBD and PTBS are essential techniques for biliary obstruction.
- SEMS are preferred in malignant obstructions.
- Complications are manageable.
- Follow-up imaging is crucial.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting**  
*Marco Das, Christiaan van der Leij, Marcus Katoh, Daniel Benten, Babs M. F. Hendriks, Adam Hatzidakis*
________________________________________
""",
    
    "Below-the-Knee Revascularisation": r"""
**CIRSE Standards of Practice on Below-the-Knee Revascularisation**  
**Authors:** Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for BTK revascularisation.
- Scope:  
  - Covers indications, contraindications, technical aspects, outcomes, and follow-up.
  - Focus on endovascular treatment for chronic limb-threatening ischemia (CLTI).
- Clinical Importance:  
  - Infra-popliteal arterial disease is a major cause of limb loss.
  - Endovascular interventions improve limb salvage and wound healing.

________________________________________
### 2. Methods
- Writing Group: Six experts in peripheral arterial disease.
- Literature Review:  
  - PubMed search (2004–2020).
  - Consensus agreement.

________________________________________
### 3. Background
- Affects diabetics, dialysis patients, and the elderly.
- CLTI is severe PAD with rest pain and non-healing ulcers.
- Goal: Restore perfusion to promote wound healing; endovascular-first approach is preferred.

________________________________________
### 4. Indications for BTK Revascularisation
- Rest pain or non-healing ischemic ulcers.
- Salvage of failing bypass grafts.
- Limb preservation in severe PAD.
- Rapidly progressing diabetic foot ulcers.
- Prevention of major amputation.

________________________________________
### 5. Contraindications
**Absolute:**  
- Severe systemic infection or uncontrolled sepsis.
- Severe renal failure (eGFR <15 mL/min without dialysis).
- No viable target arteries.

**Relative:**  
- Poor functional status or short life expectancy.
- Extensive necrosis.

________________________________________
### 6. Pre-Procedural Assessment
- **Imaging:** Duplex ultrasound, CTA/MRA, DSA.
- **Hemodynamic Testing:** ABI (<0.4), TBI, TcPO2 (<30 mmHg).

________________________________________
### 7. Procedure: BTK Revascularisation
- **Options:**  
  1. Balloon angioplasty (POBA).  
  2. Drug-Coated Balloons (DCB).  
  3. Drug-Eluting Stents (DES).  
  4. Atherectomy for calcified lesions.  
  5. Pedal arch reconstruction.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Antithrombotic therapy: DAPT for 3–6 months, anticoagulation for high-risk patients.
- Monitoring: Doppler ultrasound at 1, 3, and 6 months; angiography if needed.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Technical: ~85–95%.  
  - Clinical: ~70–90%.
- **Complications:**  
  - Mild: Hematoma, transient spasm.
  - Moderate: Stent thrombosis (5–10%), distal embolization (2–5%).
  - Severe: Acute limb ischemia, arterial rupture.

________________________________________
### 10. Level of Evidence
- Level 1: Endovascular-first is the standard in CLTI.
- Level 2: DES offer superior outcomes.
- Level 3: Pedal arch reconstruction is essential.

________________________________________
### 11. Summary & Key Takeaways
- Endovascular-first approach is preferred.
- Balloon angioplasty is standard; DCB and DES improve outcomes.
- Pedal arch reconstruction enhances wound healing.
- DAPT is critical post-procedure.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Below-the-Knee Revascularisation**  
*Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi*
________________________________________
""",
    
    "Hepatic Transarterial Chemoembolisation (TACE)": r"""
**CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE)**  
**Authors:** Pierleone Lucatelli, Marta Burrel, Boris Guiu, Gianluca de Rubeis, Otto van Delden, Thomas Helmberger  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for TACE in hepatic tumors.
- Scope:  
  - Covers indications, contraindications, technical aspects, and post-procedural management.
  - Includes cTACE, DEM-TACE, DSM-TACE, and b-TACE.
- Clinical Importance:  
  - Standard-of-care for unresectable HCC in patients with preserved liver function.
  - Also used in ICC and metastatic liver tumors.

________________________________________
### 2. Methods
- Writing Group: Six experts in interventional oncology.
- Literature Review:  
  - PubMed and EMBASE search (2012–2020).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- TACE delivers chemotherapy directly into the tumor while embolizing its arterial supply.
- **Types of TACE:**  
  1. cTACE: Lipiodol–chemotherapy emulsion + embolization.  
  2. DEM-TACE: Drug-eluting microspheres.
  3. DSM-TACE: Temporary embolization.
  4. b-TACE: Balloon-occluded technique.
- Primarily indicated for HCC; also for ICC and metastatic disease.

________________________________________
### 4. Indications for TACE
- HCC patients with BCLC stage B.
- Non-surgical candidates for liver tumors.
- Palliative treatment for unresectable ICC.
- Metastatic liver tumors.

________________________________________
### 5. Contraindications
**Absolute:**  
- Decompensated liver disease (Child-Pugh C).
- Severe portal vein thrombosis.
- Uncontrolled infection or sepsis.

**Relative:**  
- Bilirubin >3 mg/dL.
- Extensive tumor burden.
- Untreated varices.

________________________________________
### 6. Pre-Procedural Preparation
- **Imaging:** Multiphasic CT or MRI with contrast; ultrasound with Doppler for portal patency.
- **Laboratory:** LFTs, AFP levels.
- **Antibiotic Prophylaxis:** Consider in high-risk patients.

________________________________________
### 7. Procedure: TACE Techniques
- **Step 1:** Vascular access via the common femoral artery.
- **Step 2:** Chemotherapy administration:
  - cTACE: Lipiodol–chemotherapy emulsion followed by embolic agent.
  - DEM-TACE: Drug-eluting microspheres.
- **Step 3:** Embolization with particles (PVA/microspheres); b-TACE may be used.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for post-embolization syndrome.
- Manage pain as needed.
- LFTs at 24–48 hours; follow-up imaging at 1 and 3 months.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Tumor response: 50–70% for HCC.
  - Median overall survival: 20–30 months.
- **Complications:**  
  - Mild: Post-embolization syndrome.
  - Moderate: Cholecystitis, tumor rupture.
  - Severe: Liver failure, hepatic abscess.

________________________________________
### 10. Level of Evidence
- Level 1: TACE is first-line for unresectable HCC with preserved liver function.
- Level 2: DEM-TACE reduces systemic toxicity.
- Level 3: b-TACE improves drug delivery but requires further study.

________________________________________
### 11. Summary & Key Takeaways
- TACE is the standard-of-care for unresectable HCC.
- DEM-TACE offers lower systemic toxicity.
- Post-embolization syndrome is common but manageable.
- Follow-up imaging is essential.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE)**  
*Pierleone Lucatelli, Marta Burrel, Boris Guiu, Gianluca de Rubeis, Otto van Delden, Thomas Helmberger*
________________________________________
""",
    
    "Thermal Ablation of Bone Tumours": r"""
**CIRSE Standards of Practice on Thermal Ablation of Bone Tumours**  
**Authors:** Anthony Ryan, Caoimhe Byrne, Claudio Pusceddu, Xavier Buy, Georgia Tsoumakidou, Dimitrios Filippiadis  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for thermal ablation of bone tumors.
- Scope:  
  - Covers RFA, cryoablation, MWA, and HIFU.
  - Applies to both benign and malignant lesions.
- Clinical Importance:  
  - Minimally invasive technique offering effective pain relief and local tumor control.
  - Serves as an alternative to surgery and radiation therapy.

________________________________________
### 2. Methods
- Writing Group: Six experts in musculoskeletal interventions.
- Literature Review:  
  - PubMed search (2009–2021).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- Thermal ablation is an image-guided treatment for osseous lesions.
- **Indications:**  
  1. Benign bone tumors (e.g., osteoid osteoma).  
  2. Painful bone metastases.  
  3. Selected primary malignant bone tumors.
- **Comparison of Techniques:**

| Technique    | Mechanism                     | Applications                      |
|--------------|-------------------------------|-----------------------------------|
| RFA          | Heat-induced necrosis         | Osteoid osteoma, metastases       |
| MWA          | Faster, deeper heating        | Larger tumors, metastases         |
| Cryoablation | Freezing-induced apoptosis    | Painful metastases, soft tissue tumors |
| HIFU         | Ultrasound-induced damage     | Non-invasive ablation             |

________________________________________
### 4. Indications for Thermal Ablation
- Osteoid osteoma (first-line).
- Bone metastases causing intractable pain.
- Selected primary malignant bone tumors.
- Recurrent tumors post-surgery or radiation.
- Oligometastatic disease when surgery is not feasible.

________________________________________
### 5. Contraindications
**Absolute Contraindications:**  
- Unsafe tumor access.
- Extensive cortical destruction with high fracture risk.
- Severe uncorrectable bleeding disorders.

**Relative Contraindications:**  
- Lesions near neurovascular structures.
- Active infection at the planned entry site.
- Poor prognosis where alternative therapies are preferable.

________________________________________
### 6. Pre-Procedural Preparation
- **Imaging:** CT (preferred), MRI, bone scan/PET-CT.
- **Laboratory Tests:** Coagulation profile, CBC.
- **Anesthesia:** General or conscious sedation.

________________________________________
### 7. Procedure: Thermal Ablation Techniques
- **Step 1:** Patient positioning and anesthesia.
- **Step 2:** Image-guided needle/probe placement.
- **Step 3:** Ablation:
  - RFA: 90–100°C for 5–7 minutes.
  - MWA: >100°C.
  - Cryoablation: Freeze-thaw cycles (-40°C).
  - HIFU: Non-invasive option.
________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for pain relief (typically 48–72 hours for osteoid osteoma).
- Assess for complications (fracture, nerve injury).
- Follow-up imaging (CT/MRI at 3–6 months).

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Osteoid osteoma: 90–95% complete relief.
  - Bone metastases: 70–85% pain reduction.
  - Malignant tumors: 50–70% local control.
- **Complications:**  
  - Mild: Post-procedural pain, minor skin burns.
  - Moderate: Pathologic fractures (~5%), temporary nerve injury.
  - Severe: Infection (~1–2%), persistent tumor growth.

________________________________________
### 10. Level of Evidence
- Level 1: RFA is first-line for osteoid osteoma.
- Level 2: Cryoablation offers superior pain relief for metastases.
- Level 3: HIFU is promising but requires further validation.

________________________________________
### 11. Summary & Key Takeaways
- Thermal ablation is effective and minimally invasive.
- RFA is preferred for osteoid osteoma; cryoablation for painful metastases.
- Complications are rare; follow-up imaging is essential.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Thermal Ablation of Bone Tumours**  
*Anthony Ryan, Caoimhe Byrne, Claudio Pusceddu, Xavier Buy, Georgia Tsoumakidou, Dimitrios Filippiadis*
________________________________________
""",
    
    "Prostate Artery Embolisation (PAE)": r"""
**CIRSE Standards of Practice on Prostate Artery Embolisation (PAE)**  
**Authors:** Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for PAE as a treatment for benign prostatic hyperplasia (BPH).
- Scope:  
  - Covers patient selection, procedural techniques, safety measures, and follow-up.
- Clinical Importance:  
  - PAE is a minimally invasive alternative to TURP with fewer complications.

________________________________________
### 2. Methods
- Writing Group: Six experts in IR and urology.
- Literature Review:  
  - PubMed search (2010–2021).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- BPH causes LUTS such as frequency, urgency, weak stream, and retention.
- PAE reduces prostate volume by embolizing the prostatic arteries.
- **Comparison (PAE vs. TURP):**

| Feature               | PAE                             | TURP                          |
|-----------------------|---------------------------------|-------------------------------|
| Invasiveness          | Minimally invasive              | Surgical                      |
| Hospital Stay         | Outpatient/24-hour              | 2–3 days                      |
| Sexual Dysfunction    | Low                             | Higher (~65% retrograde)      |
| Catheterization       | 24 hours or none                | 2–7 days                      |

________________________________________
### 4. Indications for PAE
- Symptomatic BPH (IPSS >12).
- Prostate volume >40 mL.
- Patients unfit for surgery.
- Patients who decline surgery.

________________________________________
### 5. Contraindications
**Absolute Contraindications:**  
- Severe atherosclerosis of the iliac arteries.
- Severe CKD (GFR <30 mL/min).
- Contrast allergy (unless premedicated).

**Relative Contraindications:**  
- Small prostate (<40 mL).
- Significant median lobe enlargement.
- Active UTI.

________________________________________
### 6. Pre-Procedural Preparation
- **Imaging:** Multiparametric MRI or CTA for vascular mapping; TRUS for prostate volume; DSA during the procedure.
- **Laboratory Tests:** Renal function, CBC, coagulation profile, PSA.
- **Antibiotic Prophylaxis:** Ciprofloxacin 500 mg BID for 3–5 days pre- and post-procedure.

________________________________________
### 7. Procedure: PAE
- **Step 1:** Arterial access via right femoral or radial artery.
- **Step 2:** Superselective microcatheterization of the prostatic arteries.
- **Step 3:** Embolization using PVA particles (100–300 μm) or microspheres.
- **Step 4:** Post-embolization angiography to confirm occlusion.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for urinary retention or hematuria.
- Use NSAIDs for pain and alpha-blockers for urinary symptoms.
- Follow-up evaluations at 1, 3, and 6 months.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - IPSS improvement: 60–80%.
  - Prostate volume reduction: ~30% at 6 months.
  - Urinary flow rate improvement: 50–70%.
- **Complications:**  
  - Mild: Post-embolization syndrome, transient urinary symptoms.
  - Moderate: Transient urinary retention (5–10%), hematuria.
  - Severe: Non-target embolization (<1%), rare erectile dysfunction.

________________________________________
### 10. Level of Evidence
- Level 1: PAE is safe and effective for moderate-to-severe BPH.
- Level 2: Quality-of-life improvements are comparable to TURP.
- Level 3: Particularly beneficial in large prostates (>80 mL).

________________________________________
### 11. Summary & Key Takeaways
- PAE is a minimally invasive alternative to TURP.
- Best candidates have prostate volumes >40 mL and refractory LUTS.
- Pre-procedural imaging is critical.
- High success with low complication risk.
- Follow-up imaging is recommended.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Prostate Artery Embolisation (PAE)**  
*Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale*
________________________________________
""",
    
    "Endovascular Treatment of Acute Pulmonary Embolism (PE)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE)**  
**Authors:** Andreas F. Kütting, Michael D. Chick, Constantino Del Giudice, Martin P. Gunn, Maged A. N. Alharbi, Reinhold G. Erbel, Christoph A. Nienaber  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for endovascular treatment of acute PE.
- Scope:  
  - Covers indications, contraindications, technical approaches (CDT, mechanical thrombectomy, aspiration thrombectomy), and post-procedure management.
- Clinical Importance:  
  - Acute PE is life-threatening.
  - Endovascular treatments offer rapid reperfusion with a lower bleeding risk compared to systemic thrombolysis.

________________________________________
### 2. Methods
- Writing Group: Six experts in PE treatment.
- Literature Review:  
  - PubMed search (2012–2021).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- PE is a major cause of cardiovascular mortality.
- **Risk Stratification (ESC):**  
  - High Risk (Massive PE): Shock, severe RV dysfunction.  
  - Intermediate-High Risk (Submassive PE): RV strain, elevated biomarkers.
- Lower risk cases are managed with anticoagulation.

________________________________________
### 4. Indications for Endovascular PE Treatment
- Massive PE with hemodynamic instability.
- Submassive PE with RV strain.
- Contraindications to systemic thrombolysis.
- Failure of anticoagulation alone.

________________________________________
### 5. Contraindications
**Absolute:**  
- Active major bleeding or recent intracranial hemorrhage.
- Severe coagulopathy.
- Uncontrolled severe hypertension.

**Relative:**  
- Recent major surgery/trauma (<14 days).
- History of hemorrhagic stroke.
- Severe renal impairment.

________________________________________
### 6. Pre-Procedural Workup
- **Imaging:** CTPA (gold standard), echocardiography, lower limb Doppler.
- **Laboratory:** Coagulation profile, D-dimer, troponin, BNP, renal function.
- **Anticoagulation:** Immediate IV heparin; bridge to DOACs post-procedure.

________________________________________
### 7. Procedure: Endovascular PE Treatment
- **Step 1:** Venous access (common femoral or internal jugular) and guidewire advancement into the pulmonary artery.
- **Step 2:** Treatment modalities:  
  1. Catheter-Directed Thrombolysis (CDT) with low-dose tPA.
  2. Mechanical Thrombectomy (e.g., AngioJet, FlowTriever, Penumbra Indigo).
  3. Aspiration Thrombectomy.
- **Step 3:** Continuous hemodynamic monitoring.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- ICU/telemetry monitoring for 24 hours.
- Monitor for bleeding and hemodynamic stability.
- Repeat imaging (CTPA/echocardiography) at 24–48 hours.
- Transition to long-term anticoagulation.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Clinical improvement: 85–95%.
  - Reduction in pulmonary artery pressure by 30–50%.
- **Complications:**  
  - Mild: Transient hypotension, minor hematoma.
  - Moderate: Minor systemic bleeding (~5%), device issues.
  - Severe: Major bleeding (~2–5%), pulmonary artery perforation/dissection (~1%).

________________________________________
### 10. Level of Evidence
- Level 1: CTPA is the gold standard.
- Level 2: CDT reduces clot burden with lower bleeding risk.
- Level 3: Mechanical thrombectomy is reserved for unstable cases.

________________________________________
### 11. Summary & Key Takeaways
- Endovascular treatment is essential for high-risk and selected submassive PE.
- CTPA and echocardiography are critical for risk stratification.
- CDT offers effective clot lysis with reduced bleeding.
- Mechanical thrombectomy is reserved for contraindications to thrombolysis.
- Post-procedural anticoagulation is mandatory.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE)**  
*Andreas F. Kütting, Michael D. Chick, Constantino Del Giudice, Martin P. Gunn, Maged A. N. Alharbi, Reinhold G. Erbel, Christoph A. Nienaber*
________________________________________
""",
    
    "Endovascular Treatment of Aortic Dissection": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection**  
**Authors:** Philipp A. Lüddecke, Martin M. Mortimer, Henrik A. Buenting, Konstantinos Stavroulakis, Klaus Hausegger, Constantino Del Giudice  
________________________________________
### 1. Introduction
- Purpose: To provide best practices for the endovascular treatment of aortic dissection (focusing on TEVAR).
- Scope:  
  - Covers indications, techniques, post-procedural care, and complications.
  - Primarily addresses Stanford Type B dissection with select Type A considerations.
- Clinical Importance:  
  - Aortic dissection is a life-threatening emergency.
  - TEVAR is a minimally invasive alternative to open surgery.

________________________________________
### 2. Methods
- Writing Group: Six experts in aortic interventions.
- Literature Review:  
  - PubMed search (2012–2021).
  - Consensus-based recommendations.

________________________________________
### 3. Background
- Aortic dissection is due to a tear in the intima, creating a false lumen.
- **Stanford Classification:**  
  - Type A: Involves the ascending aorta (requires surgery).
  - Type B: Involves the descending aorta (often managed with TEVAR).
- Indications include rupture, malperfusion, and rapid expansion.

________________________________________
### 4. Indications for TEVAR
- Complicated Type B dissection with malperfusion.
- Aortic rupture or impending rupture.
- Rapid expansion (>5 mm in 6 months).
- Persistent pain despite medical therapy.
- Recurrent hypertension due to false lumen perfusion.

________________________________________
### 5. Contraindications
**Absolute:**  
- Proximal landing zone <15 mm from the left subclavian without adequate sealing.
- Severe iliac or femoral artery disease.
- Active uncontrolled infection.

**Relative:**  
- Chronic stable dissection.
- Severe renal dysfunction.

________________________________________
### 6. Pre-Procedural Workup
- **Imaging:** CTA (gold standard), TEE, MRA.
- **Laboratory:** Renal function, coagulation profile, D-dimer, inflammatory markers.
- **Medical Optimization:** Blood pressure control (target SBP <120 mmHg).

________________________________________
### 7. Procedure: TEVAR
- **Step 1:** Vascular access via femoral artery; perform initial angiography.
- **Step 2:** Stent-graft placement with 10–15% oversizing.
- **Step 3:** Post-stent optimization (balloon molding; consider left subclavian coverage if needed).

________________________________________
### 8. Post-Procedural Care & Follow-Up
- ICU monitoring for 24–48 hours.
- Strict BP control.
- CTA at 1 month, then every 6–12 months.
- Lifelong surveillance.

________________________________________
### 9. Outcomes & Complications
- **Success Rates:**  
  - Technical success: 95–98%.
  - 1-year survival: 85–90% in complicated TBAD.
  - False lumen thrombosis in ~75%.
- **Complications:**  
  - Mild: Transient BP instability, groin hematoma.
  - Moderate: Endoleaks, left subclavian occlusion.
  - Severe: Spinal cord ischemia, retrograde Type A dissection, stent migration.

________________________________________
### 10. Level of Evidence
- Level 1: TEVAR is the standard for complicated Type B dissection.
- Level 2: BP control is essential.
- Level 3: Lifelong imaging follow-up is necessary.

________________________________________
### 11. Summary & Key Takeaways
- TEVAR is preferred for complicated Type B dissection.
- CTA is essential for planning and follow-up.
- Optimal BP control (<120 mmHg) is critical.
- Complications include endoleak, retrograde dissection, and spinal cord ischemia.
- Long-term surveillance is mandatory.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection**  
*Philipp A. Lüddecke, Martin M. Mortimer, Henrik A. Buenting, Konstantinos Stavroulakis, Klaus Hausegger, Constantino Del Giudice*
________________________________________
"""
}

# Remove any duplicate keys (if any value is None, it will be removed)
documents = {k: v for k, v in documents.items() if v is not None}

# Sidebar: Intervention selection
doc_choice = st.sidebar.selectbox("Select an Intervention", list(documents.keys()))

# Display the selected document
st.markdown(documents[doc_choice])

# Disclaimer at the end
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="disclaimer"><strong>Disclaimer:</strong> This application is intended for educational use only and does not substitute for professional clinical judgment. All recommendations and content are provided as a reference guide based on published standards. Please consult the full CIRSE Standards of Practice and other clinical resources before making clinical decisions.</div>',
    unsafe_allow_html=True
)
