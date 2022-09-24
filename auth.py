import bcrypt
import environment as env

def hashPassword(password):

    password  = password.encode("utf-8")

    # Génération d'un sel alétatoire et détermination du facteur coût
    saltDepart = bcrypt.gensalt(rounds=12)

    hashed = bcrypt.hashpw(password, saltDepart)
    return hashed

def login(login, password):
    if(login != env.login): return False
    
    password = password.encode("utf-8")
    if bcrypt.checkpw(password, env.password.encode("utf-8")): return True
    return False