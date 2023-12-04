from turtle import Screen
from middle_line import MiddleLine
from racket import Racket
from ball import Ball


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.listen()
my_screen.tracer(0)

middle_line = MiddleLine()
middle_line.create_line()

right_racket = Racket()
right_racket.right_racket()

left_racket = Racket()
left_racket.left_racket()

my_screen.onkeypress(key="Up", fun=right_racket.up)
my_screen.onkeypress(key="Down", fun=right_racket.down)
my_screen.onkeypress(key="w", fun=left_racket.up)
my_screen.onkeypress(key="s", fun=left_racket.down)

ball = Ball()

game_is_on = True
while game_is_on:
    my_screen.update()
    ball.wall_collision()
    ball.move()


my_screen.exitonclick()
