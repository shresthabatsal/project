from tkinter import*
from tkinter import ttk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import tkinter as tk
root= Tk()
root.title("DASHBOARD")
root.geometry("600x600")
root.eval('tk::PlaceWindow . Center')
custom_font = ("Helvetica", 32, "bold","italic","underline",)
bgcolor="gold"
label_name = Label(root, text="Welcome to the GharBAR",font=custom_font,)
label_name.grid(row=1, column=0, padx=5, pady=10, sticky=W+E, columnspan=3)  
root.columnconfigure(0, weight=2)

baveragecategory  = Label(root,text="baverage cateogory:")
baveragecategory.place(x=40, y=120)
combo = ttk.Combobox(values=["Cold drinks", "BEER", "RUM", "WINE"],state="readonly")
combo.bind("<<ComboboxSelected>>")
combo.place(x=150, y=160)

user_beveragename = Label(root,text="Beverage name:")
user_beveragename.place(x=50, y=160)
user_entry = Entry(root,width=32)
user_entry.place(x=150,y=120)


root.mainloop()