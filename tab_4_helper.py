# registration_page.py
import tkinter as tk
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from tkinter import messagebox
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Registration Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry fields for registration information
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.car_var = tk.StringVar()
        self.email_var = tk.StringVar()

        name_label = CTkLabel(self, text="Name:")
        name_label.pack(pady=5)
        name_entry = CTkEntry(self, textvariable=self.name_var)
        name_entry.pack(pady=5)

        phone_label = CTkLabel(self, text="Phone Number:")
        phone_label.pack(pady=5)
        phone_entry = CTkEntry(self, textvariable=self.phone_var)
        phone_entry.pack(pady=5)

        car_label = CTkLabel(self, text="Car Number Plate:")
        car_label.pack(pady=5)
        car_entry = CTkEntry(self, textvariable=self.car_var)
        car_entry.pack(pady=5)

        email_label = CTkLabel(self, text="Email:")
        email_label.pack(pady=5)
        email_entry = CTkEntry(self, textvariable=self.email_var)
        email_entry.pack(pady=5)

        register_button = CTkButton(self, text="Register", command=self.register_user)
        register_button.pack(pady=10)

    def register_user(self):
        # Get user registration information
        name = self.name_var.get()
        phone = self.phone_var.get()
        car_plate = self.car_var.get()
        email = self.email_var.get()

        # Validate and save user registration (you can save to a file or database)
        if name and phone and car_plate and email:
            # Save user information (implement saving logic)
            messagebox.showinfo("Registration Successful", "User registered successfully!")
            self.page_controller.show_login_page()
        else:
            messagebox.showerror("Registration Failed", "Please fill in all fields.")




# controllers\page_controller.py
from pages.registration_page import RegistrationPage

class PageController:
    # Existing code...

    def show_registration_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = RegistrationPage(self.root, self)
        self.registration_page.show()


# pages/login_page.py
from customtkinter import CTkButton

class LoginPage(BasePage):
    def create_widgets(self):
        # Existing code...

        register_button = CTkButton(self, text="Register", command=self.page_controller.show_registration_page)
        register_button.pack(pady=10)
