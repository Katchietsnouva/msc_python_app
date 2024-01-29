import sqlite3
import os

os.makedirs("sqlite_db", exist_ok=True)

# Connect to the database (create it if it doesn't exist)
db_connection = sqlite3.connect("sqlite_db\\parking_app.db")
db_cursor = db_connection.cursor()

# Create the users table if it doesn't exist
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')
db_connection.commit()

# Insert sample user data
user_data = [
    ("admin", "admin_password"),
    ("john_doe", "password123"),
    ("alice_smith", "qwerty"),
]

for username, password in user_data:
    db_cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# Commit the changes to the database
db_connection.commit()

# Close the database connection
db_connection.close()
os.rename("sqlite_db/parking_app.db", "sqlite_db/parking_app.sqlite")
