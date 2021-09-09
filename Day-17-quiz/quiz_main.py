"""
Program: Quiz Main Program
Author: Subhashish Dhar
Date: 03/09/2021
"""

from data import question_data
from quiz_brain import QuizBrain, Question

question_bank = []

for question in question_data:
    QUESTION = question['text']
    ANSWER = question['answer']
    new_question = Question(QUESTION, ANSWER)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
