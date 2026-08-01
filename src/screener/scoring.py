import pandas as pd


def normalize(series, reverse=False):
    """
    Normalize a numeric series to a 0-100 scale.
    If reverse=True, lower values receive higher scores.
    """
    s = series.copy().fillna(series.median())

    minimum = s.min()
    maximum = s.max()

    if minimum == maximum:
        return pd.Series(50, index=s.index)

    score = ((s - minimum) / (maximum - minimum)) * 100

    if reverse:
        score = 100 - score

    return score


def calculate_composite_score(df):

    result = df.copy()

    # Profitability
    result["roe_score"] = normalize(result["roe"])
    result["roce_score"] = normalize(result["roce"])
    result["npm_score"] = normalize(result["net_profit_margin"])

    # Cash Quality
    result["fcf_score"] = normalize(result["free_cash_flow"])
    result["cash_quality_score"] = normalize(result["cashflow_quality"])

    # Growth
    result["revenue_growth_score"] = normalize(result["revenue_cagr_5y"])
    result["pat_growth_score"] = normalize(result["pat_cagr_5y"])

    # Leverage
    result["debt_score"] = normalize(
        result["debt_to_equity"],
        reverse=True
    )

    result["interest_score"] = normalize(
        result["interest_coverage"]
    )

    result["composite_score"] = (
        (
            result["roe_score"] +
            result["roce_score"] +
            result["npm_score"]
        ) / 3 * 0.35
        +
        (
            result["fcf_score"] +
            result["cash_quality_score"]
        ) / 2 * 0.30
        +
        (
            result["revenue_growth_score"] +
            result["pat_growth_score"]
        ) / 2 * 0.20
        +
        (
            result["debt_score"] +
            result["interest_score"]
        ) / 2 * 0.15
    )

    return result