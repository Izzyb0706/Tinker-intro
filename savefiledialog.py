from tkinter import *
from tkinter import filedialog


def save_text():
    file = filedialog.askopenfilename(
        defaulttextextension=".txt", filetypes=[("Text Files", "*.txt")])

    if file:
        with open(file, "w") as writer:
            writer.write(text_area.get(1.0, END))


window = Tk()

text_area = Text(window)
text_area.pack()
Button(window, text="Save text", command=save_text).pack()

window.mainloop()
