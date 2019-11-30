import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd ='',
	database = 'm4141'
	)

mycursor = mydb.cursor()
# create a table
# sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255))"
# Alter table if it exists
sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
 

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
# 	print(x)


