import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
company_id,
year,
net_profit_margin,
operating_profit_margin,
roe,
roce,
roa,
debt_to_equity,
interest_coverage,
asset_turnover,
free_cash_flow,
cashflow_quality,
cashflow_status
FROM financial_ratios
LIMIT 20;
"""

df = pd.read_sql_query(query, conn)

print(df)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

conn.close()