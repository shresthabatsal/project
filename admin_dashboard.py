from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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