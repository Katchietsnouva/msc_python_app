# from tkinter import *
from tkcalendar import *
import tkinter as tk
import customtkinter as ctk
from datetime import datetime

clock_frame = ctk.CTk()
clock_frame.title("Python Guides")
clock_frame.geometry("500x400")

main_frame = ctk.CTkFrame(clock_frame)

initial_date = datetime.now()
cal = Calendar(
    main_frame,
    selectmode="day",
    day=initial_date.day,
    month=initial_date.month,
    year=initial_date.year,
    font=("Arial", 20) 
)
cal.pack(fill=tk.BOTH, expand=True)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

clock_frame.mainloop()
