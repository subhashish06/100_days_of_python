from tkinter import *
import pandas as pd
from random import randint
import time
BACKGROUND_COLOR = "#B1DDC6"

try:
    data_df = pd.read_csv("./data/words_to_learn.csv")
    data_dict = data_df.to_dict(orient='records')
except FileNotFoundError:
    data_df = pd.read_csv("./data/french_words.csv")
    data_dict = data_df.to_dict(orient='records')
finally:
    number_of_words = 100


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=chosen_word['English'], fill='white')


# ---------------------------- REMOVE CARD ------------------------------- #
def remove_card():
    global data_dict, number_of_words
    data_dict.remove(chosen_word)
    number_of_words -= 1
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)


# ---------------------------- CREATE NEW FLASH CARD ------------------------------- #
def draw_new_card():
    global chosen_word, flip_timer, random_word_index
    window.after_cancel(flip_timer)
    random_word_index = randint(0, number_of_words)
    canvas.itemconfig(image, image=front_image)
    chosen_word = data_dict[random_word_index]
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=chosen_word['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def tick_pressed():
    remove_card()
    draw_new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Declare all the image objects
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
tick_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")

# Create the main canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text='French', font=("Ariel", 40, "italic"))
random_word_index = randint(0, 100)
chosen_word = data_dict[random_word_index]
word = canvas.create_text(400, 263, text=chosen_word['French'], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create the buttons
correct_button = Button(image=tick_image, highlightthickness=0, command=tick_pressed)
correct_button.grid(row=1, column=0)
incorrect_button = Button(image=cross_image, highlightthickness=0, command=draw_new_card)
incorrect_button.grid(row=1, column=1)

window.mainloop()
