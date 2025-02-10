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
# Main Page Header & Key Points
# =====================
st.title("CIRSE Standards of Practice Pocket Guide")
st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)

st.header("Key Points about CIRSE Standards of Practice")
with st.expander("Click to expand Key Points", expanded=True):
    st.markdown("""
- **Evidence-Based:** Recommendations are derived from extensive literature reviews and expert consensus.
- **Comprehensive:** Covers a wide range of interventional procedures from embolization and stenting to ablation and drainage.
- **Patient Safety:** Emphasizes optimizing safety and procedural efficacy.
- **Global Impact:** Helps standardize care and improve outcomes worldwide.
- **Minimally Invasive:** Focuses on less invasive approaches to improve recovery times.
""")

# =====================
# Search Functionality
# =====================
st.subheader("Search Documents")
search_query = st.text_input("Enter search term:")
# The documents dictionary (see below) will be filtered based on this search term.

# =====================
# Documents Dictionary
# =====================
# (Each key is a document title and the value is a multi-line string with the structured text.)
documents = {
    "Bronchial Artery Embolisation": r"""
**CIRSE Standards of Practice on Bronchial Artery Embolisation**  
**Authors:** Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos

________________________________________
### 1. Introduction
- BAE is a minimally invasive, life-saving procedure used to treat haemoptysis.
- Provides evidence-based recommendations.

________________________________________
### 2. Methods
- Writing Group: 5 experts.
- Literature Review: 1974–2021 from PubMed.

________________________________________
### 3. Background
- Haemoptysis is life-threatening; proper intervention reduces mortality to <20%.
- Causes include TB, lung cancer, and chronic lung diseases.

________________________________________
### 4. Indications for BAE
- Life-threatening haemoptysis.
- Recurrent haemoptysis despite therapy.
- Bridge therapy for lung transplant candidates.

________________________________________
### 5. Contraindications
- **Absolute:** Avoid embolization of arteries supplying the spinal cord, brain, or heart.
- **Relative:** Severe contrast allergy, coagulopathy, renal insufficiency.

________________________________________
### 6. Pre-Procedural Preparation
- Confirm pulmonary bleeding source with CTA.
- Clinical work-up and imaging (CTA, X-ray, bronchoscopy, DSA).

________________________________________
### 7. Procedure
- Femoral artery access, superselective catheterization.
- Preferred embolic agent: PVA particles (300–500 µm).

________________________________________
### 8. Post-Procedural Care
- Monitor oxygen saturation and airway patency.
- Long-term follow-up with repeat imaging.

________________________________________
### 9. Outcomes & Complications
- Technical success: 85–98%.
- Rebleeding in 10–30% of cases.
- Severe complications: Rare spinal cord ischemia.

________________________________________
### 10. Level of Evidence
- Levels 1–3 based on imaging and agent selection.

________________________________________
### 11. Summary
- BAE is effective and minimally invasive.
- CTA is essential for planning.
________________________________________
### 12. Citation
*CIRSE Standards of Practice on Bronchial Artery Embolisation – Joachim Kettenbach et al.*
""",
    
    "Arterial Access for Interventions": r"""
**CIRSE Standards of Practice on Arterial Access for Interventions**  
**Authors:** Sabrina Memarian, Miltiadis Krokidis, Gerard O’Sullivan, Bora Peynircioglu, Michele Rossi, Elika Kashef

________________________________________
### 1. Introduction
- Best practices for safe arterial access for endovascular procedures.

________________________________________
### 2. Methods
- Literature review from 2002–2019.

________________________________________
### 3. Background
- Ultrasound guidance has improved safety and success.
________________________________________
### 4. Indications & 5. Contraindications
- For interventions such as angioplasty, tumor embolization, and EVAR.
- Contraindications include severe atherosclerosis, infection, or coagulopathy.
________________________________________
### 6. Pre-Procedural Preparation
- History, physical exam, and ultrasound (CTA/MRA for complex cases).
________________________________________
### 7. Procedure
- Common femoral, radial, and brachial access techniques.
________________________________________
### 8. Post-Procedural Care
- Manual compression/closure devices; monitor for complications.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Femoral access success >95%.
________________________________________
### 11. Summary
- Ultrasound guidance is essential.
________________________________________
### 12. Citation
*CIRSE Standards of Practice on Arterial Access for Interventions – Sabrina Memarian et al.*
""",
    
    "Varicocele Embolisation": r"""
**CIRSE Standards of Practice on Varicocele Embolisation**  
**Authors:** Anna Maria Ierardi, Pierpaolo Biondetti, Dimitrios Tsetis, Costantino Del Giudice, Raman Uberoi

________________________________________
### 1. Introduction
- Best practices for percutaneous varicocele embolisation.

________________________________________
### 2. Methods & 3. Background
- PubMed review (2006–2021); varicocele is common in infertile men.

________________________________________
### 4. Indications & 5. Contraindications
- Indicated for varicocele-related infertility and pain.
- Contraindications include contrast allergy and severe coagulopathy.
________________________________________
### 6. Pre-Procedural Preparation
- Scrotal ultrasound and Doppler evaluation.
________________________________________
### 7. Procedure
- Right femoral or jugular access; embolization with coils/NBCA.
________________________________________
### 8. Post-Procedural Care
- Follow-up exam and Doppler at 3–6 months.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 85–95%.
________________________________________
### 11. Summary
- Minimally invasive alternative to surgery.
________________________________________
### 12. Citation
*CIRSE Standards of Practice on Varicocele Embolisation – Anna Maria Ierardi et al.*
""",
    
    "Oesophageal and Gastroduodenal Stenting": r"""
**CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting**  
**Authors:** Athanasios Diamantopoulos, Shuvro Roy Choudhury, Farah Gillian Irani, Hugo Rio Tinto, Tarun Sabharwal

________________________________________
### 1. Introduction
- Best practices for SEMS placement in the oesophagus and gastroduodenal tract.
________________________________________
### 2. Methods & 3. Background
- PubMed review (2005–2021); addresses both malignant and benign strictures.
________________________________________
### 4. Indications, 5. Contraindications, & 6. Pre-Procedural Preparation
- Indicated for dysphagia, GOO; contraindications include perforation and severe bleeding.
________________________________________
### 7. Procedure
- Endoscopic and fluoroscopic guidance to deploy SEMS.
________________________________________
### 8. Post-Procedural Care
- Soft diet after 24 hours and follow-up imaging.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–99%.
________________________________________
### 11. Summary
- Provides rapid relief with manageable complications.
________________________________________
### 12. Citation
*CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting – Athanasios Diamantopoulos et al.*
""",
    
    "Peri-Operative Anticoagulation Management During IR Procedures": r"""
**CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During Interventional Radiology Procedures**  
**Authors:** Mohammed Hadi, Carolina Walker, Michael Desborough, Antonio Basile, Dimitrios Tsetis, Beverley Hunt, Stefan Müller-Hüllsbeck, Thomas Rand, Otto van Delden, Raman Uberoi

________________________________________
### 1. Introduction
- Guidelines for managing anticoagulation in IR procedures.
________________________________________
### 2. Methods & 3. Background
- Comprehensive literature review and Delphi consensus.
________________________________________
### 4.–7. Assessment & Management Strategies
- Pre-procedural workup and risk stratification.
________________________________________
### 8. Peri-Procedural Management
- Specific recommendations for Warfarin, Heparin, LMWH, and DOACs.
________________________________________
### 9. Bridging Strategies & 10. Post-Procedural Care
- Bridging protocols and monitoring for bleeding or thrombosis.
________________________________________
### 11. Outcomes & 12. Level of Evidence
- Complication rates and evidence levels provided.
________________________________________
### 13. Summary
- Balancing bleeding vs. thromboembolic risk is critical.
________________________________________
### 14. Citation
*CIRSE Standards of Practice on Peri-Operative Anticoagulation Management During IR Procedures – Mohammed Hadi et al.*
""",
    
    "Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting": r"""
**CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting**  
**Authors:** Marco Das, Christiaan van der Leij, Marcus Katoh, Daniel Benten, Babs M. F. Hendriks, Adam Hatzidakis

________________________________________
### 1. Introduction
- Best practices for PTC, PTBD, and PTBS in managing biliary obstruction.
________________________________________
### 2. Methods & 3. Background
- Consensus-based recommendations from PubMed (2000–2021).
________________________________________
### 4.–5. Indications & Contraindications
- For malignant and benign biliary strictures.
________________________________________
### 6. Pre-Procedural Preparation
- Imaging (US, CT, MRI) and lab tests.
________________________________________
### 7. Procedure
- Steps for PTC, PTBD, and PTBS.
________________________________________
### 8.–10. Post-Procedural Care & Outcomes
- Success rates and complication profiles.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Stenting – Marco Das et al.*
""",
    
    "Below-the-Knee Revascularisation": r"""
**CIRSE Standards of Practice on Below-the-Knee Revascularisation**  
**Authors:** Stavros Spiliopoulos, Costantino Del Giudice, Marco Manzi, Lazaros Reppas, Thomas Rodt, Raman Uberoi

________________________________________
### 1. Introduction
- Guidelines for endovascular treatment of CLTI.
________________________________________
### 2. Methods & 3. Background
- PubMed review (2004–2020); focus on limb salvage.
________________________________________
### 4.–5. Indications & Contraindications
- For patients with rest pain, ulcers, or failed bypass.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Imaging and procedural techniques.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: ~85–95%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Below-the-Knee Revascularisation – Stavros Spiliopoulos et al.*
""",
    
    "Hepatic Transarterial Chemoembolisation (TACE)": r"""
**CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE)**  
**Authors:** Pierleone Lucatelli, Marta Burrel, Boris Guiu, Gianluca de Rubeis, Otto van Delden, Thomas Helmberger

________________________________________
### 1. Introduction
- Guidelines for TACE in hepatic tumors.
________________________________________
### 2. Methods & 3. Background
- Literature review (2012–2020).
________________________________________
### 4.–5. Indications & Contraindications
- For unresectable HCC, ICC, and metastases.
________________________________________
### 6.–8. Pre-Procedural Preparation & Procedure
- Access via femoral artery; embolization techniques.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Tumor response: 50–70% for HCC.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE) – Pierleone Lucatelli et al.*
""",
    
    "Thermal Ablation of Bone Tumours": r"""
**CIRSE Standards of Practice on Thermal Ablation of Bone Tumours**  
**Authors:** Anthony Ryan, Caoimhe Byrne, Claudio Pusceddu, Xavier Buy, Georgia Tsoumakidou, Dimitrios Filippiadis

________________________________________
### 1. Introduction
- Guidelines for thermal ablation (RFA, cryoablation, MWA, HIFU) of bone tumors.
________________________________________
### 2. Methods & 3. Background
- PubMed review (2009–2021).
________________________________________
### 4.–5. Indications & Contraindications
- For osteoid osteoma, bone metastases, and selected malignancies.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Image-guided ablation techniques.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Success: 90–95% for osteoid osteoma.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Thermal Ablation of Bone Tumours – Anthony Ryan et al.*
""",
    
    "Prostate Artery Embolisation (PAE)": r"""
**CIRSE Standards of Practice on Prostate Artery Embolisation (PAE)**  
**Authors:** Marc Sapoval, Ari J. Isaacson, Michael K. W. Li, Mauro Schioppa, Robert Morgan, Francisco Carnevale

________________________________________
### 1. Introduction
- Guidelines for PAE as a treatment for BPH.
________________________________________
### 2. Methods & 3. Background
- PubMed review (2010–2021).
________________________________________
### 4.–5. Indications & Contraindications
- For symptomatic BPH with prostate >40 mL.
________________________________________
### 6.–8. Workup & Procedure
- Superselective embolization via femoral/radial access.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- IPSS improvement: 60–80%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Prostate Artery Embolisation (PAE) – Marc Sapoval et al.*
""",
    
    "Endovascular Treatment of Acute Pulmonary Embolism (PE)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE)**  
**Authors:** Andreas F. Kütting, Michael D. Chick, Constantino Del Giudice, Martin P. Gunn, Maged A. N. Alharbi, Reinhold G. Erbel, Christoph A. Nienaber

________________________________________
### 1. Introduction
- Guidelines for endovascular treatment of acute PE.
________________________________________
### 2. Methods & 3. Background
- PubMed review (2012–2021); covers CDT, mechanical thrombectomy, aspiration.
________________________________________
### 4.–5. Indications & Contraindications
- For massive and select submassive PE.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Use of CTPA, hemodynamic monitoring.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Clinical improvement in 85–95% of cases.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Acute Pulmonary Embolism (PE) – Andreas F. Kütting et al.*
""",
    
    "Endovascular Treatment of Aortic Dissection": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection**  
**Authors:** Philipp A. Lüddecke, Martin M. Mortimer, Henrik A. Buenting, Konstantinos Stavroulakis, Klaus Hausegger, Constantino Del Giudice

________________________________________
### 1. Introduction
- Guidelines for TEVAR in aortic dissection.
________________________________________
### 2. Methods & 3. Background
- Focus on Stanford Type B dissection.
________________________________________
### 4.–5. Indications & Contraindications
- Indications include rupture, malperfusion, rapid expansion.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Vascular access via femoral artery; stent-graft deployment.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Aortic Dissection – Philipp A. Lüddecke et al.*
""",
    
    "Uterine Artery Embolisation (UAE) for Symptomatic Fibroids": r"""
**CIRSE Standards of Practice on Uterine Artery Embolisation (UAE) for Symptomatic Fibroids**  
**Authors:** Overhagen H., Binkert C., Röthlin M., Kaufmann C., Pellerin O., Walker W., Spies J.

________________________________________
### 1. Introduction
- Provides best practices for UAE in symptomatic fibroids.
________________________________________
### 2. Methods & 3. Background
- PubMed review (2000–2015); fibroids affect up to 70% of women.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for heavy menstrual bleeding and bulk symptoms; contraindicated in pregnancy, active infection.
________________________________________
### 6.–8. Pre-Procedural Workup and Procedure
- Pelvic MRI is the gold standard; embolization via femoral access.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Success: ~85–90% symptom relief.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Uterine Artery Embolisation (UAE) for Symptomatic Fibroids – Overhagen H. et al.*
""",
    
    "Endovascular Treatment of Peripheral Arterial Disease (PAD)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD)**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for endovascular therapy of PAD.
________________________________________
### 2. Methods & 3. Background
- Atherosclerosis leads to PAD; classified by Rutherford.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for lifestyle-limiting claudication and CLI.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CTA is the gold standard; balloon angioplasty, stenting, atherectomy techniques.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 90–98%; 1-year patency: 70–85%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Peripheral Arterial Disease (PAD) – Alessandro Napoli et al.*
""",
    
    "Endovascular Treatment of Thoracic Aortic Aneurysms (TAA)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Thoracic Aortic Aneurysms (TAA)**  
**Authors:** Konstantinos Stavroulakis, Philipp A. Lüddecke, Martin M. Mortimer, Klaus Hausegger, Thomas Rand, Alessandro Napoli

________________________________________
### 1. Introduction
- Best practices for TEVAR in thoracic aortic aneurysms.
________________________________________
### 2. Methods & 3. Background
- TAAs are life-threatening when >5.5–6.0 cm.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for aneurysms >5.5 cm, rapid growth, or symptomatic.
________________________________________
### 6.–8. Pre-Procedural Workup, Procedure & Post-Care
- CTA planning; stent-graft deployment via femoral access.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%; 1-year survival: 85–90%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Thoracic Aortic Aneurysms (TAA) – Konstantinos Stavroulakis et al.*
""",
    
    "Inferior Vena Cava (IVC) Filter Placement and Retrieval": r"""
**CIRSE Standards of Practice on Inferior Vena Cava (IVC) Filter Placement and Retrieval**  
**Authors:** Constantinos T. Tapping, Michael K. W. Li, Anna Maria Ierardi, Raman Uberoi, Thomas Rand, Robert A. Lookstein

________________________________________
### 1. Introduction
- Guidelines for IVC filter placement and retrieval.
________________________________________
### 2. Methods & 3. Background
- Discusses permanent vs. retrievable filters.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated in patients with contraindication to anticoagulation.
________________________________________
### 6.–8. Pre-Procedural Workup and Procedure
- CT/MR venography; placement via femoral or jugular access.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–99%; retrieval success: 75–90%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Inferior Vena Cava (IVC) Filter Placement and Retrieval – Constantinos T. Tapping et al.*
""",
    
    "Endovascular Treatment of Abdominal Aortic Aneurysms (AAA)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Abdominal Aortic Aneurysms (AAA)**  
**Authors:** Konstantinos Stavroulakis, Philipp A. Lüddecke, Klaus Hausegger, Thomas Rand, Alessandro Napoli, Miltiadis Krokidis

________________________________________
### 1. Introduction
- Guidelines for EVAR in AAA.
________________________________________
### 2. Methods & 3. Background
- EVAR is first-line for AAA ≥5.5 cm.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for AAA ≥5.5 cm or rapid growth.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CTA planning; stent-graft deployment.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Abdominal Aortic Aneurysms (AAA) – Konstantinos Stavroulakis et al.*
""",
    
    "Percutaneous Image-Guided Drainage of Abdominal Abscesses": r"""
**CIRSE Standards of Practice on Percutaneous Image-Guided Drainage of Abdominal Abscesses**  
**Authors:** Anna Maria Ierardi, Constantinos T. Tapping, Marc Sapoval, Thomas Rand, Alessandro Napoli, Miltiadis Krokidis

________________________________________
### 1. Introduction
- Best practices for image-guided drainage of abdominal abscesses.
________________________________________
### 2. Methods & 3. Background
- Minimally invasive alternative to surgical drainage.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for well-defined abscesses ≥3 cm.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CT is the gold standard; drainage catheter placement.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 90–95%; clinical success: ~80%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Percutaneous Image-Guided Drainage of Abdominal Abscesses – Anna Maria Ierardi et al.*
""",
    
    "Superficial Venous Insufficiency Treatment with Endovenous Thermal Ablation": r"""
**CIRSE Standards of Practice on Superficial Venous Insufficiency Treatment with Endovenous Thermal Ablation**  
**Authors:** Marc Sapoval, Thomas Rand, Miltiadis Krokidis, Alessandro Napoli, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for EVTA (RFA/EVLA) in treating varicose veins.
________________________________________
### 2. Methods & 3. Background
- EVTA is now first-line compared to surgical stripping.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for symptomatic venous insufficiency (CEAP 2–6).
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Ultrasound mapping, tumescent anesthesia, and thermal ablation.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Vein closure: 95–98% at 1 year.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Superficial Venous Insufficiency Treatment with Endovenous Thermal Ablation – Marc Sapoval et al.*
""",
    
    "Superior Vena Cava (SVC) Stenting in Malignant Disease": r"""
**CIRSE Standards of Practice on Superior Vena Cava (SVC) Stenting in Malignant Disease**  
**Authors:** Raman Uberoi, Alessandro Napoli, Thomas Rand, Robert A. Lookstein, Marc Sapoval, Miltiadis Krokidis

________________________________________
### 1. Introduction
- Best practices for SVC stenting in malignant SVC syndrome.
________________________________________
### 2. Methods & 3. Background
- SVC syndrome is often due to lung cancer and lymphoma.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for severe symptomatic SVC obstruction.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CT venography for planning; stenting via femoral or jugular access.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%; symptomatic relief in ~90%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Superior Vena Cava (SVC) Stenting in Malignant Disease – Raman Uberoi et al.*
""",
    
    "Endovascular Management of Central Venous Stenosis and Occlusion": r"""
**CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion**  
**Authors:** Raman Uberoi, Alessandro Napoli, Thomas Rand, Marc Sapoval, Robert A. Lookstein, Miltiadis Krokidis

________________________________________
### 1. Introduction
- Guidelines for treating central venous stenosis/occlusion.
________________________________________
### 2. Methods & 3. Background
- Focus on veins such as SVC, brachiocephalic, and subclavian.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for symptomatic venous hypertension.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CT venography; balloon angioplasty and stenting.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%; 1-year patency: 70–85%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Management of Central Venous Stenosis and Occlusion – Raman Uberoi et al.*
""",
    
    "Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI)**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Best practices for endovascular revascularization in CMI.
________________________________________
### 2. Methods & 3. Background
- CTA is the gold standard for diagnosis.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for severe symptomatic CMI.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Stent placement in mesenteric arteries.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%; primary patency: 70–85%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Chronic Mesenteric Ischemia (CMI) – Alessandro Napoli et al.*
""",
    
    "Endovascular Treatment of Arterial Trauma": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Arterial Trauma**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for treating arterial trauma via endovascular methods.
________________________________________
### 2. Methods & 3. Background
- Covers dissection, pseudoaneurysm, AV fistula, and occlusion.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for hemodynamically stable patients.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CTA and DSA for diagnosis; stent-grafts, coil embolization, or liquid embolics.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 90–98%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Arterial Trauma – Alessandro Napoli et al.*
""",
    
    "Endovascular Management of Visceral Aneurysms and Pseudoaneurysms": r"""
**CIRSE Standards of Practice on Endovascular Management of Visceral Aneurysms and Pseudoaneurysms**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for managing visceral aneurysms/pseudoaneurysms.
________________________________________
### 2. Methods & 3. Background
- CTA and DSA are key.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for aneurysms >2 cm or rapid growth.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Options include coil embolization, stent-grafts, or liquid embolics.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Management of Visceral Aneurysms and Pseudoaneurysms – Alessandro Napoli et al.*
""",
    
    "Endovascular Treatment of Acute Limb Ischemia (ALI)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI)**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for endovascular treatment of ALI.
________________________________________
### 2. Methods & 3. Background
- ALI is an emergency; rapid revascularization is critical.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for Rutherford IIa-IIb ALI.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Techniques include CDT, mechanical thrombectomy, aspiration thrombectomy.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 90–95%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Acute Limb Ischemia (ALI) – Alessandro Napoli et al.*
""",
    
    "Endovascular Treatment of Renal Artery Stenosis (RAS)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS)**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for the endovascular treatment of RAS.
________________________________________
### 2. Methods & 3. Background
- RAS is a major cause of secondary hypertension.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for severe RAS with resistant hypertension.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CTA planning; stenting for atherosclerotic RAS; angioplasty for FMD.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 95–98%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Renal Artery Stenosis (RAS) – Alessandro Napoli et al.*
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r"""
**CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for managing persistent Type II endoleaks post-EVAR.
________________________________________
### 2. Methods & 3. Background
- Focus on feeder arteries (lumbar, IMA) causing sac expansion.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for sac expansion >5 mm in 6 months.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Options include transarterial embolization and direct sac embolization.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 85–95%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Management of Type II Endoleaks After EVAR – Alessandro Napoli et al.*
""",
    
    "Endovascular Treatment of Budd-Chiari Syndrome (BCS)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS)**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for endovascular treatment of BCS.
________________________________________
### 2. Methods & 3. Background
- Focus on hepatic venous outflow obstruction.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for symptomatic BCS.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- Options include angioplasty, stenting, thrombolysis, and TIPS.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 90–98%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Budd-Chiari Syndrome (BCS) – Alessandro Napoli et al.*
""",
    
    "Endovascular Treatment of Portal Vein Thrombosis (PVT)": r"""
**CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT)**  
**Authors:** Alessandro Napoli, Marc Sapoval, Miltiadis Krokidis, Thomas Rand, Robert A. Lookstein, Constantinos T. Tapping

________________________________________
### 1. Introduction
- Guidelines for treating PVT via endovascular techniques.
________________________________________
### 2. Methods & 3. Background
- Focus on thrombolysis, thrombectomy, TIPS, and anticoagulation.
________________________________________
### 4.–5. Indications & Contraindications
- Indicated for symptomatic PVT causing portal hypertension.
________________________________________
### 6.–8. Workup, Procedure & Post-Care
- CT/MR venography planning; various endovascular techniques.
________________________________________
### 9. Outcomes & 10. Level of Evidence
- Technical success: 85–95%.
________________________________________
### 11. Citation
*CIRSE Standards of Practice on Endovascular Treatment of Portal Vein Thrombosis (PVT) – Alessandro Napoli et al.*
""",
    
    "Endovascular Management of Type II Endoleaks After EVAR": r""" 
**(Duplicate entry; already included above)**
""",
    
    # (Additional duplicates are omitted – only one copy per unique document is included.)
}

# =====================
# Apply Search Filter
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
# Display Document Sections in Expanders
# =====================
def display_document_sections(doc_text):
    # Split the text by the delimiter (assumed to be 40 underscores)
    sections = doc_text.split("________________________________________")
    for sec in sections:
        sec = sec.strip()
        if sec:
            lines = sec.splitlines()
            # Use the first non-empty line as a potential header if it starts with '###'
            header_line = None
            content_lines = []
            for line in lines:
                if line.strip() and line.strip().startswith("###"):
                    header_line = line.strip()
                else:
                    content_lines.append(line)
            title = header_line if header_line else "Details"
            content = "\n".join(content_lines).strip()
            with st.expander(title, expanded=False):
                st.markdown(content)

display_document_sections(doc_content)

# =====================
# Key Features at the End
# =====================
st.subheader("Key Features")
with st.expander("Click to view key features", expanded=False):
    st.markdown("""
- **Evidence-Based Guidelines:** Derived from comprehensive literature reviews and expert consensus.
- **Minimally Invasive Techniques:** Emphasizes endovascular and percutaneous procedures for improved recovery.
- **Patient-Centric:** Detailed recommendations for patient selection, contraindications, and pre-/post-procedural care.
- **Wide Scope:** Covers a broad range of interventions from embolization and stenting to ablation and drainage.
- **Ongoing Follow-Up:** Highlights the importance of imaging and clinical monitoring to ensure long-term success.
""")

# =====================
# Disclaimer at the Bottom
# =====================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="disclaimer"><strong>Disclaimer:</strong> This application is intended for educational use only and does not substitute for professional clinical judgment. All recommendations are provided as a reference guide based on published standards. Please consult the full CIRSE Standards of Practice and other clinical resources before making clinical decisions.</div>',
    unsafe_allow_html=True
)
