# # #!/usr/bin/env python3
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import ImageTk, Image
import queue

# import all functions /
# everything from chat.py file
# from chat import *

PORT = 55555
host = "127.0.0.1"
FORMAT = "utf-8"

# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)
client.connect((host, 55555))


# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self):
    
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
        
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Find a Game Server")
        self.login.resizable(width = False,
                            height = False)
        self.login.configure(width = 500,
                            height = 500)
        # create a Label
        self.pls = Label(self.login,
                    text = "Pick an Active Game Server",
                    justify = CENTER,
                    font = "Helvetica 14 bold")
        
        self.pls.place(x = 100,y = 20)
        
        # create a Label
 
        self.labelName5 = Label(self.login,
                            text = "Game                 Players     ServerID",
                            font = "Helvetica 10")
        
        self.labelName = Label(self.login,
                            text = "Clue Game (Mods)          4       169.1.0.1",
                            font = "Helvetica 10")
        
        self.labelName2 = Label(self.login,
                            text = "Clue Game (Mods)          3       254.0.0.1",
                            font = "Helvetica 10")

        self.labelName3 = Label(self.login,
                            text = "Clue Game (No Mods)     3       127.0.11.1",
                            font = "Helvetica 10")

        self.labelName4 = Label(self.login,
                            text = "Clue Game (Creative)     4       210.0.7.1",
                            font = "Helvetica 10")
        
        self.labelName5.place(x = 100, y = 50)
        self.labelName.place(x = 100, y = 100)
        self.labelName2.place(x = 100, y = 150)
        self.labelName3.place(x = 100, y = 200)
        self.labelName4.place(x = 100, y = 250)

        # create a entry box for
        # tyoing the message
        self.entryName = Entry(self.login,
                            font = "Helvetica 14")
        
        self.entryName.place(x = 100, y = 300)

        
        # set the focus of the cursor
        self.entryName.focus()
        
        # create a Continue Button
        # along with action
        self.go = Button(self.login,
                        text = "LOGIN",
                        font = "Helvetica 14 bold",
                        command = lambda: self.goAhead(self.entryName.get()))
        
        self.go.place(relx = 0.4,
                    y = 400)
        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)

        chatRcv = threading.Thread(target = self.chatRecieve)
        chatRcv.start()
        
        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()

    # The main layout of the chat
    def layout(self,name):
    
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("ClueX (Online)")
        self.Window.resizable(width = False,
                            height = False)
        self.Window.configure(width = 1000,
                            height = 840,
                            bg = "#17202A")
        self.labelHead = Label(self.Window,
                            bg = "#17202A",
                            fg = "#EAECEE",
                            text = self.name ,
                            font = "Helvetica 13 bold",
                            pady = 5)
        
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                        width = 450,
                        bg = "#ABB2B9")

        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)

        
        self.textCons = Text(self.Window,
                            width = 20,
                            height = 2,
                            bg = "#17202A",
                            fg = "#EAECEE",
                            font = "Helvetica 10",
                            padx = 5,
                            pady = 5)
        
        self.textCons.place(relheight = 0.735,
                            relwidth = .35,
                            rely = 0.08)
        
        self.labelBottom = Label(self.Window,
                                bg = "#ABB2B9",
                                height = 120)
        
        self.labelBottom.place(relwidth = 1,
                            rely = 0.775)
        
        self.entryMsg = Entry(self.labelBottom,
                            bg = "#2C3E50",
                            fg = "#EAECEE",
                            font = "Helvetica 13")
        
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.74,
                            relheight = 0.03,
                            rely = 0.008,
                            relx = 0.011)
        
        self.entryMsg.focus()
        
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "ENTER",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
        
        self.buttonMsg.place(relx = 0.77,
                            rely = 0.008,
                            relheight = 0.03,
                            relwidth = 0.22)
        
        self.textCons.config(cursor = "arrow")

        # ###Chat
        self.chatEntryMsg = Entry(self.labelBottom,
                    bg = "#2C3E50",
                    fg = "#EAECEE",
                    font = "Helvetica 13")
        
        # # place the given widget
        # # into the gui window
        self.chatEntryMsg.place(relwidth = 0.74,
                            relheight = 0.03,
                            rely = 0.05,
                            relx = 0.011)
        
        # # create a Send Button
        self.chatButtonMsg = Button(self.labelBottom,
                                text = "SEND CHAT",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendChatButton(self.chatEntryMsg.get()))
    
        self.chatButtonMsg.place(relx = 0.77,
                            rely = 0.05,
                            relheight = 0.03,
                            relwidth = 0.22)

        # ###endChat
        
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
        
        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
        
        scrollbar.config(command = self.textCons.yview)
        
        self.textCons.config(state = DISABLED)

        filename = "board.png"
        pillow_image = Image.open(filename)
        pillow_image.thumbnail((550,550),Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(pillow_image)
        self.Window.bg = bg  # to prevent the image garbage collected.

        self.labelBoard = Canvas(self.Window)
        self.labelBoard.place(x=400, y=75, width=550, height=550)
        self.labelBoard.create_image(0, 0, image = bg, 
                        anchor = "nw")


        #Load in all of the players (four)
        filename_mustard = "./tokens/Colonel Mustard.png"
        filename_plum = "./tokens/Professor Plum.png"
        filename_green = "./tokens/Reverend Green.png"
        filename_white = "./tokens/Mrs. White.png"

        pillow_image_1 = Image.open(filename_mustard)
        pillow_image_2 = Image.open(filename_plum)
        pillow_image_3 = Image.open(filename_green)
        pillow_image_4 = Image.open(filename_white)

        pillow_image_1.thumbnail((70,70),Image.ANTIALIAS)
        pillow_image_2.thumbnail((70,70),Image.ANTIALIAS)
        pillow_image_3.thumbnail((70,70),Image.ANTIALIAS)
        pillow_image_4.thumbnail((70,70),Image.ANTIALIAS)

        bg1 = ImageTk.PhotoImage(pillow_image_1)
        bg2 = ImageTk.PhotoImage(pillow_image_2)
        bg3 = ImageTk.PhotoImage(pillow_image_3)
        bg4 = ImageTk.PhotoImage(pillow_image_4)

        self.Window.bg1 = bg1  # to prevent the image garbage collected.
        self.Window.bg2 = bg2  # to prevent the image garbage collected.
        self.Window.bg3 = bg3  # to prevent the image garbage collected.
        self.Window.bg4 = bg4  # to prevent the image garbage collected.

        self.labelPlayer1 = Canvas(self.Window, borderwidth=2, background="red")
        self.labelPlayer2 = Canvas(self.Window, borderwidth=2, background="red")
        self.labelPlayer3 = Canvas(self.Window, borderwidth=2, background="red")
        self.labelPlayer4 = Canvas(self.Window, borderwidth=2, background="red")

        self.labelPlayer1.place(x=400, y=75, width=50, height=70)
        self.labelPlayer2.place(x=400, y=95, width=50, height=70)
        self.labelPlayer3.place(x=400, y=105, width=50, height=70)
        self.labelPlayer4.place(x=400, y=125, width=50, height=70)

        self.labelPlayer1.create_image(0, 0, image = bg1, anchor = "nw")
        self.labelPlayer2.create_image(0, 0, image = bg2, anchor = "nw")
        self.labelPlayer3.create_image(0, 0, image = bg3, anchor = "nw")
        self.labelPlayer4.create_image(0, 0, image = bg4, anchor = "nw")

    # def playerMove(self, msg):
    #     self.labelPlayer1.place(x=700, y=300, width=50, height=70)

    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.msg=msg
        self.entryMsg.delete(0, END)
        snd= threading.Thread(target = self.sendMessage)
        snd.start()

    def sendChatButton(self, msg):
        self.chatMsg=msg
        self.chatEntryMsg.delete(0, END)
        chatSnd= threading.Thread(target = self.chatSendMessage)
        chatSnd.start()


    # function to receive messages
    def receive(self):
        original_player_positions = {1:[400,420], 2:[400,190], 3:[900,210], 4:[900,400]}
        room_positions = {"Hall":[650,125], "Lounge":[800,125], "Library":[475,250], 
            "Kitchen":[800,500], "Billiard Room":[475,350], "Study":[475,100],
            "Dining Room": [800,300], "Conservatory":[475,500], "Ballroom": [650,500]}

        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                
                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                
                elif message[:2] == 'MP':
                    generic , playerPiece, roomPlace = message.split(":")[0],message.split(":")[1],message.split(":")[2]
                    
                    if playerPiece == "Colonel Mustard":
                        self.labelPlayer1.place(x=room_positions[roomPlace][0], y=room_positions[roomPlace][1], width=50, height=70)

                    elif playerPiece == "Professor Plum":
                        self.labelPlayer2.place(x=room_positions[roomPlace][0], y=room_positions[roomPlace][1], width=50, height=70)
                    
                    elif playerPiece == "Reverend Green":
                        self.labelPlayer3.place(x=room_positions[roomPlace][0], y=room_positions[roomPlace][1], width=50, height=70)

                    else:
                        self.labelPlayer4.place(x=room_positions[roomPlace][0], y=room_positions[roomPlace][1], width=50, height=70)

                elif message[:2] == 'SC':
                    self.labelPlayer1.place(x=original_player_positions[1][0], y=original_player_positions[1][1], width=50, height=70)
                    self.labelPlayer2.place(x=original_player_positions[2][0], y=original_player_positions[2][1], width=50, height=70)
                    self.labelPlayer3.place(x=original_player_positions[3][0], y=original_player_positions[3][1], width=50, height=70)
                    self.labelPlayer4.place(x=original_player_positions[4][0], y=original_player_positions[4][1], width=50, height=70)
                else:
                    # insert messages to text box
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END,
                                        message+"\n\n")
                    
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)

            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break

    def new_chat(msg):
        print("cows")
        msg_list = msg.split()
        if msg[0] == "@":
            usr = msg_list[0][1:]
            if usr == self.name:
                print("hi")
                self.textCons.config(state = NORMAL)
                self.textCons.insert(END,
                                    msg_list[-1] + ": " + " ".join(msg_list[1:-1]) + "\n\n")
                
                self.textCons.config(state = DISABLED)
                self.textCons.see(END)
        else:
            self.textCons.config(state = NORMAL)
            self.textCons.insert(END,
                               msg_list[-1] + ": " + " ".join(msg_list[0:-1])+"\n\n")
            
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)

    def chatRecieve(self):
        lastChat = ""
        with open('chat.txt') as f:
            while True:
                try:
                    line = f.readlines()[-1]
                    if line != lastChat:
                        msg=line
                        msg_list = line.split()
                        if msg[0] == "@":
                            
                            usr = msg_list[0][1:]
                            if usr == self.name:
                                self.textCons.config(state = NORMAL)
                                self.textCons.insert(END,
                                                    msg_list[-1] + ": " + " ".join(msg_list[1:-1]) + "\n\n")
                                
                                self.textCons.config(state = DISABLED)
                                self.textCons.see(END)
                        else:
                            self.textCons.config(state = NORMAL)
                            self.textCons.insert(END,
                                            msg_list[-1] + ": " + " ".join(msg_list[0:-1])+"\n\n")
                            
                            self.textCons.config(state = DISABLED)
                            self.textCons.see(END)
                        lastChat = line
                except:
                    pass
    # function to send messages
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break

    def chatSendMessage(self):
        with open("chat.txt", "a") as chatfile:
            chatfile.write(self.chatMsg + " " + self.name + "\n")




# create a GUI class object
g = GUI()
