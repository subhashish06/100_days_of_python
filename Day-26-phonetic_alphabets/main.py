import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Type a word: ").upper()
user_word_code = [code_dict[letter] for letter in user_word]

print(user_word_code)
