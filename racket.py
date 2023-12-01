from turtle import Turtle


class Racket(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=3, stretch_wid=0.5)
        self.setheading(90)
        self.penup()

    def right_racket(self):
        self.goto(x=280, y=0)

    def left_racket(self):
        self.goto(x=-280, y=0)

    def up(self):
        self.forward(10)

    def down(self):
        self.forward(-10)



