import streamlit as st


def render_sidebar():
    """Render the application sidebar with About and How It Works sections."""
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; margin-bottom:1.5rem;">
            <span style="font-size:2.5rem;">🎯</span>
            <h2 style="margin:0.5rem 0 0 0; 
                        background: linear-gradient(135deg, #6C63FF, #48C6EF);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-weight:800;">ATS Analyzer</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: rgba(108,99,255,0.08); 
                    border-left: 3px solid #6C63FF; 
                    padding: 1rem; 
                    border-radius: 0 8px 8px 0;
                    margin-bottom: 1rem;">
            <p style="margin:0; font-size:0.92rem; color:#B8B8CC;">
                <b style="color:#E0E0E0;">This tool helps you:</b>
            </p>
            <ul style="margin:0.5rem 0 0 1rem; padding:0; color:#B8B8CC; font-size:0.88rem;">
                <li>Measure resume-to-job alignment</li>
                <li>Identify important job keywords</li>
                <li>Improve your resume for ATS systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: rgba(72,198,239,0.06); 
                    border-left: 3px solid #48C6EF; 
                    padding: 1rem; 
                    border-radius: 0 8px 8px 0;">
            <p style="margin:0; font-size:0.92rem; color:#B8B8CC;">
                <b style="color:#E0E0E0;">How It Works</b>
            </p>
            <ol style="margin:0.5rem 0 0 1rem; padding:0; color:#B8B8CC; font-size:0.88rem;">
                <li>Upload your resume (PDF)</li>
                <li>Paste the job description</li>
                <li>Click <b>Analyze Match</b></li>
                <li>Review your score & suggestions</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-top:2rem; text-align:center; 
                    padding:0.8rem; 
                    border-top: 1px solid rgba(108,99,255,0.2);">
            <p style="margin:0; font-size:0.75rem; color:#666;">
                Powered by <b style="color:#6C63FF;">TF-IDF</b> + <b style="color:#48C6EF;">Cosine Similarity</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
