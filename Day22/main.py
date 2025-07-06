from turtle import Screen,Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.bgcolor("black")
my_screen.setup(width=900,height=600)
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle=Paddle((400,0))
l_paddle=Paddle((-410,0))
ball=Ball()
score=Scoreboard()

my_screen.listen()
my_screen.onkey(key="Up",fun=r_paddle.move_up)
my_screen.onkey(key="Down",fun=r_paddle.move_down)
my_screen.onkey(key="w",fun=l_paddle.move_up)
my_screen.onkey(key="s",fun=l_paddle.move_down)



game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor()>280 or  ball.ycor()<-280:
        ball.bounce()
    # Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>370 or ball.distance(l_paddle)<50 and ball.xcor()<-380:
        ball.bounce_paddle()

    if ball.xcor()>480 :
        ball.refresh()
        score.l_point()

    if ball.xcor() < -480:
        ball.refresh()
        score.r_point()








my_screen.exitonclick()