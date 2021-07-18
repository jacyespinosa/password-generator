from tkinter import *
from tkinter import simpledialog


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

word = ''


def generate_password():
    length_letters = ("How many letters would you like in your password?\n")
    length_symbols = ("How many symbols would you like?\n")
    length_numbers = ("How many numbers would you like?\n")

    letter_input = simpledialog.askstring(title="Letters Length", prompt=f"{length_letters}\n")
    symbol_input = simpledialog.askstring(title="Symbols Length", prompt=f"{length_symbols}\n")
    number_input = simpledialog.askstring(title="Numbers Length", prompt=f"{length_numbers}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_photo)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:", fg="black", bg="white", font=("Arial", 15))
website_label.grid(column=1, row=2)

website_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan= 2)

email_username_label = Label(text="Email/Username:", fg="black", bg="white", font=("Arial", 15))
email_username_label.grid(column=1, row=3)

email_username_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0)
email_username_entry.insert(END)
email_username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text="Password:", fg="black", bg="white", font=("Arial", 15))
password_label.grid(column=1, row=4)

password_entry = Entry(width=21, bg="white", fg="black", highlightthickness=0)
password_entry.grid(column=2, row=4)

generate_button = Button(text="Generate Password", command="")
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=36, command="")
add_button.grid(column=2, row=5, columnspan=2)


window.mainloop()