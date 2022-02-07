import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv('.env')


database = mysql.connect(
    host= os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = database.cursor()