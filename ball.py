from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5)
        self.penup()
        self.x_move = 0.4
        self.y_move = 0.4

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_collision(self):
        if self.ycor() >= 285 or self.ycor() <= -285:
            self.y_move *= -1
            self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

