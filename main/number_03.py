""" Creating Buttons """

# importing relevant libraries
from tkinter import *

# Creating root widget
root = Tk()

# Creating button widget and packing it
myButton = Button(root, text="Click on me!", padx=50, pady=50)
myButton.pack()

root.mainloop()
