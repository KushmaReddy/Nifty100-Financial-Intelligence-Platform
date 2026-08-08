import re
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "analysis.xlsx"
OUTPUT_PATH = PROJECT_ROOT / "output"

OUTPUT_PATH.mkdir(exist_ok=True) 
# -----------------------------
# Load Analysis Dataset
# -----------------------------

print("Loading analysis dataset...")

df = pd.read_excel(
    RAW_DATA_PATH,
    header=1
)

print(f"Rows Loaded : {len(df)}")
print(f"Columns : {list(df.columns)}")

print("\nFirst 5 Rows\n")
print(df.head())
# -----------------------------
# Regex Parser
# -----------------------------

def parse_metric(text):

    if pd.isna(text):
        return None, None

    text = str(text).strip()

    pattern = r"(TTM|Last Year|\d+\s*Years?|\d+\s*Year)\s*:?\s*(-?\d+\.?\d*)%?"

    match = re.search(pattern, text)

    if match:

        period = match.group(1)
        value = float(match.group(2))

        return period, value

    return None, None
print("\nTesting Parser\n")

sample = df.loc[0, "compounded_sales_growth"]

period, value = parse_metric(sample)

print("Input :", sample)
print("Period:", period)
print("Value :", value)
# -----------------------------
# Parse All Metrics
# -----------------------------

parsed_records = []
failed_records = []

metrics = [
    "compounded_sales_growth",
    "compounded_profit_growth",
    "stock_price_cagr",
    "roe"
]

for _, row in df.iterrows():

    company_id = row["company_id"]

    for metric in metrics:

        period, value = parse_metric(row[metric])

        if period is None:

            failed_records.append({
                "company_id": company_id,
                "metric": metric,
                "original_value": row[metric]
            })

        else:

            parsed_records.append({
                "company_id": company_id,
                "metric_type": metric,
                "period": period,
                "value_pct": value
            })

print(f"\nParsed Records : {len(parsed_records)}")
print(f"Failed Records : {len(failed_records)}")
# -----------------------------
# Save Output Files
# -----------------------------

parsed_df = pd.DataFrame(parsed_records)
failed_df = pd.DataFrame(failed_records)

parsed_file = OUTPUT_PATH / "analysis_parsed.csv"
failed_file = OUTPUT_PATH / "parse_failures.csv"

parsed_df.to_csv(parsed_file, index=False)
failed_df.to_csv(failed_file, index=False)

print("\nFiles Generated Successfully")
print(parsed_file)
print(failed_file)