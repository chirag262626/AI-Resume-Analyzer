import streamlit as st


def _get_score_color(score):
    """Return gradient colors and label based on the match score."""
    if score < 40:
        return "#FF4B4B", "#FF6B6B", "Low Match"
    elif score < 70:
        return "#FFA726", "#FFD54F", "Good Match"
    else:
        return "#00C853", "#69F0AE", "Excellent Match"


def _render_gauge(score):
    """Render a premium animated CSS gauge bar."""
    color_start, color_end, label = _get_score_color(score)

    st.markdown(f"""
    <div style="margin: 1.5rem 0;">
        <div style="display: flex; justify-content: space-between; 
                    align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.85rem; color: #888; font-weight: 500;">
                Match Percentage
            </span>
            <span style="font-size: 0.85rem; color: {color_start}; 
                        font-weight: 700;">{label}</span>
        </div>
        <div style="width: 100%; height: 14px; 
                    background: rgba(255,255,255,0.05); 
                    border-radius: 50px; 
                    overflow: hidden;
                    box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);">
            <div style="width: {score}%; height: 100%; 
                        background: linear-gradient(90deg, {color_start}, {color_end}); 
                        border-radius: 50px;
                        transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
                        box-shadow: 0 0 12px {color_start}44;
                        animation: gaugeGlow 2s ease-in-out infinite alternate;">
            </div>
        </div>
    </div>
    <style>
        @keyframes gaugeGlow {{
            from {{ box-shadow: 0 0 8px {color_start}33; }}
            to   {{ box-shadow: 0 0 20px {color_start}66; }}
        }}
    </style>
    """, unsafe_allow_html=True)


def render_results(similarity_score):
    """Render the full results section: score card, gauge, and feedback."""
    color_start, color_end, label = _get_score_color(similarity_score)

    # Score card
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, 
                    rgba(108,99,255,0.12), rgba(72,198,239,0.08));
                border: 1px solid rgba(108,99,255,0.2);
                border-radius: 16px; padding: 2rem; 
                text-align: center; margin: 1.5rem 0;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0,0,0,0.2);">
        <p style="margin:0; font-size:0.9rem; color:#888; 
                  text-transform:uppercase; letter-spacing:2px; 
                  font-weight:600;">Match Score</p>
        <p style="margin:0.5rem 0; font-size:3.5rem; font-weight:800;
                  background: linear-gradient(135deg, {color_start}, {color_end});
                  -webkit-background-clip: text;
                  -webkit-text-fill-color: transparent;
                  line-height: 1.1;">
            {similarity_score:.1f}%
        </p>
        <p style="margin:0; font-size:1rem; color:{color_start}; 
                  font-weight:600;">{label}</p>
    </div>
    """, unsafe_allow_html=True)

    # Gauge bar
    _render_gauge(similarity_score)

    # Feedback message
    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

    if similarity_score < 40:
        st.markdown(f"""
        <div style="background: rgba(255,75,75,0.08); 
                    border-left: 4px solid #FF4B4B;
                    border-radius: 0 12px 12px 0; 
                    padding: 1rem 1.5rem; margin: 0.5rem 0;">
            <p style="margin:0; color:#FF6B6B; font-weight:600; font-size:1rem;">
                ⚠️ Low Match</p>
            <p style="margin:0.3rem 0 0 0; color:#B8B8CC; font-size:0.9rem;">
                Consider tailoring your resume more closely to the job description. 
                Focus on adding relevant keywords and matching required skills.</p>
        </div>
        """, unsafe_allow_html=True)

    elif similarity_score < 70:
        st.markdown(f"""
        <div style="background: rgba(255,167,38,0.08); 
                    border-left: 4px solid #FFA726;
                    border-radius: 0 12px 12px 0; 
                    padding: 1rem 1.5rem; margin: 0.5rem 0;">
            <p style="margin:0; color:#FFD54F; font-weight:600; font-size:1rem;">
                💡 Good Match</p>
            <p style="margin:0.3rem 0 0 0; color:#B8B8CC; font-size:0.9rem;">
                Your resume aligns fairly well with this job. 
                Some fine-tuning could push your score higher.</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style="background: rgba(0,200,83,0.08); 
                    border-left: 4px solid #00C853;
                    border-radius: 0 12px 12px 0; 
                    padding: 1rem 1.5rem; margin: 0.5rem 0;">
            <p style="margin:0; color:#69F0AE; font-weight:600; font-size:1rem;">
                🎉 Excellent Match!</p>
            <p style="margin:0.3rem 0 0 0; color:#B8B8CC; font-size:0.9rem;">
                Your resume strongly aligns with this job description. 
                Great job optimizing for ATS systems!</p>
        </div>
        """, unsafe_allow_html=True)
