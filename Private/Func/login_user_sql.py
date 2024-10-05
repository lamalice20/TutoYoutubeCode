import datetime

def login_user(username, password, client, conn):
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    if cursor.fetchone():
        client.send("Connecter sur le compte : {}".format(username).encode("utf-8"))
        
        with open("Private/Logs/logins.log", "a+") as loginsFile:
            
            heure =  datetime.datetime.now().strftime("%Hh:%Mm:%Ss")
            
            loginsFile.write("Le compte {} a eter authentifier a {}\n".format(username, heure))
                
    else:
        with open("Private/Logs/logins.log", "a+") as loginsFile:
            heure =  datetime.datetime.now().strftime("%Hh:%Mm:%Ss")   
            loginsFile.write("Le compte {} a ete refuser a {}\n".format(username, heure))
            client.send(f"Utilisateur inexistant ou mdp incorrecte sur le compte : {username}".encode("utf-8"))