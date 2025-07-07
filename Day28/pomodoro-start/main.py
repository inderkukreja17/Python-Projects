from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=NONE

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    Label.config(Timer_label, text="Timer", font=(FONT_NAME, 38), fg=GREEN, bg=YELLOW)
    check_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps
    reps += 1

    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        Label.config(Timer_label, text="Break", font=(FONT_NAME, 38), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Label.config(Timer_label, text="Break", font=(FONT_NAME, 38), fg=PINK, bg=YELLOW)
    else:
        count_down(works_sec)
        Label.config(Timer_label, text="Work", font=(FONT_NAME, 38), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global  timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer=window.after(1000, count_down, count - 1)
    else:
        timer_start()
        marks=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks+="✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # To store any image in a variable
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

Timer_label = Label(text="Timer", font=(FONT_NAME, 38), fg=GREEN, bg=YELLOW)
Timer_label.grid(column=1, row=0)

check_label = Label(text="✔", font=(FONT_NAME, 38), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

button_start = Button(text="Start", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 10), command=timer_start, bd=0, highlightbackground=YELLOW)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 10), bd=0, highlightbackground=YELLOW,command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
