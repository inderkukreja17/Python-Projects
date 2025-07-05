import art
from game_data import data
import random
print(art.logo)

def format_data(account):
    name=account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name},{description} from {country}"

def check_answer(guess,a_count,b_count):
    if a_count > b_count:
        return guess == "a"
    else:
        return guess == "b"


B = random.choice(data)

score=0

right_answer=True
while right_answer:
    A=B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    print(f"Compare A: {format_data(A)}")
    print(art.vs)
    print(f"Against B: {format_data(B)}")

    choice=input("Who has more followers? Type 'A' or 'B':  ").lower()
    a_follower_count=A["follower_count"]
    b_follower_count = B["follower_count"]
    print(a_follower_count)
    print(b_follower_count)

    is_correct = check_answer(choice, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        right_answer = False


