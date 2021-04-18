from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

class editbook:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("950x600+100+50")
        self.root.resizable(False,False)
        self.root.configure(bg = "Paleturquoise")

        title = Label(self.root, text = "Library Management System", font=("Impact", 34, "bold"), fg = "#000000", bg = "Paleturquoise").place(x=200,y=10)

        back = Button(self.root, cursor = "hand2", command = self.back_func, text = "<Back", bd = 0, bg ="Paleturquoise", fg = "purple", font = ("times new roman",16)).place(x=50,y=100, width =170, height = 38 )

    def back_func(self):
        self.root.destroy()
        exec(open('admin.py').read())
    
root = Tk()
obj = editbook(root)
root.mainloop()
