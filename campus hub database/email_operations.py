from db import get_connection

def add_email_summary():
    subject = input("Subject: ")
    summary = input("Summary: ")
    category = input("Category: ")
    priority = input("Priority: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO email_summaries (subject, summary, category, priority)
        VALUES (%s, %s, %s, %s)
    """, (subject, summary, category, priority))

    conn.commit()
    print("Email summary added.")
    cursor.close()
    conn.close()


def view_email_summaries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT subject, summary FROM email_summaries")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
