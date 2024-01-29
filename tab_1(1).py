# controller.py
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage
from pages.booking_page import BookingPage
from pages.pg_a import PageA
from pages.pg_b import PageB
from user_data.userdata_manager import UserDataManager

class AppController:
    def __init__(self):
        self.current_page = None
        self.user_data_manager = UserDataManager()

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
        if self.user_data_manager.validate_credentials(username, password):
            self.show_home_page()
        else:
            # Show an error message or handle unsuccessful login
            pass

# userdata_manager.py (to be implemented)
class UserDataManager:
    def __init__(self):
        pass

    def validate_credentials(self, username, password):
        # Implement logic to validate user credentials
        # Check against global_users_data and local_user_data
        pass

    # Add other methods for handling user data operations


# __main__.py
from controller import AppController

if __name__ == "__main__":
    controller = AppController()
    controller.show_login_page()


# user_data/userdata_manager.py
import json
import os
class UserDataManager:
    def __init__(self):
        # Placeholder initialization
        pass

    def validate_credentials(self, username, password):
        # Placeholder validation logic
        # This is where you would check against global_users_data and local_user_data
        return True  # Placeholder return value

class UserDataManager:
    def __init__(self):
        self.global_users_path = "user_data/global_users_data/customers_db.json"
        self.local_users_path = "user_data/local_user_data/"

    def _load_global_users(self):
        try:
            with open(self.global_users_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_global_users(self, data):
        with open(self.global_users_path, 'w') as file:
            json.dump(data, file, indent=2)

    def _load_local_user(self, username):
        user_file_path = os.path.join(self.local_users_path, f"{username}_userdata.json")
        try:
            with open(user_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_local_user(self, username, data):
        user_file_path = os.path.join(self.local_users_path, f"{username}_userdata.json")
        with open(user_file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def validate_credentials(self, username, password):
        global_users = self._load_global_users()
        for user in global_users:
            if user["Name"] == username and user["Password"] == password:
                # User found in global users, now check local user data
                local_user_data = self._load_local_user(username)
                return local_user_data.get("Password") == password

        return False

    def register_user(self, username, password):
        global_users = self._load_global_users()
        user_exists = any(user["Name"] == username for user in global_users)

        if not user_exists:
            # Add user to global users
            new_user = {"Name": username, "Password": password}
            global_users.append(new_user)
            self._save_global_users(global_users)

            # Create and save local user data       
            local_user_data = {"Name": username, "Password": password}
            self._save_local_user(username, local_user_data)

            return True  # Registration successful
        else:
            return False  # User already exists
