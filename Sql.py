import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rhesus@22",
  database= "mydata"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Students (name VARCHAR(255), age INTEGER(10))")
mycursor.execute("SHOW TABLES")
for TB in mycursor:
  print(TB)