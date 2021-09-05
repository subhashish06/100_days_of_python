"""
Program: Password Generator GUI
Author: Subhashish Dhar
Date: 04/09/2021
"""

import random
import json
from tkinter import Tk, Canvas, Label, Entry, PhotoImage, Button, END
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    """generate the password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_in_password = random.sample(letters, random.randint(8, 10))
    symbols_in_password = random.sample(symbols, random.randint(2, 4))
    numbers_in_password = random.sample(numbers, random.randint(2, 4))

    final_list = letters_in_password + symbols_in_password + numbers_in_password

    random.shuffle(final_list)
    password = ''.join(final_list)

    if website_entry.get() != '' and username_entry.get() != 0:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    else:
        messagebox.showinfo(title='Data Missing', message="Please provide website and username "
                                                          "before generating password")


# ---------------------------- COPY PASSWORD ------------------------------- #
def copy():
    """copies the password to clipboard"""
    if password_entry.get() != '':
        pyperclip.copy(password_entry.get())


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    """searches the credentials in database"""
    try:
        with open("data_file.json", "r", encoding='utf-8') as file_handler:
            saved_data = json.load(file_handler)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        search_key = website_entry.get().title()
        if search_key in saved_data:
            username_searched = saved_data[search_key]['username']
            password_searched = saved_data[search_key]['password']
            messagebox.showinfo(title=search_key,
                                message=f"Username : {username_searched}\n"
                                        f"Password : {password_searched}")
        else:
            messagebox.showinfo(title="Error", message=f"No password saved for {search_key}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """saves credentials to the database"""
    web = website_entry.get().title()
    user = username_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "username": user,
            "password": password
        }
    }
    if web == '' or password == '' or user == '':
        messagebox.showinfo(title='Data Missing', message="Please don't leave any entries empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"Email: {user}\n"
                                                          f"Password: {password}\nOK to save?")
        if is_ok:
            try:
                with open('data_file.json', 'r', encoding='utf-8') as file_handler:
                    data = json.load(file_handler)
            except FileNotFoundError:
                with open('data_file.json', 'w', encoding='utf-8') as file_handler:
                    json.dump(new_data, file_handler, indent=4)
            else:
                with open('data_file.json', 'w', encoding='utf-8') as file_handler:
                    data.update(new_data)
                    json.dump(data, file_handler, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
username_entry = Entry(width=49)
username_entry.grid(row=2, column=1, columnspan=3)
username_entry.insert(0, 'sdhar@example.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate', command=generate)
generate_button.grid(row=3, column=3)

copy_button = Button(text='Copy', command=copy)
copy_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=3)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=3)

window.mainloop()
