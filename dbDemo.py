from dbSetup import connection, cursor
import pandas

data = pandas.read_csv('tweets.csv')
df = pandas.DataFrame(data)

#Split the csv file into each table 
tweets_table = df.filter(like='TWEET:')
user_table = df.filter(like='USER:').drop_duplicates()
metrics_table = df.filter(like='METRICS:')
hashtag_table = df.filter(like='HASHTAG')
location_table = df.filter(like='LOCATION:')


# for value in user_table['USER: Username'].to_list():
# 	# print(str(value))
# 	cursor.execute("INSERT INTO demo (username) VALUES (%s)", (value,))
# cursor.execute("select * from demo;")
# print(cursor.fetchall())

#Populating into Tweet table
# for index, row in tweets_table.iterrows():
#     print(row)
#     print('\n')
#     cursor.execute("INSERT INTO tweet (text, links, datetime) VALUES (%s, %s, %s)", (row["TWEET: Text"], row["TWEET: Links"], row["TWEET: Date"],))

# #Populating into UserTwitter table
# for index, row in user_table.iterrows():
#     # print(row)
#     # print('\n')
#     cursor.execute("INSERT INTO usertwitter (description, username, followercount, created) VALUES (%s, %s, %s, %s)", (row["USER: Description"], row["USER: Username"], row["USER: Follower Count"], row["USER: Created"]))

# #Populating into UserTwitter table
# for index, row in user_table.iterrows():
#     cursor.execute("INSERT INTO usertwitter (description, username, followercount, created) VALUES (%s, %s, %s, %s)", (row["USER: Description"], row["USER: Username"], row["USER: Follower Count"], row["USER: Created"]))

#Populating into tweetMetrics table
for index, row in metrics_table.iterrows():
    print(index)
    cursor.execute("INSERT INTO tweetmetrics (replycount, retweetcount, favoritecount, tweetid) VALUES (%s, %s, %s, %s)", (row["METRICS: Reply Count"], row["METRICS: Retweet Count"], row["METRICS: Like Count"], int(index)))

#Applies any transactions made to the actual database
connection.commit()

#Important to close the connection after using the database
connection.close()


# Creation of tables
# cursor.execute("CREATE TABLE Location(locationID VARCHAR, city VARCHAR, placeType VARCHAR, completeLocation VARCHAR, country VARCHAR, countryCode VARCHAR);")
# cursor.execute("CREATE TABLE UserTwitter(userID INT, description TEXT, username VARCHAR, followerCount INT, created VARCHAR);")
# cursor.execute("CREATE TABLE Tweet(tweetID INT, text TEXT, language VARCHAR, dateTime VARCHAR);")
# cursor.execute("CREATE TABLE TweetMetric(tweetID INT, tweetMetricID INT, replyCount INT, retweetCount INT, favoriteCount INT);")
# cursor.execute("CREATE TABLE Hashtag(tweetID INT, hashtagID INT, text TEXT);")

# Creation of relationships
# cursor.execute("CREATE TABLE tweets(userID INT, tweetID INT);")
# cursor.execute("CREATE TABLE lives(userID INT, locationID INT);")
# cursor.execute("CREATE TABLE locatedFrom(locationID INT, tweetID INT);")
# cursor.execute("CREATE TABLE has(tweetMetricID INT, tweetID INT);")
# cursor.execute("CREATE TABLE contains(hashtagID INT, tweetID INT);")

# Defining primary key
# cursor.execute("ALTER TABLE Location ADD PRIMARY KEY(locationID);")
# cursor.execute("ALTER TABLE UserTwitter ADD PRIMARY KEY(userID);")
# cursor.execute("ALTER TABLE Tweet ADD PRIMARY KEY(tweetID);")
# cursor.execute("ALTER TABLE TweetMetric ADD PRIMARY KEY(tweetID, tweetMetricID);")
# cursor.execute("ALTER TABLE Hashtag ADD PRIMARY KEY(tweetID, hashtagID);")
# cursor.execute("ALTER TABLE tweets ADD PRIMARY KEY(userID INT, tweetID INT);")
# cursor.execute("ALTER TABLE lives ADD PRIMARY KEY(userID INT, locationID INT);")
# cursor.execute("ALTER TABLE locatedFrom ADD PRIMARY KEY(locationID INT, tweetID INT);")
# cursor.execute("ALTER TABLE has ADD PRIMARY KEY(tweetMetricID INT, tweetID INT);")
# cursor.execute("ALTER TABLE contains ADD PRIMARY KEY(hashtagID INT, tweetID INT);")

# Defining foreign key
# cursor.execute("ALTER TABLE Hashtag ADD FOREIGN KEY (tweetID) REFERENCES Tweet (tweetID);")
# cursor.execute("ALTER TABLE TweetMetrics ADD FOREIGN KEY (tweetID) REFERENCES Tweet (tweetID);")

# Test demo
# cursor.execute("INSERT INTO demo (id) VALUES (3);")

# cursor.execute("select * from demo;")

# print(cursor.fetchall())

# alter table tweet
#    alter tweetid add generated always as identity;
