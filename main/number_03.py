""" Creating Buttons """

# importing relevant libraries
from tkinter import *

# Creating root widget
root = Tk()

def my_click():
    my_label = Label(root, text="I clicked a button")
    my_label.pack()


# Creating button widget and packing it
myButton = Button(root, text="Click on me!", command=my_click, fg="blue", bg="red")
myButton.pack()

root.mainloop()
