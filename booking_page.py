import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
import datetime

# from controllers.page_controller import PageController
# from controllers.user_controller import UserController
from pages.base_page import BasePage
# from pages.login_page import LoginPage
# from pages.registration_page import RegisterPage
# from pages.home_page import HomePage
# from pages.booking_page import BookingPage
# from extend_packing_page import ExtendParkingPage
# from payment_page import PaymentPage
# from profit_loss_page import ProfitLossPage

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
