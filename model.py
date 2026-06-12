import json

import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "students.json")

students = []

print("MODEL FILE LOADED")

def load_students():
    global students

    print("Loading students from file...")

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
        print("No file found, starting fresh")

def save_students():
    print("SAVING FILE TO:", FILE_NAME)

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student_data(student):
    students.append(student)
    save_students()

def delete_student_data(student):
    students.remove(student)
    save_students()
students = []


def add_student_data(student):
    students.append(student)


def get_students():
    return students


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def delete_student_data(student):
    students.remove(student)
