import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd ='',
	database = 'm4141'
	)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val = ('Gidi','Nakuru')
# val =[
# 	  ('Dennis','Nairobi'),
# 	  ('Mary','Machakos'),
# 	  ('Max','Kitui')
# 	  ]

mycursor.execute(sql, val)

# Use this line if you want to insert many rows
# mycursor.executemany(sql,val)

# The next line is required to make the changes,otherwise no changes are made to the table
mydb.commit()

print(mycursor.rowcount, 'record inserted')
# To see the id of the last row inserted
# print('1 recordinserted ID:',mycursor.lastrowid)