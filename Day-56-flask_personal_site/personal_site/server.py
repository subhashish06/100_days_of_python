"""
Program: Personal Site
Author: Subhashish Dhar
Date: 12/10/2021
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def say_hello():
    return render_template("subbu.html")


if __name__ == "__main__":
    app.run(debug=True)
