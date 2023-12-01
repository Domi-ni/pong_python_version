from turtle import Screen
from middle_line import MiddleLine
from racket import Racket


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.listen()

middle_line = MiddleLine()
middle_line.create_line()

right_racket = Racket()
right_racket.right_racket()

if right_racket.ycor() > 280:
    pass
else:
    my_screen.onkeypress(key="Up", fun=right_racket.up)
    
if right_racket.ycor() < -280:
    pass
else:
    my_screen.onkeypress(key="Down", fun=right_racket.down)


left_racket = Racket()
left_racket.left_racket()

my_screen.exitonclick()
