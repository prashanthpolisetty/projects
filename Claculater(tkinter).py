from tkinter import *

window = Tk()
window.geometry('500x500')

e = Entry(window, font=("bold", 20))
e.place(x=0, y=0, height=60, width=500)


def click(num):
    res = e.get()
    e.delete(0, "end")
    e.insert(0, str(res) + str(num))


b = Button(window, text="1", height=5, width=10, background="blue", command=lambda: click(1))
b.place(x=10, y=70)

b = Button(window, text="2", height=5, width=10, background="blue", command=lambda: click(2))
b.place(x=90, y=70)

b = Button(window, text="3", height=5, width=10, background="blue", command=lambda: click(3))
b.place(x=170, y=70)

b = Button(window, text="4", height=5, width=10, background="blue", command=lambda: click(4))
b.place(x=10, y=155)

b = Button(window, text="5", height=5, width=10, background="blue", command=lambda: click(5))
b.place(x=90, y=155)

b = Button(window, text="6", height=5, width=10, background="blue", command=lambda: click(6))
b.place(x=170, y=155)

b = Button(window, text="7", height=5, width=10, background="blue", command=lambda: click(7))
b.place(x=10, y=240)

b = Button(window, text="8", height=5, width=10, background="blue", command=lambda: click(8))
b.place(x=90, y=240)

b = Button(window, text="9", height=5, width=10, background="blue", command=lambda: click(9))
b.place(x=170, y=240)

b = Button(window, text="0", height=5, width=10, background="blue", command=lambda: click(0))
b.place(x=90, y=325)


def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text="+", height=5, width=10, background="blue", command=add)
b.place(x=250, y=70)


def sub():
    n1 = e.get()
    global math
    math = "subtracetion"
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text="-", height=5, width=10, background="blue", command=sub)
b.place(x=250, y=155)


def multi():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text="*", height=5, width=10, background="blue", command=multi)
b.place(x=250, y=240)


def div():
    n1 = e.get()
    global math
    math = "divison"
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text="/", height=5, width=10, background="blue", command=div)
b.place(x=250, y=325)


def clear():
    e.delete(0, END)


b = Button(window, text="clear", height=5, width=10, background="blue", command=clear)
b.place(x=10, y=325)

def dot():
    n1 = e.get()
    global math
    math = "dot"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text=".", height=5, width=10, background="blue" , command=dot)
b.place(x=170, y=325)

def equals():
    n2 = e.get()
    e.delete(0, END)
    if (math == "addition"):
        e.insert(0, i + int(n2))
    elif (math == "subtracetion"):
        e.insert(0, i - int(n2))
    elif (math == "divison"):
        e.insert(0, i / int(n2))
    elif (math == "multiplication"):
        e.insert(0, i * int(n2))

b = Button(window, text="ENTER", height=5, width=10, background="blue" , command=equals)
b.place(x=10, y=410)


def equal():
    n2 = e.get()
    e.delete(0, END)
    if (math == "addition"):
        e.insert(0, i + int(n2))
    elif (math == "subtracetion"):
        e.insert(0, i - int(n2))
    elif (math == "divison"):
        e.insert(0, i / int(n2))
    elif (math == "multiplication"):
        e.insert(0, i * int(n2))


b = Button(window, text="=", height=5, width=10, background="blue", command=equal)
b.place(x=90, y=410)

mainloop()
