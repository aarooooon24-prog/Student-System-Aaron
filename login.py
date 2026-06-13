import tkinter as tk
from tkinter import messagebox
import gui


# ---------- LOGIN WINDOW ----------
def login_screen():
    root = tk.Tk()
    root.title("Student Information System")
    root.geometry("400x350")
    root.configure(bg="#1e1e1e")

    # ---------- TITLE ----------
    tk.Label(
        root,
        text="STUDENT\nINFORMATION\nSYSTEM",
        font=("Arial", 20, "bold"),
        bg="#1e1e1e",
        fg="white"
    ).pack(pady=20)

    # ---------- USERNAME ----------
    tk.Label(
        root,
        text="Username",
        bg="#1e1e1e",
        fg="white"
    ).pack(pady=5)

    username_entry = tk.Entry(root, width=25)
    username_entry.pack()

    # ---------- PASSWORD ----------
    tk.Label(
        root,
        text="Password",
        bg="#1e1e1e",
        fg="white"
    ).pack(pady=5)

    password_entry = tk.Entry(root, show="*", width=25)
    password_entry.pack()

    # ---------- LOGIN FUNCTION ----------
    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "aaron" and password == "dit11":
            root.destroy()
            gui.start_app()
        else:
            messagebox.showerror("Error", "Invalid login")

    # ---------- LOGIN BUTTON ----------
    tk.Button(
        root,
        text="Login",
        command=check_login,
        width=15
    ).pack(pady=20)

    root.mainloop()