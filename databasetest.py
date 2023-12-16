import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database="student_management_system"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM std_registration")

myresult = mycursor.fetchall()

print(myresult)