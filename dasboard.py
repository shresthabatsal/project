from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk

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

discover_icon = PhotoImage(file='discover_small.png')
favourite_icon = PhotoImage(file='favourite_small.png')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')

frame1 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightblue")
home_icon = PhotoImage(file='home_small.png')
notebook.add(frame1, text='Home', image=home_icon, compound=tk.LEFT)

ad = tk.Frame(frame1, width=1100, height=320, bg='#FFFFFF')
ad.place(relx=0.43, rely=0.25, anchor='center')

top_rated = tk.Frame(frame1, width=1100, height=320, bg='#FFFFFF')
top_rated.place(relx=0.43, rely=0.71, anchor='center')


frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightgreen")
discover_icon = PhotoImage(file='discover_small.png')
notebook.add(frame2, text="Discover", image=discover_icon, compound=tk.LEFT)


# frame3 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightcoral")
# favourite_icon = PhotoImage(file='favourite_small.png')
# notebook.add(frame3, text="Favourites", image=favourite_icon, compound=tk.LEFT)

# frame4 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightcoral")
# your_books_icon = PhotoImage(file='your_books_small.png')
# notebook.add(frame4, text="Your Books", image=your_books_icon, compound=tk.LEFT)

# # logo = tk.PhotoImage(file='kitapp_style.png')
# # label = tk.Label(root, image=logo)
# # label.place(relx=0.005, rely=0.85)

notebook.place(relx=0)

root.mainloop()