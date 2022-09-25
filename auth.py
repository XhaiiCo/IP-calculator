import bcrypt
import sqlite3 

def hashPassword(password):

    password  = password.encode("utf-8")

    # Génération d'un sel alétatoire et détermination du facteur coût
    saltDepart = bcrypt.gensalt(rounds=12)

    hashed = bcrypt.hashpw(password, saltDepart)
    return hashed

def login(login, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    row = c.execute("SELECT password from users where users.login = ?", [login]).fetchone()
    conn.close()
    if row == None: return False
    
    hashedPassword = row[0].encode("utf-8")
    if bcrypt.checkpw(password.encode("utf-8"), hashedPassword): return True
    return False