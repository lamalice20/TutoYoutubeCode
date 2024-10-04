import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5500))


def login():
    client.send(bytes("login", "utf-8"))
    
    username = input('Entrer votre nom d\'utilisateur : ')
    password = input('Entrer votre mot de passe : ')

    client.sendall(bytes(username, "utf-8"))
    client.sendall(bytes(password, "utf-8"))

    response = client.recv(1024).decode("utf-8")

    print(response)

def register():
    client.send(bytes("register", "utf-8"))
    username = input('Entrer votre nom d\'utilisateur : ')
    password = input('Entrer votre mot de passe : ')

    client.sendall(bytes(username, "utf-8"))
    client.sendall(bytes(password, "utf-8"))

    response = client.recv(1024).decode("utf-8")

    print(response)


choice = input('1. Login\n2. Register\n3. Quitter\n')

if choice == "1":
    login()

if choice == "2":
    register()

if choice == "3":
    quit()

