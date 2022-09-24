import auth 

if auth.login(input("login: "), input("password: ")): 
    print("loged")
else:
    print("Erreur")