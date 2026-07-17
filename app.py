import streamlit as st
from styles.theme import inject_custom_css
from components import render_sidebar, render_results
from utils import extract_text_from_pdf, calculate_similarity


# ─── Page Configuration ───
st.set_page_config(
    page_title="AI Resume Reviewer · ATS Analyzer",
    page_icon="🎯",
    layout="wide",
)

# ─── Inject Custom Theme ───
inject_custom_css()

# ─── Sidebar ───
render_sidebar()


# ─── Main Content ───
def main():
    # Hero Header
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1 style="font-size: 2.8rem; font-weight: 800; margin: 0;
                    background: linear-gradient(135deg, #6C63FF 0%, #48C6EF 50%, #6C63FF 100%);
                    background-size: 200% auto;
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    animation: gradientShift 3s ease-in-out infinite;">
            AI Resume Reviewer
        </h1>
        <p style="color: #888; font-size: 1.1rem; margin-top: 0.5rem; font-weight: 400;">
            Upload your resume & paste a job description to see how well they match
        </p>
        <p style="color: #555; font-size: 0.85rem; margin-top: 0.25rem;">
            Powered by <b style="color:#6C63FF;">TF-IDF</b> + 
            <b style="color:#48C6EF;">Cosine Similarity</b>
        </p>
    </div>
    <style>
        @keyframes gradientShift {
            0%, 100% { background-position: 0% center; }
            50%      { background-position: 100% center; }
        }
    </style>
    """, unsafe_allow_html=True)

    # ─── Input Section ───
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <p style="font-size: 0.95rem; font-weight: 600; color: #B8B8CC; 
                  margin-bottom: 0.5rem;">
            📄 Resume Upload
        </p>
        """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload your resume (PDF)",
            type=["pdf"],
            label_visibility="collapsed",
        )

    with col2:
        st.markdown("""
        <p style="font-size: 0.95rem; font-weight: 600; color: #B8B8CC; 
                  margin-bottom: 0.5rem;">
            📋 Job Description
        </p>
        """, unsafe_allow_html=True)
        job_description = st.text_area(
            "Paste the job description",
            height=200,
            label_visibility="collapsed",
            placeholder="Paste the full job description here...",
        )

    # ─── Analyze Button ───
    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        analyze_clicked = st.button("🔍  Analyze Match", use_container_width=True)

    # ─── Processing ───
    if analyze_clicked:
        if not uploaded_file:
            st.warning("Please upload your resume.")
            return
        if not job_description:
            st.warning("Please paste the job description.")
            return

        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            if not resume_text:
                st.error(
                    "Could not extract text from PDF. Please try another file."
                )
                return

            similarity_score, _, _ = calculate_similarity(
                resume_text, job_description
            )

        # ─── Results ───
        st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
        render_results(similarity_score)


if __name__ == "__main__":
    main()