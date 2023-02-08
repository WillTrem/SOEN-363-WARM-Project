from dbSetup import connection, cursor

# Creation of tables
# cursor.execute("CREATE TABLE Location(locationID VARCHAR, city VARCHAR, placeType VARCHAR, completeLocation VARCHAR, country VARCHAR, countryCode VARCHAR);")
# cursor.execute("CREATE TABLE UserTwitter(userID INT, description TEXT, username VARCHAR, followerCount INT, created VARCHAR);")
# cursor.execute("CREATE TABLE Tweet(tweetID INT, text TEXT, language VARCHAR, dateTime VARCHAR);")
# cursor.execute("CREATE TABLE Platform(platformID INT, platformName VARCHAR);")
# cursor.execute("CREATE TABLE TweetMetrics(tweetID INT, tweetMetricID INT, replyCount INT, retweetCount INT, favoriteCount INT);")
# cursor.execute("CREATE TABLE Hashtag(tweetID INT, hashtagID INT, text TEXT);")

# Creation of relationships
# cursor.execute("CREATE TABLE uses(userID INT, platformID INT);")
# cursor.execute("CREATE TABLE lives(userID INT, locationID INT);")
# cursor.execute("CREATE TABLE locatedFrom(locationID INT, tweetID INT);")
# cursor.execute("CREATE TABLE has(tweetMetricID INT, tweetID INT);")
# cursor.execute("CREATE TABLE contains(hashtagID INT, tweetID INT);")

# Defining primary key
# cursor.execute("ALTER TABLE Location ADD PRIMARY KEY(locationID);")
# cursor.execute("ALTER TABLE UserTwitter ADD PRIMARY KEY(userID);")
# cursor.execute("ALTER TABLE Tweet ADD PRIMARY KEY(tweetID);")
# cursor.execute("ALTER TABLE Platform ADD PRIMARY KEY(platformID);")
# cursor.execute("ALTER TABLE TweetMetrics ADD PRIMARY KEY(tweetID, tweetMetricID);")
# cursor.execute("ALTER TABLE Hashtag ADD PRIMARY KEY(tweetID, hashtagID);")

# Defining foreign key
# cursor.execute("ALTER TABLE Hashtag ADD FOREIGN KEY (tweetID) REFERENCES Tweet (tweetID);")
# cursor.execute("ALTER TABLE TweetMetrics ADD FOREIGN KEY (tweetID) REFERENCES Tweet (tweetID);")

# Test demo
# cursor.execute("INSERT INTO demo (id) VALUES (3);")

# cursor.execute("select * from demo;")

# print(cursor.fetchall())

#Applies any transactions made to the actual database
connection.commit()

#Important to close the connection after using the database
connection.close()
