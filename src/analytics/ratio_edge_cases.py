import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    fr.company_id,
    fr.year,
    fr.net_profit_margin,
    fr.operating_profit_margin,
    fr.roe,
    fr.roce,
    fr.debt_to_equity,
    fr.interest_coverage,
    pl.sales,
    pl.interest,
    bs.equity_capital,
    bs.reserves

FROM financial_ratios fr

JOIN profitandloss pl
ON fr.company_id = pl.company_id
AND fr.year = pl.year

JOIN balancesheet bs
ON fr.company_id = bs.company_id
AND fr.year = bs.year
"""

df = pd.read_sql_query(query, conn)

logs = []

for _, row in df.iterrows():

    if row["sales"] == 0:
        logs.append([
            row["company_id"],
            row["year"],
            "Sales = 0",
            "Net Profit Margin / Operating Profit Margin"
        ])

    if row["interest"] == 0:
        logs.append([
            row["company_id"],
            row["year"],
            "Interest = 0",
            "Interest Coverage"
        ])

    equity = (row["equity_capital"] or 0) + (row["reserves"] or 0)

    if equity <= 0:
        logs.append([
            row["company_id"],
            row["year"],
            "Negative Equity",
            "ROE"
        ])

log_df = pd.DataFrame(
    logs,
    columns=[
        "company_id",
        "year",
        "edge_case",
        "reason"
    ]
)

log_df.to_csv(
    "src/reports/ratio_edge_cases.log",
    index=False
)

print(log_df.head())
print()
print("Total edge cases:", len(log_df))

conn.close()