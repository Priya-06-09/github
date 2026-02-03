import sqlite3

conn = sqlite3.connect("health_app.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS patient_data (
    username TEXT,
    next_checkup TEXT,
    condition TEXT
)
""")

conn.commit()

def add_user(username, password):
    c.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()

def validate_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def save_patient_data(username, date, condition):
    c.execute("INSERT INTO patient_data VALUES (?,?,?)", (username, date, condition))
    conn.commit()

def get_patient_data(username):
    c.execute("SELECT * FROM patient_data WHERE username=?", (username,))
    return c.fetchall()
