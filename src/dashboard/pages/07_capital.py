import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("💰 Capital Allocation")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

# -----------------------------
# Company List
# -----------------------------
companies = pd.read_sql(
    "SELECT id, company_name FROM companies ORDER BY company_name",
    conn
)

ticker = st.selectbox(
    "Select Company",
    companies["id"]
)

# -----------------------------
# Cash Flow Data
# -----------------------------
query = f"""
SELECT
    year,
    operating_activity,
    investing_activity,
    financing_activity,
    net_cash_flow
FROM cashflow
WHERE company_id='{ticker}'
ORDER BY year
"""

df = pd.read_sql(query, conn)

# -----------------------------
# Treemap Data
# -----------------------------
treemap_query = """
SELECT
    c.company_name,
    s.broad_sector,
    mc.market_cap_crore
FROM companies c

JOIN sectors s
ON c.id = s.company_id

JOIN market_cap mc
ON c.id = mc.company_id

WHERE mc.year = (
    SELECT MAX(year)
    FROM market_cap m2
    WHERE m2.company_id = mc.company_id
)
"""

treemap_df = pd.read_sql(treemap_query, conn)

conn.close()

# -----------------------------
# Cash Flow Table
# -----------------------------
st.subheader("📋 Cash Flow Data")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# Operating Cash Flow
# -----------------------------
st.subheader("📈 Operating Cash Flow")

fig = px.line(
    df,
    x="year",
    y="operating_activity",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Investing Cash Flow
# -----------------------------
st.subheader("📉 Investing Cash Flow")

fig = px.line(
    df,
    x="year",
    y="investing_activity",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Financing Cash Flow
# -----------------------------
st.subheader("💳 Financing Cash Flow")

fig = px.line(
    df,
    x="year",
    y="financing_activity",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Net Cash Flow
# -----------------------------
st.subheader("💵 Net Cash Flow")

fig = px.bar(
    df,
    x="year",
    y="net_cash_flow",
    text="net_cash_flow"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Treemap
# -----------------------------
st.subheader("🌳 Market Capitalization Treemap")

fig = px.treemap(
    treemap_df,
    path=["broad_sector", "company_name"],
    values="market_cap_crore",
    color="market_cap_crore",
    color_continuous_scale="Blues"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Company Summary
# -----------------------------
st.subheader("🏢 Company Market Cap Summary")

st.dataframe(
    treemap_df.sort_values(
        by="market_cap_crore",
        ascending=False
    ),
    use_container_width=True
)