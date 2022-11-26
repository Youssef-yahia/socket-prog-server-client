import socket
import threading
import CaesarCipher

nickname = input("Write your nickname : ")

host = "127.0.0.1"
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

def receive():
    while True:
        try:
            
            message = client.recv(1024).decode('utf-8')
            if message == "NICK" :
                client.send(nickname.encode('utf-8'))
            else:
                #unlockedMessage = caesarDecrypt(message,7)
                print(message)
        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()