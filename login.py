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
root.configure(bg='#ADD8E6')
root.state('zoomed')
root.resizable(False, False)


def login():
    email = email_entry.get()
    password = password_entry.get()

    try:
        connection = mysql.connect(
            host="localhost",
            user="root",
            password="batsal1019",
            database="project"
        )
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            stored_password = user[6]
            if password == stored_password:
                MessageBox.showinfo("Success", "Login successful!")
                root.destroy()
                import user_dashboard
                user_dashboard.open_register_window()
            else:
                MessageBox.showerror("Error", "Incorrect password!")
        else:
            MessageBox.showerror("Error", "User not found!")

    except Exception as e:
        MessageBox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


box = tk.Frame(root, width=500, height=600, bg='#FFFFFF')
box.place(relx=0.5, rely=0.5, anchor='center')

welcome = Label(box, text='WELCOME', font=('Montserrat Black', 30), bg='#FFFFFF')
welcome.place(relx=0.5, rely=0.15, anchor='center')

email = Label(box, text='Email', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
email.place(relx=0.125, rely=0.25)
email_entry = Entry(box, width=26, font=('Montserrat Light', 16), bg='#FFFFFF')
email_entry.place(relx=0.5, rely=0.32, anchor='center')

def password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_hide.config(image=show_icon)
    else:
        password_entry.config(show='')
        show_hide.config(image=hide_icon)
        

password = Label(box, text='Password', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
password.place(relx=0.125, rely=0.37)
password_entry = Entry(box, width=23, font=('Montserrat Light', 16), bg='#FFFFFF', show='*')
password_entry.place(relx=0.46, rely=0.44, anchor='center')

show_icon = PhotoImage(file='show_small.png')
hide_icon = PhotoImage(file='hide_small.png')
show_hide = Button(box,image=show_icon, width=25, command=password_visibility, bg='#FFFFFF')
show_hide.place(relx=0.83, rely=0.44, anchor='center')

role = Label(box, text='Role', font=('Montserrat', 10), fg='#413F3F', bg='#FFFFFF')
role.place(relx=0.125, rely=0.49)
clicked = tk.StringVar()

role_menu = ttk.Combobox(box, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
role_menu.place(relx=0.5, rely=0.56, anchor='center')

def open_register():
    root.destroy()
    import register
    register.open_register_window()

def open_dashboard():
    root.destroy()
    #import dashboard
    #dashboard.open_register_window()

login_button = Button(box, width=26, text='Login', font=('Montserrat', 10), command=login, fg='#FFFFFF', bg='black')
login_button.place(relx=0.5, rely=0.7, anchor='center')

sign_up = Label(box, text="Don't have an account?", font=('Montserrat', 10, 'italic'), fg='#413F3F', bg='#FFFFFF')
sign_up.place(relx=0.4, rely=0.75, anchor='center')

register_button = Button(box, text='Create one.', command=open_register, font=('Montserrat', 10, 'bold'), fg='black', bg='#FFFFFF')
register_button.place(relx=0.65, rely=0.75, anchor='center')

# logo = tk.PhotoImage(file='kitapp_style.png')
# label = tk.Label(root, image=logo, bg='#ADD8E6')
# label.place(relx=0.005, rely=0.85)

root.mainloop()
