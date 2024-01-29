import datetime
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from tkinter import messagebox


# models/user_model.py
class UserModel:
    def __init__(self, username, password, name, phone, car_plate, email):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.car_plate = car_plate
        self.email = email

# controllers/user_controller.py
import json
import os
# from pathlib import Path

class UserController:
    def __init__(self):
        # user_data_path = "user_data\\"
        self.users_data_path = "user_data\\global_users_data\\customers_db.json"
        # self.users_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "user_data/global_users_data/customers_db.json"))
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
            self.users_data = []
            self.save_users_data()
        else:
            self.users_data = self.load_users_data()
        return self.users_data

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


class BasePage(ctk.CTkFrame):
    def __init__(self, master, page_controller):
        super().__init__(master)
        self.page_controller = page_controller
        self.create_widgets()

    def create_widgets(self):
        # Common widgets for all pages can go here
        pass

    def show(self):
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        if self.winfo_ismapped():  # Check if the widget is currently visible
            self.pack_forget()

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

        self.checkvalue = tk.IntVar(value=0)
        checkbtn = CTkCheckBox(self, text="Remember me?", variable=self.checkvalue)
        checkbtn.pack(pady=5)

        login_button = CTkButton(self, text="Login", command=self.getvals_login)
        login_button.pack(pady=10)

        register_button = CTkButton(self, text="Register", command=self.page_controller.show_registration_page)
        register_button.pack(pady=10)



    def getvals_login(self):
        user_name = self.username_var.get()
        password = self.password_var.get()
        # user_authenticated = self.authenticate_user(user_name, password)
        user_authenticated = self.page_controller.user_controller.authenticate_user(user_name, password)

        if user_authenticated:
            messagebox.showinfo("Login Successful", f"Welcome, {user_name}!\nWe missed you.")
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    # def authenticate_user(self, username, password):
    #     return username == "a" and password == "b"

class HomePage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the home page
        greeting_label = CTkLabel(self, text="Welcome to the Home Page!", font=("ar", 15, "bold"))
        greeting_label.pack(pady=20)

        logout_button = CTkButton(self, text="Logout", command=self.page_controller.show_login_page)
        logout_button.pack(pady=10)

        Car_register_button = CTkButton(self, text="Register", command=self.page_controller.show_registration_page)
        Car_register_button.pack(pady=10)

        book_parking_button = CTkButton(self, text="Book Parking", command=self.page_controller.show_booking_page)
        book_parking_button.pack(pady=10)

        extend_parking_button = CTkButton(self, text="Extend Parking", command=self.page_controller.show_extend_parking_page)
        extend_parking_button.pack(pady=10)

        profit_loss_button = CTkButton(self, text="Profit/Loss", command=self.page_controller.show_profit_loss_page)
        profit_loss_button.pack(pady=10)

# controllers/page_controller.py
# from controllers.user_controller import UserController  # Import UserController
class PageController:
    def __init__(self, root):
        self.root = root
        self.login_page = LoginPage(root, self)
        self.home_page = HomePage(root, self)
        self.registration_page = RegisterPage(root, self)
        self.user_controller = UserController()  
        self.booking_page = BookingPage(root, self)
        self.extend_parking_page = ExtendParkingPage(root, self)
        self.payment_page = PaymentPage(root, self)
        self.profit_loss_page = ProfitLossPage(root, self)
        self.current_page = None

        self.show_login_page()

    def show_login_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.login_page
        self.login_page.show()

    def show_home_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.home_page
        self.home_page.show()

    def show_registration_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.registration_page
        self.registration_page.show()
    
    def show_booking_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.booking_page
        self.booking_page.show()

    def show_extend_parking_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.extend_parking_page
        self.extend_parking_page.show()

    def show_payment_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.payment_page
        self.payment_page.show()

    def show_profit_loss_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.profit_loss_page
        self.profit_loss_page.show()


# pages/register_page.py
# class RegistrationPage(BasePage):
class RegisterPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Account Creation", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry fields for registration in  formation
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.car_var = tk.StringVar()
        self.email_var = tk.StringVar()

        username_label = CTkLabel(self, text="Username:")
        username_label.pack(pady=5)
        username_entry = CTkEntry(self, textvariable=self.username_var)
        username_entry.pack(pady=5)

        password_label = CTkLabel(self, text="Password:")
        password_label.pack(pady=5)
        password_entry = CTkEntry(self, textvariable=self.password_var, show="*")
        password_entry.pack(pady=5)

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

        back_to_login_button = CTkButton(self, text="Back to Login", command=self.page_controller.show_login_page)
        back_to_login_button.pack(pady=10)

    def register_user(self):
        # Get user registration information
        username = self.username_var.get()
        password = self.password_var.get()
        name = self.name_var.get()
        phone = self.phone_var.get()
        car_plate = self.car_var.get()
        email = self.email_var.get()

        # Validate and save user registration (you can save to a file or database)
        if username and password and name and phone and car_plate and email:
            user_model = UserModel(username, password, name, phone, car_plate, email)
            registration_successful = self.page_controller.user_controller.register_user(user_model)

            if registration_successful:
                messagebox.showinfo("Registration Successful", "User registered successfully!")
                self.page_controller.show_login_page()
            else:
                messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        else:
            messagebox.showerror("Registration Failed", "Please fill in all fields.")

class BookingPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Booking Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry fields for booking information
        self.duration_var = tk.StringVar()

        duration_label = CTkLabel(self, text="Parking Duration (hours):")
        duration_label.pack(pady=5)
        duration_entry = CTkEntry(self, textvariable=self.duration_var)
        duration_entry.pack(pady=5)

        book_button = CTkButton(self, text="Book Parking", command=self.book_parking)
        book_button.pack(pady=10)

        home_button = CTkButton(self, text="Home Page", command=self.page_controller.show_home_page)
        home_button.pack(pady=10)

        

    def book_parking(self):
        duration = self.duration_var.get()
        # Implement logic to process parking booking with the provided duration
        # You may want to save the booking information or perform other actions.

        # Validate if a valid duration is entered (you can add more validation as needed)
        if duration.isdigit() and int(duration) > 0:
            # Process the parking booking (this is just an example, you may need to customize this part)
            booking_info = {
                "user": "CurrentUser",  # You can replace this with the actual user information
                "duration": int(duration),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Save the booking information or perform other actions
            # For now, let's print the information
            print("Parking booked successfully!")
            print("Booking Information:", booking_info)

            # Show a messagebox with the booking details
            messagebox.showinfo("Booking Successful", f"Parking booked for {duration} hours!")

            # You can add more logic here, such as updating a database or UI elements

            # Navigate back to the home page
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Invalid Duration", "Please enter a valid positive number for parking duration.")

class ExtendParkingPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Extend Parking Time", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry field for extending duration
        self.extend_duration_var = tk.StringVar()
        extend_duration_label = CTkLabel(self, text="Extend Duration (hours):")
        extend_duration_label.pack(pady=5)
        extend_duration_entry = CTkEntry(self, textvariable=self.extend_duration_var)
        extend_duration_entry.pack(pady=5)

        extend_button = CTkButton(self, text="Extend Parking", command=self.extend_parking)
        extend_button.pack(pady=10)

        pay_button = CTkButton(self, text="Proceed to Payment", command=self.page_controller.show_payment_page)
        pay_button.pack(pady=10)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)


    def extend_parking(self):
        extend_duration = self.extend_duration_var.get()

        # Validate if a valid duration is entered (you can add more validation as needed)
        if extend_duration.isdigit() and int(extend_duration) > 0:
            # Process the parking extension (this is just an example, you may need to customize this part)
            extension_info = {
                "user": "CurrentUser",  # Replace with actual user information
                "extended_duration": int(extend_duration),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Save the extension information or perform other actions
            # For now, let's print the information
            print("Parking extended successfully!")
            print("Extension Information:", extension_info)

            # Show a messagebox with the extension details
            messagebox.showinfo("Extension Successful", f"Parking extended for {extend_duration} hours!")

            # You can add more logic here, such as updating a database or UI elements

            # Navigate back to the home page
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Invalid Duration", "Please enter a valid positive number for extension duration.")

class PaymentPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Payment Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry fields for payment information
        self.card_number_var = tk.StringVar()
        self.expiry_date_var = tk.StringVar()
        self.cvv_var = tk.StringVar()

        card_number_label = CTkLabel(self, text="Card Number:")
        card_number_label.pack(pady=5)
        card_number_entry = CTkEntry(self, textvariable=self.card_number_var)
        card_number_entry.pack(pady=5)

        expiry_date_label = CTkLabel(self, text="Expiry Date (MM/YY):")
        expiry_date_label.pack(pady=5)
        expiry_date_entry = CTkEntry(self, textvariable=self.expiry_date_var)
        expiry_date_entry.pack(pady=5)

        cvv_label = CTkLabel(self, text="CVV:")
        cvv_label.pack(pady=5)
        cvv_entry = CTkEntry(self, textvariable=self.cvv_var, show="*")
        cvv_entry.pack(pady=5)

        pay_button = CTkButton(self, text="Pay", command=self.process_payment)
        pay_button.pack(pady=10)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)

    def process_payment(self):
        # Get payment information
        card_number = self.card_number_var.get()
        expiry_date = self.expiry_date_var.get()
        cvv = self.cvv_var.get()

        # Validate payment information (you can add more validation as needed)
        if card_number and expiry_date and cvv:
            # Process the payment (this is just an example, you may need to customize this part)
            payment_info = {
                "card_number": card_number,
                "expiry_date": expiry_date,
                "cvv": cvv
            }

            # Save the payment information or perform other actions
            # For now, let's print the information
            print("Payment processed successfully!")
            print("Payment Information:", payment_info)

            # Show a messagebox with payment details
            messagebox.showinfo("Payment Successful", "Payment processed successfully!")

            # You can add more logic here, such as updating a database or UI elements

            # Navigate back to the home page
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Invalid Payment Information", "Please fill in all payment fields.")


class ProfitLossPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Profit/Loss Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # You might fetch revenue and expenses from a database or other sources
        revenue = 0  # Placeholder for revenue
        expenses = 0  # Placeholder for expenses

        # Display revenue and expenses
        revenue_label = CTkLabel(self, text=f"Total Revenue: ${revenue}")
        revenue_label.pack(pady=5)

        expenses_label = CTkLabel(self, text=f"Total Expenses: ${expenses}")
        expenses_label.pack(pady=5)

        # Calculate profit/loss
        profit_loss = revenue - expenses
        result_text = f"Profit: ${profit_loss}" if profit_loss >= 0 else f"Loss: ${abs(profit_loss)}"

        result_label = CTkLabel(self, text=result_text)
        result_label.pack(pady=20)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)


class ProfitLossPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Profit/Loss Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # You might fetch revenue and expenses from a database or other sources
        revenue = 0  # Placeholder for revenue
        expenses = 0  # Placeholder for expenses

        # Display revenue and expenses
        revenue_label = CTkLabel(self, text=f"Total Revenue: ${revenue}")
        revenue_label.pack(pady=5)

        expenses_label = CTkLabel(self, text=f"Total Expenses: ${expenses}")
        expenses_label.pack(pady=5)

        # Calculate profit/loss
        profit_loss = revenue - expenses
        result_text = f"Profit: ${profit_loss}" if profit_loss >= 0 else f"Loss: ${abs(profit_loss)}"

        result_label = CTkLabel(self, text=result_text)
        result_label.pack(pady=20)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)




if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Parking Management System")
    app.geometry("400x600")

    page_controller = PageController(app)

    app.mainloop()
