# checkboxes
import tkinter as tk

window = tk.Tk()
window.title("Mac and Cheese Survey")
window.geometry("500x500")


def grade_submission():
    kraft = check_Kraft.get()
    Velveta = check_Velveta.get()
    if kraft == 1 and Velveta == 0:
        label_outcome.config(text="you are 100% correct")
    elif kraft == 0 and Velveta == 1:
        label_outcome.config(text="nice!")
    else:
        label_outcome.config(text="your partially correct")


# variable to hold the state of the checkbox
check_Kraft = tk.IntVar()

checkbox_kraft = tk.Checkbutton(
    window, text="Kraft Mac and Cheese is good", variable=check_Kraft)
checkbox_kraft.pack()
check_Velveta = tk.IntVar()

checkbox_velveta = tk.Checkbutton(
    window, text="Velveta is good", variable=check_Velveta)
checkbox_velveta.pack()

button_submit = tk.Button(window, text="submit", command=grade_submission)

button_submit.pack()


label_outcome = tk.Label(window, text="Please submit your response")
label_outcome.pack()


window.mainloop()
