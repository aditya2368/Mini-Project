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
# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 0:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 1:
        print(count)
        window.after(1000, count_down,count - 1)
    else:
        start_timer()

timer_label = Label(text="TIMER",bg=YELLOW, fg=GREEN, font=(FONT_NAME,35,"bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(99, 112, image=tomato_image)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="start",command=start_timer,highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2,row=2)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()