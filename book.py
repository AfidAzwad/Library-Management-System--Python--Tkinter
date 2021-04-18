from tkinter import*
import tkinter as tk
from tkinter import messagebox,ttk
import mysql.connector


class book:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("950x600+100+50")
        self.root.resizable(False,False)
        self.root.configure(bg = "Paleturquoise")

        title = Label(self.root, text = "Library Management System", font=("Impact", 34, "bold"), fg = "#000000", bg = "Paleturquoise").place(x=200,y=10)
        Back = Button(self.root, cursor = "hand2", command = self.back_func, text = "<back", bd = 0, bg ="Paleturquoise", fg = "purple", font = ("times new roman",16, "bold")).place(x=25,y=118, width =170, height = 38 )
        
        title2 = Label(self.root, text = "Book List", font=("Impact", 24, "bold"), fg = "#FF6347", bg = "Paleturquoise").place(x=385,y=130)

        mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "afid", database = "librarymanagement")
        mycursor = mydb.cursor()
        mycursor.execute("select * from book")
        rows = mycursor.fetchall()
        frame = Frame(self.root)
        frame.pack(side = tk.LEFT, padx = 40)
        self.tv = ttk.Treeview(frame, columns = (1,2,3,4),  show = "headings", y=500, height = "11")
        self.tv.pack()
        self.tv.heading(1, text = "Book ID")
        self.tv.heading(2, text = "Book Name")
        self.tv.heading(3, text = "Author")
        self.tv.heading(4, text = "ISBN")

        for i in rows:
            self.tv.insert( '', 'end', values = i)
 
          
    def back_func(self):
        self.root.destroy()
        exec(open('admin.py').read())
    
root = Tk()
obj = book(root)
root.mainloop()
