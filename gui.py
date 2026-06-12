import tkinter as tk
from tkinter import ttk, messagebox
import model


# ---------- COLORS ----------
BG = "#1e1e1e"
FG = "#ffffff"
SIDEBAR = "#2b2b2b"
BTN = "#3a3a3a"
ENTRY = "#2b2b2b"


# ---------- APP ----------
def start_app():
    global root, id_entry, name_entry, age_entry, table, content_frame

    root = tk.Tk()
    root.title("Student Dashboard System")
    root.geometry("900x500")
    root.configure(bg=BG)


    # ======================================================
    # SIDEBAR
    # ======================================================
    sidebar = tk.Frame(root, bg=SIDEBAR, width=200)
    sidebar.pack(side="left", fill="y")


    tk.Label(sidebar, text="MENU", bg=SIDEBAR, fg=FG, font=("Arial", 14, "bold")).pack(pady=20)

    tk.Button(sidebar, text="Add Student", bg=BTN, fg=FG, command=lambda: show_frame("add")).pack(fill="x", pady=5)
    tk.Button(sidebar, text="View Students", bg=BTN, fg=FG, command=lambda: show_frame("view")).pack(fill="x", pady=5)
    tk.Button(sidebar, text="Search", bg=BTN, fg=FG, command=lambda: show_frame("search")).pack(fill="x", pady=5)


    # ======================================================
    # MAIN CONTENT AREA
    # ======================================================
    content_frame = tk.Frame(root, bg=BG)
    content_frame.pack(side="right", expand=True, fill="both")


    # ======================================================
    # FRAMES
    # ======================================================
    add_frame = tk.Frame(content_frame, bg=BG)
    view_frame = tk.Frame(content_frame, bg=BG)
    search_frame = tk.Frame(content_frame, bg=BG)


    # ================= ADD STUDENT =================
    tk.Label(add_frame, text="ID", bg=BG, fg=FG).grid(row=0, column=0)
    id_entry = tk.Entry(add_frame, bg=ENTRY, fg=FG, insertbackground="white")
    id_entry.grid(row=0, column=1)

    tk.Label(add_frame, text="Name", bg=BG, fg=FG).grid(row=1, column=0)
    name_entry = tk.Entry(add_frame, bg=ENTRY, fg=FG, insertbackground="white")
    name_entry.grid(row=1, column=1)

    tk.Label(add_frame, text="Age", bg=BG, fg=FG).grid(row=2, column=0)
    age_entry = tk.Entry(add_frame, bg=ENTRY, fg=FG, insertbackground="white")
    age_entry.grid(row=2, column=1)


    def add_student():
        student = {
            "id": id_entry.get(),
            "name": name_entry.get(),
            "age": int(age_entry.get())
        }

        model.add_student_data(student)
        refresh_table()
        messagebox.showinfo("Success", "Student Added")


    tk.Button(add_frame, text="Add Student", bg=BTN, fg=FG, command=add_student).grid(row=3, column=1, pady=10)


    # ================= VIEW STUDENTS =================
    table = ttk.Treeview(view_frame, columns=("ID", "Name", "Age"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Name", text="Name")
    table.heading("Age", text="Age")
    table.pack(expand=True, fill="both")


    def refresh_table():
        for row in table.get_children():
            table.delete(row)

        for s in model.get_students():
            table.insert("", "end", values=(s["id"], s["name"], s["age"]))


    # ================= SEARCH =================
    tk.Label(search_frame, text="Search Name or ID", bg=BG, fg=FG).pack()

    search_entry = tk.Entry(search_frame, bg=ENTRY, fg=FG, insertbackground="white")
    search_entry.pack()

    result = tk.Label(search_frame, text="", bg=BG, fg=FG)
    result.pack()

    def search():
        query = search_entry.get().lower()

        matches = []
        for s in model.get_students():
            if query in s["id"].lower() or query in s["name"].lower():
                matches.append(f"{s['id']} | {s['name']} | {s['age']}")

        result.config(text="\n".join(matches) if matches else "No results")


    tk.Button(search_frame, text="Search", bg=BTN, fg=FG, command=search).pack()


    # ======================================================
    # FRAME SWITCHER
    # ======================================================
    def show_frame(name):
        for f in (add_frame, view_frame, search_frame):
            f.pack_forget()

        if name == "add":
            add_frame.pack(fill="both", expand=True)
        elif name == "view":
            view_frame.pack(fill="both", expand=True)
            refresh_table()
        elif name == "search":
            search_frame.pack(fill="both", expand=True)


    # default view
    show_frame("view")

    root.mainloop()