import pandas as pd
import numpy as np

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": ranking
})

# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]
# print(df)

# df = df.sort_index()
# df = df.reset_index()
# print(df)

new_data = pd.DataFrame({
    "Languages" : ["PHP", "Typescript", "Java"],
    "Ranking" : [11, 5, 7]
})

# adding new columns : concatenation
df = pd.concat([df, new_data], ignore_index=True)


# adding new columns : column reference
# df["Ranking 2022"] = [4, 1, 2, 3, 10, 6, 5]
df["Ranking 2022"] = [4,1,2,3,10,6,5]
df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]
print(df)

# new_data_column = pd.DataFrame({
#     "Ranking 2022": [4, 1, 2, 3, 10, 6, 5],
#     "Ranking 2020": [4,1,2,3,8,5,9],
#     "Ranking 2019": [4,1,2,3,8,5,10]
# })

df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])

print(df)

df.rename(columns={"ranking" : "ranking 2023"}, inplace=True)
# df = df.set_index("languages")
print(df)