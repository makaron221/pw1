import sqlite3
conn = sqlite3.connect("database.db")
conn.execute("CREATE TABLE posts(id, content)")
conn.commit()
conn.close()