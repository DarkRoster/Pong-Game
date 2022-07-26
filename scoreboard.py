from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))

        self.goto(0, 180)
        self.write("|", align="center", font=("Courier", 80, "normal"))

        self.goto(100, 180)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.lscore += 1

    def r_point(self):
        self.rscore += 1
