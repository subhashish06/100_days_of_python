"""
Program: Pomodoro Timer
Author: Subhashish Dhar
Date: 04/09/2021
"""

from tkinter import Tk, Canvas, Label, Button, PhotoImage
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #


def restart_timer():
    """restarts the timer"""
    window.after_cancel(TIMER)
    timer_label.config(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN)
    tick_label.config(text='')
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """starts the timer"""
    global REPS
    REPS += 1
    if REPS > 8:
        restart_timer()
    elif REPS % 2 != 0:
        timer_label.config(text='Work', font=(FONT_NAME, 30, 'bold'), fg=GREEN)
        countdown(WORK_MIN * 60)
    elif REPS < 8:
        timer_label.config(text='Break', font=(FONT_NAME, 30, 'bold'), fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text='Break', font=(FONT_NAME, 30, 'bold'), fg=RED)
        countdown(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    """
    input : integer value of number of seconds
    """
    time_min = count // 60
    time_sec = count % 60
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    if time_min < 10:
        time_min = f"0{time_min}"
    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        work_sessions = REPS // 2
        tick_label.config(text="🗸" * work_sessions)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(fg=GREEN, bg=YELLOW)
timer_label.config(text='Timer', font=(FONT_NAME, 30, 'bold'))
timer_label.grid(column=1, row=0)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.config(font=(FONT_NAME, 14, 'bold'))
tick_label.grid(column=1, row=3)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=restart_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
