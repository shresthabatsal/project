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

box = tk.Frame(root, width=500, height=2000, bg='#FFFFFF')
box.place(relx=0, rely=0, anchor='center')

ad = tk.Frame(root, width=1000, height=310, bg='#FFFFFF')
ad.place(relx=0.59, rely=0.3, anchor='center')

top_rated = tk.Frame(root, width=1000, height=310, bg='#FFFFFF')
top_rated.place(relx=0.59, rely=0.8, anchor='center')

home_icon = PhotoImage(file='home_small.png')
home = Button(root, text='     Home  ',image=home_icon, compound=tk.LEFT, anchor='w', padx=5, font=('Montserrat Medium', 12), width=235, fg='black', bg='#FFFFFF')
home.place(relx=0.091, rely=0.2, anchor='center')

discover_icon = PhotoImage(file='discover_small.png')
discover = Button(root, text='     Discover  ',image=discover_icon, compound=tk.LEFT, anchor='w', padx=5, font=('Montserrat Medium', 12), width=235, fg='black', bg='#FFFFFF')
discover.place(relx=0.091, rely=0.25, anchor='center')

favourite_icon = PhotoImage(file='favourite_small.png')
favourite = Button(root, text='     Favourite  ',image=favourite_icon, compound=tk.LEFT, anchor='w', padx=5, font=('Montserrat Medium', 12), width=235, fg='black', bg='#FFFFFF')
favourite.place(relx=0.091, rely=0.3, anchor='center')

your_books_icon = PhotoImage(file='your_books_small.png')
your_books = Button(root, text='     Your Books  ',image=your_books_icon, compound=tk.LEFT, anchor='w', padx=5, font=('Montserrat Medium', 12), width=235, fg='black', bg='#FFFFFF')
your_books.place(relx=0.091, rely=0.35, anchor='center')

history_icon = PhotoImage(file='history_small.png')
history = Button(root, text='     History  ',image=favourite_icon, compound=tk.LEFT, anchor='w', padx=5, font=('Montserrat Medium', 12), width=235, fg='black', bg='#FFFFFF')
history.place(relx=0.091, rely=0.4, anchor='center')

root.mainloop()