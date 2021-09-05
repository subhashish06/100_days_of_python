"""
Program: Automated Letter Sender
Author: Subhashish Dhar
Date: 03/09/2021
"""

# Create a letter using starting_letter.txt for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

NAMES = "Input/Names/invited_names.txt"
DRAFT = "Input/Letters/starting_letter.txt"

# Read the names from the file and save in a list
with open(NAMES, mode='r', encoding='utf-8') as file_handler:
    content = file_handler.readlines()

# Strip the newline that is added to each name by the readlines() method
invitees = []
for line in content:
    name = line.rstrip('\n')
    invitees.append(name)

with open(DRAFT, mode='r', encoding='utf-8') as file_handler:
    generic_content = file_handler.read()

for name in invitees:
    personalised_content = generic_content.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w', encoding='utf-8') \
            as file_handler:
        file_handler.write(personalised_content)
