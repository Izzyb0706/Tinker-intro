import tkinter as tk
# radio buttons


def record_vote():
    label_vote.config(text=f"you voted for {vote.get()}")


base_font = ("comic sans", 20, "bold", "italic")
back = "#0ABAB5"
window = tk.Tk()
window.geometry("3440x1440")
window.configure(bg=back)
window.title("class prez")

label_vote = tk.Label(
    text="Make a selection for class prez", font=base_font, bg=back)
label_vote.pack()
vote = tk.StringVar(value="Dakota")

tk.Radiobutton(window, text="James", variable=vote,
               value="James Clark", font=base_font, bg=back).pack()
tk.Radiobutton(window, text="Coby", variable=vote,
               value="Coby Hughes", font=base_font, bg=back).pack()
tk.Radiobutton(window, text="Kerry", variable=vote,
               value="Kerry Sowers", font=base_font, bg=back).pack()


submit_btn = tk.Button(window, text=("submit"),
                       command=record_vote, font=base_font, bg=back).pack()
window.mainloop()
