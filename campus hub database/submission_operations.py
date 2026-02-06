from db import get_connection

def submit_assignment():
    assignment_id = input("Assignment ID: ")
    student_id = input("Student ID: ")
    file_url = input("File URL: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO submissions
        (assignment_id, student_id, file_url)
        VALUES (%s, %s, %s)
    """, (assignment_id, student_id, file_url))

    conn.commit()
    print("Submission successful.")
    cursor.close()
    conn.close()


def view_submissions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT submission_id, assignment_id, student_id, grade
        FROM submissions
    """)

    print("\n--- Submissions ---")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
