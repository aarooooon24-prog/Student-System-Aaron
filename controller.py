import model
import view


# ---------- VALIDATION ----------

def get_valid_id():
    while True:
        i = view.get_input("Enter Student ID: ")
        if i.isdigit():
            return i
        view.show("Invalid ID!")


def get_valid_name():
    while True:
        n = view.get_input("Enter Name: ")
        if n.replace(" ", "").isalpha():
            return n
        view.show("Invalid Name!")


def get_valid_age():
    while True:
        a = view.get_input("Enter Age: ")
        if a.isdigit() and 0 < int(a) < 120:
            return int(a)
        view.show("Invalid Age!")


# ---------- OPERATIONS ----------

def add_student():
    view.show("\n--- Add Student ---")

    student = {
        "id": get_valid_id(),
        "name": get_valid_name(),
        "age": get_valid_age()
    }

    if model.find_student(student["id"]):
        view.show("ID already exists!")
        return

    model.add_student_data(student)
    view.show("Student added!")


def view_students():
    view.display_students(model.get_students())


def search_student():
    view.show("\n--- Search ---")

    student_id = view.get_input("Enter ID: ")
    student = model.find_student(student_id)

    if student:
        view.display_student(student)
    else:
        view.show("Not found")


def update_student():
    view.show("\n--- Update ---")

    student_id = view.get_input("Enter ID: ")
    student = model.find_student(student_id)

    if student:
        name = view.get_input(f"New Name ({student['name']}): ")
        age = view.get_input(f"New Age ({student['age']}): ")

        if name:
            student["name"] = name
        if age.isdigit():
            student["age"] = int(age)

<<<<<<< HEAD
        model.save_students()   

        view.show("Updated!")
    else:
        view.show("Not found")
   
=======
        view.show("Updated!")
    else:
        view.show("Not found")

>>>>>>> 173670d2fdef9fee75fdd776c86f409755b08e78

def delete_student():
    view.show("\n--- Delete ---")

    student_id = view.get_input("Enter ID: ")
    student = model.find_student(student_id)

    if student:
        model.delete_student_data(student)
        view.show("Deleted!")
    else:
        view.show("Not found")


# ---------- MAIN LOOP ----------

def run():
    while True:
        view.display_menu()
        choice = view.get_input("Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            view.show("Goodbye!")
            break
        else:
            view.show("Invalid choice")