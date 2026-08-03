import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='root',database='sepmdb')
cur = con.cursor()
cur.execute("show databases")         
print("=====Database present in mysql===============") 
for dbname in cur:
    print(dbname)
    


