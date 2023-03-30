from mongodbSetup import db
from dbSetup import connection, cursor


#Inserting into Tweet table
# cursor.execute('SELECT * FROM tweet;')
# tweetSQL = cursor.fetchall()
# tweetList = []
# tweetMongo = db["tweet"]

# for tweet in tweetSQL:
#     id, text, datetime = tweet
#     tweetList.append({
#         "_id": id,
# 		"text": text,
# 		"datetime": datetime
# 	})

# tweetMongo.insert_many(tweetList)

# #Inserting into Tweets table
# cursor.execute('SELECT tweetId, userId FROM tweets;')
# tweetsSQL = cursor.fetchall()
# tweetsList = []
# tweetsMongo = db["tweets"]

# for tweets in tweetsSQL:
#     tweetId, userId = tweets
#     tweetsList.append({
#         "tweetId": tweetId,
# 		"userId": userId,
# 	})

# tweetsMongo.insert_many(tweetsList)

#Inserting into userTwitter table
# cursor.execute('SELECT * FROM userTwitter;')
# userTwitterSQL = cursor.fetchall()
# userTwitterList = []
# userTwitterMongo = db["userTwitter"]

# for userTwitter in userTwitterSQL:
#     userId, description, username, followercount, created = userTwitter
#     userTwitterList.append({
#         "userId": userId,
# 		"description": description,
# 		"username": username,
# 		"followercount": followercount,
# 		"created": created
# 	})

# userTwitterMongo.insert_many(userTwitterList)


#Inserting into tweetmetrics table
# cursor.execute('SELECT * FROM tweetmetrics;')
# tweetmetricsSQL = cursor.fetchall()
# tweetmetricsList = []
# tweetmetricsMongo = db["tweetmetrics"]

# for tweetmetrics in tweetmetricsSQL:
#     replycount, retweetcount, favoritecount, tweetid = tweetmetrics
#     tweetmetricsList.append({
#         "replycount": replycount,
#         "retweetcount": retweetcount,
#         "favoritecount": favoritecount,
#         "tweetid": tweetid
# 	})

# tweetmetricsMongo.insert_many(tweetmetricsList)

# # #Inserting into hashtag table
# cursor.execute('SELECT * FROM hashtag;')
# hashtagSQL = cursor.fetchall()
# hashtagList = []
# hashtagMongo = db["hashtag"]

# for hashtag in hashtagSQL:
#     tweetid, text, hashtagid = hashtag
#     hashtagList.append({
#         "tweetid": tweetid,
#         "text": text,
#         "hashtagid": hashtagid
# 	})

# hashtagMongo.insert_many(hashtagList)


# #Inserting into links table
# cursor.execute('SELECT * FROM links;')
# linksSQL = cursor.fetchall()
# linksList = []
# linksMongo = db["links"]

# for links in linksSQL:
#     linkid, tweetid, text, url = links
#     linksList.append({
#         "linkid": link
#         "tweetid": tweetid,
#         "text": text,
#         "url": url
# 	})

# linksMongo.insert_many(linksList)

# #Inserting into instagramaccount table
# cursor.execute('SELECT * FROM instagramaccount;')
# instagramaccountSQL = cursor.fetchall()
# instagramaccountList = []
# instagramaccountMongo = db["instagramaccount"]

# for instagramaccount in instagramaccountSQL:
#     instagramuserid, username, bio, numberofposts,followercount, followingcount = instagramaccount
#     instagramaccountList.append({
#         "instagramuserid": instagramuserid,
#         "username": username,
#         "bio": bio,
#         "numberofposts":numberofposts,
#         "followercount":followercount,
#         "followingcount": followingcount
# 	})

# instagramaccountMongo.insert_many(instagramaccountList)


#Inserting into hasinstagramaccount table
cursor.execute('SELECT * FROM hasinstagramaccount;')
hasinstagramaccountSQL = cursor.fetchall()
hasinstagramaccountList = []
hasinstagramaccountMongo = db["hasinstagramaccount"]

for hasinstagramaccount in hasinstagramaccountSQL:
    userid, instagramuserid = hasinstagramaccount
    hasinstagramaccountList.append({
        "userid": userid,
        "instagramuserid": instagramuserid,
	})

hasinstagramaccountMongo.insert_many(hasinstagramaccountList)
connection.close()
