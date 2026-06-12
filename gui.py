import tkinter as tk
from tkinter import messagebox
import model


# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")


# ---------- INPUT FIELDS ----------
tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()


# ---------- FUNCTIONS ----------

def add_student():
    student = {
        "id": id_entry.get(),
        "name": name_entry.get(),
        "age": int(age_entry.get())
    }

    if model.find_student(student["id"]):
        messagebox.showerror("Error", "ID already exists!")
        return

    model.add_student_data(student)
    messagebox.showinfo("Success", "Student Added!")


def view_students():
    students = model.get_students()

    text = ""
    for s in students:
        text += f"{s['id']} | {s['name']} | {s['age']}\n"

    messagebox.showinfo("Students List", text if text else "No students found")


def search_student():
    student = model.find_student(id_entry.get())

    if student:
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

        name_entry.insert(0, student["name"])
        age_entry.insert(0, student["age"])
    else:
        messagebox.showerror("Not Found", "Student not found")


def update_student():
    student = model.find_student(id_entry.get())

    if student:
        student["name"] = name_entry.get()
        student["age"] = int(age_entry.get())

        model.update_student_data(student)

        messagebox.showinfo("Updated", "Student updated!")
    else:
        messagebox.showerror("Error", "Student not found")


def delete_student():
    student_id = id_entry.get()

    if model.find_student(student_id):
        model.delete_student_data(student_id)
        messagebox.showinfo("Deleted", "Student deleted!")
    else:
        messagebox.showerror("Error", "Student not found")


# ---------- BUTTONS ----------

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Search Student", command=search_student).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)


# ---------- START ----------
root.mainloop()