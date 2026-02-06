from db import get_connection

def add_menu():
    day = input("Day: ")
    meal = input("Meal (breakfast/lunch/dinner): ")
    items = input("Items: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO mess_menu (day_of_week, meal_type, items)
        VALUES (%s, %s, %s)
    """, (day, meal, items))

    conn.commit()
    print("Menu added.")
    cursor.close()
    conn.close()


def view_menu():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT day_of_week, meal_type, items FROM mess_menu")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
