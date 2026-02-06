from db import get_connection

def add_course():
    name = input("Course name: ")
    faculty = input("Faculty ID: ")
    credits = input("Credits: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO courses (course_name, faculty_id, credits)
        VALUES (%s, %s, %s)
    """, (name, faculty, credits))

    conn.commit()
    print("Course added.")
    cursor.close()
    conn.close()


def view_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name FROM courses")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
