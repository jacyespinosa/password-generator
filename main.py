import random
from tkinter import messagebox
import pyperclip
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
    '''
    Ask user for their password preferences: length of letters, symbols and numbers.
    '''
    length_letters = ("How many letters would you like in your password?\n")
    length_symbols = ("How many symbols would you like?\n")
    length_numbers = ("How many numbers would you like?\n")

    letter_input = simpledialog.askstring(title="Letters Length", prompt=f"{length_letters}\n")
    symbol_input = simpledialog.askstring(title="Symbols Length", prompt=f"{length_symbols}\n")
    number_input = simpledialog.askstring(title="Numbers Length", prompt=f"{length_numbers}\n")

    '''
    List comprehension using the user's input (length of letters, symbols and numbers) to generate random letters,
    symbols and numbers.
    '''
    password_letters = [random.choice(letters) for i in range(int(letter_input))]
    password_symbols = [random.choice(symbols) for i in range(int(symbol_input))]
    password_numbers = [random.choice(numbers) for i in range(int(number_input))]

    '''
    Concatenate the result of the randomization and shuffle the three variables (password_letters, password_symbols and
    password_numbers) to further strengthen the user's password.
    After shuffling the letters, remove the "," to join the characters together and save the result in the password
    variable.
    The generated password will be displayed on the PASSWORD_ENTRY field.
    '''
    word = password_letters + password_symbols + password_numbers
    random.shuffle(word)
    password = (''.join(word))
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
'''
This function will save the generated password into a separate .txt file ('data.txt'). This is where the user can access
their password data whenever they need to log in.
'''
def add_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showwarning(title="Warning!", message="Website information must be filled out!")

    elif len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Password information must be filled out!")

    else:
        save = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} "
                                                     f"\nPassword: {password}"
                                                     f"\nIs it okay to save?")
    if save:
        with open("data.txt", "a") as file:
            file.write(f"{website}   |  {email_username}   |  {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
email_username_entry.insert(END, string="ENTER YOUR DEFAULT EMAIL ADDRESS")
email_username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text="Password:", fg="black", bg="white", font=("Arial", 15))
password_label.grid(column=1, row=4)

password_entry = Entry(width=21, bg="white", fg="black", highlightthickness=0)
password_entry.grid(column=2, row=4)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=2, row=5, columnspan=2)


window.mainloop()