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
        self.goto(-150, 270)

    def display_score(self):
        self.clear()
        self.write(f'Your Score : {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def display_game_over(self):
        self.home()
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)


class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(150, 270)
        self.display_high_score()

    def display_high_score(self):
        with open('high_score_record.txt', 'r') as f:
            high_score = f.read().rstrip('\n')
            self.clear()
            self.write(f'High Score : {high_score}', align=ALIGNMENT, font=FONT)

    @staticmethod
    def update_high_score(score):
        with open('high_score_record.txt', 'r') as f:
            high_score = f.read().rstrip('\n')
        if score > int(high_score):
            with open('high_score_record.txt', 'w') as f:
                f.write(str(score))

    @staticmethod
    def reset_high_score():
        with open('high_score_record.txt', 'w') as f:
            f.write('0')
