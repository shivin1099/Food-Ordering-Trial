import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Replace this list with a database in a real-world scenario
users_database = [
    User(username="user1", password="pass1"),
    User(username="user2", password="pass2"),
]

class AuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack()

        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if the provided username and password match any user in the database
        authenticated_user = self.authenticate(username, password)

        if authenticated_user:
            messagebox.showinfo("Login Successful", f"Welcome, {authenticated_user.username}!")
            self.root.destroy()  # Close the authentication window upon successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def authenticate(self, username, password):
        for user in users_database:
            if user.username == username and user.password == password:
                return user
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthenticationApp(root)
    root.mainloop()

