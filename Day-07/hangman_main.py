#Step 5

import random
from hangman_art import logo, stages
from hangman_words import word_list, alphabets

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Create a list of all the guessed letters
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
      print(f"You have already guessed the letter {guess}. Try again.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in alphabets:
        print("Choose a proper alphabet!")
    elif guess not in chosen_word and guess not in guessed_letters:
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        guessed_letters.append(guess)
    else:
        guessed_letters.append(guess)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(stages[lives])

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")