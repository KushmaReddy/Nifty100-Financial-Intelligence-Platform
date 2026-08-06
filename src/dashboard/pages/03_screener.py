import streamlit as st
import sqlite3
import pandas as pd

from src.screener.presets import (
    quality_compounder,
    growth_accelerator,
    debt_free_bluechip,
    value_pick,
    dividend_champion,
    turnaround_watch
)

st.title("🔍 Stock Screener")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    c.id,
    c.company_name,
    s.broad_sector,
    fr.roe,
    fr.roce,
    fr.debt_to_equity,
    fr.revenue_cagr_5y,
    fr.net_profit_margin,
    fr.free_cash_flow,
    mc.pe_ratio,
    mc.pb_ratio,
    mc.dividend_yield_pct

FROM companies c

JOIN financial_ratios fr
ON c.id = fr.company_id

JOIN market_cap mc
ON c.id = mc.company_id

JOIN sectors s
ON c.id = s.company_id

WHERE fr.year = (
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
# Sidebar Filters
# -----------------------------
st.sidebar.header("📊 Filters")

preset = st.sidebar.selectbox(
    "📌 Preset Screener",
    [
        "Custom",
        "Quality Compounder",
        "Growth Accelerator",
        "Debt-Free Blue Chip",
        "Value Pick",
        "Dividend Champion",
        "Turnaround Watch"
    ]
)

company_search = st.sidebar.text_input(
    "🔍 Search Company",
    ""
)

roe = st.sidebar.slider("Minimum ROE", 0.0, 100.0, 0.0)
roce = st.sidebar.slider("Minimum ROCE", 0.0, 100.0, 0.0)
de = st.sidebar.slider("Maximum Debt/Equity", 0.0, 5.0, 5.0)
cagr = st.sidebar.slider("Minimum Revenue CAGR (5Y)", -20.0, 50.0, 0.0)
npm = st.sidebar.slider("Minimum Net Profit Margin", -20.0, 60.0, 0.0)

fcf = st.sidebar.slider(
    "Minimum Free Cash Flow",
    float(df["free_cash_flow"].min()),
    float(df["free_cash_flow"].max()),
    0.0
)

pe = st.sidebar.slider(
    "Maximum P/E Ratio",
    float(df["pe_ratio"].min()),
    float(df["pe_ratio"].max()),
    float(df["pe_ratio"].max())
)

pb = st.sidebar.slider(
    "Maximum P/B Ratio",
    float(df["pb_ratio"].min()),
    float(df["pb_ratio"].max()),
    float(df["pb_ratio"].max())
)

dividend = st.sidebar.slider(
    "Minimum Dividend Yield",
    float(df["dividend_yield_pct"].min()),
    float(df["dividend_yield_pct"].max()),
    0.0
)

# -----------------------------
# Manual Filters
# -----------------------------
filtered = df[
    (df["roe"] >= roe) &
    (df["roce"] >= roce) &
    (df["debt_to_equity"] <= de) &
    (df["revenue_cagr_5y"] >= cagr) &
    (df["net_profit_margin"] >= npm) &
    (df["free_cash_flow"] >= fcf) &
    (df["pe_ratio"] <= pe) &
    (df["pb_ratio"] <= pb) &
    (df["dividend_yield_pct"] >= dividend)
]

# -----------------------------
# Company Search
# -----------------------------
if company_search:
    filtered = filtered[
        filtered["company_name"].str.contains(
            company_search,
            case=False,
            na=False
        )
    ]

# -----------------------------
# Preset Screeners
# -----------------------------
if preset == "Quality Compounder":
    filtered = quality_compounder(filtered)

elif preset == "Growth Accelerator":
    filtered = growth_accelerator(filtered)

elif preset == "Debt-Free Blue Chip":
    filtered = debt_free_bluechip(filtered)

elif preset == "Value Pick":
    filtered = value_pick(filtered)

elif preset == "Dividend Champion":
    filtered = dividend_champion(filtered)

elif preset == "Turnaround Watch":
    filtered = turnaround_watch(filtered)

# -----------------------------
# Composite Score
# -----------------------------
filtered["composite_score"] = (
    filtered["roe"] * 0.30 +
    filtered["roce"] * 0.25 +
    filtered["revenue_cagr_5y"] * 0.20 +
    filtered["net_profit_margin"] * 0.15 +
    (filtered["free_cash_flow"] / 1000) * 0.10
).round(2)

# -----------------------------
# Sort & Rank
# -----------------------------
filtered = filtered.sort_values(
    by="composite_score",
    ascending=False
).reset_index(drop=True)

filtered.index = filtered.index + 1

# -----------------------------
# Display
# -----------------------------
st.subheader(f"✅ {len(filtered)} Companies Found")

st.info(
    f"Showing {len(filtered)} companies that match the selected filters."
)

display_df = filtered[
    [
        "company_name",
        "broad_sector",
        "roe",
        "roce",
        "pe_ratio",
        "pb_ratio",
        "dividend_yield_pct",
        "composite_score"
    ]
]

st.dataframe(
    display_df,
    use_container_width=True
)

# -----------------------------
# Download CSV
# -----------------------------
csv = display_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="screener_results.csv",
    mime="text/csv"
)