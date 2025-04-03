import streamlit as st
import pandas as pd
from io import BytesIO

# ===============================
# 1) TRANSLATIONS (Merged)
# ===============================
translations = {
    "English": {
        # General UI elements
        "app_title": "CIRSE Standards of Practice Pocket Guide",
        "search_placeholder": "Enter search term:",
        "search_button": "Search",
        "no_results": "No documents found matching your search criteria.",
        "disclaimer_title": "Disclaimer:",
        "disclaimer_text": "The information provided in these standards of practice documents is believed to be true and accurate at the time of publication. Neither the Standards of Practice Committee members, their working group members, nor CIRSE can accept any legal responsibility for any errors or omissions made.",
        
        # Tab names
        "tab_standards": "Standards of Practice",
        "tab_educational": "Educational Resources",
        "tab_evidence": "Evidence Levels",
        "tab_procedures": "Procedures",
        "tab_about": "About",
        
        # Subtab names
        "subtab_all": "All Documents",
        "subtab_year": "By Year",
        "subtab_category": "By Category",
        
        # Section headers
        "section_search": "Search Documents",
        "section_evidence": "Evidence Levels in CIRSE Standards of Practice",
        "section_about": "About CIRSE Standards of Practice",
        
        # Sidebar elements
        "sidebar_about": "About CIRSE",
        "sidebar_about_text": "CIRSE (Cardiovascular and Interventional Radiological Society of Europe) is the world's biggest community of healthcare professionals involved in minimally invasive image-guided procedures. CIRSE promotes excellence in interventional radiology through education, research, and dissemination of best practices.",
        "sidebar_contact": "Contact",
        "sidebar_contact_text": "Contact Information\nEmail: info@cirse.org\nPhone: +43 1 904 2003\nAddress: CIRSE Central Office, Neutorgasse 9/6, 1010 Vienna, AUSTRIA",
        "sidebar_language": "Select Language",
        "sidebar_resources": "Resources",
        "sidebar_download": "Download Complete PDF Guide",
        "sidebar_educational": "Educational Resources",
        
        # Introduction text
        "intro_text": "This application provides access to the Cardiovascular and Interventional Radiological Society of Europe (CIRSE) Standards of Practice documents. These documents are designed to provide a reference for physicians on topics relevant to the field of interventional radiology.\n\nThe standards are created by the CIRSE Standards of Practice Committee (SOPC) and are aimed at experienced interventional radiologists as well as novices in the field of IR, and may also be used as a reference for physicians from other medical specialties.",
        
        # Evidence levels
        "evidence_intro": "CIRSE Standards of Practice documents use a three-level system to grade the strength of evidence and recommendations:",
        "evidence_level1": "Level 1",
        "evidence_level1_desc": "Strong evidence from at least one systematic review of multiple well-designed randomized controlled trials.",
        "evidence_level2": "Level 2",
        "evidence_level2_desc": "Strong evidence from at least one properly designed randomized controlled trial of appropriate size, or from well-designed, non-randomized clinical trials.",
        "evidence_level3": "Level 3",
        "evidence_level3_desc": "Evidence from descriptive studies, case reports, or reports of expert committees/consensus conferences.",
        "evidence_examples": "Examples of Evidence-Based Recommendations",
        "evidence_importance": "Importance of Evidence Levels",
        
        # Procedures section
        "procedures_title": "Procedures",
        "procedures_intro": "This section provides detailed procedural guides for common interventional radiology procedures. Each guide includes pre-procedure preparation, procedural steps, and post-procedure care.",
        "procedures_select": "Select Procedure",
        "pre_procedure": "Pre-Procedure",
        "procedure": "Procedure",
        "post_procedure": "Post-Procedure",
        
        # Educational resources
        "educational_title": "Educational Resources",
        "educational_intro": "This section provides educational resources for interventional radiologists at all stages of their career, from trainees to experienced practitioners seeking to expand their knowledge.",
        "training_resources": "Training Resources",
        "clinical_cases": "Clinical Cases",
        "procedural_videos": "Procedural Videos",
        "ir_glossary": "IR Glossary",
        
        # About section
        "about_purpose": "Purpose and Development",
        "about_process": "Development Process",
        "about_committee": "Standards of Practice Committee",
        "about_structure": "Document Structure",
        "about_citation": "Citation and Publication",
        
        # Translation notice
        "translation_notice": "Currently, all documents are only available in English. Translations coming soon!"
    }
    # Additional languages truncated for brevity (Spanish, French, etc.)
}

def get_translation(key, lang="English"):
    """Return the string for the given key in the requested language."""
    if lang not in translations:
        lang = "English"
    if key in translations[lang]:
        return translations[lang][key]
    else:
        return key


# ===============================
# 2) EDUCATIONAL_RESOURCES (Merged)
# ===============================
def display_educational_resources():
    st.markdown(f"## {get_translation('educational_title', st.session_state.language)}")
    st.markdown(get_translation("educational_intro", st.session_state.language))
    
    subtab1, subtab2, subtab3, subtab4 = st.tabs([
        get_translation("training_resources", st.session_state.language),
        get_translation("clinical_cases", st.session_state.language),
        get_translation("procedural_videos", st.session_state.language),
        get_translation("ir_glossary", st.session_state.language)
    ])
    
    with subtab1:
        st.markdown(f"### {get_translation('training_resources', st.session_state.language)} for Interventional Radiology")
        st.markdown("""
        **(Example content)**  
        - European Curriculum and Syllabus for IR  
        - CIRSE Academy  
        - EBIR exam info  
        - Textbooks, journals, etc.
        """)
    
    with subtab2:
        st.markdown(f"### {get_translation('clinical_cases', st.session_state.language)}")
        st.write("**(Example clinical cases)**")
        with st.expander("Case 1: Massive Hemoptysis - Bronchial Artery Embolization"):
            st.markdown("Details about the case, imaging, procedure steps, outcome...")
        with st.expander("Case 2: Hepatocellular Carcinoma - TACE"):
            st.markdown("Another example case...")

    with subtab3:
        st.markdown(f"### {get_translation('procedural_videos', st.session_state.language)}")
        st.write("**(Example videos)**")
        st.markdown("Video 1: Transjugular Liver Biopsy, Video 2: PAE, etc.")
    
    with subtab4:
        st.markdown(f"### {get_translation('ir_glossary', st.session_state.language)}")
        st.write("**(Example glossary)**")
        st.markdown("- A: Something\n- B: Something else")


# ===============================
# 3) PROCEDURES (Merged)
# ===============================
def display_procedures():
    st.markdown(f"## {get_translation('procedures_title', st.session_state.language)}")
    st.markdown(get_translation("procedures_intro", st.session_state.language))
    
    procedures = [
        "Bronchial Artery Embolisation",
        "Varicocele Embolisation",
        "Prostatic Artery Embolisation",
        "Thermal Ablation of Liver Tumours",
        "Percutaneous Transhepatic Biliary Drainage",
        "Transjugular Intrahepatic Portosystemic Shunt (TIPS)",
        "Carotid Artery Stenting",
        "Uterine Artery Embolisation",
        "Inferior Vena Cava Filter Placement",
        "Endovascular Aneurysm Repair",
        "Peripheral Arterial Angioplasty and Stenting",
        "Vertebroplasty and Kyphoplasty",
        "Radiofrequency Ablation of Osteoid Osteoma",
        "Transarterial Chemoembolization (TACE)",
        "Percutaneous Nephrostomy"
    ]
    
    selected_procedure = st.selectbox(get_translation("procedures_select", st.session_state.language), procedures)
    
    st.write(f"**(Example instructions for** {selected_procedure}**)**")
    st.markdown("""
    ### Pre-Procedure
    - Basic steps go here...
    ### Procedure
    - Steps 1, 2, 3...
    ### Post-Procedure
    - Follow-up, discharge, etc.
    """)


# ===============================
# 4) MAIN APPLICATION MERGED
# ===============================
def get_documents_data():
    """Example documents. In a real app, you can define your full set or load from a DB."""
    return [
        {
            "title": "Bronchial Artery Embolisation",
            "year": "2023",
            "authors": "Kettenbach et al.",
            "category": "Vascular Interventions",
            "content_preview": "Guidelines for managing haemoptysis..."
        },
        {
            "title": "Varicocele Embolisation",
            "year": "2022",
            "authors": "Ierardi et al.",
            "category": "Nonvascular Interventions",
            "content_preview": "Percutaneous approach to varicocele..."
        },
        {
            "title": "Uterine Artery Embolisation (UAE) for Fibroids",
            "year": "2021",
            "authors": "Hacking et al.",
            "category": "Embolization Procedures",
            "content_preview": "Symptomatic fibroid management..."
        },
    ]


def setup_sidebar():
    with st.sidebar.expander(get_translation("sidebar_about", st.session_state.language)):
        st.markdown(get_translation("sidebar_about_text", st.session_state.language))
    with st.sidebar.expander(get_translation("sidebar_contact", st.session_state.language)):
        st.markdown(get_translation("sidebar_contact_text", st.session_state.language))
    
    # Language selection
    st.session_state.language = st.sidebar.selectbox(
        get_translation("sidebar_language", st.session_state.language),
        ["English", "Spanish", "French", "German", "Chinese"],
        index=0
    )
    
    st.sidebar.markdown("---")
    
    # PDF guide
    if st.sidebar.button(get_translation("sidebar_download", st.session_state.language)):
        st.success("Pretend PDF is downloaded. In a real app, you'd generate or serve a file.")


def display_document_card(doc):
    st.markdown(f"""
    <div class="document-card">
        <h3>{doc["title"]}</h3>
        <div style="margin-bottom: 10px;">
            <span class="year-badge">{doc["year"]}</span>
            <span class="author-badge">{doc["authors"]}</span>
            <span class="category-badge">{doc["category"]}</span>
        </div>
        <p>{doc["content_preview"]}...</p>
    </div>
    """, unsafe_allow_html=True)


def display_documents(search_query):
    all_docs = get_documents_data()
    displayed = 0
    for d in all_docs:
        if search_query == "":
            display_document_card(d)
            displayed += 1
        else:
            # match title, preview, or category
            if (search_query.lower() in d["title"].lower() or
                search_query.lower() in d["content_preview"].lower() or
                search_query.lower() in d["category"].lower()):
                display_document_card(d)
                displayed += 1
    if displayed == 0:
        st.warning(get_translation("no_results", st.session_state.language))


def main():
    # -----------
    # Initialize language
    if "language" not in st.session_state:
        st.session_state.language = "English"
    # -----------
    
    # Setup sidebar
    setup_sidebar()
    
    # Main header
    st.title("CIRSE Standards of Practice Pocket Guide")
    st.markdown('<div class="small-font">Created by Michailidis A. for free use</div>', unsafe_allow_html=True)
    
    # Introduction text
    st.markdown(get_translation("intro_text", st.session_state.language))
    
    # Search Documents
    st.subheader(get_translation("section_search", st.session_state.language))
    search_query = st.text_input(get_translation("search_placeholder", st.session_state.language), "")
    
    if search_query:
        st.write(f"Results for: **{search_query}**")
    display_documents(search_query)
    
    st.markdown("---")
    
    # Tabs for educational / procedures if you want
    tab1, tab2 = st.tabs(["Educational Resources", "Procedures"])
    with tab1:
        display_educational_resources()
    with tab2:
        display_procedures()
    
    # disclaimer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="disclaimer">
    <strong>{get_translation("disclaimer_title", st.session_state.language)}</strong> {get_translation("disclaimer_text", st.session_state.language)}
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
