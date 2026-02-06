from db import get_connection

def add_user():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Role (student/faculty/admin): ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO users (full_name, email, password_hash, role)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, password, role))
    conn.commit()

    print("User added.")
    cursor.close()
    conn.close()


def view_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, full_name, role FROM users")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
