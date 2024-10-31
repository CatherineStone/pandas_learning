import pandas as pd

# df = pd.read_excel("results2024-10-24-152.xlsx")
df = pd.read_excel("group_results (1).xlsx")
df = df.set_index("Internet Service Provider")
df = df.drop(columns=["Fastest Download", "Fastest Upload", "Median Download", "Median Upload","Slowest Download", "Slowest Upload", "Package (if known)"])
# df = df.dropna(how="any")
print(df.describe())
print(df.info())


#Mean upload and download speed
# print(df["Download (Mb/s)"].mean())
# print(df["Upload (Mb/s)"].mean())

#Median upload and download speed
# print(df["Download (Mb/s)"].median())
# print(df["Upload (Mb/s)"].median())

#Upload speed from highest to lowest and vice versa
# print(df["Upload (Mb/s)"].sort_values())
# print(df["Upload (Mb/s)"].sort_values(ascending=False))

#Download speed from highest to lowest and vice versa
# print(df["Download (Mb/s)"].sort_values())
# print(df["Download (Mb/s)"].sort_values(ascending=False))