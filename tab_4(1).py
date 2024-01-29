# main.py

import tkinter as tk
from controllers.page_controller import PageController
from controllers.user_controller import UserController
from pages.login_page import LoginPage
from pages.home_page import HomePage

class ParkingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parking Space App")
        self.geometry("600x400")

        self.page_controller = PageController(self)
        self.user_controller = UserController()

        self.login_page = LoginPage(self, self.page_controller)
        self.home_page = HomePage(self, self.page_controller)

        self.show_login_page()

    def show_login_page(self):
        self.login_page.show()

    def show_home_page(self):
        self.home_page.display_greeting()
        self.home_page.show()

if __name__ == "__main__":
    app = ParkingApp()
    app.mainloop()



# pages/login_page.py v1
import tkinter as tk
from customtkinter import CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from controllers.page_controller import PageController
from controllers.user_controller import UserController

class LoginPage(tk.Frame):
    def __init__(self, master, page_controller: PageController, user_controller: UserController):
        super().__init__(master)
        self.page_controller = page_controller
        self.user_controller = user_controller

        self.create_widgets()

    def create_widgets(self):
        # Your login page UI creation code goes here

        # Example labels, entries, and buttons
        label_username = CTkLabel(self, text="Username:")
        entry_username = CTkEntry(self)
        label_password = CTkLabel(self, text="Password:")
        entry_password = CTkEntry(self, show="*")
        checkbox_remember = CTkCheckBox(self, text="Remember me?")
        button_login = CTkButton(self, text="Login", command=self.handle_login)

        # Place your widgets using grid, pack, or place

    def handle_login(self):
        # Your login logic goes here
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Example: Check credentials with user controller
        if self.user_controller.authenticate_user(username, password):
            self.page_controller.show_home_page()
        else:
            # Display an error message or handle unsuccessful login
            pass

    def show(self):
        self.pack(fill=tk.BOTH, expand=True)

# pages/base_page.py
import tkinter as tk
from customtkinter import CTkButton

class BasePage(tk.Frame):
    def __init__(self, master, page_controller):
        super().__init__(master)
        self.page_controller = page_controller

        self.create_widgets()

    def create_widgets(self):
        # Common widgets for all pages can go here
        # button_home = CTkButton(self, text="Home", command=self.page_controller.show_home_page)
        # button_logout = CTkButton(self, text="Logout", command=self.page_controller.logout)

        # Place your widgets using grid, pack, or place
        pass

    # def show(self):
    #     self.pack(fill=tk.BOTH, expand=True)



# pages/login_page.py v2
import tkinter as tk
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from tkinter import messagebox
from base_page import BasePage

class LoginPage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the login page
        label_title = CTkLabel(self, text="Login Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Username and Password entry fields
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        username_label = CTkLabel(self, text="Username:")
        username_label.pack(pady=5)
        username_entry = CTkEntry(self, textvariable=self.username_var)
        username_entry.pack(pady=5)

        password_label = CTkLabel(self, text="Password:")
        password_label.pack(pady=5)
        password_entry = CTkEntry(self, textvariable=self.password_var, show="*")
        password_entry.pack(pady=5)

        # Remember me checkbox
        self.checkvalue = tk.IntVar(value=0)
        checkbtn = CTkCheckBox(self, text="Remember me?", variable=self.checkvalue)
        checkbtn.pack(pady=5)

        login_button = CTkButton(self, text="Login", command=self.getvals_login)
        login_button.pack(pady=10)

        # Register new user button
        register_button = CTkButton(self, text="Register New User", command=self.page_controller.show_register_page)
        register_button.pack(pady=10)

    def getvals_login(self):
        # Add your logic to validate login credentials
        user_name = self.username_var.get()
        password = self.password_var.get()
        print(f"User: {user_name}, Password: {password}")
        # You can perform authentication logic here
        user_authenticated = self.authenticate_user(user_name, password)

        if user_authenticated:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def authenticate_user(self, username, password):
        # Replace this with your authentication logic
        # For demonstration, let's check if the username is "admin" and password is "password"
        return username == "a" and password == "b"



# pages/register_page.py
import tkinter as tk
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from base_page import BasePage

class RegisterPage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the register page
        label_title = CTkLabel(self, text="Registration Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Form fields
        self.entry_name = CTkEntry(self, placeholder="Enter your name")
        self.entry_password = CTkEntry(self, placeholder="Enter your password", show="*")

        # Remember me checkbox
        self.checkvalue = tk.IntVar(value=0)
        checkbtn = CTkCheckBox(self, text="Remember me?", variable=self.checkvalue)
        checkbtn.pack(pady=5)

        # Register button
        register_button = CTkButton(self, text="Register", command=self.validate_registration)
        register_button.pack(pady=10)

        # Back to login button
        back_button = CTkButton(self, text="Back to Login", command=self.page_controller.show_login_page)
        back_button.pack(pady=10)

    def validate_registration(self):
        # Add your logic to validate registration details
        user_name = self.entry_name.get()
        password = self.entry_password.get()

        # Add logic to check if the user already exists and save the registration details
        # For now, let's just print the registration details
        print("Validating registration...")
        print(f"User: {user_name}, Password: {password}")

        # Example: If registration is successful, show a success message
        self.show_info_message("Registration Successful", "You have been successfully registered!")

        # You can add further logic to navigate to another page or perform additional actions


# pages/home_page.py
from customtkinter import CTkButton, CTkLabel
from base_page import BasePage

class HomePage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the home page
        label_title = CTkLabel(self, text="Home Page", font=("Helvetica", 18, "bold"))
        label_title.pack(pady=20)

        # Add more widgets or buttons as needed
        manage_parking_button = CTkButton(self, text="Manage Parking", command=self.manage_parking)
        manage_parking_button.pack(pady=10)

        view_reports_button = CTkButton(self, text="View Reports", command=self.view_reports)
        view_reports_button.pack(pady=10)

        logout_button = CTkButton(self, text="Logout", command=self.page_controller.show_login_page)
        logout_button.pack(pady=10)

        exit_button = CTkButton(self, text="Exit", command=self.page_controller.exit_application)
        exit_button.pack(pady=10)

    def manage_parking(self):
        # Functionality for managing parking
        print("Manage Parking")

    def view_reports(self):
        # Functionality for viewing reports
        print("View Reports")


# page_controller.py
from login_page import LoginPage
from home_page import HomePage

class PageController:
    def __init__(self, root):
        self.root = root
        self.show_login_page()

    def show_login_page(self):
        self.clear_current_page()
        self.current_page = LoginPage(self.root, self)

    def show_home_page(self):
        self.clear_current_page()
        self.current_page = HomePage(self.root, self)

    def clear_current_page(self):
        if hasattr(self, 'current_page'):
            self.current_page.destroy()
