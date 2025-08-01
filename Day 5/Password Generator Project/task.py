# # fruits=["apple","peach","pear"]
# # for fruit in fruits:
# #     print(fruit)


# student_scores=[55,45,67,232,566,456,322,12,34]

# max_score=max(student_scores)
# print(max_score)

# a=0
# for score in student_scores:
#     if score>a:
#         a=score

# print(a)

# total=0        
# for i in range(1,101):
#     total=total+i
# print(total)


# Final project of day 5
# Password Generator Project


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
password1 = ""
password2 = ""
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password1 += random_num

for char in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password2 += random_symbol

final_pass = password + password1 + password2

print(final_pass)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char

for char in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password_list += random_num

for char in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list += random_symbol

print(password_list)

# random.shuffle(password_list)
# print(password_list)

password4 = ""
for char in password_list:
    password4 += char

print(f"Your password is {password4}")