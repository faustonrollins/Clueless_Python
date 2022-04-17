# Import module 
from tkinter import *
from PIL import Image, ImageTk

  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("900x900")
  
# Add image file
filename = "board.png"
pillow_image = Image.open(filename)
# You must keep a reference to this `tk_image`
# Otherwise the image would show up on the board
bg = ImageTk.PhotoImage(pillow_image)
  
# Create Canvas 
canvas1 = Canvas( root, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
  
# Add Text
canvas1.create_text( 200, 850, text = "Welcome")
  
# Create Buttons
button1 = Button( root, text = "Exit")
button3 = Button( root, text = "Start")
button2 = Button( root, text = "Reset")
  
# Display Buttons
button1_canvas = canvas1.create_window( 100, 10, 
                                       anchor = "nw",
                                       window = button1)
  
button2_canvas = canvas1.create_window( 100, 40,
                                       anchor = "nw",
                                       window = button2)
  
button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
                                       window = button3)
  
# Execute tk
root.mainloop()