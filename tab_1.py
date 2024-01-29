# main.py
from pages import HomePage

if __name__ == "__main__":
    home_page = HomePage()
    home_page.show()

# pages/home_page.py
import tkinter as tk
from pages import LoginPage, UserProfilePage, BookingPage, PageA, PageB

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # UI/UX design for the home page

        # Buttons for navigating to other pages
        self.btn_profile = tk.Button(self, text="User Profile", command=self.show_profile)
        self.btn_booking = tk.Button(self, text="Booking Page", command=self.show_booking)
        self.btn_page_a = tk.Button(self, text="Page A", command=self.show_page_a)
        self.btn_page_b = tk.Button(self, text="Page B", command=self.show_page_b)

    def show_profile(self):
        UserProfilePage(self).show()

    def show_booking(self):
        BookingPage(self).show()

    def show_page_a(self):
        PageA(self).show()

    def show_page_b(self):
        PageB(self).show()

# Implement similar structures for other pages.

# Consider using a controller to manage page navigation and data.


# pages/__init__.py

# Define a variable to be used across modules in the 'pages' package
package_variable = "This is a variable defined in the pages package."

# You can also import specific modules to make them directly accessible
from .login_page import LoginPage
from .register_page import RegisterPage
from .home_page import HomePage
# ... import other modules as needed




# pages/home_page.py
from . import package_variable
from .login_page import LoginPage

print(package_variable)

# Use the imported LoginPage class
login_page_instance = LoginPage()






# controller.py
class AppController:
    def __init__(self):
        self.current_page = None
        self.user_data_manager = UserDataManager()  # You need to implement this class

    def show_home_page(self):
        self.current_page = HomePage(self)
        self.current_page.show()

    def show_login_page(self):
        self.current_page = LoginPage(self)
        self.current_page.show()

    def show_user_profile_page(self):
        self.current_page = UserProfilePage(self)
        self.current_page.show()

    def show_booking_page(self):
        self.current_page = BookingPage(self)
        self.current_page.show()

    def show_page_a(self):
        self.current_page = PageA(self)
        self.current_page.show()

    def show_page_b(self):
        self.current_page = PageB(self)
        self.current_page.show()

    def handle_login(self, username, password):
        # Implement logic to check credentials
        if self.user_data_manager.validate_credentials(username, password):
            self.show_home_page()
        else:
            print("error")
            # Show an error message or handle unsuccessful login

# userdata_manager.py (to be implemented)
class UserDataManager:
    def __init__(self):
        pass

    def validate_credentials(self, username, password):
        # Implement logic to validate user credentials
        # Check against global_users_data and local_user_data
        pass

    # Add other methods for handling user data operations

# Modify pages accordingly to accept the controller
# pages/home_page.py (an example modification)
class HomePage(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        # UI/UX design for the home page


