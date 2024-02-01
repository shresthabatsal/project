from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title('Library')
root.configure(bg='#EEEBEB')
root.state('zoomed')
root.resizable(False, False)

box = tk.Frame(root, width=500, height=600, bg='#FFFFFF')
box.place(relx=0.5, rely=0.5, anchor='center')

register = Label(root, text='REGISTER', font=('Montserrat Black', 30), bg='#FFFFFF')
register.place(relx=0.5, rely=0.15, anchor='center')

first_name = Label(root, text='First name', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
first_name.place(relx=0.365, rely=0.25)
first_name_entry = Entry(root, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
first_name_entry.place(relx=0.419, rely=0.3, anchor='center')

second_name = Label(root, text='Second name', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
second_name.place(relx=0.525, rely=0.25)
second_name_entry = Entry(root, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
second_name_entry.place(relx=0.58,rely=0.3, anchor='center')

email = Label(root, text='Email', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
email.place(relx=0.365, rely=0.35)
email_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
email_entry.place(relx=0.5, rely=0.4, anchor='center')

role = Label(root, text='Role', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
role.place(relx=0.365, rely=0.45)
clicked = tk.StringVar()

role_menu = ttk.Combobox(root, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
role_menu.place(relx=0.5, rely=0.5, anchor='center')

def password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_hide.config(image=show_icon)
    else:
        password_entry.config(show='')
        show_hide.config(image=hide_icon)

password = Label(root, text='Password', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
password.place(relx=0.365, rely=0.55)
password_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
password_entry.place(relx=0.5, rely=0.6, anchor='center')

show_icon = PhotoImage(file='show_small.png')
hide_icon = PhotoImage(file='hide_small.png')
show_hide = Button(root,image=show_icon, width=25, command=password_visibility, fg='white', bg='#FFFFFF')
show_hide.place(relx=0.622, rely=0.6, anchor='center')

def confirm_password_visibility():
    if confirm_password_entry.cget('show') == '':
        confirm_password_entry.config(show='*')
        confirm_show_hide.config(confirm_show_hide.config(image=show_icon))
    else:
        confirm_password_entry.config(show='')
        confirm_show_hide.config(confirm_show_hide.config(image=hide_icon))

confirm_password = Label(root, text='Confirm password', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
confirm_password.place(relx=0.365, rely=0.65)
confirm_password_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
confirm_password_entry.place(relx=0.5, rely=0.7, anchor='center')

confirm_show_hide = Button(root,image=show_icon, width=25, command=confirm_password_visibility, fg='white', bg='#FFFFFF')
confirm_show_hide.place(relx=0.622, rely=0.7, anchor='center')

def open_login():
    root.destroy()
    import login
    login.open_register_window()

login_button = Button(root, width=26, text='Create my account', font=('Montserrat', 10), command=open_login, fg='#FFFFFF', bg='black')
login_button.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()
