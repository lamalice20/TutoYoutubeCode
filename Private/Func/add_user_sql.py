import sqlite3 as lite

def add_user(username, password, client, conn):
    cursor = conn.cursor()
    query = f"INSERT INTO users VALUES(?,?)"
    cursor.execute(query, (username, password))
    with open("Private/Logs/registers.log", "a+") as registersFile:
        registersFile.write("Le compte {} a ete creer\n".format(username))
        client.send(bytes("Le compte {} a ete creer\n".format(username), "utf-8"))
    conn.commit()
        
    cursor.close()