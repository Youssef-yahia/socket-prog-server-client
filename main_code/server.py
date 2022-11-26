import threading
import socket
import CaesarCipher


host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []


#boardcast function send message to clients

def broadcast(message,owner):
    for client in clients:
        if client != owner:
            client.send(message)




def handle(client,name):
    while True:
        try:

            message = client.recv(1024)
            mss = message.decode('utf-8')
            encryptM = cipher.caesarEncrypt(mss,7)
            decryptM = cipher.decrypt_message(encryptM,7)
            print(encryptM)
            print(decryptM)
            
            broadcast(message,client)

        except:
            index = clients.index(client)
            broadcast(f"{name} left the chat !".encode("utf-8"),client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

#receive message from clients

def receive():
    while True:
        client , address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat !".encode("utf-8"),client)
        client.send("Connected to the server".encode("utf-8"))



        thread = threading.Thread(target=handle, args=(client,nickname))
        thread.start()

print("server is listening ....")
receive()
