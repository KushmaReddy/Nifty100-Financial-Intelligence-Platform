import streamlit as st
import sqlite3
import pandas as pd
import sys
import plotly.express as px
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_table

st.title("🏠 Home Dashboard")

# -----------------------------
# Load Companies
# -----------------------------
companies = load_table("companies")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

# -----------------------------
# Year Selector
# -----------------------------
years = pd.read_sql(
    "SELECT DISTINCT year FROM financial_ratios ORDER BY year",
    conn
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    years["year"],
    index=len(years) - 1
)

# -----------------------------
# KPI Query
# -----------------------------
query = f"""
SELECT
    c.id,
    c.company_name,
    fr.roe,
    fr.debt_to_equity,
    fr.debt_free,
    fr.revenue_cagr_5y,
    mc.pe_ratio
FROM companies c
JOIN financial_ratios fr
ON c.id = fr.company_id
JOIN market_cap mc
ON c.id = mc.company_id
WHERE fr.year = {selected_year}
AND mc.year = {selected_year}
"""

kpi = pd.read_sql(query, conn)

# -----------------------------
# Sector Query
# -----------------------------
sector_query = """
SELECT
    broad_sector,
    COUNT(*) AS companies
FROM sectors
GROUP BY broad_sector
ORDER BY companies DESC
"""

sector_df = pd.read_sql(sector_query, conn)

# -----------------------------
# Top 5 Companies
# -----------------------------
top5_query = f"""
SELECT
    c.id,
    c.company_name,
    fr.roe,
    fr.roce,
    fr.revenue_cagr_5y
FROM companies c
JOIN financial_ratios fr
ON c.id = fr.company_id
WHERE fr.year = {selected_year}
ORDER BY fr.roe DESC
LIMIT 5
"""

top5 = pd.read_sql(top5_query, conn)

conn.close()

# -----------------------------
# KPI Cards
# -----------------------------
c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Companies",
    len(kpi)
)

c2.metric(
    "Median ROE",
    f"{kpi['roe'].median():.2f}%"
)

c3.metric(
    "Median Revenue CAGR (5Y)",
    f"{kpi['revenue_cagr_5y'].median():.2f}%"
)

c4, c5, c6 = st.columns(3)

c4.metric(
    "Median Debt/Equity",
    f"{kpi['debt_to_equity'].median():.2f}"
)

debt_free_count = (
    kpi["debt_free"]
    .astype(str)
    .str.lower()
    .eq("yes")
    .sum()
)

c5.metric(
    "Debt-Free Companies",
    debt_free_count
)

c6.metric(
    "Median P/E",
    f"{kpi['pe_ratio'].median():.2f}"
)

# -----------------------------
# Company Preview
# -----------------------------
st.subheader("Company Preview")

st.dataframe(
    companies.head(),
    use_container_width=True
)

# -----------------------------
# Sector Distribution
# -----------------------------
st.subheader("Sector Distribution")

fig = px.pie(
    sector_df,
    names="broad_sector",
    values="companies",
    hole=0.5,
    title="Companies by Sector"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Top 5 Companies
# -----------------------------
st.subheader("🏆 Top 5 Companies by ROE")

st.dataframe(
    top5,
    use_container_width=True
)