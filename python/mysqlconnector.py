import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python'
)

cursor = conn.cursor()
"""
cursor.execute(
    "CREATE TABLE IF NOT EXISTS students ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "name VARCHAR(255),"
    "age INT"
    ")"
)

sql = "INSERT INTO students(name, age) VALUES (%s, %s)"
values = ('abhay', 23)

cursor.execute(sql, values)

conn.commit()

print("Student inserted successfully")

cursor.close()
conn.close()"""
try:
    cursor.execute("SELECT *FROM students")
    rows=cursor. fetchall()
    for row in rows:
        print(row)
    conn.commit()
    print("Suceessfully got data")
except mysql.connector.Error:
    coon.rollback


import json
metadata = {"hobbies": ["reading", "coding"]}
json_str = json.dumps (metadata)
cursor.execute(
"INSERT INTO users (metadata) VALUES (%s)",
(json_str,))



import json
metadata = {"hobbies": ["reading", "coding"]}
json_str = json.dumps (metadata)
cursor.execute(
"INSERT INTO users (metadata) VALUES (%s)",
(json_str,)