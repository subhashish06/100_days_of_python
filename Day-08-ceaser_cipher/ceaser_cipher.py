"""
Program: Caesar Cipher Encryption Machine
Author: Subhashish Dhar
Date: 02/09/2021
"""

from ceaser_art import LOGO

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(text, key, direction):
    """Caesar encryption function"""
    result = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if direction == "encode":
                new_index = (letter_index + key) % 26
            else:
                new_index = (letter_index - key) % 26
            result += alphabet[new_index]
        else:
            result += letter
    print(f"The {direction}d text is: {result}")


print(LOGO)
NEXT_ROUND = True
while NEXT_ROUND:
    user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))
    caesar(user_text, user_shift, user_direction)
    user_continue = input("Type 'yes' to continue or 'no' to stop\n").lower()
    if user_continue == "no":
        NEXT_ROUND = False
        print("Goodbye!")
