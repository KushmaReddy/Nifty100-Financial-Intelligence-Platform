import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "market_cap"
]

for table in tables:
    print(f"\n===== {table} =====")
    try:
        df = pd.read_sql(f"SELECT * FROM {table} LIMIT 5", conn)
        print(df.columns.tolist())
    except Exception as e:
        print(e)

conn.close()