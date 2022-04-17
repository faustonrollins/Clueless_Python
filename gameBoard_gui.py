# Import module 
from tkinter import *
from PIL import Image, ImageTk

  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1400x900")
  
# Add image file
filename = "board.png"
pillow_image = Image.open(filename)
# You must keep a reference to this `tk_image`
# Otherwise the image would show up on the board
bg = ImageTk.PhotoImage(pillow_image)
  
# Create Canvas 
canvas1 = Canvas( root, width = 1400,
                 height = 900)
  
canvas1.pack(fill = "both", expand = True)
  
# Main Board Image
canvas1.create_image(400, 200, image = bg, 
                     anchor = "nw")
  
# Add Text
# canvas1.create_text( 200, 850, text = "Welcome")
  
# Create Buttons
button1 = Button( root, text = "Up", height = 3, width=5)
button2 = Button( root, text = "Down",height = 3, width=5)
button3 = Button( root, text = "Left",height = 3, width=5)
button4 = Button( root, text = "Right",height = 3, width=5)

chat_log  = Text(root, width = 30, height = 40, takefocus=0)
gamepPlay_log  = Text(root, width = 30, height = 40, takefocus=0)
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

chat_log_canvas = canvas1.create_window( 1370, 10, anchor = "ne",
                                       window = chat_log)


gamePlay_log_canvas = canvas1.create_window( 10, 10, anchor = "nw",
                                       window = gamepPlay_log)

label1_canvas = canvas1.create_window( 400, 30, anchor = "nw",
                                       window = label1)

label2_canvas = canvas1.create_window( 600, 30, anchor = "nw",
                                       window = label2)

label2_canvas = canvas1.create_window( 800, 30, anchor = "nw",
                                       window = label3)
# Execute tk
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