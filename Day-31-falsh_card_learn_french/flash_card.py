"""
Program: Flash Cards to learn French
Author: Subhashish Dhar
Date: 04/09/2021
"""

from tkinter import Button, Tk, Canvas, PhotoImage
from random import randint
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    data_df = pd.read_csv("./data/words_to_learn.csv")
    DATA = data_df.to_dict(orient='records')
except FileNotFoundError:
    data_df = pd.read_csv("./data/french_words.csv")
    DATA = data_df.to_dict(orient='records')
finally:
    WORDS_COUNT = 100


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    """flips the card"""
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=CHOSEN_WORD['English'], fill='white')


# ---------------------------- REMOVE CARD ------------------------------- #
def remove_card():
    """removes the word from the 'to learn' dictionary"""
    global DATA, WORDS_COUNT
    DATA.remove(CHOSEN_WORD)
    WORDS_COUNT -= 1
    new_data = pd.DataFrame(DATA)
    new_data.to_csv("./data/words_to_learn.csv", index=False)


# ---------------------------- CREATE NEW FLASH CARD ------------------------------- #
def draw_new_card():
    """draws new card"""
    global CHOSEN_WORD, FLIP_TIMER, INDEX
    window.after_cancel(FLIP_TIMER)
    INDEX = randint(0, WORDS_COUNT)
    canvas.itemconfig(image, image=front_image)
    CHOSEN_WORD = DATA[INDEX]
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=CHOSEN_WORD['French'], fill='black')
    FLIP_TIMER = window.after(3000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def tick_pressed():
    """action function : clicking tick"""
    remove_card()
    draw_new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

FLIP_TIMER = window.after(3000, func=flip_card)

# Declare all the image objects
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
tick_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")

# Create the main canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text='French', font=("Ariel", 40, "italic"))
INDEX = randint(0, 100)
CHOSEN_WORD = DATA[INDEX]
word = canvas.create_text(400, 263, text=CHOSEN_WORD['French'], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create the buttons
correct_button = Button(image=tick_image, highlightthickness=0, command=tick_pressed)
correct_button.grid(row=1, column=0)
incorrect_button = Button(image=cross_image, highlightthickness=0, command=draw_new_card)
incorrect_button.grid(row=1, column=1)

window.mainloop()
