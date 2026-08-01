import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    company_id,
    year,
    COUNT(*) AS cnt
FROM financial_ratios
GROUP BY company_id, year
HAVING COUNT(*) > 1;
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()