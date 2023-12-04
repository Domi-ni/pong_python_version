from turtle import Turtle


class Racket(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=4.5)
        self.penup()

    def right_racket(self):
        self.goto(x=375, y=0)

    def left_racket(self):
        self.goto(x=-380, y=0)

    def up(self):
        if self.ycor() < 370:
            self.goto(self.xcor(), self.ycor()+18)

    def down(self):
        if self.ycor() > -370:
            self.goto(self.xcor(), self.ycor()-18)
