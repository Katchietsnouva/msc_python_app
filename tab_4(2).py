import tkinter as tk
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from tkinter import messagebox

class BasePage(tk.Frame):
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



    def getvals_login(self):
        user_name = self.username_var.get()
        password = self.password_var.get()
        user_authenticated = self.authenticate_user(user_name, password)

        if user_authenticated:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def authenticate_user(self, username, password):
        return username == "a" and password == "b"

class HomePage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the home page
        greeting_label = CTkLabel(self, text="Welcome to the Home Page!", font=("ar", 15, "bold"))
        greeting_label.pack(pady=20)

        logout_button = CTkButton(self, text="Logout", command=self.page_controller.show_login_page)
        logout_button.pack(pady=10)

        Car_register_button = CTkButton(self, text="Register", command=self.page_controller.show_registration_page)
        Car_register_button.pack(pady=10)

class PageController:
    def __init__(self, root):
        self.root = root
        self.login_page = LoginPage(root, self)
        self.home_page = HomePage(root, self)
        self.registration_page = RegistrationPage(root, self)
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

        homepage_button = CTkButton(self, text="Home Page", command=self.page_controller.show_home_page)
        homepage_button.pack(pady=10)

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

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Your App Title")
    app.geometry("600x400")

    page_controller = PageController(app)

    app.mainloop()
