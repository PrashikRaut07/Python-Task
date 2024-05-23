import mysql.connector as myconn

mydb = myconn.connect(
    host="localhost",
    user="root",
    password="0358",
    database="prashik"
)

print(mydb,"Connected to Prashik....")
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE TABLE student (student_id INT, first_name VARCHAR(255), last_name VARCHAR(255), age INT, grade FLOAT)")

# print("Table Created Successfully....")

my_cursor.execute("INSERT INTO student (student_id, first_name, last_name, age, grade) VALUES (5, 'Alice', 'Smith', 18, 95.5)")

print("New Student Record Inserted Successfully....")

my_cursor.execute("UPDATE student SET grade = 97.0 WHERE first_name = 'Alice'")

print("Grade updated for student name alice ....")

# my_cursor.execute("DELETE FROM student WHERE last_name = 'Smith'")

# print(" Student With Last_name 'Smith' Deleted Successfully...") 

my_cursor.execute("show tables")

for record in my_cursor:
    print(record)

mydb.commit()
mydb.close()