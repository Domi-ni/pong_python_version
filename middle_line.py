from turtle import Turtle


class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(2)
        self.hideturtle()
        self.create_line()

    def create_line(self):
        self.penup()
        self.goto(x=0, y=-290)
        self.setheading(90)

        while self.ycor() < 290:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(10)

