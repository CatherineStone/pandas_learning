import pandas as pd

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])

# print(languages)
 

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
# ranking = pd.Series([3,1,2,4])

# df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie",55)], columns=['Name','Age'])
# print(df)

# df = pd.DataFrame({
#     "Languages": languages,
#     "Ranking": ranking
# })

# print(df)


# pd.concat([languages, ranking] axis=1)

# planets = pd.DataFrame([("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"), 
#                         (167, 464, 15, -65, -110, -140, -195, -200), (2439.7, 6051.8, 6371.0, 3390.0, 69911, 58232, 25362, 24622, 1153), 
#                         ("grey", "golden brown", "blue", "red", "yellow, brown, red", "yellow, brown, grey", "cyan", "blue", "brown"), 
#                         ("Mercury takes roughly three Earth months to orbit the Sun", "A day is longer than a year on Venus", "Earth has a squishy interior", "The whole of Mars is as cold as the South Pole", "Jupiter's largest moon has a salty ocean that contains more water than on Earth", "Saturn's rings are 90% water", "You can't stand on Uranus", "Neptune is more than 30 times as far from the Sun as Earth", "Pluto isn't the only dwarf planet in our Solar System - we have six")],
#                         columns=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
#                         # rows=["planet name", "planet's temperature (in degress celcius)", "planet's radius (in km)", "planet's colour", "interesting fact"])



planet_names = pd.Series(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
planet_temp = pd.Series([167, 464, 15, -65, -110, -140, -195, -200]) 
planet_radius = pd.Series([2439.7, 6051.8, 6371.0, 3390.0, 69911, 58232, 25362, 24622, 1153])
planet_colour = pd.Series(["grey", "golden brown", "blue", "red", "yellow, brown, red", "yellow, brown, grey", "cyan", "blue", "brown"])
planet_fact = pd.Series(["Mercury takes roughly three Earth months to orbit the Sun", "A day is longer than a year on Venus", "Earth has a squishy interior", "The whole of Mars is as cold as the South Pole", "Jupiter's largest moon has a salty ocean that contains more water than on Earth", "Saturn's rings are 90% water", "You can't stand on Uranus", "Neptune is more than 30 times as far from the Sun as Earth", "Pluto isn't the only dwarf planet in our Solar System - we have six"])

planets = pd.DataFrame({
    "Planet names": planet_names,
    "planet temperatures (in degrees Celcius)": planet_temp,
    "Planet radius' (in km)": planet_radius,
    "Planet colours": planet_colour,
    "Fun fact about planet": planet_fact
})

print(planets)