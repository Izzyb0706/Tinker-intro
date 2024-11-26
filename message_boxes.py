import tkinter as tk

from tkinter import messagebox


def show_message():
    response = messagebox.askquestion
    print(response)
    if response:
        print("")
    else:
        print("User wimped out")


window = tk.Tk()
window.title("Message Box Example")
window.geometry("400x300")

button = tk.Button(window, text="Show Message Box", command=show_message)
button.pack()


window.mainloop()
