# app.py
# Python 3.14.4
# Streamlit single-file multi-page workplace accountability documentation app

import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Workplace Accountability Review",
    page_icon="📋",
    layout="wide",
)

# ---------------------------------------------------------
# STYLES
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 0.5rem;
        }

        .section-title {
            font-size: 1.8rem;
            font-weight: 600;
            color: #111827;
            margin-top: 1rem;
        }

        .concept-box {
            background-color: #f3f4f6;
            padding: 1rem;
            border-radius: 12px;
            border-left: 6px solid #2563eb;
            margin-bottom: 1rem;
        }

        .warning-box {
            background-color: #fef2f2;
            padding: 1rem;
            border-radius: 12px;
            border-left: 6px solid #dc2626;
            margin-bottom: 1rem;
        }

        .info-box {
            background-color: #ecfeff;
            padding: 1rem;
            border-radius: 12px;
            border-left: 6px solid #0891b2;
            margin-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------

st.sidebar.title("Navigation")

pages = {
    "Overview": "overview",
    "Asymmetric Accountability": "asymmetric",
    "Selective Enforcement": "selective",
    "Scan-Based Monitoring": "scan_monitoring",
    "Managerial Time Encoding": "time_encoding",
    "Conduct Enforcement Example": "conduct_example",
    "Health & Safety Concerns": "health_safety",
    "Reporting & Documentation": "documentation",
}

selection = st.sidebar.radio(
    "Select a Concept Page",
    list(pages.keys())
)

current_page = pages[selection]

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">Workplace Accountability & Enforcement Review</div>',
    unsafe_allow_html=True,
)

st.caption(
    f"Generated with Streamlit • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

# ---------------------------------------------------------
# PAGE: OVERVIEW
# ---------------------------------------------------------

if current_page == "overview":

    st.markdown(
        '<div class="section-title">Overview</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="concept-box">
        This application documents concepts related to workplace accountability,
        differential enforcement standards, scan-based labor tracking,
        managerial oversight gaps, and operational reporting inconsistencies.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("""
    The application separates each workplace concept into its own page
    while maintaining a single-file codebase for simplified deployment
    using Streamlit Cloud.
    """)

    st.info("""
    This application is informational and organizational in nature and
    does not constitute legal advice.
    """)

# ---------------------------------------------------------
# PAGE: ASYMMETRIC ACCOUNTABILITY
# ---------------------------------------------------------

elif current_page == "asymmetric":

    st.markdown(
        '<div class="section-title">Asymmetric Accountability</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="concept-box">
        Asymmetric accountability refers to workplace systems where
        hourly employees are measured and disciplined under stricter
        operational standards than supervisory personnel.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Observed Characteristics")

    st.write("""
    - Employees monitored through scan-based productivity systems
    - Managers operating outside equivalent measurable controls
    - Unequal disciplinary exposure
    - Different operational visibility standards
    """)

    st.subheader("Potential Impacts")

    st.write("""
    - Reduced trust in enforcement systems
    - Perceived unfairness
    - Reporting inconsistencies
    - Accountability gaps
    """)

# ---------------------------------------------------------
# PAGE: SELECTIVE ENFORCEMENT
# ---------------------------------------------------------

elif current_page == "selective":

    st.markdown(
        '<div class="section-title">Selective Enforcement</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="warning-box">
        Selective enforcement occurs when conduct rules are applied
        differently depending on organizational role or status.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Example Scenario")

    st.write("""
    An hourly employee may receive corrective attention for
    approximately 180 seconds of conversation while actively working,
    whereas managers or managers-in-training may engage in prolonged
    non-operational discussion without equivalent enforcement action.
    """)

    st.subheader("Indicators")

    st.write("""
    - Unequal policy application
    - Different monitoring standards
    - Inconsistent corrective action
    - Lack of transparent oversight
    """)

# ---------------------------------------------------------
# PAGE: SCAN-BASED MONITORING
# ---------------------------------------------------------

elif current_page == "scan_monitoring":

    st.markdown(
        '<div class="section-title">Scan-Based Monitoring Systems</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-box">
        Scan-based labor systems track employee productivity through
        measurable workflow interactions tied to operational scanners,
        timestamps, or automated labor metrics.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Common Characteristics")

    st.write("""
    - Time-off-task measurements
    - Productivity rate tracking
    - Scan interval analysis
    - Automated reporting systems
    """)

    st.subheader("Potential Limitations")

    st.write("""
    - Limited contextual awareness
    - Differential visibility between employees and managers
    - Possible overemphasis on measurable activity
    """)

# ---------------------------------------------------------
# PAGE: MANAGERIAL TIME ENCODING
# ---------------------------------------------------------

elif current_page == "time_encoding":

    st.markdown(
        '<div class="section-title">Managerial Time Encoding</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="concept-box">
        Managerial time encoding refers to administrative labor coding
        systems that allow supervisory staff to classify operational
        time differently from scan-based employee labor tracking.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Examples")

    st.write("""
    - Administrative coding
    - Indirect labor categories
    - Meeting classifications
    - Coaching activity entries
    """)

    st.subheader("Operational Concerns")

    st.write("""
    - Reduced audit parity
    - Unequal visibility
    - Potential reporting blind spots
    """)

# ---------------------------------------------------------
# PAGE: CONDUCT ENFORCEMENT EXAMPLE
# ---------------------------------------------------------

elif current_page == "conduct_example":

    st.markdown(
        '<div class="section-title">Conduct Enforcement Example</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="warning-box">
        Example documentation structure for workplace reporting and
        internal accountability review.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Documented Observation")

    st.text_area(
        "Scenario",
        value="""
An employee remained continuously productive while experiencing
pneumonia-like symptoms and engaged in approximately 180 seconds
of conversation while actively working.

At the same time, three managers or managers-in-training remained
in prolonged discussion for an estimated four-hour period without
equivalent enforcement, documentation, or corrective attention.
        """,
        height=250,
    )

    st.subheader("Potential Workplace Concerns")

    st.write("""
    - Unequal enforcement standards
    - Differential accountability systems
    - Health and safety concerns
    - Selective monitoring practices
    """)

# ---------------------------------------------------------
# PAGE: HEALTH & SAFETY
# ---------------------------------------------------------

elif current_page == "health_safety":

    st.markdown(
        '<div class="section-title">Health & Safety Concerns</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="warning-box">
        Workplace health concerns may become operationally significant
        when visibly ill employees continue active labor under
        productivity-focused enforcement systems.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Relevant Considerations")

    st.write("""
    - Employee wellness
    - Illness visibility
    - Operational pressure
    - Attendance expectations
    - Safety exposure
    """)

    st.subheader("Potential Organizational Risks")

    st.write("""
    - Reduced morale
    - Workplace illness spread
    - Perceived unfair treatment
    - Increased reporting escalation
    """)

# ---------------------------------------------------------
# PAGE: REPORTING & DOCUMENTATION
# ---------------------------------------------------------

elif current_page == "documentation":

    st.markdown(
        '<div class="section-title">Reporting & Documentation</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="concept-box">
        Effective workplace documentation separates observable facts,
        comparative conduct, operational impact, and policy concerns.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Documentation Structure")

    st.write("""
    1. Observable facts  
    2. Comparative conduct  
    3. Operational impact  
    4. Policy inconsistency  
    5. Reporting outcomes
    """)

    st.subheader("Example Categories")

    st.write("""
    - Unequal enforcement
    - Accountability gaps
    - Supervisory conduct
    - Reporting deficiencies
    - Operational inconsistency
    """)

    st.download_button(
        label="Download Documentation Notes",
        data="""
Workplace Accountability Documentation

- Asymmetric accountability
- Selective enforcement
- Scan-based monitoring
- Managerial time encoding
- Health and safety concerns
- Reporting inconsistencies
        """,
        file_name="workplace_accountability_notes.txt",
        mime="text/plain",
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Single-file Streamlit application • Compatible with Streamlit Cloud deployment"
)
