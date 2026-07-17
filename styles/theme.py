import streamlit as st


def inject_custom_css():
    """Inject premium custom CSS into the Streamlit app."""
    st.markdown("""
    <style>
        /* ─── Google Fonts ─── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* ─── Global Overrides ─── */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        /* ─── Main Container ─── */
        .stApp {
            background: linear-gradient(180deg, #0E1117 0%, #151922 50%, #0E1117 100%);
        }

        /* ─── Hide Default Header & Footer ─── */
        header[data-testid="stHeader"] {
            background: transparent !important;
        }
        footer { visibility: hidden; }

        /* ─── Sidebar ─── */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #12151E 0%, #1A1F2E 100%) !important;
            border-right: 1px solid rgba(108, 99, 255, 0.15) !important;
        }

        /* ─── Buttons ─── */
        .stButton > button {
            background: linear-gradient(135deg, #6C63FF, #5A52E0) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.7rem 2.5rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3) !important;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #7B73FF, #6C63FF) !important;
            box-shadow: 0 6px 25px rgba(108, 99, 255, 0.5) !important;
            transform: translateY(-2px) !important;
        }
        .stButton > button:active {
            transform: translateY(0) !important;
        }

        /* ─── File Uploader ─── */
        [data-testid="stFileUploader"] {
            border: 2px dashed rgba(108, 99, 255, 0.3) !important;
            border-radius: 16px !important;
            padding: 1rem !important;
            transition: all 0.3s ease !important;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: rgba(108, 99, 255, 0.6) !important;
            background: rgba(108, 99, 255, 0.03) !important;
        }

        /* ─── Text Area ─── */
        .stTextArea textarea {
            background: rgba(26, 31, 46, 0.8) !important;
            border: 1px solid rgba(108, 99, 255, 0.2) !important;
            border-radius: 12px !important;
            color: #E0E0E0 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 0.92rem !important;
            transition: all 0.3s ease !important;
        }
        .stTextArea textarea:focus {
            border-color: #6C63FF !important;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15) !important;
        }

        /* ─── Spinner ─── */
        .stSpinner > div {
            border-top-color: #6C63FF !important;
        }

        /* ─── Warning / Info / Success / Error Boxes ─── */
        [data-testid="stAlert"] {
            border-radius: 12px !important;
            border: none !important;
        }

        /* ─── Subheader Styling ─── */
        .stMarkdown h2, .stMarkdown h3 {
            background: linear-gradient(135deg, #6C63FF, #48C6EF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700 !important;
        }

        /* ─── Metric Styling ─── */
        [data-testid="stMetric"] {
            background: rgba(108, 99, 255, 0.06);
            border: 1px solid rgba(108, 99, 255, 0.15);
            border-radius: 12px;
            padding: 1rem;
        }

        /* ─── Scrollbar ─── */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(108, 99, 255, 0.3);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(108, 99, 255, 0.5);
        }
    </style>
    """, unsafe_allow_html=True)
