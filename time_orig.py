# from tkinter import *
# from tkcalendar import *
# from datetime import datetime

# ws = Tk()
# ws.title("Python Guides")
# ws.geometry("500x400")
# ws.config(bg="#cd950c")

# hour_string = StringVar()
# min_string = StringVar()
# last_value_sec = ""
# last_value = ""
# font_prefab = ('Times', 20)


# def display_msg():
#     date = cal.get_date()
#     formatted_date = datetime.strptime(date, "%m/%d/%y").strftime("%d/%m/%Y")
#     m = min_sb.get()
#     h = sec_hour.get()
#     s = sec.get()
#     t = f"Your Parking slot is booked for {formatted_date} at {m}:{h}:{s}."
#     book_msg_display.config(text=t)
#     print(t)

# def update_current_time():
#     current_time = datetime.now().strftime("%H:%M:%S")
#     min_sb.set(current_time.split(":")[1])
#     sec_hour.set(current_time.split(":")[0])
#     sec.set(current_time.split(":")[2])
#     ws.after(1000, update_current_time)  # Update every second

# fone = Frame(ws)
# ftwo = Frame(ws)

# fone.pack(pady=10)
# ftwo.pack(pady=10)

# sec_hour = Spinbox(
#     ftwo,
#     from_=0,
#     to=59,
#     wrap=True,
#     textvariable=min_string,
#     font=font_prefab,
#     width=2,
#     justify=CENTER
# )

# min_sb = Spinbox(
#     ftwo,
#     from_=0,
#     to=23,
#     wrap=True,
#     textvariable=hour_string,
#     width=2,
#     state="readonly",
#     font=font_prefab,
#     justify=CENTER
# )

# sec = Spinbox(
#     ftwo,
#     from_=0,
#     to=59,
#     wrap=True,
#     textvariable=sec_hour,
#     width=2,
#     font=font_prefab,
#     justify=CENTER
# )

# # if last_value == "59" and min_string.get() == "0":
# #     hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
# #     last_value = min_string.get()

# # if last_value_sec == "59" and sec_hour.get() == "0":
# #     min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)
# # if last_value == "59":
# #     hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
# #     last_value_sec = sec_hour.get()

# update_current_time()

# initial_date = datetime.now()
# cal = Calendar(
#     fone,
#     selectmode="day",
#     day=initial_date.day,
#     month=initial_date.month,
#     year=initial_date.year,
# )
# cal.pack()


# min_sb.pack(side=LEFT, fill=X, expand=True)
# sec_hour.pack(side=LEFT, fill=X, expand=True)
# sec.pack(side=LEFT, fill=X, expand=True)

# msg = Label(
#     ws,
#     text="Hour  Minute  Seconds",
#     font=("Times", 12),
#     bg="#cd950c"
# )
# msg.pack(side=TOP)

# actionBtn = Button(
#     ws,
#     text="Book Parking Slot",
#     padx=10,
#     pady=10,
#     command=display_msg
# )
# actionBtn.pack(pady=10)

# book_msg_display = Label(
#     ws,
#     text="Pick Booking Time",
#     bg="#cd950c"
# )
# book_msg_display.pack(pady=10)

# ws.mainloop()