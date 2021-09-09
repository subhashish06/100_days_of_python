"""
Program: Quiz User Interface
Author: Subhashish Dhar
Date: 04/09/2021
"""

from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    """creates the user interface"""
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR,
                                                     text='Question Text', font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image,
                                     highlightthickness=0, command=self.tick_clicked)
        self.correct_button.grid(row=2, column=0)

        incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=incorrect_image,
                                       highlightthickness=0, command=self.cross_clicked)
        self.incorrect_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """fetches the next question"""
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def tick_clicked(self):
        """gives feedback when tick is clicked"""
        self.give_feedback(self.quiz.check_answer("True"))

    def cross_clicked(self):
        """gives feedback when cross is clicked"""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """changes background color depending on feedback"""
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
