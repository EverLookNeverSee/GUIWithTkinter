""" Creating Buttons """

# importing relevant libraries
from tkinter import *

# Creating root widget
root = Tk()

# Creating button widget and packing it
myButton = Button(root, text="Click on me!")
myButton.pack()

root.mainloop()
