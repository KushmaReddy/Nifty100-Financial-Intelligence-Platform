import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT company_name, roe_percentage
FROM companies
WHERE roe_percentage > 30
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()
import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()
import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT face_value, COUNT(*) AS total_companies
FROM companies
GROUP BY face_value
ORDER BY total_companies DESC
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()