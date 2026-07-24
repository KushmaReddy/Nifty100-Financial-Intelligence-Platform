import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
company_id,
year,
operating_activity,
investing_activity,
financing_activity
FROM cashflow
"""

df = pd.read_sql_query(query, conn)


def get_sign(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"


def classify_pattern(cfo, cfi, cff):

    pattern = (cfo, cfi, cff)

    mapping = {
        ("+", "-", "-"): "Reinvestment",
        ("+", "+", "-"): "Shareholder Returns",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "+", "+"): "Distress",
        ("-", "-", "+"): "Debt Funded Growth",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed",
        ("-", "+", "-"): "Mixed"
    }

    return mapping.get(pattern, "Other")


df["cfo_sign"] = df["operating_activity"].apply(get_sign)
df["cfi_sign"] = df["investing_activity"].apply(get_sign)
df["cff_sign"] = df["financing_activity"].apply(get_sign)

df["pattern_label"] = df.apply(
    lambda row: classify_pattern(
        row["cfo_sign"],
        row["cfi_sign"],
        row["cff_sign"]
    ),
    axis=1
)

output = df[
    [
        "company_id",
        "year",
        "cfo_sign",
        "cfi_sign",
        "cff_sign",
        "pattern_label"
    ]
]

output.to_csv(
    "src/reports/capital_allocation.csv",
    index=False
)

print(output.head())

conn.close()