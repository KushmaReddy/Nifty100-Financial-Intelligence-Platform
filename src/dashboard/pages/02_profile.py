import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

# -----------------------------
# Load Companies
# -----------------------------
companies = pd.read_sql(
    "SELECT * FROM companies",
    conn
)

st.title("🏢 Company Profile")

ticker = st.selectbox(
    "Select Company",
    companies["id"].sort_values()
)

company = companies[
    companies["id"] == ticker
].iloc[0]

# -----------------------------
# Company Information
# -----------------------------
st.header(company["company_name"])

st.write(company["about_company"])

st.write("🌐 Website:", company["website"])

# -----------------------------
# Sector Information
# -----------------------------
sector = pd.read_sql(
    f"""
    SELECT
        broad_sector,
        sub_sector,
        market_cap_category
    FROM sectors
    WHERE company_id='{ticker}'
    """,
    conn
)

if not sector.empty:

    s = sector.iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Broad Sector",
        s["broad_sector"]
    )

    c2.metric(
        "Sub Sector",
        s["sub_sector"]
    )

    c3.metric(
        "Market Cap Category",
        s["market_cap_category"]
    )

# -----------------------------
# Company Details
# -----------------------------
c1, c2 = st.columns(2)

c1.metric(
    "Book Value",
    company["book_value"]
)

c2.metric(
    "Face Value",
    company["face_value"]
)

# -----------------------------
# Latest Financial Ratios
# -----------------------------
ratios = pd.read_sql(
    f"""
    SELECT *
    FROM financial_ratios
    WHERE company_id='{ticker}'
    ORDER BY year DESC
    LIMIT 1
    """,
    conn
)

if not ratios.empty:

    r = ratios.iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "ROE",
        f"{r['roe']:.2f}%"
    )

    c2.metric(
        "ROCE",
        f"{r['roce']:.2f}%"
    )

    c3.metric(
        "Net Profit Margin",
        f"{r['net_profit_margin']:.2f}%"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Debt / Equity",
        f"{r['debt_to_equity']:.2f}"
    )

    c5.metric(
        "Revenue CAGR (5Y)",
        f"{r['revenue_cagr_5y']:.2f}%"
    )

    c6.metric(
        "Free Cash Flow",
        f"{r['free_cash_flow']:,.0f}"
    )

# -----------------------------
# Profit & Loss Trends
# -----------------------------
profit = pd.read_sql(
    f"""
    SELECT
        year,
        sales,
        net_profit,
        eps,
        opm_percentage
    FROM profitandloss
    WHERE company_id='{ticker}'
    ORDER BY year
    """,
    conn
)

if not profit.empty:

    st.subheader("📈 Revenue Trend")

    fig = px.line(
        profit,
        x="year",
        y="sales",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Net Profit Trend")

    fig = px.line(
        profit,
        x="year",
        y="net_profit",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 EPS Trend")

    fig = px.line(
        profit,
        x="year",
        y="eps",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Operating Profit Margin")

    fig = px.line(
        profit,
        x="year",
        y="opm_percentage",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROE vs ROCE Trend
# -----------------------------
ratio_history = pd.read_sql(
    f"""
    SELECT
        year,
        roe,
        roce
    FROM financial_ratios
    WHERE company_id='{ticker}'
    ORDER BY year
    """,
    conn
)

if not ratio_history.empty:

    st.subheader("📊 ROE vs ROCE Trend")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ratio_history["year"],
            y=ratio_history["roe"],
            mode="lines+markers",
            name="ROE"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ratio_history["year"],
            y=ratio_history["roce"],
            mode="lines+markers",
            name="ROCE"
        )
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Percentage",
        legend_title="Metrics"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Pros & Cons
# -----------------------------
pc = pd.read_sql(
    f"""
    SELECT *
    FROM prosandcons
    WHERE company_id='{ticker}'
    """,
    conn
)

if not pc.empty:

    st.subheader("✅ Pros")

    pros = str(pc.iloc[0]["pros"]).split(";")

    for p in pros:
        if p.strip():
            st.success(p.strip())

    st.subheader("❌ Cons")

    cons = str(pc.iloc[0]["cons"]).split(";")

    for c in cons:
        if c.strip():
            st.error(c.strip())

conn.close()