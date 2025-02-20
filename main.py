from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip, json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_p = [choice(letters) for _ in range(randint(8, 10))]
    numbers_p = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_p = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_p + numbers_p + symbols_p
    shuffle(password_list)
    final_password = "".join(password_list)

    # clear entry and put the final password
    password.delete(0, END)
    password.insert(0, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    service_name = service.get()
    email_name = email.get()
    pass_code = password.get()
    new_data = {
        service_name: {
            "email": email_name,
            "password": pass_code,
        }
    }

    if service_name == "":
        messagebox.showinfo(title="Oops", message="Please fill service / website")
    elif pass_code == "":
        messagebox.showinfo(title="Oops", message="Please fill password")
    elif email_name == "":
        messagebox.showinfo(title="Oops", message="Please fill email")
    else:
        is_ok = messagebox.askokcancel(title=service_name, message=f"There are details:"f"\n "
                                                                   f"Email / Username: {email_name}\n "
                                                                   f"Password: {pass_code}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
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
generate_button = Button(text="Generate password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add password", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
