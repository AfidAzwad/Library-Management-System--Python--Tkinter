from tkinter import*
import mysql.connector


class admin:
    def __init__(self,root):
        self.root = root
        self.root.title("Admin")
        self.root.geometry("950x600+100+50")
        self.root.resizable(False,False)
        self.root.configure(bg = "Paleturquoise")

        title = Label(self.root, text = "Library Management System", font=("Impact", 34, "bold"), fg = "#000000", bg = "Paleturquoise").place(x=200,y=10)
        
        #=======Admin Frame======
        #Frame_admin = Frame(self.root, bg = "Paleturquoise")
        #Frame_admin.place(x = 120, y = 100, height = 350, width = 350 )

        title2 = Label(self.root, text = "Admin Page", font=("Impact", 24, "bold"), fg = "#FF6347", bg = "Paleturquoise").place(x=385,y=130)


       #========admin informations========
       # Label_id = Label(Frame_admin, text = "ID:", font=("Arial", 18, "bold"), fg = "grey", bg = "Paleturquoise").place(x=25,y=140)
        #Label_name = Label(Frame_admin, text = "Name:", font=("Arial", 18, "bold"), fg = "grey", bg = "Paleturquoise").place(x=25,y=170)

        #========Buttons========
        book_list = Button(self.root, command= self.book_func , cursor = "hand2", text = "See book list", bd = 0, bg ="Paleturquoise", fg = "purple", font = ("times new roman",16)).place(x=190,y=260, width =170, height = 38 )
        add_book = Button(self.root, command = self.addbook, text = "Add Book",  cursor = "hand2", bg ="Paleturquoise", fg = "purple", bd = 0, font = ("times new roman", 16)).place(x=190,y=290, width =170, height = 38 )

        members = Button(self.root,  command = self.member_func, cursor = "hand2", text = "Member list", bd = 0, bg ="Paleturquoise", fg = "purple", font = ("times new roman",16)).place(x=590,y=260, width =170, height = 38 )
        add_member = Button(self.root,  command = self.addmember, text = "Add Member",  cursor = "hand2", bg ="Paleturquoise", fg = "purple", bd = 0, font = ("times new roman", 16)).place(x=590,y=290, width =170, height = 38 )

        logout = Button(self.root, command = self.logout, cursor = "hand2", text = "Log out", bg ="#FF6347", fg = "white", font = ("times new roman",16)).place(x=800,y=439, width =85, height = 30 )   
    
    def book_func(self):
        self.root.destroy()
        exec(open('book.py').read())

    def addbook(self):
        self.root.destroy()
        exec(open('addbook.py').read())
    def addmember(self):
        self.root.destroy()
        exec(open('addmember.py').read())
    def member_func(self):
        self.root.destroy()
        exec(open('member.py').read())   
    def logout(self):
        self.root.destroy()
        exec(open('login.py').read())
root = Tk()
obj = admin(root)
root.mainloop()
