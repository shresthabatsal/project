from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
import re

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title('Library')
root.configure(bg='#ADD8E6')
root.state('zoomed')
root.resizable(False, False)

def create_account():
    first = first_name_entry.get()
    second = second_name_entry.get()
    email = email_entry.get()
    role = 'User'
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    def validate_entries():
        if not email or not password or not confirm_password:
            MessageBox.showerror('Error', 'Please fill all the fields.')
            return False
        elif not is_valid_email(email):
            MessageBox.showerror('Error', 'Invalid email address.')
            return False
        elif password != confirm_password:
            MessageBox.showerror('Error', 'Passwords do not match.')
            return False
        else:
            return True

    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email)

    def add_to_database():
        try:
            connection = mysql.connect(
                host="localhost",
                    user="root",
                    password="",
                    database ="project"
                    )
            cursor= connection.cursor()

            query = "INSERT INTO users(`first_name`, `second_name`, `email`, `role`, `password`, `confirm_password`) VALUES (%s,%s,%s,%s,%s,%s)"
            data= (first, second, email, role, password, confirm_password)
            cursor.execute(query,data)

            connection.commit()
            MessageBox.showinfo("Done", "Account created successfully.")
            root.destroy()
            import login
            login.open_register_window()
        except Exception as e:
            MessageBox.showerror("Error",f"Error:{e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    if validate_entries():
        add_to_database()


box = tk.Frame(root, width=500, height=600, bg='#FFFFFF')
box.place(relx=0.5, rely=0.5, anchor='center')

register = Label(box, text='REGISTER', font=('Montserrat Black', 30), bg='#FFFFFF')
register.place(relx=0.5, rely=0.15, anchor='center')

first_name = Label(box, text='First name', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
first_name.place(relx=0.125, rely=0.25)
first_name_entry = Entry(box, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
first_name_entry.place(relx=0.275, rely=0.32, anchor='center')

second_name = Label(box, text='Second name', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
second_name.place(relx=0.575, rely=0.25)
second_name_entry = Entry(box, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
second_name_entry.place(relx=0.725, rely=0.32, anchor='center')

email = Label(box, text='Email', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
email.place(relx=0.125, rely=0.37)
email_entry = Entry(box, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
email_entry.place(relx=0.5, rely=0.44, anchor='center')

def password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_hide.config(image=show_icon)
    else:
        password_entry.config(show='')
        show_hide.config(image=hide_icon)

password = Label(box, text='Password', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
password.place(relx=0.125, rely=0.49)
password_entry = Entry(box, width=23, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
password_entry.place(relx=0.46, rely=0.56, anchor='center')

show_icon = PhotoImage(file='pics/show.png')
hide_icon = PhotoImage(file='pics/hide.png')
show_hide = Button(box,image=show_icon, width=25, command=password_visibility, fg='white', bg='#FFFFFF')
show_hide.place(relx=0.83, rely=0.56, anchor='center')

def confirm_password_visibility():
    if confirm_password_entry.cget('show') == '':
        confirm_password_entry.config(show='*')
        confirm_show_hide.config(confirm_show_hide.config(image=show_icon))
    else:
        confirm_password_entry.config(show='')
        confirm_show_hide.config(confirm_show_hide.config(image=hide_icon))

confirm_password = Label(box, text='Confirm password', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
confirm_password.place(relx=0.125, rely=0.61)
confirm_password_entry = Entry(box, width=23, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
confirm_password_entry.place(relx=0.46, rely=0.68, anchor='center')

confirm_show_hide = Button(box,image=show_icon, width=25, command=confirm_password_visibility, fg='white', bg='#FFFFFF')
confirm_show_hide.place(relx=0.83, rely=0.68, anchor='center')

def open_login():
    root.destroy()
    import login
    login.open_register_window()

login_button = Button(box, width=26, text='Create my account', font=('Montserrat', 10), command=create_account, fg='#FFFFFF', bg='black')
login_button.place(relx=0.5, rely=0.83, anchor='center')

sign_up = Label(box, text="Already have an account?", font=('Montserrat', 10, 'italic'), fg='#413F3F', bg='#FFFFFF')
sign_up.place(relx=0.45, rely=0.88, anchor='center')

register_button = Button(box, text='Login', command=open_login, font=('Montserrat', 10, 'bold'), fg='black', bg='#FFFFFF')
register_button.place(relx=0.68, rely=0.88, anchor='center')

logo = tk.PhotoImage(file='pics/kitapp.png')
label = tk.Label(root, image=logo, bg='#ADD8E6')
label.place(relx=0.005, rely=0.85)

root.mainloop()
