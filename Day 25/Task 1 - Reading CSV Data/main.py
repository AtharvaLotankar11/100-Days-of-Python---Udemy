# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

"""
(Bunch of codes for just listing)
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

Print out temperatures in int form as list
"""

import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))   - data type: series
# print(type(data))           - data type: dataframe

"""
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)  --alt is below
print(data["temp"].mean())
print(data["temp"].max())

#Get Data in columns
# print(data["condition"]) - alt below
print(data.condition)

#Get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
"""

monday = data[data.day == "Monday"]
print(monday.condition)

#Get Monday's Temp in Fahrenheit
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
