"""
Initialize the campus_hub database and tables.
Run once: python init_db.py
Requires MySQL running with user/password from db.py (or env vars).
"""
import os
import mysql.connector

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "campus_hub")


def main():
    print("Connecting to MySQL (without database)...")
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    print(f"Database '{DB_NAME}' ready.")
    cursor.execute(f"USE `{DB_NAME}`")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_summaries (
            id INT AUTO_INCREMENT PRIMARY KEY,
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
            id INT AUTO_INCREMENT PRIMARY KEY,
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
