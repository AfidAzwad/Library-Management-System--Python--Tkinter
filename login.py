from tkinter import*
from tkinter import messagebox
from PIL import ImageTk #pip install pillow
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "afid", database = "librarymanagement")
mycursor = mydb.cursor()
mycursor.execute("select username,password from admin")
myresult = mycursor.fetchall()

class login_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("950x600+100+50")
        self.root.resizable(False,False)
        self.username = StringVar()
        

        #=====Background======
        self.bg = ImageTk.PhotoImage(file = "images/login.jpg")
        self.bg_image = Label(self.root,image = self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        
        #=======Login Frame======
        Frame_login = Frame(self.root, bg = "Paleturquoise")
        Frame_login.place(x = 100, y = 150, height = 380, width = 350 )

        title = Label(Frame_login, text = "Login Here", font=("Impact", 36, "bold"), fg = "#FF6347", bg = "Paleturquoise").place(x=60,y=35)
        desc = Label(Frame_login, text = "Admin login area", font=("Arial", 12, "bold"), fg = "#000000", bg = "Paleturquoise").place(x=100,y=100)

       #========login informations========
        Label_user = Label(Frame_login, text = "Username:", font=("Arial", 12, "bold"), fg = "grey", bg = "Paleturquoise").place(x=25,y=180)
        self.txt_user = Entry(Frame_login, font = ("times new roman", 13), bg = "lightgrey")
        self.txt_user.place(x=120, y= 180, width = 200, height = 30)

        Label_pass = Label(Frame_login, text = "Passwprd:", font=("Arial", 12, "bold"),  fg = "grey", bg = "Paleturquoise").place(x=25,y=250)
        self.txt_pass = Entry(Frame_login, font = ("times new roman", 13), show = "*", bg = "lightgrey")
        self.txt_pass.place(x=120, y= 250, width = 200, height = 30)

        #========Buttons========
        login = Button(self.root, command = self.login_func, cursor = "hand2", text = "login", bg ="#FF6347", fg = "white", font = ("times new roman",18)).place(x=190,y=510, width =170, height = 38 )
        #forget = Button(Frame_login, command = self.forget, text = "Forget Password ?",  cursor = "hand2", bg ="Paleturquoise", fg = "purple", bd = 0, font = ("times new roman", 12)).place(x=180,y=290)
   
    def login_func(self):
        if self.txt_user.get() == "" or self.txt_pass.get()=="":
           messagebox.showerror("Error", "All fields are required", parent = self.root)       
        elif self.txt_user.get() != "" or self.txt_pass.get() !="":
            try:
               for (self.username ,password) in myresult:
                    if self.txt_user.get() == self.username:                   
                            if self.txt_pass.get() == password:
                                root.destroy()
                                exec(open('admin.py').read())
                            else:
                                messagebox.showerror("Error", "Wrong password", parent= self.root)
                    else:
                        messagebox.showerror("Error", "Invalid Username/Password", parent= self.root)

            except:
                 messagebox.showerror("Error", "Invalid username/password", parent= self.root)
           

     
root = Tk()
obj = login_class(root)
root.mainloop()
