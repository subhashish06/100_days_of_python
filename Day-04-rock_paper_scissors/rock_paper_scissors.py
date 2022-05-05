"""
Program: Rock Paper Scissors Game
Author: Subhashish Dhar
Date: 02/09/2021
"""

import sys
import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

input_code = input(
    "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "
)

if input_code == "0":
    CHOICE = ROCK
elif input_code == "1":
    CHOICE = PAPER
elif input_code == "2":
    CHOICE = SCISSORS
else:
    print("You can't even choose! You lose!")
    sys.exit()

computer_choice = random.choice([ROCK, PAPER, SCISSORS])

print(CHOICE)
print("Computer chose:")
print(computer_choice)

if CHOICE == ROCK:
    if computer_choice == ROCK:
        print("You draw!")
    elif computer_choice == PAPER:
        print("You lose!")
    else:
        print("You win!")
elif CHOICE == PAPER:
    if computer_choice == ROCK:
        print("You win!")
    elif computer_choice == PAPER:
        print("You draw!")
    else:
        print("You lose!")
else:
    if computer_choice == ROCK:
        print("You lose!")
    elif computer_choice == PAPER:
        print("You win!")
    else:
        print("You draw!")
