from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0)


snake=Snake()
food=Food()
score=Scoreboard()
score.update_scoreboard()
my_screen.listen()
my_screen.onkey(key="Up",fun=snake.up)
my_screen.onkey(key="Down",fun=snake.down)
my_screen.onkey(key="Left",fun=snake.left)
my_screen.onkey(key="Right",fun=snake.right)
game_is_on= True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food)<13:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()


    #Detect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()








my_screen.exitonclick()