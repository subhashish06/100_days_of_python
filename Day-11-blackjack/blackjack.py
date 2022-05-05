"""
Program: Blackjack Game
Author: Subhashish Dhar
Date: 02/09/2021
"""

import random
from blacjack_art import LOGO


def deal_card():
    """returns a random card from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    return random.choice(deck)


def score(cards):
    """returns the score of a deck. returns 0 for blackjack"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


player_cards = []
computer_cards = []

for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

print(LOGO)
print(f"Your cards: {player_cards}")
print(f"Computer's first card: {computer_cards[0]}")

SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    call = input("Type 'y' to get another card, type 'n' to pass: ")
    if call == "n":
        print(f"Computer's hand: {computer_cards}")
        while score(computer_cards) < 17:
            print("Computer is dealing another card...")
            computer_cards.append(deal_card())
            if score(computer_cards) > 21:
                print("Computer is busted! You win!")
            else:
                print(f"Computer's new hand: {computer_cards}")
        print(f"Your final hand: {player_cards}")
        print(f"Computer's final hand: {computer_cards}")
        if (21 - score(computer_cards)) > (21 - score(player_cards)):
            print("You win!")
        elif (21 - score(computer_cards)) == (21 - score(player_cards)):
            print("Game drawn!")
        else:
            print("You lose!")
        SHOULD_CONTINUE = False
    else:
        player_cards.append(deal_card())
        print(f"Your new hand: {player_cards}")
        if score(player_cards) > 21:
            print("Busted! You lose!")
            SHOULD_CONTINUE = False
