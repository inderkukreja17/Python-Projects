# # import random

# # random_no=random.random()
# # print(random_no)

# # random_float=random.uniform(1,10)
# # print(random_float)

import random

# # random_no=random.randint(0,1)
# # if random_no==1:
# #     print("heads")
# # else:
# #     print("tails") 

friends = ["Alice", "bob", "charlie", "david", "emanuel"]
random_name = random.randint(0, 4)
# 1 option
print(friends[random_name])
# 2 option
print(random.choice(friends))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors\n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissor)
else:
    (print("Invalid input"))

print("Computer Choose:\n")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissor)
else:
    (print("Invalid input"))

if user_choice == 0 and computer_choice == 0:
    print("Draw")
elif user_choice == 1 and computer_choice == 2:
    print("you loose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 0 and computer_choice == 1:
    print("you win")
elif user_choice == 1 and computer_choice == 1:
    print("Draw")
elif user_choice == 2 and computer_choice == 2:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You loose")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
else:
    print("Some error occured")