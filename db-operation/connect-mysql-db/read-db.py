import pymysql


server  = "localhost"
user    = "temp"
password= "temp"
database= "world"

conn = pymysql.connect(server, user, password, database)

cursor = conn.cursor()

cursor.execute("SELECT * FROM country WHERE Name like %s ", "I%")

row = cursor.fetchone()

while row: 
    print row
    row = cursor.fetchone()


conn.close()


