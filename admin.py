from tkinter import*
import tkinter.messagebox as messagebox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title('LIBRARY')
root.configure(bg='#5C4033')
root.state('zoomed')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')
notebook.pack(fill='both', expand=True)

style=ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn', background='#EEEBEB')
style.configure('lefttab.TNotebook.Tab', font=('Montserrat Medium', 15), width=12, background='#6F3434')
style.map("TNotebook.Tab", background = [("selected", '#F63A3A')])

frame1 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightblue")
notebook.add(frame1, text='ADMIN PAGE ', compound=tk.RIGHT)

ad = tk.Frame(frame1, width=1100, height=320, bg='#5C4033')
ad.place(relx=0.43, rely=0.25, anchor='center')

top_rated = tk.Frame(frame1, width=1100, height=320, bg='#7f5112')
top_rated.place(relx=0.43, rely=0.71, anchor='center')

frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightgreen")
# discover_icon = PhotoImage(file='discover_small.png')
notebook.add(frame2, text="Discover", compound=tk.LEFT)

notebook.place(relx=0)




root.mainloop()