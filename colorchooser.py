from tkinter import *
from tkinter import colorchooser


def changebg():
    color = colorchooser.askcolor()
    print(color)
    window.config(bg=color[1])


window = Tk()
window.geometry("400x400")


button = Button(text="Change bg", command=changebg)
button.pack()


window.mainloop()
