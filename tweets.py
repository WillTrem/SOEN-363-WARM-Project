import snscrape.modules.twitter as sntwitter
import pandas as pd

# this query searches for english tweets using the words insta or instagram between Oct and Dec 2022
query = '(insta OR instagram) lang:en until:2022-12-31 since:2022-10-01'
tweets = []

# how many tweets to generate
limit = 2000

# for each tweet found using the query, add it to the list of tweets, with specific data in else statement
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        # appends tweets to the list of tweets with the desired information
        tweets.append([tweet.date, tweet.user.username, tweet.user.verified, tweet.user.rawDescription, tweet.user.created, tweet.user.followersCount, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.user.location, tweet.hashtags, tweet.links, tweet.rawContent])

# create data frame to hold the tweet data in a table
df = pd.DataFrame(tweets, columns=['TWEET: Date', 'USER: Username', 'USER: Verified', 'USER: Description', 'USER: Created', 'USER: Follower Count', 'METRICS: Reply Count', 'METRICS: Retweet Count', 'METRICS: Like Count', 'LOCATION: Location', 'HASHTAGS: tags', 'TWEET: Links', 'TWEET: Text'])

# sends the data frame to a csv file
df.to_csv('tweets.csv')
