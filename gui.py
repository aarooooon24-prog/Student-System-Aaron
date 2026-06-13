import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import model

# ======================================================
# PROFESSIONAL COLOR THEME
# ======================================================
BG = "#F4F6F9"
FG = "#2C3E50"
SIDEBAR = "#2C3E50"
BTN = "#3498DB"
BTN_DANGER = "#E74C3C"
ENTRY = "#FFFFFF"
ACCENT = "#1ABC9C"


def start_app():
    global root, id_entry, name_entry, age_entry, table

    root = tk.Tk()
    root.title("Student Information System")
    root.geometry("1200x700")
    root.configure(bg=BG)

    # ======================================================
    # SIDEBAR
    # ======================================================
    sidebar = tk.Frame(root, bg=SIDEBAR, width=220)
    sidebar.pack(side="left", fill="y")

    tk.Label(
        sidebar,
        text="SIS",
        bg=SIDEBAR,
        fg=ACCENT,
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(30, 5))

    tk.Label(
        sidebar,
        text="Student Information System",
        bg=SIDEBAR,
        fg="white",
        font=("Segoe UI", 9)
    ).pack(pady=(0, 30))

    # ======================================================
    # MAIN CONTENT
    # ======================================================
    content_frame = tk.Frame(root, bg=BG)
    content_frame.pack(side="right", expand=True, fill="both")

    # TITLE
    title_frame = tk.Frame(content_frame, bg=BG)
    title_frame.pack(fill="x", pady=15)

    tk.Label(
        title_frame,
        text="STUDENT INFORMATION SYSTEM",
        font=("Segoe UI", 24, "bold"),
        bg=BG,
        fg=FG
    ).pack()

    tk.Label(
        title_frame,
        text="Student Management Dashboard",
        font=("Segoe UI", 11),
        bg=BG,
        fg="#7F8C8D"
    ).pack()

    # PAGES
    page_container = tk.Frame(content_frame, bg=BG)
    page_container.pack(fill="both", expand=True)

    add_frame = tk.Frame(page_container, bg=BG)
    view_frame = tk.Frame(page_container, bg=BG)
    search_frame = tk.Frame(page_container, bg=BG)

    # ======================================================
    # ADD STUDENT
    # ======================================================
    tk.Label(add_frame, text="ID", bg=BG, fg=FG, font=("Segoe UI", 10)).grid(row=0, column=0, pady=5)
    id_entry = tk.Entry(add_frame, bg=ENTRY, font=("Segoe UI", 10), width=30)
    id_entry.grid(row=0, column=1)

    tk.Label(add_frame, text="Name", bg=BG, fg=FG, font=("Segoe UI", 10)).grid(row=1, column=0, pady=5)
    name_entry = tk.Entry(add_frame, bg=ENTRY, font=("Segoe UI", 10), width=30)
    name_entry.grid(row=1, column=1)

    tk.Label(add_frame, text="Age", bg=BG, fg=FG, font=("Segoe UI", 10)).grid(row=2, column=0, pady=5)
    age_entry = tk.Entry(add_frame, bg=ENTRY, font=("Segoe UI", 10), width=30)
    age_entry.grid(row=2, column=1)

    def clear():
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

    def add_student():
        try:
            student = {
                "id": id_entry.get(),
                "name": name_entry.get(),
                "age": int(age_entry.get())
            }

            if model.find_student(student["id"]):
                messagebox.showerror("Error", "Student already exists")
                return

            model.add_student_data(student)
            refresh()
            clear()
            messagebox.showinfo("Success", "Student Added")

        except:
            messagebox.showerror("Error", "Invalid input")

    tk.Button(
        add_frame,
        text="➕ Add Student",
        bg=BTN,
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        command=add_student
    ).grid(row=3, column=1, pady=10)

    # ======================================================
    # VIEW TABLE
    # ======================================================
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Treeview",
        background="white",
        foreground=FG,
        rowheight=30,
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        background=BTN,
        foreground="white",
        font=("Segoe UI", 10, "bold")
    )

    table = ttk.Treeview(view_frame, columns=("ID", "Name", "Age"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Name", text="Name")
    table.heading("Age", text="Age")
    table.pack(expand=True, fill="both")

    def refresh():
        for i in table.get_children():
            table.delete(i)

        for s in model.get_students():
            table.insert("", "end", values=(s["id"], s["name"], s["age"]))

    # ======================================================
    # UPDATE + DELETE
    # ======================================================
    def update_student():
        selected = table.focus()
        if not selected:
            messagebox.showerror("Error", "Select a student")
            return

        data = table.item(selected, "values")

        new_name = simpledialog.askstring("Update", "New name:", initialvalue=data[1])
        new_age = simpledialog.askstring("Update", "New age:", initialvalue=data[2])

        if new_name and new_age:
            model.update_student_data({
                "id": data[0],
                "name": new_name,
                "age": int(new_age)
            })

            refresh()
            messagebox.showinfo("Updated", "Student updated")

    def delete_student():
        selected = table.focus()
        if not selected:
            messagebox.showerror("Error", "Select a student")
            return

        data = table.item(selected, "values")

        if messagebox.askyesno("Delete", "Are you sure?"):
            model.delete_student_data(data[0])
            refresh()

    tk.Button(view_frame, text="✏ Update", bg=BTN, fg="white",
              font=("Segoe UI", 10, "bold"),
              command=update_student).pack(side="left", padx=10, pady=10)

    tk.Button(view_frame, text="🗑 Delete", bg=BTN_DANGER, fg="white",
              font=("Segoe UI", 10, "bold"),
              command=delete_student).pack(side="left", pady=10)

    # ======================================================
    # SEARCH
    # ======================================================
    search_entry = tk.Entry(search_frame, bg=ENTRY, font=("Segoe UI", 10), width=30)
    search_entry.pack(pady=10)

    result = tk.Label(search_frame, text="", bg=BG, fg=FG)
    result.pack()

    def search():
        q = search_entry.get().lower()
        out = []

        for s in model.get_students():
            if q in s["id"].lower() or q in s["name"].lower():
                out.append(f"{s['id']} | {s['name']} | {s['age']}")

        result.config(text="\n".join(out) if out else "No results")

    tk.Button(search_frame, text="Search", bg=BTN, fg="white",
              command=search).pack()

    # ======================================================
    # NAVIGATION
    # ======================================================
    def show(frame):
        for f in (add_frame, view_frame, search_frame):
            f.pack_forget()

        frame.pack(fill="both", expand=True)
        if frame == view_frame:
            refresh()

    tk.Button(sidebar, text="➕ Add Student", bg=BTN, fg="white",
              command=lambda: show(add_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="📋 View Students", bg=BTN, fg="white",
              command=lambda: show(view_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="🔍 Search", bg=BTN, fg="white",
              command=lambda: show(search_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="🚪 Exit", bg=BTN_DANGER, fg="white",
              command=root.destroy).pack(fill="x", pady=20)

    show(view_frame)
    root.mainloop()