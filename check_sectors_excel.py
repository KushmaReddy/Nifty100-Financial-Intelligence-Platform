import pandas as pd

df = pd.read_excel("data/raw/sectors.xlsx", header=None)

print(df.head())