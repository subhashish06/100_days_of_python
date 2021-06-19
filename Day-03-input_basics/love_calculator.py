# # Instructions
#
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
#
# > Take both people's names and check for the number of times the letters in the word TRUE occurs.
# > Then check for the number of times the letters in the word LOVE occurs.
# > Then combine these numbers to make a 2 digit number.
#
# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."`
# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`
# Otherwise, the message will just be their score. e.g.:
# `"Your score is **z**."`
#
# e.g.
# `name1 = "Angela Yu"`
# `name2 = "Jack Bauer"`
#
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
#
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
#
# Love Score = 53
# Print: "Your score is 53."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = (name1 + name2).lower()
first_digit = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
second_digit = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

love_value = int(str(first_digit) + str(second_digit))

if love_value < 10 or love_value > 90:
    print(f'Your score is {love_value}, you go together like coke and mentos.')
elif 40 < love_value < 50:
    print(f'Your score is {love_value}, you are alright together.')
else:
    print(f'Your score is {love_value}.')
