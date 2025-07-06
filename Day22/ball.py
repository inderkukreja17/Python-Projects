from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.x=10
        self.y=10
        self.move_speed=0.05
    def move(self):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x, new_y)
    def bounce(self):
        self.y*=-1

    def bounce_paddle(self):
        self.x*=-1
        self.move_speed*=0.9


    def refresh(self):
        self.goto(0,0)
        self.move_speed = 0.05
        self.bounce_paddle()