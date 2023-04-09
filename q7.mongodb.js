// Find all tweets that contain a specific URL.

use("project-phase-3-db");

db.links.aggregate([
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
            text: "https://www.instagram.com/kinlwu/",
        },
    },
    {
        $project:
           {
             _id: 0,
             tweetid: "$tweetid",
             text: "$text",
             url: "$count"
           }
     }
]).toArray();