from dbSetup import connection, cursor
import pandas as pd
import instaloader


#Obtaining the data already fetched from the csv file
instagramUsersDf = pd.read_csv('instagramUsers.csv')
savedInstagramProfileIds = instagramUsersDf["TwitterUserId"].values
print(savedInstagramProfileIds)
lastProfileIdSaved = savedInstagramProfileIds[len(savedInstagramProfileIds)-1]

print(lastProfileIdSaved)

#Obtaining the list of twitter usernames from the database
cursor.execute('SELECT userId, username FROM usertwitter ORDER BY userId;')
userDf = pd.DataFrame(cursor.fetchall(), columns=['UserId', 'Username'])

#print(userDf)

#Have to run 'import_firefox_session.py' first (while being logged in instagram on firefox)
scraper = instaloader.Instaloader(max_connection_attempts=1)
scraper.load_session_from_file("<ADD YOUR INSTAGRAM USERNAME HERE>") #<- then put your instagram username here

for row in userDf.itertuples(): 
    twitterUserId = row[1]
    twitterUserName = row[2]
    if twitterUserId <= lastProfileIdSaved:
        print(f"Information of {twitterUserName} has already been processed.")
    else:
        try:
            profile = instaloader.Profile.from_username(scraper.context, twitterUserName)
            print(f"Profile found for {twitterUserName}! Writing its information to the csv file.")
            
            profileInfo = {
                "TwitterUserId": [twitterUserId],
                "Username": [profile.username],
                "InstagramUserId": [profile.userid],
                "NumberofPosts": [profile.mediacount],
                "FollowersCount": [profile.followers],
                "FollowingCount": [profile.followees],
                "Bio": [profile.biography],
                "ExternalURL": [profile.external_url],
            }
            
            profileDf = pd.DataFrame(profileInfo)
            profileDf.to_csv('instagramUsers.csv', mode='a', index=False, header=False)
            
        except instaloader.exceptions.ProfileNotExistsException:
            print(f'User {twitterUserName} not found on Instagram.')