"""
Program: Quiz Model
Author: Subhashish Dhar
Date: 04/09/2021
"""


class Question:
    """creates the question object"""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
