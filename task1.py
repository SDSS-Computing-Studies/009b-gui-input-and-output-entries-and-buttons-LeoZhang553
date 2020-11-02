"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
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
    number2 = e3.get()
    number3 = e4.get()
    e2.delete(0,END)
    a=str(number+number2+number3)
    e2.insert(0,a)

b1 = tk.Button(win, text="Click to enter",command=clickFunction)
e1=tk.Entry(win,width=20)
e2=tk.Entry(win, width=20, textvariable=eoutput)

e3=tk.Entry(win,width=20)
e4=tk.Entry(win,width=20)

e1.grid(row=1,column=1)
e3.grid(row=1,column=2)
e4.grid(row=1,column=3)
b1.grid(row=2, column=1,columnspan=3)
e2.grid(row=3,column=1)

win.mainloop()

