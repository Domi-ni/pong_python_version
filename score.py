from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 15, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(arg=f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 270)
        self.write(arg=f"{self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
