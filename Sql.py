import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="Rhesus@22"
)

print(mydb)