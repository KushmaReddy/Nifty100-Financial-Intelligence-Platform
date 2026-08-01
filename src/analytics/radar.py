import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------

DB_PATH = Path("db/nifty100.db")
OUTPUT_PATH = Path("reports/radar_charts")

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Connect Database
# -----------------------------

conn = sqlite3.connect(DB_PATH)

# -----------------------------
# Load Peer Percentiles
# -----------------------------

peer_percentiles = pd.read_sql(
    "SELECT * FROM peer_percentiles",
    conn
)

conn.close()

print("\nPeer Percentiles Shape :", peer_percentiles.shape)

print("\nPeer Percentiles Preview\n")
print(peer_percentiles.head())

# -----------------------------
# Convert Long Format to Wide Format
# -----------------------------
# Each company becomes one row
# Each metric becomes one column

radar_data = (
    peer_percentiles
    .pivot_table(
        index=[
            "company_id",
            "peer_group_name",
            "year"
        ],
        columns="metric",
        values="percentile_rank"
    )
    .reset_index()
)

print("\nRadar Data Shape :", radar_data.shape)

print("\nRadar Data Preview\n")
print(radar_data.head())

# -----------------------------
# Metrics Required
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
# Calculate Peer Group Average
# -----------------------------

peer_average = (
    radar_data
    .groupby("peer_group_name")[metrics]
    .mean()
    .reset_index()
)

print("\nPeer Group Average Shape :", peer_average.shape)

print("\nPeer Group Average Preview\n")
print(peer_average.head())

# -----------------------------
# Select One Company
# -----------------------------

company = "AXISBANK"

company_data = radar_data[
    radar_data["company_id"] == company
].iloc[0]

peer_name = company_data["peer_group_name"]

peer_data = peer_average[
    peer_average["peer_group_name"] == peer_name
].iloc[0]

# -----------------------------
# Prepare Values
# -----------------------------

company_values = (
    company_data[metrics]
    .fillna(0)
    .tolist()
)

peer_values = (
    peer_data[metrics]
    .fillna(0)
    .tolist()
)

print("\nCompany :", company)

print("\nCompany Values\n")
print(company_values)

print("\nPeer Group :", peer_name)

print("\nPeer Average Values\n")
print(peer_values)
# -----------------------------
# Radar Chart Function
# -----------------------------

def create_radar_chart(company_name,
                       company_values,
                       peer_values,
                       metrics):

    labels = metrics

    angles = np.linspace(
        0,
        2 * np.pi,
        len(labels),
        endpoint=False
    ).tolist()

    company_values = company_values + company_values[:1]
    peer_values = peer_values + peer_values[:1]
    angles = angles + angles[:1]

    fig = plt.figure(figsize=(8, 8))

    ax = plt.subplot(111, polar=True)

    ax.plot(
        angles,
        company_values,
        linewidth=2,
        label=company_name
    )

    ax.fill(
        angles,
        company_values,
        alpha=0.25
    )

    ax.plot(
        angles,
        peer_values,
        linewidth=2,
        linestyle="--",
        label="Peer Average"
    )

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_ylim(0, 100)

    plt.title(company_name)

    plt.legend(loc="upper right")

    plt.savefig(
        OUTPUT_PATH / f"{company_name}_radar.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# -----------------------------
# Generate Radar Charts for All Companies
# -----------------------------

count = 0

for _, row in radar_data.iterrows():

    company = row["company_id"]
    peer_name = row["peer_group_name"]

    if pd.isna(peer_name):
        continue

    company_values = (
        row[metrics]
        .fillna(0)
        .tolist()
    )

    peer_row = peer_average[
        peer_average["peer_group_name"] == peer_name
    ]

    if peer_row.empty:
        continue

    peer_values = (
        peer_row.iloc[0][metrics]
        .fillna(0)
        .tolist()
    )

    create_radar_chart(
        company,
        company_values,
        peer_values,
        metrics
    )

    count += 1

print(f"\n{count} radar charts created successfully!")
count = 0

for _, row in radar_data.iterrows():

    company = row["company_id"]
    peer_name = row["peer_group_name"]

    if pd.isna(peer_name):
        continue

    company_values = (
        row[metrics]
        .fillna(0)
        .tolist()
    )

    peer_row = peer_average[
        peer_average["peer_group_name"] == peer_name
    ]

    if peer_row.empty:
        continue

    peer_values = (
        peer_row.iloc[0][metrics]
        .fillna(0)
        .tolist()
    )

    create_radar_chart(
        company,
        company_values,
        peer_values,
        metrics
    )

    count += 1

print(f"\n{count} radar charts created successfully!")