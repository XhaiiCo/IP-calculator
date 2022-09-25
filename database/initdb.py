import sqlite3

from database import environment as env


def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS users")
    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
            login varchar(256) primary key,
            password varchar(256)
        )
    ''')

    c.execute("INSERT INTO users VALUES (?,?)", (env.login, env.password))
    conn.commit()
    conn.close()