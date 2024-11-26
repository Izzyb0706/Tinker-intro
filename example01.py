# GUI - Graphical user interface
import tkinter as tk


def on_button_click():
   # print("Stoichiometry is dumb")
    label.config(text="Arnold is Better", image=img)


default_font = font = ("Arial", 20, "bold"),


window = tk.Tk()
img = tk.PhotoImage(file=r".\resources\arnold.png")

# give the window a title
window.title("Garfield Application")

# set the sixe of window
window.geometry("400x300")  # width x height

# change the icon in the top left
icon = tk.PhotoImage(file=r".\resources\garfield.png")
window.iconphoto(True, icon)


# change background color of window
window.config(bg="#055555")

# create a label
label = tk.Label(window,
                 text="hi",
                 font=default_font,
                 foreground="pink",
                 background="purple",
                 image=icon,
                 compound="top",
                 bd=20,
                 relief="raised",
                 padx=15,
                 pady=25)
# Could shorthand foreground/background with fg/bg

# The label will not be there until we pack it
label.pack(pady=20)

# label.place(x=0, y=0)

button = tk.Button(window, text="I hate chemistry",
                   font=default_font,
                   command=on_button_click,
                   activebackground="red",
                   activeforeground="green"
                   )


button.pack()

window.mainloop()
