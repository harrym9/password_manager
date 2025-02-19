from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    service_name = service.get()
    email_name = email.get()
    pass_code = password.get()

    if service_name == "":
        messagebox.showinfo(title="Oops", message="Please fill service / website")
    elif pass_code == "":
        messagebox.showinfo(title="Oops", message="Please fill password")
    elif email_name == "":
        messagebox.showinfo(title="Oops", message="Please fill email")
    else:
        is_ok = messagebox.askokcancel(title=service_name, message=f"There are details:"
                                                                   f"\n Email / Username: {email_name}\n Password: {pass_code}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{service_name.title()} | {email_name.lower()} | {pass_code}\n")
                # clear the entries
                service.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=220)
canvas.create_image(102, 102, image=logo)
canvas.grid(column=1, row=0)

# Labels
service_label = Label(text="Service/Website:")
service_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
service = service_entry = Entry(width=51)
service_entry.grid(row=1, column=1, columnspan=2)
service.focus()
email = email_entry = Entry(width=51)

# You can change the default email with your own email :D or fully delete this line
email.insert(0, "gayratrahmatulayev8@gmail.com")

email_entry.grid(row=2, column=1, columnspan=2)
password = password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate password", width=14)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add password", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
