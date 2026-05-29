def display_menu():
    print("\n===== STUDENT INFORMATION SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def show(message):
    print(message)


def display_students(students):
    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    for i, s in enumerate(students, 1):
        print(f"{i}. ID: {s['id']}, Name: {s['name']}, Age: {s['age']}")


def display_student(s):
    print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}")


def get_input(text):
    return input(text)