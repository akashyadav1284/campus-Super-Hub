from db import get_connection

def add_place():
    name = input("Place name: ")
    category = input("Category: ")
    address = input("Address: ")
    rating = input("Rating (0–5): ")
    description = input("Description: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO places (name, category, address, rating, description)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, category, address, rating, description))

    conn.commit()
    print("Place added.")
    cursor.close()
    conn.close()


def view_places():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT place_id, name, category, rating FROM places")

    print("\n--- Places ---")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
