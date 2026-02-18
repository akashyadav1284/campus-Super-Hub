"""
Database connection for AIfusion / Campus Hub.
Uses MySQL. Set env vars DB_HOST, DB_USER, DB_PASSWORD, DB_NAME to override defaults.
"""
import os
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", ""),
        database=os.environ.get("DB_NAME", "campus_hub"),
    )
