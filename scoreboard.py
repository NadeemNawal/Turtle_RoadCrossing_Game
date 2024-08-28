from turtle import Turtle

FONT_SCORE = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT_SCORE)

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=FONT_SCORE)




