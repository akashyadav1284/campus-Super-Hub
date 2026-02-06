from db import get_connection

def add_item():
    seller = input("Seller ID: ")
    title = input("Title: ")
    price = input("Price: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO marketplace_items (seller_id, title, price)
        VALUES (%s, %s, %s)
    """, (seller, title, price))

    conn.commit()
    print("Item added.")
    cursor.close()
    conn.close()


def view_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT item_id, title, price FROM marketplace_items")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
