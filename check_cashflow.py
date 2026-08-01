import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

cashflow = pd.read_sql("SELECT * FROM cashflow LIMIT 5", conn)

print("===== COLUMNS =====")
for col in cashflow.columns:
    print(col)

print("\n===== FIRST 5 ROWS =====")
print(cashflow)

conn.close()