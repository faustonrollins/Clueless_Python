# Import module 
from tkinter import *
from PIL import Image, ImageTk
import Clueless

# Pull data from the Clueless.py
# When the GUI starts, the import function instantiates a Clueless object
gameLogic = Clueless
caseFile = Clueless.case_file   # Case file
playerDecks = Clueless.player_decks # Player hands
commonCard = Clueless.common_cards # Common cards

# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1700x900")   #Increase size from 1400x900. Can be changed back once the game logic texts are broken up into smaller pieces
  
# Add image file
filename = "board.png"
pillow_image = Image.open(filename)
# You must keep a reference to this `tk_image`
# Otherwise the image would show up on the board
bg = ImageTk.PhotoImage(pillow_image)
  
# Create Canvas 
canvas1 = Canvas( root, width = 1650,
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
    print("Herro")
    gamePlay_log.insert(str(2)+".0", "\nPLAYER DECKS\n")
    # Insert text for the player decks
    textLineNum=2
    gamePlay_log.insert(str(textLineNum)+".0", "\nPLAYER DECKS\n")
    for i in playerDecks:
        gamePlay_log.insert(str(textLineNum)+".0", (str(i) + ": " + str(playerDecks[i])))
        gamePlay_log.insert(str(textLineNum+1)+".0","\n")
        textLineNum += 1

gamePlay_log  = Text(root, width = 75, height = 40, takefocus=0)
gamePlay_log_canvas = canvas1.create_window( 1650, 10, anchor = "ne",
                                       window = gamePlay_log)
# gamePlay_log.config(state=DISABLED)     #Make the Text box read-only

# Create Buttons
button1 = Button( root, text = "Up", height = 3, width=5, command = playerDeckLogs)
button2 = Button( root, text = "Down",height = 3, width=5)
button3 = Button( root, text = "Left",height = 3, width=5)
button4 = Button( root, text = "Right",height = 3, width=5)



# # Insert text for the Case File
# gamePlay_log.insert("1.0", "CASE FILE\n")
# textLineNum=2
# for i in caseFile:
#     gamePlay_log.insert(str(textLineNum)+".0", (str(i) + ": " + str(caseFile[i])))
#     gamePlay_log.insert(str(textLineNum+1)+".0","\n")
#     textLineNum += 1


# # Insert text for the common cards
# gamePlay_log.insert(str(textLineNum)+".0", "\nCOMMON CARDS\n")
# textLineNum +=2
# for i in commonCard:
#     gamePlay_log.insert(str(textLineNum)+".0", (str(i)))
#     gamePlay_log.insert(str(textLineNum+1)+".0","\n")
#     textLineNum += 1

chat_log  = Text(root, width = 30, height = 40, takefocus=0)
label1 = Label(root, text="PLAYER 1", borderwidth=1, relief="solid", height=3, width=20)
label2 = Label(root, text="PLAYER 2", borderwidth=0, relief="solid", height=3, width=20)
label3 =  Label(root, text="PLAYER 3", borderwidth=0, relief="solid", height=3, width=20)


  
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