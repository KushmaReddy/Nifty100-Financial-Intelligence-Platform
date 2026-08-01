import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

ratios = pd.read_csv("src/reports/financial_ratios.csv")
cagr = pd.read_csv("src/reports/cagr_report.csv")
cashflow = pd.read_csv("src/reports/cashflow_kpis.csv")

financial_ratios = ratios.merge(
    cagr,
    on="company_id",
    how="left"
)

financial_ratios = financial_ratios.merge(
    cashflow[
        [
            "company_id",
            "free_cash_flow",
            "cashflow_quality",
            "cashflow_status"
        ]
    ],
    on="company_id",
    how="left"
)

financial_ratios = financial_ratios[
    [
        "company_id",
        "year",
        "net_profit_margin",
        "operating_profit_margin",
        "roe",
        "roce",
        "roa",
        "debt_to_equity",
        "interest_coverage",
        "asset_turnover",
        "net_debt",
        "debt_free",
        "high_leverage_flag",
        "revenue_cagr_3y",
        "revenue_cagr_5y",
        "revenue_cagr_10y",
        "pat_cagr_3y",
        "pat_cagr_5y",
        "pat_cagr_10y",
        "eps_cagr_3y",
        "eps_cagr_5y",
        "eps_cagr_10y",
        "free_cash_flow",
        "cashflow_quality",
        "cashflow_status"
    ]
]

financial_ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)
print(financial_ratios.head())

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM financial_ratios"
)

print("\nRows inserted into financial_ratios:",
      cursor.fetchone()[0])

conn.close()