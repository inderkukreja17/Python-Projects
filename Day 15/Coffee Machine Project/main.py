from sympy import false

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def is_resources_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items]>=resources[items]:
            print(f"Sorry we are out of {items}")
            return False
    return True



def process_coins():
    print("Please insert coins")
    quarters=int(input("How many quarters:"))
    dimes = int(input("How many dimes:"))
    nickles = int(input("How many nickles:"))
    pennies = int(input("How many pennies:"))
    total=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    return total

def is_transaction_successful(money_received,drink_amount):
    if money_received>=drink_amount:
        change=round(money_received-drink_amount,2)
        print(f"Here is your change: ${change}")

        global profit
        profit+=drink_amount
        return True
    else:
        print("Sorry not enough money, Money refunded!")
        return false

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")



is_on=True
while is_on:
    order=input("What would you like? (espresso/latte/cappuccino):").lower()
    if order=="off":
        is_on=False
    elif order=="report":
        for key,values in resources.items():
            print(f"{key}: {values}")
        print(f"Money: ${profit}")
    else:
        drink=MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(order, drink["ingredients"])
                print(f"Enjoy your {order}")






#TODO 1 :DO THIS
