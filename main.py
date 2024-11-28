from symbol import with_item
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()


    with open("credential.txt", "a") as credential:
        credential.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column=1)

#labels
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label= Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
#Entrie
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "idy.ndoye@gmail.com")
password_entry = Entry(width=16)
password_entry.grid(row=3, column=1)
#Button
generate_password_button = Button(text="Generate Password", width=15)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)












window.mainloop()