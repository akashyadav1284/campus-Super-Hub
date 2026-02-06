from db import get_connection

def send_notification():
    user = input("User ID: ")
    message = input("Message: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO notifications (user_id, message)
        VALUES (%s, %s)
    """, (user, message))

    conn.commit()
    print("Notification sent.")
    cursor.close()
    conn.close()
