# print("Welcome to the rollercoaster")
# height=int(input("Enter your heightin cm: "))
# age=int(input("Enter your age"))

# if(height>=120):
#     print("You can ride")

#     if(age>18):
#         if(age>=45 and age<=55):
#             print("Free ride for you")
#         else:
#             print("You have to pay $12")

#     elif(age>=12 and age<=18):
#         print("You have to pay $7")

#     else:
#         print("you have to pay $5")
# else:
#     print("You cannot ride")


# # num=int(input("Enter the number: "))

# # if(num%2==0):
# #     print("Even number")
# # else:
# #     print("Odd number")


# Final project of day 3


print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input("You are at cross road. where do you want to go? \nType 'left' or 'right' \n").lower()

if (road == "left"):
    water = input("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across").lower()
    if (water == "wait"):
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?").lower()
        if (door == "yellow"):
            print("You win")
        elif (door == "red"):
            print("Burned by fire.Game Over.")
        elif (door == "blue"):
            print("Eaten by beasts.Game Over.")
        else:
            print("Game over")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")

