from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.print_score()

    def print_score(self):
        text = "Score: " + str(self.score)
        self.write(text, move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        text = "GAME OVER"
        self.write(text, move=False, align=ALIGN, font=FONT)