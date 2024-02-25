from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Entry, Button, messagebox
# database = mysql.connect(host="localhost", user="root", password="", database="library")
# cursor = database.cursor()

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    # quantity = entry_quantity.get()


    # if title and author and quantity:
    #     # Placeholder for actual database insertion
    #     query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
    #     values = (title, author, quantity)
    #     # cursor.execute(query, values)
    #     # database.commit()
        
    #     # Displaying book information (replace this with your actual database handling)
    #     message = f"Book added successfully:\nTitle: {title}\nAuthor: {author}\nQuantity: {quantity}"
    #     messagebox.showinfo("Success", message)
    # else:
    #     messagebox.showerror("Error", "Please fill in all the fields.")

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
style.configure('lefttab.TNotebook.Tab', font=('Montserrat Medium', 15), width=12, background='#6F3434')
style.map("TNotebook.Tab", background=[("selected", '#F63A3A')])

frame1 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightblue")
notebook.add(frame1, text='ADMIN PAGE ', compound=tk.RIGHT)

ad = tk.Frame(frame1, width=1100, height=1000, bg='#5C4033')
ad.place(relx=0.43, rely=0.25, anchor='center')


top_rated = tk.Frame(frame1, width=2500, height=320, bg='#7f5112')
top_rated.place(relx=0.43, rely=0.71, anchor='center')

def open_add_book_form():
    add_book_form_window = Toplevel(top_rated)
    add_book_form_window.title("Add Book Form")

    # Entry widgets for adding books
    label_title_add = Label(add_book_form_window, text="ADD TITLE:", font=("Montserrat", 12))
    entry_title_add = Entry(add_book_form_window, width=30, font=("Montserrat", 12))
    label_author_add = Label(add_book_form_window, text="ADD AUTHOR:", font=("Montserrat", 12))
    entry_author_add = Entry(add_book_form_window, width=30, font=("Montserrat", 12))

    # Function to handle book addition
    def add_book_form():
        title = entry_title_add.get()
        author = entry_author_add.get()

        if title and author:
            # Placeholder for actual database insertion
            # Perform your database insertion logic here

            # Displaying book information (replace this with your actual database handling)
            message = f"Book added successfully:\nTitle: {title}\nAuthor: {author}"
            messagebox.showinfo("Success", message)
            add_book_form_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in both Title and Author fields.")

    # Button for submitting the form
    button_add_book_form = Button(add_book_form_window, text="Add Book", command=add_book_form, font=("Montserrat", 12))

    # Packing the Entry widgets and Button
    label_title_add.pack(pady=10)
    entry_title_add.pack(pady=10)
    label_author_add.pack(pady=10)
    entry_author_add.pack(pady=10)
    button_add_book_form.pack(pady=20)

# Create widgets for the top_rated frame
label_top_rated = Label(top_rated, text="Top Rated Books", font=("Montserrat Medium", 18), fg="white", bg='#7f5112')
label_top_rated.pack(pady=10)

# Button to open the book addition form
button_add_book = Button(top_rated, text="ADD BOOK", command=open_add_book_form, font=("Montserrat", 14))
button_add_book.pack(pady=20)
    




frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightgreen")
notebook.add(frame2, text="Discover", compound=tk.LEFT)

notebook.place(relx=0)

# Create widgets for the admin page
label_adduser = Label(ad, text="ADD USER:")
label_activeusers= Label(ad, text="Active users")

entry_title = Entry(ad)
entry_author = Entry(ad)


button_add_book = Button(ad, text="Add Book", command=add_book)

# Arrange widgets in a grid
label_adduser.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_activeusers.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_title.grid(row=0, column=1, padx=10, pady=10)
entry_author.grid(row=1, column=1, padx=10, pady=10)

# Create widgets for the discover page


label_title_discover = Label(frame2, text="Title:")
label_author_discover = Label(frame2, text="Author:")
label_quantity_discover = Label(frame2, text="Quantity:")
label_cover_discover = Label(frame2, text="Cover Image URL:")

entry_title_discover = Entry(frame2)
entry_author_discover = Entry(frame2)
entry_quantity_discover = Entry(frame2)
entry_cover_discover = Entry(frame2)

button_add_book_discover = Button(frame2, text="Add Book", command=add_book)

# Arrange widgets in a grid for the discover page
label_title_discover.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_author_discover.grid(row=1, column=0, padx=10, pady=10, sticky="e")
label_quantity_discover.grid(row=2, column=0, padx=10, pady=10, sticky="e")
label_cover_discover.grid(row=3, column=0, padx=10, pady=10, sticky="e")

entry_title_discover.grid(row=0, column=1, padx=10, pady=10)
entry_author_discover.grid(row=1, column=1, padx=10, pady=10)
entry_quantity_discover.grid(row=2, column=1, padx=10, pady=10)
entry_cover_discover.grid(row=3, column=1, padx=10, pady=10)

button_add_book_discover.grid(row=4, columnspan=2, pady=10)

# Create widgets for the admin page (bottom box)
label_library_info = Label(ad, text="This is Your KitAPP :)", font=("Montserrat Medium", 16))
text_library_info = Text(ad, height=6, width=50)
text_library_info.insert(tk.END, "Welcome to our library! Explore our collection of books.", "dark_blue")
text_library_info.tag_configure("dark_blue", background="#00008B", foreground="#FFD700")  # Set background and foreground colors
text_library_info.config(state=tk.DISABLED)

# Arrange widgets in a grid for the admin page (bottom box)
label_library_info.grid(row=10, column=0, columnspan=2, pady=10)
text_library_info.grid(row=6, column=0, columnspan=2, pady=10)



root.mainloop()
