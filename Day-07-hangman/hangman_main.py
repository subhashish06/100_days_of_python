"""
Program: Hangman Game
Author: Subhashish Dhar
Date: 02/09/2021
"""

import random
from hangman_art import LOGO, STAGES
from hangman_words import WORD_LIST, ALPHABETS

CHOSEN_WORD = random.choice(WORD_LIST)
word_length = len(CHOSEN_WORD)

END_OF_GAME = False
LIVES = 6

print(LOGO)

# Testing code
# print(f"Pssst, the solution is {CHOSEN_WORD}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Create a list of all the guessed letters
guessed_letters = []

while not END_OF_GAME:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed the letter {guess}. Try again.")

    # Check guessed letter
    for position in range(word_length):
        letter = CHOSEN_WORD[position]
        # print(f"Current position: {position}\n
        #   Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in ALPHABETS:
        print("Choose a proper alphabet!")
    elif guess not in CHOSEN_WORD and guess not in guessed_letters:
        print(f"The letter {guess} is not in the word. You lose a life.")
        LIVES -= 1
        if LIVES == 0:
            END_OF_GAME = True
            print("You lose.")
        guessed_letters.append(guess)
    else:
        guessed_letters.append(guess)

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(STAGES[LIVES])

    # Check if user has got all letters.
    if "_" not in display:
        END_OF_GAME = True
        print("You win.")
