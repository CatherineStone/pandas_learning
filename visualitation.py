import matplotlib.pyplot as plt

# years = [2018, 2019, 2020, 2021, 2022, 2023]

# python_position = [7, 4, 4, 3, 4, 3]
# js_position = [1, 1, 1, 1, 1, 1]
# sql_position = [4,3,3,4,3,4]
# typescript_position = [12,10,9,7,5,5]

# #X axis first, Y axis second.
# plt.plot(years, python_position, label = "Python") #Defaults to a solid line.
# plt.plot(years, js_position, label = "Javascript", linestyle = "dashed")
# plt.plot(years, sql_position, label = "SQL", linestyle = "dotted")
# plt.plot(years, typescript_position, label = "Typescript", linestyle = "dashdot")

# #Gives our graph a title
# plt.title("Most Popular Programming Languages Ranked")

# #Labels our axis
# plt.xlabel("Year")
# plt.ylabel("Position")

# #Allows us to set our limits of the Y-axis
# plt.ylim(bottom=20, top=0)


# #Creates a legend that labels the lines
# # plt.legend([
# #     "Python",
# #     "Javascript",
# #     "SQL",
# #     "Typescript"
# # ])
# plt.legend()

# plt.show()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
youtube_screentime = [2, 1, 3 ,6 ,3]
twitter_screentime = [1, 1, 0, 0, 2]
whatsapp_screentime = [3, 1, 0, 2, 1]
raid_screentime = [0, 4, 2, 3, 3]
tiktok_screentime = [3, 0, 1, 0, 2]


plt.title("Screentime on Apps")

plt.xlabel("Days of the Week")
plt.ylabel("Screentime (in hours)")

plt.ylim(bottom=0, top=7)

plt.plot(days, youtube_screentime, label = "Youtube", color = "#f10c45")
plt.plot(days, twitter_screentime, label = "Twitter", color = "#247afd", linestyle = ":" )
plt.plot(days, whatsapp_screentime, label = "WhatsApp", color = "#0add08", linestyle = "--")
plt.plot(days, raid_screentime, label = "Raid: Shadow Legends", color = "#feb209", linestyle = "-.")
plt.plot(days, tiktok_screentime, label = "TikTok", color = "#000000", linestyle = "-")

plt.legend()


plt.show()