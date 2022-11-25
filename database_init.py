import mysql.connector
def set2():
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="admin",
    database="student"
    )
    cur=mydb.cursor()
    cur.execute("Create table if not exists login(id int(5) primary key not null auto_increment,email text(35),password varchar(35))")
    mydb.commit()

    cur.execute("Create table if not exists data(name varchar(20),rollno int(3),email text(30),gender varchar(15),dob text(30),address text,semester varchar(10),section varchar(10),phono bigint)")
    mydb.commit()

    mydb.close()
def set():
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="admin"
    )
    cur=mydb.cursor()
    cur.execute("Create database if not exists student")    
    mydb.commit()
    mydb.close()
if __name__=="main":
    set()
    set2()