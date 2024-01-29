# __main__.py
import tkinter as tk
from pages import login_page, register_page, home_page

class ParkingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parking Space App")
        self.geometry("600x400")

        self.current_user = None

        # Create instances of pages
        self.login_page = login_page.LoginPage(self, self.show_home_page)
        self.register_page = register_page.RegisterPage(self, self.show_login_page)
        self.home_page = home_page.HomePage(self, self.show_user_profile_page, self.show_booking_page, self.show_pg_a, self.show_pg_b)

        # Show login page by default
        self.show_login_page()

    def show_login_page(self):
        self.login_page.show()
        self.current_user = None

    def show_register_page(self):
        self.register_page.show()

    def show_home_page(self, username):
        self.home_page.show(username)
        self.current_user = username

    def show_user_profile_page(self):
        # Implement the logic to show the user profile page
        pass

    def show_booking_page(self):
        # Implement the logic to show the booking page
        pass

    def show_pg_a(self):
        # Implement the logic to show page A
        pass

    def show_pg_b(self):
        # Implement the logic to show page B
        pass

if __name__ == "__main__":
    app = ParkingApp()
    app.mainloop()


# pages/base_page.py

import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

    def show(self):
        self.lift()


# pages/login_page.py

from .base_page import BasePage
import tkinter as tk

class LoginPage(BasePage):
    def __init__(self, master, show_home_page_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.show_home_page_callback = show_home_page_callback

        # Add your login page UI elements here
        self.label = tk.Label(self, text="Login Page")
        self.label.pack()

        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.btn_login = tk.Button(self, text="Login", command=self.login)
        self.btn_register = tk.Button(self, text="Register", command=self.master.show_register_page)

        # Place your UI elements using grid or pack 

    def login(self):
        # Implement the login logic here
        # Check if the user exists in global_users_data and local_user_data
        # If login successful, show the home page
        # Otherwise, show an error message
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Add your login logic here
        self.show_home_page_callback(username)
