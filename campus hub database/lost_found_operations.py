from db import get_connection

def report_item():
    user = input("User ID: ")
    name = input("Item name: ")
    location = input("Location: ")
    status = input("Status (lost/found): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO lost_found (user_id, item_name, location, status)
        VALUES (%s, %s, %s, %s)
    """, (user, name, location, status))

    conn.commit()
    print("Reported.")
    cursor.close()
    conn.close()
