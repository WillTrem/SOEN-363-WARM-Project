// Lists Instagram usernames and the hashtags used in their tweets from Twitter

use('project-phase-3-db');

db.instagramaccount.aggregate([
    {
       $lookup:
          {
            from: "userTwitter",
            localField: "username",
            foreignField: "username",
            as: "twitteraccount"
          }
    },
    {
        $unwind: "$twitteraccount"
     },
     {
        $lookup:
           {
             from: "tweets",
             localField: "twitteraccount.userId",
             foreignField: "userId",
             as: "tweets"
           }
     },
     {
        $unwind: "$tweets"
     },  
     {
        $lookup:
           {
             from: "hashtag",
             localField: "tweets.tweetId",
             foreignField: "tweetid",
             as: "hashtags"
           }
     },
     {
        $unwind: "$hashtags"
     },
     {
        $group:
           {
             _id: { "username": "$username", "hashtag": "$hashtags.text" },
             count: { $sum: 1 }
           }
     },
     {
        $project:
           {
             _id: 0,
             username: "$_id.username",
             hashtag: "$_id.hashtag",
             hashtag_count: "$count"
           }
     },
     {
        $sort:
           {
             hashtag_count: -1
           }
     }  
 ]).toArray();
 