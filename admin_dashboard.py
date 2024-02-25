from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title('Library')
root.configure(bg='#ffffff')
root.state('zoomed')
root.resizable(False, False)
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn', background='#EEEBEB')
style.configure('lefttab.TNotebook.Tab', font=('Montserrat Medium', 15), width=12, background='#6F3434')
style.map("TNotebook.Tab", background = [("selected", '#F63A3A')])

notebook = ttk.Notebook(root, style='lefttab.TNotebook')

frame1 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
dashboard_icon = PhotoImage(file='pics/dashboard.png')
notebook.add(frame1, text='Dashboard', image=dashboard_icon, compound=tk.LEFT)
box1=tk.Frame(frame1,width=1100,height=674,bg="#FFFFFF")
box1.place(relx=0.43,rely=0.481,anchor="center")

frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
manage_books_icon = PhotoImage(file='pics/manage_books.png')
notebook.add(frame2, text="Manage books", image=manage_books_icon, compound=tk.LEFT)
box2=tk.Frame(frame2,width=1100,height=674,bg="#FFFFFF")
box2.place(relx=0.43,rely=0.481,anchor="center")

frame3 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
manage_users_icon = PhotoImage(file='pics/manage_users.png')
notebook.add(frame3, text="Manage users", image=manage_users_icon, compound=tk.LEFT)
box3=tk.Frame(frame3,width=1100,height=674,bg="#FFFFFF")
box3.place(relx=0.43,rely=0.481,anchor="center")

def add_users():
    add_form = tk.Toplevel()
    add_form.title("Add users")
    add_form.geometry("500x600")
    add_form.resizable(False,False)
    add_form.transient(root)

    register = Label(add_form, text='ADD USER', font=('Montserrat Black', 30))
    register.place(relx=0.5, rely=0.15, anchor='center')

    first_name = Label(add_form, text='First name', font=('Montserrat', 10), fg='#413F3F')
    first_name.place(relx=0.125, rely=0.25)
    first_name_entry = Entry(add_form, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
    first_name_entry.place(relx=0.275, rely=0.32, anchor='center')

    second_name = Label(add_form, text='Second name', font=('Montserrat', 10), fg='#413F3F')
    second_name.place(relx=0.575, rely=0.25)
    second_name_entry = Entry(add_form, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
    second_name_entry.place(relx=0.725, rely=0.32, anchor='center')

    email = Label(add_form, text='Email', font=('Montserrat', 10), fg='#413F3F')
    email.place(relx=0.125, rely=0.37)
    email_entry = Entry(add_form, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
    email_entry.place(relx=0.5, rely=0.44, anchor='center')

    role = Label(add_form, text='Role', font=('Montserrat', 10), fg='#413F3F')
    role.place(relx=0.125, rely=0.49)
    clicked = tk.StringVar()

    role_menu = ttk.Combobox(add_form, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
    role_menu.place(relx=0.5, rely=0.56, anchor='center')

    def password_visibility():
        if password_entry.cget('show') == '':
            password_entry.config(show='*')
            show_hide.config(image=show_icon)
        else:
            password_entry.config(show='')
            show_hide.config(image=hide_icon)

    password = Label(add_form, text='Password', font=('Montserrat', 10), fg='#413F3F')
    password.place(relx=0.125, rely=0.61)
    password_entry = Entry(add_form, width=23, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
    password_entry.place(relx=0.46, rely=0.68, anchor='center')

    show_icon = PhotoImage(file='pics/show.png')
    hide_icon = PhotoImage(file='pics/hide.png')
    show_hide = Button(add_form,image=show_icon, width=25, command=password_visibility, fg='white', bg='#FFFFFF')
    show_hide.place(relx=0.83, rely=0.68, anchor='center')

    def confirm_password_visibility():
        if confirm_password_entry.cget('show') == '':
            confirm_password_entry.config(show='*')
            confirm_show_hide.config(confirm_show_hide.config(image=show_icon))
        else:
            confirm_password_entry.config(show='')
            confirm_show_hide.config(confirm_show_hide.config(image=hide_icon))

    confirm_password = Label(add_form, text='Confirm password', font=('Montserrat', 10), fg='#413F3F')
    confirm_password.place(relx=0.125, rely=0.73)
    confirm_password_entry = Entry(add_form, width=23, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
    confirm_password_entry.place(relx=0.46, rely=0.80, anchor='center')

    confirm_show_hide = Button(add_form,image=show_icon, width=25, command=confirm_password_visibility, fg='white', bg='#FFFFFF')
    confirm_show_hide.place(relx=0.83, rely=0.80, anchor='center')

    def create_account():
        first = first_name_entry.get()
        second = second_name_entry.get()
        email = email_entry.get()
        role = role_menu.get()
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
                        password="batsal1019",
                        database ="project"
                        )
                cursor= connection.cursor()

                query = "INSERT INTO users(`first_name`, `second_name`, `email`, `role`, `password`, `confirm_password`) VALUES (%s,%s,%s,%s,%s,%s)"
                data= (first, second, email, role, password, confirm_password)
                cursor.execute(query,data)

                connection.commit()
                MessageBox.showinfo("Done", "Account created successfully.")
                add_form.destroy()
            except Exception as e:
                MessageBox.showerror("Error",f"Error:{e}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        if validate_entries():
            add_to_database()

    login_button = Button(add_form, width=26, text='Add', font=('Montserrat', 10), command=create_account,fg='white', bg='black')
    login_button.place(relx=0.5, rely=0.90, anchor='center')


add = tk.Button(frame3, text="Add users", command=add_users)
add.place(relx=0.1, rely=0.5)

def edit_users():
    def fetch_data():
        user_id = user_id_entry.get()
        query = "SELECT * FROM users WHERE userid = %s"
        cursor.execute(query, (user_id,))
        data = cursor.fetchone()
        if data:
            first_name_entry.delete(0, tk.END)
            first_name_entry.insert(0, data[1])
            second_name_entry.delete(0, tk.END)
            second_name_entry.insert(0, data[2])
            email_entry.delete(0, tk.END)
            email_entry.insert(0, data[3])
            role_menu.set(data[4])
            password_entry.delete(0, tk.END)
            password_entry.insert(0, data[5])
        else:
            clear_entries()
            MessageBox.showerror("Error", "User ID not found")

    def update_data():
        user_id = user_id_entry.get()
        first_name = first_name_entry.get()
        second_name = second_name_entry.get()
        email = email_entry.get()
        role = role_menu.get()
        password = password_entry.get()
        query = "UPDATE users SET first_name = %s, second_name = %s, email = %s, Role = %s, password = %s WHERE userid = %s"
        try:
            cursor.execute(query, (first_name, second_name, email, role, password, user_id))
            db_connection.commit()
            MessageBox.showinfo("Success", "Data updated successfully")
        except Exception as e:
            MessageBox.showerror("Error", f"Error:{e}")

    def clear_entries():
        first_name_entry.delete(0, tk.END)
        second_name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        role_menu.set("")
        password_entry.delete(0, tk.END)

    db_connection = mysql.connect(
        host="localhost",
        user="root",
        password="batsal1019",
        database="project"
    )
    cursor = db_connection.cursor()

    edit_form = tk.Toplevel()
    edit_form.title("Edit user")
    edit_form.geometry("500x600")
    edit_form.resizable(False,False)
    edit_form.transient(root)

    title = Label(edit_form, text='EDIT USER', font=('Montserrat Black', 30))
    title.place(relx=0.5, rely=0.08, anchor='center')

    user_id = tk.Label(edit_form, text="User ID", font=('Montserrat', 10), fg='#413F3F')
    user_id.place(relx=0.125, rely=0.13)
    user_id_entry = tk.Entry(edit_form, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
    user_id_entry.place(relx=0.275, rely=0.2, anchor='center')

    first_name = Label(edit_form, text='First name', font=('Montserrat', 10), fg='#413F3F')
    first_name.place(relx=0.125, rely=0.25)
    first_name_entry = Entry(edit_form, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
    first_name_entry.place(relx=0.275, rely=0.32, anchor='center')

    second_name = Label(edit_form, text='Second name', font=('Montserrat', 10), fg='#413F3F')
    second_name.place(relx=0.575, rely=0.25)
    second_name_entry = Entry(edit_form, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
    second_name_entry.place(relx=0.725, rely=0.32, anchor='center')

    email = Label(edit_form, text='Email', font=('Montserrat', 10), fg='#413F3F')
    email.place(relx=0.125, rely=0.37)
    email_entry = Entry(edit_form, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
    email_entry.place(relx=0.5, rely=0.44, anchor='center')

    role = Label(edit_form, text='Role', font=('Montserrat', 10), fg='#413F3F')
    role.place(relx=0.125, rely=0.49)
    clicked = tk.StringVar()

    role_menu = ttk.Combobox(edit_form, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
    role_menu.place(relx=0.5, rely=0.56, anchor='center')

    password = Label(edit_form, text='Password', font=('Montserrat', 10), fg='#413F3F')
    password.place(relx=0.125, rely=0.61)
    password_entry = Entry(edit_form, width=23, font=('Montserrat Light', 16), bg='#fdfdfd', show='*')
    password_entry.place(relx=0.46, rely=0.68, anchor='center')

    button_fetch = tk.Button(edit_form, text="Fetch", font=('Montserrat', 10), command=fetch_data)
    button_fetch.place(relx=0.63, rely=0.2, anchor='center')

    button_update = tk.Button(edit_form, text="Update", font=('Montserrat', 10),  command=update_data)
    button_update.place(relx=0.5, rely=0.8, anchor='center')

    button_clear = tk.Button(edit_form, text="Clear", font=('Montserrat', 10), command=clear_entries)
    button_clear.place(relx=0.82, rely=0.2, anchor='center')

add = tk.Button(frame3, text="Edit user", command=edit_users)
add.place(relx=0.25, rely=0.5)

frame4 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
borrowings_icon = PhotoImage(file='pics/borrowings.png')
notebook.add(frame4, text="Borrowings", image=borrowings_icon, compound=tk.LEFT)
box4=tk.Frame(frame4,width=1100,height=674,bg="#FFFFFF")
box4.place(relx=0.43,rely=0.481,anchor="center")

frame5 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
profile_icon = PhotoImage(file='pics/profile.png')
notebook.add(frame5, text="Profile", image=profile_icon, compound=tk.LEFT)
box5=tk.Frame(frame5,width=1100,height=674,bg="#FFFFFF")
box5.place(relx=0.43,rely=0.481,anchor="center")

logo = tk.PhotoImage(file='pics/kitapp.png')
label = tk.Label(root, image=logo)
label.place(relx=0.005, rely=0.85)

notebook.place(relx=0)

root.mainloop()