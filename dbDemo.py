from dbSetup import connection, cursor


cursor.execute("INSERT INTO demo (id) VALUES (3);")

cursor.execute("select * from demo;")
print(cursor.fetchall())

#Applies any transactions made to the actual database
connection.commit()

#Important to close the connection after using the database
connection.close()
