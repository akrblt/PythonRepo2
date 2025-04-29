import tkinter as tk
from tkinter import *

# Creating the window
win = tk.Tk()
win.title("Login / Register avec pack")
win.geometry("400x700")
win.resizable(False, False)
win.configure(bg="#FFFFFF")

# Spacer for facility
def add_spacer(height):
    spacer = Label(win, text="", bg="#FFFFFF", height=height)
    spacer.pack()

# Title
label_title = Label(win, text="Login", font=("Arial", 50), bg="#FFFFFF", fg="#000000")
add_spacer(2)
label_title.pack(pady=10)

#add_spacer(2)
#label_title.pack(pady=10)

# Email label and entry
email_label = Label(win, text="Enter your email", font=("Arial", 20), bg="#FFFFFF", fg="#000000")
# configurer le font
email_label.pack(pady=(30, 5))

email_entry = Entry(win, width=40)
email_entry.pack()

# Password label and entry
password_label = Label(win, text="Enter your password", font=("Arial", 15), bg="#FFFFFF", fg="#000000")
password_label.pack(pady=(30, 5))

password_entry = Entry(win, width=40, show="*")  # caché le chiffre="*"
password_entry.pack()

# Login button
add_spacer(4)
btn_login = Button(win, text="Log in", width=15, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_login.pack(pady=10)

# Register button
btn_register = Button(win, text="Register", width=15, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_register.pack(pady=10)

win.mainloop()
