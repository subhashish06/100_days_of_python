"""
Program: Post Class
Author: Subhashish Dhar
Date: 26/10/2021
"""


class Post:
    """Defines the Post Class for individual posts"""

    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
