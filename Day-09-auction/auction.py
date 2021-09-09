"""
Program: Auction
Author: Subhashish Dhar
Date: 02/09/2021
"""

from auction_art import LOGO
print(LOGO)

SHOULD_CONTINUE = True
bidders = {}
while SHOULD_CONTINUE:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if more_bidders == 'no':
        SHOULD_CONTINUE = False

# Code to get the key,value pair from a dictionary with highest value.
highest_bidder_tuple = max(bidders.items(), key=lambda i: i[1])

print(f"The winner is {highest_bidder_tuple[0]} with a bid of {highest_bidder_tuple[1]}")
