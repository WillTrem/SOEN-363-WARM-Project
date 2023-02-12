from dbSetup import connection, cursor
import pandas

data = pandas.read_csv(r'tweets.csv')
df = pandas.DataFrame(data)

print(df)

user_userName = pandas.DataFrame(data, columns=['USER: Username'])
user_description = pandas.DataFrame(data, columns=['USER: Description'])
user_created = pandas.DataFrame(data, columns=['USER: Created'])
user_followerCount = pandas.DataFrame(data, columns=['USER: Follower Count'])
user_verified = pandas.DataFrame(data, columns=['USER: USER: Verified'])



# print(user_userName)
# bitQuery = "INSERT INTO demo (username) VALUES (%s)"
# values = ("hellllllo")
# bitQuery = "INSERT INTO demo (username) VALUES ({s});".format(user_userName)
# values = (user_userName)
# user_userName = "hellllllo"
# cursor.executemany(bitQuery, user_userName)
# cursor.executemany(f"INSERT INTO demo (username) VALUES {user_userName};")
# user_userName = "username"
# cursor.execute("INSERT INTO demo (username) VALUES (%s)" % user_userName)
# cursor.execute("INSERT INTO demo (id) VALUES (3);")

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

#Applies any transactions made to the actual database
connection.commit()

#Important to close the connection after using the database
connection.close()
