from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    # Detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R Paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
