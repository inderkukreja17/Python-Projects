# # with open("weather_data.csv","r") as weather:
# #     data=weather.readlines()
# #     print(data)
# import pandas
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temp=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temp.append(int(row[1]))
# #
# #     print(temp)
#
#
#
#
# #
# import pandas as pd
# from pandas import DataFrame
# #
# data=pd.read_csv("weather_data.csv")
# print(data)
# # # data_dict=data.to_dict()
# # # print(data_dict)
# # temp_list=data["temp"].to_list()
# # avg_temp=sum(temp_list)/len(temp_list)
# # print(avg_temp)
# #
# # print(data["temp"].max())
# #
# # #Get data in columns
# # print(data["condition"])
# #print(data.condition)
#
# #Get data in row
# #
# # print(data[data.day=="Monday"])
# # temp=(data.temp .max())
# # print(data[data.temp==temp])
# #
# # monday=(data[data.day=="Monday"])
# # monday_temp=monday.temp
# # temp_in_fara=(9/5)*monday_temp+32
# # print(temp_in_fara)
#
# data_dict={
#     "student":["Inder","Sahil"],
#     "scores":[56,65],
# }
#
# data=pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


#Challenege part 1
#
#
# import pandas as pd
# from pandas import DataFrame
# from pandas.core.internals.construction import dataclasses_to_dicts
#
# data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# fur_colour_list=data["Primary Fur Color"].to_list()
# gray_count=fur_colour_list.count("Gray")
# black_count=fur_colour_list.count("Black")
# red_count=fur_colour_list.count("Cinnamon")
#
#
#
#
# data_dict={
#     "Fur_Colour":["Gray","Red","Black"],
#     "Count":[gray_count,red_count,black_count]
# }
# data=pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data1.csv")

























