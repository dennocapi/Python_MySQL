import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd ='',
	)

mycursor = mydb.cursor()

# sql = "CREATE DATABASE m4141"

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
# 	print(x)

