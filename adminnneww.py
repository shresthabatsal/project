from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import tkinter as tk

# Create a MySQL connection
# db = mysql.connect(host="localhost", user="root", password="1234567890", database="library")
# cursor = db.cursor()

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    quantity = entry_quantity.get()

    if title and author and quantity:
        # Placeholder for actual database insertion
        # query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
        # values = (title, author, quantity)
        # cursor.execute(query, values)
        # db.commit()
        
        # Displaying book information (replace this with your actual database handling)
        message = f"Book added successfully:\nTitle: {title}\nAuthor: {author}\nQuantity: {quantity}"
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", "Please fill in all the fields.")

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

ad = tk.Frame(frame1, width=1100, height=320, bg='#5C4033')
ad.place(relx=0.43, rely=0.25, anchor='center')

top_rated = tk.Frame(frame1, width=1100, height=320, bg='#7f5112')
top_rated.place(relx=0.43, rely=0.71, anchor='center')

frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="lightgreen")
notebook.add(frame2, text="Discover", compound=tk.LEFT)

notebook.place(relx=0)

# Create widgets for the admin page
label_title = Label(ad, text="Title:")
label_author = Label(ad, text="Author:")
label_quantity = Label(ad, text="Quantity:")
label_cover = Label(ad, text="Cover Image URL:")

entry_title = Entry(ad)
entry_author = Entry(ad)
entry_quantity = Entry(ad)
entry_cover = Entry(ad)

button_add_book = Button(ad, text="Add Book", command=add_book)

# Arrange widgets in a grid
label_title.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_author.grid(row=1, column=0, padx=10, pady=10, sticky="e")
label_quantity.grid(row=2, column=0, padx=10, pady=10, sticky="e")
label_cover.grid(row=3, column=0, padx=10, pady=10, sticky="e")

entry_title.grid(row=0, column=1, padx=10, pady=10)
entry_author.grid(row=1, column=1, padx=10, pady=10)
entry_quantity.grid(row=2, column=1, padx=10, pady=10)
entry_cover.grid(row=3, column=1, padx=10, pady=10)

button_add_book.grid(row=4, columnspan=2, pady=10)

root.mainloop()
