import socket
import sys
from _thread import *

HOST = '127.0.0.1'
PORT = 8884
clients = 0
connected_id = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket successfully binded')

# Start listening on socket
s.listen(10)
print('Socket is listening')

clients = []

# Function for handling connections.
def clientthread(conn):
    # Sending message to connected client
    conn.sendall(b"hello")  # send only takes string
    global clients
    # loop until disconnect
    while True:
        # Receiving from client
        data = conn.recv(1024)
        if data.lower().find("id=-1") != -1:
            clients += 1
            print("new client ID set to " + str(clients))
            conn.sendall(b"SID=" + str(clients))
        if not data:
            break

    # If client disconnects
    conn.close()

def addclientsthread(sock): 
    global clients
    conn, addr = sock.accept()
    clients += [conn]
    print('Client connected on ' + addr[0])
    start_new_thread(clientthread, (conn,))

def sendallclients(message): 
    for client in clients : 
        client.send(message)

# now keep talking with the clients
start_new_thread(addclientsthread, (s,))
usr_input = ""
while str(usr_input) != "Q":
    # do stuff
    usr_input = input("Enter 'Q' to quit")
    if usr_input.find("cmd") == 0:
        sendallclients(usr_input[3:])
    if usr_input.find("hi") == 0:
        sendallclients("hey")
s.close()