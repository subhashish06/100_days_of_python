"""
Program: Blog templating
Author: Subhashish Dhar
Date: 22/10/2021
"""

import requests
from flask import Flask, render_template
from post import Post

posts = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    """shows home page with all posts"""
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    """shows particular post upon clicking on Read link"""
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
