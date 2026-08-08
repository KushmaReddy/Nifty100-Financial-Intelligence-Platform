import sqlite3
from pathlib import Path

import pandas as pd

from tearsheet import generate_tearsheet


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_PATH = PROJECT_ROOT / "db" / "nifty100.db"


conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql(
    """
    SELECT id
    FROM companies
    ORDER BY id
    """,
    conn
)

conn.close()


print(f"\nTotal Companies : {len(companies)}\n")


success = 0
failed = 0


for company_id in companies["id"]:

    try:

        generate_tearsheet(company_id)

        success += 1

    except Exception as e:

        print(f"Failed : {company_id}")

        print(e)

        failed += 1


print("\n----------------------------")

print("Batch Generation Completed")

print("Successful :", success)

print("Failed     :", failed)

print("----------------------------")