#Day 84: GUI using Tkinter


#Build a calculator app with a GUI using Tkinter.

import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        tk.Button(root, text=char, font=("Arial", 18), width=5, height=2,
                  command=lambda ch=char: on_click(ch)).grid(row=r+1, column=c)

root.mainloop()
