import pandas as pd

df = pd.read_csv("results.csv")
# print(df)

# print(df.describe())

# print(df["home_score"].value_counts(normalize=True)*100)

mask = df["home_score"] < 7

masked_df = df[mask]

print(masked_df["home_score"].mean())