import psycopg2
from dbConfig import dbConfig

connection = psycopg2.connect(database = dbConfig["name"],
                            user = dbConfig["username"],
                            password = dbConfig["password"],
                            host = dbConfig["host"],
                            port = dbConfig["port"])
print("Sucessfully connected to " + dbConfig["name"] + ".")
cursor = connection.cursor()

