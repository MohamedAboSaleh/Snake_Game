from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 260)
        self.refresh()

    def refresh(self):
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)