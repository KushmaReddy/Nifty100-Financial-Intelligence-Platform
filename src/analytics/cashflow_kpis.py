import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"


def load_cashflow():

    conn = sqlite3.connect(DB_PATH)

    cashflow = pd.read_sql_query(
        """
        SELECT
            company_id,
            year,
            operating_activity,
            investing_activity,
            financing_activity,
            net_cash_flow
        FROM cashflow
        ORDER BY company_id, year
        """,
        conn
    )

    conn.close()

    return cashflow


def calculate_cashflow_quality(row):

    denominator = (
        abs(row["investing_activity"]) +
        abs(row["financing_activity"])
    )

    if denominator == 0:
        return None

    return round(
        row["operating_activity"] / denominator,
        2
    )


def calculate_cashflow_kpis(cashflow):

    latest = (
        cashflow
        .sort_values("year")
        .groupby("company_id")
        .tail(1)
        .reset_index(drop=True)
    )

    latest["free_cash_flow"] = (
        latest["operating_activity"] +
        latest["investing_activity"]
    )

    latest["cashflow_quality"] = latest.apply(
        calculate_cashflow_quality,
        axis=1
    )

    latest["cashflow_status"] = latest[
        "operating_activity"
    ].apply(
        lambda x: "Positive" if x >= 0 else "Negative"
    )

    return latest


if __name__ == "__main__":

    cashflow = load_cashflow()

    report = calculate_cashflow_kpis(cashflow)

    report.to_csv(
        "src/reports/cashflow_kpis.csv",
        index=False
    )

    print(report.head(15))

    print("\ncashflow_kpis.csv saved successfully.")