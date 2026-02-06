from db import get_connection

def add_review():
    place_id = input("Place ID: ")
    user_id = input("User ID: ")
    rating = input("Rating (1–5): ")
    comment = input("Comment: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO place_reviews (place_id, user_id, rating, comment)
        VALUES (%s, %s, %s, %s)
    """, (place_id, user_id, rating, comment))

    conn.commit()
    print("Review added.")
    cursor.close()
    conn.close()


def view_reviews():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT review_id, place_id, user_id, rating, comment
        FROM place_reviews
    """)

    print("\n--- Reviews ---")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
