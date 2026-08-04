import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='root',database='sedb')
if con.is_connected():
    print("Database Connected Successfully")
else:
    print("Database not Connected")