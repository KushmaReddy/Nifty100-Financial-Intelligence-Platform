import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    fr.company_id,
    fr.year,
    fr.roe,
    fr.operating_profit_margin,
    fr.net_profit_margin,
    fr.debt_to_equity,
    fr.interest_coverage,
    pl.sales,
    pl.net_profit,
    pl.operating_profit,
    pl.interest,
    bs.equity_capital,
    bs.reserves,
    bs.borrowings
FROM financial_ratios fr

JOIN profitandloss pl
ON fr.company_id = pl.company_id
AND fr.year = pl.year

JOIN balancesheet bs
ON fr.company_id = bs.company_id
AND fr.year = bs.year

LIMIT 10
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()