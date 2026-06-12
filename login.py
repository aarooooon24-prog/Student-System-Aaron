import tkinter as tk
from tkinter import messagebox
import gui


# ---------- LOGIN WINDOW ----------
def login_screen():
    root = tk.Tk()
    root.title("Login System")
    root.geometry("300x200")
    root.configure(bg="#1e1e1e")


    tk.Label(root, text="Username", bg="#1e1e1e", fg="white").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack()


    tk.Label(root, text="Password", bg="#1e1e1e", fg="white").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()


    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "aaron" and password == "dit11":
            root.destroy()      # close login window
            gui.start_app()     # open dashboard
        else:
            messagebox.showerror("Error", "Invalid login")


    tk.Button(root, text="Login", command=check_login).pack(pady=20)

    root.mainloop()