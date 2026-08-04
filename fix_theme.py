import sqlite3

try:
    conn = sqlite3.connect('CTFd/CTFd/ctfd.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE config SET value='pafms-theme' WHERE key='ctf_theme'")
    conn.commit()
    conn.close()
    print("Theme updated successfully")
except Exception as e:
    print(f"Error: {e}")
