from db import get_connection

def add_assignment():
    course_id = input("Course ID: ")
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due date (YYYY-MM-DD HH:MM:SS): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO assignments
        (course_id, title, description, due_date)
        VALUES (%s, %s, %s, %s)
    """, (course_id, title, description, due_date))

    conn.commit()
    print("Assignment added.")
    cursor.close()
    conn.close()


def view_assignments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT assignment_id, title, due_date
        FROM assignments
    """)

    print("\n--- Assignments ---")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
