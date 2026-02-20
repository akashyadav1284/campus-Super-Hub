"""
Initialize the campus_hub database and tables using SQLite.
Run once: python init_db.py
"""
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "campus_hub.db")

def main():
    print("Connecting to SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    print("Database ready.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject VARCHAR(500) NOT NULL,
            summary TEXT NOT NULL,
            category VARCHAR(50) NOT NULL,
            priority VARCHAR(50) DEFAULT 'Normal',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("Table email_summaries ready.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mess_menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_of_week VARCHAR(20) NOT NULL,
            meal_type VARCHAR(20) NOT NULL,
            items TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("Table mess_menu ready.")

    conn.commit()
    cursor.close()
    conn.close()
    print("Done. You can start the API with: uvicorn main:app --reload")

if __name__ == "__main__":
    main()
