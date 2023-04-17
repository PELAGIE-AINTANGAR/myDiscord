import socket
import threading

surname = input("Enter your surname: ")
clientIP = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((clientIP, 12345))


def receive():
    global surname
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "surname":
                client.send(surname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
        
def write():
    global surname
    while True:
        try:
            message = "{}: {}" .format(surname, input(""))
            client.send(message.encode("utf-8"))
        except:
            print("An error occured!")
            client.close()
            break

        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
