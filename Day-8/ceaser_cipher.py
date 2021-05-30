from ceaser_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(text, key, direction):
    result = ''
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if direction == 'encode':
                new_index = (letter_index + key) % 26
            else:
                new_index = (letter_index - key) % 26
            result += alphabet[new_index]
        else:
            result += letter
    print(f"The {direction}d text is: {result}")


print(logo)
next_round = True
while next_round:
    user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))
    caeser(user_text, user_shift, user_direction)
    user_continue = input("Type 'yes' to continue or 'no' to stop\n").lower()
    if user_continue == 'no':
        next_round = False
