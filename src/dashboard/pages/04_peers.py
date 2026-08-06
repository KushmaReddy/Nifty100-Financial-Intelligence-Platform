import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("⚖️ Peer Comparison")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql(
    "SELECT id, company_name FROM companies ORDER BY company_name",
    conn
)

# -----------------------------
# Peer Group
# -----------------------------
peer_groups = pd.read_sql(
    """
    SELECT DISTINCT broad_sector
    FROM sectors
    ORDER BY broad_sector
    """,
    conn
)

peer_group = st.selectbox(
    "Select Peer Group",
    peer_groups["broad_sector"]
)

peer_companies = pd.read_sql(
    f"""
    SELECT c.id
    FROM companies c
    JOIN sectors s
    ON c.id = s.company_id
    WHERE s.broad_sector='{peer_group}'
    ORDER BY c.id
    """,
    conn
)

company1 = st.selectbox(
    "Select Company 1",
    peer_companies["id"],
    key="company1"
)

company2 = st.selectbox(
    "Select Company 2",
    peer_companies["id"],
    index=1 if len(peer_companies) > 1 else 0,
    key="company2"
)

query = f"""
SELECT
    c.id,
    c.company_name,
    s.broad_sector,
    fr.roe,
    fr.roce,
    fr.net_profit_margin,
    fr.debt_to_equity,
    fr.revenue_cagr_5y,
    fr.free_cash_flow
FROM companies c

JOIN financial_ratios fr
ON c.id = fr.company_id

JOIN sectors s
ON c.id = s.company_id

WHERE c.id IN ('{company1}','{company2}')

AND fr.year = (
    SELECT MAX(year)
    FROM financial_ratios f2
    WHERE f2.company_id = fr.company_id
)
"""

df = pd.read_sql(query, conn)

conn.close()

# -----------------------------
# Comparison Table
# -----------------------------
st.subheader("📋 Comparison Table")

benchmark = company1

def highlight(row):
    if row["id"] == benchmark:
        return ["background-color: lightgreen"] * len(row)
    return [""] * len(row)

st.dataframe(
    df.style.apply(highlight, axis=1),
    use_container_width=True
)

# -----------------------------
# Radar Chart
# -----------------------------
st.subheader("🕸️ Radar Comparison")

categories = [
    "roe",
    "roce",
    "net_profit_margin",
    "debt_to_equity",
    "revenue_cagr_5y"
]

fig = go.Figure()

for _, row in df.iterrows():

    fig.add_trace(
        go.Scatterpolar(
            r=[
                row["roe"],
                row["roce"],
                row["net_profit_margin"],
                row["debt_to_equity"],
                row["revenue_cagr_5y"]
            ],
            theta=[
                "ROE",
                "ROCE",
                "Net Profit Margin",
                "Debt/Equity",
                "Revenue CAGR"
            ],
            fill="toself",
            name=row["company_name"]
        )
    )

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True)),
    showlegend=True
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROE
# -----------------------------
st.subheader("📊 ROE Comparison")

fig = px.bar(
    df,
    x="company_name",
    y="roe",
    color="company_name",
    text="roe"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROCE
# -----------------------------
st.subheader("📊 ROCE Comparison")

fig = px.bar(
    df,
    x="company_name",
    y="roce",
    color="company_name",
    text="roce"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Net Profit Margin
# -----------------------------
st.subheader("📊 Net Profit Margin")

fig = px.bar(
    df,
    x="company_name",
    y="net_profit_margin",
    color="company_name",
    text="net_profit_margin"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Revenue CAGR
# -----------------------------
st.subheader("📊 Revenue CAGR (5Y)")

fig = px.bar(
    df,
    x="company_name",
    y="revenue_cagr_5y",
    color="company_name",
    text="revenue_cagr_5y"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Free Cash Flow
# -----------------------------
st.subheader("📊 Free Cash Flow")

fig = px.bar(
    df,
    x="company_name",
    y="free_cash_flow",
    color="company_name",
    text="free_cash_flow"
)

st.plotly_chart(fig, use_container_width=True)