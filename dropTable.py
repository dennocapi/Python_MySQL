import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd ='',
	database = 'm4141'
	)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)