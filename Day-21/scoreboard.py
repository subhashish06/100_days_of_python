from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def display_score(self):
        self.clear()
        self.write(f'Your score : {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def display_game_over(self):
        self.home()
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)
