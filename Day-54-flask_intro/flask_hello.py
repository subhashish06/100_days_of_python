"""
Program: Hello World with Flask
Author: Subhashish Dhar
Date: 04/10/2021
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye_world():
    return 'Bye, World!'


if __name__ == "__main__":
    app.run()
