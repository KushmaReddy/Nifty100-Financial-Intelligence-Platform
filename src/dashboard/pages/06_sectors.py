import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("🏭 Sector Analysis")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

# -----------------------------
# Load Sectors
# -----------------------------
sectors = pd.read_sql(
    """
    SELECT DISTINCT broad_sector
    FROM sectors
    ORDER BY broad_sector
    """,
    conn
)

sector = st.selectbox(
    "Select Sector",
    sectors["broad_sector"]
)

# -----------------------------
# Load Sector Data
# -----------------------------
query = f"""
SELECT
    c.company_name,
    s.broad_sector,
    s.sub_sector,
    fr.roe,
    fr.roce,
    fr.net_profit_margin,
    fr.revenue_cagr_5y,
    mc.market_cap_crore
FROM sectors s

JOIN companies c
ON s.company_id = c.id

JOIN financial_ratios fr
ON c.id = fr.company_id

JOIN market_cap mc
ON c.id = mc.company_id

WHERE s.broad_sector = '{sector}'

AND fr.year = (
    SELECT MAX(year)
    FROM financial_ratios f2
    WHERE f2.company_id = fr.company_id
)

AND mc.year = (
    SELECT MAX(year)
    FROM market_cap m2
    WHERE m2.company_id = mc.company_id
)
"""

df = pd.read_sql(query, conn)

conn.close()

# -----------------------------
# Company Table
# -----------------------------
st.subheader(f"{sector} Companies")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# ROE
# -----------------------------
st.subheader("📊 ROE Comparison")

fig = px.bar(
    df,
    x="company_name",
    y="roe",
    color="company_name"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# ROCE
# -----------------------------
st.subheader("📊 ROCE Comparison")

fig = px.bar(
    df,
    x="company_name",
    y="roce",
    color="company_name"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Revenue CAGR
# -----------------------------
st.subheader("📊 Revenue CAGR (5Y)")

fig = px.bar(
    df,
    x="company_name",
    y="revenue_cagr_5y",
    color="company_name"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Net Profit Margin
# -----------------------------
st.subheader("📊 Net Profit Margin")

fig = px.bar(
    df,
    x="company_name",
    y="net_profit_margin",
    color="company_name"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Bubble Chart
# -----------------------------
st.subheader("🫧 Market Cap vs ROE")

fig = px.scatter(
    df,
    x="market_cap_crore",
    y="roe",
    size="market_cap_crore",
    color="company_name",
    hover_name="company_name",
    labels={
        "market_cap_crore": "Market Cap (₹ Crore)",
        "roe": "ROE (%)"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Sector Median KPI
# -----------------------------
st.subheader("📈 Sector Median KPIs")

median_df = pd.DataFrame({
    "Metric": [
        "ROE",
        "ROCE",
        "Revenue CAGR",
        "Net Profit Margin"
    ],
    "Median": [
        df["roe"].median(),
        df["roce"].median(),
        df["revenue_cagr_5y"].median(),
        df["net_profit_margin"].median()
    ]
})

fig = px.bar(
    median_df,
    x="Metric",
    y="Median",
    color="Metric",
    text="Median"
)

st.plotly_chart(
    fig,
    use_container_width=True
)