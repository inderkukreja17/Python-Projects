# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# # print(squared_numbers
#
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [nom for nom in numbers if nom%2==0]
# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words=sentence.split()



result = {n:len(n) for n in words}
print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}

print(weather_f)
