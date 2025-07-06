import turtle
from turtle import Turtle,Screen
import random

tim=Turtle()
tim.shape("turtle")
# tim.color("red")
#
# for i in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# colors=["red","blue","green","yellow","black","pink","brown","coral"]




# def draw_shape(num_sides):
#     angle=360/num_sides
#     for i in range(num_sides):
#         tim.right(angle)
#         tim.forward(100)
#
#
# for shape_side in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)



# Random Walk code


angle=[0,90,180,360]
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color


# def random_walk(angle_side):
#     tim.speed("fastest")
#     tim.pensize(15)
#     tim.forward(100)
#     tim.right(angle_side)
#
#

# for i in range(200):
#     random_angle=random.choice(angle)
#     random_walk(random_angle)
#     tim.color(random_color())


#Spirograph
tim.speed("fastest")
for i in range(72):
    tim.circle(100)
    tim.color(random_color())
    tim.right(5)



#
my_screen=Screen()
my_screen.exitonclick()