import pandas as pd

df = pd.read_excel("data/raw/market_cap.xlsx", header=None)

print(df.head(10))