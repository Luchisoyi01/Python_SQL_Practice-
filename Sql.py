import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rhesus@22"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Mydata")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)