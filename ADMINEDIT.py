from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Entry, Button, messagebox




root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title('LIBRARY')
root.configure(bg='#5C4033')
root.state('zoomed')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')
notebook.pack(fill='both', expand=True)

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn', background='#EEEBEB')
style.configure('lefttab.TNotebook.Tab', font=('Montserrat Medium', 15), width=14, background='#6F3434')
style.map("TNotebook.Tab", background=[("selected", '#F63A3A')])

# Replaced frame1 code
frame1 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
dashboard_icon = PhotoImage(file='dashboard.png')
notebook.add(frame1, text='Dashboard', image=dashboard_icon, compound=tk.LEFT)
box1 = tk.Frame(frame1, width=1100, height=674, bg="#FFFFFF")
box1.place(relx=0.43, rely=0.481, anchor="center")

ad= tk.Frame(frame1, width=1100, height=1000, bg='#5C4033')
ad.place(relx=0.43, rely=0.25, anchor='center')


top_rated = tk.Frame(frame1, width=2500, height=320, bg='#7f5112')
top_rated.place(relx=0.43, rely=0.71, anchor='center')

entry_title = Entry(ad)
entry_author = Entry(ad)
entry_genre = Entry(ad)

def open_add_book_form():
   
    global Add_book_box
    Add_book_box=tk.Toplevel()
    Add_book_box.title("ADD BOOK")
    Add_book_box.geometry(f"700x500")
    Add_book_box.resizable(False,False)
    Add_book_box.configure(bg="#FFFFFF")

    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()

    # Entry widgets for adding books
    label_title_add = Label(Add_book_box, text="ADD TITLE:", font=("Montserrat", 12))
    label_title_add.place(relx=0.3,rely=0.1)
    entry_title_add = tk.Entry(Add_book_box, width=30, font=("Montserrat", 12))
    entry_title_add.place(relx=0.3,rely=0.2)
    
    label_author_add = Label(Add_book_box, text="ADD AUTHOR:", font=("Montserrat", 12),)
    label_author_add.place(relx=0.3,rely=0.3)
    entry_author_add = tk.Entry(Add_book_box, width=30, font=("Montserrat", 12))
    entry_author_add.place(relx=0.3,rely=0.4)
    
    label_genre_add = Label(Add_book_box, text="GENRE:", font=("Montserrat", 12))
    label_genre_add.place(relx=0.3,rely=0.5)
    entry_genre_add = tk.Entry(Add_book_box, width=30, font=("Montserrat", 12))
    entry_genre_add.place(relx=0.3,rely=0.6)

    ADD_button = tk.Button(Add_book_box, text="ADD",fg='black',bg="#FFFFFF",font=("Monstserrat SemiBold",15),borderwidth=5)
    ADD_button.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    

# Replaced frame2 code
frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
manage_books_icon = PhotoImage(file='manage_books.png')
notebook.add(frame2, text="Manage books", image=manage_books_icon, compound=tk.LEFT)

add_book_button=tk.Button(frame2,text="ADD BOOKS",bg="#FFFFFF",command=open_add_book_form,width=15,height=10,font=("Montserrat SemiBold",9))
add_book_button.place(relx=0.1,rely=0.5,anchor="center")

notebook.place(relx=0)


frame3 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
manage_users_icon = PhotoImage(file='manage_users.png')
notebook.add(frame3, text="Manage users", image=manage_users_icon, compound=tk.LEFT)



def open_add_user_form():
   
    global Add_user_box
    Add_user_box=tk.Toplevel()
    Add_user_box.title("ADD BOOK")
    Add_user_box.geometry(f"700x500")
    Add_user_box.resizable(False,False)
    Add_user_box.configure(bg="#FFFFFF")

    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()

    # Entry widgets for adding users
    first_name = Label(Add_user_box, text='First name', font=('Montserrat black', 10), fg='#413F3F', bg='#FFFFFF')
    first_name.place(relx=0.1, rely=0.1)
    first_name_entry = Entry(Add_user_box, width=15, font=('Montserrat ', 16), bg='#fdfdfd')
    first_name_entry.place(relx=0.1, rely=0.15)

    second_name = Label(Add_user_box, text='Second name', font=('Montserrat black', 10), fg='#413F3F', bg='#FFFFFF')
    second_name.place(relx=0.5, rely=0.1)
    second_name_entry = Entry(Add_user_box, width=15, font=('Montserrat ', 16), bg='#fdfdfd')
    second_name_entry.place(relx=0.5,rely=0.15)
    
    email = Label(Add_user_box, text='Email', font=('Montserrat black', 10), fg='#413F3F', bg='#FFFFFF')
    email.place(relx=0.1, rely=0.25)
    email_entry = Entry(Add_user_box, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
    email_entry.place(relx=0.1, rely=0.3)

    user_id = Label(Add_user_box, text='USERID', font=('Montserrat black', 10), fg='#413F3F', bg='#FFFFFF')
    user_id.place(relx=0.1, rely=0.4)
    user_id_entry = Entry(Add_user_box, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
    user_id_entry.place(relx=0.1, rely=0.45)

    password = Label(Add_user_box, text='Password', font=('Montserrat black', 10), fg='#413F3F', bg='#FFFFFF')
    password.place(relx=0.1, rely=0.55)
    password_entry = Entry(Add_user_box, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
    password_entry.place(relx=0.1, rely=0.6)


    ADD_button = tk.Button(Add_user_box, text="ADD",fg='black',bg="#FFFFFF",font=("Monstserrat SemiBold",15),borderwidth=5)
    ADD_button.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

add_user_button=tk.Button(frame3,text="ADD USER",bg="#FFFFFF",command=open_add_user_form,width=15,height=10,font=("Montserrat SemiBold",9))
add_user_button.place(relx=0.1,rely=0.5,anchor="center")


notebook.place(relx=0)


frame4 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
borrowings_icon = PhotoImage(file='borrowings.png')
notebook.add(frame4, text="Borrowings", image=borrowings_icon, compound=tk.LEFT)
box4=tk.Frame(frame4,width=1100,height=674,bg="#FFFFFF")
box4.place(relx=0.43,rely=0.481,anchor="center")

frame5 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
profile_icon = PhotoImage(file='profile.png')
notebook.add(frame5, text="Profile", image=profile_icon, compound=tk.LEFT)
box5=tk.Frame(frame5,width=1100,height=674,bg="#FFFFFF")
box5.place(relx=0.43,rely=0.481,anchor="center")


root.mainloop()