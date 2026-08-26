import sqlite3
def find(conn: sqlite3.Connection, user: str):
    # XG-BENCH:PY-TP-001 START
    sql = "SELECT * FROM users WHERE name='" + user + "'"
    return conn.execute(sql).fetchall()
    # XG-BENCH:PY-TP-001 END
