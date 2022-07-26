import time
from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.home()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.screen = Screen()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.move_speed = 0.1
        self.home()
        self.screen.update()
        time.sleep(1)
        self.bounce_x()
