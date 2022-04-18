import socket
import select
from glob import glob
from tkinter import *
from PIL import Image, ImageTk
import Clueless

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, so server informs operating system that it's going to use given IP and port
# For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.bind((IP, PORT))

# This makes server listen to new connections
server_socket.listen()

# List of sockets for select.select()
sockets_list = [server_socket]

# List of connected clients - socket as a key, user header and name as data
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')


gameLogic = Clueless
caseFile = Clueless.case_file   # Case file
playerDecks = Clueless.player_decks # Player hands
commonCard = Clueless.common_cards # Common cards

class GUI:
    def __init__(self):

        # Create object 
        self.root = Tk()
        
        # Adjust size 
        self.root.geometry("1700x900")   #Increase size from 1400x900. Can be changed back once the game logic texts are broken up into smaller pieces
        
        # Add image file
        filename = "board.png"
        pillow_image = Image.open(filename)
        # You must keep a reference to this `tk_image`
        # Otherwise the image would show up on the board
        bg = ImageTk.PhotoImage(pillow_image)
        
        # Create Canvas 
        canvas1 = Canvas( self.root, width = 1650,
                        height = 900)
        
        canvas1.pack(fill = "both", expand = True)
        
        # Main Board Image
        canvas1.create_image(400, 200, image = bg, 
                            anchor = "nw")
        
        # Add Text
        # canvas1.create_text( 200, 850, text = "Welcome")
        
        # def pretty(d, indent=0):
        #     for key, value in d.items():
        #         print('\t' * indent + str(key))
        #         if isinstance(value, dict):
        #             pretty(value, indent+1)
        #         else:
        #             print('\t' * (indent+1) + str(value))

        def playerDeckLogs():
            textBoxLineNum = 1   # Initial line number for text box

            # global textBoxLineNum
            print("Herro")
            # gamePlay_log.delete("1.0", tk.END)
            # Insert text for the player decks
            # gamePlay_log.insert(str(textBoxLineNum)+".0", "\nPLAYER DECKS\n")
            gamePlay_log.insert(str(textBoxLineNum)+".0", "PLAYER DECKS\n")
            textBoxLineNum += 1
            for i in playerDecks:
                gamePlay_log.insert(str(textBoxLineNum)+".0", (str(i) + ": " + str(playerDecks[i])))
                gamePlay_log.insert(str(textBoxLineNum+1)+".0","\n")
                textBoxLineNum += 1
            gamePlay_log.insert(str(textBoxLineNum)+".0", "\n")
            textBoxLineNum += 1
        
        def chatRoom(message):
            # global textBoxLineNum
            print("Sup with message")
            # gamePlay_log.delete("1.0", tk.END)
            # Insert text for the player decks
            # gamePlay_log.insert(str(textBoxLineNum)+".0", "\nPLAYER DECKS\n")
            chat_log.insert(message + "\n")


        gamePlay_log  = Text(self.root, width = 75, height = 40, takefocus=0)
        gamePlay_log_canvas = canvas1.create_window( 1650, 10, anchor = "ne",
                                            window = gamePlay_log)
        # gamePlay_log.config(state=DISABLED)     #Make the Text box read-only

        # Create Buttons
        button1 = Button( self.root, text = "Up", height = 3, width=5, command = playerDeckLogs)
        button2 = Button( self.root, text = "Down",height = 3, width=5)
        button3 = Button( self.root, text = "Left",height = 3, width=5)
        button4 = Button( self.root, text = "Right",height = 3, width=5)

        chat_log  = Text(self.root, width = 30, height = 40, takefocus=0)
        label1 = Label(self.root, text="PLAYER 1", borderwidth=1, relief="solid", height=3, width=20)
        label2 = Label(self.root, text="PLAYER 2", borderwidth=0, relief="solid", height=3, width=20)
        label3 =  Label(self.root, text="PLAYER 3", borderwidth=0, relief="solid", height=3, width=20)


        
        # Display Buttons
        button1_canvas = canvas1.create_window( 50, 700, 
                                            anchor = "nw",
                                            window = button1)
        
        button2_canvas = canvas1.create_window( 50, 770,
                                            anchor = "nw",
                                            window = button2)
        
        button3_canvas = canvas1.create_window( 100, 700, anchor = "nw",
                                            window = button3)

        button4_canvas = canvas1.create_window( 100, 770, anchor = "nw",
                                            window = button4)


        chat_log_canvas = canvas1.create_window( 100, 10, anchor = "nw",
                                            window = chat_log)

        label1_canvas = canvas1.create_window( 400, 30, anchor = "nw",
                                            window = label1)

        label2_canvas = canvas1.create_window( 600, 30, anchor = "nw",
                                            window = label2)

        label2_canvas = canvas1.create_window( 800, 30, anchor = "nw",
                                            window = label3)    

        
        self.root.mainloop()
        
        
        # Handles message receiving
        def receive_message(client_socket):

            try:

                # Receive our "header" containing message length, it's size is defined and constant
                message_header = client_socket.recv(HEADER_LENGTH)

                # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                if not len(message_header):
                    return False

                # Convert header to int value
                message_length = int(message_header.decode('utf-8').strip())

                # Return an object of message header and message data
                return {'header': message_header, 'data': client_socket.recv(message_length)}

            except:

                # If we are here, client closed connection violently, for example by pressing ctrl+c on his script
                # or just lost his connection
                # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
                # and that's also a cause when we receive an empty message
                return False

        while True:

            # Calls Unix select() system call or Windows select() WinSock call with three parameters:
            #   - rlist - sockets to be monitored for incoming data
            #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
            #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
            # Returns lists:
            #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
            #   - writing - sockets ready for data to be send thru them
            #   - errors  - sockets with some exceptions
            # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
            read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)


            # Iterate over notified sockets
            for notified_socket in read_sockets:

                # If notified socket is a server socket - new connection, accept it
                if notified_socket == server_socket:

                    # Accept new connection
                    # That gives us new socket - client socket, connected to this given client only, it's unique for that client
                    # The other returned object is ip/port set
                    client_socket, client_address = server_socket.accept()

                    # Client should send his name right away, receive it
                    user = receive_message(client_socket)

                    # If False - client disconnected before he sent his name
                    if user is False:
                        continue

                    # Add accepted socket to select.select() list
                    sockets_list.append(client_socket)

                    # Also save username and username header
                    clients[client_socket] = user

                    print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
                # Else existing socket is sending a message
                else:

                    # Receive message
                    message = receive_message(notified_socket)

                    # If False, client disconnected, cleanup
                    if message is False:
                        print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                        # Remove from list for socket.socket()
                        sockets_list.remove(notified_socket)

                        # Remove from our list of users
                        del clients[notified_socket]

                        continue

                    # Get user by notified socket, so we will know who sent the message
                    user = clients[notified_socket]

                    print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

                    # Iterate over connected clients and broadcast message
                    for client_socket in clients:

                        # But don't sent it to sender
                        if client_socket != notified_socket:

                            # Send user and message (both with their headers)
                            # We are reusing here message header sent by sender, and saved username header send by user when he connected
                            client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

            # It's not really necessary to have this, but will handle some socket exceptions just in case
            for notified_socket in exception_sockets:

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                del clients[notified_socket]
            

g = GUI()