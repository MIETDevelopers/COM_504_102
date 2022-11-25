from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import os
class registers:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.iconbitmap("registration.ico")
        self.root.title("Registration")

        #Background frame
        frame=Frame(self.root)
        image=Image.open("login.jpg")
        resized=image.resize((1536,864))
        self.new_image=ImageTk.PhotoImage(resized)
        Label(frame,image=self.new_image).pack()
        frame.pack()
        #Frame for login screen
        f1=Frame(frame,bg="white")
        Label(f1,text="Registration",font=("times new roman",30,"bold"),background="#6600ff",foreground="white",borderwidth=4,relief=GROOVE).pack(fill=X)

        lab_Email=Label(f1,text="Email",font=("helvetica",22,"bold"),background="#6600ff",foreground="white")
        lab_Email.pack(pady=30,fill=X)
        self.lab_entry=Entry(f1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE)
        self.lab_entry.pack(pady=5,fill=X)

        lab_password=Label(f1,text="Password",font=("helvetica",22,"bold"),background="#6600ff",foreground="white")
        lab_password.pack(pady=18,fill=X)

        self.lab_entry_pass=Entry(f1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE)
        self.lab_entry_pass.pack(pady=15,fill=X)
        f1.place(x=650,y=150,height=500,width=400) 
     
        button1=Button(f1,text="Signup",width=10,background="orange",foreground="black",height=3,font=("helvetica",10,"bold"),command=self.action)
        self.lab_entry_pass.config(show='*')
        button1.pack(pady=15)

        button2=Button(f1,text="Back To Login",width=12,background="orange",foreground="black",height=3,font=("helvetica",10,"bold"),command=self.back)
        self.lab_entry_pass.config(show='*')
        button2.pack(pady=15)
        

    def action(self):
        try:
            mydb=mysql.connector.connect(user="root",password="admin",database="student")
            cur=mydb.cursor()
            if self.lab_entry.get()=="" or self.lab_entry_pass.get()=="":
                messagebox.showwarning("Warning","All field are requried")
            else:
                cur.execute("select email,password from login where email=%s",(self.lab_entry.get(),))
                row=cur.fetchone()
                if row==None:
                    cur.execute("insert into login(email,password)values(%s,%s)",(self.lab_entry.get(),self.lab_entry_pass.get()))
                    messagebox.showinfo("Info","You are succesfully registered with us:)")
                    self.lab_entry.delete(0,END)
                    self.lab_entry_pass.delete(0,END) 
                    mydb.commit()
                    mydb.close()
                else:
                    messagebox.showerror("Error","This email is already registered")
                    self.lab_entry.delete(0,END)
                    self.lab_entry_pass.delete(0,END) 
                    mydb.commit()
                    mydb.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def back(self):
        self.root.destroy()
        os.system("python main.py")

      
root=Tk()
r1=registers(root)
root.mainloop()