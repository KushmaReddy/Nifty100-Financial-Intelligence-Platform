import pandas as pd


def remove_duplicates(df, subset):
    original_rows = len(df)

    df = df.drop_duplicates(
        subset=subset,
        keep="first"
    )

    removed_rows = original_rows - len(df)

    print(f"Removed {removed_rows} duplicate rows.")

    return df
def clean_opm(df):
    df = df.copy()

    mask = (
        df["sales"].notna() &
        df["operating_profit"].notna() &
        (df["sales"] != 0)
    )

    df.loc[mask, "opm_percentage"] = (
        df.loc[mask, "operating_profit"] /
        df.loc[mask, "sales"]
    ) * 100

    df["opm_percentage"] = df["opm_percentage"].round(2)

    return df