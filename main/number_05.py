""" Building a simple calculator app """

# importing relevant modules
from tkinter import *

# creating root widget
root = Tk()
# setting app title
root.title("Simple Calculator")

# creating an entry and positioning using grid system
e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()