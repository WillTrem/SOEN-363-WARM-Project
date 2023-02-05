# SOEN-363-WARM-Project
SOEN 363 Project Repository of team WARM

# Database Information
## General Information
We are using a PostgreSQL database hosted by bit.io.
## How to Use the Database in a Python Script
### Setup
To be able to execute queries, simply paste the following line at the top of the python file: 
`from dbSetup import cursor`
This will import the `cursor` variable from the database setup, which can be used to manipulate the database.

### Executing a query on the Database
Queries can be executed with the following function: 
`cursor.execute("<SQL_Query>")`

Here, you would replace <SQL_Query> with any valid SQL query.

e.g. `cursor.execute("SELECT * FROM demo;")`

Then, to display the result of the last query executed (if applicable), you have to use the `cursor.fetchall()` function as following:

`print(cursor.fetchall())`

This will print the results of the query to the console. 

For more information on how to use the database in a python script, please take a look at the [Official Psycopg Documentation](https://www.psycopg.org/docs/) 




