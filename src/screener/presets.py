import pandas as pd


def quality_compounder(df):
    return df[
        (df["roe"] >= 15)
        & (df["debt_to_equity"] <= 1)
        & (df["free_cash_flow"] > 0)
    ]


def growth_accelerator(df):
    return df[
        (df["roe"] >= 20)
        & (df["debt_to_equity"] <= 2)
        & (df["free_cash_flow"] > 0)
    ]


def debt_free_bluechip(df):
    return df[
        (df["debt_to_equity"] <= 0.2)
        & (df["roe"] >= 15)
    ]


def value_pick(df):
    return df[
        (df["pe_ratio"] <= 25)
        & (df["pb_ratio"] <= 5)
        & (df["roe"] >= 15)
    ]


def dividend_champion(df):
    return df[
        (df["dividend_yield_pct"] >= 2)
        & (df["roe"] >= 15)
    ]


def turnaround_watch(df):
    return df[
        (df["roe"] >= 10)
        & (df["debt_to_equity"] <= 2)
        & (df["free_cash_flow"] > 0)
    ]