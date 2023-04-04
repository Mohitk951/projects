import datetime
import mysql.connector
con = mysql.connector.connect(
    host='localhost', password='Beater@95', user='root')
if con.is_connected:
    print("connected")
c = con.cursor()
c.execute("show databases")
dl = c.fetchall()
f = False
for i in dl:
    if 'lib' == i[0]:
        sql = "use lib"
        c.execute(sql)
        f = True
if f == False:
    sql1 = "Create database lib"
    c.execute(sql1)
    sql2 = "use lib"
    c.execute(sql2)
    sql3 = "create table books(bname char(50),bcode char(50),total int,subject char(50))"
    c.execute(sql3)
    sql4 = "create table issue(sname char(50),regno char(10),bcode char(10),idate date)"
    c.execute(sql4)
    sql5 = "create table submit(sname varchar(50),regno varchar(10),bcode varchar(10),sdate varchar(50))"
    c.execute(sql5)
    con.commit()


def pswd():
    ps = input("enter password:")
    if ps == "1":
        main()
    else:
        print("wrong password")
        pswd()


def main():
    print("""
                LIBRARY MANAGEMENT SYSTEM
     1. ADD     2.ISSUE   3.SUBMIT   4.REMOVE   5.DISPLAY
     """)
    choice = input("Enter your choice")
    print(">---x---x----x-----x------x-----x----x----x----<")
    if (choice == '1'):
        addbook()
    elif (choice == '2'):
        print("1. Student  2. Faculty")
        cho=input("Enter your choice :")
        print(">---x---x----x-----x------x-----x----x----x----<")
        if cho == '1':
            issuebookstudent()
        else:
            issuebookfaculty()

    elif (choice == "3"):
        submitbook()
    elif (choice == "4"):
        removebook()
    elif (choice == "5"):
        print("1.All 2.Issued")
        ch = input("Enter Task No.")
        print(">---x---x----x-----x------x-----x----x----x----<")
        if ch == '1':
            abooks()
        else:
            ibooks()

    else:
        print(" Wrong choice..........")
        main()


def addbook():
    bname = input("Enter BOOK Name: ")
    bcode= input("Enter BOOK Code: ")
    total= int(input("Total Books: "))
    subject= input("Enter Subject: ")
    data = (bname, bcode, total, subject)
    sql = 'insert into books values (%s,%s,%s,%s)'
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()


def issuebookstudent():
    sname = input("Enter Name : ")
    regno = input("Enter Reg No : ")
    bcode = input("Enter Book Code: ")
    idate= datetime.datetime.now()
    a = "insert into issue values(%s,%s,%s,%s)"
    data = (sname, regno, bcode, idate)
    print(idate)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-----------------------------------------------------------------<")
    print("Book issued to : ", sname) 
    bookup(bcode, -1)

def issuebookfaculty():
    sname = input("Enter Name : ")
    regno = input("Enter Reg No : ")
    bcode = input("Enter Book Code: ")
    idate= datetime.datetime.now()
    a = "insert into issue values(%s,%s,%s,%s)"
    data = (sname, regno, bcode, idate)
    print(idate)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-----------------------------------------------------------------<")
    print("Book issued to : ", sname) 
    bookup(bcode, -1)

def bookup(bcode, u):
    a = "select TOTAL from books where BCODE = %s"
    data = (bcode,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set TOTAL = %s where BCODE=%s"
    d = (t, bcode)
    c.execute(sql, d)
    con.commit()
    main()
def submitbook():
    sname = input("Enter Name : ")
    regno = input("Enter Reg No: ")
    bcode = input("Enter Book Code: ")
    sdate =datetime.datetime.now()
    a = "insert into submit values(%s,%s,%s,%s)"
    data = (sname,regno,bcode,sdate)
    print(sdate)
    c = con.cursor()
    c.execute(a, data)
    con.commit() 
    print(">----------------------------------------------------<")
    print("Book Submitted from : ",sname) 
    bookup(bcode, 1)


def removebook():
    ac = input("Enter Book Code: ")

   #####    121  to 140#


def removebook():
    ac = input("Enter book code:")
    a = "delete from books where BCODE=%s"
    data = (ac,)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    main()


def abooks():
    a = "select * from books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name:", i[0])
        print("Book Code:", i[1])
        print("Total:", i[2])
        print("Subject:", i[3])
        print(">---x---x----x-----x------x-----x----x----x----<")
    main()


def ibooks():
    a = "select * from issue"
    c = con.cursor() 
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Student Name : ", i[0]) 
        print("Reg No: ", i[1])
        print("Book Code: ", i[2])
        #
        [(1,2,3,4),(1,2,3,4)]
        print("Issue Date: ", i[3])
        print(">--------------------------------------------------<")
        main()


pswd()
