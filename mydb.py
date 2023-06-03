# Installl MySQL database
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    auth_plugin='mysql_native_password'
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("All Done!")

cursorObject.close()
database.close()
