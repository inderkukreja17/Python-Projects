# # print("hello"[-5])
# # print("123"+"345")
# # print(123+345)

# # print(type("hello"))#tells the datatype
# # print(type(123))
# # print(type(True))
# # print(type(12.34))

# # print("Number of letter in your name: " + str(len(input("Enter your name"))))

# print(3* (3+3) /3-3)

# print(round(30.23423832,2))


# #f-strings

# score=0
# height=1.8
# is_winning=True

# print(f"your score is: {score} ,your height is: {height}, you winning is: {is_winning}")


#Final project of day 2

print("Welcome to the tip calculator")
total_bill=float(input("What was the the total bill? $"))
tip=int(input("How much tip you would like to give?10,12 or 15: "))
no_of_people=int(input("How many people to split the bill?"))

final_total_bill=(total_bill + tip/100 *total_bill)

Per_person=final_total_bill/no_of_people

final_amt=(round(Per_person , 2))
print(f"Each person should pay: ${final_amt}")