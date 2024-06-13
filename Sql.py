import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rhesus@22",
  database= "mydata"
)

mycursor = mydb.cursor()

sql= "INSERT INTO students (name, age) VALUES (%s , %s)"
students=[("John", 22),
          ("Wendy", 20),
          ("Moraa", 17),
          ("Joy", 21),
          ("Ann", 22)]


mycursor.executemany(sql, students)

mydb.commit()

#mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("CREATE TABLE Students (name VARCHAR(255), age INTEGER(10))")
#mycursor.execute("SHOW TABLES")
#for TB in mycursor:
 # print(TB)