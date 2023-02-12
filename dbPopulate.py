from dbSetup import connection, cursor
import pandas
import numpy as np
import ast
import json

# Read the CSV file
data = pandas.read_csv('tweets.csv')
df = pandas.DataFrame(data)

#Split the csv file into each table 
tweets_table = df.filter(like='TWEET:')
user_table = df.filter(like='USER:').drop_duplicates()
metrics_table = df.filter(like='METRICS:')
hashtag_table = df.filter(like='HASHTAG').dropna()
links_table = df.filter(like='TWEET: Links').dropna()

# Populating into Tweet table
# for index, row in tweets_table.iterrows():
#     print(row)
#     print('\n')
#     cursor.execute("INSERT INTO tweet (text, links, datetime) VALUES (%s, %s, %s)", (row["TWEET: Text"], row["TWEET: Links"], row["TWEET: Date"],))

# Populating into UserTwitter table
# for index, row in user_table.iterrows():
#     # print(row)
#     # print('\n')
#     cursor.execute("INSERT INTO usertwitter (description, username, followercount, created) VALUES (%s, %s, %s, %s)", (row["USER: Description"], row["USER: Username"], row["USER: Follower Count"], row["USER: Created"]))

# Populating into tweetMetrics table
# for index, row in metrics_table.iterrows():
#     print(index)
#     cursor.execute("INSERT INTO tweetmetrics (replycount, retweetcount, favoritecount, tweetid) VALUES (%s, %s, %s, %s)", (int(row["METRICS: Reply Count"]), int(row["METRICS: Retweet Count"]), int(row["METRICS: Like Count"]), (index+1)))

# Populating into hashtags table
# for index, row in hashtag_table.iterrows():
#     for hashtag in ast.literal_eval(row["HASHTAGS: tags"]):
#         print(hashtag)
#         cursor.execute("INSERT INTO hashtag (tweetid, text) VALUES (%s, %s)", ((index+1), hashtag))

# Populating into links table
# for index, row in links_table.iterrows():
#     for link in row:
#         TextLinks = link.strip('][').split("), ")
#         for s in TextLinks:
#             w = list(filter(lambda k: '=' not in k, s.split("\'")))
#             print(w)
#             if len(w) == 1:
#                     cursor.execute("INSERT INTO links (tweetid, url) VALUES (%s, %s)", ((index+1), w[0]))
#             else:
#                     cursor.execute("INSERT INTO links (tweetid, text, url) VALUES (%s, %s, %s)", ((index+1), w[0], w[1]))

# Populating into tweets table
# for index, row in df.iterrows():
#     cursor.execute("SELECT userid FROM usertwitter WHERE username = %s", (row["USER: Username"],))
#     userid = cursor.fetchall()[0][0]
#     cursor.execute("INSERT INTO tweets (tweetid, userid) VALUES (%s, %s)", (index+1, userid))

#Applies any transactions made to the actual database
connection.commit()

#Important to close the connection after using the database
connection.close()

