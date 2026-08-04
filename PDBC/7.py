import mysql.connector as mysql
con = mysql.connect(host ='localhost',user='root',password ='root',database='sedb')
cur = con.cursor()
query = input('Enter Your Query : ')
cur.execute(query)
records = cur.fetchall()
print("Records Present in the table")
for rec in records:
    print(rec)

