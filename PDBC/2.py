import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='root',database='sepmdb')
cur = con.cursor()
cur.execute("insert into employee values(%s,%s,%s)",(111,"abc",50000))
con.commit()