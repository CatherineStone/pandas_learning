import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")
# print(df.describe())
# print(df.info())

#Sets in the index column to the Transaction ID column.
df = df.set_index("Transaction ID")

#Drops a column that is not needed in the data frame.
df = df.drop(columns=["Till ID"])

#Removes individual rows but can be time consuming to remove multiple rows.
df = df.drop([6.0])

#Removes any null/undefined values and is a faster way to clean data.
df = df.dropna(how="any")

#Searches for any duplicate values.
# print(df[df.duplicated()])

df = df.drop_duplicates()

#We can use the .at property to reassign a value.
#E.g, For the 15th item in the ID column at the cost column, change the value to 6.0.
df.at[15.0, "Cost"] = 6.00

#.apply will run the function against every value, so we can update the "Time" column to the updated values.
def float_to_time(time_record):
    #Convert float to a string
    time_record = str(time_record)
    #Split the input strign at the decimal point
    hours, minutes = time_record.split(".")
    #Format the hours and minutes into HH:MM
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return(timestamp)

float_to_time(8.32)
df["Time"] = df["Time"].apply(float_to_time)

def split_basket(basket_item):
    items = basket_item.split(",")
    stripped_items = [item.strip() for item in items]
    return(stripped_items)

df["Basket"] = df["Basket"].apply(split_basket)
# print(df["Basket"])

exploded_data = df.explode("Basket", ignore_index=False)
# print (exploded_data["Basket"])

# split_basket("Hot Chocolate, Americano, Tea, Latte, Latte")

#Average basket price
print(df["Cost"].mean())

#The maximum spend in one transaction
max_spend = df['Cost'].max()

#The minimum spend in one transaction
min_spend = df['Cost'].min()

#Most common spend amount
most_common_spend = df['Cost'].mode()[0]
# print(f"Most common spend amount: £{most_common_spend:.2f}")

#Most common payment type
