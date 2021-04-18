from tkinter import*
from tkinter import messagebox
import mysql.connector


class Member:
    def __init__(self,root):
        self.root = root
        self.root.title("Member adding window")
        self.root.geometry("450x400+600+230")
        self.root.resizable(False,False)
        self.mtype = StringVar()

        Frame_member= Frame(self.root, bg = "Paleturquoise")
        Frame_member.place(height = 400, width = 450 )
        
        Back = Button(self.root, cursor = "hand2", command = self.back_func, text = "<back", bd = 0, bg ="Paleturquoise", fg = "purple", font = ("times new roman",16, "bold")).place(x=10,y=50, width =150, height = 35 )

        Mname = Label(Frame_member, text = "Member Name:", font=("Arial", 12, "bold"), fg = "grey", bg = "Paleturquoise").place(x=40,y=110)
        self.txt_mname = Entry(Frame_member, font = ("times new roman", 13), bg = "lightgrey")
        self.txt_mname.place(x=160, y= 110, width = 200, height = 30)

        Lb_mtype = Label(Frame_member, text = "Member Type:", font=("Arial", 12, "bold"),  fg = "grey", bg = "Paleturquoise").place(x=40,y=165)
        Radiobutton(self.root, text = "Regular", bg = "Paleturquoise", padx = 5,  variable =self.mtype, value = "Regular").place(x=150, y=165)
        Radiobutton(self.root, text = "Permanent", bg = "Paleturquoise", padx = 5, variable =self.mtype, value = "Permanent").place(x=220, y=165)

        borrow = Label(Frame_member, text = "Borrowed Book:", font=("Arial", 12, "bold"),  fg = "grey", bg = "Paleturquoise").place(x=30,y=220)
        self.txt_borrow = Entry(Frame_member, font = ("times new roman", 13), bg = "lightgrey")
        self.txt_borrow.place(x=160, y= 220, width = 200, height = 30)

        reset = Button(Frame_member, command = self.resetfunc, text = "Reset",  cursor = "hand2", bg ="Paleturquoise", fg = "purple", bd = 0, font = ("times new roman", 14)).place(x=290,y=260)
        add = Button(Frame_member, command = self.Add_func, cursor = "hand2", text = "Add", bg ="#FF6347", fg = "white", font = ("times new roman",18)).place(x=260,y=300, width =100, height = 32 )

    def Add_func(self):
        if self.txt_mname.get() == "" or self.mtype.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            if self.txt_borrow.get().isdigit() == True:
                try:                          
                    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "afid", database = "librarymanagement")                
                    check = mydb.cursor(buffered=True)
                    check.execute("SELECT available from book where bookID in(%s)", 
                    (self.txt_borrow.get(), ))

                    if check.rowcount > 0:                      
                        mycursor = mydb.cursor()
                        mycursor.execute("INSERT INTO member(mname,mtype,borrowed) VALUES(%s,%s,%s)",(
                        self.txt_mname.get(),
                        self.mtype.get(),
                        self.txt_borrow.get() ))
                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo("Adding Member", "Member added successfully", parent= self.root)
                        #else:
                        #messagebox.showerror("Error", "The book is not available", parent= self.root)
                    else:
                        messagebox.showerror("Error", "The book is not available", parent= self.root)

                except:
                    messagebox.showerror("Error", "Mysql error occured", parent= self.root)
            else:
                messagebox.showerror("Error", "Book ID should be a digit", parent= self.root)
                     

    def resetfunc(self):
        self.txt_mname.delete(0,END)
        self.txt_borrow.delete(0,END)
 
    def back_func(self):
        self.root.destroy()
        exec(open('admin.py').read())

root = Tk()
obj = Member(root)
root.mainloop()