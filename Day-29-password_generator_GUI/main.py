from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_entry.get()
    user = username_entry.get()
    pw = password_entry.get()
    if web == '' or pw == '' or user == '':
        messagebox.showinfo(title='Data Missing', message="Please don't leave any entries empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"Email: {user}\nPassword: {pw}\nOK to save?")
        if is_ok:
            with open('data_file.txt', 'a') as f:
                f.write(f"{web} | {user} | {pw}\n")
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
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'sdhar@example.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate Password')
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
