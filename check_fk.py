import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_key_check;")

rows = cursor.fetchall()

if len(rows) == 0:
    print("✅ No Foreign Key Violations")
else:
    print("Foreign Key Violations:")
    for row in rows:
        print(row)

conn.close()