"""
Program: Hirst Painting Program
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen
from random import choice

# import colorgram
#
#
# def get_colors_list(image, number_of_colors):
#     extracted_colors = colorgram.extract(image, number_of_colors)
#     list_of_colors = []
#     for color in extracted_colors:
#         rgb_color = color.rgb
#         list_of_colors.append(tuple(rgb_color))
#     return list_of_colors
#
#
# my_colours = get_colors_list('hirst_image.jpg', 30)
# print(my_colours)

colors = [
    (1, 12, 31),
    (53, 25, 17),
    (218, 127, 106),
    (10, 104, 159),
    (242, 213, 68),
    (149, 83, 39),
    (215, 87, 63),
    (155, 6, 24),
    (165, 162, 31),
    (157, 62, 102),
    (10, 64, 33),
    (206, 74, 104),
    (11, 96, 57),
    (95, 6, 20),
    (174, 135, 163),
    (1, 61, 145),
    (7, 172, 216),
    (3, 213, 207),
    (159, 33, 24),
    (8, 140, 85),
    (145, 227, 217),
    (122, 193, 147),
    (220, 177, 216),
    (100, 218, 229),
    (117, 171, 192),
    (79, 135, 178),
]


screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

for y in range(-250, 250, 50):
    tim.sety(y)
    for x in range(-250, 250, 50):
        tim.setx(x)
        tim.dot(20, choice(colors))

screen.exitonclick()
