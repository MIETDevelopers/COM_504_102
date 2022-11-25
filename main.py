from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import mysql.connector
import database_init

class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Login")
        self.root.iconbitmap("login.ico")

        #Background frame
        frame=Frame(self.root)

        image=Image.open("login.jpg")

        resized=image.resize((1536,864))

        self.new_image=ImageTk.PhotoImage(resized)

        Label(frame,image=self.new_image).pack()

        frame.pack()
        #Frame for login screen

        f1=Frame(frame,bg="white")
        
        Label(f1,text="Login",font=("times new roman",30,"bold"),background="#6600ff",foreground="white",borderwidth=4,relief=GROOVE).pack(fill=X)

        lab_Email=Label(f1,text="Email",font=("helvetica",22,"bold"),background="#6600ff",foreground="white") 
        lab_Email.pack(pady=30,fill=X)
        
        self.lab_entry=Entry(f1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE)
        self.lab_entry.pack(pady=5,fill=X)

        lab_password=Label(f1,text="Password",font=("helvetica",22,"bold"),background="#6600ff",foreground="white")
        lab_password.pack(pady=18,fill=X)
        
        self.lab_entry_pass=Entry(f1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE)
        self.lab_entry_pass.pack(pady=15,fill=X)
        
        button1=Button(f1,text="Login",width=10,background="orange",foreground="black",height=3,font=("helvetica",10,"bold"),command=self.action)
        
        button2=Button(f1,text="Register",width=10,background="orange",foreground="black",height=3,font=("helvetica",10,"bold"),command=self.reg)
       
        button1.pack(pady=15)
        
        button2.pack()
        
        self.lab_entry_pass.config(show='*')
        
        f1.place(x=650,y=150,height=500,width=400) 

    def action(self):

        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="student")
            cur=mydb.cursor()
            if self.lab_entry.get()=="" or self.lab_entry_pass.get()=="":
                messagebox.showwarning("Warning","All field are requried")
            else:
                cur.execute("select email,password from login where email=%s and password=%s",(self.lab_entry.get(),self.lab_entry_pass.get()))
                row=cur.fetchone()
                if row!=None:
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Info","Success")
                    self.lab_entry.delete(0,END)
                    self.lab_entry_pass.delete(0,END) 
                    self.root.destroy()
                    os.system("python student_management.py")
                else:
                    messagebox.showwarning("Warning","Either wrong Email or password")
                    self.lab_entry.delete(0,END)
                    self.lab_entry_pass.delete(0,END) 
                 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def reg(self):
            self.root.destroy()
            os.system("python registration.py")

database_init.set()
database_init.set2()  
root=Tk()
login(root)
root.mainloop()
