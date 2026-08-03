import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='root',database='sepmdb')
cur = con.cursor()
choice = int(input("1.Insert 2.Delete 3.Update 4.Select Enter Your choice : "))
match choice:
    case 1:
         id = int(input('Enter Id : '))
         name = input('Enter Name : ')
         sal = int(input('Enter Sal : '))
         cur.execute("insert into employee values(%s,%s,%s)",(id,name,sal))
         con.commit()
         print("Record Inerted Successfully")
    case 2:
        id = int(input('Enter Id : '))
        cur.execute("delete from employee where eid = %s",(id,))
        con.commit()
        print("Record Deleted Successfully")
        con.commit()
    case 3:
        id = int(input('Enter Id : '))
        name = input('Enter Name : ')
        sal = int(input('Enter Sal : '))
        cur.execute("update employee set ename = %s,esal = %s where eid = %s",(name,sal,id))
        con.commit()
        print("Record Updated Successfully")
    case 4:
        cur.execute("select * from employee")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
    case _:
        print("Invalid choice :")
    