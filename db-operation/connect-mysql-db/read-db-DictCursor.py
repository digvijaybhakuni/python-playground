import pymysql as mysql

con = mysql.connect(host="localhost", user="temp", password="temp", db="world", charset='utf8mb4', cursorclass=mysql.cursors.DictCursor)


try:
    with con.cursor() as cur:
        sqlStr = "SELECT * FROM city WHERE CountryCode = %s LIMIT 10"
        cur.execute(sqlStr, ['IND'])
        result = cur.fetchone()
        while result:
    	    print result
            result = cur.fetchone()
finally:
    con.close()



