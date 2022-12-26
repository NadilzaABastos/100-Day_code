from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.updade_level()

    def updade_level(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Level : {self.score} ", align= "center", font=FONT)

    def point(self):
        self.score += 1
        self.updade_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Comic Sans", 20, "normal"))


