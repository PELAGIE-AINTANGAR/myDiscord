import socket
import threading
import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="discord"
)
def join_channel(id_utilisateur, channel):
    # Vérifie si l'utilisateur est déjà dans le canal de discussion
        if id_utilisateur in channel.users:
        # Ajoute le canal de discussion à la liste des canaux de l'utilisateur
            sql="INSERT INTO users (channels) VALUES (%s)"
            values=(channel.name)
            db.execute(sql, values)
            db.commit()
            db.close()
        # Envoie un message au serveur pour informer que l'utilisateur a rejoint le canal de discussion
            # self.send_message(f"{self.username} a rejoint le canal de discussion {channel}", channel)
    # cursor = db.cursor()
    # sql = "INSERT INTO channels (name, description) VALUES (%s, %s)"
    # values = (name, description)
    # cursor.execute(sql, values)
    # db.commit()
    # print("channel created")
    # db.close()
    # leave_channel permet à un utilisateur de quitter un canal de discussion spécifique
def leave_channel(self, channel):
    # Vérifie si l'utilisateur est déjà dans le canal de discussion
    if channel in self.channels:
        # Supprime le canal de discussion de la liste des canaux de l'utilisateur
        self.channels.remove(channel)
        # Envoie un message au serveur pour informer que l'utilisateur a quitté le canal de discussion
        self.send_message(f"{self.username} a quitté le canal de discussion {channel}", channel)
    

entre_surname = input("Enter your surname: ")

# Client 1
clientIP = socket.gethostbyname(socket.gethostname())
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((clientIP, 12345))

# Client 2
clientIP2 = socket.gethostbyname(socket.gethostname())
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((clientIP2, 12345))

def receive(client):
    global entre_surname
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "surname":
                client.send(entre_surname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
        
def write(client):
    global entre_surname
    while True:
        try:
            message = "{}: {}" .format(entre_surname, input(""))
            client.send(message.encode("utf-8"))
        except:
            print("An error occured!")
            client.close()
            break

        
receive_thread1 = threading.Thread(target=receive, args=(client1,))
receive_thread1.start()

write_thread1 = threading.Thread(target=write, args=(client1,))
write_thread1.start()

receive_thread2 = threading.Thread(target=receive, args=(client2,))
receive_thread2.start()

write_thread2 = threading.Thread(target=write, args=(client2,))
write_thread2.start()


