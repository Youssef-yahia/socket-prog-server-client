import socket
# specify the host
host = '127.0.0.1'

# specify the port (that we are going to use, note that 0 to 1023 is reserved)
port = 12345

# specify the type of networking standard which is ipv4 & Transport
# Layer protocol which is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now to assign (bind) our socket to the IP & port, here we till os our socket will use the following IP Interface: port
# bind the socket
s.bind((host, port))

# our socket listen & accept only 5 clients.
s.listen(5)
# here we start to accept the connection from the client

print("Blocked Wating till a connection show up")

conn, addr = s.accept()  # block wait untill a connection come
'''
conn is the new socket 
created to communicate with the client, for every client a new socket
is created to communicate with it ;)

addr is some information with the connected client, is a tuple contains two data
add[0] --> ip address of client.
add[1] --> port of the client.

'''
while True:  # recive data from the client until it closes the connection
    # block wait until client send data [1024] is buffer
    data = conn.recv(1024)
    if not data:  # here an indicator that the client closed the connection
        break  # go outside loop
    conn.send(data)  # else replay with the same received data
conn.close()  # close the connection
s.close()
