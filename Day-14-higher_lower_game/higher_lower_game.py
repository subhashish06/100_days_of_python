from higher_lower_art import logo, vs
from higher_lower_game_data import data
import random

# a function that selects a contestant from game_data
# selection needs to be random, but it cannot have the same candidate

score = 0
contestant_1 = random.choice(data)
contestant_2 = random.choice(data)
while contestant_2 == contestant_1:
    contestant_2 = random.choice(data)

print(logo)
print(f"Compare A: {contestant_1['name']}, a {contestant_1['description']}, from {contestant_1['country']}")
print(vs)
print(f"Compare B: {contestant_2['name']}, a {contestant_2['description']}, from {contestant_2['country']}")
user_choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()


def check_answer(contestant_a, contestant_b, choice):
    """
    input : the two contestants and the user answer
    output : return True is user_choice is correct otherwise False
    """
    if contestant_a['follower_count'] > contestant_b['follower_count']:
        answer = 'A'
    else:
        answer = 'B'
    if choice == answer:
        return True
    else:
        return False


def get_contestants_for_next_round(contestant):
    """
    returns a tuple of two contestants for the next round
    """
    contestant_a = contestant
    contestant_b = random.choice(data)
    while contestant_b == contestant_a:
        contestant_b = random.choice(data)
    return contestant_a, contestant_b


while check_answer(contestant_1, contestant_2, user_choice):
    score += 1
    print(f"That's right. Your score is {score}")
    contestant_1, contestant_2 = get_contestants_for_next_round(contestant_2)
    print(logo)
    print(f"Compare A: {contestant_1['name']}, a {contestant_1['description']}, from {contestant_1['country']}")
    print(vs)
    print(f"Compare B: {contestant_2['name']}, a {contestant_2['description']}, from {contestant_2['country']}")
    user_choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()

print(f"Sorry. that's wrong. Final score: {score}")
