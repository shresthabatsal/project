from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Entry, Button, messagebox
# database = mysql.connect(host="localhost", user="root", password="123456789", database="library")
# cursor = database.cursor()
# Placeholder for database connection (replace with your actual connection)
# database = mysql.connect(host="localhost", user="root", password="123456789", database="library")
# cursor = database.cursor()

def add_book():
    title = entry_title.get()
    author = entry_author.get()

    if title and author:
        # Placeholder for actual database insertion
        # query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
        # values = (title, author, quantity)
        # cursor.execute(query, values)
        # database.commit()

        # Displaying book information (replace this with your actual database handling)
        message = f"Book added successfully:\nTitle: {title}\nAuthor: {author}"
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", "Please fill in both Title and Author fields.")

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
    label_cover_add = Label(add_book_form_window, text="COVER IMAGE URL:", font=("Montserrat", 12))
    entry_cover_add = Entry(add_book_form_window, width=30, font=("Montserrat", 12))

    # Function to handle book addition
    def add_book_form():
        title = entry_title_add.get()
        author = entry_author_add.get()
        cover_url = entry_cover_add.get()

        if title and author:
            # Placeholder for actual database insertion
            # Perform your database insertion logic here

            # Displaying book information (replace this with your actual database handling)
            message = f"Book added successfully:\nTitle: {title}\nAuthor: {author}\nCover Image URL: {cover_url}"
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
    label_cover_add.pack(pady=10)
    entry_cover_add.pack(pady=10)
    button_add_book_form.pack(pady=20)

# Create widgets for the top_rated frame
label_top_rated = Label(top_rated, text="Top Rated Books", font=("Montserrat Medium", 18), fg="white", bg='#7f5112')
label_top_rated.pack(pady=10)

# Button to open the book addition form
button_add_book = Button(top_rated, text="ADD BOOK", command=open_add_book_form, font=("Montserrat", 14))
button_add_book.pack(pady=20)




# Replaced frame2 code
frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
manage_books_icon = PhotoImage(file='manage_books.png')
notebook.add(frame2, text="Manage books", image=manage_books_icon, compound=tk.LEFT)

# Frame inside frame2
box2 = tk.Frame(frame2,width=screen_width, height=screen_height, bg="brown")
box2.place(relx=0.5, rely=0.5, anchor="center")  # Center the box2 within frame2

notebook.place(relx=0)

# Create widgets for the admin page
label_adduser = Label(ad, text="ADD USER:")
label_activeusers = Label(ad, text="Active users")

entry_title = Entry(ad)
entry_author = Entry(ad)

button_add_book = Button(ad, text="Add Book", command=add_book)

# Arrange widgets in a grid
label_adduser.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_activeusers.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_title.grid(row=0, column=1, padx=10, pady=10)
entry_author.grid(row=1, column=1, padx=10, pady=10)

# Create widgets for the discover page
label_title_discover = Label(box2, text="Title:")
label_author_discover = Label(box2, text="Author:")
label_quantity_discover = Label(box2, text="Quantity:")
label_cover_discover = Label(box2, text="Cover Image URL:")

entry_title_discover = Entry(box2)
entry_author_discover = Entry(box2)
entry_quantity_discover = Entry(box2)
entry_cover_discover = Entry(box2)

button_add_book_discover = Button(box2, text="Add Book", command=add_book)

# Arrange widgets in a grid for the discover page
label_title_discover.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_author_discover.grid(row=1, column=0, padx=10, pady=10, sticky="e")
label_quantity_discover.grid(row=2, column=0, padx=10, pady=10, sticky="e")
label_cover_discover.grid(row=3, column=0, padx=10, pady=10, sticky="e")

entry_title_discover.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # Align entry to the left
entry_author_discover.grid(row=1, column=1, padx=10, pady=10, sticky="w")
entry_quantity_discover.grid(row=2, column=1, padx=10, pady=10, sticky="w")
entry_cover_discover.grid(row=3, column=1, padx=10, pady=10, sticky="w")

button_add_book_discover.grid(row=4, column=0, columnspan=2, pady=10)

# Arrange widgets in a grid for the discover page
label_title_discover.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_author_discover.grid(row=1, column=0, padx=10, pady=10, sticky="e")
label_quantity_discover.grid(row=2, column=0, padx=10, pady=10, sticky="e")
label_cover_discover.grid(row=3, column=0, padx=10, pady=10, sticky="e")

entry_title_discover.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # Align entry to the left
entry_author_discover.grid(row=1, column=1, padx=10, pady=10, sticky="w")
entry_quantity_discover.grid(row=2, column=1, padx=10, pady=10, sticky="w")
entry_cover_discover.grid(row=3, column=1, padx=10, pady=10, sticky="w")

button_add_book_discover.grid(row=4, column=0, columnspan=2, pady=10)
# Create widgets for the admin page (bottom box)
label_library_info = Label(ad, text="This is Your KitAPP :)", font=("Montserrat Medium", 16))
text_library_info = Text(ad, height=6, width=50)
text_library_info.insert(tk.END, "Welcome to our library! Explore our collection of books.", "dark_blue")
text_library_info.tag_configure("dark_blue", background="#00008B", foreground="#FFD700")  # Set background and foreground colors
text_library_info.config(state=tk.DISABLED)

# Arrange widgets in a grid for the admin page (bottom box)
label_library_info.grid(row=10, column=0, columnspan=2, pady=10)
text_library_info.grid(row=6, column=0, columnspan=2, pady=10)

# Replaced frame3 code
frame3 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
manage_users_icon = PhotoImage(file='manage_users.png')
notebook.add(frame3, text="Manage users", image=manage_users_icon, compound=tk.LEFT)

# Frame inside frame3
box3 = tk.Frame(frame3, width=screen_width, height=screen_height, bg="#FFFFFF")
box3.place(relx=0.5, rely=0.5, anchor="center")  # Center the box3 within frame3

notebook.place(relx=0)

# Create widgets for the manage users page
label_registered_users = Label(box3, text="NO OF REGISTERED USERS:")
label_registered_books = Label(box3, text="NO OF BOOKS:")
label_noofborrowed = Label(box3, text="NO OF BORROWED BOOKS")
label_Number_of_not_borrowed_books = Label(box3, text="Number of not borrowed books")
label_Number_of_past_due_date = Label(box3, text="No of past due date")

entry_registered_users = Entry(box3)
entry_registered_books = Entry(box3)
entry_borrowed_books = Entry(box3)
entry_notborrowed_books = Entry(box3)
entry_Number_of_past_due_date = Entry(box3)

label_registered_users.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_registered_books.grid(row=1, column=0, padx=10, pady=10, sticky="e")
label_noofborrowed.grid(row=2, column=0, padx=10, pady=10, sticky="e")
label_Number_of_not_borrowed_books.grid(row=4, column=0, padx=10, pady=10, sticky="e")
label_Number_of_past_due_date.grid(row=4, column=0, padx=10, pady=10, sticky="e")

entry_registered_users.grid(row=0, column=1, padx=10, pady=10)
entry_registered_books.grid(row=1, column=1, padx=10, pady=10)
entry_borrowed_books.grid(row=2, column=1, padx=10, pady=10)
entry_notborrowed_books.grid(row=4, column=1, padx=10, pady=10)
entry_Number_of_past_due_date.grid(row=4, column=1, padx=10, pady=10)

# Placeholder for database connection (replace with your actual connection)
# database = mysql.connect(host="localhost", user="root", password="123456789", database="library")
# cursor = database.cursor()

# Placeholder for getting statistics (replace with your actual query)
# Example: SELECT COUNT(*) FROM users;
# Example: SELECT COUNT(*) FROM books;
registered_users_count = 100  # Replace with your actual count from the query
registered_books_count = 500  # Replace with your actual count from the query

# Update the entry widgets with the fetched statistics
entry_registered_users.insert(0, registered_users_count)
entry_registered_books.insert(0, registered_books_count)

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
