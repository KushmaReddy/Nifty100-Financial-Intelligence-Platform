import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📈 Financial Trends")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql(
    "SELECT id, company_name FROM companies ORDER BY company_name",
    conn
)

# -----------------------------
# Company Selection
# -----------------------------
ticker = st.selectbox(
    "Select Company",
    companies["id"]
)

# -----------------------------
# Load Financial Data
# -----------------------------
query = f"""
SELECT
    year,
    sales,
    net_profit,
    eps,
    opm_percentage
FROM profitandloss
WHERE company_id='{ticker}'
ORDER BY year
"""

df = pd.read_sql(query, conn)

conn.close()

# -----------------------------
# Metric Selection
# -----------------------------
metric_options = [
    "sales",
    "net_profit",
    "eps",
    "opm_percentage"
]

selected_metrics = st.multiselect(
    "Select up to 3 Metrics",
    metric_options,
    default=["sales", "net_profit"],
    max_selections=3
)

# -----------------------------
# Overlay Trend Chart
# -----------------------------
st.subheader("📊 Multi-Metric Trend")

if selected_metrics:

    fig = px.line(
        df,
        x="year",
        y=selected_metrics,
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Individual Charts
# -----------------------------
st.subheader("📈 Revenue Trend")

fig = px.line(
    df,
    x="year",
    y="sales",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📈 Net Profit Trend")

fig = px.line(
    df,
    x="year",
    y="net_profit",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📈 EPS Trend")

fig = px.line(
    df,
    x="year",
    y="eps",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📈 Operating Profit Margin")

fig = px.line(
    df,
    x="year",
    y="opm_percentage",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Year-over-Year Growth
# -----------------------------
st.subheader("📋 Year-over-Year Sales Growth")

yoy = df[["year", "sales"]].copy()

yoy["YoY Growth (%)"] = (
    yoy["sales"].pct_change() * 100
).round(2)

st.dataframe(
    yoy,
    use_container_width=True
)