import sqlite3
import pandas as pd
import numpy as np
import os

# ----------------------------------
# Configuration
# ----------------------------------

DB_PATH = "db/nifty100.db"
OUTPUT_PATH = "outputs"

os.makedirs(OUTPUT_PATH, exist_ok=True)

# ----------------------------------
# Connect Database
# ----------------------------------

conn = sqlite3.connect(DB_PATH)

query = """
SELECT
    c.id,
    c.company_name,
    s.broad_sector,

    mc.market_cap_crore,
    mc.pe_ratio,
    mc.pb_ratio,
    mc.ev_ebitda,
    mc.dividend_yield_pct,

    fr.free_cash_flow,
    fr.roe,
    fr.roce

FROM companies c

JOIN sectors s
ON c.id = s.company_id

JOIN market_cap mc
ON c.id = mc.company_id

JOIN financial_ratios fr
ON c.id = fr.company_id

WHERE mc.year = (
    SELECT MAX(year)
    FROM market_cap m2
    WHERE m2.company_id = mc.company_id
)

AND fr.year = (
    SELECT MAX(year)
    FROM financial_ratios f2
    WHERE f2.company_id = fr.company_id
)
"""

df = pd.read_sql(query, conn)
conn.close()

print("=" * 60)
print("VALUATION ANALYSIS")
print("=" * 60)
print(f"Companies Loaded : {len(df)}")

# ----------------------------------
# Calculate FCF Yield
# ----------------------------------

df["fcf_yield_pct"] = np.where(
    df["market_cap_crore"] > 0,
    (df["free_cash_flow"] / df["market_cap_crore"]) * 100,
    np.nan
)

df["fcf_yield_pct"] = df["fcf_yield_pct"].round(2)

print("✓ FCF Yield Calculated")

# ----------------------------------
# Sector Median Valuation
# ----------------------------------

sector_median = (
    df.groupby("broad_sector")[[
        "pe_ratio",
        "pb_ratio",
        "ev_ebitda"
    ]]
    .median()
    .reset_index()
)

sector_median.rename(
    columns={
        "pe_ratio": "sector_median_pe",
        "pb_ratio": "sector_median_pb",
        "ev_ebitda": "sector_median_ev_ebitda"
    },
    inplace=True
)

print("✓ Sector Median Calculated")

# ----------------------------------
# Merge
# ----------------------------------

df = df.merge(
    sector_median,
    on="broad_sector",
    how="left"
)

print("✓ Sector Median Merged")

# ----------------------------------
# PE vs Sector %
# ----------------------------------

df["pe_vs_sector_pct"] = (
    df["pe_ratio"] /
    df["sector_median_pe"]
) * 100

df["pe_vs_sector_pct"] = df["pe_vs_sector_pct"].round(2)

print("✓ PE Comparison Calculated")

# ----------------------------------
# Valuation Flag
# ----------------------------------

def valuation_flag(row):

    if pd.isna(row["sector_median_pe"]):
        return "Fair"

    if row["pe_ratio"] > row["sector_median_pe"] * 1.5:
        return "Caution"

    elif row["pe_ratio"] < row["sector_median_pe"] * 0.7:
        return "Discount"

    else:
        return "Fair"

df["valuation_flag"] = df.apply(
    valuation_flag,
    axis=1
)

print("✓ Valuation Flags Assigned")

# ----------------------------------
# Round Numeric Columns
# ----------------------------------

numeric_columns = [
    "market_cap_crore",
    "pe_ratio",
    "pb_ratio",
    "ev_ebitda",
    "fcf_yield_pct",
    "roe",
    "roce",
    "sector_median_pe",
    "pe_vs_sector_pct"
]

df[numeric_columns] = df[numeric_columns].round(2)

# ----------------------------------
# Prepare Summary
# ----------------------------------

summary = df[
    [
        "id",
        "company_name",
        "broad_sector",
        "pe_ratio",
        "pb_ratio",
        "ev_ebitda",
        "fcf_yield_pct",
        "sector_median_pe",
        "pe_vs_sector_pct",
        "valuation_flag"
    ]
].sort_values(
    by="fcf_yield_pct",
    ascending=False
)

print("\nTop 10 Companies by FCF Yield\n")
print(summary.head(10))

# ----------------------------------
# Export Reports
# ----------------------------------

summary.to_excel(
    os.path.join(
        OUTPUT_PATH,
        "valuation_summary.xlsx"
    ),
    index=False
)

df.to_csv(
    os.path.join(
        OUTPUT_PATH,
        "valuation_flags.csv"
    ),
    index=False
)

print("\nReports Exported Successfully")
print(f"Excel : {OUTPUT_PATH}/valuation_summary.xlsx")
print(f"CSV   : {OUTPUT_PATH}/valuation_flags.csv")

print("\nSprint 4 - Valuation Module Completed")