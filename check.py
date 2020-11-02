#!python3
"""
Assigning a function to a Button widget
Getting and Inserting Entry widgets
"""
import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("Madlib")
win.geometry("600x200")

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction():
    number = e1.get()
    e2.delete(0,END)
    e2.insert(0,number)

b1 = tk.Button(win, text="Click to enter",command=clickFunction)
e1=tk.Entry(win,width=20)
e2=tk.Entry(win, width=20, textvariable=eoutput)

e1.grid(row=1,column=1)
b1.grid(row=2, column=1)
e2.grid(row=3,column=1)




win.mainloop()

# a^2 + 5x + 4
# x^2 + 5X + 6
# X^2 + 2x + 1

# x^2 -3x +2

# X^2 - x -2