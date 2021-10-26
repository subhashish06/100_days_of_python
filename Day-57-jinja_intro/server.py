"""
Program: Dynamic Blog using Jinja
Author: Subhashish Dhar
Date: 22/10/2021
"""

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    """prints home page"""
    return "<h1>Guess Age and Gender Game</h1>"


@app.route("/<name>")
def guess_page(name):
    """renders template depending upon <name> passed"""
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template("index.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
