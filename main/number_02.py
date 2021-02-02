""" Positioning using tkinter's grid system """

# import necessary modules
from tkinter import *

# creating root widget
root = Tk()

# creating label widgets
my_label_1 = Label(root, text="HelloWorld")
my_label_2 = Label(root, text="My name is EverLookNeverSee")


# setting grid positioning system
my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=1)


root.mainloop()
