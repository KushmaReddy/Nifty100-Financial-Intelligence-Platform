import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql_query(
    "PRAGMA table_info(cashflow);",
    conn
)

print(df)

conn.close()