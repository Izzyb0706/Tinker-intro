import tkinter as tk


def submit():
    name = entry2.get()
    ssn = entry.get()
    print(f"We got {name}'s ssn! {ssn}")


default_font = font = ("Arial", 16, "bold")

# Create window
window = tk.Tk()
window.title("Social Security Scam App")
window.geometry("500x500")  # width x height
icon = tk.PhotoImage(file=r"./resources/imposter.png")
window.iconphoto(True, icon)

label = tk.Label(window,
                 text="Enter your social security number",
                 font=default_font,
                 )


label.pack()

entry = tk.Entry(window, font=default_font,
                 width=11)
entry2 = tk.Entry(window,
                  font=default_font,
                  width=11,
                  )

entry2.pack()

entry = tk.Entry(window,
                 font=default_font,
                 width=11,
                 )
entry.pack()

# set default text
entry.insert(0, "555-55-5555")

submit_btn = tk.Button(
    window, text="Sumbit for research purposes", command=submit)
submit_btn.pack()

window.mainloop()
