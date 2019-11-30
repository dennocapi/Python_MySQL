import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd ='',
	database = 'm4141'
	)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"
# use WHERE to select with a filter

# escape query values by using the placeholder %s to avoid sql injection
# wildcharacters - use % to represent wild characters
# sql = "SELECT * from customers WHERE address LIKE '%way%' "


mycursor.execute(sql)

myresult = mycursor.fetchall()
# using fetchone() will return the first row of the result

for x in myresult:
	print(x)