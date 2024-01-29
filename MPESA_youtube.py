import tkinter as tk
import customtkinter as ctk

foundation_window = ctk.CTk()

mpesa_page_1 = ctk.CTkFrame(foundation_window)
mpesa_page_2 = ctk.CTkFrame(foundation_window)
mpesa_page_3 = ctk.CTkFrame(foundation_window)

# mpesa_page_1.pack(padx=20, pady=20, sticky="nsew")
# mpesa_page_2.pack(padx=20, pady=20)
# mpesa_page_3.pack(padx=20, pady=20)
mpesa_page_1.grid(row=0, column=0,sticky="nsew")
mpesa_page_2.grid(row=0, column=0, sticky="nsew")
mpesa_page_3.grid(row=0, column=0, sticky="nsew")


label_1 = ctk.CTkLabel(mpesa_page_1, text="Pay now via Mpesa?", font=("Calibri", 16))
label_1.pack(padx=20, pady=20, fill=tk.X, expand=True)

label_2 = ctk.CTkLabel(mpesa_page_2, text="Confirm Amount Payable.", font=("Calibri", 16))
label_2.pack(padx=20, pady=20, fill=tk.X, expand=True)

label_3 = ctk.CTkLabel(mpesa_page_3, text="Submit Payment.", font=("Calibri", 16))
label_3.pack(padx=20, pady=20, fill=tk.X, expand=True)


button_1a = ctk.CTkButton(mpesa_page_1, text="Exit", command=lambda:mpesa_page_1.tkraise(),font=('HP Simplified', 14, "italic"))
button_1a.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.LEFT)
button_1b = ctk.CTkButton(mpesa_page_1, text="Next", command=lambda:mpesa_page_2.tkraise(),font=('HP Simplified', 14, "italic"))
button_1b.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.RIGHT)
button_2a = ctk.CTkButton(mpesa_page_2, text="Back", command=lambda:mpesa_page_1.tkraise(),font=('HP Simplified', 14, "italic"))
button_2a.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.LEFT)
button_2b = ctk.CTkButton(mpesa_page_2, text="Next", command=lambda:mpesa_page_3.tkraise(),font=('HP Simplified', 14, "italic"))
button_2b.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.RIGHT)
button_3a = ctk.CTkButton(mpesa_page_3, text="Back", command=lambda:mpesa_page_2.tkraise(),font=('HP Simplified', 14, "italic"))
button_3a.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.LEFT)
button_3b = ctk.CTkButton(mpesa_page_3, text="Exit", command=lambda:mpesa_page_3.tkraise(),font=('HP Simplified', 14, "italic"))
button_3b.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.RIGHT)

mpesa_page_1.tkraise()
foundation_window.geometry("360x200")
foundation_window.title("Payment Page")
foundation_window.resizable(False, False)
foundation_window.mainloop()