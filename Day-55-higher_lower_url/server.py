"""
Program: Higher Lower game on web
Author: Subhashish Dhar
Date: 05/10/2021
"""

import random
from flask import Flask

app = Flask(__name__)
number = random.randint(0, 10)



@app.route("/")

def display_homepage():
    """displays the home page"""
    return '<h1 style="color:red";>Guess a number between 0 and 9</h1>" \
           "<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'



@app.route("/<int:guess>")
def display_guessed_page(guess):
    """displays the guessed page"""
    if guess == number:
        return (
            "<h1>You found me!</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        )
    if guess < number:
        return (
            "<h1>Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        )
    if guess > number:
        return (
            "<h1>Too high, try again!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        )



if __name__ == "__main__":
    app.run(debug=True)
