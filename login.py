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

welcome = Label(root, text='WELCOME', font=('Montserrat Black', 30), bg='#FFFFFF')
welcome.place(relx=0.5, rely=0.2, anchor='center')

email = Label(root, text='Email', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
email.place(relx=0.365, rely=0.3)
email_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
email_entry.place(relx=0.5, rely=0.35, anchor='center')

def password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_hide.config(image=show_icon)
    else:
        password_entry.config(show='')
        show_hide.config(image=hide_icon)
        

password = Label(root, text='Password', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
password.place(relx=0.365, rely=0.4)
password_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
password_entry.place(relx=0.5, rely=0.45, anchor='center')

show_icon = PhotoImage(file='show_small.png')
hide_icon = PhotoImage(file='hide_small.png')
show_hide = Button(root,image=show_icon, width=25, command=password_visibility, fg='white', bg='#FFFFFF')
show_hide.place(relx=0.622, rely=0.45, anchor='center')

role = Label(box, text='Role', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
role.place(relx=0.125, rely=0.5)
clicked = tk.StringVar()

role_menu = ttk.Combobox(root, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
role_menu.place(relx=0.5, rely=0.55, anchor='center')

def open_register():
    root.destroy()
    import register
    register.open_register_window()

def open_dashboard():
    root.destroy()
    #import dashboard
    #dashboard.open_register_window()

login_button = Button(root, width=26, text='Login', font=('Montserrat', 10), command=open_dashboard, fg='#FFFFFF', bg='black')
login_button.place(relx=0.5, rely=0.7, anchor='center')

sign_up = Label(root, text="Don't have an accout?", font=('Montserrat', 10, 'italic'), fg='#413F3F', bg='#FFFFFF')
sign_up.place(relx=0.47, rely=0.75, anchor='center')

register_button = Button(root, text='Create one.', command=open_register, font=('Montserrat', 10, 'bold'), fg='black', bg='#FFFFFF')
register_button.place(relx=0.557, rely=0.75, anchor='center')

root.mainloop()
