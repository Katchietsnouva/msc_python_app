# BasePage (base_page.py)
import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def show(self):
        self.lift()

    def hide(self):
        self.lower()


# login_page.py
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, master=None):
        super().__init__(master)
        # Add your login page UI elements here

    def login(self):
        # Add login logic here
        pass

    def register(self):
        # Add logic to switch to register page
        pass

# register_page.py
from .base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, master=None):
        super().__init__(master)
        # Add your register page UI elements here

    def register_user(self):
        # Add logic to register a new user
        # Save data to global_users_data and local_user_data folders
        pass

# home_page.py
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, master=None, current_user=None):
        super().__init__(master)
        self.current_user = current_user
        # Add your home page UI elements here

    def display_greeting(self):
        # Add logic to display a greeting with the current user's name
        pass








#  MVC STRUCTURE:MVC pattern for parking space app. 
# app_structure_parking_sys/
# |-- controllers/
# |   |-- __init__.py
# |   |-- page_controller.py
# |   |-- user_controller.py
# |-- models/
# |   |-- __init__.py
# |   |-- user_model.py
# |-- pages/
# |   |-- __init__.py
# |   |-- base_page.py
# |   |-- login_page.py
# |   |-- registration_page
# |   |-- home_page.py
# |   |-- booking_page.py
# |   |-- extend_parking_page.py
# |   |-- payment_page.py
# |   |-- profit_loss_page.py 
# |-- user_data/
# |   |-- __init__.py
# |   |-- global_users_data/
# |   |   |-- customers_db.json
# |   |-- local_user_data/
# |       |-- Sharon_userdata.json
# |       |-- Paul_userdata.json
# |-- __main__.py

# CONTROLLERS
# controllers/page_controller.py
class PageController:
    def __init__(self, app):
        self.app = app

    def show_login_page(self):
        self.app.show_login_page()

    def show_register_page(self):
        self.app.show_register_page()

    def show_home_page(self, current_user):
        self.app.show_home_page(current_user)

# controllers/user_controller.py
import os
import json
from models.user_model import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self, name, password):
        return self.user_model.register_user(name, password)

    def authenticate_user(self, name, password):
        return self.user_model.authenticate_user(name, password)

    def get_current_user_data(self):
        return self.user_model.get_current_user_data()
    
# MODELS
# models/user_model.py
import os
import json

class UserModel:
    USER_DATA_PATH = "user_data/local_user_data"

    def register_user(self, name, password):
        # Add logic to register a new user
        # Save data to global_users_data and local_user_data folders
        return True  # Placeholder, replace with actual logic

    def authenticate_user(self, name, password):
        # Add logic to authenticate user
        return True  # Placeholder, replace with actual logic

    def get_current_user_data(self):
        # Add logic to get current user data
        return {}  # Placeholder, replace with actual logic


# PAGES
# pages/base_page.py
import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def show(self):
        self.lift()

    def hide(self):
        self.lower()

# pages/login_page.py
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        # Add your login page UI elements here

    def login(self):
        # Add login logic here
        pass

    def register(self):
        # Add logic to switch to register page
        self.controller.show_register_page()


# pages/register_page.py
from .base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        # Add your register page UI elements here

    def register_user(self):
        # Add logic to register a new user
        pass

# pages/home_page.py
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, master=None, controller=None, current_user=None):
        super().__init__(master)
        self.controller = controller
        self.current_user = current_user
        # Add your home page UI elements here

    def display_greeting(self):
        # Add logic to display a greeting with the current user's name
        pass

    
# __main__.py
import tkinter as tk
from controllers.page_controller import PageController
from controllers.user_controller import UserController
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage

class ParkingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parking Space App")
        self.geometry("600x400")

        self.page_controller = PageController(self)
        self.user_controller = UserController()

        self.login_page = LoginPage(self, self.page_controller)
        self.register_page = RegisterPage(self, self.page_controller)
        self.home_page = HomePage(self, self.page_controller)

        self.show_login_page()

    def show_login_page(self):
        self.login_page.show()

    def show_register_page(self):
        self.register_page.show()

    def show_home_page(self, current_user):
        self.home_page.display_greeting()
        self.home_page.show()

if __name__ == "__main__":
    app = ParkingApp()
    app.mainloop()











class UserController:
    def __init__(self):
        self.users_data_path = "user_data/global_users_data/customers_db.json"
        self.users_data = self.load_or_create_users_data()

    def save_users_data(self):
        with open(self.users_data_path, "w") as file:
            json.dump(self.users_data, file, indent=4)

    def load_users_data(self):
        with open(self.users_data_path, "r") as file:
            return json.load(file)

    def load_or_create_users_data(self):
        directory = os.path.dirname(self.users_data_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.users_data_path):
            users_data = []
            self.save_users_data()
        else:
            users_data = self.load_users_data()

        return users_data

    def register_user(self, user_model):
        # Check if the username is already taken
        if any(user["username"] == user_model.username for user in self.users_data):
            return False  # Username is taken
        else:
            self.users_data.append(vars(user_model))
            self.save_users_data()
            return True  # Registration successful

    def authenticate_user(self, username, password):
        return any(user["username"] == username and user["password"] == password for user in self.users_data)

