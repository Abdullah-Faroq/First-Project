import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management_system"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO std_registration (First_Name,Last_Name,Age,Email,Phone_No,CNIC,Address,Gender,University,Roll_No,Department,Date_Of_Birth,City,Status,Date_Of_Addmission) VALUES ('Muhammad','Ali','20','muhammadali414@gmail.com','0309712345','3660268486205','Mahajar colony house 38.','male','Islamia University of Bahawalpur','F22NDOCS1M01108','Computer Science','2003-3-12','Bahawalnagar','Inactive','2022-12-3')")

mydb.commit()