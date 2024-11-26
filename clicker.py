import tkinter as tk

default_font = font = ("Arial", 20, "bold")
num = 0


def count():
    global num
    num = num + 1
    label.config(text=num)


def clicker():
    print("Stoichiometry is dumb")


window = tk.Tk()
window.config(bg="#289555")

label = tk.Label(window,
                 text=num,
                 font=default_font,
                 foreground="black",
                 background="red",
                 )

window.geometry("400x300")

button = tk.Button(window, text="I hate chemistry",
                   font=default_font,
                   command=clicker,
                   activebackground="blue",
                   activeforeground="pink"
                   )

label.pack()
button.pack()

window.mainloop()
