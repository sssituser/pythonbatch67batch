import mysql.connector as mysql 
con = mysql.connect(host ='localhost',user='root',password = 'root',database='sedb')
cur = con.cursor()
query = input('Enter Your Query   : ')
id = int(input('Enter Employee Id : '))
name = input('Enter Employee Name : ')
sal = int(input('Enter Salary : '))
cur.execute(query,(id,name,sal))
cur.close()
con.commit()

