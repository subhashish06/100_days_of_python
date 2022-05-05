"""
Program: Turtle Crossing Scorecard Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "bold")
GAME_OVER_FONT = ("Courier", 20, "bold")


class Score(Turtle):
    """creates the score object"""

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=280)

    def display_score(self):
        """displays the score"""
        self.clear()
        self.write(f"Level : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increases the score by 1"""
        self.score += 1

    def display_game_over(self):
        """displays game over"""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
