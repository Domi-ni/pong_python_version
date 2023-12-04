from turtle import Screen
from middle_line import MiddleLine
from racket import Racket
from ball import Ball
from score import Score
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Pong")
my_screen.tracer(0)

middle_line = MiddleLine()
score_board = Score()

right_racket = Racket()
right_racket.right_racket()

left_racket = Racket()
left_racket.left_racket()

ball = Ball()

my_screen.listen()
my_screen.onkeypress(key="Up", fun=right_racket.up)
my_screen.onkeypress(key="Down", fun=right_racket.down)
my_screen.onkeypress(key="w", fun=left_racket.up)
my_screen.onkeypress(key="s", fun=left_racket.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.move()

    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()

    if (360 <= ball.xcor() and ball.distance(right_racket) <= 50 or ball.xcor() < -360 and
            ball.distance(left_racket) <= 50):
        ball.bounce_x()

    if 385 <= ball.xcor():
        ball.reset_position()
        score_board.r_point()

    if ball.xcor() < -385:
        ball.reset_position()
        score_board.l_point()

my_screen.exitonclick()
