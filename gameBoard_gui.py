# Import module 
from asyncore import read
from glob import glob
from tkinter import *
from PIL import Image, ImageTk
import Clueless
import threading
from time import time, sleep

# import tkinter as tk      // Uncomment this to use tk.END
# Pull data from the Clueless.py
# When the GUI starts, the import function instantiates a Clueless object
gameLogic = Clueless
caseFile = Clueless.case_file   # Case file
playerDecks = Clueless.player_decks # Player hands
commonCard = Clueless.common_cards # Common cards
chatRoomMessage = " "
starttime = time()
chatLine = 1

with open('readme.txt', 'w') as f:
    f.write(chatRoomMessage)

# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1700x900")   #Increase size from 1400x900. Can be changed back once the game logic texts are broken up into smaller pieces
  
# Add image file
filename = "board.png"
pillow_image = Image.open(filename)
bg = ImageTk.PhotoImage(pillow_image)

# Add image file
filename_deck = "deck.png"
pillow_image_deck = Image.open(filename_deck)
deck_bg = ImageTk.PhotoImage(pillow_image_deck)
  
# Create Canvas 
canvas1 = Canvas( root, width = 1650,
                 height = 900)
  
canvas1.pack(fill = "both", expand = True)
  
textBoxLineNum = 1   # Initial line number for text box
def playerDeckLogs():
    global textBoxLineNum
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

def gameChatRoom():
    global chatRoomMessage
    global chatLine

    chatRoomMessage = "Welcome to the Clue Party \n"
    chat_log.insert(str(chatLine) +".0", chatRoomMessage)

def refreshChat():
    global chatRoomMessage
    global chatLine

    with open('readme.txt') as f: 
        lines = f.readlines()[0] + "\n"
    if chatRoomMessage != lines:
        chat_log.insert(str(chatLine) +".0", lines)
        chatRoomMessage = lines
        chatLine += 2
    root.after(1000, refreshChat) # every second...

# Create Buttons
button1 = Button( root, text = "Up", height = 3, width=5, command = playerDeckLogs)
button2 = Button( root, text = "Down",height = 3, width=5)
button3 = Button( root, text = "Left",height = 3, width=5)
button4 = Button( root, text = "Right",height = 3, width=5)


label1 = Label(root, text="PLAYER 1", borderwidth=1, relief="solid", height=3, width=20)
label2 = Label(root, text="PLAYER 2", borderwidth=0, relief="solid", height=3, width=20)
label3 =  Label(root, text="PLAYER 3", borderwidth=0, relief="solid", height=3, width=20)

gamePlay_log  = Text(root, width = 50, height = 40, takefocus=0)
chat_log  = Text(root, width = 50, height = 40, takefocus=0)
  
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


chat_log_canvas = canvas1.create_window( 50, 10, anchor = "nw",
                                       window = chat_log)

gamePlay_log_canvas = canvas1.create_window( 1650, 10, anchor = "ne",
                                       window = gamePlay_log)

label1_canvas = canvas1.create_window( 600, 30, anchor = "nw",
                                       window = label1)

label2_canvas = canvas1.create_window( 800, 30, anchor = "nw",
                                       window = label2)

label2_canvas = canvas1.create_window( 1000, 30, anchor = "nw",
                                       window = label3)

# Main Board Image
canvas1.create_image(525, 100, image = bg, 
                     anchor = "nw")

canvas1.create_image(1200, 700, image = deck_bg, 
                     anchor = "nw")



# Starting a new thread for the Server
def startServer():
    print("Starting server")
    import Server
if __name__ == "__main__":
    print("Starting a new thread for the Server")
    t1 = threading.Thread(target=startServer, name='t1', daemon=True)
    t1.start()
            

gameChatRoom()
refreshChat() 
root.mainloop()


# Josh: Heroo

# Melissa: Sup?

# Fauston: Hey guys!

# Logan: nice work!

# {client:
# 	{move: left,
# 		{
# 		...
# 		...
# 		...
# 		}
# 	}
# }