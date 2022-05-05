"""
Program: Quiz Brain Module
Author: Subhashish Dhar
Date: 03/09/2021
"""


class Question:
    """takes a text and an answer : creates a question object."""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    """takes a list of questions : creates a QuizBrain object."""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        """checks if all the questions in the list has been asked"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """asks the next question to the user"""
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question.text}. (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_ans, correct_ans):
        """checks if the user answer is correct"""
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
