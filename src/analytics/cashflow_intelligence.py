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
# Load Cash Flow Data
# -----------------------------

print("Loading cashflow table...")

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql(
    """
    SELECT
        company_id,
        year,
        operating_activity,
        investing_activity,
        financing_activity,
        net_cash_flow
    FROM cashflow
    """,
    conn
)

conn.close()

print(f"Rows Loaded : {len(df)}")

# -----------------------------
# Cash Flow Intelligence
# -----------------------------

def classify_cashflow(row):

    insights = []

    if row["operating_activity"] > 0:
        insights.append("Strong Operating Cash Flow")
    else:
        insights.append("Weak Operating Cash Flow")

    if row["investing_activity"] < 0:
        insights.append("Investing for Future Growth")
    else:
        insights.append("Positive Investing Cash Flow")

    if row["financing_activity"] < 0:
        insights.append("Debt Repayment / Dividend Distribution")
    else:
        insights.append("External Financing Raised")

    if row["net_cash_flow"] > 0:
        insights.append("Positive Net Cash Flow")
    else:
        insights.append("Negative Net Cash Flow")

    return " | ".join(insights)

# -----------------------------
# Apply Intelligence
# -----------------------------

df["cashflow_intelligence"] = df.apply(
    classify_cashflow,
    axis=1
)

# -----------------------------
# Preview
# -----------------------------

print("\nPreview\n")

print(
    df[
        [
            "company_id",
            "year",
            "cashflow_intelligence"
        ]
    ].head()
)

# -----------------------------
# Export
# -----------------------------

output_file = OUTPUT_PATH / "cashflow_intelligence.xlsx"

df.to_excel(
    output_file,
    index=False
)

print("\nReport Generated Successfully")

print(output_file)

print("\nSprint 5 - Day 31 Completed")