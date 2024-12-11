import tkinter as tk
from tkinter import messagebox


def show_message():
    planner = entry.get()

    num_of_guests = scale.get()
    theme = listbox.get(tk.ACTIVE)

    planning = []
    if catering.get():
        planning.append("catering")
    elif music.get():
        planning.append("music")
    elif online_streaming.get("Online Streaming"):
        planning.append()

    planning_str = ", ".join(planning) if planning else "None"
    method = vote.get() if vote.get() else "Not selected"

    response = messagebox.showinfo("Your Event", f"Event Name: {label}\nPreferences: {
                                   planning_str}\nEvent Type:{event}\nNumber Of Guests:{guests}\nEvent Theme: {theme}")


def reset():
    entry.delete(0, tk.END)
    scale.set(0)
    listbox.select_set(0)
    catering.set(0)
    music.set(0)
    onlne_streaming.set(0)
    type.set("")


window = tk.Tk()
window.title("Event Planner")
window.geometry("600x600")

title = tk.Label(window, text="Plan Your Event", font=("Arial", 20))
title.pack()

entry = tk.Entry(window)
entry.pack()

label = tk.Label(window, pady=50, text="Enter the Event Name")
label.pack()

planning = tk.Label(window, text="Select Prefrences: ")
planning.pack()

catering = tk.IntVar()
checkbox_catering = tk.Checkbutton(
    window, pady=10, text="Include Catering", variable=catering)
checkbox_catering.pack(anchor="w")

music = tk.IntVar()
checkbox_music = tk.Checkbutton(
    window, text="Provide music", pady=10, variable=music)
checkbox_music.pack(anchor="w")

online_streaming = tk.IntVar()
checkbox_online_streaming = tk.Checkbutton(
    window, text="Enable Online Streaming", pady=10, variable=online_streaming)
checkbox_online_streaming.pack(anchor="w")


event = tk.Label(window, text="Select Event Type: ")
event.pack()

vote = tk.StringVar()

tk.Radiobutton(window, text="Wedding", variable=vote,
               value="Wedding").pack(anchor="w")

tk.Radiobutton(window, text="Conference", variable=vote, value="Conference"
               ).pack(anchor="w")

tk.Radiobutton(window, text="Birthday Party", variable=vote, value="Birthday Party"
               ).pack(anchor="w")


guests = tk.Label(window, text="Number of Guests: ")
guests.pack()

scale = tk.Scale(window, from_=0, to=500, length=400,
                 orient="horizontal", tickinterval=50, highlightthickness=0)
scale.pack()

theme = tk.Label(window, text="Select Event Theme: ")
theme.pack()

listbox = tk.Listbox(window, width=25, height=8)
listbox.pack()
listbox.insert(1, "Modern")
listbox.insert(2, "Classic")
listbox.insert(3, "Rustic")
listbox.insert(4, "Futuristic")
listbox.select_set(0)

button_submit = tk.Button(window, text="Submit", font=(
    "Arial", 16), bg="Pink", command=show_message)
button_submit.pack()

button_reset = tk.Button(window, text="reset",
                         command=reset, font=("Arial", 16), bg="Blue")
button_reset.pack()

window.mainloop()
