from db import get_connection

def add_timetable_entry():
    user_id = input("User ID: ")
    course_id = input("Course ID: ")
    day = input("Day of week: ")
    start = input("Start time (HH:MM:SS): ")
    end = input("End time (HH:MM:SS): ")
    room = input("Room: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO timetable
        (user_id, course_id, day_of_week, start_time, end_time, room)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, course_id, day, start, end, room))

    conn.commit()
    print("Timetable entry added.")
    cursor.close()
    conn.close()


def view_timetable():
    user_id = input("User ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.day_of_week, c.course_name, t.start_time, t.end_time, t.room
        FROM timetable t
        JOIN courses c ON t.course_id = c.course_id
        WHERE t.user_id = %s
    """, (user_id,))

    print("\n--- Timetable ---")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
