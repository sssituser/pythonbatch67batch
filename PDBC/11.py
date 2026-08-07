import mysql.connector as mysql
con = mysql.connect(host="localhost",user="root",password="root",database ="sedb")
cur = con.cursor()
cur.execute("select * from employee")
employees = cur.fetchmany(3)
print("Employee ID \tEmployee Name\tEmployee Salary")
for emp in employees:
    print(f'{emp[0]}\t\t{emp[1]}\t\t{emp[2]}')
con.close()