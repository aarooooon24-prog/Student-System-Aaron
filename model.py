import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "students.db")


# ---------- CONNECT ----------
def connect():
    return sqlite3.connect(DB_NAME)


# ---------- CREATE TABLE ----------
def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------- ADD ----------
def add_student_data(student):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (id, name, age)
        VALUES (?, ?, ?)
    """, (student["id"], student["name"], student["age"]))

    conn.commit()
    conn.close()


# ---------- GET ALL ----------
def get_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"id": r[0], "name": r[1], "age": r[2]}
        for r in rows
    ]


# ---------- FIND ----------
def find_student(student_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {"id": row[0], "name": row[1], "age": row[2]}
    return None


# ---------- UPDATE ----------
def update_student_data(student):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?
        WHERE id = ?
    """, (student["name"], student["age"], student["id"]))

    conn.commit()
    conn.close()


# ---------- DELETE ----------
def delete_student_data(student_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()