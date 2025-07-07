from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    Email_len=len(email_entry.get())
    Password_len = len(password_entry.get())

    new_data={
        website_entry.get():{
            "Email":email_entry.get(),
            "Password":password_entry.get()
        }
    }
    if Email_len==0 or Password_len==0:
        messagebox.showinfo(title="Oops",message="Do not leave any fields empty!")
    else:
        try:
            with open("data.json",mode="r") as data_file:
                #Reading old data
                data=json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json",mode="w") as data_file:
                #Writing New data
                # updating old data
                data.update(new_data)
                json.dump(data, data_file ,indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- Find Password  ------------------------------- #

def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # To store any image in a variable
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

#LABELS
Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)

Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

#Buttons
generate_pass=Button(text="Generate Password",command=generate_password)
generate_pass.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)

#Enrty
website_entry=Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()
password_entry=Entry(width=18)
password_entry.grid(column=1, row=3)
email_entry=Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "inderkukreja2@gmail.com")












window.mainloop()
