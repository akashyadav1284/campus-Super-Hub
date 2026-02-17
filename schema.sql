-- AIfusion / Campus Hub - MySQL schema
-- Run this after creating the database (see init_db.py).

CREATE DATABASE IF NOT EXISTS campus_hub;
USE campus_hub;

CREATE TABLE IF NOT EXISTS email_summaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(500) NOT NULL,
    summary TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,
    priority VARCHAR(50) DEFAULT 'Normal',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: mess menu table for future dashboard integration
CREATE TABLE IF NOT EXISTS mess_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    day_of_week VARCHAR(20) NOT NULL,
    meal_type VARCHAR(20) NOT NULL,
    items TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
