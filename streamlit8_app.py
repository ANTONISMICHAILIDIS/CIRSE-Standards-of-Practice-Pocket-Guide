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

# Main page title and subtitle
st.title("CIRSE Standards of Practice Pocket Guide")
st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)

# Display some interesting key points about the CIRSE Standards of Practice
st.header("Key Points about CIRSE Standards of Practice")
with st.expander("Click to expand Key Points", expanded=True):
    st.markdown("""
- **Evidence-based:** The standards provide recommendations based on rigorous literature review and expert consensus.
- **Comprehensive:** They cover a wide range of interventional procedures including embolization, stenting, and ablation.
- **Patient Safety:** A key focus is on optimizing safety and procedural efficacy.
- **Continuously Updated:** The standards are periodically revised to reflect the latest research and best practices.
- **Global Impact:** They help standardize care and improve outcomes in interventional radiology worldwide.
""")

# Sidebar information: About CIRSE, Contact, etc.
with st.sidebar.expander("About CIRSE"):
    st.markdown("""
**CIRSE (Cardiovascular and Interventional Radiological Society of Europe)**  
CIRSE is dedicated to the advancement of interventional radiology through research, education, and the dissemination of best practices.  
For more information, visit the [CIRSE website](https://www.cirse.org).  
""")
with st.sidebar.expander("Contact"):
    st.markdown("""
**Contact Information**  
Email: info@cirse.org  
Phone: +44 (0)20 1234 5678  
Address: CIRSE, European Office, 123 Interventional Road, London, UK  
""")

st.markdown("---")
st.header("Select an Intervention")

# Define the intervention documents as a dictionary with multi-line strings.
documents = {
    "Bronchial Artery Embolisation": r"""
**CIRSE Standards of Practice on Bronchial Artery Embolisation**  
**Authors:** Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos

________________________________________
### 1. Introduction
- Bronchial artery embolisation (BAE) is a minimally invasive, life-saving procedure used to treat haemoptysis (coughing up blood).
- The CIRSE Standards of Practice provide best practices to optimize safety and efficacy.
- This document provides evidence-based recommendations for interventional radiologists.

________________________________________
### 2. Methods
- **Writing Group:** Five internationally recognized experts.
- **Literature Review:**
  - Timeframe: 1974–2021.
  - Source: PubMed database.
  - Consensus-Based Recommendations.

________________________________________
### 3. Background
- Haemoptysis is a life-threatening emergency with a mortality rate of 50–100% if untreated.
- Timely and optimal intervention reduces mortality to <20%.
  
**Etiology:**
- 90% from bronchial circulation.
- 5% from pulmonary circulation.
- 5% from non-bronchial systemic circulations.

**Common Causes:**
- Tuberculosis, lung cancer, chronic lung diseases, pulmonary AVMs.

**Global Variations:**
- Western countries: 80% due to lung cancer, TB, bronchiectasis, aspergillosis.
- India/Turkey: Tuberculosis accounts for 60–90%.

________________________________________
### 4. Indications for BAE
- Life-threatening (severe/massive) haemoptysis.
- Recurrent haemoptysis despite therapy.
- Bridge therapy for lung transplant candidates.
- Index minor bleeding preceding massive haemoptysis.

________________________________________
### 5. Contraindications
**Absolute:**
- Embolization of arteries supplying the spinal cord, brain, or heart.

**Relative:**
- Severe contrast allergy, coagulopathy, renal insufficiency.

________________________________________
### 6. Pre-Procedural Preparation
**Clinical Work-Up:**
- Confirm pulmonary source of bleeding.
- Assess severity; rule out non-pulmonary causes.
- Review patient history and optimize coagulation.

**Imaging:**
- **First-Line:** CTA (gold standard) to localize the bleeding source.
- **Additional:** Chest X-ray, flexible bronchoscopy, and DSA.

________________________________________
### 7. Procedure: Bronchial Artery Embolisation (BAE)
**Access & Catheterization:**
- Preferred via the femoral artery.
- Use a 4–5 Fr diagnostic catheter and a 2.7 Fr microcatheter for superselective catheterization.

**Embolization Agents:**
- **Preferred:** PVA particles (300–500 µm).
- **Alternatives:** NBCA glue and coils.

**Technique:**
1. Confirm target vessel via angiography.
2. Infuse embolic material slowly until stasis.
3. Avoid reflux.
4. Confirm success with post-embolization angiography.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- **Immediate:** Monitor for recurrent haemoptysis, oxygen saturation, and airway patency.
- **Long-Term:** Repeat CTA/bronchoscopy if needed; additional embolization in 10–30% of cases.

________________________________________
### 9. Outcomes & Complications
**Technical Success:** 85–98%.  
**Rebleeding:** 10–30% within 6 months.  
**Complications:**  
- Mild: Transient chest pain.
- Severe: Rare spinal cord ischemia, bronchial infarction, non-target embolization.

________________________________________
### 10. Level of Evidence
- Level 1: CTA is the first-line imaging modality.
- Level 2: PVA particles are preferred.
- Level 3: Consider BAE as a bridge therapy.

________________________________________
### 11. Summary
- BAE is highly effective and minimally invasive.
- CTA is essential for planning.
- PVA particles are preferred; alternatives exist.
- High success rates; rebleeding may require repeat intervention.

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
- Provides best practices for safe arterial access.
- Covers common femoral, radial, and brachial access.
- Essential for endovascular interventions.

________________________________________
### 2. Methods
- Writing Group: Six experts.
- Literature Review: PubMed (2002–2019) and expert consensus.

________________________________________
### 3. Background
- Critical for procedural success.
- Ultrasound guidance has reduced complications.
- Radial access offers lower bleeding risks.

________________________________________
### 4. Indications
- For peripheral interventions (angioplasty, stenting), tumor embolization, emergency embolization, PAE, and EVAR.

________________________________________
### 5. Contraindications
**Absolute:** Severe atherosclerosis, infection, or coagulopathy.  
**Relative:** Obesity, radial anomalies, or high-dose anticoagulation.

________________________________________
### 6. Pre-Procedural Preparation
- History and physical exam.
- Ultrasound guidance (recommended) and CTA/MRA if needed.
- Manage anticoagulation as necessary.

________________________________________
### 7. Procedure
**Common Femoral Access:** Puncture below inguinal ligament under US.  
**Radial Access:** Assess collateral circulation; use 5–6 Fr sheath.  
**Brachial Access:** Alternative when other sites are not feasible.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Use manual compression or closure devices.
- Monitor for complications.
- Radial access: use a compression device for 2–3 hours.

________________________________________
### 9. Outcomes & Complications
- Femoral: >95% success; Radial: lower bleeding but higher spasm.
- Complications include bleeding and pseudoaneurysm.

________________________________________
### 10. Level of Evidence
- Level 1: Ultrasound guidance recommended.
- Level 2: Radial access has lower bleeding risks.
- Level 3: Closure devices reduce time but carry risks.

________________________________________
### 11. Summary
- Arterial access is essential and should use ultrasound guidance.
- Radial access is safer but limited by vessel size.
- Proper patient selection is crucial.

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
- Provides best practices for percutaneous varicocele embolization.
- Alternative to surgical ligation with lower morbidity.

________________________________________
### 2. Methods
- Five expert group; PubMed search (2006–2021); consensus-based.

________________________________________
### 3. Background
- Varicocele: Abnormal dilation of testicular veins with reflux.
- Epidemiology: Affects 15% of adult males; higher in infertile men.
- Pathophysiology: Venous hypertension and increased testicular temperature.

________________________________________
### 4. Indications for Embolization
- Varicocele-related infertility.
- Testicular hypotrophy.
- Persistent scrotal pain.
- Cosmetic concerns and recurrence post-surgery.

________________________________________
### 5. Contraindications
**Absolute:** Allergy to contrast, severe coagulopathy.  
**Relative:** Renal insufficiency, bilateral varicocele.

________________________________________
### 6. Pre-Procedural Preparation
- Physical exam and scrotal ultrasound (gold standard).
- Doppler for reflux confirmation.
- Laboratory tests for coagulation and renal function.

________________________________________
### 7. Procedure: Percutaneous Varicocele Embolisation
- Access via right femoral or jugular vein.
- Venography, superselective catheterization of the internal spermatic vein.
- Embolization with coils, sclerosing agents, or NBCA glue.
- Confirm occlusion with post-embolization venography.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for pain, allergic reaction, or coil migration.
- Follow-up exam at 1–3 months and repeat Doppler at 3–6 months.

________________________________________
### 9. Outcomes & Complications
- Technical success: 85–95%; clinical success: 70–90%.
- Complications: Mild (scrotal pain), moderate (rare coil migration), severe (non-target embolization, very rare).

________________________________________
### 10. Level of Evidence
- Level 1: Scrotal ultrasound is the diagnostic gold standard.
- Level 2: Embolization is as effective as surgery with fewer complications.
- Level 3: Coils are preferred embolic material.

________________________________________
### 11. Summary & Key Takeaways
- Safe and effective minimally invasive alternative.
- Essential imaging and follow-up ensure success.
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
- Provides best practices for SEMS placement in the oesophagus and gastroduodenal tract.
- Effective palliative treatment for dysphagia and GOO.

________________________________________
### 2. Methods
- Five expert group; PubMed search (2005–2021); consensus-based.

________________________________________
### 3. Background
- SEMS are used to relieve obstruction.
- Oesophageal cancer and GOO are major clinical problems.
- Pathophysiology: Malignant or benign strictures.

________________________________________
### 4. Indications for Stenting
**Oesophageal:** Malignant strictures, TEFs, benign refractory strictures.  
**Gastroduodenal:** GOO due to malignancy, palliation, benign strictures.

________________________________________
### 5. Contraindications
**Absolute:** Perforation, severe bleeding, unsuitable obstructions.  
**Relative:** Severe coagulopathy, high migration risk, poor prognosis.

________________________________________
### 6. Pre-Procedural Preparation
- Evaluate dysphagia and nutritional status.
- Endoscopy to confirm stenosis.
- CT scan and fluoroscopy; check labs (coagulation, renal function).

________________________________________
### 7. Procedure: Stent Placement
- Oesophageal stenting: Supine; gastroduodenal: Supine/left lateral.
- Guidewire placement under fluoroscopic/endoscopic guidance.
- Deploy SEMS; balloon dilation if needed.
- Special considerations for TEFs and pyloric obstruction.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Immediate monitoring for pain, stent migration, aspiration.
- Soft diet after 24 hours.
- Follow-up imaging as needed.

________________________________________
### 9. Outcomes & Complications
- Technical success: 95–99%; clinical success: 75–90%.
- Complications: Mild (chest pain, dysphagia), moderate (migration, overgrowth), severe (aspiration, perforation).

________________________________________
### 10. Level of Evidence
- Level 1: SEMS are first-line for malignant dysphagia.
- Level 2: Combined guidance improves accuracy.
- Level 3: Benign strictures stenting reserved for refractory cases.

________________________________________
### 11. Summary & Key Takeaways
- Effective palliative intervention.
- SEMS provide immediate relief.
- Essential imaging and follow-up.
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
- Provides best practices for anticoagulation management during IR procedures.
- Balances bleeding versus thromboembolic risks.
- Critical due to complex patient profiles.

________________________________________
### 2. Methods
- Expert writing group; comprehensive PubMed/Cochrane search; Delphi consensus.

________________________________________
### 3. Background
- Challenging due to procedure complexity and comorbidities.
- Balancing bleeding risk with thrombosis risk.

________________________________________
### 4. Indications for Anticoagulation in IR Patients
- Atrial fibrillation, VTE prophylaxis, mechanical heart valves, recent MI/PAD, hypercoagulable states.

________________________________________
### 5. Contraindications
**Absolute:** Active bleeding, recent intracranial hemorrhage, uncontrolled hypertension, severe thrombocytopenia.  
**Relative:** High bleeding risk procedures, coagulation disorders, recent major surgery.

________________________________________
### 6. Pre-Procedural Coagulation Assessment
- Structured bleeding history and laboratory tests (PT/INR, aPTT, fibrinogen, platelets, TEG/ROTEM).

________________________________________
### 7. Anticoagulation Management Based on Procedure Risk
- Continue for low-risk; modify for moderate-risk; hold for high-risk procedures.

________________________________________
### 8. Peri-Procedural Management of Specific Anticoagulants
| Anticoagulant | Pre-Procedural Holding Time | Post-Procedural Restart Time |
|---------------|-----------------------------|------------------------------|
| Warfarin      | 5 days before high-risk     | 24–48 hours post-procedure   |
| Heparin       | 4–6 hours before            | Immediate (low-risk) or 24 hrs (high-risk) |
| LMWH          | 24 hours before             | 24 hours post-procedure      |
| DOACs         | 24–48 hours (renal-dependent)| 24 hours post-procedure      |

________________________________________
### 9. Bridging Strategies
- For high-risk warfarin patients: stop warfarin 5 days pre-, start LMWH bridging 3 days pre-, stop LMWH 24 hours pre-, resume LMWH/warfarin 24 hours post-procedure.

________________________________________
### 10. Post-Procedural Care & Monitoring
- Monitor for bleeding and thrombosis recurrence; gradual reintroduction of anticoagulation.

________________________________________
### 11. Outcomes & Complications
- Bleeding complications: Minor (5–15%), major (1–5%).
- Thromboembolic events: VTE recurrence (2–10%), stroke risk in AF (~5% per month).

________________________________________
### 12. Level of Evidence
- Level 1: Routine coagulation screening is not required unless indicated.
- Level 2: Bridging is necessary for high-risk warfarin patients.
- Level 3: DOACs require renal adjustment.

________________________________________
### 13. Summary & Key Takeaways
- Critical to balance bleeding and thrombosis risks.
- Bridging reserved for high-risk patients.
- Post-procedural monitoring is essential.

________________________________________
### 14. Citation
**CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During IR Procedures**  
*Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi*
________________________________________
""",
    
    "Below-the-Knee Revascularisation": r"""
**CIRSE Standards of Practice on Below-the-Knee Revascularisation**  
**Authors:** Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi

________________________________________
### 1. Introduction
- Provides best practices for BTK revascularisation.
- Focus on endovascular treatment for chronic limb-threatening ischemia (CLTI).
- Critical for limb salvage and wound healing.

________________________________________
### 2. Methods
- Six expert group; PubMed search (2004–2020); consensus agreement.

________________________________________
### 3. Background
- Affects diabetics, dialysis patients, and the elderly.
- CLTI is severe PAD with rest pain and non-healing ulcers.
- Goal: Restore perfusion; endovascular-first is preferred.

________________________________________
### 4. Indications for BTK Revascularisation
- Rest pain or non-healing ischemic ulcers.
- Salvage of failing bypass grafts.
- Limb preservation.
- Rapidly progressing diabetic foot ulcers.
- Prevention of major amputation.

________________________________________
### 5. Contraindications
**Absolute:** Severe infection, renal failure (eGFR <15 without dialysis), no viable targets.  
**Relative:** Poor functional status, extensive necrosis.

________________________________________
### 6. Pre-Procedural Assessment
- Imaging: Duplex, CTA/MRA, DSA.
- Hemodynamic tests: ABI (<0.4), TBI, TcPO2 (<30 mmHg).

________________________________________
### 7. Procedure: BTK Revascularisation
- Options: Balloon angioplasty (POBA), DCB, DES, atherectomy, pedal arch reconstruction.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Antithrombotic therapy (DAPT for 3–6 months; anticoagulation for high-risk).
- Monitor with Doppler at 1, 3, and 6 months; angiography if needed.

________________________________________
### 9. Outcomes & Complications
- Success: Technical ~85–95%, Clinical ~70–90%.
- Complications: Mild (hematoma), moderate (stent thrombosis, distal embolization), severe (limb ischemia, rupture).

________________________________________
### 10. Level of Evidence
- Level 1: Endovascular-first is standard in CLTI.
- Level 2: DES provide superior outcomes.
- Level 3: Pedal arch reconstruction is essential.

________________________________________
### 11. Summary & Key Takeaways
- Endovascular-first is preferred.
- Balloon angioplasty is standard; DCB/DES improve outcomes.
- Pedal arch reconstruction enhances healing.
- DAPT is critical.

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
- Provides best practices for TACE in hepatic tumors.
- Covers cTACE, DEM-TACE, DSM-TACE, and b-TACE.
- Standard-of-care for unresectable HCC in patients with preserved liver function.

________________________________________
### 2. Methods
- Six expert group; PubMed and EMBASE search (2012–2020); consensus-based recommendations.

________________________________________
### 3. Background
- TACE delivers chemotherapy directly into the tumor with arterial embolization.
- **Types:** cTACE, DEM-TACE, DSM-TACE, b-TACE.
- Primarily indicated for HCC, also for ICC and metastases.

________________________________________
### 4. Indications for TACE
- HCC with BCLC stage B.
- Non-surgical candidates.
- Palliative treatment for unresectable ICC.
- Metastatic liver tumors.

________________________________________
### 5. Contraindications
**Absolute:**  
- Decompensated liver disease (Child-Pugh C).  
- Severe portal vein thrombosis.  
- Uncontrolled infection.

**Relative:**  
- Bilirubin >3 mg/dL.
- Extensive tumor burden.
- Untreated varices.

________________________________________
### 6. Pre-Procedural Preparation
- **Imaging:** Multiphasic CT/MRI; Doppler ultrasound for portal vein patency.
- **Labs:** LFTs, AFP.
- **Antibiotic Prophylaxis:** Consider in high-risk patients.

________________________________________
### 7. Procedure: TACE Techniques
- Vascular access via common femoral artery.
- Chemotherapy administration: cTACE (lipiodol–chemotherapy emulsion) or DEM-TACE.
- Embolization with PVA/microspheres; b-TACE may be used.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for post-embolization syndrome.
- Pain management.
- LFTs at 24–48 hours; follow-up imaging at 1 and 3 months.

________________________________________
### 9. Outcomes & Complications
- Tumor response: 50–70% for HCC.
- Median OS: 20–30 months.
- Complications: Mild (post-embolization syndrome), moderate (cholecystitis, tumor rupture), severe (liver failure, hepatic abscess).

________________________________________
### 10. Level of Evidence
- Level 1: TACE is first-line for unresectable HCC with preserved liver function.
- Level 2: DEM-TACE reduces systemic toxicity.
- Level 3: b-TACE improves drug delivery (further study needed).

________________________________________
### 11. Summary & Key Takeaways
- TACE is the standard-of-care for unresectable HCC.
- DEM-TACE offers lower systemic toxicity.
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
- Provides best practices for thermal ablation of bone tumors.
- Covers RFA, cryoablation, MWA, and HIFU.
- Minimally invasive alternative to surgery/radiation.

________________________________________
### 2. Methods
- Six expert group; PubMed search (2009–2021); consensus-based.

________________________________________
### 3. Background
- Thermal ablation is an image-guided treatment for osseous lesions.
- **Indications:** Benign bone tumors (e.g., osteoid osteoma), painful metastases, selected malignant tumors.
- **Comparison of Techniques:** See table.

________________________________________
### 4. Indications for Thermal Ablation
- Osteoid osteoma, bone metastases causing pain, selected primary malignant tumors, recurrent tumors, oligometastatic disease.

________________________________________
### 5. Contraindications
**Absolute:** Unsafe tumor access, extensive cortical destruction, severe bleeding disorders.  
**Relative:** Lesions near neurovascular structures, active infection, poor prognosis.

________________________________________
### 6. Pre-Procedural Preparation
- Imaging: CT (preferred), MRI, bone scan/PET-CT.
- Labs: Coagulation profile, CBC.
- Anesthesia: General or conscious sedation.

________________________________________
### 7. Procedure: Thermal Ablation Techniques
- Patient positioning and anesthesia.
- CT/fluoroscopic guided probe placement.
- Ablation: RFA (90–100°C for 5–7 minutes), MWA (>100°C), cryoablation (freeze-thaw cycles), HIFU.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for pain relief (48–72 hours).
- Assess for complications (fracture, nerve injury).
- Follow-up imaging at 3–6 months.

________________________________________
### 9. Outcomes & Complications
- Success: Osteoid osteoma (90–95%), bone metastases (70–85% pain reduction), malignant tumors (50–70% control).
- Complications: Mild (pain, burns), moderate (fractures, nerve injury), severe (infection).

________________________________________
### 10. Level of Evidence
- Level 1: RFA is first-line for osteoid osteoma.
- Level 2: Cryoablation offers superior pain relief for metastases.
- Level 3: HIFU requires further validation.

________________________________________
### 11. Summary & Key Takeaways
- Effective, minimally invasive treatment.
- RFA preferred for osteoid osteoma; cryoablation for metastases.
- Follow-up imaging is crucial.

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
- Provides best practices for PAE as a treatment for BPH.
- Minimally invasive alternative to TURP.

________________________________________
### 2. Methods
- Six expert group; PubMed search (2010–2021); consensus-based.

________________________________________
### 3. Background
- BPH causes LUTS such as frequency, urgency, weak stream, and retention.
- PAE reduces prostate volume by embolizing the prostatic arteries.
- **Comparison (PAE vs. TURP):** See table.

________________________________________
### 4. Indications for PAE
- Symptomatic BPH (IPSS >12).
- Prostate volume >40 mL.
- Patients unfit for surgery or who decline it.

________________________________________
### 5. Contraindications
**Absolute:** Severe atherosclerosis, severe CKD (GFR <30), contrast allergy.  
**Relative:** Small prostate, significant median lobe enlargement, active UTI.

________________________________________
### 6. Pre-Procedural Preparation
- Imaging: Multiparametric MRI/CTA; TRUS; DSA.
- Laboratory: Renal function, CBC, coagulation profile, PSA.
- Antibiotic prophylaxis with ciprofloxacin.

________________________________________
### 7. Procedure: PAE
- Arterial access via right femoral or radial artery.
- Superselective microcatheterization.
- Embolization with PVA particles (100–300 μm) or microspheres.
- Post-embolization angiography.

________________________________________
### 8. Post-Procedural Care & Follow-Up
- Monitor for urinary retention or hematuria.
- Use NSAIDs and alpha-blockers.
- Follow-up at 1, 3, and 6 months.

________________________________________
### 9. Outcomes & Complications
- IPSS improvement 60–80%; ~30% prostate volume reduction; 50–70% improvement in flow.
- Complications: Mild (post-embolization syndrome), moderate (transient retention), severe (non-target embolization, rare).

________________________________________
### 10. Level of Evidence
- Level 1: PAE is safe and effective.
- Level 2: Comparable improvements to TURP.
- Level 3: Beneficial especially in large prostates.

________________________________________
### 11. Summary & Key Takeaways
- Minimally invasive alternative to TURP.
- Ideal for prostate >40 mL with refractory LUTS.
- Pre-procedural imaging is critical.
- High success and low complication rates.
- Follow-up imaging is recommended.

________________________________________
### 12. Citation
**CIRSE Standards of Practice on Prostate Artery Embolisation (PAE)**  
*Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale*
________________________________________
"""
}

# Sidebar: Intervention selection
selected_doc = st.selectbox("Select an Intervention", list(documents.keys()))

# Function to split document into sections based on the delimiter and create expanders
def display_document_sections(doc_text):
    # Split the text on the delimiter line (we assume 40 underscores as a marker)
    sections = doc_text.split("________________________________________")
    for sec in sections:
        sec = sec.strip()
        if sec:
            # Try to extract a title from the first line if it starts with a markdown header (e.g., ###)
            lines = sec.splitlines()
            if lines and lines[0].startswith("###"):
                title = lines[0]
                content = "\n".join(lines[1:]).strip()
            else:
                title = "Details"
                content = sec
            with st.expander(title, expanded=False):
                st.markdown(content)

# Main content: Display the selected intervention's document
doc_content = documents[selected_doc]
display_document_sections(doc_content)

# Disclaimer at the bottom
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="disclaimer"><strong>Disclaimer:</strong> This application is intended for educational use only and does not substitute for professional clinical judgment. All recommendations and content are provided as a reference guide based on published standards. Please consult the full CIRSE Standards of Practice and other clinical resources before making clinical decisions.</div>',
    unsafe_allow_html=True
)
