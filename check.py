#!python3
"""
Assigning a function to a Button widget
Getting and Inserting Entry widgets
"""

"""
# task 2
import tkinter as tk 
from tkinter import *

import math

win = tk.Tk()
win.title("Factor")
win.geometry("600x200")

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction():
    answer=""
    num1 = e1.get()
    num2 = e2.get()
    num1=float(num1)
    num2=float(num2)
    c=float((num1)**2 - 4*1*num2)
    a=1
    if c >=0 and c == int(c) and math.sqrt(c)==int(math.sqrt(c)):
        while a <= num2:
            if (num2)%a == 0:
                b=int((num2)/a)
                if a+b == num1:                    
                    b=str(b)
                    answer="(x + "+str(a)+")(x + "+b+")"

            a+=1
    else:
        answer="cannot be factored"

    e3.delete(0,END)
    e3.insert(0,answer)

l1=tk.Label(win,text="enter the coefficients: ")
l2=tk.Label(win,text="Factored form: ")
l3=tk.Label(win,text="x^2 + ")
l4=tk.Label(win,text="x + ")

b1 = tk.Button(win, text="Click to factor",command=clickFunction)

e1=tk.Entry(win,width=5)
e2=tk.Entry(win,width=5)
e3=tk.Entry(win, width=20, textvariable=eoutput)


l1.grid(row=1,column=1)
l3.grid(row=1,column=2)

e1.grid(row=1,column=3)

l4.grid(row=1,column=4)

e2.grid(row=1,column=5)


b1.grid(row=2, column=1, columnspan=5)


l2.grid(row=3,column=1)
e3.grid(row=3,column=2,columnspan=4)

win.mainloop()

"""

# a^2 + 5x + 4
# x^2 + 5X + 6
# X^2 + 2x + 1

# x^2 -3x +2

# X^2 - x -2