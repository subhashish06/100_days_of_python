"""
Program: Quiz Brain
Author: Subhashish Dhar
Date: 04/09/2021
"""

import html


class QuizBrain:
    """creates the quizbrain object from the questions list"""

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """checks if more questions are there in list to be asked"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """fetches the next question"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False)? "
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # # self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        """checks the answer and return True or False"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
