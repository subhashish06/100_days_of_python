"""
Program: Phonetic Alphabets Program
Author: Subhashish Dhar
Date: 03/09/2021
"""

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    """asks the user for a word and generates the phonetics for each letter"""
    user_word = input("Type a word: ").upper()
    try:
        user_word_code = [code_dict[letter] for letter in user_word]
    except KeyError:
        print("Please use only letters!")
        generate_phonetic()
    else:
        print(user_word_code)


generate_phonetic()
