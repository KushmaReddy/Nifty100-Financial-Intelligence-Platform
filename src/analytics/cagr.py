import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"


def load_profit_loss():
    conn = sqlite3.connect(DB_PATH)

    profit_loss = pd.read_sql_query(
        """
        SELECT company_id,
               year,
               sales,
               net_profit,
               eps
        FROM profitandloss
        ORDER BY company_id, year
        """,
        conn
    )

    conn.close()

    profit_loss["year"] = profit_loss["year"].astype(int)

    return profit_loss


def calculate_cagr(start_value, end_value, years):

    if years <= 0:
        return None

    if pd.isna(start_value) or pd.isna(end_value):
        return None

    if start_value <= 0:
        return None

    if end_value <= 0:
        return None

    return round(
        ((end_value / start_value) ** (1 / years) - 1) * 100,
        2
    )


def get_period_cagr(company_data, column, period):

    latest = company_data.iloc[-1]

    target_year = latest["year"] - period

    previous = company_data[
        company_data["year"] == target_year
    ]

    if previous.empty:
        return None

    start_value = previous.iloc[0][column]
    end_value = latest[column]

    return calculate_cagr(
        start_value,
        end_value,
        period
    )


def generate_cagr_report(profit_loss):

    results = []

    companies = sorted(
        profit_loss["company_id"].unique()
    )

    for company in companies:

        company_data = (
            profit_loss[
                profit_loss["company_id"] == company
            ]
            .sort_values("year")
            .reset_index(drop=True)
        )

        results.append({

            "company_id": company,

            "revenue_cagr_3y":
                get_period_cagr(company_data, "sales", 3),

            "revenue_cagr_5y":
                get_period_cagr(company_data, "sales", 5),

            "revenue_cagr_10y":
                get_period_cagr(company_data, "sales", 10),

            "pat_cagr_3y":
                get_period_cagr(company_data, "net_profit", 3),

            "pat_cagr_5y":
                get_period_cagr(company_data, "net_profit", 5),

            "pat_cagr_10y":
                get_period_cagr(company_data, "net_profit", 10),

            "eps_cagr_3y":
                get_period_cagr(company_data, "eps", 3),

            "eps_cagr_5y":
                get_period_cagr(company_data, "eps", 5),

            "eps_cagr_10y":
                get_period_cagr(company_data, "eps", 10)

        })

    return pd.DataFrame(results)


if __name__ == "__main__":

    profit_loss = load_profit_loss()

    cagr_report = generate_cagr_report(
        profit_loss
    )

    print(cagr_report.head(15))

    cagr_report.to_csv(
        "src/reports/cagr_report.csv",
        index=False
    )

    print("\nCAGR report generated successfully.")