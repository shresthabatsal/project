from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk

root = Tk()
root.geometry('1920x1080')
root.title('Liqour')
root.configure(bg='#EEEBEB')
root.state('zoomed')

box = tk.Frame(root, width=500, height=600, bg='#FFFFFF')
box.place(relx=0.5, rely=0.5, anchor='center')

welcome = Label(root, text='WELCOME', font=('Montserrat Black', 30), bg='#FFFFFF')
welcome.place(relx=0.5, y=150, anchor='center')

email = Label(box, text='Email', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
email.place(relx=0.125, y=170)
email_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
email_entry.place(relx=0.5, y=260, anchor='center')

def password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        hide_button.config(text='Show', font=('Montserrat Light', 10))
    else:
        password_entry.config(show='')
        hide_button.config(text='Hide', font=('Montserrat Light', 10))

password = Label(box, text='Password', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
password.place(relx=0.125, y=270)
password_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
password_entry.place(relx=0.5, y=360, anchor='center')

hide_button = tk.Button(root, text='Show', font=('Montserrat Light', 10), height=1, width= 4, command = password_visibility, bg='#FFFFFF')
hide_button.place(relx=0.603, y=345)

role = Label(box, text='Role', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
role.place(relx=0.125, y=370)
clicked = tk.StringVar()

role_menu = ttk.Combobox(root, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
role_menu.place(relx=0.5, y=460, anchor='center')

def open_register():
    import register
    register.open_register_window()

login_button = Button(root, width=26, text='Login', font=('Montserrat', 12), fg='#FFFFFF', bg='black')
login_button.place(relx=0.5, y=560, anchor='center')

sign_up = Label(root, text="Don't have an accout?", font=('Montserrat', 10, 'italic'), fg='#413F3F', bg='#FFFFFF')
sign_up.place(relx=0.47, y=600, anchor='center')
create_one = Label(root, text="Create one.", font=('Montserrat', 10, 'bold'), fg='#413F3F', bg='#FFFFFF')
create_one.place(relx=0.555, y=600, anchor='center')

register_button = Button(root, text='Create one.', command=open_register, font=('Montserrat', 10, 'bold'), fg='black', bg='#FFFFFF')
register_button.place(relx=0.557, y=600, anchor='center')

root.mainloop()