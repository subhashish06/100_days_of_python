from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 8, "bold")
GAME_OVER_FONT = ("Courier", 20, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=280)

    def display_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def display_game_over(self):
        self.home()
        self.write(f'GAME OVER', align=ALIGNMENT, font=GAME_OVER_FONT)