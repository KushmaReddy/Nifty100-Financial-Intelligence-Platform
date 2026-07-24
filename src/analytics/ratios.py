import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"


def load_data():
    conn = sqlite3.connect(DB_PATH)

    profit_loss = pd.read_sql_query(
        "SELECT * FROM profitandloss",
        conn
    )

    balance_sheet = pd.read_sql_query(
        "SELECT * FROM balancesheet",
        conn
    )

    companies = pd.read_sql_query(
        "SELECT * FROM companies",
        conn
    )

    sectors = pd.read_sql_query(
        "SELECT company_id, broad_sector FROM sectors",
        conn
    )

    conn.close()

    return profit_loss, balance_sheet, companies, sectors


def calculate_profitability_ratios(profit_loss, balance_sheet, sectors):
    data = pd.merge(
        profit_loss,
        balance_sheet,
        on=["company_id", "year"],
        how="inner"
    )

    data = pd.merge(
        data,
        sectors,
        on="company_id",
        how="left"
    )

    data["net_profit_margin"] = None
    data["operating_profit_margin"] = None
    data["roe"] = None
    data["ebit"] = None
    data["roce"] = None
    data["roa"] = None

    data["debt_to_equity"] = None
    data["interest_coverage"] = None
    data["net_debt"] = None
    data["asset_turnover"] = None
    data["debt_free"] = None
    data["high_leverage_flag"] = None

    opm_log = []

    for index, row in data.iterrows():

        if row["sales"] != 0:
            data.at[index, "net_profit_margin"] = (
                row["net_profit"] / row["sales"]
            ) * 100

            data.at[index, "operating_profit_margin"] = (
                row["operating_profit"] / row["sales"]
            ) * 100

        if (row["equity_capital"] + row["reserves"]) > 0:
            data.at[index, "roe"] = (
                row["net_profit"] /
                (row["equity_capital"] + row["reserves"])
            ) * 100

        data.at[index, "ebit"] = (
            row["operating_profit"] -
            row["depreciation"]
        )

        capital = (
            row["equity_capital"] +
            row["reserves"] +
            row["borrowings"]
        )

        if capital > 0:
            data.at[index, "roce"] = (
                data.at[index, "ebit"] /
                capital
            ) * 100

        if row["total_assets"] > 0:
            data.at[index, "roa"] = (
                row["net_profit"] /
                row["total_assets"]
            ) * 100

        equity = (
            row["equity_capital"] +
            row["reserves"]
        )

        if equity > 0:
            data.at[index, "debt_to_equity"] = (
                row["borrowings"] / equity
            )

        if row["interest"] > 0:
            data.at[index, "interest_coverage"] = (
                row["operating_profit"] +
                row["other_income"]
            ) / row["interest"]

        data.at[index, "net_debt"] = (
            row["borrowings"] -
            row["investments"]
        )

        if row["total_assets"] > 0:
            data.at[index, "asset_turnover"] = (
                row["sales"] /
                row["total_assets"]
            )

        if row["borrowings"] == 0:
            data.at[index, "debt_free"] = "Yes"
        else:
            data.at[index, "debt_free"] = "No"

        if row["broad_sector"] == "Financials":
         data.at[index, "high_leverage_flag"] = False

        elif (
         pd.notna(data.at[index, "debt_to_equity"])
         and data.at[index, "debt_to_equity"] > 5
):
         data.at[index, "high_leverage_flag"] = True

        else:
         data.at[index, "high_leverage_flag"] = False

        if (
            pd.notna(row["opm_percentage"])
            and pd.notna(data.at[index, "operating_profit_margin"])
        ):

            difference = abs(
                data.at[index, "operating_profit_margin"] -
                row["opm_percentage"]
            )

            if difference > 1:

                opm_log.append({
                    "company_id": row["company_id"],
                    "year": row["year"],
                    "calculated_opm": round(
                        data.at[index, "operating_profit_margin"], 2
                    ),
                    "source_opm": row["opm_percentage"],
                    "difference": round(difference, 2)
                })

    opm_log = pd.DataFrame(opm_log)

    if len(opm_log) > 0:
        opm_log.to_csv(
            "opm_crosscheck_log.csv",
            index=False
        )

    return data


if __name__ == "__main__":
    profit_loss, balance_sheet, companies, sectors = load_data()

    data = calculate_profitability_ratios(
    profit_loss,
    balance_sheet,
    sectors
)

    print(
        data[
            [
                "company_id",
                "year",
                "debt_to_equity",
                "interest_coverage",
                "net_debt",
                "asset_turnover",
                "debt_free",
                "high_leverage_flag",
            ]
        ].head(10)
    )
    data.to_csv(
    "src/reports/financial_ratios.csv",
    index=False
)

conn = sqlite3.connect(DB_PATH)

data.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nfinancial_ratios.csv saved successfully.")
print("financial_ratios table updated successfully.")