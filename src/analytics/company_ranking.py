import sqlite3
from pathlib import Path

import pandas as pd

# ------------------------------------
# Configuration
# ------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_PATH = PROJECT_ROOT / "db" / "nifty100.db"

OUTPUT_PATH = PROJECT_ROOT / "output"

OUTPUT_PATH.mkdir(exist_ok=True)

# ------------------------------------
# Load Data
# ------------------------------------

print("Loading financial data...")

conn = sqlite3.connect(DB_PATH)

query = """
SELECT
    fr.company_id,
    fr.year,
    fr.roe,
    fr.roce,
    fr.debt_to_equity,
    fr.interest_coverage,
    fr.free_cash_flow,
    fr.debt_free,
    fr.high_leverage_flag,
    mc.pe_ratio,
    mc.pb_ratio,
    mc.dividend_yield_pct
FROM financial_ratios fr

LEFT JOIN market_cap mc
ON fr.company_id = mc.company_id
AND fr.year = mc.year
"""

df = pd.read_sql(query, conn)

conn.close()

print(f"Rows Loaded : {len(df)}")
# ------------------------------------
# Company Score
# ------------------------------------

def calculate_score(row):

    score = 0

    if row["roe"] >= 20:
        score += 20
    elif row["roe"] >= 15:
        score += 15
    elif row["roe"] >= 10:
        score += 10

    if row["roce"] >= 20:
        score += 20
    elif row["roce"] >= 15:
        score += 15
    elif row["roce"] >= 10:
        score += 10

    if row["debt_to_equity"] <= 0.5:
        score += 15
    elif row["debt_to_equity"] <= 1:
        score += 10

    if (
        pd.notna(row["interest_coverage"])
        and row["interest_coverage"] >= 5
    ):
        score += 15

    if row["free_cash_flow"] > 0:
        score += 10

    if row["debt_free"] == "Yes":
        score += 10

    if row["high_leverage_flag"] == 0:
        score += 10

    return score
# ------------------------------------
# Apply Score
# ------------------------------------

df["score"] = df.apply(
    calculate_score,
    axis=1
)

# Keep latest year only
df = (
    df.sort_values("year")
      .groupby("company_id")
      .tail(1)
)

# Rating

def rating(score):

    if score >= 80:
        return "Excellent"

    if score >= 60:
        return "Good"

    if score >= 40:
        return "Average"

    return "Weak"

df["rating"] = df["score"].apply(rating)

ranking = (
    df.sort_values(
        by="score",
        ascending=False
    )
)

print("\nTop 10 Companies\n")

print(
    ranking[
        [
            "company_id",
            "score",
            "rating"
        ]
    ].head(10)
)

ranking.to_excel(
    OUTPUT_PATH / "company_rankings.xlsx",
    index=False
)

print("\nReport Generated Successfully")
print(OUTPUT_PATH / "company_rankings.xlsx")