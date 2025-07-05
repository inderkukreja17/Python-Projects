import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_no = random.randint(0, len(cards) - 1)
    random_card = cards[random_no]
    return random_card


def calculate_score(list_given):
    if sum(list_given) == 21 and len(list_given) == 2:
        return 0
    elif sum(list_given) > 21 and 11 in list_given:  # Check if 11 exists in the list
        list_given.remove(11)
        list_given.append(1)
        print(list_given)
    return sum(list_given)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "You loose"
    elif user_score==0:
        return "You win"
    elif user_score>21:
        return "you loose"
    elif computer_score > 21:
        return "You Win"
    elif user_score>computer_score:
        return "You win"
    elif computer_score>user_score:
        return "You loose"
    else:
        return "Some errr occurred"

play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
if play == "y":
    print("\n" * 50)
    from art import logo
    print(logo)

    is_game_over = False
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
print(f"Your final hand {user_cards},current score{user_score}")
print(f"Computer final hand{computer_cards},Computer score{computer_score}")
print(compare(user_score,computer_score))