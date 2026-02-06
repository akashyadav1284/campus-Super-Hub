from db import get_connection

def send_message():
    sender = input("Sender ID: ")
    receiver = input("Receiver ID: ")
    message = input("Message: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages (sender_id, receiver_id, message)
        VALUES (%s, %s, %s)
    """, (sender, receiver, message))

    conn.commit()
    print("Message sent.")
    cursor.close()
    conn.close()
