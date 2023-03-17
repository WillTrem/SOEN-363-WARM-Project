import psycopg2
from dbSetup import connection, cursor
import pandas
import numpy as np
import ast
import json

# Read the CSV file
data = pandas.read_csv('instagramUsers.csv')
df = pandas.DataFrame(data)


# Populating into UserTwitter table
# for index, row in user_table.iterrows():
#     # print(row)
#     # print('\n')
#     cursor.execute("INSERT INTO usertwitter (description, username, followercount, created) VALUES (%s, %s, %s, %s)", (row["USER: Description"], row["USER: Username"], row["USER: Follower Count"], row["USER: Created"]))

for index, row in df.iterrows():
    print(row)
    print('\n')
    try:
        cursor.execute("INSERT INTO instagramaccount (instagramuserid, username, bio, numberofposts,followercount, followingcount) VALUES (%s, %s,%s,%s,%s,%s)", (row["InstagramUserId"], row["Username"], row["Bio"], row["NumberofPosts"], row["FollowersCount"], row["FollowingCount"]))
        cursor.execute("INSERT INTO hasinstagramaccount (userid, instagramuserid) VALUES (%s, %s)", (row["TwitterUserId"], row["InstagramUserId"]))
    except psycopg2.errors.UniqueViolation:
        print('User already in db.')
#Applies any transactions made to the actual database
connection.commit()

#Important to close the connection after using the database
connection.close()

