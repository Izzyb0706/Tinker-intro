import tkinter as tk

window = tk.Tk()
window.title("Mario Characters")
window.geometry("400x400")

listbox = tk.Listbox(window, width=25, height=8)
listbox.pack()


def remove_selected():
    for_del = listbox.get(tk.ACTIVE)
    if for_del:
        listbox.delete(tk.ACTIVE)  # Needs to be an index
        print(f"deleted {for_del}")
        print(f"current active: {listbox.get(tk.ACTIVE)}")


def add_character():
    item = entry.get().strip()
    if item and not item in listbox.get(0, tk.END):
        listbox.insert(tk.END, item)


listbox.insert(1, "Mario")
listbox.insert(2, "Luigi")
listbox.insert(3, "Princess Peach")
print(f"current active: {listbox.get(tk.ACTIVE)}")
listbox.select_set(0)

label = tk.Label(text="Enter a character to add: ")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Add Character", command=add_character)
button.pack()

button_del = tk.Button(window, text="Remove Selected", command=remove_selected)
button.pack()
button_del.pack()

window.mainloop()
