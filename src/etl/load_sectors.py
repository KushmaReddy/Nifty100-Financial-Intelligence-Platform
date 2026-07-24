import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"
EXCEL_PATH = "data/raw/sectors.xlsx"


def load_sectors():

    # Read Excel file
    sectors = pd.read_excel(EXCEL_PATH)

    # Standardize column names
    sectors.columns = (
        sectors.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("\nColumns:")
    print(sectors.columns.tolist())

    print("\nFirst 5 rows:")
    print(sectors.head())

    # Connect to SQLite
    conn = sqlite3.connect(DB_PATH)

    # Load table
    sectors.to_sql(
        "sectors",
        conn,
        if_exists="replace",
        index=False
    )

    conn.commit()
    conn.close()

    print("\n✅ sectors table loaded successfully.")


if __name__ == "__main__":
    load_sectors()