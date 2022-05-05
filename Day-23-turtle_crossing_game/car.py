"""
Program: Turtle Crossing Car Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle
from random import randint, choice

COLORS = ["red", "green", "blue", "pink", "purple", "gray"]
STARTING_CAR_SPEED = 5


class Car:
    """creates the car object"""

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_CAR_SPEED

    def create_car(self):
        """creates the car on screen"""
        chance = randint(1, 6)
        if chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(x=-280, y=randint(-230, 230))
            self.all_cars.append(new_car)

    def move(self):
        """moves the car forward"""
        for car in self.all_cars:
            car.forward(self.speed)

    def level_up(self):
        """speeds up the car"""
        self.speed += 3
