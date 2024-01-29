import os
import json
from tkinter import Tk, Label, Entry, Button, messagebox

class ParkingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking System")
        
        # Initialize user data paths
        self.global_users_path = os.path.join("user_data", "global_users_data", "customers_db.json")
        self.local_users_path = os.path.join("user_data", "local_user_data")
        
        # Create main frame
        self.frame = Tk()
        
        # Create and display UI
        self.create_login_page()

    def create_login_page(self):
        # Code for login page UI
        pass

    def create_register_page(self):
        # Code for register page UI
        pass

    def create_home_page(self, username):
        # Code for home page UI
        pass

    def create_user_profile_page(self, username):
        # Code for user profile page UI
        pass

    def create_booking_page(self):
        # Code for booking page UI
        pass

    def create_pg_a(self):
        # Code for page A UI
        pass

    def create_pg_b(self):
        # Code for page B UI
        pass

if __name__ == "__main__":
    root = Tk()
    parking_system = ParkingSystem(root)
    root.mainloop()







class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

# Creating an instance of MyClass
obj = MyClass(42)

# Calling the print_value method on the instance
obj.print_value()

