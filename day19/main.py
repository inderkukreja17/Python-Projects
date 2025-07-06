import random
from turtle import Turtle,Screen


is_race_on=False
my_screen=Screen()
my_screen.setup(width=500,height=400)
user_bet=my_screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")


color=["red","blue","green","yellow","orange","purple"]
y_position=[-70,-30,0,30,70,100]
all_turtle=[]
for turtle in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_position[turtle])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>220:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won!. The {winning_color} turtle is the winner")
            else:
                print(f"You have lost!. The {winning_color} turtle is the winner")
        random_speed=random.randint(0,10)
        turtle.forward(random_speed)





# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def clear_screen():
#     my_screen.resetscreen()
# def clockwise():
#     tim.right(15)
# def anticlockwise():
#     tim.left(15)
#
#
# my_screen.listen()
# my_screen.onkey(fun=move_forward,key="w")
# my_screen.onkey(fun=move_backward,key="s")
# my_screen.onkey(fun=clear_screen,key="c")
# my_screen.onkey(fun=clockwise,key="d")
# my_screen.onkey(fun=anticlockwise,key="a")








my_screen.exitonclick()
