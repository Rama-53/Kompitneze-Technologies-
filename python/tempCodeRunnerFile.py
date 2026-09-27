import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
cursor=conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS students ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "name VARCHAR(255),"
    "age INT"
    ")"
)
sql=×

...

sql="insert into students(name,mark) values (%s,%s)"
values=("abhay",23)
cursor.execute(sql,values)