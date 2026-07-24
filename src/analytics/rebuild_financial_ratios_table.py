import sqlite3

conn = sqlite3.connect("db/nifty100.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS financial_ratios")

cursor.execute("""
CREATE TABLE financial_ratios (

    company_id TEXT,
    year INTEGER,

    net_profit_margin REAL,
    operating_profit_margin REAL,

    roe REAL,
    roce REAL,
    roa REAL,

    debt_to_equity REAL,
    interest_coverage REAL,
    asset_turnover REAL,

    net_debt REAL,
    debt_free TEXT,
    high_leverage_flag TEXT,

    revenue_cagr_3y REAL,
    revenue_cagr_5y REAL,
    revenue_cagr_10y REAL,

    pat_cagr_3y REAL,
    pat_cagr_5y REAL,
    pat_cagr_10y REAL,

    eps_cagr_3y REAL,
    eps_cagr_5y REAL,
    eps_cagr_10y REAL,

    free_cash_flow REAL,
    cashflow_quality REAL,
    cashflow_status TEXT
)
""")

conn.commit()

conn.close()

print("financial_ratios table recreated successfully.")