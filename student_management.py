from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
import mysql.connector
import os
class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.iconbitmap("manage_sys.ico")
        self.root.title("Student-Mangement-System")
        # 1325x1325
        title=Label(self.root,text="Student Management System",borderwidth=10,relief=SUNKEN,background="green",foreground="white",font=("times new roman",24,"bold"))
        title.pack(side=TOP,fill=X)

        #Variables
        self.rollno=IntVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.dob=StringVar()
        self.phone=IntVar()
        self.semester=StringVar()
        self.section=StringVar()
        self.searchby=StringVar()
        self.search=StringVar()

        #Student Details Frame
        frame1=Frame(self.root,background="#6600ff",borderwidth=4,relief=SOLID)

        det_title=Label(frame1,text="Student Details",font=("helvetica",23,"bold"),foreground="black",background="orange")
        det_title.grid(row=0,columnspan=3,sticky=W,pady=5,padx=5)

        det_name=Label(frame1,text="Name:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_name.grid(row=1,column=0,pady=20,padx=0,sticky="W")

        entr_name=Entry(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.name)
        entr_name.grid(row=1,column=1,padx=2)

        det_roll=Label(frame1,text="Rollno:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_roll.grid(row=2,column=0,pady=15,padx=0,sticky="W")

        entr_roll=Entry(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.rollno)
        entr_roll.grid(row=2,column=1,padx=2)

        det_email=Label(frame1,text="Email:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_email.grid(row=3,column=0,pady=15,padx=0,sticky="W")

        entr_email=Entry(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.email)
        entr_email.grid(row=3,column=1,padx=2)
        
        det_gender=Label(frame1,text="Gender:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_gender.grid(row=4,column=0,pady=15,padx=0,sticky="W")

        entr_gender=ttk.Combobox(frame1,font=("times new roman",14,"bold"),state="readonly",values=("male","female","other"),textvariable=self.gender)
        entr_gender.grid(row=4,column=1,padx=2)

        det_dob=Label(frame1,text="D.O.B:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_dob.grid(row=5,column=0,pady=15,padx=0,sticky="W")
        
        self.entr_dob=DateEntry(frame1,font=("times new roman",17,"bold"),width=15,textvariable=self.dob)
        self.entr_dob.grid(row=5,column=1,padx=1,sticky="W")

        det_address=Label(frame1,text="Address:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_address.grid(row=6,column=0,pady=15,padx=0,sticky="W")

        self.entr_address=Text(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,height=2,width=20)
        self.entr_address.grid(row=6,column=1,padx=2)

        det_semester=Label(frame1,text="Semester:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_semester.grid(row=7,column=0,pady=15,padx=0,sticky="W")

        entr_semester=Entry(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.semester)
        entr_semester.grid(row=7,column=1,padx=2)

        det_section=Label(frame1,text="Section:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_section.grid(row=8,column=0,pady=15,padx=0,sticky="W")

        entr_section=Entry(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.section)
        entr_section.grid(row=8,column=1,padx=2)
        
        det_phono=Label(frame1,text="Phoneno:",font=("helvetica",19,"bold"),background="#6600ff",foreground="white")
        det_phono.grid(row=9,column=0,pady=15,padx=0,sticky="W")

        entr_phono=Entry(frame1,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.phone)
        entr_phono.grid(row=9,column=1,padx=2)

        frame1.place(x=0,y=59,height=653,width=650)
            
        #button frame
        frame2=Frame(self.root,borderwidth=4,background="green",relief=SOLID)

        button_add=Button(frame2,text="Add",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=7,command=self.add)
        button_add.grid(row=0,column=0,pady=20,padx=8)

        button_update=Button(frame2,text="Update",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=7,command=self.update)
        button_update.grid(row=0,column=1,pady=20,padx=20)

        button_delete=Button(frame2,text="Delete",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=7,command=self.delete)
        button_delete.grid(row=0,column=2,pady=20,padx=20)

        button_clear=Button(frame2,text="Clear",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=7,command=self.clear)
        button_clear.grid(row=0,column=3,pady=20,padx=20)

        button_logout=Button(frame2,text="Logout",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=7,command=self.logout)
        button_logout.grid(row=0,column=4,pady=20,padx=20)

        frame2.place(x=0,y=713,height=89,width=650)
        
        #Table frame
        frame3=Frame(self.root,background="#4d0099",borderwidth=4,relief=SOLID)

        search_lb=Label(frame3,text="Search By:",font=("helvetica",23,"bold"),background="orange",foreground="black",)
        search_lb.grid(row=0,pady=10,padx=6)

        search_combo=ttk.Combobox(frame3,state="readonly",font=("times new roman",14,"bold"),textvariable=self.searchby)
        search_combo['values']=("name","phono","rollno")
        search_combo.grid(row=0,column=1,padx=8,pady=10)

        search_entry=Entry(frame3,font=("times new roman",14,"bold"),borderwidth=4,relief=GROOVE,textvariable=self.search)
        search_entry.grid(row=0,column=2)

        search_bt1=Button(frame3,text="Search",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=8,command=self.search_)
        search_bt1.grid(row=0,column=3,pady=10,padx=10)

        search_bt2=Button(frame3,text="Show All",font=("helvetica",14,"bold"),foreground="black",background="orange",activebackground="orange",width=8,command=self.db_data_fetch)
        search_bt2.grid(row=0,column=4,pady=10,padx=10)

        frame3.place(x=650,y=59,height=741,width=885)

        #Table data frame
        frame4=Frame(frame3,background="#e3e4e6",borderwidth=4,relief=SOLID)
            
        scrolly=Scrollbar(frame4,orient=VERTICAL)
        scrollx=Scrollbar(frame4,orient=HORIZONTAL)
        
        self.student_table=ttk.Treeview(frame4,show="headings")
        self.student_table['columns']=("name","rollno","email","gender","dob","address","semester","section","phono")
        self.student_table.column("name",width=120)
        self.student_table.column("rollno",width=70)
        self.student_table.column("email",width=150)
        self.student_table.column("gender",width=70)
        self.student_table.column("dob",width=70)
        self.student_table.column("address",width=120)
        self.student_table.column("semester",width=70)
        self.student_table.column("section",width=70)
        self.student_table.column("phono",width=120)
  
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="Rollno")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("phono",text="Phono")

        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)
        self.student_table.config(xscrollcommand=scrollx.set)
        self.student_table.config(yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        self.student_table.pack(fill=BOTH,expand=1)
        self.db_data_fetch()
        self.clear()
        self.student_table.bind("<ButtonRelease-1>",self.get_selection)
        frame4.place(x=10,y=70,height=660,width=860)

    def logout(self):
        self.root.destroy()
        os.system("python main.py")

    def add(self):
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="student")
            cur=mydb.cursor()
            if self.name.get()=="" or self.rollno.get()=="" or self.email.get()=="" or self.gender.get()=="" or self.entr_address.get(1.0,END)=="" or self.semester.get()=="" or self.section.get()=="" or self.phone.get()=="":
                messagebox.showerror("Error", "Kindly fill all the field")
            else:
                cur.execute("select * from data where rollno=%s", (self.rollno.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Roll Number already present")
                else:
                    cur.execute("insert into data(name,rollno,email,gender,dob,address,semester,section,phono)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.name.get(),self.rollno.get(),self.email.get(),self.gender.get(),self.dob.get(),self.entr_address.get(1.0,END),self.semester.get(),self.section.get(),self.phone.get())) 
                    mydb.commit()
                    self.db_data_fetch()
                    messagebox.showinfo("Success", "Student Added Successfully")
                    mydb.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    

    def clear(self):
         self.name.set(""),
         self.rollno.set(""),
         self.email.set(""),
         self.gender.set(""),
         self.entr_address.delete(1.0,END)
         self.semester.set("")
         self.section.set("")
         self.phone.set("")
         self.dob.set("")
    
    def db_data_fetch(self):
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="student")
            cur=mydb.cursor()
            cur.execute("select * from data")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            mydb.commit()
            mydb.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_selection(self,event):
        sel=self.student_table.focus()
        data=self.student_table.item(sel,'values')
        self.name.set(data[0])
        self.rollno.set(data[1])
        self.email.set(data[2])
        self.gender.set(data[3])
        self.entr_dob.set_date(data[4])
        self.entr_address.delete(1.0,END)
        self.entr_address.insert(1.0,data[5])
        self.semester.set(data[6])
        self.section.set(data[7])
        self.phone.set(data[8])
    def update(self):

        try:

            mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="student")
            cur=mydb.cursor(buffered=True)
            if self.rollno=="":
                messagebox("Error","Please input all the fields")
            else:
                sel=self.student_table.focus()
                data=self.student_table.item(sel,"values")
                a=int(data[1])
                if self.rollno.get()!=a:
                    op=messagebox.askyesno("Info","You are about to change rollno value in database.Do you want to continue?")
                    if op==True:
                        cur.execute("select * from data where rollno=%s",(self.rollno.get(),))
                        val=cur.fetchone()
                        if val==None:
                            cur.execute("update data set name=%s,rollno=%s,email=%s,gender=%s,dob=%s,address=%s,semester=%s,section=%s,phono=%s where rollno=%s",(self.name.get(),self.rollno.get(),self.email.get(),self.gender.get(),self.dob.get(),self.entr_address.get(1.0,END),self.semester.get(),self.section.get(),self.phone.get(),data[1]))
                            messagebox.showinfo("Success", "Student Updated Successfully")
                            mydb.commit()
                            mydb.close()
                            self.clear()
                        else:
                            messagebox.showerror("Error","There are Two same Rollno in database can't update:/")    
                            self.clear()
                    else:
                        messagebox.showinfo("Info","operation is cancelled the operation:)")
                        self.clear()
                else:  
                    cur.execute("select * from data where rollno=%s",(self.rollno.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox("Error","Kindly choose rollno from table")
                        self.clear()
                    else:
                        cur.execute("update data set name=%s,rollno=%s,email=%s,gender=%s,dob=%s,address=%s,semester=%s,section=%s,phono=%s where rollno=%s",(self.name.get(),self.rollno.get(),self.email.get(),self.gender.get(),self.dob.get(),self.entr_address.get(1.0,END),self.semester.get(),self.section.get(),self.phone.get(),self.rollno.get()))
                        messagebox.showinfo("Success", "Student Updated Successfully")
                        mydb.commit()
            self.db_data_fetch()
            mydb.close()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def delete(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="student")
        cur=mydb.cursor()
        try:
            if self.rollno.get()=="":
                messagebox.showerror("Error", "Roll Number should be required")
            else:
                cur.execute("select * from data where rollno=%s", (self.rollno.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select student from the table ")
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from data where rollno=%s", (self.rollno.get(),))
                        mydb.commit()
                        messagebox.showinfo("Delete", "Student deleted Successfully")
                        mydb.close()
                        self.db_data_fetch()
                        self.clear()
                    else:
                        messagebox.showinfo("Info","Operation is cancelled the operation:)")
                        mydb.commit()
                        mydb.close()
                        self.clear()    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def search_(self):
        self.clear()
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="student")
            cur=mydb.cursor()
            if self.searchby.get()=="":
                messagebox.showerror("Error","Please choose the option from dropdown before searching")
            elif self.search.get()=="":
                messagebox.showwarning("Warning","Kindly enter the value to be search")
            else:  
                cur.execute(f"select * from data where {self.searchby.get()} Like %s",(self.search.get(),))
                row=cur.fetchall()
                if row!=[]:
                    self.student_table.delete(*self.student_table.get_children())
                    for rows in row:
                        self.student_table.insert("",END,values=rows)
                    mydb.close()
                else:
                    messagebox.showwarning("Warning","Search result not found")
                    mydb.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

root=Tk()
student(root)
root.mainloop()
