import mysql.connector as mysql
con = mysql.connect(host ='localhost',user='root',password='root',database='sedb')
cur = con.cursor()
query = input('Enter Query : ')
id = int(input('Enter id : '))
cur.execute(query,(id,))
cur.close()
con.commit()
