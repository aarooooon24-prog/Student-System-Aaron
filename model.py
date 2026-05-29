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