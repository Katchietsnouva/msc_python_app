# Main Application (main.py
import tkinter as tk
from pages import home_page
from user_data import global_users_data, local_user_data

class ParkingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parking Space App")
        self.geometry("800x600")

        # Initialize data
        self.all_users_data = global_users_data.load_all_users_data()
        self.current_user_data = None

        # Load the home page
        self.switch_to_page(home_page.HomePage)

    def switch_to_page(self, page_class):
        if self.current_user_data is None and page_class != home_page.HomePage:
            # Redirect to login page if no user is logged in
            page_class = home_page.LoginPage

        page = page_class(self)
        page.pack(fill=tk.BOTH, expand=True)
        page.update_content()

if __name__ == "__main__":
    app = ParkingApp()
    app.mainloop()


# user data management
# global_users_data.py
import json

def load_all_users_data():
    try:
        with open("user_data/global_users_data/customers_db.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_all_users_data(users_data):
    with open("user_data/global_users_data/customers_db.json", "w") as file:
        json.dump(users_data, file, indent=2)

# local_user_data.py
import json
import os
from datetime import datetime

def load_user_data(user_name):
    file_path = f"user_data/local_user_data/{user_name}_userdata.json"
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def save_user_data(user_name, data):
    file_path = f"user_data/local_user_data/{user_name}_userdata.json"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def get_most_recent_user():
    user_files = os.listdir("user_data/local_user_data/")
    if not user_files:
        return None

    most_recent_file = max(user_files, key=lambda f: os.path.getmtime(f"user_data/local_user_data/{f}"))
    user_name = most_recent_file.split("_")[0]
    return user_name

# pages
# base_page.py
import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def update_content(self):
        pass

# home_page.py
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, master):
        super().__init__(master)

        # Create UI elements for the home page
        # Add buttons for switching to other pages
        # Display current user's name in a greet format

# login_page.py
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, master):
        super().__init__(master)

        # Create UI elements for the login page
        # Add logic for handling login and redirection to register page

# register_page.py
from .base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, master):
        super().__init__(master)

        # Create UI elements for the register page
        # Add logic for handling user registration

# user_profile_page.py, booking_page.py, pg_a.py, pg_b.py
# Similar to HomePage, LoginPage, and RegisterPage, implement UI and logic for these pages
 










