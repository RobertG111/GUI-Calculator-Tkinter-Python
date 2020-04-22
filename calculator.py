# Management
from tkinter import *

expression = ""

# Calculator
def calculator():
    global equation

    calculator_screen = Tk()
    calculator_screen.title("Calculator")
    calculator_screen.geometry("342x237")
    calculator_screen.configure(bg="Light Blue")

    equation = StringVar()

    entry = Entry(calculator_screen, textvariable=equation, width=10)
    entry.grid(columnspan=4, ipadx=70)

    Button(calculator_screen, text="1", fg="black", width=12, height=3 ,command=lambda: press(1)).grid(column = 1, row=1)
    Button(calculator_screen, text="2", fg="black", width=12, height=3 , command=lambda: press(2)).grid(column=2, row=1)
    Button(calculator_screen, text="3", fg="black", width=12, height=3 , command=lambda: press(3)).grid(column=3, row=1)
    Label(calculator_screen,text="", width=0, bg="Light Blue").grid(column=4,row=1)
    Button(calculator_screen, text="*", fg="black", width=5, height=2, command=lambda: press("*")).grid(column=5, row=1)

    Button(calculator_screen, text="4", fg="black", width=12, height=3 ,command=lambda: press(4)).grid(column = 1, row=2)
    Button(calculator_screen, text="5", fg="black", width=12, height=3 ,command=lambda: press(5)).grid(column=2, row=2)
    Button(calculator_screen, text="6", fg="black", width=12, height=3 ,command=lambda: press(6)).grid(column=3, row=2)
    Label(calculator_screen,text="", width=0, bg="Light Blue").grid(column=4,row=2)
    Button(calculator_screen, text="/", fg="black", width=5, height=2 ,command=lambda: press('/')).grid(column=5, row=2)

    Button(calculator_screen, text="7", fg="black", width=12, height=3 ,command=lambda: press(7)).grid(column = 1, row=3)
    Button(calculator_screen, text="8", fg="black", width=12, height=3 ,command=lambda: press(8)).grid(column=2, row=3)
    Button(calculator_screen, text="9", fg="black", width=12, height=3 ,command=lambda: press(9)).grid(column=3, row=3)
    Label(calculator_screen,text="", width=0, bg="light blue").grid(column=4,row=3)
    Button(calculator_screen, text="-", fg="black", width=5, height=2 ,command=lambda: press('-')).grid(column=5, row=3)

    Button(calculator_screen, text="0", fg="black", width=12, height=3 ,command=lambda: press(0)).grid(column = 1, row=4)
    Button(calculator_screen,text="Clear", width=12, height=3, command=clear).grid(column =2 , row=4)
    Button(calculator_screen, text="=", fg="black", width=12, height=3, command=equal).grid(column=3, row=4)
    Label(calculator_screen,text="", width=0, bg='light blue').grid(column=4,row=4)
    Button(calculator_screen, text="+", fg="black", width=5, height=2 ,command=lambda: press('+')).grid(column=5, row=4)

    calculator_screen.mainloop()

#Functions
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    global equation

    total = str(eval(expression))
    equation.set(total)

def clear():
    global expression
    expression = ""
    equation.set("")

calculator()
