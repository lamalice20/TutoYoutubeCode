import socket 
import hashlib as hasher
import datetime
import sqlite3 as lite
from Private.Func.add_user_sql import add_user
from Private.Func.login_user_sql import login_user

conn = lite.connect("Private/Data/data.db")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5500))


while True:
    try:
        server.listen(5)
        client, addr = server.accept()

        with open('Private/Logs/connexions.log', "a+") as connFile:

            connFile.write(f"Connexion depuis l'addresse : {addr[0]}:{addr[1]}\n")
        msgData = client.recv(1024).decode("utf-8")
        if msgData == "register":
            username = client.recv(1024).decode("utf-8")

            basic_password = client.recv(1024).decode("utf-8")

            new_password = hasher.md5(basic_password.encode("utf-8"))

            add_user(username, new_password.hexdigest(), client, conn)

        if msgData == "login":
            username = client.recv(1024).decode("utf-8")

            basic_password = client.recv(1024).decode("utf-8")

            new_password = hasher.md5(basic_password.encode("utf-8"))

            print(new_password.hexdigest())

            login_user(username, new_password.hexdigest(), client, conn)

    except KeyboardInterrupt:

        break

quit()

