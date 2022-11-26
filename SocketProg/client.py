import socket
#specify the IP of the server you want to connect to
host ='127.0.0.1'

#specify the port of the server
port = 12345

#specify the type of network & transport layer protocol
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect t server
s.connect((host,port))

'''now the client is connected, to send data we first to convert it to an array of bytes,
because the string in python is a class, in networking only we send data as an array(stream)
of bytes, so if we want to send a string = 'Hello' , stringBytes = 'Hello'.encode() [defualt encode utf8] by default data
is encoded using utf8, it's important to know the encoding to decode it correctly in the next side [at server]'''

#lets start to send data
s.send('Welcome User!'.encode())
#after sending we block wait until listening from server
data = s.recv(1024)
s.close()
print(data.decode())
