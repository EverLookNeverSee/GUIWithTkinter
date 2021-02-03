""" Creating input fields """

# importing necessary modules
from tkinter import *

# creating root widget
root = Tk()

# Creating an entry widget
e = Entry(root, borderwidth=3, width=50)
e.pack()

def myClick():
    my_label = Label(root, text=f"Hello {e.get()}")
    my_label.pack()

my_button = Button(root, text="Enter your name", command=myClick)
my_button.pack()

root.mainloop()
