from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import datetime



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
home_icon = ImageTk.PhotoImage(file='pics/home.png')

notebook.add(frame1, text='Home', image=home_icon, compound=tk.LEFT)

ad = tk.Frame(frame1, width=1100, height=320, bg='#FFFFFF')
ad.place(relx=0.43, rely=0.25, anchor='center')

top_rated = tk.Frame(frame1, width=1100, height=320, bg='#FFFFFF')
top_rated.place(relx=0.43, rely=0.71, anchor='center')

top_books=Label(top_rated,text="TOP RATED",font=('Montserrat Black', 25),bg="#FFFFFF")
top_books.place(relx=0.01,rely=0.01)

badge_image=ImageTk.PhotoImage(file="pics/badge.png",)
badge_label=Label(top_rated,image=badge_image,bg="#FFFFFF")
badge_label.place(relx=0.21,rely=0.03)

display_top_rated_books=tk.Frame(top_rated,width=1020,height=230, bg="#FFFFFF")
display_top_rated_books.place(relx=0.49,rely=0.55,anchor='center')

Book1_image=ImageTk.PhotoImage(file="pics/The_Great_Gatsby.png")
Book1_label=Label(display_top_rated_books,image=Book1_image,)
Book1_label.place(relx=0.03,rely=0.05)

Book2_image=ImageTk.PhotoImage(file="pics/To_Kill_a_Mockingbird.png")
Book2_label=Label(display_top_rated_books,image=Book2_image)
Book2_label.place(relx=0.238 ,rely=0.05 )

Book3_image=ImageTk.PhotoImage(file="pics/Pride and prejudice.png")
Book3_label=Label(display_top_rated_books,image=Book3_image)
Book3_label.place(relx=0.46 ,rely=0.05 )

Book4_image=ImageTk.PhotoImage(file="pics/The alchemist.png")
Book4_label=Label(display_top_rated_books,image=Book4_image)
Book4_label.place(relx=0.65 ,rely=0.05 )

Book5_image=ImageTk.PhotoImage(file="pics/Earthsea.png")
Book5_label=Label(display_top_rated_books,image=Book5_image)
Book5_label.place(relx=0.84 ,rely=0.05 )

def show_book_info(book_info_text,x,y):
    global info_box
    info_box=tk.Toplevel()
    info_box.title("Book Information")
    info_box.geometry(f"700x500+{x}+{y}")
    info_box.resizable(False,False)
    info_box.configure(bg="#FFFFFF")

    info_label=tk.Label(info_box, text=book_info_text,justify=tk.LEFT,font=("Montserrat SemiBold",10),bg="#FFFFFF")
    info_label.place(relx=0.1, rely=0.001, relwidth=0.8, relheight=0.6)

    borrow_button = tk.Button(info_box, text="Borrow",fg='black',bg="#FFFFFF",font=("Monstserrat SemiBold",15),borderwidth=5,command=borrow_book)
    borrow_button.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    
    def close_info_box():
        info_box.destroy()
        # Reset background color of all book labels
        Book1_label.config(bg="#ADD8E6")
        Book2_label.config(bg="#ADD8E6")
        Book3_label.config(bg="#ADD8E6")
        Book4_label.config(bg="#ADD8E6")
        Book5_label.config(bg="#ADD8E6")

    # Set the function to be called when the info_box window is closed
    info_box.protocol("WM_DELETE_WINDOW", close_info_box)



def show_book_info_gatsby():
    
    book_info_text=(
        "Title: The Great Gatsby\n\n"
        "Author: F. Scott Fitzgerald\n\n"
        "Genre: Fiction,Classic Literature\n\n"
        "Rating: 4.7\n\n"
        "Summary: The Great Gatsby is a classic novel by F. Scott Fitzgerald set\n"
        "in the Roaring Twenties.It follows the mysterious millionaire Jay Gatsby\n"
        "and his obsession with the beautiful Daisy Buchanan hrough themes of\n"
        "love,wealth, and the American Dream, the book explores the decadence\n" 
        "and disillusionment of the Jazz Age." 
    ) 
    
    show_book_info(book_info_text,300,100)
    pass

def show_book_info_mockingbird():
    book_info_text=(
        "Title: To Kill a Mockingbird\n\n"
        "Author: Harper Lee\n\n"
        "Genre: Fiction,Southern Gothic\n\n"
        "Rating: 4.6\n\n"
        "Summary: To Kill a Mockingbird is a novel set in the American South \n"
        "during the 1930s. It explores themes of racial injustice and moral growth\n"
        "through the eyes of young Scout Finch."
    ) 
    
    show_book_info(book_info_text,300,100)
    pass



def show_book_info_pride_and_prejudice():
    book_info_text=(
        "Title: Pride and Prejudice\n\n"
        "Author: Jane Austen\n\n"
        "Genre: Romance,Classic Literature\n\n"
        "Rating:4.4\n\n"
        "Summary:Pride and Prejudice follows the tumultuous relationship between\n"
        "Elizabeth Bennet and Mr. Darcy amidst the societal norms and prejudices of\n"
        "early 19th-century England.\n"
   
    )
    
    show_book_info(book_info_text,300,100)
    pass

def show_book_info_alchemist():
    book_info_text=(
        "Title: The Alchemist\n\n"
        "Author: Paulo Coelho\n\n"
        "Genre: Fiction,Allegorical Novel\n\n"
        "Rating:4\n\n"
        "Summary:The Alchemist tells the story of Santiago,\n"
        "a young shepherd boy,on his journey to find his\n"
        "personal legend and discover the true meaning of life."
    )
    
    show_book_info(book_info_text,300,100)
    pass



def show_book_info_earthsea():
    book_info_text=(
        "Title: Earthsea\n\n"
        "Author: Ursula K. Le Guin\n\n"
        "Genre: Fantasy\n\n"
        "Rating:4.1\n\n"
        "Summary:Earthsea is a fantasy series set in the archipelago of Earthsea,\n"
        "where magic and wizardry are deeply woven into the fabric of society. The\n"
        "series follows the adventures of various characters as they navigate the\n"
        "challenges and mysteries of their world.\n"
    )
    
    show_book_info(book_info_text,300,100)
    pass
    
    
 # Reset background color of Book1_label after a short delay
root.after(10, lambda: Book1_label.config(bg="#ADD8E6")) 
root.after(10, lambda: Book2_label.config(bg="#ADD8E6")) 
root.after(10, lambda: Book3_label.config(bg="#ADD8E6")) 
root.after(10, lambda: Book4_label.config(bg="#ADD8E6")) 
root.after(10, lambda: Book5_label.config(bg="#ADD8E6")) 

             
def on_book1_click(event):
    Book1_label.config(bg="#FFD700")
    show_book_info_gatsby()

def on_book2_click(event):
    Book2_label.config(bg="#FFD700")
    show_book_info_mockingbird()

def on_book3_click(event):
    Book3_label.config(bg="#FFD700")
    show_book_info_pride_and_prejudice()

def on_book4_click(event):
    Book4_label.config(bg="#FFD700")
    show_book_info_alchemist()

def on_book5_click(event):
    Book5_label.config(bg="#FFD700")
    show_book_info_earthsea()

Book1_label.bind("<Button-1>",  on_book1_click)
Book2_label.bind("<Button-1>", on_book2_click)
Book3_label.bind("<Button-1>", on_book3_click)
Book4_label.bind("<Button-1>",  on_book4_click)
Book5_label.bind("<Button-1>",  on_book5_click)

frame2 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
discover_icon =ImageTk.PhotoImage(file='pics/discover.png')
notebook.add(frame2, text="Discover", image=discover_icon, compound=tk.LEFT)

search_frame=tk.Frame(frame2,width=1000,height=700,bg="#FFFFFF") #big white frame inside dicover
search_frame.place(relx=0.425,rely=0.481,anchor="center")

books_table_frame=tk.Frame(search_frame,width=900,height=600,bg="#ADD8E6")
books_table_frame.place(relx=0.5,rely=0.6,anchor="center")

Search=Label(search_frame,text="SEARCH BOOKS",font=("Montserrat Black", "25"),bg="#FFFFFF")
Search.place(relx=0.5,rely=0.08,anchor="center")

Book_Id = Label(search_frame, text='Book ID', font=("Montserrat Light", "22"),bg="#FFFFFF")
Book_Id.place(relx=0.12,rely=0.251,anchor="center")

search_entry=tk.Entry(search_frame,width=50,bd=2,highlightbackground="black",font=('Montserrat Light',12))
search_entry.place(relx=0.2,rely=0.235)

def search_books():
    global books_data
    user_input = search_entry.get()
    print("Searching for:",user_input)
    found=False

    for item in books_tree.get_children():
        books_tree.delete(item)

    for book in books_data:
        if str(book[0]) == user_input:
            books_tree.insert("", "end", value=book[:4])
            found = True
            break  # Exit loop once book is found

    if not found:
        MessageBox.showerror("Error", "Book not found")


search_button=tk.Button(search_frame,text="Search",bg="#FFFFFF",command=search_books,width=12,height=1,font=("Montserrat SemiBold",9))
search_button.place(relx=0.821,rely=0.253,anchor="center")



def populate_books_listbox(books_tree):
    # Define books_data as global to ensure it's accessed from the global scope
    global books_data

    # Clear the search_entry widget
    search_entry.delete(0, tk.END)

    # Connect to the database
    connection = mysql.connect(
        host="localhost",
        user="root",
        password="batsal1019",
        database="project"
    )
    cursor = connection.cursor()

    # Query to fetch book data from the database
    query = "SELECT BookID, title, Genre, Author FROM Books"
    cursor.execute(query)

    # Fetch all rows from the query result
    books_data = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Clear the existing items in the books_tree widget
    for item in books_tree.get_children():
        books_tree.delete(item)

    # Insert fetched book data into the books_tree widget
    for book in books_data:
        books_tree.insert("", "end", value=book[:4])


# Create the books_tree widget
columns = ('BookID', 'Title', 'Genre', 'Author')
books_tree = ttk.Treeview(books_table_frame, columns=columns, show='headings', height=20)

for col in columns:
    books_tree.heading(col, text=col)

books_tree.pack(expand=True, fill='both')

# Call the function to populate the books listbox
populate_books_listbox(books_tree)




refresh_button = tk.Button(search_frame, text="Refresh", command=populate_books_listbox,width=12,height=1,font=("Montserrat SemiBold",9))
refresh_button.place(relx=0.43,rely=0.94)


frame3 = tk.Frame(notebook, width=screen_width, height=screen_height, bg="#ADD8E6")
return_books_icon =ImageTk.PhotoImage(file='pics/your_books.png')
notebook.add(frame3, text="Return Books", image=return_books_icon, compound=tk.LEFT)

return_books_frame=tk.Frame(frame3,width=1000,height=700,bg="#FFFFFF")
return_books_frame.place(relx=0.425,rely=0.481,anchor="center")


def return_books():
    user_id = user_id_entry.get().strip()  # Remove any leading/trailing spaces
    book_id = book_id_entry.get().strip()  # Remove any leading/trailing spaces
    
    if not user_id or not book_id:
        MessageBox.showerror("ERROR", "Please fill all the fields.")
        return
    
    try:
        connection = mysql.connect(
            host="localhost",
            user="root",
            password="MahotraAdhikari7@",
            database="project"
        )
        cursor = connection.cursor()
        
        # Check if the user has borrowed the specified book
        query = "SELECT * FROM borrowedbooks WHERE UserID = %s AND BookID = %s"
        cursor.execute(query, (user_id, book_id))
        borrowed_book = cursor.fetchone()
        
        if not borrowed_book:
            MessageBox.showerror("ERROR", "This book is not borrowed by the user.")
            return
        
        # Delete the borrowed book entry
        delete_query = "DELETE FROM borrowedbooks WHERE UserID = %s AND BookID = %s"
        cursor.execute(delete_query, (user_id, book_id))
        connection.commit()
        
        MessageBox.showinfo("Success", "Book returned successfully!")
        
    except Exception as e:
        MessageBox.showerror("Error", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


user_id_label = tk.Label(return_books_frame, text="User ID:",font=("Montserrat Light", "22"),bg="#FFFFFF")
user_id_label.place(relx=0.3, rely=0.3, anchor="center")

user_id_entry = tk.Entry(return_books_frame,borderwidth=3,width=20,highlightbackground="black",font=('Montserrat Light',12))
user_id_entry.place(relx=0.5, rely=0.3, anchor="center")

book_id_label = tk.Label(return_books_frame, text="Book ID:",font=("Montserrat Light", "22"),bg="#FFFFFF")
book_id_label.place(relx=0.3, rely=0.5, anchor="center")

book_id_entry = tk.Entry(return_books_frame,borderwidth=3,width=20,highlightbackground="black",font=('Montserrat Light',12))
book_id_entry.place(relx=0.5, rely=0.5, anchor="center")

return_button = tk.Button(return_books_frame, text="Return", command=return_books,width=17,height=3)
return_button.place(relx=0.5, rely=0.7, anchor="center")

Today_date = datetime.date.today()
Today_date_label = tk.Label(return_books_frame, text=f"Today's Date: {Today_date}", justify=tk.CENTER,font=("Montserrat SemiBold", 15), bg="#FFFFFF")
Today_date_label.place(relx=0.08, rely=0.1, relwidth=0.8)



def borrow_book():
    global info_box

    if 'info_box' in globals() and info_box:
            info_box.destroy()
   
    borrow_book_box=tk.Toplevel()
    borrow_book_box.title("Borrow book")
    borrow_book_box.geometry(f"700x500")
    borrow_book_box.resizable(False,False)
    borrow_book_box.configure(bg="#FFFFFF")

    borrow_book_label=tk.Label(borrow_book_box, text="You are borrowing the book",justify=tk.CENTER,font=("Montserrat SemiBold",20),bg="#FFFFFF")
    borrow_book_label.place(relx=0.46, rely=0.1,anchor="center")

    borrow_date = datetime.date.today()
    due_date = borrow_date + datetime.timedelta(days=30)  # Due date is 30 days from borrow date

    user_id_label = tk.Label(borrow_book_box, text="User ID:",font=("Montserrat Light", "18"),bg="#FFFFFF")
    user_id_label.place(relx=0.3, rely=0.3, anchor="center")

    user_id_entry = tk.Entry(borrow_book_box,borderwidth=3,width=20,highlightbackground="black",font=('Montserrat Light',12))
    user_id_entry.place(relx=0.55, rely=0.3, anchor="center")

    book_id_label = tk.Label(borrow_book_box, text="Book ID:",font=("Montserrat Light", "18"),bg="#FFFFFF")
    book_id_label.place(relx=0.3, rely=0.5, anchor="center")

    book_id_entry = tk.Entry(borrow_book_box,borderwidth=3,width=20,highlightbackground="black",font=('Montserrat Light',12))
    book_id_entry.place(relx=0.55, rely=0.5, anchor="center")

    Done_button = tk.Button(borrow_book_box, text="DONE", command=insert_to_database,width=12,height=2,font=("Montserrat SemiBold",9))
    Done_button.place(relx=0.4,rely=0.8)           

    borrow_date_label = tk.Label(borrow_book_box, text=f"Borrow Date: {borrow_date}", justify=tk.CENTER,font=("Montserrat SemiBold", 10), bg="#FFFFFF")
    borrow_date_label.place(relx=0.1, rely=0.6, relwidth=0.8)

    due_date_label = tk.Label(borrow_book_box, text=f"Due Date: {due_date}", justify=tk.CENTER,font=("Montserrat SemiBold", 10), bg="#FFFFFF")
    due_date_label.place(relx=0.1, rely=0.7, relwidth=0.8)

    # Insert borrowed book details into the database

def insert_to_database():
    user_id = user_id_entry.get().strip()  # Remove any leading/trailing spaces
    book_id = book_id_entry.get().strip()  # Remove any leading/trailing spaces
    borrow_date = datetime.date.today()
    due_date = borrow_date + datetime.timedelta(days=30)  # Due date is 30 days from borrow date
    
    # if not user_id or not book_id:
    #     MessageBox.showerror("ERROR", "Please fill all the fields.")
    #     return
    
    try:
        connection = mysql.connect(
            host="localhost",
            user="root",
            password="batsal1019",
            database="project"
        )
        cursor = connection.cursor()


        query = "SELECT * FROM Users WHERE UserID = %s AND EXISTS (SELECT 1 FROM Books WHERE BookID = %s)"
        cursor.execute(query, (user_id, book_id))
        user = cursor.fetchone()
        
        if not user:
            MessageBox.showerror("Error", "Either User ID does not exist or Book ID does not exist.")
            return

        
        insert_query = "INSERT INTO borrowedbooks (UserID,BookID, BorrowDate, DueDate) VALUES (%s, %s, %s,%s)"
        cursor.execute(insert_query,(user_id, book_id, borrow_date, due_date))
        connection.commit()

        MessageBox.showinfo("Success", "Book borrowed successfully!")

    except Exception as e:
            MessageBox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
insert_to_database()
    
    

logo = ImageTk.PhotoImage(file='pics/kitapp.png')
label = tk.Label(root, image=logo)
label.place(relx=0.005, rely=0.85)

advert = ImageTk.PhotoImage(file='pics/advert.png')
label = tk.Label(frame1, image=advert)
label.place(relx=0.025, rely=0.041)






notebook.place(relx=0)

root.mainloop()