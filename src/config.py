import mysql.connector as mysql


database = mysql.connect(
    host='localhost',
    user='your_database_username',
    password='your_database_password',
    database='your_database_name'
)

cursor = database.cursor()