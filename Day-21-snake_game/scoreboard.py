"""
Program: Score Board Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    """creates the scoreboard object"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-150, 270)

    def display_score(self):
        """displays the score"""
        self.clear()
        self.write(f'Your Score : {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increases the score by 1"""
        self.score += 1

    def display_game_over(self):
        """displays the game on screen"""
        self.home()
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)


class HighScore(Turtle):
    """creates the high score object"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(150, 270)
        self.display_high_score()

    def display_high_score(self):
        """displays the high score"""
        with open('high_score_record.txt', 'r', encoding='utf-8') as file_handler:
            high_score = file_handler.read().rstrip('\n')
            self.clear()
            self.write(f'High Score : {high_score}', align=ALIGNMENT, font=FONT)

    @staticmethod
    def update_high_score(score):
        """updates the high score in the database"""
        with open('high_score_record.txt', 'r', encoding='utf-8') as file_handler:
            high_score = file_handler.read().rstrip('\n')
        if score > int(high_score):
            with open('high_score_record.txt', 'w', encoding='utf-8') as file_handler:
                file_handler.write(str(score))

    @staticmethod
    def reset_high_score():
        """resets the high score in the database"""
        with open('high_score_record.txt', 'w', encoding='utf-8') as file_handler:
            file_handler.write('0')
