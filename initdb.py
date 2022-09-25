import sqlite3
import environment as env

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