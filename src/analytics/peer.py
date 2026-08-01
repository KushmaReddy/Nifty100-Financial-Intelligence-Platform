import sqlite3
import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------

DB_PATH = Path("db/nifty100.db")
RAW_DATA_PATH = Path("data/raw")

# -----------------------------
# Connect to Database
# -----------------------------

conn = sqlite3.connect(DB_PATH)

# -----------------------------
# Load Tables
# -----------------------------

financial_ratios = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

companies = pd.read_sql(
    "SELECT * FROM companies",
    conn
)

conn.close()

# -----------------------------
# Load Peer Groups Excel
# -----------------------------

peer_groups = pd.read_excel(
    RAW_DATA_PATH / "peer_groups.xlsx"
)

print("\nFinancial Ratios Shape :", financial_ratios.shape)
print("Companies Shape        :", companies.shape)
print("Peer Groups Shape      :", peer_groups.shape)

print("\nPeer Groups Preview\n")
print(peer_groups.head())

# -----------------------------
# Merge Peer Groups
# -----------------------------

peer_data = financial_ratios.merge(
    peer_groups,
    on="company_id",
    how="left"
)

print("\nMerged Data Shape :", peer_data.shape)

print("\nMerged Preview\n")
print(
    peer_data[
        [
            "company_id",
            "year",
            "peer_group_name",
            "is_benchmark"
        ]
    ].head(15)
)

# -----------------------------
# Keep Latest Year
# -----------------------------

peer_data = (
    peer_data
    .sort_values("year")
    .groupby("company_id", as_index=False)
    .last()
)

print("\nLatest Year Records :", len(peer_data))

print("\nLatest Data Preview\n")
print(
    peer_data[
        [
            "company_id",
            "year",
            "peer_group_name",
            "roe"
        ]
    ].head(15)
)

# -----------------------------
# Metrics for Percentile Ranking
# -----------------------------

metrics = [
    "roe",
    "roce",
    "net_profit_margin",
    "debt_to_equity",
    "free_cash_flow",
    "pat_cagr_5y",
    "revenue_cagr_5y",
    "eps_cagr_5y",
    "interest_coverage",
    "asset_turnover"
]

# -----------------------------
# Metrics for Percentile Ranking
# -----------------------------

metrics = [
    "roe",
    "roce",
    "net_profit_margin",
    "debt_to_equity",
    "free_cash_flow",
    "pat_cagr_5y",
    "revenue_cagr_5y",
    "eps_cagr_5y",
    "interest_coverage",
    "asset_turnover"
]

peer_percentiles = []

# -----------------------------
# Calculate Percentiles
# -----------------------------

for metric in metrics:

    temp = peer_data.dropna(
        subset=["peer_group_name", metric]
    ).copy()

    # Lower Debt-to-Equity is better
    if metric == "debt_to_equity":
        temp["percentile_rank"] = (
            1
            - temp.groupby("peer_group_name")[metric]
            .rank(method="average", pct=True)
        ) * 100
    else:
        temp["percentile_rank"] = (
            temp.groupby("peer_group_name")[metric]
            .rank(method="average", pct=True)
        ) * 100

    temp["metric"] = metric
    temp["value"] = temp[metric]

    peer_percentiles.append(
        temp[
            [
                "company_id",
                "peer_group_name",
                "metric",
                "value",
                "percentile_rank",
                "year"
            ]
        ]
    )

# -----------------------------
# Final DataFrame
# -----------------------------

peer_percentiles = pd.concat(
    peer_percentiles,
    ignore_index=True
)

print("\nPeer Percentiles Shape :", peer_percentiles.shape)

print("\nPeer Percentiles Preview\n")

print(peer_percentiles.head(20))
# -----------------------------
# Save to SQLite
# -----------------------------

conn = sqlite3.connect(DB_PATH)

peer_percentiles.to_sql(
    "peer_percentiles",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\npeer_percentiles table created successfully!")
print("\nRows per Metric:\n")
print(peer_percentiles["metric"].value_counts())