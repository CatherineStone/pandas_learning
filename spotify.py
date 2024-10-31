import pandas as pd

df = pd.read_csv("spotify_songs.csv")

df.info()

# print(df.shape)
# print(df.columns)
# print(df.head())

# print(df["playlist_genre"].value_counts())
# print(df["playlist_genre"].mode()[0])
# print(df["duration_ms"].median())
# print(df["duration_ms"].mean())

max_duration = df["duration_ms"].max()
min_duration = df["duration_ms"].min()

# print(max_duration - min_duration)
# print(df["duration_ms"].sum())

# sorts by a column.
# print(df.sort_values(by=["duration_ms"], ascending=False))

print(df.query("track_artist=='Ricky Martin'"))

# data = {"Category":["A", "B", "C", "D"]}