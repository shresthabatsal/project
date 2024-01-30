from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import formm as login_page

def submit():
  firstname=user_entry.get()
  lastname=lastname_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  if(firstname=="" or lastname =="" or email =="" or password ==""):
        MessageBox.showinfo("Alert","insert values!!")
  else:
        con= mysql.connect(host="localhost",user="root",password="aayushd1",database="form")
        cursor=con.cursor()
        cursor.execute("insert into form values('"+ firstname +"','"+ lastname +"','" +email +"','"+ password +"')")
        cursor.execute("commit")
        MessageBox.showinfo("status","Successfully created!")
        con.close();

from tkinter import Toplevel

def open_login_page():
    global login_email_entry
    global login_password_entry
  
    login_window = Toplevel(root)
    login_window.geometry("700x700")
    login_window.title("LOGIN PAGE")
    login_window.eval('tk::PlaceWindow . Center')

    login_email_label = Label(login_window, text="Email:")
    login_email_label.place(x=50, y=30)
    login_email_entry = Entry(login_window, width=32)
    login_email_entry.place(x=150, y=30)

    login_password_label = Label(login_window, text="Password:")
    login_password_label.place(x=50, y=80)
    login_password_entry = Entry(login_window, width=32, show="*")
    login_password_entry.place(x=150, y=80)

    login_button = Button(login_window, text="Login", command=login_function, bg='lightblue')
    login_button.place(x=150, y=120)
    register_button = Button(login_window, text="Register", command=submit, bg='gold')
    register_button.place(x=220, y=120)

def login_function():
        login_email = login_email_entry.get()
        login_password = login_password_entry.get()
        if login_email == "example@example.com" and login_password == "password":
            MessageBox.showinfo("Login Status", "Login successful!")
        else:
            MessageBox.showinfo("Login Status", "Invalid login credentials.")






root = Tk()
root.geometry("700x700")
root.title("REGESTRATION PAGE")
root.eval('tk::PlaceWindow . Center')

user_firstname = Label(root,text="firstname:")
user_firstname.place(x=50, y=30)
user_entry = Entry(root,width=32)
user_entry.place(x=150,y=30)

lastname = Label(root,text="lastname:")
lastname.place(x=50,y=80)
lastname_entry=Entry(root,width=32)
lastname_entry.place(x=150,y=80)

email = Label(root,text="email       :")
email.place(x=50,y=130)
email_entry=Entry(root,width=32)
email_entry.place(x=150,y=130)

password= Label(root,text="password:")
password.place(x=50,y=180)
password_entry=Entry(root,width=32 , show="*")
password_entry.place(x=150,y=180)



submit_Botton = Button(root,text="submit",command=submit,bg='gold').place(x=150,y=220)



root.mainloop()
