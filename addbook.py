from tkinter import*
from tkinter import messagebox
import mysql.connector


class book_add:
    def __init__(self,root):
        self.root = root
        self.root.title("Book adding window")
        self.root.geometry("450x400+600+230")
        self.root.resizable(False,False)
        self.available = IntVar()

        Frame_book= Frame(self.root, bg = "Paleturquoise")
        Frame_book.place(height = 400, width = 450 )

        Back = Button(self.root, cursor = "hand2", command = self.back_func, text = "<back", bd = 0, bg ="Paleturquoise", fg = "purple", font = ("times new roman",16, "bold")).place(x=5,y=40, width =170, height = 38 )


        bookname = Label(Frame_book, text = "Book Name:", font=("Arial", 12, "bold"), fg = "grey", bg = "Paleturquoise").place(x=60,y=110)
        self.txt_bookname = Entry(Frame_book, font = ("times new roman", 13), bg = "lightgrey")
        self.txt_bookname.place(x=160, y= 110, width = 200, height = 30)

        author = Label(Frame_book, text = "Author Name:", font=("Arial", 12, "bold"),  fg = "grey", bg = "Paleturquoise").place(x=50,y=165)
        self.txt_author = Entry(Frame_book, font = ("times new roman", 13), bg = "lightgrey")
        self.txt_author.place(x=160, y= 165, width = 200, height = 30)

        isbn = Label(Frame_book, text = "ISBN no:", font=("Arial", 12, "bold"),  fg = "grey", bg = "Paleturquoise").place(x=76,y=220)
        self.txt_isbn = Entry(Frame_book, font = ("times new roman", 13), bg = "lightgrey")
        self.txt_isbn.place(x=160, y= 220, width = 200, height = 30)

        Lb_Available = Label(Frame_book, text = "Availability", font=("Arial", 12, "bold"),  fg = "grey", bg = "Paleturquoise").place(x=64,y=260)
        Radiobutton(self.root, text = "Yes", bg = "Paleturquoise", padx = 5, variable= self.available, value =1).place(x=150, y=260)
        Radiobutton(self.root, text = "No", bg = "Paleturquoise", padx = 5, variable= self.available, value = 0).place(x=220, y=260)

        reset = Button(Frame_book, command = self.resetfunc, text = "Reset",  cursor = "hand2", bg ="Paleturquoise", fg = "purple", bd = 0, font = ("times new roman", 14)).place(x=270,y=280)
        add = Button(Frame_book, command = self.Add_func, cursor = "hand2", text = "Add", bg ="#FF6347", fg = "white", font = ("times new roman",18)).place(x=260,y=320, width =100, height = 32 )

    def Add_func(self):
        if self.txt_bookname.get() == "" or self.txt_author.get() == "" or self.txt_isbn.get() == "" or self.available.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "afid", database = "librarymanagement")
                
                copycheck = mydb.cursor(buffered=True)
                copycheck.execute("SELECT bName,ISBN from book where bName in(%s) and ISBN in(%s)", (
                self.txt_bookname.get(),
                self.txt_isbn.get() ))
                
                if copycheck.rowcount > 0:
                    messagebox.showerror("Error", "Book is already in the database", parent= self.root)
                else:
                    mycursor = mydb.cursor()
                    mycursor.execute("INSERT INTO book(bName,author,ISBN,available) VALUES(%s,%s,%s,%s)",(
                    self.txt_bookname.get(),
                    self.txt_author.get(),
                    self.txt_isbn.get(),
                    self.available.get()))
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Adding Book", "Book added successfully", parent= self.root)
                    self.txt_bookname.delete(0,END)
                    self.txt_author.delete(0,END)
                    self.txt_isbn.delete(0,END)
            except:
                messagebox.showerror("Error", "Mysql error occured", parent= self.root)             

    def resetfunc(self):
        self.txt_bookname.delete(0,END)
        self.txt_author.delete(0,END)
        self.txt_isbn.delete(0,END)
    def back_func(self):
        self.root.destroy()
        exec(open('admin.py').read())
root = Tk()
obj = book_add(root)
root.mainloop()