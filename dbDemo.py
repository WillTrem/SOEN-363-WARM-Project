from dbSetup import cursor

cursor.execute("INSERT INTO demo (id) VALUES (3);")

cursor.execute("select * from demo;")
print(cursor.fetchall())