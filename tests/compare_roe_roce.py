import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

financial_ratios = pd.read_sql_query("""
SELECT
    company_id,
    year,
    roe,
    roce
FROM financial_ratios
WHERE year = (
    SELECT MAX(year)
    FROM financial_ratios f2
    WHERE f2.company_id = financial_ratios.company_id
)
""", conn)

companies = pd.read_sql_query("""
SELECT
    id AS company_id,
    roe_percentage,
    roce_percentage
FROM companies
""", conn)

conn.close()

comparison = pd.merge(
    financial_ratios,
    companies,
    on="company_id",
    how="left"
)

comparison["roe_difference"] = (
    comparison["roe"] - comparison["roe_percentage"]
).abs()

comparison["roce_difference"] = (
    comparison["roce"] - comparison["roce_percentage"]
).abs()

THRESHOLD = 1

comparison["roe_status"] = comparison["roe_difference"].apply(
    lambda x: "PASS" if pd.notna(x) and x <= THRESHOLD else "CHECK"
)

comparison["roce_status"] = comparison["roce_difference"].apply(
    lambda x: "PASS" if pd.notna(x) and x <= THRESHOLD else "CHECK"
)

comparison.to_csv(
    "src/reports/roe_roce_validation.csv",
    index=False
)

print("\nROE & ROCE Validation\n")

print("Total Records :", len(comparison))
print("ROE Passed :", (comparison["roe_status"] == "PASS").sum())
print("ROE Need Review :", (comparison["roe_status"] == "CHECK").sum())
print("ROCE Passed :", (comparison["roce_status"] == "PASS").sum())
print("ROCE Need Review :", (comparison["roce_status"] == "CHECK").sum())

print("\nValidation report saved successfully.")