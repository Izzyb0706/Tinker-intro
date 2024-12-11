from tkinter import *


def check():
    value = text.get(1.5, "2.5")
    print(value)


window = Tk()
text = Text(window,
            font=("Courier New", 24),
            height=5,
            width=30
            )
text.pack()

button = Button(window, text="check", command=check)
button.pack()

window.mainloop()
