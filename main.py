from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo =PhotoImage(file="logo.png")
canvas = Canvas(width=300, height=300)
canvas.create_image(150, 150, image=logo)
canvas.pack()

window.mainloop()