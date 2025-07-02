from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#f4c0c4"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN *60
    shot_sec = SHORT_BREAK_MIN *60
    long_sec = LONG_BREAK_MIN * 60

    if reps %  8==0:
        count_down(long_sec)
        label.config(text="Break" , fg=RED)
    elif reps % 2 ==0:
        count_down(shot_sec)
        label.config(text="Break" , fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work" , fg=GREEN)

        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text ,text=f"{count_min}:{count_sec}")
    if count >0:
       timer = window.after(1000 , count_down , count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range (work_session):
            mark += "✓"
            check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")#means tomato in italian 
window.config(padx=100, pady=50 , bg=YELLOW) 

# #---------------------LABEL--------------
label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)
# #-------------------------------------------------------------------



# #------------------------------TOMATO PHOTO------------------

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_ing)
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# #----------------------------------------------------------------------
#---------START BUTTON-----------------
start_button = Button(text="START" , command=start_timer)
start_button.grid(row=2, column=0)
#------------------------------------------
#----------------RESET BUTTON---------------

reset_button = Button(text="RESET" , command=reset_timer )
reset_button.grid(row=2 , column=3)
#--------------------------------------

check_mark = Label( bg=YELLOW , fg=GREEN ,font=(35))
check_mark.grid(row=3 , column=1)




window.mainloop()


