// Lists all tweets that were posted after a given date (2021-01-01) and retweeted more than 100 times

use("project-phase-3-db");

db.tweetmetrics.aggregate([
    {
        $lookup: 
        {
            from: "tweet",
            localField: "tweetid",
            foreignField: "_id",
            as: "tweet",
        },
    },
    {
        $match: 
        {
            retweetcount: { $gt: 100 },
            "tweet.datetime": { $gt: "2021-01-01" },
        },
    },
    {
        $project:
           {
             _id: 0,
             tweetid: "$tweetid",
             tweet: "$tweet.text",
             tweet_Date: "$tweet.datetime",
             retweetcount: "$retweetcount"
           }
     }
]).toArray();