from number_guess_art import logo
import random

secret_number = random.randint(1,100)
is_game_over = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Psst.. the correct answer is {secret_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    life = 10
elif difficulty == 'hard':
    life = 5
else:
    print("Options are only 'easy' and 'hard'.")
    is_game_over = True


while not is_game_over:
    print(f"You have {life} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
        is_game_over = True
    else:
        life -= 1
        if life == 0:
            print("You run out of attempts. You lose!")
            is_game_over = True
        else:
            if user_guess > secret_number:
                print("Too High.\nGuess again.")
            else:
                print("Too Low.\nGuess again.")

