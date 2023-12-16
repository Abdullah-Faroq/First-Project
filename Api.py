import mysql.connector
import json
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management_system"
)

mycursor = mydb.cursor()
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    mycursor.execute("SELECT * FROM std_registration")
    myresult = mycursor.fetchall()
    return myresult

if __name__ == '__main__':
    app.run()