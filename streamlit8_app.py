import streamlit as st

# Custom CSS for colors and styling (yellow, white, grey)
st.markdown(
    """
    <style>
    /* Background and text colors */
    .reportview-container {
        background-color: #ffffff;
        color: #4d4d4d;
    }
    /* Header (title) colors */
    h1, h2, h3, h4 {
        color: #d4af37;  /* gold/yellow accent */
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f2f2f2;
    }
    /* Subtitle small font style */
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

# Title and Subtitle
st.title("CIRSE Standards of Practice Pocket Guide")
st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)

st.markdown("""
Welcome to the CIRSE Standards of Practice Pocket Guide.  
This guide provides key standards and recommendations for various interventional procedures as defined by CIRSE.  
Select an intervention from the sidebar below to view its full details.
""")

# --- Define documents as a dictionary with embedded text ---
# For demonstration, we include one example document (Bronchial Artery Embolisation).
# You can expand this dictionary with additional documents as needed.
documents = {
    "Bronchial Artery Embolisation": r"""
**CIRSE Standards of Practice on Bronchial Artery Embolisation**  
**Authors:** Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos  
________________________________________

### 1. Introduction
- **Bronchial artery embolisation (BAE)** is a minimally invasive, life‐saving procedure used to treat haemoptysis (coughing up blood).
- The CIRSE Standards of Practice provide best practices to optimize safety and efficacy in performing BAE.
- This document does not impose a strict standard but provides evidence‐based recommendations for interventional radiologists.

________________________________________

### 2. Methods
- **Writing Group:** Five internationally recognized experts in BAE.
- **Literature Review:**
  - Timeframe: 1974–2021.
  - Source: PubMed database.
  - Consensus-Based Recommendations.

________________________________________

### 3. Background
- Haemoptysis is a life-threatening emergency, with mortality rates of 50–100% if untreated (primarily due to asphyxiation).
- With timely diagnosis and treatment, mortality drops to <20%.
- **Etiology:**
  - 90% of massive haemoptysis cases arise from the bronchial circulation.
  - 5% from the pulmonary circulation.
  - 5% from non-bronchial systemic circulations.
- **Common Causes:**
  - Tuberculosis (TB)
  - Lung cancer
  - Chronic lung diseases (bronchiectasis, cystic fibrosis, chronic pulmonary aspergillosis)

________________________________________

### 4. Indications for BAE
- Life-threatening haemoptysis (severe or massive).
- Recurrent haemoptysis despite medical therapy.
- Bridge therapy for lung transplant candidates with chronic inflammatory lung diseases.
- Index bleeding: Initial minor bleeding episodes that may precede massive haemoptysis.

________________________________________

### 5. Contraindications
**Absolute Contraindications:**
- Embolisation of arteries that supply the spinal cord, brain, or heart (risk of ischemia).

**Relative Contraindications:**
- Severe contrast allergy.
- Coagulopathy (must be corrected before the procedure).
- Renal insufficiency (careful contrast use required).

________________________________________

### 6. Pre-Procedural Preparation
**Clinical Work-Up:**
- Confirm that the bleeding is from the lungs.
- Assess severity and rule out non-pulmonary sources.
- Review patient history (previous haemoptysis, infections, malignancies, lung disease).
- Optimize coagulation parameters before intervention.

**Imaging:**
- **First-Line Imaging:**  
  Computed tomography angiography (CTA) is the gold standard for localizing the bleeding source, identifying the culprit artery, and ruling out alternative diagnoses. It is essential for planning catheterization.
- **Additional Imaging:**  
  Chest X-ray (initial screening, low sensitivity) and flexible bronchoscopy (for airway clearance) may be used, with Digital Subtraction Angiography (DSA) essential for vessel selection and embolisation.

________________________________________

### 7. Procedure: Bronchial Artery Embolisation (BAE)
**Access & Catheterisation:**
- Preferred access: Femoral artery (retrograde approach).
- Use a 4–5 Fr diagnostic catheter for initial evaluation.
- Superselective catheterisation with a microcatheter (2.7 Fr or smaller) is critical to avoid non-target embolisation.

**Embolisation Agents:**
- **Preferred:** Polyvinyl alcohol (PVA) particles (300–500 µm).
- **Alternatives:** N-butyl-2-cyanoacrylate (NBCA) glue (for high-flow fistulas) or coils (used selectively).

**Technique:**
1. Confirm the target vessel via angiography.
2. Slowly infuse embolic material until stasis is achieved.
3. Avoid reflux to prevent non-target embolisation.
4. Perform post-embolisation angiography to confirm treatment success.

________________________________________

### 8. Post-Procedural Care & Follow-Up
- **Immediate Monitoring:**  
  Observe for recurrence of haemoptysis and monitor oxygen saturation and airway patency.
- **Long-Term Follow-Up:**  
  Repeat CTA or bronchoscopy if haemoptysis recurs. Additional embolisation may be required in 10–30% of cases due to recanalisation.

________________________________________

### 9. Outcomes & Complications
**Technical Success Rate:**  
- 85–98% initial success with embolisation.

**Rebleeding Rates:**  
- 10–30% rebleeding within 6 months (often due to incomplete embolisation, collateral vessel formation, or progression of underlying disease).

**Complications:**
- *Mild:* Transient chest pain due to ischemia.
- *Severe (Rare):* Spinal cord ischemia, bronchial infarction, or non-target embolisation (which may lead to stroke, myocardial infarction, or bowel ischemia).

________________________________________

### 10. Level of Evidence
- **Level 1:** CTA is the first-line imaging modality for evaluating haemoptysis.
- **Level 2:** PVA particles (300–500 µm) are the preferred embolic agent for BAE.
- **Level 3:** BAE is recommended as a bridge therapy for lung transplant candidates.

________________________________________

### 11. Summary
- **BAE** is a highly effective, minimally invasive treatment for life-threatening and recurrent haemoptysis.
- **CTA** is essential for pre-procedural planning.
- **Embolisation** with PVA particles is the preferred method, though alternatives exist.
- High success rates are achieved; however, rebleeding may occur, necessitating repeat intervention.

________________________________________

### 12. Citation
**CIRSE Standards of Practice on Bronchial Artery Embolisation**  
*Joachim Kettenbach, Harald Ittrich, Jean Yves Gaubert, Bernhard Gebauer, Jan Albert Vos*
________________________________________
""",
    # You can add more documents as additional key/value pairs if needed.
}

# --- Sidebar: Document (Intervention) Selection ---
doc_choice = st.sidebar.selectbox("Select an Intervention", list(documents.keys()))

# --- Display the Selected Document ---
st.markdown(documents[doc_choice])

# --- Disclaimer at the End ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="disclaimer"><strong>Disclaimer:</strong> This application is intended for educational use only and does not substitute for professional clinical judgment. All recommendations and content are provided as a reference guide based on published standards. Please consult the full CIRSE Standards of Practice and other clinical resources before making clinical decisions.</div>',
    unsafe_allow_html=True
)
