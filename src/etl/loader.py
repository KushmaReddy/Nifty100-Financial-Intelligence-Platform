import sqlite3
from pathlib import Path
import pandas as pd

from src.utils import normalize_ticker, normalize_year
from src.validator import run_validations
from src.etl.cleaner import remove_duplicates, clean_opm
from src.reports.load_audit import create_load_audit
RAW_DATA_PATH = Path("data/raw")
DATABASE_PATH = Path("db/nifty100.db")


def load_excel(file_name):
    file_path = RAW_DATA_PATH / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"{file_name} not found.")

    if file_name in [
        "market_cap.xlsx",
        "sectors.xlsx",
        "financial_ratios.xlsx"
    ]:
        df = pd.read_excel(file_path, header=0)
    else:
        df = pd.read_excel(file_path, header=1)

    print(f"{file_name} loaded successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df


def normalize_dataframe(df):
    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    if "company_id" in df.columns:
        df["company_id"] = df["company_id"].apply(normalize_ticker)

    if "id" in df.columns:
        df["id"] = df["id"].apply(normalize_ticker)

    return df


def load_all_datasets():
    datasets = {
        "companies": load_excel("companies.xlsx"),
        "profitandloss": load_excel("profitandloss.xlsx"),
        "balancesheet": load_excel("balancesheet.xlsx"),
        "cashflow": load_excel("cashflow.xlsx"),
        "analysis": load_excel("analysis.xlsx"),
        "documents": load_excel("documents.xlsx"),
        "prosandcons": load_excel("prosandcons.xlsx"),
        "financial_ratios": load_excel("financial_ratios.xlsx"),
        "market_cap": load_excel("market_cap.xlsx"),
        "peer_groups": load_excel("peer_groups.xlsx"),
        "sectors": load_excel("sectors.xlsx"),
        "stock_prices": load_excel("stock_prices.xlsx"),
    }

    for name in datasets:
        datasets[name] = normalize_dataframe(datasets[name])

    return datasets


def create_database():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    print("\nDatabase connected successfully.")
    return conn


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        company_id TEXT PRIMARY KEY,
        company_name TEXT,
        industry TEXT,
        sector TEXT,
        current_price REAL,
        market_cap REAL,
        book_value REAL,
        roce REAL,
        roe REAL,
        face_value REAL,
        company_logo TEXT,
        website TEXT
    )
    """)

    conn.commit()

    print("Companies table created successfully.")


def load_table(conn, table_name, df):
    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully.")


def main():
    datasets = load_all_datasets()

    datasets["profitandloss"] = datasets["profitandloss"][
        datasets["profitandloss"]["year"].notna()
    ]

    datasets["profitandloss"] = remove_duplicates(
        datasets["profitandloss"],
        ["company_id", "year"]
    )

    datasets["balancesheet"] = remove_duplicates(
        datasets["balancesheet"],
        ["company_id", "year"]
    )

    datasets["cashflow"] = remove_duplicates(
        datasets["cashflow"],
        ["company_id", "year"]
    )

    datasets["profitandloss"] = clean_opm(
        datasets["profitandloss"]
    )
    
    logger = run_validations(datasets)

    create_load_audit(datasets)
    print("\nDatasets Loaded Successfully\n")

    for name, df in datasets.items():
        print(f"{name}: {df.shape}")

    conn = create_database()

    create_tables(conn)

    for table_name, df in datasets.items():
        load_table(conn, table_name, df)

    print("\nValidation Summary")
    print(f"Total Validation Failures: {len(logger.failures)}")

    logger.save()

    print("Validation report saved as validation_failures.csv")

    conn.close()

    print("Database connection closed.")


if __name__ == "__main__":
    main()