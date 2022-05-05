"""
Program: Number Guess Game Art
Author: Subhashish Dhar
Date: 02/09/2021
"""

import random
from number_guess_art import LOGO

secret_number = random.randint(1, 100)
IS_GAME_OVER = False
LIFE = 0

print(LOGO)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Psst.. the correct answer is {secret_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    LIFE = 10
elif difficulty == "hard":
    LIFE = 5
else:
    print("Options are only 'easy' and 'hard'.")
    IS_GAME_OVER = True


while not IS_GAME_OVER:
    print(f"You have {LIFE} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
        IS_GAME_OVER = True
    else:
        LIFE -= 1
        if LIFE == 0:
            print("You run out of attempts. You lose!")
            IS_GAME_OVER = True
        else:
            if user_guess > secret_number:
                print("Too High.\nGuess again.")
            else:
                print("Too Low.\nGuess again.")
