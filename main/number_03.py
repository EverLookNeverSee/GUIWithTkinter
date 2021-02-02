""" Creating Buttons """

# importing relevant libraries
from tkinter import *

# Creating root widget
root = Tk()

def my_click():
    my_label = Label(root, text="I clicked a button")
    my_label.pack()


# Creating button widget and packing it
myButton = Button(root, text="Click on me!", padx=50, pady=50, command=my_click)
myButton.pack()

root.mainloop()
