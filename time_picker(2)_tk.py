from tkinter import *
from tkcalendar import *
import tkinter as tk
import customtkinter as ctk
from datetime import datetime

clock_frame = ctk.Tk()
clock_frame.title("Python Guides")
clock_frame.geometry("500x400")
clock_frame.config(bg="#cd950c")

hour_string = StringVar()
min_string = StringVar()
sec_string = StringVar()
last_value_sec = ""
last_value = ""
font_prefab = ('Times', 20)


def display_msg():
    date = cal.get_date()
    formatted_date = datetime.strptime(date, "%m/%d/%y").strftime("%d/%m/%Y")
    hr_d = hr_box.get()
    min_d = min_box.get()
    sec_d = sec_box.get()
    t = f"Your Parking slot is booked for {formatted_date} at {hr_d}:{min_d}:{sec_d}."
    book_msg_display.config(text=t)
    print(t)


def update_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time)
    
    hour_value = current_time.split(":")[0]
    print(hour_value)
    min_value = current_time.split(":")[1]
    print(min_value)
    sec_value = current_time.split(":")[2]
    print(sec_value)

    # Update the Spinbox values
    hr_box.delete(0, "end")
    hr_box.insert(0, hour_value)
    
    min_box.delete(0, "end")
    min_box.insert(0, min_value)
    
    sec_box.delete(0, "end")
    sec_box.insert(0, sec_value)

    clock_frame.after(1000, update_current_time)

fone = Frame(clock_frame)
ftwo = Frame(clock_frame)

fone.pack(pady=10)
ftwo.pack(pady=10)

hr_box = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    font=font_prefab,
    width=2,
    justify=CENTER
)

min_box = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    width=2,
    # state="readonly",
    font=font_prefab,
    justify=CENTER
)

sec_box = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_string,
    width=2,
    font=font_prefab,
    justify=CENTER
)

update_current_time()  # Call the function to update time continuously

initial_date = datetime.now()
cal = Calendar(
    fone,
    selectmode="day",
    day=initial_date.day,
    month=initial_date.month,
    year=initial_date.year,
)
cal.pack()


hr_box.pack(side=LEFT, fill=X, expand=True)
min_box.pack(side=LEFT, fill=X, expand=True)
sec_box.pack(side=LEFT, fill=X, expand=True)

msg = Label(
    clock_frame,
    text="Hour  Minute  Seconds",
    font=("Times", 12),
    bg="#cd950c"
)
msg.pack(side=TOP)

actionBtn = Button(
    clock_frame,
    text="Book Parking Slot",
    padx=10,
    pady=10,
    command=display_msg
)
actionBtn.pack(pady=10)

book_msg_display = Label(
    clock_frame,
    text="Pick Booking Time",
    bg="#cd950c"
)
book_msg_display.pack(pady=10)

clock_frame.mainloop()
