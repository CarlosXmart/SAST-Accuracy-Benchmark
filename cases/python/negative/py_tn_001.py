import sqlite3
def find(conn: sqlite3.Connection, user: str):
    # XG-BENCH:PY-TN-001 START
    return conn.execute("SELECT * FROM users WHERE name=?", (user,)).fetchall()
    # XG-BENCH:PY-TN-001 END
