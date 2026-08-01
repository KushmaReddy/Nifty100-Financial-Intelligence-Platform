import sqlite3
import yaml
import pandas as pd
from pathlib import Path

from src.screener.scoring import calculate_composite_score

from src.screener.presets import (
    quality_compounder,
    growth_accelerator,
    debt_free_bluechip,
    value_pick,
    dividend_champion,
    turnaround_watch
)
# ----------------------------------------------------
# Paths
# ----------------------------------------- -----------

DB_PATH = Path("db/nifty100.db")
CONFIG_PATH = Path("config/screener_config.yaml")

# ----------------------------------------------------
# Load Config
# ----------------------------------------------------

with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)

filters = config["filters"]

# ----------------------------------------------------
# Connect Database
# ----------------------------------------------------

conn = sqlite3.connect(DB_PATH)

# ----------------------------------------------------
# Load Tables
# ----------------------------------------------------

financial_ratios = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

sectors = pd.read_sql(
    """
    SELECT company_id,
           broad_sector
    FROM sectors
    """,
    conn
)

market_cap = pd.read_sql(
    """
    SELECT
        company_id,
        year,
        pe_ratio,
        pb_ratio,
        dividend_yield_pct
    FROM market_cap
    """,
    conn
)

conn.close()

# ----------------------------------------------------
# Keep Latest Year
# ----------------------------------------------------

financial_ratios["year"] = financial_ratios["year"].astype(int)

financial_ratios = (
    financial_ratios
    .sort_values("year")
    .groupby("company_id", as_index=False)
    .last()
)

market_cap["year"] = market_cap["year"].astype(int)

market_cap = (
    market_cap
    .sort_values("year")
    .groupby("company_id", as_index=False)
    .last()
)

# ----------------------------------------------------
# Merge Tables
# ----------------------------------------------------

financial_ratios = financial_ratios.merge(
    sectors,
    on="company_id",
    how="left"
)

financial_ratios = financial_ratios.merge(
    market_cap,
    on=["company_id", "year"],
    how="left"
)

print("Total Companies :", len(financial_ratios))

# ----------------------------------------------------
# Select Screener
# ----------------------------------------------------
PRESET = "turnaround"

if PRESET == "quality":
    filtered_df = quality_compounder(financial_ratios)
    title = "QUALITY COMPOUNDER"

elif PRESET == "growth":
    filtered_df = growth_accelerator(financial_ratios)
    title = "GROWTH ACCELERATOR"

elif PRESET == "debtfree":
    filtered_df = debt_free_bluechip(financial_ratios)
    title = "DEBT FREE BLUE CHIP"

elif PRESET == "value":
    filtered_df = value_pick(financial_ratios)
    title = "VALUE PICK"

elif PRESET == "dividend":
    filtered_df = dividend_champion(financial_ratios)
    title = "DIVIDEND CHAMPION"

elif PRESET == "turnaround":
    filtered_df = turnaround_watch(financial_ratios)
    title = "TURNAROUND WATCH"

else:
    raise ValueError("Invalid preset selected.")

filtered_df = filtered_df.copy()
filtered_df = calculate_composite_score(filtered_df)

# ----------------------------------------------------
# Ranking
# ----------------------------------------------------

filtered_df = filtered_df.sort_values(
    by="composite_score",
    ascending=False
)

# ----------------------------------------------------
# Output
# ----------------------------------------------------

print("\n========================================")
print(f" {title} SCREENER")
print("========================================")

print(f"\nCompanies Matched : {len(filtered_df)}")

print("\nTop 10 Companies\n")

columns = [
    "company_id",
    "year",
    "broad_sector",
    "roe",
    "debt_to_equity",
    "free_cash_flow",
]

# Show valuation columns only for Value Pick
if PRESET == "value":
    columns.extend([
        "pe_ratio",
        "pb_ratio",
        "dividend_yield_pct"
    ])

columns.append("composite_score")

print(filtered_df[columns].head(10))

print("\nScreener executed successfully.")

from pathlib import Path

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

filtered_df.to_csv(
    output_dir / "screener_results.csv",
    index=False
)

print("\nResults saved to outputs/screener_results.csv")