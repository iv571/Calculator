"""
Basic Calculator made using Python

Implements the following concepts:
-A Graphical User Interface (GUI) using Tkinter
-Functions
-If statements
-Python Math functions such as "round" and "float"
-Lambda functions
"""

from tkinter import *
import tkinter.font as font

#Initialize the GUI
root = Tk()
root.title('Calculator')
root.geometry('220x200+300+300')
root.resizable(False, False)

eq = IntVar()

#Clear the display
def clear():
    e.delete(0, END)

#Add numbers
def add():
    num1 = e.get()
    e.delete(0, END)
    eval("add", num1)

#Multiply numbers
def mult():
    num1 = e.get()
    e.delete(0, END)
    eval("mult", num1)

#Subtract numbers
def sub():
    num1 = e.get()
    e.delete(0, END)
    eval("sub", num1)

#Divide numbers
def div():
    num1 = e.get()
    e.delete(0, END)
    eval("div", num1)

#Exponentiate numbers
def pow():
    num1 = e.get()
    e.delete(0, END)
    eval("pow", num1)

#Evaluate an operation
def eval(func, num1):
    equal.wait_variable(eq)
    num2 = e.get()
    e.delete(0, END)
    if func == "add":
        e.insert(INSERT, round(float(num1) + float(num2), 7))
    elif func == "sub":
        e.insert(INSERT, round(float(num1) - float(num2), 7))
    elif func == "div":
        e.insert(INSERT, round(float(num1) / float(num2), 7))
    elif func == "mult":
        e.insert(INSERT, round(float(num1) * float(num2), 7))
    elif func == "pow":
        e.insert(INSERT, round(float(num1) ** float(num2), 7))

#Show numbers in the display
def disp1():
    e.insert(INSERT, 1)

def disp2():
    e.insert(INSERT, 2)

def disp3():
    e.insert(INSERT, 3)

def disp4():
    e.insert(INSERT, 4)

def disp5():
    e.insert(INSERT, 5)

def disp6():
    e.insert(INSERT, 6)

def disp7():
    e.insert(INSERT, 7)

def disp8():
    e.insert(INSERT, 8)

def disp9():
    e.insert(INSERT, 9)

def disp0():
    e.insert(INSERT, 9)

def dispd():
    e.insert(INSERT, ".")

#Create widgets
f = font.Font(family='Tahoma', size=14)

e = Entry(root, bg="#444444", fg="white", justify='right', font=f)
but1 = Button(root, text="1", padx="10", font=f, command=disp1)
but2 = Button(root, text="2", padx="10", font=f, command=disp2)
but3 = Button(root, text="3", padx="10", font=f, command=disp3)
but4 = Button(root, text="4", padx="10", font=f, command=disp4)
but5 = Button(root, text="5", padx="10", font=f, command=disp5)
but6 = Button(root, text="6", padx="10", font=f, command=disp6)
but7 = Button(root, text="7", padx="10", font=f, command=disp7)
but8 = Button(root, text="8", padx="10", font=f, command=disp8)
but9 = Button(root, text="9", padx="10", font=f, command=disp9)
but0 = Button(root, text="0", padx="10", font=f, command=disp0)
dot = Button(root, text=".", padx="10", font=f, command=dispd)

add = Button(root, text="+", padx="10", fg="blue", font=f, command=add)
sub = Button(root, text="-", padx="10", fg="blue", font=f, command=sub)
mult = Button(root, text="x", padx="10", fg="blue", font=f, command=mult)
div = Button(root, text="/", padx="10", fg="blue",font=f, command=div)
pow = Button(root, text="^", padx="10", fg="blue", font=f, command=pow)
c = Button(root, text="C", padx="10", font=f, bg="red", fg="white", command=clear)
equal = Button(root, bg="green", text="=", padx="50", pady="0", fg="white", font=f, command=lambda: eq.set(1))

#Add widgets
e.grid(row=0, columnspan=5)

but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)
add.grid(row=1, column=3)
c.grid(row=1, column=4)

but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
sub.grid(row=2, column=3)
div.grid(row=2, column=4)

but7.grid(row=3, column=0)
but8.grid(row=3, column=1)
but9.grid(row=3, column=2)
mult.grid(row=3, column=3)
pow.grid(row=3, column=4)

dot.grid(row=4, column=0)
but0.grid(row=4, column=1)
equal.grid(row=4, column=2, columnspan=3)



