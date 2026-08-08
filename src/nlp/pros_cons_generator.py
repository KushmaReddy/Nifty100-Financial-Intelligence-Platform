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
# Load Pros & Cons
# -----------------------------

print("Loading prosandcons table...")

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql(
    """
    SELECT
        company_id,
        pros,
        cons
    FROM prosandcons
    """,
    conn
)

conn.close()

print(f"Rows Loaded : {len(df)}")

# -----------------------------
# Replace Missing Values
# -----------------------------

df["pros"] = df["pros"].fillna("").astype(str).str.strip()
df["cons"] = df["cons"].fillna("").astype(str).str.strip()

# -----------------------------
# Group by Company
# -----------------------------

records = []

for company_id, group in df.groupby("company_id"):

    pros = [
        p for p in group["pros"]
        if p != ""
    ]

    cons = [
        c for c in group["cons"]
        if c != ""
    ]

    records.append({
        "company_id": company_id,
        "pros": "\n".join(pros),
        "cons": "\n".join(cons),
        "total_pros": len(pros),
        "total_cons": len(cons)
    })

# -----------------------------
# Create DataFrame
# -----------------------------

result = pd.DataFrame(records)

print("\nPreview\n")

print(result.head())

# -----------------------------
# Save Output
# -----------------------------

output_file = OUTPUT_PATH / "pros_cons_generated.csv"

result.to_csv(
    output_file,
    index=False
)

print("\nFile Generated Successfully")

print(output_file)

print("\nDay 30 Completed")