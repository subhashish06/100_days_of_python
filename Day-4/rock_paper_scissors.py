import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import sys
input_code = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: ")

if input_code == '0':
    player_choice = rock
elif input_code == '1':
    player_choice = paper
elif input_code == '2':
    player_choice = scissors
else:
    print("You can't even choose! You lose!")
    sys.exit()

import random

computer_choice = random.choice([rock, paper, scissors])

print(player_choice)
print("Computer chose:")
print(computer_choice)

if player_choice == rock:
    if computer_choice == rock:
        print("You draw!")
    elif computer_choice == paper:
        print("You lose!")
    else:
        print("You win!")
elif player_choice == paper:
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("You draw!")
    else:
        print("You lose!")
else:
    if computer_choice == rock:
        print("You lose!")
    elif computer_choice == paper:
        print("You win!")
    else:
        print("You draw!")
