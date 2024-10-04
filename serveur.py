import socket 
import hashlib as hasher
import datetime
import sqlite3 as lite



conn = lite.connect("data.db")

def add_user(username, password):
    cursor = conn.cursor()
    query = f"INSERT INTO users VALUES(?,?)"
    cursor.execute(query, (username, password))
    with open("registers.log", "a+") as registersFile:
        registersFile.write("Le compte {} a ete creer\n".format(username))
        client.send(bytes("Le compte {} a ete creer\n".format(username), "utf-8"))
    conn.commit()
    
    
    cursor.close()

def login_user(username, password):
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    if cursor.fetchone():
        client.send("Connecter sur le compte : {}".format(username).encode("utf-8"))
        
        with open("logins.log", "a+") as loginsFile:
            
            heure =  datetime.datetime.now().strftime("%Hh:%Mm:%Ss")
            
            loginsFile.write("Le compte {} a eter authentifier a {}\n".format(username, heure))
                
    else:
        with open("logins.log", "a+") as loginsFile:
            heure =  datetime.datetime.now().strftime("%Hh:%Mm:%Ss")   
            loginsFile.write("Le compte {} a ete refuser a {}\n".format(username, heure))
            client.send(f"Utilisateur inexistant ou mdp incorrecte sur le compte : {username}".encode("utf-8"))
        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5500))


while True:
    try:
        server.listen()
        client, addr = server.accept()

        with open('connexions.log', "a+") as connFile:

            connFile.write(f"Connexion depuis l'addresse : {addr[0]}:{addr[1]}\n")
        msgData = client.recv(1024).decode("utf-8")
        if msgData == "register":
            username = client.recv(1024).decode("utf-8")

            basic_password = client.recv(1024).decode("utf-8")

            new_password = hasher.md5(basic_password.encode("utf-8"))

            add_user(username, new_password.hexdigest())

        if msgData == "login":
            username = client.recv(1024).decode("utf-8")

            basic_password = client.recv(1024).decode("utf-8")

            new_password = hasher.md5(basic_password.encode("utf-8"))

            print(new_password.hexdigest())

            login_user(username, new_password.hexdigest())

    except KeyboardInterrupt:

        break

quit()

