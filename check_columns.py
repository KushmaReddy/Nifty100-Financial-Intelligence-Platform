import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

financial_ratios = pd.read_sql(
    "SELECT * FROM financial_ratios LIMIT 5",
    conn
)

print(financial_ratios.columns.tolist())

conn.close()