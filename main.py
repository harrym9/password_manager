from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(102, 102, image=logo)
canvas.grid(column=1, row=0)

# Labels
service_label = Label(text="Service/Website:")
service_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entry's
service_entry = Entry(width=51)
service_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate password", width=14)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add password", width=43)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
