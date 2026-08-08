import sqlite3
from pathlib import Path

import pandas as pd

# -----------------------------
# Configuration
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_PATH = PROJECT_ROOT / "db" / "nifty100.db"

OUTPUT_PATH = PROJECT_ROOT / "output"

OUTPUT_PATH.mkdir(exist_ok=True)

# -----------------------------
# Load Financial Ratios
# -----------------------------

print("Loading financial ratios...")

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql(
    """
    SELECT
        company_id,
        year,
        roe,
        roce,
        debt_to_equity,
        interest_coverage,
        free_cash_flow,
        debt_free,
        high_leverage_flag
    FROM financial_ratios
    """,
    conn
)

conn.close()

print(f"Rows Loaded : {len(df)}")

# -----------------------------
# Financial Distress Rules
# -----------------------------

def detect_distress(row):

    alerts = []

    if row["roe"] < 10:
        alerts.append("Low ROE")

    if row["roce"] < 10:
        alerts.append("Low ROCE")

    if row["debt_to_equity"] > 2:
        alerts.append("High Debt")

    if (
        pd.notna(row["interest_coverage"])
        and row["interest_coverage"] < 2
    ):
        alerts.append("Weak Interest Coverage")

    if row["free_cash_flow"] < 0:
        alerts.append("Negative Free Cash Flow")

    if row["debt_free"] == "No":
        alerts.append("Company Has Debt")

    if row["high_leverage_flag"] == 1:
        alerts.append("High Leverage")

    if len(alerts) == 0:
        alerts.append("Financially Healthy")

    return " | ".join(alerts)

# -----------------------------
# Apply Rules
# -----------------------------

df["distress_status"] = df.apply(
    detect_distress,
    axis=1
)

# -----------------------------
# Distress Score
# -----------------------------

df["distress_score"] = (
    df["distress_status"]
    .str.count(r"\|") + 1
)

healthy_mask = df["distress_status"] == "Financially Healthy"

df.loc[
    healthy_mask,
    "distress_score"
] = 0

# -----------------------------
# Preview
# -----------------------------

print("\nPreview\n")

print(
    df[
        [
            "company_id",
            "year",
            "distress_status",
            "distress_score"
        ]
    ].head()
)

# -----------------------------
# Export
# -----------------------------

output_file = OUTPUT_PATH / "distress_alerts.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nReport Generated Successfully")

print(output_file)

print("\nSprint 5 - Day 32 Completed")