import streamlit as st

st.set_page_config(
    page_title="Nifty100 Financial Intelligence Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 Nifty100 Financial Intelligence Platform")

st.markdown(
    """
    Welcome to the Nifty100 Financial Intelligence Dashboard.

    Use the navigation menu on the left to explore:

    - Home
    - Company Profile
    - Screener
    - Peer Comparison
    - Trends
    - Sector Analysis
    - Capital Allocation
    - Reports
    """
)