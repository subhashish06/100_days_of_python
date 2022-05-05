"""
Program: Ping Pong Scorecard Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Score(Turtle):
    """creates the score object"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

    def display_score(self):
        """displays the score"""
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increases the score"""
        self.score += 1

    def display_game_over(self):
        """displays game over"""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


class Net(Turtle):
    """the net object"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.pensize(3)
        self.hideturtle()
        self.goto(x=0, y=-300)
        self.setheading(90)
        while self.ycor() < 300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
