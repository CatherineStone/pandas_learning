import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("results.csv")

#There are 147 different types of tournaments
print(df["tournament"].value_counts())

print(df["home_team"].mode())
print(df["away_team"].mode())



# print(df["tournament"].sum())
# profile = ProfileReport(df, title="Football Results")

# profile.to_file("results_report.html")