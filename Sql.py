import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rhesus@22",
  database= "mydata"
)

mycursor = mydb.cursor()

#Fecthing all data in the database
mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''
#inserting values in the database
sql= "INSERT INTO students (name, age) VALUES (%s , %s)"
students=[("Julia", 24),
          ("Ben", 25),
          ("Alice", 17),
          ("Jay", 21),
          ("Anita", 23)]


mycursor.executemany(sql, students)

mydb.commit()

'''
#mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("CREATE TABLE Students (name VARCHAR(255), age INTEGER(10))")
#mycursor.execute("SHOW TABLES")
#for TB in mycursor:
 # print(TB)