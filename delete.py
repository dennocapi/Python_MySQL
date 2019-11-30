import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd ='',
	database = 'm4141'
	)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s "

adr = ('Machakos',)

mycursor.execute(sql,adr)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")