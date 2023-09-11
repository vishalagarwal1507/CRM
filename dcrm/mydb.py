import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123',
    auth_plugin='mysql_native_password'
)


cursor = database.cursor()
cursor.execute("CREATE DATABASE crm_db")
print("All Done")