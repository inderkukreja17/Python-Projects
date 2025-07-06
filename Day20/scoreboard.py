from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)

        self.hideturtle()
        file=open("data.txt")
        self.high_score=int(file.read())


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        with open("data.txt",mode="w") as file:
            file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    # def game_over(self):
    #     self.color("white")
    #     self.penup()
    #     self.goto(x=-90, y=-10)
    #     self.write(f"Game Over!",font=('Arial',29,'bold'))
    #     self.hideturtle()