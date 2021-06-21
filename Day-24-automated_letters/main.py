# Create a letter using starting_letter.txt for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names_file = "Input/Names/invited_names.txt"
starting_file = "Input/Letters/starting_letter.txt"

# Read the names from the file and save in a list
with open(names_file, mode='r') as f:
    content = f.readlines()

# Strip the newline that is added to each name by the readlines() method
invitees = []
for line in content:
    name = line.rstrip('\n')
    invitees.append(name)

with open(starting_file, mode='r') as f:
    generic_content = f.read()

for name in invitees:
    personalised_content = generic_content.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w') as f:
        f.write(personalised_content)
