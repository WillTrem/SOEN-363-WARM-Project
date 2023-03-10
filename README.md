# SOEN-363-WARM-Project
SOEN 363 Project Repository of team WARM
## General Information
We are using a PostgreSQL database hosted by bit.io.

# How to Use the Database in a Python Script
## Setup
First, you will have to install the `psycopg2` package, which takes care of connecting and communicating with the database. You can install it by running the following command in a terminal that points inside the repository:

```bash
pip install psycopg2
```

To be able to execute queries, simply paste the following line at the top of the python file:

```bash
from dbSetup import cursor
```

This will import the `connection` `cursor` variable from the database setup, which can be used to manipulate the database.

## Executing a query on the Database
Queries can be executed with the following function:

```bash
cursor.execute("<SQL_Query>")
```

Here, you would replace <SQL_Query> with any valid SQL query.

e.g.
```bash
cursor.execute("SELECT * FROM demo;")
```

Then, to display the result of the last query executed (if applicable), you have to use the `cursor.fetchall()` function as following:

```bash
print(cursor.fetchall())
```

This will print the results of the query to the console. 

If you make any transactions to the database (e.g. from an `INSERT` statement), you have to apply them to the database. To do so, simply add the following line after all desired transactions have been executed:

```bash
connection.commit()
```

For more information on how to use the database in a python script, please take a look at the [Official Psycopg Documentation](https://www.psycopg.org/docs/).


# Obtaining Tweets
## Setup

Install Python version 3.8 or later.

Install Pandas using:
```
pip install pandas
```

Install the social network scraper using:
```
pip install snscrape
```

## Execution

Download and execute tweets.py from this repository.
The tweets will be found in the same directory that you saved tweets.py to as a CSV file called tweets.csv

# Populating the Database with Tweet data
## Setup

Ensure you have obtained your tweet data as described in the Obtaining Tweets section.

## Execution

Open the dbPopulate.py script in an IDE that supports python script execution

Then, uncomment the section of the database you want to populate data with. 

e.g.,  to populate the Tweet table, uncomment its associated section like this:
```bash
# Populating into Tweet table
 for index, row in tweets_table.iterrows():
     print(row)
     print('\n')
     cursor.execute("INSERT INTO tweet (text, links, datetime) VALUES (%s, %s, %s)", (row["TWEET: Text"], row["TWEET: Links"], row["TWEET: Date"],))
```
Then, once that's done, you can comment back in the section to prevent re-populating the table.

Repeat for every table you want to populate with data.
