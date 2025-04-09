import tkinter as tk
from tkinter import *


# Title position
x0_title, y0_title = 85, 25

# Email entry position
x0_email, y0_email = 130, 150

# Password entry position
x0_pwd, y0_pwd = 130, 250

# Login button position
x0_btn_login, y0_btn_login = 130, 450

# Register button position
x0_btn_register, y0_btn_register = 130, 520

# Creating the window
win = tk.Tk()
win.title("Login / Register avec place")
win.geometry("400x700")
win.resizable(False, False)

# Title
label_title = Label(text="Login", width=10, height=1, font=("Arial", 30), bg="#FFFFFF", fg="#000000")
label_title.place(x=x0_title, y=y0_title)

# Email entry
email_label = Label(win, text="Enter your email", width=15, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
email_label.place(x=x0_email-30, y=y0_email)
email_entry = tk.Entry(win, width=40)
email_entry.place(x=x0_email-60, y=y0_email + 35)

# Password entry
password_label = Label(win, text="Enter your password", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
password_label.place(x=x0_pwd-52, y=y0_pwd)
password_entry = tk.Entry(win, width=40)
password_entry.place(x=x0_pwd-60, y=y0_pwd + 35)

# Button to log in
btn_login = tk.Button(win, text="Log in", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_login.place(x=x0_btn_login, y=y0_btn_login)

# Button to register
btn_register = tk.Button(win, text="Register", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_register.place(x=x0_btn_register, y=y0_btn_register)

win.mainloop()
